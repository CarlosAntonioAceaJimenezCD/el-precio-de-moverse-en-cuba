#!/usr/bin/env python3
"""Scrapea el catalogo completo de cada concesionario online y guarda una BD SQLite por tienda.

Salida: Data/catalogos_concesionarios/<tienda>.sqlite
Cada fila = una pagina de ficha/catalogo con todos los campos detectables en raw_json y el HTML crudo.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import time
import unicodedata
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote

from bs4 import BeautifulSoup
from curl_cffi import requests as creq

BASE = Path(__file__).resolve().parents[1]
PROJECT = BASE.parent
OUT = PROJECT / "Data" / "catalogos_concesionarios"

SHOPS: dict[str, dict] = {
    "bdc_one": {
        "name": "BDC One",
        "seeds": ["https://bdcone.online/autos/"],
        "max_pages": 70,
        "allow": ("bdcone.online",),
    },
    "dongfeng_cuba": {
        "name": "Dongfeng Cuba",
        "seeds": ["https://www.dongfengcuba.com/catalogo/"],
        "max_pages": 45,
        "allow": ("dongfengcuba.com",),
    },
    "mcv_commercial": {
        "name": "MCV Commercial",
        "seeds": ["https://www.mcvcommercial.com/brands", "https://www.mcvcommercial.com/"],
        "max_pages": 45,
        "allow": ("mcvcommercial.com",),
    },
    "finauto": {
        "name": "Finauto International",
        "seeds": ["https://finautointernational.com/catalogo", "https://finautointernational.com/"],
        "max_pages": 45,
        "allow": ("finautointernational.com",),
    },
    "changan": {
        "name": "Changan Automotive",
        "seeds": ["https://changanautomotive.com/"],
        "max_pages": 30,
        "allow": ("changanautomotive.com",),
    },
    "chinautos_cuba": {
        "name": "Chinautos Cuba (LXWY)",
        "seeds": ["https://chinautoscuba.com/autos/", "https://chinautoscuba.com/byd/", "https://chinautoscuba.com/changan/"],
        "max_pages": 70,
        "allow": ("chinautoscuba.com",),
    },
    "envision_autos": {
        "name": "Envision Autos Cuba",
        "seeds": ["https://envisionsol.com/"],
        "max_pages": 10,
        "allow": ("envisionsol.com",),
    },
    "atr_export": {
        "name": "ATR Export",
        "seeds": [
            "https://www.atrexport.com/portfolio/",
            "https://www.atrexport.com/carros-electricos-en-cuba/",
            "https://www.atrexport.com/importar-carros-gasolina-cuba/",
            "https://www.atrexport.com/importar-vehiculos-comerciales-a-cuba/",
            "https://www.atrexport.com/carros-en-plaza/",
        ],
        "max_pages": 60,
        "allow": ("atrexport.com",),
    },
    "connectingcuba": {
        "name": "ConnectingCuba",
        "seeds": ["https://www.connectingcuba.com/"],
        "max_pages": 35,
        "allow": ("connectingcuba.com",),
    },
    "subasta_cubana": {
        "name": "La Subasta Cubana",
        "seeds": [
            "https://lasubastacubana.com/inventory/vehicle-type-v",
            "https://lasubastacubana.com/inventory/vehicle-type-k",
            "https://lasubastacubana.com/inventory?order[default]=asc",
        ],
        "max_pages": 60,
        "allow": ("lasubastacubana.com",),
    },
    "agn_motors": {
        "name": "AGN Motors Cuba",
        "seeds": ["https://www.agnmotors.com/cuba/available-cars.htm"],
        "max_pages": 60,
        "allow": ("agnmotors.com",),
    },
}

KEYWORDS = re.compile(
    r"auto|carro|coche|veh[ií]cul|moto|modelo|producto|ficha|inventario|usado|seminuevo|"
    r"ocasi[oó]n|camioneta|marca|sedan|suv|hatchback|pickup|electric|hibrid",
    re.I,
)
FIELDS = [
    "marca", "modelo", "version", "anio", "anho", "year", "precio", "moneda", "km",
    "kilometraje", "combustible", "transmision", "traccion", "motor", "potencia",
    "cilindrada", "color", "puertas", "asientos", "carroceria", "garantia", "ubicacion",
    "estado", "condicion", "matricula", "chasis", "vin", "consumo", "etiqueta", "categoria",
]
PATTERNS = {
    "marca": r"(?:marca|make|brand)\s*[:\-]?\s*([A-Za-zÁÉÍÓÚñü0-9 ]{2,40})",
    "modelo": r"(?:modelo|model)\s*[:\-]?\s*([A-Za-zÁÉÍÓÚñü0-9 \-]{2,50})",
    "version": r"(?:versi[oó]n|version|trim)\s*[:\-]?\s*([A-Za-zÁÉÍÓÚñü0-9 \-]{2,50})",
    "anio": r"(?:a[oó]?o|year|model year)\s*[:\-]?\s*(19\d{2}|20\d{2})",
    "precio": r"(?:precio|price|valor|coste|cost|desde|from)\s*[:\-]?\s*([€$USD..]?\s?[\d.,]{3,12})",
    "km": r"(?:km|kil[oó]metros|mileage|millage)\s*[:\-]?\s*([\d.,]{3,10})",
    "combustible": r"(?:combustible|fuel|energ[ií]a)\s*[:\-]?\s*([A-Za-zÁÉÍÓÚñü ]{3,30})",
    "transmision": r"(?:transmisi[oó]n|transmission|gear)\s*[:\-]?\s*([A-Za-zÁÉÍÓÚñü ]{3,25})",
    "traccion": r"(?:tracci[oó]n|drive)\s*[:\-]?\s*([A-Za-zÁÉÍÓÚñü 4x4]{2,25})",
    "motor": r"(?:motor|engine)\s*[:\-]?\s*([A-Za-zÁÉÍÓÚñü0-9 .]{2,40})",
    "potencia": r"(?:potencia|power|cv|hp)\s*[:\-]?\s*([\d.,]{2,6}\s?(?:cv|hp|kw)?)",
    "cilindrada": r"(?:cilindrada|displacement|cc)\s*[:\-]?\s*([\d.,]{3,6})",
    "color": r"(?:color|colour)\s*[:\-]?\s*([A-Za-zÁÉÍÓÚñü ]{3,25})",
    "puertas": r"(?:puertas|doors)\s*[:\-]?\s*(\d{1,2})",
    "asientos": r"(?:asientos|seats|plazas)\s*[:\-]?\s*(\d{1,2})",
    "carroceria": r"(?:carrocer[ií]a|body|tipo)\s*[:\-]?\s*([A-Za-zÁÉÍÓÚñü ]{3,30})",
    "garantia": r"(?:garant[ií]a|warranty)\s*[:\-]?\s*([A-Za-zÁÉÍÓÚñü0-9 ,.]{3,40})",
    "ubicacion": r"(?:ubicaci[oó]n|location|ciudad|provincia)\s*[:\-]?\s*([A-Za-zÁÉÍÓÚñü ]{3,35})",
    "estado": r"(?:estado|condition)\s*[:\-]?\s*([A-Za-zÁÉÍÓÚñü ]{3,25})",
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def init_db(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    cols = ", ".join(f"{f} TEXT" for f in FIELDS)
    conn.execute(
        f"""CREATE TABLE IF NOT EXISTS vehiculos (
            url TEXT PRIMARY KEY,
            shop TEXT,
            shop_name TEXT,
            title TEXT,
            meta_description TEXT,
            og_image TEXT,
            headings TEXT,
            text TEXT,
            {cols},
            tables_json TEXT,
            jsonld_json TEXT,
            microdata_json TEXT,
            images_json TEXT,
            links_json TEXT,
            prices_json TEXT,
            emails_json TEXT,
            phones_json TEXT,
            raw_json TEXT,
            raw_html TEXT,
            status INTEGER,
            final_url TEXT,
            scraped_at TEXT
        )"""
    )
    conn.execute("CREATE INDEX IF NOT EXISTS idx_vehiculos_shop ON vehiculos(shop)")
    conn.commit()
    return conn


def fetch(url: str, render: bool = False) -> tuple[str, int, str]:
    r = None
    for imp in ("chrome", "safari"):
        try:
            r = creq.get(
                url, impersonate=imp, timeout=45, allow_redirects=True,
                headers={"Accept-Language": "es-ES,es;q=0.9,en;q=0.8"},
            )
            if r.status_code == 200:
                break
        except Exception:
            r = None
    html = r.text if r is not None else ""
    status = r.status_code if r is not None else 0
    final = str(r.url) if r is not None else url
    soup = BeautifulSoup(html or "", "lxml")
    visible = soup.get_text(" ", strip=True)
    if render or len(visible) < 1200 or len(soup.find_all("a")) < 5:
        try:
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                b = p.chromium.launch(
                    headless=True,
                    executable_path="/usr/bin/chromium",
                    args=["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"],
                )
                ctx = b.new_context(locale="es-ES", viewport={"width": 1440, "height": 900})
                pg = ctx.new_page()
                pg.goto(url, wait_until="domcontentloaded", timeout=60000)
                pg.wait_for_timeout(3500)
                html = pg.content()
                final = pg.url
                b.close()
        except Exception:
            pass
    return html or "", status, final


def extract(html: str, url: str) -> dict:
    soup = BeautifulSoup(html or "", "lxml")
    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    meta = {}
    for m in soup.find_all("meta"):
        k = m.get("property") or m.get("name")
        if k and m.get("content"):
            meta[k] = m["content"]
    jsonld = []
    for sc in soup.find_all("script", type="application/ld+json"):
        try:
            jsonld.append(json.loads(sc.string or sc.get_text() or "{}"))
        except Exception:
            pass
    micro = []
    for el in soup.select("[itemscope]"):
        d = {}
        for child in el.select("[itemprop]"):
            d[child.get("itemprop")] = child.get("content") or child.get_text(" ", strip=True)[:200]
        if d:
            micro.append(d)
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()
    text = " ".join(soup.get_text(" ", strip=True).split())
    nt = norm(text)
    tables = []
    for t in soup.find_all("table"):
        rows = []
        for tr in t.find_all("tr"):
            cells = [c.get_text(" ", strip=True) for c in tr.find_all(["th", "td"])]
            if cells:
                rows.append(cells)
        if rows:
            tables.append(rows)
    images = []
    for im in soup.find_all("img"):
        src = im.get("data-src") or im.get("data-lazy-src") or im.get("src")
        if src:
            images.append(urljoin(url, src))
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith(("#", "javascript:", "mailto:", "tel:")):
            continue
        links.append({"text": a.get_text(" ", strip=True)[:120], "url": urljoin(url, href)})
    prices = re.findall(r"(?:US\$|USD|\$|€)\s?[\d.,]{3,12}|[\d.,]{3,12}\s?(?:USD|EUR|CUP|MLC)", text)
    emails = list(set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text)))
    phones = list(set(re.findall(r"\+?\d[\d\s\-()]{7,18}\d", text)))

    fields: dict[str, str] = {}
    for key, pat in PATTERNS.items():
        m = re.search(pat, nt, re.I)
        if m:
            fields[key] = m.group(1).strip()[:200]
    # Campos desde JSON-LD (Product/Vehicle/Offer)
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                kk = norm(str(k))
                if kk in FIELDS and isinstance(v, (str, int, float)) and kk not in fields:
                    fields[kk] = str(v)[:200]
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    for blob in jsonld:
        walk(blob)

    raw = {
        "title": title,
        "meta": meta,
        "jsonld": jsonld,
        "microdata": micro,
        "tables": tables,
        "images": images,
        "links": links,
        "prices": prices,
        "emails": emails,
        "phones": phones,
        "fields": fields,
        "text": text,
    }
    headings = [h.get_text(" ", strip=True) for h in soup.find_all(["h1", "h2", "h3"])]
    return {
        "title": title,
        "meta_description": meta.get("og:description") or meta.get("description", ""),
        "og_image": meta.get("og:image", ""),
        "headings": json.dumps(headings, ensure_ascii=False),
        "text": text[:20000],
        "tables_json": json.dumps(tables, ensure_ascii=False),
        "jsonld_json": json.dumps(jsonld, ensure_ascii=False),
        "microdata_json": json.dumps(micro, ensure_ascii=False),
        "images_json": json.dumps(images, ensure_ascii=False),
        "links_json": json.dumps(links, ensure_ascii=False),
        "prices_json": json.dumps(prices, ensure_ascii=False),
        "emails_json": json.dumps(emails, ensure_ascii=False),
        "phones_json": json.dumps(phones, ensure_ascii=False),
        "raw_json": json.dumps(raw, ensure_ascii=False),
        "raw_html": html,
        "fields": fields,
        "links": links,
        "prices": prices,
    }


def save(conn: sqlite3.Connection, shop: dict, url: str, data: dict, status: int, final: str) -> bool:
    vals = [data["fields"].get(f, "") for f in FIELDS]
    cols = ", ".join(FIELDS)
    marks = ", ".join("?" for _ in FIELDS)
    sql = f"""INSERT OR REPLACE INTO vehiculos
        (url, shop, shop_name, title, meta_description, og_image, headings, text,
         {cols}, tables_json, jsonld_json, microdata_json, images_json, links_json,
         prices_json, emails_json, phones_json, raw_json, raw_html, status, final_url, scraped_at)
        VALUES ({", ".join(["?"] * (10 + len(FIELDS) + 11))})"""
    params = [
        url, shop["key"], shop["name"], data["title"], data["meta_description"],
        data["og_image"], data["headings"], data["text"], *vals,
        data["tables_json"], data["jsonld_json"], data["microdata_json"],
        data["images_json"], data["links_json"], data["prices_json"],
        data["emails_json"], data["phones_json"], data["raw_json"], data["raw_html"],
        status, final, now(),
    ]
    try:
        conn.execute(sql, params)
        conn.commit()
        return True
    except Exception as e:
        print(f"  ERROR BD {url}: {e}", flush=True)
        return False


def crawl_shop(shop: dict, delay: float) -> None:
    key = shop["key"]
    db = OUT / f"{key}.sqlite"
    conn = init_db(db)
    q = deque(shop["seeds"])
    seen: set[str] = set()
    pages = 0
    while q and pages < shop["max_pages"]:
        url = q.popleft().split("#")[0]
        if url in seen:
            continue
        seen.add(url)
        host = urlparse(url).netloc.lower().replace("www.", "")
        if not any(a.replace("www.", "") in host for a in shop["allow"]):
            continue
        html, status, final = fetch(url)
        if not html:
            continue
        data = extract(html, final or url)
        saved = save(conn, shop, url, data, status, final)
        pages += 1
        if saved:
            print(f"[{key}] {pages:03d}/{shop['max_pages']} {data['title'][:65]} | precios={len(data['prices'])} img={len(json.loads(data['images_json']))}", flush=True)
        for l in data["links"]:
            u = l["url"].split("#")[0]
            h = urlparse(u).netloc.lower().replace("www.", "")
            if u in seen or not any(a.replace("www.", "") in h for a in shop["allow"]):
                continue
            if KEYWORDS.search(l["text"] + " " + unquote(u)):
                q.append(u)
        time.sleep(delay)
    n = conn.execute("SELECT COUNT(*) FROM vehiculos").fetchone()[0]
    print(f"[{key}] LISTO: {n} filas en {db}", flush=True)
    conn.close()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--shops", nargs="*", help="claves de tiendas a scrapear (por defecto todas)")
    ap.add_argument("--delay", type=float, default=0.8)
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    for key, shop in SHOPS.items():
        if a.shops and key not in a.shops:
            continue
        s = dict(shop)
        s["key"] = key
        try:
            crawl_shop(s, a.delay)
        except Exception as e:
            print(f"[{key}] ERROR GENERAL: {e}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

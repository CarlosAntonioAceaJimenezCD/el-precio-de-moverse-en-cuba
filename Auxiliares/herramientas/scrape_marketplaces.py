#!/usr/bin/env python3
"""Scrapea anuncios de los marketplaces con seccion automotriz.

Guarda una SQLite por marketplace en Data/catalogos_concesionarios/marketplaces/
con tablas: anuncios, comentarios, vendedores.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import unicodedata
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote

from bs4 import BeautifulSoup
from curl_cffi import requests as creq

BASE = Path(__file__).resolve().parents[1]
OUT = BASE.parent / "Data" / "catalogos_concesionarios" / "marketplaces"

SITES = {
    "autocubana": {
        "name": "Autocubana",
        "seeds": ["https://www.autocubana.com/es/vehicle_listings?car_type=carros"],
        "page_template": "https://www.autocubana.com/es/vehicle_listings?car_type=carros&page={page}",
        "pages": 40,
        "pattern": r"/vehicle_listings/anuncio-",
        "allow": ("autocubana.com",),
        "max": 667,
    },
    "itencel": {
        "name": "iTENCEL",
        "seeds": ["https://itencel.com/anuncio-categoria/vehiculos/carros/"],
        "page_template": "https://itencel.com/anuncio-categoria/vehiculos/carros/page/{page}/",
        "pages": 40,
        "pattern": r"/anuncio/",
        "allow": ("itencel.com",),
        "max": 951,
    },
    "ventacuba": {
        "name": "VentaCuba",
        "seeds": [
            "http://www.ventacuba.com/vehiculos/carros-y-camionetas",
            "http://www.ventacuba.com/search/category,carros-y-camionetas/sOrder,i_price/iOrderType,asc",
            "http://www.ventacuba.com/search/category,carros-y-camionetas/sOrder,i_price/iOrderType,desc",
        ],
        "page_template": "http://www.ventacuba.com/search/category,carros-y-camionetas/sOrder,i_price/iOrderType,asc/page,{page}",
        "pages": 40,
        "pattern": r"_i\d+",
        "allow": ("ventacuba.com",),
        "max": 801,
    },
    "timbirichi": {
        "name": "Timbirichi",
        "seeds": ["https://www.timbirichi.com/vehiculos-y-piezas/carros"],
        "page_template": "https://www.timbirichi.com/vehiculos-y-piezas/carros?page={page}",
        "pages": 40,
        "pattern": r"/vehiculos-y-piezas/carros/.+",
        "allow": ("timbirichi.com",),
        "max": 281,
    },
    "cogetucarro": {
        "name": "Cogetucarro",
        "seeds": ["https://cogetucarro.com/view.php?id=7859"],
        "sitemap": "https://cogetucarro.com/sitemap.xml",
        "sitemap_pattern": r"view\.php\?id=\d+",
        "pattern": r"view\.php\?id=\d+",
        "allow": ("cogetucarro.com",),
        "max": 5008,
    },
    "cubisima": {
        "name": "Cubisima",
        "seeds": ["https://www.cubisima.com/carros"],
        "sitemap": "https://www.cubisima.com/sitemap-carros-1.xml",
        "sitemap_pattern": r"/carros/.+\.htm",
        "pattern": r"/carros/.+\.htm",
        "allow": ("cubisima.com",),
        "max": 155,
    },
    "apululu": {
        "name": "Apululu",
        "seeds": ["https://apululu.es/anuncio-categoria/carros/", "https://apululu.es/anuncio-categoria/autos/"],
        "page_template": "https://apululu.es/anuncio-categoria/carros/page/{page}/",
        "pages": 10,
        "pattern": r"/anuncio/",
        "allow": ("apululu.es",),
        "max": 60,
    },
    "carroscom": {
        "name": "Carros.com Cuba",
        "seeds": ["https://www.carros.com/cars-for-sale/cuba-co47/?lang=es"],
        "page_template": "https://www.carros.com/cars-for-sale/cuba-co47/?lang=es&page={page}",
        "pages": 5,
        "pattern": r"/car/",
        "allow": ("carros.com",),
        "max": 60,
    },
}

SELLER_SELECTORS = [
    ".seller-name", ".lead_user_name", "[class*=seller-name]", "[class*=seller_name]",
    "[class*=vendedor]", "[class*=anunciante]", "[class*=author]", ".user-name",
]
COMMENT_SELECTORS = [
    "[class*=comment]", "[class*=review]", "[class*=opinion]", "[class*=respuesta]",
    ".ad-seller-comment", ".post-comments",
]
PRICE_RE = re.compile(r"(?:US\$|USD|\$|€|CUP|MLC)\s?[\d.,]{2,12}|[\d.,]{3,12}\s?(?:USD|EUR|CUP|MLC)", re.I)
DATE_RE = re.compile(
    r"(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4})|(?:20\d{2}-\d{2}-\d{2})|"
    r"(?:Enero|Febrero|Marzo|Abril|Mayo|Junio|Julio|Agosto|Septiembre|Octubre|Noviembre|Diciembre)\s+\d{1,2}",
    re.I,
)
PHONE_RE = re.compile(r"\+?\d[\d\s\-()]{6,18}\d")


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def init_db(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(path)
    c.row_factory = sqlite3.Row
    c.executescript(
        """
        CREATE TABLE IF NOT EXISTS anuncios (
            url TEXT PRIMARY KEY, site TEXT, site_name TEXT, title TEXT, price TEXT,
            currency TEXT, location TEXT, date TEXT, seller_name TEXT, seller_url TEXT,
            seller_registered TEXT, seller_type TEXT, seller_phone TEXT,
            description TEXT, specs_json TEXT, images_json TEXT, prices_json TEXT,
            comments_count INTEGER, raw_json TEXT, raw_html TEXT, status INTEGER,
            final_url TEXT, scraped_at TEXT
        );
        CREATE TABLE IF NOT EXISTS comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT, author TEXT, date TEXT,
            text TEXT, rating TEXT, raw TEXT
        );
        CREATE TABLE IF NOT EXISTS vendedores (
            name TEXT, url TEXT, site TEXT, phone TEXT, registered TEXT,
            ads_count INTEGER, PRIMARY KEY(name, site)
        );
        CREATE INDEX IF NOT EXISTS idx_comentarios_url ON comentarios(url);
        """
    )
    c.commit()
    return c


def fetch(url, render=False):
    r = None
    for imp in ("chrome", "safari"):
        try:
            r = creq.get(url, impersonate=imp, timeout=45, allow_redirects=True,
                         headers={"Accept-Language": "es-ES,es;q=0.9"}, verify=False)
            if r.status_code == 200:
                break
        except Exception:
            r = None
    html = r.text if r is not None else ""
    status = r.status_code if r is not None else 0
    final = str(r.url) if r is not None else url
    soup = BeautifulSoup(html or "", "lxml")
    visible = soup.get_text(" ", strip=True)
    if render or len(visible) < 900 or len(soup.find_all("a")) < 4:
        try:
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                b = p.chromium.launch(headless=True, executable_path="/usr/bin/chromium",
                                      args=["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"])
                ctx = b.new_context(locale="es-ES", viewport={"width": 1440, "height": 900},
                                    ignore_https_errors=True)
                pg = ctx.new_page()
                pg.goto(url, wait_until="domcontentloaded", timeout=60000)
                pg.wait_for_timeout(3000)
                html = pg.content()
                final = pg.url
                b.close()
        except Exception:
            pass
    return html or "", status, final, BeautifulSoup(html or "", "lxml")


def smart_text(soup, length=30000):
    for t in soup(["script", "style", "noscript", "svg"]):
        t.decompose()
    return " ".join(soup.get_text(" ", strip=True).split())[:length]


def extract_seller(soup, text):
    name, url, registered, phone, stype = "", "", "", "", ""
    for sel in SELLER_SELECTORS:
        for el in soup.select(sel):
            t = " ".join(el.get_text(" ", strip=True).split())
            bad = {"nombre", "email", "mensaje", "usuario", "contraseña", "repetir contraseña", "comentario"}
            if t and len(t) < 120 and not name and norm(t) not in bad:
                name = t
            h = el.get("href") if el.name == "a" else (el.find("a").get("href") if el.find("a") else "")
            if h and not url:
                url = h
            if name and url:
                break
        if name and url:
            break
    ntext = norm(text)
    for pat, key in [
        (r"anuncio publicado por ([A-Za-z0-9 .\-_]{3,50})", "name"),
        (r"vendedor privado", "type"),
        (r"(?:registrad[oa]|miembro desde)\s*(?:on\s*)?(\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4})", "reg"),
        (r"informaci[oó]n de contacto:\s*([A-Za-z0-9 .\-_]{3,40})", "name"),
    ]:
        m = re.search(pat, ntext)
        if m:
            if key == "name" and not name:
                name = m.group(1).strip()
            elif key == "type" and not stype:
                stype = "Vendedor privado"
            elif key == "reg" and not registered:
                registered = m.group(1)
    phones = PHONE_RE.findall(text)
    if phones:
        phone = phones[0]
    if not name and stype:
        name = stype
    return name[:120], url, registered, stype, phone


def extract_comments(soup, text, jsonld):
    out = []
    for sel in COMMENT_SELECTORS:
        for el in soup.select(sel):
            t = " ".join(el.get_text(" ", strip=True).split())
            if 25 < len(t) < 1200 and not re.match(r"^(comentarios?|reviews?|opiniones?)\b", norm(t)):
                out.append({"author": "", "date": "", "text": t[:1000], "rating": "", "raw": t[:1200]})
    def walk(o):
        if isinstance(o, dict):
            if any(k in o for k in ("review", "comment", "reviews", "comments")):
                items = o.get("review") or o.get("reviews") or o.get("comment") or o.get("comments") or []
                if isinstance(items, dict):
                    items = [items]
                for it in items if isinstance(items, list) else []:
                    if isinstance(it, dict):
                        out.append({
                            "author": str(it.get("author", {}).get("name", "")) if isinstance(it.get("author"), dict) else str(it.get("author", "")),
                            "date": str(it.get("datePublished", "")),
                            "text": str(it.get("text", it.get("reviewBody", "")))[:1000],
                            "rating": str(it.get("reviewRating", {}).get("ratingValue", "")) if isinstance(it.get("reviewRating"), dict) else "",
                            "raw": json.dumps(it, ensure_ascii=False)[:1200],
                        })
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    for blob in jsonld:
        walk(blob)
    # desduplicar por texto
    seen, uniq = set(), []
    for c in out:
        k = norm(c["text"])[:120]
        if k and k not in seen:
            seen.add(k)
            uniq.append(c)
    return uniq


def parse_detail(html, url, soup):
    jsonld = []
    for sc in soup.find_all("script", type="application/ld+json"):
        try:
            jsonld.append(json.loads(sc.string or sc.get_text() or "{}"))
        except Exception:
            pass
    text = smart_text(soup)
    title = ""
    cand = []
    for h in soup.find_all(["h1", "h2"]):
        t = " ".join(h.get_text(" ", strip=True).split())
        if 8 < len(t) < 200:
            cand.append(t)
    if cand:
        title = max(cand, key=len)
    if not title and soup.title:
        title = soup.title.get_text(" ", strip=True)
    prices = PRICE_RE.findall(text)
    price = prices[0] if prices else ""
    cur = ""
    for c in ("USD", "CUP", "EUR", "MLC", "US$", "$", "€"):
        if c in price:
            cur = c
            break
    loc = ""
    lm = re.search(r"(La Habana|Matanzas|Villa Clara|Santiago de Cuba|Cienfuegos|Pinar del Río|Holguín|Camagüey|Artemisa|Mayabeque|Sancti Spíritus|Ciego de Ávila|Las Tunas|Granma|Guantánamo)", text, re.I)
    if lm:
        loc = lm.group(1)
    dm = DATE_RE.search(text)
    date = dm.group(0) if dm else ""
    seller, seller_url, reg, stype, phone = extract_seller(soup, text)
    comments = extract_comments(soup, text, jsonld)
    images = []
    for im in soup.find_all("img"):
        src = im.get("data-src") or im.get("data-lazy-src") or im.get("src")
        if src:
            images.append(urljoin(url, src))
    specs = {}
    for kw in ("marca", "modelo", "año", "ano", "precio", "kilómetros", "km", "combustible",
               "transmisión", "color", "condición", "motor", "potencia", "puertas", "asientos"):
        m = re.search(re.escape(kw) + r"\s*[:\-]?\s*([^\n,;]{2,60})", norm(text), re.I)
        if m:
            specs[kw] = m.group(1).strip()[:80]
    raw = {
        "title": title, "price": price, "currency": cur, "location": loc, "date": date,
        "seller": seller, "seller_url": seller_url, "seller_registered": reg,
        "seller_type": stype, "seller_phone": phone, "comments": comments,
        "prices": prices[:30], "specs": specs, "images": images[:50], "jsonld": jsonld,
        "text": text,
    }
    return {
        "title": title[:300], "price": price[:80], "currency": cur, "location": loc,
        "date": date[:80], "seller_name": seller[:120], "seller_url": seller_url[:300],
        "seller_registered": reg[:80], "seller_type": stype[:80], "seller_phone": phone[:60],
        "description": text[:12000], "specs_json": json.dumps(specs, ensure_ascii=False),
        "images_json": json.dumps(images, ensure_ascii=False),
        "prices_json": json.dumps(prices[:30], ensure_ascii=False),
        "comments_count": len(comments), "raw_json": json.dumps(raw, ensure_ascii=False),
        "raw_html": html, "comments": comments,
    }


def save_detail(conn, site, url, data, status, final):
    conn.execute(
        """INSERT OR REPLACE INTO anuncios
           (url, site, site_name, title, price, currency, location, date, seller_name,
            seller_url, seller_registered, seller_type, seller_phone, description,
            specs_json, images_json, prices_json, comments_count, raw_json, raw_html,
            status, final_url, scraped_at)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (url, site["key"], site["name"], data["title"], data["price"], data["currency"],
         data["location"], data["date"], data["seller_name"], data["seller_url"],
         data["seller_registered"], data["seller_type"], data["seller_phone"],
         data["description"], data["specs_json"], data["images_json"], data["prices_json"],
         data["comments_count"], data["raw_json"], data["raw_html"], status, final, now()),
    )
    for c in data["comments"]:
        conn.execute(
            "INSERT INTO comentarios (url, author, date, text, rating, raw) VALUES (?,?,?,?,?,?)",
            (url, c["author"], c["date"], c["text"], c["rating"], c["raw"]),
        )
    if data["seller_name"]:
        conn.execute(
            """INSERT OR REPLACE INTO vendedores (name, url, site, phone, registered, ads_count)
               VALUES (?,?,?,?,?,COALESCE((SELECT ads_count+1 FROM vendedores WHERE name=? AND site=?),1))""",
            (data["seller_name"], data["seller_url"], site["key"], data["seller_phone"],
             data["seller_registered"], data["seller_name"], site["key"]),
        )
    conn.commit()


def get_detail_urls(site):
    urls = []
    if site.get("sitemap"):
        try:
            r = creq.get(site["sitemap"], impersonate="chrome", timeout=60, verify=False)
            found = re.findall(r"<loc>\s*([^<]+?)\s*</loc>", r.text or "")
            pat = re.compile(site["sitemap_pattern"], re.I)
            urls += [u for u in found if pat.search(u)]
        except Exception as e:
            print(f"  sitemap error: {e}", flush=True)
    seeds = list(site["seeds"])
    if site.get("page_template") and site.get("pages"):
        seeds += [site["page_template"].format(page=p) for p in range(2, site["pages"] + 1)]
    for seed in seeds:
        try:
            html, _, final, soup = fetch(seed)
            for a in soup.find_all("a", href=True):
                u = urljoin(final, a["href"]).split("#")[0]
                if re.search(site["pattern"], u, re.I):
                    urls.append(u)
        except Exception as e:
            print(f"  seed error {seed}: {e}", flush=True)
    # dedup conservando orden
    return list(dict.fromkeys(urls))


def crawl_site(site, delay):
    key = site["key"]
    conn = init_db(OUT / f"{key}.sqlite")
    urls = get_detail_urls(site)[: site["max"]]
    print(f"[{key}] {len(urls)} URLs de detalle (max {site['max']})", flush=True)
    for i, u in enumerate(urls, 1):
        if conn.execute("SELECT 1 FROM anuncios WHERE url=?", (u,)).fetchone():
            continue
        html, status, final, soup = fetch(u)
        if not html:
            continue
        data = parse_detail(html, u, soup)
        save_detail(conn, site, u, data, status, final)
        if i % 10 == 0 or i == len(urls):
            print(f"[{key}] {i}/{len(urls)} | {data['title'][:55]} |comentarios={data['comments_count']} | vendedor={data['seller_name'][:25]}", flush=True)
        time.sleep(delay)
    n = conn.execute("SELECT COUNT(*) FROM anuncios").fetchone()[0]
    nc = conn.execute("SELECT COUNT(*) FROM comentarios").fetchone()[0]
    nv = conn.execute("SELECT COUNT(*) FROM vendedores").fetchone()[0]
    print(f"[{key}] LISTO anuncios={n} comentarios={nc} vendedores={nv}", flush=True)
    conn.close()


def revolico_oldest():
    """Busca la fecha mas antigua en la categoria Carros de Revolico."""
    base = "https://www.revolico.com/search?category=vehiculos&subcategory=vehiculos-carros"
    dates = []
    for order in ("date", "price", ""):
        for page in range(0, 12):
            u = base + (f"&order={order}" if order else "") + (f"&page={page}" if page else "")
            try:
                html, _, final, soup = fetch(u)
                text = smart_text(soup)
                ds = DATE_RE.findall(text)
                dates += ds
                lis = soup.select("a[href*='/item/']")
                if not lis:
                    break
            except Exception:
                break
            time.sleep(0.8)
    parsed = []
    for d in set(dates):
        for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"):
            try:
                parsed.append((datetime.strptime(d, fmt), d))
                break
            except Exception:
                pass
    parsed.sort()
    return parsed[:10], len(set(dates))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sites", nargs="*")
    ap.add_argument("--delay", type=float, default=0.6)
    ap.add_argument("--workers", type=int, default=1, help="tiendas en paralelo (BDs separadas)")
    ap.add_argument("--revolico", action="store_true")
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    if a.revolico:
        oldest, total = revolico_oldest()
        print("REVOLICO fechas encontradas:", total)
        print("MAS ANTIGUAS:", oldest[:10])
        return 0
    targets = []
    for key, site in SITES.items():
        if a.sites and key not in a.sites:
            continue
        s = dict(site)
        s["key"] = key
        targets.append(s)
    if a.workers <= 1:
        for s in targets:
            try:
                crawl_site(s, a.delay)
            except Exception as e:
                print(f"[{s['key']}] ERROR: {e}", flush=True)
    else:
        with ThreadPoolExecutor(max_workers=a.workers) as ex:
            futures = {ex.submit(crawl_site, s, a.delay): s["key"] for s in targets}
            for fut in as_completed(futures):
                try:
                    fut.result()
                except Exception as e:
                    print(f"[{futures[fut]}] ERROR: {e}", flush=True)
    lines = ["# Resumen de marketplaces", "", "| Marketplace | Anuncios | Comentarios | Vendedores |", "|---|---:|---:|---:|"]
    for db in sorted(OUT.glob("*.sqlite")):
        c = sqlite3.connect(db)
        na = c.execute("SELECT COUNT(*) FROM anuncios").fetchone()[0]
        nc = c.execute("SELECT COUNT(*) FROM comentarios").fetchone()[0]
        nv = c.execute("SELECT COUNT(*) FROM vendedores").fetchone()[0]
        c.close()
        lines.append(f"| {db.stem} | {na} | {nc} | {nv} |")
    (OUT / "resumen.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Resumen:", OUT / "resumen.md")


if __name__ == "__main__":
    raise SystemExit(main())

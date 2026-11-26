#!/usr/bin/env python3
"""Scrapeo completo de la categoria Vehiculos de Revolico, de atras hacia adelante.

Salida: Data/Revolico/revolico.sqlite
- anuncios: todos los campos del AdType + metadatos + Apollo crudo
- imagenes, telefonos, referencias (provincias/municipios/categorias)
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from curl_cffi import requests as creq

BASE = Path(__file__).resolve().parents[1]
OUT = BASE.parent / "Data" / "Revolico"
DB = OUT / "revolico.sqlite"
SEARCH = "https://www.revolico.com/search?category=vehiculos&cu=1&page={page}"
SITE = "https://www.revolico.com"
MAX_PAGE = 100


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


_tls = threading.local()


def _session():
    """Sesion por hilo: reutiliza conexion TLS y reduce latencia."""
    s = getattr(_tls, "session", None)
    if s is None:
        s = creq.Session(impersonate="chrome")
        s.headers.update({"Accept-Language": "es-ES,es;q=0.9"})
        _tls.session = s
    return s


def get_html(url, tries=3):
    last = ""
    for i in range(tries):
        try:
            r = _session().get(url, timeout=35, allow_redirects=True)
            if r.status_code == 200 and r.text:
                return r.text
            last = f"HTTP {r.status_code}"
        except Exception as e:
            last = str(e)
        time.sleep(1 + i)
    return ""


def load_json_state(html):
    soup = BeautifulSoup(html or "", "lxml")
    for sc in soup.find_all("script", type="application/json"):
        txt = sc.string or sc.get_text() or ""
        if "__APOLLO_STATE__" in txt or "pageProps" in txt:
            try:
                return json.loads(txt)
            except Exception:
                pass
    return {}


def state_from(html):
    data = load_json_state(html)
    return (((data.get("props") or {}).get("pageProps") or {}).get("__APOLLO_STATE__") or {})


def collect_urls(max_page=MAX_PAGE):
    urls = []
    for page in range(max_page, 0, -1):
        html = get_html(SEARCH.format(page=page))
        st = state_from(html)
        found = []
        for k, v in st.items():
            if k.startswith("AdType:") and isinstance(v, dict) and v.get("permalink"):
                found.append(v["permalink"])
        found = list(dict.fromkeys(found))
        urls.extend(found)
        print(f"PAGINA {page:03d}: {len(found)} anuncios (acumulado {len(urls)})", flush=True)
        time.sleep(0.35)
    return list(dict.fromkeys(urls))


def ref(obj, st):
    """Resuelve un __ref de Apollo a su objeto."""
    if isinstance(obj, dict) and "__ref" in obj:
        return st.get(obj["__ref"], {}) or {}
    return obj if isinstance(obj, dict) else {}


def parse_detail(html, url):
    st = state_from(html)
    if not st:
        return None
    soup = BeautifulSoup(html or "", "lxml")
    meta = {}
    for m in soup.find_all("meta"):
        k = m.get("property") or m.get("name")
        if k and m.get("content"):
            meta[k] = m["content"]
    ad = None
    for k, v in st.items():
        if k.startswith("AdType:") and isinstance(v, dict):
            if v.get("permalink") and (urljoin(SITE, v["permalink"]).split("?")[0] == url.split("?")[0] or len(st) < 50):
                ad = v
                break
    if not ad:
        return None
    aid = str(ad.get("id", ""))
    prov = ref(ad.get("province"), st)
    muni = ref(ad.get("municipality"), st)
    cat = ref(ad.get("category"), st)
    subcat = ref(ad.get("subcategory"), st)
    imgs = []
    for im in ad.get("readyImages") or ad.get("images") or []:
        io = ref(im, st)
        key = io.get("gcsKey") or io.get("createdKey") or ""
        if key:
            imgs.append({"id": io.get("id", ""), "key": key,
                         "url": f"https://pic.revolico.com/{key}"})
    phones = []
    pi = ad.get("phoneInfo") or {}
    for fld in ("firstPhone", "secondPhone"):
        p = pi.get(fld) or {}
        if p.get("number"):
            phones.append({"number": p.get("number"), "prefix": p.get("prefix", ""),
                           "type": p.get("type", ""), "is_whatsapp": bool(p.get("isWhatsapp"))})
    text = " ".join(soup.get_text(" ", strip=True).split())
    return {
        "id": aid,
        "url": urljoin(SITE, ad.get("permalink", "")),
        "title": ad.get("title", ""),
        "short_description": ad.get("shortDescription", ""),
        "description": ad.get("description", "") or text[:5000],
        "price": ad.get("price"),
        "currency": ad.get("currency", ""),
        "status": ad.get("status", ""),
        "seller_name": ad.get("name", ""),
        "contact_info": ad.get("contactInfo", ""),
        "updated_on_by_user": ad.get("updatedOnByUser", ""),
        "updated_on_to_order": ad.get("updatedOnToOrder", ""),
        "is_promoted": bool(ad.get("isPromoted")),
        "is_sold": bool(ad.get("isSold")),
        "views": ad.get("viewCount"),
        "images_count": ad.get("imagesCount"),
        "province_id": prov.get("id", ""),
        "province_name": prov.get("name", ""),
        "municipality_id": muni.get("id", ""),
        "municipality_name": muni.get("name", ""),
        "category_id": cat.get("id", ""),
        "category_name": cat.get("name", ""),
        "subcategory_id": subcat.get("id", ""),
        "subcategory_name": subcat.get("name", ""),
        "meta": meta,
        "images": imgs,
        "phones": phones,
        "apollo_full": json.dumps(st, ensure_ascii=False),
        "ad_json": json.dumps(ad, ensure_ascii=False),
        "text": text[:12000],
        "raw_html": html,
    }


def fetch_one(path):
    url = urljoin(SITE, path) + "?p"
    html = get_html(url, tries=2)
    if not html:
        return None
    try:
        return parse_detail(html, url)
    except Exception:
        return None


def init_db():
    OUT.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB, check_same_thread=False)
    c.row_factory = sqlite3.Row
    c.executescript(
        """
        CREATE TABLE IF NOT EXISTS anuncios (
            id TEXT PRIMARY KEY, url TEXT, title TEXT, short_description TEXT,
            description TEXT, price REAL, currency TEXT, status TEXT, seller_name TEXT,
            contact_info TEXT, updated_on_by_user TEXT, updated_on_to_order TEXT,
            is_promoted INTEGER, is_sold INTEGER, views INTEGER, images_count INTEGER,
            province_id TEXT, province_name TEXT, municipality_id TEXT, municipality_name TEXT,
            category_id TEXT, category_name TEXT, subcategory_id TEXT, subcategory_name TEXT,
            meta_json TEXT, ad_json TEXT, apollo_full TEXT, text TEXT, raw_html TEXT,
            scraped_at TEXT
        );
        CREATE TABLE IF NOT EXISTS imagenes (
            ad_id TEXT, image_id TEXT, gcs_key TEXT, url TEXT,
            PRIMARY KEY(ad_id, gcs_key)
        );
        CREATE TABLE IF NOT EXISTS telefonos (
            ad_id TEXT, number TEXT, prefix TEXT, type TEXT, is_whatsapp INTEGER,
            PRIMARY KEY(ad_id, number)
        );
        CREATE INDEX IF NOT EXISTS idx_anuncios_prov ON anuncios(province_name);
        CREATE INDEX IF NOT EXISTS idx_anuncios_date ON anuncios(updated_on_by_user);
        """
    )
    c.commit()
    return c


def save(conn, d):
    if not d:
        return
    conn.execute(
        """INSERT OR REPLACE INTO anuncios
           (id,url,title,short_description,description,price,currency,status,seller_name,
            contact_info,updated_on_by_user,updated_on_to_order,is_promoted,is_sold,views,
            images_count,province_id,province_name,municipality_id,municipality_name,
            category_id,category_name,subcategory_id,subcategory_name,meta_json,ad_json,
            apollo_full,text,raw_html,scraped_at)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (d["id"], d["url"], d["title"], d["short_description"], d["description"],
         d["price"], d["currency"], d["status"], d["seller_name"], d["contact_info"],
         d["updated_on_by_user"], d["updated_on_to_order"], int(d["is_promoted"]),
         int(d["is_sold"]), d["views"], d["images_count"], d["province_id"],
         d["province_name"], d["municipality_id"], d["municipality_name"],
         d["category_id"], d["category_name"], d["subcategory_id"], d["subcategory_name"],
         json.dumps(d["meta"], ensure_ascii=False), d["ad_json"], d["apollo_full"],
         d["text"], d["raw_html"], now()),
    )
    for im in d["images"]:
        conn.execute("INSERT OR IGNORE INTO imagenes (ad_id,image_id,gcs_key,url) VALUES (?,?,?,?)",
                     (d["id"], str(im["id"]), im["key"], im["url"]))
    for ph in d["phones"]:
        conn.execute("INSERT OR IGNORE INTO telefonos (ad_id,number,prefix,type,is_whatsapp) VALUES (?,?,?,?,?)",
                     (d["id"], str(ph["number"]), ph["prefix"], ph["type"], int(ph["is_whatsapp"])))
    conn.commit()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-page", type=int, default=MAX_PAGE)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--no-pages", action="store_true", help="reutilizar URLs ya descubiertas")
    a = ap.parse_args()

    conn = init_db()
    if not a.no_pages:
        urls = collect_urls(a.max_page)
        (OUT / "urls.txt").write_text("\n".join(urls) + "\n", encoding="utf-8")
    else:
        urls = (OUT / "urls.txt").read_text(encoding="utf-8").splitlines()
    print(f"TOTAL URLs UNICAS: {len(urls)}", flush=True)

    existing = {r[0] for r in conn.execute("SELECT id FROM anuncios")}
    pending = []
    for u in urls:
        m = re.search(r"-(\d+)(?:\?|$)", u)
        aid = m.group(1) if m else u.rsplit("/", 1)[-1].split("?")[0]
        if aid not in existing:
            pending.append(u)
    print(f"PENDIENTES: {len(pending)}", flush=True)

    done = 0
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(fetch_one, u): u for u in pending}
        for fut in as_completed(futs):
            try:
                d = fut.result()
                if d:
                    save(conn, d)
                    done += 1
            except Exception:
                pass
            if done % 200 == 0 and done:
                print(f"GUARDADOS {done}/{len(pending)}", flush=True)

    n = conn.execute("SELECT COUNT(*) FROM anuncios").fetchone()[0]
    ni = conn.execute("SELECT COUNT(*) FROM imagenes").fetchone()[0]
    nt = conn.execute("SELECT COUNT(*) FROM telefonos").fetchone()[0]
    mn = conn.execute("SELECT MIN(updated_on_by_user), MAX(updated_on_by_user) FROM anuncios").fetchone()
    lines = [
        "# Revolico — base de datos completa de la categoría Vehículos",
        "",
        f"- Anuncios: **{n}**",
        f"- Imágenes: **{ni}**",
        f"- Teléfonos: **{nt}**",
        f"- Fecha `updatedOnByUser` más antigua: **{mn[0]}**",
        f"- Fecha `updatedOnByUser` más reciente: **{mn[1]}**",
        f"- Páginas recorridas: {a.max_page} → 1 (hacia atrás)",
        "",
        "Tablas: `anuncios` (todos los campos AdType + Apollo completo), `imagenes`, `telefonos`.",
    ]
    (OUT / "resumen.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("RESUMEN:", OUT / "resumen.md")
    conn.close()


if __name__ == "__main__":
    main()

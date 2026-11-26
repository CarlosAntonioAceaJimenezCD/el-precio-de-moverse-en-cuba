#!/usr/bin/env python3
"""Scrapea talleres y servicios técnicos desde directorios y webs de concesionarios."""
import json
import re
import time
import warnings
from pathlib import Path
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from curl_cffi import requests as creq

import mapa_db as db

BASE = Path(__file__).resolve().parents[1]
RAW = BASE.parent / "Data" / "talleres"


BLOCK_MARKERS = ("captcha", "comprobación de seguridad", "verificación de seguridad", "anomaly", "just a moment")


def _blocked(status, text):
    low = (text or "").lower()
    return status != 200 or len(text or "") < 800 or any(m in low for m in BLOCK_MARKERS)


def patchright_fetch(url):
    """Navegador real con fingerprint de Chrome, util cuando curl_cffi recibe 403."""
    try:
        from patchright.sync_api import sync_playwright

        with sync_playwright() as p:
            b = p.chromium.launch(
                headless=True,
                executable_path="/usr/bin/chromium",
                args=["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"],
            )
            ctx = b.new_context(locale="es-ES", viewport={"width": 1440, "height": 900},
                                ignore_https_errors=True)
            pg = ctx.new_page()
            pg.goto(url, wait_until="domcontentloaded", timeout=60000)
            pg.wait_for_timeout(3000)
            html = pg.content()
            b.close()
            return html or ""
    except Exception:
        return ""


def flaresolverr_fetch(url):
    """Ultimo recurso: FlareSolverr resuelve challenges con navegador real."""
    try:
        r = creq.post(
            "http://127.0.0.1:8191/v1",
            json={"cmd": "request.get", "url": url, "maxTimeout": 60000},
            timeout=90,
        )
        d = r.json()
        if d.get("status") == "ok":
            return (d.get("solution") or {}).get("response") or ""
    except Exception:
        pass
    return ""


def get(url, verify=True, evasive=True):
    """curl_cffi -> patchright -> FlareSolverr, segun el bloqueo."""
    best = ""
    for imp in ("chrome", "safari"):
        try:
            r = creq.get(url, impersonate=imp, timeout=90, verify=verify,
                         headers={"Accept-Language": "es-ES,es;q=0.9"})
            best = r.text or ""
            if not _blocked(r.status_code, best):
                return best
        except Exception:
            pass
    if evasive:
        html = patchright_fetch(url)
        if html and not _blocked(200, html):
            return html
        html = flaresolverr_fetch(url)
        if html and not _blocked(200, html):
            return html
    return best


def text_of(html):
    s = BeautifulSoup(html or "", "lxml")
    for t in s(["script", "style", "noscript"]):
        t.decompose()
    return " ".join(s.get_text(" ", strip=True).split())


def geocode(q):
    try:
        r = creq.get("https://nominatim.openstreetmap.org/search",
                     params={"q": q + ", La Habana, Cuba", "format": "json", "limit": 1},
                     impersonate="chrome", timeout=40,
                     headers={"User-Agent": "ICD-Automotive-Research/1.0"})
        d = r.json()
        if d:
            return float(d[0]["lat"]), float(d[0]["lon"])
    except Exception:
        pass
    return None, None


def save_raw(name, html):
    RAW.mkdir(parents=True, exist_ok=True)
    (RAW / f"{name}.html").write_text(html or "", encoding="utf-8", errors="ignore")


def bdc(c):
    url = "https://bdcone.online/tiendas-y-talleres/"
    html = get(url)
    save_raw("bdc_tiendas_y_talleres", html)
    s = BeautifulSoup(html, "lxml")
    for sc in s.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(sc.string or sc.get_text() or "{}")
        except Exception:
            continue
        for node in data.get("@graph", []) if isinstance(data, dict) else []:
            if not isinstance(node, dict) or "Place" not in str(node.get("@type", "")):
                continue
            geo = node.get("geo") or {}
            addr = node.get("address") or {}
            if geo.get("latitude") and geo.get("longitude"):
                direccion = " ".join(str(addr.get(k, "")) for k in ("streetAddress", "addressLocality", "addressRegion")).strip()
                db.upsert(c, "taller", "BDC One - Taller y tienda de repuestos",
                          geo["latitude"], geo["longitude"], direccion, "BDC One", url,
                          detalles={"fuente": "schema.org Place", "nodo": node.get("@id", "")})
    for lat, lon in set(re.findall(r"!3d(-?\d+\.\d+)!2d(-?\d+\.\d+)", html)):
        db.upsert(c, "taller", "BDC One - Taller (mapa)",
                  lat, lon, "La Habana", "BDC One", url,
                  detalles={"fuente": "Google Maps embed en tiendas-y-talleres"})


def dongfeng(c):
    url = "https://www.dongfengcuba.com/contacto/"
    html = get(url)
    save_raw("dongfeng_contacto", html)
    txt = text_of(html)
    direcciones = re.findall(r"(?:Showroom\s*\d+|Dirección \(Oficina\)):\s*([^.]{10,120})", txt, re.I)
    if not direcciones:
        direcciones = [
            "Inmobiliaria Residencial Miramar, Ave. 7ma y Calle 20, Miramar, La Habana",
            "Complejo 5ta Avenida, 5ta Avenida y Calle 114, Playa, La Habana",
        ]
    for i, d in enumerate(direcciones[:3], 1):
        lat, lon = geocode(d.strip())
        db.upsert(c, "taller", f"Dongfeng Cuba - Servicio y soporte ({i})",
                  lat, lon, d.strip(), "Dongfeng Cuba", url,
                  estado="servicio técnico declarado; dirección de showroom/oficina",
                  detalles={"tipo": "postventa", "direccion": d.strip()})
        time.sleep(1.1)


def cubisima(c):
    url = "https://www.cubisima.com/Directorio/anuncio/taller-de-mecanica-automotriz-taller-calle-8/20896"
    html = get(url)
    save_raw("cubisima_taller_calle_8", html)
    txt = text_of(html)
    m = re.search(r"Direcci[oó]n del negocio\s+(.+?)\s+Categor[ií]a:", txt, re.I)
    direccion = m.group(1).strip() if m else "Calle 8 #112 entre 1ra y 3ra, Miramar, Playa, La Habana"
    coord = re.search(r"(-?\d{2}\.\d{4,})[, ]+(-?\d{2,3}\.\d{4,})", html)
    lat, lon = (coord.group(1), coord.group(2)) if coord else geocode(direccion)
    phones = re.findall(r"\b\d{8}\b", txt)
    db.upsert(c, "taller", "Taller de Mecánica Automotriz Taller Calle 8",
              lat, lon, direccion, "Cubisima Directorio", url,
              telefono=" / ".join(dict.fromkeys(phones[:3])),
              detalles={"negocio": "Taller Calle 8", "categoria": "Talleres de mecánica y electricidad"})


def nearplace(c):
    url = "https://cu.near-place.com/car_repair/havana"
    html = get(url)
    save_raw("nearplace_car_repair_havana", html)
    m = re.search(r"var A=(\[.*?\]);", html, re.S)
    if not m:
        return
    items = json.loads(m.group(1))
    for x in items:
        link = x.get("li", "")
        if link.startswith("//"):
            link = "https:" + link
        db.upsert(c, "taller", x.get("name", "Taller"),
                  x.get("lat"), x.get("lng"), x.get("v", "La Habana"),
                  "NearPlace", link or url,
                  detalles={"categoria": "car_repair", "raw": x})


def manolito(c):
    url = "https://tallermanolito.com/"
    html = get(url)
    save_raw("taller_manolito", html)
    txt = text_of(html)
    lat, lon = None, None
    embed = re.search(r"google\.com/maps\?cid=([^&\"]+)", html)
    if embed:
        ehtml = get("https://www.google.com/maps?cid=" + embed.group(1) + "&output=embed")
        m = re.search(r"@(-?\d+\.\d+),(-?\d+\.\d+)", ehtml) or re.search(r"!3d(-?\d+\.\d+)!2d(-?\d+\.\d+)", ehtml)
        if m:
            lat, lon = m.group(1), m.group(2)
    if lat is None:
        lat, lon = geocode("Taller Manolito, La Habana")
    db.upsert(c, "taller", "Taller Automotriz Manolito",
              lat, lon, "La Habana", "tallermanolito.com", url,
              detalles={"servicio": "repuestos y servicio mecánico"})


def pamarillas(c):
    warnings.filterwarnings("ignore")
    url = "https://pamarillas.cu/amarillas/categoria/mecanica-talleres-de"
    try:
        html = get(url, verify=False)
    except Exception:
        return
    save_raw("pamarillas_mecanica_talleres", html)
    s = BeautifulSoup(html, "lxml")
    txt = text_of(html)
    # Patron: NOMBRE Mecánica, Talleres de DIRECCION descripcion
    items = re.findall(r"([A-ZÁÉÍÓÚ0-9][^:]{2,60}?)\s+Mec[iá]nica, Talleres de\s+([^.]{8,120})", txt, re.I)
    for name, direccion in items[:50]:
        lat, lon = geocode(direccion.strip())
        db.upsert(c, "taller", name.strip()[:120], lat, lon, direccion.strip(),
                  "Páginas Amarillas", url,
                  detalles={"categoria": "Mecánica, Talleres de"})
        time.sleep(1.1)


def yellocu(c):
    url = "https://es.yellocu.com/category/Venta_de_veh%C3%ADculos/city:Havana"
    html = get(url)
    save_raw("yellocu_venta_vehiculos_habana", html)
    s = BeautifulSoup(html or "", "lxml")
    for div in s.select("div.company"):
        a = div.select_one("h3 a")
        if not a:
            continue
        nombre = a.get_text(" ", strip=True)
        link = urljoin(url, a.get("href", ""))
        addr_el = div.select_one(".address")
        direccion = addr_el.get_text(" ", strip=True) if addr_el else "La Habana"
        lat = div.get("data-map-lat") or (div.parent.get("data-map-lat") if div.parent else None)
        lon = div.get("data-map-lng") or (div.parent.get("data-map-lng") if div.parent else None)
        phone = ""
        for span in div.select("span"):
            txt = span.get_text(" ", strip=True)
            if txt.startswith("+53"):
                phone = txt
                break
        if not lat or not lon:
            lat, lon = geocode(direccion)
        db.upsert(c, "concesionario", nombre, lat, lon, direccion,
                  "Yellocu", link, telefono=phone,
                  detalles={"categoria": "Venta de vehículos", "ciudad": "Habana"})
        time.sleep(1.1)


def cybo(c):
    url = "https://es.cybo.com/CU/la-habana/concesionarios-de-los-coches-nuevos"
    html = get(url)  # patchright/FlareSolverr entran aqui si curl_cffi recibe 403
    save_raw("cybo_concesionarios_nuevos_habana", html)
    t = (html or "").replace('\\"', '"')
    pat = re.compile(
        r'cardTitle.*?"children":"([^"]+)"\s*\}\],.*?cardAddress.*?"children":"([^"]+)"',
        re.S,
    )
    for m in pat.finditer(t):
        nombre, direccion = m.group(1).strip(), m.group(2).strip()
        if not nombre or "bus stop" in nombre.lower() or "acuario" in nombre.lower():
            continue
        lat, lon = geocode(direccion)
        db.upsert(c, "concesionario", nombre, lat, lon, direccion,
                  "Cybo", url, detalles={"categoria": "Concesionarios de coches nuevos",
                                          "nota": "directorio con datos de baja verificacion"})
        time.sleep(1.1)


def main():
    c = db.import_csvs()
    bdc(c)
    dongfeng(c)
    cubisima(c)
    nearplace(c)
    manolito(c)
    pamarillas(c)
    yellocu(c)
    cybo(c)
    print("\nElementos por tipo:")
    for row in c.execute("SELECT tipo, COUNT(*), SUM(CASE WHEN lat IS NOT NULL THEN 1 ELSE 0 END) FROM elementos GROUP BY tipo"):
        print(f"  {row[0]}: {row[1]} (con coords {row[2]})")
    c.close()


if __name__ == "__main__":
    main()

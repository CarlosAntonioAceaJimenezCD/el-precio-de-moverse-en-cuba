#!/usr/bin/env python3
"""Extrae gasolineras de La Habana, estaciones de carga y precios del combustible.

Salidas:
  Data/mapas/gasolineras.csv
  Data/mapas/estaciones_carga.csv
  Data/combustible/precios_combustible.sqlite
"""
import csv
import json
import re
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path

from bs4 import BeautifulSoup
from curl_cffi import requests as creq

BASE = Path(__file__).resolve().parents[1]
PROJECT = BASE.parent
MAPS = PROJECT / "Data" / "mapas"
COMB = PROJECT / "Data" / "combustible"
DB = COMB / "precios_combustible.sqlite"

MONTHS = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "sep": 9, "octubre": 10, "oct": 10,
    "noviembre": 11, "nov": 11, "diciembre": 12, "dic": 12,
}


def get(url):
    r = creq.get(url, impersonate="chrome", timeout=90, headers={"Accept-Language": "es-ES,es;q=0.9"})
    return r.text or ""


def text_of(html):
    s = BeautifulSoup(html or "", "lxml")
    for t in s(["script", "style", "noscript"]):
        t.decompose()
    return " ".join(s.get_text(" ", strip=True).split())


def fecha_es(m):
    d, mon, y = int(m.group(1)), MONTHS[m.group(2).lower()], int(m.group(3))
    return f"{y:04d}-{mon:02d}-{d:02d}"


def gasolineras():
    d = json.loads((MAPS / "overpass_gasolineras.json").read_text(encoding="utf-8"))
    rows = []
    for e in d.get("elements", []):
        t = e.get("tags") or {}
        lat = e.get("lat") or (e.get("center") or {}).get("lat")
        lon = e.get("lon") or (e.get("center") or {}).get("lon")
        if lat is None or lon is None:
            continue
        rows.append({
            "fuente": "OpenStreetMap/Overpass",
            "nombre": t.get("name", "") or t.get("brand", "") or "Gasolinera",
            "lat": lat, "lon": lon,
            "marca": t.get("brand", ""),
            "direccion": t.get("addr:street", "") or t.get("addr:housenumber", ""),
            "diesel": t.get("fuel:diesel", ""),
            "octanaje95": t.get("fuel:octane_95", ""),
            "horario": t.get("opening_hours", ""),
        })
    with (MAPS / "gasolineras.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(f"Gasolineras: {len(rows)}")


def geocode(q):
    try:
        r = creq.get("https://nominatim.openstreetmap.org/search",
                     params={"q": q + ", Cuba", "format": "json", "limit": 1},
                     impersonate="chrome", timeout=40,
                     headers={"User-Agent": "ICD-Automotive-Research/1.0"})
        d = r.json()
        if d:
            return float(d[0]["lat"]), float(d[0]["lon"])
    except Exception:
        pass
    return None, None


def estaciones_carga():
    rows = []
    # Kargalaya (datos embebidos en la página)
    t = get("https://www.kargalaya.com/").replace('\\"', '"')
    pat = re.compile(
        r'\{"id":"[^"]+","slug":"[^"]+","name":"(?P<name>[^"]+)",'
        r'"latitude":(?P<lat>-?\d+\.\d+),"longitude":(?P<lon>-?\d+\.\d+),'
        r'"municipality":"(?P<mun>[^"]+)","province":"(?P<prov>[^"]+)",'
        r'"pricePerHour":(?P<price>\d+),"priceUnit":"[^"]+",'
        r'"verificationStatus":"(?P<ver>[^"]+)","renewableEnergy":(?P<ren>true|false)\}'
    )
    for m in pat.finditer(t):
        x = m.groupdict()
        rows.append({
            "fuente": "Kargalaya", "nombre": x["name"], "lat": x["lat"], "lon": x["lon"],
            "provincia": x["prov"], "municipio": x["mun"], "precio": x["price"],
            "estado": x["ver"], "renovable": x["ren"], "url": "https://www.kargalaya.com/estaciones",
        })
    # Electromaps: 3 puntos sin coordenadas en HTML; geocodificar por nombre
    for name, query in [
        ("Tecxol_Xetid_1", "Tecxol, Havana, Cuba"),
        ("Campismo Las Almendras", "Las Almendras, Bejucal, Cuba"),
        ("Campismo Peña Blanca", "Peña Blanca, Cuba"),
    ]:
        lat, lon = geocode(query)
        if lat is None:
            rows.append({
                "fuente": "Electromaps", "nombre": name, "lat": "", "lon": "",
                "provincia": "La Habana", "municipio": "", "precio": "", "estado": "sin coordenadas",
                "renovable": "", "url": "https://www.electromaps.com/es/puntos-carga/cuba",
            })
            continue
        rows.append({
            "fuente": "Electromaps", "nombre": name, "lat": lat, "lon": lon,
            "provincia": "La Habana", "municipio": "", "precio": "", "estado": "listado",
            "renovable": "", "url": "https://www.electromaps.com/es/puntos-carga/cuba",
        })
        time.sleep(1.1)
    with (MAPS / "estaciones_carga.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(f"Estaciones de carga: {len(rows)}")


def init_db():
    COMB.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB)
    c.execute("""CREATE TABLE IF NOT EXISTS precios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT, tipo TEXT, mercado TEXT, precio_min REAL, precio_max REAL,
        moneda TEXT, fuente TEXT, url TEXT, nota TEXT, scraped_at TEXT,
        UNIQUE(fecha,tipo,mercado,moneda,precio_min,precio_max,fuente)
    )""")
    c.commit()
    return c


def add(c, fecha, tipo, mercado, pmin, pmax, moneda, fuente, url, nota=""):
    c.execute("""INSERT OR IGNORE INTO precios
        (fecha,tipo,mercado,precio_min,precio_max,moneda,fuente,url,nota,scraped_at)
        VALUES (?,?,?,?,?,?,?,?,?,?)""",
        (fecha, tipo, mercado, pmin, pmax, moneda, fuente, url, nota, now()))


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def precios():
    c = init_db()
    # encuba (CIMEX, 15 may 2026, publicado 14 oct 2026)
    t = text_of(get("https://encuba.net/precio-gasolina-cuba/"))
    m = re.search(r"publicado por[^ ]+ on (\d{1,2}) (\w+) (\d{4})", t, re.I)
    fecha = fecha_es(m) if m else "2026-10-14"
    for tipo, val in [
        ("Gasolina B100", r"Gasolina especial B100:\s*([\d,]+) USD"),
        ("Gasolina B94", r"Gasolina especial B94:\s*([\d,]+) USD"),
        ("Gasolina B90", r"Gasolina regular B90:\s*([\d,]+) USD"),
        ("Gasolina B83", r"Gasolina motor B83:\s*([\d,]+) USD"),
    ]:
        x = re.search(val, t, re.I)
        if x:
            add(c, "2026-05-15", tipo, "oficial CIMEX", float(x.group(1).replace(",", ".")),
                float(x.group(1).replace(",", ".")), "USD", "encuba.net",
                "https://encuba.net/precio-gasolina-cuba/", "tarifa vigente desde 15/05/2026")
    # Directorio Cubano 11 sep 2026
    t = text_of(get("https://www.directoriocubano.info/precio-combustible-cuba-hoy/"))
    m = re.search(r"precios del (\d{1,2}) (\w+)\. (\d{4})", t, re.I)
    fecha = fecha_es(m) if m else "2026-09-11"
    for tipo, pat in [
        ("Gasolina B94", r"B-94 Especial\s*([\d\s]+)[–-]([\d\s]+)CUP/L"),
        ("Gasolina B90", r"B-90 Regular\s*([\d\s]+)[–-]([\d\s]+)CUP/L"),
        ("Gasolina B83", r"B-83 Motor\s*([\d\s]+)CUP/L"),
        ("Diesel", r"Petroleo/ Diesel\s*([\d\s]+)[–-]([\d\s]+)CUP/L"),
    ]:
        x = re.search(pat, t, re.I)
        if x:
            nums = [float(g.replace(" ", "")) for g in x.groups() if g]
            add(c, fecha, tipo, "informal elToque", min(nums), max(nums), "CUP",
                "Directorio Cubano", "https://www.directoriocubano.info/precio-combustible-cuba-hoy/")
    for tipo, pat in [
        ("Gasolina B100", r"Gasolina Especial B100\s+([\d.]+)\s+USD\s+([\d.]+)\s+USD"),
        ("Gasolina B94", r"Gasolina Especial B94\s+([\d.]+)\s+USD\s+([\d.]+)\s+USD"),
        ("Gasolina B90", r"Gasolina Regular B90\s+([\d.]+)\s+USD\s+([\d.]+)\s+USD"),
        ("Gasolina B83", r"Gasolina Motor B83\s+([\d.]+)\s+USD\s+([\d.]+)\s+USD"),
        ("Diesel especial", r"Diesel Especial\s+([\d.]+)\s+USD\s+([\d.]+)\s+USD"),
        ("Diesel regular", r"Diesel Regular\s+([\d.]+)\s+USD\s+([\d.]+)\s+USD"),
    ]:
        x = re.search(pat, t, re.I)
        if x:
            v = float(x.group(2))
            add(c, fecha, tipo, "oficial CIMEX", v, v, "USD", "Directorio Cubano",
                "https://www.directoriocubano.info/precio-combustible-cuba-hoy/")
    # d-cuba 20 ago 2026
    t = text_of(get("https://d-cuba.com/actualidad/precio-combustible-cuba-gasolina-diesel"))
    m = re.search(r"Última actualización: (\d{1,2}) de (\w+) de (\d{4})", t, re.I)
    fecha = fecha_es(m) if m else "2026-08-20"
    for tipo, pat in [
        ("Gasolina B94", r"Gasolina B-94 Especial\s*([\d.,]+)[–-]([\d.,]+) CUP"),
        ("Gasolina B90", r"Gasolina B-90 Regular\s*([\d.,]+)[–-]([\d.,]+) CUP"),
        ("Gasolina B83", r"Gasolina B-83 Motor\s*([\d.,]+) CUP"),
        ("Diesel", r"Diésel\s*([\d.,]+)[–-]([\d.,]+) CUP"),
    ]:
        x = re.search(pat, t, re.I)
        if x:
            nums = [float(g.replace(".", "").replace(",", ".")) for g in x.groups() if g]
            add(c, fecha, tipo, "informal", min(nums), max(nums), "CUP", "D-Cuba",
                "https://d-cuba.com/actualidad/precio-combustible-cuba-gasolina-diesel")
    # dailyfuels / globalpetrolprices (puntos recientes)
    for url, fuente in [
        ("https://www.dailyfuels.com/cuba/", "DailyFuels"),
        ("https://es.globalpetrolprices.com/Cuba/gasoline_prices/", "GlobalPetrolPrices"),
        ("https://es.globalpetrolprices.com/Cuba/diesel_prices/", "GlobalPetrolPrices"),
    ]:
        t = text_of(get(url))
        m = re.search(r"(?:Actualizado|actualizado)[:\s]*(\d{4}-\d{2}-\d{2})", t) or re.search(r"(\d{1,2}-\w{3}-\d{4})", t)
        if not m:
            continue
        fecha = m.group(1)
        if "-" in fecha and not re.match(r"\d{4}-", fecha):
            d, mo, y = fecha.split("-")
            fecha = f"{y}-{MONTHS[mo.lower()]}-{int(d):02d}"
        if "dailyfuels" in url:
            for tipo, pat in [
                ("Gasolina", r"Gasolina\s+\$\s*([\d.,]+)"),
                ("Diesel", r"Diésel\s+\$\s*([\d.,]+)"),
            ]:
                x = re.search(pat, t, re.I)
                if x:
                    v = float(x.group(1).replace(",", "."))
                    add(c, fecha[:10], tipo, "oficial/publicado", v, v, "USD", fuente, url)
        else:
            tipo = "Diesel" if "diesel" in url.lower() else "Gasolina"
            for moneda, pat in [("CUP", r"CUP\s+([\d.]+)"), ("USD", r"USD\s+([\d.]+)")]:
                x = re.search(pat, t, re.I)
                if x:
                    v = float(x.group(1).replace(",", "."))
                    add(c, fecha[:10], tipo, "publicado", v, v, moneda, fuente, url)
    c.commit()
    n = c.execute("SELECT COUNT(*) FROM precios").fetchone()[0]
    print(f"Precios guardados: {n}")
    c.close()


def main():
    gasolineras()
    estaciones_carga()
    precios()


if __name__ == "__main__":
    main()

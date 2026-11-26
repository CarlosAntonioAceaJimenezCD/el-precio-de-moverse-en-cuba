#!/usr/bin/env python3
"""Completa lat/lon de los elementos del mapa a partir de su direccion."""
import json
import sqlite3
import time
from pathlib import Path

from curl_cffi import requests as creq

BASE = Path(__file__).resolve().parents[1]
DB = BASE.parent / "Data" / "mapas" / "mapa_elementos.sqlite"
PROVINCIAS = ("habana", "matanzas", "villa clara", "holgu", "santiago", "camagüey", "pinar", "artemisa", "mayabeque")


def build_query(addr):
    a = " ".join((addr or "").split())
    low = a.lower()
    if any(p in low for p in PROVINCIAS):
        return a if a.lower().endswith("cuba") else a + ", Cuba"
    return a + ", La Habana, Cuba"


def geocode(q):
    # Nominatim
    try:
        r = creq.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": q, "format": "json", "limit": 1},
            impersonate="chrome", timeout=40,
            headers={"User-Agent": "ICD-Automotive-Research/1.0"},
        )
        d = r.json()
        if d:
            return float(d[0]["lat"]), float(d[0]["lon"]), "Nominatim"
    except Exception:
        pass
    # Photon (fallback)
    try:
        r = creq.get(
            "https://photon.komoot.io/api/",
            params={"q": q, "limit": 1},
            impersonate="chrome", timeout=40,
        )
        d = r.json()
        feats = d.get("features") or []
        if feats:
            lon, lat = feats[0]["geometry"]["coordinates"]
            return float(lat), float(lon), "Photon"
    except Exception:
        pass
    return None, None, None


def main():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    rows = c.execute(
        """SELECT id,tipo,nombre,direccion,detalles_json
           FROM elementos
           WHERE (lat IS NULL OR lon IS NULL) AND direccion IS NOT NULL AND TRIM(direccion)<>''
           ORDER BY tipo,nombre"""
    ).fetchall()
    print(f"Pendientes de geocodificar: {len(rows)}")
    cache = {}
    ok = 0
    for r in rows:
        addr = r["direccion"]
        if addr in cache:
            lat, lon, fuente = cache[addr]
        else:
            lat, lon, fuente = geocode(build_query(addr))
            cache[addr] = (lat, lon, fuente)
            time.sleep(1.1)
        detalles = {}
        try:
            detalles = json.loads(r["detalles_json"] or "{}")
        except Exception:
            pass
        if lat is not None:
            detalles["geocodificado"] = fuente
            c.execute(
                "UPDATE elementos SET lat=?,lon=?,detalles_json=?,scraped_at=datetime('now') WHERE id=?",
                (lat, lon, json.dumps(detalles, ensure_ascii=False), r["id"]),
            )
            ok += 1
            print(f"  OK {r['tipo']:15} {r['nombre'][:45]:45} -> {lat:.5f},{lon:.5f} [{fuente}]")
        else:
            print(f"  -- {r['tipo']:15} {r['nombre'][:45]:45} sin coords")
    c.commit()
    print(f"Geocodificados: {ok}/{len(rows)}")
    for row in c.execute("SELECT tipo,COUNT(*),SUM(CASE WHEN lat IS NOT NULL THEN 1 ELSE 0 END) FROM elementos GROUP BY tipo"):
        print(f"  {row[0]}: {row[1]} totales, {row[2]} con coords")
    c.close()


if __name__ == "__main__":
    main()

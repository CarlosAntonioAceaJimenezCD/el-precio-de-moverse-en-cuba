#!/usr/bin/env python3
"""Base unica de elementos del mapa: concesionarios, carga, gasolineras y talleres."""
import csv
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
MAPS = BASE.parent / "Data" / "mapas"
DB = MAPS / "mapa_elementos.sqlite"

TIPOS = [
    ("gasolinera", "negro", "#000000", "circle", "Gasolineras"),
    ("estacion_carga", "verde", "#2ca02c", "diamond", "Estaciones de carga eléctrica"),
    ("concesionario", "azul", "#1f77b4", "square", "Concesionarios y distribuidores"),
    ("taller", "rojo", "#d62728", "triangle-up", "Talleres y servicio técnico"),
]


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def init_db():
    MAPS.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB)
    c.executescript(
        """
        CREATE TABLE IF NOT EXISTS tipos (
            tipo TEXT PRIMARY KEY, color_nombre TEXT, color_hex TEXT,
            simbolo TEXT, descripcion TEXT
        );
        CREATE TABLE IF NOT EXISTS elementos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            nombre TEXT NOT NULL,
            lat REAL,
            lon REAL,
            direccion TEXT,
            fuente TEXT,
            url TEXT,
            telefono TEXT,
            horario TEXT,
            precio TEXT,
            estado TEXT,
            detalles_json TEXT,
            raw_json TEXT,
            scraped_at TEXT,
            UNIQUE(tipo, nombre, lat, lon)
        );
        CREATE INDEX IF NOT EXISTS idx_elementos_tipo ON elementos(tipo);
        """
    )
    for row in TIPOS:
        c.execute("INSERT OR REPLACE INTO tipos VALUES (?,?,?,?,?)", row)
    c.commit()
    return c


def upsert(c, tipo, nombre, lat, lon, direccion="", fuente="", url="",
           telefono="", horario="", precio="", estado="", detalles=None, raw=None):
    try:
        lat = float(lat) if lat not in (None, "") else None
        lon = float(lon) if lon not in (None, "") else None
    except (TypeError, ValueError):
        lat = lon = None
    nombre = str(nombre)[:200]
    direccion = str(direccion or "")[:300]
    existing = c.execute(
        """SELECT id FROM elementos
           WHERE tipo=? AND nombre=? AND direccion=? LIMIT 1""",
        (tipo, nombre, direccion),
    ).fetchone()
    values = (
        lat, lon, direccion, str(fuente or "")[:120], str(url or "")[:500],
        str(telefono or "")[:120], str(horario or "")[:120], str(precio or "")[:120],
        str(estado or "")[:120], json.dumps(detalles or {}, ensure_ascii=False),
        json.dumps(raw or {}, ensure_ascii=False), now(),
    )
    if existing:
        c.execute(
            """UPDATE elementos SET lat=?,lon=?,direccion=?,fuente=?,url=?,telefono=?,
               horario=?,precio=?,estado=?,detalles_json=?,raw_json=?,scraped_at=?
               WHERE id=?""",
            values + (existing[0],),
        )
    else:
        c.execute(
            """INSERT INTO elementos
               (tipo,nombre,lat,lon,direccion,fuente,url,telefono,horario,precio,estado,detalles_json,raw_json,scraped_at)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (tipo, nombre) + values,
        )
    c.commit()


def import_csvs(c=None):
    c = c or init_db()
    # Concesionarios
    p = MAPS / "concesionarios.csv"
    if p.exists():
        for r in csv.DictReader(p.open(encoding="utf-8")):
            upsert(c, "concesionario", r.get("name", ""), r.get("lat"), r.get("lon"),
                   r.get("address", ""), "web del concesionario", "", detalles=r)
    # Gasolineras
    p = MAPS / "gasolineras.csv"
    if p.exists():
        for r in csv.DictReader(p.open(encoding="utf-8")):
            upsert(c, "gasolinera", r.get("nombre", ""), r.get("lat"), r.get("lon"),
                   r.get("direccion", ""), r.get("fuente", ""), "",
                   horario=r.get("horario", ""), precio=f"diésel={r.get('diesel','')}; 95={r.get('octanaje95','')}",
                   detalles=r)
    # Estaciones de carga
    p = MAPS / "estaciones_carga.csv"
    if p.exists():
        for r in csv.DictReader(p.open(encoding="utf-8")):
            upsert(c, "estacion_carga", r.get("nombre", ""), r.get("lat"), r.get("lon"),
                   f"{r.get('municipio','')}, {r.get('provincia','')}".strip(", "),
                   r.get("fuente", ""), r.get("url", ""),
                   precio=f"{r.get('precio','')} CUP/h", estado=r.get("estado", ""),
                   detalles=r)
    return c


def main():
    c = import_csvs()
    print("Elementos por tipo:")
    for row in c.execute("SELECT tipo, COUNT(*), SUM(CASE WHEN lat IS NOT NULL THEN 1 ELSE 0 END) FROM elementos GROUP BY tipo"):
        print(f"  {row[0]}: {row[1]} (con coords {row[2]})")
    c.close()


if __name__ == "__main__":
    main()

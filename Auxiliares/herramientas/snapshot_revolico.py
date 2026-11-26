#!/usr/bin/env python3
"""Guarda un snapshot semanal de precios de los carros de Revolico.

Tabla price_history: id anuncio, precio, moneda, fecha_lectura.
Idempotente: un mismo dia sobrescribe su propia lectura.
"""
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB = Path("/home/thony70807/Proyectos/ICD Automotive Market Project/Data/Revolico/revolico.sqlite")


def main():
    c = sqlite3.connect(DB, timeout=60)
    c.execute("PRAGMA busy_timeout=60000")
    c.execute(
        """CREATE TABLE IF NOT EXISTS price_history (
            id TEXT, precio REAL, moneda TEXT, fecha_lectura TEXT,
            PRIMARY KEY(id, fecha_lectura)
        )"""
    )
    hoy = datetime.now(timezone.utc).date().isoformat()
    rows = c.execute("SELECT id, price, currency FROM autos").fetchall()
    c.executemany(
        "INSERT OR REPLACE INTO price_history (id,precio,moneda,fecha_lectura) VALUES (?,?,?,?)",
        [(i, p, m, hoy) for i, p, m in rows],
    )
    c.commit()
    total = c.execute("SELECT COUNT(*) FROM price_history").fetchone()[0]
    print(f"Snapshot {hoy}: {len(rows)} anuncios | total historico {total}")
    c.close()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Genera un resumen de todas las bases de catalogos scrapeados."""
import json
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUT = BASE.parent / "Data" / "catalogos_concesionarios"


def main():
    lines = ["# Resumen de catálogos scrapeados", "", "| Tienda | Filas | Con precio | Con modelo | Con imagen |", "|---|---:|---:|---:|---:|"]
    total = 0
    for db in sorted(OUT.glob("*.sqlite")):
        c = sqlite3.connect(db)
        n = c.execute("SELECT COUNT(*) FROM vehiculos").fetchone()[0]
        p = c.execute("SELECT COUNT(*) FROM vehiculos WHERE precio<>'' OR prices_json<>'[]'").fetchone()[0]
        m = c.execute("SELECT COUNT(*) FROM vehiculos WHERE modelo<>''").fetchone()[0]
        i = c.execute("SELECT COUNT(*) FROM vehiculos WHERE images_json<>'[]'").fetchone()[0]
        total += n
        lines.append(f"| {db.stem} | {n} | {p} | {m} | {i} |")
        c.close()
    lines += ["", f"**Total de páginas/fichas guardadas: {total}**", ""]
    (OUT / "resumen.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Resumen: {OUT / 'resumen.md'} (total {total})")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Reporte periodico de descarga/procesamiento. Lo ejecuta un timer cada 5 min."""
import sqlite3
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from db_chunks import ensure_db

PROJECT = Path(__file__).resolve().parents[2]
REV = PROJECT / "Data" / "Revolico"
MKTS = PROJECT / "Data" / "catalogos_concesionarios" / "marketplaces"
OUT = PROJECT / "Data" / "progreso_reporte.md"
ensure_db(REV / "pipeline_chunks/MANIFEST.json", REV / "pipeline.sqlite")


def count(db, table, where=""):
    try:
        c = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=10)
        n = c.execute(f"SELECT COUNT(*) FROM {table} {where}").fetchone()[0]
        c.close()
        return n
    except Exception:
        return -1


def active(unit):
    try:
        return subprocess.run(
            ["systemctl", "--user", "is-active", unit],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip()
    except Exception:
        return "?"


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [f"# Reporte de progreso — {ts}", ""]

    lines += ["## Revolico", "", "| Tabla / cola | Registros |", "|---|---:|"]
    for table in ("anuncios", "autos", "revision", "imagenes", "telefonos", "price_history"):
        lines.append(f"| revolico.sqlite : {table} | {count(REV/'revolico.sqlite', table)} |")
    for table in ("url_queue", "download_queue", "process_queue"):
        lines.append(f"| pipeline.sqlite : {table} | {count(REV/'pipeline.sqlite', table)} |")

    lines += ["", "### Colas por estado", ""]
    try:
        c = sqlite3.connect(f"file:{REV/'pipeline.sqlite'}?mode=ro", uri=True, timeout=10)
        for table in ("url_queue", "download_queue", "process_queue"):
            rows = c.execute(f"SELECT status, COUNT(*) FROM {table} GROUP BY status ORDER BY 2 DESC").fetchall()
            lines.append(f"- **{table}**: " + ", ".join(f"{s or 'null'}={n}" for s, n in rows))
        c.close()
    except Exception as e:
        lines.append(f"- Error: {e}")

    lines += ["", "## Marketplaces", "", "| Sitio | Anuncios | Comentarios | Vendedores |", "|---|---:|---:|---:|"]
    total = 0
    for db in sorted(MKTS.glob("*.sqlite")):
        na = count(db, "anuncios")
        total += max(na, 0)
        lines.append(
            f"| {db.stem} | {na} | {count(db, 'comentarios')} | {count(db, 'vendedores')} |"
        )
    lines += ["", f"**Total marketplaces: {total}**", ""]

    lines += ["## Servicios", ""]
    for u in ("revolico-revisar.service", "marketplaces-scrape.service", "revolico-snapshot.timer"):
        lines.append(f"- `{u}`: **{active(u)}**")

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Reporte actualizado: {OUT}")


if __name__ == "__main__":
    main()

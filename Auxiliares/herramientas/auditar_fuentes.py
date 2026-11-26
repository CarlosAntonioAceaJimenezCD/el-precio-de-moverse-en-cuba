#!/usr/bin/env python3
"""Auditoría de frescura de las fuentes: sitios propios, repos y oficiales."""
from __future__ import annotations

import ast
import sqlite3
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "Data/auditoria-fuentes-2026-11-23.md"
FECHA = datetime.now(timezone.utc).strftime("%d/%m/%Y")


def md(value: object) -> str:
    """Sanitiza texto para celdas de Markdown."""
    return str(value or "").replace("|", "\\|").replace("\n", " ").replace("`", "'")


def cargar_sites() -> dict:
    """Lee SITES del scraper sin ejecutar el módulo (sin dependencias de scraping)."""
    p = ROOT / "Auxiliares/herramientas/scrape_marketplaces.py"
    tree = ast.parse(p.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "SITES" for t in node.targets
        ):
            return ast.literal_eval(node.value)
    raise ValueError("SITES no encontrado en scrape_marketplaces.py")


def fetch(url: str, cabezales: bool = False) -> tuple[str, str]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            lm = r.headers.get("Last-Modified", "")
            if cabezales:
                return str(r.status), lm
            return str(r.status), r.read(200000).decode("utf-8", "replace")
    except Exception as e:
        return "ERR", str(e)[:90]


def fecha_max(db: Path, tabla: str, col: str) -> str:
    c = None
    try:
        c = sqlite3.connect(f"file:{db}?immutable=1", uri=True, timeout=10)
        v = c.execute(f"select max({col}) from {tabla}").fetchone()[0]
        return str(v)[:10] if v else "—"
    except Exception as e:
        print(f"AVISO {db.name}: {e}", file=sys.stderr)
        return "—"
    finally:
        if c is not None:
            c.close()


def filas(db: Path, tabla: str) -> int:
    c = None
    try:
        c = sqlite3.connect(f"file:{db}?immutable=1", uri=True, timeout=10)
        return c.execute(f"select count(*) from {tabla}").fetchone()[0]
    except Exception as e:
        print(f"AVISO {db.name}: {e}", file=sys.stderr)
        return -1
    finally:
        if c is not None:
            c.close()


def main() -> None:
    lineas = [
        f"# Auditoría de frescura de fuentes ({FECHA})", "",
        "Se consultan los sitios de origen y se comparan con la fecha más reciente guardada.",
        "HTTP `ERR` indica que el sitio no respondió desde este entorno; no implica que esté caído.", "",
        "## Marketplaces", "",
        "| Fuente | Semilla | HTTP | Última modificación | Anuncios BD | Último dato |", "|---|---|---|---|---:|---|",
    ]
    codigos = []
    sites = cargar_sites()
    for nombre, cfg in sorted(sites.items()):
        semilla = (cfg.get("seeds") or [""])[0]
        code, lm = fetch(semilla, cabezales=True) if semilla else ("—", "")
        codigos.append(code)
        db = ROOT / "Data/catalogos_concesionarios/marketplaces" / f"{nombre}.sqlite"
        lineas.append(
            f"| {md(nombre)} | {md(semilla[:60])} | {md(code)} | {md(lm[:25] or '—')} | "
            f"{filas(db,'anuncios')} | {md(fecha_max(db,'anuncios','scraped_at'))} |"
        )

    lineas += ["", "## Concesionarios", "",
               "| Fuente | BD | Filas | Último dato |", "|---|---|---:|---|"]
    for db in sorted((ROOT / "Data/catalogos_concesionarios").glob("*.sqlite")):
        lineas.append(f"| {md(db.stem)} | `{md(db.name)}` | {filas(db,'vehiculos')} | "
                      f"{md(fecha_max(db,'vehiculos','scraped_at'))} |")

    lineas += ["", "## Fuentes oficiales y complementarias", "",
               "| Fuente | URL | HTTP | Nota |", "|---|---|---|---|"]
    oficiales = {
        "ONEI anuario": "http://www.onei.gob.cu/cuba",
        "Gaceta Oficial": "https://www.gacetaoficial.gob.cu/es/gaceta-oficial-no-65-ordinaria-de-2026",
        "BCC tasas": "https://api.bc.gob.cu/v1/tasas-de-cambio/activas",
        "elTOQUE": "https://eltoque.com/tasas-de-cambio-cuba",
        "Womy": "https://womy.cu/cars/",
        "Clasificados.st": "https://cu.clasificados.st/motor",
        "TecnoTáctil": "https://www.tecnotactil.com/clasificados/mercado",
    }
    for nombre, url in oficiales.items():
        code, _ = fetch(url, cabezales=True)
        codigos.append(code)
        lineas.append(f"| {md(nombre)} | {md(url)} | {md(code)} | verificación {FECHA} |")

    lineas += ["", "## Repositorios cubanos", "",
               "| Repo | HEAD local | Commit remoto conocido | Cambios locales | Estado |", "|---|---|---|---:|---|"]
    base = ROOT / "Auxiliares/Repositorios Referencias"
    cuba = ["AppCubAutosScrapper_QMLQt", "AutosxCuba", "ICD-Mercado-Automotriz",
            "Mercado-automotriz", "Proyecto-Mercado-Automotriz", "autos-cuba", "scrapper_autos_electricos"]
    estados = []
    cambios_lista = []
    for nombre in cuba:
        d = base / nombre
        if not d.exists():
            continue
        local = subprocess.run(["git", "-C", str(d), "log", "-1", "--format=%h %cs"],
                               capture_output=True, text=True).stdout.strip()
        estado = subprocess.run(["git", "-C", str(d), "status", "-sb"],
                                capture_output=True, text=True).stdout.splitlines()
        status = estado[0] if estado else "(sin git)"
        cambios = len(subprocess.run(["git", "-C", str(d), "status", "--porcelain"],
                                     capture_output=True, text=True).stdout.splitlines())
        remoto = subprocess.run(["git", "-C", str(d), "log", "-1", "--format=%h %cs", "@{u}"],
                                capture_output=True, text=True).stdout.strip() or "—"
        estados.append(status)
        cambios_lista.append(cambios)
        lineas.append(f"| {md(nombre)} | {md(local)} | {md(remoto)} | {cambios} | {md(status)} |")

    atrasados = sum("[detrás" in s for s in estados)
    ok = sum(c == "200" for c in codigos)
    errores = sum(c == "ERR" for c in codigos)
    lineas += ["", "## Hallazgos calculados", "",
               f"- Fuentes web consultadas: {len(codigos)}; respondieron HTTP 200: {ok}; sin respuesta: {errores}.",
               f"- Repositorios cubanos revisados: {len(estados)}; con ref remoto atrasada: {atrasados}; "
               f"con cambios locales: {sum(1 for n in cambios_lista if n > 0)}.",
               "- Esta auditoría es de solo lectura: no se modificaron sitios, bases ni repositorios.", ""]
    OUT.write_text("\n".join(lineas), encoding="utf-8")
    print(f"escrito {OUT}")


if __name__ == "__main__":
    main()

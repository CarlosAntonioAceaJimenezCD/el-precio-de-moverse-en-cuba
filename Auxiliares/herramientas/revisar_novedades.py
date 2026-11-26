#!/usr/bin/env python3
"""Revisa las páginas ya conocidas y compara sus anuncios con la base guardada.

No modifica las BDs: solo reporta enlaces nuevos detectados en las primeras páginas.
"""
from __future__ import annotations

import ast
import re
import sqlite3
import unicodedata
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "Data/novedades-fuentes-2026-11-23.md"
DIA = datetime.now(timezone.utc).strftime("%d/%m/%Y")


def md(v: object) -> str:
    return str(v or "").replace("|", "\\|").replace("\n", " ")


def cargar_sites() -> dict:
    p = ROOT / "Auxiliares/herramientas/scrape_marketplaces.py"
    tree = ast.parse(p.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "SITES" for t in node.targets):
            return ast.literal_eval(node.value)
    raise ValueError("SITES no encontrado")


def norm(u: str) -> str:
    """Normaliza: sin www prefijo, query ordenada y Unicode NFC."""
    p = urllib.parse.urlsplit(u)
    host = (p.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    path = unicodedata.normalize("NFC", urllib.parse.unquote(p.path)).rstrip("/")
    q = "&".join(f"{k}={v}" for k, v in sorted(urllib.parse.parse_qsl(p.query, keep_blank_values=True)))
    return f"{p.scheme.lower()}://{host}{path}" + (f"?{q}" if q else "")


def es_agrupacion(url: str) -> bool:
    """Descarta páginas WebPage con muchos sub-enlaces (no son anuncios)."""
    html = pagina(url)
    if not html:
        return False
    if not re.search(r'"@type"\s*:\s*"WebPage"', html):
        return False
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
    titulo = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else ""
    return len(titulo.split()) <= 2 and not re.search(r"\d", titulo)


def guardados(db: Path) -> set[str]:
    c = sqlite3.connect(f"file:{db}?immutable=1", uri=True, timeout=10)
    try:
        return {norm(str(r[0])) for r in c.execute("select url from anuncios") if r[0]}
    finally:
        c.close()


def pagina(url: str) -> str:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read(600000).decode("utf-8", "replace")
    except Exception:
        return ""


def main() -> None:
    lineas = [
        f"# Novedades en fuentes ya conocidas ({DIA})", "",
        "Se descargan la primera y, cuando la fuente lo permite, la segunda página de listado de cada marketplace y se comparan sus enlaces con los guardados en las BDs.",
        "Un enlace «nuevo» significa que aparece hoy en la web pero no está en nuestra base; puede ser un anuncio reciente o uno que nunca se capturó.",
        "", "| Fuente | Páginas | Enlaces vistos | Nuevos | Ejemplos |", "|---|---:|---:|---:|---|",
    ]
    sites = cargar_sites()
    total_nuevos = 0
    for nombre, cfg in sorted(sites.items()):
        semilla = (cfg.get("seeds") or [""])[0]
        plantilla = cfg.get("page_template", "")
        patron = cfg.get("pattern", "")
        urls_pagina: set[str] = set()
        paginas_ok = 0
        if semilla and patron:
            for n in (1, 2):
                url = semilla if n == 1 else plantilla.format(page=n) if plantilla else ""
                if not url:
                    continue
                html = pagina(url)
                if not html:
                    continue
                paginas_ok += 1
                for href in re.findall(r"href=[\"']([^\"']+)[\"']", html, re.I):
                    if not href.startswith(("http://", "https://", "/")):
                        continue
                    if patron not in href and not re.search(patron, href):
                        continue
                    if re.search(r"publicar|contacto|mailto", href, re.I):
                        continue
                    urls_pagina.add(norm(urllib.parse.urljoin(url, href)))
        db = ROOT / "Data/catalogos_concesionarios/marketplaces" / f"{nombre}.sqlite"
        viejos = guardados(db)
        nuevos = sorted(u for u in urls_pagina if u not in viejos and not es_agrupacion(u))
        total_nuevos += len(nuevos)
        lineas.append(
            f"| {md(nombre)} | {paginas_ok} | {len(urls_pagina)} | {len(nuevos)} | "
            f"{md(' · '.join(nuevos[:2])[:120]) or '—'} |"
        )
    lineas += ["", "## Resultado", "",
               f"- Enlaces nuevos detectados en las primeras páginas: **{total_nuevos}**.",
               "- Las BDs no se modificaron; este informe es solo de detección.",
               "- Para incorporar los anuncios nuevos hay que ejecutar los scrapers completos.", ""]
    OUT.write_text("\n".join(lineas), encoding="utf-8")
    print(f"escrito {OUT} | nuevos={total_nuevos}")


if __name__ == "__main__":
    main()

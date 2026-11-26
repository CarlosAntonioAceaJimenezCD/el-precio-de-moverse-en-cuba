#!/usr/bin/env python3
"""Descarga completa de los trabajos utiles de DDG dentro de Hombros/.

Uso:
  .venv/bin/python herramientas/descargar_hombros.py

Salida:
  Hombros/01_PDFs/          documentos PDF completos
  Hombros/02_HTML/          paginas HTML completas + .txt legible
  Hombros/03_Repositorios/  clones --depth 1
  Hombros/04_Derivadas/     paginas derivadas del mismo dominio relacionadas con el proyecto
  Hombros/manifest.jsonl    registro de cada descarga
  Hombros/indice.md         ind legible
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

from curl_cffi import requests as creq

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ddg_research as d  # noqa: E402

BASE = Path(__file__).resolve().parents[1]
PROJECT = BASE.parent
HOMBROS = PROJECT / "Hombros"
DB = BASE / "cache" / "ddg.sqlite"
QUERY = "mercado automovilistico trabajos investigativos"

PDFS = HOMBROS / "01_PDFs"
HTMLS = HOMBROS / "02_HTML"
REPOS = HOMBROS / "03_Repositorios"
DERIV = HOMBROS / "04_Derivadas"

AUTO = re.compile(
    r"automovil|automóvil|automotriz|automoción|automocion|veh[ií]culo|carro|coche|"
    r"moto|movilidad|parque automotor|concesionario|repuesto|neumático|transporte",
    re.I,
)
RELAX_HOSTS = (
    ".edu", ".gob.", ".ac.cr", ".org.", "researchgate.net", "academia.edu",
    "dialnet.unirioja.es", "scielo", "redalyc.org", "elsevier.es", "repositorio",
    "dspace", "zaguan", "riunet", "uvadoc", "bibdigital", "comillas.edu",
    "uchile.cl", "unam.mx", "ups.edu.ec", "unt.edu.ar", "uva.es", "upm.es",
    "upv.es", "unizar.es", "icex.es", "mintur.gob.es", "mincotur.gob.es",
    "anfac.com", "sernauto.es", "inegi.org.mx", "kimuk.conare.ac.cr",
    "github.com", "oica.net", "cnmc.es", "banrep.gov.co", "ilo.org", "undp.org",
)


def safe_name(title: str, url: str, ext: str) -> str:
    t = re.sub(r"\s+", " ", (title or "").strip())
    t = re.sub(r"[^A-Za-z0-9ÁÉÍÓÚáéíóúñüÜ ._-]+", "", t)[:85].strip(" ._-") or "documento"
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    return f"{t}__{h}{ext}"


def candidates(query: str):
    import sqlite3

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT page,title,url,snippet FROM results WHERE qhash=? ORDER BY page,position",
        (d.qhash(query),),
    ).fetchall()
    out, seen = [], set()
    for r in rows:
        url = r["url"]
        title = r["title"] or ""
        host, path = d.norm_url(url)
        if not url or url in seen:
            continue
        if d.is_noise(title, url):
            continue
        if path.lower().endswith(".pdf") or any(m in host for m in RELAX_HOSTS):
            if AUTO.search(title + " " + unquote(path) + " " + (r["snippet"] or "")):
                seen.add(url)
                out.append({"page": r["page"], "title": title, "url": url, "origin": "principal"})
    return out


def fetch(session, url: str, tries: int = 2):
    last = ""
    for i in range(tries):
        try:
            r = session.get(url, timeout=40, allow_redirects=True)
            if r.status_code == 200:
                return r
            last = f"HTTP {r.status_code}"
        except Exception as e:
            last = str(e)
        time.sleep(2 + 3 * i)
    raise RuntimeError(last)


def save_binary(rec: dict, r, folder: Path, ext: str) -> Path:
    data = r.content or b""
    if len(data) > 40_000_000:
        raise RuntimeError(f"archivo demasiado grande: {len(data)} bytes")
    if ext == ".pdf" and not data.lstrip()[:5].startswith(b"%PDF"):
        ext = ".html"
    path = folder / safe_name(rec["title"], rec["url"], ext)
    path.write_bytes(data)
    return path


def save_html(rec: dict, r, folder: Path) -> Path:
    path = folder / safe_name(rec["title"], rec["url"], ".html")
    path.write_text(r.text or "", encoding="utf-8", errors="ignore")
    try:
        import trafilatura

        text = trafilatura.extract(r.text or "", include_comments=False) or ""
        if text:
            path.with_suffix(".txt").write_text(text, encoding="utf-8", errors="ignore")
    except Exception:
        pass
    return path


def derive_links(rec: dict, html: str, host: str, already: set[str]) -> list[dict]:
    """Paginas del mismo dominio enlazadas desde el resultado y relacionadas con el proyecto."""
    if not html:
        return []
    soup = d.BeautifulSoup(html, "lxml")
    out = []
    seen = set()
    base = rec["url"]
    for a in soup.find_all("a", href=True):
        label = a.get_text(" ", strip=True)[:120]
        href = urljoin(base, a["href"])
        if href in seen or href in already:
            continue
        h2, p2 = d.norm_url(href)
        if h2 != host or not AUTO.search(label + " " + unquote(p2)):
            continue
        if p2.lower().endswith(("#", "?")) or not p2:
            continue
        seen.add(href)
        out.append(
            {
                "page": rec["page"],
                "title": label or f"Derivada de {host}",
                "url": href,
                "origin": f"derivada de {rec['title'][:50]}",
            }
        )
        if len(out) >= 4:
            break
    return out


def main() -> int:
    global QUERY, HOMBROS, PDFS, HTMLS, REPOS, DERIV
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", default=QUERY)
    ap.add_argument("--out", type=Path, default=HOMBROS)
    ap.add_argument("--no-derive", action="store_true")
    a = ap.parse_args()

    QUERY = a.query
    HOMBROS = a.out
    PDFS = HOMBROS / "01_PDFs"
    HTMLS = HOMBROS / "02_HTML"
    REPOS = HOMBROS / "03_Repositorios"
    DERIV = HOMBROS / "04_Derivadas"
    for folder in (PDFS, HTMLS, REPOS, DERIV):
        folder.mkdir(parents=True, exist_ok=True)
    session = creq.Session(impersonate="chrome")
    session.headers.update({"Accept-Language": "es-ES,es;q=0.9,en;q=0.8"})

    base_list = candidates(QUERY)
    print(f"Consulta: {QUERY}", flush=True)
    print(f"Candidatos principales: {len(base_list)}", flush=True)
    manifest: list[dict] = []
    already = {x["url"] for x in base_list}
    derived: list[dict] = []

    for i, rec in enumerate(base_list, 1):
        url = rec["url"]
        if "github.com" in url and "jmev1/TFG-2026" in url:
            dest = REPOS / "TFG-2026"
            if not dest.exists():
                try:
                    subprocess.run(
                        ["git", "clone", "--depth", "1", "https://github.com/jmev1/TFG-2026.git", str(dest)],
                        check=True,
                        timeout=180,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                    )
                    status, path, bytes_ = "ok", str(dest), None
                except Exception as e:
                    status, path, bytes_, rec["error"] = "fail", "", 0, str(e)
            else:
                status, path, bytes_ = "ok", str(dest), None
            manifest.append({**rec, "status": status, "path": path, "bytes": bytes_})
            print(f"[{i:03d}] REPO {status} {url[:80]}", flush=True)
            continue
        # Reanudacion: si el archivo ya existe, no se vuelve a descargar.
        cached = None
        for ext, folder in ((".pdf", PDFS), (".html", HTMLS)):
            p = folder / safe_name(rec["title"], rec["url"], ext)
            if p.exists() and p.stat().st_size > 0:
                cached = (p, ext)
                break
        if cached:
            p, ext = cached
            manifest.append(
                {
                    **rec,
                    "status": "ok",
                    "path": str(p),
                    "bytes": p.stat().st_size,
                    "kind": ext.lstrip("."),
                    "final_url": url,
                    "cached": True,
                }
            )
            print(f"[{i:03d}] CACHE {ext} {rec['title'][:60]}", flush=True)
            continue
        try:
            r = fetch(session, url)
            ctype = (r.headers.get("content-type") or "").lower()
            path = d.norm_url(url)[1].lower()
            if "pdf" in ctype or path.endswith(".pdf"):
                f = save_binary(rec, r, PDFS, ".pdf")
                kind = "pdf"
            else:
                f = save_html(rec, r, HTMLS)
                kind = "html"
                h, p = d.norm_url(url)
                derived.extend(derive_links(rec, r.text or "", h, already))
            manifest.append(
                {
                    **rec,
                    "status": "ok",
                    "path": str(f),
                    "bytes": len(r.content or b""),
                    "kind": kind,
                    "final_url": str(r.url),
                }
            )
            print(f"[{i:03d}] {kind.upper():4} {len(r.content or b''):>8} {rec['title'][:60]}", flush=True)
        except Exception as e:
            manifest.append({**rec, "status": "fail", "path": "", "bytes": 0, "error": str(e)})
            print(f"[{i:03d}] FAIL {rec['title'][:60]} :: {e}", flush=True)
        time.sleep(0.8)

    # Descargar paginas derivadas relacionadas (maximo 4 por pagina padre).
    if a.no_derive:
        derived = []
    print(f"Derivadas detectadas: {len(derived)}", flush=True)
    dcount = 0
    for rec in derived:
        if rec["url"] in already:
            continue
        already.add(rec["url"])
        cached = None
        for ext, folder in ((".pdf", DERIV), (".html", DERIV)):
            p = folder / safe_name(rec["title"], rec["url"], ext)
            if p.exists() and p.stat().st_size > 0:
                cached = (p, ext)
                break
        if cached:
            p, ext = cached
            manifest.append(
                {
                    **rec,
                    "status": "ok",
                    "path": str(p),
                    "bytes": p.stat().st_size,
                    "kind": ext.lstrip("."),
                    "final_url": rec["url"],
                    "cached": True,
                }
            )
            dcount += 1
            continue
        try:
            r = fetch(session, rec["url"], tries=2)
            ctype = (r.headers.get("content-type") or "").lower()
            path = d.norm_url(rec["url"])[1].lower()
            if "pdf" in ctype or path.endswith(".pdf"):
                f = save_binary(rec, r, DERIV, ".pdf")
                kind = "pdf"
            else:
                f = save_html(rec, r, DERIV)
                kind = "html"
            manifest.append(
                {
                    **rec,
                    "status": "ok",
                    "path": str(f),
                    "bytes": len(r.content or b""),
                    "kind": kind,
                    "final_url": str(r.url),
                }
            )
            dcount += 1
        except Exception as e:
            manifest.append({**rec, "status": "fail", "path": "", "bytes": 0, "error": str(e)})
        time.sleep(0.6)
    print(f"Derivadas descargadas: {dcount}", flush=True)

    with (HOMBROS / "manifest.jsonl").open("w", encoding="utf-8") as f:
        for m in manifest:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")

    ok = [m for m in manifest if m["status"] == "ok"]
    fail = [m for m in manifest if m["status"] != "ok"]
    lines = [
        "# Hombros — trabajos investigativos descargados",
        "",
        f"Consulta DDG: `{QUERY}`",
        f"Total intentos: {len(manifest)} | OK: {len(ok)} | Fallos: {len(fail)}",
        f"PDFs: {sum(1 for m in ok if m.get('kind') == 'pdf')} | "
        f"HTML: {sum(1 for m in ok if m.get('kind') == 'html')} | "
        f"Repos: {sum(1 for m in ok if 'TFG-2026' in str(m.get('path', '')))}",
        "",
        "## Descargados",
        "",
    ]
    for m in ok:
        lines.append(f"- P{m['page']:02d} [{m.get('kind', 'repo')}] **{m['title'][:100]}** — `{m['path']}` — {m['url']}")
    lines += ["", "## No descargados", ""]
    for m in fail:
        lines.append(f"- P{m['page']:02d} **{m['title'][:90]}** — {m['url']} — `{str(m.get('error', ''))[:120]}`")
    (HOMBROS / "indice.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Indice: {HOMBROS / 'indice.md'}")
    print(f"OK={len(ok)} FAIL={len(fail)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

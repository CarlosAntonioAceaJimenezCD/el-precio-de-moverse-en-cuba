#!/usr/bin/env python3
"""Registra altas nuevas del proyecto en INFORME_TECNICO.md y regenera el PDF.

Uso:
    python actualizar_informe.py            # registra novedades y regenera el PDF
    python actualizar_informe.py --inicializar   # crea la línea base sin registrar
    python actualizar_informe.py --regenerar     # solo regenera el PDF

El estado se guarda en .informe_state.json junto a este script.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MD = ROOT / "INFORME_TECNICO.md"
PDF = ROOT / "INFORME_TECNICO.pdf"
STATE = Path(__file__).with_name(".informe_state.json")
MARKER = "<!-- REGISTRO_ALTAS -->"
MAX_ROWS = 200

EXCLUDED_DIRS = {
    ".git", ".venv", "__pycache__", "node_modules", "Copias",
    ".idea", ".vscode", ".pytest_cache", ".mypy_cache",
}
EXCLUDED_FILES = {PDF.name, STATE.name, "revolico.sqlite", ".revolico_sync.lock"}
ANEXOS_ALLOWED = {
    "Anexos/Leyes/gaceta_catalog.json",
    "Anexos/Leyes/.herramientas/descargar_gaceta.py",
}


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_excluded(path: Path) -> bool:
    rel = relative(path)
    if rel.split("/", 1)[0] == "Anexos" and rel not in ANEXOS_ALLOWED:
        return True
    # Archivos generados por el timer de Revolico: se documentan en una sola fila.
    if rel == "Data/Revolico/estado.json" or "/partes/" in rel:
        return True
    return False


def repo_origin(directory: Path) -> str | None:
    config = directory / ".git" / "config"
    if not config.is_file():
        return None
    try:
        text = config.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    match = re.search(r"^\s*url\s*=\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def manifest_origins() -> dict[str, str]:
    result: dict[str, str] = {}
    for manifest in ROOT.glob("Hombros/**/manifest.jsonl"):
        try:
            for line in manifest.read_text(encoding="utf-8", errors="replace").splitlines():
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if row.get("path") and row.get("url"):
                    result[str(Path(row["path"]).resolve())] = str(row["url"])
                    try:
                        result[relative(Path(row["path"]))] = str(row["url"])
                    except ValueError:
                        pass
        except OSError:
            continue
    return result


def phase_for(rel: str) -> str:
    if rel.split("/", 1)[0] in {"README.md", "INFORME_TECNICO.md", ".gitignore"}:
        return "9 / 9"
    if rel.startswith("Anexos/"):
        return "1 / 1"
    if rel.startswith("Auxiliares/"):
        return "3 / 3"
    if rel.startswith("Hombros/"):
        return "4 / 4"
    if rel.startswith("Data/catalogos_concesionarios/"):
        return "6 / 6"
    if rel.startswith("Data/"):
        return "2 / 2"
    return "7 / 7"


def kind_for(path: Path) -> str:
    if (path / ".git").exists():
        return "repositorio / repo"
    suffix = path.suffix.lower() if path.is_file() else ""
    return {
        ".md": "documento / document",
        ".py": "script / script",
        ".pdf": "PDF / PDF",
        ".csv": "datos / data",
        ".json": "datos / data",
        ".sqlite": "base de datos / database",
        ".html": "HTML / HTML",
        ".ipynb": "notebook / notebook",
        ".txt": "texto / text",
    }.get(suffix, "archivo / file" if path.is_file() else "carpeta / folder")


def description_for(path: Path) -> str:
    if path.is_dir():
        return "Carpeta añadida al proyecto / Folder added to the project"
    suffix = path.suffix.lower()
    if suffix in {".md", ".txt"}:
        try:
            for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
                cleaned = line.strip().lstrip("#").strip()
                if cleaned:
                    return cleaned[:160]
        except OSError:
            pass
    if suffix == ".py":
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
            match = re.search(r'"""(.*?)"""', text, re.DOTALL)
            if match:
                first = next((l.strip() for l in match.group(1).splitlines() if l.strip()), "")
                if first:
                    return first[:160]
        except OSError:
            pass
    return "Añadido al proyecto; pendiente de descripción / Added; description pending"


def size_for(path: Path) -> str:
    if path.is_file():
        try:
            value = path.stat().st_size
        except OSError:
            return "—"
        return f"{value:,} B".replace(",", " ")
    try:
        count = sum(1 for _ in path.iterdir())
    except OSError:
        count = 0
    return f"carpeta / folder ({count} entradas)"


def signature(path: Path) -> str:
    if path.is_file():
        stat = path.stat()
        return f"f:{stat.st_size}:{int(stat.st_mtime)}"
    try:
        entries = sorted(
            p.name for p in path.iterdir()
            if p.name not in EXCLUDED_DIRS and p.name not in EXCLUDED_FILES
        )
    except OSError:
        entries = []
    return "d:" + "|".join(entries)


def scan() -> dict[str, tuple[str, str]]:
    found: dict[str, tuple[str, str]] = {}

    def visit(directory: Path) -> None:
        for child in sorted(directory.iterdir(), key=lambda p: p.name):
            if child.name in EXCLUDED_DIRS or child.name in EXCLUDED_FILES:
                continue
            if child.name.endswith(("-journal", "-wal", "-shm")):
                continue
            try:
                rel = relative(child)
            except ValueError:
                continue
            if is_excluded(child):
                continue
            if child.is_dir() and (child / ".git").exists():
                origin = repo_origin(child) or "—"
                found[rel] = (signature(child), origin)
                continue
            found[rel] = (signature(child), "")
            if child.is_dir():
                visit(child)

    visit(ROOT)
    return found


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def make_rows(items: list[tuple[str, tuple[str, str], str, str]]) -> list[str]:
    today = datetime.now().strftime("%Y-%m-%d")
    origins = manifest_origins()
    rows = []
    for rel, (_sig, origin), status in items:
        path = ROOT / rel
        source = origin or origins.get(rel) or origins.get(str(path.resolve())) or "—"
        rows.append(
            "| {date} | `{rel}` | {kind} | {source} | {size} | {phase} | {desc} | {status} |".format(
                date=today,
                rel=escape_cell(rel),
                kind=escape_cell(kind_for(path)),
                source=escape_cell(source[:160]),
                size=escape_cell(size_for(path)),
                phase=phase_for(rel),
                desc=escape_cell(description_for(path)),
                status=status,
            )
        )
    return rows


def append_to_markdown(rows: list[str]) -> None:
    text = MD.read_text(encoding="utf-8")
    if MARKER not in text:
        raise RuntimeError(f"No se encontró el marcador {MARKER} en {MD}")
    insertion = "\n".join(rows) + "\n"
    text = text.replace(MARKER, MARKER + "\n" + insertion, 1)
    MD.write_text(text, encoding="utf-8")


def inline_html(text: str) -> str:
    import html as html_lib

    value = html_lib.escape(text)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", value)
    return value


def simple_markdown_to_html(source: str) -> str:
    """Conversor mínimo sin dependencias externas (encabezados, tablas, listas y código)."""
    lines = source.splitlines()
    out: list[str] = []
    i = 0
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            out.append("<p>" + inline_html(" ".join(paragraph)) + "</p>")
            paragraph.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_paragraph()
            i += 1
            code: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            out.append("<pre><code>" + "\n".join(code).replace("&", "&amp;").replace("<", "&lt;") + "</code></pre>")
            continue

        if not stripped:
            flush_paragraph()
            i += 1
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            flush_paragraph()

            def cells(row: str) -> list[str]:
                return [c.strip() for c in row.strip().strip("|").split("|")]

            headers = cells(stripped)
            i += 2
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(cells(lines[i]))
                i += 1
            out.append("<table><thead><tr>" + "".join(f"<th>{inline_html(c)}</th>" for c in headers) + "</tr></thead>")
            out.append("<tbody>" + "".join("<tr>" + "".join(f"<td>{inline_html(c)}</td>" for c in row) + "</tr>" for row in rows) + "</tbody></table>")
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            out.append(f"<h{level}>{inline_html(heading.group(2))}</h{level}>")
            i += 1
            continue

        if re.match(r"^---+$", stripped):
            flush_paragraph()
            out.append("<hr>")
            i += 1
            continue

        if stripped.startswith("- "):
            flush_paragraph()
            items: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(lines[i].strip()[2:])
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline_html(item)}</li>" for item in items) + "</ul>")
            continue

        paragraph.append(stripped)
        i += 1

    flush_paragraph()
    return "\n".join(out)


def regenerate_pdf() -> None:
    source = MD.read_text(encoding="utf-8")
    try:
        import markdown  # type: ignore

        body = markdown.markdown(source, extensions=["tables", "fenced_code", "toc"])
    except ImportError:
        body = simple_markdown_to_html(source)
    html = (
        '<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">'
        "<style>"
        "body{font-family:'DejaVu Sans',sans-serif;font-size:10pt;line-height:1.35;}"
        "table{border-collapse:collapse;width:100%;}td,th{border:1px solid #999;padding:3px;font-size:8pt;}"
        "h1{font-size:18pt;}h2{font-size:14pt;margin-top:18pt;}code{font-size:8pt;}"
        "</style></head><body>" + body + "</body></html>"
    )
    with tempfile.TemporaryDirectory(prefix="informe_pdf_") as tmp:
        html_path = Path(tmp) / "INFORME_TECNICO.html"
        html_path.write_text(html, encoding="utf-8")
        profile = Path(tmp) / "lo_profile"
        command = [
            "libreoffice",
            f"-env:UserInstallation=file://{profile}",
            "--headless",
            "--convert-to", "pdf",
            "--outdir", str(ROOT),
            str(html_path),
        ]
        result = subprocess.run(command, capture_output=True, text=True, timeout=180)
        if result.returncode != 0 or not PDF.exists():
            raise RuntimeError(result.stderr or result.stdout or "LibreOffice no generó el PDF")


def save_state(state: dict[str, tuple[str, str]]) -> None:
    payload = {rel: {"signature": sig, "origin": origin} for rel, (sig, origin) in state.items()}
    STATE.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def load_state() -> dict[str, tuple[str, str]]:
    if not STATE.exists():
        return {}
    data = json.loads(STATE.read_text(encoding="utf-8"))
    return {rel: (val["signature"], val.get("origin", "")) for rel, val in data.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inicializar", action="store_true", help="crear línea base sin registrar altas")
    parser.add_argument("--regenerar", action="store_true", help="solo regenerar el PDF")
    args = parser.parse_args()

    if args.regenerar:
        regenerate_pdf()
        print(f"PDF regenerado: {PDF}")
        return

    previous = load_state()
    current = scan()

    if args.inicializar or not previous:
        save_state(current)
        print(f"Línea base creada con {len(current)} entradas. No se añadieron registros.")
        if not args.inicializar:
            regenerate_pdf()
            print(f"PDF generado: {PDF}")
        return

    new_items: list[tuple[str, tuple[str, str], str]] = []
    for rel, value in current.items():
        if rel not in previous:
            new_items.append((rel, value, "Añadido / Added"))
        elif previous[rel][0] != value[0]:
            new_items.append((rel, value, "Actualizado / Updated"))

    if new_items:
        truncated = len(new_items) > MAX_ROWS
        selected = new_items[:MAX_ROWS]
        append_to_markdown(make_rows(selected))
        if truncated:
            note = [f"| {datetime.now():%Y-%m-%d} | … | aviso / notice | — | — | — | "
                    f"{len(new_items) - MAX_ROWS} entradas adicionales no listadas / omitted | "
                    "Pendiente / Pending |"]
            append_to_markdown(note)
        print(f"Se registraron {len(selected)} altas en {MD.name}")
    else:
        print("No hay altas nuevas.")

    save_state(current)
    regenerate_pdf()
    print(f"PDF actualizado: {PDF}")


if __name__ == "__main__":
    main()

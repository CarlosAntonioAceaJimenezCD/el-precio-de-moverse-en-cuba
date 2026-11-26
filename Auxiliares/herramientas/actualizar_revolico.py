#!/usr/bin/env python3
"""Actualización incremental de la BD de Revolico y subida por partes a Git.

Cada ejecución:
  1. Corre el scraper incremental (solo anuncios nuevos).
  2. Divide revolico.sqlite en partes de 16 MiB, reemplazando solo las que cambiaron.
  3. Escribe Data/Revolico/estado.json con hash, tamaño y timestamp.
  4. Actualiza una única fila del informe técnico y regenera el PDF.
  5. Commitea y pushea solo los archivos cambiados.

La BD completa NO se versiona como un solo archivo: queda en Data/Revolico/partes/
y se reconstruye con reconstruir_revolico.py.
"""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUX = ROOT / "Auxiliares"
OUT = ROOT / "Data/Revolico"
DB = OUT / "revolico.sqlite"
PARTS = OUT / "partes"
STATE = OUT / "estado.json"
MD = ROOT / "INFORME_TECNICO.md"
VENV_PY = AUX / ".venv/bin/python"
SCRAPER = AUX / "herramientas/scrape_revolico.py"
UPDATE_REPORT = AUX / "herramientas/actualizar_informe.py"
CHUNK = 16 * 1024 * 1024
MARKER = "<!-- SYNC_REVOLICO -->"


def run(cmd: list[str], cwd: Path | None = None) -> int:
    env = dict(os.environ)
    env["GIT_TERMINAL_PROMPT"] = "0"
    result = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
    if result.returncode != 0:
        print((result.stderr or result.stdout)[-2000:], flush=True)
    return result.returncode


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_state() -> dict:
    if STATE.is_file():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def split_database() -> dict:
    if not DB.is_file():
        raise RuntimeError(f"No existe la base de datos: {DB}")

    PARTS.mkdir(parents=True, exist_ok=True)
    old = load_state()
    new_db_hash = sha256_file(DB)
    size = DB.stat().st_size

    # Usar el mismo filesystem que OUT: /tmp es tmpfs pequeño y se agota.
    with tempfile.TemporaryDirectory(prefix="revolico_parts_", dir=OUT) as tmp:
        tmpdir = Path(tmp)
        hashes: list[str] = []
        index = 0
        with DB.open("rb") as handle:
            while True:
                block = handle.read(CHUNK)
                if not block:
                    break
                index += 1
                name = f"revolico.sqlite.part{index:03d}"
                target = tmpdir / name
                target.write_bytes(block)
                hashes.append(sha256_file(target))

        previous = {entry["sha256"]: entry["name"] for entry in old.get("parts", [])}
        kept: list[dict] = []
        for position, digest in enumerate(hashes, start=1):
            name = f"revolico.sqlite.part{position:03d}"
            final = PARTS / name
            if digest in previous and (PARTS / previous[digest]).is_file():
                source = PARTS / previous[digest]
                if source != final:
                    shutil.move(str(source), str(final))
            else:
                shutil.move(str(tmpdir / name), str(final))
            kept.append({"name": name, "sha256": digest, "orden": position})

        wanted = {entry["name"] for entry in kept}
        for existing in PARTS.glob("revolico.sqlite.part*"):
            if existing.name not in wanted:
                existing.unlink()

    state = {
        "actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "db_bytes": size,
        "db_sha256": new_db_hash,
        "tamano_parte": CHUNK,
        "partes": kept,
        "sin_cambios": old.get("db_sha256") == new_db_hash,
    }
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return state


def update_report(state: dict) -> None:
    # Bloqueo compartido con sincronizar_github.py para no escribir el informe
    # mientras Git está haciendo commit/push del mismo archivo.
    lock = (OUT / ".revolico_sync.lock").open("w")
    fcntl.flock(lock, fcntl.LOCK_EX)
    text = MD.read_text(encoding="utf-8")
    if MARKER not in text:
        print("Aviso: marcador SYNC_REVOLICO no encontrado; no se actualizó el informe", flush=True)
        return
    parts = state["partes"]
    row = (
        "| {ts} | {bytes} B | {n} partes de 16 MiB | `{hash}` | Reconstruir con "
        "`reconstruir_revolico.py` / Rebuild with `reconstruir_revolico.py` |".format(
            ts=state["actualizado_utc"],
            bytes=state["db_bytes"],
            n=len(parts),
            hash=state["db_sha256"][:16] + "…",
        )
    )
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == MARKER:
            if i + 1 < len(lines) and lines[i + 1].startswith("|"):
                lines[i + 1] = row
            else:
                lines.insert(i + 1, row)
            break
    MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    run([str(VENV_PY), str(UPDATE_REPORT), "--regenerar"], cwd=ROOT)
    lock.close()


def git_sync() -> int:
    targets = ["Data/Revolico/partes", "Data/Revolico/estado.json", "INFORME_TECNICO.md", "INFORME_TECNICO.pdf"]
    run(["git", "add", "--", *targets], cwd=ROOT)
    check = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT)
    if check.returncode == 0:
        print("Sin cambios que subir.", flush=True)
        return 0
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    run(["git", "commit", "-m", f"data(revolico): actualización incremental {stamp}"], cwd=ROOT)
    return run(["git", "push", "origin", "main"], cwd=ROOT)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    print("== Revolico scrape/split ==", flush=True)

    rc = run([str(VENV_PY), str(SCRAPER), "--no-pages", "--workers", "10"], cwd=AUX)
    print(f"Scraper exit={rc}", flush=True)

    state = split_database()
    print(
        f"BD={state['db_bytes']} B hash={state['db_sha256'][:12]} "
        f"partes={len(state['partes'])} sin_cambios={state['sin_cambios']}",
        flush=True,
    )
    update_report(state)
    print("Datos preparados; el push lo hace revolico-git.timer", flush=True)


if __name__ == "__main__":
    main()

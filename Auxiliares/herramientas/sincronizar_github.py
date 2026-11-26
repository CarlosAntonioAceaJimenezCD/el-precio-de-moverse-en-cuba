#!/usr/bin/env python3
"""Sincroniza con GitHub SOLO los archivos del proyecto ya definidos.

Lo ejecuta `revolico-git.timer` cada 10 minutos. No scrapeado, no divisiones:
únicamente git add/commit/push de las rutas acordadas. Comparte el bloqueo
`.revolico_sync.lock` con `actualizar_revolico.py` para no escribir el informe
mientras se hace commit.
"""

from __future__ import annotations

import fcntl
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOCK = ROOT / "Data/Revolico/.revolico_sync.lock"
TARGETS = [
    "README.md",
    "INFORME_TECNICO.md",
    "INFORME_TECNICO.pdf",
    ".gitignore",
    "Auxiliares/herramientas",
    "Data/Revolico/partes",
    "Data/Revolico/estado.json",
    "Data/integraciones",
    "Anexos/Investigacion Cambios",
    "Anexos/Investigacion Combustible",
    "Anexos/Leyes/gaceta_catalog.json",
    "Anexos/Leyes/.herramientas",
]


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)


def main() -> None:
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    lock = LOCK.open("w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print("Otra tarea tiene el lock; se omite este ciclo de Git.", flush=True)
        return

    #git add falla si alguna ruta aún no existe (p. ej. `partes` antes del primer split).
    existentes = [t for t in TARGETS if (ROOT / t).exists()]
    add = git("add", "--", *existentes)
    if add.returncode != 0:
        print(add.stderr[-1000:], flush=True)
        return

    if git("diff", "--cached", "--quiet").returncode == 0:
        print("Sin cambios para subir.", flush=True)
    else:
        stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        commit = git("commit", "-m", f"data(revolico): sincronización automática {stamp}")
        print((commit.stdout or commit.stderr)[-600:], flush=True)
        push = git("push", "origin", "main")
        print((push.stdout or push.stderr)[-600:], flush=True)
    lock.close()


if __name__ == "__main__":
    main()

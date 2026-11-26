#!/usr/bin/env python3
"""Reconstruye revolico.sqlite a partir de las partes versionadas en Git."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "Data/Revolico"
PARTS = OUT / "partes"
STATE = OUT / "estado.json"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--salida",
        type=Path,
        default=OUT / "revolico.sqlite.reconstruido",
        help="archivo de destino",
    )
    parser.add_argument(
        "--sobrescribir",
        action="store_true",
        help="reemplazar Data/Revolico/revolico.sqlite",
    )
    args = parser.parse_args()

    state = json.loads(STATE.read_text(encoding="utf-8"))
    destino = OUT / "revolico.sqlite" if args.sobrescribir else args.salida

    digest = hashlib.sha256()
    total = 0
    with destino.open("wb") as salida:
        for entry in sorted(state["partes"], key=lambda e: e["orden"]):
            parte = PARTS / entry["name"]
            if not parte.is_file():
                raise SystemExit(f"Falta la parte: {parte}")
            block = parte.read_bytes()
            if hashlib.sha256(block).hexdigest() != entry["sha256"]:
                raise SystemExit(f"Hash inválido en {parte}")
            salida.write(block)
            digest.update(block)
            total += len(block)

    result = digest.hexdigest()
    if result != state["db_sha256"]:
        raise SystemExit(f"Hash final incorrecto: {result} != {state['db_sha256']}")
    if total != state["db_bytes"]:
        raise SystemExit(f"Tamaño incorrecto: {total} != {state['db_bytes']}")

    print(f"OK: {destino} ({total} bytes, sha256={result})")


if __name__ == "__main__":
    main()

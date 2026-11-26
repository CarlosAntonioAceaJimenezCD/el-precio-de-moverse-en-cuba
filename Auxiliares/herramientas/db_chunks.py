#!/usr/bin/env python3
"""Divide un archivo grande en chunks y lo reconstruye con verificación.

Uso:
    python db_chunks.py split  ORIGEN DESTINO_CHUNKS [MB]
    python db_chunks.py assemble MANIFEST.json DESTINO [--force]
    python db_chunks.py verify MANIFEST.json

Los chunks se numeran desde 0 y el manifiesto guarda tamaño y SHA-256 de cada
uno más el del archivo completo, para poder reanudar una subida interrumpida:
solo faltarán los chunks ausentes en el remoto.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
from pathlib import Path

DEFAULT_CHUNK_MB = 10
CHUNK_PREFIX = "chunk_"


def sha256_file(path: Path, chunk_size: int = 4 * 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while True:
            b = fh.read(chunk_size)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def split(source: Path, dest: Path, chunk_mb: int = DEFAULT_CHUNK_MB) -> Path:
    if not source.exists():
        raise SystemExit(f"No existe el archivo: {source}")
    size = chunk_mb * 1024 * 1024
    dest.mkdir(parents=True, exist_ok=True)
    manifest = {
        "source": source.name,
        "source_size": source.stat().st_size,
        "source_sha256": sha256_file(source),
        "chunk_size": size,
        "chunk_count": 0,
        "chunks": [],
    }
    with source.open("rb") as fh:
        while True:
            data = fh.read(size)
            if not data:
                break
            i = manifest["chunk_count"]
            name = f"{CHUNK_PREFIX}{i:04d}.bin"
            out = dest / name
            if not (out.exists() and out.stat().st_size == len(data)):
                tmp = out.with_suffix(".tmp")
                tmp.write_bytes(data)
                os.replace(tmp, out)
            manifest["chunks"].append(
                {"index": i, "name": name, "offset": i * size,
                 "size": len(data), "sha256": hashlib.sha256(data).hexdigest()}
            )
            manifest["chunk_count"] += 1
            print(f"chunk {i:04d}: {len(data)/1e6:.2f} MB -> {name}")
    path = dest / "MANIFEST.json"
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"manifiesto: {path} | {manifest['chunk_count']} chunks")
    return path


def load_manifest(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def verify(manifest_path: Path) -> bool:
    m = load_manifest(manifest_path)
    root = manifest_path.parent
    ok = True
    for c in m["chunks"]:
        p = root / c["name"]
        if not p.exists():
            print(f"FALTA {c['name']}")
            ok = False
            continue
        h = sha256_file(p)
        if h != c["sha256"] or p.stat().st_size != c["size"]:
            print(f"CORRUPTO {c['name']}")
            ok = False
    print(f"verificación: {'OK' if ok else 'FALLÓ'} ({len(m['chunks'])} chunks)")
    return ok


def assemble(manifest_path: Path, target: Path, force: bool = False) -> Path:
    if target.exists() and not force:
        raise SystemExit(f"El destino ya existe (usa --force para reemplazar): {target}")
    if not verify(manifest_path):
        raise SystemExit("No se puede reconstruir: hay chunks ausentes o corruptos")
    m = load_manifest(manifest_path)
    root = manifest_path.parent
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    with tmp.open("wb") as out:
        for c in m["chunks"]:
            out.write((root / c["name"]).read_bytes())
    h = sha256_file(tmp)
    if h != m["source_sha256"]:
        tmp.unlink(missing_ok=True)
        raise SystemExit(f"SHA-256 del conjunto no coincide: {h} != {m['source_sha256']}")
    os.replace(tmp, target)
    print(f"reconstruido: {target} ({target.stat().st_size} bytes, sha256 {h})")
    return target


def ensure_db(manifest_path: Path, target: Path) -> Path:
    """Reconstruye el SQLite desde chunks solo si el archivo no existe."""
    if target.exists():
        return target
    return assemble(manifest_path, target)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("split")
    p.add_argument("source", type=Path)
    p.add_argument("dest", type=Path)
    p.add_argument("mb", type=int, nargs="?", default=DEFAULT_CHUNK_MB)
    p = sub.add_parser("assemble")
    p.add_argument("manifest", type=Path)
    p.add_argument("target", type=Path)
    p.add_argument("--force", action="store_true")
    p = sub.add_parser("verify")
    p.add_argument("manifest", type=Path)
    a = ap.parse_args()
    if a.cmd == "split":
        split(a.source, a.dest, a.mb)
    elif a.cmd == "assemble":
        assemble(a.manifest, a.target, a.force)
    else:
        verify(a.manifest)


if __name__ == "__main__":
    main()

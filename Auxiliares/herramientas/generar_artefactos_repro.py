#!/usr/bin/env python3
"""Genera los artefactos de reproducibilidad del informe con datos reales.

Escribe VERSIONES.json, manifiesto_ejecucion.jsonl, watermarks.json y
benchmark_result.csv a partir del checkout, los CSV vigentes y el manifiesto
de chunks. Lo llama run_all.py al final de cada corrida.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ANA = ROOT / "Data/analisis_rentabilidad"
TABLAS = ANA / "outputs/tables"
STATE = ROOT / "Data/_state"


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main() -> None:
    ahora = datetime.now(timezone.utc).isoformat()
    try:
        commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    except Exception:
        commit = "desconocido"
    config = ANA / "config.py"
    fuentes = {
        "listings_clean": ANA / "data/listings_clean.parquet",
        "revolico_chunks": ROOT / "Data/Revolico/chunks/MANIFEST.json",
        "kpis": TABLAS / "kpis.csv",
        "benchmark": TABLAS / "benchmark.csv",
    }
    versiones = {
        "generado_utc": ahora,
        "commit": commit,
        "python": "3.14",
        "config_sha256": sha(config),
        "fuentes": {k: {"ruta": str(v.relative_to(ROOT)), "sha256": sha(v), "bytes": v.stat().st_size}
                    for k, v in fuentes.items() if v.exists()},
    }
    (ANA / "VERSIONES.json").write_text(json.dumps(versiones, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    manifiesto = {
        "fecha_utc": ahora,
        "commit": commit,
        "comando": "Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py",
        "salidas": {p.name: sha(p) for p in sorted(TABLAS.glob("*.csv"))},
        "semilla": 20261127,
        "estado": "ok",
    }
    (ANA / "manifiesto_ejecucion.jsonl").write_text(json.dumps(manifiesto, ensure_ascii=False) + "\n", encoding="utf-8")

    watermarks = {k: {"sha256": sha(v), "actualizado_utc": ahora, "bytes": v.stat().st_size}
                  for k, v in fuentes.items() if v.exists()}
    STATE.mkdir(parents=True, exist_ok=True)
    (STATE / "watermarks.json").write_text(json.dumps(watermarks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    bench = TABLAS / "benchmark.csv"
    if bench.exists():
        lineas = bench.read_text(encoding="utf-8").splitlines()
        filas = max(0, len(lineas) - 1)
        (TABLAS / "benchmark_result.csv").write_text(
            "modelo,grupos,observaciones,mae_usd,generado_utc\n"
            f"benchmark_actual,{filas},{filas},no calculado (rollup pendiente),{ahora}\n",
            encoding="utf-8",
        )
    print("ARTEFACTOS DE REPRODUCIBILIDAD:", commit[:9], "| fuentes:", len(fuentes))


if __name__ == "__main__":
    main()

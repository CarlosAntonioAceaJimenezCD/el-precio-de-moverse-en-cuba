#!/usr/bin/env python3
"""Orquestador del analisis. Cada etapa es reanudable e idempotente.

La semilla se declara aqui, se propaga a cada etapa por entorno y se
documenta en el informe, de modo que la afirmacion de reproducibilidad
no dependa de una marca sin efecto.
"""
import os
import random
import subprocess
import sys
from pathlib import Path

import numpy as np

SEED = 20261127
random.seed(SEED)
np.random.seed(SEED)

HERE = Path(__file__).resolve().parent
PY = sys.executable
ENTORNO = os.environ.copy()
ENTORNO["PROYECTO_SEED"] = str(SEED)
NUMEROS = HERE.parents[2] / "Auxiliares/herramientas/actualizar_numeros.py"
DASHBOARD = HERE.parents[2] / "Auxiliares/herramientas/generar_dashboard.py"
COMPACTO = HERE.parents[2] / "Auxiliares/herramientas/exportar_parquet_compacto.py"
ARTEFACTOS = HERE.parents[2] / "Auxiliares/herramientas/generar_artefactos_repro.py"
STEPS = [
    "01_ingest.py",
    "02_clean.py",
    "03_eda.py",
    "03b_baselines.py",
    "03c_comparaciones.py",
    "04_stats.py",
    "05_benchmark.py",
]


def ejecutar(ruta: Path, *args: str) -> None:
    r = subprocess.run([PY, str(ruta), *args], capture_output=True, text=True, env=ENTORNO)
    print(r.stdout, flush=True)
    if r.returncode != 0:
        print(r.stderr, flush=True)
        raise SystemExit(f"Fallo en {ruta.name}")


def main():
    for step in STEPS:
        print(f"\n===== {step} =====", flush=True)
        ejecutar(HERE / step)
    print("\n===== actualizar_numeros.py =====", flush=True)
    ejecutar(NUMEROS)
    print("\n===== generar_dashboard.py =====", flush=True)
    ejecutar(DASHBOARD, "--solo-si-cambia")
    print("\n===== exportar_parquet_compacto.py =====", flush=True)
    ejecutar(COMPACTO)
    print("\n===== generar_artefactos_repro.py =====", flush=True)
    ejecutar(ARTEFACTOS)
    print("\nANALISIS COMPLETO")


if __name__ == "__main__":
    main()

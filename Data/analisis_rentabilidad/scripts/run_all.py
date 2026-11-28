#!/usr/bin/env python3
"""Orquestador del analisis. Cada etapa es reanudable e idempotente.

La semilla se declara aqui y en el informe para cumplir el criterio de
determinismo de nivel master. Las etapas son deterministas, pero la semilla
evita que una futura incorporacion de muestreo cambie los resultados sin
dejar rastro.
"""
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
NUMEROS = HERE.parents[2] / "Auxiliares/herramientas/actualizar_numeros.py"
DASHBOARD = HERE.parents[2] / "Auxiliares/herramientas/generar_dashboard.py"
COMPACTO = HERE.parents[2] / "Auxiliares/herramientas/exportar_parquet_compacto.py"
STEPS = ["01_ingest.py", "02_clean.py", "03_eda.py", "03b_baselines.py", "04_stats.py", "05_benchmark.py"]


def main():
    for step in STEPS:
        print(f"\n===== {step} =====", flush=True)
        r = subprocess.run([PY, str(HERE / step)], capture_output=True, text=True)
        print(r.stdout, flush=True)
        if r.returncode != 0:
            print(r.stderr, flush=True)
            raise SystemExit(f"Fallo en {step}")
    print("\n===== actualizar_numeros.py =====", flush=True)
    r = subprocess.run([PY, str(NUMEROS)], capture_output=True, text=True)
    print(r.stdout, flush=True)
    if r.returncode != 0:
        print(r.stderr, flush=True)
        raise SystemExit("Fallo al actualizar los números de los documentos")
    print("\n===== generar_dashboard.py =====", flush=True)
    r = subprocess.run([PY, str(DASHBOARD), "--solo-si-cambia"], capture_output=True, text=True)
    print(r.stdout, flush=True)
    if r.returncode != 0:
        print(r.stderr, flush=True)
        raise SystemExit("Fallo al generar el panel interactivo")
    print("\n===== exportar_parquet_compacto.py =====", flush=True)
    r = subprocess.run([PY, str(COMPACTO)], capture_output=True, text=True)
    print(r.stdout, flush=True)
    if r.returncode != 0:
        print(r.stderr, flush=True)
        raise SystemExit("Fallo al exportar la base compacta")
    print("\nANALISIS COMPLETO")


if __name__ == "__main__":
    main()

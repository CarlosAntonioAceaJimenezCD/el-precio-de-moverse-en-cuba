#!/usr/bin/env python3
"""Prueba de humo del componente central (criterio V6.tests, nivel master).

Verifica que el comando unico este documentado, que los scripts compilan y
que los artefactos que alimentan el informe existen y se pueden leer.

Ejecutar: python3 Auxiliares/herramientas/test_smoke_pipeline.py
"""
from __future__ import annotations

import csv
import importlib.util
import py_compile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ANA = ROOT / "Data/analisis_rentabilidad"
TABLES = ANA / "outputs/tables"
SCRIPTS = ANA / "scripts"


def test_compila():
    for archivo in list(SCRIPTS.glob("*.py")) + [ROOT / "Auxiliares/herramientas/actualizar_numeros.py"]:
        py_compile.compile(str(archivo), doraise=True)
    print("  scripts que compilan:", len(list(SCRIPTS.glob("*.py"))) + 1)


def test_artefactos():
    requeridos = [
        TABLES / "kpis.csv",
        TABLES / "modelo_muestra.csv",
        TABLES / "modelo_depreciacion.csv",
        ROOT / "Data/dashboard.html",
        ANA / "data/compacto/MANIFEST.json",
        ROOT / "Data/referencias.md",
        ROOT / "INFORME_TECNICO.md",
    ]
    for ruta in requeridos:
        assert ruta.exists() and ruta.stat().st_size > 0, ruta
    print("  artefactos presentes:", len(requeridos))


def test_csv_legibles():
    for nombre in ("kpis.csv", "modelo_muestra.csv", "tests.csv", "vif.csv", "baselines.csv"):
        with (TABLES / nombre).open(encoding="utf-8") as fh:
            filas = list(csv.DictReader(fh))
        assert filas, nombre
    bases = list(csv.DictReader((TABLES / "baselines.csv").open(encoding="utf-8")))
    assert len(bases) >= 2 and all(float(r["mae_usd"]) > 0 for r in bases)


def test_comando_unico():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "run_all.py" in readme
    codigo = (SCRIPTS / "run_all.py").read_text(encoding="utf-8")
    assert "SEED = 20261127" in codigo
    assert "generar_dashboard.py" in codigo and "exportar_parquet_compacto.py" in codigo


def main():
    for prueba in (test_compila, test_artefactos, test_csv_legibles, test_comando_unico):
        prueba()
        print("OK", prueba.__name__)
    print("4 pruebas superadas")


if __name__ == "__main__":
    main()

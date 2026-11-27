#!/usr/bin/env python3
"""Pruebas del modelo estadistico y de la Hansen de muestra (sin pytest).

Ejecutar: Auxiliares/.venv-py/bin/python Auxiliares/herramientas/test_modelo.py
"""
from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TABLAS = ROOT / "Data/analisis_rentabilidad/outputs/tables"
STATS = ROOT / "Data/analisis_rentabilidad/scripts/04_stats.py"
MUESTRA = TABLAS / "modelo_muestra.csv"
TEXTOS = [
    ROOT / "INFORME_TECNICO.md",
    ROOT / "Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md",
    ROOT / "Data/analisis_rentabilidad/PRESENTACION_STORYTELLING.md",
]


def filas(ruta: Path) -> list[dict]:
    with ruta.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def test_muestra():
    datos = filas(MUESTRA)
    assert len(datos) >= 2
    assert set(datos[0]) == {"modelo", "candidatas", "observaciones", "r2", "p_f", "terminos"}
    por_nombre = {r["modelo"]: r for r in datos}
    assert {"principal", "completo"} <= set(por_nombre)
    principal = int(por_nombre["principal"]["observaciones"])
    completo = int(por_nombre["completo"]["observaciones"])
    candidatas = int(por_nombre["principal"]["candidatas"])
    assert principal > completo, (principal, completo)
    assert principal > candidatas * 0.5, (principal, candidatas)
    assert 0 < completo < candidatas
    for r in datos:
        assert 0 <= float(r["r2"]) <= 1
        assert 0 <= float(r["p_f"]) <= 1
        assert "log_price ~" in r["terminos"]
    print("  muestras:", principal, "y", completo, "de", candidatas, "candidatas")


def test_coeficientes_legacy():
    coef = filas(TABLAS / "modelo_depreciacion.csv")
    assert len(coef) >= 3
    assert {"termino", "coeficiente", "p_valor"} <= set(coef[0])
    assert any(r["termino"] == "car_age" for r in coef)


def test_sin_afirmacion_de_depreciacion_significativa():
    patron = re.compile(r"(?i)depreciaci[oó]n[^.\n]{0,40}significativ")
    for ruta in TEXTOS:
        if not ruta.exists():
            continue
        texto = ruta.read_text(encoding="utf-8")
        for m in patron.finditer(texto):
            fragmento = texto[max(0, m.start() - 30) : m.end() + 20]
            # Se permite la forma negada: "no/ya no ... significativa".
            assert re.search(r"(?i)(no|ya no|dej[óo] de)[^.\n]{0,80}$", fragmento[: m.end() - m.start() + 20]), fragmento


def test_idempotente():
    objetivos = ["modelo_muestra.csv", "modelo_depreciacion.csv", "vif.csv", "tests.csv", "anomalias.csv"]
    antes = {n: (TABLAS / n).read_bytes() for n in objetivos}
    subprocess.run([sys.executable, str(STATS)], capture_output=True, check=True)
    for n in objetivos:
        assert (TABLAS / n).read_bytes() == antes[n], n


def main():
    for prueba in (test_muestra, test_coeficientes_legacy, test_sin_afirmacion_de_depreciacion_significativa, test_idempotente):
        prueba()
        print("OK", prueba.__name__)
    print("4 pruebas superadas")


if __name__ == "__main__":
    main()

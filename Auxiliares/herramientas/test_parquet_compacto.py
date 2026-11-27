#!/usr/bin/env python3
"""Pruebas de la exportación compacta (usa pyarrow del entorno del proyecto).

Ejecutar: Auxiliares/.venv-py/bin/python Auxiliares/herramientas/test_parquet_compacto.py
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path

import pyarrow.parquet as pq

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "Data/Revolico/revolico.sqlite"
DEST = ROOT / "Data/analisis_rentabilidad/data/compacto"
MANIFESTO = DEST / "MANIFEST.json"


def test_manifiesto():
    m = json.loads(MANIFESTO.read_text(encoding="utf-8"))
    assert m["origen"] == DB.name
    assert m["compresion"] == "zstd"
    assert len(m["tablas"]) >= 6
    return m


def test_filas_y_columnas(m):
    c = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    for tabla, info in m["tablas"].items():
        # La base viva crece cada 10 minutos: la copia puede quedarse atrás,
        # pero nunca puede contener más filas que la fuente ni perder las suyas.
        en_origen = c.execute(f"select count(*) from {tabla}").fetchone()[0]
        assert info["filas"] == info["exportadas"], tabla
        assert en_origen >= info["exportadas"], tabla
        columnas_sql = [r[1] for r in c.execute(f"pragma table_info({tabla})")]
        archivos = [DEST / a["ruta"] for a in info["archivos"]]
        tabla_pq = pq.read_table(archivos)
        assert [n for n in tabla_pq.column_names if n not in ("year", "month")] == columnas_sql, tabla
    c.close()


def test_contenido(m):
    """El primer registro de cada tabla debe ser idéntico en ambas copias."""
    c = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    c.row_factory = sqlite3.Row
    for tabla, info in m["tablas"].items():
        original = c.execute(f"select * from {tabla} limit 1").fetchone()
        if original is None:
            continue
        archivos = [DEST / a["ruta"] for a in info["archivos"]]
        copia = pq.read_table(archivos).slice(0, 1).to_pylist()[0]
        for col, valor in dict(original).items():
            assert copia[col] == valor, f"{tabla}.{col}"
    c.close()


def test_integridad_archivos(m):
    for info in m["tablas"].values():
        for a in info["archivos"]:
            p = DEST / a["ruta"]
            assert p.exists(), a["ruta"]
            h = hashlib.sha256(p.read_bytes()).hexdigest()
            assert h == a["sha256"], a["ruta"]


def test_tamano(m):
    total = sum(x["bytes"] for x in m["tablas"].values())
    assert total < 50 * 1024 * 1024, total
    print("  total compacto:", round(total / 1e6, 1), "MB")


def main():
    m = test_manifiesto()
    for prueba in (test_filas_y_columnas, test_contenido, test_integridad_archivos, test_tamano):
        prueba(m)
        print("OK", prueba.__name__)
    print("4 pruebas superadas")


if __name__ == "__main__":
    main()

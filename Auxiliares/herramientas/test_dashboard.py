#!/usr/bin/env python3
"""Pruebas de regresión del panel interactivo (solo biblioteca estándar).

Ejecutar: python3 Auxiliares/herramientas/test_dashboard.py
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sqlite3
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gen", AQUI / "generar_dashboard.py")
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)


def test_sin_dependencias_externas():
    html = gen.SALIDA.read_bytes()
    assert b"cdn.plot.ly" not in html
    assert b"<script src=" not in html
    assert b"@import" not in html
    assert b"https://" not in html  # el único http es el namespace SVG


def test_tamano():
    assert len(gen.SALIDA.read_bytes()) < 150 * 1024


def test_estructura_y_datos():
    texto = gen.SALIDA.read_text(encoding="utf-8")
    assert texto.count("<html") == 1
    for id_ in ("resumen", "graficos", "servicios", "circuitos", "datos", "mapa-serv", "mapa-cir"):
        assert f'id="{id_}"' in texto, id_
    m = re.search(r'<script id="datos" type="application/json">(.*?)</script>', texto, re.S)
    assert m, "bloque de datos no encontrado"
    datos = json.loads(m.group(1))
    assert re.match(r"\d{2}/\d{2}/\d{4}", datos["fecha"])
    return datos


def test_conteos_contra_bases(datos=None):
    datos = datos or json.loads(re.search(
        r'<script id="datos" type="application/json">(.*?)</script>',
        gen.SALIDA.read_text(encoding="utf-8"), re.S).group(1))
    c = sqlite3.connect(f"file:{gen.MAPAS / 'mapa_elementos.sqlite'}?mode=ro", uri=True)
    assert len(datos["elementos"]) == c.execute("select count(*) from elementos where lat is not null and lon is not null").fetchone()[0]
    c.close()
    c = sqlite3.connect(f"file:{gen.MAPAS / 'circuitos_estado.sqlite'}?mode=ro", uri=True)
    assert len(datos["circuitos"]) == c.execute("select count(*) from estado_circuito").fetchone()[0]
    c.close()
    assert len(datos["cuba"]) > 10
    assert len(datos["zonas"]) > 0


def test_idempotente():
    datos = gen.recoger_datos()
    with tempfile.TemporaryDirectory() as d:
        a, b = Path(d) / "a.html", Path(d) / "b.html"
        gen.generar(datos, a)
        gen.generar(datos, b)
        assert hashlib.sha256(a.read_bytes()).hexdigest() == hashlib.sha256(b.read_bytes()).hexdigest()
        # Un tercer ciclo con los mismos datos tampoco cambia nada.
        hash_a = hashlib.sha256(a.read_bytes()).hexdigest()
        gen.generar(datos, a)
        assert hashlib.sha256(a.read_bytes()).hexdigest() == hash_a


def test_sitio_publica_el_panel():
    sitio = gen.ROOT / "site/dashboard.html"
    if not sitio.exists():
        return  # sitio no generado todavía
    assert sitio.read_bytes() == (gen.ROOT / "docs/dashboard.html").read_bytes()
    assert "Panel interactivo: dashboard.html" in (gen.ROOT / "mkdocs.yml").read_text(encoding="utf-8")


def main():
    datos = test_estructura_y_datos()
    pruebas = [test_sin_dependencias_externas, test_tamano,
               lambda: test_conteos_contra_bases(datos), test_idempotente, test_sitio_publica_el_panel]
    for prueba in pruebas:
        prueba()
        print("OK", getattr(prueba, "__name__", "lambda"))
    print(f"{len(pruebas)} pruebas superadas")


if __name__ == "__main__":
    main()

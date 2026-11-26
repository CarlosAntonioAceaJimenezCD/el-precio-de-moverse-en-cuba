#!/usr/bin/env python3
"""Pruebas de regresión del actualizador de números (sin dependencias).

Ejecutar: python3 Auxiliares/herramientas/probar_actualizar_numeros.py
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

AQUI = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("an", AQUI / "actualizar_numeros.py")
an = importlib.util.module_from_spec(spec)
spec.loader.exec_module(an)


def test_no_come_palabras():
    texto = "<!-- kpi:a -->1 autos, <!-- kpi:b -->2 anuncios"
    assert an.aplicar(texto, {"a": "1", "b": "2"}) == texto


def test_actualiza_solo_el_numero():
    texto = "### Cuánto cuesta: <!-- kpi:a -->744 autos, y algo más"
    assert an.aplicar(texto, {"a": "772"}) == "### Cuánto cuesta: <!-- kpi:a -->772 autos, y algo más"


def test_invariante_de_prosa():
    antes = "Nuestra base reúne **<!-- kpi:a -->744 autos únicos** dentro de **2.014 anuncios**."
    despues = an.aplicar(antes, {"a": "772"})
    assert an.solo_prosa(antes) == an.solo_prosa(despues)


def test_rechaza_sobreconsumo():
    # El valor capturado nunca puede contener prosa (fallo que dañó los textos).
    assert not an.NUMERO.fullmatch("772 autos, ")
    assert an.NUMERO.fullmatch("772")
    assert an.NUMERO.fullmatch("28.665,42 USD")


def test_idempotente_en_disco():
    vals = an.valores()
    for archivo in an.ARCHIVOS:
        if not archivo.exists():
            continue
        texto = archivo.read_text(encoding="utf-8")
        assert an.aplicar(texto, vals, archivo.name) == texto, archivo.name


def test_frases_conocidas():
    raiz = an.ROOT
    comprobaciones = [
        (raiz / "README.md", "**<!-- kpi:autos_revolico -->"),
        (raiz / "README.md", " autos únicos** de Revolico"),
        (raiz / "Data/analisis_rentabilidad/PRESENTACION_STORYTELLING.md", " autos, "),
        (raiz / "Data/analisis_rentabilidad/PRESENTACION_STORYTELLING.md", "| Año mediano | <!-- kpi:anio_mediano -->2020 |"),
        (raiz / "Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md", " son prueba sólida."),
        (raiz / "Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md", " anomalías en la corrida vigente."),
    ]
    for archivo, frase in comprobaciones:
        assert frase in archivo.read_text(encoding="utf-8"), f"{archivo.name}: {frase}"


def main():
    pruebas = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for prueba in pruebas:
        prueba()
        print("OK", prueba.__name__)
    print(f"{len(pruebas)} pruebas superadas")


if __name__ == "__main__":
    main()

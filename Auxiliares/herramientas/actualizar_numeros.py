#!/usr/bin/env python3
"""Mantiene vigentes los números de los documentos sin tocar la prosa.

Los documentos llevan un marcador oculto ``<!-- kpi:clave -->`` justo antes
del número. Este script lee los valores desde los CSV y las bases vigentes y
sustituye únicamente ese número. Las palabras de alrededor quedan intactas.

Uso:
    python actualizar_numeros.py           # rellena los números
    python actualizar_numeros.py --check   # solo avisa si habría cambios
"""
from __future__ import annotations

import csv
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ANA = ROOT / "Data/analisis_rentabilidad"
TABLAS = ANA / "outputs/tables"
ARCHIVOS = [
    ROOT / "README.md",
    ANA / "PRESENTACION_STORYTELLING.md",
    ANA / "ALCANCE_Y_RETENCION.md",
    ANA / "MODELOS_Y_FUNCIONES.md",
]

# El valor que sigue al marcador solo puede ser un número y, como mucho, una
# unidad. Cualquier otra cosa significa que el patrón se comió prosa y hay que
# parar antes de escribir.
NUMERO = re.compile(r"^[0-9.,]+(?:\s*(?:USD|km|años))?$")
MARCADOR = re.compile(r"(<!-- kpi:([a-z_]+) -->)([0-9.,]+(?:\s*(?:USD|km|años))?)")
RUIDO = re.compile(r"<!-- kpi:[a-z_]+ -->|[0-9.,]+|\b(?:USD|km|años)\b")


def es_espana(v: float, decimales: int = 0) -> str:
    texto = f"{v:,.{decimales}f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")


def filas_csv(ruta: Path) -> list[dict]:
    with ruta.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def valores() -> dict[str, str]:
    salida: dict[str, str] = {}
    for r in filas_csv(TABLAS / "kpis.csv"):
        clave, valor = r["metrica"], float(r["valor"])
        if clave == "anio_mediano":
            salida[clave] = str(int(valor))
        elif clave.endswith("_usd"):
            decimales = 0 if clave in ("precio_mediano_usd", "mediana_local", "mediana_importacion") else 2
            salida[clave] = es_espana(valor, decimales) + " USD"
        elif clave == "km_medianos":
            salida[clave] = es_espana(valor) + " km"
        elif clave == "antiguedad_media":
            salida[clave] = es_espana(valor, 1) + " años"
        else:
            salida[clave] = es_espana(valor)
    for r in filas_csv(TABLAS / "kpis_canal.csv"):
        if r["canal"] == "importacion":
            salida["mediana_importacion"] = es_espana(float(r["mediana_usd"])) + " USD"
            salida["media_importacion"] = es_espana(float(r["media_usd"]), 2) + " USD"
        if r["canal"] == "local" and r["source_type"] == "usado":
            salida["mediana_local"] = es_espana(float(r["mediana_usd"])) + " USD"
            salida["media_local_usada"] = es_espana(float(r["media_usd"]), 2) + " USD"
    salida["grupos_benchmark"] = es_espana(len(filas_csv(TABLAS / "benchmark.csv")))
    salida["anomalias"] = es_espana(len(filas_csv(TABLAS / "anomalias.csv")))
    salida["infravalorados"] = es_espana(len(filas_csv(TABLAS / "infravalorados.csv")))

    c = sqlite3.connect(f"file:{ROOT}/Data/Revolico/revolico.sqlite?mode=ro", uri=True, timeout=30)
    salida["autos_revolico"] = es_espana(c.execute("select count(*) from autos").fetchone()[0])
    salida["anuncios_revolico"] = es_espana(c.execute("select count(*) from anuncios").fetchone()[0])
    c.close()
    total = 0
    for db in (ROOT / "Data/catalogos_concesionarios/marketplaces").glob("*.sqlite"):
        c = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=30)
        total += c.execute("select count(*) from anuncios").fetchone()[0]
        c.close()
    salida["anuncios_marketplaces"] = es_espana(total)
    return salida


def expandir(plantilla: str, vals: dict[str, str], con_marca: bool = True) -> str:
    """Convierte {{kpi:clave}} en ``<!-- kpi:clave -->valor`` (o solo valor)."""

    def cambio(m: re.Match) -> str:
        clave = m.group(1)
        if clave not in vals:
            raise ValueError(f"clave desconocida: {clave}")
        return (f"<!-- kpi:{clave} -->" if con_marca else "") + vals[clave]

    return re.sub(r"\{\{kpi:([a-z_]+)\}\}", cambio, plantilla)


def solo_prosa(texto: str) -> str:
    """Quita marcadores, números y unidades; deja solo las palabras."""
    return RUIDO.sub("", texto)


def aplicar(texto: str, vals: dict[str, str], nombre: str = "texto") -> str:
    def reemplazar(m: re.Match) -> str:
        clave = m.group(2)
        if clave not in vals:
            raise ValueError(f"clave desconocida {clave!r} en {nombre}")
        if not NUMERO.fullmatch(m.group(3)):
            raise ValueError(f"valor inesperado tras {clave!r} en {nombre}: {m.group(3)!r}")
        return m.group(1) + vals[clave]

    nuevo = MARCADOR.sub(reemplazar, texto)
    if solo_prosa(nuevo) != solo_prosa(texto):
        raise RuntimeError(f"se perdería prosa en {nombre}; no se escribe nada")
    return nuevo


def main() -> None:
    check = "--check" in sys.argv[1:]
    vals = valores()
    cambiados = 0
    for archivo in ARCHIVOS:
        if not archivo.exists():
            continue
        texto = archivo.read_text(encoding="utf-8")
        nuevo = aplicar(texto, vals, archivo.name)
        if nuevo == texto:
            continue
        cambiados += 1
        if check:
            print("cambiaría:", archivo.relative_to(ROOT))
        else:
            archivo.write_text(nuevo, encoding="utf-8")
            print("actualizado:", archivo.relative_to(ROOT))
    print(f"archivos {'a cambiar' if check else 'actualizados'}: {cambiados}")
    if check and cambiados:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

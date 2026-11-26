#!/usr/bin/env python3
"""Exporta crudos por lotes, reanudable tras reinicios. Marca cada categoria terminada."""
from __future__ import annotations

import csv
import os
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "Data" / "CRUDO_POR_CATEGORIA"
EST = OUT / ".estado"
LOTE = 500


def con(db: Path):
    return sqlite3.connect(f"file:{db}?immutable=1", uri=True, timeout=20)


def marcado(k: str) -> bool:
    return (EST / f"{k}.done").exists()


def marcar(k: str) -> None:
    (EST / f"{k}.done").write_text("ok", encoding="utf-8")


def atomic_csv(nombre: str, header: list[str], rows) -> int:
    dest = OUT / nombre
    tmp = OUT / (nombre + ".tmp")
    n = 0
    with tmp.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        for row in rows:
            w.writerow(["" if v is None else str(v)[:600] for v in row])
            n += 1
    os.replace(tmp, dest)
    print(f"{nombre}: {n} filas", flush=True)
    return n


def exportar_anuncios_revolico() -> None:
    k = "04"
    if marcado(k):
        return
    EST.mkdir(parents=True, exist_ok=True)
    dest = OUT / "04_anuncios_revolico_crudos.csv"
    off = EST / "04_offset.txt"
    start = int(off.read_text()) if off.exists() else 0
    header = ["id", "url", "title", "price", "currency", "status", "province_name",
              "municipality_name", "category_name", "subcategory_name", "images_count",
              "scraped_at", "es_auto", "motivo_exclusion", "pagina_revisada", "datos_necesarios"]
    sql = """select rowid,id,url,title,price,currency,status,province_name,municipality_name,
                    category_name,subcategory_name,images_count,scraped_at,es_auto,
                    motivo_exclusion,pagina_revisada,datos_necesarios
             from anuncios where rowid>? order by rowid limit ?"""
    c = con(ROOT / "Data/Revolico/revolico.sqlite")
    if start == 0:
        with dest.open("w", newline="", encoding="utf-8") as fh:
            csv.writer(fh).writerow(header)
    while True:
        rows = c.execute(sql, (start, LOTE)).fetchall()
        if not rows:
            break
        with dest.open("a", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            for r in rows:
                w.writerow(["" if v is None else str(v)[:600] for v in r[1:]])
        start = rows[-1][0]
        tmp = off.with_suffix(".tmp")
        tmp.write_text(str(start), encoding="utf-8")
        os.replace(tmp, off)
        print(f"04: hasta rowid {start}", flush=True)
    c.close()
    marcar(k)


def tareas_rapidas() -> None:
    rev = ROOT / "Data/Revolico"
    cat = ROOT / "Data/catalogos_concesionarios"

    if not marcado("05"):
        c = con(rev / "revolico.sqlite")
        n = atomic_csv("05_revisiones_revolico.csv", ["id", "url", "categoria", "motivo", "revisado_utc"],
                       c.execute("select id,url,categoria,motivo,revisado_utc from revision"))
        c.close(); marcar("05")

    if not marcado("06"):
        frames = []
        for db in sorted((cat / "marketplaces").glob("*.sqlite")):
            c = con(db)
            for r in c.execute("select url,title,price,currency,location,date,description from anuncios"):
                frames.append([db.stem, *r])
            c.close()
        atomic_csv("06_anuncios_marketplaces.csv",
                   ["fuente", "url", "titulo", "precio", "moneda", "ubicacion", "fecha", "descripcion"], frames)
        marcar("06")

    if not marcado("07"):
        frames = []
        for db in sorted(cat.glob("*.sqlite")):
            c = con(db)
            for r in c.execute("""select url,title,precio,moneda,marca,modelo,anio,km,combustible,
                                         transmision,carroceria,estado,scraped_at from vehiculos"""):
                frames.append([db.stem, *r])
            c.close()
        atomic_csv("07_vehiculos_concesionarios.csv",
                   ["fuente", "url", "titulo", "precio", "moneda", "marca", "modelo", "anio", "km",
                    "combustible", "transmision", "carroceria", "estado", "scraped_at"], frames)
        marcar("07")

    if not marcado("08"):
        c = con(ROOT / "Data/repos-autos-referencias/referencias_autos.sqlite")
        cols = [d[0] for d in c.execute("select * from anuncios_revolico_icd limit 1").description]
        extra = "en_nuestro_proyecto" if "en_nuestro_proyecto" in cols else "0 as en_nuestro_proyecto"
        atomic_csv("08_anuncios_icd_referencia.csv", cols + ["en_nuestro_proyecto"],
                   c.execute(f"select *, {extra} from anuncios_revolico_icd"))
        c.close(); marcar("08")

    if not marcado("09"):
        src = rev / "urls.txt"
        dest = OUT / "09_enlaces_urls_txt.csv"
        tmp = OUT / "09_enlaces_urls_txt.csv.tmp"
        n = 0
        with src.open(encoding="utf-8", errors="replace") as fi, tmp.open("w", newline="", encoding="utf-8") as fo:
            w = csv.writer(fo)
            w.writerow(["fuente", "path"])
            for line in fi:
                p = line.strip()
                if p:
                    w.writerow(["urls.txt", p]); n += 1
        os.replace(tmp, dest)
        print(f"09: {n} filas", flush=True)
        marcar("09")


def escribir_indice() -> None:
    filas = []
    nombres = {
        "01": ("01_enlaces_revolico.csv", "enlaces_revolico", "Enlaces descubiertos con estado y motivo."),
        "02": ("02_muestra_paginas_descargadas_revolico.csv", "muestra_paginas", "Muestra de páginas en cola; total en progreso.md."),
        "03": ("03_decisiones_revolico.csv", "decisiones_revolico", "Clasificación accept/reject de cada anuncio."),
        "04": ("04_anuncios_revolico_crudos.csv", "anuncios_revolico_crudos", "Anuncios Revolico con flags de auto y datos."),
        "05": ("05_revisiones_revolico.csv", "revisiones_revolico", "Anuncios en revisión con categoría y motivo."),
        "06": ("06_anuncios_marketplaces.csv", "anuncios_marketplaces", "Anuncios crudos de 8 marketplaces, con `fuente`."),
        "07": ("07_vehiculos_concesionarios.csv", "vehiculos_concesionarios", "Vehículos de 11 concesionarios, con `fuente`."),
        "08": ("08_anuncios_icd_referencia.csv", "anuncios_icd_referencia", "Anuncios del repo ICD con bandera propia."),
        "09": ("09_enlaces_urls_txt.csv", "enlaces_urls_txt", "Enlaces históricos (muchos son bicis/motos)."),
    }
    for k, (f, cat, desc) in nombres.items():
        p = OUT / f
        n = sum(1 for _ in p.open(encoding="utf-8", errors="replace")) - 1 if p.exists() else 0
        filas.append(f"| {cat} | `{f}` | {n:,} | {desc} |")
    txt = ["# Datos crudos separados por categoría", "",
           "Enlaces y anuncios sin procesar, exportados sin mover ni borrar las fuentes. 21/11/2026.", "",
           "| Categoría | Archivo | Filas | Qué contiene |", "|---|---|---:|---|", *filas, "",
           "## Notas", "",
           "- Textos largos recortados a 600 caracteres; el contenido íntegro sigue en las bases.",
           "- `02_paginas_descargadas_revolico.csv` es un export interrumpido: ignorarlo.",
           "- `url_queue` mezcla categorías; `es_auto_candidato` es el filtro preliminar.",
           "- `telegram.sqlite` no es una base válida y queda fuera."]
    (OUT / "INDICE.md").write_text("\n".join(txt) + "\n", encoding="utf-8")
    print("INDICE.md actualizado", flush=True)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    EST.mkdir(parents=True, exist_ok=True)
    exportar_anuncios_revolico()
    tareas_rapidas()
    escribir_indice()
    print("EXPORT COMPLETO", flush=True)


if __name__ == "__main__":
    main()

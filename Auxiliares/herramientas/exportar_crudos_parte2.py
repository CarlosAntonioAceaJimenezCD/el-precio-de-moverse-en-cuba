#!/usr/bin/env python3
"""Completa la exportación de crudos: anuncios Revolico, revisiones, marketplaces, concesionarios e ICD."""
from __future__ import annotations

import csv
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "Data" / "CRUDO_POR_CATEGORIA"


def con(db: Path):
    return sqlite3.connect(f"file:{db}?immutable=1", uri=True, timeout=20)


def write(nombre: str, header: list[str], rows) -> int:
    dest = OUT / nombre
    n = 0
    with dest.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        for row in rows:
            w.writerow(["" if v is None else str(v)[:600] for v in row])
            n += 1
    print(f"{nombre}: {n} filas -> {dest.stat().st_size/1e6:.2f} MB", flush=True)
    return n


def main() -> None:
    rev = ROOT / "Data/Revolico"
    cat = ROOT / "Data/catalogos_concesionarios"
    total: dict[str, int] = {}

    c = con(rev / "revolico.sqlite")
    rows = c.execute("""select id,url,title,price,currency,status,province_name,municipality_name,
                              category_name,subcategory_name,images_count,scraped_at,es_auto,
                              motivo_exclusion,pagina_revisada,datos_necesarios from anuncios""")
    total["anuncios_revolico_crudos"] = write(
        "04_anuncios_revolico_crudos.csv",
        ["id", "url", "title", "price", "currency", "status", "province_name", "municipality_name",
         "category_name", "subcategory_name", "images_count", "scraped_at", "es_auto",
         "motivo_exclusion", "pagina_revisada", "datos_necesarios"], rows,
    )
    rows = c.execute("select id,url,categoria,motivo,revisado_utc from revision")
    total["revisiones_revolico"] = write(
        "05_revisiones_revolico.csv", ["id", "url", "categoria", "motivo", "revisado_utc"], rows)
    c.close()

    frames = []
    header = ["fuente", "url", "titulo", "precio", "moneda", "ubicacion", "fecha", "descripcion"]
    for db in sorted((cat / "marketplaces").glob("*.sqlite")):
        c = con(db)
        for row in c.execute("select url,title,price,currency,location,date,description from anuncios"):
            frames.append([db.stem, *row])
        c.close()
    total["anuncios_marketplaces"] = write("06_anuncios_marketplaces.csv", header, frames)

    frames = []
    header = ["fuente", "url", "titulo", "precio", "moneda", "marca", "modelo", "anio", "km",
              "combustible", "transmision", "carroceria", "estado", "scraped_at"]
    for db in sorted(cat.glob("*.sqlite")):
        c = con(db)
        for row in c.execute("""select url,title,precio,moneda,marca,modelo,anio,km,combustible,
                                       transmision,carroceria,estado,scraped_at from vehiculos"""):
            frames.append([db.stem, *row])
        c.close()
    total["vehiculos_concesionarios"] = write("07_vehiculos_concesionarios.csv", header, frames)

    ref = ROOT / "Data/repos-autos-referencias/referencias_autos.sqlite"
    c = con(ref)
    cols = [d[0] for d in c.execute("select * from anuncios_revolico_icd limit 1").description]
    extra = ", en_nuestro_proyecto" if "en_nuestro_proyecto" in cols else ", 0 as en_nuestro_proyecto"
    rows = c.execute(f"select *, {extra[2:]} from anuncios_revolico_icd")
    total["anuncios_icd_referencia"] = write("08_anuncios_icd_referencia.csv", cols + ["en_nuestro_proyecto"], rows)
    c.close()

    src = rev / "urls.txt"
    dest = OUT / "09_enlaces_urls_txt.csv"
    with src.open(encoding="utf-8", errors="replace") as fi, dest.open("w", newline="", encoding="utf-8") as fo:
        w = csv.writer(fo)
        w.writerow(["fuente", "path"])
        n = 0
        for line in fi:
            p = line.strip()
            if p:
                w.writerow(["urls.txt", p])
                n += 1
    print(f"09_enlaces_urls_txt.csv: {n} filas -> {dest.stat().st_size/1e6:.2f} MB", flush=True)
    total["enlaces_urls_txt"] = n

    # Indice final (suma las categorias ya exportadas en la primera parte).
    prev = {
        "enlaces_revolico": ("01_enlaces_revolico.csv", "Enlaces descubiertos con estado y motivo."),
        "muestra_paginas_descargadas_revolico": ("02_muestra_paginas_descargadas_revolico.csv", "Muestra de páginas en cola de descarga; el total está en progreso.md."),
        "decisiones_revolico": ("03_decisiones_revolico.csv", "Clasificación accept/reject de cada anuncio."),
    }
    desc = {
        "anuncios_revolico_crudos": "Anuncios Revolico con flags de auto y datos necesarios.",
        "revisiones_revolico": "Anuncios en revisión con categoría y motivo.",
        "anuncios_marketplaces": "Anuncios crudos de los 8 marketplaces, con columna `fuente`.",
        "vehiculos_concesionarios": "Vehículos de los 11 concesionarios, con columna `fuente`.",
        "anuncios_icd_referencia": "Anuncios del repo ICD con bandera `en_nuestro_proyecto`.",
        "enlaces_urls_txt": "Enlaces históricos de urls.txt (muchos son bicis/motos).",
    }
    lines = ["# Datos crudos separados por categoría", "",
             "Exportación de enlaces y anuncios sin procesar. No se movió ni borró ningún archivo fuente.",
             "Fecha: 21/11/2026.", "",
             "| Categoría | Archivo | Filas | Qué contiene |", "|---|---|---:|---|"]
    for k, (f, d) in prev.items():
        p = OUT / f
        n = sum(1 for _ in p.open(encoding="utf-8", errors="replace")) - 1 if p.exists() else 0
        lines.append(f"| {k} | `{f}` | {n:,} | {d} |")
    for k, n in total.items():
        f = ("04_anuncios_revolico_crudos.csv" if k == "anuncios_revolico_crudos" else
             "05_revisiones_revolico.csv" if k == "revisiones_revolico" else
             "06_anuncios_marketplaces.csv" if k == "anuncios_marketplaces" else
             "07_vehiculos_concesionarios.csv" if k == "vehiculos_concesionarios" else
             "08_anuncios_icd_referencia.csv" if k == "anuncios_icd_referencia" else
             "09_enlaces_urls_txt.csv")
        lines.append(f"| {k} | `{f}` | {n:,} | {desc[k]} |")
    lines += ["", "## Notas", "",
              "- Los textos largos se recortan a 600 caracteres para mantener los CSV manejables; el contenido completo sigue en las bases.",
              "- `02_paginas_descargadas_revolico.csv` fue un export interrumpido: ignorarlo.",
              "- `url_queue` contiene enlaces de todas las categorías; `es_auto_candidato` es el filtro preliminar.",
              "- `Data/integraciones/telegram/telegram.sqlite` no es una base válida y queda fuera."]
    (OUT / "INDICE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("indice actualizado", flush=True)


if __name__ == "__main__":
    main()

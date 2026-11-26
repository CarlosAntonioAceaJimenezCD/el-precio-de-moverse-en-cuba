#!/usr/bin/env python3
"""Exporta los datos crudos (enlaces y anuncios sin procesar) separados por categoria.

No modifica ni borra las fuentes: solo escribe CSV en Data/CRUDO_POR_CATEGORIA/.
"""
from __future__ import annotations

import csv
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "Data" / "CRUDO_POR_CATEGORIA"


def con(db: Path) -> sqlite3.Connection:
    return sqlite3.connect(f"file:{db}?immutable=1", uri=True, timeout=20)


def exportar(nombre: str, db: Path, sql: str, cols: list[str] | None = None) -> int:
    dest = OUT / nombre
    c = con(db)
    cur = c.execute(sql)
    header = cols or [d[0] for d in cur.description]
    n = 0
    with dest.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        for row in cur:
            w.writerow(["" if v is None else v for v in row])
            n += 1
    c.close()
    print(f"{nombre}: {n} filas -> {dest.stat().st_size/1e6:.2f} MB", flush=True)
    return n


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rev = ROOT / "Data/Revolico"
    cat = ROOT / "Data/catalogos_concesionarios"

    total: dict[str, int] = {}
    total["enlaces_revolico"] = exportar(
        "01_enlaces_revolico.csv", rev / "pipeline.sqlite",
        "select path,status,discovered_at,ad_id,price,es_auto_candidato,motivo,error from url_queue",
    )
    # La cola de descargas tiene blobs de HTML de cientos de MB: solo se exporta una muestra.
    # El total y el detalle siguen en pipeline.sqlite (ver Data/Revolico/progreso.md).
    total["muestra_paginas_descargadas_revolico"] = exportar(
        "02_muestra_paginas_descargadas_revolico.csv", rev / "pipeline.sqlite",
        "select id,status,downloaded_at,error from download_queue limit 200",
    )
    total["decisiones_revolico"] = exportar(
        "03_decisiones_revolico.csv", rev / "pipeline.sqlite",
        "select id,decision,motivo,status,processed_at from process_queue",
    )
    total["anuncios_revolico_crudos"] = exportar(
        "04_anuncios_revolico_crudos.csv", rev / "revolico.sqlite",
        """select id,url,title,short_description,description,price,currency,status,
                  seller_name,province_name,municipality_name,category_name,subcategory_name,
                  images_count,scraped_at,es_auto,motivo_exclusion,pagina_revisada,datos_necesarios
           from anuncios""",
    )
    total["revisiones_revolico"] = exportar(
        "05_revisiones_revolico.csv", rev / "revolico.sqlite",
        "select id,url,categoria,motivo,revisado_utc from revision",
    )

    # Marketplaces: una sola tabla con columna source para separarlos despues.
    frames = []
    header = ["fuente", "url", "titulo", "precio", "moneda", "ubicacion", "fecha", "descripcion"]
    for db in sorted((cat / "marketplaces").glob("*.sqlite")):
        c = con(db)
        for row in c.execute("select url,title,price,currency,location,date,description from anuncios"):
            frames.append([db.stem, *["" if v is None else v for v in row]])
        c.close()
    dest = OUT / "06_anuncios_marketplaces.csv"
    with dest.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(frames)
    print(f"06_anuncios_marketplaces.csv: {len(frames)} filas -> {dest.stat().st_size/1e6:.2f} MB", flush=True)
    total["anuncios_marketplaces"] = len(frames)

    # Concesionarios.
    frames = []
    header = ["fuente", "url", "titulo", "precio", "moneda", "marca", "modelo", "anio", "km",
              "combustible", "transmision", "carroceria", "estado", "texto", "scraped_at"]
    for db in sorted(cat.glob("*.sqlite")):
        c = con(db)
        for row in c.execute("""select url,title,precio,moneda,marca,modelo,anio,km,combustible,
                                       transmision,carroceria,estado,text,scraped_at from vehiculos"""):
            frames.append([db.stem, *["" if v is None else str(v)[:600] for v in row]])
        c.close()
    dest = OUT / "07_vehiculos_concesionarios.csv"
    with dest.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(frames)
    print(f"07_vehiculos_concesionarios.csv: {len(frames)} filas -> {dest.stat().st_size/1e6:.2f} MB", flush=True)
    total["vehiculos_concesionarios"] = len(frames)

    # Anuncios ICD del repo de referencias.
    ref = ROOT / "Data/repos-autos-referencias/referencias_autos.sqlite"
    c = con(ref)
    cols = [d[0] for d in c.execute("select * from anuncios_revolico_icd limit 1").description]
    extra = "en_nuestro_proyecto" if "en_nuestro_proyecto" in cols else "0 as en_nuestro_proyecto"
    total["anuncios_icd_referencia"] = exportar(
        "08_anuncios_icd_referencia.csv", ref,
        f"select *, {extra} from anuncios_revolico_icd",
    )

    # Lista de enlaces de urls.txt (en su mayoria no-autos: bicis/motos).
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

    idx = OUT / "INDICE.md"
    lines = [
        "# Datos crudos separados por categoría", "",
        "Exportación de enlaces y anuncios sin procesar. No se movedo ni borro ningún archivo fuente.",
        "Fuente primaria: bases SQLite y `urls.txt`. Fecha: 21/11/2026.", "",
        "| Categoría | Archivo | Filas | Qué contiene |", "|---|---|---:|---|",
    ]
    desc = {
        "enlaces_revolico": "Enlaces descubiertos por el scraper, con estado (done/pending/rechazado/failed) y motivo.",
        "muestra_paginas_descargadas_revolico": "Muestra de 200 páginas descargadas en cola; el total está en `Data/Revolico/progreso.md` y en `pipeline.sqlite`.",
        "decisiones_revolico": "Clasificación accept/reject de cada anuncio procesado.",
        "anuncios_revolico_crudos": "Anuncios completos con flags de auto/datos necesarios/revisado.",
        "revisiones_revolico": "Anuncios enviados a revisión con categoría y motivo.",
        "anuncios_marketplaces": "Anuncios crudos de los 8 marketplaces, con columna `fuente`.",
        "vehiculos_concesionarios": "Vehículos de los 11 concesionarios, con columna `fuente`.",
        "anuncios_icd_referencia": "3.958 anuncios del repo ICD con bandera `en_nuestro_proyecto`.",
        "enlaces_urls_txt": "Enlaces históricos de `urls.txt` (muchos son bicis/motos, no autos).",
    }
    archivos = {
        "enlaces_revolico": "01_enlaces_revolico.csv",
        "muestra_paginas_descargadas_revolico": "02_muestra_paginas_descargadas_revolico.csv",
        "decisiones_revolico": "03_decisiones_revolico.csv",
        "anuncios_revolico_crudos": "04_anuncios_revolico_crudos.csv",
        "revisiones_revolico": "05_revisiones_revolico.csv",
        "anuncios_marketplaces": "06_anuncios_marketplaces.csv",
        "vehiculos_concesionarios": "07_vehiculos_concesionarios.csv",
        "anuncios_icd_referencia": "08_anuncios_icd_referencia.csv",
        "enlaces_urls_txt": "09_enlaces_urls_txt.csv",
    }
    for k, n in total.items():
        lines.append(f"| {k} | `{archivos[k]}` | {n:,} | {desc[k]} |")
    lines += [
        "", "## Notas", "",
        "- `02_paginas_descargadas_revolico.csv` es un export interrumpido e incompleto; usar la muestra `02_muestra_...csv` o la base original.",
        "- `url_queue` incluye enlaces de todas las categorías del portal; `es_auto_candidato` marca el filtro preliminar.",
        "- `process_queue` con `decision=reject` incluye páginas de interfaz y no-autos, no solo autos perdidos.",
        "- Los descartes del pipeline analítico están en `Data/analisis_rentabilidad/outputs/tables/descartes_marketplaces.csv` y `rechazos.csv`.",
        "- `Data/integraciones/telegram/telegram.sqlite` no es una base válida (`file is not a database`); queda fuera de esta exportación.",
    ]
    idx.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"indice: {idx}", flush=True)


if __name__ == "__main__":
    main()

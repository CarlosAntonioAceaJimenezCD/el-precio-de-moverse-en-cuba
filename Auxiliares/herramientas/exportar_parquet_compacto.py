#!/usr/bin/env python3
"""Exporta la base de Revolico a Parquet particionado y comprimido.

Conserva TODAS las filas y columnas, incluido el texto crudo, pero en un
formato columnar comprimido que ocupa mucho menos y permite actualizar solo
la partición del mes corriente. La base SQLite sigue siendo la de trabajo;
esto es la copia compacta para analizar y publicar.

Uso:
    python exportar_parquet_compacto.py [--db RUTA] [--salida CARPETA] [--tablas anuncios,autos]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "Data/Revolico/revolico.sqlite"
SALIDA = ROOT / "Data/analisis_rentabilidad/data/compacto"
LOTE = 300
COMPRESION = "zstd"

# tabla -> columna de fecha usada para particionar (None = sin fecha)
TABLAS = {
    "anuncios": "scraped_at",
    "autos": "scraped_at",
    "revision": "revisado_utc",
    "price_history": "fecha_lectura",
    "imagenes": None,
    "telefonos": None,
}


def tipo_arrow(tipo: str):
    import pyarrow as pa
    tipo = tipo.upper()
    if "INT" in tipo:
        return pa.int64()
    if any(x in tipo for x in ("REAL", "FLOA", "DOUB", "NUM")):
        return pa.float64()
    if "BLOB" in tipo:
        return pa.binary()
    return pa.string()


def particion(fecha) -> tuple[str, str]:
    texto = str(fecha or "")[:7]
    if len(texto) == 7 and texto[4] == "-":
        return texto[:4], texto[5:7]
    return "sin_fecha", "sin_fecha"


def sha256(ruta: Path) -> str:
    h = hashlib.sha256()
    with ruta.open("rb") as fh:
        for bloque in iter(lambda: fh.read(4 * 1024 * 1024), b""):
            h.update(bloque)
    return h.hexdigest()


def exportar_tabla(c, tabla: str, col_fecha: str | None, destino: Path, manifest: dict) -> None:
    import pyarrow as pa
    import pyarrow.parquet as pq

    cols = [r[1] for r in c.execute(f'pragma table_info("{tabla}")')]
    tipos = {r[1]: r[2] for r in c.execute(f'pragma table_info("{tabla}")')}
    esquema = pa.schema([(col, tipo_arrow(tipos.get(col, ""))) for col in cols])
    indice = cols.index(col_fecha) if col_fecha and col_fecha in cols else None

    cur = c.execute(f'select {",".join(chr(34)+x+chr(34) for x in cols)} from "{tabla}"')
    escritores: dict[tuple[str, str], object] = {}
    filas_por_particion: dict[tuple[str, str], list] = defaultdict(list)
    total = 0
    try:
        while True:
            lote = cur.fetchmany(LOTE)
            if not lote:
                break
            for fila in lote:
                total += 1
                clave = particion(fila[indice]) if indice is not None else ("sin_fecha", "sin_fecha")
                filas_por_particion[clave].append(dict(zip(cols, fila)))
            for clave, filas in list(filas_por_particion.items()):
                anio, mes = clave
                est = destino / tabla / f"year={anio}" / f"month={mes}"
                est.mkdir(parents=True, exist_ok=True)
                ruta = est / "parte-000.parquet"
                if clave not in escritores:
                    escritores[clave] = pq.ParquetWriter(str(ruta), esquema, compression=COMPRESION, compression_level=9)
                tab = pa.Table.from_pylist(filas, schema=esquema)
                escritores[clave].write_table(tab)
                filas_por_particion[clave] = []
    finally:
        for w in escritores.values():
            w.close()

    archivos = sorted((destino / tabla).rglob("*.parquet"))
    manifest[tabla] = {
        "filas": c.execute(f'select count(*) from "{tabla}"').fetchone()[0],
        "exportadas": total,
        "particiones": len(archivos),
        "bytes": sum(p.stat().st_size for p in archivos),
        "archivos": [{"ruta": str(p.relative_to(destino)), "bytes": p.stat().st_size, "sha256": sha256(p)} for p in archivos],
    }
    print(f"{tabla:14s} {total:6d} filas | {len(archivos):3d} particiones | {manifest[tabla]['bytes'] / 1e6:8.2f} MB")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DB))
    ap.add_argument("--salida", default=str(SALIDA))
    ap.add_argument("--tablas", default=",".join(TABLAS))
    a = ap.parse_args()

    import pyarrow  # noqa: F401  (falla temprano si no está)
    db = Path(a.db)
    destino = Path(a.salida)
    destino.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=30)
    manifest: dict = {"origen": db.name, "compresion": COMPRESION, "tablas": {}}
    for tabla in [x.strip() for x in a.tablas.split(",") if x.strip()]:
        if tabla not in TABLAS:
            raise SystemExit(f"tabla desconocida: {tabla}")
        exportar_tabla(c, tabla, TABLAS[tabla], destino, manifest["tablas"])
    c.close()
    ruta = destino / "MANIFEST.json"
    ruta.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    total = sum(v["bytes"] for v in manifest["tablas"].values())
    print(f"TOTAL: {total / 1e6:.1f} MB | manifiesto: {ruta.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

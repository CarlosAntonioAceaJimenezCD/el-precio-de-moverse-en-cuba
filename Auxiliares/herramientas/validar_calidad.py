#!/usr/bin/env python3
"""Valida la tabla limpia antes de publicar. Escribe un informe JSON y falla si el ratio malo supera el umbral."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
PARQUET = ROOT / "Data/analisis_rentabilidad/data/listings_clean.parquet"
INFORME = ROOT / "Data/_estado/validacion_calidad.json"
CUARENTENA = ROOT / "Data/_cuarentena"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--umbral", type=float, default=0.10)
    args = ap.parse_args()

    df = pd.read_parquet(PARQUET)
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    reglas = {
        "precio_positivo": df["price_usd"].gt(0),
        "anio_valido": df["year"].isna() | df["year"].between(1990, 2027),
        "km_valido": df["mileage_km"].isna() | df["mileage_km"].le(600_000),
        "moneda_valida": df["currency"].isin(["USD", "EUR", "CUP", "MLC"]),
        "clave_unica": ~df.duplicated(["source", "source_id"]),
        "titulo_valido": df["title"].fillna("").str.strip().str.len().ge(6),
    }
    conteos = {k: int((~v).sum()) for k, v in reglas.items()}
    total = len(df)
    malos = int((~pd.concat(reglas.values(), axis=1).all(axis=1)).sum())
    ratio = malos / total if total else 1.0

    if malos:
        dia = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        dest = CUARENTENA / dia
        dest.mkdir(parents=True, exist_ok=True)
        malas = df[~pd.concat(reglas.values(), axis=1).all(axis=1)]
        malas.to_csv(dest / "listings_clean.csv", index=False)

    datos = {
        "fecha_utc": datetime.now(timezone.utc).isoformat(),
        "filas": total,
        "invalidos": malos,
        "ratio": round(ratio, 4),
        "reglas": conteos,
        "umbral": args.umbral,
        "estado": "ok" if ratio <= args.umbral else "fallo",
    }
    INFORME.parent.mkdir(parents=True, exist_ok=True)
    tmp = INFORME.with_suffix(".tmp")
    tmp.write_text(json.dumps(datos, indent=2), encoding="utf-8")
    tmp.replace(INFORME)
    print(json.dumps(datos))
    if ratio > args.umbral:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

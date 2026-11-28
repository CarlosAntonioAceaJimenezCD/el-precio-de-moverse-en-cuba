#!/usr/bin/env python3
"""Calcula bases de comparación con métrica en datos propios.

Dos predictivas simples: mediana global y mediana por marca. Sus MAE se
publican en `baselines.csv` para que el informe no cite cifras sin archivo.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import config as cfg


def main() -> None:
    df = pd.read_parquet(cfg.DATA / "listings_clean.parquet")
    d = df[(df["source_type"] == "usado") & (df["canal"] == "local") & df["price_usd"].gt(0)].copy()
    filas = []

    mediana = float(d["price_usd"].median())
    filas.append({
        "modelo": "mediana_global",
        "observaciones": len(d),
        "mae_usd": round(float((d["price_usd"] - mediana).abs().mean()), 2),
        "notas": f"mediana fija {mediana:.0f} USD",
    })

    por_marca = d.groupby("brand")["price_usd"].transform("median")
    filas.append({
        "modelo": "mediana_por_marca",
        "observaciones": len(d),
        "mae_usd": round(float((d["price_usd"] - por_marca).abs().mean()), 2),
        "notas": f"{d['brand'].nunique()} marcas",
    })

    pd.DataFrame(filas).to_csv(cfg.TABLES / "baselines.csv", index=False)
    print("BASELINES:", ", ".join(f"{f['modelo']}={f['mae_usd']}" for f in filas))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Contraste entre tiers con prueba e intervalo de confianza bootstrap.

Publica `comparaciones.csv` para que el informe no afirme diferencias sin
test ni incertidumbre cuantificada.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import config as cfg

SEED = int(os.environ.get("PROYECTO_SEED", "20261127"))


def main() -> None:
    df = pd.read_parquet(cfg.DATA / "listings_clean.parquet")
    d = df[
        (df["source_type"] == "usado")
        & (df["canal"] == "local")
        & df["price_usd"].gt(0)
        & df["brand_tier"].notna()
    ].copy()
    grupos = [g["price_usd"].to_numpy() for _, g in d.groupby("brand_tier") if len(g) > 5]
    if len(grupos) < 2:
        raise SystemExit("No hay grupos suficientes para comparar")

    h, p = stats.kruskal(*grupos)

    rng = np.random.default_rng(SEED)
    alto = d[d["brand_tier"] == "premium"]["price_usd"].to_numpy()
    bajo = d[d["brand_tier"] == "economico"]["price_usd"].to_numpy()
    diffs = []
    if len(alto) and len(bajo):
        for _ in range(2000):
            diffs.append(
                float(
                    np.median(rng.choice(alto, len(alto), replace=True))
                    - np.median(rng.choice(bajo, len(bajo), replace=True))
                )
            )
    lo, hi = (float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))) if diffs else (float("nan"), float("nan"))

    pd.DataFrame([{
        "contraste": "precio por tier de marca",
        "n": len(d),
        "estadistico": round(float(h), 3),
        "p_valor": round(float(p), 5),
        "ic_bajo": round(lo, 2),
        "ic_alto": round(hi, 2),
        "metodo": "Kruskal-Wallis + bootstrap de mediana premium-economico (2000 replicas)",
    }]).to_csv(cfg.TABLES / "comparaciones.csv", index=False)
    print(f"COMPARACIONES: n={len(d)} H={h:.3f} p={p:.5f} IC=[{lo:.0f},{hi:.0f}]")


if __name__ == "__main__":
    main()

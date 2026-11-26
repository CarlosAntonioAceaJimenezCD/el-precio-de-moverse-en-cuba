#!/usr/bin/env python3
"""Limpieza y feature engineering. Los rechazos se guardan, nunca se pierden."""
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import config as cfg

GOOD = re.compile(r"buen|excelente|impecable|nuevo|original|full| completo|limpio|cuidado", re.I)
BAD = re.compile(r"mal|reparar|averiado|sin motor|para piezas|chocado|sin papeles", re.I)


def condition_score(text: str) -> int:
    t = text or ""
    return min(5, len(GOOD.findall(t))) - min(5, len(BAD.findall(t)))


def main():
    raw = pd.read_parquet(cfg.DATA / "listings_raw.parquet")
    df = raw.copy()
    reason = pd.Series("", index=df.index)

    def mark(mask, text):
        nonlocal reason
        reason = reason.mask(mask & (reason == ""), text)

    mark(~df["price_usd"].between(cfg.PRICE_MIN_USD, cfg.PRICE_MAX_USD), "precio fuera de rango")
    mark(df["year"].notna() & ~df["year"].between(cfg.YEAR_MIN, cfg.YEAR_MAX), "anio fuera de rango")
    mark(df["title"].isna() | (df["title"].astype(str).str.strip().str.len() < 6), "titulo invalido")
    mark(df["mileage_km"].notna() & (df["mileage_km"] > cfg.MILEAGE_MAX_KM), "kilometraje imposible")

    rejected = df[reason != ""].copy()
    rejected["motivo"] = reason[reason != ""]
    rejected.to_csv(cfg.TABLES / "rechazos.csv", index=False)

    clean = df[reason == ""].copy()
    clean["car_age"] = cfg.CURRENT_YEAR - clean["year"]
    clean["km_per_year"] = (clean["mileage_km"] / clean["car_age"].replace(0, float("nan"))).round(0)
    clean["brand_tier"] = clean["brand"].apply(cfg.brand_tier)
    clean["condition_score"] = clean["description"].fillna("").apply(condition_score)
    clean["price_per_1000km"] = (clean["price_usd"] / (clean["mileage_km"] / 1000).replace(0, float("nan"))).round(2)
    clean["source_type"] = clean["source"].apply(lambda s: "nuevo" if "concesionario" in str(s) else "usado")

    sig = ["brand", "model", "year", "mileage_km", "price_usd", "source_type", "canal"]
    clean = clean.drop_duplicates(subset=sig, keep="last")

    out = cfg.DATA / "listings_clean.parquet"
    clean.to_parquet(out, index=False)
    print(f"LIMPIEZA: {len(clean)} limpios | {len(rejected)} rechazos -> {out}")
    print(clean.groupby(["source_type", "brand_tier"]).size().to_string())


if __name__ == "__main__":
    main()

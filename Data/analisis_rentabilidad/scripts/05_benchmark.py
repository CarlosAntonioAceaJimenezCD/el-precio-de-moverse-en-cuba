#!/usr/bin/env python3
"""Benchmarks de precio y deteccion de infravalorados."""
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import config as cfg


def main():
    df = pd.read_parquet(cfg.DATA / "listings_clean.parquet")
    used = df[(df["source_type"] == "usado") & (df["canal"] == "local")].copy()
    new = df[(df["source_type"] == "nuevo") & (df["canal"] == "local")].copy()
    imported = df[(df["canal"] == "importacion") & df["price_usd"].gt(0)].copy()

    bench = used.groupby(["brand", "model", "year"]).agg(
        n=("price_usd", "size"),
        p25=("price_usd", lambda x: x.quantile(0.25)),
        mediana=("price_usd", "median"),
        p75=("price_usd", lambda x: x.quantile(0.75)),
    ).reset_index()
    bench = bench[bench["n"] >= 2].round(2)
    bench.to_csv(cfg.TABLES / "benchmark.csv", index=False)

    newbench = new.groupby(["brand", "model"]).agg(
        n=("price_usd", "size"), mediana_nuevo=("price_usd", "median")
    ).reset_index()
    newbench.to_csv(cfg.TABLES / "benchmark_nuevos.csv", index=False)

    bench_ren = bench[["brand", "model", "year", "n", "mediana"]].rename(columns={"mediana": "mediana_grupo"})
    merged = used.merge(bench_ren, on=["brand", "model", "year"], how="left")
    merged["descuento_pct"] = (
        (merged["mediana_grupo"] - merged["price_usd"]) / merged["mediana_grupo"] * 100
    ).round(1)
    infra = merged[merged["n"] >= 2].nsmallest(30, "descuento_pct")[
        ["url", "title", "brand", "model", "year", "price_usd", "mediana_grupo", "descuento_pct"]
    ]
    infra.to_csv(cfg.TABLES / "infravalorados.csv", index=False)

    if not newbench.empty:
        gap = used.merge(newbench, on=["brand", "model"], how="inner")
        gap["gap_vs_nuevo_pct"] = ((gap["mediana_nuevo"] - gap["price_usd"]) / gap["mediana_nuevo"] * 100).round(1)
        gap[["url", "title", "brand", "model", "year", "price_usd", "mediana_nuevo", "gap_vs_nuevo_pct"]].to_csv(
            cfg.TABLES / "gap_usado_nuevo.csv", index=False
        )

    if not imported.empty:
        imp = (
            imported.groupby("brand")
            .agg(
                n=("price_usd", "size"),
                p25=("price_usd", lambda x: x.quantile(0.25)),
                mediana=("price_usd", "median"),
                p75=("price_usd", lambda x: x.quantile(0.75)),
            )
            .sort_values("n", ascending=False)
            .round(2)
        )
        imp.to_csv(cfg.TABLES / "importacion_por_marca.csv")

    print(f"BENCHMARK: {len(bench)} grupos | {len(infra)} infravalorados | {len(newbench)} benchmarks nuevos | {len(imported)} importados")


if __name__ == "__main__":
    main()

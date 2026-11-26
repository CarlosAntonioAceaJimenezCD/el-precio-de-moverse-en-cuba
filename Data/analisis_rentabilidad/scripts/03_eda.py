#!/usr/bin/env python3
"""EDA y KPIs. Genera graficos HTML interactivos y tablas."""
import sys
from pathlib import Path

import pandas as pd
import plotly.express as px

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import config as cfg


def save(fig, name):
    fig.write_html(str(cfg.CHARTS / f"{name}.html"), include_plotlyjs="cdn")


def main():
    cfg.CHARTS.mkdir(parents=True, exist_ok=True)
    df = pd.read_parquet(cfg.DATA / "listings_clean.parquet")
    local = df[df["canal"] == "local"]
    used = local[local["source_type"] == "usado"]
    new = local[local["source_type"] == "nuevo"]
    imported = df[df["canal"] == "importacion"]

    kpis = pd.DataFrame(
        [
            ("anuncios_totales", len(df)),
            ("anuncios_locales", len(local)),
            ("anuncios_importacion", len(imported)),
            ("anuncios_usados_locales", len(used)),
            ("anuncios_nuevos_locales", len(new)),
            ("marcas_distintas", df["brand"].nunique()),
            ("precio_medio_usd", round(used["price_usd"].mean(), 2)),
            ("precio_mediano_usd", round(used["price_usd"].median(), 2)),
            ("anio_mediano", round(used["year"].median(), 1)),
            ("km_medianos", round(used["mileage_km"].median(), 0)),
            ("antiguedad_media", round(used["car_age"].mean(), 1)),
        ],
        columns=["metrica", "valor"],
    )
    kpis.to_csv(cfg.TABLES / "kpis.csv", index=False)

    canal = (
        df.groupby(["canal", "source_type"])
        .agg(
            anuncios=("price_usd", "size"),
            mediana_usd=("price_usd", "median"),
            media_usd=("price_usd", "mean"),
        )
        .round(2)
        .reset_index()
    )
    canal.to_csv(cfg.TABLES / "kpis_canal.csv", index=False)

    if not used.empty:
        save(px.histogram(used, x="price_usd", nbins=40, title="Distribucion de precios USD"), "01_precios")
        save(px.histogram(used, x="year", nbins=30, title="Distribucion por anio"), "02_anios")
        top = used["brand"].value_counts().head(15)
        save(px.bar(x=top.index, y=top.values, labels={"x": "marca", "y": "anuncios"}, title="Top marcas"), "03_marcas")
        save(px.box(used.dropna(subset=["brand_tier"]), x="brand_tier", y="price_usd", title="Precio por tier"), "04_tiers")
        save(px.scatter(used.dropna(subset=["mileage_km"]), x="mileage_km", y="price_usd", color="brand_tier", title="Precio vs km"), "05_km_precio")
        save(px.scatter(used.dropna(subset=["car_age"]), x="car_age", y="price_usd", trendline="ols", title="Precio vs antiguedad"), "06_edad_precio")

    by_brand = used.groupby("brand").agg(
        n=("price_usd", "size"), mediana=("price_usd", "median"),
        minimo=("price_usd", "min"), maximo=("price_usd", "max"),
    ).sort_values("n", ascending=False).round(2)
    by_brand.to_csv(cfg.TABLES / "por_marca.csv")

    by_prov = used.groupby("location").agg(n=("price_usd", "size"), mediana=("price_usd", "median")).sort_values("n", ascending=False).round(2)
    by_prov.to_csv(cfg.TABLES / "por_ubicacion.csv")

    print("EDA listo. KPIs:")
    print(kpis.to_string(index=False))
    print("\nPor canal:")
    print(canal.to_string(index=False))


if __name__ == "__main__":
    main()

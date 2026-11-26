#!/usr/bin/env python3
"""Funciones para generar todas las gráficas del análisis de mercado.

Entradas: CSV de Data/analisis y la BD de Revolico (vía analisis_mercado).
Salidas: PNG en Data/analisis/graficos/ y dashboard interactivo en HTML.

Librerías: matplotlib, seaborn, plotly, pandas.

Uso:
    python graficos_mercado.py
    python -c "import graficos_mercado as g; g.grafico_histograma_precios(df)"
"""

from __future__ import annotations

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
from pathlib import Path

from analisis_mercado import ROOT, OUT, add_exchange, load

GRAFICOS = OUT / "graficos"
sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams["figure.figsize"] = (11, 6)
plt.rcParams["axes.titlesize"] = 13


def _save(fig, nombre: str) -> Path:
    GRAFICOS.mkdir(parents=True, exist_ok=True)
    destino = GRAFICOS / nombre
    fig.tight_layout()
    fig.savefig(destino, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return destino


def _precios(df: pd.DataFrame) -> pd.Series:
    col = "precio_cup" if "precio_cup" in df else "price"
    return pd.to_numeric(df[col], errors="coerce").dropna()


def grafico_histograma_precios(df: pd.DataFrame) -> Path:
    """Distribución de precios válidos (USD)."""
    s = pd.to_numeric(df.loc[df["precio_valido"], "price"], errors="coerce").dropna()
    fig, ax = plt.subplots()
    sns.histplot(s, bins=40, kde=True, ax=ax)
    ax.axvline(s.median(), color="crimson", linestyle="--", label=f"Mediana {s.median():,.0f} USD")
    ax.set_title("Distribución de precios anunciados (USD)")
    ax.set_xlabel("Precio (USD)")
    ax.legend()
    return _save(fig, "01_histograma_precios.png")


def grafico_boxplot_marcas(df: pd.DataFrame, min_n: int = 3) -> Path:
    """Boxplot de precios USD por marca estimada."""
    d = df[df["precio_valido"]].dropna(subset=["marca_est"]).copy()
    conteo = d["marca_est"].value_counts()
    d = d[d["marca_est"].isin(conteo[conteo >= min_n].index)]
    orden = d.groupby("marca_est")["price"].median().sort_values(ascending=False).index
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=d, x="marca_est", y="price", order=orden, ax=ax, showfliers=False)
    ax.set_title(f"Precio (USD) por marca estimada (n≥{min_n})")
    ax.set_xlabel("Marca estimada")
    ax.set_ylabel("Precio (USD)")
    ax.tick_params(axis="x", rotation=45)
    return _save(fig, "02_boxplot_marcas.png")


def grafico_barras_municipios(by_muni: pd.DataFrame, top: int = 15) -> Path:
    """Mediana de precio por municipio."""
    d = by_muni.sort_values("mediana", ascending=False).head(top)
    fig, ax = plt.subplots()
    sns.barplot(data=d, x="municipality_name", y="mediana", ax=ax)
    ax.set_title("Precio mediano por municipio (USD)")
    ax.set_xlabel("Municipio")
    ax.set_ylabel("Mediana USD")
    ax.tick_params(axis="x", rotation=45)
    return _save(fig, "03_barras_municipios.png")


def grafico_anios(by_year: pd.DataFrame) -> Path:
    """Precio por año del vehículo en USD y CUP (doble eje)."""
    d = by_year.dropna(subset=["anio_est"]).copy()
    d["anio_est"] = d["anio_est"].astype(int)
    fig, ax1 = plt.subplots()
    ax1.bar(d["anio_est"], d["mediana_usd"], color="steelblue", alpha=0.8, label="Mediana USD")
    ax1.set_xlabel("Año del vehículo (estimado)")
    ax1.set_ylabel("USD", color="steelblue")
    ax2 = ax1.twinx()
    ax2.plot(d["anio_est"], d["mediana_cup"], color="darkorange", marker="o", label="Mediana CUP")
    ax2.set_ylabel("CUP (elTOQUE)", color="darkorange")
    ax1.set_title("Precio por año del vehículo: USD vs CUP")
    fig.legend(loc="upper left")
    return _save(fig, "04_precios_por_anio.png")


def grafico_serie_tasa(serie: pd.DataFrame) -> Path:
    """Serie diaria: precio mediano CUP vs TRMI de elTOQUE."""
    d = serie.copy()
    d["fecha_anuncio"] = pd.to_datetime(d["fecha_anuncio"], errors="coerce")
    d = d.dropna(subset=["fecha_anuncio"]).sort_values("fecha_anuncio")
    fig, ax1 = plt.subplots()
    ax1.plot(d["fecha_anuncio"], d["mediana_cup"], color="darkorange", marker="o", label="Precio mediano CUP")
    ax1.set_ylabel("CUP", color="darkorange")
    ax2 = ax1.twinx()
    ax2.plot(d["fecha_anuncio"], d["tasa_toque"], color="seagreen", marker="s", label="TRMI elTOQUE")
    ax2.set_ylabel("CUP/USD", color="seagreen")
    ax1.set_title("Precio en CUP vs tasa de cambio elTOQUE")
    ax1.tick_params(axis="x", rotation=45)
    fig.legend(loc="upper left")
    return _save(fig, "05_serie_precio_vs_tasa.png")


def grafico_variaciones(serie: pd.DataFrame) -> Path:
    """Variación porcentual de la tasa y del precio CUP."""
    d = serie.copy()
    d["fecha_anuncio"] = pd.to_datetime(d["fecha_anuncio"], errors="coerce")
    d = d.dropna(subset=["fecha_anuncio"]).sort_values("fecha_anuncio")
    fig, ax = plt.subplots()
    ax.plot(d["fecha_anuncio"], d["var_tasa_%"], marker="o", label="Δ TRMI %")
    ax.plot(d["fecha_anuncio"], d["var_cup_%"], marker="s", label="Δ precio CUP %")
    ax.axhline(0, color="grey", linewidth=0.8)
    ax.set_title("Variación diaria: tasa elTOQUE vs precio en CUP")
    ax.set_ylabel("Variación %")
    ax.tick_params(axis="x", rotation=45)
    ax.legend()
    return _save(fig, "06_variaciones_tasa_precio.png")


def grafico_outliers(outliers: pd.DataFrame) -> Path:
    """Anuncios atípicos detectados por IQR."""
    d = outliers.copy()
    d = d.sort_values("price", ascending=False).head(20)
    fig, ax = plt.subplots(figsize=(11, 6))
    sns.barplot(data=d, y="title", x="price", ax=ax)
    ax.set_title("Anuncios atípicos por precio (USD)")
    ax.set_xlabel("Precio (USD)")
    ax.set_ylabel("")
    return _save(fig, "07_outliers.png")


def grafico_cobertura(cobertura: pd.DataFrame) -> Path:
    """Cobertura porcentual de campos."""
    d = cobertura.sort_values("cobertura_%")
    fig, ax = plt.subplots()
    sns.barplot(data=d, y="campo", x="cobertura_%", ax=ax)
    ax.set_title("Cobertura de campos en la base limpia")
    ax.set_xlabel("% de anuncios con dato")
    ax.set_xlim(0, 100)
    return _save(fig, "08_cobertura.png")


def dashboard_plotly(serie: pd.DataFrame, by_year: pd.DataFrame, by_muni: pd.DataFrame) -> Path:
    """Dashboard interactivo HTML con Plotly (sin servidor)."""
    GRAFICOS.mkdir(parents=True, exist_ok=True)
    serie = serie.copy()
    serie["fecha_anuncio"] = pd.to_datetime(serie["fecha_anuncio"], errors="coerce")

    fig_tasa = go.Figure()
    fig_tasa.add_trace(go.Scatter(x=serie["fecha_anuncio"], y=serie["mediana_cup"],
                                  name="Precio CUP", line=dict(color="darkorange")))
    fig_tasa.add_trace(go.Scatter(x=serie["fecha_anuncio"], y=serie["tasa_toque"],
                                  name="TRMI elTOQUE", yaxis="y2", line=dict(color="seagreen")))
    fig_tasa.update_layout(title="Precio CUP vs tasa elTOQUE",
                           yaxis=dict(title="CUP"),
                           yaxis2=dict(title="CUP/USD", overlaying="y", side="right"))

    by_year = by_year.dropna(subset=["anio_est"]).copy()
    fig_year = go.Figure()
    fig_year.add_trace(go.Bar(x=by_year["anio_est"], y=by_year["mediana_usd"], name="USD"))
    fig_year.add_trace(go.Scatter(x=by_year["anio_est"], y=by_year["mediana_cup"],
                                  name="CUP", yaxis="y2", mode="lines+markers"))
    fig_year.update_layout(title="Precio por año del vehículo",
                           yaxis=dict(title="USD"),
                           yaxis2=dict(title="CUP", overlaying="y", side="right"))

    d = by_muni.sort_values("mediana", ascending=False).head(15)
    fig_muni = go.Figure(go.Bar(x=d["municipality_name"], y=d["mediana"]))
    fig_muni.update_layout(title="Precio mediano por municipio (USD)")

    html = "<h1>AutoDecide Habana — dashboard de mercado</h1>"
    html += fig_tasa.to_html(full_html=False, include_plotlyjs="cdn")
    html += fig_year.to_html(full_html=False, include_plotlyjs=False)
    html += fig_muni.to_html(full_html=False, include_plotlyjs=False)
    html = f"<!doctype html><html><head><meta charset='utf-8'></head><body>{html}</body></html>"
    destino = GRAFICOS / "dashboard_interactivo.html"
    destino.write_text(html, encoding="utf-8")
    return destino


def main() -> None:
    GRAFICOS.mkdir(parents=True, exist_ok=True)
    df = add_exchange(load())
    validos = df[df["precio_valido"] & (df["currency"] == "USD")].copy()

    by_muni = pd.read_csv(OUT / "precios_por_municipio.csv")
    by_year = pd.read_csv(OUT / "precios_por_anio.csv")
    serie = pd.read_csv(OUT / "serie_precio_vs_tasa.csv")
    outliers = pd.read_csv(OUT / "outliers.csv")
    cobertura = pd.read_csv(OUT / "cobertura.csv")

    generados = [
        grafico_histograma_precios(validos),
        grafico_boxplot_marcas(validos),
        grafico_barras_municipios(by_muni),
        grafico_anios(by_year),
        grafico_serie_tasa(serie),
        grafico_variaciones(serie),
        grafico_outliers(outliers),
        grafico_cobertura(cobertura),
        dashboard_plotly(serie, by_year, by_muni),
    ]
    print("Gráficas generadas:")
    for g in generados:
        print(" -", g.relative_to(ROOT))


if __name__ == "__main__":
    main()

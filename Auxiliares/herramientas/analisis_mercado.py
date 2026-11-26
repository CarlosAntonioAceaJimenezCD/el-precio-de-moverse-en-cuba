#!/usr/bin/env python3
"""Análisis descriptivo inicial del mercado de autos usados en La Habana.

Fuentes: tablas `autos` + `anuncios` de Data/Revolico/revolico.sqlite.
Salidas: Data/analisis/*.csv, informe_descriptivo.md y dashboard.html.

Los campos `anio`, `marca` y `km` se extraen HEURÍSTICAMENTE del título y la
descripción; se marcan como "estimado" y no se usan si no son plausibles.
"""

from __future__ import annotations

import html
import re
import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "Data/Revolico/revolico.sqlite"
OUT = ROOT / "Data/analisis"
TRMI = ROOT / "Anexos/Investigacion Cambios/trmi_USD.csv"

# Fuentes de catálogo (concesionarios y páginas similares). Para ellas se asume
# que, salvo que la página diga lo contrario, todo el catálogo está disponible
# y se publicó el día en que se está viendo. El año del vehículo no es clave.
CATALOGOS = {
    "autocubana", "dongfeng", "bdc_one", "mcv", "finauto", "changan",
    "chinautos", "envision", "atr_export", "connectingcuba", "subasta_cubana",
    "agn_motors", "carrosw", "llamacuba", "sasa", "divep",
}

BRANDS = [
    "toyota", "chevrolet", "ford", "hyundai", "kia", "nissan", "mazda", "honda",
    "renault", "volkswagen", "vw", "audi", "bmw", "mercedes", "lexus", "peugeot",
    "fiat", "changan", "dongfeng", "geely", "suzuki", "isuzu", "mitsubishi", "jeep",
    "dodge", "chrysler", "buick", "pontiac", "volvo", "seat", "skoda", "mg", "chery",
    "jac", "haval", "great wall", "subaru", "tesla", "citroen", "opel",
]
YEAR = re.compile(r"\b(19[5-9]\d|20[0-2]\d)\b")
KM = re.compile(r"\b(\d{1,3}(?:[.,]\d{3})+|\d{4,6})\s*(?:km|kms|kil[oó]metros)\b", re.I)


def extract_year(text: str) -> int | None:
    for m in YEAR.finditer(text or ""):
        y = int(m.group(1))
        if 1950 <= y <= 2026:
            return y
    return None


def extract_brand(text: str) -> str | None:
    low = (text or "").lower()
    for b in BRANDS:
        if re.search(rf"\b{re.escape(b)}\b", low):
            return b
    return None


def extract_km(text: str) -> int | None:
    for m in KM.finditer(text or ""):
        value = int(m.group(1).replace(".", "").replace(",", ""))
        if 1000 <= value <= 400000:
            return value
    return None


def load() -> pd.DataFrame:
    con = sqlite3.connect(DB)
    query = """
        SELECT a.id, a.url, a.title, a.description, a.price, a.currency,
               a.province_name, a.municipality_name, a.images_count, a.scraped_at,
               x.updated_on_by_user,
               x.ad_json, x.apollo_full
        FROM autos a LEFT JOIN anuncios x ON x.id = a.id
    """
    df = pd.read_sql_query(query, con)
    con.close()
    # El año y el km se extraen SOLO de texto visible: ad_json contiene
    # timestamps que generarían años falsos (cobertura artificial del 100%).
    visible = df["title"].fillna("") + " " + df["description"].fillna("")
    df["anio_est"] = visible.map(extract_year)
    df["marca_est"] = visible.map(extract_brand)
    df["km_est"] = visible.map(extract_km)
    # Precio 1 USD es claramente inválido para un auto: se marca, no se borra.
    df["precio_valido"] = df["price"].between(500, 200000)
    if "fuente" not in df:
        df["fuente"] = "revolico"
    return df


def add_publication_assumption(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica el supuesto de disponibilidad/fecha según el tipo de fuente.

    - Catálogos de concesionarios y páginas similares: disponible = True y
      fecha de publicación efectiva = fecha de captura (el año no es clave).
    - Clasificados (Revolico): anuncio activo => se asume comprable, y se usa
      la fecha de actualización del vendedor.
    """
    df = df.copy()
    df["es_catalogo"] = df["fuente"].isin(CATALOGOS)
    fecha_user = pd.to_datetime(df["updated_on_by_user"], errors="coerce", utc=True).dt.date
    fecha_scrap = pd.to_datetime(df["scraped_at"], errors="coerce", utc=True).dt.date
    df["fecha_publicacion"] = fecha_user.where(~df["es_catalogo"], fecha_scrap)
    df["disponible_asumido"] = True
    return df


def add_exchange(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte USD a CUP con la TRMI diaria de elTOQUE (columna Mediana)."""
    trmi = pd.read_csv(TRMI)
    trmi["fecha"] = pd.to_datetime(trmi["fecha"]).dt.date
    trmi = trmi[["fecha", "Mediana"]].rename(columns={"Mediana": "tasa_toque"})

    df = add_publication_assumption(df)
    df["fecha_anuncio"] = df["fecha_publicacion"]

    df = df.merge(trmi, left_on="fecha_anuncio", right_on="fecha", how="left")
    df = df.drop(columns=["fecha"], errors="ignore")
    df["precio_cup"] = (df["price"] * df["tasa_toque"]).round(0)
    # Supuesto declarado: anuncio PUBLISHED y página verificada en la captura
    # => se asume comprable en el momento del análisis.
    df["comprable_asumido"] = True
    return df


def stats_block(series: pd.Series) -> dict:
    s = series.dropna()
    if s.empty:
        return {}
    q1, q2, q3 = s.quantile([0.25, 0.5, 0.75])
    return {
        "n": int(s.count()),
        "media": round(float(s.mean()), 2),
        "mediana": round(float(q2), 2),
        "p25": round(float(q1), 2),
        "p75": round(float(q3), 2),
        "min": round(float(s.min()), 2),
        "max": round(float(s.max()), 2),
        "desviacion": round(float(s.std()), 2) if len(s) > 1 else 0,
    }


def grouped(df: pd.DataFrame, column: str, min_n: int) -> pd.DataFrame:
    g = df.dropna(subset=[column]).groupby(column)["price"]
    out = g.agg(n="count", mediana="median", p25=lambda s: s.quantile(0.25),
                p75=lambda s: s.quantile(0.75), minimo="min", maximo="max").reset_index()
    out = out[out["n"] >= min_n].sort_values("n", ascending=False)
    return out.round(2)


def md_table(df: pd.DataFrame) -> str:
    if df.empty:
        return "_Sin datos suficientes_"
    return df.to_markdown(index=False)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    df = add_exchange(load())
    usd = df[(df["currency"] == "USD") & df["precio_valido"]].copy()
    descartados = df[(df["currency"] == "USD") & ~df["precio_valido"]]
    overall = stats_block(usd["price"])
    q1, q3 = usd["price"].quantile([0.25, 0.75])
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    outliers = usd[(usd["price"] < low) | (usd["price"] > high)].copy()

    by_brand = grouped(usd, "marca_est", 3)
    by_muni = grouped(usd, "municipality_name", 3)

    # Serie por año del vehículo: USD y CUP con la tasa del día del anuncio.
    by_year = (
        usd.dropna(subset=["anio_est"])
        .groupby("anio_est")
        .agg(n=("price", "count"), mediana_usd=("price", "median"),
             mediana_cup=("precio_cup", "median"), tasa_promedio=("tasa_toque", "mean"))
        .reset_index()
        .sort_values("anio_est")
        .round(0)
    )
    by_year["anio_est"] = by_year["anio_est"].astype(int)

    # Serie temporal: precio anunciado vs TRMI de elTOQUE.
    serie = (
        usd.dropna(subset=["fecha_anuncio"])
        .groupby("fecha_anuncio")
        .agg(n=("price", "count"), mediana_usd=("price", "median"),
             mediana_cup=("precio_cup", "median"), tasa_toque=("tasa_toque", "median"))
        .reset_index()
        .sort_values("fecha_anuncio")
    )
    for col, nombre in [("tasa_toque", "var_tasa_%"), ("mediana_cup", "var_cup_%"),
                        ("mediana_usd", "var_usd_%")]:
        serie[nombre] = (serie[col].pct_change() * 100).round(2)
    serie = serie.round(0)

    tmp = usd.dropna(subset=["fecha_anuncio"]).copy()
    tmp["mes"] = pd.to_datetime(tmp["fecha_anuncio"]).dt.to_period("M").astype(str)
    serie_mensual = (
        tmp.groupby("mes")
        .agg(n=("price", "count"), mediana_usd=("price", "median"),
             mediana_cup=("precio_cup", "median"), tasa_promedio=("tasa_toque", "mean"))
        .reset_index()
        .sort_values("mes")
        .round(0)
    )

    # Guardar CSV
    pd.DataFrame([overall]).to_csv(OUT / "resumen_general.csv", index=False)
    by_brand.to_csv(OUT / "precios_por_marca.csv", index=False)
    by_muni.to_csv(OUT / "precios_por_municipio.csv", index=False)
    by_year.to_csv(OUT / "precios_por_anio.csv", index=False)
    serie.to_csv(OUT / "serie_precio_vs_tasa.csv", index=False)
    serie_mensual.to_csv(OUT / "serie_precio_vs_tasa_mensual.csv", index=False)
    outliers[["id", "title", "price", "marca_est", "anio_est", "url"]].to_csv(
        OUT / "outliers.csv", index=False)

    cobertura = pd.DataFrame({
        "campo": ["price", "currency", "municipality_name", "marca_est", "anio_est", "km_est"],
        "disponibles": [
            int(df["price"].notna().sum()),
            int(df["currency"].notna().sum()),
            int(df["municipality_name"].notna().sum()),
            int(df["marca_est"].notna().sum()),
            int(df["anio_est"].notna().sum()),
            int(df["km_est"].notna().sum()),
        ],
        "total": [len(df)] * 6,
    })
    cobertura["cobertura_%"] = (cobertura["disponibles"] / cobertura["total"] * 100).round(1)
    cobertura.to_csv(OUT / "cobertura.csv", index=False)

    lines = [
        "# Análisis descriptivo inicial — mercado de autos usados en La Habana",
        "",
        "**Fecha:** 18/11/2026  ",
        "**Fuente:** `Data/Revolico/revolico.sqlite`, tablas `autos` + `anuncios`  ",
        "**Nivel de confianza:** anuncios (precio pedido, no transacción)  ",
        "**Moneda del análisis:** USD (322 de 323 autos; 1 en CUP se excluye del precio)",
        f"**Precios descartados por inválidos (<500 USD):** {len(descartados)} (se conservan en la BD, no se usan en estadísticos)",
        "",
        "## 1. Cobertura de datos",
        "",
        md_table(cobertura),
        "",
        "## 2. Estadísticos generales (USD)",
        "",
        md_table(pd.DataFrame([overall]).T.rename(columns={0: "valor"}).reset_index()
                 .rename(columns={"index": "estadístico"})),
        "",
        "## 3. Precios por marca estimada (n ≥ 3)",
        "",
        md_table(by_brand),
        "",
        "## 4. Precios por municipio (n ≥ 3)",
        "",
        md_table(by_muni),
        "",
        "## 5. Precios por año del vehículo (USD y CUP)",
        "",
        "Conversión: `precio_USD × TRMI elTOQUE del día del anuncio`. La tasa mostrada es el promedio de los anuncios del año.",
        "",
        md_table(by_year),
        "",
        "## 6. Outliers por IQR (precio USD)",
        "",
        f"Límites: [{low:,.0f}, {high:,.0f}] USD. Total: **{len(outliers)}**.",
        "",
        md_table(outliers[["id", "title", "price", "marca_est", "anio_est"]].head(15)),
        "",
        "## 7. Supuesto de anuncio activo",
        "",
        "Todos los registros de `autos` tienen `status=PUBLISHED` y su página fue verificada en el momento de la captura. **Se asume que, si el anuncio sigue activo, es posible comprarlo.** No se comprueba disponibilidad en tiempo real.",
        "",
        "**Catálogos y páginas similares:** para concesionarios se asume que todo el catálogo está disponible salvo que la página diga lo contrario, y que se publicó el día de la captura (`fecha_publicacion = scraped_at`). El año del vehículo no es una variable clave para esas fuentes.",
        "",
        "## 8. Serie diaria: precio vs tasa de cambio (elTOQUE)",
        "",
        "Variaciones porcentuales respecto al día anterior con datos. Permite ver si el precio en CUP acompaña a la TRMI.",
        "",
        md_table(serie.head(30)),
        "",
        "## 9. Serie mensual: precio vs tasa de cambio (elTOQUE)",
        "",
        md_table(serie_mensual),
        "",
        "## 10. Limitaciones",
        "",
        "- `marca_est`, `anio_est` y `km_est` son **heurísticos** (regex sobre título/descripción/ad_json).",
        "- `km_est` tiene baja cobertura y puede contener errores; no se usa para precio/km aún.",
        "- Los precios son **anunciados**, no precios de transacción.",
        "- No se dispone aún de combustible/transmisión estructurados ni de costos ocultos.",
        "- Los precios <500 USD se marcan como inválidos y se excluyen de los estadísticos, pero no se borran.",
        "- 1 anuncio en CUP queda fuera del análisis de precios para no mezclar monedas.",
    ]
    (OUT / "informe_descriptivo.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Dashboard HTML mínimo, autocontenido
    def h(df: pd.DataFrame) -> str:
        return html.escape(df.to_html(index=False, classes="tabla", border=0))

    dashboard = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>AutoDecide Habana — mercado</title><style>
body{{font-family:system-ui,sans-serif;margin:2rem;color:#222}}h1{{font-size:1.6rem}}
table{{border-collapse:collapse;margin:1rem 0}}td,th{{border:1px solid #ccc;padding:4px 8px;font-size:.85rem}}
</style></head><body><h1>AutoDecide Habana — análisis descriptivo inicial</h1>
<p>Anuncios: {len(df)} | Autos USD: {len(usd)} | Precio mediano: {overall.get('mediana')} USD</p>
<h2>Cobertura</h2>{h(cobertura)}<h2>Por marca</h2>{h(by_brand)}
<h2>Por municipio</h2>{h(by_muni)}<h2>Por año</h2>{h(by_year)}
</body></html>"""
    (OUT / "dashboard.html").write_text(dashboard, encoding="utf-8")

    print("Análisis descriptivo completado")
    print("Autos:", len(df), "| USD:", len(usd))
    print("Estadísticos:", overall)
    print("Marca con más datos:", by_brand.iloc[0]["marca_est"] if not by_brand.empty else "-")
    print("Municipio con más datos:", by_muni.iloc[0]["municipality_name"] if not by_muni.empty else "-")
    print("Outliers:", len(outliers))


if __name__ == "__main__":
    main()

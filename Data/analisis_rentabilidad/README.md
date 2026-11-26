# Análisis de rentabilidad y relación calidad-precio

Basado en la arquitectura de `Egyptian-Used-Cars`, adaptado a **El precio de moverse en Cuba**.

## Principios

1. **Incremental e idempotente:** la ingesta usa `source + source_id` como clave; volver a correr no duplica.
2. **Por lotes:** cada script procesa Parquet, no toda la BD en memoria; al crecer los datos se particiona por `source` y `year`.
3. **Configurable:** marcas, tiers, tipos de cambio y umbrales viven en `config.py`.
4. **Trazable:** cada anuncio conserva `url`, `source` y `scraped_at`. Nada se descarta sin registro: los rechazos van a `outputs/tables/rechazos.csv`.
5. **Separación de responsabilidades:** `data/` (datos), `outputs/` (gráficos/tablas), `sql/` (consultas), `notebooks/` (exploración).

## Fuentes que se ingieren

| Fuente | Ubicación | Uso |
|---|---|---|
| Revolico (solo carros, tabla `autos`) | `Data/Revolico/revolico.sqlite` | Precios de usados, depreciación, anomalías |
| Concesionarios (11 BDs) | `Data/catalogos_concesionarios/*.sqlite` | Precios de autos nuevos como benchmark |
| Marketplaces (8 BDs) | `Data/catalogos_concesionarios/marketplaces/*.sqlite` | Anuncios adicionales: se recuperan precios del JSON-LD, se descartan no-autos/spam/precios que son modelo o año y se separa importación (`canal`) |

## Flujo

```text
01_ingest.py   -> data/listings_raw.parquet + outputs/tables/descartes_marketplaces.csv
02_clean.py    -> data/listings_clean.parquet + outputs/tables/rechazos.csv
03_eda.py      -> outputs/charts/*.html + outputs/tables/kpis.csv + kpis_canal.csv
04_stats.py    -> outputs/tables/modelo_depreciacion.csv, vif.csv, tests.csv
05_benchmark.py-> outputs/tables/benchmark.csv, infravalorados.csv, importacion_por_marca.csv
run_all.py     -> ejecuta todo en orden
```

## Ejecución

```bash
cd Auxiliares
.venv/bin/python ../Data/analisis_rentabilidad/scripts/run_all.py
```

## Necesidades para completar el análisis

Ver `NECESIDADES.md`. Los puntos críticos son el historial de precios y los campos estructurados. La conversión usa la **TRMI informal** de elTOQUE (18/11/2026), nunca la tasa oficial.

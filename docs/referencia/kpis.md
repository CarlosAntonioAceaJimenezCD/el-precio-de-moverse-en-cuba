# KPIs y evidencia del modelo

Página de referencia generada desde los CSV del pipeline. Si cambia el análisis, vuelve a generar el sitio.

## KPIs generales

| metrica | valor |
|---|---|
| anuncios_totales | 2174.0 |
| anuncios_locales | 1483.0 |
| anuncios_importacion | 691.0 |
| anuncios_usados_locales | 1462.0 |
| anuncios_nuevos_locales | 21.0 |
| marcas_distintas | 50.0 |
| precio_medio_usd | 28201.06 |
| precio_mediano_usd | 21000.0 |
| anio_mediano | 2020.0 |
| km_medianos | 32569.0 |
| antiguedad_media | 8.1 |

## Por canal

| canal | source_type | anuncios | mediana_usd | media_usd |
|---|---|---|---|---|
| importacion | usado | 691 | 26000.0 | 27046.22 |
| local | nuevo | 21 | 24623.66 | 24729.59 |
| local | usado | 1462 | 21000.0 | 28201.06 |

## Coeficientes del modelo

| termino | coeficiente | p_valor | intervalo_bajo | intervalo_alto |
|---|---|---|---|---|
| Intercept | 12.0884 | 0.0 | 10.263 | 13.9138 |
| C(brand_tier)[T.economico] | -1.0208 | 0.1421 | -2.4141 | 0.3726 |
| C(brand_tier)[T.medio] | -0.978 | 0.0941 | -2.1384 | 0.1825 |
| C(brand_tier)[T.premium] | 0.1146 | 0.8753 | -1.39 | 1.6193 |
| car_age | -0.0632 | 0.1504 | -0.1514 | 0.025 |
| np.log1p(mileage_km) | -0.0333 | 0.4711 | -0.1278 | 0.0612 |
| hp | -0.0036 | 0.1403 | -0.0085 | 0.0013 |
| condition_score | -0.0254 | 0.8168 | -0.2508 | 0.2001 |

El p_valor mínimo vigente es 0,165: ningún coeficiente es significativo con la base actual.

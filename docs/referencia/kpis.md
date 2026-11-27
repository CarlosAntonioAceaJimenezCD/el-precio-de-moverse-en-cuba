# KPIs y evidencia del modelo

Página de referencia generada desde los CSV del pipeline. Si cambia el análisis, vuelve a generar el sitio.

## KPIs generales

| metrica | valor |
|---|---|
| anuncios_totales | 2029.0 |
| anuncios_locales | 1338.0 |
| anuncios_importacion | 691.0 |
| anuncios_usados_locales | 1317.0 |
| anuncios_nuevos_locales | 21.0 |
| marcas_distintas | 50.0 |
| precio_medio_usd | 28665.42 |
| precio_mediano_usd | 21000.0 |
| anio_mediano | 2020.0 |
| km_medianos | 43000.0 |
| antiguedad_media | 8.3 |

## Por canal

| canal | source_type | anuncios | mediana_usd | media_usd |
|---|---|---|---|---|
| importacion | usado | 691 | 26000.0 | 27046.22 |
| local | nuevo | 21 | 24623.66 | 24729.59 |
| local | usado | 1317 | 21000.0 | 28665.42 |

## Coeficientes del modelo

| termino | coeficiente | p_valor | intervalo_bajo | intervalo_alto |
|---|---|---|---|---|
| Intercept | 12.4469 | 0.0 | 9.5622 | 15.3316 |
| C(brand_tier)[T.economico] | -1.1228 | 0.3279 | -3.498 | 1.2525 |
| C(brand_tier)[T.medio] | -1.2332 | 0.2391 | -3.3844 | 0.918 |
| C(brand_tier)[T.premium] | 0.0662 | 0.9474 | -2.0481 | 2.1805 |
| car_age | -0.0708 | 0.237 | -0.1936 | 0.0521 |
| np.log1p(mileage_km) | -0.0226 | 0.7398 | -0.1659 | 0.1207 |
| hp | -0.0046 | 0.1648 | -0.0114 | 0.0021 |
| condition_score | -0.034 | 0.8022 | -0.3194 | 0.2514 |

El p_valor mínimo vigente es 0,165: ningún coeficiente es significativo con la base actual.

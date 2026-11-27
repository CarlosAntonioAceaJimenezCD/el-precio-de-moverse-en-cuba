# Qué aportan los anuarios del ONEI (23/11/2026)

Se revisaron los 12 anuarios (2014–2025), sus 233 archivos y las hojas de la capítulo 13. Las series extraídas están en `series_oficiales.csv`.

## 1. Demanda de transporte (capítulo 13.1)

| Año | Pasajeros (millones) | En ómnibus |
|---|---:|---:|
| 2014 | 1.855,8 | 1.037,4 |
| 2019 | 1.899,9 | 1.102,2 |
| 2020 | 1.118,7 | 622,8 |
| 2021 | 749,5 | 502,2 |
| 2022 | 1.010,6 | 557,9 |
| 2023 | 1.006,4 | 479,0 |
| 2024 | 880,9 | 357,5 |
| 2025 | 781,1 | 324,0 |

El transporte de pasajeros en 2025 está **un 59 % por debajo de 2019**; el ómnibus cayó un 71 %. Esto coincide con la narrativa del proyecto sobre restricciones de movilidad y explica parte de la presión sobre el precio de los autos usados.

## 2. Seguridad vial (capítulo 13.11)

| Año | Accidentes | Fallecidos | Lesionados |
|---|---:|---:|---:|
| 2021 | 8.373 | 590 | 5.858 |
| 2022 | 9.848 | 705 | 7.542 |
| 2023 | 8.557 | 729 | 6.938 |
| 2024 | 7.511 | 636 | 6.617 |
| 2025 | 7.552 | 751 | 6.729 |

Los accidentes bajaron un 23 % desde 2022, pero los fallecidos subieron un 6 % en 2025: la **gravedad por accidente empeora** (9,9 fallecidos por cada 100 accidentes en 2025 frente a 7,0 en 2021).

## 3. Lo que los anuarios NO aportan

Se buscó explícitamente `parque automotor`, `matriculaciones`, `inventario de vehículos` y `vehículos por provincia` en los PDF y hojas Excel: **no hay series de parque automotor ni de matriculaciones**. El ONEI publica demanda y seguridad vial, no stock de vehículos. Por tanto:

- La laguna identificada en `NECESIDADES.md` sobre "parque automotor" **no se resuelve con los anuarios descargados**.
- Las cifras de `Vehículos automotores` que aparecen en el capítulo de sector externo son **comercio exterior** (exportaciones/importaciones), no parque circulante; no deben confundirse.
- Para stock y matriculaciones haría falta una fuente distinta (Dirección de Tránsito/MININT), que no publica estadísticas abiertas según la búsqueda previa.

## 4. Uso en el proyecto

Estas series fortalecen el contexto de demanda y seguridad del storytelling y del informe técnico, pero **no alteran los KPIs de precios** (1.973 anuncios, mediana local 21.000 USD). Se incorporan como evidencia oficial, separadas de los microdatos de anuncios.

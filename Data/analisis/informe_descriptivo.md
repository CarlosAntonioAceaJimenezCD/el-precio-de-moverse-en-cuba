# Análisis descriptivo inicial — mercado de autos usados en La Habana

**Fecha:** 18/11/2026  
**Fuente:** `Data/Revolico/revolico.sqlite`, tablas `autos` + `anuncios`  
**Nivel de confianza:** anuncios (precio pedido, no transacción)  
**Moneda del análisis:** USD (322 de 323 autos; 1 en CUP se excluye del precio)
**Precios descartados por inválidos (<500 USD):** 74 (se conservan en la BD, no se usan en estadísticos)

## 1. Cobertura de datos

| campo             |   disponibles |   total |   cobertura_% |
|:------------------|--------------:|--------:|--------------:|
| price             |           323 |     323 |         100   |
| currency          |           323 |     323 |         100   |
| municipality_name |           323 |     323 |         100   |
| marca_est         |           221 |     323 |          68.4 |
| anio_est          |           205 |     323 |          63.5 |
| km_est            |            20 |     323 |           6.2 |

## 2. Estadísticos generales (USD)

| estadístico   |   valor |
|:--------------|--------:|
| n             |   248   |
| media         | 24416.6 |
| mediana       | 22000   |
| p25           | 11375   |
| p75           | 35000   |
| min           |   600   |
| max           | 95000   |
| desviacion    | 16649.3 |

## 3. Precios por marca estimada (n ≥ 3)

| marca_est   |   n |   mediana |   p25 |   p75 |   minimo |   maximo |
|:------------|----:|----------:|------:|------:|---------:|---------:|
| hyundai     |  55 |     28000 | 20250 | 35000 |     5000 |    83000 |
| kia         |  20 |     21500 | 18500 | 33925 |    15500 |    34000 |
| toyota      |  18 |     14000 | 11500 | 33000 |     3800 |    42000 |
| chevrolet   |  11 |     18000 | 13750 | 22000 |     7000 |    28000 |
| honda       |  11 |     27000 | 24675 | 29500 |    12000 |    38000 |
| audi        |  10 |     41000 | 17500 | 45000 |     8000 |    95000 |
| peugeot     |  10 |      7500 |  5000 | 15000 |     5000 |    16000 |
| nissan      |   8 |     25500 | 16000 | 30250 |     7800 |    40000 |
| fiat        |   6 |      4750 |  2625 |  8750 |     1800 |    28000 |
| mercedes    |   5 |     52000 | 25000 | 60000 |    25000 |    80000 |
| mg          |   5 |     15000 | 15000 | 15000 |    15000 |    26500 |
| bmw         |   4 |     33500 | 28625 | 47500 |    18500 |    85000 |
| dongfeng    |   4 |     31500 | 28000 | 35000 |    28000 |    35000 |
| geely       |   4 |     10250 |  8825 | 11250 |     6800 |    12000 |
| ford        |   3 |     10000 |  7250 | 22500 |     4500 |    35000 |
| vw          |   3 |     36000 | 19750 | 37500 |     3500 |    39000 |

## 4. Precios por municipio (n ≥ 3)

| municipality_name     |   n |   mediana |   p25 |     p75 |   minimo |   maximo |
|:----------------------|----:|----------:|------:|--------:|---------:|---------:|
| Playa                 |  46 |     23750 | 18875 | 36000   |      650 |    85000 |
| Cerro                 |  33 |     24000 | 11500 | 34000   |     1100 |    95000 |
| Arroyo Naranjo        |  29 |     28000 | 11000 | 37000   |     2000 |    45000 |
| Centro Habana         |  26 |     27000 | 18500 | 34000   |      600 |    65000 |
| Plaza                 |  24 |     17750 |  9500 | 22000   |     1600 |    43000 |
| Habana del Este       |  21 |     34000 | 16000 | 45000   |     2000 |    75000 |
| Diez de Octubre       |  16 |     15000 |  8375 | 26506.2 |     4000 |    48300 |
| Boyeros               |  12 |     14000 |  5000 | 23625   |     5000 |    40000 |
| La Lisa               |   8 |     13500 | 10000 | 31250   |     3800 |    35000 |
| Marianao              |   7 |     15000 | 15000 | 20250   |     9500 |    45000 |
| Habana Vieja          |   4 |     16750 |  7000 | 29375   |     7000 |    38000 |
| San Miguel del Padrón |   4 |     11250 |  8375 | 13000   |     3500 |    14500 |
| Pinar del Río         |   3 |     30000 | 21500 | 34000   |    13000 |    38000 |

## 5. Precios por año del vehículo (USD y CUP)

Conversión: `precio_USD × TRMI elTOQUE del día del anuncio`. La tasa mostrada es el promedio de los anuncios del año.

|   anio_est |   n |   mediana_usd |   mediana_cup |   tasa_promedio |
|-----------:|----:|--------------:|--------------:|----------------:|
|       1950 |   1 |         12000 |   1.104e+07   |             920 |
|       1955 |   1 |          4000 |   3.68e+06    |             920 |
|       1957 |   5 |         22000 |   1.881e+07   |             868 |
|       1958 |   1 |         12500 |   1.0625e+07  |             850 |
|       1962 |   1 |          4500 |   4.14e+06    |             920 |
|       1978 |   1 |         13500 |   1.242e+07   |             920 |
|       1998 |   1 |          5000 |   4.6e+06     |             920 |
|       2002 |   1 |          8000 |   7.36e+06    |             920 |
|       2005 |   6 |         11500 |   1.058e+07   |             918 |
|       2006 |   2 |         15750 |   1.44512e+07 |             918 |
|       2008 |   2 |         16000 |   1.472e+07   |             920 |
|       2009 |   3 |         10000 |   9.2e+06     |             920 |
|       2011 |   1 |         22000 |   2.024e+07   |             920 |
|       2012 |   1 |         70000 |   6.44e+07    |             920 |
|       2015 |   2 |         19250 |   1.771e+07   |             920 |
|       2016 |   3 |         17000 |   1.564e+07   |             920 |
|       2017 |  17 |         24675 |   2.2701e+07  |             920 |
|       2018 |   6 |         18000 |   1.656e+07   |             920 |
|       2019 |  20 |         19000 |   1.748e+07   |             895 |
|       2020 |  11 |         21000 |   1.932e+07   |             833 |
|       2021 |  18 |         28750 |   2.645e+07   |             920 |
|       2022 |  28 |         33450 |   3.0774e+07  |             919 |
|       2023 |  16 |         32000 |   2.944e+07   |             920 |
|       2024 |  16 |         35350 |   3.2522e+07  |             920 |
|       2025 |   5 |         28000 |   2.576e+07   |             920 |
|       2026 |   9 |         35000 |   3.22e+07    |             919 |

## 6. Outliers por IQR (precio USD)

Límites: [-24,062, 70,438] USD. Total: **5**.

|       id | title                                                  |   price | marca_est   |   anio_est |
|---------:|:-------------------------------------------------------|--------:|:------------|-----------:|
| 52651826 | Mercedes Benz C300e 2022 híbrido gasolina y electrico. |   80000 | mercedes    |       2022 |
| 57875714 | Audi e-tron GT performance  2023 con 23 mil millas     |   95000 | audi        |       2023 |
| 58348032 | HYUNDAI PALISADE CALLIGRAPHY 2026                      |   83000 | hyundai     |       2026 |
| 56412195 | 🔥 INFINITI QX60 2025 – 7 PLAZAS 🔥                      |   75000 | nan         |       2025 |
| 58733654 | BMW X6 M50i 2020                                       |   85000 | bmw         |       2020 |

## 7. Supuesto de anuncio activo

Todos los registros de `autos` tienen `status=PUBLISHED` y su página fue verificada en el momento de la captura. **Se asume que, si el anuncio sigue activo, es posible comprarlo.** No se comprueba disponibilidad en tiempo real.

## 8. Serie diaria: precio vs tasa de cambio (elTOQUE)

Variaciones porcentuales respecto al día anterior con datos. Permite ver si el precio en CUP acompaña a la TRMI.

| fecha_anuncio   |   n |   mediana_usd |   mediana_cup |   tasa_toque |   var_tasa_% |   var_cup_% |   var_usd_% |
|:----------------|----:|--------------:|--------------:|-------------:|-------------:|------------:|------------:|
| 2026-07-09      |   4 |         18500 |    1.258e+07  |          680 |          nan |         nan |         nan |
| 2026-10-19      |   4 |         15000 |    1.215e+07  |          810 |           19 |          -3 |         -19 |
| 2026-10-28      |   1 |         12500 |    1.0625e+07 |          850 |            5 |         -13 |         -17 |
| 2026-10-29      |   4 |         22000 |    1.881e+07  |          855 |            1 |          77 |          76 |
| 2026-10-30      |   1 |         35000 |    3.0275e+07 |          865 |            1 |          61 |          59 |
| 2026-11-11      |   1 |          8500 |    7.7775e+06 |          915 |            6 |         -74 |         -76 |
| 2026-11-15      |  23 |         15000 |    1.3725e+07 |          915 |            0 |          76 |          76 |
| 2026-11-16      | 203 |         24000 |    2.208e+07  |          920 |            1 |          61 |          60 |
| 2026-11-17      |   7 |         24675 |    2.2701e+07 |          920 |            0 |           3 |           3 |

## 9. Serie mensual: precio vs tasa de cambio (elTOQUE)

| mes     |   n |   mediana_usd |   mediana_cup |   tasa_promedio |
|:--------|----:|--------------:|--------------:|----------------:|
| 2026-07 |   4 |         18500 |     1.258e+07 |             680 |
| 2026-10 |  10 |         18500 |     1.548e+07 |             838 |
| 2026-11 | 234 |         22500 |     2.07e+07  |             919 |

## 10. Limitaciones

- `marca_est`, `anio_est` y `km_est` son **heurísticos** (regex sobre título/descripción/ad_json).
- `km_est` tiene baja cobertura y puede contener errores; no se usa para precio/km aún.
- Los precios son **anunciados**, no precios de transacción.
- No se dispone aún de combustible/transmisión estructurados ni de costos ocultos.
- Los precios <500 USD se marcan como inválidos y se excluyen de los estadísticos, pero no se borran.
- 1 anuncio en CUP queda fuera del análisis de precios para no mezclar monedas.

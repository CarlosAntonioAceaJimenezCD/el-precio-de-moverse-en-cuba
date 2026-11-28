# Anexo: cuadros y gráficos

<a id="apoyos"></a>

Estos apoyos se insertan aquí para que la narrativa no se detenga. Cada cuadro se puede actualizar desde los CSV del pipeline sin tocar el texto.

<a id="cuadro-1"></a>

### Cuadro 1. KPIs del mercado

| Métrica | Valor |
|---|---:|
| Anuncios limpios | <!-- kpi:anuncios_totales -->2.174 |
| Locales | <!-- kpi:anuncios_locales -->1.483 |
| De importación | <!-- kpi:anuncios_importacion -->691 |
| Usados locales | <!-- kpi:anuncios_usados_locales -->1.462 |
| Nuevos locales | <!-- kpi:anuncios_nuevos_locales -->21 |
| Marcas distintas | <!-- kpi:marcas_distintas -->50 |
| Precio medio local | <!-- kpi:precio_medio_usd -->28.201,06 USD |
| Precio mediano local | <!-- kpi:precio_mediano_usd -->21.000 USD |
| Año mediano | <!-- kpi:anio_mediano -->2020 |
| Kilometraje mediano | <!-- kpi:km_medianos -->32.569 km |
| Antigüedad media | <!-- kpi:antiguedad_media -->8,1 años |

<a id="cuadro-2"></a>

### Cuadro 2. Mercado local e importación

| Canal | Tipo | Anuncios | Mediana USD | Media USD |
|---|---|---:|---:|---:|
| Importación | Usado | <!-- kpi:anuncios_importacion -->691 | <!-- kpi:mediana_importacion -->26.000 USD | <!-- kpi:media_importacion -->27.046,22 USD |
| Local | Nuevo | 21 | 24.623,66 | 24.729,59 |
| Local | Usado | <!-- kpi:anuncios_usados_locales -->1.462 | <!-- kpi:mediana_local -->21.000 USD | <!-- kpi:media_local_usada -->28.201,06 USD |

<a id="cuadro-3"></a>

### Cuadro 3. Pasajeros transportados (ONEI, millones)

| Año | Total | En ómnibus |
|---|---:|---:|
| 2014 | 1.855,8 | 1.037,4 |
| 2019 | 1.899,9 | 1.102,2 |
| 2020 | 1.118,7 | 622,8 |
| 2021 | 749,5 | 502,2 |
| 2022 | 1.010,6 | 557,9 |
| 2023 | 1.006,4 | 479,0 |
| 2024 | 880,9 | 357,5 |
| 2025 | 781,1 | 324,0 |

<a id="cuadro-4"></a>

### Cuadro 4. Seguridad vial (ONEI)

| Año | Accidentes | Fallecidos | Lesionados |
|---|---:|---:|---:|
| 2021 | 8.373 | 590 | 5.858 |
| 2022 | 9.848 | 705 | 7.542 |
| 2023 | 8.557 | 729 | 6.938 |
| 2024 | 7.511 | 636 | 6.617 |
| 2025 | 7.552 | 751 | 6.729 |

<a id="cuadro-5"></a>

### Cuadro 5. Modelo de depreciación (coeficientes vigentes)

| Término | Coeficiente | p_valor |
|---|---:|---:|
| Intercepto | 12,4469 | 0,000 |
| Económico | −1,1228 | 0,328 |
| Medio | −1,2332 | 0,239 |
| Premium | 0,0662 | 0,947 |
| Antigüedad | −0,0708 | 0,237 |
| log(km) | −0,0226 | 0,740 |
| Potencia | −0,0046 | 0,165 |
| Condición | −0,0340 | 0,802 |

Ningún coeficiente resulta estadísticamente significativo con la base actual. Es parte de la historia: el mercado no admite una curva única. La tabla `modelo_muestra.csv` documenta las 22 observaciones de este modelo frente a las 572 del modelo principal; la pendiente positiva de este último refleja la selección de anuncios con kilometraje declarado y no se interpreta como depreciación.

### Gráficos

<a id="grafico-1"></a>

- [Gráfico 1. Distribución de precios](../graficos/01_precios.html)
<a id="grafico-2"></a>

- [Gráfico 2. Distribución por año](../graficos/02_anios.html)
<a id="grafico-3"></a>

- [Gráfico 3. Top marcas](../graficos/03_marcas.html)
<a id="grafico-4"></a>

- [Gráfico 4. Precio por tier](../graficos/04_tiers.html)
<a id="grafico-5"></a>

- [Gráfico 5. Precio vs km](../graficos/05_km_precio.html)
<a id="grafico-6"></a>

- [Gráfico 6. Precio vs antigüedad](../graficos/06_edad_precio.html)

---

**El precio de moverse en Cuba** · `~/Proyectos/El precio de moverse en Cuba`

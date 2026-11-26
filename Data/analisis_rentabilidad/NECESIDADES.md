# Lo que falta para igualar o superar el análisis de Egyptian-Used-Cars

Línea base actualizada (20/11/2026) tras la deduplicación de `autos`, la reparación de precios y la separación de canales.

| Métrica | Egipto | ICD hoy | Brecha |
|---|---:|---:|---:|
| Anuncios de usados | 23.500+ | **1.973** (1.301 locales + 672 importación) | ×12 |
| Grupos marca/modelo/año con n≥2 | cientos | **98** | ×3+ |
| Historial de precios | mensual, 12+ meses | **1 snapshot** | crítico |
| Potencia (HP) estructurada | sí | **<30 válidos** | crítico |
| Kilometraje estructurado | sí | **mediana 0 km** | crítico |
| Combustible/transmisión/carrocería | sí | parcial (texto) | alto |
| Tipo de cambio informal (TRMI) | sí | **930 CUP/USD (elTOQUE 18/11)** | cubierto |
| Nuevos para benchmark | sí | **9 grupos** | parcial |
| VIF / OLS / tests / anomalías | sí | **implementado** | cubierto |
| Dashboard | Tableau + Power BI | Plotly HTML | equivalente funcional |

## Fuentes detectadas para integrar

El listado `Data/fuentes-adicionales-2026-11-20.md` documenta 25 fuentes nuevas (oficiales, compraventa, concesionarios, divisas y datos abiertos). Las prioridades de integración son la API de tasas del BCC, el Anuario ONEI 2025, el catálogo de Womy y los históricos de Clasificados.st y TecnoTáctil. La Res. 312/2026 de Aduana está derogada por la 340/2026.

## Prioridad 1 — Datos (lo crítico)

1. **Mantener actualizados los 8 marketplaces** (ya hay 8 BDs con datos; revisar cobertura y frescor): Cogetucarro, iTENCEL, VentaCuba, Autocubana, Timbirichi, Cubisima, Carros.com y Apululu. Tras la reparación aportan ~1.200 anuncios válidos, además de los 744 de Revolico.
2. **Historial de precios**: guardar un snapshot semanal de cada anuncio (`price`, `fecha`, `source_id`) durante 6–12 meses. Sin esto no hay curva de depreciación real, solo un corte transversal.
3. **Campos estructurados en la ficha**: kilometraje real, potencia HP, cilindrada, combustible, transmisión, tracción, carrocería, puertas, asientos, estado/condición, año. Hoy están en `text`/`apollo_full` pero no como columnas.
4. **Normalización de marca/modelo/versión**: alias de marcas y modelos para agrupar (ej. Hyundai/Sonata, Hyunday/Santa Fe).

## Prioridad 2 — Fuentes externas (puedo buscarlas yo con tu permiso)

5. **Serie histórica de TRMI informal (elTOQUE)** USD↔CUP y MLC↔CUP, para fechar cada anuncio con la tasa vigente.
6. **Parque automotor y matriculaciones**: se verificaron los 12 anuarios del ONEI (2014–2025) y **no contienen series de stock ni de matriculaciones**; solo demanda y seguridad vial (ver `Data/fuentes-oficiales/ONEI/ANALISIS_DATO.md`). Hace falta una fuente distinta (MININT/Dirección de Tránsito), que no publica datos abiertos.
7. **Aranceles e impuestos** de la Gaceta 65/2026 (Resoluciones 171–175 y 312) para modelar el precio final de importación.
8. **Listas de precios de autos nuevos** de BDC One, Dongfeng, Finauto, Changan, Chinautos y ATR Export con modelo y precio estructurados.

## Prioridad 3 — Ingeniería

9. Particionar Parquet por `source/year` y programar ingesta incremental con systemd timer.
10. Revisión online periódica de anuncios (la `verificar_online()` de Egipto) para caídas y cambios de precio.
11. Dashboard único en Plotly con filtros por marca/año/provincia (sustituye Tableau/Power BI).

## Lo que ya está cubierto

- Ingesta incremental e idempotente, limpieza con rechazos registrados, EDA con 6 gráficos, OLS con VIF, tests de Kruskal-Wallis, detección de anomalías, benchmarks y infravalorados, SQL con window functions y notebook.
- El código está listo para crecer: al añadir filas, los mismos scripts recalculan todo.

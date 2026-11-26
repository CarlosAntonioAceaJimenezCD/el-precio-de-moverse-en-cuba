# Histórico de tasas de cambio informales (elTOQUE / Cubanomic)

**Descargado:** 16 de noviembre de 2026
**Pregunta:** ¿hasta qué año llegan los registros de la base de datos de elTOQUE?

## Respuesta corta

**Los registros diarios empiezan el 1 de enero de 2021 y llegan hasta el 17 de noviembre de 2026** (el 17-Nov aparece como fila preliminar por el huso horario; el último día completo local es el 16-Nov-2026). Es decir, la base cubre **2021, 2022, 2023, 2024, 2025 y 2026**. No hay registros anteriores a 2021 en esta serie: el 1-ene-2021 coincide con el ordenamiento monetario cubano, momento en que elTOQUE empezó a publicar la TRMI (tasa representativa del mercado informal).

Para el dólar estadounidense hay **2.144 observaciones diarias**; la mediana pasó de **40 CUP/USD** el 1-ene-2021 a **920 CUP/USD** el 16-nov-2026, con un máximo de 935 CUP el 8-nov-2026.

## Cómo se obtuvo

1. `eltoque.com` y `api.eltoque.com` rechazan las conexiones TLS directas desde este entorno; las páginas se recuperaron con la Wayback Machine.
2. La API oficial de elTOQUE (`https://tasas.eltoque.com/docs/`) exige una clave que se solicita por formulario; no se usó.
3. Dentro de la propia página de elTOQUE (`/tasas-de-cambio-cuba`) el gráfico «Comportamiento histórico» está incrustado desde `https://iframe.cubanomic.com/chart`. El código JavaScript de ese mismo gráfico expone un botón público **«Descargar TRMI»** que apunta a:
   `https://api.cubanomic.com/api/v1/download-excel/all-days-stats`
4. Ese Excel contiene la serie diaria completa, calculada con la misma metodología de mediana de ofertas del mercado informal que elTOQUE muestra en su sitio. Se descargó sin clave y se exportó a CSV. No es un scraping de noticias: es el volcado oficial del panel que elTOQUE incrusta.

## Archivos descargados

**Formato principal de trabajo: JSON.** Todos los registros están exportados también a CSV para hojas de cálculo.

| Archivo | Contenido |
|---|---|
| `resumen.json` | Metadatos: fuente, total de registros, rango global, años y cobertura por moneda |
| `trmi_diario_todas_las_monedas.json` | Serie completa en JSON: 10.581 objetos (fecha, moneda, ofertas, mínimo, máximo, promedio, medianas) |
| `trmi_USD.json`, `trmi_ECU.json`, … | Un array JSON por moneda, con números como números y `null` en celdas vacías |
| `trmi_all_days.xlsx` | Excel original (11 hojas, una por moneda), 454 KB |
| `trmi_diario_todas_las_monedas.csv` | Serie unificada en CSV: 10.581 filas |
| `trmi_USD.csv`, `trmi_ECU.csv`, `trmi_MLC.csv`, … | Una serie por moneda (ECU = euro en la nomenclatura de la base) |
| `formal-rates-history.xlsx` | Histórico de tasas oficiales (2021-09-20 a 2026-11-16) |
| `median-by-hour.xlsx` | Medianas por hora (2025-11-16 a 2026-11-16) |
| `all-days-crypto-stats.xlsx` | Estadísticas diarias de criptomonedas (2021-01-04 a 2026-11-16) |
| `resumen_rango.txt` | Rango de fechas y conteo por moneda |

## Cobertura por moneda

| Moneda (hoja) | Registros | Primer dato | Último dato |
|---|---:|---|---|
| USD | 2.144 | 2021-01-01 | 2026-11-17 |
| ECU (euro) | 2.145 | 2021-01-02 | 2026-11-17 |
| MLC | 2.141 | 2021-01-04 | 2026-11-16 |
| CAD | 1.446 | 2021-03-24 | 2026-11-17 |
| GBP | 1.004 | 2021-02-02 | 2026-11-10 |
| MXN | 992 | 2021-04-29 | 2026-11-16 |
| CHF | 518 | 2021-01-21 | 2026-09-21 |
| RUR | 90 | 2021-07-28 | 2026-11-08 |
| FRF | 98 | 2021-02-04 | 2024-12-13 |
| DOP | 2 | 2021-06-29 | 2025-11-06 |
| JPY | 1 | 2021-02-23 | 2021-02-23 |

El histórico oficial de tasas formales (BCC) incluido en `formal-rates-history.xlsx` empieza más tarde: **20 de septiembre de 2021**.

## Salvedades

- Los valores son **medianas de ofertas de compraventa del mercado informal**, no tasas oficiales. elTOQUE los define como valores de referencia.
- Las columnas «Mediana - Compra» y «Mediana - Venta» solo aparecen en fechas recientes (cuando el panel empezó a separar ambas medianas).
- La fila del 17-nov-2026 tiene muy pocas ofertas (11 compra, 10 venta), por lo que conviene usar el 16-nov como último dato consolidado.
- La fuente detrás del panel cambió de dominio (`api.cubanomic.com` → `api.cambiocuba.money`); ambos sirven el mismo dataset.

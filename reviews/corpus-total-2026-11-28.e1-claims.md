---
type: audit-artifact
phase: e1-claims
slug: corpus-total-2026-11-28
generated_at: 2026-11-28T23:59:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/corpus-total-2026-11-28/corpus-total-2026-11-28.text.md
language: es
---

# Claim Inventory

## Summary

- Total: 115
- Load-bearing: 15 · Supporting: 70 · Contextual: 30
- By type: result 64 · methodological 27 · novelty 2 · contextual 32 · definitional 10 · citation-grounded 33

> Convención: los números de línea son absolutos dentro del documento cacheado (10 archivos concatenados). `⚠️ CONTRADICCIÓN` marca afirmaciones que chocan con otro archivo del corpus o con los CSV de `Data/analisis_rentabilidad/outputs/tables/`. `ᵛ` marca cifras de corridas históricas ya superadas por la vigente.

## Load-bearing claims

### C001 — H1: los tres tiers de marca provienen de la misma distribución (y se rechaza)

- **File**: `INFORME_TECNICO.md` (ES §Resumen, línea 30; EN §Abstract, línea 172); `README.md` línea 1716
- **Lines**: 30, 172, 1716
- **Types**: result, methodological
- **Excerpt**: «**Hipótesis falsable (H1):** «los precios de los tres tiers de marca en el mercado local provienen de la misma distribución, controlando por antigüedad y kilometraje». Se contrasta con Kruskal-Wallis; se rechaza con p < 0,001 en la corrida vigente.»
- **Restated**: El test de Kruskal-Wallis aplicado a los precios por tier rechaza la hipótesis de igualdad de distribución con p < 0,001 en la corrida vigente.
- **Internal evidence cited**: §60 (línea 1418), §71.3 (línea 1537), `MODELOS_Y_FUNCIONES.md` §3.3 (líneas 2118–2122), `tests.csv`, `comparaciones.csv`
- **External evidence cited**: —
- **Notes**: ⚠️ **CONTRADICCIÓN metodológica interna**: el enunciado dice «controlando por antigüedad y kilometraje», pero `tests.csv` registra solo «Kruskal-Wallis precio por tier» (n=1.462, H=44,313, p=0,0), un contraste no ajustado; `MODELOS_Y_FUNCIONES.md` línea 2122 describe el test como comparación de distribuciones completas sin covariables. El rechazo en sí sí coincide con el CSV.

### C002 — La novedad declarada es de procedencia y normalización, no de algoritmo

- **File**: `INFORME_TECNICO.md` (ES §Resumen, línea 27; EN §Abstract, línea 169); `README.md` línea 1758
- **Lines**: 27, 169, 1558, 1758
- **Types**: novelty, methodological
- **Excerpt**: «**Novedad:** la procedencia y la normalización se tratan como objeto de auditoría; la pérdida de muestra por variables ausentes se reporta como hallazgo y no se oculta.»
- **Restated**: El aporte original del proyecto es la auditoría de procedencia/normalización y el reporte de pérdida de muestra, no un método nuevo de predicción.
- **Internal evidence cited**: §71.6 (línea 1558), §69 (línea 1498), `MODELOS_Y_FUNCIONES.md` §4 (líneas 2138–2144)
- **External evidence cited**: [14], [26], [9], [29] (contraste en §71.6)
- **Novelty signals**: «Novedad» (27, 169); «el aporte es de procedencia y normalización, no de algoritmo» (1558); «el diferenciador declarado» (1758)
- **Notes**: Afirmación de posicionamiento; no falsifiable por CSV, sí por cotejo con trabajos citados.

### C003 — Cuatro contribuciones: base compacta, panel autocontenido, timers y 13 artefactos de auditoría

- **File**: `INFORME_TECNICO.md` (ES §Resumen, línea 28; EN §Abstract, línea 170); `README.md` línea 1768
- **Lines**: 28, 170, 2317, 1428
- **Types**: result, novelty
- **Excerpt**: «**Contribuciones:** base compacta reproducible, panel interactivo autocontenido, pipeline con timers y un expediente de auditoría con 13 artefactos.»
- **Restated**: El proyecto entrega cuatro artefactos verificables: base compacta reproducible, panel sin dependencias externas, pipeline con timers y expediente de 13 artefactos.
- **Internal evidence cited**: §69 (línea 1498), §61 (línea 1428), `ARQUITECTURA_DATOS.md` §0 (líneas 2157–2166), `AUTOMATIZACION.md` §2 (línea 2317)
- **External evidence cited**: —
- **Notes**: ⚠️ **Tensión entre archivos**: `AUTOMATIZACION.md` línea 2317 describe «un solo `Data/dashboard.html` … sin peticiones externas» de 107 KB, mientras `INFORME_TECNICO.md` línea 1428 describe el panel vigente como `Data/dashboard.html` **más seis gráficos Plotly copiados** y enlazados; ambas versiones se dicen vigentes.

### C004 — El R² citado como 0,277 se corrigió a 0,274 contra el CSV

- **File**: `INFORME_TECNICO.md` §69 (líneas 1498, 1500)
- **Lines**: 1498, 1500
- **Types**: methodological, result
- **Excerpt**: «Un ejemplo del contraste: la revisión detectó un R² citado como 0,277 que el CSV daba como 0,274 y se corrigió con marcadores.»
- **Restated**: El valor correcto del R² del modelo completo es 0,2744, según `modelo_muestra.csv`.
- **Internal evidence cited**: `modelo_muestra.csv` (`completo,r2=0.2744`), §59 (línea 1410), `MODELOS_Y_FUNCIONES.md` línea 2108
- **External evidence cited**: —
- **Notes**: Coherente con el CSV y con los marcadores `<!-- kpi:modelo_r2_completo -->` (líneas 1410, 2108, 2110).

### C005 — La corrida vigente no sostiene una tasa de depreciación anual significativa

- **File**: `INFORME_TECNICO.md` §59 (línea 1410), §60 (línea 1418), §71.2 (línea 1533); `MODELOS_Y_FUNCIONES.md` líneas 2108–2110; `PRESENTACION_STORYTELLING.md` línea 1855
- **Lines**: 1410, 1418, 1533, 1855, 2108, 2110
- **Types**: result
- **Excerpt**: «La depreciación se reformuló con honestidad: el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra.»
- **Restated**: En el modelo completo vigente, el coeficiente de `car_age` (−0,0632, p=0,1504) no es estadísticamente significativo, por lo que no se puede afirmar una depreciación anual.
- **Internal evidence cited**: `modelo_depreciacion.csv`, `modelo_muestra.csv`, Cuadro 5 (líneas 2026–2035), §71.4 (línea 1546)
- **External evidence cited**: —
- **Notes**: Contrasta explícitamente con el −5,43 % anual p<0,001 de la primera corrida (línea 1085) y con §45 (línea 1243); ambas cifras antiguas están marcadas como históricas. ᵛ

### C006 — La prima premium dejó de ser significativa

- **File**: `INFORME_TECNICO.md` §59 (línea 1410), §60 (línea 1418); `PRESENTACION_STORYTELLING.md` líneas 1889, 2029; `MODELOS_Y_FUNCIONES.md` línea 2108
- **Lines**: 1410, 1418, 1889, 2029, 2108
- **Types**: result
- **Excerpt**: «En una primera lectura parecía que la marca funcionaba como un **seguro de valor**; con los datos corregidos, esa prima premium dejó de ser significativa y ya no podemos ponerle un número fijo.»
- **Restated**: El coeficiente `C(brand_tier)[T.premium]` del modelo completo es 0,1146 con p=0,8753, por lo que la prima premium no es significativa.
- **Internal evidence cited**: `modelo_depreciacion.csv` (p=0,8753), Cuadro 5 líneas 2029, 2035
- **External evidence cited**: —
- **Notes**: ⚠️ **CONTRADICCIÓN histórica no señalizada en el propio pasaje**: §34 línea 1085 afirma «primas de +21 % para premium» y §44 línea 1235 las repite como «primas premium de +21 %»; el texto de §44 sí advierte que la depreciación ya no se sostiene, pero no que la prima tampoco.

### C007 — Los tiers no provienen de la misma distribución de precios (Kruskal-Wallis)

- **File**: `INFORME_TECNICO.md` §60 (línea 1418), §71.3 (línea 1537); `MODELOS_Y_FUNCIONES.md` §3.3 (líneas 2120–2122)
- **Lines**: 1418, 1537, 2120, 2122
- **Types**: result
- **Excerpt**: «Resultado vigente: H = <!-- kpi:kw_h -->44,313 p = <!-- kpi:kw_p -->0,00000»
- **Restated**: El contraste de Kruskal-Wallis sobre 1.462 anuncios produce H=44,313 y p<0,001, rechazando la igualdad de distribución entre tiers.
- **Internal evidence cited**: `tests.csv`, `comparaciones.csv` (`ic_bajo=10000`, `ic_alto=29500`, 2.000 réplicas)
- **External evidence cited**: —
- **Notes**: Cifras coinciden con ambos CSV. El IC bootstrap de la diferencia premium−económico se reporta solo en §71.3 y `comparaciones.csv`, no en el resumen.

### C008 — Tamaño muestral de los modelos: 993 candidatas, 28 completas, 586 principales

- **File**: `INFORME_TECNICO.md` §59 (línea 1410), §60 (línea 1418); `MODELOS_Y_FUNCIONES.md` líneas 2108–2110; `PRESENTACION_STORYTELLING.md` línea 2035
- **Lines**: 1410, 1418, 2035, 2108, 2110, 1524, 1525, 1531
- **Types**: result, methodological
- **Excerpt**: «el modelo completo (con `hp`), frente al modelo principal sin ese término, dispone de **<!-- kpi:modelo_n_completo -->28 observaciones completas** de <!-- kpi:modelo_candidatas -->993 candidatas (R² = <!-- kpi:modelo_r2_completo -->0,274; p del F = <!-- kpi:modelo_pf_completo -->0,411)»
- **Restated**: El modelo completo usa 28 de 993 candidatas (R²=0,2744) y el principal 586 de 993 (R²=0,1008).
- **Internal evidence cited**: `modelo_muestra.csv` (`principal,993,586,0.1008,0.0`; `completo,993,28,0.2744,0.4114`)
- **External evidence cited**: —
- **Notes**: ⚠️ **CONTRADICCIÓN contra CSV y contra otros archivos**: `INFORME_TECNICO.md` §71.1 línea 1524 afirma «Las 981 candidatas y las 8 fuentes» y §71.2 líneas 1531/1533 afirman «584 observaciones de 981 candidatas» y «R² … de 0,274 a 0,101»; el CSV y §59/§60/`MODELOS_Y_FUNCIONES.md` dan **993 y 586**. El propio §71.1 línea 1525 repite «584 observaciones».

### C009 — KPIs vigentes del mercado: 2.174 anuncios limpios, 974 autos, mediana 21.000 USD

- **File**: `README.md` líneas 1623, 1653; `PRESENTACION_STORYTELLING.md` líneas 1781, 1853, 1871, 1979–1989; `INFORME_TECNICO.md` §59 línea 1408
- **Lines**: 1408, 1623, 1653, 1781, 1853, 1871, 1979, 1989
- **Types**: result
- **Excerpt**: «**Resultado esperado:** <!-- kpi:anuncios_totales -->2.174 anuncios limpios (<!-- kpi:anuncios_locales -->1.483 locales + <!-- kpi:anuncios_importacion -->691 de importación), mediana local <!-- kpi:precio_mediano_usd -->21.000 USD.»
- **Restated**: La corrida vigente produce 2.174 anuncios limpios (1.483 locales + 691 de importación), 974 autos únicos de Revolico, mediana local 21.000 USD, 50 marcas, 114 grupos y 89 anomalías.
- **Internal evidence cited**: `kpis.csv`, `kpis_canal.csv`, `benchmark_result.csv` (114 grupos), `anomalias.csv`, §59 línea 1408
- **External evidence cited**: —
- **Notes**: Cifras coinciden con los CSV. ⚠️ **Ambigüedad de alcance**: `README.md` línea 1623 suma «974 autos de Revolico + 2.232 anuncios de 8 marketplaces + 256 vehículos de 11 concesionarios», mientras `kpis.csv` contabiliza 2.174 limpios; el corpus no explica si 2.232 es el crudo previo a limpieza o una población distinta.

### C010 — Conversión monetaria con TRMI informal fija de 930 CUP/USD del 18/11/2026

- **File**: `README.md` línea 1684; `MODELOS_Y_FUNCIONES.md` línea 2067; `INFORME_TECNICO.md` §52 línea 1326, §23 línea 931; `PRESENTACION_STORYTELLING.md` línea 1900
- **Lines**: 931, 1326, 1900, 2067, 1684
- **Types**: methodological, definitional
- **Excerpt**: «La conversión usa la **TRMI informal de elTOQUE (18/11/2026): 930 CUP/USD, 1.000 CUP/EUR y 845,35 CUP/MLC**. Nunca se usa la tasa oficial para los precios del mercado.»
- **Restated**: Todos los precios se convierten con la TRMI informal fechada 930 CUP/USD, 1.000 CUP/EUR y 845,35 CUP/MLC, excluyendo la tasa oficial.
- **Internal evidence cited**: `config.py` (citado en líneas 931, 1326, 2067), `AUTOMATIZACION.md` línea 2305
- **External evidence cited**: elTOQUE; BCC como referencia oficial no usada
- **Notes**: Coherente entre archivos; la serie diaria `trmi_USD.csv` queda declarada como referencia histórica (línea 931). ᵛ

### C011 — Marco normativo vigente: Decreto 163/2026 y 312/2026 derogada por 340/2026

- **File**: `INFORME_TECNICO.md` §4 línea 76, §12 línea 154, §52 línea 1332, §20 línea 895; `README.md` línea 1770; `PRESENTACION_STORYTELLING.md` línea 1903
- **Lines**: 76, 154, 895, 1332, 1770, 1903
- **Types**: contextual, citation-grounded
- **Excerpt**: «**Hallazgo normativo crítico:** la **Resolución 312/2026 de la Aduana General fue derogada por la Resolución 340/2026**. Se actualizaron las referencias […] para conservar la trazabilidad sin citar 312 como norma vigente.»
- **Restated**: La resolución aduanera vigente es la 340/2026, no la 312/2026, dentro del marco del Decreto 163/2026.
- **Internal evidence cited**: §4 (Gaceta 65/2026, 17 empresas), §52 línea 1332
- **External evidence cited**: Gaceta Oficial No. 65 Ordinaria (04/08/2026)
- **Notes**: ⚠️ **CONTRADICCIÓN interna no corregida**: `INFORME_TECNICO.md` §20 línea 895 sigue listando «resoluciones 104/17/52/171-175/**312**/102 de 2026» como marco normativo, pese a que §52, el README y el storytelling la dan por derogada.

### C012 — Los anuarios del ONEI no contienen series de parque automotor ni matriculaciones

- **File**: `INFORME_TECNICO.md` §53 línea 1346, §56 línea 1380; `PRESENTACION_STORYTELLING.md` línea 1803, Cuadro 3/4 líneas 1999–2020
- **Lines**: 1346, 1380, 1803, 1999, 2020
- **Types**: result
- **Excerpt**: «**No hay series de parque automotor ni de matriculaciones**, por lo que esa laguna signalada en `NECESIDADES.md` no se resuelve con los anuarios; la corrección quedó registrada.»
- **Restated**: Los 12 anuarios del ONEI descargados no permiten incorporar parque automotor ni matriculaciones; solo pasajeros y seguridad vial.
- **Internal evidence cited**: `Data/fuentes-oficiales/ONEI/series_oficiales.csv`, Cuadro 3 (781,1 M pasajeros 2025; 324,0 M en ómnibus), Cuadro 4 (751 fallecidos / 7.552 accidentes)
- **External evidence cited**: ONEI Anuario Estadístico 2014–2025
- **Notes**: ⚠️ **CONTRADICCIÓN directa entre secciones del mismo archivo**: §53 línea 1346 afirma que el capítulo 13 «permite incorporar parque automotor, matriculaciones y accidentes con series oficiales 2014–2025», exactamente lo que §56 línea 1380 niega. El storytelling usa solo pasajeros y seguridad vial, coherente con §56.

### C013 — Los precios son pedidos, no transaccionados; la validez externa se limita a La Habana

- **File**: `INFORME_TECNICO.md` §18 líneas 855, 860, §19 línea 884, §71.4 líneas 1543–1546
- **Lines**: 855, 860, 884, 1543, 1546
- **Types**: definitional, methodological
- **Excerpt**: «**Externa:** solo La Habana y anuncios en línea; los precios son pedidos, no transaccionados.»
- **Restated**: Todas las cifras de precio describen anuncios habaneros de venta, no operaciones cerradas, y no se generalizan a Cuba ni a precios de transacción.
- **Internal evidence cited**: §18 tabla de procedencia (líneas 845–858), §71.4
- **External evidence cited**: —
- **Notes**: Salvedad central de validez; coherente con §MODELOS líneas 2140–2144 («no se imputan…», «no se afirma causalidad»).

### C014 — La estimación de retención es inferencia de diseño, no medición

- **File**: `INFORME_TECNICO.md` §63 línea 1446; `ALCANCE_Y_RETENCION.md` líneas 2233, 2249–2262
- **Lines**: 1446, 2233, 2249, 2262
- **Types**: methodological
- **Excerpt**: «La estimación de retención (`Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md`) es **inferencia de diseño, no medición**: de cada 100 visitantes, ~58 leerían el primer párrafo, ~16 llegarían al cierre y ~5 volverían con intención de consulta.»
- **Restated**: El proyecto no tiene analytics: las cifras 58/16/5 y la proyección 22–25/18–22 son supuestos de diseño, no observaciones.
- **Internal evidence cited**: `ALCANCE_Y_RETENCION.md` §2 tabla (líneas 2253–2260)
- **External evidence cited**: —
- **Notes**: Declaración de honestidad; impide usar esas cifras como resultado empírico.

### C015 — La encuesta y las entrevistas son contexto, no datos experimentales; sin nombres publicados

- **File**: `INFORME_TECNICO.md` §71.15 líneas 1562–1564, §50 línea 1298; `PRESENTACION_STORYTELLING.md` línea 1909; `README.md` línea 1770
- **Lines**: 1298, 1562, 1564, 1770, 1909
- **Types**: methodological, definitional
- **Excerpt**: «No se reclutaron sujetos humanos: la encuesta de 33 respuestas y las entrevistas se tratan como documentación de contexto, no como datos experimentales; no se requirió un procedimiento de anonimización ejecutado.»
- **Restated**: Las 33 respuestas y 68 entrevistas se usan solo como contexto agregado; los nombres del grupo de AutosxCuba no se publican.
- **Internal evidence cited**: §50 (33 respuestas, 30+30+8 entrevistas), `README.md` línea 1770
- **External evidence cited**: —
- **Notes**: ⚠️ **Aparente contradicción numérica explicada**: §50 línea 1298 dice «17 de 18–25 prefieren eléctrico» y el storytelling línea 1909 dice «14 prefieren eléctrico» de 28 interesados; §51 línea 1314 documenta el cambio de filtro (`interes=1`, 29→28), por lo que ambas cifras corresponden a bases distintas.

## Supporting claims (70)

### C016 — 17 empresas autorizadas y precios de referencia en EUR

- **File**: `INFORME_TECNICO.md` §4 (ES línea 76, EN línea 218)
- **Lines**: 76, 218
- **Types**: result, citation-grounded
- **Excerpt**: «Se documentaron **17 empresas autorizadas** a importar y comercializar vehículos […] (BDC One 14.849–31.478 EUR; Dongfeng desde 21.900 EUR; Finauto desde 15.500 EUR; ATR Export con 46 modelos)»
- **Restated**: El marco regulatorio documenta 17 importadores autorizados y cuatro referencias de precio en EUR.
- **Notes**: Coherente con §12 línea 154 y storytelling línea 1903 («abrió el mercado a 17 empresas autorizadas»).

### C017 — 409 resultados, 400 únicos y 35 sitios inventariados

- **File**: `INFORME_TECNICO.md` §5 líneas 80, 222
- **Lines**: 80, 222
- **Types**: result
- **Excerpt**: «Se consolidaron **409 resultados, 400 únicos**. Se inventariaron **35 sitios** de compraventa»
- **Restated**: La fase de descubrimiento consolidó 409 resultados (400 únicos) e inventarió 35 sitios de compraventa.
- **Notes**: Cifras ES/EN coincidentes.

### C018 — 40 sitios verificados y nueve marketplaces con sección activa

- **File**: `INFORME_TECNICO.md` §5 líneas 82, 224, §12 línea 153
- **Lines**: 82, 153, 224
- **Types**: result
- **Excerpt**: «Se verificaron **40 sitios/URLs**. Marketplaces con sección activa: Autocubana (667 vehículos), iTENCEL (951), VentaCuba (801 carros/camionetas), Timbirichi (281 carros), Revolico (112 enlaces en la primera página), Cogetucarro (5.225 anuncios), Cubisima (155 fichas)»
- **Restated**: Se verificaron 40 URLs y se identificaron nueve marketplaces con inventario real.
- **Notes**: ⚠️ **Aparente contradicción de conteo**: el README (líneas 1623, 1678) y el resumen hablan de «8 marketplaces»; aquí se enumeran nueve contando a Revolico, que luego se trata como fuente separada. ⚠️ También los conteos de Autocubana (667) y Timbirichi (281) superan los de §39 línea 1156 (566 y 170, ya en 18/11).

### C019 — 14 organismos con competencia sobre el mercado

- **File**: `INFORME_TECNICO.md` §5 líneas 84, 226
- **Lines**: 84, 226
- **Types**: result
- **Excerpt**: «Se documentaron **14 organismos** con competencia sobre el mercado: Consejo de Ministros/Estado, MINCEX, MINCIN, MITRANS, CEMA, MFP, ONAT, Aduana General, BCC, MININT, MINJUS, MEP, MINREX y MINSAP.»
- **Restated**: El corpus documenta 14 organismos estatales con competencia normativa sobre el mercado automotor.

### C020 — 61 repositorios clonados, 92 proyectos CAPTCHA clasificados, 9 seleccionados

- **File**: `INFORME_TECNICO.md` §6 líneas 88, 230
- **Lines**: 88, 230
- **Types**: result
- **Excerpt**: «Se clonaron **61 repositorios** en `Auxiliares/Repositorios` con `--depth 1` (2,2 GB, 61 entradas `OK`) […] Se clasificaron **92 proyectos** de CAPTCHA […] y se seleccionaron 9.»
- **Restated**: La infraestructura incluye 61 clones y una clasificación de 92 proyectos anti-CAPTCHA de los que 9 se adoptaron.
- **Notes**: Coherente con §55 línea 1368 («33 repositorios auxiliares, 7 cubanos»), que es un subconjunto posterior.

### C021 — Versiones fijadas del entorno de scraping

- **File**: `INFORME_TECNICO.md` §6 líneas 90, 232
- **Lines**: 90, 232
- **Types**: result
- **Excerpt**: «Se creó `Auxiliares/.venv` con patchright 1.64.4, PyPasser 1.1.0, Scrapling 0.5.1, ddddocr 1.6.1, playwright 1.65.2, curl_cffi 0.17.0 […] onnxruntime 1.32.0, ddgs 9.16.1 y tenacity 9.2.1.»
- **Restated**: El entorno declara once dependencias con versiones concretas y usa Chromium del sistema más FlareSolverr 3.5.2 en Docker.
- **Notes**: ⚠️ §55 línea 1370 añade un segundo entorno `Auxiliares/.venv-py` funcional; el README línea 1640 usa `.venv-py`, no `.venv`.

### C022 — Tres búsquedas de corpus con regla de parada a los 10 páginas

- **File**: `INFORME_TECNICO.md` §7 tabla líneas 98–102 (EN 240–244)
- **Lines**: 98, 102, 240, 244
- **Types**: result, methodological
- **Excerpt**: «| `mercado automovilistico trabajos investigativos` | 112 | 1.086 | 11 | página 19 |»
- **Restated**: Las tres búsquedas produjeron 1.086, 226 y 230 resultados, con 11, 2 y 10 trabajos útiles respectivamente.
- **Notes**: §12 línea 156 atribuye a esta regla no haber consumido resultados repetidos.

### C023 — Descargas del corpus: 93/17, 23/10 y 78/36

- **File**: `INFORME_TECNICO.md` §7 línea 104 (EN 246)
- **Lines**: 104, 246
- **Types**: result
- **Excerpt**: «descarga inicial **93 OK / 17 fallos**, rentabilidad **23 OK / 10 fallos**, calidad/precio **78 OK / 36 fallos**»
- **Restated**: Las tres campañas de descarga registraron 93, 23 y 78 aciertos, con 17, 10 y 36 fallos.

### C024 — Esquema SQLite por tienda con 30 campos estructurados

- **File**: `INFORME_TECNICO.md` §8 líneas 108, 250; §20 línea 902
- **Lines**: 108, 250, 902
- **Types**: definitional
- **Excerpt**: «una tabla `vehiculos`: identificación (`url`, `shop`, `title`, `status`, `scraped_at`), metadatos y 30 campos estructurados […] además de campos sin normalizar (`tables_json`, `jsonld_json`, `raw_html`, …)»
- **Restated**: Cada tienda usa una base SQLite con tabla `vehiculos` de 30 campos estructurados más campos crudos.

### C025 — 11 bases preparadas y 256 filas en la fase 6

- **File**: `INFORME_TECNICO.md` §9 tabla líneas 112–126 (EN 254–268)
- **Lines**: 112, 126, 254, 268
- **Types**: result
- **Excerpt**: «Se prepararon 11 bases y se obtuvieron **256 filas**»
- **Restated**: La captura inicial de concesionarios rindió 256 filas en 11 bases; Chinautos (70), AGN Motors (60), Dongfeng (45) y Finauto (45) concentran el volumen.
- **Notes**: Coincide con README líneas 1623, 1679 («256 vehículos de 11 concesionarios»). ⚠️ La tabla da 109 filas con precio de 256; la frase «mejor densidad: AGN Motors, Chinautos Cuba, Dongfeng Cuba y Finauto» (línea 128) incluye a Chinautos con 0 precios, lo que contradice el criterio de densidad de precio.

### C026 — Exclusiones técnicas de carrosw, LlamaCuba y SASA/DIVEP

- **File**: `INFORME_TECNICO.md` §9 línea 128 (EN 270)
- **Lines**: 128, 270
- **Types**: result
- **Excerpt**: «Excluidas por bloqueo técnico: carrosw (HTTP 403 con Bot Verification), LlamaCuba (timeout) y SASA/DIVEP (sin catálogo).»
- **Restated**: Tres fuentes quedaron fuera por bloqueo o ausencia de catálogo, sin fabricar contenido.
- **Notes**: Coherente con §11 línea 147 y README línea 1772.

### C027 — Git LFS 3.8.1 y retención del esquema de partes

- **File**: `INFORME_TECNICO.md` §30 líneas 1006–1012
- **Lines**: 1006, 1012
- **Types**: methodological
- **Excerpt**: «Se instaló **Git LFS 3.8.1** y se activó en el repositorio. `.gitattributes` marca `*.sqlite`, `*.sqlite-wal` y `*.sqlite-shm` con `filter=lfs diff=lfs merge=lfs -text`»
- **Restated**: Los SQLite se gestionan con LFS 3.8.1, manteniendo el esquema de partes como respaldo auditable.

### C028 — Rango temporal Revolico y limpieza de 9.957 anuncios

- **File**: `INFORME_TECNICO.md` §31 líneas 1016–1020
- **Lines**: 1016, 1020
- **Types**: result
- **Excerpt**: «La limpieza general sobre 9.957 anuncios conservó **548 autos** y registró 9.409 exclusiones (9.316 no vehículo 4+ ruedas, 93 sin datos necesarios).»
- **Restated**: Sobre 9.957 anuncios se conservaron 548 autos; 9.409 exclusiones se registraron, ninguna por fecha.
- **Notes**: Aritmética consistente (9.316+93=9.409; 9.957−9.409=548). ᵛ

### C029 — 119 canales de Telegram y 54 anuncios en la BD compartida

- **File**: `INFORME_TECNICO.md` §29 líneas 992–1002
- **Lines**: 992, 1002
- **Types**: result
- **Excerpt**: «Objetivo de 100 canales de referencia superado (119). El descubrimiento usa 26 búsquedas en tgden.com y valida cada usuario con `t.me/s/`»
- **Restated**: La BD de Telegram contiene 119 canales (4 con contexto automotriz) y 54 anuncios marcados `es_auto`.
- **Notes**: Coherente con §28 línea 981 («152 mensajes, 54 anuncios»).

### C030 — Primera ejecución del pipeline de rentabilidad

- **File**: `INFORME_TECNICO.md` §34 tabla líneas 1072–1085
- **Lines**: 1072, 1085
- **Types**: result
- **Excerpt**: «| Filas ingeridas | 972 (716 Revolico + 256 concesionarios) | […] | Precio mediano usado | 24.000 USD | […] | Anomalías | 17 |»
- **Restated**: La primera corrida ingirió 972 filas, conservó 499 limpias (497 usados) y estimó −5,43 % anual con 328 observaciones OLS.
- **Notes**: ᵛ Corrida fundacional, explícitamente superada por §59. La mediana 24.000 USD y las 32 marcas difieren de los 21.000 USD y 50 marcas vigentes.

### C031 — Brecha frente a Egipto: 23.500 anuncios

- **File**: `INFORME_TECNICO.md` §34 línea 1089, §71.1 línea 1522; `PRESENTACION_STORYTELLING.md` línea 1935
- **Lines**: 1089, 1522, 1935
- **Types**: result, contextual
- **Excerpt**: «Egipto tiene 23.500 anuncios, historial mensual de precios, HP y kilometraje estructurados, ANOVA/OLS/VIF, Tableau y Power BI.»
- **Restated**: El baseline egipcio supera al proyecto en volumen (23.500 vs 2.174 anuncios), historial mensual y_variables estructuradas.
- **Notes**: Cifra repetida de forma consistente en tres archivos.

### C032 — La app Circuitos Habana hace scraping del canal público de Telegram

- **File**: `INFORME_TECNICO.md` §35 líneas 1097–1103
- **Lines**: 1097, 1103
- **Types**: result, citation-grounded
- **Excerpt**: «La app **no usa una API privada**: hace scraping del canal público de Telegram `https://t.me/s/EmpresaElectricaDeLaHabana` con Jsoup y User-Agent de Chrome.»
- **Restated**: El APK descompilado revela paginación `?before=<message_id>`, hasta 16 páginas/300 mensajes/8 días, y filtrado por palabras clave.
- **Notes**: Coherente con §62 línea 1436 y storytelling línea 1906.

### C033 — Docker no arranca sin root y Overpass no devuelve talleres en Cuba

- **File**: `INFORME_TECNICO.md` §36 líneas 1113–1114
- **Lines**: 1113, 1114
- **Types**: result
- **Excerpt**: «Overpass/OSM fue consultado dos veces; no devuelve `shop=car`, `shop=car_repair` ni `charging_station` etiquetados en Cuba, así que no hay datos geográficos útiles de ahí.»
- **Restated**: En la primera consulta OSM/Overpass no aportó talleres ni cargadores etiquetados en Cuba, y el scraper de Google Maps quedó descartado por permisos de Docker.
- **Notes**: ⚠️ **Aparente contradicción con §41 línea 1183**: allí Overpass devuelve «137 gasolineras en La Habana». No son las mismas etiquetas (`amenity=fuel` vs `shop=car_repair`/`charging_station`), pero el texto de §36 dice «no hay datos geográficos útiles de ahí» sin esa salvedad.

### C034 — Coordenadas de concesionarios extraídas de mapas incrustados

- **File**: `INFORME_TECNICO.md` §36 línea 1115
- **Lines**: 1115
- **Types**: result
- **Excerpt**: «BDC One: 23.1155203,-82.3596368 y 23.0992805,-82.3050631; Dongfeng: 23.1250339,-82.4227564»
- **Restated**: Se obtuvieron tres pares de coordenadas desde los sitios de BDC One y Dongfeng, más una dirección geocodificada con Nominatim.
- **Notes**:Coincide con storytelling línea 1919 («concesionarios con presencia verificada: BDC One y Dongfeng Cuba»).

### C035 — Infraestructura EV: 11 estaciones solares y 21 de CIMEX+MITRANS

- **File**: `INFORME_TECNICO.md` §36 línea 1117; `PRESENTACION_STORYTELLING.md` línea 1923
- **Lines**: 1117, 1923
- **Types**: result
- **Excerpt**: «Dongfeng/NWI 11 estaciones solares (2026), CIMEX+MITRANS 21 estaciones (2025), primera estación rápida en Santa Clara (08/2026), conectores CCS2»
- **Restated**: Las fuentes documentan 32 estaciones de carga anunciadas (11 + 21) con conectores CCS2 mayoritarios.
- **Notes**: Difieren de las 12 referencias efectivamente geolocalizadas (§41 línea 1185); no se declara si son conjuntos distintos.

### C036 — Optimización de descargas: sesiones TLS por hilo y 6 workers

- **File**: `INFORME_TECNICO.md` §37 líneas 1129–1131
- **Lines**: 1129, 1131
- **Types**: methodological, result
- **Excerpt**: «`scrape_revolico.py` ahora usa una **sesión curl_cffi por hilo** (`threading.local`) con impersonación Chrome […] El servicio `revolico-revisar.service` pasó de 8 descargadores/4 procesadores a **20/8**»
- **Restated**: La optimización elevó los anuncios de Revolico de 10.117 a 10.149 y los autos de 716 a 814 en minutos.
- **Notes**: ⚠️ **CONTRADICCIÓN con la conclusión §12 línea 155** («El scraping sostenible depende del ritmo, la sesión y la reanudación, **no principalmente del fingerprint TLS**»): aquí y en §42/README la impersonación de Chrome es la vía declarada para sortear 403.

### C037 — 2.121 anuncios tras ampliar los límites de marketplaces

- **File**: `INFORME_TECNICO.md` §39 líneas 1156–1157
- **Lines**: 1156, 1157
- **Types**: result
- **Excerpt**: «Cogetucarro de 200 → **5.008**, Autocubana y Timbirichi a 40 páginas […] Autocubana pasó de 400 a **566** y Timbirichi de 110 a **170**, totalizando **2.121 anuncios**.»
- **Restated**: Tras ampliar límites, el conjunto de marketplaces alcanzó 2.121 anuncios, con 12 descargadores/8 procesadores en Revolico.
- **Notes**: ⚠️ Ver C018: los conteos de Autocubana y Timbirichi son inferiores a los de §5, fechado un día antes.

### C038 — 137 gasolineras OSM, 12 referencias de carga y 18 precios de combustible

- **File**: `INFORME_TECNICO.md` §41 líneas 1183–1187
- **Lines**: 1183, 1187
- **Types**: result
- **Excerpt**: «**Overpass/OSM devolvió 137 gasolineras en La Habana** con coordenadas […] Se crearon `Data/mapas/gasolineras.csv` (137) y `Data/mapas/estaciones_carga.csv` (12)»
- **Restated**: La primera versión del mapa registro 137 gasolineras, 12 referencias de carga y 18 observaciones de precio entre el 20/08 y el 18/11/2026.
- **Notes**: ⚠️ **CONTRADICCIÓN con §42 línea 1206**, que da 131 gasolineras y 12 estaciones de carga como «estado final» del mismo mapa. ᵛ

### C039 — Suspensión de venta en CUP y liberalización de precios del combustible

- **File**: `INFORME_TECNICO.md` §41 línea 1189, §43 líneas 1835–1837; `PRESENTACION_STORYTELLING.md` líneas 1835–1837
- **Lines**: 1189, 1835, 1837
- **Types**: result, citation-grounded
- **Excerpt**: «desde 07/02/2026 la venta oficial en CUP está suspendida y el combustible se vende en USD vía Ticket; desde mayo cada importador fija su precio. La B94 informal pasó de 3.500–5.000 CUP (ago) a 7.000–8.000 CUP (sep 2026).»
- **Restated**: Desde el 7/02/2026 CIMEX suspendió la venta en CUP vía Ticket; desde el 15/05/2026 cada importador fija 1,80–2,60 USD/L y la B94 informal cotiza 7.000–8.000 CUP/L.
- **External evidence cited**: Cubadebate, Directorio Cubano, CubaTrámite (Circular 03/2026), D-Cuba
- **Notes**: Coherente entre §41 y §43; el storytelling precisa que no hubo resolución numerada nueva.

### C040 — Mapa unificado: 131 gasolineras, 12 cargas, 25 concesionarios, 22 talleres

- **File**: `INFORME_TECNICO.md` §42 líneas 1197–1208; `Data/mapas/README.md` líneas 2457–2467
- **Lines**: 1197, 1206, 1208, 2457, 2467
- **Types**: result
- **Excerpt**: «Estado final: **131 gasolineras, 12 estaciones de carga, 25 concesionarios (17 con coords) y 22 talleres (todos con coords)**.»
- **Restated**: `mapa_elementos.sqlite` es la fuente única con 131 gasolineras, 12 cargas, 25 concesionarios y 22 talleres, con colores negro/verde/azul/rojo.
- **Notes**: ⚠️ Ver C038 (137 gasolineras en §41). El `README.md` de mapas no repite los conteos, solo colores y símbolos.

### C041 — Premium frente a no premium: listas declaradas de marcas

- **File**: `INFORME_TECNICO.md` §48 líneas 1269–1272; `PRESENTACION_STORYTELLING.md` línea 1885
- **Lines**: 1269, 1272, 1885
- **Types**: definitional
- **Excerpt**: «**Premium:** Mercedes-Benz, BMW, Audi, Lexus, Volvo, Porsche, Land Rover, Jaguar, Cadillac, Infiniti y Acura.»
- **Restated**: La segmentación narrativa usa dos grupos (11 premium vs el resto) mientras el modelo conserva tres niveles (`premium`, `medio`, `económico`).
- **Notes**: Coherente con `config.py` y §71.2; la lista no premium del storytelling línea 1885 omite algunas marcas añadidas en §51 línea 1312 (BAIC, Opel, Volga, GAC…), posible desactualización menor.

### C042 — 648 repositorios reducidos a 36 relevantes

- **File**: `INFORME_TECNICO.md` §49 líneas 1280–1286
- **Lines**: 1280, 1286
- **Types**: result
- **Excerpt**: «usando 31 consultas en español e inglés […] Tras deduplicar se obtuvieron **648 repos**, de los que se depuraron **36 con relación directa o instrumental**»
- **Restated**: La búsqueda en GitHub produjo 648 repos únicos, de los que 36 se consideraron relevantes.
- **Notes**: Coherente con §50 línea 1292 (36 → 7 Dedicados a autos).

### C043 — Consolidación de 25 tablas y 3.958 anuncios de referencia

- **File**: `INFORME_TECNICO.md` §50 líneas 1292–1298; `README.md` línea 1681
- **Lines**: 1292, 1296, 1298, 1681
- **Types**: result
- **Excerpt**: «Se compararon 233 archivos de datos por hash y 76 CSV por contenido ordenado. Se detectaron 12 grupos de duplicados bytes y 11 de duplicados por contenido […] De los 3.958 anuncios, **369 ya estaban en nuestra base** y 3.589 son nuevos»
- **Restated**: `referencias_autos.sqlite` contiene 25 tablas no duplicadas, incluidos 3.958 anuncios de Revolico de los que 369 ya existían en el proyecto.
- **Notes**: Coherente con README línea 1630 («25 tablas»).

### C044 — Encuesta de 33 personas y 16 de 18 rechazan pagar más de 4.000 USD

- **File**: `INFORME_TECNICO.md` §50 línea 1298; `PRESENTACION_STORYTELLING.md` línea 1909
- **Lines**: 1298, 1909
- **Types**: result
- **Excerpt**: «la encuesta con datos reales fue un Google Forms de 32 preguntas aplicado a 33 personas de 4 segmentos en un barrio de La Habana (17 de 18–25 prefieren eléctrico, pero 16 de 18 no pagarían más de 4.000 USD por uno)»
- **Restated**: La encuesta tiene 33 respuestas; 16 de 18 encuestados en el segmento relevante no pagarían más de 4.000 USD por un eléctrico.
- **Notes**: Ver C015 para la aparente discrepancia 17 vs 14.

### C045 — Deduplicación de `autos`: 814 filas → 744 únicos

- **File**: `INFORME_TECNICO.md` §51 línea 1308
- **Lines**: 1308
- **Types**: result
- **Excerpt**: «La tabla se reconstruyó desde `anuncios` (fuente canónica): 814 filas con 748 IDs únicos → **744 autos únicos**. Se excluyeron 4 anuncios que no son autos»
- **Restated**: La tabla `autos` quedó en 744 filas únicas tras excluir cuatro IDs y crear el índice `idx_autos_id`.
- **Notes**: Aritmética consistente (748−4=744).Esta cifra es intermedia; la vigente es 974 (§59).

### C046 — Reparación de `parse_price` y `parse_number`

- **File**: `INFORME_TECNICO.md` §51 líneas 1310–1311; `MODELOS_Y_FUNCIONES.md` líneas 2065–2066
- **Lines**: 1310, 1311, 2065, 2066
- **Types**: methodological, result
- **Excerpt**: «`parse_price` ahora interpreta separadores de miles (973 anuncios recuperados: 872 de iTENCEL, 99 de Cubisima, 2 de VentaCuba)»
- **Restated**: La normalización sintáctica recuperó 973 anuncios y corrigió la lectura de «80,000 km» de 80 a 80.000 km, cambiando la mediana de km a 32.569.
- **Notes**: Coherente con `kpis.csv` (`km_medianos=32569`).

### C047 — Canal local frente a importación

- **File**: `INFORME_TECNICO.md` §51 línea 1310, §58 línea 1400; `kpis_canal.csv`
- **Lines**: 1310, 1400
- **Types**: result, definitional
- **Excerpt**: «Se incorporó la columna `canal`: **1.301 anuncios locales y 672 de importación** (iTENCEL), con `kpis_canal.csv` e `importacion_por_marca.csv` separados. La mediana local quedó en 21.000 USD.»
- **Restated**: El análisis separa local e importación; la corrida vigente contabiliza 1.483 locales y 691 de importación.
- **Notes**: ⚠️ Las cifras 1.301/672 (2.653) superan los 2.014 limpios de §58; parecen corresponder a una capa previa a deduplicación, sin que el corpus lo explicite.

### C048 — 25 fuentes adicionales y hallazgo de la resolución derogada

- **File**: `INFORME_TECNICO.md` §52 líneas 1322–1334
- **Lines**: 1322, 1326, 1332, 1334
- **Types**: result
- **Excerpt**: «El resultado está en `Data/fuentes-adicionales-2026-11-20.md`: **25 fuentes** verificadas, organizadas por tipo con URL, datos expuestos, viabilidad de scraping y aporte al proyecto.»
- **Restated**: Se verificaron 25 fuentes adicionales; la API del BCC es referencia oficial no usada en la conversión y la Resolución 312/2026 quedó marcada como derogada.
- **Notes**: Coherente con C010 y C011.

### C049 — Descarga íntegra de los 12 anuarios del ONEI

- **File**: `INFORME_TECNICO.md` §53 líneas 1342–1348; `README.md` línea 1632
- **Lines**: 1342, 1348, 1632
- **Types**: result
- **Excerpt**: «se descargaron **todos los documentos enlazados**: 111 PDF, 7 RAR y 103 archivos Excel extraídos, unos 311 MB en total.»
- **Restated**: Se descargaron los 117 enlaces de documento de 12 anuarios (111 PDF + 7 RAR + 103 Excel extraídos) con SHA-256 por archivo.
- **Notes**: Coherente con README («12 anuarios, 233 archivos»: 111+7+103=221; la diferencia de 12 no se explica en el corpus).

### C050 — 82 chunks de 10 MB con manifiesto SHA-256

- **File**: `INFORME_TECNICO.md` §54 líneas 1354–1360; `README.md` línea 1692
- **Lines**: 1354, 1360, 1692
- **Types**: result, methodological
- **Excerpt**: «`Data/Revolico/revolico.sqlite` (849.465.344 bytes) se dividió en **82 chunks de 10 MB** […] La verificación de los 82 chunks dio OK.»
- **Restated**: La base de 849.465.344 bytes se divide en 82 fragmentos verificables reconstruibles desde `MANIFEST.json`.
- **Notes**: Coherente con `ARQUITECTURA_DATOS.md` línea 2160 (849 MB) y `ESTRUCTURA_ESPACIO.md` línea 2412 (810 MB ≈ 849 MM bytes).

### C051 — Auditoría de 15 fuentes web con 14 HTTP 200

- **File**: `INFORME_TECNICO.md` §55 líneas 1366–1374
- **Lines**: 1366, 1374
- **Types**: result
- **Excerpt**: «Se consultaron **15 fuentes web** (8 marketplaces, 7 fuentes oficiales y complementarias): 14 respondieron HTTP 200 y elTOQUE no respondió desde este entorno.»
- **Restated**: La auditoría cubrió 15 fuentes, con 14 respuestas HTTP 200 y una fallida (elTOQUE).
- **Notes**: Coherente con README línea 1772, que atribuye el uso de la última TRMI publicada a esa caída.

### C052 — Corrección de un `NameError` en `01_ingest.py`

- **File**: `INFORME_TECNICO.md` §55 línea 1372
- **Lines**: 1372
- **Types**: methodological
- **Excerpt**: «La verificación del código detectó un `NameError` en `scripts/01_ingest.py` (`cfg` usado antes de importarse); se corrigió y se revalidó la importación»
- **Restated**: El bug de orden de importación fue corregido y las funciones `parse_price`/`parse_number` reverificadas.

### C053 — Reclasificación de URLs: 7 fuentes sin novedades, iTENCEL con 10

- **File**: `INFORME_TECNICO.md` §57 líneas 1390–1392
- **Lines**: 1390, 1392
- **Types**: result
- **Excerpt**: «Resultado: 7 fuentes sin enlaces nuevos; **iTENCEL mostró 10 anuncios nuevos** […] tras descartar una página de agrupación falsa.»
- **Restated**: La comparación de URL normalizadas detectó 10 anuncios nuevos solo en iTENCEL, sin modificar las bases hasta §58.
- **Notes**: Coherente con §58 (951 → 961).

### C054 — Sitio MkDocs con build estricto

- **File**: `INFORME_TECNICO.md` §61 líneas 1426–1430
- **Lines**: 1426, 1430
- **Types**: result
- **Excerpt**: «`mkdocs build --strict` termina sin errores ni enlaces rotos.»
- **Restated**: El sitio de documentación compila en modo estricto con navegación Diátaxis y sin enlaces rotos.
- **Notes**: ⚠️ Ver C003: la descripción del panel difiere de `AUTOMATIZACION.md` línea 2317.

### C055 — Factibilidad del timelapse eléctrico

- **File**: `INFORME_TECNICO.md` §62 línea 1436
- **Lines**: 1436
- **Types**: result
- **Excerpt**: «Del APK se extrajeron 2.473 puntos, 244 circuitos y 166 polígonos de zonas […] en su primera corrida real capturó 40 mensajes, deduplicó por ID y dejó 35 circuitos sin luz, 23 mixtos y 2 con luz»
- **Restated**: El canal público responde HTTP 200 y la primera corrida del capturador produjo 60 registros de estado de circuitos.
- **Notes**: 35+23+2=60, coherente con «40 mensajes» tras deduplicación.

### C056 — Reducción del repositorio de 20 GB a 10 GB

- **File**: `INFORME_TECNICO.md` §67 líneas 1480–1482; `ESTRUCTURA_ESPACIO.md` línea 2406
- **Lines**: 1480, 2406
- **Types**: result
- **Excerpt**: «El repositorio pasó de 20 GB a 10 GB.»
- **Restated**: Tras la limpieza autorizada, el árbol local pasó de 20 GB a 10 GB, con leyes y herramientas mudadas a `~/Utilidades`.
- **Notes**: Coherente con el mapa de espacio (`Proyecto (10 GB)`).

### C057 — Peso en GitHub y mapa de espacio

- **File**: `INFORME_TECNICO.md` §68 línea 1488; `ESTRUCTURA_ESPACIO.md` líneas 2399–2401
- **Lines**: 1488, 2399, 2401
- **Types**: result
- **Excerpt**: «La API de GitHub reporta **205.002 KB (0,20 GB)** para el historial normal; los archivos grandes se guardan aparte y su consumo en GitHub no lo expone la API. En local, esa copia ocupa 3,3 GB con 174 archivos.»
- **Restated**: La API informa 0,20 GB de historial Git y 3,3 GB locales de objetos LFS, sin exponer el consumo remoto de LFS.
- **Notes**: Cifras idénticas en ambos archivos.

### C058 — VIF entre 1,12 y 1,40

- **File**: `INFORME_TECNICO.md` §60 línea 1418; `MODELOS_Y_FUNCIONES.md` línea 2116; `vif.csv`
- **Lines**: 1418, 2116
- **Types**: result
- **Excerpt**: «VIF <!-- kpi:vif_min -->1,12–<!-- kpi:vif_max -->1,40»
- **Restated**: Los factores de inflación de varianza oscilan entre 1,12 y 1,40, por lo que no hay multicolinealidad que explique la no significancia.
- **Notes**: Coincide con `vif.csv` (min 1,12 en `hp`, max 1,40 en `mileage_km`).

### C059 — Líneas base predictivas: MAE 18.188,34 y 16.603,28 USD

- **File**: `INFORME_TECNICO.md` §71.1 líneas 1520–1521, 1527; `baselines.csv`
- **Lines**: 1520, 1521, 1527
- **Types**: result
- **Excerpt**: «| Mediana global ( ingenua ) | Predice la mediana de los usados locales | MAE <!-- kpi:mae_mediana_global -->18.188,34 USD sobre <!-- kpi:n_mediana_global -->1.462 anuncios |»
- **Restated**: La mediana global tiene MAE 18.188,34 USD y la mediana por marca 16.603,28 USD, ambas sobre 1.462 anuncios.
- **Notes**: Coincide con `baselines.csv`. `ARQUITECTURA_DATOS.md` línea 2172 las califica como predictivas, no experimentales.

### C060 — Ablación del término `hp`

- **File**: `INFORME_TECNICO.md` §71.2 líneas 1531–1533; `MODELOS_Y_FUNCIONES.md` línea 2110; `modelo_muestra.csv`
- **Lines**: 1531, 1533, 2110
- **Types**: result, methodological
- **Excerpt**: «`modelo_muestra.csv` documenta la ablación del término `hp`: al retirarlo, la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² baja de 0,274 a 0,101.»
- **Restated**: Retirar `hp` aumenta la muestra de 28 a 586 y reduce el R² de 0,2744 a 0,1008.
- **Notes**: ⚠️ **CONTRADICCIÓN contra CSV**: 584 y 981 en el texto vs 586 y 993 en `modelo_muestra.csv`; ver C008.

### C061 — Intervalo bootstrap de la diferencia premium−económico

- **File**: `INFORME_TECNICO.md` §71.3 línea 1537; `comparaciones.csv`
- **Lines**: 1537
- **Types**: result
- **Excerpt**: «un intervalo bootstrap de la diferencia de medianas premium−económico de <!-- kpi:ci_bajo -->10.000 a <!-- kpi:ci_alto -->29.500 USD (`comparaciones.csv`, 2.000 réplicas)»
- **Restated**: El IC bootstrap al 95 % de la diferencia de medianas premium−económico va de 10.000 a 29.500 USD con 2.000 réplicas.
- **Notes**: ⚠️ **Tensión con C006**: el IC es positivo y no cruza cero, mientras el coeficiente premium del OLS completo es no significativo (p=0,8753); el corpus no reconcilia ambos resultados.

### C062 — Sin diseño pareado: Kruskal-Wallis y Welch

- **File**: `INFORME_TECNICO.md` §71.3 líneas 1537–1539; `MODELOS_Y_FUNCIONES.md` §3.4 líneas 2124–2128
- **Lines**: 1537, 2124, 2128
- **Types**: methodological
- **Excerpt**: «No hay diseño pareado: los anuncios son observaciones independientes, por lo que no se aplican Wilcoxon de pares ni t de diferencias; se usan Kruskal-Wallis y Welch para grupos independientes.»
- **Restated**: Los tests empleados son de grupos independientes; Welch está codificado pero no se ejecuta en la corrida actual.

### C063 — Semilla `SEED = 20261127` declarada y propagada

- **File**: `INFORME_TECNICO.md` §71.5 línea 1552; `AUTOMATIZACION.md` línea 2313
- **Lines**: 1552, 2313
- **Types**: methodological
- **Excerpt**: «La semilla `SEED = 20261127` está declarada en `run_all.py` y se propaga a cada etapa por la variable de entorno `PROYECTO_SEED`; antes se declaraba sin efecto.»
- **Restated**: La semilla se declara y propaga a todas las etapas del pipeline.
- **Notes**: ⚠️ **CONTRADICCIÓN entre archivos**: `AUTOMATIZACION.md` línea 2313 afirma que «solo el bootstrap de `03c_comparaciones.py` la consume, porque las demás etapas son deterministas». La propagación a todas las etapas no equivaldría a consumo en todas.

### C064 — Estimación de ancho de banda de los timers

- **File**: `INFORME_TECNICO.md` §65 líneas 1462–1464; `AUTOMATIZACION.md` líneas 2377–2384
- **Lines**: 1462, 2377, 2382
- **Types**: result
- **Excerpt**: «Estimación de red: **5–10 MB/mes** si no hay cambios y **50–90 MB/mes** con novedades.»
- **Restated**: El consumo mensual estimado es 5–10 MB sin cambios y 50–90 MB con novedades.
- **Notes**: ⚠️ **CONTRADICCIÓN directa entre archivos**: `AUTOMATIZACION.md` línea 2382 da «**~2–3 MB/mes**» y «**~56–100 MB/mes**» para el mismo conjunto de jobs. Ambos se presentan como estimaciones de diseño.

### C065 — Panel de 107 KB sin peticiones externas

- **File**: `AUTOMATIZACION.md` línea 2317
- **Lines**: 2317
- **Types**: result, methodological
- **Excerpt**: «antes hacían falta los 6 HTML de Plotly (168 KB) más ~4,5 MB de JavaScript remoto por visita […] ahora un solo archivo de **107 KB** sin peticiones externas funciona por `file://` y en 3G.»
- **Restated**: El panel consume 107 KB y cero peticiones externas, frente a ~4,7 MB de la versión anterior.
- **Notes**: ⚠️ Ver C003 y C054: `INFORME_TECNICO.md` línea 1428 sigue describiendo seis gráficos Plotly copiados al sitio.

### C066 — DuckDB desinstalado pero bloquea por `SIGILL`

- **File**: `INFORME_TECNICO.md` §34 línea 1068, §66 línea 1472; `ARQUITECTURA_DATOS.md` líneas 2178, 2224; `ESTRUCTURA_ESPACIO.md` línea 2429
- **Lines**: 1068, 1472, 2178, 2224, 2429
- **Types**: result
- **Excerpt**: «`duckdb` se desinstaló porque produce `Illegal instruction` en esta CPU; se usa Parquet + Pandas en su lugar.»
- **Restated**: DuckDB no es usable en esta CPU y la fase 1 se implementa con pyarrow/pandas.
- **Notes**: ⚠️ **Aparente contradicción**: §34 dice «se desinstaló», pero `ESTRUCTURA_ESPACIO.md` línea 2429 lo cuenta entre las bibliotecas del entorno en uso que ocupan 66 MB.

### C067 — Formato Parquet compacto: 849 MB → 27,5 MB

- **File**: `ARQUITECTURA_DATOS.md` líneas 2157–2166
- **Lines**: 2157, 2160, 2166
- **Types**: result, methodological
- **Excerpt**: «Medición real: **849 MB → 27,5 MB** (10.379 anuncios, 974 autos, 23.697 imágenes, 14.512 revisiones, 12.538 teléfonos y 716 precios), con las mismas filas, columnas y valores»
- **Restated**: La exportación Parquet comprimida reduce la base de 849 MB a 27,5 MB sin pérdida de filas ni columnas.
- **Notes**: Coherente con README línea 1630 (10.379 anuncios, 974 autos) y §37 línea 1131 (10.149 en una corrida anterior).

### C068 — Validación de calidad: 2.174 filas limpias, 0 inválidos

- **File**: `AUTOMATIZACION.md` línea 2364
- **Lines**: 2364
- **Types**: result
- **Excerpt**: «Corrida vigente: 2.174 filas limpias, 0 inválidos; la corrida de 2.014 filas quedó registrada como estado anterior.»
- **Restated**: `validar_calidad.py` no encontró filas inválidas en la corrida de 2.174 registros.
- **Notes**: Coherente con `kpis.csv` y §58/§59.

### C069 — Reglas de particionamiento y watermark

- **File**: `ARQUITECTURA_DATOS.md` líneas 2185, 2196–2201
- **Lines**: 2185, 2196, 2199, 2201
- **Types**: methodological
- **Excerpt**: «El watermark se actualiza en la misma transacción que el KPI. Si la corrida muere, el watermark no avanza.»
- **Restated**: El diseño prevé escrituras solo del delta con watermark transaccional y umbrales de higiene (100 MB por partición, <2.000 archivos).
- **Notes**: Es diseño propuesto (fase 2), no implementación verificada; el propio documento lo declara «Fase 0–1 de diseño» (línea 2224).

### C070 — Cuarentena antes que borrado y dead-man's switch

- **File**: `AUTOMATIZACION.md` líneas 2339, 2365–2367
- **Lines**: 2339, 2365
- **Types**: methodological
- **Excerpt**: «Los registros inválidos van a **cuarentena** (`Data/_cuarentena/<fecha>/`), nunca se borran. Si el ratio de rechazo > 10 % el job falla; entre 5 y 10 % solo avisa.»
- **Restated**: Los datos inválidos se aíslan, nunca se eliminan, y `SALUD.md` marca periodos perdidos sin correo ni webhook.
- **Notes**: Coherente con §65 línea 1462 (`salud.py` distingue `SIN DATOS` de `STALE`).

### C071 — Timers activos y Linger=yes

- **File**: `INFORME_TECNICO.md` §65 líneas 1462–1464; `AUTOMATIZACION.md` líneas 2360–2369
- **Lines**: 1462, 2360, 2367, 2369
- **Types**: result
- **Excerpt**: «Se activaron cinco timers `precio-*` (circuitos, calidad, salud, análisis y sitio) con `Linger=yes`, envoltorio `run_step.sh` con `flock` y estado atómico»
- **Restated**: Cinco timers `precio-*` están habilitados con `Linger=yes`, `flock` y estados atómicos; el servicio `push-final` fue detenido tras 8 reinicios.
- **Notes**: Coherente con §64 línea 1454 y §66 línea 1470.

### C072 — Revolico cada 10 minutos y corrección de enlaces `pending`

- **File**: `INFORME_TECNICO.md` §66 líneas 1470–1472; `ARQUITECTURA_DATOS.md` línea 2222
- **Lines**: 1470, 1472, 2222
- **Types**: result, methodological
- **Excerpt**: «El primer debug reveló que 3.351 enlaces `es_auto_candidato=0` quedaban `pending` para siempre: se marcan `rechazado` y se excluyen del conteo de salida»
- **Restated**: El job de 10 minutos marca como rechazados los 3.351 enlaces no-auto atascados y guarda lote, snapshot y partes al recibir `SIGTERM`.
- **Notes**: Coherente con §37 línea 1131 (3.351 pendientes).

### C073 — Evolución del conteo de anuncios y autos de Revolico

- **File**: `INFORME_TECNICO.md` §15 línea 800, §16 línea 816, §24 línea 942, §37 línea 1131; `README.md` línea 1630
- **Lines**: 800, 816, 942, 1131, 1630
- **Types**: result
- **Excerpt**: «El scraper había ampliado la BD de 3.682 a **6.332 anuncios** (520,6 MB) antes de detenerse»
- **Restated**: La BD pasó de 3.682 a 6.332 anuncios, luego a 6.334, 10.149 y finalmente 10.379, con autos de 304 a 974.
- **Notes**: Secuencia histórica consistente; cada cifra está fechada en su sección. ᵛ

### C074 — Umbral de 4.000 anuncios sin revisar

- **File**: `INFORME_TECNICO.md` §27 líneas 970–973
- **Lines**: 970, 973
- **Types**: result
- **Excerpt**: «cuando `anuncios WHERE pagina_revisada=0` llega a **4.000** (configurable con `REVISAR_UMBRAL`), el aviso lanza `revolico-revisar.service`»
- **Restated**: El aviso de cada 10 minutos dispara el drenado de colas al alcanzar 4.000 anuncios sin revisar.
- **Notes**: Estado entonces: 3.623 sin revisar, bajo el umbral. ᵛ

### C075 — Supuesto de anuncio activo y de catálogo disponible

- **File**: `INFORME_TECNICO.md` §23 línea 932, §25 línea 950
- **Lines**: 932, 950
- **Types**: methodological
- **Excerpt**: «todos los registros tienen `status=PUBLISHED` y página verificada en la captura, por lo que se asume que son comprables; no se comprueba disponibilidad en tiempo real.»
- **Restated**: Los anuncios se tratan como comprables por su estado `PUBLISHED`; los catálogos se suponen disponibles y publicados el día de captura.
- **Notes**: Salvedad metodológica explícita.

### C076 — Cuatro fuerzas invisibles: divisa, reglas, luz, expectativas

- **File**: `PRESENTACION_STORYTELLING.md` líneas 1895–1909; `INFORME_TECNICO.md` §51 línea 1314
- **Lines**: 1895, 1909, 1314
- **Types**: result, contextual
- **Excerpt**: «Debajo hay cuatro corrientes que mueven el precio: […] La divisa […] Las reglas […] La luz […] Las expectativas»
- **Restated**: El relato organiza la explicación del precio en cuatro capas verificables en el corpus.
- **Notes**: Cuarta fuerza añadida en §51 («expectativas») tras la reconciliación de la encuesta.

### C077 — Cobertura de campos derivados en el análisis inicial

- **File**: `INFORME_TECNICO.md` §22 línea 923, §24 línea 940
- **Lines**: 923, 940
- **Types**: result
- **Excerpt**: «Cobertura de campos derivados: marca 68,4 %, año 63,5 %, km 6,2 % (heurísticos, extraídos solo de título/descripción).»
- **Restated**: El análisis inicial sobre 323 autos solo cubría 68,4 % de marca, 63,5 % de año y 6,2 % de kilómetro.
- **Notes**: ᵛ Base del posterior reporte de pérdida de muestra como hallazgo (C002).

### C078 — Los JSON de Revolico no traen año, km, marca ni modelo estructurados

- **File**: `INFORME_TECNICO.md` §24 líneas 940–942
- **Lines**: 940, 942
- **Types**: result
- **Excerpt**: «**No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**: por eso `anio_est`, `marca_est` y `km_est` se derivan con regex del texto visible»
- **Restated**: Los 6.334 anuncios solo traen estructurados precio, moneda, estado, fecha y geografía; el resto se infiere por regex.
- **Notes**: Coherente con C077 y con `MODELOS_Y_FUNCIONES.md` línea 2068.

### C079 — 30 oportunidades infravaloradas y 89 anomalías vigentes

- **File**: `INFORME_TECNICO.md` §59 línea 1408; `PRESENTACION_STORYTELLING.md` líneas 1855, 1873; `MODELOS_Y_FUNCIONES.md` línea 2134; `infravalorados.csv`, `anomalias.csv`
- **Lines**: 1408, 1855, 1873, 2134
- **Types**: result
- **Excerpt**: «<!-- kpi:grupos_benchmark -->114 grupos comparables y <!-- kpi:anomalias -->89 anomalías»
- **Restated**: La corrida vigente identifica 30 anuncios infravalorados y 89 anomalías entre precio y kilometraje.
- **Notes**: ⚠️ **CONTRADICCIÓN histórica**: §44 línea 1235 dice «**30 infravalorados**, **66 anomalías**» presentando 66 como cifra de la corrida que ya corrigió la depreciación; la vigente es 89. ᵛ

### C080 — Reglas de anomalía y descuento por comparable

- **File**: `MODELOS_Y_FUNCIONES.md` líneas 2084–2087, 2132–2136
- **Lines**: 2084, 2087, 2132, 2136
- **Types**: definitional, methodological
- **Excerpt**: «`km_anormal`: `km_per_year > 40.000` o `< 500`. […] `precio_atipico`: precio por debajo del percentil 1 o por encima del percentil 99.»
- **Restated**: Las anomalías se señalan con umbrales de km/año y percentiles 1/99, sin eliminar filas del análisis principal.
- **Notes**: Coherente con la definición de infravalorados (`descuento_pct` con grupos de al menos 2 anuncios).

### C081 — Requisitos de significancia del OLS

- **File**: `MODELOS_Y_FUNCIONES.md` líneas 2099, 2108
- **Lines**: 2099, 2108
- **Types**: methodological
- **Excerpt**: «Solo se incluye un término si hay más de 30 observaciones no nulas, y el modelo exige más de 30 filas.»
- **Restated**: El modelo exige más de 30 filas para estimarse.
- **Notes**: ⚠️ **CONTRADICCIÓN interna**: el modelo completo se reporta con **28 observaciones** (línea 2108 y `modelo_muestra.csv`), por debajo del propio umbral declarado.

### C082 — Licencia declarada frente a licencia pendiente

- **File**: `README.md` línea 1768; `INFORME_TECNICO.md` §71.5 línea 1552, §71.15 línea 1564
- **Lines**: 1552, 1564, 1768
- **Types**: definitional
- **Excerpt**: «Licencia: código MIT y datos derivados CC BY 4.0; las fuentes de terceros se rigen por sus propias condiciones.»
- **Restated**: El README declara licencia MIT/CC BY 4.0.
- **Notes**: ⚠️ **CONTRADICCIÓN directa**: la línea 1552 dice «No se ha declarado todavía una licencia de datos o código» y la línea 1564 repite «la licencia queda pendiente de declaración».

### C083 — Criterio de premium en la narrativa frente a los tres tiers del modelo

- **File**: `INFORME_TECNICO.md` §48 línea 1272; `MODELOS_Y_FUNCIONES.md` línea 2072
- **Lines**: 1272, 2072
- **Types**: definitional
- **Excerpt**: «El modelo econométrico conserva sus tres niveles (`premium`, `medio`, `económico`); la narrativa usa solo dos grupos para ser legible.»
- **Restated**: La narrativa colapsa tres tiers en dos grupos sin alterar el modelo.
- **Notes**: Coherente con `modelo_depreciacion.csv`, que conserva tres dummies.

### C084 — Declaración de uso de IA con rastro en `reviews/`

- **File**: `INFORME_TECNICO.md` §69 líneas 1498–1500; `README.md` línea 1770
- **Lines**: 1498, 1500, 1770
- **Types**: methodological
- **Excerpt**: «Las herramientas de IA (OpenCode/Claude Code con las skills `review`, `deep-research` y `technical-writing`) se usaron en investigación, redacción, código y traducción. Cada cifra se contrastó contra los CSV versionados y las pruebas automatizadas»
- **Restated**: El uso de IA está declarado y las cifras se cotejaron contra CSV con registro en `reviews/`.
- **Notes**: ⚠️ **CONTRADICCIÓN material con el propio expediente**: el R² corregido (C004) es 0,274 y coincide con el CSV, pero C008/C060 muestran que 981/584 siguen sin corregirse en §71, pese a la afirmación de que «cada cifra se contrastó».

### C085 — Referencias verificadas frente a referencias incompletas

- **File**: `INFORME_TECNICO.md` §70 líneas 1506–1508; `Data/referencias.md` líneas 2500–2584; `README.md` líneas 1755–1757
- **Lines**: 1506, 2500, 2505, 2527, 2580, 1755
- **Types**: citation-grounded
- **Excerpt**: «Referencias citadas y verificadas externamente durante la auditoría: Akerlof (1970) […] UK Department for Transport / DVLA […] ANFAC […] AEADE.»
- **Restated**: Solo cuatro fuentes se presentan como verificadas; las demás llevan `(metadata incomplete)` y no se cuentan como verificadas.
- **Notes**: ⚠️ **Aparente contradicción interna**: `Data/referencias.md` línea 2527 marca a Hulten [12] como `(metadata incomplete: PDF no extraido)` y línea 2580 a DfT/DVLA [39] como `(metadata incomplete: URL profunda no confirmada)`, mientras §70 afirma que DVLA está «verificada externamente (GOV.UK)». `README.md` línea 1716 sí incluye [12] entre «los más próximos».

## Contextual claims (30)

### C086 — Akerlof [1] y la asimetría de información

- **File**: `INFORME_TECNICO.md` §71.14 línea 1570; `Data/referencias.md` línea 2505
- **Lines**: 1570, 2505
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [1] | Asimetría de informaci | Akerlof (1970) | The Market for "Lemons": Quality Uncertainty and the Market Mech |»
- **Notes**: DOI 10.2307/1879431 verificado en OpenAlex; resumen indexado marcado incompleto.

### C087 — Lewis [2] sobre eBay Motors

- **File**: `INFORME_TECNICO.md` línea 1571; `Data/referencias.md` línea 2507
- **Lines**: 1571, 2507
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [2] | Asimetría de informaci | Lewis (2011) | Asymmetric Information, Adverse Selection and Online Disclosure: |»
- **Notes**: `Citada en el informe: no`.

### C088 — Peterson [3], selección adversa y patrones de reparación

- **File**: `INFORME_TECNICO.md` línea 1572; `Data/referencias.md` línea 2509
- **Lines**: 1572, 2509
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [3] | Asimetría de informaci | Peterson (2014) | Adverse selection in the used-car market: evidence from purchase |»

### C089 — Englmaier [4] sobre discontinuidades de precio

- **File**: `INFORME_TECNICO.md` línea 1573; `Data/referencias.md` línea 2511
- **Lines**: 1573, 2511
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [4] | Asimetría de informaci | Englmaier (2017) | Price Discontinuities in an Online Market for Used Cars |»

### C090 — Che [5], garantía y reputación del vendedor

- **File**: `INFORME_TECNICO.md` línea 1574; `Data/referencias.md` línea 2513
- **Lines**: 1574, 2513
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [5] | Asimetría de informaci | Che (2019) | Warranty, Seller Reputation, and Buyer Experience: Evidence From |»

### C091 — Wolf [6] y los sistemas de reputación en subastas

- **File**: `INFORME_TECNICO.md` línea 1575; `Data/referencias.md` línea 2515
- **Lines**: 1575, 2515
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [6] | Asimetría de informaci | Wolf (2005) | Adverse Selection and Reputation Systems in Online Auctions: Evi |»

### C092 — Sultan [7], modelo con limones y arrendamiento

- **File**: `INFORME_TECNICO.md` línea 1576; `Data/referencias.md` línea 2517
- **Lines**: 1576, 2517
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [7] | Asimetría de informaci | Sultan (2009) | A model of the used car market with lemons and leasing |»

### C093 — Tilles [8], modelo markoviano de asimetría

- **File**: `INFORME_TECNICO.md` línea 1577; `Data/referencias.md` línea 2519
- **Lines**: 1577, 2519
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [8] | Asimetría de informaci | Tilles (2011) | A Markovian model market—Akerlof's lemons and the asymmetry of i |»

### C094 — Du [9], depreciación no lineal y heterogeneidad de marca

- **File**: `INFORME_TECNICO.md` líneas 1578, 1558; `Data/referencias.md` línea 2521
- **Lines**: 1558, 1578, 2521
- **Types**: contextual, citation-grounded
- **Excerpt**: «Du y otros [9] modelan depreciación no lineal y heterogeneidad de marca con evaluación fuera de muestra; este informe no estima una tasa anual y reporta la pérdida de muestra como hallazgo.»
- **Notes**: Citada en §71.6 y §71.14.

### C095 — Kang [10] y los VE usados

- **File**: `INFORME_TECNICO.md` línea 1579; `Data/referencias.md` línea 2523
- **Lines**: 1579, 2523
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [10] | Modelos de precio, reg | Kang (2026) | The pricing of used electric vehicles via machine learning and h |»
- **Notes**: `(metadata incomplete: resumen no indexado)`.

### C096 — Miranda [11], depreciación en Emiratos

- **File**: `INFORME_TECNICO.md` línea 1580; `Data/referencias.md` línea 2525
- **Lines**: 1580, 2525
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [11] | Modelos de precio, reg | Miranda (2026) | Depreciation Patterns in the UAE Used Car Market: Evidence from |»

### C097 — Hulten [12], revisión crítica de precios hedónicos

- **File**: `INFORME_TECNICO.md` línea 1581; `Data/referencias.md` línea 2527
- **Lines**: 1581, 2527
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [12] | Modelos de precio, reg | Hulten (2003) | Price Hedonics: A Critical Review |»
- **Notes**: Ver C085: marcada incompleta en `referencias.md` pero incluida entre «los más próximos» en el README.

### C098 — Francke [13], heterogeneidad no observada

- **File**: `INFORME_TECNICO.md` línea 1582; `Data/referencias.md` línea 2529
- **Lines**: 1582, 2529
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [13] | Modelos de precio, reg | Francke (2020) | Modeling unobserved heterogeneity in hedonic price models |»

### C099 — Gegić [14], predicción con aprendizaje automático

- **File**: `INFORME_TECNICO.md` líneas 1558, 1583; `Data/referencias.md` línea 2531
- **Lines**: 1558, 1583, 2531
- **Types**: contextual, citation-grounded
- **Excerpt**: «Gegić y otros [14] predicen precios con aprendizaje automático sobre catálogos estructurados; aquí las variables se extraen de anuncios en lenguaje libre, así que el aporte es de procedencia y normalización, no de algoritmo.»

### C100 — Mutİ [15] y Jin [16], regresión y ML sobre precios usados

- **File**: `INFORME_TECNICO.md` líneas 1584–1585; `Data/referencias.md` líneas 2533, 2535
- **Lines**: 1584, 1585, 2533, 2535
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [15] | Modelos de precio, reg | Mutİ (2023) | Using Linear Regression For Used Car Price Prediction |»
- **Notes**: `Citada en el informe: no` en ambos casos.

### C101 — Ahtesham [17] y Madhusudhanan [18]

- **File**: `INFORME_TECNICO.md` líneas 1586–1587; `Data/referencias.md` líneas 2537, 2539
- **Lines**: 1586, 1587, 2537, 2539
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [18] | Modelos de precio, reg | Madhusudhanan (2024) | ProbSAINT: Probabilistic Tabular Regression for Used Car Pricing |»
- **Notes**: [18] verificada con 13 citas en OpenAlex y versión IEEE BigData 2024 (línea 2539); citada en §71.14.

### C102 — Pal [19] y Arefin [20], Random Forest y Tesla

- **File**: `INFORME_TECNICO.md` líneas 1588–1589; `Data/referencias.md` líneas 2541, 2543
- **Lines**: 1588, 1589, 2541, 2543
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [20] | Modelos de precio, reg | Arefin (2021) | Second Hand Price Prediction for Tesla Vehicles |»
- **Notes**: [19] registra discrepancia de año: preprint 2017, publicación 2018.

### C103 — Krotov [21] y Brown [22], legalidad y ética del scraping

- **File**: `INFORME_TECNICO.md` líneas 1590–1591; `Data/referencias.md` líneas 2545, 2547
- **Lines**: 1590, 1591, 2545, 2547
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [21] | Ética, legalidad, proc | Krotov (2020) | Legality and Ethics of Web Scraping |»
- **Notes**: Ninguna de las dos está marcada como citada en el informe.

### C104 — Priestley [23], Hohensinner [24] y Wenger [25], calidad y provenance

- **File**: `INFORME_TECNICO.md` líneas 1592–1594; `Data/referencias.md` líneas 2549, 2551, 2553
- **Lines**: 1592, 1594, 2549, 2553
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [24] | Ética, legalidad, proc | Hohensinner (2026) | Tracing the Data Trail: A Survey of Data Provenance, Transparenc |»
- **Notes**: [24] es manuscrito enviado a ACM Computing Surveys; marcado `metadata incomplete` implícito por su condición de preprint.

### C105 — Muça [26], integración de datos públicos albaneses

- **File**: `INFORME_TECNICO.md` líneas 1558, 1595; `Data/referencias.md` línea 2555
- **Lines**: 1558, 1595, 2555
- **Types**: contextual, citation-grounded
- **Excerpt**: «Muça, Bani y Alla [26] integran datos públicos albaneses por scraping; en este trabajo el énfasis está en la conversión con TRMI fechada y en auditar la procedencia.»

### C106 — Essien [27] y Paige [28], ética del scraping

- **File**: `INFORME_TECNICO.md` líneas 1596–1597; `Data/referencias.md` líneas 2557, 2559
- **Lines**: 1596, 1597, 2557, 2559
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [27] | Ética, legalidad, proc | Essien (2023) | The Ethics of Web Scraping In Research: A Review |»

### C107 — Vidal Alejandro [29], mercado informal de divisas en Cuba

- **File**: `INFORME_TECNICO.md` líneas 1558, 1598; `Data/referencias.md` línea 2561
- **Lines**: 1558, 1598, 2561
- **Types**: contextual, citation-grounded
- **Excerpt**: «Vidal Alejandro y otros [29] estudian el mercado informal de divisas en Cuba; aquí esa tasa es una convención de conversión fechada, no el objeto de estudio.»

### C108 — Castro Fernández [30] y Ritter [31], contexto cubano

- **File**: `INFORME_TECNICO.md` líneas 1599–1600; `Data/referencias.md` líneas 2563, 2565
- **Lines**: 1599, 1600, 2563, 2565
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [30] | Cuba: divisas informal | Castro Fernández (2024) | Electromobility and Energy Transition in Cuba |»

### C109 — Ávila Castellanos [32], espera institucional por dólares

- **File**: `INFORME_TECNICO.md` línea 1601; `Data/referencias.md` línea 2567
- **Lines**: 1601, 2567
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [32] | Cuba: divisas informal | Ávila Castellanos (2024) | Currency exchange in post-ordenamiento Cuba: An exploration of i |»

### C110 — Guerra [33], Klein [34] y Srisan [35], propiedad y asequibilidad del auto

- **File**: `INFORME_TECNICO.md` líneas 1602–1604; `Data/referencias.md` líneas 2569, 2571, 2573
- **Lines**: 1602, 1604, 2569, 2573
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [33] | Cuba: divisas informal | Guerra (2015) | The geography of car ownership in Mexico City: a joint model of |»
- **Notes**: Agrupadas en el clúster «Cuba: divisas informal» pese a tratar México, EE. UU. y seguros; clasificación de clúster discutible.

### C111 — Holtz [36], Etro [37] y Quariguasi [38], señales en marketplaces

- **File**: `INFORME_TECNICO.md` líneas 1605–1607; `Data/referencias.md` líneas 2575, 2577, 2579
- **Lines**: 1605, 1607, 2575, 2579
- **Types**: contextual, citation-grounded
- **Excerpt**: «| [36] | Señales de precio en m | Holtz (2020) | Reducing Interference Bias in Online Marketplace Pricing Experim |»
- **Notes**: [38] registra discrepancia de año (2015 en OpenAlex, 2016 en Crossref).

### C112 — DfT/DVLA [39], ANFAC [40] y AEADE [41] como fuentes institucionales

- **File**: `INFORME_TECNICO.md` líneas 1608, 847, 851–852; `Data/referencias.md` líneas 2580–2584
- **Lines**: 847, 851, 1608, 2580, 2584
- **Types**: contextual, citation-grounded
- **Excerpt**: «Los trabajos [1], [9], [14], [26] y [29] se discuten además en §71.6; el resto se registra aquí con su marcador numérico y se enlaza a `Data/referencias.md`.»
- **Notes**: §18 línea 847 da la URL profunda de DVLA y la fecha de actualización 23/09/2026, contradiciendo parcialmente el flag `(metadata incomplete: URL profunda no confirmada)` de línea 2580.

### C113 — Clasificación de calidad por antigüedad según el estudio PUCE

- **File**: `INFORME_TECNICO.md` §17 línea 826, §19 línea 882
- **Lines**: 826, 882
- **Types**: contextual, citation-grounded
- **Excerpt**: «Asimetría de información (Akerlof); clasificación de calidad por antigüedad (≤5 años alta, >5 años con defectos); encuesta a 130 comerciantes»
- **Restated**: El marco adaptado toma del estudio PUCE la regla ≤5 años = alta calidad, >5 años = con defectos.
- **Notes**: Regla declarada como marco, no validada en la muestra cubana; el storytelling línea 1887 la matiza («ya no podemos afirmar que caigan más rápido de forma significativa»).

### C114 — Marco genérico de ocho pasos adaptado a La Habana

- **File**: `INFORME_TECNICO.md` §19 líneas 866–884; §20 línea 890
- **Lines**: 866, 890, 884
- **Types**: methodological, contextual
- **Excerpt**: «Marco general (8 pasos, derivado de los trabajos revisados) [...] Adaptación a Cuba / La Habana»
- **Restated**: El análisis se organiza en ocho pasos genéricos (§19) y en nueve bloques operativos (§20) adaptados a La Habana.
- **Notes**: ⚠️ §20 línea 895 aún lista la Resolución 312/2026 como vigente; ver C011.

### C115 — Definición de TRMI y glosario del README

- **File**: `README.md` línea 1759; `INFORME_TECNICO.md` §71.5 línea 1552
- **Lines**: 1759, 1552
- **Types**: definitional
- **Excerpt**: «**Términos:** TRMI (tasa de cambio informal), KPI (indicador), OLS (mínimos cuadrados ordinarios), UTM (parámetros de seguimiento), E-E-A-T […] CDN […] long-form (texto extenso).»
- **Notes**: Definiciones, no afirmaciones falsables; se registran por ser operativas para C010 y C014.

## Contradicciones detectadas (resumen descriptivo)

| # | Afirmación A | Afirmación B / CSV | Archivos y líneas |
|---|---|---|---|
| 1 | H1 «controlando por antigüedad y kilometraje» | Kruskal-Wallis no ajustado, sin covariables | `INFORME_TECNICO.md` 30, 172 vs 2118–2122; `tests.csv` |
| 2 | «981 candidatas», «584 observaciones» | 993 candidatas, 586 observaciones | `INFORME_TECNICO.md` 1524, 1525, 1531 vs 1410, 1418; `modelo_muestra.csv`; `MODELOS_Y_FUNCIONES.md` 2108 |
| 3 | 312/2026 en el marco normativo | 312 derogada por 340 | `INFORME_TECNICO.md` 895 vs 1332, 154; `README.md` 1770 |
| 4 | Capítulo 13 ONEI «permite incorporar parque automotor, matriculaciones» | «No hay series de parque automotor ni de matriculaciones» | `INFORME_TECNICO.md` 1346 vs 1380 |
| 5 | Overpass «no hay datos geográficos útiles» | Overpass devuelve 137 gasolineras | `INFORME_TECNICO.md` 1114 vs 1183 |
| 6 | 137 gasolineras en el mapa | 131 gasolineras como «estado final» | `INFORME_TECNICO.md` 1185 vs 1206 |
| 7 | 66 anomalías | 89 anomalías vigentes | `INFORME_TECNICO.md` 1235 vs 1408; `anomalias.csv` |
| 8 | +21 % premium vigente | Prima premium no significativa | `INFORME_TECNICO.md` 1085, 1235 vs 1410, 2029; `modelo_depreciacion.csv` |
| 9 | IC bootstrap premium−económico 10.000–29.500 USD | Coeficiente premium p=0,8753 | `INFORME_TECNICO.md` 1537 vs 2029; `comparaciones.csv` vs `modelo_depreciacion.csv` |
| 10 | «El modelo exige más de 30 filas» | Modelo completo con 28 observaciones | `MODELOS_Y_FUNCIONES.md` 2099 vs 2108; `modelo_muestra.csv` |
| 11 | Semilla «se propaga a cada etapa» | «Solo la consume `03c_comparaciones.py`» | `INFORME_TECNICO.md` 1552 vs `AUTOMATIZACION.md` 2313 |
| 12 | Red 5–10 / 50–90 MB por mes | Red ~2–3 / ~56–100 MB por mes | `INFORME_TECNICO.md` 1462 vs `AUTOMATIZACION.md` 2382 |
| 13 | Panel con seis gráficos Plotly | Panel único de 107 KB sin externos | `INFORME_TECNICO.md` 1428 vs `AUTOMATIZACION.md` 2317 |
| 14 | DuckDB «se desinstaló» | DuckDB ocupa 66 MB en el entorno en uso | `INFORME_TECNICO.md` 1068 vs `ESTRUCTURA_ESPACIO.md` 2429 |
| 15 | «No se ha declarado todavía una licencia» | «Licencia: código MIT y datos CC BY 4.0» | `INFORME_TECNICO.md` 1552, 1564 vs `README.md` 1768 |
| 16 | DVLA verificada externamente | `[39] (metadata incomplete: URL profunda no confirmada)` | `INFORME_TECNICO.md` 1506–1508, 847 vs `Data/referencias.md` 2580 |
| 17 | «Cada cifra se contrastó contra los CSV» | 981/584 persisten en §71 | `INFORME_TECNICO.md` 1498 vs 1524, 1531; `modelo_muestra.csv` |
| 18 | 8 marketplaces / 2.232 anuncios | nueve marketplaces enumerados / 2.174 limpios | `README.md` 1623, 1678 vs `INFORME_TECNICO.md` 82, 153; `kpis.csv` |
| 19 | 17 de 18–25 prefieren eléctrico | 14 de 28 interesados | `INFORME_TECNICO.md` 1298 vs `PRESENTACION_STORYTELLING.md` 1909 (explicado por el filtro en 1314) |
| 20 | Autocubana 667 / Timbirichi 281 (17/11) | 566 / 170 (18/11) | `INFORME_TECNICO.md` 82 vs 1156 |
| 21 | «El scraping sostenible no depende principalmente del fingerprint TLS» | Impersonación Chrome como vía anti-403 | `INFORME_TECNICO.md` 155 vs 1129, 2491 |
| 22 | 111 PDF + 7 RAR + 103 Excel = 221 | «12 anuarios, 233 archivos» | `INFORME_TECNICO.md` 1342 vs `README.md` 1632 |

## Truncation note

Sin truncamiento: se inventariaron los 10 archivos completos (2.584 líneas, 43.233 palabras).

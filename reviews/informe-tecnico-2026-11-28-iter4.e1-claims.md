---
type: audit-artifact
phase: e1-claims
slug: informe-tecnico-2026-11-28-iter4
generated_at: 2026-11-28T11:00:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-28-iter4/informe-tecnico-2026-11-28-iter4.text.md
language: es
---

# Claim Inventory

## Summary
- Total: 125
- Load-bearing: 15 · Supporting: 72 · Contextual: 38
- By type: result 66 · methodological 45 · novelty 3 · contextual 43 · definitional 9 · citation-grounded 5

## Load-bearing claims

### C001 — Hipótesis falsable H1 y rechazo con Kruskal-Wallis

- **Section**: Resumen (VSN-C) (L14–21); Abstract (VSN-C) (L156–163)
- **Lines**: 21, 163
- **Types**: result, methodological
- **Excerpt**: «**Hipótesis falsable (H1):** «los precios de los tres tiers de marca en el mercado local provienen de la misma distribución, controlando por antigüedad y kilometraje». Se contrasta con Kruskal-Wallis; se rechaza con p < 0,001 en la corrida vigente.»
- **Restated**: En la corrida vigente se rechaza con p < 0,001 la hipótesis de que los tres tiers de marca provienen de la misma distribución de precios, controlando por antigüedad y kilometraje.
- **Internal evidence cited**: §71.3 (L1528: H = 44,313; IC bootstrap 10.000–29.500 USD), §60 (L1409: Kruskal-Wallis p = 0,00000), §71.2 (L1522)
- **External evidence cited**: — (sin citas numeradas en el enunciado)
- **Novelty signals**: «Hipótesis falsable (H1)» (L21), «Falsifiable hypothesis (H1)» (L163)
- **Notes**: el paralelo inglés (L163) declara el mismo rechazo con la notación «p < 0.001»; §60 y §71.3 usan «0,00000» y H = 44,313.

### C002 — Cifras canónicas de la corrida vigente del 27/11/2026

- **Section**: §59 Storytelling alineado con los datos finales (L1397–1403)
- **Lines**: 1399
- **Types**: result
- **Excerpt**: «El relato ahora usa **<!-- kpi:autos_revolico -->974 autos únicos**, **<!-- kpi:anuncios_totales -->2.174 anuncios limpios** (<!-- kpi:anuncios_locales -->1.483 locales y <!-- kpi:anuncios_importacion -->691 de importación), mediana local de **<!-- kpi:precio_mediano_usd -->21.000 USD**,…»
- **Restated**: La corrida vigente produce 974 autos únicos, 2.174 anuncios limpios (1.483 locales y 691 de importación), mediana local 21.000 USD, kilometraje mediano 32.569 km, 50 marcas, 114 grupos comparables y 89 anomalías.
- **Internal evidence cited**: §59 (L1403, espejo inglés con 974/2.174/21.000 USD), §58 (L1391, estado previo 2.014 anuncios y 44.125 km), §71.1 (L1511–1512, 1.462 anuncios en las bases)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: los marcadores `<!-- kpi:... -->` forman parte del texto cacheado; la frase «los valores se actualizan solos» remite al actualizador de `outputs/tables/kpis.csv`.

### C003 — Depreciación anual y prima premium retiradas en la corrida vigente

- **Section**: §59 (L1401); §60 Inventario de funciones y modelos (L1409)
- **Lines**: 1401
- **Types**: result, methodological
- **Excerpt**: «La depreciación se reformuló con honestidad: el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra.»
- **Restated**: En la corrida vigente el coeficiente de edad del modelo hedónico no es significativo tras controlar por kilometraje y no se reporta una prima premium cuantificada.
- **Internal evidence cited**: §60 (L1409: p mínimo 0,0941; VIF 1,12–1,40; Kruskal-Wallis p = 0,00000), §71.2 (L1522), §71.4 (L1537), §34 (L1076: cifra retirada de −5,43 % anual)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: §44 (L1226)conserva −5,43 %, +21 % y −22 % con la salvedad explícita de que la corrida vigente ya no los sostiene; §45 (L1234) conserva −5,43 % sin esa salvedad.

### C004 — Ablación del término `hp`: muestra y R²

- **Section**: §71.2 Ablación explícita / Explicit ablation (L1520–1524)
- **Lines**: 1522
- **Types**: result, methodological
- **Excerpt**: «`modelo_muestra.csv` documenta la ablación del término `hp`: al retirarlo, la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² baja de 0,274 a 0,101. El cambio de especificación y el cambio de muestra se informan juntos.»
- **Restated**: Retirar `hp` reduce el R² de 0,274 a 0,101 y amplía la muestra de 28 a 584 de 981 candidatas, informando ambos cambios conjuntamente.
- **Internal evidence cited**: §59 (L1401: 28 observaciones, R² 0,274, p del F 0,411), §71.1 (L1516: modelo principal con 584 observaciones y R² 0,101)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: el propio apartado atribuye la pendiente positiva de antigüedad a la selección de anuncios con kilometraje declarado, no a una tasa de depreciación (L1522).

### C005 — Intervalo bootstrap de la diferencia de medianas premium−económico

- **Section**: §71.3 Pruebas y tamaño muestral / Tests and sample size (L1526–1530)
- **Lines**: 1528
- **Types**: result, methodological
- **Excerpt**: «El contraste central se cuantifica con H = 44,313 y un intervalo bootstrap de la diferencia de medianas premium−económico de <!-- kpi:ci_bajo -->10.000 a <!-- kpi:ci_alto -->29.500 USD (`comparaciones.csv`, 2.000 réplicas).»
- **Restated**: El contraste central se cuantifica con H = 44,313 y un intervalo bootstrap de 10.000 a 29.500 USD para la diferencia de medianas entre premium y económico, con 2.000 réplicas.
- **Internal evidence cited**: §71.1 (L1511–1512: bases informan solo MAE), §60 (L1409), §71.4 (L1537)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: es el único intervalo numérico declarado en el documento; las bases de comparación de §71.1 no llevan intervalo asociado a su MAE.

### C006 — Semilla declarada y propagada a cada etapa

- **Section**: §71.5 Protocolo, semillas y reproducción / Protocol, seeds and reproduction (L1541–1545)
- **Lines**: 1543
- **Types**: methodological
- **Excerpt**: «La semilla `SEED = 20261127` está declarada en `run_all.py` y se propaga a cada etapa por la variable de entorno `PROYECTO_SEED`; antes se declaraba sin efecto.»
- **Restated**: La semilla 20261127 está declarada en el orquestador y se propaga a las etapas mediante la variable de entorno `PROYECTO_SEED`, frente a la declaración anterior sin efecto.
- **Internal evidence cited**: §71.5 (L1543: comando único, puntos de entrada, dependencias fijadas y prueba de humo), §69 (L1489: registro de auditoría)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: el enunciado consigna explícitamente el cambio de estado respecto de la declaración sin propagación.

### C007 — Declaración de uso de inteligencia artificial

- **Section**: §69 Declaración de uso de inteligencia artificial / AI-use declaration (L1487–1491)
- **Lines**: 1489
- **Types**: methodological
- **Excerpt**: «Las herramientas de IA (OpenCode/Claude Code con las skills `review`, `deep-research` y `technical-writing`) se usaron en investigación, redacción, código y traducción. Cada cifra se contrastó contra los CSV versionados y las pruebas automatizadas; la huella queda en `reviews/`. Un ejemplo…»
- **Restated**: Las herramientas de IA se usaron en cuatro labores declaradas y cada cifra fue contrastada contra CSV versionados y pruebas automatizadas, con un ejemplo concreto de corrección de R².
- **Internal evidence cited**: §59 (L1401: R² 0,274), §70 (L1497), mención de `reviews/informe-tecnico-2026-11-27-iter3.{md,forensic.md}` y sus 13 artefactos (L1489)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: el texto de esta iteración ya no enumera las cuatro fases ni los tres pasos de supervisión registrados en la iteración 3; conserva el ejemplo de corrección y el apuntador a la pasada anterior.

### C008 — Declaraciones éticas, de doble uso y de disponibilidad

- **Section**: §71.15 Declaraciones / Declarations (L1551–1555)
- **Lines**: 1553
- **Types**: methodological, definitional
- **Excerpt**: «No se reclutaron sujetos humanos: la encuesta de 33 respuestas y las entrevistas se tratan como documentación de contexto, no como datos experimentales; no se requirió un procedimiento de anonimización ejecutado. Se declara ausencia de conflicto de intereses. El tema no se considera de…»
- **Restated**: El documento declara ausencia de sujetos reclutados, de procedimiento de anonimización ejecutado, de conflicto de intereses y de doble uso sensible, con datos y código disponibles según §71.5 y licencia pendiente.
- **Internal evidence cited**: §71.5 (L1543: repositorio público, comando único y Git LFS), §50 (L1289: 33 respuestas y entrevistas)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: el apartado se numera 71.15 y antecede al 71.14 (L1557).

### C009 — Referencias verificadas y convención numérica

- **Section**: §70 Referencias verificadas / Verified references (L1495–1499); §71.14 Obras del mapa literario citadas en el cuerpo (L1557–1600)
- **Lines**: 1497, 1499
- **Types**: citation-grounded
- **Excerpt**: «Referencias citadas y verificadas externamente durante la auditoría: Akerlof (1970), *The Market for "Lemons"* (DOI 10.2307/1879431 confirmado en OpenAlex; el resumen indexado es solo un índice de secciones, por lo que su flag es `(metadata incomplete: resumen)`); UK Department for…»
- **Restated**: El documento declara cuatro referencias verificadas externamente, con el resto marcado como `(metadata incomplete)`, y remite la convención numerada a `Data/referencias.md`.
- **Internal evidence cited**: §18 (L838–849: tabla de procedencia), §71.6 (L1549), §71.14 (L1561–1598: fichas [1]–[38])
- **External evidence cited**: [1] Akerlof (1970), DOI 10.2307/1879431 confirmado en OpenAlex; DfT/DVLA (GOV.UK); ANFAC (sitio oficial); AEADE (sitio oficial) — todos según L1497
- **Novelty signals**: ninguno.
- **Notes**: la convención declarada es de «38 referencias» (L1497, L1499) y la tabla de §71.14 llega a [38] (L1598); el resto se remite a `reviews/informe-tecnico-2026-11-27.e2-literature.md`.

### C010 — Objetivo vigente: análisis de mercado; recomendador diferido

- **Section**: §1 Objetivo (L23–27); §21 Cambio de objetivo (L899–908); Parte II §1 (L165–169); Parte II §12 (L284–290)
- **Lines**: 25
- **Types**: definitional, contextual
- **Excerpt**: «El proyecto se llama **El precio de moverse en Cuba**. Su objetivo actual es realizar un **análisis del mercado automotor cubano**: caracterizar estructura, precios, oferta, segmentos, tendencias, asequibilidad y condiciones de rentabilidad. La definición de un producto interactivo que…»
- **Restated**: El objetivo declarado es el análisis del mercado automotor cubano y no la recomendación interactiva, diferida a una especialización futura.
- **Internal evidence cited**: §21 (L903–905), Parte II §12 (L290), Parte II §1 (L167)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: la conclusión 5 inglesa (L290) declara ahora el mismo diferimiento que la Parte I (L148), sin la contradicción registrada en la iteración 3.

### C011 — Fase 8 implementada y regenerada automáticamente

- **Section**: §12 Conclusiones (L142–148); §2 nota de actualización (L47); §61 Sitio MkDocs (L1415–1421)
- **Lines**: 148
- **Types**: result, methodological
- **Excerpt**: «El análisis de mercado y el modelo de rentabilidad (fase 8) están implementados en `Data/analisis_rentabilidad/` y se regeneran de forma automática; la definición del producto interactivo se difiere a una especialización futura.»
- **Restated**: El pipeline de análisis y rentabilidad existe en `Data/analisis_rentabilidad/` y puede regenerarse automáticamente.
- **Internal evidence cited**: §34 (L1036–1057), §59 (L1399), §61 (L1417–1419)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: la nota de §2 (L47) data la creación del pipeline el 18/11/2026 y remite sus resultados vigentes a §59–§60.

### C012 — Procedencia de los datos y separación de tasas y precios

- **Section**: §18 Auditoría de procedencia (L834–853); §23 (L922); §71.4 (L1534)
- **Lines**: 851
- **Types**: methodological, definitional
- **Excerpt**: «**Conclusión:** las fuentes oficiales y gremiales sirven de **contexto y validación**; los anuncios y redes son la **señal de precio** pero no sustituyen estadísticas oficiales. El análisis debe etiquetar cada métrica con su procedencia y nivel de confianza, y no mezclar tasas oficiales e…»
- **Restated**: El análisis trata los anuncios como señal de precio pedido, etiqueta cada métrica con procedencia y confianza, y prohíbe mezclar tasas oficiales con informales o precios anunciados con transaccionados.
- **Internal evidence cited**: §18 (L838–849: tabla de procedencia), §23 (L922: TRMI fija de 930 CUP/USD), §52 (L1317: API del BCC como referencia oficial)
- **External evidence cited**: DfT/DVLA y ANFAC/AEADE, declarados verificados en vivo en §18 (L838, L842–843) y §70 (L1497)
- **Novelty signals**: ninguno.
- **Notes**: el par inglés (L853) repite la misma restricción con «advertised-price signals only».

### C013 — Posicionamiento frente a trabajos cercanos con remisiones [14], [26], [9], [29]

- **Section**: §71.6 Posicionamiento frente a trabajos cercanos / Positioning against prior work (L1547–1549)
- **Lines**: 1549
- **Types**: novelty, citation-grounded
- **Excerpt**: «Gegić y otros [14] predicen precios con aprendizaje automático sobre catálogos estructurados; aquí las variables se extraen de anuncios en lenguaje libre, así que el aporte es de procedencia y normalización, no de algoritmo. Muça, Bani y Alla [26] integran datos públicos albaneses por…»
- **Restated**: El aporte se diferencia de cuatro trabajos cercanos por procedencia y normalización, conversión con TRMI fechada, ausencia de tasa anual y tratamiento de la divisa informal como convención.
- **Internal evidence cited**: §70 (L1497), §71.14 (L1569 [9], L1574 [14], L1586 [26], L1589 [29])
- **External evidence cited**: [14] Gegić (2019), [26] Muça (2026), [9] Du (2026), [29] Vidal Alejandro (2024), según las fichas de §71.14
- **Novelty signals**: «el aporte es de procedencia y normalización, no de algoritmo» (L1549); «el énfasis está en la conversión con TRMI fechada» (L1549)
- **Notes**: el pasaje incorpora marcadores numéricos [14], [26], [9] y [29]; L1600 enlaza las fichas con `Data/referencias.md`.

### C014 — Novedad declarada: procedencia y normalización como objeto de auditoría

- **Section**: Resumen (VSN-C) (L18); Abstract (VSN-C) (L160)
- **Lines**: 18
- **Types**: novelty, methodological
- **Excerpt**: «**Novedad:** la procedencia y la normalización se tratan como objeto de auditoría; la pérdida de muestra por variables ausentes se reporta como hallazgo y no se oculta.»
- **Restated**: La novedad reclamada es el tratamiento de la procedencia y la normalización como objeto de auditoría y el reporte explícito de la pérdida de muestra por variables ausentes.
- **Internal evidence cited**: §18 (L834–853), §60 (L1409), §71.2 (L1522), §71.4 (L1535)
- **External evidence cited**: —
- **Novelty signals**: «Novedad» (L18), «News» (L160), «no se oculta» (L18), «is reported as a finding» (L160)
- **Notes**: el resumen inglés (L160) llama «News» a este apartado y usa «sample loss from missing variables is reported as a finding».

### C015 — Contribuciones declaradas en el resumen VSN-C

- **Section**: Resumen (VSN-C) (L19); Abstract (VSN-C) (L161); §69 (L1489)
- **Lines**: 19
- **Types**: result, novelty
- **Excerpt**: «**Contribuciones:** base compacta reproducible, panel interactivo autocontenido, pipeline con timers y un expediente de auditoría con 13 artefactos.»
- **Restated**: Las contribuciones declaradas son una base compacta reproducible, un panel interactivo autocontenido, un pipeline con timers y un expediente de auditoría de 13 artefactos.
- **Internal evidence cited**: §54 (L1345: chunks y manifiesto), §61 (L1419: `Data/dashboard.html`), §65 (L1453: cinco timers), §69 (L1489: 13 artefactos de la pasada anterior)
- **External evidence cited**: —
- **Novelty signals**: «Contribuciones» (L19), «Contributions» (L161)
- **Notes**: la cifra 13 se apoya en la huella de la iteración 3 citada en L1489, no en una enumeración de esta sección.

## Supporting claims (72)

### C016 — Diecisiete empresas autorizadas y Decreto 163/2026
- **Section**, **Lines**: §4 Marco normativo y regulatorio (L65–67), 67
- **Types**: result, contextual
- **Excerpt**: «Se documentaron **17 empresas autorizadas** a importar y comercializar vehículos, distribuidores privados (BDC One, Dongfeng, MCV, Finauto, Changan, Chinautos, Envision, ATR Export), precios de referencia (BDC One 14.849–31.478 EUR; Dongfeng desde 21.900 EUR; Finauto desde 15.500 EUR; ATR…»
- **Restated**: La fase 1 documentó 17 empresas autorizadas, precios de referencia y el Decreto 163/2026 como norma vigente.
- **Internal/External evidence**: §4 (L67), §4 inglés (L209), §10 (L125); sin citas numeradas en el cuerpo.
- **Notes**: la derogación de la Resolución 312/2026 por la 340/2026 se registra en §52 (L1323).

### C017 — Descubrimiento de fuentes: 409 resultados, 400 únicos y 35 sitios
- **Section**, **Lines**: §5 Descubrimiento y verificación de fuentes (L69–71), 71
- **Types**: result
- **Excerpt**: «Se consolidaron **409 resultados, 400 únicos**. Se inventariaron **35 sitios** de compraventa en `Data/mercados-compraventa-cuba.md` y repositorios útiles en `Data/github-scraping-repos.md`.»
- **Restated**: La fase 2 consolidó 409 resultados, 400 únicos, e inventarió 35 sitios de compraventa.
- **Internal/External evidence**: §5 (L71, L213 en inglés); sin citas numeradas.
- **Notes**: el cambio de DuckDuckGo a Yahoo por CAPTCHA se registra en la misma línea.

### C018 — Cuarenta URLs verificadas y marketplaces con inventario real
- **Section**, **Lines**: §5 (L73)
- **Types**: result
- **Excerpt**: «Se verificaron **40 sitios/URLs**. Marketplaces con sección activa: Autocubana (667 vehículos), iTENCEL (951), VentaCuba (801 carros/camionetas), Timbirichi (281 carros), Revolico (112 enlaces en la primera página), Cogetucarro (5.225 anuncios), Cubisima (155 fichas), Apululu y Carros.com Cuba.»
- **Restated**: Se verificaron 40 sitios y nueve marketplaces presentaban sección activa con los recuentos declarados.
- **Internal/External evidence**: §5 (L73, L215), §12 (L144).
- **Notes**: la misma línea registra correcciones de clasificación de sitios sin sección real o con categoría vacía.

### C019 — Catorce organismos con competencia sobre el mercado
- **Section**, **Lines**: §5 (L75)
- **Types**: result
- **Excerpt**: «Se documentaron **14 organismos** con competencia sobre el mercado: Consejo de Ministros/Estado, MINCEX, MINCIN, MITRANS, CEMA, MFP, ONAT, Aduana General, BCC, MININT, MINJUS, MEP, MINREX y MINSAP.»
- **Restated**: La fase 2 documentó 14 organismos con competencia sobre el mercado automotor.
- **Internal/External evidence**: §5 (L75, L217).
- **Notes**: —
### C020 — Sesenta y un repositorios, 92 proyectos de CAPTCHA y 9 seleccionados
- **Section**, **Lines**: §6 Infraestructura técnica y herramientas (L77–79), 79
- **Types**: result
- **Excerpt**: «Se clonaron **61 repositorios** en `Auxiliares/Repositorios` con `--depth 1` (2,2 GB, 61 entradas `OK`). El conjunto cubre scraping general (Firecrawl, browser-use, Scrapling, crawl4ai, Scrapy, SeleniumBase, trafilatura, curl_cffi, Patchright, Playwright), Facebook, WhatsApp, Telegram y…»
- **Restated**: La fase 3 clonó 61 repositorios, clasificó 92 proyectos de CAPTCHA y seleccionó 9.
- **Internal/External evidence**: §6 (L79, L221).
- **Notes**: el entorno virtual y sus versiones se detallan en L81.

### C021 — Seis herramientas creadas en la fase 3
- **Section**, **Lines**: §6 (L83)
- **Types**: result
- **Excerpt**: «Herramientas creadas: `ddg_research.py`, `buscar_fallback.py`, `descargar_hombros.py`, `scrape_concesionarios.py`, `resumen_catalogos.py` y `actualizar_informe.py`.»
- **Restated**: La fase 3 produjo seis scripts nominales para búsqueda, descarga, scraping y actualización del informe.
- **Internal/External evidence**: §6 (L83, L225).
- **Notes**: —
### C022 — Corpus documental: tres búsquedas y regla de parada
- **Section**, **Lines**: §7 Corpus documental y trabajos investigativos (L85–95), 91–95
- **Types**: result, methodological
- **Excerpt**: «El material se guardó en `Hombros/`: descarga inicial **93 OK / 17 fallos**, rentabilidad **23 OK / 10 fallos**, calidad/precio **78 OK / 36 fallos**, con `manifest.jsonl` e `indice.md`.»
- **Restated**: La regla de parar tras 10 páginas sin enlaces útiles se aplicó a tres búsquedas y produjo los recuentos de descargas declarados.
- **Internal/External evidence**: §7 (L89–95 tabla y texto; L231–237 en inglés).
- **Notes**: la tabla registra 112/1.086/11, 24/226/2 y 23/230/10 páginas/resultados/útiles.

### C023 — Esquema SQLite por tienda con 30 campos estructurados
- **Section**, **Lines**: §8 Diseño del esquema de datos y del pipeline (L97–99), 99
- **Types**: result, definitional
- **Excerpt**: «Se diseñó una base SQLite por tienda con una tabla `vehiculos`: identificación (`url`, `shop`, `title`, `status`, `scraped_at`), metadatos y 30 campos estructurados (`marca`, `modelo`, `anio`, `precio`, `moneda`, `km`, `combustible`, `transmision`, `potencia`, etc.), además de campos sin…»
- **Restated**: La fase 5 definió una base SQLite por tienda con 30 campos estructurados y campos sin normalizar.
- **Internal/External evidence**: §8 (L99, L241).
- **Notes**: §24 (L931) precisa que los campos estructurados de año/km/marca no existen en los JSON de Revolico y se derivan por regex.

### C024 — Once bases preparadas y 256 filas en la fase 6
- **Section**, **Lines**: §9 Scraping y captura (L101–119), 103
- **Types**: result
- **Excerpt**: «Se prepararon 11 bases y se obtuvieron **256 filas**:»
- **Restated**: La fase 6 preparó 11 bases de tienda con 256 filas en total, según la tabla de L105–L117.
- **Internal/External evidence**: §9 (L105–117 tabla; L245–259 en inglés).
- **Notes**: la tabla suma 60+6+19+2+70+1+45+1+45+4+3 = 256 filas.

### C025 — Exclusiones técnicas y densidad de la fase 6
- **Section**, **Lines**: §9 (L119)
- **Types**: result
- **Excerpt**: «Excluidas por bloqueo técnico: carrosw (HTTP 403 con Bot Verification), LlamaCuba (timeout) y SASA/DIVEP (sin catálogo). Mejor densidad: AGN Motors, Chinautos Cuba, Dongfeng Cuba y Finauto. Esta fase sigue abierta: quedan por ampliar fuentes y completar campos.»
- **Restated**: Tres tiendas quedaron excluidas por bloqueo técnico y cuatro se señalan como de mejor densidad, con la fase aún abierta.
- **Internal/External evidence**: §9 (L119, L261).
- **Notes**: Chinautos Cuba aporta 70 filas pero 0 con precio (L111).

### C026 — No elusión anti-automatización y datos agregados
- **Section**, **Lines**: §10 Marco legal (L121–129), 127–128
- **Types**: methodological, definitional
- **Excerpt**: «**Condiciones de uso de cada portal**: criterio operativo para la recolección. No se eluden mecanismos anti-automatización; los HTTP 403/429 se registran como limitación.»
- **Restated**: La recolección declara no eludir mecanismos anti-automatización y registrar los HTTP 403/429 como limitación.
- **Internal/External evidence**: §10 (L127, L269), §11 (L138).
- **Notes**: L128 añade la condición de publicar solo datos agregados, sin nombres, teléfonos ni información personal.

### C027 — Cuatro primeras conclusiones del informe
- **Section**, **Lines**: §12 Conclusiones (L142–148), 144–147
- **Types**: result, contextual
- **Excerpt**: «1. El mercado habanero tiene nueve marketplaces con inventario real y una docena con categorías vacías o solo piezas. / 2. El marco regulatorio vigente es el Decreto 163/2026 y el paquete de resoluciones citado. / 3. El scraping sostenible depende del ritmo, la sesión y la reanudación, no…»
- **Restated**: Las conclusiones 1–4 afirman nueve marketplaces reales, el Decreto 163/2026, la primacía del ritmo y la sesión sobre el fingerprint TLS, y la eficacia de la regla de 10 páginas.
- **Internal/External evidence**: §5 (L71–75), §10 (L125), §11 (L135–140), §7 (L87).
- **Notes**: la conclusión 5 se inventaría por separado (C011).

### C028 — Sincronización de Revolico en fragmentos de 16 MiB
- **Section**, **Lines**: §14 Sincronización automática de Revolico (L774–783), 776
- **Types**: methodological, result
- **Excerpt**: «La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**. Cada 10 minutos un timer de systemd ejecuta `Auxiliares/herramientas/actualizar_revolico.py`: corre el scraper incremental, divide la BD en partes de 16 MiB dentro de `Data/Revolico/partes/`, sube solo las partes…»
- **Restated**: La base de Revolico se sincroniza cada 10 minutos en partes de 16 MiB, con reconstrucción verificada por hash.
- **Internal/External evidence**: §14 (L778–783 tabla: última ejecución 2026-11-17T15:47:42+00:00, 795373568 B, 48 partes).
- **Notes**: §54 (L1345) describe un esquema posterior de 82 chunks de 10 MB sobre 849.465.344 bytes.

### C029 — Eficiencia comparada de Telegram, Facebook, WhatsApp y Playwright
- **Section**, **Lines**: §15 Eficiencia de Telegram, WhatsApp y Facebook (L785–789), 787
- **Types**: methodological
- **Excerpt**: «Para obtener más datos del mercado habanero, la ruta más eficiente es Telegram MTProto (`telethon`, ya integrado): sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`. Le sigue Facebook GQL (`facebook_gql_scraper`): llamadas GraphQL…»
- **Restated**: El documento ordena las rutas de captura por eficiencia, con Telegram MTProto primero, Facebook GQL después y Playwright/Selenium como último recurso.
- **Internal/External evidence**: §15 (L787, L789).
- **Notes**: para WhatsApp declara «no existe API pública personal» y propone WAHA auto-hospedado.

### C030 — Limpieza de 6.332 anuncios: 304 autos y 6.028 exclusiones
- **Section**, **Lines**: §15 (L791–793), 793
- **Types**: result
- **Excerpt**: «**Limpieza ejecutada / Cleaning run (17/11/2026):** sobre los 6.332 anuncios actuales, `limpiar_revolico.py` conservó **304 autos** en la tabla `autos` y registró **6.028 exclusiones** en `revision` (5.983 no vehículo 4+ ruedas, 45 sin datos necesarios, 0 páginas sin datos suficientes).»
- **Restated**: La limpieza del 17/11 conservó 304 autos y registró 6.028 exclusiones sin borrar filas originales.
- **Internal/External evidence**: §15 (L791–793), §31 (L1009: corrida posterior sobre 9.957 anuncios).
- **Notes**: la columna de auditoría `es_auto`, `motivo_exclusion`, `pagina_revisada` y `datos_necesarios` se declara conservada en `anuncios`.

### C031 — Permanencia empírica de los anuncios de Revolico
- **Section**, **Lines**: §15 (L795)
- **Types**: result
- **Excerpt**: «Empíricamente, un anuncio con `updated_on_by_user=2024-12-17` seguía en HTTP 200 el 17/11/2026 (~699 días), por lo que no puede asumirse una expiración de 30 días. El 99,3 % de los anuncios tiene `updated_on_by_user` en los últimos 7 días (mediana 1 día en los 189 autos), lo que indica…»
- **Restated**: Un anuncio con 699 días de antigüedad seguía accesible y el 99,3 % fue actualizado en los últimos 7 días, lo que descarta asumir expiración de 30 días.
- **Internal/External evidence**: §15 (L795), §31 (L1009: anuncio más antiguo 2024-12-17).
- **Notes**: las Condiciones de Uso de Revolico (23/09/2026) no fijan plazo de caducidad según el mismo renglón.

### C032 — Pipeline de colas con commit cada 25 anuncios
- **Section**, **Lines**: §16 Pipeline de colas (L797–809), 803
- **Types**: methodological, result
- **Excerpt**: «3. **Procesamiento**: workers clasifican cada anuncio con `limpiar_revolico.clasificar` y escriben la decisión en `process_queue`. Cada **25 anuncios procesados** (aceptados o rechazados) se hace un commit por lotes en `anuncios`/`autos`/`imagenes`/`telefonos` o en `revision`.»
- **Restated**: El pipeline separa descubrimiento, descarga y procesamiento con colas persistentes y hace commit cada 25 anuncios procesados.
- **Internal/External evidence**: §16 (L799–809), §26 (L948–955: orden corregido), §66 (L1461: lotes de 50 en la corrida posterior).
- **Notes**: L805 registra que `--skip-unchanged` quedó desactivado porque `updatedOnToOrder` es marcador de ranking, no de edición.

### C033 — Prueba del pipeline de colas con una página
- **Section**, **Lines**: §16 (L807)
- **Types**: result
- **Excerpt**: «Prueba con 1 página: **119 enlaces** descubiertos y procesados, 7 lotes de 25, BD principal de 6.332 a **6.334 anuncios** y de 304 a **317 autos**. Todo queda auditado; no se descarta información.»
- **Restated**: La prueba con una página procesó 119 enlaces en 7 lotes y elevó la base de 6.332 a 6.334 anuncios y de 304 a 317 autos.
- **Internal/External evidence**: §16 (L807, L809), §19 (L871: 6.334/317).
- **Notes**: §26 (L955) registra una prueba distinta con 120 enlaces, 63 rechazos tempranos y 326 autos.

### C034 — Siete requerimientos derivados de las fuentes revisadas
- **Section**, **Lines**: §17 Guía de análisis de mercado (L811–832), 830
- **Types**: methodological
- **Excerpt**: «**Requerimientos derivados:** (1) esquema común con precio+moneda normalizada, año/km/combustible/transmisión/marca/modelo/provincia/tipo de vendedor y procedencia; (2) clasificación de calidad y estimación de costos ocultos; (3) comparables por marca-modelo-año-provincia; (4) modelo de…»
- **Restated**: El marco de análisis deriva siete requerimientos, desde esquema común hasta dashboard y validación sin datos personales.
- **Internal/External evidence**: §17 (L815–827 tabla de fuentes; L830), §19 (L868–875), §20 (L881–895).
- **Notes**: la ponderación de preferencias y el producto interactivo quedan fuera de alcance (L830).

### C035 — Clasificación de fuentes por naturaleza y confianza
- **Section**, **Lines**: §18 Auditoría de procedencia (L834–849), 838–849
- **Types**: methodological, contextual
- **Excerpt**: «CarDekho (Kaggle), Spinny, OLX, Revolico, Autocubana, Dongfeng | **Marketplace / anuncios** | No son estadísticas oficiales; son precios **pedidos**, no transaccionados | Señal de precios; requiere dedup, verificación y sesgo declarado»
- **Restated**: La tabla de procedencia clasifica doce tipos de fuente y asigna a los anuncios el papel de señal de precio, no de estadística oficial.
- **Internal/External evidence**: §18 (L838–849), §70 (L1497).
- **Notes**: DfT/DVLA y ANFAC/AEADE figuran como verificados en vivo (L838, L842–843); VAHAN y BCC como no accesibles desde el entorno (L839–840).

### C036 — Adaptación a La Habana: fuentes, variables y límites
- **Section**, **Lines**: §19 Marco de análisis de mercado (L855–877), 871–875
- **Types**: methodological
- **Excerpt**: «- **Fuentes**: Revolico (BD propia, 6.334 anuncios / 317 autos), concesionarios (Autocubana, Dongfeng, BDC One…), Gaceta/Decreto 163/2026, BCC (oficial) y elTOQUE (informal), salarios de la Resolución 14, y señales de Telegram/WhatsApp/Facebook sin datos personales.»
- **Restated**: La adaptación a La Habana declara fuentes, variables, métodos y límites, con precios anunciados separados por moneda.
- **Internal/External evidence**: §19 (L871–875), §20 (L883–891).
- **Notes**: las clases de calidad «≤5 años alta, >5 años con defectos» se atribuyen a PUCE (L873) y a la tabla de §17 (L817).

### C037 — Activos existentes y datos pendientes del marco detallado
- **Section**, **Lines**: §20 Marco analítico detallado (L879–897), 893–895
- **Types**: result
- **Excerpt**: «**Lo que ya existe:** BD de 6.334 anuncios / 317 autos, esquema con 30 campos + auditoría, imágenes/teléfonos, snapshots de precios, normativa documentada, tasas y salarios referenciados, repositorios de modelos y dashboards.»
- **Restated**: El marco detallado enumera activos disponibles y, en la línea siguiente, datos aún pendientes como costos ocultos y precios de transacción.
- **Internal/External evidence**: §20 (L893–895), §56 (L1371: los anuarios no resuelven la laguna de parque y matriculaciones).
- **Notes**: la lista de pendientes incluye año/km/marca/modelo estructurados, series históricas de tasas y salarios y geocodificación (L895).

### C038 — Análisis descriptivo inicial sobre 323 autos
- **Section**, **Lines**: §22 Análisis descriptivo inicial (L910–916), 914
- **Types**: result
- **Excerpt**: «Resultados sobre 323 autos: 248 precios USD válidos (≥500 USD); 74 precios <500 USD marcados como inválidos y 1 en CUP excluidos. Precio mediano **22.000 USD**, media 24.416,59 USD, IQR 11.375–35.000 USD, rango 600–95.000 USD. Marca más frecuente: Hyundai (n=75); municipio con más oferta:…»
- **Restated**: El análisis descriptivo inicial sobre 323 autos halló 248 precios USD válidos, mediana 22.000 USD y predominio de Hyundai y Playa.
- **Internal/External evidence**: §22 (L912–916), §24 (L933: 323 autos).
- **Notes**: es una corrida anterior a la vigente documentada en §59; la mediana allí es 21.000 USD (L1399).

### C039 — Cobertura de campos derivados por heurística
- **Section**, **Lines**: §22 (L914)
- **Types**: result
- **Excerpt**: «Cobertura de campos derivados: marca 68,4 %, año 63,5 %, km 6,2 % (heurísticos, extraídos solo de título/descripción). Detectados 5 outliers por IQR.»
- **Restated**: Los campos derivados por regex cubren 68,4 % de marca, 63,5 % de año y 6,2 % de kilometraje, con 5 outliers por IQR.
- **Internal/External evidence**: §22 (L914, L916), §24 (L931), §71.4 (L1535).
- **Notes**: la baja cobertura de km se vuelve eje de la ablación de §71.2 (L1522).

### C040 — Conversión elTOQUE diaria frente a TRMI fija del modelo
- **Section**, **Lines**: §23 Conversión elTOQUE, serie temporal y gráficas (L918–927), 922
- **Types**: methodological
- **Excerpt**: «**Aclaración vigente:** el pipeline de `Data/analisis_rentabilidad/` usa la TRMI fija de 930 CUP/USD del 18/11/2026 (`config.py`); la serie diaria es referencia histórica, no insumo del modelo actual.»
- **Restated**: El pipeline vigente convierte con TRMI fija de 930 CUP/USD del 18/11/2026 y usa la serie diaria solo como referencia histórica.
- **Internal/External evidence**: §23 (L922, L924), §52 (L1317: API del BCC como referencia oficial).
- **Notes**: L924 registra la TRMI pasando de 680 CUP/USD (09/07/2026) a 920 (16–17/11/2026), ya sustituida por la convención fija.

### C041 — Serie mensual de precios y tasa
- **Section**, **Lines**: §23 (L924)
- **Types**: result
- **Excerpt**: «Ejemplo histórico: la TRMI pasó de 680 CUP/USD (09/07/2026) a 920 (16-17/11/2026), valor ya sustituido por la convención fija de 930 del 18/11/2026 que usa el pipeline; la mediana mensual CUP subió de 12,58 M (julio) a 20,7 M (noviembre).»
- **Restated**: La serie histórica muestra TRMI de 680 a 920 CUP/USD y mediana mensual CUP de 12,58 M a 20,7 M entre julio y noviembre.
- **Internal/External evidence**: §23 (L924, L925).
- **Notes**: L925 registra 8 PNG y `dashboard_interactivo.html` generados por `graficos_mercado.py`.

### C042 — Supuesto de anuncio activo = comprable
- **Section**, **Lines**: §23 (L923); §25 (L941)
- **Types**: methodological, definitional
- **Excerpt**: «**Supuesto de anuncio activo**: todos los registros tienen `status=PUBLISHED` y página verificada en la captura, por lo que se asume que son comprables; no se comprueba disponibilidad en tiempo real.»
- **Restated**: El análisis asume que los anuncios con `status=PUBLISHED` y página verificada son comprables, sin comprobación de disponibilidad en tiempo real.
- **Internal/External evidence**: §23 (L923), §25 (L941: supuesto distinto para catálogos), §19 (L875: sesgo de supervivencia).
- **Notes**: es un supuesto operativo declarado, no una verificación de transaccionalidad.

### C043 — Ausencia de campos estructurados en los JSON de Revolico
- **Section**, **Lines**: §24 Estado del scrapeo y procesamiento de diccionarios (L929–935), 931
- **Types**: result
- **Excerpt**: «**No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**: por eso `anio_est`, `marca_est` y `km_est` se derivan con regex del texto visible (cobertura 63,5 %, 68,4 % y 6,2 %).»
- **Restated**: Los diccionarios `ad_json` y `apollo_full` no contienen claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión.
- **Internal/External evidence**: §24 (L931), §22 (L914), §51 (L1302).
- **Notes**: los JSON sí guardan precio, moneda, estado, fecha y geografía (L931).

### C044 — Reporte de scrapeo y estado de colas
- **Section**, **Lines**: §24 (L933)
- **Types**: result
- **Excerpt**: «**Reporte de scrapeo:** `anuncios` 6.334 · `autos` 323 · `revision` 6.085 · `imagenes` 13.932 · `telefonos` 7.699 · BD 520,6 MB. Colas: `url_queue` 141 (125 done, 3 downloading, 13 pending); `download_queue` 125 (123 processed, 1 processing, 1 pending); `process_queue` 123 (107 committed,…»
- **Restated**: El reporte de scrapeo declara 6.334 anuncios, 323 autos, 6.085 revisiones, 13.932 imágenes y 7.699 teléfonos, con colas pendientes de una corrida interrumpida.
- **Internal/External evidence**: §24 (L933, L935), §27 (L964).
- **Notes**: los pendientes se atribuyen a un reinicio del servidor (L933).

### C045 — Reinicio automático del servicio de scrapeo
- **Section**, **Lines**: §25 Reanudación, resiliencia y supuesto de catálogos (L937–944), 940
- **Types**: methodological
- **Excerpt**: «**Reinicio automático:** `revolico-scrape.service` ahora tiene `Restart=on-failure`, `RestartSec=30`, `StartLimitIntervalSec=300` y `StartLimitBurst=20`, de modo que una pérdida de conexión que detenga el proceso provoca su relanzamiento.»
- **Restated**: El servicio de scrapeo se relanza automáticamente tras fallo con los parámetros systemd declarados.
- **Internal/External evidence**: §25 (L940), §37 (L1124), §65 (L1453).
- **Notes**: —
### C046 — Supuesto de disponibilidad de catálogos
- **Section**, **Lines**: §25 (L941)
- **Types**: methodological, definitional
- **Excerpt**: «Para concesionarios y páginas similares (`CATALOGOS`) se asume que todo el catálogo está disponible salvo que la página indique lo contrario y que se publicó el día de la captura (`fecha_publicacion = scraped_at`); el año del vehículo no es clave.»
- **Restated**: Para catálogos se asume disponibilidad total y fecha de publicación igual a la captura, salvo indicación contraria.
- **Internal/External evidence**: §25 (L941), §9 (L117).
- **Notes**: para clasificados se mantiene `fecha_publicacion = updated_on_by_user` (L941).

### C047 — Causa del retraso en clasificación y orden corregido
- **Section**, **Lines**: §26 Orden corregido (L946–957), 948
- **Types**: result, methodological
- **Excerpt**: «Se identificó la causa del retraso en la clasificación: el timer ejecutaba `actualizar_revolico.py`, que solo corre el scraper y divide la BD, sin escribir nunca `autos`/`revision`. El servicio ahora ejecuta `scrape_revolico_pipeline.py`, que sigue el orden pedido:»
- **Restated**: El retraso se atribuyó a que el timer ejecutaba un script que no escribía `autos`/`revision`, y se corrigió ejecutando el pipeline de colas.
- **Internal/External evidence**: §26 (L948–955), §16 (L799–807).
- **Notes**: la prueba posterior registra 120 enlaces, 63 descartados tempranamente y autos 323→326 (L955).

### C048 — Umbral de 4.000 anuncios sin revisar
- **Section**, **Lines**: §27 Aviso periódico y umbral de revisión (L959–966), 961–964
- **Types**: methodological, result
- **Excerpt**: «**Umbral:** cuando `anuncios WHERE pagina_revisada=0`llega a **4.000** (configurable con `REVISAR_UMBRAL`), el aviso lanza `revolico-revisar.service`, que ejecuta el pipeline con `--solo-colas`: drena descargas y decisiones pendientes **sin descubrir páginas nuevas**.»
- **Restated**: Un timer de 10 minutos avisa el progreso y lanza el drenaje de colas cuando los anuncios sin revisar alcanzan 4.000.
- **Internal/External evidence**: §27 (L961–964), §33 (L1030).
- **Notes**: el estado declarado es 3.623 sin revisar, por debajo del umbral (L964).

### C049 — Primera corrida del scraper público de Telegram
- **Section**, **Lines**: §28 Primeros datos de Telegram (L968–976), 970–974
- **Types**: result
- **Excerpt**: «Corrida final (50 páginas): **152 mensajes**, **54 anuncios de autos** del canal `goldenbullbusinessfamilycars`, 45 con año detectable y **ninguno con precio explícito** (el canal expresa kilómetros como `25500K`, `40K`, etc.). Esta fuente sirve hoy para señal de oferta/modelo/año, no de precio.»
- **Restated**: La corrida de 50 páginas obtuvo 152 mensajes y 54 anuncios de autos sin precio explícito, útiles solo como señal de oferta/modelo/año.
- **Internal/External evidence**: §28 (L972–974), §29 (L988–991).
- **Notes**: once canales adicionales probados resultaron no aprovechables sin unirse (L974).

### C050 — Base de datos de Telegram y descubrimiento de canales
- **Section**, **Lines**: §29 Base de datos de Telegram (L978–993), 986–991
- **Types**: result
- **Excerpt**: «| `canales` | 119 | ... | `anuncios` | 54 | ... | `anuncios` marcados `es_auto` | 54 | ... / Objetivo de 100 canales de referencia superado (119). El descubrimiento usa 26 búsquedas en tgden.com y valida cada usuario con `t.me/s/`, filtrando por contexto cubano.»
- **Restated**: La base de Telegram consolidó 119 canales, 4 con contexto automotriz y 54 anuncios marcados como autos, superando el objetivo de 100 canales.
- **Internal/External evidence**: §29 (L984–991), §28 (L972).
- **Notes**: los JSONL originales se conservan como respaldo (L991).

### C051 — Git LFS 3.8.1 para SQLite
- **Section**, **Lines**: §30 Gestión de bases de datos con Git LFS (L995–1003), 997–999
- **Types**: methodological
- **Excerpt**: «Se instaló **Git LFS 3.8.1** y se activó en el repositorio. `.gitattributes` marca `*.sqlite`, `*.sqlite-wal` y `*.sqlite-shm` con `filter=lfs diff=lfs merge=lfs -text`; se retiraron las reglas de `.gitignore` que excluían `revolico.sqlite` y los SQLite de concesionarios.»
- **Restated**: Las bases SQLite pasaron a gestionarse con Git LFS 3.8.1, conservando el esquema de partes de Revolico como respaldo auditable.
- **Internal/External evidence**: §30 (L997–1001), §54 (L1347), §71.5 (L1543).
- **Notes**: L1001 advierte sobre el consumo de cuota LFS por blobs nuevos cada 10 minutos.

### C052 — Rango temporal de anuncios y limpieza sobre 9.957
- **Section**, **Lines**: §31 Rango temporal de anuncios Revolico (L1005–1011), 1007–1009
- **Types**: result, methodological
- **Excerpt**: «Se fijó el rango permitido de `updated_on_by_user` entre **2021-01-01 y la fecha actual** en `limpiar_revolico.py` (`FECHA_MINIMA`). Los anuncios fuera de rango van a `revision` con motivo `fuera de rango temporal`.»
- **Restated**: El rango permitido arranca el 01/01/2021; con el anuncio más antiguo del 17/12/2024 no hubo exclusiones por fecha y la limpieza conservó 548 de 9.957 anuncios.
- **Internal/External evidence**: §31 (L1007–1009), §15 (L795).
- **Notes**: —
### C053 — Línea base real de la primera ejecución del pipeline
- **Section**, **Lines**: §34 Esqueleto de análisis de rentabilidad (L1036–1082), 1065–1076
- **Types**: result
- **Excerpt**: «| Filas ingeridas | 972 (716 Revolico + 256 concesionarios) | ... | Filas limpias | 499 (497 usados, 2 nuevos) | ... | Marcas | 32 | ... | Precio mediano usado | 24.000 USD | ... | Antigüedad media | 5,9 años | ... | Observaciones del modelo OLS | 328 | ... | Grupos de benchmark | 21 | ...…»
- **Restated**: La primera ejecución ingirió 972 filas, conservó 499 limpias, reportó 32 marcas, mediana 24.000 USD y 5,9 años de antigüedad media.
- **Internal/External evidence**: §34 (L1063–1074 tabla), §34 (L1082 en inglés).
- **Notes**: L1076 atribuye a esa corrida la depreciación de −5,43 % anual (p<0,001) y primas de +21 %/−22 %.

### C054 — Brecha frente al repositorio egipcio
- **Section**, **Lines**: §34 (L1078–1080), 1080
- **Types**: result, contextual
- **Excerpt**: «Egipto tiene 23.500 anuncios, historial mensual de precios, HP y kilometraje estructurados, ANOVA/OLS/VIF, Tableau y Power BI. La predicción de precios sobre catálogos estructurados tiene antecedentes [14], [18], ausentes del contraste original. Nosotros tenemos el pipeline y las técnicas…»
- **Restated**: El texto declara una brecha de cobertura y frescura frente a Egyptian-Used-Cars y cita como antecedentes [14] y [18].
- **Internal/External evidence**: §34 (L1080), §71.1 (L1513: Egyptian-Used-Cars como referencia cualitativa), §71.14 (L1574 [14], L1578 [18]).
- **Notes**: es un contraste cualitativo sin métrica calculada sobre datos propios.

### C055 — Mecanismo de la app Circuitos Habana
- **Section**, **Lines**: §35 App de circuitos eléctricos de Apklis (L1086–1098), 1088–1093
- **Types**: result
- **Excerpt**: «Con **jadx 1.5.6** descompilé la primera y encontré el mecanismo que buscábamos: - La app **no usa una API privada**: hace scraping del canal público de Telegram `https://t.me/s/EmpresaElectricaDeLaHabana` con Jsoup y User-Agent de Chrome. - Paginación con `?before=<message_id>`, hasta 16…»
- **Restated**: La app descompilada scrapea el canal público de Telegram con Jsoup, pagina con `?before=` y convierte timestamps UTC a hora de Cuba con +1 h de horario de verano.
- **Internal/External evidence**: §35 (L1088–1096), §62 (L1427).
- **Notes**: evidencia y APKs en `Data/apklis/` (L1096).

### C056 — Mapa offline, coordenadas e infraestructura EV
- **Section**, **Lines**: §36 Mapa offline, talleres e infraestructura EV (L1102–1112), 1104–1108
- **Types**: result
- **Excerpt**: «Se extrajeron coordenadas de los **mapas incrustados en las propias webs** de los concesionarios (BDC One: 23.1155203,-82.3596368 y 23.0992805,-82.3050631; Dongfeng: 23.1250339,-82.4227564) y se geocodificó una dirección adicional con Nominatim.»
- **Restated**: Ante la imposibilidad de usar Docker y la ausencia de datos OSM útiles, se extrajeron coordenadas de los mapas incrustados en webs de concesionarios y se documentaron fuentes de infraestructura EV.
- **Internal/External evidence**: §36 (L1104–1108), §41 (L1175), §42 (L1197).
- **Notes**: L1108 registra Dongfeng/NWI 11 estaciones solares (2026) y CIMEX+MITRANS 21 estaciones (2025), con detalle en `Data/mapas/infraestructura_ev_cuba.md`.

### C057 — Optimización de pipelines y efecto medido
- **Section**, **Lines**: §37 Optimización de pipelines (L1116–1126), 1120–1122
- **Types**: result, methodological
- **Excerpt**: «**Efecto medido:** en minutos, los anuncios de Revolico pasaron de 10.117 a **10.149** y los autos de 716 a **814**; quedan 3.351 URLs pendientes y 1.940 rechazadas. Los marketplaces ya completaron Cubisima, Apululu, Carros.com, Autocubana y VentaCuba y siguen con iTENCEL/Timbirichi.»
- **Restated**: La optimización elevó los anuncios de 10.117 a 10.149 y los autos de 716 a 814, con 3.351 URLs pendientes.
- **Internal/External evidence**: §37 (L1120–1122), §39 (L1147–1148), §66 (L1461).
- **Notes**: L1120 atribuye la mejora a sesiones curl_cffi por hilo y al paso de 8/4 a 20/8 descargadores/procesadores.

### C058 — Ampliación de límites de marketplaces
- **Section**, **Lines**: §39 Continuación del scrapeo y presentación narrativa (L1145–1152), 1147
- **Types**: result
- **Excerpt**: «Se ampliaron los límites de `scrape_marketplaces.py`: Cogetucarro de 200 → **5.008**, Autocubana y Timbirichi a 40 páginas. El servicio `marketplaces-scrape.service` se relanzó con 6 workers; en minutos Autocubana pasó de 400 a **566** y Timbirichi de 110 a **170**, totalizando **2.121 anuncios**.»
- **Restated**: Los límites de captura se ampliaron y, en minutos, Autocubana pasó de 400 a 566 y Timbirichi de 110 a 170 anuncios.
- **Internal/External evidence**: §39 (L1147), §9 (L105–117).
- **Notes**: L1148 registra además reintento explícito ante `database is locked` (`_retry_exec`).

### C059 — Gasolineras, cargadores y serie de precios del combustible
- **Section**, **Lines**: §41 Gasolineras, estaciones de carga y serie de precios del combustible (L1171–1182), 1174–1177
- **Types**: result
- **Excerpt**: «**Overpass/OSM devolvió 137 gasolineras en La Habana** con coordenadas, marca, dirección y tipos de combustible. ... Se crearon `Data/mapas/gasolineras.csv` (137) y `Data/mapas/estaciones_carga.csv` (12), y se regeneró `mapa_ofline.html` con tres capas: concesionarios (3), carga eléctrica…»
- **Restated**: Overpass/OSM devolvió 137 gasolineras y se creó una base con 18 observaciones de precios de combustible entre el 20/08/2026 y el 18/11/2026.
- **Internal/External evidence**: §41 (L1174–1178), §42 (L1197: 131 gasolineras en la base unificada).
- **Notes**: Kargalaya aportó 9 estaciones con coordenadas, Electromaps 3 sin coordenadas y ChargeFinder respondió 403 (L1175).

### C060 — Marco normativo del combustible en el storytelling
- **Section**, **Lines**: §43 Apartado de “cuánto costaría moverse” (L1205–1217), 1209–1215
- **Types**: result, contextual
- **Excerpt**: «**7/02/2026:** CIMEX anunció medidas temporales —respaldadas por el MEP y el viceministro Oscar Pérez-Oliva Fraga— que suspendieron la venta en CUP y activaron **Ticket** (20 L por turno, 24 h para usarlo). No se localizó una resolución numerada nueva en la Gaceta Oficial; fue una disposición…»
- **Restated**: El bloque de “cuánto costaría moverse” fecha el Acuerdo 9811 de 2024, las medidas de CIMEX del 07/02/2026, la autorización de importación del 15/02/2026 y la liberalización de precios del 15/05/2026.
- **Internal/External evidence**: §43 (L1209–1215: Cubadebate, Directorio Cubano, CubaTrámite y D-Cuba), §41 (L1180).
- **Notes**: el 15/05/2026 cada importador habilitado fija su precio según costo real de importación (1,80–2,60 USD/L, L1212).

### C061 — Base unificada del mapa con 131/12/25/22 elementos
- **Section**, **Lines**: §42 Base unificada del mapa y talleres (L1186–1201), 1197
- **Types**: result
- **Excerpt**: «Estado final: **131 gasolineras, 12 estaciones de carga, 25 concesionarios (17 con coords) y 22 talleres (todos con coords)**. Los 8 concesionarios sin coords se exportan a `elementos_sin_coordenadas.csv`.»
- **Restated**: La base unificada del mapa contiene 131 gasolineras, 12 estaciones de carga, 25 concesionarios y 22 talleres, con 8 concesionarios sin coordenadas.
- **Internal/External evidence**: §42 (L1188–1199), §41 (L1176).
- **Notes**: L1199 registra el uso de patchright y FlareSolverr tras un 403 de Cybo con curl_cffi.

### C062 — Cifras de la corrida del 18/11 conservadas en el storytelling
- **Section**, **Lines**: §45 Reescritura de la sección 3 del storytelling (L1232–1236), 1234
- **Types**: result
- **Excerpt**: «Se transformó la sección **Lo que encontramos** de una tabla de datos en una narrativa de hallazgos (cifras de la corrida del 18/11/2026, posteriores a las que se recogen en §59): la proporción de anuncios que resisten el filtro de auto real, la mediana de 23.000 USD, la antigüedad media de…»
- **Restated**: El storytelling conserva cifras de la corrida del 18/11/2026 —23.000 USD, 6,3 años, 34 marcas, −5,43 %, 27 grupos y 30 oportunidades— posteriores a las de §59.
- **Internal/External evidence**: §45 (L1234), §59 (L1399–1401), §34 (L1069–1076).
- **Notes**: la depreciación de −5,43 % aparece aquí sin la salvedad que sí se registra en §44 (L1226).

### C063 — Definición de marcas premium y no premium
- **Section**, **Lines**: §48 Definición de marcas premium y no premium (L1256–1265), 1260–1263
- **Types**: definitional
- **Excerpt**: «**Premium:** Mercedes-Benz, BMW, Audi, Lexus, Volvo, Porsche, Land Rover, Jaguar, Cadillac, Infiniti y Acura. - **No premium:** Hyundai, Kia, Toyota, Lada, Fiat, Chevrolet, Peugeot, Honda, Nissan, MG, Dongfeng, Moskvich, Volkswagen, Mitsubishi, Geely, Ford, Jeep, Foton, GMC, SEAT, Renault,…»
- **Restated**: El documento fija una segmentación de dos grupos de marcas para la narrativa, mientras el modelo econométrico conserva tres niveles.
- **Internal/External evidence**: §48 (L1260–1263), §1 (L21: tres tiers de marca), §71.3 (L1528: premium−económico).
- **Notes**: la lista completa con evidencia y conteos se remite a `Data/analisis_rentabilidad/marcas_cuba.md` (L1263).

### C064 — Treinta y seis repositorios cubanos de automoción
- **Section**, **Lines**: §49 Búsqueda de repositorios cubanos de automoción (L1269–1277), 1271
- **Types**: result
- **Excerpt**: «Se buscaron repositorios en GitHub con la API (`gh api search/repositories`) usando 31 consultas en español e inglés: mercado automotriz cubano, carros/autos/vehículos en Cuba, Revolico, motos/triciclos, precios y divisas. Tras deduplicar se obtuvieron **648 repos**, de los que se depuraron…»
- **Restated**: Treinta y y una consultas a la API de GitHub produjeron 648 repositorios únicos, de los que 36 se depuraron como relacionados.
- **Internal/External evidence**: §49 (L1271–1275), §55 (L1359).
- **Notes**: la lista se remite a `Data/github-repos-automotriz-cuba-2026-11-19.md` (L1273).

### C065 — Consolidación de 25 tablas de repositorios de referencia
- **Section**, **Lines**: §50 Consolidación de bases de los repositorios de autos (L1281–1291), 1285–1289
- **Types**: result
- **Excerpt**: «Se creó `Data/repos-autos-referencias/referencias_autos.sqlite` con **25 tablas** (3.958 anuncios de Revolico, 3.566 limpios, catálogos de comercializadoras, 33 respuestas de encuesta, 30 + 30 + 8 entrevistas, datasets de AutosxCuba) y una tabla `provenancia`. De los 3.958 anuncios, **369…»
- **Restated**: La consolidación produjo 25 tablas con 3.958 anuncios, de los que 369 ya estaban en la base propia y 3.589 son nuevos.
- **Internal/External evidence**: §50 (L1283–1289), §71.15 (L1553: 33 respuestas).
- **Notes**: L1285 registra 12 grupos de duplicados bytes y 11 por contenido entre 233 archivos y 76 CSV.

### C066 — Encuesta de 33 respuestas y entrevistas cualitativas
- **Section**, **Lines**: §50 (L1289)
- **Types**: result
- **Excerpt**: «la encuesta con datos reales fue un Google Forms de 32 preguntas aplicado a 33 personas de 4 segmentos en un barrio de La Habana (17 de 18–25 prefieren eléctrico, pero 16 de 18 no pagarían más de 4.000 USD por uno); los otros dos cuestionarios son solo instrumentos sin respuestas. Las…»
- **Restated**: La documentación de encuestas reporta una encuesta con 33 respuestas y 68 entrevistas cualitativas, con un grupo que incluye nombres.
- **Internal/External evidence**: §50 (L1289), §51 (L1305: 28 interesados tras reconciliar), §71.15 (L1553).
- **Notes**: el cruce posterior filtra `interes=1` y da 28 interesados (L1305).

### C067 — Deduplicación de `autos` a 744 únicos
- **Section**, **Lines**: §51 Mejoras del proyecto (L1295–1307), 1299
- **Types**: result
- **Excerpt**: «La tabla se reconstruyó desde `anuncios` (fuente canónica): 814 filas con 748 IDs únicos → **744 autos únicos**. Se excluyeron 4 anuncios que no son autos (`58867937`, `53777554`, `53843413`, `58886962`), marcados en `anuncios` con `es_auto=0` y motivo `no es auto: servicio/combustible`.»
- **Restated**: La deduplicación redujo 814 filas con 748 IDs únicos a 744 autos únicos tras excluir cuatro anuncios reclasificados.
- **Internal/External evidence**: §51 (L1299–1300), §59 (L1399: 974 autos únicos en la corrida vigente).
- **Notes**: se creó el índice único `idx_autos_id` y se incorporaron `EXCLUDE_IDS` e `INSERT OR REPLACE` en `limpiar_revolico.py` (L1299).

### C068 — Reparación de precios y separación por canal en marketplaces
- **Section**, **Lines**: §51 (L1301)
- **Types**: result, methodological
- **Excerpt**: «`parse_price` ahora interpreta separadores de miles (973 anuncios recuperados: 872 de iTENCEL, 99 de Cubisima, 2 de VentaCuba). Los precios vacíos de Autocubana se recuperan del JSON-LD (614 anuncios, mediana 17.000 USD) ... Se incorporó la columna `canal`: **1.301 anuncios locales y 672 de…»
- **Restated**: La reparación recuperó 973 precios y 614 de Autocubana, separó 1.301 anuncios locales de 672 de importación y fijó la mediana local en 21.000 USD.
- **Internal/External evidence**: §51 (L1301), §58 (L1391: 1.323 locales y 691 de importación), §59 (L1399: 1.483 locales y 691 de importación).
- **Notes**: L1301 también registra 116 casos de precios que en realidad son modelo/año en Cogetucarro y 11 marcadores de precio en VentaCuba.

### C069 — Corrección del parseo de kilometraje y ampliación de marcas
- **Section**, **Lines**: §51 (L1302–1303)
- **Types**: result
- **Excerpt**: «`parse_specs` y `parse_title` convertían `80,000 km` en 80 km. Se extrajo `parse_number()` con la lógica de separadores ya usada en `parse_price`. El código está aplicado y probado (`80,000` → 80.000); la regeneración final de los outputs se registra al cierre de la tanda.»
- **Restated**: El parseo de kilometraje corrige los separadores de miles y `config.py` incorpora catorce marcas adicionales con sus alias y tiers.
- **Internal/External evidence**: §51 (L1302–1303), §59 (L1399: mediana de kilometraje 32.569 km).
- **Notes**: el objetivo declarado era reducir los 442 anuncios en tier «desconocido» (L1303).

### C070 — Veinticinco fuentes adicionales y derogación de la Resolución 312/2026
- **Section**, **Lines**: §52 Ampliación de fuentes de datos (L1311–1327), 1313–1323
- **Types**: result, methodological
- **Excerpt**: «El resultado está en `Data/fuentes-adicionales-2026-11-20.md`: **25 fuentes** verificadas, organizadas por tipo con URL, datos expuestos, viabilidad de scraping y aporte al proyecto.»
- **Restated**: La ampliación verificó 25 fuentes y registró que la Resolución 312/2026 fue derogada por la 340/2026, actualizando las referencias.
- **Internal/External evidence**: §52 (L1313–1325), §10 (L126), §4 (L67).
- **Notes**: las cinco fuentes más valiosas se enumeran en L1317–L1321, con la API del BCC como referencia oficial frente a la TRMI informal (L1317).

### C071 — Descarga completa de los anuarios del ONEI
- **Section**, **Lines**: §53 Descarga completa de los anuarios del ONEI (L1331–1339), 1333
- **Types**: result
- **Excerpt**: «A partir del índice oficial `http://www.onei.gob.cu/cuba` se recorrieron las 12 páginas de anuarios disponibles (2014–2025) y se descargaron **todos los documentos enlazados**: 111 PDF, 7 RAR y 103 archivos Excel extraídos, unos 311 MB en total.»
- **Restated**: Se descargaron todos los documentos enlazados de los 12 anuarios del ONEI 2014–2025: 111 PDF, 7 RAR y 103 Excel, unos 311 MB.
- **Internal/External evidence**: §53 (L1333–1337), §56 (L1371).
- **Notes**: L1335 registra 117 enlaces de documento descargados, 0 archivos sospechosos por MIME y conservación sin modificar de los RAR.

### C072 — Base de Revolico distribuida en 82 fragmentos
- **Section**, **Lines**: §54 Base de datos distribuida en chunks (L1343–1351), 1345
- **Types**: result, methodological
- **Excerpt**: «`Data/Revolico/revolico.sqlite` (849.465.344 bytes) se dividió en **82 chunks de 10 MB** en `Data/Revolico/chunks/`, con un `MANIFEST.json` que guarda el SHA-256 del archivo completo, el orden, el offset y el hash de cada fragmento. La verificación de los 82 chunks dio OK.»
- **Restated**: La base de 849.465.344 bytes se dividió en 82 fragmentos de 10 MB con manifiesto SHA-256 y verificación OK.
- **Internal/External evidence**: §54 (L1345–1349), §71.5 (L1543: reconstruible desde `chunks/MANIFEST.json`).
- **Notes**: los fragmentos se publican en la rama huérfana `chunked-db` para no arrastrar el objeto LFS de 804 MB en `main` (L1349).

### C073 — Auditoría de 15 fuentes web y hallazgo de código
- **Section**, **Lines**: §55 Auditoría de fuentes, README y verificación final (L1355–1365), 1357–1363
- **Types**: result
- **Excerpt**: «Se consultaron **15 fuentes web** (8 marketplaces, 7 fuentes oficiales y complementarias): 14 respondieron HTTP 200 y elTOQUE no respondió desde este entorno. Las fechas más recientes en las bases son 17–18/11/2026.»
- **Restated**: La auditoría consultó 15 fuentes, 14 respondieron HTTP 200 y elTOQUE no respondió; la verificación del código detectó y corrigió un `NameError` en `01_ingest.py`.
- **Internal/External evidence**: §55 (L1357–1363), §57 (L1381).
- **Notes**: L1359 registra 33 repositorios auxiliares, 7 cubanos, uno con ref remota atrasada 24 commits y todos con cambios locales sin commitear.

### C074 — Análisis de los anuarios: series útiles y laguna sin resolver
- **Section**, **Lines**: §56 Análisis de los anuarios y estructura de GitHub (L1369–1375), 1371
- **Types**: result
- **Excerpt**: «el transporte de pasajeros cayó un 59 % entre 2019 y 2025 y el ómnibus un 71 %; los accidentes bajaron pero la gravedad aumentó (9,9 fallecidos por cada 100 accidentes en 2025). **No hay series de parque automotor ni de matriculaciones**, por lo que esa laguna signalada en `NECESIDADES.md`…»
- **Restated**: Los anuarios permiten extraer series de transporte y accidentalidad, pero no contienen series de parque automotor ni de matriculaciones.
- **Internal/External evidence**: §56 (L1371), §37 (L895: laguna declarada), §53 (L1337).
- **Notes**: la serie útil se remite a `Data/fuentes-oficiales/ONEI/series_oficiales.csv` y su lectura a `ANALISIS_DATO.md` (L1371).

### C075 — Estructura versionada del repositorio
- **Section**, **Lines**: §56 (L1373)
- **Types**: result
- **Excerpt**: «Se documentó además la estructura versionada en `Data/estructura_github.md`: 1.288 archivos, 157 objetos LFS, distribuidos en `Data` (836), `Hombros` (280), `Auxiliares` (110) y `Anexos` (56), con el detalle de extensiones por carpeta y la lista de repositorios no versionados.»
- **Restated**: El repositorio versiona 1.288 archivos y 157 objetos LFS, distribuidos entre cuatro carpetas con los recuentos declarados.
- **Internal/External evidence**: §56 (L1373), §68 (L1479).
- **Notes**: —
### C076 — Reclasificación de páginas y diez anuncios nuevos en iTENCEL
- **Section**, **Lines**: §57 Reclassificación de páginas y novedades detectadas (L1379–1383), 1381; §58 (L1389–1391)
- **Types**: result
- **Excerpt**: «Resultado: 7 fuentes sin enlaces nuevos; **iTENCEL mostró 10 anuncios nuevos** (`gmc-sierra-2022-add`, `honda-acord-2025-add`, entre otros), tras descartar una página de agrupación falsa.»
- **Restated**: La comparación de enlaces normalizados encontró 7 fuentes sin novedades y 10 anuncios nuevos en iTENCEL, que luego se scrapearon e insertaron.
- **Internal/External evidence**: §57 (L1381), §58 (L1389–1391: 951→961 anuncios, `integrity_check=ok`).
- **Notes**: la normalización incluyó `www.`, query, Unicode NFC y barras finales (L1381).

### C077 — Inventario de transformaciones y estimaciones
- **Section**, **Lines**: §60 Inventario de funciones y modelos (L1407–1411), 1409
- **Types**: methodological, result
- **Excerpt**: «El respaldo es metodológico y empírico: se explica por qué cada forma encaja con datos asimétricos y por qué la corrida actual **no** sostiene una tasa de depreciación ni una prima premium significativa (p mínimo <!-- kpi:modelo_p_min -->0,0941; VIF <!-- kpi:vif_min -->1,12–<!-- kpi:vif_max…»
- **Restated**: El inventario declara p mínimo 0,0941, VIF 1,12–1,40 y Kruskal-Wallis p = 0,00000 para la corrida vigente.
- **Internal/External evidence**: §60 (L1409), §59 (L1401), §71.3 (L1528).
- **Notes**: las tres cifras van en marcadores `<!-- kpi:... -->` del texto cacheado.

### C078 — Sitio MkDocs con compilación estricta
- **Section**, **Lines**: §61 Sitio MkDocs del proyecto (L1415–1421), 1417–1419
- **Types**: result, methodological
- **Excerpt**: «El panel interactivo vigente es `Data/dashboard.html`, copiado a `docs/dashboard.html`; los seis gráficos Plotly se copian a `docs/graficos/` y se enlazan desde el apéndice; las tablas del apéndice y la página de KPIs se generan desde los CSV. `mkdocs build --strict` termina sin errores ni…»
- **Restated**: El sitio MkDocs Material se genera desde Markdown y CSV, incluye el panel y seis gráficos, y compila con `--strict` sin errores ni enlaces rotos.
- **Internal/External evidence**: §61 (L1417–1419), §71.5 (L1543: ruta del panel).
- **Notes**: la navegación sigue Diátaxis con cuatro secciones (L1417).

### C079 — Factibilidad del timelapse de circuitos eléctricos
- **Section**, **Lines**: §62 Factibilidad del timelapse eléctrico (L1425–1429), 1427
- **Types**: result
- **Excerpt**: «Del APK se extrajeron 2.473 puntos, 244 circuitos y 166 polígonos de zonas a `Data/mapas/circuitos/`. El plan de captura, parseo, mapa temporal y límites está en `Data/mapas/TIMELAPSE_CIRCUITOS.md`. Se implementó además `Auxiliares/herramientas/scraper_circuitos.py`: en su primera corrida…»
- **Restated**: El canal público responde HTTP 200 con mensajes del 23/11/2026 y la primera corrida del capturador produjo 35 circuitos sin luz, 23 mixtos y 2 con luz.
- **Internal/External evidence**: §62 (L1427), §35 (L1088–1096).
- **Notes**: un informe de debug corrigió tres fallos —fecha local, filtro de relevancia y palabras de afectación— sin borrar filas (L1427).

### C080 — Estimación de retención declarada como inferencia
- **Section**, **Lines**: §63 Calidad del storytelling como puerta de entrada (L1433–1439), 1435–1437
- **Types**: result, methodological
- **Excerpt**: «La estimación de retención (`Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md`) es **inferencia de diseño, no medición**: de cada 100 visitantes, ~58 leerían el primer párrafo, ~16 llegarían al cierre y ~5 volverían con intención de consulta. Con promesa, CTA y artefacto actualizable, la…»
- **Restated**: La retención estimada es una inferencia de diseño no medida, con 58/16/5 de cada 100 visitantes y una proyección condicionada de 22–25 finalizaciones y 18–22 retornos.
- **Internal/External evidence**: §63 (L1437).
- **Notes**: la propia línea distingue explícitamente inferencia de medición.

### C081 — Cinco timers operativos y coste de red estimado
- **Section**, **Lines**: §65 Automatización operativa y coste de red (L1451–1455), 1453
- **Types**: result, methodological
- **Excerpt**: «Estimación de red: **5–10 MB/mes** si no hay cambios y **50–90 MB/mes** con novedades. Sin internet no se puede scrapear, pero sí ejecutar sin presencia del usuario; si falla la red, `SALUD.md` marca el periodo perdido y el siguiente ciclo `Persistent=true` lo recupera.»
- **Restated**: Se activaron cinco timers `precio-*` con `Linger=yes`, bloqueo `flock`, validación con cuarentena y `SALUD.md`, con un coste de red estimado de 5–10 o 50–90 MB/mes.
- **Internal/External evidence**: §65 (L1453), §64 (L1445).
- **Notes**: el mismo renglón registra dos fallos latentes corregidos: `salud.py` distinguía mal `SIN DATOS` de `STALE` y el ETag se escribía antes del `commit`.

### C082 — Captura continua de Revolico y arquitectura de datos
- **Section**, **Lines**: §66 Extracción continua de Revolico y arquitectura de datos (L1459–1465), 1461–1463
- **Types**: result, methodological
- **Excerpt**: «Se activó `precio-revolico.timer` cada 10 minutos con `--max-pages 3`, 2 descargadores, 2 procesadores y lotes de 50, sin `git push`. ... En la primera corrida corregida los anuncios `done` pasaron de 6.783 a 6.955.»
- **Restated**: El timer de Revolico corre cada 10 minutos con 2 descargadores, 2 procesadores y lotes de 50; tras corregir los enlaces `pending` irreversibles, los anuncios `done` pasaron de 6.783 a 6.955.
- **Internal/External evidence**: §66 (L1461–1463), §37 (L1122), §39 (L1148).
- **Notes**: L1463 documenta Parquet particionado por `year/month`, watermark y rollups mensuales, con DuckDB bloqueado por `SIGILL`.

### C083 — Optimización de espacio y peso en GitHub
- **Section**, **Lines**: §67 Optimización de espacio (L1469–1473), 1471; §68 (L1477–1479), 1479
- **Types**: result
- **Excerpt**: «El repositorio pasó de 20 GB a 10 GB. ... La API de GitHub reporta **205.002 KB (0,20 GB)** para el historial normal; los archivos grandes se guardan aparte y su consumo en GitHub no lo expone la API. En local, esa copia ocupa 3,3 GB con 174 archivos.»
- **Restated**: La limpieza redujo el repositorio de 20 GB a 10 GB, y la API de GitHub reporta 205.002 KB para el historial normal frente a 3,3 GB locales de objetos LFS.
- **Internal/External evidence**: §67 (L1471), §68 (L1479), §56 (L1373).
- **Notes**: leyes y herramientas de scraping se movieron a `~/Utilidades/Leyes` y `~/Utilidades/HerramientasScraping` sin borrarse (L1471).

### C084 — Bases de comparación y sus métricas observadas
- **Section**, **Lines**: §71.1 Bases de comparación / Baselines (L1507–1518), 1511–1516
- **Types**: result, methodological
- **Excerpt**: «| Mediana global ( ingenua ) | Predice la mediana de los usados locales | MAE <!-- kpi:mae_mediana_global -->18.188,34 USD sobre <!-- kpi:n_mediana_global -->1.462 anuncios | ... | Modelo principal propio | OLS de log-precio con antigüedad, km, condición y tier | R² 0,101 sobre 584 observaciones |»
- **Restated**: La mediana global ingenua tiene MAE 18.188,34 USD y la mediana por marca 16.603,28 USD, ambas sobre 1.462 anuncios; el modelo principal reporta R² 0,101 sobre 584 observaciones.
- **Internal/External evidence**: §71.1 (L1511–1518), §71.2 (L1522), §71.3 (L1528).
- **Notes**: las bases llevan MAE sin intervalo asociado; el único IC del documento está en §71.3 (L1528).

### C085 — Diseño independiente y tamaño muestral en anuncios
- **Section**, **Lines**: §71.3 (L1528–1530), 1528
- **Types**: methodological
- **Excerpt**: «No hay diseño pareado: los anuncios son observaciones independientes, por lo que no se aplican Wilcoxon de pares ni t de diferencias; se usan Kruskal-Wallis y Welch para grupos independientes. El tamaño se mide en anuncios (981 candidatas de 8 marketplaces), no en ensayos experimentales.»
- **Restated**: El diseño es independiente, sin pruebas pareadas, y el tamaño se mide en 981 candidatas de 8 marketplaces.
- **Internal/External evidence**: §71.3 (L1528), §71.2 (L1522).
- **Notes**: el par inglés (L1530) declara que falta una línea base SOTA operacionalizada.

### C086 — Amenazas a la validez declaradas
- **Section**, **Lines**: §71.4 Amenazas a la validez / Threats to validity (L1532–1539), 1534–1537
- **Types**: contextual, methodological
- **Excerpt**: «- **Externa:** solo La Habana y anuncios en línea; los precios son pedidos, no transaccionados. - **De constructo:** kilometraje y potencia faltan en la mayoría de los anuncios; la condición se infiere del texto. - **Interna:** no hay asignación aleatoria; la ablación es observacional.…»
- **Restated**: El documento declara amenazas externa, de constructo, interna y estadística, incluida la no significancia de los coeficientes del modelo completo.
- **Internal/External evidence**: §71.4 (L1534–1537), §59 (L1401), §71.2 (L1522), §22 (L914).
- **Notes**: sección incorporada en la iteración 3 y conservada en esta pasada.

### C087 — Comando único, puntos de entrada y prueba de humo
- **Section**, **Lines**: §71.5 (L1543)
- **Types**: methodological
- **Excerpt**: «Comando único: `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py`. Puntos de entrada con argumentos: `generar_dashboard.py --solo-si-cambia`, `exportar_parquet_compacto.py --tablas ...`, `db_chunks.py split|verify|assemble` y `generar_sitio_mkdocs.py`. Las…»
- **Restated**: La sección declara un comando único, cuatro puntos de entrada con argumentos, dependencias fijadas a serie menor y una prueba de humo.
- **Internal/External evidence**: §71.5 (L1543), §55 (L1361: `requirements.txt` y `.venv-py`).
- **Notes**: la disponibilidad pública se declara en la misma línea con la URL del repositorio y la ausencia de licencia (C008).

## Contextual claims (38)

### C088 — Nombres anteriores conservados por trazabilidad
- **Section**, **Lines**: §1 Objetivo (L27), 27
- **Types**: contextual
- **Excerpt**: «Se conservan los nombres anteriores, *AutoDecide Habana* e *ICD Automotive Market Project*, para mantener la trazabilidad de la documentación ya producida.»

### C089 — Nota de actualización sobre fases y resultados vigentes
- **Section**, **Lines**: §2 Estado y fases (L47), 47
- **Types**: contextual
- **Excerpt**: «**Nota de actualización (27/11/2026):** esta tabla registra el estado al 17/11/2026. El pipeline de análisis (fase 8) se creó después, el 18/11/2026 (§34), y sus resultados vigentes se documentan en §59–§60.»

### C090 — Decisiones de diseño de carpetas y clones
- **Section**, **Lines**: §3 Organización de carpetas (L63), 63
- **Types**: contextual, methodological
- **Excerpt**: «Decisiones de diseño: todo el material auxiliar vive dentro de `Auxiliares/`; los clones se hicieron con `--depth 1` y se registraron en `~/Utilidades/HerramientasScraping/_clone_log.tsv`; la descubrimiento se separó de la verificación; `Copias/` no se registra en este informe por decisión…»
### C091 — Índice de gacetas como referencia
- **Section**, **Lines**: §10 Marco legal (L129), 129
- **Types**: contextual
- **Excerpt**: «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe, solo se citan las normas anteriores.»

### C092 — Problemas y soluciones de la captura
- **Section**, **Lines**: §11 Problemas y soluciones (L135–140), 135–140
- **Types**: contextual, methodological
- **Excerpt**: «| CAPTCHA en paginación DDG | Yahoo + visitas directas; después sesión con `vqd`. | ... | Repetidos y mirrors | Deduplicación por título normalizado, prefijo y dominio. |»

### C093 — Registro automático de altas y exclusión de `Copias/`
- **Section**, **Lines**: §13 Registro de altas / Change log (L294–298), 296
- **Types**: contextual
- **Excerpt**: «Registro automático de todo lo que se añade a la carpeta del proyecto. El script `Auxiliares/herramientas/actualizar_informe.py` añade filas debajo del marcador y regenera el PDF. `Copias/` queda excluido por decisión explícita.»

### C094 — Entradas omitidas en el registro de altas
- **Section**, **Lines**: §13 (L315), 315
- **Types**: contextual
- **Excerpt**: «| 2026-11-17 | … | aviso / notice | — | — | — | 175 entradas adicionales no listadas / omitted | Pendiente / Pending |»

### C095 — Última ejecución registrada de sincronización
- **Section**, **Lines**: §14 (L783), 783
- **Types**: contextual
- **Excerpt**: «| 2026-11-17T15:47:42+00:00 | 795373568 B | 48 partes de 16 MiB | `dadd2bffba615d8a…` | Reconstruir con `reconstruir_revolico.py` / Rebuild with `reconstruir_revolico.py` |»

### C096 — Detención manual del temporizador de Revolico
- **Section**, **Lines**: §15 (L791), 791
- **Types**: contextual
- **Excerpt**: «**Nota / Note (17/11/2026):** se detuvo manualmente `revolico-scrape.timer` y su servicio a petición del usuario. El scraper había ampliado la BD de 3.682 a **6.332 anuncios** (520,6 MB) antes de detenerse; no se generaron partes (`estado.json` ausente) porque se detuvo antes de la fase de división.»

### C097 — Adaptación del patrón de diferencias de `spinny-scraper`
- **Section**, **Lines**: §16 (L805), 805
- **Types**: contextual, methodological
- **Excerpt**: «Se adaptó el patrón `output_writer.py` + `diff_runs.py` de `spinny-scraper` como snapshot `Data/Revolico/snapshots/ultimo.json` (`{id: firma}`).»

### C098 — Fuentes académicas y repositorios revisados para fases 7–8
- **Section**, **Lines**: §17 (L813), 813
- **Types**: contextual
- **Excerpt**: «Fuentes académicas y repositorios revisados para definir los requerimientos del análisis (Fases 7-8):»

### C099 — Verificación en vivo y accesibilidad de fuentes oficiales
- **Section**, **Lines**: §18 (L838–840), 838–840
- **Types**: contextual, citation-grounded
- **Excerpt**: «VAHAN (India), declarado por `vahan-india-automotive-market-2025` | **Oficial gubernamental** (MoRTH) | No accesible desde este entorno (error de transporte); el repo documenta 12 exportaciones mensuales 2025 y manifiesto de verificacion | Registros por fabricante/combustible»

### C100 — Marco general de ocho pasos derivado de trabajos revisados
- **Section**, **Lines**: §19 Marco general (L857–866), 857
- **Types**: contextual
- **Excerpt**: «### Marco general (8 pasos, derivado de los trabajos revisados)»

### C101 — Límites declarados de la adaptación
- **Section**, **Lines**: §19 (L875), 875
- **Types**: contextual
- **Excerpt**: «- **Límites**: precios pedidos no transaccionados, sesgo de supervivencia de anuncios, sin datos personales, vigencia normativa a verificar.»

### C102 — Cambio de objetivo a petición del usuario
- **Section**, **Lines**: §21 (L901), 901
- **Types**: contextual
- **Excerpt**: «A petición del usuario, el objetivo inmediato deja de ser la recomendación interactiva de compra y pasa a ser **un análisis de mercado**.»

### C103 — Generación de gráficas del análisis descriptivo
- **Section**, **Lines**: §23 (L925), 925
- **Types**: contextual
- **Excerpt**: «**Gráficas**: `Auxiliares/herramientas/graficos_mercado.py` usa matplotlib, seaborn y plotly (instalados) y genera 8 PNG + `dashboard_interactivo.html` en `Data/analisis/graficos/`.»

### C104 — Librerías de mapas instaladas
- **Section**, **Lines**: §25 (L939), 939
- **Types**: contextual
- **Excerpt**: «**Librerías de mapas instaladas:** `geopandas 1.2.0`, `shapely 2.2.0`, `pyproj`, `folium 1.0.0`, `mapclassify`, `geopy` (además de matplotlib/seaborn/plotly ya instaladas).»

### C105 — Búsqueda de canales adicionales de Telegram
- **Section**, **Lines**: §28 (L974), 974
- **Types**: contextual
- **Excerpt**: «**Búsqueda de más canales:** se probaron `Revolico_Cuba_Oficial`, `Ventas_Revolico_Holguin_Cuba`, `revolico_baracoa`, `timbirichi_compra_y_venta_cuba`, `PiezasdeCarrosCU`, `directoriocubano`, `eltoquecom`, `coventcuba`, `APublished`, `GEEKSCUBANS_PLUS` y `lachopivaraderooo`. Ninguno publicó…»
### C106 — Advertencia sobre la cuota de Git LFS
- **Section**, **Lines**: §30 (L1001), 1001
- **Types**: contextual
- **Excerpt**: «**Advertencia:** la cuota LFS del plan gratuito es limitada; una BD que cambia cada 10 minutos genera un blob nuevo por commit. Vigilar el consumo con `git lfs ls-files` y `git lfs env`.»

### C107 — Modo de descubrimiento sin procesamiento
- **Section**, **Lines**: §32 (L1015–1020), 1015–1020
- **Types**: contextual, methodological
- **Excerpt**: «Se añadió `--solo-descubrimiento` a `scrape_revolico_pipeline.py`. En ese modo: - se recorren las páginas de búsqueda desde la 1 hacia atrás; - se guardan todos los enlaces en `url_queue` con estado `descubierto`; - **no hay descarga de anuncios, ni clasificación definitiva, ni inserción en…»
### C108 — Parada por página sin enlaces nuevos
- **Section**, **Lines**: §33 (L1028), 1028
- **Types**: contextual, methodological
- **Excerpt**: «Se modificó `descubrir_hasta_fecha()` para que se detenga en cuanto una página no aporte **ningún enlace nuevo** (todos sus anuncios ya fueron vistos), además de las condiciones de fecha mínima, fin de páginas y límite de seguridad.»

### C109 — DuckDB desinstalado por fallo de CPU
- **Section**, **Lines**: §34 (L1059), 1059
- **Types**: contextual
- **Excerpt**: «`duckdb` se desinstaló porque produce `Illegal instruction` en esta CPU; se usa Parquet + Pandas en su lugar.»

### C110 — Descarga y descompilación de tres APKs de Apklis
- **Section**, **Lines**: §35 (L1088), 1088
- **Types**: contextual
- **Excerpt**: «Descargué tres APKs desde la API de Apklis (`api.apklis.cu/v2/application/` + `POST /v2/release/get_url/`): **Circuitos Habana** (`com.ermetic.circuitoshabana`, v2.2), **Apagones Habana** y **Donde Hay Luz Habana**. Con **jadx 1.5.6** descompilé la primera y encontré el mecanismo que buscábamos:»

### C111 — Restricciones de Docker y Overpass
- **Section**, **Lines**: §36 (L1104–1105), 1104–1105
- **Types**: contextual
- **Excerpt**: «Se intentó usar `google-maps-scraper` en Docker, pero **el daemon Docker no arranca sin root** en este entorno (`dockerd needs to be started with root privileges`), por lo que se descartó esa vía. - Overpass/OSM fue consultado dos veces; no devuelve `shop=car`, `shop=car_repair` ni…»
### C112 — Servicios de usuario con reinicio automático
- **Section**, **Lines**: §37 (L1124), 1124
- **Types**: contextual
- **Excerpt**: «Los servicios de usuario (`revolico-revisar`, `marketplaces-scrape`, `revolico-snapshot`) se reinician automáticamente tras fallo, de modo que los reinicios del servidor ya no detienen el trabajo.»

### C113 — Temporizador persistente de progreso
- **Section**, **Lines**: §38 Reporte automático de progreso (L1130–1141), 1139
- **Types**: contextual, methodological
- **Excerpt**: «El timer es persistente (`Persistent=true`) y arranca 1 minuto después del boot. De este modo el seguimiento sobrevive a los reinicios del servidor.»

### C114 — Renombre del repositorio en GitHub
- **Section**, **Lines**: §40 Renombre del repositorio en GitHub (L1156–1167), 1161–1165
- **Types**: contextual
- **Excerpt**: «antes: CarlosAntonioAceaJimenezCD/autodecide-habana / ahora: CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba» / «GitHub no permite espacios en los nombres de repositorio, por lo que se usó el slug `el-precio-de-moverse-en-cuba`.»

### C115 — Fuentes de estaciones de carga y respuesta 403
- **Section**, **Lines**: §41 (L1175), 1175
- **Types**: contextual
- **Excerpt**: «**Kargalaya** aportó 9 estaciones de carga con coordenadas y precio por hora (Super48, Battery Lab, SOLGUARA, Parqueo M y 25, Universidad de Ciencias Médicas, Trisolinera Habana, PDL Campeño, ADT64, Automovion SRL). **Electromaps** añadió 3 referencias sin coordenadas. ChargeFinder…»
### C116 — Colores y símbolos asignados en el mapa
- **Section**, **Lines**: §42 (L1188–1195), 1190–1195
- **Types**: definitional
- **Excerpt**: «| Gasolinera | negro | círculo | ... | Estación de carga | verde | diamante | ... | Concesionario | azul | cuadrado | ... | Taller | rojo | triángulo |»

### C117 — Uso de patchright y FlareSolverr tras un 403
- **Section**, **Lines**: §42 (L1199), 1199
- **Types**: contextual
- **Excerpt**: «**Cybo devolvió 403 con curl_cffi**, por lo que se aplicó el stack anti-bot disponible: `patchright` (Chromium con fingerprint de Chrome) y FlareSolverr en `http://127.0.0.1:8191/v1`. Las direcciones se geocodificaron con Nominatim y Photon (`geocode_elementos.py`); las tres referencias de…»
### C118 — Apertura del storytelling en dos capas de mercado
- **Section**, **Lines**: §46 Apertura de la sección 3 del storytelling (L1240–1244), 1242
- **Types**: contextual
- **Excerpt**: «Se añadió una apertura que hace explícita la división del mercado en dos capas —marketplaces y concesionarios/tiendas oficiales— y una nota que define el propósito de la sección: mostrar la forma real del mercado después de separar el ruido, sin explicar el proceso de adquisición de datos.»

### C119 — Curva de valor como narrativa de envejecimiento desigual
- **Section**, **Lines**: §47 Reescritura de la sección 4 del storytelling (L1248–1252), 1250
- **Types**: contextual
- **Excerpt**: «Se transformó **La curva de valor** en una narrativa sobre el envejecimiento desigual del parque: premium frente a autos de uso medio, combinación de antigüedad con kilometraje, estado y marca, y la idea de la marca como “seguro de valor”. Se eliminaron los porcentajes repetidos de la…»
### C120 — Exclusión de falsos positivos en la búsqueda de repositorios
- **Section**, **Lines**: §49 (L1275), 1275
- **Types**: contextual
- **Excerpt**: «Se excluyeron falsos positivos de la búsqueda amplia (GTA, proyectos genéricos “Taller 1”, repos sin relación con Cuba o automoción). El repositorio `kremondherranz-lgtm/Mercado-automotriz` ya había sido clonado en `Auxiliares/Repositorios Referencias`.»

### C121 — Grupos de duplicados detectados al consolidar repositorios
- **Section**, **Lines**: §50 (L1285), 1285
- **Types**: result
- **Excerpt**: «Se compararon 233 archivos de datos por hash y 76 CSV por contenido ordenado. Se detectaron 12 grupos de duplicados bytes y 11 de duplicados por contenido: anuncios repetidos dentro de `Mercado-automotriz`, `anuncios_limpios` = `mercado_havana`, `DATASET_COMPLETO_MEJORADO` =…»
### C122 — Convención de la tabla de obras del mapa literario
- **Section**, **Lines**: §71.14 (L1559–1560, L1600), 1559–1560, 1600
- **Types**: contextual, citation-grounded
- **Excerpt**: «| Ref. | Clúster | Autor (año) | Obra | ... / Los trabajos [1], [9], [14], [26] y [29] se discuten además en §71.6; el resto se registra aquí con su marcador numérico y se enlaza a `Data/referencias.md`.»

### C123 — Convención de referencias numeradas y su estado de verificación
- **Section**, **Lines**: §70 (L1497, L1499), 1497, 1499
- **Types**: contextual, citation-grounded
- **Excerpt**: «La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`; la correspondencia entre afirmación y fuente se documenta en el expediente forense.»

### C124 — Registro de la tercera pasada y sus 13 artefactos
- **Section**, **Lines**: §69 (L1489), 1489
- **Types**: contextual
- **Excerpt**: «El registro de la tercera pasada está en `reviews/informe-tecnico-2026-11-27-iter3.{md,forensic.md}` y sus 13 artefactos.»

### C125 — Firma y última actualización del informe
- **Section**, **Lines**: cierre del documento (L1604–1605), 1604–1605
- **Types**: contextual
- **Excerpt**: «**Firma / Signature:** responsable del proyecto / project owner. / **Última actualización / Last update:** 27/11/2026.»

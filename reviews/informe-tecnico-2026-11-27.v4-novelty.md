---
type: audit-artifact
phase: v4-novelty
slug: informe-tecnico-2026-11-27
generated_at: 2026-11-27T05:51:34Z
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27/informe-tecnico-2026-11-27.text.md
language: es
level: master
---

## Resumen

- E1 registra 191 afirmaciones con `novelty 0` y los 14 campos «Novelty signals: Ninguno»: no hay claims etiquetados como novedad que evaluar literalmente.
- Se derivan nueve candidatos de originalidad del texto audicionado, contrastados con los 38 trabajos del mapa E2; la mayoría conserva un diferenciador local pero no articula comparación explícita con el trabajo más cercano.
- El solapamiento más fuerte aparece en scraping + modelado de precios (P014) y en regresión hedónica (P009); la cobertura de E2 es incompleta (8 búsquedas web con HTTP 403, 38 trabajos L1 de 50 objetivo), lo que limita toda conclusión de novedad.

### F-V4-001 — E1 no contiene ninguna afirmación etiquetada `novelty`; los candidatos se derivan del texto

El resumen de E1 consigna: «By type: result 86 · methodological 66 · novelty 0 · contextual 122 · definitional 16 · citation-grounded 21» (e1-claims, línea 16), y los catorce campos «**Novelty signals**: Ninguno» que acompañan a C001–C014 (líneas 31, 43, 55, 67, 79, 91, 103, 115, 127, 139, 151, 163, 175, 187). En consecuencia, la misión literal de V4 —filtrar claims etiquetados `novelty`— no tiene objetos de entrada en este caso. Los hallazgos F-V4-002 a F-V4-010 construyen candidatos a partir de enunciados de originalidad implícita en el documento (§1, §15, §17, §19–20, §23, §34, §36–42, §50, §52, §64–66), marcados uno por uno como derivaciones interpretativas.

Incertidumbre: el mapa E2 declara `queries_run: 33`, `papers_l1: 38` frente a un objetivo de 50 del preset Standard, «WebSearch queries: 8 intentos, todos con HTTP 403» y un trabajo L3 de tres previstos (e2-literature, líneas 6–11 y 556–565). Una conclusión de «novedad confirmada» en este artefacto significa únicamente «sin antecedente en el mapa disponible», no ausencia de arte previo. El criterio `V4.scope_of_novelty_claim` para `level=master` se lee: «Component novelty + integration novelty: one of the two should be substantive» (level-criteria.md, línea 97).

— polarity: neutral · confidence: high · related: — · criteria: V4.scope_of_novelty_claim.master

### F-V4-002 — Pipeline de scraping con SQLite por tienda: gemelo metodológico P014 sin citar

Candidato derivado. El documento declara en §1 (L16): «El análisis se apoya en dos pilares: la base de datos del mercado cubano y un pipeline de scraping reutilizable que se actualiza para adaptarse al momento en que se revise», y en §8 (L88): «El scraper `scrape_concesionarios.py` usa adaptadores por dominio y renderizado opcional con Playwright». El trabajo más cercano del mapa es P014 — Gegić, E.; Isaković, B.; Keco, D.; Mašetić, Z.; Kevrić, J. (2019), «Car Price Prediction using Machine Learning Techniques», *TEM Journal*, DOI 10.18421/tem81-16 (OpenAlex W4288610071, 188 citas), marcado `Cited in document: no`. E2 lo describe como «el antecedente más directo de la combinación scraping + modelado de precios que el informe implementa con Revolico y los concesionarios» (e2-literature, L176). El segundo vecino es P026 — Muça, M.; Bani, K.; Alla, A. (2026), «A Pipeline for Integrating and Analyzing Public Business Data in Albania Using Web Scraping and Machine Learning», *IJACSA*, DOI 10.14569/ijacsa.2026.0170845, también `Cited in document: no`.

El diferenciador que el informe declara es de integración local: bases SQLite separadas por tienda (§8, L88), commits por lotes de 25 anuncios (§16, L779), deduplicación por título normalizado, prefijo y dominio (§11, L129), separación de monedas (§19, L846), columnas de auditoría (§15, L769) y tabla `provenancia` (§50, L1263). E2 observa que son «justamente los ejes del informe» los que P014 no documenta (L176), de modo que el candidato subsiste como novedad de integración; sin embargo, no hay párrafo de comparación con P014 ni con P026, y ninguno de los dos aparece nombrado en el documento. El alcance es local («primera integración en este mercado»), no global.

Incertidumbre: la atribución a P014 como «closest prior work» proviene del `abstract_analysis` de E2, no de una lectura directa del artículo en esta evaluación; E1 no etiquetó C031/C045 como `novelty`. Para `level=master`, `V4.differentiation_from_prior_art` exige «at least one explicit comparison paragraph to one closest prior work» (level-criteria.md, línea 88); aquí la comparación se da contra el repositorio egipcio (F-V4-004), no contra P014.

— polarity: negative · confidence: medium · related: [[#C031]], [[#C045]], [[#C163]], [[#P014]], [[#P026]] · criteria: V4.differentiation_from_prior_art.master

### F-V4-003 — Marco analítico «derivado de los trabajos revisados»: Akerlof citado solo por nombre

Candidato derivado. §19 (L833) rotula el marco como «**Marco general (8 pasos, derivado de los trabajos revisados)**» y §19 (L849) precisa: «clases de calidad (≤5 años alta, >5 años con defectos, según PUCE); bandera de asimetría por ocultamiento; comparables por modelo ±2 años y municipio; rentabilidad = reventa esperada − compra − reacondicionamiento − impuestos (Decreto 163/2026); asequibilidad = precio / salario; series con snapshots». El origen se declara explícitamente: §17 (L793) atribuye a la PUCE «Asimetría de información (Akerlof); clasificación de calidad por antigüedad [...] encuesta a 130 comerciantes».

El trabajo más cercano es P001 — Akerlof, G. A. (1970), «The Market for "Lemons": Quality Uncertainty and the Market Mechanism», *The Quarterly Journal of Economics*, DOI 10.2307/1879431 —, con `Cited in document: yes` pero solo como mención nominal en §17, §19 y §20, sin numeración (`metadata incomplete`). El eslabón empírico identificado por E2, P002 — Lewis, G. M. (2011), «Asymmetric Information, Adverse Selection and Online Disclosure: The Case of eBay Motors», *American Economic Review*, DOI 10.1257/aer.101.4.1535 —, figura en `likely_missing important works` y tiene `Cited in document: no`. Lo mismo ocurre con P003 (Peterson & Schneider, 2014, *RAND Journal of Economics*, DOI 10.1111/1756-2171.12045) y con P033 (Guerra, 2015, *Journal of Transport Geography*, DOI 10.1016/j.jtrangeo.2015.01.014), antecedente regional de la métrica `precio / salario`.

El diferenciador declarado es la adaptación a La Habana con doble tasa de cambio y precios pedidos (§19, L846–851), y el propio texto califica el marco como «derivado», por lo que no se registra sobreclaim de originalidad. En cambio, no hay contraste argumentativo con Akerlof, Lewis ni Guerra: la referencia a Akerlof es una invocación de marco, no una discusión de métodos, resultados o limitaciones. `V4.prior_art_engagement` para `level=master` pide «closest prior works cited, contrasted, and discussed in their own subsection» (level-criteria.md, línea 106); la primera y la tercera condición no se observan para P002 y P033, y la segunda tampoco para P001.

Incertidumbre: la clasificación de P002/P003/P033 como trabajos más cercanos sigue el juicio de E2; la sección 17 del documento cita además fuentes no académicas (PUCE, Chile, spinny) que no entran en el mapa.

— polarity: negative · confidence: medium · related: [[#C048]], [[#C052]], [[#C098]], [[#C099]], [[#P001]], [[#P002]], [[#P003]], [[#P033]] · criteria: V4.prior_art_engagement.master

### F-V4-004 — «Brecha frente a Egipto»: única comparación explícita, con referente ajeno al mapa

El documento incorpora en §34 (L1054–L1056) el apartado «Brecha frente a Egipto» con el texto: «Egipto tiene 23.500 anuncios, historial mensual de precios, HP y kilometraje estructurados, ANOVA/OLS/VIF, Tableau y Power BI. Nosotros tenemos el pipeline y las técnicas cubiertas, pero solo 497 usados, un único snapshot, HP/kilometraje mayormente ausentes y un solo benchmark de auto nuevo». Es el único pasaje del corpus con estructura de párrafo comparativo orientado a diferenciar la propia aproximación de un antecedente concreto; §34 (L1014) atribuye además la arquitectura del esqueleto al repositorio `Egyptian-Used-Cars` (C121). El diferenciador que emerge es de escala y cobertura de datos, no de método.

El referente egipcio no figura en el mapa E2, que tampoco registra ningún trabajo sobre mercados automotores egipcios; por tanto, el párrafo satisface la forma del criterio `V4.differentiation_from_prior_art.master` («at least one explicit comparison paragraph to one closest prior work») respecto de una fuente de ingeniería, pero no respecto del trabajo académico más cercano (P014, P009). Se registra como observación descriptiva, sin valoración de la comparación en sí.

Incertidumbre: E1 clasificó este pasaje como `contextual` (C123), no como `novelty`; la lectura aquí es derivada.

— polarity: neutral · confidence: high · related: [[#C121]], [[#C123]] · criteria: V4.differentiation_from_prior_art.master

### F-V4-005 — Modelo hedónico log-lineal: forma funcional y cautela coincidentes con P009

Candidato derivado. §34 (L1052) reporta: «El modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` da una depreciación media de **−5,43 % anual** (p<0,001), con primas de +21 % para premium y −22 % para tier medio frente al desconocido»; §59 (L1377) y §60 (L1385) retiran después la pendiente anual y la prima premium tras corregir kilometraje. El vecino más cercano del mapa es P009 — Du, Z.; Yang, Z.; Zhang, Y.; Li, S.; Liu, Y. (2026), «Nonlinear Depreciation and Brand Heterogeneity in Chinese Used-Car Listing Prices: An Interpretable Hedonic Regression and Out-of-Sample Evaluation», *Advances in Economics, Management and Political Sciences*, DOI 10.54254/2754-1169/2026.38524 —, con `Cited in document: no`. E2 lo llama «el paralelo metodológico más cercano al informe» y señala que «la coincidencia en la forma funcional y en la cautela interpretativa es alta» (L123). Complementan P011 (Miranda et al., 2026, *Journal of Business Insight and Innovation*, DOI 10.63544/jbii.v5i6.110) y P013 (Francke & Van de Minne, 2020, *Real Estate Economics*, DOI 10.1111/1540-6229.12320), ambos sin citar; P004 (Englmaier et al., 2017, *Management Science*, DOI 10.1287/mnsc.2016.2714) documenta saltos de precio en umbrales de año y kilometraje.

El documento no enuncia originalidad para el modelo: lo presenta como estimación ejecutada sobre datos propios. Leído como novedad local de aplicación, el diferenciador declarado es el contexto cubano, los precios pedidos y el tamaño muestral (744 autos únicos en §59, L1375), junto con el reporte de VIF y Kruskal-Wallis (§60, L1385). P009 cubre ya la misma forma log-lineal, laheterogeneidad por marca premium y la pérdida de significancia del kilometraje, de modo que existe solapamiento de alcance; la conclusión de E2 (H2, L542) es que la inestabilidad es «un resultado esperable de la especificación, no una anomalía del proyecto». Bajo `V4.scope_of_novelty_claim.master` («component novelty + integration novelty: one of the two should be substantive»), el componente metodológico no se distingue de P009 y la integración se apoya en los datos, no en una contribución de método.

Incertidumbre: la semejanza se establece a partir del `abstract_analysis` de E2, no de una comparación directa de coeficientes entre ambos trabajos; E1 marcó `Novelty signals: Ninguno` en C009 y C011.

— polarity: negative · confidence: medium · related: [[#C009]], [[#C011]], [[#C074]], [[#C176]], [[#P009]], [[#P011]], [[#P013]], [[#P004]] · criteria: V4.scope_of_novelty_claim.master

### F-V4-006 — Conversión por TRMI informal fechada: precedente cubano P029 sin citar

Candidato derivado. §23 (L898) establece: «la conversión usa `precio_USD × TRMI elTOQUE` del día del anuncio (columna `Mediana` de `Anexos/Investigacion Cambios/trmi_USD.csv`)», y §52 (L1293) remata: «La conversión del proyecto sigue usando la **TRMI informal** de elTOQUE (930 CUP/USD), nunca la oficial». El trabajo más cercano es P029 — Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A. (2024), «Using AI in the informal currency market: evidence from Cuba», *Applied Economics*, DOI 10.1080/00036846.2024.2416091 —, `Cited in document: no`, descrito en E2 como «el precedente académico directo del uso del TRMI de elTOQUE en el informe» (L342). El vecino P032 — Ávila Castellanos, D. D. (2024), «Currency exchange in post-ordenamiento Cuba: An exploration of institutional waiting for dollar purchases», *Revista Foro Cubano*, DOI 10.22518/jour.rfc/2023.6a02 — tampoco se cita.

El diferenciador que el texto declara es doble: anclar la tasa al día del anuncio y mantener la tasa informal separada de la oficial. E2 precisa el contraste: «el informe toma la tasa publicada como insumo y no construye su propio estimador, y que su serie de precios es de autos, no de divisas» (L342). No se registra, por tanto, sobreclaim: la novedad es de integración local (serie de precios de autos × TRMI diaria), y no hay arte previo en el mapa que haga exactamente esa conversión fechada. Tampoco hay párrafo de comparación con P029 ni mención de su nombre, de modo que el diferenciador queda enunciado pero no contrastado.

Incertidumbre: E1 clasificó C056 y C058 como `methodological`/`result` sin señal de novedad; la cercanía de P029 se toma del juicio de E2, y la afirmación de «sin antecedente exacto» depende de un mapa incompleto.

— polarity: negative · confidence: medium · related: [[#C056]], [[#C058]], [[#C068]], [[#C099]], [[#P029]], [[#P032]] · criteria: V4.differentiation_from_prior_art.master

### F-V4-007 — Procedencia, cuarentena e idempotencia: P023 y P024 en `likely_missing`

Candidato derivado. §64 (L1421) describe: «tres carriles desacoplados (recolectar, procesar, publicar), periodicidad realista en UTC, idempotencia por clave de fuente, marcas de agua, escrituras atómicas, cuarentena de datos inválidos, `SALUD.md` como dead-man's switch y manifiestos con hashes para reconstruir qué se sabía en cualquier fecha»; §54 (L1321) añade los 82 chunks de 10 MB con `MANIFEST.json` y SHA-256; §50 (L1263) la tabla `provenancia`; §65 (L1429) la distinción entre `SIN DATOS` y `STALE`. El vecino más cercano es P023 — Priestley, M.; O'Donnell, F.; Simperl, E. P. B. (2023), «A Survey of Data Quality Requirements That Matter in ML Development Pipelines», *Journal of Data and Information Quality*, DOI 10.1145/3592616 —, y el segundo P024 — Hohensinner, R.; Mutlu, B.; Mendoza Estrada, I. G.; Vukovic, M.; Kopeinik, S.; Kern, R. (2026), «Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability in LLMs», arXiv:2601.14311. Ambos tienen `Cited in document: no` y ambos figuran en la sección `likely_missing important works` de E2 (L512–L515 y L527–L530); P022 (Brown et al., 2025, *Big Data & Society*, DOI 10.1177/20539517251381686) completa el grupo y tampoco se cita.

El diferenciador declarado es la concreción operativa —timers de systemd cada 10 minutos, Git LFS, hashes por fragmento, cuarentena— frente a los marcos normativos generales de esos tres trabajos. La arquitectura se describe con detalle de implementación, sin reclamar primacía conceptual; el componente de idempotencia y dead-man's switch no tiene equivalente en el mapa. Sin embargo, no se registra ninguna mención de P023, P024 ni P022 en el documento, ni un párrafo que contraste la implementación con esos marcos, y E2 caracteriza la adopción como «de facto» y no «una adopción deliberada» (L530). Para `level=master`, `V4.prior_art_engagement` exige trabajos citados, contrastados y discutidos en su propio subapartado (level-criteria.md, línea 106); aquí falta la primera condición para los tres.

Incertidumbre: la correspondencia entre mecanismos del informe y categorías de P023/P024 proviene del `abstract_analysis` de E2; E1 etiquetó C183 y C185 como `contextual, methodological`, sin `novelty`.

— polarity: negative · confidence: medium · related: [[#C091]], [[#C163]], [[#C183]], [[#C185]], [[#P022]], [[#P023]], [[#P024]] · criteria: V4.prior_art_engagement.master

### F-V4-008 — Mapa offline e infraestructura EV: solapamiento parcial con P030

Candidato derivado. §36 (L1083) registra «Se generó `Data/mapas/mapa_ofline.html`: contorno de Cuba embebido + marcadores + Plotly incluido, funciona sin internet», §41 (L1152) las tres capas y §42 (L1173) el estado final «131 gasolineras, 12 estaciones de carga, 25 concesionarios (17 con coords) y 22 talleres (todos con coords)»; §62 (L1403) añade la extracción de 2.473 puntos, 244 circuitos y 166 polígonos del APK de Circuitos Habana. El vecino del mapa es P030 — Castro Fernández, M.; Vilaragut Llanes, M.; Hernández, J. C. (2024), «Electromobility and Energy Transition in Cuba», *Sustainability*, DOI 10.3390/su16229688 —, `Cited in document: no`. E2 describe la superposición con §36, §41 y §42 y la diferencia: «el artículo propone política energética nacional, mientras el informe geolocaliza infraestructura existente para contextualizar el costo de moverse» (L353).

El diferenciador, según esa lectura, es de propósito y escala (inventario geolocalizado frente a hoja de ruta nacional) y el timelapse de circuitos constituye un componente sin par en el mapa. El documento no articula la comparación con P030: el trabajo no se nombra y no hay párrafo que explicite la distinción. El alcance es local y el componente de geolocalización es substantivo, pero la ventaja declarada queda implícita en la elección de datos.

Incertidumbre: E1 registró C130, C144, C149 y C180 como `contextual`/`result`; la lectura como candidato de novedad es derivada. E2 no incluye trabajos de cartografía de infraestructura de transporte en Cuba más allá de P030.

— polarity: negative · confidence: medium · related: [[#C130]], [[#C144]], [[#C149]], [[#C180]], [[#P030]] · criteria: V4.differentiation_from_prior_art.master

### F-V4-009 — Ranking de eficiencia Telegram/Facebook/WhatsApp sin antecedente en el mapa

Candidato derivado. §15 (L763) afirma: «Para obtener más datos del mercado habanero, la ruta más eficiente es Telegram MTProto (`telethon`, ya integrado): sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`. Le sigue Facebook GQL [...] Playwright/Selenium quedan como último recurso para páginas JS». E1 (C007) observa que «el texto no adjunta una medición de tiempo por fuente». El mapa E2 no contiene ningún clúster de comparación de eficiencia entre canales de adquisición: el clúster 3 agrupa ética, legalidad y calidad de datos (P021–P028), sin benchmarks de scraping.

En consecuencia, no se identifica arte previo dentro del mapa que contradiga o cubra el mismo alcance; el enunciado opera como hallazgo operativo local, no como reclamación de originalidad. No se registra una declaración explícita de diferenciador frente a trabajo académico alguno. Bajo `V4.scope_of_novelty_claim.master`, la novedad de componente no se distingue de una preferencia de ingeniería y la de integración no se enuncia como contribución.

Incertidumbre: alta: la ausencia en el mapa se produce en un subárea que E2 no consultó con queries dedicadas (las búsquedas declaran ética/legalidad y calidad, no eficiencia de canales), y las 8 búsquedas web fallaron con HTTP 403. La calificación es «sin antecedente en el mapa», no «novedad confirmada».

— polarity: neutral · confidence: low · related: [[#C007]], [[#C092]], [[#C093]], [[#C094]] · criteria: V4.scope_of_novelty_claim.master

### F-V4-010 — Recomendador interactivo: reclamación de novedad diferida, sin objeto vigente

La Parte II (L145) conserva la formulación original: «Its goal is to define an interactive product able to recommend the most profitable car purchase in the **Havana** automotive market, based on the user's values, concerns and constraints». La Parte I (L16) y §21 (L877–884) registran el cambio: «La definición de un producto interactivo que recomiende la compra más rentable según las preocupaciones del usuario queda diferida a una especialización posterior», y §12 (L137) confirma que «el producto interactivo se difiere a una especialización futura». E1 lo inventaría como C001 y C103, con `Novelty signals: Ninguno`.

No hay en el mapa E2 un clúster de sistemas de recomendación de automóviles ni de ponderación de preferencias del usuario, de modo que no existe arte previo con el cual contrastar una eventual reclamación; pero el documento no sostiene esa reclamación en el estado evaluado. Se registra la ausencia de objeto de novedad como observación descriptiva, sin atribuir mérito ni vacío.

Incertidumbre: la Parte II no fue actualizada al nuevo objetivo y mantiene la redacción inglesa anterior (C001, Notas), por lo que la lectura depende de qué versión se tome como vigente; se eligió la Parte I y §21 por ser posteriores en el texto.

— polarity: neutral · confidence: high · related: [[#C001]], [[#C103]] · criteria: V4.scope_of_novelty_claim.master

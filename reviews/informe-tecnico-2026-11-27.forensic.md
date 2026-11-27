---
type: audit-forensic
slug: informe-tecnico-2026-11-27
generated_at: 2026-11-27T02:10:00-05:00
audited_document: INFORME_TECNICO.md
audited_document_title: Informe técnico / Technical report — El precio de moverse en Cuba
language: es
level: master
preset: Standard
phases_executed: [0, 1, 2, 3]
dimensions_run: [V1, V2, V3, V4, V5, V6, V7, V8, V9]
dimensions_skipped: []
phase1_failures: []
phase2_failures: []
phase_artifacts:
  plan: informe-tecnico-2026-11-27.plan.md
  e1: informe-tecnico-2026-11-27.e1-claims.md
  e2: informe-tecnico-2026-11-27.e2-literature.md
  e3: informe-tecnico-2026-11-27.e3-artifacts.md
  v1: informe-tecnico-2026-11-27.v1-structure.md
  v2: informe-tecnico-2026-11-27.v2-methodology.md
  v3: informe-tecnico-2026-11-27.v3-results-evidence.md
  v4: informe-tecnico-2026-11-27.v4-novelty.md
  v5: informe-tecnico-2026-11-27.v5-state-of-the-art.md
  v6: informe-tecnico-2026-11-27.v6-reproducibility.md
  v7: informe-tecnico-2026-11-27.v7-writing.md
  v8: informe-tecnico-2026-11-27.v8-bibliography.md
  v9: informe-tecnico-2026-11-27.v9-ethics.md
  forensic: informe-tecnico-2026-11-27.forensic.md
previous_iterations: []
---
# Auditoría forense — Informe técnico / Technical report

## §0 — Resumen del documento

El documento auditado es `INFORME_TECNICO.md`, un informe técnico bilingüe español/inglés titulado «Informe técnico / Technical report», fechado el 23 de noviembre de 2026 y firmado por «responsable del proyecto / project owner» (L1–8). La copia cacheada tiene 1.462 líneas y declara como estado «Fase 6 — scraping y captura de catálogos y anuncios, en curso / Phase 6 — scraping and capture, in progress». El plan fija el nivel `master` y el alcance declarado en §1 es un «análisis del mercado automotor cubano» —estructura, precios, oferta, segmentos, tendencias, asequibilidad y condiciones de rentabilidad—, con la definición del producto interactivo diferida a una especialización posterior.

E1 inventaría 191 afirmaciones, 14 de ellas load-bearing y ninguna etiquetada `novelty`, sin `hypotheses_planned` recibidas. Los ejes load-bearing son el cambio de objetivo y el estado de la fase 8 (C001, C002), el marco normativo del Decreto 163/2026 (C003), la naturaleza de «precios **pedidos**, no transaccionados» (C008), la depreciación hedónica y su retirada (C009, C011), los KPIs finales de autos, anuncios y mediana de precio (C010) y la ausencia de series oficiales de parque automotor y matriculaciones en los anuarios del ONEI (C012). §12 cierra con cinco conclusiones numeradas, una de las cuales afirma que «El análisis de mercado y el modelo de rentabilidad (fase 8) aún no están implementados» (L137), mientras §59–§60 reportan la corrida vigente de ese mismo modelo.

El repositorio `CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba` se nombra en §40 (L1136–1143). El texto declara 11 bases SQLite por tienda (§9), ocho marketplaces (§55), 12 anuarios del ONEI con 2014–2025 (§53), 82 fragmentos de 10 MB con `MANIFEST.json` (§54) y 25 tablas en `referencias_autos.sqlite` (§50). E3 registró el repo como no clonado; V6 verificó en el checkout un `README.md` de 105 líneas, un `requirements.txt` de 13 líneas, un orquestador `run_all.py` y 17 funciones `test_*` en tres scripts. El texto cacheado contiene 14 tablas sin numerar y no incrusta figuras, aunque el checkout conserva ocho PNG en `Data/analisis/graficos/` y seis HTML de Plotly en `docs/graficos/` (§23, §61).

La auditoría ejecutó las tres extracciones (E1–E3) y las nueve evaluaciones (V1–V9) con preset `Standard`, sobre un documento en español e inglés; el plan fue aprobado el 27/11/2026 con alcance «completa + mejoras». La verificación externa encontró HTTP 403 en WebSearch y Semantic Scholar y respuesta en vivo de Crossref y OpenAlex. E3 se produjo sin clon local y V6 operó sobre el checkout en `~/Proyectos/El precio de moverse en Cuba`. No se registró fallo de subagentes; V9 consignó que no recibió la tabla de densidad de V7, y V4 señaló cobertura incompleta del mapa literario (38 trabajos L1 de 50 objetivo).

## §1 — v1-structure


# V1 — Structure (findings)

### F-V1-001 — Encabezado de seis campos, sin resumen VSN-C ni contribuciones enumeradas

El texto cacheado se abre con seis campos en negrita —«**Proyecto / Project:**», «**Autor / Author:**», «**Fecha / Date:**», «**Ubicación / Location:**», «**Estado / Status:**», «**Idioma / Language:**» (L1–8)— y cierra con «**Firma / Signature:** responsable del proyecto / project owner» y «**Última actualización / Last update:** 23/11/2026» (L1461–1462). Tanto el campo de autoría (L4) como la firma (L1461) consignan un rol, no un nombre. Ninguno de los 87 encabezados del texto es «Resumen» o «Abstract», y no aparecen dedicatoria, agradecimientos ni dictamen de tutor en las 1462 líneas.

El material más próximo a un resumen se reparte entre §1 (L14–18), que enuncia problema y enfoque —«realizar un **análisis del mercado automotor cubano**: caracterizar estructura, precios, oferta, segmentos, tendencias, asequibilidad y condiciones de rentabilidad»—, y §12 (L131–137), cinco conclusiones numeradas. Ninguno de los dos bloques declara un elemento de novedad ni enumera contribuciones: el inventario de claims consigna `novelty 0` (E1, L16). Tampoco se enuncia una hipótesis central como proposición falsable: §20 (L857–871) despliega nueve bloques operativos y una lista de datos pendientes, y §34 (L1052) reporta «una depreciación media de **−5,43 % anual** (p<0,001)» sin proposición previa que la someta a contraste. E2 deja constancia de que no se recibieron `hypotheses_planned` y de que no existe un archivo `<slug>.plan.md` (E2, L16, L532–534).

— polarity: negative · confidence: high · related: [[#C001]], [[#C009]]

### F-V1-002 — Objetivo y fase 8 divergen entre Parte I, Parte II y §21; numeración 1–12 duplicada

Las dos partes paralelas abren con objetivos distintos. §1 (L14–18) nombra «El precio de moverse en Cuba», fija como objetivo actual «un análisis del mercado automotor cubano» y añade que «La definición de un producto interactivo que recomiende la compra más rentable según las preocupaciones del usuario queda diferida a una especialización posterior». §1 EN (L143–147), en cambio, nombra «AutoDecide Habana» y declara: «Its goal is to define an interactive product able to recommend the most profitable car purchase», sin la salvedad. La tabla de fases reproduce la divergencia en la fila 8: «Análisis de mercado, comparables y rentabilidad» (L33) frente a «Analysis, profitability model and interactive product» (L162).

§21 (L875–884) registra la revisión —«A petición del usuario, el objetivo inmediato deja de ser la recomendación interactiva de compra y pasa a ser **un análisis de mercado**»—, declara que «La fase 8 pasa a llamarse **Análisis de mercado, comparables y rentabilidad**» y reinterpretaba los bloques 1 y 8 del marco de §20; la Parte II no incorpora ese cambio. La numeración, por su parte, se reinicia: hay dos secciones «1.» (L14 y L143) y dos «12. Conclusiones» (L131 y L260), tras las cuales la secuencia continúa con §13 (L270) hasta §68 (L1453). E1 consigna la tensión entre la conclusión de §12 y las secciones de análisis ejecutado en C001, y el estado de las nueve fases en C002.

— polarity: negative · confidence: high · related: [[#C001]], [[#C002]]

### F-V1-003 — Macroestructura de registro cronológico; tablas y figuras sin numerar

Después de §12 EN (L260), el documento prosigue como bitácora: §13 «Registro de altas / Change log» ocupa L270–748, es decir 479 de las 1462 líneas del texto cacheado, con el marcador automático `<!-- REGISTRO_ALTAS -->` (L278) y una fila que declara «175 entradas adicionales no listadas / omitted» (L291). De las 55 secciones numeradas §14–§68, 53 llevan una fecha entre paréntesis en el encabezado (§16–§68; p. ej. §59 «Storytelling alineado con los datos finales (23/11/2026)», L1373); §14 y §15 son las dos sin fecha (L750 y L761). Varios títulos nombran una acción de edición más que el contenido que sigue —§45 «Reescritura de la sección 3 del storytelling» (L1208), §46 «Apertura de la sección 3 del storytelling» (L1216), §47 «Reescritura de la sección 4 del storytelling» (L1224)—, mientras otros sí lo anticipan, como §26 «Orden corregido: enlace → clasificación → BD» (L922) y §62 «Factibilidad del timelapse eléctrico» (L1401).

En las 1462 líneas no aparecen marcadores `??`, comandos `\ref{}` ni leyendas numeradas «Tabla N» o «Figure N»; E3 registra «Tables: none-detected» (L39) y «Figures: none-detected» (L148). Las tablas se localizan por su encabezado o por la sección que las contiene —«Métrica | Valor» en §34 (L1039–1050)— y las figuras por ruta de archivo —`Data/analisis/graficos/` en §23 (L901)—. §59 (L1377) añade que «el texto solo deja referencias discretas entre paréntesis, de modo que las tablas y figuras puedan insertarse sin romper la narrativa».

— polarity: neutral · confidence: high · related: []

## Resumen

- El encabezado es un bloque de seis campos con autoría y firma por rol; no hay resumen VSN-C, contribuciones enumeradas ni hipótesis falsable enunciada.
- Parte I y Parte II divergen en el objetivo, en el nombre de la fase 8 y en la numeración 1–12; §21 documenta un cambio que la versión inglesa no refleja.
- A partir de §13 predomina la bitácora fechada (53 de 55 secciones); tablas y figuras carecen de numeración y se citan por encabezado, sección o ruta, sin referencias rotas.


## §2 — v2-methodology


# V2 — Methodology (findings)

## Resumen

El documento declara tamaños muestrales, pruebas estadísticas y un protocolo con scripts, hashes y regeneración documentada, en el nivel de maestría.
No registra baseline SOTA-adjacente, ablación de componentes ni medición comparada de la eficiencia de las fuentes de captura.
Persisten la ausencia de semillas, la falta de tests pareados entre corridas y cifras incompatibles del mismo objeto sin marcador de versión.

### F-V2-001 — Modelo hedónico sin comparador SOTA-adjacente; el «benchmark» es descriptivo

El único componente comparativo del esqueleto de rentabilidad es `05_benchmark.py`, descrito como «benchmark por marca/modelo/año e infravalorados» (§34, líneas 1019–1025), con 21 «Grupos de benchmark» y 30 «Infravalorados» en la línea base (§34, líneas 1047–1050). El contraste con el estudio egipcio se presenta como brecha de volumen —«Egipto tiene 23.500 anuncios, historial mensual de precios, HP y kilometraje estructurados [...] Nosotros tenemos el pipeline y las técnicas cubiertas, pero solo 497 usados, un único snapshot» (§34, líneas 1054–1056)—, no como un comparador reproducible de desempeño. No se declara una comparación del modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` frente a un predictor trivial, a otra especificación o a un enfoque vecino al estado del arte. El criterio `V2.baselines` para `level=master` se lee: «≥2 baselines, one of which corresponds to a SOTA-adjacent approach in the field».

— polarity: neutral · confidence: high · related: [[#C009]], [[#C011]], [[#C123]], [[#F-V2-002]] · criteria: V2.baselines.master

### F-V2-002 — Orden de eficiencia de Telegram, Facebook y WAHA sin medición comparada

El informe establece un orden de eficiencia entre rutas de captura: «la ruta más eficiente es Telegram MTProto (`telethon`, ya integrado): sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`. Le sigue Facebook GQL [...] Playwright/Selenium quedan como último recurso» (§15, líneas 763–765). El inventario de claims registra la salvedad de que «el texto no adjunta una medición de tiempo por fuente» ([[#C007]]); la propia corrida pública de Telegram reporta «152 mensajes, 54 anuncios de autos [...] y ninguno con precio explícito» (§28, línea 948), mientras que el descubrimiento de canales suma 119 entradas (§29, líneas 962–967). La jerarquía se apoya en propiedades de las herramientas, sin tiempos, tasas de éxito ni tamaños de muestra comparables por ruta. El criterio `V2.baselines` para `level=master` se lee: «≥2 baselines, one of which corresponds to a SOTA-adjacent approach in the field».

— polarity: neutral · confidence: high · related: [[#C007]], [[#C092]], [[#C093]], [[#C113]], [[#F-V2-001]] · criteria: V2.baselines.master

### F-V2-003 — Sensibilidad al kilometraje como ablación implícita, sin ablación de componentes declarada

La primera ejecución reporta «El modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` da una depreciación media de **−5,43 % anual** (p<0,001), con primas de +21 % para premium y −22 % para tier medio» (§34, línea 1052); la narrativa final consigna que «el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra» (§59, línea 1377), con «p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05» (§60, línea 1385). Esta variación de especificación funciona como comprobación de sensibilidad de un covariable, no como ablación de los componentes declarados como aporte. Las mejoras posteriores se ejecutaron «una por una, sin borrar archivos» (§51, línea 1273), incluida la corrección del parseo de kilometraje (§51, línea 1278), sin que el texto aísle el efecto de cada cambio sobre la estimación. El mapa literario registra [[#P009]] (Du et al., 2026, DOI: 10.54254/2754-1169/2026.38524) con especificación log-lineal anidada casi idéntica y conclusión de no linealidad edad–precio, trabajo que el documento no cita. El criterio `V2.ablations` para `level=master` se lee: «Explicit ablation of at least one component».

— polarity: neutral · confidence: high · related: [[#C009]], [[#C011]], [[#C165]], [[#C067]], [[#P009]], [[#F-V2-005]] · criteria: V2.ablations.master

### F-V2-004 — Pruebas estadísticas y diagnósticos declarados en el pipeline final

El inventario de funciones y modelos enumera «normalización sintáctica y TRMI, features derivados, mediana y cuartiles, modelo hedónico log-lineal, VIF, Kruskal-Wallis, Welch t-test y detección de anomalías» y reporta «p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05» (§60, línea 1385). La arquitectura del esqueleto ya declaraba `04_stats.py` como «OLS log-precio, VIF, Kruskal-Wallis, anomalías» (§34, línea 1023) y la primera corrida acompañó el coeficiente de depreciación de `p<0,001` (§34, línea 1052). En el nivel de maestría, la presencia de pruebas y de diagnósticos de multicolinealidad, con la decisión de no sostener la significancia, constituye una observación positiva sobre la práctica estadística del documento. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)».

— polarity: positive · confidence: high · related: [[#C011]], [[#C176]], [[#C009]] · criteria: V2.statistical_tests.master

### F-V2-005 — Contrastes múltiples y cambio de corrida sin test pareado ni corrección declarada

Los tres coeficientes de la primera corrida —pendiente anual y dos contrastes de `brand_tier` (+21 % y −22 % frente al desconocido)— comparten un `p<0,001` sin que se declare ajuste por comparaciones múltiples (§34, línea 1052); la corrida final enuncia un «p mínimo 0,165» entre varias pruebas (§60, línea 1385) sin ajuste descrito. El paso de una depreciación significativa a su retirada compara dos ejecuciones sobre estados de datos distintos ([[#C009]], [[#C011]]), sin test pareado ni intervalo de diferencia. La reconciliación de la encuesta, de 29 a 28 interesados (§51, línea 1281), tampoco se acompaña de prueba estadística. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)».

— polarity: neutral · confidence: high · related: [[#C009]], [[#C011]], [[#C167]], [[#F-V2-003]], [[#F-V2-004]] · criteria: V2.statistical_tests.master

### F-V2-006 — Tamaños muestrales y cobertura declarados en cada etapa del análisis

El documento explicita el n en cada etapa: «Resultados sobre 323 autos: 248 precios USD válidos (≥500 USD); 74 precios <500 USD marcados como inválidos y 1 en CUP excluidos» (§22, línea 890); «Filas ingeridas 972 (716 Revolico + 256 concesionarios); Filas limpias 499; Observaciones del modelo OLS 328» (§34, líneas 1041–1047); «744 autos únicos» (§51, línea 1275); «2.014 anuncios limpios, de ellos 1.323 locales y 691 de importación» (§58, línea 1367); encuesta de «33 personas de 4 segmentos» y entrevistas «30 + 30 + 8» (§50, línea 1265). El número de instancias declaradas supera diez (11 bases por tienda en §9, 8 marketplaces en §55) y las observaciones del modelo superan veinte. El criterio `V2.sample_size` para `level=master` se lee: «≥20 trials; ≥10 datasets/instances».

— polarity: positive · confidence: high · related: [[#C053]], [[#C032]], [[#C010]], [[#C063]], [[#C164]] · criteria: V2.sample_size.master

### F-V2-007 — Cobertura de precio desigual entre tiendas y de kilometraje al 6,2 %

La tabla de la fase 6 muestra asimetrías de cobertura del campo de precio entre las 11 bases: «Chinautos Cuba | 70 | 0», «Envision Autos | 1 | 0», «MCV Commercial | 4 | 0», frente a «AGN Motors | 60 | 45» y «Finauto | 45 | 34» (§9, líneas 94–106). En el análisis descriptivo la cobertura declarada es «marca 68,4 %, año 63,5 %, km 6,2 % (heurísticos, extraídos solo de título/descripción)» (§22, línea 890), y el estado del scrapeo precisa que «No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión» (§24, línea 907). El texto añade que la línea base dispone de «un único snapshot» (§34, línea 1056): los recuentos son abundantes, pero la densidad de variables y la repetición temporal no son uniformes entre fuentes. El criterio `V2.sample_size` para `level=master` se lee: «≥20 trials; ≥10 datasets/instances».

— polarity: neutral · confidence: high · related: [[#C033]], [[#C055]], [[#C059]], [[#C123]], [[#F-V2-006]] · criteria: V2.sample_size.master

### F-V2-008 — Subsección «Límites» dedicada y auditoría de procedencia

El marco de análisis incluye un apartado específico: «**Límites**: precios pedidos no transaccionados, sesgo de supervivencia de anuncios, sin datos personales, vigencia normativa a verificar» (§19, línea 851). La auditoría de procedencia refuerza esa sección al clasificar las fuentes y sentenciar «No son estadísticas oficiales; son precios **pedidos**, no transaccionados» (§18, línea 822) y «las fuentes oficiales y gremiales sirven de **contexto y validación**; los anuncios y redes son la **señal de precio** pero no sustituyen estadísticas oficiales» (§18, línea 827). Se declaran además supuestos operativos —«se asume que son comprables; no se comprueba disponibilidad en tiempo real» (§23, línea 899) y el supuesto de catálogos de §25 (línea 917)— y la retención como «inferencia de diseño, no medición» (§63, línea 1413). El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations».

— polarity: positive · confidence: high · related: [[#C008]], [[#C057]], [[#C061]], [[#C097]], [[#C013]], [[#C123]] · criteria: V2.threats_to_validity.master

### F-V2-009 — Atribuciones causales y diagnósticos sin diseño comparativo

Tres conclusiones y diagnósticos del informe tienen forma causal sin comparación explícita: «El scraping sostenible depende del ritmo, la sesión y la reanudación, no principalmente del fingerprint TLS» (§12, línea 135; [[#C006]]), «La regla de las 10 páginas evitó consumir resultados repetidos» (§12, línea 136; [[#C014]]), y «Se identificó la causa del retraso en la clasificación: el timer ejecutaba `actualizar_revolico.py`, que solo corre el scraper y divide la BD, sin escribir nunca `autos`/`revision`» (§26, línea 924; [[#C062]]). La primera y la segunda se apoyan en reglas y conteos de las búsquedas (§7, líneas 76–84; §11, líneas 124–129), no en un contraste de condiciones. El propio texto deja «vigencia normativa a verificar» (§19, línea 851) y condiciona la publicación a la verificación de normas cubanas (§10, línea 117); el mapa literario concluye que la evidencia revisada «no permite pronunciarse sobre el cumplimiento legal en Cuba» (E2, comprobación H4). Las cuatro categorías clásicas de validez no aparecen nombradas en el documento. El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations».

— polarity: neutral · confidence: high · related: [[#C006]], [[#C014]], [[#C062]], [[#C005]], [[#F-V2-008]] · criteria: V2.threats_to_validity.master

### F-V2-010 — Protocolo reproducible con scripts, manifiestos con hash y regeneración documentada

La arquitectura de rentabilidad declara puntos de entrada numerados (`01_ingest.py` a `05_benchmark.py`, `run_all.py`) y `config.py` (§34, líneas 1016–1033). La integridad de datos se documenta con «un `MANIFEST.json` que guarda el SHA-256 del archivo completo, el orden, el offset y el hash de cada fragmento. La verificación de los 82 chunks dio OK» (§54, línea 1321), con herramienta `db_chunks.py` de `split`, `verify` y `assemble` (§54, línea 1323) y reconstrucción verificada por hash también en la sincronización por timer (§14, líneas 752–759). La regeneración se registra en dos puntos —«`run_all.py` volvió a correr sobre la base de 744 autos» (§51, línea 1276) y «El pipeline se regeneró con el entorno `Auxiliares/.venv-py`» (§58, línea 1367)—, junto a `requirements.txt` (§55, línea 1337), commits por lotes de 25 (§16, línea 779) y compilación `mkdocs build --strict` sin errores (§61, línea 1395). El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced».

— polarity: positive · confidence: high · related: [[#C121]], [[#C170]], [[#C176]], [[#C049]], [[#C024]], [[#C091]] · criteria: V2.reproducibility_protocol.master

### F-V2-011 — Semillas no declaradas en un protocolo por lo demás determinista

No aparece ninguna semilla aleatoria en el documento: la búsqueda textual solo devuelve «Las 8 semillas de marketplaces también se descargaron» (§55, línea 1333), referida a URLs semilla, no a `seed` o `random_state`. El inventario de modelos enumera transformaciones y estimaciones (§60, línea 1385) sin declarar semillas, al igual que la arquitectura de rentabilidad (§34, líneas 1016–1035) y la configuración del temporizador de captura (§66, línea 1437). Las estimaciones reportadas —OLS, medianas, IQR, VIF, pruebas de rangos— son deterministas dado el dataset; la selección de canales (§29, línea 967: 26 búsquedas en tgden.com) y las reglas de parada (§7, línea 76) se describen sin semilla asociada. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced».

— polarity: neutral · confidence: high · related: [[#C176]], [[#C121]], [[#C025]], [[#C187]] · criteria: V2.reproducibility_protocol.master

### F-V2-012 — Cifras incompatibles del mismo objeto sin marcador de versión entre secciones

Varios estados del mismo conjunto se presentan sin etiqueta que los distinga: «Se prepararon 11 bases y se obtuvieron **256 filas**» (§9, línea 92), «`anuncios` 6.334» (§24, línea 909), «**744 autos únicos**» (§51, línea 1275) y «**2.014 anuncios limpios**» (§58, línea 1367). La mediana de precio adoptada oscila entre «22.000 USD» (§22, línea 890), «24.000 USD» (§34, línea 1045), «23.000 USD» (§45, línea 1210) y «21.000 USD» (§59, línea 1375). La depreciación pasa de «−5,43 % anual (p<0,001)» (§34, línea 1052) y de su reiteración en el relato (§44, línea 1202) a «no encuentra una pendiente anual significativa tras corregir el kilometraje» (§59, línea 1377), sin que el texto marque qué corrida produce cada cifra. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced»; la coherencia entre declaraciones de distintas secciones queda así sin resolución interna.

— polarity: negative · confidence: high · related: [[#C032]], [[#C010]], [[#C054]], [[#C075]], [[#C009]], [[#C011]], [[#F-V2-005]] · criteria: V2.reproducibility_protocol.master

### F-V2-013 — Encuesta de demanda con n declarado pero marco de muestreo local

La encuesta de demanda se describe como «un Google Forms de 32 preguntas aplicado a 33 personas de 4 segmentos en un barrio de La Habana (17 de 18–25 prefieren eléctrico, pero 16 de 18 no pagarían más de 4.000 USD por uno)» (§50, línea 1265), y su reconciliación reduce a «28 interesados (14 eléctrico, 10 combustión, 4 híbrido)» (§51, línea 1281). El documento no declara marco de muestreo, tasa de respuesta ni intervalos de confianza para esas proporciones, y las «entrevistas (30 + 30 + 8) son cualitativas» (§50, línea 1265). La proyección de alcance se presenta como «inferencia de diseño, no medición» (§63, línea 1413), distinción que el texto explicita para la retención pero no para las preferencias de pago de la encuesta. El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations».

— polarity: neutral · confidence: high · related: [[#C063]], [[#C167]], [[#C164]], [[#C013]], [[#F-V2-008]] · criteria: V2.threats_to_validity.master


## §3 — v3-results-evidence


# V3 — Resultados y evidencia

## Resumen

Las afirmaciones de resultado con contenido numérico se contrastaron con las tablas internas del documento y con los CSV reales de `Data/analisis_rentabilidad/outputs/tables/`.
El respaldo más sólido aparece en los desgloses aritméticos internos, en 50 marcas / 81 anomalías / 30 infravalorados / mediana de 21.000 USD y en la no significancia actual del modelo hedónico.
Las discrepancias se concentran en el relato final (2.014 frente a 2.029 anuncios; 44.125 frente a 43.000 km), en la depreciación de −5,43 % anual y en cifras de infraestructura y fechas no reconciliadas entre secciones.

### F-V3-001 — La conclusión declara la fase 8 no implementada mientras las secciones 34–60 documentan su ejecución

La conclusión de §12 (línea 137) afirma: «El análisis de mercado y el modelo de rentabilidad (fase 8) aún no están implementados; el producto interactivo se difiere a una especialización futura». La misma afirmación se repite en la Parte II (§12 EN, línea 266) y en §1 (línea 16). Sin embargo, §34 (líneas 1012–1058) describe la creación de `Data/analisis_rentabilidad/` con `01_ingest.py` a `05_benchmark.py`, `sql/analysis.sql` y una «Línea base real de la primera ejecución» con 972 filas ingeridas, 499 limpias y un modelo OLS; §59 (líneas 1375–1377) y §60 (línea 1385) reportan resultados finales del mismo pipeline. La tabla real `outputs/tables/modelo_resumen.txt` contiene una regresión OLS fechada el 23/11/2026. El texto sostiene simultáneamente la inexistencia y la existencia del modelo sin una declaración que separe «modelo de apoyo exploratorio» de «modelo de rentabilidad entregado».

— polarity: negative · confidence: high · related: [[#C001]], [[#C009]], [[#C010]], [[#C011]], [[#C121]]

### F-V3-002 — «Nueve marketplaces con inventario real» y «una docena» frente al desglose de §5

La conclusión de §12 (línea 133) dice: «El mercado habanero tiene nueve marketplaces con inventario real y una docena con categorías vacías o solo piezas». La evidencia citada, §5 (líneas 60–64), enumera siete marketplaces con cifra (Autocubana 667, iTENCEL 951, VentaCuba 801, Timbirichi 281, Revolico 112 enlaces de primera página, Cogetucarro 5.225 y Cubisima 155) más dos sin cifra (Apululu y Carros.com Cuba): nueve en total, por lo que el primer conteo coincide con la enumeración. El segundo no coincide: la misma línea 62 reclasifica nueve sitios con «categoría vacía» y seis «de piezas, motos o servicios», es decir 15 sitios en las dos categorías que la conclusión resume como «una docena»; los dos sitios «sin sección real» quedan fuera de esa suma. La cifra de la conclusión no se desglosa en una tabla ni en §5 ni en §12.

— polarity: negative · confidence: high · related: [[#C004]], [[#C019]], [[#C020]]

### F-V3-003 — «Mejor densidad» incluye a Chinautos Cuba con cero filas con precio

§9 (línea 108) afirma: «Mejor densidad: AGN Motors, Chinautos Cuba, Dongfeng Cuba y Finauto». La tabla «Tienda | Filas | Con precio» de §9 (líneas 94–106) registra a Chinautos Cuba con 70 filas y 0 con precio, mientras que AGN Motors tiene 45/60, Finauto 34/45 y Dongfeng Cuba 16/45. La tabla de la Parte II (líneas 223–235) repite los mismos valores. Si «densidad» se lee como densidad de precio —la única columna derivada de la tabla— Chinautos Cuba es el extremo inferior de las cuatro tiendas citadas; si se lee como volumen, la etiqueta no distingue esa dimensión de la precedente. El texto no define el criterio.

— polarity: negative · confidence: high · related: [[#C032]], [[#C033]]

### F-V3-004 — Desgloses internos aritméticamente consistentes en seis secciones

Varios desgloses citados en el documento cuadran exactamente con sus totales: las 11 filas de §9 (líneas 94–106) suman 256, igual a la cifra de la línea 92; en §15 (línea 769), 304 autos + 6.028 exclusiones = 6.332 anuncios, y 5.983 + 45 + 0 = 6.028; en §31 (línea 985), 548 autos + 9.409 exclusiones = 9.957 anuncios, y 9.316 + 93 = 9.409; en §50 (línea 1263), 369 anuncios ya presentes + 3.589 nuevos = 3.958; en §51 (línea 1275), 748 identificadores únicos − 4 anuncios excluidos = 744 autos; en §51 (línea 1277), 872 + 99 + 2 = 973 anuncios recuperados. Estas cadenas aparecen con las mismas cifras en las versiones en inglés de cada sección.

— polarity: positive · confidence: high · related: [[#C032]], [[#C033]], [[#C042]], [[#C064]], [[#C065]], [[#C163]]

### F-V3-005 — El relato final reporta 2.014 anuncios y 1.323 locales; el CSV vigente registra 2.029 y 1.338

§59 (línea 1375) afirma: «El relato ahora usa **744 autos únicos**, **2.014 anuncios limpios** (1.323 locales y 691 de importación)», cifra que repite §58 (línea 1367) tras la inserción de diez anuncios de iTENCEL y que en §51 (línea 1277) aparecía como 1.301 locales y 672 de importación. El archivo real `Data/analisis_rentabilidad/outputs/tables/kpis.csv` (generado el 23/11/2026 a las 16:17) registra `anuncios_totales,2029.0`, `anuncios_locales,1338.0` y `anuncios_importacion,691.0`; `kpis_canal.csv` desglosa 1.317 locales usados + 21 locales nuevos = 1.338 y 691 de importación. La cifra de importación coincide; el total y el canal local difieren en 15 anuncios. El documento no consigna los 2.029 ni los 1.338 en ninguna sección.

— polarity: negative · confidence: high · related: [[#C010]], [[#C066]], [[#C074]]

### F-V3-006 — Kilometraje mediano: 44.125 km en el relato frente a 43.000 km en `kpis.csv`

La misma frase de §59 (línea 1375) y de §58 (línea 1367) fija «mediana de kilometraje 44.125 km». El CSV `Data/analisis_rentabilidad/outputs/tables/kpis.csv` registra `km_medianos,43000.0`. La diferencia es de 1.125 km. Ninguna sección del documento reporta 43.000 km ni describe un recálculo del kilometraje posterior al 23/11 que explique ambas cifras; §51 (línea 1278) documenta la corrección de `parse_number()` para `80,000 km`, sin adjuntar el valor agregado resultante.

— polarity: negative · confidence: high · related: [[#C010]], [[#C067]], [[#C074]]

### F-V3-007 — Cinco cifras del relato final coinciden con los CSV reales de rentabilidad

La frase de §59 (línea 1375) «50 marcas, 100 grupos comparables y 81 anomalías» y la mediana de 21.000 USD encuentran respaldo directo en los archivos reales: `kpis.csv` registra `marcas_distintas,50.0` y `precio_mediano_usd,21000.0`; `benchmark.csv` contiene 101 filas de datos de grupos; `anomalias.csv` contiene 81 filas. La cifra de 30 infravalorados, presente en la tabla de §34 (línea 1049) y en §44 (línea 1202), coincide con las 30 filas de `infravalorados.csv`; `importacion_por_marca.csv` y `kpis_canal.csv` coinciden en los 691 anuncios de importación. La única divergencia menor de este conjunto es de una fila en `benchmark.csv` (101 frente a 100 grupos).

— polarity: positive · confidence: high · related: [[#C010]], [[#C066]], [[#C074]], [[#C156]]

### F-V3-008 — −5,43 % anual con p<0,001 convive con la retirada del coeficiente en §59–§60

§34 (línea 1052) afirma: «El modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` da una depreciación media de **−5,43 % anual** (p<0,001), con primas de +21 % para premium y −22 % para tier medio frente al desconocido». La cifra se reutiliza en §44 (línea 1202), §45 (línea 1210) y en el resumen EN de §34 (línea 1058). En sentido opuesto, §59 (línea 1377) declara que «el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra», y §60 (línea 1385) confirma la no significancia. El archivo real `outputs/tables/modelo_depreciacion.csv` registra `car_age,-0.0708,0.237` y `C(brand_tier)[T.premium],0.0662,0.9474`; el único p_valor igual a 0,0 en esa tabla corresponde a `Intercept`, no a la edad. La revisión bibliográfica independiente describe el mismo patrón de inestabilidad en especificaciones log-lineales anidadas ([[#P009]], [[#P011]]).

— polarity: negative · confidence: high · related: [[#C009]], [[#C011]], [[#C075]], [[#C156]]

### F-V3-009 — Tres tablas reales sostienen la formulación cautelosa de §59–§60

La afirmación de §60 (línea 1385) —«la corrida actual **no** sostiene una tasa de depreciación ni una prima premium significativa (p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05)»— coincide con tres archivos reales: `modelo_depreciacion.csv` y `modelo_resumen.txt` muestran el menor p_valor no intercepto en `hp` (0,1648 / 0,165), `car_age` con p = 0,237 y `C(brand_tier)[T.premium]` con p = 0,9474; `vif.csv` contiene 1,54, 1,58, 1,17, 1,13 y 1,13; `tests.csv` contiene `Kruskal-Wallis precio por tier,26.518,1e-05`. Las tres líneas de evidencia concuerdan entre sí y con el lenguaje de la conclusión, que retira la cifra en lugar de mantenerla con cautela.

— polarity: positive · confidence: high · related: [[#C011]], [[#C176]], [[#P009]], [[#P013]]

### F-V3-010 — El modelo citado como «actual» se ajusta sobre 22 observaciones, cifra ausente del relato

`outputs/tables/modelo_regresion.txt` no existe; el respaldo es `modelo_resumen.txt`, que registra «No. Observations: 22», «R-squared: 0.277», «Adj. R-squared: -0.084», «F-statistic: 0.7674» y «Prob (F-statistic): 0.623». La narrativa de §59 (líneas 1375–1377) enmarca la reformulación dentro del conjunto final de «744 autos únicos» y «2.014 anuncios limpios», y §60 (línea 1385) habla de «la corrida actual» sin declarar el tamaño de la muestra estimada. La tabla interna de §34 (línea 1047) sí declaraba «Observaciones del modelo OLS | 328» para la primera ejecución; ninguna sección registra el paso de 328 a 22 observaciones. La base empírica de la afirmación de no significancia queda así sin dimensión muestral en el texto.

— polarity: negative · confidence: high · related: [[#C009]], [[#C010]], [[#C011]], [[#C123]]

### F-V3-011 — «7 lotes de 25» no cuadra con los 119 enlaces de la prueba de §16

§16 (línea 783) describe: «Prueba con 1 página: **119 enlaces** descubiertos y procesados, 7 lotes de 25, BD principal de 6.332 a **6.334 anuncios** y de 304 a **317 autos**». La regla de commit declarada en la línea 779 es «Cada **25 anuncios procesados** [...] se hace un commit por lotes». Con 119 enlaces procesados, el número máximo de lotes completos es cuatro y el de lotes con commit es cinco; siete lotes de 25 implican al menos 151 decisiones. El texto no explica si los lotes incluyen reprocesamientos de la corrida interrumpida descrita en la línea 909.

— polarity: negative · confidence: medium · related: [[#C045]], [[#C047]], [[#C060]]

### F-V3-012 — 120 enlaces descubiertos menos 63 descartados no dan 185 candidatos descargados

§26 (línea 931) registra: «Prueba con 1 página: 120 enlaces descubiertos, 63 descartados tempranamente y 185 candidatos descargados; `autos` pasó de 323 a 326 y `revision` de 6.085 a 6.134». Los propios términos de la frase dan 57 enlaces restantes tras el descarte temprano (120 − 63), frente a los 185 candidatos declarados. El orden corregido descrito en las líneas 926–928 establece que solo se descargan enlaces con `es_auto_candidato=1`, por lo que 185 descargas no pueden proceder de esos 57 enlaces sin una fuente adicional no declarada. El resumen EN de la línea 933 repite las tres cifras sin reconciliarlas.

— polarity: negative · confidence: high · related: [[#C062]], [[#C108]], [[#C044]]

### F-V3-013 — Tres conteos distintos para el corpus del ONEI: 117 enlaces, 118 documentos, 221 archivos y 233 archivos

§53 (líneas 1309–1311) afirma: «se descargaron **todos los documentos enlazados**: 111 PDF, 7 RAR y 103 archivos Excel extraídos» y añade que «Los 117 enlaces de documento encontrados se descargaron todos; solo se omitieron CSS y favicon». Los dos tipos de documento descargados suman 118 (111 PDF + 7 RAR), no 117; con los Excel extraídos el total es 221. §56 (línea 1347), en cambio, se refiere a «los 12 anuarios del ONEI y sus 233 archivos». El inventario de E3 (§53 y §56) ya consigna ambas cifras. El documento no explica la diferencia entre 221 y 233 ni entre 117 y 118.

— polarity: negative · confidence: high · related: [[#C069]], [[#C169]], [[#C174]]

### F-V3-014 — El número de gasolineras cambia de 137 en §41 a 131 en §42 sin registro del ajuste

§41 (líneas 1150 y 1152) reporta «**Overpass/OSM devolvió 137 gasolineras en La Habana**» y la creación de `Data/mapas/gasolineras.csv` con 137 registros, cifra repetida en la línea 1152 al regenerar `mapa_ofline.html` con tres capas. §42 (línea 1173) cierra con «Estado final: **131 gasolineras, 12 estaciones de carga, 25 concesionarios (17 con coords) y 22 talleres (todos con coords)»; el inventario de figuras de E3 reproduce ambos valores. Ni §41 ni §42 consignan una depuración, fusión o exclusión de seis gasolineras que explique el tránsito de 137 a 131.

— polarity: negative · confidence: high · related: [[#C143]], [[#C145]], [[#C149]]

### F-V3-015 — La TRMI informal aparece como 920 CUP/USD en §23 y como 930 CUP/USD en §52

§23 (línea 900) describe la serie con «la TRMI pasó de 680 CUP/USD (09/07/2026) a 920 (16-17/11/2026)» y en la línea 898 fija el procedimiento: «la conversión usa `precio_USD × TRMI elTOQUE` del día del anuncio (columna `Mediana` de `Anexos/Investigacion Cambios/trmi_USD.csv`)». §52 (línea 1293), fechado tres días después, afirma: «La conversión del proyecto sigue usando la **TRMI informal** de elTOQUE (930 CUP/USD), nunca la oficial». Las dos cifras corresponden al mismo concepto en fechas próximas y el documento no registra el valor del 20/11 ni una actualización de la serie; además, una expresión describe una tasa diaria por anuncio y la otra una tasa única.

— polarity: negative · confidence: medium · related: [[#C056]], [[#C058]], [[#C068]]

### F-V3-016 — «No se eluden mecanismos anti-automatización» frente al uso declarado de stack anti-bot e impersonación TLS

§10 (línea 116) establece: «No se eluden mecanismos anti-automatización; los HTTP 403/429 se registran como limitación», y §11 (línea 127) añade para carrosw: «Registrado como limitación; no se falsificó su contenido». Otras secciones describen medidas técnicas sobre bloqueos: §37 (línea 1096) reporta «una sesión curl_cffi por hilo (`threading.local`) con impersonación Chrome», y §42 (línea 1175) declara: «**Cybo devolvió 403 con curl_cffi**, por lo que se aplicó el stack anti-bot disponible: `patchright` [...] y FlareSolverr en `http://127.0.0.1:8191/v1`». El texto no distingue entre registrar un bloqueo como limitación y desplegar un stack anti-bot tras ese bloqueo; ambas formulaciones conviven sin una delimitación explícita de la regla operativa.

— polarity: negative · confidence: medium · related: [[#C005]], [[#C006]], [[#C150]]

### F-V3-017 — Telegram MTProto se presenta como «ya integrado» y «la ruta más eficiente» sin medición y sin credenciales

§15 (línea 763) afirma: «Para obtener más datos del mercado habanero, la ruta más eficiente es Telegram MTProto (`telethon`, ya integrado): sin navegador [...] Le sigue Facebook GQL [...] más rápido que Selenium». §28 (línea 946) registra lo contrario sobre la integración: «No hay credenciales MTProto (`TELEGRAM_API_ID`/`TELEGRAM_API_HASH` vacías), así que se implementó `Auxiliares/herramientas/scraper_telegram_publico.py`, que lee la vista pública `t.me/s/<canal>`». La corrida de esa alternativa (línea 948) produjo 54 anuncios «y **ninguno con precio explícito**». El orden de eficiencia se enuncia sin tiempos de ejecución, tasas de éxito ni comparación pareada entre las tres vías; E1 ya consigna la ausencia de medición en las notas de C007.

— polarity: negative · confidence: high · related: [[#C007]], [[#C092]], [[#C093]], [[#C112]], [[#C113]]

### F-V3-018 — §53 anuncia que el capítulo 13 incorporará parque y matriculaciones; §56 confirma que no existen

§53 (línea 1313) presenta el capítulo 13 como «la serie más útil [...] que permite incorporar parque automotor, matriculaciones y accidentes con series oficiales 2014–2025, hoy ausentes del análisis». §56 (línea 1347), tras revisar los 12 anuarios, corrige: «**No hay series de parque automotor ni de matriculaciones**, por lo que esa laguna signalada en `NECESIDADES.md` no se resuelve con los anuarios; la corrección quedó registrada». El inventario de E3 clasifica ambas series como artefactos ausentes. La expectativa de §53 permanece en el documento junto a su corrección, sin que la primera se marque como superada dentro de la propia sección.

— polarity: negative · confidence: high · related: [[#C012]], [[#C069]], [[#C072]]

### F-V3-019 — Mediana de 22.000 USD en el análisis inicial frente a 21.000 USD en el relato final

§22 (línea 890) reporta «Precio mediano **22.000 USD**, media 24.416,59 USD, IQR 11.375–35.000 USD» sobre 323 autos y 248 precios USD válidos. El cierre de §51 (línea 1277), §58 (línea 1367) y §59 (línea 1375) fija la mediana local en 21.000 USD sobre el conjunto regenerado, valor que coincide con `precio_mediano_usd,21000.0` y con `mediana_usd` de `local,usado` en `kpis_canal.csv`. La diferencia de 1.000 USD entre ambas etapas no se comenta en el texto; §51 (línea 1276) documenta la regeneración, pero no presenta una tabla de transición entre los 323 autos iniciales y los 744 finales.

— polarity: neutral · confidence: high · related: [[#C054]], [[#C010]], [[#C075]]

### F-V3-020 — Salvedades de procedencia y proyección formuladas con lenguaje no medido

La tabla de §18 (línea 822) clasifica los precios de marketplaces como «precios **pedidos**, no transaccionados», y la conclusión de la línea 827 añade que las fuentes oficiales sirven de «**contexto y validación**» sin sustituir a la señal de precio. §23 (línea 899) declara explícitamente el supuesto de anuncio activo y que «no se comprueba disponibilidad en tiempo real», y §19 (línea 851) enumera los límites. En la misma línea, §63 (línea 1413) rotula la retención como «**inferencia de diseño, no medición**» antes de dar las proyecciones. El léxico de estas cuatro afirmaciones no excede el tipo de evidencia disponible.

— polarity: positive · confidence: high · related: [[#C008]], [[#C013]], [[#C057]], [[#C097]], [[#P021]]

### F-V3-021 — «99,3 %» y mediana de un día en 189 autos sin tabla ni archivo citado

§15 (línea 771) afirma: «El 99,3 % de los anuncios tiene `updated_on_by_user` en los últimos 7 días (mediana 1 día en los 189 autos), lo que indica renovación frecuente por parte del vendedor». La afirmación se apoya en la misma línea en un caso empírico individual (un anuncio de 2024-12-17 en HTTP 200) y en las Condiciones de Uso de Revolico, pero no cita archivo, consulta SQL ni tabla para el 99,3 % ni para el subconjunto de 189 autos. El inventario de E3 no registra ningún artefacto de frescor de anuncios, y E1 consigna la ausencia de evidencia interna para C041. El denominador de 189 autos tampoco aparece en los recuentos de autos de §15 (304), §16 (317), §22 (323), §51 (744) ni §59 (744).

— polarity: negative · confidence: medium · related: [[#C040]], [[#C041]]

### F-V3-022 — Conteos de marketplaces de §5 y §39 difieren para las mismas tiendas sin reconciliación

§5 (línea 62) registra «Autocubana (667 vehículos), iTENCEL (951), VentaCuba (801 carros/camionetas), Timbirichi (281 carros) [...] Cogetucarro (5.225 anuncios)». §39 (línea 1123), fechado al día siguiente, reporta «Cogetucarro de 200 → **5.008**, Autocubana y Timbirichi a 40 páginas [...] Autocubana pasó de 400 a **566** y Timbirichi de 110 a **170**, totalizando **2.121 anuncios**». §58 (línea 1367) eleva iTENCEL de 951 a 961. Los valores para Cogetucarro (5.225 frente a 5.008), Autocubana (667 frente a 566) y Timbirichi (281 frente a 170) se refieren a las mismas tiendas y no incluyen una nota que identifique cuál de los dos recuentos es el vigente ni qué cambió entre uno y otro. Las unidades también difieren: la línea 62 mezcla vehículos, anuncios y enlaces de primera página, y la línea 1123 usa «anuncios».

— polarity: negative · confidence: high · related: [[#C019]], [[#C074]], [[#C137]]

### F-V3-023 — La estimación de tráfico de §65 se presenta como estimación, no como medición

§65 (línea 1429) cierra con «Estimación de red: **5–10 MB/mes** si no hay cambios y **50–90 MB/mes** con novedades». El resumen EN de la línea 1431 mantiene el calificativo «estimated». La frase no adjunta mediciones de transferencia ni contadores de `precio-*`, y el propio texto las presenta como proyección condicionada a la existencia de novedades. El alcance de la afirmación queda limitado por el léxico empleado.

— polarity: positive · confidence: high · related: [[#C077]], [[#C184]]


## §4 — v4-novelty


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


## §5 — v5-state-of-the-art


- Cobertura: 1 de 38 trabajos del mapa E2 aparece citado por nombre (2,6 %); 4 de los 5 clústeres tienen 0 citas, frente al rango 25–60 del criterio `V5.coverage_breadth.master`.
- Actualidad: la única cita académica es de 1970 (0 % de obras de los últimos 5 años, frente al ≥40 % del criterio `V5.recency.master`); 0 de los trabajos recientes del mapa aparecen en el documento.
- Peso y ausencias: 14 de 14 afirmaciones load-bearing de E1 sin cita numerada; 22 de los 23 trabajos del top-5 por clúster están ausentes; WebSearch devolvió HTTP 403 y OpenAlex respondió en vivo.

### F-V5-001 — Cobertura del mapa E2 — 1 de 38 trabajos citado y cuatro clústeres sin ninguna referencia

El mapa literario de E2 enumera 38 trabajos (P001–P038) repartidos en cinco clústeres: asimetría de información (8), modelos de precio y depreciación (12), ética/legalidad/procedencia/calidad de datos (8), Cuba/divisas/movilidad/asequibilidad (7) y señales de precio en marketplaces (3). En el documento auditado solo aparece citado por nombre un trabajo de ese mapa: Akerlof (P001), en la celda de aporte metodológico de la tabla de §17 (L793) y en el paso 3 del marco general de §19 (L837). La tabla de §17 (L789–804) nombra doce fuentes, pero son informes institucionales, gremiales y repositorios de código, no entradas del mapa académico. La distribución observada es 1/8 en el clúster 1 (12,5 %) y 0/12, 0/8, 0/7 y 0/3 en los otros cuatro; el total es 1/38 (2,6 %). El criterio `V5.coverage_breadth.master` se lee: «Main + adjacent clusters covered (25–60 papers)». El clúster 5 es de frontera y no exigible en este nivel, pero también queda sin citas.

El esfuerzo de descubrimiento documentado en §7 (L76–84) no se refleja en esa distribución: tres búsquedas recorrieron 159 páginas, devolvieron 1.542 resultados, 23 se marcaron como útiles y las descargas sumaron 194 aciertos y 63 fallos, con `manifest.jsonl` e `indice.md`. La investigación previa produjo un corpus en `Hombros/` y §17 convierte doce fuentes —del corpus y de repositorios de referencia— en requerimientos, sin que ninguna de las 37 obras académicas restantes del mapa pase a las secciones analíticas de §19–§20 o §34.

— polarity: negative · confidence: high · related: [[#P001]], [[#C048]] · criteria: V5.coverage_breadth.master

### F-V5-002 — Actualidad de la bibliografía — 0 citas de los últimos cinco años y 0 de los trabajos de 2024–2026

La tabla de distribución temporal de E2 (L439–451) consigna para la columna «In document bibliography» un solo registro, ubicado en `≤2021`, y cero registros en 2022, 2023, 2024, 2025 y 2026. Ese registro es P001, Akerlof 1970, verificado en vivo en OpenAlex (registro W2156109180, DOI 10.2307/1879431, `cited_by_count: 32562`, actualizado el 26/11/2026). La proporción de citas recientes es, por tanto, 0 de 1 (0 %); el criterio `V5.recency.master` se lee: «At least 40% from the last 5 years; foundational classics balanced». El único clásico fundacional presente no aparece acompañado de obras contemporáneas que lo conecten con los datos habaneros.

En el mapa, 14 trabajos tienen año 2024 o posterior según la tabla de E2 (7 de 2026, 1 de 2025 y 6 de 2024); ninguno se menciona en el documento, incluidos los dos textos completos leídos por E2 (P018, ProbSAINT, de 2024, arXiv:2403.03812; P024, de 2026, arXiv:2601.14311) y los tres trabajos de 2026 sobre precios de anuncios (P009, P010, P011). Nota de alcance: el recuento directo de los años asignados a P001–P038 en el propio mapa da 13 trabajos de 2024 o posterior (6 de 2026, 1 de 2025 y 6 de 2024) y 4 de 2023, frente a los 14 y 3 de la tabla resumen de E2; el total de 38 y la columna del documento (1 en `≤2021`, 0 en el resto) coinciden en ambas lecturas.

— polarity: negative · confidence: high · related: [[#P001]], [[#P018]], [[#P024]] · criteria: V5.recency.master

### F-V5-003 — Peso de la citación — 14 de 14 afirmaciones load-bearing sin cita numerada y un único autor nombrado en listas

El inventario de E1 registra 191 afirmaciones, 14 de ellas load-bearing (C001–C014). En las catorce, el campo «External evidence cited» dice «— (sin citas numeradas)»: por ejemplo C003 (L134, marco normativo), C008 (L822 y L827, precios pedidos frente a transaccionados) y C012 (L1347, ausencia de series del ONEI). El documento no emplea numeración tipo `[N]`, conforme a la nota de alcance de E1 (L18) y a la nota de entrada de E2 (L16); las fuentes se nombran, pero sin par autor-año en las afirmaciones centrales. El criterio `V5.citation_weight.master` se lee: «Load-bearing claims cite source + author named in body at first mention».

El único autor académico nombrado, Akerlof, aparece dos veces y en contextos de enumeración: como «Asimetría de información (Akerlof)» en la columna «Aporte metodológico» de la tabla de §17 (L793) y como «asimetría de información (Akerlof), selección adversa, riesgo moral» en el paso 3 de §19 (L837). En §20 (L861) los mismos conceptos reaparecen sin el nombre. No hay párrafo propio que discuta el trabajo, ni menciones posteriores que lo vinculen a los resultados de §22, §34 o §59. Las fuentes institucionales sí se nombran con precisión operativa —DfT/DVLA en L814, ONEI en L1347, TRMI de elTOQUE en L898— pero como fuentes de datos, sin atribución académica.

— polarity: negative · confidence: high · related: [[#C001]], [[#C003]], [[#C008]], [[#C012]] · criteria: V5.citation_weight.master

### F-V5-004 — Obras importantes ausentes — 8 de 8 de la lista de E2 y 22 de 23 del top-5 por clúster

La lista «Likely missing important works» de E2 (L490–530) contiene ocho entradas; las ocho están ausentes del documento. Metadatos verificados en vivo en OpenAlex durante esta revisión: Lewis 2011, *American Economic Review*, 342 citas (P002; el registro OpenAlex indexa la versión SSRN de 2010); Gegić et al. 2019, *TEM Journal*, 188 (P014); Krotov et al. 2020, *Communications of the AIS*, 224 (P021); Brown et al. 2025, *Big Data & Society*, 118 (P022); Priestley et al. 2023, *Journal of Data and Information Quality*, 153 (P023); Guerra 2015, *Journal of Transport Geography*, 113 (P033). Las cifras de P004 (Englmaier et al. 2017, 50) y P024 (Hohensinner et al. 2026, 13) proceden del mapa E2.

La relación con afirmaciones y secciones cargadas es directa en cada caso. P002 conecta el marco de Akerlof con la divulgación de defectos y tipo de vendedor que el documento registra en §19 (L848) y con la salvedad de C008. P004 advierte sobre saltos de precio en umbrales de año y cada 10.000 km, frente a la serie `precios_por_anio.csv` de §23 (L898) y los comparables por modelo ±2 años de §19 (L849). P014 es el paralelo metodológico de scraping más modelado de precios que el informe describe en §8 (L88) y §51 (L1275–1278). P021 y P022 corresponden a la regla operativa de C005 y a §10 (L110–118); P023 a la arquitectura de colas y cuarentena de §16 (L775–783); P033 a la métrica `asequibilidad = precio / salario` de §19 (L849) y §20 (L865); P024 a la distinción entre procedencia y linaje aplicada en los hashes y manifiestos de §54. El criterio `V5.missing_important_work.master` se lee: «Top-5 most-cited of each adjacent cluster expected». Ordenando por citas conocidas, los cinco primeros de cada clúster suman 23 obras distintas; solo P001 está citada y las 22 restantes, ausentes (95,7 %).

— polarity: negative · confidence: high · related: [[#P002]], [[#P004]], [[#P014]], [[#P021]], [[#P022]], [[#P023]], [[#P024]], [[#P033]] · criteria: V5.missing_important_work.master

### F-V5-005 — Ancla teórica fundacional — Akerlof 1970 citado y aplicado de forma consistente en tres secciones

La única obra académica citada por nombre sostiene el marco teórico en tres puntos del documento: como aporte metodológico del estudio PUCE en §17 (L793), dentro del marco general de ocho pasos en §19 (L837) y, sin el nombre del autor pero con los mismos conceptos, en el bloque 3 del marco detallado de §20 (L861). La clasificación de calidad por antigüedad y palabras de defecto de §19 (L848–L849) es la operacionalización de ese marco. La verificación en vivo de OpenAlex confirma los metadatos de P001: Akerlof, 1970, *Quarterly Journal of Economics*, DOI 10.2307/1879431, 32.562 citas y percentil 99–100 según año de publicación. E2 (H3, L544–546) observa que la literatura posterior apoya la relevancia del marco para mercados de usados, aunque no lo valida en un mercado con doble tasa de cambio y parque informal. La elección de un clásico fundacional como ancla, y su reutilización coherente en el marco analítico, aparece bien calibrada en el sentido del criterio `V5.citation_weight.master`.

— polarity: positive · confidence: high · related: [[#P001]], [[#C048]] · criteria: V5.citation_weight.master

### F-V5-006 — Trazabilidad del descubrimiento — 1.542 resultados, 23 útiles y doce fuentes convertidas en requerimientos

§7 (L76–84) documenta tres búsquedas con regla de parada explícita, paginación y conteos de aciertos y fallos por tanda, además de manifiestos con `manifest.jsonl` e `indice.md`. §17 (L787–806) convierte ese corpus en una tabla de doce filas con tres columnas —fuente, aporte metodológico y requerimiento para el proyecto— que va desde el estudio de la PUCE (L793) y el mercado automotriz chileno (L795) hasta repositorios de referencia (L798–804). Los siete requerimientos derivados en L806 y el marco de nueve bloques de §20 (L857–867) se apoyan en esa tabla. El registro es verificable dentro del documento y conserva la procedencia de cada aporte metodológico, aun cuando solo una de esas fuentes coincida con el mapa académico de E2 y el resto sean informes institucionales o repositorios de código.

— polarity: positive · confidence: high · related: [[#C025]], [[#C026]], [[#C029]], [[#C049]]

### F-V5-007 — Convergencia sin citación — la retirada de la depreciación del −5,43 % coincide con el estado de la evidencia de E2

§34 (L1037–1052) reporta una primera ejecución con depreciación de −5,43 % anual (p<0,001), prima premium de +21 % y prima de tier medio de −22 %. §59 (L1377) y §60 (L1385) consignan que la corrida vigente no encuentra pendiente anual significativa tras corregir kilometraje, con p mínimo 0,165, VIF 1,13–1,58 y Kruskal-Wallis p = 1e−05; las cifras anteriores quedan como versión intermedia. E2 (H2, L540–542) reúne cuatro trabajos ausentes del documento que apuntan en el mismo sentido: P009 (Du et al. 2026, especificación log-lineal anidada casi idéntica, relación edad–precio no lineal), P011 (Miranda et al. 2026, R² = 0,256, kilometraje p = 0,077, correlación edad–km r = 0,639), P004 (Englmaier et al. 2017, saltos en umbrales de año y 10.000 km) y P013 (Francke y Van de Minne 2020, heterogeneidad no observada). La decisión final del informe coincide con ese estado de la evidencia sin que esos trabajos se mencionen en el texto; la coincidencia es de resultado, no de engagement bibliográfico.

— polarity: neutral · confidence: high · related: [[#C009]], [[#C011]], [[#P009]], [[#P011]], [[#P013]]

### F-V5-008 — Alcance de la verificación externa — WebSearch 403, OpenAlex disponible y cuatro registros con metadata incompleta

Esta revisión intentó una búsqueda web con la consulta «Lewis 2011 Asymmetric Information Adverse Selection Online Disclosure eBay Motors American Economic Review» y obtuvo HTTP 403, coherente con los ocho intentos fallidos registrados por E2 (L558); Semantic Scholar también devolvió 403 en el único intento de E2 (L560). La verificación bibliográfica se apoyó en OpenAlex, que respondió en vivo: W2156109180 (Akerlof 1970, 32.562 citas) y siete registros más consultados en esta revisión —P002, P014, P021, P023, P033, P022 y P009— con título, año, revista, DOI y conteo de citas. E2 documenta 92 registros de OpenAlex a partir de 18 consultas, 9 de arXiv y 3 de Crossref (L559–563). Cuatro entradas del mapa conservan límites de metadata declarados: resumen no indexado en P010 y conteos de citas no verificables en P018, P019 y P020 (L565). Las cifras y años empleados en los hallazgos anteriores proceden de esas respuestas en vivo o, en su defecto, se atribuyen explícitamente al mapa E2.

— polarity: neutral · confidence: high · related: [[#P010]], [[#P018]], [[#P019]], [[#P020]]


## §6 — v6-reproducibility


# V6 — Reproducibilidad (nivel master / maestría)

## Resumen

- El inventario de E3 se produjo sin clon local (`repo_clone_status: not-attempted`); esta pasada V6 sí dispuso de un checkout en `~/Proyectos/El precio de moverse en Cuba` y verificó `README.md`, `requirements.txt`, `Data/AUTOMATIZACION.md`, los scripts de análisis y los archivos de prueba contra el texto cacheado.
- La infraestructura reproducible declarada en §55 y §61 aparece en disco: README de 105 líneas con quickstart y ejemplos, `requirements.txt` con cotas `>=`, un orquestador `run_all.py` de un solo comando y 17 funciones `test_*` en tres scripts independientes; el criterio `master` de dependencias fijadas a versiones menores y de semillas declaradas no se satisface literalmente.
- Se registran dos desajustes de código a documento con efecto directo sobre la reproducción de cifras: los KPIs del README (772 autos, 2.029 anuncios) difieren de §59 (744 autos, 2.014 anuncios), y la conversión diaria por TRMI descrita en §23 corresponde en el código a un tipo de cambio fijo `FX=930` en `Data/analisis_rentabilidad/config.py:25`.

### F-V6-001 — README sustancial con nombre del proyecto, quickstart ejecutable y ejemplos de uso

`README.md` está presente con 105 líneas: abre con `# El precio de moverse en Cuba` (`README.md:1`), declara ubicación y repositorio (`README.md:5`), y contiene una sección `## Quickstart` (`README.md:15`) con tres comandos encadenados —creación de `Auxiliares/.venv-py`, `pip install -r requirements.txt` y ejecución de `Data/analisis_rentabilidad/scripts/run_all.py` (`README.md:19–23`)— seguidos de la lista de salidas esperadas (`README.md:25–33`). Incluye además ejemplos de uso para verificar y ensamblar chunks (`README.md:77–80`) y para construir y servir el sitio MkDocs (`README.md:86–90`). El texto cacheado registra la reescritura en §55, línea 1337: «Se reescribió `README.md` como página de entrada: descripción de una frase, quickstart ejecutable, estructura, tabla de fuentes, configuración, enlaces por tipo de documento y marco legal». El criterio `V6.documentation.master` —«README + dependencies list + brief usage examples»— se satisface en el checkout examinado, a diferencia del inventario de E3, que solo consignó el README a nivel de documento.

— polarity: positive · confidence: high · related: [[#F-V6-009]] · criteria: V6.documentation.master

### F-V6-002 — `requirements.txt` con cotas inferiores, sin fijación a versiones menores

El archivo `requirements.txt` existe con 13 líneas y declara diez dependencias mediante cotas inferiores —`pandas>=2.2`, `numpy>=1.26`, `plotly>=5.18`, `statsmodels>=0.14`, `scipy>=1.11`, `curl_cffi>=0.7`, `tenacity>=8.2`, `trafilatura>=1.6`, `pyarrow>=14.0`, `mkdocs>=1.6`, `mkdocs-material>=9.5` (`requirements.txt:2–12`)— sin cotas superiores ni versiones exactas. Existe también `Auxiliares/herramientas/integraciones/requirements-integraciones.txt`. En paralelo, el informe declara versiones concretas instaladas en §6, línea 70: «patchright 1.64.4, PyPasser 1.1.0, Scrapling 0.5.1, ddddocr 1.6.1, playwright 1.65.2, curl_cffi 0.17.0 [...] onnxruntime 1.32.0, ddgs 9.16.1 y tenacity 9.2.1»; §25 añade geopandas 1.2.0 y shapely 2.2.0, y §34 cita statsmodels 0.15 y pyarrow 26. Estas versiones exactas no se reflejan en el archivo de dependencias, que además difiere en `curl_cffi` (`>=0.7` frente a 0.17.0 declarada) y en `tenacity` (`>=8.2` frente a 9.2.1). No se encuentran `pyproject.toml`, lockfiles ni `Dockerfile` en el árbol. El criterio `V6.environment.master` —«Dependencies pinned to minor versions»— no se cumple en `requirements.txt`; la declaración de versiones queda confinada al texto de §6, §25 y §34 y a la sección «Declared environment» de E3.

— polarity: negative · confidence: high · related: [[#F-V6-001]], [[#F-V6-009]] · criteria: V6.environment.master

### F-V6-003 — Ausencia de semillas aleatorias declaradas, con idempotencia verificada en pruebas

La búsqueda de `semilla`, `seed`, `random_state`, `np.random` y `RandomState` en el texto cacheado devuelve solo dos coincidencias, ambas con sentido de URL de partida: §50, línea 1263, «Script reproducible en `Auxiliares/herramientas/consolidar_repos_autos.py`» y §55, línea 1333, «Las 8 semillas de marketplaces también se descargaron». La misma búsqueda sobre `Data/analisis_rentabilidad/scripts/*.py` no devuelve ninguna coincidencia: los cinco scripts de `01_ingest.py` a `05_benchmark.py` no invocan generadores aleatorios, muestreos ni divisiones entrenamiento/prueba con semilla. En su lugar, la determinación de salidas se apoya en idempotencia declarada y probada: `run_all.py:2` describe el orquestador como «reanudable e idempotente», `Auxiliares/herramientas/test_dashboard.py:60–70` comprueba `test_idempotente()` comparando hashes SHA-256 de tres generaciones consecutivas, y `Auxiliares/herramientas/probar_actualizar_numeros.py:40–46` declara `test_idempotente_en_disco()`. El criterio `V6.determinism.master` —«Seeds declared in code and in document, consistent»— no encuentra semillas que cotejar en ninguno de los dos lugares; la observación es neutra porque el componente central es regresión OLS y agregaciones deterministas.

— polarity: neutral · confidence: high · related: [[#F-V6-005]], [[#F-V6-006]] · criteria: V6.determinism.master

### F-V6-004 — Punto de entrada único documentado y comandos con argumentos

`README.md:19–23` documenta un único comando de reproducción para el análisis (`Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py`), y `run_all.py:12` declara la secuencia `["01_ingest.py", "02_clean.py", "03_eda.py", "04_stats.py", "05_benchmark.py"]`, seguida de `actualizar_numeros.py`, `generar_dashboard.py --solo-si-cambia` y `exportar_parquet_compacto.py` (`run_all.py:23–40`). `Data/analisis_rentabilidad/README.md:21–37` mapea cada etapa a sus tablas y gráficos de salida y da una segunda forma de invocación desde `Auxiliares/`. Los argumentos aparecen documentados en los comandos de reconstrucción `db_chunks.py verify <MANIFEST.json>` y `db_chunks.py assemble <MANIFEST.json> <destino>` (`README.md:78–79`) y en los comandos de MkDocs (`README.md:87–89`). El informe añade banderas por herramienta: `--solo-colas` en §33, línea 939, `--skip-unchanged` en §16, línea 781, y `--max-pages 3` en §66, línea 1437. El criterio `V6.entry_points.master` —«Entry points documented with arguments»— se cubre para las herramientas de chunks y para el orquestador en modo sin argumentos; la presencia de un comando único supera el umbral de este nivel.

— polarity: positive · confidence: high · related: [[#F-V6-001]], [[#F-V6-010]] · criteria: V6.entry_points.master

### F-V6-005 — Diecisiete funciones de prueba presentes en el checkout, no inventariadas por E3

El inventario de E3 cierra su tabla de mapeo con «Tests (`test_*.py`, `*_test.py`, `tests/`) | not located (no test files or test framework named in the document)». El checkout contiene tres scripts ejecutables con un total de 17 funciones `test_*`: `Auxiliares/herramientas/test_dashboard.py` (6 funciones, líneas 22–78, ejecuta 5 en `main()`), `Auxiliares/herramientas/test_parquet_compacto.py` (5 funciones, líneas 21–68) y `Auxiliares/herramientas/probar_actualizar_numeros.py` (6 funciones, líneas 17–60, descubiertas por prefijo en `main():64`). Cada archivo declara su propia línea de ejecución en la docstring —«Ejecutar: python3 Auxiliares/herramientas/test_dashboard.py» (:4), «Ejecutar: Auxiliares/.venv-py/bin/python [...] test_parquet_compacto.py» (:4) y «Ejecutar: python3 [...] probar_actualizar_numeros.py» (:4)—. Son scripts autónomos con `assert` y `main()`, sin `pytest.ini`, `tox.ini`, `setup.cfg` ni directorio `.github/`. `Data/AUTOMATIZACION.md:29` y `:33` nombran dos de ellos como «pruebas» del panel y del actualizador de cifras.

— polarity: positive · confidence: high · related: [[#F-V6-006]], [[#F-V6-009]] · criteria: V6.tests.master

### F-V6-006 — Las pruebas existentes no cubren el componente central del análisis

Las 17 funciones detectadas ejercitan tres artefactos periféricos: la generación del panel HTML (`test_dashboard.py:22–78`), la exportación compacta a Parquet (`test_parquet_compacto.py:21–68`) y el reemplazo de marcadores `<!-- kpi:clave -->` en documentos (`probar_actualizar_numeros.py:17–60`). Ningún archivo importa o invoca `Data/analisis_rentabilidad/scripts/01_ingest.py` … `05_benchmark.py`, ni `Auxiliares/herramientas/scrape_revolico_pipeline.py` o `limpiar_revolico.py`. En consecuencia no hay prueba de regresión para la deduplicación de 814 filas a 744 autos (§51, línea 1275; [[#C064]]), para los totales de 2.014 anuncios limpios (§58, línea 1367; [[#C010]]), ni para los coeficientes de −5,43 % anual y su posterior retirada (§34 y §59; [[#C009]], [[#C011]]). El criterio `V6.tests.master` —«At least smoke tests of the central component»— encuentra pruebas del entorno de publicación y del exportador, pero no del pipeline de rentabilidad ni del pipeline de limpieza que producen las cifras cargadas del informe.

— polarity: negative · confidence: high · related: [[#C009]], [[#C010]], [[#C011]], [[#C064]], [[#F-V6-005]] · criteria: V6.tests.master

### F-V6-007 — Divergencia de KPIs entre el informe cacheado y el README regenerado

§59, línea 1375, fija el relato final en «**744 autos únicos**, **2.014 anuncios limpios** (1.323 locales y 691 de importación), mediana local de **21.000 USD**, kilometraje mediano de **44.125 km**», cifra repetida en §58, línea 1367 y resumida en [[#C010]]. El README vigente declara en cambio «**<!-- kpi:autos_revolico -->772 autos únicos** de Revolico, **<!-- kpi:anuncios_marketplaces -->2.232 anuncios** de 8 marketplaces» (`README.md:3`), «10.177 anuncios, 772 autos» (:10) y «**Resultado esperado:** 2.029 anuncios limpios (1.338 locales + 691 de importación)» (:33). El propio `Auxiliares/herramientas/probar_actualizar_numeros.py:23–24` codifica la transición: el texto de prueba pasa de `744 autos` a `772 autos`, y `actualizar_numeros.py` reescribe los marcadores al terminar `run_all.py` (`README.md:31–33`; `Data/AUTOMATIZACION.md:33`). El desajuste impide obtener del texto cacheado los números que el pipeline actual produce, y afecta a [[#C010]], [[#C032]], [[#C066]] y a la tabla de fuentes de `README.md:56–62`.

— polarity: negative · confidence: high · related: [[#C010]], [[#C032]], [[#C066]], [[#F-V6-004]] · criteria: V6.documentation.master

### F-V6-008 — Conversión por TRMI diaria descrita en §23 frente a tipo de cambio fijo en el código

§23, línea 898, describe: «la conversión usa `precio_USD × TRMI elTOQUE` del día del anuncio (columna `Mediana` de `Anexos/Investigacion Cambios/trmi_USD.csv`)», y la misma línea 900 reporta una serie donde la TRMI «pasó de 680 CUP/USD (09/07/2026) a 920 (16-17/11/2026)» ([[#C056]], [[#C058]]). El checkout muestra otro mecanismo: `Data/analisis_rentabilidad/config.py:22–26` fija `FX = {"USD": 1.0, "CUP": 1 / 930.0, "EUR": 1000.0 / 930.0, "MLC": 845.35 / 930.0}` con `FX_NOTE = "TRMI elTOQUE 18/11/2026: USD 930 CUP..."`, y `01_ingest.py:398` convierte cada precio con `cfg.to_usd(p, c)` —función definida en `config.py:102–110`— sin leer `trmi_USD.csv`. La búsqueda de `trmi`, `FX`, `to_usd`, `930` y `Mediana` en los cinco scripts de análisis devuelve esa única coincidencia. `README.md:64` y `Data/analisis_rentabilidad/README.md:41` reproducen el valor fijo 930 CUP/USD, y `Data/AUTOMATIZACION.md:17–18` registra «Evita el `FX=930` clavado en `config.py`» como trabajo de la fase siguiente. La afirmación de conversión diaria de §23 no se reproduce desde el pipeline vigente.

— polarity: negative · confidence: high · related: [[#C056]], [[#C058]], [[#F-V6-007]] · criteria: V6.data_availability.master

### F-V6-009 — E3 registró el repositorio como no clonado; V6 operó sobre un checkout local

El frontmatter de E3 consigna `repo_url: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba` y `repo_clone_status: not-attempted`, y el cuerpo abre con «Repository: not-declared / not-cloned (no local `repo_path` was supplied for this extraction; §40 declares the remote repository [...], reproduced in frontmatter but not cloned or verified here). All entries below are document-level observations only» (`informe-tecnico-2026-11-27.e3-artifacts.md:6–13`). En esta pasada V6 el checkout local `~/Proyectos/El precio de moverse en Cuba` estuvo disponible y se inspeccionaron `README.md`, `requirements.txt`, `Data/AUTOMATIZACION.md`, `Data/analisis_rentabilidad/config.py`, los cinco scripts de `run_all.py`, tres scripts de prueba y el estado de seguimiento de Git. El criterio de nivel `master` presupone que los puntos de entrada, dependencias y rutas de datos constan en el repositorio; la verificación de E3 no pudo realizarse contra esos archivos y varias de sus entradas —tests, figuras, archivo SQLite— quedaron registradas como «Found in repo: no (no local clone supplied)» y son reinterpretadas en [[#F-V6-005]], [[#F-V6-010]] y [[#F-V6-015]].

— polarity: neutral · confidence: high · related: [[#F-V6-001]], [[#F-V6-005]], [[#F-V6-010]], [[#F-V6-015]]

### F-V6-010 — Base de Revolico no versionada como archivo único; chunks y LFS como forma de acceso

E3 registra como artifact ausente el «Full Revolico SQLite file in the main branch», citando §14, línea 752 —«La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**»— y §54, línea 1321, donde «`main` queda intacto hasta decidir su sustitución». En el checkout, `Data/Revolico/revolico.sqlite` y `pipeline.sqlite` existen en el árbol de trabajo, pero `git check-ignore` los resolve a `.gitignore:34` y `git ls-files --error-unmatch` devuelve código 1: no están versionados. La forma declarada de acceso son los manifiestos `Data/Revolico/chunks/MANIFEST.json` (82 fragmentos de 10 MB, §54) y `Data/Revolico/pipeline_chunks/MANIFEST.json` (52 fragmentos, `README.md:73`), con hashes SHA-256; `README.md:75–80` documenta `db_chunks.py verify` y `db_chunks.py assemble`. `Data/AUTOMATIZACION.md:41–42` describe el ledger LFS y el empuje del ref solo sin pendientes, y :81 lo deja como tarea de la fase siguiente. El criterio `V6.data_availability.master` —«datasets named + access path documented»— se satisface mediante los manifiestos, no mediante un archivo canónico rastreable en el historial.

— polarity: neutral · confidence: high · related: [[#C037]], [[#C070]], [[#F-V6-004]] · criteria: V6.data_availability.master

### F-V6-011 — Series oficiales de parque automotor y matriculaciones ausentes de los anuarios descargados

E3 lista como artifact ausente las «Official Cuban vehicle-fleet and registration series». §56, línea 1347, declara: «**No hay series de parque automotor ni de matriculaciones**, por lo que esa laguna signalada en `NECESIDADES.md` no se resuelve con los anuarios; la corrección quedó registrada» ([[#C012]]), a pesar de que §53, línea 1309, describe la descarga completa de los 12 anuarios del ONEI (2014–2025). El inventario de E3 observa que `series_oficiales.csv` contiene series de transporte y seguridad vial, sin parque ni matriculaciones, y que §52 había presentado el capítulo 13 del ONEI como fuente que cubriría la laguna. La fuente está nombrada y su ruta documentada, pero la variable requerida por el marco de asequibilidad (§17, línea 806; [[#C049]]) no existe entre los datos descargados.

— polarity: negative · confidence: high · related: [[#C012]], [[#C049]] · criteria: V6.data_availability.master

### F-V6-012 — Conjunto VAHAN (India) nombrado pero no accesible desde el entorno

E3 incluye «VAHAN (India) dataset» entre los artifacts ausentes. §18, línea 816, registra «No accesible desde este entorno (error de transporte)» para una fuente oficial del MoRTH de la que el repositorio documenta «12 exportaciones mensuales 2025» ([[#C051]]). El inventario de E3 la clasifica con `Publicly accessible: no` y observa que solo se dispuso del manifiesto de verificación del propio repositorio. La fuente aparece nombrada como benchmark de matriculaciones por fabricante y combustible, sin ruta de acceso utilizable en este entorno.

— polarity: negative · confidence: high · related: [[#C051]] · criteria: V6.data_availability.master

### F-V6-013 — Endpoint vivo del BCC declarado como URL pero no recuperable

E3 registra «BCC live exchange-rate endpoint» como artifact ausente. §52 declara `https://api.bc.gob.cu/v1/tasas-de-cambio/activas` como API diaria de tasas activas, mientras §18, línea 815–816, anota «No accesible en vivo desde este entorno» ([[#C051]]). El inventario de E3 marca `Publicly accessible: no` y señala que la tasa oficial se cita de forma indirecta en `Data/investigacion-mercado-automotor-cuba.md` y en la Resolución 102/2026; §55, línea 1333, añade que elTOQUE tampoco respondió en la auditoría final. `README.md:64` documenta el uso de la TRMI informal de elTOQUE de 18/11/2026 en lugar del endpoint oficial. La ruta de acceso está declarada como URL, con disponibilidad observacional ausente en este entorno.

— polarity: negative · confidence: high · related: [[#C051]], [[#C056]], [[#F-V6-008]] · criteria: V6.data_availability.master

### F-V6-014 — Corpus completo de gacetas ubicado fuera del árbol del proyecto

E3 incluye «Full gazette corpus» entre los artifacts ausentes, con cita de §10: «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe», y de §67, que sitúa las leyes en `~/Utilidades/Leyes` tras el paso de optimización de espacio. Solo se nombran Decreto 163/2026 y las resoluciones 104, 17, 52, 171–175, 340 y 102/2026 ([[#C003]], [[#C016]]). El índice de referencia y los documentos subyacentes residen fuera del proyecto, de modo que las afirmaciones normativas no se apoyan en archivos inventariables dentro del repositorio.

— polarity: negative · confidence: high · related: [[#C003]], [[#C016]] · criteria: V6.data_availability.master

### F-V6-015 — Figuras del informe sí presentes en el checkout, aunque no embebidas en el texto cacheado

E3 listó «Rendered figures for the descriptive and profitability analyses» como artifact no localizado, con «Found in repo: no (no local clone supplied; paths named in document only)», y su sección de figuras marca «Rendered in document: no» para cada entrada. El checkout contradice la primera parte: `Data/analisis/graficos/` contiene los ocho PNG nombrados en §23, línea 901 (`01_histograma_precios.png` … `08_cobertura.png`), y `docs/graficos/` contiene seis HTML de Plotly (`01_precios.html` … `06_edad_precio.html`), copias descritas en §61, línea 1395. La caché textual en cambio no incrusta ninguna imagen y §59, línea 1377, se limita a «un **apéndice visual** con cinco cuadros y seis gráficos reales; el texto solo deja referencias discretas entre paréntesis». La entrada de E3 queda así resuelta en el plano de disco y pendiente solo en el plano del texto auditado.

— polarity: neutral · confidence: high · related: [[#F-V6-009]] · criteria: V6.documentation.master

### F-V6-016 — Daemon Docker no disponible para la ruta de google-maps-scraper

E3 recoge «Docker daemon for the Google Maps scraper» como artifact ausente, citando §36: «el daemon Docker no arranca sin root en este entorno (`dockerd needs to be started with root privileges`)». La misma entrada observa que §6 sí reporta FlareSolverr 3.5.2 funcionando en Docker en `http://127.0.0.1:8191/` y que la ruta `google-maps-scraper` fue descartada. El entorno presentado en la declaración de E3 contiene por tanto un servicio contenedorizado operativo y un daemon inaccesible para otra herramienta; la segunda ruta no forma parte de los componentes reproducibles del checkout.

— polarity: negative · confidence: high · related: [[#C024]] · criteria: V6.environment.master

### F-V6-017 — Especificaciones estructuradas de vehículo y precios transados ausentes de los datos

E3 consigna «Structured vehicle specifications and real transaction prices» entre los artifacts ausentes. §24, línea 907, declara que los 6.334 anuncios conservan `meta_json`, `ad_json` y `apollo_full`, pero «**No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**» ([[#C059]]); §22, línea 890, cuantifica la cobertura derivada por regex en marca 68,4 %, año 63,5 % y km 6,2 %. §20 enumera «precios de transacción reales» y «montos de costos ocultos» entre necesidades pendientes. En `config.py:31–32` el umbral de precio válido es `PRICE_MIN_USD = 200`, distinto de los 500 USD declarados en §22, línea 890 ([[#C053]]). La combinación de campos derivados, cobertura parcial y umbral distinto condiciona la réplica de las estimaciones hedónicas de [[#C009]] y [[#C011]] a partir de los datos publicados.

— polarity: negative · confidence: high · related: [[#C009]], [[#C011]], [[#C053]], [[#C059]] · criteria: V6.data_availability.master

### F-V6-018 — `Copias/` excluidas del informe pero citadas como insumo metodológico

E3 incluye «`Copias/` reference repositories» entre los artifacts ausentes. §3 declara «`Copias/` no se registra en este informe por decisión explícita», mientras §17 cita código de `Copias/AutosxCuba/code/{unir_todo_final,modelo_predictivo,generar_graficos}.py` y §50, línea 1263, describe la tabla `provenancia` construida a partir de repositorios externos. `README.md:48–52` confirma que `Auxiliares/Repositorios Referencias/` y `Copias/` se conservan en disco pero quedan excluidos de Git. La procedencia metodológica de esas funciones y tablas queda documentada por mención, sin que los archivos citados formen parte del inventario versionado.

— polarity: neutral · confidence: high · related: [[#C048]], [[#C063]] · criteria: V6.data_availability.master

### F-V6-019 — Fuentes con ruta, URL, checksums y licencia declarados

Varias entradas del inventario de E3 cumplen el umbral `master` de «datasets named + access path documented». Los 12 anuarios del ONEI están en `Data/fuentes-oficiales/ONEI/` con URL, tamaño y SHA-256 por archivo en el `INDICE.md` de cada año (§53, líneas 1309–1311); `README.md:44` y `:96` señalan la ruta y el índice. La serie DfT/DVLA se cita en §18, línea 814, con URL de `gov.uk`, fecha de actualización 23/09/2026 y licencia «Open Government Licence» ([[#C050]]). La geolocalización de 137 gasolineras se apoya en Overpass/OSM en `Data/mapas/gasolineras.csv` (§41), marcada como públicamente accesible por E3. Los chunks de `revolico.sqlite` y `pipeline.sqlite` publican `source_sha256`, offsets y generador en sus manifiestos (`Data/AUTOMATIZACION.md:62`). El criterio `V6.data_availability.master` se satisface para este conjunto, con las excepciones registradas en [[#F-V6-012]], [[#F-V6-013]] y [[#F-V6-014]].

— polarity: positive · confidence: high · related: [[#C050]], [[#F-V6-010]] · criteria: V6.data_availability.master


## §7 — v7-writing


# V7 — Writing and AI patterns (findings)

Resumen (tres líneas):
- El corpus es un informe técnico bilingüe de 1.462 líneas: dos partes paralelas (§1–12), 55 secciones fechadas (§14–68) y un registro de altas generado por script (§13); la prosa se apoya en cifras, rutas y enumeraciones antes que en metadiscurso.
- Los patrones de mayor frecuencia son estructurales —paralelismo ES/EN, apertura «Se + verbo» (51 líneas), bloques «EN.» con participio inicial (53), metaconceptos «análisis» (37) y «marco» (20)—; los ítems estrictos de Romero §13 aparecen en densidad baja y se concentran en dos bloques.
- La densidad se califica como alta en §17–21 y §59–63 y como media en el resto de la prosa; el texto cacheado no contiene declaración de uso de IA, de modo que el contraste queda consignado para V9.

Alcance. Las cifras se obtuvieron por conteo sobre el texto cacheado; «palabra» incluye identificadores y rutas. El §13 (L270–748) se excluye del denominador de densidades por ser un registro automático de tabla, y se inventaría en F-V7-016. Winston, Pinker y Romero §13 se emplean como rótulos de las róbricas aplicadas. El artefacto se limita a describir patrones y densidades.

### F-V7-001 — Paralelismo ES/EN en 54 de 55 secciones y en las Partes I/II

El encabezado declara «Idioma / Language: español e inglés / Spanish and English» (L8). Las Partes I y II repiten íntegramente §1–12 (L14–137 y L143–268). En el bloque §14–68, 54 de 55 secciones llevan un párrafo inglés: 53 con la etiqueta «**EN.**» (§15–39 y §41–68) y §14 con un párrafo inglés sin etiqueta (L754); §40 carece de paralelo. La duplicación opera a nivel de sección, no como glosa puntual: en §18, la «**Conclusión:**» de L827 se enuncia de nuevo en L829, y en §20 el cierre de L873 reitera los nueve bloques de L857–L867. Bajo Winston (structure-of-prose), esta es la característica estructural dominante del documento.

— polarity: neutral · confidence: high · related: [[#F-V7-003]]

### F-V7-002 — Apertura «Se + verbo» en 51 líneas y primera persona aislada

Cincuenta y una líneas comienzan con «Se» seguido de verbo en pretérito, y la construcción «se + verbo» aparece 133 veces en total. La distribución cubre casi todo el rango narrativo: §5 (L60, L62, L64), §29 (L956), §30 (L973, L975), §50 (L1259, L1261, L1263), §55 (L1333, L1335, L1337, L1339), §59 (L1375, L1377) y §66 (L1437, L1439). La voz activa en primera persona se restringe a cuatro pasajes: §34 «Creé `Data/analisis_rentabilidad/`» (L1014) e «Instalé además `statsmodels 0.15`» (L1035), §35 «Descargué tres APKs» (L1064) y §38 «Creé `Auxiliares/herramientas/reporte_progreso.py`» (L1108). Los paralelos ingleses emplean pasiva («was created», «were cloned», «was designed») o participio inicial. Winston sitúa la oración de apertura como oración temática: aquí esa función la cumple de modo regular la construcción impersonal.

— polarity: neutral · confidence: high · related: [[#F-V7-003]]

### F-V7-003 — Bloques «EN.» con participio inicial y función de cierre-resumen (53)

De los 53 bloques etiquetados «**EN.**», la mayoría se abre con un participio pasado seguido de objeto y complemento: «Built a scalable analysis skeleton» (L1058), «Rewrote the findings section» (L1212), «Built a MkDocs Material site» (L1397), «Activated five unattended timers» (L1431), «Audited 15 web sources» (L1341), «Split the 811 MiB Revolico database» (L1327). Dos variantes usan sintagma nominal: «Initial descriptive analysis: 323 cars, 248 valid USD prices» (L892) y «Map libraries installed, systemd auto-restart added» (L920). Cada bloque reemite en forma condensada el resultado del párrafo español precedente: es una glosa sistemática posterior a la exposición, con la regularidad de Romero §13 Don't 8 a escala de sección. Su carácter es declarado por el encabezado bilingüe (L8), por lo que se registra como patrón estructural y no como una ocurrencia aislada.

— polarity: neutral · confidence: high · related: [[#F-V7-001]], [[#F-V7-009]]

### F-V7-004 — Metaconceptos «análisis» (37) y «marco» (20) concentrados en §17–21

El recuento global sobre el texto cacheado da «análisis» 37, «estructura» 22, «marco» 20, «procesamiento» 6, «implement-» 6, «señal» 5, «arquitectura» 5, «proceso» 2, «evaluación» 1 y «consideración» 0. La concentración más alta está en §17–21 (1.671 palabras): «análisis» 14 y «marco» 9, unas 13,8 ocurrencias por 1.000 palabras. Las róbricas nominales se encadenan: «Marco general (8 pasos, derivado de los trabajos revisados)» (L833), «**Conclusión:**» (L827), «El marco operativo completo consta de nueve bloques» (L857), «**Marco teórico:**» (L861), «**Marco normativo:**» (L862), «**Arquitectura de datos:**» (L863). En §10 y §12, «marco» reaparece en «norma marco» (L56), «marco legal» (L112) y «marco regulatorio» (L134). Bajo Pinker (metaconcepts and zombie nouns), estos sustantivos abstractionan la acción que las cifras vecinas concretan. Romero §13 Don't 4, en su forma estricta («landscapes/paradigms/ecosystems/transformations»), no registra ocurrencias: no aparecen «ecosistema», «paradigma» ni «transformación».

— polarity: neutral · confidence: high · related: [[#F-V7-005]], [[#F-V7-010]]

### F-V7-005 — Siglas no desplegadas en primera aparición (Pinker, curse of knowledge)

Varios términos técnicos se introducen ya abreviados y no se despliegan en el documento: «TRMI» (L898, L1293, L1385), «VIF» (L1023, L1385), «OLS» (L1052, L1058), «IQR» (L890, L892), «MLC» (L800, L846, L860), «GQL» (L763), «MTProto» (L763, L946), «WAHA» (L763, L765), «SHAP» (L801, L865), «EDA» (L801), «vqd» (L124) y «NFC» (L1357). La lista de organismos de L64 —«MINCEX, MINCIN, MITRANS, CEMA, MFP, ONAT, Aduana General, BCC, MININT, MINJUS, MEP, MINREX y MINSAP»— sola no expande ninguna sigla; «BCC (Banco Central de Cuba)» aparece recién en L816 y L1293, y «DDG» en L124 depende de «DuckDuckGo» en L60. Pinker clasifica este patrón como curse of knowledge: el texto supone el vocabulario ya conocido en el primer uso.

— polarity: negative · confidence: high · related: [[#F-V7-004]]

### F-V7-006 — Negaciones de salvaguarda «no se…/sin…» — 15 instancias

El texto registra 151 ocurrencias de «no» y «sin», de las cuales un subconjunto se reitera como declaración de lo que no se hizo: «No se eluden mecanismos anti-automatización» (L116), «no se falsificó su contenido» (L127), «no se descarta información» (L783), «sin escribir nunca `autos`/`revision`» (L924), «no hay claves estructuradas» (L907), «no hay descarga de anuncios, ni clasificación definitiva, ni inserción» (L994), «LFS no lo sustituye» (L975), «no se modificó `revolico.sqlite`» (L1263), «sin borrar archivos. Ninguna modificó las bases fuente» (L1273), «no se hizo `pull` para no sobrescribir trabajo» (L1335), «sin modificar las bases» (L1357), «las filas existentes se migraron sin borrarse» (L1403), «sin `git push`» (L1437) y «Las leyes y las herramientas de scraping **no se borraron**» (L1447). En la mayoría hay distinción metodológica efectiva, de modo que Romero §13 Don't 2 («not just X, but Y» sin trabajo para la negación) cuenta 0–2 instancias: las más cercanas son «La app **no usa una API privada**: hace scraping del canal público» (L1066) y «es **inferencia de diseño, no medición**» (L1413). La negación funciona aquí principalmente como constancia de límites, no como énfasis retórico.

— polarity: neutral · confidence: high · related: [[#C005]], [[#C008]]

### F-V7-007 — Romero §13 Don't 3 — triadas con cola larga: 2–3 instancias

Se identifican dos o tres construcciones de tres elementos con tercer término marcadamente más largo o abstracto: «sin nombres, teléfonos ni información personal de anunciantes» (L117); «values, concerns and constraints (budget, reliability, fuel use, maintenance, resale value, spare-part availability, etc.)» (L145); «sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`» (L763). Un caso límite es «requiere dedup, verificación y sesgo declarado» (L822), donde la cola no es sustancialmente más larga, y la enumeración de siete métricas de L1375 —«**744 autos únicos**», «**2.014 anuncios limpios**», «mediana local de **21.000 USD**», «kilometraje mediano de **44.125 km**», «50 marcas, 100 grupos comparables y 81 anomalías»— es una lista de resultados, no una triada. La densidad del patrón es baja en relación con el volumen total de prosa.

— polarity: neutral · confidence: medium · related: [[#F-V7-008]]

### F-V7-008 — Romero §13 Don't 5 — adjetivos valorativos sin ancla en §52 y §63

Los equivalentes de «significant/important/considerable/notable/substantial» como adjetivos sueltos no aparecen: «importante», «notable», «considerable» y «sustancial» registran 0 ocurrencias, y «significativ-» 2 (L1052 y L1385), ambas con ancla estadística explícita («p<0,001»; «p mínimo 0,165»). Los modificadores no numéricos se concentran en dos zonas: §52 «Las cinco más valiosas son» (L1291) y §41 «Hallazgo relevante:» (L1156), seguidos de datos concretos; y §63 «El contenido es sólido, pero antes de la revisión tenía fricción inicial (metadatos antes de la promesa), un H2 genérico, el dato fuerte enterrado y ninguna llamada a la acción» (L1411), con cuatro adjetivos valorativos seguidos. Se suman «con honestidad» (L1377), «a statistically honest depreciation narrative» (L1379), «antiguo e inservible» (L1447) y «bibliotecas quizá innecesarias» (L1455).

— polarity: neutral · confidence: high · related: [[#F-V7-014]]

### F-V7-009 — Romero §13 Don't 8 — reescrituras descritas, no mostradas (§43–47, §59)

Varias secciones informan de una reescritura y exponen su resultado como enunciado, sin incorporar el texto reescrito: «Se transformó la sección **Lo que encontramos** de una tabla de datos en una narrativa de hallazgos» (L1210), con cierre explicitado —«El cierre deja la idea central: un mercado pequeño pero con estructura suficiente para dejar de improvisar»—; «Se transformó **La curva de valor** en una narrativa sobre el envejecimiento desigual del parque» y «la idea de la marca como "seguro de valor"» (L1226); «Se añadió una apertura que hace explícita la división del mercado en dos capas» (L1218). En §59, «los diez anuncios nuevos de iTENCEL entraron en la historia sin convertirla en una explicación técnica» (L1375) y el apéndice «solo deja referencias discretas entre paréntesis» (L1377). §63 califica las intervenciones como «correcciones quirúrgicas» (L1411). El inventario de artefactos consigna que las figuras se nombran pero no se incrustan en el texto cacheado, de modo que la conclusión se da antes que la evidencia mostrada.

— polarity: neutral · confidence: medium · related: [[#C013]], [[#F-V7-001]], [[#F-V7-003]]

### F-V7-010 — Anclaje concreto: cifras, rutas e IDs en cada sección (Pinker)

El síntoma lack of concrete examples no se observa: las definiciones van seguidas de instancias y las afirmaciones de resultados llevan unidad y magnitud. §7 define «útil = primera aparición de un trabajo investigativo automotriz» (L76) y lo aplica en la tabla de L78–82; §9 desglosa 11 tiendas con filas y precios (L94–106); §51 identifica cuatro anuncios por ID (L1275) y enumera cinco mejoras con rutas y recuentos (L1275–L1279); §58 nombra los diez anuncios nuevos de iTENCEL (L1365); §48 lista marcas premium y no premium (L1236–L1237); §41 registra 137 gasolineras, 12 estaciones de carga y 18 observaciones fechadas (L1150–L1154). Esta densidad de anclajes es la contrapartida de los metaconceptos de F-V7-004.

— polarity: positive · confidence: high · related: [[#C010]], [[#F-V7-004]]

### F-V7-011 — Winston: títulos instructivos y fechados; cuatro excepciones genéricas

Los 55 encabezados numerados de §14–68 llevan año entre paréntesis y un nombre que designa la operación: «Sincronización automática de Revolico» (§14, L750), «Esqueleto de análisis de rentabilidad inspirado en Egyptian-Used-Cars» (§34, L1012), «Definición de marcas premium y no premium» (§48, L1232), «Automatización operativa y coste de red» (§65, L1427). Cuatro títulos permanecen en un nivel genérico: «Continuación del scrapeo y presentación narrativa» (§39, L1121), «Mejoras del proyecto» (§51, L1271), «Ampliación de fuentes de datos» (§52, L1287) y «Peso en GitHub y mapa de espacio» (§68, L1453). Bajo Winston (section titles: instructive vs vacuous), la proporción de títulos instructivos es alta.

— polarity: positive · confidence: high · related: []

### F-V7-012 — Winston: listas y tablas en función enumerativa, no sustitutiva de prosa

El documento emplea listas para enumeraciones, requerimientos y alternativas: «Requerimientos derivados» con siete ítems (L806), «Marco general (8 pasos)» (L835–L842), los nueve bloques del marco analítico (L859–L867), las cinco mejoras de §51 (L1275–L1279) y las cinco fuentes más valiosas de §52 (L1293–L1297). Las tablas —14 sin numerar según el inventario de artefactos— sostienen recuentos por fase, búsqueda, tienda, fuente y problema (L24–34, L78–82, L94–106, L122–129, L812–825). No se detecta una lista que reemplace un argumento continuo; el movimiento inverso se describe en §45, donde una tabla se convierte en narrativa (L1210).

— polarity: neutral · confidence: high · related: [[#F-V7-010]]

### F-V7-013 — Pinker: 0 instancias de metadiscurso y de professional narcissism

No aparecen las fórmulas «this section discusses», «we will see that» ni «as discussed above», y tampoco «research in recent years» o «the field has shown». La señalización interna se hace con etiquetas nominales en negrita —«**Requerimientos derivados:**» (L806), «**Conclusión:**» (L827), «**Lo que ya existe:**» (L869), «**Lo que falta por conseguir:**» (L871), «**Advertencia:**» (L977), «**Hallazgo relevante:**» (L1156), «**Hallazgo normativo crítico:**» (L1299)— y con remisiones punctuales: «El marco detallado de la sección 20 se mantiene» (L882), «El detalle y la priorización están en `NECESIDADES.md`» (L1056), «El detalle está en `Data/auditoria-fuentes-2026-11-23.md`» (L1333). Bajo Pinker, el metadiscurso y el professional narcissism figuran en densidad nula.

— polarity: neutral · confidence: high · related: []

### F-V7-014 — Pinker: hedging-as-tic casi ausente — «quizá» 1, «aproximad-» 1

La cuenta de atenuadores es «quizá» 1 —«bibliotecas quizá innecesarias (66 MB de DuckDB)» (L1455)—, «aproximad-» 1 —«marcadas como aproximadas al centro de La Habana» (L1175)— y 0 para «relativamente», «somewhat», «perhaps» y «presumably». Las expresiones «se asume que» (L899, L917) y «supuesto» (L917, L921) funcionan como supuestos metodológicos etiquetados: «se asume que son comprables; no se comprueba disponibilidad en tiempo real» (L899) y «se asume que todo el catálogo está disponible salvo que la página indique lo contrario» (L917). «de modo que las tablas y figuras puedan insertarse sin romper la narrativa» (L1377) declara una intención de diseño. La densidad de hedging-as-tic es baja, aproximadamente 0,7 por 1.000 palabras de prosa.

— polarity: neutral · confidence: high · related: [[#F-V7-008]]

### F-V7-015 — Ritmo: cadenas con punto y coma; baja uniformidad de longitud

Varios párrafos se resuelven en una sola oración larga con cadenas de punto y coma: §4 (L56), §5 (L62), §15 «Para obtener más datos del mercado habanero, la ruta más eficiente es Telegram MTProto» (L763), §17 (L806) y §34 (L1052). No se detectan secuencias de cuatro o más oraciones consecutivas de 18–25 palabras: el ritmo alterna esas frases densas con ítems de lista de pocas palabras (L94–106, L1275–L1279) y con los bloques «EN.» condensados. La uniformidad de longitud se califica como baja.

— polarity: neutral · confidence: medium · related: [[#F-V7-003]]

### F-V7-016 — §13: 473 líneas de registro generado por `actualizar_informe.py`

El §13 se presenta como «Registro automático de todo lo que se añade a la carpeta del proyecto. El script `Auxiliares/herramientas/actualizar_informe.py` añade filas debajo del marcador y regenera el PDF» (L272). Las líneas L276–L748 son filas de tabla con valores repetidos: «Añadido al proyecto; pendiente de descripción / Added; description pending», «Carpeta añadida al proyecto / Folder added to the project» y «Actualizado / Updated»; L291 consigna «175 entradas adicionales no listadas / omitted». La secuencia incluye instantáneas sucesivas del mismo archivo con tamaños decrecientes (por ejemplo, `INFORME_TECNICO.md` en L284, L289, L504, L519, L526 y L562). Se trata de una tabla generada por script y se mantiene fuera del denominador de densidades de prosa.

— polarity: neutral · confidence: high · related: []

## AI-pattern density by section

Valores aproximados sobre el texto cacheado. «Metaconcepto/1k» agrega `análisis`, `marco`, `estructura`, `procesamiento`, `proceso`, `señal`, `arquitectura`, `evaluación` e `implement-` en la acepción de Pinker. «Openers» cuenta fórmulas de apertura («Se + verbo», participio en los bloques «EN.», pasiva inglesa); no aparecen «In recent years…» ni «This study demonstrates that…».

| Section | Density | Notes |
|---|---|---|
| §1–3 — Objetivo, estados, carpetas (L14–53) | low | 0–1 hedges/1k; «análisis» 2 en §1; 0 triadas; openers «Se + verbo»; sin bloque EN |
| §4–9 — Fases 1–6 (L54–108) | low | ≈0,5 metaconceptos/1k; 0 triadas largas; 15 openers «Se…»; tablas y listas; 0 atenuadores |
| §10–12 — Marco legal, problemas, conclusiones (L110–137) | medium | «marco» 3; 7 «no/sin»; triada en L117; cierre numerado en L133–137 |
| Parte II §1–12 — Objective…Conclusions (L143–268) | low | voz pasiva y paralelismo con la Parte I; 0 hedges; 0 triadas largas salvo L145 |
| §13 — Registro de altas (L270–748) | n/a | tabla generada por script; 473 líneas; excluida del denominador (F-V7-016) |
| §14–33 — Sincronización, eficiencia, colas, marcos (L750–1008) | medium | 19 openers «Se…»; 18 bloques EN de participio; 13 «no/sin» en §18 (mayoría en tabla) |
| §17–21 — Guía, auditoría y marcos analíticos (L787–884) | high | 14 «análisis» + 9 «marco» en 1.671 palabras (≈13,8/1k); escaleras de 8 y 9 pasos; triada en L848; 5 glosas EN |
| §34–48 — Rentabilidad, APK, mapas, storytelling (L1012–1242) | medium | 4 pasajes en primera persona; 15 bloques EN; d8 en §43–47; «seguro de valor» entre comillas (L1226); 0 hedges |
| §49–58 — Repos, mejoras, fuentes, ONEI, chunks (L1245–1369) | medium | ≈25 «no/sin»; d5 en L1156 y L1291; ≈25 openers «Se…»; densidad alta de cifras y rutas |
| §59–63 — Storytelling final, modelos, sitio, retención (L1373–1415) | high | d8 en §59 y §63; d5 con 4 adjetivos en L1411 y «honestidad» en L1377/1379; «inferencia de diseño, no medición» (L1413) |
| §64–68 — Automatización y espacio (L1419–1457) | low–medium | «quizá» en L1455; «no se borraron» en L1447; 5 bloques EN de participio; 0 triadas |

## Hook para V9

Dos bloques registran `ai-pattern-density: high`: §17–21 (metaconceptos ≈13,8/1k, escaleras de pasos, glosas «EN.» sistemáticas) y §59–63 (adjetivos valorativos y reescrituras descritas, Romero §13 Don't 5 y Don't 8). El texto cacheado no incluye una sección de declaración de uso de IA; el pasaje más cercano es §55 (L1337), donde se consigna que las skills `technical-writing`, `readme-writing`, `diataxis-docs`, `marketing-copy` y `pptx` «quedaron instaladas y activas para redacción y presentación». Ambos extremos quedan consignados para el contraste de V9.


## §8 — v8-bibliography


## Resumen

- El informe no contiene bibliografía numerada ni sección de referencias: las 36 fuentes nominales que sostienen sus afirmaciones aparecen dispersas en tablas y prosa, sin convención autor-año ni identificadores.
- Solo cuatro entradas pudieron confirmarse en fuentes externas (Akerlof 1970; DfT/DVLA; ANFAC; AEADE); las 32 restantes quedan marcadas `(metadata incomplete)` por falta de metadatos mínimos o por fallo de acceso en este entorno.
- Se registra un desajuste de contexto entre la atribución del capítulo 13 del anuario 2025 del ONEI como fuente de «parque automotor» (§52) y la corrección posterior que niega esa serie (§56); no se detectaron entradas duplicadas ni identificadores falsos, porque el documento no declara ninguno.

## Alcance y método

No se recibió un artefacto separado `document_bibliography`. Se tomó como bibliografía efectiva el conjunto de fuentes nominales que el texto usa para apoyar afirmaciones: las tablas de «Fuentes académicas y repositorios revisados» (§17, L791–804), «Auditoría de procedencia» (§18, L812–825), el marco normativo (§4, §10), las «fuentes más valiosas» de §52 (L1293–1297) y las menciones dispersas en §15, §19, §20 y §56. Se excluyeron del cómputo los archivos internos del proyecto que funcionan como artefactos de datos (bases SQLite, CSV y PNG), salvo cuando el propio documento los presenta como fuente metodológica.

Las verificaciones se ejecutaron el 2026-11-27 contra Crossref API, OpenAlex API, páginas de publishers/organismos y resolución de URLs. Los intentos de `WebSearch` devolvieron error de ejecución del proveedor, por lo que las normas cubanas y los trabajos locales no pudieron cotejarse por esa vía. Todo dato no confirmado se marca `(metadata incomplete)`; no se ha asignado ningún DOI, ID de arXiv ni venue que no conste en una fuente verificada.

### Inventario auditado

| # | Fuente nominal | Clase | Resultado externo |
|---:|---|---|---|
| 1 | Akerlof, «The Market for "Lemons"», 1970 | Académica | Verificado (Crossref + OpenAlex) |
| 2 | PDF PUCE en `Hombros/01_PDFs/` | Académica local | `(metadata incomplete)` |
| 3 | «Informe de competencia del mercado automotriz ...» / «Mercado automotriz chileno: un análisis empírico» | Informe | `(metadata incomplete)` |
| 4 | `Hombros/RESUMEN_NUEVAS_BUSQUEDAS.md` | Resumen interno | `(metadata incomplete)` |
| 5 | «Inteligencia De Negocios Aplicada Al Sector Automovilístico» (HTML) | Informe | `(metadata incomplete)` |
| 6 | ANFAC | Gremial | Verificado (sitio institucional) |
| 7 | AEADE | Gremial | Verificado (sitio institucional) |
| 8 | EY | Consultoría | `(metadata incomplete)` |
| 9 | INEGI | Oficial | `(metadata incomplete)` |
| 10 | BBVA Research | Consultoría | `(metadata incomplete)` |
| 11 | COIIM | Gremial | `(metadata incomplete)` |
| 12 | Decreto 163/2026 + Gaceta 65 Ordinaria | Norma | `(metadata incomplete)` |
| 13 | Decreto 119/2024 (derogado) | Norma | `(metadata incomplete)` |
| 14 | Resoluciones 104/17/52/171–175/312/340/102 de 2026 | Normas | `(metadata incomplete)` |
| 15 | Resolución 14 (salarios) | Norma | `(metadata incomplete)` |
| 16 | ONEI, anuarios 2014–2025 y Anuario 2025 cap. 13 | Oficial | `(metadata incomplete)` |
| 17 | DfT / DVLA, vehicle licensing statistics data files | Oficial | Verificado (GOV.UK) |
| 18 | VAHAN (India, MoRTH) | Oficial | `(metadata incomplete)` |
| 19 | BCC, API de tasas activas | Oficial | `(metadata incomplete)` |
| 20 | elTOQUE, TRMI | No oficial | `(metadata incomplete)` |
| 21 | Condiciones de Uso de Revolico (23/09/2026) | Términos de uso | `(metadata incomplete)` |
| 22 | Universidades (PUCE, UPS, UPV, UChile, UNAL, etc.) | Académica | `(metadata incomplete)` |
| 23 | CarDekho (Kaggle) | Dataset | `(metadata incomplete)` |
| 24 | UCI Automobile | Dataset | `(metadata incomplete)` |
| 25 | Datasets sintéticos Zimbabwe/Nigeria | Dataset | `(metadata incomplete)` |
| 26 | `spinny-scraper` | Repositorio | `(metadata incomplete)` |
| 27 | `taso-api` | Repositorio | `(metadata incomplete)` |
| 28 | `AutosxCuba` | Repositorio | `(metadata incomplete)` |
| 29 | `guani-saimc` | Repositorio | `(metadata incomplete)` |
| 30 | `IDSE-DATA-SCIENCE-PROJECT-` | Repositorio | `(metadata incomplete)` |
| 31 | `used-cars-price-prediction` | Repositorio | `(metadata incomplete)` |
| 32 | `Iran-Car-Market-Intelligence` | Repositorio | `(metadata incomplete)` |
| 33 | `uk-automotive-transition` | Repositorio | `(metadata incomplete)` |
| 34 | `vahan-india` | Repositorio | `(metadata incomplete)` |
| 35 | `nz-vehicle-market-tracker` / `zimbabwe-used-vehicle-market-analysis` | Repositorios | `(metadata incomplete)` |
| 36 | Womy / Clasificados.st / TecnoTáctil | Portales | `(metadata incomplete)` |

### F-V8-001 — El documento no constituye una bibliografía verificable en el sentido convencional

La búsqueda de una sección de referencias, de citas numeradas `[N]` y de un patrón autor-año dio resultado negativo en el texto cacheado. E1 ya había consignado que «El documento no emplea citas numeradas tipo `[N]`; por eso `External evidence cited` se marca «— (sin citas numeradas)» y las fuentes nombradas se consignan, cuando procede, en `Notes`», y E2 confirma: «el documento no tiene bibliografía numerada, así que `Cited in document` se determina por mención nominal». La consecuencia bibliográfica es concreta: no hay entradas que puedan cotejarse como unidades completas (autor, título, año, venue, identificador), sino menciones de fuentes repartidas entre tablas de procedencia, rutas de archivo y prosa. El encabezado de la tabla de §17 —«| Fuente | Aporte metodológico | Requerimiento para AutoDecide |» (L791)— ilustra el patrón: la columna «Fuente» admite indistintamente un PDF, un repositorio, una asociación gremial y una norma.

— polarity: negativo · confidence: alta · related: [[#C003]], [[#C048]]

### F-V8-002 — Akerlof (1970): metadatos confirmados en fuentes externas, pero sin entrada en el informe

El documento invoca la obra únicamente por apellido: «**Marco teórico y normativo**: asimetría de información (Akerlof), selección adversa, riesgo moral, regulación vigente» (§19, L837), y en la tabla de §17 atribuye al PDF de la PUCE «Asimetría de información (Akerlof)» (L793). No existe ficha bibliográfica propia: `(metadata incomplete)` en el documento.

La verificación externa sí confirma la obra. La consulta a `https://api.crossref.org/works/10.2307/1879431` devolvió `status: ok` con título «The Market for "Lemons": Quality Uncertainty and the Market Mechanism», autor `George A. Akerlof`, `published-print 1970-08`, contenedor «The Quarterly Journal of Economics», volumen 84, número 3, página 488 y DOI `10.2307/1879431`. La consulta a `https://api.openalex.org/works?search=The%20Market%20for%20Lemons%20Quality%20Uncertainty%20and%20the%20Market%20Mechanism&per-page=1` devolvió el registro `W2156109180` con el mismo DOI, año 1970, autor George A. Akerlof y la misma revista. El DOI y la revista se transcriben aquí porque fueron devueltos por esas dos APIs, no por el documento. El registro incluye además un resumen indexado que contiene solo el índice de secciones («I. Introduction, 488. — II. The model with automobiles as an example, 489. ...»), por lo que la comprobación de contexto se apoya en el título y las palabras clave indexadas (`adverse selection`, `information asymmetry`, `used cars`), no en un abstract sustantivo.

La ausencia de ficha es relevante porque el marco teórico de §19 y §20 apoya la captura de defectos y calidad declarada como requerimiento: la alegación teórica queda mediada por un PDF local sin metadatos (véase F-V8-009).

— polarity: negativo · confidence: alta · related: [[#C048]], [[#C052]]

### F-V8-003 — Corpus normativo cubano citado por número, sin URL oficial ni fecha de acceso verificables

El documento sostiene una afirmación cargada (C003) con normas citadas solo por número: «La norma marco es el **Decreto 163/2026** (Gaceta Oficial No. 65 Ordinaria, 04/08/2026, vigente desde el 11/08/2026), que deroga el Decreto 119/2024» (§4, L56), y «Se cotejaron las resoluciones 104/2026 (MINCEX), 17/2026 (MINCIN), 52/2026 (MITRANS), 171–175/2026 (MFP), 312/2026, derogada por 340/2026 (Aduana) y 102/2026 (BCC)» (L56). Más adelante añade la «**Resolución 14**» como fuente de salarios (§19, L847; §20, L863) y el «**Hallazgo normativo crítico:** la **Resolución 312/2026 de la Aduana General fue derogada por la Resolución 340/2026**» (§52, L1299).

Los dos intentos de búsqueda (`"Decreto 163/2026" Cuba Gaceta Oficial importación vehículos` y una consulta equivalente sobre el estudio PUCE) devolvieron `Unable to search the web`, y el documento no incluye URL de la Gaceta Oficial ni fecha de acceso para ninguna de estas normas; remite a `~/Utilidades/Leyes/gaceta_catalog.json`, un índice local (§10, L118). En consecuencia, las entradas 12–15 del inventario quedan `(metadata incomplete)`: se registra lo que el texto afirma, sin atribuir sede, página de publicación ni identificador externo que no haya sido verificado. La coherencia interna de la cadena de derogaciones (163/2026 → 119/2024; 340/2026 → 312/2026) se conserva tal como aparece en L56, L1299 y L185, pero no ha podido cotejarse con una fuente oficial en este entorno.

— polarity: negativo · confidence: media · related: [[#C003]], [[#C016]], [[#C085]]

### F-V8-004 — ONEI: institución y corpus documentados internamente, pero inaccesibles para verificación externa

La entrada 16 se apoya en un inventario interno detallado: «A partir del índice oficial `http://www.onei.gob.cu/cuba` se recorrieron las 12 páginas de anuarios disponibles (2014–2025) y se descargaron **todos los documentos enlazados**: 111 PDF, 7 RAR y 103 archivos Excel extraídos, unos 311 MB en total. El inventario está en `Data/fuentes-oficiales/ONEI/README.md` y, con URL, tamaño y SHA-256 por archivo, en el `INDICE.md` de cada año» (§53, L1309). El acceso a `http://www.onei.gob.cu/cuba` desde este evaluador devolvió `{"error":{"type":"unknown","message":"Transport error (GET http://www.onei.gob.cu/cuba)"}}`.

No se trata de una obra fantasma: el documento declara manifiestos con URL, tamaño y hash por archivo y E3 confirma la existencia del inventario como observación de nivel de documento. Aun así, la ficha bibliográfica sigue siendo `(metadata incomplete)` porque no hay título formal de la serie, fecha de consulta externa verificable ni resolución del sitio desde el entorno de auditoría. La afirmación de §56 —«Se revisaron los 12 anuarios del ONEI y sus 233 archivos» (L1347)— descansa en ese inventario local, no en una comprobación reproducible aquí.

— polarity: neutro · confidence: alta · related: [[#C069]], [[#C072]]

### F-V8-005 — Desajuste de contexto: el capítulo 13 del Anuario 2025 se cita por «parque automotor» y después se corrige

Existe una inconsistencia entre la fuente invocada y el contenido que se le atribuye. En §52, L1295, el documento escribe: «**ONEI, Anuario Estadístico 2025, capítulo 13**: serie oficial más reciente de transporte y parque automotor, ausente hasta ahora en la base». En §53, L1313, refuerza: «la serie más útil es el capítulo 13 (Transporte y Seguridad Vial), que permite incorporar parque automotor, matriculaciones y accidentes con series oficiales 2014–2025». Sin embargo, §56, L1347, concluye: «**No hay series de parque automotor ni de matriculaciones**, por lo que esa laguna signalada en `NECESIDADES.md` no se resuelve con los anuarios; la corrección quedó registrada». E3 confirma la corrección como hallazgo de ausencia de artefacto.

La entrada ONEI (ítem 16) es, por tanto, citada en dos contextos incompatibles: se la presenta como fuente de una serie que, según la verificación interna posterior, no contiene. El uso que sí resiste el cotejo es el de transporte de pasajeros y seguridad vial (L1347). La atribución de «parque automotor» queda `(metadata incomplete)` en el sentido de contexto, no de existencia de la fuente.

— polarity: negativo · confidence: alta · related: [[#C012]], [[#C069]], [[#C072]]

### F-V8-006 — DfT/DVLA: entrada verificada y concordante con su contexto de uso

La fila de §18, L814, dice: «DfT / DVLA (UK), `gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files` | **Oficial gubernamental** | Verificado en vivo: publicado por Department for Transport + DVLA, actualizado 23/09/2026, Open Government Licence | Repos `uk-automotive-transition`: erste Registrierungen por marca/combustible/trimestre».

La descarga de `https://www.gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files` confirmó todos los elementos: título «Vehicle licensing statistics data files», `From: Department for Transport and Driver and Vehicle Licensing Agency`, `Published: 24 May 2022`, `Last updated: 23 September 2026`, licencia `Open Government Licence v3.0`, y datos de `df_VEH0160_GB`/`df_VEH0160_UK` descritos como «Vehicles registered for the first time by body type, make, generic model and model». Es la única entrada del inventario cuyos tres metadatos declarados (organismo, fecha de actualización y licencia) coinciden literalmente con la fuente externa. El contexto de uso declarado —matriculaciones por marca/combustible/trimestre— es compatible con el esquema de esos ficheros CSV.

— polarity: positivo · confidence: alta · related: [[#C050]]

### F-V8-007 — ANFAC y AEADE: organismos confirmados, informes concretos sin ficha

Las filas L818–L819 del §18 afirman verificación en vivo de «ANFAC (España) | **Gremial** (asociación de fabricantes) | Verificado en vivo: anfac.com, cifras de matriculaciones y parque, informe anual» y «AEADE (Ecuador) | **Gremial** | Verificado en vivo: aeade.net, anuarios y boletines de ventas | Fuente declarada por el estudio PUCE de vehículos usados».

`https://www.anfac.com/` resolvió y expone las secciones «Notas de matriculación», «Informe Anual» y «Parque Vehículos», además de cifras de matriculaciones de octubre de 2026. `https://aeade.net/` resolvió y expone «Estadísticas → Anuarios» y «Boletines de prensa: venta de vehículos». La existencia de ambos organismos y de las categorías de datos citadas queda verificada. No obstante, las entradas siguen siendo incompletas en sentido estricto: no se identifica el informe anual concreto, el año del anuario ni la URL profunda de cada documento. Se registran como verificadas a nivel de organismo y `(metadata incomplete)` a nivel de publicación específica.

— polarity: neutro · confidence: alta

### F-V8-008 — VAHAN, BCC y elTOQUE: fallos de acceso declarados por el documento y reproducidos aquí

Tres fuentes nominales tienen verificación explícitamente frustrada. En §18: «VAHAN (India), declarado por `vahan-india-automotive-market-2025` | **Oficial gubernamental** (MoRTH) | No accesible desde este entorno (error de transporte); el repo documenta 12 exportaciones mensuales 2025 y manifiesto de verificacion» (L815); «BCC (Banco Central de Cuba) | **Oficial gubernamental** | No accesible en vivo desde este entorno» (L816). En §52 se da la URL «`https://api.bc.gob.cu/v1/tasas-de-cambio/activas`» (L1293), y en §55: «14 respondieron HTTP 200 y elTOQUE no respondió desde este entorno» (L1333).

La comprobación de `https://api.bc.gob.cu/v1/tasas-de-cambio/activas` devolvió `{"error":{"type":"unknown","message":"Transport error (GET https://api.bc.gob.cu/v1/tasas-de-cambio/activas)"}}`, reproduciendo lo declarado. No se intentó una URL alternativa para VAHAN ni para elTOQUE porque el documento no las aporta. Las tres entradas (18–20) quedan `(metadata incomplete)`: no son invenciones —el propio texto las etiqueta como no verificadas— pero tampoco pueden atribuirse a una edición, fecha o respuesta concreta. El uso analítico declarado (registros por fabricante/combustible, tasa oficial de referencia y TRMI informal) se conserva como atribución del informe, no como hecho verificado.

— polarity: neutro · confidence: alta · related: [[#C051]], [[#C056]], [[#C068]], [[#C071]]

### F-V8-009 — Estudio de la PUCE: ficha sin autores, año, título completo ni identificador

La entrada 2 se cita con una ruta local y una etiqueta institucional: «`Hombros/01_PDFs/Análisis del mercado de vehículos usados y su comercialización en el__73e1773e.pdf` (PUCE) | Asimetría de información (Akerlof); clasificación de calidad por antigüedad (≤5 años alta, >5 años con defectos); encuesta a 130 comerciantes; medición de costos ocultos y margen de reventa» (§17, L793). E3 la inventaría como «PUCE used-vehicle study survey», también sin autor ni año.

El sufijo `__73e1773e` parece un hash de archivo, no un identificador bibliográfico; el documento no declara autores, año, facultad, serie ni DOI. El intento de búsqueda por el título devolvió `Unable to search the web`, por lo que la ficha queda `(metadata incomplete)`. Tiene peso específico: de esta entrada dependen la regla de calidad por antigüedad (§19, L849), la encuesta a 130 comerciantes (C048) y la justificación de «costos ocultos» como requerimiento (§20, L865). Que la fuente sea un PDF local con manifestación de procedencia no sustituye la atribución académica.

— polarity: negativo · confidence: alta · related: [[#C048]], [[#C052]]

### F-V8-010 — Entradas truncadas y agrupadas en las tablas de fuentes

Varias celdas de §17 y §18 condensan múltiples obras en una sola fila o truncan el título, de modo que no constituyen entradas diferenciables: «`Hombros/01_PDFs/PDF Informe de competencia del mercado automotriz ...` / `Mercado automotriz chileno: un análisis empírico`» (L795); «Informes ANFAC / EY / INEGI / BBVA / COIIM en `Hombros/01_PDFs/`» (L797); «Universidades (PUCE, UPS, UPV, UChile, UNAL, etc.) | **Académico** | Repositorios institucionales (.edu / repositorios oficiales) en `Hombros/indice.md`» (L821); «CarDekho (Kaggle), Spinny, OLX, Revolico, Autocubana, Dongfeng» (L822); «UCI Automobile, datasets sintéticos (Zimbabwe/Nigeria) | **Académico/sintético** | Declarado en los propios README» (L825).

En los casos 8–11, 22–25 del inventario no hay título de documento, año, autor ni URL individual; la tabla de §18 añade además la salvedad «Citados en los informes descargados en `Hombros/01_PDFs/`; no todos re-verificados en vivo» (L820) y «No verificados en vivo; elTOQUE es medio independiente, no BCC» (L824). Todas se marcan `(metadata incomplete)`. La agregación no es en sí misma un error —el informe declara que son contexto— pero impide decidir qué obra sostiene cada afirmación y dificulta detectar duplicados internos.

— polarity: negativo · confidence: alta · related: [[#C050]], [[#C051]], [[#C071]]

### F-V8-011 — Repositorios usados como antecedente metodológico sin versión, URL ni compromiso

El documento atribuye decisiones de diseño a código de terceros: «Se adaptó el patrón `output_writer.py` + `diff_runs.py` de `spinny-scraper` como snapshot `Data/Revolico/snapshots/ultimo.json`» (§16, L781); «`Copias/taso-api/src/*` | Tasas de cambio múltiples | Normalizar CUP/USD/MLC/EUR» (§17, L800); «`Copias/AutosxCuba/code/{unir_todo_final,modelo_predictivo,generar_graficos}.py`» (L798); y el bloque «`Auxiliares/Repositorios Referencias/{uk-automotive-transition,vahan-india,nz-vehicle-market-tracker,zimbabwe-used-vehicle-market-analysis}` | Series por período, EDA, viabilidad» (L804).

Ninguna de las entradas 26–35 del inventario incluye URL de repositorio, commit, tag, licencia o fecha de acceso. E3 consigna que no se aportó cloned path y que `repo_clone_status: not-attempted`, por lo que la atribución no pudo cotejarse contra el código. Todas quedan `(metadata incomplete)`. El caso de `Copias/` es además paradójico: §3 declara «`Copias/` no se registra en este informe por decisión explícita» (L52), mientras §17 y §50 sí citan su código como insumo metodológico, de modo que la fuente se usa sin entrar en el inventario de fuentes ni en el de artefactos.

— polarity: negativo · confidence: alta · related: [[#C062]], [[#C083]]

### F-V8-012 — Condiciones de Uso de Revolico citadas sin URL ni copia archivada

La afirmación de permanencia (C040) se apoya en un documento sin ficha: «las Condiciones de Uso de Revolico (23/09/2026) no fijan un plazo de caducidad de los anuncios. Empíricamente, un anuncio con `updated_on_by_user=2024-12-17` seguía en HTTP 200 el 17/11/2026 (~699 días)» (§15, L771). La entrada 21 del inventario tiene fecha pero no URL, título completo, editor ni copia local identificable; el texto sí nombra como fuente alternativa el repositorio de diferencias en §16. Queda `(metadata incomplete)`.

Conviene distinguir los dos componentes: la observación empírica del HTTP 200 es interna al proyecto y no requiere cita externa; la negativa de la fuente a fijar caducidad sí es una afirmación sobre un documento tercero y, tal como está escrita, no puede verificarse sin el texto de las condiciones.

— polarity: negativo · confidence: media · related: [[#C040]]

### F-V8-013 — Convención de formato heterogénea y fuentes que aparecen solo en prosa

Además de las tablas, varias fuentes se mencionan únicamente en el texto y nunca se consolidan: «salarios de la Resolución 14» (§19, L847; §20, L863), «Womy (`https://womy.cu/cars/`)» y «Clasificados.st y TecnoTáctil» (§52, L1296–1297), el «índice oficial `http://www.onei.gob.cu/cuba`» (§53, L1309) y «DfT / DVLA» fuera de la tabla de auditoría. La tabla de §18 usa una columna «Naturaleza» con valores mezclados (`Oficial gubernamental`, `Gremial`, `Académico`, `Marketplace / anuncios`, `Redes sociales`, `No oficial`) y la de §17 mezcla normas, informes, repositorios y rutas de archivo bajo la misma etiqueta «Fuente».

No hay fecha de acceso sistemática, ni separación entre «obra citada» y «archivo descargado», ni normalización de mayúsculas/idioma de títulos (`Inteligencia De Negocios Aplicada Al Sector Automovilístico`, `Mercado automotriz chileno: un análisis empírico`, `Análisis del mercado de vehículos usados y su comercialización en el__73e1773e.pdf`). Para un lector que quiera reconstruir la cadena evidencia→afirmación, la consecuencia es que la procedencia está documentada en el nivel de la fuente pero no en el nivel de la entrada bibliográfica. Las entradas afectadas se mantienen `(metadata incomplete)`.

— polarity: negativo · confidence: alta · related: [[#C068]], [[#C071]]

### F-V8-014 — No hay duplicados ni identificadores espurios en el documento; el mapa E2 queda fuera de la bibliografía auditable

La inspección de las 36 menciones nominales no encontró la misma obra presentada dos veces con identidades distintas dentro del documento. Tampoco hay DOI, ID de arXiv ni venue asignados por el informe a fuente alguna: el único DOI que aparece en este artefacto, `10.2307/1879431`, procede de la respuesta de Crossref/OpenAlex verificada en F-V8-002 y no se atribuye al texto auditado.

El mapa de literatura E2 contiene 38 trabajos con sus propios DOI y URLs, pero es un artefacto generado por el evaluador de literatura, no una bibliografía del informe: E2 lo declara explícitamente —«el documento no tiene bibliografía numerada [...] la única obra académica citada por nombre es P001 (1970)»—. Por extensión, las 37 obras restantes de E2 no se cuentan aquí ni se auditan como entradas del documento; hacerlo equivaldría a atribuir al informe citas que no contiene. Este hallazgo delimita el alcance del cómputo del frontmatter (`bibliography_entries_total: 36`).

— polarity: positivo · confidence: alta

## Nota de cierre

Las verificaciones se registran tal como fueron obtenidas: Crossref y OpenAlex confirmaron la ficha de Akerlof; GOV.UK confirmó organismo, fecha y licencia de DfT/DVLA; los sitios de ANFAC y AEADE confirmaron la existencia de las secciones citadas; ONEI y la API de BCC fallaron con error de transporte; las búsquedas web no estuvieron disponibles. Ningún dato ausente se completó por inferencia. Las 32 entradas `(metadata incomplete)` requieren, para una auditoría completa, acceso a la Gaceta Oficial cubana, a los PDFs de `Hombros/` y a los repositorios referenciados, además de una fecha de consulta declarada por fuente.


## §9 — v9-ethics


## Resumen

- §10 declara una regla operativa de recolección (no elusión de anti-automatización, registro de HTTP 403/429, solo datos agregados sin nombres ni teléfonos); no se localiza una declaración de uso de IA ni una declaración consolidada de disponibilidad de datos o código.
- §50 documenta la encuesta de 33 personas y las 30 + 30 + 8 entrevistas con anonimato parcial; no aparece declarado el consentimiento de los participantes ni una aprobación de comité de ética.
- No se recibió tabla de densidad de V7 para contraste ni clon verificado de E3; ausencia de COI y de declaración de doble uso se registran con el calibrado `master`, sin extenderlo a niveles superiores.

### F-V9-001 — Sin declaración de uso de IA en la investigación o la redacción

Búsqueda de «inteligencia artificial», «IA generativa», «uso de IA», «AI», «ChatGPT», «Claude», «asistencia» y «declaración» en las secciones 1–12 (L14–268), en el registro de altas §13 (L276–748) y en §14–§68 (L750–1462): no se localiza declaración alguna de herramientas de IA, fases de uso ni protocolo de supervisión. El único crédito textual con la sigla es `AutofillAiModelCache` en filas del registro de altas (L317–320), relativo a un directorio de caché del perfil de WhatsApp, no a una declaración de asistencia. §55 (L1341) consigna la instalación de habilidades de escritura y presentación, sin nombrar herramientas de IA. El criterio `V9.ai_use_declaration.master` se lee: «Declaration expected; should name tools, phases (research, drafting, code generation, translation), and supervision protocol». No se recibió el `v7_ai_density_hint`, por lo que no se emite hallazgo cruzado de densidad.

— polarity: negative · confidence: high · related: [] · criteria: V9.ai_use_declaration.master

### F-V9-002 — Regla operativa de recolección y exclusión de datos personales declarada en §10

§10 (L116) registra: «Condiciones de uso de cada portal: criterio operativo para la recolección. No se eluden mecanismos anti-automatización; los HTTP 403/429 se registran como limitación». La misma sección (L117) añade: «Protección de datos personales, ciberseguridad y derechos de autor: antes de publicar resultados deben verificarse las normas cubanas vigentes y aplicar solo datos agregados, sin nombres, teléfonos ni información personal de anunciantes». La versión inglesa reproduce ambos enunciados (§10 EN, L245–246). La regla reaparece como criterio de fuente en §18 (L823): «No verificables como fuente estadística; requieren consentimiento y sin datos personales», y como límite en §19 (L851): «precios pedidos no transaccionados, sesgo de supervivencia de anuncios, sin datos personales, vigencia normativa a verificar». El enunciado es operativo y prospectivo —«antes de publicar resultados»— y no nombra un marco de cumplimiento ni una revisión ya realizada. El criterio `V9.data_ethics.master` se lee: «Consent + IRB/ethics-committee approval named when applicable». La literatura de ética de scraping mapeada en E2 (P021, P022) coincide con el contenido de esta regla sin que el informe la cite.

— polarity: positive · confidence: high · related: [[#F-V9-003]], [[#P021]], [[#P022]] · criteria: V9.data_ethics.master

### F-V9-003 — Sin consentimiento ni aprobación de comité declarados para la encuesta y las entrevistas

§50 (L1265) describe: «la encuesta con datos reales fue un Google Forms de 32 preguntas aplicado a 33 personas de 4 segmentos en un barrio de La Habana». El mismo pasaje consigna: «Las entrevistas (30 + 30 + 8) son cualitativas, anónimas salvo el grupo de AutosxCuba —que incluye nombres y requiere cuidado—». E3 inventaría 33 respuestas de encuesta y 30 + 30 + 8 entrevistas entre las 25 tablas de `Data/repos-autos-referencias/referencias_autos.sqlite` (§50, L1263). La búsqueda de «consentimiento», «consent informado», «IRB», «comité de ética» y «aprobación» en todo el documento solo devuelve la expresión condicional de §18 (L823) —«requieren consentimiento»— y la verificación pendiente de §10 (L117). No hay declaración de consentimiento obtenido, de aprobación de comité ni de procedimiento de anonimización aplicado a los 33 encuestados; la única precisión sobre anonimato es la nota descriptiva de §50 referida a las entrevistas. El criterio `V9.data_ethics.master` se lee: «Consent + IRB/ethics-committee approval named when applicable».

— polarity: negative · confidence: high · related: [[#C063]], [[#F-V9-002]] · criteria: V9.data_ethics.master

### F-V9-004 — Procedencia y anonimato parcial registrados en el consolidado de encuestas y entrevistas

§50 (L1261) registra que la comparación de 233 archivos detectó, entre otros duplicados, «snapshots parciales de la encuesta, copias de entrevistas y tablas de reporte». El consolidado de §50 (L1263) conserva «33 respuestas de encuesta, 30 + 30 + 8 entrevistas» junto a «una tabla `provenancia`», con script reproducible en `Auxiliares/herramientas/consolidar_repos_autos.py`. La nota de §50 (L1265) precisa el estado del anonimato: «anónimas salvo el grupo de AutosxCuba —que incluye nombres y requiere cuidado—». El informe registra así la procedencia de los instrumentos y la excepción de identificación, sin una declaración de tratamiento para ese grupo con nombres. §17 (L793) menciona además una «encuesta a 130 comerciantes» del estudio PUCE como fuente externa, distinta de los 33 encuestados del proyecto.

— polarity: neutral · confidence: high · related: [[#C063]], [[#F-V9-003]] · criteria: V9.data_ethics.master

### F-V9-005 — Sin declaración de conflictos de interés; el nivel `master` no la requiere

La búsqueda de «conflicto de interés», «interés», «patrocinio», «financiación», «tutor», «asesor» y «agradecimientos» en §1–§68 no localiza declaración de COI. El cierre del documento (L1461) consigna únicamente «Firma / Signature: responsable del proyecto / project owner.» Cambios de rumbo se atribuyen a terceros sin identificar como patrocinadores: §15 (L767) «se detuvo manualmente `revolico-scrape.timer` y su servicio a petición del usuario» y §21 (L877) «A petición del usuario, el objetivo inmediato deja de ser la recomendación interactiva de compra». §67 (L1447) registra borrados «Con autorización explícita». El criterio `V9.coi_statement.master` se lee: «Not required; tutor/advisor relationship implicit». La ausencia no constituye una brecha en el calibrado de nivel `master`; tutors, patrocinadores ni financiadores aparecen nombrados.

— polarity: neutral · confidence: high · related: [] · criteria: V9.coi_statement.master

### F-V9-006 — Sin declaración de doble uso o impacto societario; tema fuera de la lista sensible

El objetivo declarado en §1 (L16) es un «análisis del mercado automotor cubano» y un pipeline de scraping; el documento no trata modelos de lenguaje, vigilancia, bioseguridad, armas autónomas ni diagnóstico clínico. §10, §18 y §19 contienen notas éticas y legales operativas, pero no una sección dedicada a impacto societario. La única proyección de alcance público, §63 (L1413), se etiqueta a sí misma: «es **inferencia de diseño, no medición**». El criterio `V9.dual_use.master` se lee: «Discussion encouraged for dual-use-relevant topics».

— polarity: neutral · confidence: medium · related: [[#F-V9-002]] · criteria: V9.dual_use.master

### F-V9-007 — Disponibilidad de datos: rutas, fragmentación y hashes sin declaración consolidada

El documento describe la localización y reconstrucción de los datos sin concentrarlas en un enunciado de disponibilidad. §14 (L752) declara: «La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**», con fragmentos de 16 MiB y `reconstruir_revolico.py`; la tabla de L759 registra 795373568 B, 48 partes y un prefijo SHA-256 `dadd2bffba615d8a…`. §54 (L1321) describe 82 fragmentos de 10 MB con `MANIFEST.json` y verificación de hashes. §53 (L1309–1311) documenta los anuarios del ONEI con URL, tamaño y SHA-256 por archivo en `INDICE.md`; §10 (L118) acota: «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe». No hay sección titulada «Disponibilidad de datos», ni condiciones de acceso o licencia propias consolidadas; la única licencia explícita del documento pertenece a una fuente externa, DfT/DVLA, en §18 (L814): «Open Government Licence». El inventario E3 marca como `unknown` la accesibilidad pública de varias bases propias. El criterio `V9.data_availability_statement.master` se lee: «Brief statement: where the data lives, how to obtain».

— polarity: neutral · confidence: high · related: [[#F-V9-008]] · criteria: V9.data_availability_statement.master

### F-V9-008 — Disponibilidad de código: repositorio nombrado por propietario y slug, sin URL completa ni versión fijada

§40 (L1136–1139) identifica el remoto con un bloque de texto: «antes: CarlosAntonioAceaJimenezCD/autodecide-habana / ahora: CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba»; L1141 añade que `gh` actualizó el remoto `origin`, y L1143 registra la descripción del repositorio. El texto no imprime la URL completa ni un enunciado de tipo «código disponible en», y no fija commit, tag o DOI para la versión que produjo los resultados. E3 consigna en su frontmatter `repo_url: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba` con `repo_clone_status: not-attempted`, y mapea las rutas de scripts declaradas en el documento a ubicaciones no verificadas en disco. El criterio `V9.code_availability_statement.master` se lee: «"Code available at" statement with URL and brief description».

— polarity: neutral · confidence: high · related: [[#F-V9-007]] · criteria: V9.code_availability_statement.master

### F-V9-009 — Única licencia explícita del documento corresponde a una fuente externa

La auditoría de fuentes §18 (L814) registra para DfT/DVLA: «Verificado en vivo: publicado por Department for Transport + DVLA, actualizado 23/09/2026, Open Government Licence». Ninguna otra fila de la tabla de §18 (L812–825) declara licencia, y no aparece licencia para el código propio ni para las bases propias inventariadas en E3 (`revolico.sqlite`, catálogos, `telegram.sqlite`, `referencias_autos.sqlite`). Los términos de uso de los portales se tratan en §10 (L116) como «criterio operativo para la recolección», sin que se registren condiciones de redistribución de los datos capturados. Los criterios `V9.data_availability_statement.master` y `V9.code_availability_statement.master` comprenden respectivamente «how to obtain» y una declaración con URL y descripción; el documento cubre rutas y procedencia, no régimen de licencias propias.

— polarity: neutral · confidence: high · related: [[#F-V9-007]], [[#F-V9-008]] · criteria: V9.data_availability_statement.master



## §10 — Observaciones transversales

### F-V10-001 — KPIs del relato final, CSV reales y README: cuatro estados del mismo objeto

§59 (L1375) fija «**744 autos únicos**, **2.014 anuncios limpios** (1.323 locales y 691 de importación)» y «kilometraje mediano de **44.125 km**», mientras `Data/analisis_rentabilidad/outputs/tables/kpis.csv` registra `anuncios_totales,2029.0`, `anuncios_locales,1338.0` y `km_medianos,43000.0` (F-V3-005, F-V3-006). El README vigente declara «772 autos únicos de Revolico» y «2.029 anuncios limpios (1.338 locales + 691 de importación)», y `Auxiliares/herramientas/probar_actualizar_numeros.py:23–24` codifica el tránsito de 744 a 772 autos (F-V6-007). Junto a los recuentos de §24 (6.334 anuncios, 499 filas limpias) y §34 (972 ingeridas), estas cuatro versiones del mismo conjunto conviven sin marcador de fecha o corrida que las distinga (F-V2-012).

— polarity: negative · confidence: high · related: [[#F-V3-005]], [[#F-V3-006]], [[#F-V6-007]], [[#F-V2-012]]

### F-V10-002 — Retirada de la depreciación −5,43 % sin ablación ni engagement bibliográfico

§34 (L1052) reporta «una depreciación media de **−5,43 % anual** (p<0,001)» con primas de +21 % y −22 %; §59–§60 retiran la pendiente anual tras corregir kilometraje, con «p mínimo 0,165», y `outputs/tables/modelo_depreciacion.csv` registra `car_age,-0.0708,0.237` (F-V3-008). Esa retirada coincide con el estado de la evidencia reunido por E2 (H2, L540–542): P009 (Du et al., 2026), P011, P004 y P013 documentan no linealidad y heterogeneidad edad–precio, y ninguno se menciona en el informe (F-V5-007, F-V4-005). La sucesión de mejoras se ejecutó «una por una, sin borrar archivos» (§51, L1273), sin ablación de componentes declarada ni test pareado entre la corrida de 328 observaciones y la vigente (F-V2-003, F-V2-005); E2 califica la inestabilidad como «un resultado esperable de la especificación, no una anomalía del proyecto».

— polarity: negative · confidence: high · related: [[#F-V3-008]], [[#F-V5-007]], [[#F-V4-005]], [[#F-V2-003]], [[#F-V2-005]]

### F-V10-003 — Densidad alta en §17–21 y §59–63 sin declaración de uso de IA

La tabla «AI-pattern density by section» sitúa en nivel `high` dos bloques: §17–21 acumula 14 ocurrencias de «análisis» y 9 de «marco» en 1.671 palabras (≈13,8/1k) con escaleras de ocho y nueve pasos y glosas «EN.» sistemáticas (F-V7-004), y §59–63 reúne Romero §13 Don't 5 y Don't 8, con cuatro adjetivos valorativos seguidos en L1411 (F-V7-008, F-V7-009). La búsqueda de «inteligencia artificial», «IA generativa», «uso de IA», «ChatGPT», «Claude» y «declaración» en §1–§68 y §13 no localiza herramientas, fases ni protocolo de supervisión; el pasaje más cercano, §55 (L1341), consigna habilidades de escritura instaladas sin nombrar IA (F-V9-001). V9 dejó constancia de que no recibió la tabla de densidad de V7 para el contraste; la tabla sí figura en el material evaluado en esta pasada.

— polarity: negative · confidence: high · related: [[#F-V7-004]], [[#F-V7-008]], [[#F-V7-009]], [[#F-V9-001]]

### F-V10-004 — Conversión por TRMI: diaria en el texto, fija en el código y 920 frente a 930

§23 (L898) describe «la conversión usa `precio_USD × TRMI elTOQUE` del día del anuncio (columna `Mediana` de `Anexos/Investigacion Cambios/trmi_USD.csv`)» y en L900 reporta una serie que «pasó de 680 CUP/USD (09/07/2026) a 920 (16-17/11/2026)». §52 (L1293) fija en cambio «la **TRMI informal** de elTOQUE (930 CUP/USD), nunca la oficial», y `Data/analisis_rentabilidad/config.py:22–26` define `FX` con `1 / 930.0` y `FX_NOTE = "TRMI elTOQUE 18/11/2026..."`, sin que `01_ingest.py:398` lea el CSV (F-V6-008). Las dos cifras y los dos mecanismos no se reconcilian en el texto (F-V3-015), y la verificación externa de elTOQUE devolvió error de transporte, de modo que la entrada 20 permanece `(metadata incomplete)` (F-V8-008).

— polarity: negative · confidence: high · related: [[#F-V3-015]], [[#F-V6-008]], [[#F-V8-008]]

### F-V10-005 — Conclusión que niega la fase 8 frente a la bitácora de ejecución

§1 (L16) y §12 (L137) afirman que «El análisis de mercado y el modelo de rentabilidad (fase 8) aún no están implementados», mientras §34 (L1012–1058) describe la creación de `Data/analisis_rentabilidad/` con `01_ingest.py` a `05_benchmark.py` y §59–§60 reportan resultados del mismo pipeline (F-V3-001). La macroestructura refuerza el desajuste: después de §12 predomina el registro cronológico, 53 de las 55 secciones de §14–§68 llevan fecha en el encabezado y §13 ocupa 479 líneas de tabla generada por `actualizar_informe.py` (F-V1-003); los títulos nombran operaciones de edición —«Reescritura de la sección 3 del storytelling» (§45, L1208)— y las reescrituras se describen sin mostrar el texto resultante (F-V7-009, F-V7-011). La Parte II conserva además el objetivo anterior y la fase 8 sin el cambio registrado en §21 (F-V1-002).

— polarity: negative · confidence: high · related: [[#F-V1-003]], [[#F-V1-002]], [[#F-V3-001]], [[#F-V7-009]], [[#F-V7-011]]

### F-V10-006 — Diferenciación declarada solo contra el repositorio egipcio

El único pasaje con estructura de párrafo comparativo es «Brecha frente a Egipto» (§34, L1054–1056), que opone escalas de datos —«Egipto tiene 23.500 anuncios [...] Nosotros tenemos el pipeline y las técnicas cubiertas, pero solo 497 usados, un único snapshot»— al repositorio `Egyptian-Used-Cars`, fuente de ingeniería ausente del mapa E2 (F-V4-004). En ese mapa, los vecinos académicos de los candidatos de originalidad están marcados `Cited in document: no`: P014 para scraping más modelado de precios (F-V4-002), P009 para la regresión hedónica (F-V4-005) y P029 para el TRMI en Cuba (F-V4-006). La cobertura global del mapa en el documento es 1/38 obras, con cuatro clústeres sin ninguna cita (F-V5-001) y 22 de los 23 trabajos del top-5 por clúster ausentes (F-V5-004); los diferenciadores declarados —integración local, forma funcional, conversión fechada— quedan enunciados sin contraste argumentativo con esos trabajos.

— polarity: negative · confidence: high · related: [[#F-V4-002]], [[#F-V4-004]], [[#F-V4-005]], [[#F-V4-006]], [[#F-V5-001]], [[#F-V5-004]]

### F-V10-007 — Fuentes nominales incompletas y artefactos fuera del árbol del proyecto

El documento reúne 36 fuentes nominales, 32 de ellas `(metadata incomplete)`, sin citas numeradas ni convención autor-año (F-V8-001), y las 14 afirmaciones load-bearing de E1 consignan «— (sin citas numeradas)» en el campo de evidencia externa (F-V5-003). En paralelo, el corpus normativo se localiza en `~/Utilidades/Leyes/gaceta_catalog.json`, fuera del árbol (F-V6-014); VAHAN y el endpoint vivo del BCC figuran como no accesibles desde este entorno (F-V6-012, F-V6-013); y las búsquedas web devolvieron HTTP 403 mientras la verificación se apoyó en Crossref y OpenAlex (F-V5-008). La procedencia queda documentada en nivel de fuente y de ruta, pero la correspondencia entre afirmación y entrada bibliográfica verificable no queda establecida dentro del documento ni dentro del repositorio.

— polarity: negative · confidence: high · related: [[#F-V8-001]], [[#F-V5-003]], [[#F-V6-014]], [[#F-V5-008]]

### F-V10-008 — Muestra del modelo «actual» de 22 observaciones, ausente del relato

§22 (L890) reporta 323 autos con 248 precios USD válidos y la tabla interna de §34 (L1047) declara 328 observaciones del modelo OLS; el archivo vigente `outputs/tables/modelo_resumen.txt` registra en cambio «No. Observations: 22», R-squared 0,277 y Prob(F-statistic) 0,623, cifra que no aparece en la reformulación de §59–§60 (F-V3-010). El umbral de precio declarado en §22 es 500 USD y `config.py:31–32` fija `PRICE_MIN_USD = 200` (F-V6-017). Las 17 funciones `test_*` del checkout ejercitan el panel HTML, la exportación Parquet y el reemplazo de marcadores, sin importar los cinco scripts de `01_ingest.py` a `05_benchmark.py` (F-V6-006): la dimensión muestral de la estimación vigente queda fuera del texto y sin prueba de regresión en el código.

— polarity: negative · confidence: high · related: [[#F-V3-010]], [[#F-V2-006]], [[#F-V6-017]], [[#F-V6-006]]

## Apéndice A — Plan ejecutado

# Plan de auditoría — Informe técnico / Technical report

## Documento detectado
- Ruta: `INFORME_TECNICO.md` (~1.462 líneas, bilingüe español/inglés)
- Idioma: es (confianza alta)
- Nivel: master (informe técnico calibrado con rasero de maestría)
- Autor: responsable del proyecto
- Repo: `CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba`

## Profundidad
- Preset: Standard

## Fase 1 — Recolección
- E1: inventario de afirmaciones (load-bearing, supporting, contextual)
- E2: mapa de literatura con fuentes verificables
- E3: inventario de artefactos (datasets, tablas, figuras)

## Fase 2 — Evaluación
- V1 estructura, V2 metodología, V3 resultados/evidencia, V4 novedad,
  V5 estado del arte, V6 reproducibilidad, V7 escritura y tics de IA,
  V8 integridad bibliográfica, V9 ética y declaraciones.

## Fase 3 — Síntesis
- Expediente forense: `reviews/informe-tecnico-2026-11-27.forensic.md`
- Informe narrativo: `reviews/informe-tecnico-2026-11-27.md`
- Aprobado por el usuario el 27/11/2026; alcance "completa + mejoras".


## Apéndice B — Inventario de afirmaciones

# Claim Inventory

## Summary

- Total: 191
- Load-bearing: 14 · Supporting: 65 · Contextual: 112
- By type: result 86 · methodological 66 · novelty 0 · contextual 122 · definitional 16 · citation-grounded 21

Nota de alcance: el documento es bilingüe y varias secciones aparecen duplicadas en inglés (Parte II, L141–268, y bloques `**EN.**` a lo largo de §14–68). El inventario registra cada afirmación una sola vez, usando como excerpt la versión en español cuando existe; la versión inglesa se cita en los campos de evidencia interna. No hay páginas numeradas en el texto cacheado, por lo que `Section` identifica la sección y `Lines` las líneas del archivo. El documento no emplea citas numeradas tipo `[N]`; por eso `External evidence cited` se marca «— (sin citas numeradas)» y las fuentes nombradas se consignan, cuando procede, en `Notes`. Las filas del registro de altas (§13, L276–748) son metadatos de archivos y no se inventarían una por una; solo se registran las que afirman una propiedad verificable de una herramienta.

## Load-bearing claims

### C001 — Análisis y modelo de rentabilidad (fase 8) aún no implementados; producto interactivo diferido

- **Section**: §12. Conclusiones (Parte I); §21. Cambio de objetivo
- **Lines**: 137 (eco en 16, 866, 877–884, 266)
- **Types**: result, contextual
- **Excerpt**: «El análisis de mercado y el modelo de rentabilidad (fase 8) aún no están implementados; el producto interactivo se difiere a una especialización futura.»
- **Restated**: A la fecha de la conclusión no existía un modelo de rentabilidad operativo ni un recomendador interactivo entregado; sería falso si cualquiera de los dos estuviera implementado en ese momento.
- **Internal evidence cited**: §1 (L16), §20.8 (L866), §21 (L877–884), §12 EN (L266), Part II §1 (L145).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: La Parte II (L145) conserva el objetivo anterior de recomendación interactiva; §21 atribuye el cambio a una petición del usuario. Existe tensión con §34, §58 y §59, donde sí se documentan análisis y modelo ejecutados.

### C002 — Fase activa sexta y estado de las nueve fases

- **Section**: §2. Estado y fases (Parte I)
- **Lines**: 22–34
- **Types**: result, contextual
- **Excerpt**: «Las fases se redefinieron para que la fase activa sea la sexta. Estado a 17/11/2026:»
- **Restated**: A 17/11/2026 las fases 1–5 estaban completadas, la 6 en curso y las 7–9 pendientes; sería falso si otra fase estuviera activa.
- **Internal evidence cited**: Tabla de fases (L24–34); §2 EN (L151–163).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: La creación del informe y del README se declara transversal (L36), sin alterar este estado.

### C003 — Marco normativo vigente: Decreto 163/2026 y resolución 312/2026 derogada

- **Section**: §12. Conclusiones (Parte I); §4. Fase 1; §10. Marco legal; §52. Ampliación de fuentes
- **Lines**: 134 (eco en 56, 114–115, 1299)
- **Types**: citation-grounded, contextual
- **Excerpt**: «El marco regulatorio vigente es el Decreto 163/2026 y el paquete de resoluciones citado.»
- **Restated**: La norma rectora de importación y comercialización es el Decreto 163/2026 (Gaceta 65 Ordinaria, 04/08/2026, vigente desde el 11/08/2026), que deroga el Decreto 119/2024, y la Resolución 312/2026 quedó derogada por la 340/2026; sería falso si rigiera otra norma.
- **Internal evidence cited**: §4 (L56), §10 (L114–115), §52 (L1299), §12 EN (L263), §4 EN (L185).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Fuentes nombradas: Gaceta Oficial No. 65 Ordinaria y resoluciones 104/17/52/171–175/312/340/102 de 2026.

### C004 — Nueve marketplaces con inventario real

- **Section**: §12. Conclusiones (Parte I); §5. Fase 2
- **Lines**: 133 (eco en 62)
- **Types**: result
- **Excerpt**: «El mercado habanero tiene nueve marketplaces con inventario real y una docena con categorías vacías o solo piezas.»
- **Restated**: El conteo de marketplaces con inventario real es nueve y el de sitios con categorías vacías o solo piezas es aproximadamente una docena; sería falso si los conteos difirieran.
- **Internal evidence cited**: §5 (L60–64), §12 EN (L262), §5 EN (L189–191).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: La enumeración de L62 da cifras para siete marketplaces y menciona otros dos sin cifra; la cifra «nueve» no se desglosa en una tabla.

### C005 — No elusión de anti-automatización y registro de HTTP 403/429

- **Section**: §10. Marco legal para la recolección y el análisis de datos
- **Lines**: 116 (eco en 127, 245)
- **Types**: methodological, result
- **Excerpt**: «No se eluden mecanismos anti-automatización; los HTTP 403/429 se registran como limitación.»
- **Restated**: La recolección respetó los mecanismos anti-automatización y trató los HTTP 403/429 como limitaciones documentadas, no como obstáculos sorteados.
- **Internal evidence cited**: §9 (L108), §11 (L127), §10 EN (L245).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Se declara además que el contenido de carrosw no se falsificó (L127).

### C006 — Sostenibilidad del scraping: ritmo, sesión y reanudación

- **Section**: §12. Conclusiones (Parte I)
- **Lines**: 135 (eco en 124–129, 264)
- **Types**: methodological, result
- **Excerpt**: «El scraping sostenible depende del ritmo, la sesión y la reanudación, no principalmente del fingerprint TLS.»
- **Restated**: Según el informe, el factor principal de la sostenibilidad del scraping es el ritmo, la sesión y la reanudación, y no el fingerprint TLS; sería falso si el fingerprint TLS fuera el determinante principal.
- **Internal evidence cited**: §11 (L124–129), §6 (L70), §37 (L1096), §12 EN (L264).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Afirmación causal sin diseño comparativo explícito en el texto; se registra como atribución del informe.

### C007 — Eficiencia comparada de Telegram MTProto, Facebook GQL y WAHA

- **Section**: §15. Eficiencia de Telegram, WhatsApp y Facebook
- **Lines**: 763–765
- **Types**: methodological, result, contextual
- **Excerpt**: «Para obtener más datos del mercado habanero, la ruta más eficiente es Telegram MTProto (`telethon`, ya integrado): sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`. Le sigue Facebook GQL»
- **Restated**: El orden de eficiencia declarado es Telegram MTProto, luego Facebook GQL, luego WAHA para WhatsApp, con Playwright/Selenium como último recurso; sería falso si otro orden fuera el sostenido por la evidencia del proyecto.
- **Internal evidence cited**: §15 EN (L765), §28–29 (L946–969), §35 (L1064–1070).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Comparación cualitativa; el texto no adjunta una medición de tiempo por fuente.

### C008 — Anuncios como precios pedidos, no transaccionados

- **Section**: §18. Auditoría de procedencia
- **Lines**: 822, 827 (eco en 829)
- **Types**: methodological, definitional, citation-grounded
- **Excerpt**: «No son estadísticas oficiales; son precios **pedidos**, no transaccionados»
- **Restated**: Las señales de precio de marketplaces y redes son precios anunciados y no sustituyen estadísticas oficiales de transacción; sería falso si se tratara de precios efectivamente transaccionados.
- **Internal evidence cited**: §18 (L822, L827), §19 (L851), §20 (L871), §18 EN (L829).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: La conclusión de L827 añade que las fuentes oficiales y gremiales sirven de contexto y validación.

### C009 — Primera ejecución del modelo hedónico: −5,43 % anual

- **Section**: §34. Esqueleto de análisis de rentabilidad — Línea base real de la primera ejecución
- **Lines**: 1037–1052
- **Types**: result, methodological
- **Excerpt**: «El modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` da una depreciación media de **−5,43 % anual** (p<0,001), con primas de +21 % para premium y −22 % para tier medio frente al desconocido.»
- **Restated**: En esa ejecución el modelo estimó una depreciación anual de −5,43 % con p<0,001 y primas de +21 %/−22 %; sería falso si esos coeficientes no correspondieran a la corrida descrita.
- **Internal evidence cited**: §34 (L1041–1052), §44 (L1202), §45 (L1210), §34 EN (L1058).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Cifra posteriormente reformulada como no significativa en §59 (L1377) y §60 (L1385); ambas versiones coexisten en el documento.

### C010 — Estado final del conjunto de datos al 23/11/2026

- **Section**: §59. Storytelling alineado con los datos finales
- **Lines**: 1375 (eco en 1275–1277, 1365–1369)
- **Types**: result
- **Excerpt**: «El relato ahora usa **744 autos únicos**, **2.014 anuncios limpios** (1.323 locales y 691 de importación), mediana local de **21.000 USD**, kilometraje mediano de **44.125 km**, 50 marcas, 100 grupos comparables y 81 anomalías.»
- **Restated**: El dataset vigente para el relato final tiene 744 autos únicos y 2.014 anuncios limpios, con mediana local de 21.000 USD y kilometraje mediano de 44.125 km; sería falso si el pipeline regenerado produjera otros totales.
- **Internal evidence cited**: §51 (L1275–1277), §58 (L1365–1369), §59 EN (L1379).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: §58 reporta además 961 anuncios en `itencel.sqlite` e `integrity_check=ok`.

### C011 — Depreciación final no significativa tras corregir kilometraje

- **Section**: §59. Storytelling alineado con los datos finales; §60. Inventario de funciones y modelos
- **Lines**: 1377, 1385
- **Types**: result, methodological
- **Excerpt**: «el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra»
- **Restated**: En la corrida vigente la pendiente anual y la prima premium no son estadísticamente significativas (p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05); sería falso si los coeficientes alcanzaran significancia.
- **Internal evidence cited**: §60 (L1385), §59 (L1377), §60 EN (L1387).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Entra en tensión con C009, correspondiente a una ejecución anterior.

### C012 — Anuarios del ONEI sin series de parque automotor ni matriculaciones

- **Section**: §56. Análisis de los anuarios y estructura de GitHub
- **Lines**: 1347
- **Types**: result, citation-grounded
- **Excerpt**: «**No hay series de parque automotor ni de matriculaciones**, por lo que esa laguna signalada en `NECESIDADES.md` no se resuelve con los anuarios; la corrección quedó registrada.»
- **Restated**: Los 12 anuarios del ONEI revisados no contienen series de parque automotor ni de matriculaciones; sería falso si alguna de esas series estuviera presente.
- **Internal evidence cited**: §52 (L1295), §53 (L1313), §56 (L1347), §56 EN (L1351).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Corrige la expectativa registrada antes en §52 y §53 y la laguna señalada en `NECESIDADES.md`.

### C013 — Estimación de retención: inferencia de diseño, no medición

- **Section**: §63. Calidad del storytelling como puerta de entrada
- **Lines**: 1413
- **Types**: methodological, contextual
- **Excerpt**: «La estimación de retención (`Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md`) es **inferencia de diseño, no medición**: de cada 100 visitantes, ~58 leerían el primer párrafo, ~16 llegarían al cierre y ~5 volverían con intención de consulta.»
- **Restated**: Las cifras de retención son proyecciones de diseño y no datos observados; sería falso si se presentaran como mediciones de tráfico real.
- **Internal evidence cited**: §63 (L1411–1413), §63 EN (L1415).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: La proyección condicionada es de ~22–25 finalizaciones y ~18–22 retornos.

### C014 — Regla de las 10 páginas y resultados repetidos

- **Section**: §12. Conclusiones (Parte I); §7. Fase 4
- **Lines**: 136 (eco en 76, 265)
- **Types**: methodological, result
- **Excerpt**: «La regla de las 10 páginas evitó consumir resultados repetidos.»
- **Restated**: La regla de parar tras 10 páginas sin enlaces útiles tuvo como efecto evitar el consumo de resultados repetidos; sería falso si esa regla no hubiera incidido en la deduplicación.
- **Internal evidence cited**: §7 (L76–84), §12 EN (L265).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Afirmación causal atribuida al informe; las tres búsquedas pararon en las páginas 19, 11 y 22.

## Supporting claims (65)

### C015 — 17 empresas autorizadas y precios de referencia

- **Section**: §4. Fase 1 — Marco normativo y regulatorio
- **Lines**: 56
- **Types**: result, citation-grounded
- **Excerpt**: «Se documentaron **17 empresas autorizadas** a importar y comercializar vehículos [...] precios de referencia (BDC One 14.849–31.478 EUR; Dongfeng desde 21.900 EUR; Finauto desde 15.500 EUR; ATR Export con 46 modelos)»
- **Restated**: El informe registra 17 empresas autorizadas y rangos de precios de referencia por distribuidor.
- **Internal evidence cited**: §4 (L56), §4 EN (L185).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: `Data/investigacion-mercado-automotor-cuba.md`.

### C016 — Resoluciones sectoriales cotejadas

- **Section**: §4. Fase 1; §10. Marco legal
- **Lines**: 56, 115
- **Types**: citation-grounded, contextual
- **Excerpt**: «Se cotejaron las resoluciones 104/2026 (MINCEX), 17/2026 (MINCIN), 52/2026 (MITRANS), 171–175/2026 (MFP), 312/2026, derogada por 340/2026 (Aduana) y 102/2026 (BCC).»
- **Restated**: El informe declara cotejadas siete resoluciones de 2026, con la 312/2026 marcada como derogada por la 340/2026.
- **Internal evidence cited**: §4 (L56), §10 (L115), §4 EN (L185).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Las fuentes se nombran, no se numeran como citas.

### C017 — Consolidación de resultados de búsqueda

- **Section**: §5. Fase 2 — Descubrimiento y verificación de fuentes
- **Lines**: 60
- **Types**: result
- **Excerpt**: «Se consolidaron **409 resultados, 400 únicos**.»
- **Restated**: La consolidación produjo 409 resultados, de los cuales 400 eran únicos.
- **Internal evidence cited**: §5 (L60), §5 EN (L189).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Dos búsquedas iniciales en DuckDuckGo, 30 páginas cada una, bloqueadas por CAPTCHA.

### C018 — Sitios inventariados y verificados

- **Section**: §5. Fase 2
- **Lines**: 60, 62
- **Types**: result
- **Excerpt**: «Se inventariaron **35 sitios** de compraventa en `Data/mercados-compraventa-cuba.md` [...] Se verificaron **40 sitios/URLs**.»
- **Restated**: El inventario comprendió 35 sitios de compraventa y la verificación cubrió 40 sitios o URLs.
- **Internal evidence cited**: §5 (L60, L62), §5 EN (L189, L191).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C019 — Marketplaces con sección activa y sus conteos

- **Section**: §5. Fase 2
- **Lines**: 62
- **Types**: result
- **Excerpt**: «Marketplaces con sección activa: Autocubana (667 vehículos), iTENCEL (951), VentaCuba (801 carros/camionetas), Timbirichi (281 carros), Revolico (112 enlaces en la primera página), Cogetucarro (5.225 anuncios), Cubisima (155 fichas), Apululu y Carros.com Cuba.»
- **Restated**: Los conteos declarados por marketplace son 667, 951, 801, 281, 112 enlaces, 5.225 y 155 fichas, más dos sitios sin cifra.
- **Internal evidence cited**: §5 (L62), §5 EN (L191), §12 (L133).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Mezcla unidades heterogéneas (vehículos, anuncios, enlaces de primera página).

### C020 — Correcciones de clasificación de sitios

- **Section**: §5. Fase 2
- **Lines**: 62
- **Types**: result
- **Excerpt**: «Se corrigieron clasificaciones: Mercadoba y Fagales Market sin sección real; TuCuevita, Mercubano, Mercandil, Revoltillo, QvaVentas [...] con categoría vacía; BizneCubano, Katapulk, A la Venta, Pymes Bulevar, MeroliCU y Rico Cuba son de piezas, motos o servicios.»
- **Restated**: Diecisiete sitios fueron reclasificados en tres grupos: sin sección real, con categoría vacía y de piezas/motos/servicios.
- **Internal evidence cited**: §5 (L62), §5 EN (L191), §12 (L133).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Sustenta la conclusión C004.

### C021 — 14 organismos con competencia sobre el mercado

- **Section**: §5. Fase 2
- **Lines**: 64
- **Types**: result, contextual
- **Excerpt**: «Se documentaron **14 organismos** con competencia sobre el mercado: Consejo de Ministros/Estado, MINCEX, MINCIN, MITRANS, CEMA, MFP, ONAT, Aduana General, BCC, MININT, MINJUS, MEP, MINREX y MINSAP.»
- **Restated**: El informe enumera 14 organismos con competencia sobre el mercado automotor cubano.
- **Internal evidence cited**: §5 (L64), §5 EN (L193).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C022 — 61 repositorios clonados

- **Section**: §6. Fase 3 — Infraestructura técnica y herramientas
- **Lines**: 68
- **Types**: result
- **Excerpt**: «Se clonaron **61 repositorios** en `Auxiliares/Repositorios` con `--depth 1` (2,2 GB, 61 entradas `OK`).»
- **Restated**: La clonación produjo 61 repositorios, 2,2 GB y 61 entradas registradas como `OK`.
- **Internal evidence cited**: §6 (L68), §6 EN (L197).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C023 — Clasificación y selección de proyectos CAPTCHA

- **Section**: §6. Fase 3
- **Lines**: 68
- **Types**: result
- **Excerpt**: «Se clasificaron **92 proyectos** de CAPTCHA en `Data/github-captcha-repos.md` y se seleccionaron 9.»
- **Restated**: Se clasificaron 92 proyectos de CAPTCHA y se seleccionaron 9.
- **Internal evidence cited**: §6 (L68), §6 EN (L197).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C024 — Versiones del entorno y servicios de renderizado

- **Section**: §6. Fase 3
- **Lines**: 70
- **Types**: result, methodological
- **Excerpt**: «Se creó `Auxiliares/.venv` con patchright 1.64.4, PyPasser 1.1.0, Scrapling 0.5.1, ddddocr 1.6.1, playwright 1.65.2, curl_cffi 0.17.0, trafilatura, pandas, numpy, onnxruntime 1.32.0, ddgs 9.16.1 y tenacity 9.2.1. Se usa el Chromium del sistema y FlareSolverr 3.5.2 en Docker»
- **Restated**: El entorno declara versiones específicas de once paquetes y el uso de Chromium del sistema con FlareSolverr 3.5.2.
- **Internal evidence cited**: §6 (L70), §6 EN (L199).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C025 — Regla de parada tras 10 páginas y definición de «útil»

- **Section**: §7. Fase 4 — Corpus documental y trabajos investigativos
- **Lines**: 76
- **Types**: methodological, definitional
- **Excerpt**: «Tres búsquedas con la regla de parar tras 10 páginas sin enlaces útiles (útil = primera aparición de un trabajo investigativo automotriz)»
- **Restated**: La regla de parada se define como 10 páginas consecutivas sin enlaces útiles, donde «útil» significa la primera aparición de un trabajo investigativo automotriz.
- **Internal evidence cited**: §7 (L76–82), §7 EN (L205–211).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Operacionaliza la conclusión C014.

### C026 — Primera búsqueda de trabajos investigativos

- **Section**: §7. Fase 4
- **Lines**: 80
- **Types**: result
- **Excerpt**: «`mercado automovilistico trabajos investigativos` | 112 | 1.086 | 11 | página 19»
- **Restated**: La primera búsqueda recorrió 112 páginas, devolvió 1.086 resultados, 11 útiles y se detuvo en la página 19.
- **Internal evidence cited**: §7 (L80), §7 EN (L209).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C027 — Segunda búsqueda de trabajos investigativos

- **Section**: §7. Fase 4
- **Lines**: 81
- **Types**: result
- **Excerpt**: «`rentabilidad del precio de automoviles trabajos investigativos` | 24 | 226 | 2 | página 11»
- **Restated**: La segunda búsqueda recorrió 24 páginas, devolvió 226 resultados, 2 útiles y se detuvo en la página 11.
- **Internal evidence cited**: §7 (L81), §7 EN (L210).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C028 — Tercera búsqueda de trabajos investigativos

- **Section**: §7. Fase 4
- **Lines**: 82
- **Types**: result
- **Excerpt**: «`calidad precio mercado automotriz trabajo investigativo` | 23 | 230 | 10 | página 22»
- **Restated**: La tercera búsqueda recorrió 23 páginas, devolvió 230 resultados, 10 útiles y se detuvo en la página 22.
- **Internal evidence cited**: §7 (L82), §7 EN (L211).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C029 — Resultados de descarga del corpus

- **Section**: §7. Fase 4
- **Lines**: 84
- **Types**: result
- **Excerpt**: «descarga inicial **93 OK / 17 fallos**, rentabilidad **23 OK / 10 fallos**, calidad/precio **78 OK / 36 fallos**, con `manifest.jsonl` e `indice.md».
- **Restated**: Las tres tandas de descarga produjeron 93/17, 23/10 y 78/36 aciertos y fallos respectivamente.
- **Internal evidence cited**: §7 (L84), §7 EN (L213).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C030 — Esquema SQLite por tienda

- **Section**: §8. Fase 5 — Diseño del esquema de datos y del pipeline
- **Lines**: 88
- **Types**: methodological, definitional
- **Excerpt**: «Se diseñó una base SQLite por tienda con una tabla `vehiculos`: identificación (`url`, `shop`, `title`, `status`, `scraped_at`), metadatos y 30 campos estructurados [...] además de campos sin normalizar (`tables_json`, `jsonld_json`, `raw_html`, ...)»
- **Restated**: El esquema declarado comprende una tabla `vehiculos` por tienda con cinco campos de identificación, 30 campos estructurados y campos sin normalizar.
- **Internal evidence cited**: §8 (L88), §8 EN (L217).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Los nombres de campos difieren entre la versión española y la inglesa.

### C031 — Adaptadores por dominio y renderizado opcional

- **Section**: §8. Fase 5
- **Lines**: 88
- **Types**: methodological
- **Excerpt**: «El scraper `scrape_concesionarios.py` usa adaptadores por dominio y renderizado opcional con Playwright.»
- **Restated**: El scraper declarado usa un adaptador por dominio y puede activar renderizado con Playwright.
- **Internal evidence cited**: §8 (L88), §8 EN (L217).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C032 — Fase 6: 11 bases y 256 filas

- **Section**: §9. Fase 6 — Scraping y captura (en curso)
- **Lines**: 92
- **Types**: result
- **Excerpt**: «Se prepararon 11 bases y se obtuvieron **256 filas**»
- **Restated**: En el estado descrito se prepararon 11 bases de datos y se capturaron 256 filas.
- **Internal evidence cited**: §9 (L92–106), §9 EN (L221–235).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Cifra de la síntesis inicial; las secciones posteriores reportan volúmenes mucho mayores.

### C033 — Desglose de filas por tienda

- **Section**: §9. Fase 6
- **Lines**: 94–106
- **Types**: result
- **Excerpt**: «| AGN Motors | 60 | 45 | [...] | Chinautos Cuba | 70 | 0 | [...] | Finauto | 45 | 34 |»
- **Restated**: El desglose declara 11 tiendas con sus recuentos de filas totales y filas con precio.
- **Internal evidence cited**: §9 (L94–106), §9 EN (L223–235).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: La suma de las filas del desglose coincide con las 256 declaradas en L92.

### C034 — Exclusiones por bloqueo técnico en Fase 6

- **Section**: §9. Fase 6
- **Lines**: 108
- **Types**: result
- **Excerpt**: «Excluidas por bloqueo técnico: carrosw (HTTP 403 con Bot Verification), LlamaCuba (timeout) y SASA/DIVEP (sin catálogo).»
- **Restated**: Tres fuentes quedaron excluidas por causas técnicas específicas: 403 con verificación de bot, timeout y ausencia de catálogo.
- **Internal evidence cited**: §9 (L108), §11 (L127), §9 EN (L237).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C035 — Cambio de buscador y manejo de HTTP 202

- **Section**: §11. Problemas y soluciones
- **Lines**: 124–125
- **Types**: methodological, result
- **Excerpt**: «CAPTCHA en paginación DDG | Yahoo + visitas directas; después sesión con `vqd`. [...] HTTP 202 y página "anomaly" | Pausa 7–10 s con jitter, backoff exponencial y cooldown.»
- **Restated**: El informe atribuye a Yahoo y a una sesión `vqd` la respuesta al CAPTCHA, y a pausas de 7–10 s con jitter y backoff el manejo de HTTP 202.
- **Internal evidence cited**: §11 (L124–125), §5 (L60), §11 EN (L253–254).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C036 — Deduplicación por título, prefijo y dominio

- **Section**: §11. Problemas y soluciones
- **Lines**: 129
- **Types**: methodological
- **Excerpt**: «Repetidos y mirrors | Deduplicación por título normalizado, prefijo y dominio.»
- **Restated**: La estrategia de deduplicación declarada combina título normalizado, prefijo y dominio.
- **Internal evidence cited**: §11 (L129), §11 EN (L258).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C037 — Esquema de sincronización de Revolico en partes

- **Section**: §14. Sincronización automática de Revolico
- **Lines**: 752
- **Types**: methodological, result
- **Excerpt**: «La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**. Cada 10 minutos un timer de systemd ejecuta `Auxiliares/herramientas/actualizar_revolico.py`: corre el scraper incremental, divide la BD en partes de 16 MiB [...] sube solo las partes que cambiaron»
- **Restated**: La base no se versiona como archivo único sino en fragmentos de 16 MiB actualizados cada 10 minutos, con reconstrucción verificada por hash.
- **Internal evidence cited**: §14 (L752, L754), §14 (L759).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Esquema posteriormente complementado con Git LFS (§30) y con chunks de 10 MB (§54).

### C038 — Última ejecución registrada de la sincronización

- **Section**: §14. Sincronización automática de Revolico
- **Lines**: 759
- **Types**: result
- **Excerpt**: «| 2026-11-17T15:47:42+00:00 | 795373568 B | 48 partes de 16 MiB | `dadd2bffba615d8a…` |»
- **Restated**: La fila de sincronización registra 795.373.568 bytes, 48 partes de 16 MiB y un SHA-256 que comienza con `dadd2bffba615d8a`.
- **Internal evidence cited**: §14 (L756–759).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: El hash aparece truncado en el documento.

### C039 — Parada manual del timer de scrapeo

- **Section**: §15. Eficiencia de Telegram, WhatsApp y Facebook — Nota
- **Lines**: 767
- **Types**: result
- **Excerpt**: «se detuvo manualmente `revolico-scrape.timer` y su servicio a petición del usuario. El scraper había ampliado la BD de 3.682 a **6.332 anuncios** (520,6 MB) antes de detenerse; no se generaron partes»
- **Restated**: El scraper elevó la base de 3.682 a 6.332 anuncios antes de detenerse manualmente, sin producir partes; `revolico-git.timer` permaneció activo.
- **Internal evidence cited**: §15 (L767), §15 EN (L767), §24 (L909).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C040 — Permanencia de anuncios y ausencia de caducidad fija

- **Section**: §15. Eficiencia — Permanencia
- **Lines**: 771
- **Types**: result, citation-grounded
- **Excerpt**: «las Condiciones de Uso de Revolico (23/09/2026) no fijan un plazo de caducidad de los anuncios. Empíricamente, un anuncio con `updated_on_by_user=2024-12-17` seguía en HTTP 200 el 17/11/2026 (~699 días)»
- **Restated**: Las condiciones de uso no establecen caducidad y se observó un anuncio de 2024-12-17 aún accesible 699 días después.
- **Internal evidence cited**: §15 (L771), §15 EN (L771), §31 (L983–985).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: Condiciones de Uso de Revolico (23/09/2026).

### C041 — Frecuencia de renovación de anuncios

- **Section**: §15. Eficiencia — Permanencia
- **Lines**: 771
- **Types**: result
- **Excerpt**: «El 99,3 % de los anuncios tiene `updated_on_by_user` en los últimos 7 días (mediana 1 día en los 189 autos)»
- **Restated**: El 99,3 % de los anuncios tiene fecha de actualización en los últimos siete días y la mediana en los 189 autos es de un día.
- **Internal evidence cited**: §15 (L771), §15 EN (L771).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C042 — Limpieza ejecutada sobre 6.332 anuncios

- **Section**: §15. Eficiencia — Limpieza ejecutada
- **Lines**: 769
- **Types**: result
- **Excerpt**: «`limpiar_revolico.py` conservó **304 autos** en la tabla `autos` y registró **6.028 exclusiones** en `revision` (5.983 no vehículo 4+ ruedas, 45 sin datos necesarios, 0 páginas sin datos suficientes).»
- **Restated**: La limpieza conservó 304 autos y registró 6.028 exclusiones, desglosadas en 5.983, 45 y 0.
- **Internal evidence cited**: §15 (L769), §15 EN (L769), §16 (L783).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C043 — Conservación de filas originales y columnas de auditoría

- **Section**: §15. Eficiencia — Limpieza ejecutada
- **Lines**: 769
- **Types**: methodological, result
- **Excerpt**: «No se borraron filas originales: `anuncios` conserva las columnas de auditoría `es_auto`, `motivo_exclusion`, `pagina_revisada` y `datos_necesarios`. Se añadieron `microbús/guagua/ómnibus/bus` a los patrones de inclusión.»
- **Restated**: Ninguna fila original fue eliminada y la tabla conserva cuatro columnas de auditoría, además de ampliarse la lista de términos de inclusión.
- **Internal evidence cited**: §15 (L769), §15 EN (L769).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C044 — Pipeline de tres etapas con colas persistentes

- **Section**: §16. Pipeline de colas
- **Lines**: 775–779
- **Types**: methodological, result
- **Excerpt**: «`scrape_revolico_pipeline.py` separa el trabajo en tres etapas simultáneas con colas persistentes en `Data/Revolico/pipeline.sqlite`»
- **Restated**: El pipeline declarado ejecuta descubrimiento, descarga y procesamiento como tres etapas simultáneas con colas persistentes.
- **Internal evidence cited**: §16 (L775–779), §16 EN (L785).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C045 — Commit por lotes de 25 anuncios

- **Section**: §16. Pipeline de colas
- **Lines**: 779
- **Types**: methodological
- **Excerpt**: «Cada **25 anuncios procesados** (aceptados o rechazados) se hace un commit por lotes en `anuncios`/`autos`/`imagenes`/`telefonos` o en `revision`.»
- **Restated**: El tamaño de lote declarado para los commits es 25 anuncios procesados, aceptados o rechazados.
- **Internal evidence cited**: §16 (L779), §20 (L863).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C046 — Marcador de fecha del listado y salto de descarga desactivado

- **Section**: §16. Pipeline de colas
- **Lines**: 781
- **Types**: methodological, result
- **Excerpt**: «El campo `updatedOnToOrder` del listado resultó ser un marcador de ranking y no de edición, así que el salto de descarga queda desactivado por defecto (`--skip-unchanged`)»
- **Restated**: El campo `updatedOnToOrder` interpreta como ranking y no como edición, por lo que la opción de omitir descargas permanece desactivada por defecto.
- **Internal evidence cited**: §16 (L781), §16 EN (L785).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C047 — Prueba de una página del pipeline de colas

- **Section**: §16. Pipeline de colas
- **Lines**: 783
- **Types**: result
- **Excerpt**: «Prueba con 1 página: **119 enlaces** descubiertos y procesados, 7 lotes de 25, BD principal de 6.332 a **6.334 anuncios** y de 304 a **317 autos**.»
- **Restated**: La prueba procesó 119 enlaces en siete lotes y elevó la base de 6.332 a 6.334 anuncios y de 304 a 317 autos.
- **Internal evidence cited**: §16 (L783), §16 EN (L785).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C048 — Aporte metodológico del estudio PUCE

- **Section**: §17. Guía de análisis de mercado
- **Lines**: 793
- **Types**: contextual, citation-grounded
- **Excerpt**: «Asimetría de información (Akerlof); clasificación de calidad por antigüedad (≤5 años alta, >5 años con defectos); encuesta a 130 comerciantes; medición de costos ocultos y margen de reventa»
- **Restated**: El trabajo PUCE aporta el marco de asimetría de información, una clasificación por antigüedad y una encuesta a 130 comerciantes.
- **Internal evidence cited**: §17 (L793), §19 (L837), §19 (L849).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: PDF de la PUCE en `Hombros/01_PDFs/`.

### C049 — Requerimientos derivados para el análisis

- **Section**: §17. Guía de análisis de mercado
- **Lines**: 806
- **Types**: methodological, definitional
- **Excerpt**: «**Requerimientos derivados:** (1) esquema común con precio+moneda normalizada [...] (4) modelo de rentabilidad = precio de reventa esperado − precio de compra − costos − impuestos; (5) serie temporal con snapshots; (6) dashboard de mercado; (7) validación, dedup y sin datos personales.»
- **Restated**: El informe deriva siete requerimientos para las fases 7–8, incluida la fórmula del modelo de rentabilidad.
- **Internal evidence cited**: §17 (L806), §19 (L849), §20 (L863–865).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C050 — Verificación en vivo de DfT/DVLA

- **Section**: §18. Auditoría de procedencia
- **Lines**: 814
- **Types**: citation-grounded
- **Excerpt**: «Verificado en vivo: publicado por Department for Transport + DVLA, actualizado 23/09/2026, Open Government Licence»
- **Restated**: La fuente DfT/DVLA fue verificada en vivo, con fecha de actualización 23/09/2026 y licencia Open Government Licence.
- **Internal evidence cited**: §18 (L814), §17 (L804).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: `gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files`.

### C051 — Fuentes oficiales no accesibles desde el entorno

- **Section**: §18. Auditoría de procedencia
- **Lines**: 815–816
- **Types**: citation-grounded, contextual
- **Excerpt**: «VAHAN (India) [...] No accesible desde este entorno (error de transporte); el repo documenta 12 exportaciones mensuales 2025 [...] BCC (Banco Central de Cuba) [...] No accesible en vivo desde este entorno»
- **Restated**: VAHAN y BCC no pudieron verificarse en vivo desde el entorno, aunque el repositorio VAHAN documenta 12 exportaciones mensuales de 2025.
- **Internal evidence cited**: §18 (L815–816), §52 (L1293).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C052 — Clases de calidad y comparables adaptados

- **Section**: §19. Marco de análisis de mercado y su adaptación
- **Lines**: 849
- **Types**: methodological, definitional
- **Excerpt**: «clases de calidad (≤5 años alta, >5 años con defectos, según PUCE); bandera de asimetría por ocultamiento; comparables por modelo ±2 años y municipio; rentabilidad = reventa esperada − compra − reacondicionamiento − impuestos; asequibilidad = precio / salario; series con snapshots.»
- **Restated**: El marco adaptado define clases de calidad por antigüedad, comparables ±2 años y municipio, y fórmulas de rentabilidad y asequibilidad.
- **Internal evidence cited**: §19 (L846–851), §20 (L861–865).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C053 — Análisis descriptivo inicial: muestra y precios válidos

- **Section**: §22. Análisis descriptivo inicial
- **Lines**: 890
- **Types**: result
- **Excerpt**: «Resultados sobre 323 autos: 248 precios USD válidos (≥500 USD); 74 precios <500 USD marcados como inválidos y 1 en CUP excluidos.»
- **Restated**: El análisis se realizó sobre 323 autos, de los que 248 tenían precio USD válido, 74 se marcaron inválidos y uno se excluyó por estar en CUP.
- **Internal evidence cited**: §22 (L888–892), §24 (L909).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C054 — Estadísticos de precio del análisis inicial

- **Section**: §22. Análisis descriptivo inicial
- **Lines**: 890
- **Types**: result
- **Excerpt**: «Precio mediano **22.000 USD**, media 24.416,59 USD, IQR 11.375–35.000 USD, rango 600–95.000 USD.»
- **Restated**: La distribución de precios del análisis inicial tiene mediana 22.000 USD, media 24.416,59 USD, IQR 11.375–35.000 USD y rango 600–95.000 USD.
- **Internal evidence cited**: §22 (L890), §22 EN (L892).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Cifra divergente respecto de la mediana local de 21.000 USD en §51 y §59.

### C055 — Líderes de frecuencia y cobertura de campos derivados

- **Section**: §22. Análisis descriptivo inicial
- **Lines**: 890
- **Types**: result
- **Excerpt**: «Marca más frecuente: Hyundai (n=75); municipio con más oferta: Playa (n=53). Cobertura de campos derivados: marca 68,4 %, año 63,5 %, km 6,2 % (heurísticos, extraídos solo de título/descripción). Detectados 5 outliers por IQR.»
- **Restated**: Hyundai y Playa lideran las frecuencias; la cobertura de campos derivados es 68,4 %, 63,5 % y 6,2 %, con cinco outliers por IQR.
- **Internal evidence cited**: §22 (L890), §24 (L907).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C056 — Conversión con la TRMI diaria de elTOQUE

- **Section**: §23. Conversión elTOQUE, serie temporal y gráficas
- **Lines**: 898
- **Types**: methodological, result
- **Excerpt**: «la conversión usa `precio_USD × TRMI elTOQUE` del día del anuncio (columna `Mediana` de `Anexos/Investigacion Cambios/trmi_USD.csv`).»
- **Restated**: La conversión a CUP aplica la TRMI de elTOQUE correspondiente al día del anuncio, tomada de la columna `Mediana` del CSV indicado.
- **Internal evidence cited**: §23 (L898), §52 (L1293).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: §52 menciona 930 CUP/USD para la TRMI informal, cifra distinta de la de §23.

### C057 — Supuesto de anuncio activo

- **Section**: §23. Conversión elTOQUE, serie temporal y gráficas
- **Lines**: 899
- **Types**: methodological, definitional
- **Excerpt**: «todos los registros tienen `status=PUBLISHED` y página verificada en la captura, por lo que se asume que son comprables; no se comprueba disponibilidad en tiempo real.»
- **Restated**: El análisis asume que los anuncios con `status=PUBLISHED` y página verificada son comprables, sin comprobar disponibilidad en tiempo real.
- **Internal evidence cited**: §23 (L899), §25 (L917), §19 (L851).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Supuesto explícitamente declarado, no medición.

### C058 — Serie precio versus tasa

- **Section**: §23. Conversión elTOQUE, serie temporal y gráficas
- **Lines**: 900
- **Types**: result
- **Excerpt**: «la TRMI pasó de 680 CUP/USD (09/07/2026) a 920 (16-17/11/2026); la mediana mensual CUP subió de 12,58 M (julio) a 20,7 M (noviembre).»
- **Restated**: La TRMI declarada pasó de 680 a 920 CUP/USD entre julio y noviembre de 2026, y la mediana mensual en CUP de 12,58 M a 20,7 M.
- **Internal evidence cited**: §23 (L900), §23 EN (L903).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C059 — Diccionarios JSON completos sin campos estructurados de vehículo

- **Section**: §24. Estado del scrapeo y procesamiento de diccionarios
- **Lines**: 907
- **Types**: result
- **Excerpt**: «**Diccionarios/JSON guardados** (6.334/6.334 anuncios): `meta_json`, `ad_json` y `apollo_full`. [...] **No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**: por eso `anio_est`, `marca_est` y `km_est` se derivan con regex del texto visible»
- **Restated**: Los 6.334 anuncios conservan tres diccionarios JSON, pero no contienen claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión.
- **Internal evidence cited**: §24 (L907), §22 (L890), §24 EN (L911).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C060 — Reporte de scrapeo y estado de colas

- **Section**: §24. Estado del scrapeo y procesamiento de diccionarios
- **Lines**: 909
- **Types**: result
- **Excerpt**: «`anuncios` 6.334 · `autos` 323 · `revision` 6.085 · `imagenes` 13.932 · `telefonos` 7.699 · BD 520,6 MB. Colas: `url_queue` 141 (125 done, 3 downloading, 13 pending)»
- **Restated**: El reporte declara recuentos por tabla, 520,6 MB de base y colas con elementos pendientes de una corrida interrumpida.
- **Internal evidence cited**: §24 (L909), §25 (L918), §24 EN (L911).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C061 — Supuesto de disponibilidad en catálogos

- **Section**: §25. Reanudación, resiliencia y supuesto de catálogos
- **Lines**: 917
- **Types**: methodological, definitional
- **Excerpt**: «Para concesionarios y páginas similares se asume que todo el catálogo está disponible salvo que la página indique lo contrario y que se publicó el día de la captura [...] Para clasificados se mantiene el supuesto de anuncio activo = comprable, con `fecha_publicacion = updated_on_by_user`.»
- **Restated**: El código distingue dos supuestos de publicación: catálogos con fecha de captura y clasificados con fecha de actualización del anuncio.
- **Internal evidence cited**: §25 (L917), §23 (L899).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C062 — Causa del retraso y orden corregido de clasificación

- **Section**: §26. Orden corregido: enlace → clasificación → BD
- **Lines**: 924
- **Types**: methodological, result
- **Excerpt**: «Se identificó la causa del retraso en la clasificación: el timer ejecutaba `actualizar_revolico.py`, que solo corre el scraper y divide la BD, sin escribir nunca `autos`/`revision`. El servicio ahora ejecuta `scrape_revolico_pipeline.py`»
- **Restated**: El informe atribuye el retraso a un timer que no escribía `autos`/`revision` y declara corregido el orden mediante clasificación temprana en el descubrimiento.
- **Internal evidence cited**: §26 (L924–929), §33 (L1004).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Se presenta como diagnóstico de causa raíz.

### C063 — Encuesta de demanda sobre preferencia eléctrica

- **Section**: §50. Consolidación de bases de los repositorios de autos
- **Lines**: 1265
- **Types**: result
- **Excerpt**: «la encuesta con datos reales fue un Google Forms de 32 preguntas aplicado a 33 personas de 4 segmentos en un barrio de La Habana (17 de 18–25 prefieren eléctrico, pero 16 de 18 no pagarían más de 4.000 USD por uno)»
- **Restated**: La encuesta aplicada a 33 personas registró que 17 de 18–25 prefieren eléctrico y que 16 de 18 no pagarían más de 4.000 USD por uno.
- **Internal evidence cited**: §50 (L1265), §51 (L1281), §50 EN (L1267).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: La reconciliación posterior en §51 reduce a 28 los interesados y corrige las propulsiones.

### C064 — Deduplicación de `autos` a 744 registros únicos

- **Section**: §51. Mejoras del proyecto
- **Lines**: 1275
- **Types**: result, methodological
- **Excerpt**: «La tabla se reconstruyó desde `anuncios` (fuente canónica): 814 filas con 748 IDs únicos → **744 autos únicos**. Se excluyeron 4 anuncios que no son autos (`58867937`, `53777554`, `53843413`, `58886962`)»
- **Restated**: La deduplicación redujo 814 filas a 744 autos únicos y excluyó cuatro anuncios identificados por ID.
- **Internal evidence cited**: §51 (L1273–1275), §59 (L1375).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Se creó el índice único `idx_autos_id`.

### C065 — Reparación del análisis de precios en marketplaces

- **Section**: §51. Mejoras del proyecto
- **Lines**: 1277
- **Types**: result, methodological
- **Excerpt**: «`parse_price` ahora interpreta separadores de miles (973 anuncios recuperados: 872 de iTENCEL, 99 de Cubisima, 2 de VentaCuba). Los precios vacíos de Autocubana se recuperan del JSON-LD (614 anuncios, mediana 17.000 USD)»
- **Restated**: La reparación recuperó 973 anuncios con separadores de miles y 614 precios de Autocubana desde JSON-LD, con mediana 17.000 USD.
- **Internal evidence cited**: §51 (L1277), §55 (L1339), §51 EN (L1283).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C066 — Separación por canal local e importación

- **Section**: §51. Mejoras del proyecto
- **Lines**: 1277
- **Types**: result
- **Excerpt**: «Se incorporó la columna `canal`: **1.301 anuncios locales y 672 de importación** (iTENCEL), con `kpis_canal.csv` e `importacion_por_marca.csv` separados. La mediana local quedó en 21.000 USD.»
- **Restated**: El conjunto reparado se divide en 1.301 anuncios locales y 672 de importación, con mediana local de 21.000 USD.
- **Internal evidence cited**: §51 (L1277), §58 (L1367), §59 (L1375).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C067 — Corrección del parseo de kilometraje

- **Section**: §51. Mejoras del proyecto
- **Lines**: 1278
- **Types**: result, methodological
- **Excerpt**: «`parse_specs` y `parse_title` convertían `80,000 km` en 80 km. Se extrajo `parse_number()` con la lógica de separadores ya usada en `parse_price`. El código está aplicado y probado (`80,000` → 80.000)»
- **Restated**: El error de parseo convertía 80.000 km en 80 km y la corrección declarada produce 80.000.
- **Internal evidence cited**: §51 (L1278), §55 (L1339).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: El texto señala que la regeneración final de outputs se registra al cierre de la tanda.

### C068 — 25 fuentes adicionales verificadas y tasa informal empleada

- **Section**: §52. Ampliación de fuentes de datos
- **Lines**: 1289, 1293
- **Types**: result, citation-grounded
- **Excerpt**: «**25 fuentes** verificadas, organizadas por tipo con URL, datos expuestos, viabilidad de scraping y aporte al proyecto. [...] La conversión del proyecto sigue usando la **TRMI informal** de elTOQUE (930 CUP/USD), nunca la oficial.»
- **Restated**: El informe declara 25 fuentes verificadas y que la conversión emplea la TRMI informal de elTOQUE a 930 CUP/USD.
- **Internal evidence cited**: §52 (L1289–1297), §23 (L900).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: `Data/fuentes-adicionales-2026-11-20.md`.

### C069 — Descarga completa de los anuarios del ONEI

- **Section**: §53. Descarga completa de los anuarios del ONEI
- **Lines**: 1309–1311
- **Types**: result, citation-grounded
- **Excerpt**: «se recorrieron las 12 páginas de anuarios disponibles (2014–2025) y se descargaron **todos los documentos enlazados**: 111 PDF, 7 RAR y 103 archivos Excel extraídos, unos 311 MB en total»
- **Restated**: La descarga cubrió 12 anuarios (2014–2025), 111 PDF, 7 RAR y 103 Excel, unos 311 MB.
- **Internal evidence cited**: §53 (L1309–1311), §56 (L1347).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: índice oficial `http://www.onei.gob.cu/cuba`.

### C070 — División de la base de Revolico en chunks verificados

- **Section**: §54. Base de datos distribuida en chunks
- **Lines**: 1321
- **Types**: result, methodological
- **Excerpt**: «`Data/Revolico/revolico.sqlite` (849.465.344 bytes) se dividió en **82 chunks de 10 MB** en `Data/Revolico/chunks/`, con un `MANIFEST.json` que guarda el SHA-256 del archivo completo, el orden, el offset y el hash de cada fragmento. La verificación de los 82 chunks dio OK.»
- **Restated**: La base de 849.465.344 bytes se dividió en 82 fragmentos de 10 MB y los 82 pasaron la verificación de hashes.
- **Internal evidence cited**: §54 (L1321–1325), §14 (L759), §30 (L975).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C071 — Auditoría de fuentes web del 23/11/2026

- **Section**: §55. Auditoría de fuentes, README y verificación final
- **Lines**: 1333
- **Types**: result
- **Excerpt**: «Se consultaron **15 fuentes web** (8 marketplaces, 7 fuentes oficiales y complementarias): 14 respondieron HTTP 200 y elTOQUE no respondió desde este entorno. Las fechas más recientes en las bases son 17–18/11/2026.»
- **Restated**: De 15 fuentes consultadas, 14 respondieron HTTP 200 y elTOQUE no respondió; las fechas más recientes en las bases son 17–18/11/2026.
- **Internal evidence cited**: §55 (L1333), §55 EN (L1341).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: `Data/auditoria-fuentes-2026-11-23.md`.

### C072 — Series del ONEI y su interpretación

- **Section**: §56. Análisis de los anuarios y estructura de GitHub
- **Lines**: 1347
- **Types**: result, citation-grounded
- **Excerpt**: «el transporte de pasajeros cayó un 59 % entre 2019 y 2025 y el ómnibus un 71 %; los accidentes bajaron pero la gravedad aumentó (9,9 fallecidos por cada 100 accidentes en 2025)»
- **Restated**: Las series extraídas muestran caídas del 59 % y 71 % en transporte de pasajeros y ómnibus, y 9,9 fallecidos por cada 100 accidentes en 2025.
- **Internal evidence cited**: §56 (L1347), §56 EN (L1351).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: `Data/fuentes-oficiales/ONEI/series_oficiales.csv`.

### C073 — Reclasificación de enlaces y novedades en iTENCEL

- **Section**: §57. Reclassificación de páginas y novedades detectadas
- **Lines**: 1357
- **Types**: result, methodological
- **Excerpt**: «7 fuentes sin enlaces nuevos; **iTENCEL mostró 10 anuncios nuevos** [...] El detalle está en `Data/novedades-fuentes-2026-11-23.md` [...] sin modificar las bases.»
- **Restated**: La comparación de las dos primeras páginas de ocho marketplaces detectó diez anuncios nuevos solo en iTENCEL, sin modificar las bases de datos.
- **Internal evidence cited**: §57 (L1357), §58 (L1365).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: La normalización incluyó `www.`, query, Unicode NFC y barras finales.

### C074 — Incorporación de los diez anuncios nuevos de iTENCEL

- **Section**: §58. Incorporación de anuncios nuevos de iTENCEL
- **Lines**: 1365–1367
- **Types**: result
- **Excerpt**: «La BD pasó de 951 a **961 anuncios** (961 URLs únicas, `integrity_check=ok`). El pipeline se regeneró [...] **2.014 anuncios limpios**, de ellos 1.323 locales y 691 de importación; mediana local 21.000 USD y mediana de kilometraje 44.125 km.»
- **Restated**: La base de iTENCEL pasó de 951 a 961 anuncios únicos y el pipeline regenerado produjo 2.014 anuncios limpios con mediana local de 21.000 USD.
- **Internal evidence cited**: §58 (L1365–1369), §59 (L1375), §10 de la Parte I (L60).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Se realizó copia de seguridad `itencel.sqlite.bak-20261123` antes de escribir.

### C075 — Cifras narrativas de la sección 3 del storytelling

- **Section**: §45. Reescritura de la sección 3 del storytelling
- **Lines**: 1210
- **Types**: contextual, result
- **Excerpt**: «la mediana de 23.000 USD, la antigüedad media de 6,3 años, las 34 marcas, la depreciación de −5,43 % anual, los 27 grupos comparables y las 30 oportunidades infravaloradas»
- **Restated**: La versión intermedia del relato empleaba 23.000 USD de mediana, 6,3 años, 34 marcas, 27 grupos y 30 oportunidades.
- **Internal evidence cited**: §45 (L1210), §59 (L1375), §34 (L1045–1050).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Cifras divergentes de las finales de C010 y C074.

### C076 — Geometría extraída del APK de Circuitos Habana

- **Section**: §62. Factibilidad del timelapse eléctrico
- **Lines**: 1403
- **Types**: result
- **Excerpt**: «Del APK se extrajeron 2.473 puntos, 244 circuitos y 166 polígonos de zonas a `Data/mapas/circuitos/».
- **Restated**: La extracción produjo 2.473 puntos, 244 circuitos y 166 polígonos.
- **Internal evidence cited**: §62 (L1403), §35 (L1070).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C077 — Estimación de consumo de red de la automatización

- **Section**: §65. Automatización operativa y coste de red
- **Lines**: 1429
- **Types**: result, methodological
- **Excerpt**: «Estimación de red: **5–10 MB/mes** si no hay cambios y **50–90 MB/mes** con novedades.»
- **Restated**: La estimación declarada de tráfico es 5–10 MB mensuales sin cambios y 50–90 MB con novedades.
- **Internal evidence cited**: §65 (L1429), §65 EN (L1431).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: El texto la presenta como estimación, no como medición.

### C078 — Corrección de estados pendientes en el pipeline de Revolico

- **Section**: §66. Extracción continua de Revolico y arquitectura de datos
- **Lines**: 1437
- **Types**: result, methodological
- **Excerpt**: «3.351 enlaces `es_auto_candidato=0` quedaban `pending` para siempre: se marcan `rechazado` y se excluyen del conteo de salida [...] En la primera corrida corregida los anuncios `done` pasaron de 6.783 a 6.955.»
- **Restated**: El diagnóstico identificó 3.351 enlaces atascados y, tras la corrección, los anuncios `done` pasaron de 6.783 a 6.955.
- **Internal evidence cited**: §66 (L1437), §37 (L1098), §39 (L1124).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Se presenta como hallazgo de depuración.

### C079 — Reducción de tamaño del repositorio

- **Section**: §67. Optimización de espacio
- **Lines**: 1447
- **Types**: result
- **Excerpt**: «El repositorio pasó de 20 GB a 10 GB.»
- **Restated**: El tamaño del repositorio se redujo de 20 GB a 10 GB tras la eliminación autorizada de archivos.
- **Internal evidence cited**: §67 (L1447), §67 EN (L1449).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

## Contextual claims (72)

### C080 — Nombres anteriores conservados

- **Section**: §1. Objetivo
- **Lines**: 18
- **Types**: contextual
- **Excerpt**: «Se conservan los nombres anteriores, *AutoDecide Habana* e *ICD Automotive Market Project*, para mantener la trazabilidad de la documentación ya producida.»

### C081 — Clones con profundidad 1 y registro

- **Section**: §3. Organización de carpetas
- **Lines**: 52
- **Types**: contextual, methodological
- **Excerpt**: «los clones se hicieron con `--depth 1` y se registraron en `~/Utilidades/HerramientasScraping/_clone_log.tsv`»

### C082 — Descubrimiento separado de verificación

- **Section**: §3. Organización de carpetas
- **Lines**: 52
- **Types**: contextual, methodological
- **Excerpt**: «la descubrimiento se separó de la verificación»

### C083 — Exclusión de `Copias/` del informe

- **Section**: §3. Organización de carpetas; §13. Registro de altas
- **Lines**: 52, 272, 274
- **Types**: contextual
- **Excerpt**: «`Copias/` no se registra en este informe por decisión explícita.»

### C084 — Alcance restringido del marco legal

- **Section**: §10. Marco legal
- **Lines**: 112
- **Types**: contextual
- **Excerpt**: «Solo se incluyen las normas y fuentes relevantes para el contexto del proyecto»

### C085 — Índice de gacetas y corpus no registrado entrada por entrada

- **Section**: §10. Marco legal
- **Lines**: 118
- **Types**: contextual, citation-grounded
- **Excerpt**: «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe»

### C086 — Falso «anomaly» en HTTP 200

- **Section**: §11. Problemas y soluciones
- **Lines**: 126
- **Types**: contextual, methodological
- **Excerpt**: «Falso "anomaly" en HTTP 200 | Detector ajustado para exigir texto real de anomalía.»

### C087 — Renderizado de sitios JS-heavy

- **Section**: §11. Problemas y soluciones
- **Lines**: 128
- **Types**: contextual, methodological
- **Excerpt**: «Sitios JS-heavy | Renderizado con Chromium del sistema desde Playwright.»

### C088 — Registro automático de altas y regeneración del PDF

- **Section**: §13. Registro de altas
- **Lines**: 272, 274
- **Types**: contextual, methodological
- **Excerpt**: «El script `Auxiliares/herramientas/actualizar_informe.py` añade filas debajo del marcador y regenera el PDF.»

### C089 — Entradas omitidas en el registro

- **Section**: §13. Registro de altas
- **Lines**: 291
- **Types**: contextual
- **Excerpt**: «175 entradas adicionales no listadas / omitted»

### C090 — Herramientas declaradas en el registro de altas

- **Section**: §13. Registro de altas
- **Lines**: 279, 296, 297, 495, 496, 564
- **Types**: contextual, methodological
- **Excerpt**: «Pipeline de 3 etapas con colas persistentes para Revolico. [...] Scraper de WhatsApp Web mediante Playwright (sin WAHA/Docker). [...] Limpieza de la BD de Revolico: solo vehículos de 4+ ruedas con datos útiles.»

### C091 — Reconstrucción verificada por hash

- **Section**: §14. Sincronización automática de Revolico
- **Lines**: 752, 754
- **Types**: contextual, methodological
- **Excerpt**: «Para recuperar el archivo completo se usa `Auxiliares/herramientas/reconstruir_revolico.py`, que verifica el hash.»

### C092 — Telegram MTProto: sin navegador y cursor incremental

- **Section**: §15. Eficiencia de Telegram, WhatsApp y Facebook
- **Lines**: 763
- **Types**: contextual, methodological
- **Excerpt**: «sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`»

### C093 — Facebook GQL y normalización de precios

- **Section**: §15. Eficiencia de Telegram, WhatsApp y Facebook
- **Lines**: 763
- **Types**: contextual, methodological
- **Excerpt**: «Facebook GQL (`facebook_gql_scraper`): llamadas GraphQL con sesión autenticada y normalización con `price-parser`/`iso4217parse`, más rápido que Selenium.»

### C094 — WhatsApp sin API pública personal

- **Section**: §15. Eficiencia de Telegram, WhatsApp y Facebook
- **Lines**: 763
- **Types**: contextual, citation-grounded
- **Excerpt**: «Para grupos de WhatsApp no existe API pública personal; la opción operativa es un servidor WAHA auto-hospedado y su REST (`/api/sessions`, `/api/{session}/chats`, `/api/{session}/chats/{chatId}/messages`) con deduplicación por id»

### C095 — Esquema común de las tres fuentes

- **Section**: §15. Eficiencia de Telegram, WhatsApp y Facebook
- **Lines**: 763
- **Types**: contextual, definitional
- **Excerpt**: «La salida de las tres fuentes debe convergir en un esquema común (`fuente`, `id`, `chat/página`, `timestamp`, `texto`, `precio`, `moneda`, `url`) con dedup por `hash(fuente,id)` y sin datos personales.»

### C096 — Eliminación de palabras de defecto para costos ocultos

- **Section**: §19. Marco de análisis de mercado
- **Lines**: 848
- **Types**: contextual
- **Excerpt**: «estado y palabras de defecto en el texto (para estimar costos ocultos)»

### C097 — Límites declarados del análisis

- **Section**: §19. Marco de análisis de mercado
- **Lines**: 851
- **Types**: contextual, methodological
- **Excerpt**: «**Límites**: precios pedidos no transaccionados, sesgo de supervivencia de anuncios, sin datos personales, vigencia normativa a verificar.»

### C098 — Marco general de ocho pasos

- **Section**: §19. Marco de análisis de mercado — Marco general
- **Lines**: 833–842
- **Types**: contextual, definitional
- **Excerpt**: «**Marco general (8 pasos, derivado de los trabajos revisados)**»

### C099 — Delimitación geográfica y monetaria

- **Section**: §19. Adaptación a Cuba / La Habana
- **Lines**: 846
- **Types**: contextual, definitional
- **Excerpt**: «La Habana; autos de 4+ ruedas; canales formal e informal; precios anunciados en CUP/USD/MLC/EUR **sin mezclar**.»

### C100 — Marco detallado de nueve bloques

- **Section**: §20. Marco analítico detallado
- **Lines**: 857–867
- **Types**: contextual, definitional
- **Excerpt**: «El marco operativo completo consta de nueve bloques»

### C101 — Regresión hedónica y explicabilidad previstas

- **Section**: §20. Marco analítico detallado
- **Lines**: 865
- **Types**: contextual, methodological
- **Excerpt**: «regresión hedónica, margen de rentabilidad, asequibilidad precio/salario, ponderación de preferencias, explicabilidad tipo SHAP.»

### C102 — Necesidades de datos pendientes

- **Section**: §20. Marco analítico detallado
- **Lines**: 871
- **Types**: contextual
- **Excerpt**: «extracción estructurada de año/km/marca/modelo/combustible/transmisión desde `ad_json`/`apollo_full`; montos de costos ocultos; precios de transacción reales; estadísticas oficiales cubanas de parque y matriculaciones»

### C103 — Cambio de objetivo a petición del usuario

- **Section**: §21. Cambio de objetivo
- **Lines**: 877–884
- **Types**: contextual, definitional
- **Excerpt**: «A petición del usuario, el objetivo inmediato deja de ser la recomendación interactiva de compra y pasa a ser **un análisis de mercado**.»

### C104 — Archivos generados por el análisis descriptivo

- **Section**: §22. Análisis descriptivo inicial
- **Lines**: 888
- **Types**: contextual
- **Excerpt**: «genera en `Data/analisis/`: `resumen_general.csv`, `precios_por_marca.csv`, `precios_por_municipio.csv`, `precios_por_anio.csv`, `outliers.csv`, `cobertura.csv`, `informe_descriptivo.md` y `dashboard.html`.»

### C105 — Módulo de gráficas

- **Section**: §23. Conversión elTOQUE, serie temporal y gráficas
- **Lines**: 901
- **Types**: contextual
- **Excerpt**: «`Auxiliares/herramientas/graficos_mercado.py` usa matplotlib, seaborn y plotly (instalados) y genera 8 PNG + `dashboard_interactivo.html`»

### C106 — Librerías de mapas instaladas

- **Section**: §25. Reanudación, resiliencia y supuesto de catálogos
- **Lines**: 915
- **Types**: contextual
- **Excerpt**: «`geopandas 1.2.0`, `shapely 2.2.0`, `pyproj`, `folium 1.0.0`, `mapclassify`, `geopy`»

### C107 — Reinicio automático del servicio de scrapeo

- **Section**: §25. Reanudación, resiliencia y supuesto de catálogos
- **Lines**: 916
- **Types**: contextual, methodological
- **Excerpt**: «`revolico-scrape.service` ahora tiene `Restart=on-failure`, `RestartSec=30`, `StartLimitIntervalSec=300` y `StartLimitBurst=20`»

### C108 — Prueba del orden corregido

- **Section**: §26. Orden corregido: enlace → clasificación → BD
- **Lines**: 931
- **Types**: contextual, result
- **Excerpt**: «120 enlaces descubiertos, 63 descartados tempranamente y 185 candidatos descargados; `autos` pasó de 323 a 326 y `revision` de 6.085 a 6.134.»

### C109 — Aviso periódico de progreso

- **Section**: §27. Aviso periódico y umbral de revisión
- **Lines**: 937–938
- **Types**: contextual
- **Excerpt**: «`revolico-aviso.timer` avisa **cada 10 minutos** mediante `revolico-aviso.py`: escribe `Data/Revolico/progreso.md`, envía `notify-send` al escritorio y registra en el journal.»

### C110 — Umbral de revisión

- **Section**: §27. Aviso periódico y umbral de revisión
- **Lines**: 939
- **Types**: contextual, methodological
- **Excerpt**: «cuando `anuncios WHERE pagina_revisada=0`llega a **4.000** (configurable con `REVISAR_UMBRAL`), el aviso lanza `revolico-revisar.service`, que ejecuta el pipeline con `--solo-colas`»

### C111 — Estado de colas en §27

- **Section**: §27. Aviso periódico y umbral de revisión
- **Lines**: 940
- **Types**: contextual, result
- **Excerpt**: «Estado actual: 3.623 sin revisar, por debajo del umbral; 266 URLs, 11 descargas y 24 decisiones pendientes en colas.»

### C112 — Scraper público de Telegram sin credenciales

- **Section**: §28. Primeros datos de Telegram
- **Lines**: 946
- **Types**: contextual, methodological
- **Excerpt**: «No hay credenciales MTProto (`TELEGRAM_API_ID`/`TELEGRAM_API_HASH` vacías), así que se implementó [...] que lee la vista pública `t.me/s/<canal>` y pagina con `?before=<id>`. No requiere login, redacta teléfonos»

### C113 — Corrida del scraper de Telegram

- **Section**: §28. Primeros datos de Telegram
- **Lines**: 948
- **Types**: contextual, result
- **Excerpt**: «Corrida final (50 páginas): **152 mensajes**, **54 anuncios de autos** del canal `goldenbullbusinessfamilycars`, 45 con año detectable y **ninguno con precio explícito**»

### C114 — Canales de Telegram descartados

- **Section**: §28. Primeros datos de Telegram
- **Lines**: 950
- **Types**: contextual
- **Excerpt**: «Ninguno publicó anuncios de autos accesibles sin unirse: son noticias, eventos, compra-venta general, repuestos o grupos con invitación.»

### C115 — Base compartida de Telegram

- **Section**: §29. Base de datos de Telegram
- **Lines**: 956, 962–967
- **Types**: contextual, result
- **Excerpt**: «tres tablas: `canales`, `anuncios` y `estado`. Ambos scripts escriben en ella **mientras corren [...] Objetivo de 100 canales de referencia superado (119). El descubrimiento usa 26 búsquedas en tgden.com»

### C116 — Configuración de Git LFS

- **Section**: §30. Gestión de bases de datos con Git LFS
- **Lines**: 973
- **Types**: contextual, methodological
- **Excerpt**: «Se instaló **Git LFS 3.8.1** y se activó en el repositorio. `.gitattributes` marca `*.sqlite`, `*.sqlite-wal` y `*.sqlite-shm` con `filter=lfs diff=lfs merge=lfs -text`»

### C117 — Advertencia sobre cuota de LFS

- **Section**: §30. Gestión de bases de datos con Git LFS
- **Lines**: 977
- **Types**: contextual
- **Excerpt**: «la cuota LFS del plan gratuito es limitada; una BD que cambia cada 10 minutos genera un blob nuevo por commit.»

### C118 — Rango temporal permitido de anuncios

- **Section**: §31. Rango temporal de anuncios Revolico
- **Lines**: 983
- **Types**: contextual, definitional
- **Excerpt**: «Se fijó el rango permitido de `updated_on_by_user` entre **2021-01-01 y la fecha actual** en `limpiar_revolico.py` (`FECHA_MINIMA`).»

### C119 — Modo de descubrimiento sin procesamiento

- **Section**: §32. Backfill de descubrimiento sin procesamiento
- **Lines**: 991–996
- **Types**: contextual, methodological
- **Excerpt**: «**no hay descarga de anuncios, ni clasificación definitiva, ni inserción en `anuncios`/`autos`/`revision`**»

### C120 — Parada por página sin enlaces nuevos

- **Section**: §33. Parada por repetición y procesamiento de anuncios
- **Lines**: 1004
- **Types**: contextual, methodological
- **Excerpt**: «se detenga en cuanto una página no aporte **ningún enlace nuevo** (todos sus anuncios ya fueron vistos) [...] El contador `total` ahora acumula solo enlaces nuevos.»

### C121 — Arquitectura del esqueleto de rentabilidad

- **Section**: §34. Esqueleto de análisis de rentabilidad
- **Lines**: 1014, 1017–1033
- **Types**: contextual, methodological
- **Excerpt**: «Creé `Data/analisis_rentabilidad/` siguiendo la arquitectura del repositorio **Egyptian-Used-Cars** (ingesta → limpieza → EDA → estadística → benchmark)»

### C122 — Paquetes estadísticos y exclusión de DuckDB

- **Section**: §34. Esqueleto de análisis de rentabilidad
- **Lines**: 1035
- **Types**: contextual
- **Excerpt**: «Instalé además `statsmodels 0.15`, `pyarrow 26`, `kaleido`, `nbformat` y `nbconvert`. `duckdb` se desinstaló porque produce `Illegal instruction` en esta CPU»

### C123 — Brecha frente al estudio egipcio

- **Section**: §34. Esqueleto de análisis de rentabilidad — Brecha frente a Egipto
- **Lines**: 1056
- **Types**: contextual
- **Excerpt**: «Egipto tiene 23.500 anuncios, historial mensual de precios, HP y kilometraje estructurados, ANOVA/OLS/VIF, Tableau y Power BI. Nosotros tenemos el pipeline y las técnicas cubiertas, pero solo 497 usados, un único snapshot»

### C124 — Descarga y descompilación de APKs de Apklis

- **Section**: §35. App de circuitos eléctricos de Apklis
- **Lines**: 1064
- **Types**: contextual
- **Excerpt**: «Descargué tres APKs desde la API de Apklis [...] **Circuitos Habana** (`com.ermetic.circuitoshabana`, v2.2) [...] Con **jadx 1.5.6** descompilé la primera»

### C125 — La app Circuitos Habana sin API privada

- **Section**: §35. App de circuitos eléctricos de Apklis
- **Lines**: 1066
- **Types**: contextual, result
- **Excerpt**: «La app **no usa una API privada**: hace scraping del canal público de Telegram `https://t.me/s/EmpresaElectricaDeLaHabana` con Jsoup y User-Agent de Chrome.»

### C126 — Paginación y conversión horaria de la app

- **Section**: §35. App de circuitos eléctricos de Apklis
- **Lines**: 1067–1068
- **Types**: contextual
- **Excerpt**: «Paginación con `?before=<message_id>`, hasta 16 páginas / 300 mensajes / 8 días [...] convierte timestamps UTC a hora de Cuba con +1 h de horario de verano.»

### C127 — Docker sin privilegios de root

- **Section**: §36. Mapa offline, talleres e infraestructura EV
- **Lines**: 1080
- **Types**: contextual
- **Excerpt**: «el daemon Docker no arranca sin root en este entorno (`dockerd needs to be started with root privileges`), por lo que se descartó esa vía.»

### C128 — Ausencia de etiquetas OSM de talleres y carga

- **Section**: §36. Mapa offline, talleres e infraestructura EV
- **Lines**: 1081
- **Types**: contextual, result
- **Excerpt**: «Overpass/OSM fue consultado dos veces; no devuelve `shop=car`, `shop=car_repair` ni `charging_station` etiquetados en Cuba»

### C129 — Coordenadas extraídas de webs de concesionarios

- **Section**: §36. Mapa offline, talleres e infraestructura EV
- **Lines**: 1082
- **Types**: contextual, result
- **Excerpt**: «BDC One: 23.1155203,-82.3596368 y 23.0992805,-82.3050631; Dongfeng: 23.1250339,-82.4227564»

### C130 — Mapa offline sin internet

- **Section**: §36. Mapa offline, talleres e infraestructura EV
- **Lines**: 1083
- **Types**: contextual
- **Excerpt**: «Se generó `Data/mapas/mapa_ofline.html`: contorno de Cuba embebido + marcadores + Plotly incluido, funciona sin internet.»

### C131 — Infraestructura EV documentada

- **Section**: §36. Mapa offline, talleres e infraestructura EV
- **Lines**: 1084
- **Types**: contextual, citation-grounded
- **Excerpt**: «Dongfeng/NWI 11 estaciones solares (2026), CIMEX+MITRANS 21 estaciones (2025), primera estación rápida en Santa Clara (08/2026), conectores CCS2»

### C132 — Sesiones TLS por hilo

- **Section**: §37. Optimización de pipelines
- **Lines**: 1096
- **Types**: contextual, methodological
- **Excerpt**: «`scrape_revolico.py` ahora usa una **sesión curl_cffi por hilo** (`threading.local`) con impersonación Chrome, reutilizando conexiones TLS en vez de crear una por petición.»

### C133 — Aumento de descargadores y procesadores

- **Section**: §37. Optimización de pipelines
- **Lines**: 1096
- **Types**: contextual, methodological
- **Excerpt**: «El servicio `revolico-revisar.service` pasó de 8 descargadores/4 procesadores a **20/8** con `--batch-size 100`, `TimeoutStartSec=0` y `Restart=on-failure`»

### C134 — Marketplaces en paralelo

- **Section**: §37. Optimización de pipelines
- **Lines**: 1097
- **Types**: contextual, methodological
- **Excerpt**: «el nuevo servicio `marketplaces-scrape.service` corre **6 tiendas en paralelo** con `--delay 0.8`, cada una escribiendo su propia SQLite»

### C135 — Reporte periódico de progreso

- **Section**: §38. Reporte automático de progreso
- **Lines**: 1108–1113
- **Types**: contextual
- **Excerpt**: «actualiza **`Data/progreso_reporte.md` cada 5 minutos** con: conteos de `revolico.sqlite` [...] estado de las colas de `pipeline.sqlite` [...] estado de los servicios systemd.»

### C136 — Persistencia del temporizador de progreso

- **Section**: §38. Reporte automático de progreso
- **Lines**: 1115
- **Types**: contextual
- **Excerpt**: «El timer es persistente (`Persistent=true`) y arranca 1 minuto después del boot.»

### C137 — Ampliación de límites de marketplaces

- **Section**: §39. Continuación del scrapeo y presentación narrativa
- **Lines**: 1123
- **Types**: contextual, result
- **Excerpt**: «Cogetucarro de 200 → **5.008**, Autocubana y Timbirichi a 40 páginas [...] Autocubana pasó de 400 a **566** y Timbirichi de 110 a **170**, totalizando **2.121 anuncios**.»

### C138 — Reintento ante bloqueo de SQLite

- **Section**: §39. Continuación del scrapeo y presentación narrativa
- **Lines**: 1124
- **Types**: contextual, methodological
- **Excerpt**: «se añadió reintento explícito ante `database is locked` (`_retry_exec`). Quedan **3.351 URLs pendientes**; autos: **814**.»

### C139 — Presentación narrativa en diez actos

- **Section**: §39. Continuación del scrapeo y presentación narrativa
- **Lines**: 1126
- **Types**: contextual
- **Excerpt**: «Se redactó `Data/analisis_rentabilidad/PRESENTACION_STORYTELLING.md`: relato en 10 actos con personajes, conflicto, hallazgos, comparación con Egipto y llamada a la acción.»

### C140 — Renombre del repositorio en GitHub

- **Section**: §40. Renombre del repositorio en GitHub
- **Lines**: 1134–1141
- **Types**: contextual, result
- **Excerpt**: «antes: CarlosAntonioAceaJimenezCD/autodecide-habana [...] ahora: CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba»

### C141 — Permanencia de la carpeta local

- **Section**: §40. Renombre del repositorio en GitHub
- **Lines**: 1141
- **Types**: contextual
- **Excerpt**: «La carpeta local sigue siendo `~/Proyectos/ICD Automotive Market Project` para no romper las rutas absolutas de los servicios systemd»

### C142 — Descripción actual del repositorio

- **Section**: §40. Renombre del repositorio en GitHub
- **Lines**: 1143
- **Types**: contextual
- **Excerpt**: «Descripción actual del repo: *"Minimizar los gastos de la compra de coches en La Habana Cuba"*.»

### C143 — Gasolineras de Overpass/OSM

- **Section**: §41. Gasolineras, estaciones de carga y serie de precios del combustible
- **Lines**: 1150
- **Types**: contextual, result
- **Excerpt**: «**Overpass/OSM devolvió 137 gasolineras en La Habana** con coordenadas, marca, dirección y tipos de combustible. WhereFUEL usa esa misma base OSM (110 puntos en radio de 12 km).»

### C144 — Fuentes de estaciones de carga

- **Section**: §41. Gasolineras, estaciones de carga y serie de precios del combustible
- **Lines**: 1151
- **Types**: contextual, result
- **Excerpt**: «**Kargalaya** aportó 9 estaciones de carga con coordenadas y precio por hora [...] **Electromaps** añadió 3 referencias sin coordenadas. ChargeFinder respondió 403 en su API.»

### C145 — Capas del mapa regenerado

- **Section**: §41. Gasolineras, estaciones de carga y serie de precios del combustible
- **Lines**: 1152
- **Types**: contextual, result
- **Excerpt**: «Se crearon `Data/mapas/gasolineras.csv` (137) y `Data/mapas/estaciones_carga.csv` (12), y se regeneró `mapa_ofline.html` con tres capas: concesionarios (3), carga eléctrica (9) y gasolineras (137).»

### C146 — Base histórica de precios de combustible

- **Section**: §41. Gasolineras, estaciones de carga y serie de precios del combustible
- **Lines**: 1153–1154
- **Types**: contextual, result
- **Excerpt**: «`Data/combustible/precios_combustible.sqlite` con **18 observaciones** entre 20/08/2026 y 18/11/2026 [...] El script [...] es idempotente y el timer `precio-combustible.timer` lo ejecuta mensualmente»

### C147 — Régimen de combustible desde 2026

- **Section**: §41. Gasolineras, estaciones de carga y serie de precios del combustible
- **Lines**: 1156
- **Types**: contextual, citation-grounded
- **Excerpt**: «desde 07/02/2026 la venta oficial en CUP está suspendida y el combustible se vende en USD vía Ticket; desde mayo cada importador fija su precio. La B94 informal pasó de 3.500–5.000 CUP (ago) a 7.000–8.000 CUP (sep 2026).»

### C148 — Base unificada del mapa

- **Section**: §42. Base unificada del mapa y talleres
- **Lines**: 1164–1171
- **Types**: contextual, definitional
- **Excerpt**: «Se creó `Data/mapas/mapa_elementos.sqlite` como **fuente única** del mapa offline, con tablas `tipos` y `elementos`. Cada elemento guarda coordenadas, dirección, fuente, URL, teléfono, horario, precio, estado y detalle crudo en JSON.»

### C149 — Estado final de capas del mapa

- **Section**: §42. Base unificada del mapa y talleres
- **Lines**: 1173
- **Types**: contextual, result
- **Excerpt**: «Estado final: **131 gasolineras, 12 estaciones de carga, 25 concesionarios (17 con coords) y 22 talleres (todos con coords)».

### C150 — Anti-bot y geocodificación para talleres

- **Section**: §42. Base unificada del mapa y talleres
- **Lines**: 1175
- **Types**: contextual, methodological
- **Excerpt**: «**Cybo devolvió 403 con curl_cffi**, por lo que se aplicó el stack anti-bot disponible: `patchright` [...] y FlareSolverr en `http://127.0.0.1:8191/v1`. Las direcciones se geocodificaron con Nominatim y Photon»

### C151 — Acuerdo 9811 de 2024

- **Section**: §43. Apartado de «cuánto costaría moverse»
- **Lines**: 1185
- **Types**: contextual, citation-grounded
- **Excerpt**: «**Marco previo:** Acuerdo **9811 de 2024** del Consejo de Ministros, que fijaba precios minoristas de combustibles en CUP y USD.»

### C152 — Medidas de CIMEX del 7 de febrero de 2026

- **Section**: §43. Apartado de «cuánto costaría moverse»
- **Lines**: 1186
- **Types**: contextual, citation-grounded
- **Excerpt**: «CIMEX anunció medidas temporales —respaldadas por el MEP y el viceministro Oscar Pérez-Oliva Fraga— que suspendieron la venta en CUP y activaron **Ticket** (20 L por turno, 24 h para usarlo). No se localizó una resolución numerada nueva en la Gaceta Oficial; fue una disposición administrativa.»

### C153 — Autorización a actores no estatales

- **Section**: §43. Apartado de «cuánto costaría moverse»
- **Lines**: 1187
- **Types**: contextual, citation-grounded
- **Excerpt**: «**15/02/2026:** el Gobierno autorizó a **mipymes, cooperativas y otros actores económicos no estatales** a importar combustible directamente.»

### C154 — Circular Especial 03/2026

- **Section**: §43. Apartado de «cuánto costaría moverse»
- **Lines**: 1188
- **Types**: contextual, citation-grounded
- **Excerpt**: «**12–15/05/2026:** nota del MFP y **Circular Especial 03/2026 de CIMEX**; desde el 15/05 cada importador habilitado fija su precio según costo real de importación (1,80–2,60 USD/L).»

### C155 — Fuentes del apartado de combustible

- **Section**: §43. Apartado de «cuánto costaría moverse»
- **Lines**: 1191
- **Types**: contextual, citation-grounded
- **Excerpt**: «Fuentes: Cubadebate (07/02/2026), Directorio Cubano (12 y 15/05/2026), CubaTrámite (Circular 03/2026) y D-Cuba (20/02/2026).»

### C156 — Mantenimiento e infraestructura en el relato

- **Section**: §44. Reescritura de mantenimiento y retorno
- **Lines**: 1201–1202
- **Types**: contextual
- **Excerpt**: «incorpora los **22 talleres** y **25 concesionarios** geolocalizados [...] la depreciación de **−5,43 % anual** (p < 0,001), primas premium de **+21 %**, descuentos del **−22 %** para tier medio, **30 infravalorados**, **66 anomalías**»

### C157 — División del mercado en dos capas

- **Section**: §46. Apertura de la sección 3 del storytelling
- **Lines**: 1218
- **Types**: contextual
- **Excerpt**: «la división del mercado en dos capas —marketplaces y concesionarios/tiendas oficiales—»

### C158 — Envejecimiento desigual del parque

- **Section**: §47. Reescritura de la sección 4 del storytelling
- **Lines**: 1226
- **Types**: contextual
- **Excerpt**: «una narrativa sobre el envejecimiento desigual del parque: premium frente a autos de uso medio, combinación de antigüedad con kilometraje, estado y marca, y la idea de la marca como "seguro de valor".»

### C159 — Criterio de segmentación premium

- **Section**: §48. Definición de marcas premium y no premium
- **Lines**: 1236–1237
- **Types**: contextual, definitional
- **Excerpt**: «**Premium:** Mercedes-Benz, BMW, Audi, Lexus, Volvo, Porsche, Land Rover, Jaguar, Cadillac, Infiniti y Acura.»

### C160 — Niveles del modelo frente a los dos grupos narrativos

- **Section**: §48. Definición de marcas premium y no premium
- **Lines**: 1239
- **Types**: contextual, definitional
- **Excerpt**: «El modelo econométrico conserva sus tres niveles (`premium`, `medio`, `economico`); la narrativa usa solo dos grupos para ser legible.»

### C161 — Búsqueda de repositorios cubanos de automoción

- **Section**: §49. Búsqueda de repositorios cubanos de automoción
- **Lines**: 1247–1251
- **Types**: contextual, result
- **Excerpt**: «usando 31 consultas en español e inglés [...] Tras deduplicar se obtuvieron **648 repos**, de los que se depuraron **36 con relación directa o instrumental**»

### C162 — Duplicados detectados entre repositorios

- **Section**: §50. Consolidación de bases de los repositorios de autos
- **Lines**: 1259–1261
- **Types**: contextual, result
- **Excerpt**: «De los 7 resultantes, los dos repos de `randoloc` son duplicados en código [...] Se compararon 233 archivos de datos por hash y 76 CSV por contenido ordenado. Se detectaron 12 grupos de duplicados bytes y 11 de duplicados por contenido»

### C163 — Consolidación en una base con procedencia

- **Section**: §50. Consolidación de bases de los repositorios de autos
- **Lines**: 1263
- **Types**: contextual, result
- **Excerpt**: «se creó `Data/repos-autos-referencias/referencias_autos.sqlite` con **25 tablas** [...] De los 3.958 anuncios, **369 ya estaban en nuestra base** [...] y 3.589 son nuevos; no se modificó `revolico.sqlite`»

### C164 — Entrevistas cualitativas

- **Section**: §50. Consolidación de bases de los repositorios de autos
- **Lines**: 1265
- **Types**: contextual
- **Excerpt**: «Las entrevistas (30 + 30 + 8) son cualitativas, anónimas salvo el grupo de AutosxCuba —que incluye nombres y requiere cuidado— y aportan precios de combustible 2,00–2,70 USD/L, mantenimientos de 200 a 3.000 USD»

### C165 — Mejoras sin borrar archivos

- **Section**: §51. Mejoras del proyecto
- **Lines**: 1273
- **Types**: contextual, methodological
- **Excerpt**: «Se ejecutó una tanda de mejoras una por una, sin borrar archivos. Ninguna modificó las bases fuente: todas actúan sobre código, documentación y outputs derivados, con respaldos en `/tmp/opencode/`.»

### C166 — Ampliación de marcas en la configuración

- **Section**: §51. Mejoras del proyecto
- **Lines**: 1279
- **Types**: contextual
- **Excerpt**: «`config.py` incorporó Land Rover, Jaguar, Infiniti, Acura, BAIC, Daewoo, Opel, Volga, GAC, Bestune, Maxus, SsangYong y VW, con sus alias y tiers (premium/medio), para reducir los 442 anuncios en tier "desconocido".»

### C167 — Reconciliación de la encuesta

- **Section**: §51. Mejoras del proyecto
- **Lines**: 1281
- **Types**: contextual
- **Excerpt**: «el cruce filtra ahora `interes=1`, dando **28 interesados** (14 eléctrico, 10 combustión, 4 híbrido) en lugar de los 29 que contaba el script anterior»

### C168 — Fuentes descartadas

- **Section**: §52. Ampliación de fuentes de datos
- **Lines**: 1301
- **Types**: contextual
- **Excerpt**: «se descartaron fuentes sin valor verificable: `cubamotor.com` (dominio estacionado), agregadores de divisas con cifras contradictorias, datasets genéricos de Kaggle/UCI, Marketplace de Facebook (login obligatorio) y MININT/Dirección de Tránsito (sin estadísticas públicas de matriculaciones).»

### C169 — Estructura de los anuarios descargados

- **Section**: §53. Descarga completa de los anuarios del ONEI
- **Lines**: 1311
- **Types**: contextual
- **Excerpt**: «La estructura es `Anuario_Estadistico_AAAA/{PDF,Archivo,Excel}/`. Los años 2014–2016, 2018 y 2019 solo publican un PDF íntegro; 2020–2025 publican capítulos en PDF más un RAR de cuadros.»

### C170 — Herramienta de chunks y rama aislada

- **Section**: §54. Base de datos distribuida en chunks
- **Lines**: 1323–1325
- **Types**: contextual, methodological
- **Excerpt**: «Se añadió `Auxiliares/herramientas/db_chunks.py` con tres comandos (`split`, `verify`, `assemble`) [...] los chunks se publican en la rama huérfana `chunked-db`»

### C171 — Revisión de repositorios auxiliares

- **Section**: §55. Auditoría de fuentes, README y verificación final
- **Lines**: 1335
- **Types**: contextual, result
- **Excerpt**: «Se revisaron los 33 repositorios auxiliares. De los **7 cubanos**, solo `AutosxCuba` tiene ref remoto atrasada (24 commits), pero los 7 tienen cambios locales sin commitear»

### C172 — README, entorno y skills

- **Section**: §55. Auditoría de fuentes, README y verificación final
- **Lines**: 1337
- **Types**: contextual
- **Excerpt**: «Se reescribió `README.md` como página de entrada [...] Se añadió `requirements.txt` y un entorno `Auxiliares/.venv-py` funcional.»

### C173 — Corrección de un error de importación

- **Section**: §55. Auditoría de fuentes, README y verificación final
- **Lines**: 1339
- **Types**: contextual, methodological
- **Excerpt**: «La verificación del código detectó un `NameError` en `scripts/01_ingest.py` (`cfg` usado antes de importarse); se corrigió y se revalidó la importación y las funciones `parse_price`/`parse_number`.»

### C174 — Estructura versionada en GitHub

- **Section**: §56. Análisis de los anuarios y estructura de GitHub
- **Lines**: 1349
- **Types**: contextual, result
- **Excerpt**: «1.288 archivos, 157 objetos LFS, distribuidos en `Data` (836), `Hombros` (280), `Auxiliares` (110) y `Anexos` (56)»

### C175 — Copia de seguridad antes de insertar

- **Section**: §58. Incorporación de anuncios nuevos de iTENCEL
- **Lines**: 1365
- **Types**: contextual, methodological
- **Excerpt**: «Se hizo copia de seguridad de `itencel.sqlite` antes de escribir (`itencel.sqlite.bak-20261123`), se canonizaron las URLs con barra final para no duplicar y se reparó un título de interfaz usando el JSON-LD.»

### C176 — Documentación de funciones y modelos

- **Section**: §60. Inventario de funciones y modelos
- **Lines**: 1385
- **Types**: contextual, methodological
- **Excerpt**: «cada transformación y cada estimación del pipeline, con su justificación: normalización sintáctica y TRMI, features derivados, mediana y cuartiles, modelo hedónico log-lineal, VIF, Kruskal-Wallis, Welch t-test y detección de anomalías.»

### C177 — Sitio MkDocs y navegación Diátaxis

- **Section**: §61. Sitio MkDocs del proyecto
- **Lines**: 1393
- **Types**: contextual
- **Excerpt**: «La navegación sigue Diátaxis: **Historia** [...] **Referencia** [...] **Cómo** [...] y **Fuentes**»

### C178 — Compilación estricta del sitio

- **Section**: §61. Sitio MkDocs del proyecto
- **Lines**: 1395
- **Types**: contextual, result
- **Excerpt**: «`mkdocs build --strict` termina sin errores ni enlaces rotos. `site/` queda ignorado por Git»

### C179 — Accesibilidad del canal eléctrico

- **Section**: §62. Factibilidad del timelapse eléctrico
- **Lines**: 1403
- **Types**: contextual, result
- **Excerpt**: «el canal público de Telegram de la Empresa Eléctrica de La Habana (`t.me/s/EmpresaElectricaDeLaHabana`) responde HTTP 200 y publica mensajes fechados el 23/11/2026.»

### C180 — Primera corrida del scraper de circuitos

- **Section**: §62. Factibilidad del timelapse eléctrico
- **Lines**: 1403
- **Types**: contextual, result
- **Excerpt**: «en su primera corrida real capturó 40 mensajes, deduplicó por ID y dejó 35 circuitos sin luz, 23 mixtos y 2 con luz en `Data/mapas/circuitos_estado.sqlite`.»

### C181 — Correcciones de depuración en el timelapse

- **Section**: §62. Factibilidad del timelapse eléctrico
- **Lines**: 1403
- **Types**: contextual, methodological
- **Excerpt**: «Un informe de debug corrigió tres fallos (fecha local, filtro de relevancia y palabras de afectación) y las filas existentes se migraron sin borrarse.»

### C182 — Revisión de la narrativa como puerta de entrada

- **Section**: §63. Calidad del storytelling como puerta de entrada
- **Lines**: 1411
- **Types**: contextual
- **Excerpt**: «antes de la revisión tenía fricción inicial (metadatos antes de la promesa), un H2 genérico, el dato fuerte enterrado y ninguna llamada a la acción.»

### C183 — Arquitectura de automatización propuesta

- **Section**: §64. Automatización hacia una fuente auditable a dos años
- **Lines**: 1421
- **Types**: contextual, methodological
- **Excerpt**: «tres carriles desacoplados (recolectar, procesar, publicar), periodicidad realista en UTC, idempotencia por clave de fuente, marcas de agua, escrituras atómicas, cuarentena de datos inválidos, `SALUD.md` como dead-man's switch»

### C184 — Límite de ejecución sin internet

- **Section**: §65. Automatización operativa y coste de red
- **Lines**: 1429
- **Types**: contextual
- **Excerpt**: «Sin internet no se puede scrapear, pero sí ejecutar sin presencia del usuario; si falla la red, `SALUD.md` marca el periodo perdido y el siguiente ciclo `Persistent=true` lo recupera.»

### C185 — Cinco temporizadores y envoltorio con bloqueo

- **Section**: §65. Automatización operativa y coste de red
- **Lines**: 1429
- **Types**: contextual, methodological
- **Excerpt**: «Se activaron cinco timers `precio-*` [...] envoltorio `run_step.sh` con `flock` y estado atómico, validación con cuarentena y `SALUD.md`.»

### C186 — Distinción entre SIN DATOS y STALE

- **Section**: §65. Automatización operativa y coste de red
- **Lines**: 1429
- **Types**: contextual, methodological
- **Excerpt**: «`salud.py` ahora distingue `SIN DATOS` de `STALE` (antes generaba 10 alertas falsas) y el capturador escribe el ETag solo después del `commit` en SQLite»

### C187 — Configuración del temporizador de Revolico

- **Section**: §66. Extracción continua de Revolico y arquitectura de datos
- **Lines**: 1437
- **Types**: contextual, methodological
- **Excerpt**: «Se activó `precio-revolico.timer` cada 10 minutos con `--max-pages 3`, 2 descargadores, 2 procesadores y lotes de 50, sin `git push`. El job usa `flock` y un timeout de 45 min con 5 min de margen»

### C188 — Arquitectura de almacenamiento por fases

- **Section**: §66. Extracción continua de Revolico y arquitectura de datos
- **Lines**: 1439
- **Types**: contextual, methodological
- **Excerpt**: «Parquet particionado por `year/month`, watermark, rollups mensuales y evaluación de DuckDB/Polars/Arrow. En esta CPU `import duckdb` falla con `SIGILL`, así que la Fase 1 se hará con pyarrow/pandas»

### C189 — Archivos eliminados y mudanzas

- **Section**: §67. Optimización de espacio
- **Lines**: 1447
- **Types**: contextual
- **Excerpt**: «se quitaron: el entorno de Python antiguo e inservible (1,7 GB), dos versiones viejas de archivos grandes [...] Las leyes y las herramientas de scraping **no se borraron**: se mudaron a `~/Utilidades/Leyes` y `~/Utilidades/HerramientasScraping`.»

### C190 — Peso en GitHub y mapa de espacio

- **Section**: §68. Peso en GitHub y mapa de espacio
- **Lines**: 1455
- **Types**: contextual, result
- **Excerpt**: «La API de GitHub reporta **205.002 KB (0,20 GB)** para el historial normal; los archivos grandes se guardan aparte y su consumo en GitHub no lo expone la API. En local, esa copia ocupa 3,3 GB con 174 archivos.»

### C191 — Candidatos a optimización de espacio

- **Section**: §68. Peso en GitHub y mapa de espacio
- **Lines**: 1455
- **Types**: contextual
- **Excerpt**: «las tres copias partidas de Revolico (2,1 GB), el historial normal (1,0 GB), bibliotecas quizá innecesarias (66 MB de DuckDB, que además falla en esta CPU), repos de referencia (606 MB) y documentos descargados (261 MB).»


## Apéndice C — Mapa de literatura

# Literature Map

Nota de entrada. No se recibieron los inputs `queries_planned`, `hypotheses_planned`, `novelty_claims_preliminary`, `preset` ni `bibliography_extracted` descritos en el extractor, y no existe un archivo `<slug>.plan.md` en el destino ni en el caché de auditoría. En consecuencia: (a) el `preset: Standard` se asumió por defecto; (b) las queries se derivaron del título, objetivo y secciones 17–22, 34, 52–60 del documento; (c) la sección de hipótesis consigna comprobaciones derivadas, no hipótesis declaradas en un plan aprobado; (d) el documento no tiene bibliografía numerada, así que `Cited in document` se determina por mención nominal y `Document reference` se marca `(metadata incomplete)` cuando no hay número. Toda la metadata bibliográfica fue verificada en vivo el 2026-11-27; cuando un dato no pudo verificarse se marca explícitamente `(metadata incomplete)`.

## Clusters

### Cluster 1 — Asimetría de información y calidad en el mercado de vehículos usados

**Query**: `used car market asymmetric information adverse selection` (OpenAlex `fulltext.search`, 2026-11-27); query complementaria `market for lemons Akerlof` y búsqueda directa por DOI `10.2307/1879431`.

#### P001 — The Market for "Lemons": Quality Uncertainty and the Market Mechanism
- **Authors**: Akerlof, G. A.
- **Year**: 1970
- **Venue**: The Quarterly Journal of Economics
- **Citations**: 32562 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.2307/1879431
- **Layer**: L2
- **Cited in document**: yes
- **Document reference**: mención nominal «Akerlof» en las secciones 17, 19 y 20; sin numeración `(metadata incomplete)`
- **source_of_metadata**: OpenAlex (registro W2156109180, verificado por DOI)
- **Abstract analysis**: El artículo fundacional formaliza la selección adversa: cuando el comprador no observa la calidad, el precio promedio expulsa a los bienes buenos y puede colapsar el mercado. El documento lo invoca como marco teórico para justificar la captura de antigüedad, estado y palabras de defecto en los anuncios de La Habana. La concordancia es conceptual: ambos tratan la calidad como información privada del vendedor. La diferencia es de escala y de diseño: Akerlof construye un modelo teórico general, mientras el informe propone un esquema de datos y una clasificación empírica sin testear formalmente el mecanismo de selección adversa. El resumen indexado en OpenAlex contiene solo el índice de secciones, no un resumen sustantivo `(metadata incomplete)`.

#### P002 — Asymmetric Information, Adverse Selection and Online Disclosure: The Case of eBay Motors
- **Authors**: Lewis, G. M.
- **Year**: 2011 (el registro OpenAlex indexa la versión SSRN de 2010; la publicación AER es de 2011)
- **Venue**: American Economic Review
- **Citations**: 342 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1257/aer.101.4.1535
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W2157565524)
- **Abstract analysis**: Testea en eBay Motors la hipótesis de que la divulgación voluntaria de información privada por parte del vendedor mitiga la selección adversa y sostiene precios más altos; encuentra que las divulgaciones son determinantes importantes del precio. Es el puente natural entre Akerlof y el pipeline del informe: el documento registra defectos en el texto libre, estado, año y tipo de vendedor, pero no trata esas variables como una decisión estratégica de divulgación. Su ausencia es notable porque el informe afirma que el precio anunciado lleva implícita una señal de calidad y propone clasificar la calidad por antigüedad y palabras de defecto.

#### P003 — Adverse selection in the used-car market: evidence from purchase and repair patterns in the Consumer Expenditure Survey
- **Authors**: Peterson, J. R.; Schneider, H. S.
- **Year**: 2014
- **Venue**: The RAND Journal of Economics
- **Citations**: 34 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1111/1756-2171.12045
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W2108227678)
- **Abstract analysis**: Analiza la selección adversa tratando el auto como un ensamblaje de piezas, algunas con información simétrica y otras no, y usa patrones de compra y reparación para cuantificar el efecto sobre el volumen y la calidad del mercado secundario. Aporta una operacionalización de «costos ocultos» que el informe declara como requerimiento (sección 17) pero aún no mide: el documento lista la estimación de reacondicionamiento como tarea pendiente en la sección 20. La diferencia es de fuente de datos: encuestas de gasto estadounidenses frente a anuncios web habaneros.

#### P004 — Price Discontinuities in an Online Market for Used Cars
- **Authors**: Englmaier, F.; Schmöller, A.; Stowasser, T.
- **Year**: 2017
- **Venue**: Management Science
- **Citations**: 50 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1287/mnsc.2016.2714
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W1956884180)
- **Abstract analysis**: Documenta discontinuidades sistemáticas de precio en umbrales salientes de edad y kilometraje en un marketplace europeo: autos idénticos registrados en meses contiguos de años distintos pueden diferir hasta cinco veces más que autos dentro del mismo año, y aparece un patrón análogo en las marcas de 10.000 km. El informe construye series `precios_por_anio.csv` y comparables por modelo ±2 años, lo que hace relevante la advertencia: el año y el kilometraje no entran de forma lineal en el precio. La literatura sugiere además que los saltos pueden reflejar procesamiento burdo de información o fricciones de búsqueda, algo que el modelo log-lineal del documento no considera.

#### P005 — Warranty, Seller Reputation, and Buyer Experience: Evidence From EBAY Used Car Auctions
- **Authors**: Che, X.; Katayama, H.; Lee, P.; Shi, N.
- **Year**: 2019
- **Venue**: The Journal of Industrial Economics
- **Citations**: 13 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1111/joie.12213
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W2967052949)
- **Abstract analysis**: Encuentra que la garantía genera una prima de precio cuyo tamaño disminuye cuando el vendedor tiene reputación consolidada, y que los vendedores profesionales se benefician menos de la sustitubilidad entre garantía y reputación. El informe distingue canales locales e importación y registra tipo de vendedor, pero no incorpora garantía ni reputación como covariables. La superposición es el interés por la identidad del vendedor; la diferencia es que aquí esas señales se testean sobre precio final de subasta, no sobre precio pedido.

#### P006 — Adverse Selection and Reputation Systems in Online Auctions: Evidence from eBay Motors
- **Authors**: Wolf, J. R.; Muhanna, W. A.
- **Year**: 2005
- **Venue**: ICIS 2005 Proceedings (AIS Electronic Library)
- **Citations**: 28 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: http://aisel.aisnet.org/cgi/viewcontent.cgi?article=1273&context=icis2005
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W2166780536)

#### P007 — A model of the used car market with lemons and leasing
- **Authors**: Sultan, A.
- **Year**: 2009
- **Venue**: Applied Economics
- **Citations**: 11 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1080/00036840802314556
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W1965378525)

#### P008 — A Markovian model market—Akerlof's lemons and the asymmetry of information
- **Authors**: Tilles, P. F. C.; Ferreira, F. F.; Francisco, G.; Pereira, C. de B.; Sarti, F. M.
- **Year**: 2011
- **Venue**: Physica A: Statistical Mechanics and its Applications
- **Citations**: 9 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1016/j.physa.2011.03.007
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W1499498447)

### Cluster 2 — Modelos de precio, regresión hedónica y depreciación

**Query**: `hedonic price model used car depreciation` y `used car price prediction machine learning` (OpenAlex `fulltext.search`); query arXiv `all:"used car price"`; búsqueda adicional `Used Linear Regression For Used Car Price Prediction`.

#### P009 — Nonlinear Depreciation and Brand Heterogeneity in Chinese Used-Car Listing Prices: An Interpretable Hedonic Regression and Out-of-Sample Evaluation
- **Authors**: Du, Z.; Yang, Z.; Zhang, Y.; Li, S.; Liu, Y.
- **Year**: 2026
- **Venue**: Advances in Economics, Management and Political Sciences
- **Citations**: 0 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.54254/2754-1169/2026.38524
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W7225188457)
- **Abstract analysis**: Sobre 1.000 anuncios chinos divididos en 800 entrenamiento y 200 prueba, estima tres especificaciones OLS log-lineales anidadas y muestra que la relación edad–precio es no lineal y heterogénea por marca premium; el kilometraje orthogonalizado deja de ser significativo al incluir los términos de edad e interacción. Es el paralelo metodológico más cercano al informe: este también usa una especificación `log(precio) ~ car_age + condition_score + C(brand_tier)`, reporta una caída de −5,43 % anual y después reconoce que la pendiente no resiste la corrección por kilometraje. La coincidencia en la forma funcional y en la cautela interpretativa es alta; la diferencia es de tamaño muestral y de contexto de precios pedidos, y el trabajo chino advierte explícitamente que sus resultados son descriptivos dentro de la muestra, no causales.

#### P010 — The pricing of used electric vehicles via machine learning and hedonic price model: A comparative study
- **Authors**: Kang, W.; Fu, X.
- **Year**: 2026
- **Venue**: Computers & Industrial Engineering
- **Citations**: 2 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1016/j.cie.2026.111964
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W7134932779); resumen no indexado `(metadata incomplete)`

#### P011 — Depreciation Patterns in the UAE Used Car Market: Evidence from Dubizzle Listings
- **Authors**: Miranda, A. M.; Alavi, A. B.; Gella, M. A.
- **Year**: 2026
- **Venue**: Journal of Business Insight and Innovation
- **Citations**: 0 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.63544/jbii.v5i6.110
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W7171439123)
- **Abstract analysis**: Con 400 anuncios de Dubizzle y OLS sobre precio, edad, kilometraje y marca, estima una caída de unos 4.263 AED por año adicional (F = 27,16; p < 0,001; R² = 0,256), mientras el kilometraje no resulta significativo (p = 0,077) y está fuertemente correlacionado con la edad (r = 0,639). Es un casi-experimento del problema del informe: también trabaja con precios pedidos, también usa una muestra pequeña y también obtiene una tasa de depreciación que puede ser frágil frente a la multicolinealidad. La diferencia es que este estudio sí reporta una pendiente anual significativa, mientras el informe, con 744 autos únicos, retira la afirmación de depreciación significativa en la sección 59.

#### P012 — Price Hedonics: A Critical Review
- **Authors**: Hulten, C. R.
- **Year**: 2003
- **Venue**: Federal Reserve Bank of New York Economic Policy Review
- **Citations**: 82 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://newyorkfed.org/research/epr/03v09n3/0309hult.pdf
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W2164155028)

#### P013 — Modeling unobserved heterogeneity in hedonic price models
- **Authors**: Francke, M.; Van de Minne, A.
- **Year**: 2020
- **Venue**: Real Estate Economics
- **Citations**: 43 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1111/1540-6229.12320
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W3024067924)
- **Abstract analysis**: Revisa la especificación hedónica cuando la heterogeneidad no observada puede sesgar los coeficientes de calidad. El documento aplica una especificación hedónica log-lineal con `brand_tier` como proxy de calidad y advierte que la prima premium dejó de sostenerse tras corregir kilometraje (sección 60, p mínimo 0,165). El trabajo aporta el respaldo metodológico para interpretar esa inestabilidad como un problema de heterogeneidad no observada y no como ausencia de efecto. La diferencia es sustantiva: es literatura de precios inmobiliarios, no automotriz.

#### P014 — Car Price Prediction using Machine Learning Techniques
- **Authors**: Gegić, E.; Isaković, B.; Keco, D.; Mašetić, Z.; Kevrić, J.
- **Year**: 2019
- **Venue**: TEM Journal
- **Citations**: 188 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.18421/tem81-16
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4288610071)
- **Abstract analysis**: Recolecta anuncios del portal `autopijaca.ba` con un scraper propio en PHP, aplica ANN, SVM y Random Forest y reporta exactitud de 87,38 % al integrar el modelo en una aplicación Java. Es el antecedente más directo de la combinación scraping + modelado de precios que el informe implementa con Revolico y los concesionarios. La superposición es el flujo completo desde anuncios web hasta predicción; la diferencia es que no documenta deduplicación, procedencia por fuente ni separación de monedas, que son justamente los ejes del informe.

#### P015 — Using Linear Regression For Used Car Price Prediction
- **Authors**: Mutİ, S.; Yıldız, K.
- **Year**: 2023
- **Venue**: International Journal of Computational and Experimental Science and Engineering
- **Citations**: 40 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.22399/ijcesen.1070505
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4323355978)
- **Abstract analysis**: Evalúa regresión lineal sobre características de vehículos turcos de 2020 y obtiene R² de 73 % con un tercio de los datos reservado para prueba. Confirma que una especificación lineal simple alcanza ajuste aceptable en mercados de anuncios, pero también que el resultado depende fuertemente del preprocesamiento. El informe adopta una forma log-lineal con menos variables y reporta R² y VIF como parte de su documentación de modelo (sección 60); la diferencia es la escala: 40 citas frente a una muestra local de cientos de autos, con cobertura parcial de año y kilometraje.

#### P016 — Price Prediction of Used Cars Using Machine Learning
- **Authors**: Jin, C.
- **Year**: 2021
- **Venue**: IEEE International Conference on Emergency Science and Information Technology (ICESIT)
- **Citations**: 42 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1109/icesit53460.2021.9696839
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4211143196)

#### P017 — Used Car Price Prediction with Pyspark
- **Authors**: Ahtesham, M.; Zulfiqar, J.
- **Year**: 2022
- **Venue**: Lecture Notes in Networks and Systems (Springer)
- **Citations**: 15 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1007/978-3-031-01942-5_17
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4285160726)

#### P018 — ProbSAINT: Probabilistic Tabular Regression for Used Car Pricing
- **Authors**: Madhusudhanan, K.; Behrens, G.; Stubbemann, M.; Schmidt-Thieme, L.
- **Year**: 2024
- **Venue**: arXiv:2403.03812; IEEE BigData 2024, Industry & Government Track
- **Citations**: unknown (metadata incomplete; el registro arXiv no expone conteo y Semantic Scholar devolvió 403)
- **URL**: https://arxiv.org/abs/2403.03812
- **Layer**: L3
- **Cited in document**: no
- **source_of_metadata**: arXiv API + texto completo HTML (verificado 2026-11-27T05:30:00Z)
- **Abstract analysis**: Extiende SAINT con una cabeza probabilística entrenada por verosimilitud negativa para predecir media y desviación del precio, y muestra desempeño superior a CatBoost, NGBoost y MC-dropout en NLL sobre aproximadamente 2 millones de registros B2C. Introduce además pronóstico dinámico condicionado a los días de permanencia del anuncio, una noción directamente relacionada con las series de snapshots del informe. La lectura de Introducción, Método y Conclusión confirma dos lecciones aplicables: el tiempo de permanencia es una variable de decisión comercial, y la incertidumbre de la predicción debe reportarse, no solo el punto. El informe reporta puntos y p-valores pero no intervalos ni incertidumbre calibrada; la escala de datos (2 M frente a 744 autos) es la diferencia principal.

#### P019 — How much is my car worth? A methodology for predicting used cars prices using Random Forest
- **Authors**: Pal, N.; Arora, P.; Sundararaman, D.; Kohli, P.; Palakurthy, S. S.
- **Year**: 2017
- **Venue**: arXiv:1711.06970 (FICC, Camera Ready)
- **Citations**: unknown (metadata incomplete; Semantic Scholar devolvió 403)
- **URL**: https://arxiv.org/abs/1711.06970
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: arXiv API (verificado 2026-11-27T05:30:00Z)
- **Abstract analysis**: Entrena un Random Forest de 500 árboles tras EDA para identificar variables correlacionadas con el precio, con exactitud de entrenamiento 95,82 % y de prueba 83,63 %, yMotiva el problema por la asequibilidad en países en desarrollo y por precios irreales publicados por vendedores. El segundo motivo coincide casi literalmente con la problemática del informe: anuncios con precios pedidos que requieren filtros y validación. La diferencia es metodológica: EDA + Random Forest frente al esquema de limpieza auditada y regresión hedónica del proyecto cubano; además no separa entre monedas ni documenta deduplicación.

#### P020 — Second Hand Price Prediction for Tesla Vehicles
- **Authors**: Arefin, S. E.
- **Year**: 2021
- **Venue**: arXiv:2101.03788
- **Citations**: unknown (metadata incomplete; Semantic Scholar devolvió 403)
- **URL**: https://arxiv.org/abs/2101.03788
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: arXiv API (verificado 2026-11-27T05:15:00Z)

### Cluster 3 — Ética, legalidad, procedencia y calidad de datos

**Query**: `web scraping research data collection ethics legal` y `data provenance quality validation pipeline scraped data` (OpenAlex `fulltext.search`).

#### P021 — Legality and Ethics of Web Scraping
- **Authors**: Krotov, V.; Johnson, L.; Silva, L.
- **Year**: 2020
- **Venue**: Communications of the Association for Information Systems
- **Citations**: 224 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.17705/1cais.04724
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W3125851220)
- **Abstract analysis**: Revisa literatura legal y de privacidad para identificar áreas de riesgo y preguntas concretas que investigadores y profesionales deben responder antes de recolectar datos web. El informe declara una regla operativa equivalente —no eludir mecanismos anti-automatización y registrar HTTP 403/429 como limitación— pero no cita ningún marco de cumplimiento. La superposición es directa con la sección 10; la diferencia es de jurisdicción: la literatura analiza sobre todo los Estados Unidos y Europa, mientras el informe se remite a normas cubanas que aún deben verificarse antes de publicar.

#### P022 — Web scraping for research: Legal, ethical, institutional, and scientific considerations
- **Authors**: Brown, M. A.; Gruen, A.; Maldoff, G.; Messing, S.; Sanderson, Z.; Zimmer, M. T.
- **Year**: 2025
- **Venue**: Big Data & Society
- **Citations**: 118 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1177/20539517251381686
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4416422179)
- **Abstract analysis**: Propone un marco de cuatro dimensiones —legal, ética, institucional y científica— para investigadores que recurren al scraping cuando los canales oficiales se restringen, con recomendaciones para recolectar, almacenar y compartir datos de forma legítima. Encaja con la decisión del informe de conservar `raw_html`, `tables_json` y `jsonld_json` como respaldo de trazabilidad y de no publicar datos personales. La diferencia es que el marco se dirige a investigadores de ciencias sociales con base en los Estados Unidos y no aborda la particularidad de marketplaces cubanos ni la separación entre tasa oficial e informal.

#### P023 — A Survey of Data Quality Requirements That Matter in ML Development Pipelines
- **Authors**: Priestley, M.; O'Donnell, F.; Simperl, E. P. B.
- **Year**: 2023
- **Venue**: Journal of Data and Information Quality
- **Citations**: 153 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1145/3592616
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4366407820)
- **Abstract analysis**: Cuestiona la noción clásica de «aptitud para el uso» y propone organizar los requisitos de calidad por etapa del ciclo de vida de ML y por categoría (intrínseca, contextual, representacional, accesibilidad). El informe despliega exactamente esa lógica por etapas: deduplicación, clasificación en `autos`/`revision`, columnas de auditoría, validación con cuarentena y manifiestos con hashes en las secciones 16, 51 y 64–66. La diferencia es que la encuesta es normativa y general, mientras el documento describe una implementación concreta sin contrastarla con un marco de calidad reconocido.

#### P024 — Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability in LLMs
- **Authors**: Hohensinner, R.; Mutlu, B.; Mendoza Estrada, I. G.; Vukovic, M.; Kopeinik, S.; Kern, R.
- **Year**: 2026
- **Venue**: arXiv:2601.14311 (manuscrito enviado a ACM Computing Surveys)
- **Citations**: 13 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://arxiv.org/abs/2601.14311
- **Layer**: L3
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W7125390097) + texto completo HTML (verificado 2026-11-27T05:35:00Z)
- **Abstract analysis**: Sistematiza 95 publicaciones en torno a procedencia, trazabilidad y transparencia, con pilares de sesgo, privacidad y herramientas, y distingue formalmente procedencia (origen) de linaje (transformaciones a lo largo del ciclo de vida). El informe persigue esa misma distinción con `provenancia`, hashes SHA-256, watermarks e idempotencia por clave de fuente, aunque orientado a datos de mercado y no a modelos de lenguaje. La lectura de Introducción, Preliminares y Herramientas confirma que «registro de orígenes y procesamiento» es la definición estándar que el proyecto adopta de facto. La diferencia es el dominio: aquí la trazabilidad se persigue hasta pesos y tokens; en el informe, hasta la fila de anuncio y su fuente.

#### P025 — Data Isotopes for Data Provenance in DNNs
- **Authors**: Wenger, E.; Li, X.; Zhao, B. Y.; Shmatikov, V.
- **Year**: 2024
- **Venue**: Proceedings on Privacy Enhancing Technologies
- **Citations**: 24 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.56553/popets-2024-0024
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4387857422)

#### P026 — A Pipeline for Integrating and Analyzing Public Business Data in Albania Using Web Scraping and Machine Learning
- **Authors**: Muça, M.; Bani, K.; Alla, A.
- **Year**: 2026
- **Venue**: International Journal of Advanced Computer Science and Applications
- **Citations**: 0 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.14569/ijacsa.2026.0170845
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W7204683515)

#### P027 — The Ethics of Web Scraping In Research: A Review
- **Authors**: Essien, I. A.; Adebayo, A. O.; Afuwape, A. A.; Eboseremen, B. O.; Oladega, F.; Soneye, O. M.
- **Year**: 2023
- **Venue**: Journal of Frontiers in Multidisciplinary Research
- **Citations**: 22 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.54660/.jfmr.2023.4.1.529-538
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4413861058)

#### P028 — The Legality and Ethics of Web Scraping in Archaeology
- **Authors**: Paige, J.
- **Year**: 2024
- **Venue**: Advances in Archaeological Practice
- **Citations**: 8 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1017/aap.2023.42
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4394961981)

### Cluster 4 — Cuba: divisas informales, movilidad y asequibilidad

**Query**: `Cuba informal exchange rate dual currency economy`, `electric vehicle adoption Cuba willingness to pay` y `vehicle affordability price income car ownership` (OpenAlex `fulltext.search`).

#### P029 — Using AI in the informal currency market: evidence from Cuba
- **Authors**: Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A.
- **Year**: 2024
- **Venue**: Applied Economics
- **Citations**: 1 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1080/00036846.2024.2416091
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4403850866)
- **Abstract analysis**: Describe una metodología para extraer con PLN datos de grupos de redes sociales y sitios clasificados y calcular un tipo de cambio paralelo, implementada desde 2021, y valida la serie con modelos VAR e índices de spillover frente a un tipo oficial fijo y sobrevaluado. Es el precedente académico directo del uso del TRMI de elTOQUE en el informe: convierte señales informales en serie temporal verificable y mantiene separadas las tasas oficiales. La diferencia es que el informe toma la tasa publicada como insumo y no construye su propio estimador, y que su serie de precios es de autos, no de divisas.

#### P030 — Electromobility and Energy Transition in Cuba
- **Authors**: Castro Fernández, M.; Vilaragut Llanes, M.; Hernández, J. C.
- **Year**: 2024
- **Venue**: Sustainability
- **Citations**: 4 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.3390/su16229688
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4404141321)
- **Abstract analysis**: Analiza la introducción de energías renovables y la electrificación del transporte en Cuba, e identifica limitaciones y barreras de movilidad además de una hoja de ruta que incluye estaciones de carga y talleres de reparación/mantenimiento. Se solapa con las secciones 36, 41 y 42 del informe, que inventarian 12 estaciones de carga, 22 talleres y la dependencia de los circuitos eléctricos. La diferencia es de escala y propósito: el artículo propone política energética nacional, mientras el informe geolocaliza infraestructura existente para contextualizar el costo de moverse.

#### P031 — Cuba's Underground Economy
- **Authors**: Ritter, A. R. M.
- **Year**: 2004
- **Venue**: RePEc (Carleton Economic Papers)
- **Citations**: 20 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: http://www.carleton.ca/economics/wp-content/uploads/cep04-12.pdf
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W2188956700)

#### P032 — Currency exchange in post-ordenamiento Cuba: An exploration of institutional waiting for dollar purchases
- **Authors**: Ávila Castellanos, D. D.
- **Year**: 2024
- **Venue**: Revista Foro Cubano
- **Citations**: 2 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.22518/jour.rfc/2023.6a02
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4402744941)

#### P033 — The geography of car ownership in Mexico City: a joint model of households' residential location and car ownership decisions
- **Authors**: Guerra, E.
- **Year**: 2015
- **Venue**: Journal of Transport Geography
- **Citations**: 113 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1016/j.jtrangeo.2015.01.014
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W2015444861)

#### P034 — Transitions into and out of Car Ownership among Low-Income Households in the United States
- **Authors**: Klein, N. J.; Basu, R.; Smart, M. J.
- **Year**: 2023
- **Venue**: Journal of Planning Education and Research
- **Citations**: 27 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1177/0739456x231163755
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4367844458)

#### P035 — Auto insurance affordability and the gap in car ownership: An analysis of transportation burden
- **Authors**: Srisan, T.; Ong, P. M.; Bills, T. S.
- **Year**: 2026
- **Venue**: Transport Policy
- **Citations**: 0 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1016/j.tranpol.2026.104491
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W7222828916)

### Cluster 5 — Señales de precio en marketplaces y lógica de comparables

**Query**: `online marketplace listing price asking transaction bias` y `used car market quality uncertainty Ebay motors online disclosure` (OpenAlex `fulltext.search`).

#### P036 — Reducing Interference Bias in Online Marketplace Pricing Experiments
- **Authors**: Holtz, D.; Lobel, R.; Liskovich, I.; Aral, S.
- **Year**: 2020
- **Venue**: SSRN Electronic Journal
- **Citations**: 59 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.2139/ssrn.3583836
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W3020710313)

#### P037 — Product Selection in Online Marketplaces
- **Authors**: Etro, F.
- **Year**: 2020
- **Venue**: Journal of Economics & Management Strategy
- **Citations**: 106 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1111/jems.12428
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W3163415732)

#### P038 — Market prices of remanufactured, used and new items: Evidence from eBay
- **Authors**: Quariguasi Frota Neto, J.; Bloemhof-Ruwaard, J. M.; Corbett, C. J.
- **Year**: 2015
- **Venue**: International Journal of Production Economics
- **Citations**: 136 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1016/j.ijpe.2015.02.006
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W1991842457)

## Recency distribution

El documento no contiene una sección de referencias bibliográficas numeradas. La única obra académica citada por nombre es P001 (1970); las demás fuentes mencionadas son normas, informes institucionales y repositorios, sin año bibliográfico asignable en este esquema. Por eso la columna derecha es 1 en `≤2021` y 0 en el resto.

| Year | In map | In document bibliography |
|---|---:|---:|
| 2026 | 7 | 0 |
| 2025 | 1 | 0 |
| 2024 | 6 | 0 |
| 2023 | 3 | 0 |
| 2022 | 1 | 0 |
| ≤2021 | 20 | 1 |

## Venue distribution

| Venue | Count in map |
|---|---:|
| arXiv (incl. arXiv/IEEE BigData) | 3 |
| Applied Economics | 2 |
| The Quarterly Journal of Economics | 1 |
| American Economic Review | 1 |
| The RAND Journal of Economics | 1 |
| Management Science | 1 |
| The Journal of Industrial Economics | 1 |
| ICIS Proceedings (AISeL) | 1 |
| Physica A | 1 |
| Advances in Economics, Management and Political Sciences | 1 |
| Computers & Industrial Engineering | 1 |
| Journal of Business Insight and Innovation | 1 |
| Federal Reserve Bank of New York Economic Policy Review | 1 |
| Real Estate Economics | 1 |
| TEM Journal | 1 |
| IJCESEN | 1 |
| IEEE ICESIT | 1 |
| Lecture Notes in Networks and Systems (Springer) | 1 |
| Communications of the AIS | 1 |
| Big Data & Society | 1 |
| Journal of Data and Information Quality | 1 |
| Proceedings on Privacy Enhancing Technologies | 1 |
| IJACSA | 1 |
| Journal of Frontiers in Multidisciplinary Research | 1 |
| Advances in Archaeological Practice | 1 |
| RePEc (Carleton Economic Papers) | 1 |
| Revista Foro Cubano | 1 |
| Journal of Transport Geography | 1 |
| Journal of Planning Education and Research | 1 |
| Transport Policy | 1 |
| SSRN Electronic Journal | 1 |
| Journal of Economics & Management Strategy | 1 |
| International Journal of Production Economics | 1 |

## Likely missing important works

### P002 — Asymmetric Information, Adverse Selection and Online Disclosure: The Case of eBay Motors
- Lewis, 2011, American Economic Review, 342 citas.
- **Cluster**: Asimetría de información y calidad en el mercado de vehículos usados.
- **Why likely missing**: Primero por citas en el clúster que da soporte teórico a una afirmación cargada del documento (la calidad se infiere de atributos visibles en el anuncios). Es el eslabón empírico entre Akerlof, citado, y la captura de defectos y tipo de vendedor; su ausencia deja el marco teórico sin la evidencia que lo conecta con precios observados en plataformas.

### P004 — Price Discontinuities in an Online Market for Used Cars
- Englmaier, Schmöller & Stowasser, 2017, Management Science, 50 citas.
- **Cluster**: Asimetría de información y calidad en el mercado de vehículos usados.
- **Why likely missing**: Top-5 por citas en un clúster directamente relevante para la serie `precios_por_anio.csv` y los comparables por modelo ±2 años. Advierte que el año de matrícula y el kilometraje operan como umbrales salientes, no como predictores lineales; el informe estima una pendiente log-lineal anual y después la retira, sin discutir esta alternativa.

### P014 — Car Price Prediction using Machine Learning Techniques
- Gegić et al., 2019, TEM Journal, 188 citas.
- **Cluster**: Modelos de precio, regresión hedónica y depreciación.
- **Why likely missing**: Obra más citada de su subárea y casi gemela metodológica del proyecto: scraping de portal de anuncios, extracción de atributos y modelo de predicción integrado en una aplicación. Cubre exactamente la combinación que el informe presenta como propio y permitiría situar la novedad del manejo de monedas, deduplicación y procedencia.

### P021 — Legality and Ethics of Web Scraping
- Krotov, Johnson & Silva, 2020, Communications of the AIS, 224 citas.
- **Cluster**: Ética, legalidad, procedencia y calidad de datos.
- **Why likely missing**: Obra fundacional del subárea que el informe declara central en la sección 10 sin referirla. La regla operativa «no eludir anti-automatización; registrar 403/429 como limitación» es una instancia de las preguntas que este trabajo formula para investigadores; citarlo reforzaría la distinción entre decisión técnica y justificación normativa.

### P023 — A Survey of Data Quality Requirements That Matter in ML Development Pipelines
- Priestley, O'Donnell & Simperl, 2023, Journal of Data and Information Quality, 153 citas.
- **Cluster**: Ética, legalidad, procedencia y calidad de datos.
- **Why likely missing**: Primera por citas del clúster de calidad de datos y directamente aplicable a la fase 7 (unificación, limpieza y control de calidad). El informe implementa validación por etapas pero no la enmarca en un marco reconocido, lo que deja sin respaldo la afirmación de que la arquitectura de colas y cuarentena es una decisión metodológica y no solo operativa.

### P022 — Web scraping for research: Legal, ethical, institutional, and scientific considerations
- Brown et al., 2025, Big Data & Society, 118 citas.
- **Cluster**: Ética, legalidad, procedencia y calidad de datos.
- **Why likely missing**: Cumple el criterio de publicación reciente del mismo tema (menos de 18 meses) y es la referencia más actualizada sobre cómo almacenar y compartir datos recolectados por scraping. La decisión del informe de conservar HTML crudo y excluir datos personales coincide con sus recomendaciones.

### P033 — The geography of car ownership in Mexico City
- Guerra, 2015, Journal of Transport Geography, 113 citas.
- **Cluster**: Cuba: divisas informales, movilidad y asequibilidad.
- **Why likely missing**: Obra influyente sobre asequibilidad y tenencia de automóvil en América Latina; el informe propone `asequibilidad = precio / salario` como métrica de la fase 8 sin antecedente regional. Su ausencia deja sin contexto comparativo una de las variables derivadas previstas en el marco analítico.

### P024 — Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability
- Hohensinner et al., 2026, arXiv:2601.14311, 13 citas.
- **Cluster**: Ética, legalidad, procedencia y calidad de datos.
- **Why likely missing**: Trabajo reciente del mismo tema que define con precisión la distinción entre procedencia y linaje que el informe aplica de facto en `provenancia`, hashes y manifiestos. Es la referencia contemporánea que permitiría declarar esa arquitectura como una adopción deliberada y no una solución ad hoc.

## Hypothesis checks (from plan)

No se recibieron `hypotheses_planned`. Las comprobaciones siguientes son observaciones derivadas de las afirmaciones cargadas del propio documento (secciones 17–20, 34, 52, 59–60); no son tests de hipótesis declaradas en un plan aprobado y no emiten veredicto.

### H1 — Los precios pedidos recogidos de anuncios pueden sustituir a estadísticas oficiales de transacción (derivada de §18 y §52)

La literatura coincide en que los datos de anuncios son una señal de precios pedidos y no de transacciones: Lewis (P002) muestra que el precio de subasta depende de divulgaciones del vendedor; Holtz et al. (P036) documentan interferencia entre participantes en experimentos de precios de marketplace; Etro (P037) modela la selección de productos en marketplaces; Quariguasi Frota Neto et al. (P038) comparan precios de bienes remanufacturados, usados y nuevos en eBay. Ninguno de estos trabajos sostiene que el precio anunciado sea equivalente al precio transado. El informe ya registra la salvedad en su auditoría de fuentes («precios pedidos, no transaccionados»), de modo que la evidencia encontrada respalda la cautela y no la sustitución. Queda sin dirección empírica la compatibilidad entre anuncios y estadísticas oficiales cubanas, porque los anuarios ONEI revisados no contienen series de parque ni de matriculaciones según el propio documento (§56).

### H2 — La tasa de depreciación anual estimada es estable y significativa (derivada de §34, §59 y §60)

El estado de la evidencia es mixto y desfavorable a una tasa única. Du et al. (P009), con especificación log-lineal anidada casi idéntica a la del informe, muestran que la relación edad–precio es no lineal y que el kilometraje pierde significancia al introducir términos de edad e interacción. Miranda et al. (P011) obtienen una pendiente anual significativa pero con R² de 0,256, kilometraje no significativo (p = 0,077) y correlación alta entre edad y kilometraje (r = 0,639). Englmaier et al. (P004) documentan saltos de precio en umbrales de año y cada 10.000 km. Francke y Van de Minne (P013) advierten sobre heterogeneidad no observada en modelos hedónicos. Este conjunto es compatible con la decisión del informe de retirar la afirmación de −5,43 % anual tras corregir kilometraje (p mínimo 0,165) y sugiere que la inestabilidad es un resultado esperable de la especificación, no una anomalía del proyecto.

### H3 — El marco de asimetría de información es aplicable al mercado de usados de La Habana (derivada de §17, §19 y §20)

Akerlof (P001) proporciona el marco y el documento lo cita explícitamente. La evidencia posterior muestra que los mecanismos que mitigan la asimetría son observables en datos de anuncios: divulgación voluntaria (P002), garantía y reputación del vendedor (P005), patrones de reparación como proxy de calidad oculta (P003) y alternativas institucionales como el leasing (P007). El informe captura año, texto de defectos y tipo de vendedor, pero no ha convertido esas variables en prueba del mecanismo; los campos de condición y costos de reacondicionamiento siguen en la lista de datos faltantes (§20). La literatura apoya la relevancia del marco, aunque no validan directamente su validez en un mercado con doble tasa de cambio y parque automotor informal.

### H4 — La recolección por scraping es sostenible sin eludir mecanismos anti-automatización (derivada de §10 y §11)

Krotov et al. (P021) y Brown et al. (P022) coinciden en que la legitimidad depende de revisar términos de uso, privacidad y normativa institucional antes de recolectar, no solo de la viabilidad técnica. Priestley et al. (P023) y Hohensinner et al. (P024) añaden que la calidad y la procedencia deben documentarse por etapa. El informe satisface la parte operativa —respeta HTTP 403/429, registra como limitación el bloqueo de carrosw y Cybo, conserva trazabilidad y evita datos personales— pero las fuentes revisadas no cubren el derecho cubano aplicable, que el propio informe deja como verificación pendiente antes de publicar. La evidencia encontrada apoya la coherencia procedimental; no permite pronunciarse sobre el cumplimiento legal en Cuba.

### H5 — La separación entre tasa oficial e informal es metodológicamente necesaria (derivada de §23, §52 y §18)

Vidal Alejandro et al. (P029) construyen una serie de tipo de cambio paralelo a partir de redes sociales y clasificados y la validan econométricamente, manteniendo separado el tipo oficial fijo y sobrevaluado. Ávila Castellanos (P032) documenta la experiencia cubana de espera institucional para comprar dólares. El informe adopta la TRMI de elTOQUE para convertir precios y conserva la tasa oficial de la BCC como referencia contrastada, sin mezclarlas. La literatura confirma que esa separación es una decisión metodológica estándar en el contexto cubano, aunque no resuelve cuál de las dos tasas debe emplearse para medir asequibilidad frente al salario.

## Sources used

- WebSearch queries: 8 intentos, todos con HTTP 403; registrados como fallo sostenido del proveedor.
- WebFetch URLs: 26 (OpenAlex API, arXiv API/abs/HTML y Crossref API).
- Semantic Scholar API hits: 0 (HTTP 403 en la única llamada intentada).
- OpenAlex API hits: 92 registros devueltos a partir de 18 consultas (búsquedas por texto completo, búsqueda por DOI y filtros por ID para resúmenes); 38 trabajos únicos incorporados al mapa.
- arXiv API hits: 9 registros de la consulta `all:"used car price"`; 3 páginas de resumen y 2 textos completos HTML consultados.
- Crossref API hits: 3 registros de la consulta `used car market asymmetric information`; solo uno relevante y ya cubierto por OpenAlex.
- Degradación: `degraded: false` — 38 trabajos L1 frente a 50 objetivo del preset Standard (76 %). La cobertura L3 quedó en 2 de 3 por disponibilidad de texto completo; los trabajos restantes se mantienen en L2.
- Nota de confianza: todas las citas y años se tomaron de las respuestas en vivo de OpenAlex o arXiv el 2026-11-27. Los conteos de citas de P018, P019 y P020 no son verificables desde las fuentes accesibles y se marcan `(metadata incomplete)`; el resumen de P010 no está indexado y también se marca `(metadata incomplete)`.


## Apéndice D — Inventario de artefactos

# Artifact Inventory

Repository: not-declared / not-cloned (no local `repo_path` was supplied for this extraction; §40 declares the remote repository `CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba`, reproduced in frontmatter but not cloned or verified here). All entries below are document-level observations only.

## Datasets

| Name | Source | ID | Publicly accessible | Notes |
|---|---|---|---|---|
| Revolico scraped ads database | custom (own scrape) | `Data/Revolico/revolico.sqlite` | unknown | §54 reports 849,465,344 bytes split into 82 chunks; §66 reports 6,955 `done` ads; §14 states it is not versioned as a single file. |
| Revolico pipeline queues | custom | `Data/Revolico/pipeline.sqlite` | unknown | §16 defines `url_queue`, `download_queue`, `process_queue`; §30 gives ~117 MB; §24 lists pending items from an interrupted run. |
| Dealer and marketplace catalogues | custom | `Data/catalogos_concesionarios/` (per-store `.sqlite`) | unknown | §9 reports 11 prepared databases and 256 rows; §30 places them under Git LFS. |
| Telegram public-channel database | custom | `Data/integraciones/telegram/telegram.sqlite` | unknown | §29: tables `canales` (119), `anuncios` (54), `estado`; §30 places it under Git LFS. |
| ONEI statistical yearbooks 2014–2025 | official/government (ONEI Cuba) | `Data/fuentes-oficiales/ONEI/` | yes | §53: 111 PDF, 7 RAR, 103 extracted Excel files (~311 MB) downloaded from `onei.gob.cu`, with URL, size and SHA-256 per file in `INDICE.md`. §56 reports 233 files. |
| UK DfT/DVLA vehicle licensing statistics | official/government | `gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files` | yes | §18: verified live, updated 23/09/2026, Open Government Licence. |
| VAHAN (India, MoRTH) | official/government | `vahan-india-automotive-market-2025` | no | §18: «No accesible desde este entorno (error de transporte)»; the repo documents 12 monthly exports for 2025. |
| BCC exchange rates | official/government | `https://api.bc.gob.cu/v1/tasas-de-cambio/activas` | no | §52 declares the daily JSON API; §18 records «No accesible en vivo desde este entorno». |
| elTOQUE TRMI | non-official (independent media) | `Anexos/Investigacion Cambios/trmi_USD.csv` | unknown | §23 uses its daily TRMI for CUP conversion; §55 records «elTOQUE no respondió desde este entorno». |
| CarDekho (Kaggle) | Kaggle | not declared in the document | unknown | §18: marketplace/advertised price signal, not official statistics; requires dedup and bias declaration. |
| UCI Automobile | UCI | not declared in the document | unknown | §18: academic/synthetic, methodological reference only, never real Cuban prices. |
| PUCE used-vehicle study survey | academic | `Hombros/01_PDFs/Análisis del mercado de vehículos usados y su comercialización en el__73e1773e.pdf` | unknown | §17: survey of 130 merchants; source of the ≤5-year quality classification. |
| Consolidated reference-repository tables | custom (derived) | `Data/repos-autos-referencias/referencias_autos.sqlite` | unknown | §50: 25 tables including 3,958 Revolico ads, 33 survey responses, 30+30+8 interviews and a `provenancia` table. |
| Fuel price series | custom | `Data/combustible/precios_combustible.sqlite` | unknown | §41: 18 observations between 20/08/2026 and 18/11/2026, official CIMEX / informal elToque / published prices kept separate. |
| OSM/Overpass geodata | custom (OpenStreetMap) | `Data/mapas/gasolineras.csv` | yes | §41: 137 Havana fuel stations; §42 folds them into `Data/mapas/mapa_elementos.sqlite`. |
| EV charging references | marketplace/directory | `Data/mapas/estaciones_carga.csv` | unknown | §41: 12 references (9 from Kargalaya with coordinates, 3 from Electromaps without coordinates). |
| Circuitos Habana APK extracts | custom (APK decompilation) | `Data/mapas/circuitos/` | unknown | §62: 2,473 points, 244 circuits and 166 polygons extracted; plan in `TIMELAPSE_CIRCUITOS.md`. |

## Tables

Tables: none-detected (no numbered `Tabla N` / `Table N` captions occur in the document). The unnumbered Markdown tables actually present are inventoried below; captions are taken verbatim from the header row. Page numbers are unavailable in the text-only cache.

### Table (unnumbered) — «Fase | Nombre | Estado» (§2, ES)
- **Section**: §2 Estado y fases (p. n/a)
- **Lines**: 24–34
- **Columns**: Fase, Nombre, Estado
- **Rows**: 9
- **Claims supported** (preliminary): phase status; active phase 6, phases 7–9 pending. No claim IDs occur in the document.

### Table (unnumbered) — «Búsqueda | Páginas | Resultados | Útiles | Parada» (§7, ES)
- **Section**: §7 Fase 4 — Corpus documental (p. n/a)
- **Lines**: 78–82
- **Columns**: Búsqueda, Páginas, Resultados, Útiles, Parada
- **Rows**: 3
- **Claims supported** (preliminary): search effort and the 10-page stopping rule.

### Table (unnumbered) — «Tienda | Filas | Con precio» (§9, ES)
- **Section**: §9 Fase 6 — Scraping y captura (p. n/a)
- **Lines**: 94–106
- **Columns**: Tienda, Filas, Con precio
- **Rows**: 11
- **Claims supported** (preliminary): «11 bases» and «256 filas»; price density per store.

### Table (unnumbered) — «Problema | Solución» (§11, ES)
- **Section**: §11 Problemas y soluciones (p. n/a)
- **Lines**: 122–129
- **Columns**: Problema, Solución
- **Rows**: 6
- **Claims supported** (preliminary): CAPTCHA, HTTP 202/429, anti-bot and dedup handling.

### Table (unnumbered) — «Phase | Name | Status» (§2, EN)
- **Section**: §2 Status and phases (p. n/a)
- **Lines**: 153–163
- **Columns**: Phase, Name, Status
- **Rows**: 9
- **Claims supported** (preliminary): English parallel of the phase-status table.

### Table (unnumbered) — «Search | Pages | Results | Useful | Stopped at» (§7, EN)
- **Section**: §7 Phase 4 — Document corpus and research (p. n/a)
- **Lines**: 207–211
- **Columns**: Search, Pages, Results, Useful, Stopped at
- **Rows**: 3
- **Claims supported** (preliminary): English parallel of the search-effort table.

### Table (unnumbered) — «Store | Rows | With price» (§9, EN)
- **Section**: §9 Phase 6 — Scraping and capture (p. n/a)
- **Lines**: 223–235
- **Columns**: Store, Rows, With price
- **Rows**: 11
- **Claims supported** (preliminary): English parallel of the per-store row counts.

### Table (unnumbered) — «Problem | Solution» (§11, EN)
- **Section**: §11 Problems and solutions (p. n/a)
- **Lines**: 251–258
- **Columns**: Problem, Solution
- **Rows**: 6
- **Claims supported** (preliminary): English parallel of the problem/solution table.

### Table (unnumbered) — «Fecha / Date | Ruta / Path | Tipo / Type | Origen / Source | Tamaño / Size | Fase / Phase | Descripción / Description | Estado / Status» (§13)
- **Section**: §13 Registro de altas / Change log (p. n/a)
- **Lines**: 276–748 (marker `<!-- REGISTRO_ALTAS -->` at 278; multiple dated snapshots)
- **Columns**: Fecha/Date, Ruta/Path, Tipo/Type, Origen/Source, Tamaño/Size, Fase/Phase, Descripción/Description, Estado/Status
- **Rows**: varies (line 291 explicitly states «175 entradas adicionales no listadas / omitted»)
- **Claims supported** (preliminary): automatic inventory of added files, sizes and phases; regenerated by `actualizar_informe.py`.

### Table (unnumbered) — «Última ejecución / Last run | Tamaño / Size | Partes / Chunks | SHA-256 (inicio) | Reconstrucción / Rebuild» (§14)
- **Section**: §14 Sincronización automática de Revolico (p. n/a)
- **Lines**: 756–759 (marker `<!-- SYNC_REVOLICO -->` at 758)
- **Columns**: Última ejecución/Last run, Tamaño/Size, Partes/Chunks, SHA-256 (inicio), Reconstrucción/Rebuild
- **Rows**: 1
- **Claims supported** (preliminary): 795,373,568 B, 48 chunks of 16 MiB, truncated SHA-256 prefix.

### Table (unnumbered) — «Fuente | Aporte metodológico | Requerimiento para AutoDecide» (§17)
- **Section**: §17 Guía de análisis de mercado (p. n/a)
- **Lines**: 791–804
- **Columns**: Fuente, Aporte metodológico, Requerimiento para AutoDecide
- **Rows**: 12
- **Claims supported** (preliminary): methodological provenance of Fases 7–8 requirements (PUCE, Chile, spinny, taso-api, etc.).

### Table (unnumbered) — «Fuente | Naturaleza | Verificación | Uso en el análisis» (§18)
- **Section**: §18 Auditoría de procedencia (p. n/a)
- **Lines**: 812–825
- **Columns**: Fuente, Naturaleza, Verificación, Uso en el análisis
- **Rows**: 12
- **Claims supported** (preliminary): source nature, live-verification status and permitted analytical use; distinguishes official/industry context from advertised-price signals.

### Table (unnumbered) — «Tabla | Registros» (§29)
- **Section**: §29 Base de datos de Telegram (p. n/a)
- **Lines**: 960–965
- **Columns**: Tabla, Registros
- **Rows**: 4
- **Claims supported** (preliminary): `canales` 119, 4 with automotive context, `anuncios` 54, 54 marked `es_auto`.

### Table (unnumbered) — «Métrica | Valor» (§34)
- **Section**: §34 Esqueleto de análisis de rentabilidad (p. n/a)
- **Lines**: 1039–1050
- **Columns**: Métrica, Valor
- **Rows**: 10
- **Claims supported** (preliminary): first-run baseline (972 ingested, 499 clean, 376 rejections, 32 brands, 24,000 USD median, −5.43 %/year OLS depreciation).

### Table (unnumbered) — «Tipo | Color | Símbolo» (§42)
- **Section**: §42 Base unificada del mapa (p. n/a)
- **Lines**: 1166–1171
- **Columns**: Tipo, Color, Símbolo
- **Rows**: 4
- **Claims supported** (preliminary): required map layer styling (fuel, charging, dealership, workshop).

## Figures

Figures: none-detected (no numbered `Figura N` / `Figure N` captions occur in the document). Referenced figure artifacts:

### Figure (unnumbered) — eight PNG charts under `Data/analisis/graficos/` (§23, §24)
- **Section**: §23 Conversión elTOQUE, serie temporal y gráficas (p. n/a); §24 (p. n/a)
- **Files named**: `01_histograma_precios.png`, `02_boxplot_marcas.png`, `03_barras_municipios.png`, `04_precios_por_anio.png`, `05_serie_precio_vs_tasa.png`, `06_variaciones_tasa_precio.png`, `07_outliers.png`, `08_cobertura.png`
- **Rendered in document**: no (text-only cache; files named, not embedded)
- **Type**: histogram, boxplot, bar chart, yearly-price plot, time-series plots, outlier and coverage charts
- **Claims supported** (preliminary): price distribution, brand/municipality segmentation, price-vs-rate series, outliers and field coverage.

### Figure (unnumbered) — `Data/analisis/graficos/dashboard_interactivo.html` and `Data/analisis/dashboard.html` (§22, §23)
- **Section**: §22 Análisis descriptivo inicial; §23 (p. n/a)
- **Rendered in document**: no
- **Type**: interactive HTML dashboard
- **Claims supported** (preliminary): descriptive market indicators produced by `analisis_mercado.py`.

### Figure (unnumbered) — six Plotly HTML charts of the profitability pipeline (§34, §59, §61)
- **Section**: §34 (p. n/a), §59 (p. n/a), §61 Sitio MkDocs (p. n/a)
- **Paths named**: `Data/analisis_rentabilidad/outputs/charts/`; copies in `docs/graficos/`; visual appendix with «cinco cuadros y seis gráficos reales»
- **Rendered in document**: no
- **Type**: Plotly HTML charts
- **Claims supported** (preliminary): KPIs, benchmark, hedonic model and anomaly results; appendix references kept discrete in the narrative.

### Figure (unnumbered) — `Data/mapas/mapa_ofline.html` (§36, §41, §42)
- **Section**: §36 Mapa offline, talleres e infraestructura EV; §41; §42 (p. n/a)
- **Rendered in document**: no
- **Type**: offline Plotly map with embedded Plotly and Cuba outline; layers for dealerships, charging stations, fuel stations and workshops
- **Claims supported** (preliminary): geolocated infrastructure counts (§42: 131 fuel stations, 12 charging stations, 25 dealerships with 17 coordinates, 22 workshops).

### Figure (unnumbered) — circuit timelapse assets (§62)
- **Section**: §62 Factibilidad del timelapse eléctrico (p. n/a)
- **Paths named**: `Data/mapas/circuitos/`, `Data/mapas/circuitos_estado.sqlite`, `Data/mapas/TIMELAPSE_CIRCUITOS.md`
- **Rendered in document**: no
- **Type**: geospatial circuit geometry and planned temporal map
- **Claims supported** (preliminary): 2,473 points, 244 circuits, 166 polygons; first scrape produced 35 circuits without power, 23 mixed, 2 with power.

## Missing artifacts

### Full Revolico SQLite file in the main branch
- **Mentioned in document**: §14 (p. n/a): «La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**.»; §54: «`main` queda intacto hasta decidir su sustitución.»
- **Found in repo**: no (no local clone supplied; document-level statement only)
- **Observation**: The document describes the full database as deliberately absent from normal versioning: an earlier 16 MiB chunk scheme (§14) and a later 82-chunk 10 MB scheme with `MANIFEST.json` (§54) are used instead, and the chunks are published on the orphan branch `chunked-db` while `main` still references the ~804 MB LFS object. Git LFS is described in §30 as managing the `.sqlite` files. No single authoritative file is therefore inventoryable from the versioned history described.

### Official Cuban vehicle-fleet and registration series
- **Mentioned in document**: §56 (p. n/a): «**No hay series de parque automotor ni de matriculaciones**, por lo que esa laguna signalada en `NECESIDADES.md` no se resuelve con los anuarios»; §20 lists «estadísticas oficiales cubanas de parque y matriculaciones» among outstanding needs.
- **Found in repo**: no (no local clone supplied; document-level statement only)
- **Observation**: The ONEI yearbooks were downloaded in full (§53), but §56 states that the transport and road-safety series extracted into `series_oficiales.csv` do not include fleet size or registrations. The document records this gap as unresolved and notes the correction was logged, while §52 had earlier presented ONEI chapter 13 as a source that would fill it.

### VAHAN (India) dataset
- **Mentioned in document**: §18 (p. n/a): «No accesible desde este entorno (error de transporte)»; the row classifies it as official MoRTH data with 12 monthly 2025 exports.
- **Found in repo**: no (no local clone supplied; document-level statement only)
- **Observation**: The dataset is named as a benchmark input for registrations by manufacturer and fuel, but the document records that it could not be retrieved in this environment and that only the repository's own verification manifest was available.

### BCC live exchange-rate endpoint
- **Mentioned in document**: §18 (p. n/a): «No accesible en vivo desde este entorno»; §52 declares `https://api.bc.gob.cu/v1/tasas-de-cambio/activas`.
- **Found in repo**: no (no local clone supplied; document-level statement only)
- **Observation**: The official rate is cited via `Data/investigacion-mercado-automotor-cuba.md` and Resolution 102/2026, but §18 marks live retrieval as unavailable; the project's conversion continues to use the informal elTOQUE TRMI (§23, §52), and §55 records that elTOQUE itself did not respond from this environment in the final audit.

### Full gazette corpus
- **Mentioned in document**: §10 (p. n/a): «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe»; §67 states laws were moved to `~/Utilidades/Leyes`.
- **Found in repo**: no (no local clone supplied; document-level statement only)
- **Observation**: Only named decrees and resolutions (163/2026, 104, 17, 52, 171–175, 340, 102) are cited; the reference index and corpus live outside the project tree after the space-optimization step, so the underlying legal documents are not inventoried here.

### Rendered figures for the descriptive and profitability analyses
- **Mentioned in document**: §23 (p. n/a): «genera 8 PNG + `dashboard_interactivo.html` en `Data/analisis/graficos/`»; §59: «un **apéndice visual** con cinco cuadros y seis gráficos reales».
- **Found in repo**: no (no local clone supplied; paths named in document only)
- **Observation**: The cached document text names the eight PNG files, the interactive dashboards and the six Plotly charts copied to `docs/graficos/`, but embeds none of them. The visual appendix is described as leaving only discrete in-text references so tables and figures can be inserted without breaking the narrative.

### Docker daemon for the Google Maps scraper
- **Mentioned in document**: §36 (p. n/a): «el daemon Docker no arranca sin root en este entorno (`dockerd needs to be started with root privileges`)».
- **Found in repo**: no (no local clone supplied; document-level statement only)
- **Observation**: The `google-maps-scraper` route was discarded; §6 does report FlareSolverr 3.5.2 running in Docker at `http://127.0.0.1:8191/`, so the document records both a working containerized service and an unavailable daemon for a different tool.

### Structured vehicle specifications and real transaction prices
- **Mentioned in document**: §24 (p. n/a): «**No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**»; §20 lists «precios de transacción reales» and «montos de costos ocultos» as outstanding.
- **Found in repo**: no (no local clone supplied; document-level statement only)
- **Observation**: `ad_json` (21 keys) and `apollo_full` (five types plus `ROOT_QUERY`) are stored for all 6,334 ads, but year, km, brand, model, fuel and transmission are derived by regex with 63.5 %, 6.2 % and 68.4 % coverage (§22, §24). §59–§60 further state that the current model does not support a significant annual depreciation slope or a premium brand premium, so the earlier −5.43 %/year and +21 % figures (§34) are not carried into the final narrative.

### `Copias/` reference repositories
- **Mentioned in document**: §3 (p. n/a): «`Copias/` no se registra en este informe por decisión explícita»; §17 cites code from `Copias/AutosxCuba/code/{unir_todo_final,modelo_predictivo,generar_graficos}.py`.
- **Found in repo**: no (excluded by explicit decision; no local clone supplied)
- **Observation**: Four reference repositories are listed in the folder structure but deliberately excluded from the report; nevertheless, §17 and §50 use their code and data as methodological inputs, so those artifacts are cited without being inventoried.

## Declared environment (document-level; not verified in a clone)

- §6 `Auxiliares/.venv`: patchright 1.64.4, PyPasser 1.1.0, Scrapling 0.5.1, ddddocr 1.6.1, playwright 1.65.2, curl_cffi 0.17.0, trafilatura, pandas, numpy, onnxruntime 1.32.0, ddgs 9.16.1, tenacity 9.2.1; system Chromium; FlareSolverr 3.5.2 in Docker at `http://127.0.0.1:8191/` (§42 uses `/v1`).
- §23: matplotlib, seaborn and plotly described as installed for chart generation.
- §25: geopandas 1.2.0, shapely 2.2.0, pyproj, folium 1.0.0, mapclassify, geopy.
- §34: statsmodels 0.15, pyarrow 26, kaleido, nbformat, nbconvert; `duckdb` uninstalled because it raises `Illegal instruction` on this CPU (§66 repeats `SIGILL`).
- §30: Git LFS 3.8.1 installed and enabled; `.gitattributes` marks `*.sqlite`, `*.sqlite-wal`, `*.sqlite-shm` with LFS filters; §54 adds `.bin` handling.
- §55: `requirements.txt` added and a functional `Auxiliares/.venv-py` created; §58 adds `pyarrow` to requirements.
- §61: MkDocs Material site with `mkdocs.yml`; `mkdocs build --strict` reported without errors; `site/` ignored by Git.
- §35: jadx 1.5.6 used to decompile the Circuitos Habana APK.
- §55: skills `technical-writing`, `readme-writing`, `diataxis-docs`, `marketing-copy` and `pptx` described as installed and active.
- systemd units named in the document: `revolico-scrape.timer`, `revolico-git.timer`, `revolico-revisar.service`, `revolico-aviso.timer`, `revolico-backfill.service`, `marketplaces-scrape.service`, `revolico-snapshot`, `progreso-report.timer`, `precio-combustible.timer`, five `precio-*` timers (§65), `revolico-revisar`/`marketplaces-scrape`/`revolico-snapshot` with automatic restart (§37). §64–§65 add `linger`, `run_step.sh` with `flock`, `SALUD.md` and atomic state.
- §40: remote renamed from `CarlosAntonioAceaJimenezCD/autodecide-habana` to `CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba`; the local folder is stated as `~/Proyectos/ICD Automotive Market Project`, while the report header (line 6) states `~/Proyectos/El precio de moverse en Cuba`.

## Code-to-document mapping (when discernible)

Paths below are the locations declared in the document; with no clone available, none were verified on disk.

| Document component | Repo location (document-declared) |
|---|---|
| Revolico scraper / incremental updates | `Auxiliares/herramientas/scrape_revolico.py`, `Auxiliares/herramientas/actualizar_revolico.py`, `Auxiliares/herramientas/actualizar_informe.py` |
| Queue pipeline and early link classification | `Auxiliares/herramientas/scrape_revolico_pipeline.py`, `Auxiliares/herramientas/limpiar_revolico.py` |
| Database reconstruction / chunking | `Auxiliares/herramientas/reconstruir_revolico.py`, `Auxiliares/herramientas/db_chunks.py` |
| Dealer/marketplace scraping | `Auxiliares/herramientas/scrape_concesionarios.py`, `Auxiliares/herramientas/integraciones/fuentes_cubanas/*`, `scrape_marketplaces.py` (§37) |
| Telegram / WhatsApp integrations | `Auxiliares/herramientas/scraper_telegram_publico.py`, `Auxiliares/herramientas/descubrir_canales_telegram.py`, `Auxiliares/herramientas/telegram_db.py`, `Auxiliares/herramientas/integraciones/whatsapp/waha_client.py` |
| Descriptive analysis and charts | `Auxiliares/herramientas/analisis_mercado.py`, `Auxiliares/herramientas/graficos_mercado.py`, `Data/analisis/` |
| Profitability pipeline | `Data/analisis_rentabilidad/config.py`, `scripts/01_ingest.py` … `05_benchmark.py`, `run_all.py`, `sql/analysis.sql` |
| Reference-repo consolidation | `Auxiliares/herramientas/consolidar_repos_autos.py`, `Data/repos-autos-referencias/` |
| Maps and infrastructure | `Auxiliares/herramientas/scrape_infraestructura.py`, `geocode_elementos.py`, `generar_mapa_ofline.py`, `Auxiliares/herramientas/scraper_circuitos.py`, `Data/mapas/` |
| Progress reporting / source audit | `Auxiliares/herramientas/reporte_progreso.py`, `auditar_fuentes.py`, `revisar_novedades.py`, `Data/progreso_reporte.md`, `Data/auditoria-fuentes-2026-11-23.md` |
| Documentation site | `docs/`, `mkdocs.yml`, `Auxiliares/herramientas/generar_sitio_mkdocs.py` |
| Report and changelog generator | `INFORME_TECNICO.md` / `INFORME_TECNICO.pdf`, `README.md`, `Auxiliares/herramientas/actualizar_informe.py` |
| Tests (`test_*.py`, `*_test.py`, `tests/`) | not located (no test files or test framework named in the document) |


## Apéndice E — Criterios por nivel aplicados

# Level criteria — calibration tables

Tables consumed by V2, V4, V5, V6, and V9 to calibrate their findings
by academic level (diploma / master / phd / paper). When an evaluator
emits a finding that anchors to a level-criterion, it cites the path
(e.g., `V2.statistical_tests.diploma`) in the finding's metadata
line. The final report reproduces the consulted sub-sections in
Appendix E.

Levels:

- `diploma` — undergraduate final-year thesis (Trabajo de Diploma, BSc thesis).
- `master` — Master's thesis (MSc/MA).
- `phd` — Doctoral dissertation (PhD).
- `paper` — submitted/published research paper at a peer-reviewed venue.

Criteria are descriptive standards drawn from community norms.
Evaluators report observations against them; they never instruct the
document to meet them.

---

## V2 — Methodology

### V2.baselines

| Level | Criterion |
|---|---|
| diploma | ≥1 baseline; may be trivial (random / mean predictor / simplest model). |
| master | ≥2 baselines, one of which corresponds to a SOTA-adjacent approach in the field. |
| phd | ≥3 baselines, at least one of which is the explicit SOTA at submission time. |
| paper | ≥3 baselines including explicit SOTA; venue-typical ablations expected (component-by-component). |

### V2.ablations

| Level | Criterion |
|---|---|
| diploma | Implicit ablations acceptable (e.g., comparing two configurations of own system). |
| master | Explicit ablation of at least one component. |
| phd | Ablation of each major component declared as a contribution. |
| paper | Ablation per component + sensitivity analysis of key hyperparameters. |

### V2.statistical_tests

| Level | Criterion |
|---|---|
| diploma | Recommended for paired comparisons; not required. Reporting std-dev across trials suffices. |
| master | Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI). |
| phd | Required for all comparative claims. Correction for multiple comparisons when applicable. |
| paper | Required + correction for multiple comparisons + effect-size reporting (Cohen's d, Cliff's delta, etc.). |

### V2.sample_size

| Level | Criterion |
|---|---|
| diploma | ≥10 independent trials per configuration; ≥5 datasets/instances. |
| master | ≥20 trials; ≥10 datasets/instances. |
| phd | ≥30 trials + power analysis for primary claims; ≥20 datasets/instances when applicable. |
| paper | ≥30 trials + power + seeds reported; dataset count justified against venue norms. |

### V2.threats_to_validity

| Level | Criterion |
|---|---|
| diploma | Implicit threats acknowledged in discussion. |
| master | Brief dedicated subsection on threats / limitations. |
| phd | Dedicated section addressing internal, external, construct, and statistical conclusion validity. |
| paper | Dedicated section + explicit mitigations + replicability statement. |

### V2.reproducibility_protocol

| Level | Criterion |
|---|---|
| diploma | Protocol describable (datasets, splits, metrics named). |
| master | Protocol fully described + seeds mentioned + code referenced. |
| phd | Protocol + seeds + environment + dataset versions + code DOI/commit pinned. |
| paper | All of phd + reproducibility checklist (NeurIPS-style or venue-specific). |

---

## V4 — Novelty

### V4.differentiation_from_prior_art

| Level | Criterion |
|---|---|
| diploma | Differentiator named at least once in the document, even informally. |
| master | Differentiator articulated with at least one explicit comparison paragraph to one closest prior work. |
| phd | Differentiator articulated against ≥3 closest prior works; conceptual contribution distinct from incremental engineering. |
| paper | Differentiator articulated + venue-aligned (matches the kind of contribution the venue rewards: theory / system / empirical study). |

### V4.scope_of_novelty_claim

| Level | Criterion |
|---|---|
| diploma | Local novelty acceptable ("first integration of X+Y in this context", "first application to Z"). |
| master | Component novelty + integration novelty: one of the two should be substantive. |
| phd | Genuine novelty on at least one axis: problem formulation, method, or experimental insight. |
| paper | Novelty must clear the bar of the venue's typical contribution profile. |

### V4.prior_art_engagement

| Level | Criterion |
|---|---|
| diploma | Closest prior works cited and briefly contrasted. |
| master | Closest prior works cited, contrasted, and discussed in their own subsection. |
| phd | All closest prior works engaged with substantively (methods, results, limitations of each). |
| paper | Full engagement + venue-appropriate related-work survey. |

---

## V5 — State of the Art

### V5.coverage_breadth

| Level | Criterion |
|---|---|
| diploma | The main cluster of work surrounding the thesis topic is covered (10–25 papers). |
| master | Main + adjacent clusters covered (25–60 papers). |
| phd | Main + adjacent + boundary clusters covered (60–150+ papers). |
| paper | Venue-aligned: NeurIPS/ICML/ACL-class survey of the directly-relevant literature; orthogonal areas referenced. |

### V5.recency

| Level | Criterion |
|---|---|
| diploma | At least 30% of citations from the last 5 years. |
| master | At least 40% from the last 5 years; foundational classics balanced. |
| phd | At least 50% from the last 5 years; tracking of last 12-18 months of arXiv preprints expected. |
| paper | At least 60% from the last 3 years; explicit engagement with venue-recent prior work (last 1–2 cycles). |

### V5.citation_weight

| Level | Criterion |
|---|---|
| diploma | Load-bearing claims must cite at least one source per claim. |
| master | Load-bearing claims cite source + author named in body at first mention. |
| phd | Citation weight calibrated: foundational classics in introduction, recent works in related-work, peer SOTA in experimental comparison. |
| paper | All cited works' role in the argument must be clear (foundational vs comparison vs replicated vs disputed). |

### V5.missing_important_work

| Level | Criterion |
|---|---|
| diploma | Tolerable to miss minor recent works; the top-3 most-cited of the cluster expected. |
| master | Top-5 most-cited of each adjacent cluster expected. |
| phd | Top-10 most-cited of each cluster + last 12-month preprints expected. |
| paper | No top-tier cluster-paper should be absent; gap-spot checks against Semantic Scholar / OpenAlex expected. |

---

## V6 — Reproducibility

### V6.documentation

| Level | Criterion |
|---|---|
| diploma | README naming the project + how to run the main experiment. |
| master | README + dependencies list + brief usage examples. |
| phd | README + dependencies pinned + script-to-table mapping + environment description. |
| paper | All of phd + reproducibility statement aligned with venue norms. |

### V6.environment

| Level | Criterion |
|---|---|
| diploma | Dependencies file present (requirements.txt / pyproject.toml / environment.yml) even if loosely versioned. |
| master | Dependencies pinned to minor versions. |
| phd | Dependencies fully pinned + lockfile + Python/R version declared. |
| paper | Dependencies pinned + lockfile + Dockerfile or equivalent environment freeze. |

### V6.determinism

| Level | Criterion |
|---|---|
| diploma | Seeds mentioned in document; presence in code optional. |
| master | Seeds declared in code and in document, consistent. |
| phd | Seeds + deterministic execution flag (where framework supports) + GPU-determinism note when applicable. |
| paper | All of phd + verified bit-reproducibility of at least one headline result. |

### V6.entry_points

| Level | Criterion |
|---|---|
| diploma | At least one entry-point script identifiable from documentation or filename. |
| master | Entry points documented with arguments. |
| phd | Entry points + one-command reproduction (Makefile / justfile / shell script). |
| paper | All of phd + a single command produces all reported tables and figures. |

### V6.tests

| Level | Criterion |
|---|---|
| diploma | Tests not required. |
| master | At least smoke tests of the central component. |
| phd | Unit tests + at least one integration test of the experimental pipeline. |
| paper | Tests + CI configured if repo is public. |

### V6.data_availability

| Level | Criterion |
|---|---|
| diploma | Datasets named with source. |
| master | Datasets named + access path documented (URL / DOI / "available on request"). |
| phd | Datasets named + access path + version pinned + license documented. |
| paper | All of phd + venue-specific data statement. |

---

## V9 — Ethics and Declarations

### V9.ai_use_declaration

| Level | Criterion |
|---|---|
| diploma | Declaration of generative-AI use in research and writing recommended if any AI tools were used. |
| master | Declaration expected; should name tools, phases (research, drafting, code generation, translation), and supervision protocol. |
| phd | Declaration expected and complete; sections of the document where AI assistance was significant identified. |
| paper | Declaration expected and aligned with venue policy (NeurIPS, ICML, ACL, Nature, etc. have specific requirements). |

### V9.data_ethics

| Level | Criterion |
|---|---|
| diploma | When human subjects involved, consent statement mentioned. |
| master | Consent + IRB/ethics-committee approval named when applicable. |
| phd | Full statement on human subjects, consent, anonymisation, data governance, IRB approval where applicable. |
| paper | All of phd + venue-specific data ethics review (e.g., NeurIPS broader-impact). |

### V9.coi_statement

| Level | Criterion |
|---|---|
| diploma | Not required. |
| master | Not required; tutor/advisor relationship implicit. |
| phd | Tutors/advisors + sponsors declared. |
| paper | Full COI statement aligned with venue policy. |

### V9.dual_use

| Level | Criterion |
|---|---|
| diploma | Not required unless topic is clearly dual-use sensitive (LLMs, surveillance ML, biosec, autonomous weapons). |
| master | Discussion encouraged for dual-use-relevant topics. |
| phd | Dual-use / societal-impact discussion expected for relevant topics. |
| paper | Venue-aligned: NeurIPS broader-impact statement; ACL ethics statement; etc. |

### V9.data_availability_statement

| Level | Criterion |
|---|---|
| diploma | Not required as a formal statement; data sources mentioned in methodology. |
| master | Brief statement: where the data lives, how to obtain. |
| phd | Formal "Data availability" statement: location, version, license, access conditions. |
| paper | Formal statement aligned with venue requirements. |

### V9.code_availability_statement

| Level | Criterion |
|---|---|
| diploma | Repo URL printed somewhere in the document if code exists. |
| master | "Code available at" statement with URL and brief description. |
| phd | Formal "Code availability" statement: repo URL + commit/tag/DOI pinned to the version that produced the reported results. |
| paper | Formal statement + Zenodo DOI or equivalent permanent identifier when venue requires. |

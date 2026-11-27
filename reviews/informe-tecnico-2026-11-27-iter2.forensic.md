---
type: audit-forensic
slug: informe-tecnico-2026-11-27-iter2
generated_at: 2026-11-27T18:00:00-05:00
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
  plan: informe-tecnico-2026-11-27-iter2.plan.md
  e1: informe-tecnico-2026-11-27-iter2.e1-claims.md
  e2: informe-tecnico-2026-11-27-iter2.e2-literature.md
  e3: informe-tecnico-2026-11-27-iter2.e3-artifacts.md
  v1: informe-tecnico-2026-11-27-iter2.v1-structure.md
  v2: informe-tecnico-2026-11-27-iter2.v2-methodology.md
  v3: informe-tecnico-2026-11-27-iter2.v3-results-evidence.md
  v4: informe-tecnico-2026-11-27-iter2.v4-novelty.md
  v5: informe-tecnico-2026-11-27-iter2.v5-state-of-the-art.md
  v6: informe-tecnico-2026-11-27-iter2.v6-reproducibility.md
  v7: informe-tecnico-2026-11-27-iter2.v7-writing.md
  v8: informe-tecnico-2026-11-27-iter2.v8-bibliography.md
  v9: informe-tecnico-2026-11-27-iter2.v9-ethics.md
  forensic: informe-tecnico-2026-11-27-iter2.forensic.md
previous_iterations: [reviews/informe-tecnico-2026-11-27.md]
---
# Auditoría forense — Iteración 2

## §0 — Resumen del documento

El documento auditado es el *Informe técnico / Technical report — El precio de moverse en Cuba*, de autoría consignada por rol («responsable del proyecto / project owner», L4) y sin nombre propio ni institución declarada. La fecha del encabezado es 23/11/2026 y la de última actualización, 27/11/2026 (L1484). El texto es bilingüe —Parte I en español y Parte II en inglés—, no tiene paginación en la copia cacheada y ocupa 1.484 líneas. El alcance declarado en §1 (L16) es «un análisis del mercado automotor cubano» —estructura, precios, oferta, segmentos, tendencias, asequibilidad y rentabilidad—, con la recomendación interactiva diferida; la tabla de §2 fija la fase activa en la sexta y añade una nota de actualización que remite los resultados de la fase 8 a §59–§60 (L38, L169).

El inventario E1 de esta pasada registra 13 afirmaciones load-bearing (C001–C013), de las cuales nueve conservan «sin citas numeradas» (C001–C006, C008, C010, C013). Los ejes del relato son el objetivo de análisis y el estado de la fase 8 (C001–C002); la reformulación de la depreciación y de la prima premium como no significativas en la corrida vigente (C004–C006); las cifras de cierre del relato final (C003); la diferenciación declarada como adopción de la arquitectura de `Egyptian-Used-Cars` adaptada a fuentes cubanas (C011–C012); y el aparato de 38 referencias con cuatro fuentes declaradas verificadas (C009). Los números del modelo se leen de `modelo_muestra.csv` (`principal`: 981 candidatas / 584 observaciones / R² 0,101 / p 0,0; `completo`: 981 / 28 / 0,2744 / 0,4114) y los indicadores de `outputs/tables/kpis.csv`.

El repositorio `CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba` está disponible en disco con 190 commits y HEAD en `99c7065` (27/11/2026), 41.689 líneas de Python propio y `README.md` de 105 líneas. E3 inventaría dos SQLite de Revolico bajo LFS y con manifiestos de chunks SHA-256, 11 bases de concesionarios y marketplaces, 12 anuarios del ONEI, 38 referencias numeradas en `Data/referencias.md`, `modelo_muestra.csv` y el panel autocontenido `Data/dashboard.html` (109.929 B). Las tablas y figuras no llevan numeración: E3 consigna «Tables: none-detected» y «Figures: none-detected» y las localiza por encabezado, sección o ruta; el texto cita ocho PNG, seis gráficos Plotly y dashboards descriptivos de `Data/analisis/`, sin nombrar por esa ruta el panel vigente.

La pasada corresponde a la fase 3 de la iteración 2, con `level: master` y `preset: Standard`, y re-ejecuta E1, E2, E3 y V1–V9 sobre el texto cacheado, en español y en inglés, con el informe y el expediente de la iteración 1 como contexto heredado. E2 ejecutó 22 consultas de re-verificación dirigida (`papers_l1: 6`, `papers_l2: 6`, `papers_l3: 0`) sin búsquedas temáticas nuevas. No se registraron dimensiones omitidas ni subagentes fallidos; sí se registran fallos de herramientas y desfases de inventario: `WebSearch` falló en E2 y en V5, Crossref devolvió error de transporte para Akerlof en V8, E3 cerró a las 17:15 sin inventariar `Auxiliares/herramientas/test_smoke_pipeline.py`, y V9 dejó constancia de no haber recibido la tabla de densidad de V7, que V7 consignó al cierre de su propio artefacto.

Respecto de la iteración 1, el texto incorpora 520 palabras y 22 líneas (28.586 → 29.106), siete reescrituras puntuales y dos secciones nuevas: §69 «Declaración de uso de inteligencia artificial / AI-use declaration» (L1467–L1471) y §70 «Referencias verificadas / Verified references» (L1475–L1479); la bitácora pasa de §68 a §70. En el repositorio aparecen `modelo_muestra.csv`, `Data/referencias.md` y `Data/dashboard.html`, y el relato de §59 adopta la corrida de 28 observaciones con marcadores `<!-- kpi:… -->` actualizados por `Auxiliares/herramientas/actualizar_numeros.py`. La fila de la fase 8 y la conclusión 5 siguen divergiendo entre el español y el inglés (L33/L164, L139/L270; E3, L196).

## §1 — v1-structure


# V1 — Structure (findings)

### F-V1-001 — Persiste la ausencia de resumen VSN-C, hipótesis y contribuciones

El encabezado conserva los seis campos de la iteración 1 —«**Proyecto / Project:**», «**Autor / Author:**», «**Fecha / Date:**», «**Ubicación / Location:**», «**Estado / Status:**», «**Idioma / Language:**» (L3–8)— con la autoría consignada como rol («responsable del proyecto / project owner», L4) y la firma igualmente por rol (L1483); la fecha de cierre sube a «**Última actualización / Last update:** 27/11/2026» (L1484). Ninguno de los 89 encabezados del texto es «Resumen» o «Abstract», y no aparecen dedicatoria, agradecimientos ni dictamen de tutor. Las dos secciones nuevas respecto a la pasada 1 —§69 «Declaración de uso de inteligencia artificial / AI-use declaration» (L1467–1471) y §70 «Referencias verificadas / Verified references» (L1475–1479), después del antiguo cierre en §68— aportan declaración procedimental y aparato bibliográfico, pero no sustituyen un resumen ni una sección de contribuciones.

El material más cercano a un resumen sigue repartido entre §1 (L14–18) y las cinco conclusiones de §12 (L133–139), sin elemento de novedad ni contribuciones enumeradas. El inventario E1 de esta pasada clasifica una señal de novedad —«Creé `Data/analisis_rentabilidad/`… adaptada a nuestras fuentes y preparada para crecer» (C011, §34 L1018)— frente a `novelty 0` de la pasada 1, aunque el enunciado ya figuraba en el texto anterior (L1014). Tampoco se enuncia una hipótesis central como proposición falsable: §34 (L1056) reporta «una depreciación media de **−5,43 % anual** (p<0,001)» sin proposición previa que la someta a contraste, y §59–§60 (L1381, L1389) retiran esa pendiente; E2 hace constar que el plan no declaró `hypotheses_planned`. E1 C009 consigna además que el cuerpo del informe no lleva citas numeradas.

— polarity: negative · confidence: high · related: [[#C001]], [[#C008]], [[#C011]], [[#C009]]

### F-V1-002 — Objetivo alineado en ambas partes, pero fase 8 y conclusión 5 divergen

La divergencia observada en la iteración 1 entre las dos introducciones queda cerrada: §1 ES (L16) y §1 EN (L147) enuncian ahora el mismo objetivo —«un análisis del mercado automotor cubano» / «to analyse the Cuban automotive market»— con la recomendación interactiva diferida, donde la pasada 1 leía «The project is named **AutoDecide Habana**. Its goal is to define an interactive product…». §21 (L881–886) documenta el cambio —«el objetivo inmediato deja de ser la recomendación interactiva de compra y pasa a ser **un análisis de mercado**»— y la Parte II lo recoge en su §1; ambas partes añaden ahora una nota de actualización en §2 (L38, L169) que remite el estado vigente de la fase 8 a «§59–§60». El objetivo de análisis se corresponde con secciones ejecutadas: el marco de ocho pasos (§19, L837–846), los nueve bloques (§20, L861–871), el pipeline (§34, L1016–1037) y los resultados (§59–§60, L1377–1391).

Persisten, sin embargo, dos puntos de la observación anterior. La fila 8 de la tabla de fases se lee «Análisis de mercado, comparables y rentabilidad» en español (L33) pero «Analysis, profitability model and interactive product» en inglés (L164), nombre que §21 había retirado. La conclusión 5 diverge en el mismo sentido: §12 ES (L139) afirma que «El análisis de mercado y el modelo de rentabilidad (fase 8) están implementados… y se regeneran de forma automática», mientras §12 EN (L270) sostiene «The interactive product and profitability model (phase 8) are not implemented yet». E1 lo registra en C001–C002 y E3 lo describe como divergencia de contenido entre párrafos paralelos (L196), no de traducción.

— polarity: neutral · confidence: high · related: [[#C001]], [[#C002]], [[#C029]]

### F-V1-003 — Numeración 1–12 duplicada y referencias sin anclar en el cuerpo

La numeración se reinicia igual que en la pasada 1: dos secciones «1.» (L14, L145) y dos «12. Conclusiones» (L133, L264), tras las cuales la secuencia continúa hasta §70 (L1479), tres secciones más que el §68 final de la iteración 1. El bloque §13 «Registro de altas / Change log» (L274–748, 475 líneas) usa encabezado de nivel 1 mientras §14–§70 usan nivel 2 (L754, L1467, L1475), y declara «175 entradas adicionales no listadas / omitted» (L295). De las 57 secciones numeradas §14–§70, 53 llevan fecha en el título; §14, §15, §69 y §70 no la llevan, y §69 va precedido de dos reglas horizontales consecutivas (L1463, L1465). Los títulos de edición señalados en la pasada 1 permanecen —§45, §46, §47 «Reescritura de la sección 3 / Apertura de la sección 3 / Reescritura de la sección 4 del storytelling» (L1212, L1220, L1228)—, mientras §69–§70 son títulos descriptivos de contenido.

En integridad de referencias cruzadas no aparecen marcadores `??` ni comandos `\ref{}` en esta iteración, como tampoco en la anterior; E3 consigna «Tables: none-detected» (L164) y «Figures: none-detected» (L239), y las tablas y figuras se localizan por encabezado, sección o ruta de archivo. Lo nuevo es la aparición de cuatro marcadores de plantilla insertados en la prosa de §59 (L1381): `<!-- kpi:modelo_n_completo -->`, `<!-- kpi:modelo_candidatas -->`, `<!-- kpi:modelo_r2_completo -->` y `<!-- kpi:modelo_pf_completo -->`, actualizados por `Auxiliares/herramientas/actualizar_numeros.py` (E3, L62, L330), además del «apéndice visual con cinco cuadros y seis gráficos reales» descrito con «referencias discretas entre paréntesis» (L1381). §70 anuncia «La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`» (L1477–1479), pero el cuerpo no contiene citas `[N]` (E1 C009; E3 L136, L281), y E2 H1–H2 observa que Akerlof figura a la vez como referencia verificada en §70 y con `(metadata incomplete)` en `[1]` (P001).

— polarity: neutral · confidence: high · related: [[#C003]], [[#C009]], [[#P001]]

## Resumen

- Persisten el encabezado con autoría por rol, la ausencia de resumen VSN-C, hipótesis falsable, contribuciones y firma nominativa; §69–§70 son las únicas secciones nuevas.
- §1 coincide ya en ambas partes y §2 añade notas de actualización, pero la fila de la fase 8 y la conclusión 5 siguen divergiendo entre español e inglés.
- La numeración 1–12 continúa duplicada y la bitácora llega a §70; no hay referencias rotas, pero los marcadores KPI y las 38 referencias de §70 no están anclados en el cuerpo.


## §2 — v2-methodology


# V2 — Methodology (findings)

## Resumen

La ablación `principal`/`completo` existe en el CSV del pipeline pero no se declara como tal en el documento y confunde el cambio de especificación con una caída de 584 a 28 observaciones: no satisface `V2.ablations.master`.
No hay semillas aleatorias: las únicas «semillas» del texto son ocho URLs de marketplaces en §55, frente a la cláusula «seeds mentioned» de `V2.reproducibility_protocol.master`.
Sí se registran límites dedicados, pruebas estadísticas y código referenciado; persisten la ausencia de test pareado y tres estados incompatibles del mismo modelo.

### F-V2-001 — El «benchmark» sigue siendo descriptivo, sin comparador SOTA-adjacente

El esqueleto de rentabilidad declara `05_benchmark.py` como «benchmark por marca/modelo/año e infravalorados» (§34, L1028) y la línea base consigna «Grupos de benchmark | 21» e «Infravalorados | 30» (§34, L1052–1053), pero no compare el desempeño del modelo hedónico contra otro enfoque. El único contraste nombrado es de escala: «Egipto tiene 23.500 anuncios [...] Nosotros tenemos el pipeline y las técnicas cubiertas, pero solo 497 usados, un único snapshot» (§34, L1060; [[#C012]]), presentado como «Brecha frente a Egipto» y no como línea base reproducible; la arquitectura se describe como «inspirada en Egyptian-Used-Cars» ([[#C011]]). El contexto de la iteración 2 mantiene F-V10-006 como «NO RESUELTA» en cuanto a diferenciación. El criterio `V2.baselines` para `level=master` se lee: «≥2 baselines, one of which corresponds to a SOTA-adjacent approach in the field».

— polarity: neutral · confidence: high · related: [[#C011]], [[#C012]], [[#F-V10-006]] · criteria: V2.baselines.master

### F-V2-002 — Ablación `principal`/`completo` presente en el artefacto, no declarada en el documento

El CSV que respalda §59 contiene dos configuraciones: `principal` con 981 candidatas, 584 observaciones, R² 0,101 y p del F 0,0; `completo` con 981 candidatas, 28 observaciones, R² 0,2744 y p del F 0,4114, con la formulación `log_price ~ car_age + np.log1p(mileage_km) + condition_score + C(brand_tier)` y la variante con `hp` (E3, «New artifacts», líneas 138–144). El documento, en cambio, nombra una sola: «El modelo con todos los términos dispone de 28 observaciones completas de 981 candidatas (R² = 0,277; p del F = 0,411)» (§59, L1381), sin citar `modelo_muestra.csv` — la búsqueda de esa ruta en la caché del documento no devuelve coincidencias— y sin presentar la comparación entre configuraciones como ablación. Las dos especificaciones no difieren solo en un término: el n pasa de 584 a 28 y el p del F de 0,0 a 0,4114, de modo que el efecto del componente queda confundido con la selección muestral. El inventario E1 registra «sin ablación ni test pareado entre corridas» ([[#C004]]) y F-V10-002 permanece «PARCIALMENTE RESUELTA». El criterio `V2.ablations` para `level=master` se lee: «Explicit ablation of at least one component».

— polarity: negative · confidence: high · related: [[#C004]], [[#C005]], [[#C006]], [[#F-V10-002]], [[#F-V2-003]] · criteria: V2.ablations.master

### F-V2-003 — Sensibilidad al kilometraje sin aislamiento de componentes

La primera corrida atribuye al modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` una «depreciación media de −5,43 % anual (p<0,001)» (§34, L1056; [[#C006]]), mientras que la narrativa vigente afirma que «el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje» (§59, L1381; [[#C004]]), con «p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05» (§60, L1389). La corrección del campo se documenta como `parse_number()` para separadores de miles (§51, L1282), pero el texto no separa el efecto de esa reparación del efecto de cambiar la especificación ni del cambio de muestra; la retirada de la cifra se reitera en §44 (L1206) y §45 (L1214) sin un contraste controlado. Es una comprobación de sensibilidad declarada, no una ablación explícita de un componente. El criterio `V2.ablations` para `level=master` se lee: «Explicit ablation of at least one component».

— polarity: neutral · confidence: high · related: [[#C004]], [[#C006]], [[#F-V10-002]], [[#F-V2-002]] · criteria: V2.ablations.master

### F-V2-004 — Pruebas estadísticas y diagnósticos declarados, con decisión de no significancia

El inventario de funciones enumera «modelo hedónico log-lineal, VIF, Kruskal-Wallis, Welch t-test y detección de anomalías» y explica «por qué la corrida actual **no** sostiene una tasa de depreciación ni una prima premium significativa (p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05)» (§60, L1389). La arquitectura ya reservaba `04_stats.py` para «OLS log-precio, VIF, Kruskal-Wallis, anomalías» (§34, L1027) y la estimación vigente acompaña el p del F de 0,411 con la limitación de n (§59, L1381; [[#C005]]). La presencia de pruebas y de diagnósticos de colinealidad, junto con la decisión de retirar una afirmación de significancia, constituye una observación positiva dentro de este criterio. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)».

— polarity: positive · confidence: high · related: [[#C004]], [[#C005]], [[#C011]] · criteria: V2.statistical_tests.master

### F-V2-005 — Comparaciones entre configuraciones y corridas sin test pareado

La comparación que sostiene el cambio de conclusión —de «−5,43 % anual (p<0,001)» (§34, L1056) a «no encuentra una pendiente anual significativa» (§59, L1381)— enfrenta dos ejecuciones sobre estados de datos distintos, sin prueba pareada ni intervalo de la diferencia; el propio [[#C004]] lo anota. Lo mismo ocurre entre `principal` y `completo` en el CSV descrito por E3: el Welch t-test aparece en el inventario de §60 (L1389), pero no se registra como contraste pareado entre esas dos especificaciones ni se declara qué comparación realiza. No hay declaración de Wilcoxon, test de signos, t-test de diferencias ni intervalo bootstrap para estos pares. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)».

— polarity: neutral · confidence: high · related: [[#C004]], [[#C005]], [[#C006]], [[#F-V2-002]], [[#F-V2-003]] · criteria: V2.statistical_tests.master

### F-V2-006 — Tamaños muestrales e instancias declarados en cada etapa

El documento explicita n en todas las fases: «11 bases» y 256 filas (§9, L94–108), «Resultados sobre 323 autos: 248 precios USD válidos» (§22, L894), «Filas ingeridas 972 [...] Filas limpias 499 [...] Observaciones del modelo OLS 328» (§34, L1045–1051), «33 respuestas de encuesta» y entrevistas «30 + 30 + 8» (E3, Datasets; §50), «15 fuentes web» con «8 semillas de marketplaces» (§55, L1337) y «981 candidatas» con 28 observaciones completas (§59, L1381). El número de instancias y de observaciones supera los umbrales numéricos del criterio. El criterio `V2.sample_size` para `level=master` se lee: «≥20 trials; ≥10 datasets/instances».

— polarity: positive · confidence: high · related: [[#C014]], [[#C035]], [[#C040]], [[#C005]], [[#C100]] · criteria: V2.sample_size.master

### F-V2-007 — Un único snapshot, sin repeticiones y cobertura desigual entre fuentes

Los recuentos son abundantes pero no constituyen repeticiones: la propia comparación declara «un único snapshot, HP/kilometraje mayormente ausentes» (§34, L1060), sin corridas independientes por condición. La cobertura de variables es heterogénea —«marca 68,4 %, año 63,5 %, km 6,2 % (heurísticos, extraídos solo de título/descripción)» (§22, L894; [[#C100]])— y la tabla de tiendas registra «Chinautos Cuba | 70 | 0» y «Envision Autos | 1 | 0» frente a «AGN Motors | 60 | 45» (§9, L96–108). En el modelo, la condición `completo` reduce el n de 584 a 28 (E3, líneas 138–144), apenas sobre el umbral de veinte observaciones. El criterio `V2.sample_size` para `level=master` se lee: «≥20 trials; ≥10 datasets/instances».

— polarity: neutral · confidence: high · related: [[#C014]], [[#C100]], [[#C105]], [[#F-V2-002]], [[#F-V2-006]] · criteria: V2.sample_size.master

### F-V2-008 — Subsección «Límites» dedicada y auditoría de procedencia

El marco de análisis incluye el apartado específico «**Límites**: precios pedidos no transaccionados, sesgo de supervivencia de anuncios, sin datos personales, vigencia normativa a verificar» (§19, L855; [[#C013]]). La auditoría de procedencia lo refuerza: «No son estadísticas oficiales; son precios **pedidos**, no transaccionados» y «las fuentes oficiales y gremiales sirven de **contexto y validación**; los anuncios y redes son la **señal de precio** pero no sustituyen estadísticas oficiales» (§18, L826, L831; [[#C007]]). Se añaden supuestos operativos —«no se comprueba disponibilidad en tiempo real» (§23, L903; [[#C103]])— y la distinción «inferencia de diseño, no medición» para la retención (§63, L1417; [[#C053]]). El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations».

— polarity: positive · confidence: high · related: [[#C007]], [[#C013]], [[#C053]], [[#C103]], [[#C108]] · criteria: V2.threats_to_validity.master

### F-V2-009 — Atribuciones causales sin diseño comparativo

Tres afirmaciones conservan forma causal sin contraste de condiciones: «El scraping sostenible depende del ritmo, la sesión y la reanudación, no principalmente del fingerprint TLS» (§12, L137; [[#C027]]), «La regla de las 10 páginas evitó consumir resultados repetidos» (§12, L138; [[#C028]]) y la jerarquía «la ruta más eficiente es Telegram MTProto [...] Le sigue Facebook GQL» (§15, L767–769; [[#C032]]), y el inventario E1 anota «jerarquía declarada sin medición comparativa de rendimiento». Las dos primeras se apoyan en reglas y conteos (§7, L78–84; §11, L126–131), no en condiciones comparadas. El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations».

— polarity: neutral · confidence: high · related: [[#C027]], [[#C028]], [[#C032]], [[#F-V2-008]] · criteria: V2.threats_to_validity.master

### F-V2-010 — Protocolo con puntos de entrada, manifiestos con hash y regeneración documentada

La arquitectura declara `config.py` y `01_ingest.py` a `05_benchmark.py`, además de `run_all.py` (§34, L1020–1036); la regeneración se registra en «`run_all.py` volvió a correr sobre la base de 744 autos» (§51, L1280) y «El pipeline se regeneró con el entorno `Auxiliares/.venv-py`» (§58, L1371). La integridad se documenta con «un `MANIFEST.json` que guarda el SHA-256 del archivo completo, el orden, el offset y el hash de cada fragmento. La verificación de los 82 chunks dio OK» (§54, L1325), con reconstrucción por hash también en la sincronización por timer (§14, L756). E3 inventaría los entry points y `test_modelo.py` comprueba la idempotencia de `04_stats.py`; la compilación «`mkdocs build --strict` termina sin errores ni enlaces rotos» (§61, L1399). La parte «Protocol fully described» y «code referenced» del criterio queda cubierta; la cláusula de semillas se evalúa por separado. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced».

— polarity: positive · confidence: high · related: [[#C002]], [[#C033]], [[#C042]], [[#C054]], [[#F-V2-011]] · criteria: V2.reproducibility_protocol.master

### F-V2-011 — Semillas: solo URLs de entrada, ninguna semilla aleatoria declarada

La única aparición de «semillas» en el documento es «Las 8 semillas de marketplaces también se descargaron y se contaron sus enlaces de anuncio» (§55, L1337): son URLs de partida del crawl, no semillas de generación aleatoria. No hay `seed`, `random_state` ni declaración equivalente en §34 (L1018–1039), §59 (L1379–1381) ni §60 (L1387–1389), y el inventario E1 no registra ningún claim de semillas. Los elementos estocásticos declarados —«Pausa 7–10 s con jitter» (§11, L127) y las «26 búsquedas en tgden.com» para descubrir canales ([[#C113]])— se describen sin semilla asociada. Las estimaciones reportadas (OLS, medianas, IQR, VIF, pruebas de rangos) son deterministas dado el dataset, pero la conjunción literal del criterio no se satisface. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced».

— polarity: neutral · confidence: high · related: [[#C002]], [[#C005]], [[#C074]], [[#C075]], [[#C113]], [[#F-V2-010]] · criteria: V2.reproducibility_protocol.master

### F-V2-012 — Tres estados incompatibles del mismo modelo sin marcador de versión

El estado vigente de §59 es «28 observaciones completas de 981 candidatas (R² = 0,277; p del F = 0,411)» (L1381), con marcadores `<!-- kpi:modelo_* -->` que se actualizan desde `kpis.csv`. El CSV archivado registra, para esa misma `completo`, R² 0,2744 y p 0,4114, y para `principal` 584 observaciones con R² 0,101 y p 0,0 (E3, líneas 138–144); en paralelo, `MODELOS_Y_FUNCIONES.md` y sus copias describen «572 observaciones de 897 candidatas [...] el completo usa 22 (R² = 0,277; p del F = 0,623)» (E3, línea 143). El paralelo inglés de §59 añade otro estado: «744 unique cars, 2,014 clean listings» (L1383) frente a «772 autos únicos, 2.029 anuncios limpios» del español (L1379). E1 califica F-V10-001 como «PARCIALMENTE RESUELTA» y F-V10-008 como «RESUELTA», pero las tres versiones del modelo no llevan etiqueta que indique cuál produce cada cifra. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced»; la coherencia interna entre secciones queda sin resolución.

— polarity: negative · confidence: high · related: [[#C003]], [[#C005]], [[#C050]], [[#F-V10-001]], [[#F-V10-008]], [[#F-V2-002]], [[#F-V2-011]] · criteria: V2.reproducibility_protocol.master


## §3 — v3-results-evidence


# V3 — Resultados ↔ evidencia

Se recorren los claims de tipo `result` y los claims metodológicos con contenido numérico del inventario E1 de la iteración 2, contrastados contra los CSV vigentes en `Data/analisis_rentabilidad/outputs/tables/` y contra el inventario E3 de esta misma iteración. Los números del modelo se leen de `modelo_muestra.csv` (principal: 981 candidatas / 584 observaciones / R² 0,101 / p_f 0,0; completo: 981 / 28 / 0,2744 / 0,4114).

### F-V3-001 — «2.029 anuncios limpios» y «43.000 km» en §59 contra 2.156 y 33.256 km en el `kpis.csv` que cita

El §59 (L1379) afirma: «El relato ahora usa **772 autos únicos**, **2.029 anuncios limpios** (1.338 locales y 691 de importación), mediana local de **21.000 USD**, kilometraje mediano de **43.000 km**, 50 marcas, 101 grupos comparables y 81 anomalías (corrida vigente del 27/11/2026; los valores se actualizan solos en `outputs/tables/kpis.csv`)». El archivo citado, `Data/analisis_rentabilidad/outputs/tables/kpis.csv`, registra `anuncios_totales=2156.0`, `anuncios_locales=1465.0`, `anuncios_importacion=691.0`, `precio_mediano_usd=21000.0`, `marcas_distintas=50.0` y `km_medianos=33256.0`; `benchmark.csv` contiene 113 filas de datos y `anomalias.csv` 89. Coinciden tres de las nueve cifras (691, 21.000 USD, 50); difieren las otras seis: 772/952 autos (el marcador `<!-- kpi:autos_revolico -->` de `PRESENTACION_STORYTELLING.md:3,75` vale 952), 2.029/2.156, 1.338/1.465, 43.000/33.256 km, 101/113 grupos y 81/89 anomalías.

La cláusula «los valores se actualizan solos en `outputs/tables/kpis.csv`» no se sostiene en el estado contrastado: `Auxiliares/herramientas/actualizar_numeros.py:49–86` deriva precisamente `anuncios_totales`, `anuncios_locales`, `km_medianos`, `grupos_benchmark` (longitud de `benchmark.csv`) y `anomalias` (longitud de `anomalias.csv`) de esos CSV, y son los valores del párrafo anterior los que allí figuran. El propio `PRESENTACION_STORYTELLING.md:75–77,201–211`, que §59 dice haber actualizado con la narrativa vigente, lleva los marcadores resueltos 952 / 2.156 / 1.465 / 33.256 km / 113 / 89, no los del informe. El inventario E3 (§Missing artifacts, líneas 268–271) ya anticipó esta desincronización parcial del artefacto.

— polarity: negative · confidence: high · related: [[#C003]], [[#C050]], [[#C036]]

### F-V3-002 — Tres estados de la misma corrida conviven entre §58, §59 español y §59 inglés

El §59 español (L1379) describe la «corrida vigente del 27/11/2026» con 772 autos, 2.029 anuncios y 43.000 km; el párrafo **EN.** inmediatamente posterior (L1383) presenta esa misma sección con «744 unique cars, 2,014 clean listings, 21,000 USD median»; y §58 (L1371) atribuye a la regeneración anterior «**2.014 anuncios limpios**, de ellos 1.323 locales y 691 de importación; mediana local 21.000 USD y mediana de kilometraje 44.125 km». El espejo inglés no reproduce la cifra de su párrafo español, sino el estado previo. §51 (L1279) añade 744 autos únicos y §45 (L1214) una cuarta versión con mediana de 23.000 USD, 6,3 años, 34 marcas, 27 grupos y −5,43 %/año, sin marca de vigencia. Solo §59 español rotula su estado como vigente; los pasajes paralelos sostienen cifras distintas sin señalar la fecha de referencia que las diferencia.

— polarity: negative · confidence: high · related: [[#C003]], [[#C036]], [[#C049]], [[#C050]], [[#C006]]

### F-V3-003 — R² 0,277 en §59 frente a 0,274 en `modelo_muestra.csv` y en `MODELOS_Y_FUNCIONES.md`

El §59 (L1381) escribe, con marcadores automáticos: «El modelo con todos los términos dispone de **<!-- kpi:modelo_n_completo -->28 observaciones completas** de <!-- kpi:modelo_candidatas -->981 candidatas (R² = <!-- kpi:modelo_r2_completo -->0,277; p del F = <!-- kpi:modelo_pf_completo -->0,411)». En `modelo_muestra.csv` la fila `completo` registra `r2=0.2744`, y `modelo_resumen.txt` muestra «R-squared: 0.274»; `Auxiliares/herramientas/actualizar_numeros.py:80` formata esa clave con tres decimales, lo que da `0,274`. El mismo marcador en `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md` está resuelto como `<!-- kpi:modelo_r2_completo -->0,274`. El valor 0,277 no es el redondeo de 0,2744 y coincide con el estado retirado de 22 observaciones de 897 candidatas que describe el inventario E3 (línea 143). Los otros tres marcadores de la frase sí concuerdan con el CSV: `observaciones=28`, `candidatas=981` y `p_f=0.4114` → 0,411.

— polarity: negative · confidence: high · related: [[#C003]], [[#C004]], [[#C005]]

### F-V3-004 — «p mínimo 0,165» y «VIF 1,13–1,58» de §60 no aparecen en los CSV de la corrida vigente

El §60 (L1389) afirma que «la corrida actual **no** sostiene una tasa de depreciación ni una prima premium significativa (p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05)». En `modelo_depreciacion.csv` el menor `p_valor` de los coeficientes no intercepto es 0,0941 (`C(brand_tier)[T.medio]`), `car_age` vale 0,1504 y `hp` 0,1403; en `vif.csv` el rango va de 1,12 (`hp`) a 1,40 (`mileage_km`); y `tests.csv` registra el Kruskal-Wallis con `p_valor=0.0`, sin la precisión `1e−05` que consigna el texto. Las tres cifras del paréntesis sí se encuentran en la fuente citada por §60, `MODELOS_Y_FUNCIONES.md` (líneas 56 y 62: «el p_valor más bajo es 0,165, de potencia; antigüedad tiene p = 0,237» y «los actuales van de 1,13 a 1,58»), de modo que la cadena claim → documento citado → CSV se rompe en el último eslabón: esas cifras son de una corrida anterior. La afirmación cualitativa de fondo, en cambio, se sostiene con los archivos vigentes: los siete coeficientes no intercepto tienen p ≥ 0,0941 y ninguno alcanza 0,05.

— polarity: negative · confidence: high · related: [[#C004]], [[#C005]]

### F-V3-005 — El modelo principal de 584 observaciones queda fuera del relato de «no significancia» de §59

El §59 (L1381) sintetiza: «la depreciación se reformuló con honestidad: el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje». `modelo_muestra.csv` contiene una segunda especificación, `principal` (981 candidatas, 584 observaciones, R² 0,101, `p_f=0.0`), que el párrafo no menciona: el único modelo cuantificado en la frase es el `completo`, de 28 observaciones y `p_f=0.4114`. El propio `MODELOS_Y_FUNCIONES.md`, en el bloque «Modelo principal frente a modelo completo», registra que «en el modelo principal el coeficiente de antigüedad es positivo y alcanza p < 0,05» y lo atribuye a «un artefacto de selección, no una tasa anual» de la submuestra que declaró kilometraje. La frase en singular «el modelo actual» describe por tanto una de las dos especificaciones archivadas, y `actualizar_numeros.py:82–86` expone explícitamente los marcadores del modelo omitido (`modelo_n_principal`, `modelo_r2_principal`, `modelo_pf_principal`) que §59 no usa. La cobertura del relato es parcial respecto de la evidencia del propio pipeline.

— polarity: negative · confidence: high · related: [[#C004]], [[#C005]]

### F-V3-006 — La retirada de la depreciación y de la prima premium coincide con los coeficientes archivados

El §59 (L1381) sostiene que «la depreciación se reformuló con honestidad: el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra», y §60 (L1389) que «la corrida actual **no** sostiene una tasa de depreciación ni una prima premium significativa». En `modelo_depreciacion.csv` el coeficiente de `car_age` es −0,0632 con `p_valor=0.1504` y el de `C(brand_tier)[T.premium]` es +0,1146 con `p_valor=0.8753`; `modelo_resumen.txt` reproduce la misma estimación (28 observaciones, R² 0,274, F 1,081, p del F 0,411). Ninguno de los siete coeficientes no intercepto alcanza p < 0,05. La retirada del −5,43 %/año y del +21 % de prima de la §34 (L1056) como cifras vigentes queda respaldada por los archivos de la corrida, con la salvedad de la especificación principal de 584 observaciones descrita en [[#F-V3-005]]. Los marcadores `28`, `981` y `0,411` de §59 también coinciden con `modelo_muestra.csv`; el que no coincide es el R² (ver [[#F-V3-003]]).

— polarity: positive · confidence: high · related: [[#C004]], [[#C005]], [[#C006]], [[#F-V3-003]]

## Resumen

- Seis hallazgos: cinco negativos y uno positivo; ninguno depende de un juicio de nivel, sino de cotejo claim ↔ CSV.
- §59 cita `kpis.csv` como fuente autoactualizada pero seis de sus nueve cifras difieren de los CSV vigentes (2.029/2.156; 43.000/33.256 km; 101/113; 81/89).
- El R² 0,277, el p mínimo 0,165 y el VIF 1,13–1,58 de §59–§60 corresponden a una corrida anterior; la no significancia cualitativa sí se sostiene, aunque el modelo principal de 584 observaciones queda fuera del relato.


## §4 — v4-novelty


## Resumen

- E1 registra una sola afirmación etiquetada `novelty` (C011, §34): la arquitectura del pipeline adaptada de `Egyptian-Used-Cars`; el diferenciador sigue siendo de integración local, sin componente nuevo.
- La nueva §70 y `Data/referencias.md` **no resuelven F-V10-006**: añaden transparencia bibliográfica (38 referencias, cuatro verificadas) pero ningún contraste argumentativo con los vecinos académicos más cercanos (P014, P026, P009, P029), todos `Cited in document: no`.
- No se detecta sobreclaim de originalidad; tampoco puede declararse «novedad confirmada», porque la iteración 2 fue una re-verificación de metadata (`papers_l3: 0`, consultas no temáticas) y el propio E2 constata que los flags y la contradicción de Akerlof (P001) permanecen.

### F-V4-001 — E1 registra un solo claim `novelty`: la arquitectura adaptada de Egyptian-Used-Cars

El inventario de la iteración 2 consigna «By type: result 60 · methodological 43 · novelty 1 · contextual 43 · definitional 5 · citation-grounded 11» (e1-claims, línea 15). El único objeto de esta evaluación es C011 (líneas 139–149), que cita verbatim en §34 (L1018): «Creé `Data/analisis_rentabilidad/` siguiendo la arquitectura del repositorio **Egyptian-Used-Cars** (ingesta → limpieza → EDA → estadística → benchmark), pero adaptada a nuestras fuentes y preparada para crecer:». El propio E1 anota en C011: «es la única diferenciación comparativa declarada del documento (F-V10-006)». El diferenciador declarado es de integración —adaptación de una arquitectura de ingeniería a las fuentes cubanas y disposición a crecer—, no de componente ni de formulación de problema. La brecha «frente a Egipto» descrita en C012 (§34, L1058–1060) es de escala y cobertura: «solo 497 usados, un único snapshot, HP/kilometraje mayormente ausentes», es decir, una diferencia de datos en contra del propio proyecto.

El criterio `V4.scope_of_novelty_claim` para `level=master` se lee: «Component novelty + integration novelty: one of the two should be substantive» (level-criteria.md, línea 97). La integración aquí es substantiva en términos de ingeniería (adaptadores por dominio, SQLite por tienda, procedencia), pero el texto la presenta como adopción y adaptación de una arquitectura ajena, no como contribución de método; no hay una reclamación de primacía global que cotejar.

— polarity: neutral · confidence: high · related: [[#C011]], [[#C012]], [[#F-V10-006]] · criteria: V4.scope_of_novelty_claim.master

### F-V4-002 — §70 y `Data/referencias.md` no resuelven F-V10-006: transparencia sin contraste

La sección nueva §70 (L1477–1479) declara: «Referencias citadas y verificadas externamente durante la auditoría: Akerlof (1970), *The Market for "Lemons"* (Crossref/OpenAlex); UK Department for Transport / DVLA, estadísticas de vehículos (GOV.UK); ANFAC, informes del sector automotriz español (sitio oficial); AEADE, estadísticas de matriculaciones (sitio oficial)», y remite «La convención numerada de 38 referencias y su estado de verificación [...] en `Data/referencias.md`». El archivo enlazado contiene 38 entradas con `Citada: sí/no` y seis marcadores `(metadata incomplete)`. El propio E1 lo confirma en su contexto de iteración: «**F-V10-006 — Diferenciación solo contra el repositorio egipcio: NO RESUELTA.** §34 (L1018, L1058–1060) sigue siendo el único pasaje comparativo, por escala de datos; §70 (L1477) añade cuatro referencias verificadas pero ningún contraste argumentativo con los vecinos académicos. El inventario registra una sola señal de novedad (C011, L1018)» (L849).

El criterio `V4.prior_art_engagement` para `level=master` exige «Closest prior works cited, contrasted, and discussed in their own subsection» (level-criteria.md, línea 106). §70 satisface la primera condición para Akerlof (P001) y para tres fuentes institucionales (P007–P009), pero no las otras dos: no hay discusión de métodos, resultados o limitaciones de los trabajos más cercanos al claim de C011, ni subsección dedicada a ellos. Los vecinos de ese claim —P014 (Gegić et al., 2019), P026 (Muça et al., 2026), P009 (Du et al., 2026) y P029 (Vidal Alejandro et al., 2024)— figuran en `Data/referencias.md` como [14], [26], [9] y [29] y mantienen «Citada en el informe: no»; aparecer en la lista numerada no equivale a estar citados en el cuerpo. En paralelo, E2 constata en H1 que «mejoró la transparencia formal, no la completitud de los campos señalados» (L176) y en H2 la doble etiqueta de Akerlof: verificada en §70 y `(metadata incomplete)` en [1] (L180). La resolución de F-V10-006 queda, por tanto, en el plano formal/bibliográfico, no en el de la novedad.

— polarity: negative · confidence: high · related: [[#C011]], [[#C009]], [[#C048]], [[#P001]], [[#P007]], [[#P008]], [[#P009]], [[#F-V10-006]], [[#F-V4-003]] · criteria: V4.prior_art_engagement.master

### F-V4-003 — Único párrafo comparativo: repositorio egipcio, no el vecino académico

El pasaje comparativo sigue siendo «Brecha frente a Egipto» (§34, L1058–1060): «Egipto tiene 23.500 anuncios, historial mensual de precios, HP y kilometraje estructurados, ANOVA/OLS/VIF, Tableau y Power BI. Nosotros tenemos el pipeline y las técnicas cubiertas, pero solo 497 usados, un único snapshot, HP/kilometraje mayormente ausentes y un solo benchmark de auto nuevo». El referente es `Egyptian-Used-Cars`, fuente de ingeniería que no figura en el mapa E2; la comparación opone escalas de datos y declara una desventaja, sin discriminar qué hace diferente el método propio.

Los vecinos académicos del claim están en el mapa completo de la pasada 1, que la iteración 2 declara vigente (e2-literature iter2, nota (b), L16): P014 — Gegić, E.; Isaković, B.; Keco, D.; Mašetić, Z.; Kevrić, J. (2019), «Car Price Prediction using Machine Learning Techniques», *TEM Journal*, DOI 10.18421/tem81-16, descrito como «el antecedente más directo de la combinación scraping + modelado de precios» (L176) —; P026 — Muça, M.; Bani, K.; Alla, A. (2026), «A Pipeline for Integrating and Analyzing Public Business Data in Albania Using Web Scraping and Machine Learning», *IJACSA*, DOI 10.14569/ijacsa.2026.0170845 —; y P009 — Du, Z.; Yang, Z.; Zhang, Y.; Li, S.; Liu, Y. (2026), «Nonlinear Depreciation and Brand Heterogeneity in Chinese Used-Car Listing Prices: An Interpretable Hedonic Regression and Out-of-Sample Evaluation», DOI 10.54254/2754-1169/2026.38524, «el paralelo metodológico más cercano al informe» (L123). Los tres están marcados `Cited in document: no`. Bajo `V4.differentiation_from_prior_art.master` («Differentiator articulated with at least one explicit comparison paragraph to one closest prior work», level-criteria.md, línea 88), la forma del criterio se cumple solo respecto de una fuente ajena al mapa: sigue sin haber párrafo comparativo con el trabajo académico más cercano.

— polarity: negative · confidence: high · related: [[#C011]], [[#C012]], [[#P009]], [[#P014]], [[#P026]], [[#F-V10-006]], [[#F-V4-002]] · criteria: V4.differentiation_from_prior_art.master

### F-V4-004 — No se detecta sobreclaim: alcance local declarado y recomendador diferido

El claim evaluado usa verbos de adopción, no de primacía: §34 (L1018) dice «siguiendo la arquitectura del repositorio **Egyptian-Used-Cars** [...] pero adaptada a nuestras fuentes» y el encabezado del §34 (L1016) rotula el trabajo como «inspirado en Egyptian-Used-Cars». El marco analítico se presenta como «**Marco general (8 pasos, derivado de los trabajos revisados)**» (§19, L837) y el objetivo vigente excluye explícitamente la novedad de producto: «La definición de un producto interactivo que recomiende la compra más rentable según las preocupaciones del usuario queda diferida a una especialización posterior» (§1, L16; C001). No aparece en el texto una afirmación de «primero», «nuevo método» o «contribución original» que contradiga a los trabajos del mapa; la única reclamación comparativa, «Brecha frente a Egipto», se enuncia en dirección desfavorable al propio proyecto. Bajo `V4.scope_of_novelty_claim.master`, el alcance es local y está declarado como tal; no se observa sobreclaim que corregir.

— polarity: positive · confidence: high · related: [[#C001]], [[#C011]], [[#C012]], [[#P014]] · criteria: V4.scope_of_novelty_claim.master

### F-V4-005 — Iteración 2 sin búsquedas temáticas ni lectura L3: sin novedad confirmada

El mapa E2 de esta pasada declara `queries_run: 22`, `papers_l1: 6`, `papers_l2: 6`, `papers_l3: 0` (frontmatter) y explica que «las consultas se derivaron del mandato recibido —comprobar si la nueva §70 y `Data/referencias.md` resolvieron los `(metadata incomplete)` de la pasada 1— y no son búsquedas temáticas nuevas» (L16). La sección `likely_missing important works` se limita a declarar «Sin cambios respecto al mapa de la pasada 1» (L168). En consecuencia no se incorporó ningún trabajo capaz de desplazar a P014, P026 o P009 como vecinos más cercanos, y tampoco se leyó texto completo que permita refinar el solapamiento. Los tres flags heredados cuyo motivo era el conteo de citas (P003, P004, P005) «sí se resolvió por OpenAlex (13, 96 y 9 citas respectivamente), pero `Data/referencias.md` no incorporó ni los conteos ni las versiones publicadas con DOI; los marcadores siguen ahí» (H1, L176); P001 conserva el resumen como índice de secciones y P002 el suyo sin indexar.

Una conclusión de «novedad confirmada» excedería esta evidencia: según el criterio `V4.prior_art_engagement.master` (level-criteria.md, línea 106), los trabajos más cercanos no están citados en el cuerpo, contrastados ni discutidos en su propia subsección, y el mapa disponible es el mismo de la pasada 1 con una capa de re-verificación de metadata. La lectura permitida es «sin antecedente nuevo añadido en esta pasada», no ausencia de arte previo ni validación de originalidad.

— polarity: neutral · confidence: high · related: [[#C009]], [[#C048]], [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#P005]], [[#P014]], [[#F-V4-002]] · criteria: V4.prior_art_engagement.master


## §5 — v5-state-of-the-art


- Cobertura y actualidad: 1 de 38 referencias numeradas está marcada «Citada: sí» (2,6 %); 18 de 38 (47,4 %) son de 2022–2026 en la bibliografía, pero ninguna de ellas aparece citada en el cuerpo del informe.
- Peso y ausencias: Akerlof pasa de 2 a 3 menciones con nombre (4 apariciones en total) con §70, mientras 9 de 13 afirmaciones load-bearing siguen «sin citas numeradas» y las ocho obras de la lista de ausencias probables permanecen fuera del texto.
- Flags: seis marcadores `(metadata incomplete)` sin campo especificado; tres motivos resueltos en vivo ([18], [19], [20]) no reflejados, dos vigentes ([1], [10]) y uno nuevo ([38]); §70 mantiene la contradicción con [1].

### F-V5-001 — Cobertura tras la numeración — 1 de 38 referencias citada en el cuerpo y 37 marcadas «Citada: no»

La iteración 2 incorpora `Data/referencias.md`, enlazado desde §70 (L1477), con 38 entradas numeradas generadas a partir del mapa E2 de la pasada 1. El campo «Citada en el informe: sí/no» registra «yes» solo en [1] (Akerlof, L8); las 37 restantes dicen «no», incluidas todas las obras de 2024 o posteriores. E2 de iter2 (L16, L144) define «Cited in document» por mención nominal y «In document bibliography» por presencia en `Data/referencias.md`, de modo que la formación del aparato numerado no equivale a engagement con la literatura. La distribución por clúster del mapa de 38 trabajos se mantiene en 1/8 para asimetría de información y 0/12, 0/8, 0/7 y 0/3 para modelos de precio, ética/procedencia/calidad, Cuba/divisas/movilidad y señales de marketplace. El criterio `V5.coverage_breadth.master` se lee: «Main + adjacent clusters covered (25–60 papers)».

§70 (L1477) nombra tres fuentes institucionales adicionales —DfT/DVLA, ANFAC y AEADE— que no figuran en la lista numerada y que E2 cataloga como fuentes de datos (P007–P009, L102–140), no como entradas del mapa académico. Su presencia no altera el recuento de 1/38. En el cuerpo, Akerlof aparece en la tabla de aportes metodológicos de §17 (L797), en el marco general de §19 (L841) y, sin el nombre del autor, en el marco detallado de §20 (L865); los siete requerimientos de §19 (L853) y los bloques analíticos de §20 (L863–L871) no incorporan ninguna de las otras 37 obras, aunque la tabla de §17 (L787–806) convierte fuentes del corpus en requerimientos de captura.

— polarity: negative · confidence: high · related: [[#P001]], [[#F-V5-003]] · criteria: V5.coverage_breadth.master

### F-V5-002 — Actualidad — 18 de 38 referencias de los últimos cinco años en la bibliografía, 0 citadas en el cuerpo

`Data/referencias.md` contiene seis entradas de 2026 ([9], [10], [11], [24], [26], [35]), una de 2025 ([22]), seis de 2024 ([18], [25], [28], [29], [30], [32]), cuatro de 2023 ([15], [23], [27], [34]), una de 2022 ([17]) y veinte de 2021 o antes. El tramo 2022–2026 suma 18 de 38 (47,4 %), proporción que supera el umbral del criterio `V5.recency.master` —«At least 40% from the last 5 years; foundational classics balanced»— si se mide la bibliografía numerada. La tabla de distribución de E2 de iter2 (L142–153) cubre únicamente las seis entradas re-verificadas (1 de 2026, 1 de 2024, 4 de ≤2021) y no el listado completo. El recuento directo de años del mapa de la pasada 1 difiere de su tabla resumen (L439–451): 6 y 4 entradas en 2026 y 2023 frente a 7 y 3, con 13 frente a 14 obras de 2024 o posteriores; el total de 2022–2026 es 18 en ambas lecturas.

Las 18 referencias recientes conservan «Citada en el informe: no». La única obra académica citada en el cuerpo es Akerlof 1970, también en §70 (L1477), por lo que la proporción de citas de los últimos cinco años es 0 de 1 (0 %): el clásico fundacional no aparece acompañado en el argumento por las obras contemporáneas del mapa, incluidos los dos textos completos leídos por E2 (ProbSAINT 2024, arXiv:2403.03812; Hohensinner et al. 2026, arXiv:2601.14311) y los tres trabajos de 2026 sobre precios de anuncios [9], [10] y [11].

— polarity: negative · confidence: high · related: [[#P001]], [[#F-V5-001]] · criteria: V5.recency.master

### F-V5-003 — Peso de la citación — 9 de 13 afirmaciones load-bearing sin cita y 37 entradas numeradas sin nombre en el texto

El inventario de E1 de esta iteración registra 13 afirmaciones load-bearing (L14). Nueve conservan «External evidence cited: — (sin citas numeradas)» en los casos C001–C006, C008, C010 y C013 (L27, L39, L51, L63, L75, L87, L111, L135, L171); dos —C007 (L99) y C009 (L123)— remiten a las fuentes institucionales de §18 y §70, y dos —C011 y C012 (L147, L159)— al repositorio `Egyptian-Used-Cars`. El cuerpo del documento no contiene ninguna marca `[N]`: la búsqueda de corchetes con dígitos devuelve 0 coincidencias en las 1.484 líneas del texto auditado, pese a la existencia de la lista numerada. El criterio `V5.citation_weight.master` se lee: «Load-bearing claims cite source + author named in body at first mention».

El único autor académico nombrado en el texto sigue siendo Akerlof, ahora en cuatro puntos: tabla de §17 (L797), marco general de §19 (L841), conceptos sin nombre en §20 (L865) y §70 con título y año (L1477). Es una mención recurrente pero confinada a la enunciación del marco teórico: no hay párrafo propio que discuta el trabajo ni vínculo con los resultados de §59–§60 (L1379–1391). Las tres fuentes institucionales de §70 se nombran una sola vez cada una y permanecen fuera de la numeración; E1 consigna en C009 (L125) que «el cuerpo del informe sigue sin citas numeradas».

— polarity: negative · confidence: high · related: [[#C009]], [[#F-V5-001]], [[#F-V5-006]] · criteria: V5.citation_weight.master

### F-V5-004 — Tres flags resueltos en vivo en la iteración 2 y no reflejados en las fichas [18], [19] y [20]

E2 de iter2 (L50–87) re-verificó tres entradas cuyo único motivo de `(metadata incomplete)` era un conteo de citas no accesible por HTTP 403 de Semantic Scholar en la pasada 1. P003 —ProbSAINT, [18] (L42)— tiene ahora 13 citas y DOI de la versión publicada `10.1109/bigdata62323.2024.10825740` vía OpenAlex W4406461714 (L54–61). P004 —Pal et al., [19] (L44)— tiene 96 citas y versión publicada de 2018 en Springer, `10.1007/978-3-030-03402-3_28` (L63–74). P005 —Arefin, [20] (L46)— tiene 9 citas y DOI `10.48550/arxiv.2101.03788` (L76–87). En los tres casos el dato ausente pasó a estar disponible por otra vía.

Las tres fichas de `Data/referencias.md` conservan el marcador genérico sin campo, sin los conteos y sin los DOI de la versión publicada: [18] y [19] mantienen solo la URL de arXiv, y [19] mantiene el año 2017 frente a la publicación de 2018, discrepancia no consignada. E2 (H1, L174–176) describe el estado como «resuelto en vivo pero no reflejado». La consecuencia para la calibración es que tres de las seis entradas marcadas son verificables campo por campo, pero la ficha no distingue entre un dato aún ausente y un dato ya recuperado.

— polarity: negative · confidence: high · related: [[#F-V5-005]] · criteria: V5.citation_weight.master

### F-V5-005 — Dos flags con motivo sustantivo vigente y un sexto introducido sin justificación

En [1] (L8), el campo bibliográfico está completo y verificado en OpenAlex, pero el resumen indexado sigue siendo el índice de secciones de la revista, no un resumen sustantivo; E2 (P001, L24–35) declara el flag «no resuelto en su motivo». En [10] (L26), Kang & Fu 2026 tienen título, autores, afiliación, revista, volumen, artículo y 3 citas verificadas, pero `abstract_inverted_index` es `null`; E2 (P002, L37–48) registra el mismo estado. En [38] (L82), el marcador aparece por primera vez en esta iteración: la pasada 1 tenía la obra verificada con 136 citas y sin flag, y la re-verificación confirma título, autores, revista, volumen, páginas y DOI, con texto completo en acceso verde vía Universidad de Manchester aunque el resumen de OpenAlex siga sin indexarse (P006, L89–100). La ficha no explica la causa del nuevo marcador ni registra la discrepancia de año entre 2015 (OpenAlex y la ficha) y 2016 (`published-print` de Crossref). Los seis marcadores de `Data/referencias.md` —[1], [10], [18], [19], [20] y [38]— usan la misma etiqueta `(metadata incomplete)` sin nombre de campo; E2 (L176) observa que un marcador por campo es lo que permite a V5 y V8 confiar o descontar cada entrada.

— polarity: negative · confidence: high · related: [[#P001]], [[#F-V5-004]], [[#F-V5-006]]

### F-V5-006 — Estado «verificado» de §70 frente a la ficha [1] y límites de tres fuentes institucionales

§70 (L1477) presenta a Akerlof 1970 como «referencia citada y verificada externamente (Crossref/OpenAlex)», mientras [1] (L8) lo mantiene como `(metadata incomplete)`. La re-verificación de E2 (L28, L174–180) confirma los campos bibliográficos por OpenAlex, pero Crossref devolvió HTTP 429, de modo que solo una de las dos mitades de la afirmación de §70 pudo contrastarse en esta pasada; la ficha no especifica qué campo falta. Las tres fuentes institucionales sí se verificaron en vivo a nivel de organismo: ANFAC expone matriculaciones de octubre de 2026 y cifras de 2025 (P007, L106–116); AEADE publica ventas Ene–sep 2026, pero es la asociación ecuatoriana y §70 no lo aclara, con riesgo de inferencia de nacionalidad desde el contexto de ANFAC (P008, L118–128); DVLA/DfT mantiene 48 millones de registros y la serie «Vehicle licensing statistics data files» del 23/09/2026, aunque tres URL directas devolvieron 404 y el `WebSearch` de apoyo falló, sin enlace profundo confirmado (P009, L130–140).

— polarity: negative · confidence: medium · related: [[#P001]], [[#C009]], [[#F-V5-005]] · criteria: V5.citation_weight.master

### F-V5-007 — Ausencias probables — 8 de 8 de la lista de E2 y 22 de 23 del top-5 por clúster siguen fuera del texto

La lista «Likely missing important works» del mapa de la pasada 1 (E2 iter1, L490–530) contiene ocho entradas que la iteración 2 reafirma sin cambios, porque la re-verificación no ejecutó búsquedas temáticas nuevas (E2 iter2, L166–168). Las ocho permanecen ausentes del documento y de la columna «Citada en el informe: no»: Lewis 2011 (P002 del mapa anterior, 342 citas), Englmaier et al. 2017 (P004, 50), Gegić et al. 2019 (P014, 188), Krotov et al. 2020 (P021, 224), Priestley et al. 2023 (P023, 153), Brown et al. 2025 (P022, 118), Guerra 2015 (P033, 113) y Hohensinner et al. 2026 (P024, 13). El proveedor de `WebSearch` volvió a fallar en esta iteración (L184), por lo que no se propusieron obras nuevas.

La relación con afirmaciones cargadas se mantiene: Lewis conecta el marco de Akerlof (§17, L797) con la captura de defectos y tipo de vendedor (§19, L853); Englmaier advierte sobre saltos en umbrales de año y 10.000 km frente a `precios_por_anio.csv` (L902); Gegić es el paralelo de scraping más modelado de §8 (L90) y §34 (L1018); Krotov y Brown corresponden a la regla operativa de §10 (L118); Priestley a la arquitectura de colas y cuarentena (§16); Guerra a `asequibilidad = precio / salario` (L853); Hohensinner a la distinción entre procedencia y linaje de §54. El criterio `V5.missing_important_work.master` se lee: «Top-5 most-cited of each adjacent cluster expected». Los cinco primeros por citas de cada clúster suman 23 obras distintas y solo P001 está citada: 22 ausentes (95,7 %).

— polarity: negative · confidence: high · related: [[#F-V5-001]] · criteria: V5.missing_important_work.master

### F-V5-008 — Mejora formal del aparato — 38 referencias numeradas, campo de citación y cuatro fuentes declaradas verificadas

La iteración 2 incorpora un aparato de 38 referencias numeradas con autor, título, revista, año, DOI o URL y un campo explícito «Citada en el informe: sí/no» (`Data/referencias.md`, L1–82), enlazado desde §70 (L1477) y con correspondencia claim-fuente remitida al expediente forense. La pasada 1 no tenía bibliografía numerada y la única obra académica reconocible en el cuerpo se identificaba por mención nominal. §70 distingue cuatro fuentes verificadas externamente y declara que el resto permanece marcado, información que E1 registra como afirmación load-bearing C009 (E1 iter2, L115–125) y que atiende parcialmente la observación transversal de la iteración 1. La verificación en vivo de E2 confirma tres de esas cuatro fuentes a nivel de organismo (P007–P009, L106–140) y los campos bibliográficos de la cuarta (P001, L24–35). El cambio es de transparencia formal: la lista y el estado de verificación existen y son auditables, aun cuando la citación en el cuerpo no se haya modificado.

— polarity: positive · confidence: high · related: [[#C009]], [[#F-V5-003]] · criteria: V5.citation_weight.master

### F-V5-009 — Convergencia sin engagement — la retirada de la depreciación coincide con cuatro trabajos no citados del mapa

§34 (L1056) reportó una depreciación de −5,43 % anual (p<0,001) con prima premium de +21 %; §59 y §60 (L1381, L1389) consignan que la corrida vigente no sostiene pendiente anual significativa tras corregir kilometraje, con p mínimo 0,165, VIF 1,13–1,58 y Kruskal-Wallis p = 1e−05. Cuatro obras del mapa apuntan en el mismo sentido sin aparecer en el texto: Du et al. 2026 [9] (especificación log-lineal anidada casi idéntica, relación edad–precio no lineal), Miranda et al. 2026 [11] (R² = 0,256; kilometraje p = 0,077; r = 0,639), Englmaier et al. 2017 (saltos en umbrales de año y 10.000 km) y Francke y Van de Minne 2020 [13] (heterogeneidad no observada). E2 (H2, L540–542 del mapa de la pasada 1) reúne esa evidencia. La coincidencia es de resultado, no de citación: las cuatro obras figuran con «Citada en el informe: no» en `Data/referencias.md`.

— polarity: neutral · confidence: high · related: [[#P001]], [[#F-V5-007]] · criteria: V5.citation_weight.master


## §6 — v6-reproducibility


# V6 — Reproducibilidad (nivel master / maestría)

## Resumen

- El checkout sí contiene las mejoras pedidas: `requirements.txt` usa `~=`, `Data/analisis_rentabilidad/scripts/run_all.py` declara `SEED = 20261127` y `Auxiliares/herramientas/test_smoke_pipeline.py` existe y pasa sus 4 pruebas; E3, sin embargo, no inventarió este último y todas las mejoras están sin commitear en `99c7065`.
- La calibración `master` queda parcial: el README y el comando único cubren documentación y puntos de entrada, pero `~=X.Y` fija la serie mayor (no la versión menor), la semilla no aparece en el informe y no se propaga a los cinco subprocesos, y el panel, las cifras del modelo y los KPIs del texto cacheado están desincronizados del disco.
- Las lagunas de disponibilidad de datos de la iteración 1 persisten (parque/matriculaciones, VAHAN, BCC, gacetas, campos estructurados), mitigadas solo por los manifiestos con SHA-256 de Revolico y por las fuentes oficiales con URL y licencia.

### F-V6-001 — README sustancial con quickstart, salidas esperadas y mapeo de componentes

`README.md` tiene 105 líneas y abre con `# El precio de moverse en Cuba` (`README.md:1`); la sección `## Quickstart` (`README.md:15–23`) da tres comandos ejecutables —creación de `Auxiliares/.venv-py`, `pip install -r requirements.txt` y `python Data/analisis_rentabilidad/scripts/run_all.py`—, seguidos de las tres salidas esperadas (`README.md:25–33`). La tabla `## Configuración` (`README.md:66–73`) asocia cada archivo de configuración con lo que controla y la sección `## Documentación` (`README.md:94–99`) enlaza informe, guías y datos por tipo. E3 consigna `README.md | 105` en su tabla de Documentation (`informe-tecnico-2026-11-27-iter2.e3-artifacts.md:76`) y el texto registra la reescritura en §55, línea 1341. El criterio `V6.documentation.master` —«README + dependencies list + brief usage examples»— se satisface en el checkout; la divergencia de cifras se trata por separado en [[#F-V6-007]].

— polarity: positive · confidence: high · related: [[#F-V6-004]], [[#F-V6-007]] · criteria: V6.documentation.master

### F-V6-002 — `requirements.txt` paso de `>=` a `~=`, pero sin fijación real a versiones menores

El archivo cambió respecto de la iteración 1: las doce dependencias usan ahora operadores compatibles (`pandas~=2.2`, `numpy~=1.26`, `plotly~=5.18`, `statsmodels~=0.14`, `scipy~=1.11`, `beautifulsoup4~=4.12`, `curl_cffi~=0.7`, `tenacity~=8.2`, `trafilatura~=1.6`, `pyarrow~=14.0`, `mkdocs~=1.6`, `mkdocs-material~=9.5`; `requirements.txt:3–14`) y la línea 2 afirma «Fijadas a versiones menores (criterio de reproducibilidad de nivel master)». En PEP 440, `~=2.2` equivale a `>=2.2, ==2.*` y `~=0.7` a `>=0.7, ==0.*`: la cota fija la serie mayor, no el número menor, por lo que la afirmación de la línea 2 no es exacta. Además las restricciones contradicen versiones declaradas en el propio informe: `tenacity~=8.2` excluye la 9.2.1 de §6 (L72) y `pyarrow~=14.0` excluye la 26 de §34 (L1039). No hay `pyproject.toml`, lockfile ni `Dockerfile` (E3, Environment, líneas 84–88), y la versión de Python solo aparece como `3.10+` en `README.md:17`. El criterio `V6.environment.master` —«Dependencies pinned to minor versions»— no se cumple literalmente, aunque el cambio reduce la ambigüedad respecto de `>=`.

— polarity: negative · confidence: high · related: [[#F-V6-006]], [[#C023]] · criteria: V6.environment.master

### F-V6-003 — `SEED = 20261127` declarada en el orquestador, pero ausente en el informe y sin efecto en los subprocesos

`Data/analisis_rentabilidad/scripts/run_all.py:9–18` importa `random` y `numpy`, define `SEED = 20261127` y llama a `random.seed(SEED)` y `np.random.seed(SEED)`; el docstring (`run_all.py:4–7`) afirma explícitamente «La semilla se declara aqui y en el informe para cumplir el criterio de determinismo de nivel master». La búsqueda de `SEED`, `20261127`, `semilla aleatoria`, `determinismo` y `determinist` en la caché del informe y en `INFORME_TECNICO.md` no devuelve esa semilla: las únicas «semillas» del texto son las ocho URLs de partida de marketplaces de §55 (L1337), ajenas a los generadores aleatorios. Hay un segundo problema técnico: los cinco pasos se lanzan con `subprocess.run([PY, ...])` (`run_all.py:29–35`), es decir, intérpretes nuevos que no heredan el estado de los generadores del proceso padre; la semilla del orquestador no alcanza a `01_ingest.py` … `05_benchmark.py`. En sentido favorable, esos cinco scripts no contienen llamadas a `random`, `np.random` ni muestreos con semilla (búsqueda negativa en `Data/analisis_rentabilidad/scripts/*.py`) y `run_all.py:2` declara las etapas «reanudable e idempotente», de modo que el resultado actual es determinista por agregación y OLS, no por la semilla. El criterio `V6.determinism.master` —«Seeds declared in code and in document, consistent»— queda incumplido por el lado del documento y por la afirmación del docstring.

— polarity: negative · confidence: high · related: [[#F-V6-005]], [[#F-V6-006]] · criteria: V6.determinism.master

### F-V6-004 — Comando único y puntos de entrada identificables; argumentos documentados de forma desigual

`README.md:19–23` documenta un solo comando de reproducción del análisis, y `run_all.py:25` fija la secuencia `["01_ingest.py", "02_clean.py", "03_eda.py", "04_stats.py", "05_benchmark.py"]`, seguida de `actualizar_numeros.py`, `generar_dashboard.py --solo-si-cambia` y `exportar_parquet_compacto.py` (`run_all.py:36–53`). E3 inventaria diez puntos de entrada con sus LOC en la tabla `### Entry points` (`…e3-artifacts.md:50–63`) y `Data/analisis_rentabilidad/README.md:21–37` mapea cada etapa a sus tablas y gráficos. Los argumentos constan para `db_chunks.py verify|assemble` (`README.md:77–80`) y para MkDocs (`README.md:86–89`); en cambio `run_all.py` carece de docstring de uso o de banderas propias, y el propio E3 marca «Args documented: no» para las diez entradas. El criterio `V6.entry_points.master` —«Entry points documented with arguments»— se cubre para las herramientas auxiliares y para la invocación sin argumentos del orquestador, que además satisface el umbral superior de un solo comando; la documentación de argumentos del componente central queda como punto débil menor.

— polarity: positive · confidence: high · related: [[#F-V6-001]], [[#F-V6-005]] · criteria: V6.entry_points.master

### F-V6-005 — Nueva prueba de humo del componente central, ejecutada con éxito y no inventariada por E3

`Auxiliares/herramientas/test_smoke_pipeline.py` (66 líneas) declara cuatro pruebas: `test_compila()` compila los siete scripts Python del pipeline, `test_artefactos()` existe siete salidas (`kpis.csv`, `modelo_muestra.csv`, `modelo_depreciacion.csv`, `Data/dashboard.html`, `MANIFEST.json` de Parquet, `Data/referencias.md`, `INFORME_TECNICO.md`), `test_csv_legibles()` lee cuatro CSV y `test_comando_unico()` verifica que el README cite `run_all.py` y que el código contenga `SEED = 20261127` (`test_smoke_pipeline.py:22–55`). Ejecutado en este checkout con `python3 Auxiliares/herramientas/test_smoke_pipeline.py`, terminó con «4 pruebas superadas». E3, cerrado a las 17:15, solo registra tres archivos de prueba y 259 LOC (`…e3-artifacts.md:65–70`), por lo que omite este cuarto archivo; en el momento de la revisión aparece como `??` en `git status`. El criterio `V6.tests.master` —«At least smoke tests of the central component»— queda cubierto por primera vez, si bien la prueba comprueba presencia y compilación, no la reproducción numérica de los KPIs ni la ejecución completa del pipeline.

— polarity: positive · confidence: high · related: [[#F-V6-003]], [[#F-V6-006]] · criteria: V6.tests.master

### F-V6-006 — Las mejoras de reproducibilidad viven en el árbol de trabajo, no en el commit declarado

`git status --short` muestra como modificados `requirements.txt`, `Data/analisis_rentabilidad/scripts/run_all.py`, `README.md`, `Auxiliares/herramientas/actualizar_numeros.py` y tres documentos derivados, y como no rastreado `Auxiliares/herramientas/test_smoke_pipeline.py`. El HEAD sigue siendo `99c7065` (27/11/2026, «viz: refrescar panel con el ultimo estado de circuitos»), que es también el commit citado por E3 en su sección Repository (`…e3-artifacts.md:23`). En consecuencia, un clon limpio de `main` no encuentra ni las cotas `~=`, ni la semilla, ni la prueba de humo. §69 (L1469) afirma que «las cifras, los modelos estadísticos y las decisiones de diseño provienen de los datos y del código versionados en este repositorio», y §55 (L1341) da por añadido `requirements.txt`; ambas afirmaciones describen un estado posterior al commit. El criterio `V6.documentation.master`, que presupone que dependencias, puntos de entrada y rutas constan en el repositorio, no se cumple para un tercero que reproduzca desde `main`.

— polarity: negative · confidence: high · related: [[#F-V6-002]], [[#F-V6-003]], [[#F-V6-005]] · criteria: V6.documentation.master

### F-V6-007 — KPIs del texto cacheado contra KPIs regenerados en README y `kpis.csv`

§59 (L1379) fija la corrida vigente en «772 autos únicos, 2.029 anuncios limpios (1.338 locales y 691 de importación) […] kilometraje mediano de 43.000 km» y añade que «los valores se actualizan solos en `outputs/tables/kpis.csv`». En el checkout, `Data/analisis_rentabilidad/outputs/tables/kpis.csv` registra `anuncios_totales=2156`, `anuncios_locales=1465`, `anuncios_importacion=691`, `km_medianos=33256`, y `README.md:3,10,33` repite 952 autos y 2.156 anuncios. §58 (L1371) conserva además el estado intermedio de 2.014 anuncios y 44.125 km. El marcador `<!-- kpi:autos_revolico -->` se actualizó en el README (de 947 a 952 según el diff), pero la caché de texto auditada no se regeneró: el lector no puede obtener del documento las cifras que el comando único produce. Afecta a [[#C003]] y al criterio `V6.documentation.master` en su faceta de correspondencia documento↔repositorio.

— polarity: negative · confidence: high · related: [[#C003]], [[#F-V6-001]] · criteria: V6.documentation.master

### F-V6-008 — Cifras del modelo hedónico desincronizadas entre §59 y `modelo_muestra.csv`

E3 registra como artifact ausente «Cifras de `modelo_muestra.csv` citadas en la narrativa técnica» (`…e3-artifacts.md:268–271`). §59 (L1381) reporta 28 observaciones de 981 candidatas con R² 0,277 y p del F 0,411. El archivo vigente contiene `principal,981,584,0.101,0.0` y `completo,981,28,0.2744,0.4114`: coinciden candidatas, observaciones y p, pero no el R² (0,2744 frente a 0,277, que no es su redondeo). En paralelo, `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md` y sus copias describen 572/22 observaciones de 897 candidatas, un estado que ya no existe en disco. [[#C005]] no puede verificarse byte a byte desde el artefacto citado sin elegir entre tres versiones del mismo resultado, y `test_smoke_pipeline.py:43–47` solo comprueba que el CSV sea legible, no que concuerde con la narrativa.

— polarity: negative · confidence: high · related: [[#C005]], [[#F-V6-005]], [[#F-V6-007]] · criteria: V6.documentation.master

### F-V6-009 — Panel interactivo vigente documentado fuera del informe

E3 incluye «Ruta del panel interactivo en el informe» entre los artifacts ausentes (`…e3-artifacts.md:273–276`). El checkout contiene `Data/dashboard.html` (109.929 B, regenerado en `99c7065`) y su copia en `docs/dashboard.html`, generadas por `Auxiliares/herramientas/generar_dashboard.py` y probadas en `test_dashboard.py`. El informe cita en cambio los dashboards antiguos de `Data/analisis/` (§22, §23) y en §59 se limita a «un apéndice visual con cinco cuadros y seis gráficos reales». La ruta actual del panel aparece en `Data/AUTOMATIZACION.md`, no en `INFORME_TECNICO.md`; un lector que siga solo el documento no encuentra el artefacto que `run_all.py:42–47` regenera. El criterio `V6.documentation.master` no satisface aquí el mapeo entre componente y ubicación en el repositorio.

— polarity: negative · confidence: high · related: [[#F-V6-001]], [[#F-V6-004]] · criteria: V6.documentation.master

### F-V6-010 — Cuatro referencias «verificadas» sin marca positiva en `Data/referencias.md`

§70 (L1477) declara verificadas externamente a Akerlof (1970), DfT/DVLA, ANFAC y AEADE y remite a `Data/referencias.md` para la convención de 38 entradas. E3 observa que el archivo solo porta la marca negativa `(metadata incomplete)` (`…e3-artifacts.md:278–281`). La lectura directa confirma que el encabezado (`Data/referencias.md:4–6`) define esa marca y que la entrada `[1] Akerlof` (`referencias.md:8`) aparece precisamente como `(metadata incomplete)`, en contradicción con la lista de §70. La distinción entre verificadas y no verificadas vive en `reviews/informe-tecnico-2026-11-27.e2-literature.md`, por lo que el estado afirmado en el documento no es autónomo dentro del artefacto citado; afecta a [[#C048]] y [[#C009]].

— polarity: negative · confidence: high · related: [[#C009]], [[#C048]] · criteria: V6.documentation.master

### F-V6-011 — Revolico no se versiona como archivo único, pero sí con manifiestos verificables

E3 mantiene el artifact ausente «Full Revolico SQLite file in the main branch» (`…e3-artifacts.md:283–286`). §14 declara que `Data/Revolico/revolico.sqlite` «no se versiona como archivo único» y §54 (L1325–1329) describe 82 fragmentos de 10 MB con SHA-256 del archivo completo, offsets y hashes por parte, publicados en la rama huérfana `chunked-db` mientras `main` conserva el objeto LFS grande. En disco los SQLite existen y `README.md:71–80` documenta `db_chunks.py verify <MANIFEST.json>` y `db_chunks.py assemble <MANIFEST.json> <destino>`; `01_ingest.py` reconstruye la base si falta. El criterio `V6.data_availability.master` —«datasets named + access path documented»— se cumple por la vía de los manifiestos, no mediante un archivo canónico rastreable en el historial; la observación es neutra porque la propia laguna está declarada.

— polarity: neutral · confidence: high · related: [[#C042]], [[#F-V6-004]] · criteria: V6.data_availability.master

### F-V6-012 — Series de parque automotor y matriculaciones siguen ausentes tras descargar los anuarios

E3 conserva «Official Cuban vehicle-fleet and registration series» como artifact no localizado (`…e3-artifacts.md:288–291`). §53 (L1317) presentaba el capítulo 13 del anuario 2025 como fuente que permitiría incorporar parque automotor y matriculaciones, pero §56 (L1351) corrige: «**No hay series de parque automotor ni de matriculaciones**». El checkout confirma que `Data/fuentes-oficiales/ONEI/series_oficiales.csv` solo cubre transporte de pasajeros y accidentes. La fuente está nombrada y su ruta documentada, pero la variable requerida por el marco de asequibilidad no existe entre los datos descargados; [[#C041]] no es reproducible desde el repositorio.

— polarity: negative · confidence: high · related: [[#C041]], [[#C096]] · criteria: V6.data_availability.master

### F-V6-013 — VAHAN y el endpoint vivo del BCC: fuentes nombradas sin ruta utilizable

E3 agrupa «VAHAN (India) y endpoint vivo del BCC» (`…e3-artifacts.md:293–296`). §18 (L819–820) registra «No accesible desde este entorno (error de transporte)» para VAHAN y «No accesible en vivo desde este entorno» para `https://api.bc.gob.cu/v1/tasas-de-cambio/activas`; el modelo usa en su lugar la TRMI fija de 930 CUP/USD de `Data/analisis_rentabilidad/config.py`, como aclara §52 (L1297) y [[#C010]]. La URL está declarada, pero no hay datos recuperados ni ruta de acceso operativa en este entorno, de modo que la comparación con matriculaciones por fabricante y la tasa oficial no pueden recalcularse.

— polarity: negative · confidence: high · related: [[#C010]], [[#C090]] · criteria: V6.data_availability.master

### F-V6-014 — Corpus de gacetas fuera del árbol del proyecto

E3 lista «Full gazette corpus» (`…e3-artifacts.md:298–301`). §10 (L120) sitúa el índice en `~/Utilidades/Leyes/gaceta_catalog.json` y §67 (L1451) confirma que leyes y herramientas se mudaron fuera del repositorio durante la optimización de espacio. Solo se nombran en el texto Decreto 163/2026 y las resoluciones 104, 17, 52, 171–175, 340 y 102/2026 ([[#C020]], [[#C021]]); ni el índice ni los PDFs son inventariables dentro del checkout, por lo que las afirmaciones normativas no pueden cotejarse con los documentos fuente que las sustentan.

— polarity: negative · confidence: high · related: [[#C020]], [[#C021]], [[#C073]] · criteria: V6.data_availability.master

### F-V6-015 — Docker: FlareSolverr operativo pero daemon inaccesible para `google-maps-scraper`

E3 recoge «Docker daemon for the Google Maps scraper» (`…e3-artifacts.md:303–306`). §36 (L1084) explica que el daemon «no arranca sin root en este entorno» y que esa vía se descartó, mientras §6 (L72) declara FlareSolverr 3.5.2 funcionando en `http://127.0.0.1:8191/`. El entorno reproducible presentado contiene por tanto un servicio contenedorizado operativo y un daemon inaccesible para otra herramienta; la ruta descartada no forma parte de los componentes centrales, pero la convivencia de ambas declaraciones excluye una descripción uniforme del entorno en `V6.environment.master`.

— polarity: negative · confidence: high · related: [[#C065]] · criteria: V6.environment.master

### F-V6-016 — Especificaciones estructuradas y precios de transacción: cobertura parcial y umbral distinto

E3 consigna «Especificaciones estructuradas y precios de transacción reales» (`…e3-artifacts.md:308–311`). §24 (L911) declara que no hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión y que los campos se derivan con regex; §22 (L894) cuantifica la cobertura en marca 68,4 %, año 63,5 % y km 6,2 %, y fija el precio válido en ≥500 USD, mientras `Data/analisis_rentabilidad/config.py:31` usa `PRICE_MIN_USD = 200`. A ello se añade la ausencia de precios transados declarada en §20 ([[#C096]], [[#C105]]). La combinación de campos derivados, cobertura incompleta y umbral distinto condiciona la réplica de las estimaciones hedónicas desde los datos publicados.

— polarity: negative · confidence: high · related: [[#C096]], [[#C105]] · criteria: V6.data_availability.master

### F-V6-017 — `Copias/` excluidas del informe pero citadas como insumo metodológico

E3 mantiene «`Copias/` reference repositories» (`…e3-artifacts.md:313–316`). §3 (L54) declara que `Copias/` no se registra «por decisión explícita», mientras la tabla metodológica de §17 cita código de `Copias/AutosxCuba/code/…` y §50 (L1267) describe la tabla `provenancia` construida a partir de repositorios externos. Los cuatro repositorios existen en disco y `README.md:48–52` confirma que quedan fuera de Git, así que la procedencia de esas funciones y tablas queda documentada por mención, sin que los archivos citados formen parte del inventario versionado.

— polarity: neutral · confidence: high · related: [[#C046]], [[#C059]] · criteria: V6.data_availability.master

### F-V6-018 — Fuentes con ruta, URL, checksum y licencia declarados

Varias entradas del inventario superan el umbral `master`. Los 12 anuarios del ONEI están en `Data/fuentes-oficiales/ONEI/` con URL, tamaño y SHA-256 por archivo en el `INDICE.md` de cada año (§53, L1313–1315; `README.md:12,44`); la serie DfT/DVLA se cita en §18 (L818) con URL de GOV.UK, fecha de actualización 23/09/2026 y licencia Open Government Licence ([[#C088]]); las 137 gasolineras de `Data/mapas/gasolineras.csv` se apoyan en Overpass/OSM; los manifiestos de `revolico.sqlite` y `pipeline.sqlite` publican `source_sha256`, offsets y generador. El criterio `V6.data_availability.master` se satisface para este conjunto, con las excepciones de [[#F-V6-012]], [[#F-V6-013]] y [[#F-V6-014]].

— polarity: positive · confidence: high · related: [[#C040]], [[#C088]], [[#F-V6-011]] · criteria: V6.data_availability.master


## §7 — v7-writing


# V7 — Writing and AI patterns (findings)

Resumen (tres líneas):
- La iteración 2 añade 520 palabras y 22 líneas sobre la iteración 1 (28.586 → 29.106 palabras); los patrones estructurales (paralelismo ES/EN, apertura «Se + verbo», bloques «EN.», registro generado del §13) permanecen sin cambio y la densidad global se mantiene baja.
- Las únicas subidas medibles son metaconceptos (197 → 205; 6,89 → 7,04 por 1.000 palabras) y adjetivos valorativos sin ancla (4 → 7; 0,14 → 0,24 por 1.000 palabras), todas ellas introducidas por la nueva §69; hedging (1), openers de fórmula (0), «not just X, but Y» (0) y triadas largas (2–3) no varían.
- La §69 nombra fases como actividades genéricas y enuncia un principio de contraste contra archivos, pero no nombra herramientas generativas (solo el genérico y la skill `review`), no enumera fases por identificador ni las del criterio V9, y no designa un protocolo de supervisión con nombre; densidad de §69 = media, sin disparar el hook de densidad alta.

Alcance y método. Conteo directo sobre los textos cacheados de la iteración 1 (`informe-tecnico-2026-11-27.text.md`, 1.462 líneas) y de la iteración 2 (`informe-tecnico-2026-11-27-iter2.text.md`, 1.484 líneas); «palabra» incluye identificadores, rutas y tablas. El §13 (registro automático) queda fuera del denominador de densidades de prosa, como en el informe V7 de la iteración 1. El diff entre ambas versiones consta de siete pasajes editados, las secciones nuevas §69–§70 y el cambio de fecha de cierre; por eso la comparación se formula como «sin cambio» salvo donde se documenta lo contrario. Winston, Pinker y Romero §13 se citan como rótulos de las róbricas aplicadas; el artefacto describe patrones y densidades, sin emitir juicio de autoría.

### F-V7-001 — Diff acotado: los patrones estructurales de la iteración 1 pasan intactos a la iteración 2

La comparación línea por línea muestra siete reescrituras puntuales —nota de actualización en §2 (L38–L39) y su paralelo inglés (L169–L170), conclusión 5 (L139), aclaración de TRMI (L902), revisión de la depreciación (L1206), conversión (L1297) y cifras del relato (L1379–L1381)— más la inserción de §69–§70 (L1465–L1482) y el cambio de «Última actualización» a 27/11/2026 (L1484). No se modifica ninguno de los rasgos que el V7 de la iteración 1 inventarió como dominantes: el paralelismo ES/EN de §1–12 y de 54 de 55 secciones fechadas, la apertura «Se + verbo», los bloques «**EN.**» de participio inicial ni las 473 líneas de tabla generada del §13. Bajo Winston (structure-of-prose), la estructura de la prosa es la misma; el cambio es de contenido y de una sección nueva, no de ritmo ni de organización.

— polarity: neutral · confidence: high · related: [[#F-V7-005]], [[#F-V7-008]]

### F-V7-002 — §69: herramientas genéricas, fases declaradas como actividades, supervisión enunciada como principio

La sección nueva «Declaración de uso de inteligencia artificial / AI-use declaration» (§69, L1467–L1471) dice en ES: «Las herramientas de inteligencia artificial se utilizaron como apoyo para la redacción, la edición quirúrgica de la narrativa, la revisión bibliográfica asistida y la auditoría sistemática del propio informe» (L1469); el bloque EN reproduce las mismas cuatro actividades (L1471). **Herramientas:** el único nombre propio es `review` —«la skill `review` de MatCom» (L1469)—, que designa el procedimiento de auditoría, no una herramienta generativa; no aparecen nombres de modelos ni de asistentes en L1467–L1471. **Fases:** sí se nombran cuatro actividades (redacción, edición, revisión bibliográfica, auditoría), pero como sustantivos comunes y en prosa corrida: no hay identificadores de fase, ni enumeración, ni las fases que el criterio `V9.ai_use_declaration.master` pide (research, drafting, code generation, translation); el único guiño cuantitativo es «los trece artefactos de fase» (L1469), un conteo sin lista. **Protocolo de supervisión:** aparece como principio —«ninguna afirmación empírica se originó en una salida de IA sin contraste contra los archivos» (L1469) / «no empirical claim was taken from an AI output without verification against the files» (L1471)—, acompañado de procedencia («provienen de los datos y del código versionados en este repositorio») y de huella de auditoría (`reviews/informe-tecnico-2026-11-27.{md,forensic.md}`). No se designa un protocolo con nombre ni se especifican sus pasos. Descriptivamente: fases y supervisión están presentes en forma genérica; herramientas, solo de modo implícito.

— polarity: neutral · confidence: high · related: [[#F-V9-001]], [[#F-V9-002]], [[#F-V9-003]]

### F-V7-003 — Romero §13 Don't 3 en §69: dos enumeraciones con cola creciente

La primera oración de §69 encadena cuatro miembros de longitud creciente: «la redacción, la edición quirúrgica de la narrativa, la revisión bibliográfica asistida y la auditoría sistemática del propio informe» (L1469); el cuarto es el más largo y el más abstracto. La segunda oración abre con otra serie de tres —«Las cifras, los modelos estadísticos y las decisiones de diseño» (L1469)— cuyo tercer término es el de mayor abstracción, y el bloque EN duplica ambas series (L1471). Fuera de §69 el recuento se mantiene en las 2–3 instancias ya registradas en la iteración 1 (L117, L145, L763 en aquella numeración; L118, L147 y L765 en esta). En un bloque de 520 palabras, dos tetradas/triadas de cola larga equivalen a una densidad media del patrón, concentrada íntegramente en la declaración nueva.

— polarity: neutral · confidence: high · related: [[#F-V7-004]]

### F-V7-004 — Romero §13 Don't 5: los tres adjetivos sin ancla nuevos están todos en §69

El recuento global de equivalentes de «significant/important/considerable/notable/substantial» y modificadores afines pasa de 4 (iteración 1) a 7 (iteración 2). Los tres nuevos son «edición **quirúrgica** de la narrativa», «revisión bibliográfica **asistida**» y «auditoría **sistemática** del propio informe» (L1469), repetidos en la versión EN (L1471); ninguno lleva ancla numérica. Los cuatro preexistentes sí la llevan o van seguidos de dato concreto: «pendiente anual significativa» aparece con p mínimo 0,165 (L1389), «correcciones quirúrgicas» con una lista de cuatro cambios (L1415), «significativa» con p < 0,001 (L1206) y «quizá innecesarias» con 66 MB (L1459). La subida de densidad (0,14 → 0,24 por 1.000 palabras) es, por tanto, un efecto local de §69 y no un cambio de hábito en el resto del informe.

— polarity: neutral · confidence: high · related: [[#F-V7-003]], [[#F-V7-005]]

### F-V7-005 — Metaconceptos: 197 → 205, con el incremento localizado en §69–§70

Bajo Pinker (metaconcepts and zombie nouns), la suma de `análisis`, `proceso`, `evaluación`, `consideración`, `implementación`, `auditoría`, `herramientas`, `decisiones`, `resultados` y afines pasa de 197 a 205 ocurrencias (6,89 → 7,04 por 1.000 palabras; +0,15). El incremento se reparte entre §69 —«herramientas», «apoyo», «edición», «revisión», «auditoría», «cifras», «modelos», «decisiones», «afirmación», «salida», «resultados», «artefactos» (L1469, L1471)— y §70 —«referencias», «verificación», «fuentes», «auditoría» (L1477, L1479)—. Las dos zonas que el V7 anterior calificó como densidad alta, §17–21 (≈13,8 metaconceptos/1.000 palabras) y §59–63, no cambian. La lectura descriptiva es de estabilidad global con un repunte local en las secciones declarativas nuevas.

— polarity: neutral · confidence: high · related: [[#F-V7-001]], [[#F-V7-004]]

### F-V7-006 — Las reescrituras de la iteración 2 añaden anclaje concreto, no atenuadores

Las siete pasajes editados fuera de §69–§70 refuerzan el síntoma inverso al de Pinker (lack of concrete examples): «el pipeline de `Data/analisis_rentabilidad/` usa la TRMI fija de 930 CUP/USD del 18/11/2026 (`config.py`)» (L902); «la depreciación de −5,43 % anual obtenida en la primera corrida (p < 0,001; §34), cifra que la corrida vigente ya no sostiene» (L1206); «28 observaciones completas» de «981 candidatas (R² = 0,277; p del F = 0,411)» (L1381); «772 autos únicos», «2.029 anuncios limpios» y «corrida vigente del 27/11/2026» (L1379); «están implementados en `Data/analisis_rentabilidad/` y se regeneran de forma automática» (L139). La expresión «ya no sostiene» funciona como corrección con fecha y cifra, no como hedging-as-tic; el único atenuador del documento sigue siendo «bibliotecas quizá innecesarias» (L1459). Densidad de hedging en la iteración 2: 1 instancia, 0,03 por 1.000 palabras, idéntica a la iteración 1.

— polarity: positive · confidence: high · related: [[#F-V7-010]], [[#F-V7-005]]

### F-V7-007 — §70: título instructivo, lista enumerativa y procedencia verificable

La sección «Referencias verificadas / Verified references» (L1475–L1481) abre con la serie «Akerlof (1970), *The Market for "Lemons"* (Crossref/OpenAlex); UK Department for Transport / DVLA … (GOV.UK); ANFAC … (sitio oficial); AEADE … (sitio oficial)» (L1477) y cierra con `(metadata incomplete)` para el resto y `Data/referencias.md` como convención numerada de 38 referencias. Bajo Winston, el título es instructivo y la lista cumple una función enumerativa (no sustituye un argumento); bajo Pinker, cada fuente lleva ancla externa concreta. No hay metadiscurso («this section discusses»), professional narcissism («research in recent years»), openers de fórmula ni shudder quotes fuera del título citado de Akerlof, que es un título real. Densidad: baja.

— polarity: neutral · confidence: high · related: [[#F-V7-011]], [[#F-V7-012]]

### F-V7-008 — Romero §13 Don't 2, Don't 4, Don't 8 y Pinker (metadiscurso): continuidad sin cambios

«No solo… sino» y «not just… but» registran 0 instancias en ambas iteraciones; las negaciones de salvaguarda («no se eluden mecanismos anti-automatización», L118; «no se falsificó su contenido», L129; «no se borraron», L1451) siguen funcionando como constancia de límites, no como énfasis retórico. La forma estricta de Don't 4 (landscapes/paradigms/ecosystems/transformations) mantiene 3 coincidencias, todas concretas —«cada transformación y cada estimación del pipeline» (L1389) se refiere a transformación de datos—. Don't 8 conserva las mismas reescrituras descritas de §43–47 y §59–63 (L1381, L1415), sin nuevas apariciones. El metadiscurso y el professional narcissism permanecen en 0; la señalización interna sigue haciéndose con etiquetas en negrita y remisiones a rutas. La uniformidad de longitud tampoco cambia: §69 alterna tres oraciones largas (≈30–39 palabras) con los párrafos cortos de §70, sin cadenas de cuatro o más frases de 18–25 palabras.

— polarity: neutral · confidence: high · related: [[#F-V7-001]], [[#F-V7-003]]

### F-V7-009 — Romero §13 Don't 8 en §69: la declaración describe la auditoría, no la muestra

§69 enuncia el resultado de la auditoría —«La auditoría completa de este documento se realizó con la skill `review` de MatCom y sus resultados se conservan en …» (L1469)— y su paralelo EN (L1471) sin incluir ningún hallazgo, densidad ni fragmento del resultado; la conclusión se da antes que la evidencia. Es el mismo mecanismo que el V7 de la iteración 1 registró en §43–47 y §59 (reescrituras descritas, no mostradas), ahora aplicado a la propia declaración de uso de IA. Se consigna como patrón de cierre, no como déficit de evidencia: las cifras de la declaración («trece artefactos de fase») son verificables en el directorio `reviews/`.

— polarity: neutral · confidence: medium · related: [[#F-V7-002]], [[#F-V7-007]]

### F-V7-010 — Pinker: anclaje concreto sostenido en las secciones editadas y en las nuevas

El síntoma «definiciones sin instancias» no aparece en los pasajes nuevos: §69 ancla la procedencia a «los datos y del código versionados en este repositorio» y a la ruta `reviews/informe-tecnico-2026-11-27.{md,forensic.md}`; §70 ancla cada referencia a Crossref/OpenAlex, GOV.UK, ANFAC o AEADE; §59–60 ancla cada cifra a `outputs/tables/kpis.csv` o a `config.py`. Esta densidad de anclajes es la contrapartida de los metaconceptos de F-V7-005 y explica que, pese al repunte local, el patrón global siga siendo de baja densidad de tics.

— polarity: positive · confidence: high · related: [[#F-V7-006]], [[#F-V7-005]]

## AI-pattern density by section

Valores aproximados sobre los textos cacheados; «metaconcepto/1k» agrega las palabras de la róbrica Pinker indicadas en F-V7-005, «openers» cuenta «Se + verbo», participio de los bloques «EN.» y pasiva inglesa, y no incluye «In recent years…» ni «This study demonstrates that…» (0 instancias). La columna «Densidad» compara iteración 1 → iteración 2.

| Section | Density (iter1 → iter2) | Notes |
|---|---|---|
| §1–3 — Objetivo, estados, carpetas (L14–53) | low → low | Sin cambio; 0 triadas; openers «Se + verbo» |
| §4–9 — Fases 1–6 (L54–108) | low → low | Sin cambio; tablas y listas; 0 atenuadores |
| §10–12 — Marco legal, problemas, conclusiones (L110–139) | medium → medium | Conclusión 5 reescrita con ruta y «se regeneran de forma automática» (L139); «marco» 3; triada en L118 |
| Parte II §1–12 — Objective…Conclusions (L145–270) | low → low | Sin cambio salvo la nota de actualización (L169–L170); 0 hedges; 0 triadas nuevas |
| §13 — Registro de altas (L274–748) | n/a → n/a | Tabla generada por script; excluida del denominador |
| §14–33 — Sincronización, eficiencia, colas, marcos (L750–1008) | medium → medium | Sin cambio; 19 openers «Se…»; 18 bloques EN |
| §17–21 — Guía, auditoría y marcos analíticos (L787–884) | high → high | Sin cambio; 14 «análisis» + 9 «marco» en 1.671 palabras (≈13,8/1k); escaleras de 8 y 9 pasos |
| §34–48 — Rentabilidad, APK, mapas, storytelling (L1012–1242) | medium → medium | §37 añade ancla TRMI 930 y `config.py` (L902); 0 hedges |
| §49–58 — Repos, mejoras, fuentes, ONEI, chunks (L1245–1369) | medium → medium | Sin cambio; ≈25 «no/sin»; d5 con ancla en L1291 |
| §59–63 — Storytelling final, modelos, sitio, retención (L1373–1415) | high → high | Sin cambio en d8/d5; se añaden 28/981, R² 0,277, p 0,411 (L1381) y cifras vigentes (L1379); anclaje, no hedging |
| §64–68 — Automatización y espacio (L1419–1461) | low–medium → low–medium | Sin cambio; «quizá» en L1459 (único hedge del corpus); «no se borraron», L1451 |
| §69 — Declaración de uso de IA (L1467–L1473) | n/a → **medium** | Nueva: d3 ×2, d5 ×3, ≈12 metaconceptos en ~200 palabras; 0 hedges, 0 openers de fórmula, 0 «not just…but» |
| §70 — Referencias verificadas (L1475–L1481) | n/a → low | Nueva: lista enumerativa con procedencia externa concreta; 0 tics estrictos de Romero §13 |

Totales comparados (texto completo, incluidas tablas): palabras 28.586 → 29.106; hedging 1 → 1 (0,03/1k en ambos); metaconceptos 197 → 205 (6,89 → 7,04/1k); adjetivos valorativos sin ancla 4 → 7 (0,14 → 0,24/1k); openers de fórmula 0 → 0; «not just X, but Y» 0 → 0; Don't 4 estricto 3 → 3.

## Hook para V9

La tabla de densidad que V9 (§15 de su informe, «No se recibió tabla de densidad de V7») declaró no haber recibido queda aquí consignada: ninguna sección nueva alcanza `ai-pattern-density: high`; §69 es `medium` y §70 es `low`. Los dos bloques que sí permanecen en `high` —§17–21 y §59–63— son idénticos a los de la iteración 1 y su anclaje numérico es incompatible con un tic de atenuación: la declaración de «contraste contra los archivos» (L1469) se corresponde con esas cifras y rutas. Para el contraste con `V9.ai_use_declaration.master`, la densidad media de §69 se debe a dispositivos de superficie (triadas de cola larga, tres adjetivos sin ancla y metaconceptos), no a hedging ni a openers de fórmula; las tres lagunas de nombrado —herramientas genéricas, fases no enumeradas y protocolo sin nombre— se detallan en F-V7-002. Se señala además que la huella de auditoría citada en §69 apunta a `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` (iteración 1), no a los artefactos `-iter2`; dato descriptivo para el alcance de la declaración.


## §8 — v8-bibliography


## Resumen

- La enumeración `[1]`–`[38]` en `Data/referencias.md` es nueva en esta iteración; los seis marcadores `(metadata incomplete)` concentran todo el flag del aparato y las 32 fichas restantes no se re-verificaron en esta pasada dirigida.
- Los tres conteos recuperados por E2 se confirman en OpenAlex —`[18]` 13, `[19]` 96, `[20]` 9 citas— junto con los DOI de las versiones publicadas de `[18]` y `[19]`, que las fichas no incorporan.
- La contradicción Akerlof entre §70 («verificada externamente (Crossref/OpenAlex)») y `[1]` (`(metadata incomplete)`) subsiste porque la ficha no nombra el campo incompleto: OpenAlex confirma la identidad, el resumen es solo un índice de secciones y Crossref no respondió en esta pasada.

## Alcance y método

Se tomó como bibliografía del documento la lista numerada de 38 entradas de `Data/referencias.md`, anexo enlazado desde la nueva §70 (L1475–1479), y no las 36 menciones nominales dispersas que se auditaron en la iteración 1. La re-verificación se ejecutó el 2026-11-27 contra OpenAlex API (6 registros por ID) y Crossref API (1 registro), con foco en los seis marcadores heredados o nuevos y en las cuatro fuentes institucionales que §70 declara verificadas; E2 de iter2 aporta las verificaciones de páginas institucionales y el historial de la pasada 1. En el frontmatter, `verified: 6` cuenta las fichas re-verificadas en vivo aquí y `unverified: 32` las que quedan fuera de esta pasada dirigida: no es un juicio sobre su existencia ni una declaración de obra fantasma.

Los fetch a `https://api.openalex.org/works/W4406461714`, `W2770052903`, `W3120241027`, `W2156109180`, `W7134932779` y `W1991842457` devolvieron registro completo. El fetch a `https://api.crossref.org/works/10.2307/1879431` devolvió `{"error":{"type":"unknown","message":"Transport error (GET https://api.crossref.org/works/10.2307/1879431)"}}`, reproduciendo el HTTP 429 que E2 consignó para Akerlof. Ningún campo ausente se completó por inferencia.

### F-V8-001 — Seis marcadores genéricos cubren cinco causas de campo distinto

`Data/referencias.md` emplea la misma etiqueta `(metadata incomplete)` en `[1]`, `[10]`, `[18]`, `[19]`, `[20]` y `[38]` sin indicar qué campo falta. La re-verificación muestra que el motivo no es homogéneo y que en tres casos el marker ya no corresponde a ningún campo:

| Entrada | Campo realmente afectado | Hallazgo de esta pasada |
|---|---|---|
| `[1]` Akerlof | resumen: `abstract_inverted_index` solo con índice de secciones; Crossref sin contraste | identidad completa en OpenAlex (DOI `10.2307/1879431`, W2156109180) |
| `[10]` Kang & Fu | resumen: `abstract_inverted_index: null` | título, autores, afiliación, vol. 216/art. 111964 y 3 citas confirmados |
| `[18]` ProbSAINT | ninguno: el motivo (citas no verificables por HTTP 403) quedó resuelto | 13 citas y DOI publicado `10.1109/bigdata62323.2024.10825740` |
| `[19]` Pal et al. | ninguno: motivo resuelto; falta consignar año y DOI de la versión publicada | 96 citas, `2018`, DOI `10.1007/978-3-030-03402-3_28` |
| `[20]` Arefin | ninguno: motivo resuelto | 9 citas, DOI `10.48550/arxiv.2101.03788` |
| `[38]` Quariguasi | resumen no indexado con texto completo accesible; año 2015 vs 2016 | 136 citas, vol. 171(3), 371–380 |

E2 de iter2 lo declaró en H1: el marker «debería ser por campo —por ejemplo `(metadata incomplete: resumen no indexado)`— y no una etiqueta genérica». En la ficha vigente, un lector no puede distinguir entre «resumen ausente», «conteo resuelto pero no transcrito» y «flag nuevo sin justificación», de modo que el estado de verificación no es operable entrada por entrada.

— polarity: negative · confidence: high · related: [[#C009]], [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#P005]], [[#P006]], [[#F-V8-002]], [[#F-V8-003]], [[#F-V8-004]], [[#F-V8-005]], [[#F-V8-006]]

### F-V8-002 — Los conteos recuperados 13 / 96 / 9 se confirman en OpenAlex

Las tres cifras que E2 recuperó por vía alternativa al HTTP 403 de Semantic Scholar se reproducen en los registros consultados aquí. Para `[18]`, `https://api.openalex.org/works/W4406461714` devuelve `"cited_by_count":13` con `counts_by_year` 2025: 7 y 2026: 6, `updated_date: 2026-11-25T09:40:18.809321`; la obra es `ProbSAINT: Probabilistic Tabular Regression for Used Car Pricing`, con `publication_date: 2024-12-15`, DOI `10.1109/bigdata62323.2024.10825740` y `arxiv: https://arxiv.org/abs/2403.03812`. Para `[19]`, `W2770052903` devuelve `"cited_by_count":96`, DOI `10.1007/978-3-030-03402-3_28`, `publication_year: 2018` y `publication_date: 2018-12-06`, con los cinco autores coincidentes. Para `[20]`, `W3120241027` devuelve `"cited_by_count":9`, DOI `10.48550/arxiv.2101.03788` y `publication_date: 2021-01-11`. Las tres cifras quedan por tanto verificadas en vivo y no dependen de la afirmación de E2.

Estos son los únicos conteos que la lista numerada expone de forma indirecta: ninguna de las tres fichas los incluye, porque el campo de citas no forma parte del formato de `Data/referencias.md`. La verificación es válida para los identificadores citados, no para un conteo declarado por el documento.

— polarity: positive · confidence: high · related: [[#P003]], [[#P004]], [[#P005]], [[#F-V8-003]]

### F-V8-003 — Los flags de `[18]`, `[19]` y `[20]` permanecen tras resolverse su único motivo

Las fichas conservan `(metadata incomplete)` y solo la URL de arXiv para `[18]` («arXiv:2403.03812; IEEE BigData 2024, Industry & Government Track (2024). https://arxiv.org/abs/2403.03812 ... **(metadata incomplete)**»), `[19]` y `[20]`, aunque el único dato que E2 declaró no verificable —el conteo de citas, bloqueado por HTTP 403 de Semantic Scholar— quedó cubierto por OpenAlex (13, 96 y 9; F-V8-002). En `[18]` falta además el DOI de la versión publicada; en `[19]` faltan el DOI `10.1007/978-3-030-03402-3_28` y el año 2018 de la publicación frente al 2017 del preprint declarado, una discrepancia de año que la ficha no consigna; en `[20]` falta el conteo. E2 denominó este estado «resuelto en vivo pero no reflejado» y la comparación de la lista con los registros confirma que el marcador no se actualizó entre el 27/11 y la generación de esta pasada.

— polarity: negative · confidence: high · related: [[#C009]], [[#P003]], [[#P004]], [[#P005]], [[#F-V8-001]], [[#F-V8-002]]

### F-V8-004 — Akerlof: §70 y `[1]` sostienen estados incompatibles sin campo identificado

La §70 (L1477) escribe: «Referencias citadas y verificadas externamente durante la auditoría: Akerlof (1970), *The Market for "Lemons"* (Crossref/OpenAlex) ...», y su versión inglesa (L1479) repite «Externally verified references cited during the audit: Akerlof (1970) ... (Crossref/OpenAlex)». En la misma fecha, `Data/referencias.md` `[1]` cierra con «https://doi.org/10.2307/1879431. Citada en el informe: yes. **(metadata incomplete)**», y añade que «Los metadatos se verificaron en vivo con OpenAlex/Crossref». El claim C009 de E1 reformula: «Solo cuatro referencias están verificadas externamente; las restantes figuran como `(metadata incomplete)`».

La consulta a `https://api.openalex.org/works/W2156109180` confirma todos los campos bibliográficos: DOI `10.2307/1879431`, autor `George A. Akerlof` con ORCID, revista `The Quarterly Journal of Economics`, volumen 84, número 3, `publication_date: 1970-08-01`, páginas 488–500 en el registro RePEc y `"cited_by_count":32658`. El campo `abstract_inverted_index` contiene únicamente «I. Introduction, 488. — II. The model with automobiles as an example, 489. — III. Examples and applications, 492. — IV. Counteracting institutions, 499. — V. Conclusion, 500.», que es el motivo original del flag y sigue sin cambiar. La parte Crossref de la afirmación no pudo contrastarse aquí: la API devolvió error de transporte, igual que el HTTP 429 registrado por E2. Las dos afirmaciones solo se reconcilian si se entiende que el flag alude al resumen y no a la identidad de la obra; la ficha no lo dice, y por eso la contradicción entre «verificada» e «incompleta» queda abierta en el único trabajo que sostiene el marco teórico de asimetría de información (§17, §19, §20).

— polarity: negative · confidence: high · related: [[#C009]], [[#P001]], [[#F-V8-001]], [[#F-V8-002]]

### F-V8-005 — `[10]`: el flag por resumen no indexado se confirma campo por campo

La ficha `[10]` termina en `(metadata incomplete)` y el registro `https://api.openalex.org/works/W7134932779` devuelve `"abstract_inverted_index": null`, de modo que el motivo subsiste exactamente donde E2 lo localizó. El resto de campos sí se confirma en la misma respuesta: título *The pricing of used electric vehicles via machine learning and hedonic price model: A comparative study*, autores Wentao Kang y Xiao Fu con ORCID, afiliación Hangzhou Dianzi University, `Computers & Industrial Engineering` volumen 216, artículo 111964, `publication_date: 2026-03-11` y `"cited_by_count":3` (frente a 2 en la pasada 1). La ficha declara 2026 y el DOI `10.1016/j.cie.2026.111964`; no hay DOI espurio ni ID imposible. Es el segundo caso, con `[1]`, en que el marcador corresponde a un campo real y no a un dato ya recuperado.

— polarity: neutral · confidence: high · related: [[#P002]], [[#P006]], [[#F-V8-001]]

### F-V8-006 — `[38]`: flag nuevo sin justificación y discrepancia de año no consignada

La ficha `[38]` incorpora `(metadata incomplete)` en esta iteración, mientras E2 consigna que en la pasada 1 la misma obra figuraba verificada con 136 citas y sin marker; el propio E2 lo califica como «introducido en la iteración 2 sin justificación explícita». El registro `https://api.openalex.org/works/W1991842457` confirma título, tres autores, `International Journal of Production Economics` vol. 171 parte 3, pp. 371–380, DOI `10.1016/j.ijpe.2015.02.006` y `"cited_by_count":136`. El campo `abstract_inverted_index` es `null`, pero `best_oa_location` apunta al texto completo de la Universidad de Manchester; el `raw_source_name` de esa ubicación registra «Quariguasi Frota Neto, J, Bloemhof, J & Corbett, C 2016», frente al `publication_year: 2015` de OpenAlex y al 2015 de la ficha. La lista no consigna esa discrepancia ni explica el cambio de estado, de modo que `[38]` es la única entrada cuyo flag aparece sin un motivo declarado en ninguno de los dos artefactos.

— polarity: negative · confidence: high · related: [[#P006]], [[#F-V8-001]]

### F-V8-007 — Las cuatro fuentes institucionales de §70 operan fuera de la numeración y DVLA carece de URL profunda

§70 declara como verificadas cuatro fuentes: Akerlof (1970), DfT/DVLA, ANFAC y AEADE. Solo la primera tiene ficha numerada (`[1]`); las tres institucionales aparecen como mención nominal sin número, de modo que el cómputo de 38 entradas de `Data/referencias.md` no las incluye y el claim C009 («Solo cuatro referencias están verificadas externamente») mezcla dos regímenes de cita. E2 iter2 verificó las páginas oficiales de ANFAC (P007), AEADE (P008) y DVLA/GOV.UK (P009) a nivel de organismo: ANFAC expone matriculaciones y cifras 2025, AEADE publica anuarios y boletines de ventas Ene–sep 2026, y GOV.UK confirma la serie «Vehicle licensing statistics data files»; en esta pasada no se re-fetcharon esas tres páginas. El punto no verificado según P009 es la URL profunda de la colección de estadísticas de vehículos: tres intentos directos devolvieron HTTP 404 y el `WebSearch` de apoyo falló a nivel de proveedor, por lo que la afirmación queda contrastada a nivel de organismo, no de enlace concreto. La precisión de atribución de AEADE es además ecuatoriana, no española; §70 no asigna país pero la vecindad de ANFAC en la misma frase puede inducir otra lectura.

— polarity: neutral · confidence: medium · related: [[#C009]], [[#P007]], [[#P008]], [[#P009]], [[#F-V8-004]]

### F-V8-008 — Convención de entrada uniforme en las 38 fichas, sin duplicados ni identificadores espurios

Las 38 entradas siguen una sola plantilla —autores, título en cursiva, venue, año, URL o DOI, «Citada en el informe: sí/no»— y todas incluyen autores nominales. No aparece la misma obra dos veces con identidades distintas: los DOI no se repiten y las tres versiones preprint/publicadas de `[18]`, `[19]` y `[20]` están representadas por una sola ficha cada una. Los DOI declarados se ajustan al patrón `10\.\d{4,9}/.*`; los cuatro identificadores de arXiv (`2403.03812`, `1711.06970`, `2101.03788`, `2601.14311`) tienen prefijo de fecha compatible con un documento de noviembre de 2026 y ninguno resuelve a otra obra en los registros consultados. Dos artefactos tipográficos son sistemáticos y no afectan a la atribución: el doble punto tras las iniciales del último autor en las 38 fichas («Akerlof, G. A..», «Krotov, V.; Johnson, L.; Silva, L..») y los paréntesis anidados en el venue de `[2]` («American Economic Review (2011 (el registro OpenAlex indexa la versión SSRN de 2010; la publicación AER es de 2011))»).

— polarity: positive · confidence: high · related: [[#F-V8-001]]

## Nota de cierre

La iteración 2 cambió el objeto auditable: de 36 menciones nominales sin convención a 38 fichas numeradas con DOI y estado declarado. Los conteos 13, 96 y 9 y los DOI publicados de `[18]` y `[19]` son verificables y no figuran en esas fichas; los flags de `[1]` y `[10]` corresponden a resúmenes no sustantivos o no indexados; el de `[38]` aparece sin motivo declarado. La contradicción entre §70 y `[1]` no es de existencia de la obra sino de etiqueta de estado: la ficha no nombra el campo incompleto y la sección no distingue verificación de identidad de verificación de resumen. Todo dato ausente se registró como no verificado; no se asignó ningún DOI, conteo ni año que no conste en la respuesta de la API consultada.


## §9 — v9-ethics


## Resumen

- §69 incorpora una declaración explícita de uso de IA (L1467–L1471) que nombra fases y un protocolo de contraste contra archivos versionados; cierra la ausencia registrada en el F-V9-001 de la iteración 1.
- Las herramientas no se identifican por nombre (solo «herramientas de inteligencia artificial» y la skill `review` de MatCom), y faltan las fases de generación de código y traducción pese al carácter bilingüe del documento y a los scripts creados.
- No se recibió tabla de densidad de V7 ni clon verificado de E3 para esta pasada; el contraste se limita a `V9.ai_use_declaration.master` con `level=master`.

### F-V9-001 — Declaración de uso de IA presente en §69, con fases y protocolo de verificación

§69 (L1467) lleva por título «Declaración de uso de inteligencia artificial / AI-use declaration». El pasaje ES (L1469) declara: «Las herramientas de inteligencia artificial se utilizaron como apoyo para la redacción, la edición quirúrgica de la narrativa, la revisión bibliográfica asistida y la auditoría sistemática del propio informe». La versión EN (L1471) reproduce las mismas fases: «AI tools were used to support writing, surgical editing of the narrative, assisted literature review and a systematic audit of this report». El protocolo de supervisión aparece en el mismo párrafo: «ninguna afirmación empírica se originó en una salida de IA sin contraste contra los archivos» (L1469) / «no empirical claim was taken from an AI output without verification against the files» (L1471), con procedencia declarada —«las cifras, los modelos estadísticos y las decisiones de diseño provienen de los datos y del código versionados en este repositorio»— y una huella de auditoría conservada en `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` junto con los trece artefactos de fase. La firma de cierre (L1483), «responsable del proyecto / project owner», atribuye la declaración. El criterio `V9.ai_use_declaration.master` se lee: «Declaration expected; should name tools, phases (research, drafting, code generation, translation), and supervision protocol». Este hallazgo sustituye el F-V9-001 negativo de la iteración 1 (`reviews/informe-tecnico-2026-11-27.v9-ethics.md`), que no localizaba declaración en §1–§68.

— polarity: positive · confidence: high · related: [[#F-V9-002]], [[#F-V9-003]] · criteria: V9.ai_use_declaration.master

### F-V9-002 — Herramientas de IA no nombradas individualmente en §69

La declaración emplea solo el genérico «Las herramientas de inteligencia artificial» (L1469) / «AI tools» (L1471). El único nombre propio del pasaje es `review` —«La auditoría completa de este documento se realizó con la skill `review` de MatCom» (L1469)—, que designa el procedimiento de auditoría y no una herramienta generativa concreta. La búsqueda de «ChatGPT», «Claude», «Gemini», «Copilot», «OpenCode», «DeepSeek» y nombres de modelos en §69 (L1467–L1471) no devuelve coincidencias. Frente al criterio `V9.ai_use_declaration.master` («should name tools»), la declaración nombra fases y supervisión, pero deja las herramientas en términos genéricos. No se recibió `v7_ai_density_hint`, por lo que no se emite hallazgo cruzado de densidad.

— polarity: negative · confidence: high · related: [[#F-V9-001]] · criteria: V9.ai_use_declaration.master

### F-V9-003 — Generación de código y traducción ausentes de la declaración; investigación solo parcial

De las cuatro fases enumeradas en `V9.ai_use_declaration.master`, §69 declara redacción («la redacción», L1469), edición («la edición quirúrgica de la narrativa») e investigación en forma limitada («la revisión bibliográfica asistida»); añade la auditoría sistemática, que no figura en la lista del criterio. No declara generación de código: §6 (L74) enumera «Herramientas creadas: `ddg_research.py`, `buscar_fallback.py`, `descargar_hombros.py`, `scrape_concesionarios.py`, `resumen_catalogos.py` y `actualizar_informe.py`» y §8 (L90) describe el scraper con adaptadores por dominio, sin que §69 atribuya o excluya asistencia de IA en ese trabajo. Tampoco declara traducción: el documento es bilingüe —Parte II (L143–L270) y las dos versiones ES/EN de §69 (L1469, L1471)— sin que se mencione la traducción como fase asistida. La fase de investigación tampoco cubre el descubrimiento y la verificación de fuentes de §5 y §7, aunque la declaración no las excluya explícitamente.

— polarity: negative · confidence: high · related: [[#F-V9-001]], [[#F-V9-002]] · criteria: V9.ai_use_declaration.master



## §10 — Observaciones transversales

**Estado de las observaciones de la iteración 1.** E1 de iter2 (L840–851) evalúa las ocho observaciones transversales registradas en `reviews/informe-tecnico-2026-11-27.forensic.md` (L991–1037) contra el texto nuevo; E3 de iter2 aporta el contraste de artefactos en disco. Los identificadores F-V10-001..008 citados en este párrafo pertenecen a la pasada 1 y se conservan sin reasignación; los hallazgos nuevos de esta pasada se numeran a continuación. **Resueltas según E1: F-V10-003** (la declaración bilingüe de §69 cierra la ausencia de declaración de IA, con la salvedad de que no nombra herramientas ni protocolo) **y F-V10-008** (la muestra de 28 observaciones de 981 candidatas entra en el relato de §59–§60); E3 (L138–144, L268–271) matiza la segunda: el R² de 0,277 del texto no es el redondeo de 0,2744 del CSV y el estado previo de 572/22 de `MODELOS_Y_FUNCIONES.md` ya no existe en disco. **Siguen abiertas: F-V10-001** (E1: parcial; E3 confirma los estados simultáneos de §45, §58, §59 ES/EN, `kpis.csv` y README), **F-V10-002** (parcial; sin ablación ni test pareado; E3 muestra `principal` y `completo` sin citar en el relato), **F-V10-004** (parcial; E3 mantiene la TRMI fija de `config.py` frente al 920 y la conversión diaria del espejo inglés), **F-V10-005** (parcial; E3, L196, describe la divergencia de contenido entre §12 ES y §12 EN), **F-V10-006** (no resuelta; el único párrafo comparativo sigue siendo «Brecha frente a Egipto») **y F-V10-007** (parcial; E3, L131–136 y L278–281, confirma 38 entradas sin marca positiva de verificación, gacetas fuera del árbol y VAHAN/BCC sin ruta operativa).

### F-V10-001 — La declaración de §69 concentra los dispositivos de superficie y deja fuera código y traducción

La tabla de densidad de V7 sitúa §69 en nivel `medium` —dos series de cola larga, tres adjetivos sin ancla y unos doce metaconceptos en ~200 palabras— mientras los dos bloques que permanecen en `high` (§17–21 y §59–63) son idénticos a los de la pasada 1; los tres adjetivos nuevos («edición **quirúrgica**», «revisión bibliográfica **asistida**», «auditoría **sistemática**», L1469 y L1471) aparecen todos en la sección declarativa. V9 confirma que §69 nombra redacción, edición, revisión bibliográfica y auditoría como sustantivos comunes, sin herramientas generativas identificadas, y que no declara la generación de código que §6 (L74) atribuye a seis scripts propios ni la traducción del documento bilingüe. En paralelo, V6 localiza `SEED = 20261127` en `Data/analisis_rentabilidad/scripts/run_all.py:9–18`, con un docstring que afirma que la semilla se declara «aqui y en el informe», sin que la cifra aparezca en la caché auditada. La declaración existe y describe fases y procedencia, pero los rasgos de superficie y las fases no nombradas coinciden en el mismo bloque.

— polarity: neutral · confidence: high · related: [[#F-V7-002]], [[#F-V7-004]], [[#F-V9-002]], [[#F-V9-003]], [[#F-V6-003]]

### F-V10-002 — El aparato numerado nuevo no modera la cadena claim→fuente ni el contraste con los vecinos académicos

§70 y `Data/referencias.md` son los añadidos bibliográficos de esta pasada: 38 entradas con autores, DOI o URL y campo «Citada en el informe: sí/no». V5 registra, sin embargo, una sola entrada marcada «yes» ([1]), 9 de 13 afirmaciones load-bearing sin citas numeradas y 0 marcas `[N]` en las 1.484 líneas del texto; las 18 referencias de 2022–2026 conservan «Citada en el informe: no». V4 constata que P014 (Gegić et al., 2019), P026 (Muça et al., 2026), P009 (Du et al., 2026) y P029 (Vidal Alejandro et al., 2024) figuran en la lista sin citas en el cuerpo y que el único párrafo comparativo sigue siendo «Brecha frente a Egipto» (§34, L1058–1060), por escala de datos y en dirección desfavorable al propio proyecto; la observación F-V10-006 de la pasada 1 permanece «NO RESUELTA» en el propio E1 (L849). V8 añade la contradicción de etiquetas: §70 presenta a Akerlof como «verificada externamente (Crossref/OpenAlex)» mientras `[1]` cierra con `(metadata incomplete)`, y tres flags cuyo motivo quedó resuelto en vivo ([18], [19], [20]) no se reflejan en las fichas. La transparencia formal del aparato y la ausencia de engagement argumentativo avanzan por caminos distintos.

— polarity: negative · confidence: high · related: [[#F-V4-002]], [[#F-V4-003]], [[#F-V5-001]], [[#F-V5-003]], [[#F-V8-004]]

### F-V10-003 — Marcadores autoactualizados: CSV y README convergen, la caché y el espejo inglés no

§59 (L1379–L1381) fija «772 autos únicos», «2.029 anuncios limpios», «43.000 km» y añade que «los valores se actualizan solos en `outputs/tables/kpis.csv`». V3 coteja esa frase con el archivo citado —2.156 anuncios, 1.465 locales, 33.256 km, 113 grupos y 89 anomalías— y con `PRESENTACION_STORYTELLING.md:75–77,201–211`, que lleva los marcadores resueltos 952 / 2.156 / 1.465 / 33.256 km / 113 / 89; V6 confirma que `README.md:3,10,33` repite 952 autos y 2.156 anuncios, que el panel vigente `Data/dashboard.html` se documenta en `Data/AUTOMATIZACION.md` y no en el informe, y que la caché auditada no se regeneró tras actualizar el marcador `<!-- kpi:autos_revolico -->`. V1 y E3 (L196) registran que el párrafo **EN.** de §59 (L1383) conserva el estado previo de «744 unique cars, 2,014 clean listings» y que la conclusión 5 de §12 EN niega la implementación que §12 ES afirma. La automatización produce cifras operables en el repositorio y, al mismo tiempo, tres lecturas distintas del mismo objeto dentro del documento.

— polarity: negative · confidence: high · related: [[#F-V3-001]], [[#F-V3-002]], [[#F-V6-007]], [[#F-V6-009]], [[#F-V1-002]]

### F-V10-004 — La retirada de la depreciación coincide con los coeficientes archivados, pero deja fuera la segunda especificación y la literatura convergente

§34 (L1056) reportó «−5,43 % anual (p<0,001)» y una prima premium; §59–§60 (L1381, L1389) consignan que la corrida vigente «no sostiene una tasa de depreciación ni una prima premium significativa». V3 verifica la afirmación cualitativa en `modelo_depreciacion.csv`: `car_age` con p 0,1504, `C(brand_tier)[T.premium]` con p 0,8753 y ninguno de los siete coeficientes no intercepto por debajo de 0,05. El mismo cotejo muestra dos límites: V3 (F-V3-005) señala que `modelo_muestra.csv` archiva `principal` con 584 observaciones y p del F 0,0 —donde la antigüedad alcanza p<0,05 según `MODELOS_Y_FUNCIONES.md`— sin que el relato lo mencione, y V2 describe que el paso de 584 a 28 observaciones confunde el efecto del componente con la selección muestral, sin ablación declarada ni test pareado. V5 (F-V5-009) reúne cuatro obras que apuntan en el mismo sentido —Du et al. 2026 [9], Miranda et al. 2026 [11], Englmaier et al. 2017 y Francke y Van de Minne 2020 [13]— todas con «Citada en el informe: no». La corrección del resultado y la cobertura del relato sobre la evidencia disponible no coinciden.

— polarity: neutral · confidence: high · related: [[#F-V2-002]], [[#F-V2-005]], [[#F-V3-005]], [[#F-V3-006]], [[#F-V5-009]]

### F-V10-005 — Semilla declarada en el orquestador, ausente del informe y sin propagación a los cinco pasos

V6 localiza en `Data/analisis_rentabilidad/scripts/run_all.py:9–18` la definición `SEED = 20261127`, las llamadas `random.seed(SEED)` y `np.random.seed(SEED)` y un docstring que afirma: «La semilla se declara aqui y en el informe para cumplir el criterio de determinismo de nivel master». La búsqueda de `SEED`, `20261127` y «determinismo» en el texto cacheado no devuelve coincidencias: V2 registra que las únicas «semillas» del documento son las ocho URLs de partida de marketplaces de §55 (L1337). Los cinco scripts se lanzan con `subprocess.run` (`run_all.py:29–35`), es decir, en intérpretes nuevos que no heredan el estado de los generadores del padre; los pasos declarados son deterministas por agregación y OLS, no por esa semilla. V6 añade que `run_all.py`, `requirements.txt` y la prueba de humo figuran como modificados o no rastreados frente al HEAD `99c7065`, de modo que la afirmación de §69 (L1469) sobre datos y código «versionados en este repositorio» describe un estado posterior al commit. La declaración de reproducibilidad del texto y la declaración de determinismo del código no se corresponden.

— polarity: negative · confidence: high · related: [[#F-V2-010]], [[#F-V2-011]], [[#F-V6-003]], [[#F-V6-006]]

## Apéndice A — Plan

# Plan de auditoría — Iteración 2

## Iteración declarada
Segunda pasada sobre `INFORME_TECNICO.md` tras las mejoras aplicadas el 27/11/2026:
secciones 69 (declaración de IA) y 70 (referencias verificadas), modelo con
572/22 observaciones y `modelo_muestra.csv`, KPIs con marcadores automáticos
y estado mutable de timers fuera del repositorio.

## Dimensiones
- Re-ejecutar: E1, E2, E3 y V1–V9.
- Heredar como contexto: informe y expediente de la iteración 1.
- Comprobar específicamente: que las ocho observaciones transversales de la
  pasada anterior quedaron resueltas y que no aparecieron contradicciones nuevas.

## Fase 3
- Informe narrativo: `reviews/informe-tecnico-2026-11-27-iter2.md`
- Expediente: `reviews/informe-tecnico-2026-11-27-iter2.forensic.md`


## Apéndice B — Claims

# Claim Inventory

## Summary
- Total: 120
- Load-bearing: 13 · Supporting: 42 · Contextual: 65
- By type: result 60 · methodological 43 · novelty 1 · contextual 43 · definitional 5 · citation-grounded 11

## Load-bearing claims

### C001 — Objetivo vigente: análisis de mercado, recomendador diferido

- **Section**: §1 Objetivo (L16); §21 Cambio de objetivo (L881–886); Parte II §1 (L147)
- **Lines**: 16–18
- **Types**: definitional, contextual
- **Excerpt**: «Su objetivo actual es realizar un **análisis del mercado automotor cubano**: caracterizar estructura, precios, oferta, segmentos, tendencias, asequibilidad y condiciones de rentabilidad.»
- **Restated**: El objetivo declarado es el análisis del mercado automotor cubano y no la recomendación interactiva, que queda diferida a una especialización futura.
- **Internal evidence cited**: §21 (L881–886), §20 (L863, L870), Parte II §12 (L270, en sentido opuesto)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: la conclusión 5 de la Parte II (L270) sigue afirmando que el modelo y el producto interactivo «are not implemented yet», en contradicción con §12 español (L139).

### C002 — Fase 8 implementada y regenerada automáticamente

- **Section**: §12 Conclusiones (L139); §2 nota de actualización (L38); §34 (L1016–1037)
- **Lines**: 139
- **Types**: result, methodological
- **Excerpt**: «El análisis de mercado y el modelo de rentabilidad (fase 8) están implementados en `Data/analisis_rentabilidad/` y se regeneran de forma automática; la definición del producto interactivo se difiere a una especialización futura.»
- **Restated**: El pipeline de análisis y rentabilidad existe en `Data/analisis_rentabilidad/` y puede regenerarse automáticamente.
- **Internal evidence cited**: §34 (L1018–1037), §38 (L1112), §59–§60 (L1377–1391)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: cierra la contradicción principal de la iteración 1 en la Parte I; permanece en la Parte II (L164, L270).

### C003 — Cifras canónicas de la corrida vigente

- **Section**: §59 Storytelling alineado con los datos finales (L1379–1381)
- **Lines**: 1379
- **Types**: result
- **Excerpt**: «**772 autos únicos**, **2.029 anuncios limpios** (1.338 locales y 691 de importación), mediana local de **21.000 USD**, kilometraje mediano de **43.000 km**, 50 marcas, 101 grupos comparables y 81 anomalías»
- **Restated**: La corrida vigente del 27/11/2026 produce 772 autos únicos, 2.029 anuncios limpios, mediana local de 21.000 USD y 43.000 km, 50 marcas, 101 grupos y 81 anomalías.
- **Internal evidence cited**: §59 (L1379, `outputs/tables/kpis.csv` con marcadores automáticos), §58 (L1371, estado anterior)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: §45 (L1214) conserva 23.000 USD, 6,3 años, 34 marcas y 27 grupos; §58 (L1371) conserva 2.014 anuncios y 44.125 km.

### C004 — Modelo vigente sin pendiente anual significativa ni prima premium

- **Section**: §59 (L1381); §60 (L1389); §44 (L1206)
- **Lines**: 1381
- **Types**: result, methodological
- **Excerpt**: «La depreciación se reformuló con honestidad: el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra.»
- **Restated**: En la corrida vigente el coeficiente de edad del modelo hedónico no es significativo tras controlar por kilometraje.
- **Internal evidence cited**: §60 (L1389: p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05), §44 (L1206)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: retirada declarada del −5,43 % de §34; sin ablación ni test pareado entre corridas.

### C005 — Muestra del modelo completo: 28 observaciones de 981 candidatas

- **Section**: §59 (L1381)
- **Lines**: 1381
- **Types**: result
- **Excerpt**: «28 observaciones completas de <!-- kpi:modelo_candidatas -->981 candidatas (R² = <!-- kpi:modelo_r2_completo -->0,277; p del F = <!-- kpi:modelo_pf_completo -->0,411), límite que se registra explícitamente en `MODELOS_Y_FUNCIONES.md`.»
- **Restated**: La estimación completa usa 28 observaciones, con R² 0,277 y p del estadístico F 0,411, y la limitación está documentada.
- **Internal evidence cited**: §60 (L1389), `MODELOS_Y_FUNCIONES.md` (mencionado en L1381)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: incorpora al relato la dimensión muestral ausente en la iteración 1.

### C006 — Primera ejecución: depreciación −5,43 % anual (p<0,001)

- **Section**: §34 Línea base real de la primera ejecución (L1041–1056)
- **Lines**: 1056
- **Types**: result
- **Excerpt**: «El modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` da una depreciación media de **−5,43 % anual** (p<0,001), con primas de +21 % para premium y −22 % para tier medio frente al desconocido.»
- **Restated**: La primera corrida estimó −5,43 % anual de depreciación, +21 % de prima premium y −22 % para el tier medio.
- **Internal evidence cited**: §34 tabla «Línea base real de la primera ejecución» (L1043–1054)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: cifra retirada en §59–§60 pero reutilizada en §44 (L1206, con salvedad) y §45 (L1214, sin salvedad).

### C007 — Procedencia: anuncios como precios pedidos, no transaccionados

- **Section**: §18 Auditoría de procedencia (L826, L831–833)
- **Lines**: 831
- **Types**: methodological, definitional
- **Excerpt**: «los anuncios y redes son la **señal de precio** pero no sustituyen estadísticas oficiales. El análisis debe etiquetar cada métrica con su procedencia y nivel de confianza, y no mezclar tasas oficiales e informales ni precios anunciados con precios de transacción.»
- **Restated**: El análisis trata los anuncios como señal de precio pedido y prohíbe mezclar tasas oficiales con informales.
- **Internal evidence cited**: §18 tabla de procedencia (L816–829), §19 (L850, L855), §20 (L864)
- **External evidence cited**: DfT/DVLA y ANFAC/AEADE, verificados en vivo según §18 (L818, L822–823) y §70 (L1477)
- **Novelty signals**: ninguno.
- **Notes**: —

### C008 — Declaración de uso de inteligencia artificial

- **Section**: §69 Declaración de uso de inteligencia artificial (L1467–1471)
- **Lines**: 1469–1471
- **Types**: methodological
- **Excerpt**: «Las cifras, los modelos estadísticos y las decisiones de diseño provienen de los datos y del código versionados en este repositorio; ninguna afirmación empírica se originó en una salida de IA sin contraste contra los archivos.»
- **Restated**: Toda afirmación empírica del informe fue contrastada contra archivos versionados y la auditoría con la skill `review` quedó registrada.
- **Internal evidence cited**: §69 (L1469–1471), `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` y trece artefactos de fase
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: sección nueva que cierra la ausencia de declaración de F-V10-003; no nombra herramientas concretas ni protocolo de supervisión.

### C009 — Referencias verificadas y estado del resto del aparato

- **Section**: §70 Referencias verificadas (L1475–1479)
- **Lines**: 1477–1479
- **Types**: citation-grounded
- **Excerpt**: «Akerlof (1970), *The Market for "Lemons"* (Crossref/OpenAlex); UK Department for Transport / DVLA, estadísticas de vehículos (GOV.UK); ANFAC, informes del sector automotriz español (sitio oficial); AEADE, estadísticas de matriculaciones (sitio oficial).»
- **Restated**: Solo cuatro referencias están verificadas externamente; las restantes figuran como `(metadata incomplete)` y la convención numerada reúne 38 entradas.
- **Internal evidence cited**: §70 (L1477–1479), `Data/referencias.md`, `reviews/informe-tecnico-2026-11-27.e2-literature.md`
- **External evidence cited**: Crossref, OpenAlex, GOV.UK, sitios oficiales de ANFAC y AEADE (según declara L1477)
- **Novelty signals**: ninguno.
- **Notes**: atiende parcialmente F-V10-007; el cuerpo del informe sigue sin citas numeradas.

### C010 — Conversión TRMI: serie diaria referencial, 930 fijo en el modelo

- **Section**: §23 Conversión elTOQUE (L902); §52 (L1297); Parte II §23 (L907)
- **Lines**: 902
- **Types**: methodological
- **Excerpt**: «**Aclaración vigente:** el pipeline de `Data/analisis_rentabilidad/` usa la TRMI fija de 930 CUP/USD del 18/11/2026 (`config.py`); la serie diaria es referencia histórica, no insumo del modelo actual.»
- **Restated**: La conversión del modelo usa 930 CUP/USD fijos y la serie diaria de elTOQUE no alimenta la estimación vigente.
- **Internal evidence cited**: §23 (L902), §52 (L1297), `config.py` (mencionado en L902)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: aclara la dualidad 920/930 de F-V10-004 en español; L904 mantiene el 920 histórico y L907 (inglés) sigue describiendo conversión diaria.

### C011 — Arquitectura del esqueleto inspirada en Egyptian-Used-Cars

- **Section**: §34 (L1018–1039)
- **Lines**: 1018
- **Types**: methodological, novelty
- **Excerpt**: «Creé `Data/analisis_rentabilidad/` siguiendo la arquitectura del repositorio **Egyptian-Used-Cars** (ingesta → limpieza → EDA → estadística → benchmark), pero adaptada a nuestras fuentes y preparada para crecer:»
- **Restated**: La arquitectura del pipeline de rentabilidad deriva de Egyptian-Used-Cars y fue adaptada a las fuentes cubanas.
- **Internal evidence cited**: §34 (L1018–1039), §60 (L1387–1390)
- **External evidence cited**: repositorio `Egyptian-Used-Cars` (fuente de ingeniería, sin ficha académica en el documento)
- **Novelty signals**: «Creé» (L1018), «adaptada a nuestras fuentes» (L1018), «preparada para crecer» (L1018).
- **Notes**: es la única diferenciación comparativa declarada del documento (F-V10-006).

### C012 — Brecha frente a Egipto

- **Section**: §34 Brecha frente a Egipto (L1058–1060)
- **Lines**: 1060
- **Types**: result, contextual
- **Excerpt**: «Egipto tiene 23.500 anuncios, historial mensual de precios, HP y kilometraje estructurados, ANOVA/OLS/VIF, Tableau y Power BI. Nosotros tenemos el pipeline y las técnicas cubiertas, pero solo 497 usados, un único snapshot, HP/kilometraje mayormente ausentes y un solo benchmark de auto nuevo.»
- **Restated**: Frente a 23.500 anuncios del repositorio egipcio, el proyecto dispone de 497 usados, una sola instantánea y campos mayormente ausentes.
- **Internal evidence cited**: §34 tabla de la primera ejecución (L1045–1054), `NECESIDADES.md`
- **External evidence cited**: repositorio `Egyptian-Used-Cars` (sin verificación académica en el documento)
- **Novelty signals**: ninguno.
- **Notes**: diferenciación por escala y cobertura, no por método.

### C013 — Límites declarados del marco analítico

- **Section**: §19 Adaptación a Cuba / La Habana (L848–855)
- **Lines**: 855
- **Types**: definitional, methodological
- **Excerpt**: «- **Límites**: precios pedidos no transaccionados, sesgo de supervivencia de anuncios, sin datos personales, vigencia normativa a verificar.»
- **Restated**: El análisis declara como límites los precios pedidos, el sesgo de supervivencia, la ausencia de datos personales y la vigencia normativa pendiente.
- **Internal evidence cited**: §19 (L850–855), §18 (L831), §20 (L871)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: —

## Supporting claims (42)

### C014 — Fase 6: 11 bases y 256 filas
- **Section**, **Lines**: §9 (L94–110), 94–108
- **Types**: result
- **Excerpt**: «Se prepararon 11 bases y se obtuvieron **256 filas**:»
- **Restated**: La fase 6 produjo 256 filas distribuidas en 11 tiendas.
- **Internal/External evidence**: tabla de tiendas (L96–108); sin citas numeradas.
- **Notes**: las once filas suman 256 (AGN 60, ATR 6, BDC 19, Changan 2, Chinautos 70, ConnectingCuba 1, Dongfeng 45, Envision 1, Finauto 45, MCV 4, Subasta 3).

### C015 — Fuentes excluidas por bloqueo técnico
- **Section**, **Lines**: §9 (L110), 110
- **Types**: result, contextual
- **Excerpt**: «Excluidas por bloqueo técnico: carrosw (HTTP 403 con Bot Verification), LlamaCuba (timeout) y SASA/DIVEP (sin catálogo).»
- **Restated**: Tres fuentes quedaron fuera de la captura por 403, timeout o ausencia de catálogo.
- **Internal/External evidence**: §9 (L110), §11 (L129); sin citas numeradas.
- **Notes**: —

### C016 — Descubrimiento: 409 resultados, 400 únicos
- **Section**, **Lines**: §5 (L62), 62
- **Types**: result
- **Excerpt**: «Se consolidaron **409 resultados, 400 únicos**.»
- **Restated**: La consolidación inicial produjo 409 resultados, de los cuales 400 son únicos.
- **Internal/External evidence**: §5 (L62); sin citas numeradas.
- **Notes**: —

### C017 — Inventario y verificación de sitios
- **Section**, **Lines**: §5 (L62, L64), 62–64
- **Types**: result
- **Excerpt**: «Se inventariaron **35 sitios** de compraventa en `Data/mercados-compraventa-cuba.md`» / «Se verificaron **40 sitios/URLs**.»
- **Restated**: Se inventariaron 35 sitios de compraventa y se verificaron 40 sitios o URLs.
- **Internal/External evidence**: §5 (L62, L64); sin citas numeradas.
- **Notes**: —

### C018 — Organismos con competencia sobre el mercado
- **Section**, **Lines**: §5 (L66), 66
- **Types**: result, contextual
- **Excerpt**: «Se documentaron **14 organismos** con competencia sobre el mercado: Consejo de Ministros/Estado, MINCEX, MINCIN, MITRANS, CEMA, MFP, ONAT, Aduana General, BCC, MININT, MINJUS, MEP, MINREX y MINSAP.»
- **Restated**: El documento identifica 14 organismos con competencia sobre el mercado automotor.
- **Internal/External evidence**: §5 (L66); sin citas numeradas.
- **Notes**: —

### C019 — Empresas autorizadas y precios de referencia
- **Section**, **Lines**: §4 (L58), 58
- **Types**: result, citation-grounded
- **Excerpt**: «Se documentaron **17 empresas autorizadas** a importar y comercializar vehículos, distribuidores privados (BDC One, Dongfeng, MCV, Finauto, Changan, Chinautos, Envision, ATR Export), precios de referencia (BDC One 14.849–31.478 EUR; Dongfeng desde 21.900 EUR; Finauto desde 15.500 EUR»
- **Restated**: El marco normativo registra 17 empresas autorizadas y precios de referencia por distribuidor.
- **Internal/External evidence**: §4 (L58), `Data/investigacion-mercado-automotor-cuba.md`; sin citas numeradas.
- **Notes**: el equivalente inglés (L189) usa separadores de miles con coma.

### C020 — Marco normativo: Decreto 163/2026 y resoluciones
- **Section**, **Lines**: §4 (L58), §10 (L116–117), 58/116–117
- **Types**: citation-grounded
- **Excerpt**: «La norma marco es el **Decreto 163/2026** (Gaceta Oficial No. 65 Ordinaria, 04/08/2026, vigente desde el 11/08/2026), que deroga el Decreto 119/2024.»
- **Restated**: El Decreto 163/2026 es la norma marco vigente y deroga el Decreto 119/2024.
- **Internal/External evidence**: §4 (L58), §10 (L116–118); Gaceta Oficial No. 65/2026 citada sin numeración.
- **Notes**: —

### C021 — Derogación de la Resolución 312/2026
- **Section**, **Lines**: §52 (L1303), 1303
- **Types**: citation-grounded, result
- **Excerpt**: «la **Resolución 312/2026 de la Aduana General fue derogada por la Resolución 340/2026**.»
- **Restated**: La Resolución 340/2026 deroga a la 312/2026, que no debe citarse como norma vigente.
- **Internal/External evidence**: §52 (L1303), §4 (L58), §10 (L117); sin citas numeradas.
- **Notes**: corrección documentada en README, informe y verificación de marketplaces.

### C022 — Clonación de repositorios y clasificación CAPTCHA
- **Section**, **Lines**: §6 (L70), 70
- **Types**: result
- **Excerpt**: «Se clonaron **61 repositorios** en `Auxiliares/Repositorios` con `--depth 1` (2,2 GB, 61 entradas `OK`).»
- **Restated**: Se clonaron 61 repositorios (2,2 GB) y se clasificaron 92 proyectos CAPTCHA, de los que se seleccionaron 9.
- **Internal/External evidence**: §6 (L70); sin citas numeradas.
- **Notes**: —

### C023 — Entorno y dependencias instaladas
- **Section**, **Lines**: §6 (L72), 72
- **Types**: contextual
- **Excerpt**: «Se creó `Auxiliares/.venv` con patchright 1.64.4, PyPasser 1.1.0, Scrapling 0.5.1, ddddocr 1.6.1, playwright 1.65.2, curl_cffi 0.17.0, trafilatura, pandas, numpy, onnxruntime 1.32.0, ddgs 9.16.1 y tenacity 9.2.1.»
- **Restated**: El entorno virtual contiene las versiones declaradas de once dependencias.
- **Internal/External evidence**: §6 (L72); sin citas numeradas.
- **Notes**: —

### C024 — Regla de parada en la búsqueda documental
- **Section**, **Lines**: §7 (L78–86), 78–84
- **Types**: methodological, result
- **Excerpt**: «Tres búsquedas con la regla de parar tras 10 páginas sin enlaces útiles (útil = primera aparición de un trabajo investigativo automotriz):»
- **Restated**: Las tres búsquedas se detuvieron tras diez páginas sin enlaces útiles, con 159 páginas y 1.542 resultados en total.
- **Internal/External evidence**: tabla de búsquedas (L80–84); sin citas numeradas.
- **Notes**: las paradas declaradas fueron páginas 19, 11 y 22.

### C025 — Esquema SQLite por tienda
- **Section**, **Lines**: §8 (L90), 90
- **Types**: definitional, methodological
- **Excerpt**: «Se diseñó una base SQLite por tienda con una tabla `vehiculos`: identificación (`url`, `shop`, `title`, `status`, `scraped_at`), metadatos y 30 campos estructurados»
- **Restated**: El diseño prevé una base SQLite por tienda con 30 campos estructurados y campos sin normalizar.
- **Internal/External evidence**: §8 (L90); sin citas numeradas.
- **Notes**: —

### C026 — Conclusión: nueve marketplaces con inventario real
- **Section**, **Lines**: §12 (L135), 135
- **Types**: result, contextual
- **Excerpt**: «El mercado habanero tiene nueve marketplaces con inventario real y una docena con categorías vacías o solo piezas.»
- **Restated**: El mercado habanero cuenta con nueve marketplaces con inventario real y alrededor de una docena sin inventario de autos.
- **Internal/External evidence**: §5 (L64), §12 (L135); sin citas numeradas.
- **Notes**: el expediente de la iteración 1 observó quince sitios en esa categoría.

### C027 — Causalidad declarada del scraping sostenible
- **Section**, **Lines**: §12 (L137), 137
- **Types**: methodological
- **Excerpt**: «El scraping sostenible depende del ritmo, la sesión y la reanudación, no principalmente del fingerprint TLS.»
- **Restated**: El ritmo, la sesión y la reanudación son los factores decisivos del scraping sostenible, por encima del fingerprint TLS.
- **Internal/External evidence**: §11 (L126–131), §37 (L1100), §65 (L1433); sin comparación de condiciones.
- **Notes**: atribución causal sin contraste experimental.

### C028 — Regla de las 10 páginas
- **Section**, **Lines**: §12 (L138), 138
- **Types**: methodological, result
- **Excerpt**: «La regla de las 10 páginas evitó consumir resultados repetidos.»
- **Restated**: La regla de parada de diez páginas impidió procesar resultados repetidos.
- **Internal/External evidence**: §7 (L78–84), §33 (L1008); sin citas numeradas.
- **Notes**: —

### C029 — Nota de actualización de fases
- **Section**, **Lines**: §2 (L38); Parte II §2 (L169), 38
- **Types**: contextual, result
- **Excerpt**: «El pipeline de análisis (fase 8) se creó después, el 18/11/2026 (§34), y sus resultados vigentes se documentan en §59–§60.»
- **Restated**: La tabla de fases refleja el estado al 17/11/2026 y la fase 8 se creó el 18/11/2026.
- **Internal/External evidence**: §2 (L22–38), §34 (L1016), §59–§60; sin citas numeradas.
- **Notes**: atenúa pero no elimina la contradicción con la tabla de la Parte II (L164).

### C030 — Permanencia empírica de anuncios en Revolico
- **Section**, **Lines**: §15 (L775), 775
- **Types**: result
- **Excerpt**: «un anuncio con `updated_on_by_user=2024-12-17` seguía en HTTP 200 el 17/11/2026 (~699 días), por lo que no puede asumirse una expiración de 30 días.»
- **Restated**: Un anuncio con 699 días de antigüedad seguía accesible, de modo que no se puede asumir caducidad a los 30 días.
- **Internal/External evidence**: §15 (L775), Condiciones de Uso de Revolico (23/09/2026) citadas sin numeración.
- **Notes**: —

### C031 — Limpieza de la BD de Revolico
- **Section**, **Lines**: §15 (L773), 773
- **Types**: result
- **Excerpt**: «`limpiar_revolico.py` conservó **304 autos** en la tabla `autos` y registró **6.028 exclusiones** en `revision` (5.983 no vehículo 4+ ruedas, 45 sin datos necesarios, 0 páginas sin datos suficientes).»
- **Restated**: Sobre 6.332 anuncios se conservaron 304 autos y se registraron 6.028 exclusiones.
- **Internal/External evidence**: §15 (L771–773), §16 (L787); sin citas numeradas.
- **Notes**: 304 + 6.028 = 6.332.

### C032 — Eficiencia relativa de las fuentes
- **Section**, **Lines**: §15 (L767–769), 767
- **Types**: methodological
- **Excerpt**: «la ruta más eficiente es Telegram MTProto (`telethon`, ya integrado): sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`. Le sigue Facebook GQL»
- **Restated**: Telegram MTProto es la fuente más eficiente, seguida de Facebook GQL, WAHA para WhatsApp y Playwright/Selenium como último recurso.
- **Internal/External evidence**: §15 (L767–769), §28 (L950); sin citas numeradas.
- **Notes**: jerarquía declarada sin medición comparativa de rendimiento.

### C033 — Pipeline de tres colas persistentes
- **Section**, **Lines**: §16 (L779–783), 779–783
- **Types**: methodological
- **Excerpt**: «separa el trabajo en tres etapas simultáneas con colas persistentes en `Data/Revolico/pipeline.sqlite`»
- **Restated**: El pipeline separa descubrimiento, descarga y procesamiento con colas persistentes y commit cada 25 anuncios.
- **Internal/External evidence**: §16 (L779–787), §26 (L928–933); sin citas numeradas.
- **Notes**: —

### C034 — Prueba inicial del pipeline por colas
- **Section**, **Lines**: §16 (L787), 787
- **Types**: result
- **Excerpt**: «Prueba con 1 página: **119 enlaces** descubiertos y procesados, 7 lotes de 25, BD principal de 6.332 a **6.334 anuncios** y de 304 a **317 autos**.»
- **Restated**: La prueba con una página procesó 119 enlaces y elevó la BD a 6.334 anuncios y 317 autos.
- **Internal/External evidence**: §16 (L787, L789); sin citas numeradas.
- **Notes**: el número de lotes completos de 25 es cuatro, no siete (coherencia interna no verificada).

### C035 — Rango temporal de anuncios
- **Section**, **Lines**: §31 (L987–989), 987–989
- **Types**: methodological, result
- **Excerpt**: «Se fijó el rango permitido de `updated_on_by_user` entre **2021-01-01 y la fecha actual** en `limpiar_revolico.py` (`FECHA_MINIMA`).»
- **Restated**: Los anuncios se acotan entre 2021-01-01 y la fecha de ejecución, sin exclusiones en la corrida declarada.
- **Internal/External evidence**: §31 (L987–991); sin citas numeradas.
- **Notes**: anuncio más antiguo 2024-12-17, más reciente 2026-11-17; 548 autos de 9.957 anuncios.

### C036 — Deduplicación de `autos`
- **Section**, **Lines**: §51 (L1279), 1279
- **Types**: result
- **Excerpt**: «La tabla se reconstruyó desde `anuncios` (fuente canónica): 814 filas con 748 IDs únicos → **744 autos únicos**.»
- **Restated**: La deduplicación redujo 814 filas a 744 autos únicos y creó el índice `idx_autos_id`.
- **Internal/External evidence**: §51 (L1279), §59 (L1379, 772 autos en la corrida vigente); sin citas numeradas.
- **Notes**: cuatro anuncios se marcaron como no-auto.

### C037 — Reparación de precios y títulos de marketplaces
- **Section**, **Lines**: §51 (L1281), 1281
- **Types**: result, methodological
- **Excerpt**: «`parse_price` ahora interpreta separadores de miles (973 anuncios recuperados: 872 de iTENCEL, 99 de Cubisima, 2 de VentaCuba).»
- **Restated**: La corrección del parseo recuperó 973 precios y 614 precios de Autocubana desde JSON-LD.
- **Internal/External evidence**: §51 (L1281), `descartes_marketplaces.csv`; sin citas numeradas.
- **Notes**: mediana local declarada de 21.000 USD.

### C038 — Corrección del kilometraje con separador de miles
- **Section**, **Lines**: §51 (L1282), 1282
- **Types**: methodological, result
- **Excerpt**: «`parse_specs` y `parse_title` convertían `80,000 km` en 80 km. Se extrajo `parse_number()` con la lógica de separadores ya usada en `parse_price`.»
- **Restated**: La nueva función `parse_number()` convierte correctamente `80,000 km` en 80.000 km.
- **Internal/External evidence**: §51 (L1282); sin citas numeradas.
- **Notes**: —

### C039 — Reconciliación de la encuesta de demanda
- **Section**, **Lines**: §51 (L1285), 1285
- **Types**: result
- **Excerpt**: «el cruce filtra ahora `interes=1`, dando **28 interesados** (14 eléctrico, 10 combustión, 4 híbrido) en lugar de los 29 que contaba el script anterior»
- **Restated**: El cruce vigente cuenta 28 interesados, frente a 29 del script anterior.
- **Internal/External evidence**: §50 (L1269), §51 (L1285); sin citas numeradas.
- **Notes**: —

### C040 — Descarga de los anuarios del ONEI
- **Section**, **Lines**: §53 (L1313–1315), 1313–1315
- **Types**: result
- **Excerpt**: «se descargaron **todos los documentos enlazados**: 111 PDF, 7 RAR y 103 archivos Excel extraídos, unos 311 MB en total.»
- **Restated**: Se descargaron los 117 enlaces de los 12 anuarios del ONEI (2014–2025), con 111 PDF, 7 RAR y 103 Excel.
- **Internal/External evidence**: §53 (L1313–1315), `Data/fuentes-oficiales/ONEI/INDICE.md`; sin citas numeradas.
- **Notes**: validación MIME sin archivos sospechosos.

### C041 — Hallazgos de los anuarios y laguna de parque automotor
- **Section**, **Lines**: §56 (L1351), 1351
- **Types**: result
- **Excerpt**: «el transporte de pasajeros cayó un 59 % entre 2019 y 2025 y el ómnibus un 71 %; los accidentes bajaron pero la gravedad aumentó (9,9 fallecidos por cada 100 accidentes en 2025). **No hay series de parque automotor ni de matriculaciones**»
- **Restated**: Las series del ONEI muestran caídas del 59 % y 71 %, pero no contienen parque automotor ni matriculaciones.
- **Internal/External evidence**: §53 (L1317), §56 (L1351), `ANALISIS_DATO.md`; sin citas numeradas.
- **Notes**: corrige la expectativa registrada en §53 (L1317).

### C042 — Fragmentación de la BD con manifiesto
- **Section**, **Lines**: §54 (L1325–1329), 1325
- **Types**: methodological, result
- **Excerpt**: «`Data/Revolico/revolico.sqlite` (849.465.344 bytes) se dividió en **82 chunks de 10 MB** en `Data/Revolico/chunks/`, con un `MANIFEST.json` que guarda el SHA-256 del archivo completo, el orden, el offset y el hash de cada fragmento.»
- **Restated**: La BD de 849.465.344 bytes se dividió en 82 fragmentos verificados con manifiesto SHA-256.
- **Internal/External evidence**: §54 (L1325–1329), §14 (L756–763); sin citas numeradas.
- **Notes**: los chunks se publican en la rama huérfana `chunked-db`.

### C043 — Gestión con Git LFS
- **Section**, **Lines**: §30 (L977–981), 977–981
- **Types**: methodological
- **Excerpt**: «Se instaló **Git LFS 3.8.1** y se activó en el repositorio. `.gitattributes` marca `*.sqlite`, `*.sqlite-wal` y `*.sqlite-shm` con `filter=lfs diff=lfs merge=lfs -text`»
- **Restated**: Las bases SQLite se gestionan con Git LFS y se advierte sobre el consumo de cuota.
- **Internal/External evidence**: §30 (L977–983), §54 (L1327); sin citas numeradas.
- **Notes**: —

### C044 — Fuentes adicionales verificadas
- **Section**, **Lines**: §52 (L1293), 1293
- **Types**: result
- **Excerpt**: «El resultado está en `Data/fuentes-adicionales-2026-11-20.md`: **25 fuentes** verificadas, organizadas por tipo con URL, datos expuestos, viabilidad de scraping y aporte al proyecto.»
- **Restated**: Se verificaron 25 fuentes adicionales organizadas por tipo.
- **Internal/External evidence**: §52 (L1293–1305); sin citas numeradas.
- **Notes**: —

### C045 — Repositorios cubanos de automoción
- **Section**, **Lines**: §49 (L1251), 1251
- **Types**: result
- **Excerpt**: «Tras deduplicar se obtuvieron **648 repos**, de los que se depuraron **36 con relación directa o instrumental** al mercado automotor cubano.»
- **Restated**: La búsqueda produjo 648 repositorios únicos y 36 con relación directa o instrumental.
- **Internal/External evidence**: §49 (L1251–1255), `Data/github-repos-automotriz-cuba-2026-11-19.md`; sin citas numeradas.
- **Notes**: —

### C046 — Consolidación de bases de repositorios de referencia
- **Section**, **Lines**: §50 (L1267), 1267
- **Types**: result
- **Excerpt**: «Se creó `Data/repos-autos-referencias/referencias_autos.sqlite` con **25 tablas** (3.958 anuncios de Revolico, 3.566 limpios, catálogos de comercializadoras, 33 respuestas de encuesta, 30 + 30 + 8 entrevistas, datasets de AutosxCuba) y una tabla `provenancia`.»
- **Restated**: La base consolidada reúne 25 tablas con procedencia declarada.
- **Internal/External evidence**: §50 (L1263–1269); sin citas numeradas.
- **Notes**: 369 anuncios ya estaban en la base propia y 3.589 son nuevos.

### C047 — Detección de duplicados entre repositorios
- **Section**, **Lines**: §50 (L1265), 1265
- **Types**: result
- **Excerpt**: «Se compararon 233 archivos de datos por hash y 76 CSV por contenido ordenado. Se detectaron 12 grupos de duplicados bytes y 11 de duplicados por contenido»
- **Restated**: La comparación detectó 23 grupos de duplicados entre los archivos de los repositorios referencia.
- **Internal/External evidence**: §50 (L1265); sin citas numeradas.
- **Notes**: —

### C048 — Convención de 38 referencias con estado de verificación
- **Section**, **Lines**: §70 (L1477), 1477
- **Types**: result, citation-grounded
- **Excerpt**: «Las fuentes restantes figuran con estado `(metadata incomplete)` en `reviews/informe-tecnico-2026-11-27.e2-literature.md` y no se presentan como referencias verificadas. La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`»
- **Restated**: Existen 38 referencias numeradas con estado de verificación, cuatro de ellas confirmadas externamente.
- **Internal/External evidence**: §70 (L1477–1479), `Data/referencias.md`; Crossref/OpenAlex según el propio texto.
- **Notes**: —

### C049 — Incorporación de diez anuncios de iTENCEL
- **Section**, **Lines**: §58 (L1369–1371), 1371
- **Types**: result
- **Excerpt**: «La BD pasó de 951 a **961 anuncios** (961 URLs únicas, `integrity_check=ok`).»
- **Restated**: La base de iTENCEL pasó de 951 a 961 anuncios únicos tras insertar diez anuncios nuevos.
- **Internal/External evidence**: §57 (L1361), §58 (L1369–1373); sin citas numeradas.
- **Notes**: se realizó copia de seguridad `itencel.sqlite.bak-20261123` antes de escribir.

### C050 — Estado previo de los anuncios limpios
- **Section**, **Lines**: §58 (L1371), 1371
- **Types**: result
- **Excerpt**: «**2.014 anuncios limpios**, de ellos 1.323 locales y 691 de importación; mediana local 21.000 USD y mediana de kilometraje 44.125 km.»
- **Restated**: Tras la incorporación de iTENCEL, la regeneración produjo 2.014 anuncios limpios y 44.125 km de mediana.
- **Internal/External evidence**: §58 (L1371), §59 (L1379, cifras vigentes 2.029 y 43.000 km); sin citas numeradas.
- **Notes**: estado intermedio sustituido por §59.

### C051 — Capas del mapa offline
- **Section**, **Lines**: §41 (L1154–1157), §42 (L1177), 1177
- **Types**: result
- **Excerpt**: «Estado final: **131 gasolineras, 12 estaciones de carga, 25 concesionarios (17 con coords) y 22 talleres (todos con coords)**.»
- **Restated**: El mapa unificado contiene 131 gasolineras, 12 estaciones de carga, 25 concesionarios y 22 talleres.
- **Internal/External evidence**: §41 (L1154–1157, 137 gasolineras iniciales), §42 (L1168–1179); sin citas numeradas.
- **Notes**: el descenso de 137 a 131 gasolineras no se explica en el texto.

### C052 — Serie de precios del combustible
- **Section**, **Lines**: §41 (L1157–1160), 1157–1160
- **Types**: result, citation-grounded
- **Excerpt**: «Se creó `Data/combustible/precios_combustible.sqlite` con **18 observaciones** entre 20/08/2026 y 18/11/2026, diferenciando mercado oficial CIMEX, informal elToque y precios publicados, sin convertir monedas automáticamente.»
- **Restated**: La serie de combustible tiene 18 observaciones y separa mercado oficial, informal y precios publicados.
- **Internal/External evidence**: §41 (L1157–1160), §43 (L1189–1195, hitos normativos); sin citas numeradas.
- **Notes**: la B94 informal pasó de 3.500–5.000 CUP (agosto) a 7.000–8.000 CUP (septiembre 2026).

### C053 — Estimación de retención como inferencia de diseño
- **Section**, **Lines**: §63 (L1417), 1417
- **Types**: methodological
- **Excerpt**: «La estimación de retención (`Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md`) es **inferencia de diseño, no medición**»
- **Restated**: Las cifras de retención son una proyección de diseño, no una medición observada.
- **Internal/External evidence**: §63 (L1415–1419), `ALCANCE_Y_RETENCION.md`; sin citas numeradas.
- **Notes**: el propio texto rotula la naturaleza no empírica de la estimación.

### C054 — Compilación estricta del sitio
- **Section**, **Lines**: §61 (L1399), 1399
- **Types**: methodological, result
- **Excerpt**: «`mkdocs build --strict` termina sin errores ni enlaces rotos.»
- **Restated**: La compilación estricta del sitio MkDocs termina sin errores ni enlaces rotos.
- **Internal/External evidence**: §61 (L1397–1401), `mkdocs.yml`, `docs/`; sin citas numeradas.
- **Notes**: —

### C055 — Primera corrida real del scraper de circuitos
- **Section**, **Lines**: §62 (L1407), 1407
- **Types**: result
- **Excerpt**: «en su primera corrida real capturó 40 mensajes, deduplicó por ID y dejó 35 circuitos sin luz, 23 mixtos y 2 con luz en `Data/mapas/circuitos_estado.sqlite`.»
- **Restated**: El primer scrapeo de circuitos produjo 60 registros clasificados a partir de 40 mensajes.
- **Internal/External evidence**: §62 (L1405–1409), `TIMELAPSE_CIRCUITOS.md`; sin citas numeradas.
- **Notes**: 35 + 23 + 2 = 60, cifra superior a los 40 mensajes declarados.

## Contextual claims (65)

### C056 — Fase activa redefinida como sexta
- **Section**, **Lines**: §2 (L22), 22
- **Types**: contextual
- **Excerpt**: «Las fases se redefinieron para que la fase activa sea la sexta. Estado a 17/11/2026:»

### C057 — Informe y README como soporte transversal
- **Section**, **Lines**: §2 (L36), 36
- **Types**: contextual
- **Excerpt**: «La creación de este informe y del `README.md` es soporte transversal y no cambia la fase activa.»

### C058 — Decisiones de organización de carpetas
- **Section**, **Lines**: §3 (L54), 54
- **Types**: methodological, contextual
- **Excerpt**: «todo el material auxiliar vive dentro de `Auxiliares/`; los clones se hicieron con `--depth 1` y se registraron en `~/Utilidades/HerramientasScraping/_clone_log.tsv`; la descubrimiento se separó de la verificación»

### C059 — Exclusión de `Copias/`
- **Section**, **Lines**: §3 (L54), 54
- **Types**: contextual
- **Excerpt**: «`Copias/` no se registra en este informe por decisión explícita.»

### C060 — Decreto 163/2026 y Gaceta Oficial
- **Section**, **Lines**: §4 (L58), 58
- **Types**: citation-grounded
- **Excerpt**: «La norma marco es el **Decreto 163/2026** (Gaceta Oficial No. 65 Ordinaria, 04/08/2026, vigente desde el 11/08/2026), que deroga el Decreto 119/2024.»

### C061 — Cambio de motor de búsqueda
- **Section**, **Lines**: §5 (L62), 62
- **Types**: contextual
- **Excerpt**: «Dos búsquedas iniciales en DuckDuckGo, 30 páginas cada una, con bloqueo por CAPTCHA: se cambió a Yahoo y visitas directas.»

### C062 — Correcciones de clasificación de sitios
- **Section**, **Lines**: §5 (L64), 64
- **Types**: result, contextual
- **Excerpt**: «Se corrigieron clasificaciones: Mercadoba y Fagales Market sin sección real; TuCuevita, Mercubano, Mercandil, Revoltillo, QvaVentas, Casinuevo, Publicid, WAnuncios y AnunciosCuba con categoría vacía»

### C063 — Inventario de marketplaces activos
- **Section**, **Lines**: §5 (L64), 64
- **Types**: result
- **Excerpt**: «Marketplaces con sección activa: Autocubana (667 vehículos), iTENCEL (951), VentaCuba (801 carros/camionetas), Timbirichi (281 carros), Revolico (112 enlaces en la primera página), Cogetucarro (5.225 anuncios), Cubisima (155 fichas)»

### C064 — Cobertura temática de los repositorios clonados
- **Section**, **Lines**: §6 (L70), 70
- **Types**: contextual
- **Excerpt**: «El conjunto cubre scraping general (Firecrawl, browser-use, Scrapling, crawl4ai, Scrapy, SeleniumBase, trafilatura, curl_cffi, Patchright, Playwright), Facebook, WhatsApp, Telegram y CAPTCHA.»

### C065 — Chromium del sistema y FlareSolverr
- **Section**, **Lines**: §6 (L72), 72
- **Types**: contextual
- **Excerpt**: «Se usa el Chromium del sistema y FlareSolverr 3.5.2 en Docker (`http://127.0.0.1:8191/`).»

### C066 — Herramientas creadas en la fase 3
- **Section**, **Lines**: §6 (L74), 74
- **Types**: contextual
- **Excerpt**: «Herramientas creadas: `ddg_research.py`, `buscar_fallback.py`, `descargar_hombros.py`, `scrape_concesionarios.py`, `resumen_catalogos.py` y `actualizar_informe.py`.»

### C067 — Definición operativa de «útil»
- **Section**, **Lines**: §7 (L78), 78
- **Types**: definitional, methodological
- **Excerpt**: «útil = primera aparición de un trabajo investigativo automotriz»

### C068 — Resultados de descarga del corpus
- **Section**, **Lines**: §7 (L86), 86
- **Types**: result
- **Excerpt**: «descarga inicial **93 OK / 17 fallos**, rentabilidad **23 OK / 10 fallos**, calidad/precio **78 OK / 36 fallos**, con `manifest.jsonl` e `indice.md`.»

### C069 — Adaptadores por dominio y renderizado opcional
- **Section**, **Lines**: §8 (L90), 90
- **Types**: methodological
- **Excerpt**: «El scraper `scrape_concesionarios.py` usa adaptadores por dominio y renderizado opcional con Playwright.»

### C070 — Filtro de normas relevantes
- **Section**, **Lines**: §10 (L114), 114
- **Types**: contextual
- **Excerpt**: «Solo se incluyen las normas y fuentes relevantes para el contexto del proyecto:»

### C071 — No elusión de anti-automatización
- **Section**, **Lines**: §10 (L118), 118
- **Types**: methodological, contextual
- **Excerpt**: «No se eluden mecanismos anti-automatización; los HTTP 403/429 se registran como limitación.»

### C072 — Condiciones para publicar resultados
- **Section**, **Lines**: §10 (L119), 119
- **Types**: methodological, contextual
- **Excerpt**: «antes de publicar resultados deben verificarse las normas cubanas vigentes y aplicar solo datos agregados, sin nombres, teléfonos ni información personal de anunciantes.»

### C073 — Índice de gacetas fuera del árbol
- **Section**, **Lines**: §10 (L120), 120
- **Types**: contextual
- **Excerpt**: «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe»

### C074 — Solución al CAPTCHA de paginación
- **Section**, **Lines**: §11 (L126), 126
- **Types**: methodological, contextual
- **Excerpt**: «CAPTCHA en paginación DDG | Yahoo + visitas directas; después sesión con `vqd`.»

### C075 — Manejo de HTTP 202 y página anomaly
- **Section**, **Lines**: §11 (L127–128), 127–128
- **Types**: methodological, contextual
- **Excerpt**: «HTTP 202 y página “anomaly” | Pausa 7–10 s con jitter, backoff exponencial y cooldown.»

### C076 — Registro de carrosw como limitación
- **Section**, **Lines**: §11 (L129), 129
- **Types**: methodological, contextual
- **Excerpt**: «carrosw anti-bot | Registrado como limitación; no se falsificó su contenido.»

### C077 — Deduplicación por título, prefijo y dominio
- **Section**, **Lines**: §11 (L131), 131
- **Types**: methodological, contextual
- **Excerpt**: «Repetidos y mirrors | Deduplicación por título normalizado, prefijo y dominio.»

### C078 — Conclusión sobre marketplaces y categorías vacías
- **Section**, **Lines**: §12 (L135), 135
- **Types**: result, contextual
- **Excerpt**: «El mercado habanero tiene nueve marketplaces con inventario real y una docena con categorías vacías o solo piezas.»

### C079 — Registro automático de altas
- **Section**, **Lines**: §13 (L276), 276
- **Types**: contextual
- **Excerpt**: «El script `Auxiliares/herramientas/actualizar_informe.py` añade filas debajo del marcador y regenera el PDF.»

### C080 — Entradas omitidas en el registro
- **Section**, **Lines**: §13 (L295), 295
- **Types**: contextual
- **Excerpt**: «175 entradas adicionales no listadas / omitted»

### C081 — Sincronización de Revolico en partes
- **Section**, **Lines**: §14 (L756), 756
- **Types**: methodological
- **Excerpt**: «La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**. Cada 10 minutos un timer de systemd ejecuta `Auxiliares/herramientas/actualizar_revolico.py»»

### C082 — Última ejecución registrada de sincronización
- **Section**, **Lines**: §14 (L763), 763
- **Types**: result, contextual
- **Excerpt**: «2026-11-17T15:47:42+00:00 | 795373568 B | 48 partes de 16 MiB | `dadd2bffba615d8a…`»

### C083 — Detención manual del timer de scrapeo
- **Section**, **Lines**: §15 (L771), 771
- **Types**: result, contextual
- **Excerpt**: «se detuvo manualmente `revolico-scrape.timer` y su servicio a petición del usuario. El scraper había ampliado la BD de 3.682 a **6.332 anuncios** (520,6 MB) antes de detenerse»

### C084 — Renovación reciente de anuncios
- **Section**, **Lines**: §15 (L775), 775
- **Types**: result
- **Excerpt**: «El 99,3 % de los anuncios tiene `updated_on_by_user` en los últimos 7 días (mediana 1 día en los 189 autos)»

### C085 — Marcador `updatedOnToOrder` desactivado
- **Section**, **Lines**: §16 (L785), 785
- **Types**: methodological
- **Excerpt**: «El campo `updatedOnToOrder` del listado resultó ser un marcador de ranking y no de edición, así que el salto de descarga queda desactivado por defecto (`--skip-unchanged`)»

### C086 — Fuentes revisadas para requerimientos de fases 7–8
- **Section**, **Lines**: §17 (L793), 793
- **Types**: contextual
- **Excerpt**: «Fuentes académicas y repositorios revisados para definir los requerimientos del análisis (Fases 7-8):»

### C087 — Requerimientos derivados
- **Section**, **Lines**: §17 (L810), 810
- **Types**: methodological
- **Excerpt**: «La ponderación de preferencias del usuario y el producto interactivo quedan para la especialización futura.»

### C088 — Verificación en vivo de DfT/DVLA
- **Section**, **Lines**: §18 (L818), 818
- **Types**: citation-grounded
- **Excerpt**: «Verificado en vivo: publicado por Department for Transport + DVLA, actualizado 23/09/2026, Open Government Licence»

### C089 — VAHAN no accesible desde el entorno
- **Section**, **Lines**: §18 (L819), 819
- **Types**: contextual, citation-grounded
- **Excerpt**: «No accesible desde este entorno (error de transporte); el repo documenta 12 exportaciones mensuales 2025 y manifiesto de verificacion»

### C090 — BCC no accesible en vivo
- **Section**, **Lines**: §18 (L820), 820
- **Types**: contextual, citation-grounded
- **Excerpt**: «No accesible en vivo desde este entorno; citado en `Data/investigacion-mercado-automotor-cuba.md` y Resolución 102/2026»

### C091 — Redes sociales como fuente no estadística
- **Section**, **Lines**: §18 (L827), 827
- **Types**: contextual
- **Excerpt**: «No verificables como fuente estadística; requieren consentimiento y sin datos personales»

### C092 — Marco general de ocho pasos
- **Section**, **Lines**: §19 (L837–846), 837–846
- **Types**: contextual, methodological
- **Excerpt**: «Marco general (8 pasos, derivado de los trabajos revisados)»

### C093 — Fuentes de la adaptación a La Habana
- **Section**, **Lines**: §19 (L851), 851
- **Types**: result, contextual
- **Excerpt**: «Revolico (BD propia, 6.334 anuncios / 317 autos), concesionarios (Autocubana, Dongfeng, BDC One…), Gaceta/Decreto 163/2026, BCC (oficial) y elTOQUE (informal), salarios de la Resolución 14»

### C094 — Métodos adaptados del marco
- **Section**, **Lines**: §19 (L853), 853
- **Types**: methodological
- **Excerpt**: «comparables por modelo ±2 años y municipio; rentabilidad = reventa esperada − compra − reacondicionamiento − impuestos (Decreto 163/2026); asequibilidad = precio / salario; series con snapshots.»

### C095 — Activos existentes según el marco detallado
- **Section**, **Lines**: §20 (L873), 873
- **Types**: result, contextual
- **Excerpt**: «BD de 6.334 anuncios / 317 autos, esquema con 30 campos + auditoría, imágenes/teléfonos, snapshots de precios, normativa documentada, tasas y salarios referenciados, repositorios de modelos y dashboards.»

### C096 — Datos pendientes según el marco detallado
- **Section**, **Lines**: §20 (L875), 875
- **Types**: contextual
- **Excerpt**: «extracción estructurada de año/km/marca/modelo/combustible/transmisión desde `ad_json`/`apollo_full`; montos de costos ocultos; precios de transacción reales; estadísticas oficiales cubanas de parque y matriculaciones»

### C097 — Renombre de la fase 8
- **Section**, **Lines**: §21 (L883), 883
- **Types**: contextual
- **Excerpt**: «La fase 8 pasa a llamarse **Análisis de mercado, comparables y rentabilidad**.»

### C098 — Salidas del análisis descriptivo inicial
- **Section**, **Lines**: §22 (L892), 892
- **Types**: contextual
- **Excerpt**: «genera en `Data/analisis/`: `resumen_general.csv`, `precios_por_marca.csv`, `precios_por_municipio.csv`, `precios_por_anio.csv`, `outliers.csv`, `cobertura.csv`, `informe_descriptivo.md` y `dashboard.html`.»

### C099 — Resultados del análisis descriptivo inicial
- **Section**, **Lines**: §22 (L894), 894
- **Types**: result
- **Excerpt**: «Precio mediano **22.000 USD**, media 24.416,59 USD, IQR 11.375–35.000 USD, rango 600–95.000 USD.»

### C100 — Cobertura de campos derivados
- **Section**, **Lines**: §22 (L894), 894
- **Types**: result
- **Excerpt**: «Cobertura de campos derivados: marca 68,4 %, año 63,5 %, km 6,2 % (heurísticos, extraídos solo de título/descripción). Detectados 5 outliers por IQR.»

### C101 — Conversión diaria por año del vehículo
- **Section**, **Lines**: §23 (L902), 902
- **Types**: result, methodological
- **Excerpt**: «la conversión usa `precio_USD × TRMI elTOQUE` del día del anuncio (columna `Mediana` de `Anexos/Investigacion Cambios/trmi_USD.csv`)»

### C102 — Serie histórica de TRMI y precios
- **Section**, **Lines**: §23 (L904), 904
- **Types**: result
- **Excerpt**: «la TRMI pasó de 680 CUP/USD (09/07/2026) a 920 (16-17/11/2026); la mediana mensual CUP subió de 12,58 M (julio) a 20,7 M (noviembre).»

### C103 — Supuesto de anuncio activo
- **Section**, **Lines**: §23 (L903), 903
- **Types**: methodological
- **Excerpt**: «todos los registros tienen `status=PUBLISHED` y página verificada en la captura, por lo que se asume que son comprables; no se comprueba disponibilidad en tiempo real.»

### C104 — Generación de gráficas
- **Section**, **Lines**: §23 (L905), 905
- **Types**: contextual
- **Excerpt**: «usa matplotlib, seaborn y plotly (instalados) y genera 8 PNG + `dashboard_interactivo.html` en `Data/analisis/graficos/`.»

### C105 — Ausencia de campos estructurados en los JSON
- **Section**, **Lines**: §24 (L911), 911
- **Types**: result
- **Excerpt**: «**No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**: por eso `anio_est`, `marca_est` y `km_est` se derivan con regex del texto visible»

### C106 — Reporte de scrapeo y colas
- **Section**, **Lines**: §24 (L913), 913
- **Types**: result
- **Excerpt**: «`anuncios` 6.334 · `autos` 323 · `revision` 6.085 · `imagenes` 13.932 · `telefonos` 7.699 · BD 520,6 MB.»

### C107 — Reinicio automático del servicio
- **Section**, **Lines**: §25 (L920), 920
- **Types**: methodological
- **Excerpt**: «`revolico-scrape.service` ahora tiene `Restart=on-failure`, `RestartSec=30`, `StartLimitIntervalSec=300` y `StartLimitBurst=20`»

### C108 — Supuesto de disponibilidad de catálogos
- **Section**, **Lines**: §25 (L921), 921
- **Types**: methodological
- **Excerpt**: «Para concesionarios y páginas similares (`CATALOGOS`) se asume que todo el catálogo está disponible salvo que la página indique lo contrario y que se publicó el día de la captura (`fecha_publicacion = scraped_at`)»

### C109 — Causa del retraso en la clasificación
- **Section**, **Lines**: §26 (L928), 928
- **Types**: methodological
- **Excerpt**: «el timer ejecutaba `actualizar_revolico.py`, que solo corre el scraper y divide la BD, sin escribir nunca `autos`/`revision`.»

### C110 — Umbral de revisión de 4.000 anuncios
- **Section**, **Lines**: §27 (L943), 943
- **Types**: methodological
- **Excerpt**: «cuando `anuncios WHERE pagina_revisada=0`llega a **4.000** (configurable con `REVISAR_UMBRAL`), el aviso lanza `revolico-revisar.service`»

### C111 — Scraper de Telegram sin credenciales MTProto
- **Section**, **Lines**: §28 (L950), 950
- **Types**: contextual
- **Excerpt**: «No hay credenciales MTProto (`TELEGRAM_API_ID`/`TELEGRAM_API_HASH` vacías), así que se implementó `Auxiliares/herramientas/scraper_telegram_publico.py», que lee la vista pública `t.me/s/<canal>`»

### C112 — Primera corrida de Telegram
- **Section**, **Lines**: §28 (L952), 952
- **Types**: result
- **Excerpt**: «Corrida final (50 páginas): **152 mensajes**, **54 anuncios de autos** del canal `goldenbullbusinessfamilycars`, 45 con año detectable y **ninguno con precio explícito»»

### C113 — Base de datos de Telegram y descubrimiento de canales
- **Section**, **Lines**: §29 (L960, L966–971), 960–971
- **Types**: result
- **Excerpt**: «`canales` | 119» / «`anuncios` | 54» / «El descubrimiento usa 26 búsquedas en tgden.com y valida cada usuario con `t.me/s/`, filtrando por contexto cubano.»

### C114 — Modo de descubrimiento sin procesamiento
- **Section**, **Lines**: §32 (L995–1000), 995–1000
- **Types**: methodological
- **Excerpt**: «no hay descarga de anuncios, ni clasificación definitiva, ni inserción en `anuncios`/`autos`/`revision`»; «se detiene al llegar a `FECHA_MINIMA = 2021-01-01`»

### C115 — Parada por página sin enlaces nuevos
- **Section**, **Lines**: §33 (L1008), 1008
- **Types**: methodological
- **Excerpt**: «se detenga en cuanto una página no aporte **ningún enlace nuevo** (todos sus anuncios ya fueron vistos)»

### C116 — Mecanismo de la app Circuitos Habana
- **Section**, **Lines**: §35 (L1068–1074), 1068–1074
- **Types**: result, citation-grounded
- **Excerpt**: «La app **no usa una API privada**: hace scraping del canal público de Telegram `https://t.me/s/EmpresaElectricaDeLaHabana` con Jsoup y User-Agent de Chrome.»

### C117 — Restricciones de Docker y Overpass
- **Section**, **Lines**: §36 (L1084–1085), 1084–1085
- **Types**: contextual
- **Excerpt**: «el daemon Docker no arranca sin root en este entorno (`dockerd needs to be started with root privileges`), por lo que se descartó esa vía.»

### C118 — Optimización de pipelines y efecto medido
- **Section**, **Lines**: §37 (L1100–1102), 1100–1102
- **Types**: methodological, result
- **Excerpt**: «los anuncios de Revolico pasaron de 10.117 a **10.149** y los autos de 716 a **814**; quedan 3.351 URLs pendientes y 1.940 rechazadas.»

### C119 — Reporte automático de progreso
- **Section**, **Lines**: §38 (L1112), 1112
- **Types**: contextual
- **Excerpt**: «actualiza **`Data/progreso_reporte.md` cada 5 minutos** con:»

### C120 — Ampliación de límites de marketplaces
- **Section**, **Lines**: §39 (L1127), 1127
- **Types**: result
- **Excerpt**: «en minutos Autocubana pasó de 400 a **566** y Timbirichi de 110 a **170**, totalizando **2.121 anuncios**.»

## Iteration context — estado de F-V10-001..008

Evaluación descriptiva de las ocho observaciones transversales de `reviews/informe-tecnico-2026-11-27.forensic.md` (L991–1037) contra el texto de esta iteración. No se ha verificado el contenido de archivos externos: solo se cita lo que el documento declara.

- **F-V10-001 — KPIs, CSV y README (cuatro estados): PARCIALMENTE RESUELTA.** §59 (L1379) adopta 772 autos, 2.029 anuncios, 1.338 locales, 21.000 USD y 43.000 km, y L1381 incrusta marcadores `<!-- kpi:... -->` que se actualizan solos desde `kpis.csv`. Persisten §45 (L1214: 23.000 USD, 6,3 años, 34 marcas, 27 grupos), §58 (L1371: 2.014 anuncios, 44.125 km), §44 (L1206: 66 anomalías frente a 81) y el paralelo inglés de §59 (L1383: 744 autos, 2.014 anuncios).
- **F-V10-002 — Retirada de −5,43 % sin ablación ni literatura: PARCIALMENTE RESUELTA.** §59 (L1381) y §60 (L1389) explicitan la no significancia (p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05) y la registran en `MODELOS_Y_FUNCIONES.md`; §69 (L1469) declara el uso de IA. §34 (L1056) mantiene la cifra, §44 (L1206) la reutiliza con salvedad y §45 (L1214) sin ella; no hay ablación, test pareado ni contraste con los trabajos sobre no linealidad edad–precio.
- **F-V10-003 — Densidad sin declaración de IA: RESUELTA.** §69 (L1467–1471) añade declaración bilingüe de uso de IA para redacción, edición quirúrgica, revisión bibliográfica y auditoría, y nombra la skill `review` y los artefactos conservados. No detalla herramientas ni protocolo de supervisión.
- **F-V10-004 — TRMI diario frente a fijo, 920 frente a 930: PARCIALMENTE RESUELTA.** §23 (L902) incorpora la «Aclaración vigente»: el pipeline usa 930 CUP/USD fijos de `config.py` y la serie diaria es solo referencia histórica; §52 (L1297) coincide. L904 sigue reportando 920 sin registrar el cambio y el paralelo inglés (L907) continúa describiendo conversión con TRMI diaria.
- **F-V10-005 — Conclusión que niega la fase 8: PARCIALMENTE RESUELTA.** §12 español (L139) afirma la implementación y §2 (L38) añade nota de actualización; la tabla de §2 (L33) mantiene «Pendiente» mitigada por la nota. La Parte II conserva «not implemented yet» (L270) y la fase 8 «Pending» con producto interactivo (L164).
- **F-V10-006 — Diferenciación solo contra el repositorio egipcio: NO RESUELTA.** §34 (L1018, L1058–1060) sigue siendo el único pasaje comparativo, por escala de datos; §70 (L1477) añade cuatro referencias verificadas pero ningún contraste argumentativo con los vecinos académicos. El inventario registra una sola señal de novedad (C011, L1018).
- **F-V10-007 — Fuentes nominales incompletas y artefactos fuera del árbol: PARCIALMENTE RESUELTA.** §70 (L1477–1479) crea la convención de 38 referencias en `Data/referencias.md`, nombra cuatro verificadas y marca el resto como `(metadata incomplete)`; §69 (L1469) sitúa la auditoría en `reviews/`. Persisten la ausencia de citas numeradas en el cuerpo, el índice de gacetas en `~/Utilidades/Leyes/gaceta_catalog.json` (§10, L120) y la inaccesibilidad de VAHAN y BCC (§18, L819–820).
- **F-V10-008 — Muestra de 22 observaciones ausente del relato: RESUELTA.** §59 (L1381) declara 28 observaciones completas de 981 candidatas, R² 0,277 y p del F 0,411, con marcadores automáticos y referencia a `MODELOS_Y_FUNCIONES.md`; §60 (L1389) reitera la no significancia. La cifra sustituye a la omitida en la iteración 1 y queda dentro del relato.


## Apéndice C — Literatura

# Literature Map — iteración 2 (re-verificación dirigida)

Nota de entrada. El plan aprobado (`informe-tecnico-2026-11-27-iter2.plan.md`) declara `preset: Standard`, pide re-ejecutar E2 y comprobar las observaciones de la pasada 1, pero no contiene `queries_planned` ni `hypotheses_planned`. En consecuencia: (a) las consultas se derivaron del mandato recibido —comprobar si la nueva §70 y `Data/referencias.md` resolvieron los `(metadata incomplete)` de la pasada 1— y no son búsquedas temáticas nuevas; (b) el mapa completo de 38 trabajos sigue vigente en `reviews/informe-tecnico-2026-11-27.e2-literature.md` y aquí solo se re-verifican las 6 entradas marcadas más las 3 fuentes institucionales invocadas en §70; (c) los IDs `P` continúan la convención dentro de este artefacto, no la del mapa anterior; (d) `Cited in document` se determina por mención nominal en el cuerpo del informe, mientras que `In document bibliography` significa «presente en `Data/referencias.md`», anexo enlazado desde §70. Toda la metadata fue consultada en vivo el 2026-11-27; lo que no pudo confirmarse se marca explícitamente.

## Clusters

### Cluster 1 — Entradas con `(metadata incomplete)` heredadas de la pasada 1

**Query**: consultas directas por DOI y por identificador: `10.2307/1879431`, `10.1016/j.cie.2026.111964`, `arXiv:2403.03812`, `arXiv:1711.06970`, `arXiv:2101.03788`, `10.1016/j.ijpe.2015.02.006` (OpenAlex, Crossref y arXiv API).

#### P001 — The Market for "Lemons": Quality Uncertainty and the Market Mechanism
- **Authors**: Akerlof, G. A.
- **Year**: 1970
- **Venue**: The Quarterly Journal of Economics
- **Citations**: 32658 (source: OpenAlex, fetched 2026-11-27T21:02Z; Crossref devolvió HTTP 429 y no pudo contrastarse en esta pasada)
- **URL**: https://doi.org/10.2307/1879431
- **Layer**: L2
- **Cited in document**: yes (§17, §19, §20 y ahora §70)
- **Document reference**: [1] en `Data/referencias.md`
- **source_of_metadata**: OpenAlex W2156109180 (registro completo, actualizado 2026-11-27T09:11Z)
- **Abstract analysis**: El registro confirma DOI, autor con ORCID, revista, volumen 84(3), páginas 488–500 y fecha 1970-08-01. El campo `abstract_inverted_index` sigue conteniendo únicamente el índice de secciones («I. Introduction, 488. — II. The model with automobiles as an example, 489. — III. Examples and applications, 492. ...»), no un resumen sustantivo: es exactamente el motivo del flag original y **no ha cambiado** entre pasadas.
- **Estado del flag**: **no resuelto en su motivo**, aunque los campos bibliográficos están completos y verificados. `Data/referencias.md` [1] conserva `(metadata incomplete)` sin indicar qué campo falta, mientras §70 lo enumera entre las «referencias citadas y verificadas externamente»: ambas afirmaciones solo se reconcilian si se entiende que el flag alude al resumen, no a la identidad de la obra.

#### P002 — The pricing of used electric vehicles via machine learning and hedonic price model: A comparative study
- **Authors**: Kang, W.; Fu, X.
- **Year**: 2026
- **Venue**: Computers & Industrial Engineering
- **Citations**: 3 (source: OpenAlex, fetched 2026-11-27T21:02Z; 2 en la pasada 1)
- **URL**: https://doi.org/10.1016/j.cie.2026.111964
- **Layer**: L2
- **Cited in document**: no
- **Document reference**: [10] en `Data/referencias.md`
- **source_of_metadata**: OpenAlex W7134932779 (actualizado 2026-11-27T09:11Z)
- **Abstract analysis**: El registro confirma título, autores con ORCID, afiliación (Hangzhou Dianzi University), revista, volumen 216, artículo 111964, fecha 2026-03-11 y 3 citas. `abstract_inverted_index` es `null`: el resumen **sigue sin indexarse**, que era el motivo original del flag. Las palabras clave del registro (hedonic pricing, vehicle depreciation, model interpretability) permiten caracterizar el tema, pero no sustituyen al resumen del autor.
- **Estado del flag**: **no resuelto en su motivo**; verificables en vivo todos los demás campos. No verificable: el resumen.

#### P003 — ProbSAINT: Probabilistic Tabular Regression for Used Car Pricing
- **Authors**: Madhusudhanan, K.; Behrens, G.; Stubbemann, M.; Schmidt-Thieme, L.
- **Year**: 2024
- **Venue**: arXiv:2403.03812; versión publicada en IEEE International Conference on Big Data (BigData), Industry & Government Track
- **Citations**: 13 (source: OpenAlex, fetched 2026-11-27T21:03Z; Semantic Scholar devolvió HTTP 403 otra vez)
- **URL**: https://arxiv.org/abs/2403.03812 · https://doi.org/10.1109/bigdata62323.2024.10825740
- **Layer**: L2
- **Cited in document**: no
- **Document reference**: [18] en `Data/referencias.md`
- **source_of_metadata**: arXiv API (verificado 2026-11-27T21:02Z) + OpenAlex W4406461714 (versión publicada)
- **Abstract analysis**: La API de arXiv confirma título, los cuatro autores, fecha 2024-03-06, `journal_ref` IEEE BigData 2024 y resumen completo. La pasada 1 marcó `(metadata incomplete)` porque el conteo de citas era desconocido y Semantic Scholar respondía 403; en esta pasada OpenAlex expone la versión publicada con DOI IEEE y **13 citas**, de modo que el dato antes no verificable ahora sí lo es. No se realizó lectura de texto completo en esta iteración (`papers_l3: 0`); el análisis L2 se mantiene vigente.
- **Estado del flag**: **resuelto en vivo pero no reflejado**: [18] sigue con `(metadata incomplete)` y solo la URL de arXiv, sin el DOI publicado ni el conteo recuperado.

#### P004 — How much is my car worth? A methodology for predicting used cars prices using Random Forest
- **Authors**: Pal, N.; Arora, P.; Sundararaman, D.; Kohli, P.; Palakurthy, S. S.
- **Year**: 2017 (preprint arXiv); 2018 (versión publicada en Springer)
- **Venue**: arXiv:1711.06970 (FICC Camera Ready); Advances in Intelligent Systems and Computing (Springer), pp. 413–422
- **Citations**: 96 (source: OpenAlex, fetched 2026-11-27T21:04Z; versión publicada W2770052903)
- **URL**: https://arxiv.org/abs/1711.06970 · https://doi.org/10.1007/978-3-030-03402-3_28
- **Layer**: L2
- **Cited in document**: no
- **Document reference**: [19] en `Data/referencias.md`
- **source_of_metadata**: arXiv API (verificado 2026-11-27T21:02Z) + OpenAlex W2770052903 (verificado 2026-11-27T21:05Z)
- **Abstract analysis**: La API de arXiv confirma título, los cinco autores, fecha 2017-11-19, comentario «FICC Camera Ready» y resumen completo (Random Forest de 500 árboles; exactitud 95,82 % entrenamiento y 83,63 % prueba). OpenAlex vincula el mismo preprint con su versión publicada de 2018 y confirma que los cinco autores coinciden uno a uno, con **96 citas**. El conteo que la pasada 1 declaró no verificable por 403 de Semantic Scholar es, por tanto, verificable por otra vía.
- **Estado del flag**: **resuelto en vivo pero no reflejado**: [19] mantiene `(metadata incomplete)`, el año 2017 y solo la URL de arXiv. Queda una discrepancia de año no documentada entre preprint (2017) y publicación (2018).

#### P005 — Second Hand Price Prediction for Tesla Vehicles
- **Authors**: Arefin, S. E.
- **Year**: 2021
- **Venue**: arXiv:2101.03788
- **Citations**: 9 (source: OpenAlex, fetched 2026-11-27T21:04Z; registro W3120241027 con DOI 10.48550/arxiv.2101.03788)
- **URL**: https://arxiv.org/abs/2101.03788
- **Layer**: L2
- **Cited in document**: no
- **Document reference**: [20] en `Data/referencias.md`
- **source_of_metadata**: arXiv API (verificado 2026-11-27T21:02Z) + OpenAlex W3120241027
- **Abstract analysis**: La API de arXiv confirma título, autor (Sayed Erfan Arefin), fecha 2021-01-11 y resumen completo (comparación de árboles de decisión, SVM, Random Forest y deep learning, implementación final con boosted decision tree regression). OpenAlex añade el conteo de **9 citas**. Como en P003 y P004, el dato antes no verificable se recuperó sin Semantic Scholar.
- **Estado del flag**: **resuelto en vivo pero no reflejado**: [20] sigue marcado `(metadata incomplete)` sin el conteo.

#### P006 — Market prices of remanufactured, used and new items: Evidence from eBay
- **Authors**: Quariguasi Frota Neto, J.; Bloemhof-Ruwaard, J. M.; Corbett, C. J.
- **Year**: 2015 (OpenAlex) / publicación impresa 2016 (Crossref)
- **Venue**: International Journal of Production Economics, vol. 171, parte 3, pp. 371–380
- **Citations**: 136 (source: OpenAlex, fetched 2026-11-27T21:03Z); 107 (source: Crossref `is-referenced-by-count`, fetched 2026-11-27T21:02Z)
- **URL**: https://doi.org/10.1016/j.ijpe.2015.02.006
- **Layer**: L2
- **Cited in document**: no
- **Document reference**: [38] en `Data/referencias.md`
- **source_of_metadata**: OpenAlex W1991842457 + Crossref (ambos verificados en vivo)
- **Abstract analysis**: OpenAlex y Crossref confirman título, los tres autores, revista, volumen, páginas y DOI; OpenAlex additionally expone texto completo en acceso verde vía Universidad de Manchester, aunque `abstract_inverted_index` es `null`. En la pasada 1 esta obra (P038) figuraba con 136 citas verificadas y **sin** flag; el marker aparece por primera vez en `Data/referencias.md` [38] y no se corresponde con ninguna pérdida de metadata entre iteraciones.
- **Estado del flag**: **introducido en la iteración 2 sin justificación explícita**. La causa plausible es el resumen no indexado en OpenAlex, pero la ficha no lo dice y existe texto completo accesible. Queda además una discrepancia de año (2015 en OpenAlex y en la ficha; 2016 en el campo `published-print` de Crossref) no consignada en `[38]`.

### Cluster 2 — Fuentes institucionales declaradas como verificadas en la nueva §70

**Query**: fetch directo a las páginas oficiales de ANFAC, AEADE y DVLA/GOV.UK; un `WebSearch` complementario falló a nivel de proveedor.

#### P007 — ANFAC — Asociación Española de Fabricantes de Automóviles y Camiones
- **Authors**: n/a (organización)
- **Year**: n/a (datos vigentes 2026; cifras del ejercicio 2025 en la portada)
- **Venue**: sitio oficial https://www.anfac.com/
- **Citations**: n/a
- **URL**: https://www.anfac.com/
- **Layer**: L1
- **Cited in document**: yes (§70, como «informes del sector automotriz español»)
- **Document reference**: sin número; mención nominal en §70
- **source_of_metadata**: fetch directo verificado 2026-11-27T21:06Z
- **Abstract analysis**: La portada oficial expone «Notas de matriculación», «Cifras clave — Matriculaciones Turismos y Todoterreno», «El sector del Automóvil en España — Cifras del año 2025» y un bloque de matriculaciones de octubre de 2026. La afirmación de §70 sobre estadísticas del sector automotriz español es verificable en vivo y coincide con la descripción del documento.

#### P008 — AEADE — Asociación de Empresas Automotrices del Ecuador
- **Authors**: n/a (organización)
- **Year**: n/a (datos Ene–sep 2026 en la portada)
- **Venue**: sitio oficial https://www.aeade.net/
- **Citations**: n/a
- **URL**: https://www.aeade.net/
- **Layer**: L1
- **Cited in document**: yes (§70, como «estadísticas de matriculaciones»)
- **Document reference**: sin número; mención nominal en §70
- **source_of_metadata**: fetch directo verificado 2026-11-27T21:06Z
- **Abstract analysis**: La portada oficial ofrece «Estadísticas: Anuarios, Boletines de prensa: venta de vehículos, Boletín de facturación del sector automotor» y cuadros de importación, exportación y ventas Ene–sep 2026. La fuente existe y publica lo que §70 afirma. Precisión de atribución: se trata de la asociación **ecuatoriana**, no española; §70 no asigna país, pero el lector de la versión española podría inferirlo del contexto de ANFAC.

#### P009 — DVLA / Department for Transport — Vehicle licensing statistics
- **Authors**: n/a (organismo)
- **Year**: n/a (último conjunto de datos anunciado: 23/09/2026)
- **Venue**: GOV.UK, página oficial de DVLA
- **Citations**: n/a
- **URL**: https://www.gov.uk/government/organisations/driver-and-vehicle-licensing-agency
- **Layer**: L1
- **Cited in document**: yes (§70, como «estadísticas de vehículos»)
- **Document reference**: sin número; mención nominal en §70
- **source_of_metadata**: fetch directo verificado 2026-11-27T21:09Z
- **Abstract analysis**: La página oficial confirma que DVLA es una agencia ejecutiva patrocinada por el Department for Transport, mantiene registros de 48 millones de vehículos en el Reino Unido y publica «Vehicle licensing statistics data files» (23/09/2026) bajo «Research and statistics». La afirmación general de §70 queda verificada a nivel de organismo y de serie estadística. No verificable en esta pasada: la URL concreta de la colección «vehicle statistics» (tres intentos de URL directa devolvieron 404) y el `WebSearch` de apoyo falló; por eso la cita no puede darse con enlace profundo confirmado.

## Recency distribution

La tabla considera solo las 6 entradas bibliográficas re-verificadas (P001–P006); las fuentes institucionales P007–P009 no tienen año bibliográfico asignable. «In document bibliography» = presente en `Data/referencias.md`, no mencionada en el cuerpo del informe.

| Year | In map | In document bibliography |
|---|---:|---:|
| 2026 | 1 | 1 |
| 2025 | 0 | 0 |
| 2024 | 1 | 1 |
| 2023 | 0 | 0 |
| 2022 | 0 | 0 |
| ≤2021 | 4 | 4 |

## Venue distribution

| Venue | Count in map |
|---|---:|
| The Quarterly Journal of Economics | 1 |
| Computers & Industrial Engineering | 1 |
| arXiv:2403.03812 / IEEE BigData 2024 | 1 |
| arXiv:1711.06970 / Springer FICC 2018 | 1 |
| arXiv:2101.03788 | 1 |
| International Journal of Production Economics | 1 |

## Likely missing important works

Sin cambios respecto al mapa de la pasada 1: se mantienen las entradas P002 (Lewis), P004 (Englmaier et al.), P014 (Gegić et al.), P021 (Krotov et al.), P023 (Priestley et al.), P022 (Brown et al.), P033 (Guerra) y P024 (Hohensinner et al.) con sus identificadores originales en `reviews/informe-tecnico-2026-11-27.e2-literature.md`. La iteración 2 se limitó a la re-verificación de metadata; no se ejecutaron búsquedas temáticas que permitan proponer obras nuevas sin inventar evidencia.

## Hypothesis checks (from plan)

El plan no declara hipótesis. Las dos comprobaciones siguientes se derivan del mandato de esta iteración y son observaciones sin veredicto.

### H1 — Los `(metadata incomplete)` de la pasada 1 quedaron resueltos por la §70 y `Data/referencias.md` (derivada)

Estado de la evidencia: de los cinco flags heredados, **ninguno fue retirado**. Tres (P003, P004, P005) tenían un único motivo —conteo de citas no verificable por HTTP 403 de Semantic Scholar— que en esta pasada sí se resolvió por OpenAlex (13, 96 y 9 citas respectivamente), pero `Data/referencias.md` no incorporó ni los conteos ni las versiones publicadas con DOI; los marcadores siguen ahí. Dos (P001, P002) conservan su motivo original: el resumen de Akerlof sigue siendo un índice de secciones y el de Kang & Fu sigue sin indexarse. En paralelo apareció un sexto flag, P006 [38], que en la pasada 1 estaba verificado y ahora se marca sin explicación. Lo que sí cambió es la presentación: existe por primera vez una lista numerada de 38 referencias y la §70 distingue cuatro fuentes como verificadas. Es decir, mejoró la transparencia formal, no la completitud de los campos señalados. Para que V5/V8 puedan confiar o descontar cada entrada, el marker debería ser por campo —por ejemplo `(metadata incomplete: resumen no indexado)`— y no una etiqueta genérica.

### H2 — La §70 presenta como «verificadas» referencias que `Data/referencias.md` sigue marcando como incompletas (derivada)

Observación: Akerlof aparece simultáneamente en §70 como referencia «verificada externamente (Crossref/OpenAlex)» y en `[1]` como `(metadata incomplete)`. En esta pasada OpenAlex confirmó todos los campos bibliográficos (Crossref devolvió 429), por lo que la parte OpenAlex de la afirmación es verificable y la parte Crossref no pudo contrastarse. Las fuentes institucionales ANFAC, AEADE y DVLA/GOV.UK sí se verificaron en vivo a nivel de organismo; la de DVLA no pudo enlazarse a una URL profunda concreta. No hay evidencia de que la contradicción entre §70 y `[1]` sea intencional; el estado de la evidencia es ambiguo porque la ficha no especifica qué campo está incompleto.

## Sources used

- WebSearch queries: 1 (falló a nivel de proveedor; mismo comportamiento que la pasada 1).
- WebFetch URLs: 21 = 2 Crossref + 7 OpenAlex + 3 Semantic Scholar + 3 arXiv + 6 páginas institucionales.
- Semantic Scholar API hits: 0 (HTTP 403 en las 3 consultas por ID de arXiv).
- OpenAlex API hits: 20 registros devueltos en 7 consultas (búsqueda por DOI, por ID y por título).
- Crossref API hits: 1 registro (Quariguasi Frota Neto); 1 consulta con HTTP 429 (Akerlof).
- arXiv API hits: 3 registros (uno por ID de arXiv).
- Landing pages institucionales: 3 verificadas (ANFAC, AEADE, DVLA/GOV.UK) y 3 URL de GOV.UK con HTTP 404.
- Degradación: `degraded: false` — las 6 entradas marcadas se re-verificaron y 9 fuentes entraron en el mapa. No verificable en esta pasada: el conteo de citas vía Semantic Scholar (403), la confirmación Crossref de Akerlof (429), el resumen de Kang & Fu (no indexado), el resumen sustantivo de Akerlof (índice de secciones), la URL profunda de la colección de estadísticas de vehículos de GOV.UK (404) y cualquier obra nueva propuesta por búsqueda temática (proveedor de WebSearch no disponible).


## Apéndice D — Artefactos

# Artifact Inventory

Iteración 2. A diferencia de la iteración 1, en esta pasada sí se dispuso del repositorio local (`repo_path` efectivo: `/home/thony70807/Proyectos/El precio de moverse en Cuba`), por lo que la sección Repository se verificó en disco con `git` y `find`. Las path declaradas en el documento se contrastaron con el árbol real; cuando una ruta citada no existe se indica expresamente.

## Repository

- **URL**: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba
- **Clone status**: success (checkout local existente, 190 commits; no se realizó un clonado nuevo)
- **Languages**: Python: 41.689 LOC propias (excluye `.venv*`, `Auxiliares/Repositorios Referencias`, `Copias`, `site`); Markdown: 59.110 LOC en todo el repo, de las cuales 2.456 LOC en `docs/`; HTML: panel autocontenido y 6 gráficos Plotly (ver Figures)
- **Commits**: 190
- **Authors**: CarlosAntonioAceaJimenezCD <CarlosAntonioAceaJimenezCD@users.noreply.github.com>
- **First commit**: 2026-11-17
- **Last commit**: 2026-11-27 (`99c7065 viz: refrescar panel con el ultimo estado de circuitos`)
- **Default branch**: main
- **Git LFS**: 157 objetos referenciados (`*.sqlite`, `*.bin` de chunks) según `.gitattributes`; `Data/PROGRESO_PUSH.md` (20:58 UTC) informa 175 objetos en disco y `origin/main` en `99c7065`

### Structure

```tree
./
├── Anexos/                  # Investigacion Cambios, Investigacion Combustible
├── Auxiliares/              # cache, herramientas (scripts propios), Repositorios Referencias, .venv*
├── Copias/                  # 4 repos de referencia (excluidos por decisión del §3)
├── Data/                    # investigaciones y bases por tienda
│   ├── analisis/            # 8 PNG + dashboards descriptivos
│   ├── analisis_rentabilidad/  # config.py, scripts/, sql/, data/, outputs/{charts,tables}/, *.md
│   ├── Revolico/            # revolico.sqlite, pipeline.sqlite, chunks/, partes/
│   ├── mapas/               # mapa_ofline.html, circuitos/, CSV de infraestructura
│   ├── fuentes-oficiales/   # anuarios ONEI, series_oficiales.csv
│   ├── repos-autos-referencias/  # referencias_autos.sqlite
│   └── dashboard.html       # panel interactivo autocontenido (nuevo en la iteración 2)
├── docs/                    # historia, referencia, guias, fuentes, graficos/, dashboard.html
├── Hombros/                 # 01_PDFs … 06_Calidad_precio_mercado
├── reviews/                 # informe + forensic iteración 1, 13 artefactos de fase, plan iter2
├── site/                    # salida MkDocs (ignorada por Git)
├── INFORME_TECNICO.md / .pdf, README.md, requirements.txt, mkdocs.yml
└── .playground/audit-cache/ # cachés de texto de las iteraciones 26/27 y 27-iter2
```

### Entry points

| Path | LOC | Args documented | Notes |
|---|---|---|---|
| `Data/analisis_rentabilidad/scripts/run_all.py` | 45 | no | Orquestador; docstring «Cada etapa es reanudable e idempotente»; invoca las 5 etapas y los generadores de KPI, dashboard y Parquet. |
| `Data/analisis_rentabilidad/scripts/01_ingest.py` | 409 | no | Ingesta Revolico + concesionarios + marketplaces → Parquet. |
| `Data/analisis_rentabilidad/scripts/02_clean.py` | 57 | no | Limpieza y features. |
| `Data/analisis_rentabilidad/scripts/03_eda.py` | 80 | no | KPIs y 6 gráficos Plotly HTML. |
| `Data/analisis_rentabilidad/scripts/04_stats.py` | 133 | no | OLS, VIF, Kruskal-Wallis, anomalías; escribe `modelo_muestra.csv` y `modelo_resumen.txt`. |
| `Data/analisis_rentabilidad/scripts/05_benchmark.py` | 67 | no | Benchmark por marca/modelo/año e infravalorados. |
| `Auxiliares/herramientas/actualizar_informe.py` | 416 | yes | Docstring con `Uso:`, `--inicializar` y `--regenerar`; registro de altas y regeneración del PDF. |
| `Auxiliares/herramientas/generar_dashboard.py` | 402 | no | Genera `Data/dashboard.html` sin CDN; invocado por `run_all.py`, el job de circuitos y `sitio_build.sh`. |
| `Auxiliares/herramientas/actualizar_numeros.py` | 153 | no | Actualiza los marcadores `<!-- kpi:… -->` del informe (§59). |
| `Auxiliares/herramientas/generar_sitio_mkdocs.py` | 242 | no | Regenera `docs/` y copia los gráficos y el dashboard. |

### Tests

- Files: `Auxiliares/herramientas/test_dashboard.py` (92 LOC), `Auxiliares/herramientas/test_parquet_compacto.py` (83 LOC), `Auxiliares/herramientas/test_modelo.py` (84 LOC)
- Total LOC: 259
- Framework: scripts (no usan `pytest`; no hay `pytest.ini`/`conftest.py` propios; se ejecutan con `Auxiliares/.venv-py/bin/python …`)
- Tests cover (named): `test_modelo.py` verifica el esquema y la coherencia de `modelo_muestra.csv`, los coeficientes legacy, la ausencia de afirmaciones de depreciación significativa y la idempotencia de `04_stats.py`; además hay suites de tests en repositorios de referencia (`Auxiliares/Repositorios Referencias/…/tests/`), ajenas al código propio.

### Documentation

| File | LOC |
|---|---|
| README.md | 105 |
| INFORME_TECNICO.md | 1.484 (la caché de texto de la iteración 2 tiene 1.481) |
| docs/ (32 archivos) | 2.456 LOC en Markdown + 6 HTML de gráficos + `dashboard.html` |
| Data/referencias.md | 82 (38 referencias numeradas) |
| reviews/ (19 archivos) | informe y forensic de la iteración 1, 13 artefactos de fase, y plan + artefactos e1/e2/e3 de la iteración 2 |

### Environment

- requirements.txt: present, 12 líneas útiles (pandas, numpy, plotly, statsmodels, scipy, beautifulsoup4, curl_cffi, tenacity, trafilatura, pyarrow, mkdocs, mkdocs-material)
- pyproject.toml: absent
- environment.yml: absent
- Dockerfile: absent (FlareSolverr se declara como servicio Docker externo en §6)
- Other: `.gitattributes` con filtros LFS; `mkdocs.yml`; `Auxiliares/.venv` y `Auxiliares/.venv-py`; `Auxiliares/herramientas/integraciones/README.md`; systemd timers (`precio-*`, `revolico-*`) documentados fuera del repo

### Heavy artifacts in repo

| Path | Size | Type |
|---|---|---|
| `Data/Revolico/revolico.sqlite` | 834,5 MB | sqlite (LFS) |
| `Data/Revolico/pipeline.sqlite` | 736,2 MB | sqlite (LFS) |
| `Data/catalogos_concesionarios/bdc_one.sqlite` | 73,3 MB | sqlite |
| `Data/catalogos_concesionarios/changan.sqlite` | 57,5 MB | sqlite |
| `Data/catalogos_concesionarios/marketplaces/autocubana.sqlite` | 56,2 MB | sqlite |
| `Data/catalogos_concesionarios/marketplaces/itencel.sqlite` | 56,1 MB | sqlite |
| `Data/analisis_rentabilidad/data/compacto/anuncios/year=2026/month=11/parte-000.parquet` | 24,0 MB | parquet |
| `Hombros/01_PDFs/PDF EY Highlights Automotive 2025__2e4f0d88.pdf` | 14,8 MB | pdf |
| `Data/fuentes-oficiales/ONEI/Anuario_Estadistico_2023/Archivo/aec-2023.rar` | 14,0 MB | rar |

## Datasets

| Name | Source | ID | Publicly accessible | Notes |
|---|---|---|---|---|
| Revolico scraped ads database | custom (own scrape) | `Data/Revolico/revolico.sqlite` | unknown | §14/§54: no se versiona como archivo único (chunks LFS); §66 reporta 6.955 anuncios `done`. |
| Revolico pipeline queues | custom | `Data/Revolico/pipeline.sqlite` | unknown | §16, §24, §30: colas `url_queue`, `download_queue`, `process_queue`. |
| Dealer and marketplace catalogues | custom | `Data/catalogos_concesionarios/` | unknown | §9: 11 bases y 256 filas; §30: bajo Git LFS. |
| Telegram public-channel database | custom | `Data/integraciones/telegram/telegram.sqlite` | unknown | §28–§29: `canales` 119, `anuncios` 54. |
| ONEI statistical yearbooks 2014–2025 | official (ONEI Cuba) | `Data/fuentes-oficiales/ONEI/` | yes | §53: 12 anuarios, 233 archivos (§56); `series_oficiales.csv` (§56). |
| UK DfT/DVLA vehicle statistics | official | gov.uk/…/vehicle-licensing-statistics-data-files | yes | §18: verificado en vivo, Open Government Licence. |
| VAHAN (India, MoRTH) | official | no ID declarado | no | §18: «No accesible desde este entorno (error de transporte)». |
| BCC exchange rates | official | `https://api.bc.gob.cu/v1/tasas-de-cambio/activas` | no | §52/§18: API declarada pero no accesible en vivo desde el entorno. |
| elTOQUE TRMI | non-official | `Anexos/Investigacion Cambios/trmi_USD.csv` | unknown | §23/§52: serie diaria de referencia; el modelo usa TRMI fija 930 CUP/USD de `config.py`. |
| UCI Automobile / CarDekho (Kaggle) | UCI / Kaggle | not declared in document | unknown | §18: referencias metodológicas, no precios cubanos reales. |
| PUCE used-vehicle survey | academic | `Hombros/01_PDFs/…73e1773e.pdf` | unknown | §17: 130 comerciantes; base de la clasificación de calidad ≤5 años. |
| Consolidated reference-repository tables | custom (derived) | `Data/repos-autos-referencias/referencias_autos.sqlite` | unknown | §50: 25 tablas, 3.958 anuncios, encuestas y entrevistas. |
| Fuel price series | custom | `Data/combustible/precios_combustible.sqlite` | unknown | §41: 18 observaciones (20/08–18/11/2026). |
| OSM/Overpass geodata | OpenStreetMap | `Data/mapas/gasolineras.csv` | yes | §41/§42: 137 gasolineras. |
| EV charging references | marketplace/directory | `Data/mapas/estaciones_carga.csv` | unknown | §41: 12 referencias (9 con coordenadas). |
| Circuitos Habana APK extracts | custom (APK decompilation) | `Data/mapas/circuitos/` | unknown | §62: 2.473 puntos, 244 circuitos, 166 polígonos. |
| Profitability-model sample (**new**) | derivado del pipeline | `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` | yes (en repo) | Detalle en New artifacts; respalda las cifras del modelo en §59. |
| Numbered reference list (**new**) | bibliographic (OpenAlex/Crossref) | `Data/referencias.md` | yes (en repo) | 38 entradas; detalle en New artifacts y §70. |

## New artifacts (iteración 2)

Inventario explícito de los cuatro artefactos señalados por el coordinador, contrastados en disco.

### `Data/referencias.md` — referenced in §70

- **Found in repo**: yes — 9.634 B, 82 líneas, 38 entradas numeradas `[1]`…`[38]`; generado el 27/11/2026 desde `reviews/informe-tecnico-2026-11-27.e2-literature.md`.
- **Content**: una línea por referencia con autores, título, revista, año, DOI/URL, campo `Citada en el informe: yes/no` y marca `(metadata incomplete)` cuando algún metadato no se confirmó (aparece en [1], [10] y [38] entre otras).
- **Claims supported (preliminary)**: §70 «La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`»; el propio §70 distingue cuatro referencias verificadas en vivo (Akerlof 1970, DfT/DVLA, ANFAC, AEADE) del resto.
- **Observation**: las cuatro fuentes verificadas que nombra §70 no se distinguen dentro de `referencias.md` mediante una etiqueta positiva explícita — solo aparece la marca negativa `(metadata incomplete)` —, por lo que la condición de «verificadas» debe cotejarse con `e2-literature.md`, como el propio §70 indica.

### `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` — backs §59

- **Found in repo**: yes — 265 B, cabecera + 2 filas; columnas `modelo,candidatas,observaciones,r2,p_f,terminos`.
- **Content**: `principal`: 981 candidatas / 584 observaciones / R² 0,101 / p_f 0,0; `completo`: 981 candidatas / 28 observaciones / R² 0,2744 / p_f 0,4114; términos `log_price ~ car_age + np.log1p(mileage_km) + condition_score + C(brand_tier)` y la variante con `hp`.
- **Claims supported (preliminary)**: §59 «28 observaciones completas» de «981 candidatas», R² 0,277 y p del F 0,411; coincides en observaciones, candidatas y p, aunque el R² archivado es 0,2744.
- **Observation**: existen tres estados distintos del mismo artefacto en el repositorio. `MODELOS_Y_FUNCIONES.md` (56) y sus copias en `docs/referencia/modelos.md` y `PRESENTACION_STORYTELLING.md` (257) describen 572/22 observaciones de 897 candidatas (R² 0,106 / 0,277; p 0,623), cifras que ya no coinciden con el CSV actual; el plan de esta iteración (línea 20) repite 572/22; en cambio §59 y el CSV coinciden en 28/981. El test `test_modelo.py` comprueba la estructura y la coherencia interna del CSV, no la igualdad con esas cifras documentadas.
- **Companion outputs**: `modelo_depreciacion.csv` (423 B), `modelo_resumen.txt` (2.621 B, OLS de 28 observaciones, R² 0,274, p del F 0,411), `vif.csv` (85 B), `tests.csv` (67 B), `kpis.csv` (285 B).

### `reviews/` — audit artifacts cited in §69–§70

- **Found in repo**: yes — 19 archivos `.md` al cierre de este inventario. Los trece artefactos de fase que §69 denomina «los trece artefactos de fase» están presentes: `informe-tecnico-2026-11-27.plan.md`, `.e1-claims.md`, `.e2-literature.md`, `.e3-artifacts.md`, `.v1-structure.md`, `.v2-methodology.md`, `.v3-results-evidence.md`, `.v4-novelty.md`, `.v5-state-of-the-art.md`, `.v6-reproducibility.md`, `.v7-writing.md`, `.v8-bibliography.md` y `.v9-ethics.md`.
- **Also present**: `informe-tecnico-2026-11-27.md` (45,6 KB), `.forensic.md` (343 KB) y, de la iteración 2, `informe-tecnico-2026-11-27-iter2.plan.md` (1,2 KB) junto con los artefactos `…iter2.e1-claims.md`, `…iter2.e2-literature.md` y este `…iter2.e3-artifacts.md`, escritos en paralelo durante la auditoría.
- **Claims supported (preliminary)**: §69 «sus resultados se conservan en `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` junto con los trece artefactos de fase»; §70 « Las fuentes restantes figuran con estado `(metadata incomplete)` en `reviews/informe-tecnico-2026-11-27.e2-literature.md`».
- **Observation**: las rutas citadas existen y el conteo de artefactos de fase es correcto. El informe narrativo y el expediente forensic de la iteración 2 aún no eran visibles al cerrar este inventario; la afirmación de §69 sobre «los trece artefactos» se refiere a la iteración 1, no a la 2.

### Panel interactivo — `Data/dashboard.html`

- **Found in repo**: yes — 109.929 B, título «Panel interactivo — El precio de moverse en Cuba», actualizado el 27/11/2026 (commit `99c7065`); copia en `docs/dashboard.html` (109.970 B); generado por `Auxiliares/herramientas/generar_dashboard.py` (402 LOC).
- **Type**: HTML autocontenido (vanilla JS + SVG, sin CDN ni peticiones externas) con gráficos, mapa de servicios y mapa de circuitos; fecha derivada de los datos para idempotencia.
- **Rendered in document**: no (el texto cacheado no lo incrusta ni lo nombra por esa ruta; §22/§23 citan `Data/analisis/dashboard.html` y `Data/analisis/graficos/dashboard_interactivo.html`, y §59 describe un «apéndice visual con cinco cuadros y seis gráficos reales»).
- **Documented outside the report**: `Data/AUTOMATIZACION.md`, apartado «Panel interactivo autocontenido»: un solo archivo de ~107 KB en lugar de los 6 HTML de Plotly (168 KB) más ~4,5 MB de JavaScript remoto por visita; funciona por `file://` y en 3G.
- **Claims supported (preliminary)**: «dashboard de mercado» y «entrega y monitoreo» (§17–§20), visualización de los KPIs y del estado de circuitos; probado por `Auxiliares/herramientas/test_dashboard.py`.
- **Observation**: el panel existe, está versionado y se regenera desde `run_all.py`, el job de circuitos y `sitio_build.sh`, pero el informe no declara su ruta: un lector que siga solo `INFORME_TECNICO.md` encontrará los dashboards antiguos de `Data/analisis/` y no este artefacto vigente.

## Tables

Tables: none-detected (no aparecen marcadores numerados `Tabla N` / `Table N`). Se inventarían las tablas Markdown sin numerar, con las leyendas taken verbatim de la fila de cabecera; los números de página no están disponibles en la caché de texto.

### Table (unnumbered) — «Fase | Nombre | Estado» (§2, ES)
- **Section**: §2 Estado y fases (p. n/a)
- **Lines**: 24–34
- **Columns**: Fase, Nombre, Estado
- **Rows**: 9
- **Claims supported** (preliminary): estado de fases; fase activa 6, fases 7–9 pendientes.

### Table (unnumbered) — «Búsqueda | Páginas | Resultados | Útiles | Parada» (§7, ES)
- **Section**: §7 Fase 4 — Corpus documental (p. n/a)
- **Lines**: 78–82
- **Columns**: Búsqueda, Páginas, Resultados, Útiles, Parada
- **Rows**: 3

### Table (unnumbered) — «Tienda | Filas | Con precio» (§9, ES)
- **Section**: §9 Fase 6 — Scraping y captura (p. n/a)
- **Lines**: 94–106
- **Columns**: Tienda, Filas, Con precio
- **Rows**: 11
- **Claims supported** (preliminary): «11 bases» y «256 filas»; densidad de precio por tienda.

### Table (unnumbered) — «Problema | Solución» (§11, ES)
- **Section**: §11 Problemas y soluciones (p. n/a)
- **Lines**: 122–129
- **Columns**: Problema, Solución
- **Rows**: 6

### Table (unnumbered) — «Phase | Name | Status» / «Search | Pages | Results | Useful | Stopped at» / «Store | Rows | With price» / «Problem | Solution» (§2, §7, §9, §11, EN)
- **Section**: espejo inglés de las cuatro tablas anteriores (p. n/a)
- **Lines**: 153–163, 207–211, 223–235, 251–258
- **Rows**: 9, 3, 11, 6
- **Observation**: el espejo inglés de §12 (§264–270) no reproduce la conclusión 5 del original: donde el texto español afirma que el modelo de rentabilidad está implementado (§139), la versión inglesa afirma «The interactive product and profitability model (phase 8) are not implemented yet» (§270). Es una divergencia de contenido entre tablas/parrafos paralelos, no solo de traducción.

### Table (unnumbered) — «Fecha / Date | Ruta / Path | Tipo / Type | Origen / Source | Tamaño / Size | Fase / Phase | Descripción / Description | Estado / Status» (§13)
- **Section**: §13 Registro de altas / Change log (p. n/a)
- **Lines**: 276–748 (marcador `<!-- REGISTRO_ALTAS -->` en 278; múltiples instantáneas fechadas)
- **Columns**: ocho columnas según la cabecera
- **Rows**: varies; la línea 291 declara «175 entradas adicionales no listadas / omitted»
- **Claims supported** (preliminary): inventario automático de altas, tamaños y fases; regenerado por `actualizar_informe.py`.

### Table (unnumbered) — «Última ejecución / Last run | Tamaño / Size | Partes / Chunks | SHA-256 (inicio) | Reconstrucción / Rebuild» (§14)
- **Section**: §14 Sincronización automática de Revolico (p. n/a)
- **Lines**: 756–759 (marcador `<!-- SYNC_REVOLICO -->` en 758)
- **Rows**: 1

### Table (unnumbered) — «Fuente | Aporte metodológico | Requerimiento para AutoDecide» (§17)
- **Section**: §17 Guía de análisis de mercado (p. n/a)
- **Lines**: 791–804
- **Rows**: 12

### Table (unnumbered) — «Fuente | Naturaleza | Verificación | Uso en el análisis» (§18)
- **Section**: §18 Auditoría de procedencia (p. n/a)
- **Lines**: 812–825
- **Rows**: 12

### Table (unnumbered) — «Tabla | Registros» (§29)
- **Section**: §29 Base de datos de Telegram (p. n/a)
- **Lines**: 960–965
- **Rows**: 4
- **Claims supported** (preliminary): `canales` 119, `anuncios` 54.

### Table (unnumbered) — «Métrica | Valor» (§34)
- **Section**: §34 Esqueleto de análisis de rentabilidad (p. n/a)
- **Lines**: 1041–1055
- **Rows**: 10
- **Claims supported** (preliminary): línea base de la primera ejecución (972 ingeridas, 499 limpias, 376 rechazos, 32 marcas, mediana 24.000 USD, −5,43 %/año). Es una cifra histórica: §59–§60 ya no sostienen esa pendiente.

### Table (unnumbered) — «Tipo | Color | Símbolo» (§42)
- **Section**: §42 Base unificada del mapa (p. n/a)
- **Lines**: 1166–1171
- **Rows**: 4

## Figures

Figures: none-detected (no hay marcadores `Figura N` / `Figure N`). Se inventarían los artefactos gráficos citados.

### Figure (unnumbered) — ocho PNG en `Data/analisis/graficos/` (§23, §24)
- **Section**: §23 Conversión elTOQUE, serie temporal y gráficas; §24 (p. n/a)
- **Files named**: `01_histograma_precios.png`, `02_boxplot_marcas.png`, `03_barras_municipios.png`, `04_precios_por_anio.png`, `05_serie_precio_vs_tasa.png`, `06_variaciones_tasa_precio.png`, `07_outliers.png`, `08_cobertura.png`
- **Rendered in document**: no
- **Type**: histograma, boxplots, barras, series temporales, outliers y cobertura

### Figure (unnumbered) — dashboards descriptivos (§22, §23)
- **Paths named**: `Data/analisis/dashboard.html`, `Data/analisis/graficos/dashboard_interactivo.html`
- **Rendered in document**: no
- **Type**: dashboard HTML interactivo
- **Observation**: son los dashboards que el informe cita; el panel vigente (`Data/dashboard.html`) es un artefacto distinto, descrito en New artifacts.

### Figure (unnumbered) — seis gráficos Plotly del pipeline de rentabilidad (§34, §59, §61)
- **Paths named**: `Data/analisis_rentabilidad/outputs/charts/{01_precios,02_anios,03_marcas,04_tiers,05_km_precio,06_edad_precio}.html` (23,7–51,2 KB), copias idénticas en `docs/graficos/`
- **Rendered in document**: no (§59 describe un «apéndice visual con cinco cuadros y seis gráficos reales» con referencias discretas entre paréntesis)
- **Type**: gráficos Plotly interactivos

### Figure (unnumbered) — `Data/mapas/mapa_ofline.html` (§36, §41, §42)
- **Rendered in document**: no
- **Type**: mapa Plotly sin conexión con contorno de Cuba embebido; capas de concesionarios, carga, gasolineras y talleres

### Figure (unnumbered) — activos del timelapse de circuitos (§62)
- **Paths named**: `Data/mapas/circuitos/`, `Data/mapas/circuitos_estado.sqlite`, `Data/mapas/TIMELAPSE_CIRCUITOS.md`
- **Rendered in document**: no

## Missing artifacts

### Cifras de `modelo_muestra.csv` citadas en la narrativa técnica
- **Mentioned in document**: §59 (p. n/a): «28 observaciones completas» de «981 candidatas» (R² 0,277; p del F 0,411); en paralelo, `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md` (56): «572 observaciones de 897 candidatas … el completo usa 22 (R² = 0,277; p del F = 0,623)».
- **Found in repo**: yes (el CSV existe), pero parcialmente desincronizado
- **Observation**: el archivo vigente registra 584/28 observaciones sobre 981 candidatas (R² 0,101/0,2744; p 0,0/0,4114). El escenario 572/22 de 897 candidatas que describen el plan de la iteración 2 y tres documentos derivados ya no existe en disco. No se puede reconstruir de qué corrida provienen esas cifras sin una versión anterior del CSV, y el R² de §59 (0,277) tampoco es el redondeo de 0,2744.

### Ruta del panel interactivo en el informe
- **Mentioned in document**: §17 (p. n/a): «(6) dashboard de mercado»; §19: «dashboard de mercado, limitaciones y actualización periódica»; §59: «apéndice visual con cinco cuadros y seis gráficos reales».
- **Found in repo**: yes (`Data/dashboard.html`, 109.929 B) pero no citado por esa ruta
- **Observation**: el informe nombra los dashboards de `Data/analisis/` generados el 18/11/2026, pero no el panel autocontenido que sustituye a los seis HTML de Plotly y que fue refrescado el 27/11/2026 con el estado de circuitos. El artefacto está documentado en `Data/AUTOMATIZACION.md` y se prueba en `test_dashboard.py`, pero queda fuera de la cadena de citas del documento auditado.

### `Data/referencias.md` y labellling de referencias verificadas
- **Mentioned in document**: §70 (p. n/a): «Referencias citadas y verificadas externamente durante la auditoría: Akerlof (1970) … DfT/DVLA … ANFAC … AEADE».
- **Found in repo**: yes
- **Observation**: el archivo existe con 38 entradas, pero no porta una marca positiva de «verificada» para esas cuatro; la única marca es `(metadata incomplete)` para las entradas incompletas. La distinción entre verificadas y no verificadas vive en `reviews/…e2-literature.md`, por lo que el estado que afirma §70 no es autónomo dentro del artefacto citado.

### Full Revolico SQLite file in the main branch
- **Mentioned in document**: §14 (p. n/a): «La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**»; §54: «`main` queda intacto hasta decidir su sustitución».
- **Found in repo**: yes en local (834,5 MB), no como archivo único en el historial versionado
- **Observation**: el documento describe esquemas de 48 chunks de 16 MiB (§14) y de 82 chunks de 10 MB con `MANIFEST.json` (§54) publicados en la rama huérfana `chunked-db`; `.gitattributes` confirma el manejo LFS de `*.sqlite` y `*.bin`, y `git lfs ls-files` reporta 157 objetos referenciados.

### Official Cuban vehicle-fleet and registration series
- **Mentioned in document**: §56 (p. n/a): «**No hay series de parque automotor ni de matriculaciones**».
- **Found in repo**: no
- **Observation**: los 12 anuarios ONEI están descargados, pero `series_oficiales.csv` solo contiene transporte de pasajeros y accidentes; la laguna sigue registrada como no resuelta.

### VAHAN (India) y endpoint vivo del BCC
- **Mentioned in document**: §18 (p. n/a): «No accesible desde este entorno (error de transporte)» / «No accesible en vivo desde este entorno».
- **Found in repo**: no
- **Observation**: se documentan como fuentes de referencia, sin datos recuperados; la conversión del modelo sigue usando la TRMI informal de elTOQUE fijada en `config.py`.

### Full gazette corpus
- **Mentioned in document**: §10 (p. n/a): «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe»; §67: mudanza a `~/Utilidades/Leyes`.
- **Found in repo**: no (fuera del árbol del proyecto)
- **Observation**: solo se inventarian las normas citadas por su número; el índice y los PDFs quedan fuera del repositorio después de la optimización de espacio.

### Docker daemon para el Google Maps scraper
- **Mentioned in document**: §36 (p. n/a): «el daemon Docker no arranca sin root en este entorno».
- **Found in repo**: no
- **Observation**: convive con el FlareSolverr 3.5.2 en Docker que sí se declara operativo en §6 (`http://127.0.0.1:8191/`).

### Especificaciones estructuradas y precios de transacción reales
- **Mentioned in document**: §24 (p. n/a): «**No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**»; §59–§60: pendiente anual y prima premium no significativas.
- **Found in repo**: parcial (`ad_json`, `apollo_full`, features derivados por regex)
- **Observation**: los campos se derivan con cobertura incompleta y el modelo completo solo reúne 28 observaciones; la afirmación de −5,43 %/año de §34 queda como línea base histórica, no como resultado vigente.

### `Copias/` reference repositories
- **Mentioned in document**: §3 (p. n/a): «`Copias/` no se registra en este informe por decisión explícita»; §17 cita código de `Copias/AutosxCuba/code/…`.
- **Found in repo**: yes, excluidas por decisión explícita
- **Observation**: cuatro repositorios de referencia existen en disco pero se excluyen del informe, aunque sus rutas aparecen en la tabla metodológica de §17.

## Code-to-document mapping (when discernible)

| Document component | Repo location |
|---|---|
| Revolico scraper / incremental updates | `Auxiliares/herramientas/scrape_revolico.py`, `actualizar_revolico.py`, `actualizar_informe.py` |
| Queue pipeline / classification | `Auxiliares/herramientas/scrape_revolico_pipeline.py`, `limpiar_revolico.py` |
| Dealer/marketplace scraping | `Auxiliares/herramientas/scrape_concesionarios.py`, `scrape_marketplaces.py` |
| Telegram / WhatsApp integrations | `Auxiliares/herramientas/scraper_telegram_publico.py`, `descubrir_canales_telegram.py`, `telegram_db.py` |
| Descriptive analysis and charts | `Auxiliares/herramientas/analisis_mercado.py`, `graficos_mercado.py`, `Data/analisis/` |
| Profitability pipeline | `Data/analisis_rentabilidad/config.py`, `scripts/01_ingest.py` … `05_benchmark.py`, `run_all.py`, `sql/analysis.sql` |
| Model sample backing §59 | `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` (plus `modelo_depreciacion.csv`, `modelo_resumen.txt`) |
| Panel interactivo / market dashboard | `Data/dashboard.html` and its copy `docs/dashboard.html`; generator `Auxiliares/herramientas/generar_dashboard.py`; not path-cited in the report |
| KPI markers in §59 | `Data/analisis_rentabilidad/outputs/tables/kpis.csv`; `Auxiliares/herramientas/actualizar_numeros.py` |
| Numbered references (§70) | `Data/referencias.md`; source `reviews/informe-tecnico-2026-11-27.e2-literature.md` |
| Audit artifacts (§69–§70) | `reviews/informe-tecnico-2026-11-27.{md,forensic.md}`, `.e*.md`, `.v*.md`, `.plan.md`, `informe-tecnico-2026-11-27-iter2.plan.md` |
| Reference-repo consolidation | `Auxiliares/herramientas/consolidar_repos_autos.py`, `Data/repos-autos-referencias/` |
| Maps and infrastructure | `Auxiliares/herramientas/geocode_elementos.py`, `generar_mapa_ofline.py`, `scraper_circuitos.py`, `Data/mapas/` |
| Documentation site | `docs/`, `mkdocs.yml`, `Auxiliares/herramientas/generar_sitio_mkdocs.py` |
| AI-use declaration (§69) | procedimental, sin artefacto de código asociado |

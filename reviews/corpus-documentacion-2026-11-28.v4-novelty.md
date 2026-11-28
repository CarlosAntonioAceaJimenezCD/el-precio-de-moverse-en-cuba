---
type: audit-artifact
phase: v4-novelty
slug: corpus-documentacion-2026-11-28
generated_at: 2026-11-28T14:05:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md
language: es
level: master
---

## Resumen

- El corpus sí declara diferenciadores: el temporal de §7 frente a Egyptian-Used-Cars, el de integración de «cuatro capas» en §5 y el de honestidad metodológica en MODELOS §4; solo el primero adopta forma de párrafo comparativo contra un trabajo cercano.
- No cita trabajos cercanos con marcadores: cero `[N]`, DOI o arXiv en los 8 archivos y cero coincidencias con las 41 entradas de `Data/referencias.md`; P014 y P029–P032 aparecen por nombre, y P033–P037 solo viven en el anexo.
- Las cinco reclamaciones `novelty` (C013, C052, C058, C061, C107) son ingeniería local sin componente sustantivo demostrado: el criterio master se satisface en la forma de un diferenciador y queda abierto en engagement y en sustantividad.

### F-V4-001 — §7 declara el diferenciador temporal frente a Egyptian-Used-Cars en un párrafo comparativo

El claim C107 (e1-claims, líneas 842–847; tipos `contextual`, `novelty`) recoge `PRESENTACION_STORYTELLING.md` §7 «El espejo egipcio», líneas 275–283: «Tomamos como referencia **`Egyptian-Used-Cars`**, uno de los análisis de mercado automotriz más completos que tenemos: 23.500 anuncios, historial mensual de precios, econometría, SQL, Tableau y Power BI», y más adelante «Nuestro proyecto ya tiene esa arquitectura: ingesta incremental, limpieza y features, análisis exploratorio, modelo econométrico con tests, benchmarks e infravalorados, salidas versionables. La diferencia es el tiempo. Egipto construyó su serie durante meses; aquí el mecanismo ya está sembrado y cada semana suma una observación real de precio». El diferenciador declarado es explícito y de alcance local: no se reclama otra arquitectura, sino que el mecanismo de series ya está instalado antes de acumular datos. E2 (P014, líneas 210–221) identifica vecino más cercano a `Egyptian-Used-Cars` —proyecto/repositorio, autoría no declarada en el corpus, sin año, sin URL, `(metadata incomplete: repositorio no enlazado; imposible verificar autoría, licencia o fecha desde el corpus)`— y lo marca `Cited in document: yes` en la línea 277.

El criterio `V4.differentiation_from_prior_art` para `level=master` se lee: «Differentiator articulated with at least one explicit comparison paragraph to one closest prior work» (level-criteria.md, línea 88). §7 es un apartado propio con un párrafo comparativo formulado contra ese único vecino, de modo que la condición formal se cumple. La cita es nominal, sin marcador ni ficha verificable, y el propio E1 (C107) registra la tensión con `ARQUITECTURA_DATOS.md:566`, que califica el trabajo como «Fase 0–1 de diseño»; la comparación sostiene la forma del diferenciador, no su estado implementado.

— polarity: positive · confidence: high · related: [[#C107]], [[#C013]], [[#P014]], [[#F-V4-005]] · criteria: V4.differentiation_from_prior_art.master

### F-V4-002 — Las cinco reclamaciones de novedad son ingeniería local sin componente sustantivo demostrado

Las cinco reclamaciones etiquetadas `novelty` en E1 son C013 («**El diseño está listo para crecer igual que crezcan los datos.**», L283), C052 («El objetivo no es "comprar un motor más rápido", sino cambiar la complejidad por ejecución de `O(total)` a `O(nuevo + particiones consultadas)`», L512–514), C058 («**Recolectar → procesar → publicar.** Ningún job de recolección hace `git push`; ningún push dispara scrapers», L637), C061 («llevan un marcador oculto `<!-- kpi:clave -->` […] `actualizar_numeros.py` lee los CSV y las bases vigentes y reemplaza **solo el número**», L663) y C107 (L279–283). Ninguna emplea verbos de primacía ni propone un método nuevo: C052 enuncia un objetivo de complejidad, C058 una separación de etapas y C061 una convención de plantillas, mientras C013 y C107 reclaman disponibilidad. El vecino más cercano del mapa E2 para estas reclamaciones es P014, al que el propio corpus atribuye «ingesta incremental, limpieza y features […] salidas versionables» (L279): la diferencia que el documento declara contra él es temporal («La diferencia es el tiempo», L281), no de componente ni de arquitectura.

El criterio `V4.scope_of_novelty_claim` para `level=master` exige «Component novelty + integration novelty: one of the two should be substantive» (level-criteria.md, línea 97). El lado de integración queda enunciado en C058 y C061 y contrastado una sola vez en C107; la sustantividad no se demuestra comparativamente contra P014 ni contra P029–P032 (modelo hedónico, Kruskal-Wallis, VIF y Welch, invocados sin atribución en `MODELOS_Y_FUNCIONES.md` §3, L433–470). C052 declara además la línea base como trabajo futuro —`benchmark_result.csv` se anuncia en L566—, de modo que el cambio de complejidad no tiene medición propia en el corpus. La calibración master no se alcanza en el eje de sustantividad: las cinco reclamaciones permanecen en novedad de alcance local e incremental.

— polarity: negative · confidence: high · related: [[#C013]], [[#C052]], [[#C058]], [[#C061]], [[#C107]], [[#P014]], [[#P029]], [[#P030]], [[#P031]], [[#P032]] · criteria: V4.scope_of_novelty_claim.master

### F-V4-003 — Cero marcadores `[N]`, DOI o arXiv para trabajos cercanos en los ocho archivos

E2 (nota de entrada, líneas 17–19; H1, líneas 585–587; cotejo, línea 471) constata que «el corpus no contiene marcadores `[N]`, DOI ni identificadores arXiv; ninguno de los 41 autores, títulos ni fuentes institucionales de `Data/referencias.md` aparece citado», con «cero coincidencias» en los dos sentidos. La verificación literal de los 41 apellidos/títulos dio «cero resultados» y los únicos aciertos parciales de cadena («Che,», «Pal,», «Etro») resultaron falsos positivos dentro de «Chevrolet», «página» y «película». Los trabajos cercanos que el corpus sí menciona —P014 `Egyptian-Used-Cars` (L277), P015–P017 repos ICD/AutosxCuba/Mercado-automotriz (L70) y P029–P032 métodos estadísticos (L433–470)— comparecen solo por nombre, sin marcador y con `(metadata incomplete)`; los cinco vecinos académicos de `Likely missing` (P033–P037) tienen ficha y marcador `[29]`, `[30]`, `[21]`, `[22]` y `[12]` en `Data/referencias.md`, pero no aparecen en ninguno de los 8 archivos.

El criterio `V4.prior_art_engagement` para `level=master` exige tres condiciones conjuntas: «Closest prior works cited, contrasted, and discussed in their own subsection» (level-criteria.md, línea 106). Solo la tercera se da de forma aislada en §7, y aun allí falta el marcador que acredite la cita. La consecuencia observable es una documentación con diferenciadores declarados pero bibliográficamente muda en su cara pública: el anexo y el corpus describen «dos regímenes de citas distintos» (E2, H1, L587).

— polarity: negative · confidence: high · related: [[#C107]], [[#C013]], [[#P014]], [[#P015]], [[#P016]], [[#P017]], [[#P029]], [[#P030]], [[#P031]], [[#P032]], [[#P033]], [[#P034]], [[#P035]], [[#P036]], [[#P037]] · criteria: V4.prior_art_engagement.master

### F-V4-004 — Diferenciadores de contenido declarados sin contraste con P033, P034, P035 ni P037

Además del diferenciador temporal, el corpus declara tres contrastes de contenido. En `README.md` §Fuentes de datos (L73): «La conversión usa la **TRMI informal de elTOQUE (18/11/2026): 930 CUP/USD, 1.000 CUP/EUR y 845,35 CUP/MLC**. Nunca se usa la tasa oficial para los precios del mercado» (C012). En storytelling §5 (L255): «Cruzar estas cuatro capas convierte un catálogo de anuncios en inteligencia de mercado». En `MODELOS_Y_FUNCIONES.md` §4 (L482–486, C051): «No se usa la tasa oficial de cambio. No se imputan precios ni kilómetros faltantes. No se afirma causalidad […] No se mezclan mercados: local e importación se reportan por separado».

E2 sitúa frente a esos diferenciadores los vecinos académicos que el corpus no cita: P033 —Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A. (2024), *Using AI in the informal currency market: evidence from Cuba*, *Applied Economics*, `[29]` en el anexo—, con «solapamiento directo con P004 (TRMI informal)» (L551–555); P034 —Castro Fernández, M.; Vilaragut Llanes, M.; Hernández, J. C. (2024), *Electromobility and Energy Transition in Cuba*, *Sustainability*, `[30]`—, «antecedente cubano directo» de las secciones 2, 5 y 6 (L557–561); P035 —Krotov, V.; Johnson, L.; Silva, L. (2020), *Legality and Ethics of Web Scraping*, `[21]`— y P036 —Brown, M. A.; Gruen, A.; Maldoff, G.; Messing, S.; Sanderson, Z.; Zimmer, M. T. (2025), *Web scraping for research*, *Big Data & Society*, `[22]`—, frente a la tensión entre «respeta los términos de uso» (L112) y la impersonación de navegador con FlareSolverr (L833); y P037 —Hulten, C. R. (2003), *Price Hedonics: A Critical Review*, `[12]`, `(metadata incomplete)`—, frente a la justificación del modelo hedónico en L433–452. Ninguno de los cinco se discute en el corpus con marcador, resultado o limitación ajena.

— polarity: negative · confidence: high · related: [[#C012]], [[#C051]], [[#P004]], [[#P028]], [[#P029]], [[#P033]], [[#P034]], [[#P035]], [[#P036]], [[#P037]], [[#F-V4-003]] · criteria: V4.prior_art_engagement.master

### F-V4-005 — «Listo para crecer» y «ya tiene esa arquitectura» exceden el estado Fase 0–1 declarado

Los claims C013 y C107 formulan la disponibilidad en términos más fuertes que el estado que el propio corpus registra. C013 (L283): «**El diseño está listo para crecer igual que crezcan los datos.**»; C107 (L279): «Nuestro proyecto ya tiene esa arquitectura». `ARQUITECTURA_DATOS.md` §6 (L566) cierra con «Este documento es la Fase 0–1 de diseño; la línea base de rendimiento se guardará en `benchmark_result.csv` antes de tocar el pipeline» y consigna que «`import duckdb` falla con `SIGILL` (Instrucción ilegal)» con el motor recomendado en L520 pendiente de reevaluación; E1 (C052, C053, C055) consigna que la recomendación queda condicionada por ese bloqueo y que la medición de línea base no figura en el corpus. En paralelo, `MODELOS_Y_FUNCIONES.md` §4 (L485) y storytelling §8 (L290) sitúan la serie de precios de 6–12 meses en el trabajo futuro, mientras `AUTOMATIZACION.md` §2 (L645) afirma que «104 observaciones en 2 años bastan para depreciación» (C010).

Frente a P014, cuyo «historial mensual de precios» se describe en L277 como ya construido, el diferenciador de C107 se apoya en un mecanismo sembrado, no en una serie observada. Bajo `V4.scope_of_novelty_claim.master` («Component novelty + integration novelty: one of the two should be substantive», línea 97), la reclamación de disponibilidad no se sostiene en componente ni en integración medidos dentro del corpus; es un sobreclaim de estado, no de primacía frente a arte previo.

— polarity: negative · confidence: high · related: [[#C013]], [[#C107]], [[#C010]], [[#C052]], [[#C053]], [[#C055]], [[#P014]], [[#F-V4-001]], [[#F-V4-002]] · criteria: V4.scope_of_novelty_claim.master

### F-V4-006 — Mapa sin búsquedas nuevas ni lectura L3: novedad no confirmable

El frontmatter de E2 declara `queries_run: 0`, `papers_l1: 37`, `papers_l2: 0`, `papers_l3: 0` y `degraded: false` para el mandato estrecho de cotejo. La nota de entrada (L17) precisa que «no se ejecutaron búsquedas web nuevas —los metadatos se reutilizan de la verificación OpenAlex/Crossref del 27/11/2026 consignada en `Data/referencias.md`—» y que «todos los ítems son L1, sin lectura de resúmenes (L2) ni de texto completo (L3)»; el cierre (L608) limita el mapa al cotejo entre corpus y anexo, «no para proponer obras externas nuevas ni para certificar enlaces institucionales». Las 37 fuentes del corpus quedan marcadas `(metadata incomplete)` (E2, L517 y H3, L593–595).

En ese régimen no hay antecedente nuevo capaz de desplazar a P014 o a P033–P037 como vecinos más cercanos, pero tampoco lectura L3 que permita afinar solapamientos. Bajo `V4.prior_art_engagement.master` la lectura permitida es «sin verificación de originalidad en esta pasada», no «novedad confirmada»: ninguna de las cinco reclamaciones novelty puede certificarse como libre de arte previo con este mapa.

— polarity: neutral · confidence: high · related: [[#C013]], [[#C052]], [[#C058]], [[#C061]], [[#C107]], [[#P014]], [[#P033]], [[#P034]], [[#P035]], [[#P036]], [[#P037]], [[#F-V4-002]], [[#F-V4-003]] · criteria: V4.prior_art_engagement.master

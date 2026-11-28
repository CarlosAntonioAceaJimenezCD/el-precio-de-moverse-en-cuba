---
type: audit-artifact
phase: e2-literature
slug: informe-tecnico-2026-11-27-iter3
generated_at: 2026-11-28T01:03:14-04:00
preset: Standard
queries_run: 0
papers_l1: 4
papers_l2: 4
papers_l3: 0
language: es
---

# Literature Map — iteración 3 (re-verificación dirigida de flags)

Nota de entrada. El plan aprobado (`reviews/informe-tecnico-2026-11-27-iter3.plan.md`, 23 líneas) declara `level: master` y `preset: Standard`, pero no contiene `queries_planned` ni `hypotheses_planned`. El mandato recibido para este extractor es estrecho: re-visar `Data/referencias.md` y la §71.6 del informe para determinar si las comparaciones con Gegić, Muça, Du y Vidal Alejandro están en el cuerpo con cita, y verificar los flags campo por campo. En consecuencia: (a) no se ejecutaron búsquedas web nuevas —los metadatos se reutilizan del mapa completo de 38 trabajos de la pasada 1 y de la verificación OpenAlex/Crossref del 27/11/2026 consignada en `Data/referencias.md`—; (b) el mapa de 38 obras sigue vigente en `reviews/informe-tecnico-2026-11-27.e2-literature.md`; (c) los IDs `P001`–`P004` de este artefacto son propios y se mapean a los IDs de la pasada 1 y a las entradas numeradas; (d) `Cited in document` significa mención nominal en el cuerpo del informe, y se reporta por separado la presencia de marcador numérico `[N]`.

## Clusters

### Cluster 1 — Posicionamiento frente a trabajos cercanos (§71.6)

**Query**: `§71.6` ∩ `Data/referencias.md` — búsqueda en el cuerpo por apellido y año (Gegić 2019; Muça 2026; Du 2026; Vidal Alejandro 2024) y contraste campo por campo con el flag «Citada en el informe» de las entradas [14], [26], [9] y [29].

Los cuatro trabajos aparecen juntos en un único párrafo de la §71.6 (`INFORME_TECNICO.md`, líneas 1518–1520; idéntico en la copia en caché de la iteración 3, líneas 1518–1520). Cada comparación tiene la forma «Frente a <apellidos> (<año>), que <descripción del trabajo ajeno>, este trabajo <diferenciador>». Ninguna de las cuatro lleva marcador numérico de cita.

#### P001 — Car Price Prediction using Machine Learning Techniques
- **Authors**: Gegić, E.; Isaković, B.; Keco, D.; Mašetić, Z.; Kevrić, J.
- **Year**: 2019
- **Venue**: TEM Journal
- **Citations**: 188 (source: OpenAlex, fetched 2026-11-27T05:15:00Z; mapa E2 pasada 1, P014)
- **URL**: https://doi.org/10.18421/tem81-16
- **Layer**: L2 (re-visado en cuerpo; sin nueva lectura de resumen en esta iteración)
- **Cited in document**: yes — mención nominal en §71.6, línea 1520: «Frente a Gegić, Isaković, Keco, Mašetić y Kevrić (2019), que predicen precios con machine learning sobre catálogos estructurados…».
- **Document reference**: [14] en `Data/referencias.md` (marcador `[14]` ausente en el cuerpo).
- **source_of_metadata**: OpenAlex W4288610071 (mapa E2 pasada 1) + `Data/referencias.md` [14].
- **Flag verificado**: `Citada en el informe: no` en [14] → **desactualizado**; el propio archivo define el flag como «mención nominal en el informe» (línea 6). Debe pasar a `sí` con calificación «mención nominal en §71.6, sin marcador numérico».

#### P002 — A Pipeline for Integrating and Analyzing Public Business Data in Albania Using Web Scraping and Machine Learning
- **Authors**: Muça, M.; Bani, K.; Alla, A.
- **Year**: 2026
- **Venue**: International Journal of Advanced Computer Science and Applications (IJACSA)
- **Citations**: 0 (source: OpenAlex, fetched 2026-11-27T05:15:00Z; mapa E2 pasada 1, P026)
- **URL**: https://doi.org/10.14569/ijacsa.2026.0170845
- **Layer**: L2 (re-visado en cuerpo; sin nueva lectura de resumen en esta iteración)
- **Cited in document**: yes — mención nominal en §71.6, línea 1520: «Frente a Muça, Bani y Alla (2026), que integran datos públicos empresariales albaneses mediante scraping…».
- **Document reference**: [26] en `Data/referencias.md` (marcador `[26]` ausente en el cuerpo).
- **source_of_metadata**: OpenAlex W7204683515 (mapa E2 pasada 1) + `Data/referencias.md` [26].
- **Flag verificado**: `Citada en el informe: no` en [26] → **desactualizado**; debe pasar a `sí` con la misma calificación.

#### P003 — Nonlinear Depreciation and Brand Heterogeneity in Chinese Used-Car Listing Prices: An Interpretable Hedonic Regression and Out-of-Sample Evaluation
- **Authors**: Du, Z.; Yang, Z.; Zhang, Y.; Li, S.; Liu, Y.
- **Year**: 2026
- **Venue**: Advances in Economics, Management and Political Sciences
- **Citations**: 0 (source: OpenAlex, fetched 2026-11-27T05:15:00Z; mapa E2 pasada 1, P009)
- **URL**: https://doi.org/10.54254/2754-1169/2026.38524
- **Layer**: L2 (re-visado en cuerpo; sin nueva lectura de resumen en esta iteración)
- **Cited in document**: yes — mención nominal en §71.6, línea 1520: «Frente a Du, Yang, Zhang, Li y Liu (2026), que modelan depreciación no lineal y heterogeneidad de marca con evaluación fuera de muestra…».
- **Document reference**: [9] en `Data/referencias.md` (marcador `[9]` ausente en el cuerpo).
- **source_of_metadata**: OpenAlex W7225188457 (mapa E2 pasada 1) + `Data/referencias.md` [9].
- **Flag verificado**: `Citada en el informe: no` en [9] → **desactualizado**; debe pasar a `sí` con la misma calificación.

#### P004 — Using AI in the informal currency market: evidence from Cuba
- **Authors**: Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A.
- **Year**: 2024
- **Venue**: Applied Economics
- **Citations**: 1 (source: OpenAlex, fetched 2026-11-27T05:15:00Z; mapa E2 pasada 1, P029)
- **URL**: https://doi.org/10.1080/00036846.2024.2416091
- **Layer**: L2 (re-visado en cuerpo; sin nueva lectura de resumen en esta iteración)
- **Cited in document**: yes — mención nominal en §71.6, línea 1520: «Frente a Vidal Alejandro, Muñiz-Cuza y Calas Torres (2024), que estudian el mercado informal de divisas en Cuba…».
- **Document reference**: [29] en `Data/referencias.md` (marcador `[29]` ausente en el cuerpo).
- **source_of_metadata**: OpenAlex W4403850866 (mapa E2 pasada 1) + `Data/referencias.md` [29].
- **Flag verificado**: `Citada en el informe: no` en [29] → **desactualizado**; debe pasar a `sí` con la misma calificación.

## Recency distribution

Convenio: «In map» cuenta las cuatro entradas re-visadas en este artefacto; «In document bibliography» cuenta las 38 entradas presentes en `Data/referencias.md` (no menciones en el cuerpo); «Nominal mention in body» cuenta los apellidos efectivamente presentes en el texto del informe tras la §71.6.

| Year | In map | In document bibliography | Nominal mention in body |
|---|---:|---:|---:|
| 2026 | 2 | 6 | 2 (Muça [26], Du [9]) |
| 2025 | 0 | 1 | 0 |
| 2024 | 1 | 6 | 1 (Vidal Alejandro [29]) |
| 2023 | 0 | 4 | 0 |
| 2022 | 0 | 1 | 0 |
| ≤2021 | 1 | 20 | 1 (Gegić [14]) |

Las menciones nominales totales en el cuerpo son 5 de 38: Akerlof [1] —ya marcada `yes` y presente desde antes de la iteración 3— más las cuatro de §71.6. Los Marcadores `[N]` siguen siendo 0 en el texto (búsqueda de `[1]`–`[38]` en el cuerpo: sin coincidencias). La §70 («Referencias verificadas», línea 1477) enumera como citadas y verificadas solo Akerlof y tres fuentes institucionales (DfT/DVLA, ANFAC, AEADE); las cuatro obras de §71.6 no figuran en esa enumeración aunque sí lo están en el anexo numerado.

## Venue distribution

| Venue | Count in map |
|---|---:|
| TEM Journal | 1 |
| International Journal of Advanced Computer Science and Applications | 1 |
| Advances in Economics, Management and Political Sciences | 1 |
| Applied Economics | 1 |

## Likely missing important works

La lista de ocho obras probablemente decisivas de la pasada 1 (E2 iter1, líneas 490–530; reafirmada sin cambios en la iteración 2, línea 168) queda en siete para esta iteración: P002 Lewis (2011), P004 Englmaier et al. (2017), P021 Krotov et al. (2020), P023 Priestley et al. (2023), P022 Brown et al. (2025), P033 Guerra (2015) y P024 Hohensinner et al. (2026). Gegić et al. (2019) sale de la lista porque ya no está ausente del cuerpo: tiene comparación nominal explícita en §71.6. No se proponen obras nuevas: no se ejecutaron búsquedas temáticas en esta iteración y los metadatos se reutilizan de fuentes verificadas el 27/11/2026.

## Hypothesis checks (from plan)

El plan no declara hipótesis. Las tres comprobaciones siguientes se derivan del mandato recibido y son observaciones sin veredicto.

### H1 — Las comparaciones con Gegić, Muça, Du y Vidal Alejandro están en el cuerpo con cita (derivada)

Estado de la evidencia: **sí, como menciones nominales con autor y año**. Las cuatro comparecen en la §71.6, un apartado específico titulado «Posicionamiento frente a trabajos cercanos / Positioning against prior work» (líneas 1518–1520), y cada una recibe una cláusula contrastiva que describe el trabajo ajeno y enuncia el diferenciador propio. Es un cambio sustantivo frente a la iteración 2, donde el expediente forense constataba que «no hay párrafo comparativo con el trabajo académico más cercano» (`informe-tecnico-2026-11-27-iter2.forensic.md`, línea 247) y el informe iter2 resumía que los cuatro «figuran en la lista numerada sin citas en el cuerpo» (`informe-tecnico-2026-11-27-iter2.md`, línea 109).

La calificación de «con cita» es sin embargo parcial: las menciones no van acompañadas de marcador numérico `[14]`, `[26]`, `[9]` ni `[29]`, el documento no contiene ningún marcador `[N]` en su cuerpo, y la lista de «referencias citadas y verificadas externamente» de §70 no incluye a estas cuatro obras. La forma es, por tanto, cita nominal en el argumento, no cita numerada enlazada al anexo.

### H2 — Los flags por campo de `Data/referencias.md` reflejan el estado actual del cuerpo (derivada)

Estado de la evidencia: **no para cuatro campos**. El archivo define en su línea 6 que «`Citada: sí/no` indica mención nominal en el informe», y fue generado el 27/11/2026 desde el mapa E2 de la primera iteración, es decir, antes de que existiera la §71.6. Las fichas [9], [14], [26] y [29] conservan `Citada en el informe: no` mientras el cuerpo sí las nombra. Son cuatro flags desactualizados por campo, no un problema de metadatos bibliográficos: autores, año, revista, DOI y conteo de citas permanecen verificados. La actualización que corresponde, sin alterar otros campos, es `Citada en el informe: sí (mención nominal en §71.6; sin marcador numérico)`. Los marcadores `(metadata incomplete)` de [1], [10] y [38] y las notas de discrepancia de año de [2], [19] y [38] no fueron re-verificados en esta iteración y se dejan como están.

### H3 — La §71.6 satisface la condición de discusión dedicada de trabajos cercanos (derivada)

Estado de la evidencia: hay un apartado propio con cuatro párrafos comparativos nominales, uno por vecino académico, y cada uno formula una diferencia de procedencia, conversión, estimación u objeto de estudio. La observación se limita a la forma: el apartado no incorpora marcadores numéricos, cifras de los trabajos ajenos ni discusión de sus resultados o limitaciones más allá de la descripción de una frase. Corresponde a V4 y V5 decidir cómo ponderar este cambio respecto del criterio de nivel master.

## Sources used

- WebSearch queries: 0 (re-visación dirigida; sin búsquedas temáticas nuevas).
- WebFetch URLs: 0 en esta iteración.
- Semantic Scholar API hits: 0.
- OpenAlex API hits: 0 nuevos; los conteos de citas se reutilizan del mapa E2 de la pasada 1 (OpenAlex, fetched 2026-11-27T05:15:00Z) y de la verificación consignada en `Data/referencias.md` (27/11/2026).
- Archivos locales inspeccionados: `INFORME_TECNICO.md` (§70, línea 1477; §71.6, líneas 1518–1520); copia en caché `.playground/audit-cache/informe-tecnico-2026-11-27-iter3/informe-tecnico-2026-11-27-iter3.text.md` (mismo contenido); `Data/referencias.md` (líneas 3–6 y entradas [1], [9], [14], [26], [29]); `reviews/informe-tecnico-2026-11-27.e2-literature.md` (P009, P014, P026, P029; lista de obras ausentes); `reviews/informe-tecnico-2026-11-27-iter2.e2-literature.md` (nota de entrada y línea 168); `reviews/informe-tecnico-2026-11-27-iter2.forensic.md` ( línea 247) y `reviews/informe-tecnico-2026-11-27-iter2.md` (línea 109).
- Degradación: `degraded: false` para el mandato recibido —las cuatro comparaciones y sus cuatro flags quedaron resueltos por inspección directa del cuerpo—. Limitación declarada: no se re-verificaron los otros 34 flags ni se ejecutó búsqueda bibliográfica nueva; este mapa no debe usarse para proponer obras adicionales.

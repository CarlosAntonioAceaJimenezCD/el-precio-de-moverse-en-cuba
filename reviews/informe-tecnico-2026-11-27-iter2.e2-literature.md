---
type: audit-artifact
phase: e2-literature
slug: informe-tecnico-2026-11-27-iter2
generated_at: 2026-11-27T16:10:00-05:00
preset: Standard
queries_run: 22
papers_l1: 6
papers_l2: 6
papers_l3: 0
language: es
---

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

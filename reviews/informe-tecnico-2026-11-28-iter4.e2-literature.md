---
type: audit-artifact
phase: e2-literature
slug: informe-tecnico-2026-11-28-iter4
generated_at: 2026-11-28T03:00:41-04:00
preset: Standard
queries_run: 0
papers_l1: 9
papers_l2: 9
papers_l3: 0
language: es
---

# Literature Map — iteración 4 (re-verificación dirigida de marcadores y flags)

Nota de entrada. El plan aprobado (`reviews/informe-tecnico-2026-11-28-iter4.plan.md`, 22 líneas) declara `level: master` y `preset: Standard`, pero no contiene `queries_planned` ni `hypotheses_planned`. El mandato recibido para este extractor es estrecho: verificar `Data/referencias.md` (41 entradas), los marcadores `[N]` en §71.6, §71.14, §17 y §34, la coherencia de los flags campo por campo y la representación de las fuentes institucionales [39]–[41]. En consecuencia: (a) no se ejecutaron búsquedas web nuevas ni re-lecturas de resúmenes —los metadatos se reutilizan del mapa E2 de la pasada 1 y de la verificación OpenAlex/Crossref del 27/11/2026 consignada en `Data/referencias.md`—; (b) las capas L1/L2 indicadas son heredadas, no nuevas; (c) los IDs `P001`–`P009` son propios de este artefacto y se mapean a las entradas numeradas; (d) los números de línea corresponden a la copia en caché `.playground/audit-cache/informe-tecnico-2026-11-28-iter4/informe-tecnico-2026-11-28-iter4.text.md`, idéntica en contenido al informe auditado; (e) `Cited in document` significa mención en el cuerpo, y se reporta por separado la presencia de marcador numérico `[N]`.

## Clusters

### Cluster 1 — Posicionamiento frente a trabajos cercanos (§71.6) y sus flags

**Query**: `§71.6` ∩ `Data/referencias.md` — búsqueda por apellido y año (Du 2026; Gegić 2019; Muça 2026; Vidal Alejandro 2024) y contraste campo por campo con el flag «Citada en el informe» de [9], [14], [26] y [29].

Las cuatro comparaciones siguen en un único párrafo (línea 1549) y ahora **sí llevan marcador numérico**: `[14]`, `[26]`, `[9]` y `[29]`. Es el cambio sustantivo frente a la iteración 3, donde el mismo párrafo no tenía marcadores. Los cuatro flags conservan sin embargo la calificación «sin marcador numérico» que se les asignó en la iteración 4 anterior.

#### P001 — Nonlinear Depreciation and Brand Heterogeneity in Chinese Used-Car Listing Prices

- **Authors**: Du, Z.; Yang, Z.; Zhang, Y.; Li, S.; Liu, Y.
- **Year**: 2026
- **Venue**: Advances in Economics, Management and Political Sciences
- **Citations**: no re-contadas en esta iteración; DOI 10.54254/2754-1169/2026.38524 verificado el 27/11/2026 según `Data/referencias.md` [9].
- **URL**: https://doi.org/10.54254/2754-1169/2026.38524
- **Layer**: L2 (heredada del mapa E2 de la pasada 1; sin nueva lectura de resumen)
- **Cited in document**: yes — línea 1549: «Du y otros [9] modelan depreciación no lineal y heterogeneidad de marca con evaluación fuera de muestra».
- **Document reference**: [9] (marcador presente en §71.6).
- **source_of_metadata**: mapa E2 pasada 1 (OpenAlex, fetched 2026-11-27) + `Data/referencias.md` [9].
- **Flag verificado**: `Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)` en la línea 24 → **el calificador ya no corresponde**: el marcador `[9]` está presente. La forma correcta sería `sí (§71.6, con marcador numérico)`.

#### P002 — Car Price Prediction using Machine Learning Techniques

- **Authors**: Gegić, E.; Isaković, B.; Keco, D.; Mašetić, Z.; Kevrić, J.
- **Year**: 2019
- **Venue**: TEM Journal
- **Citations**: no re-contadas en esta iteración; DOI 10.18421/tem81-16 verificado el 27/11/2026 según `Data/referencias.md` [14].
- **URL**: https://doi.org/10.18421/tem81-16
- **Layer**: L2 (heredada; sin nueva lectura de resumen)
- **Cited in document**: yes — línea 1549 (`Gegić y otros [14]`) y línea 1080 (`antecedentes [14], [18]`).
- **Document reference**: [14] (dos marcadores en el cuerpo: §71.6 y §34).
- **source_of_metadata**: mapa E2 pasada 1 (OpenAlex) + `Data/referencias.md` [14].
- **Flag verificado**: `Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)` en la línea 34 → **el calificador ya no corresponde** y además omite §34.

#### P003 — A Pipeline for Integrating and Analyzing Public Business Data in Albania Using Web Scraping and Machine Learning

- **Authors**: Muça, M.; Bani, K.; Alla, A.
- **Year**: 2026
- **Venue**: International Journal of Advanced Computer Science and Applications
- **Citations**: no re-contadas en esta iteración; DOI 10.14569/ijacsa.2026.0170845 verificado el 27/11/2026 según `Data/referencias.md` [26].
- **URL**: https://doi.org/10.14569/ijacsa.2026.0170845
- **Layer**: L2 (heredada; sin nueva lectura de resumen)
- **Cited in document**: yes — línea 1549: «Muça, Bani y Alla [26] integran datos públicos albaneses por scraping».
- **Document reference**: [26] (marcador presente en §71.6).
- **source_of_metadata**: mapa E2 pasada 1 (OpenAlex) + `Data/referencias.md` [26].
- **Flag verificado**: `Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)` en la línea 58 → **el calificador ya no corresponde**.

#### P004 — Using AI in the informal currency market: evidence from Cuba

- **Authors**: Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A.
- **Year**: 2024
- **Venue**: Applied Economics
- **Citations**: no re-contadas en esta iteración; DOI 10.1080/00036846.2024.2416091 verificado el 27/11/2026 según `Data/referencias.md` [29].
- **URL**: https://doi.org/10.1080/00036846.2024.2416091
- **Layer**: L2 (heredada; sin nueva lectura de resumen)
- **Cited in document**: yes — línea 1549: «Vidal Alejandro y otros [29] estudian el mercado informal de divisas en Cuba».
- **Document reference**: [29] (marcador presente en §71.6).
- **source_of_metadata**: mapa E2 pasada 1 (OpenAlex) + `Data/referencias.md` [29].
- **Flag verificado**: `Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)` en la línea 64 → **el calificador ya no corresponde**.

### Cluster 2 — Citas numeradas en §19, §17 y §34

**Query**: `§17` ∪ `§19` ∪ `§34` ∩ `Data/referencias.md` — inventario de marcadores `[N]` presentes fuera de §71.6 y contraste con los flags de [1] y [18].

Resultado del inventario: §17 (líneas 811–832) contiene **0 marcadores**; §19 (línea 861) contiene `[1]`; §34 (línea 1080) contiene `[14]` e `[18]`; §71.14 (líneas 1561–1598) contiene 38 marcadores de tabla `[1]`–`[38]` y la línea 1600 repite `[1]`, `[9]`, `[14]`, `[26]` y `[29]`. En prosa de cuerpo, las obras con marcador son seis: [1], [9], [14], [18], [26] y [29].

#### P005 — The Market for "Lemons": Quality Uncertainty and the Market Mechanism

- **Authors**: Akerlof, G. A.
- **Year**: 1970
- **Venue**: The Quarterly Journal of Economics
- **Citations**: no re-contadas; DOI 10.2307/1879431 confirmado en OpenAlex el 27/11/2026 según `Data/referencias.md` [1].
- **URL**: https://doi.org/10.2307/1879431
- **Layer**: L2 (heredada; sin nueva lectura de resumen)
- **Cited in document**: yes — línea 861 (`asimetría de información (Akerlof [1])`), línea 817 (mención nominal sin marcador en §17) y línea 1561 (tabla de §71.14).
- **Document reference**: [1].
- **source_of_metadata**: mapa E2 pasada 1 (OpenAlex) + `Data/referencias.md` [1].
- **Abstract analysis** (L2 heredada): el resumen indexado es un índice de secciones, no un resumen sustantivo; por eso la entrada lleva `(metadata incomplete: resumen indexado no sustantivo; identidad y DOI verificados en OpenAlex)`, coherente con la glosa `(metadata incomplete: resumen)` / `(metadata incomplete: abstract)` de §70 (líneas 1497 y 1499).
- **Flag verificado**: `Citada en el informe: sí` → correcto, aunque no registra las tres ubicaciones. Incidencia aparte: la línea 1600 afirma que [1] «se discute además en §71.6», pero el párrafo de §71.6 (línea 1549) no incluye a Akerlof; su discusión está en §17 y §19.

#### P006 — ProbSAINT: Probabilistic Tabular Regression for Used Car Pricing

- **Authors**: Madhusudhanan, K.; Behrens, G.; Stubbemann, M.; Schmidt-Thieme, L.
- **Year**: 2024
- **Venue**: arXiv:2403.03812 / IEEE BigData 2024, Industry & Government Track
- **Citations**: 13 verificadas en OpenAlex el 27/11/2026 según `Data/referencias.md` [18]; no re-contadas.
- **URL**: https://arxiv.org/abs/2403.03812
- **Layer**: L2 (heredada; sin nueva lectura de resumen)
- **Cited in document**: yes — línea 1080: «La predicción de precios sobre catálogos estructurados tiene antecedentes [14], [18]».
- **Document reference**: [18] (marcador presente en §34).
- **source_of_metadata**: mapa E2 pasada 1 (OpenAlex) + `Data/referencias.md` [18].
- **Flag verificado**: `Citada en el informe: no` en la línea 42 → **desactualizado**: [18] tiene marcador numérico en §34. Debe pasar a `sí (§34, con marcador numérico)`. Esta es la única entrada del bloque [1]–[38] cuyo flag `no` contradice directamente un marcador en prosa.

### Cluster 3 — Fuentes institucionales [39]–[41] (§18 / §70)

**Query**: `§18` ∪ `§70` ∩ `Data/referencias.md` [39]–[41] — contraste de flags, campo «Citada en el informe» y tipo de fuente declarado.

Ninguna de las tres fuentes tiene marcador numérico en el cuerpo y ninguna figura en la tabla de §71.14, que se detiene en [38]. Su presencia se documenta por nombre en §18 y §70.

#### P007 — Vehicle statistics (Department for Transport / DVLA)

- **Authors**: Department for Transport / DVLA (institucional)
- **Year**: sin campo de año en la entrada
- **Venue**: GOV.UK (sitio institucional)
- **Citations**: no aplica; sin re-verificación en vivo en esta iteración.
- **URL**: https://www.gov.uk/government/organisations/department-for-transport
- **Layer**: L1 (metadatos institucionales heredados; sin fetch nuevo)
- **Cited in document**: yes — línea 838 (§18, con URL profunda `gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files`) y línea 1497 (§70).
- **Document reference**: [39] (sin marcador numérico en el cuerpo).
- **source_of_metadata**: `Data/referencias.md` [39] + informe §18 y §70.
- **Flag verificado**: dos incidencias. (i) Es la **única de las 41 entradas sin campo `Citada en el informe`**; por el contenido del cuerpo debería ser `sí (fuente institucional en §18 y §70)`. (ii) Lleva `(metadata incomplete: URL profunda no confirmada)` mientras §18 declara «Verificado en vivo: publicado por Department for Transport + DVLA, actualizado 23/09/2026, Open Government Licence» con esa URL profunda y §70 la enumera entre las «Referencias citadas y verificadas externamente durante la auditoría». No se re-fetchó la URL en esta pasada, así que solo se constata la contradicción interna, no la validez del enlace.

#### P008 — Informes del sector automotriz español (ANFAC)

- **Authors**: ANFAC (asociación gremial)
- **Year**: sin campo de año en la entrada
- **Venue**: anfac.com (sitio institucional)
- **Citations**: no aplica; sin re-verificación en vivo en esta iteración.
- **URL**: https://anfac.com/
- **Layer**: L1 (metadatos institucionales heredados; sin fetch nuevo)
- **Cited in document**: yes — línea 821 (§17, mención nominal agrupada con EY/INEGI/BBVA/COIIM), línea 842 (§18, «Verificado en vivo») y línea 1497 (§70, «sitio oficial»).
- **Document reference**: [40] (sin marcador numérico en el cuerpo).
- **source_of_metadata**: `Data/referencias.md` [40] + informe §17, §18 y §70.
- **Flag verificado**: `Citada en el informe: sí (fuente institucional en §70)` y sin `(metadata incomplete)` → coherente con §18 y §70. La glosa omite §17 y §18, pero no contradice ningún campo. La ausencia de marcador `[40]` es consecuencia de que §17 no usa marcadores y de que §71.14 no incluye a [39]–[41].

#### P009 — Estadísticas de matriculaciones (AEADE)

- **Authors**: AEADE (gremial, Ecuador)
- **Year**: sin campo de año en la entrada
- **Venue**: aeade.net (sitio institucional)
- **Citations**: no aplica; sin re-verificación en vivo en esta iteración.
- **URL**: https://www.aeade.net/
- **Layer**: L1 (metadatos institucionales heredados; sin fetch nuevo)
- **Cited in document**: yes — línea 843 (§18, «Verificado en vivo: aeade.net, anuarios y boletines de ventas; fuente declarada por el estudio PUCE») y línea 1497 (§70, «sitio oficial»).
- **Document reference**: [41] (sin marcador numérico en el cuerpo; no aparece en §17).
- **source_of_metadata**: `Data/referencias.md` [41] + informe §18 y §70.
- **Flag verificado**: `Citada en el informe: sí (fuente institucional en §70)` y sin `(metadata incomplete)` → coherente. Como en [40], la glosa no menciona §18, donde está la verificación en vivo.

## Recency distribution

Convenio: «In document bibliography» cuenta las 41 entradas de `Data/referencias.md`; 38 tienen año y las tres institucionales ([39]–[41]) no lo tienen. «In map» cuenta las nueve entradas re-visadas en este artefacto.

| Year | In map | In document bibliography |
|---|---:|---:|
| 2026 | 2 | 6 |
| 2025 | 0 | 1 |
| 2024 | 2 | 6 |
| 2023 | 0 | 4 |
| 2022 | 0 | 1 |
| ≤2021 | 2 | 20 |
| Sin año (institucionales [39]–[41]) | 3 | 3 |

Las nueve entradas re-visadas son [1], [9], [14], [18], [26], [29], [39], [40] y [41]. El conteo de años coincide con el consignado en la iteración 3 para el bloque [1]–[38].

## Venue distribution

| Venue | Count in map |
|---|---:|
| The Quarterly Journal of Economics | 1 |
| Advances in Economics, Management and Political Sciences | 1 |
| TEM Journal | 1 |
| arXiv / IEEE BigData 2024 | 1 |
| International Journal of Advanced Computer Science and Applications | 1 |
| Applied Economics | 1 |
| Sitio institucional (GOV.UK / ANFAC / AEADE) | 3 |

## Auditoría de flags por campo

| Entrada | Campo | Estado en `Data/referencias.md` | Evidencia en el informe | Observación |
|---|---|---|---|---|
| [1] | `Citada` / `metadata incomplete` | `sí` / resumen indexado no sustantivo | §17 (nominal), §19 (`[1]`), §71.14 | Coherente; la línea 1600 de §71.14 lo atribuye erróneamente a §71.6 |
| [9] | `Citada` | `sí (…sin marcador numérico)` | §71.6 `[9]` | Calificador desactualizado |
| [14] | `Citada` | `sí (…sin marcador numérico)` | §71.6 `[14]`, §34 `[14]` | Calificador desactualizado y ubicación incompleta |
| [18] | `Citada` | `no` | §34 `[18]` | Flag desactualizado |
| [26] | `Citada` | `sí (…sin marcador numérico)` | §71.6 `[26]` | Calificador desactualizado |
| [29] | `Citada` | `sí (…sin marcador numérico)` | §71.6 `[29]` | Calificador desactualizado |
| [39] | `Citada` / `metadata incomplete` | campo ausente / URL profunda no confirmada | §18 (URL profunda «verificada en vivo»), §70 («verificada externamente») | Flag y campo en contradicción con el cuerpo |
| [40] | `Citada` | `sí (fuente institucional en §70)` | §17, §18, §70 | Coherente; ubicación incompleta |
| [41] | `Citada` | `sí (fuente institucional en §70)` | §18, §70 | Coherente; ubicación incompleta |

Dos observaciones agregadas sobre el campo `Citada`:

1. El archivo define ese campo como «indicación de mención nominal en el informe» (línea 6) y 33 de las 41 entradas lo tienen en `no`. Sin embargo, §71.14 se titula «Obras del mapa literario citadas en el cuerpo» (línea 1557) y su cierre dice que «el resto se registra aquí con su marcador numérico» (línea 1600), mientras 33 de las 38 filas de esa tabla llevan `no` en `Data/referencias.md`. El título/cierre de la sección y el campo de flag describen estados distintos; no se ha re-escrito ninguno de los dos en esta pasada.
2. §70 afirma que «las fuentes restantes figuran con estado `(metadata incomplete)` en `reviews/informe-tecnico-2026-11-27.e2-literature.md`» (líneas 1497 y 1499). En `Data/referencias.md` solo cuatro entradas llevan efectivamente esa marca —[1], [10], [12] y [39]— y el archivo enlazado es el mapa de la primera pasada, no el de esta iteración. La frase de §70 generaliza un estado que el anexo no sostiene campo por campo; las notas de discrepancia de año de [2], [19] y [38] son otro campo distinto del flag `(metadata incomplete)`.

## Likely missing important works

Sin búsquedas nuevas en esta iteración, se mantienen las siete obras arrastradas de la iteración 3 (presentes en `Data/referencias.md` con `Citada: no`, ausentes como discusión en el cuerpo): Lewis (2011) [2], Englmaier et al. (2017) [4], Krotov et al. (2020) [21], Priestley et al. (2023) [23], Brown et al. (2025) [22], Guerra (2015) [33] y Hohensinner et al. (2026) [24]. Gegić et al. (2019) [14] sigue fuera de la lista porque sí tiene discusión comparativa en §71.6 y marcadores en §71.6 y §34. No se proponen obras adicionales.

## Hypothesis checks (from plan)

El plan no declara hipótesis; las cuatro siguientes se derivan del mandato recibido y son observaciones sin veredicto.

### H1 — `Data/referencias.md` contiene 41 entradas numeradas de forma continua, en coherencia con el plan (derivada)

Estado de la evidencia: **sí para el archivo y el plan**. La comprobación directa da 41 líneas `^[n]`, de [1] a [41] sin huecos, y el plan (línea 19) declara «41 referencias». La incoherencia está aguas abajo: §70 (líneas 1497 y 1499) dice «La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`», cifra que coincide con las 38 filas de la tabla de §71.14 pero no con el anexo al que apunta. Las tres entradas sobrantes son precisamente las institucionales [39]–[41], que no están en esa tabla. El encabezado del anexo (línea 3) indica además que fue generado el 27/11/2026 desde `reviews/informe-tecnico-2026-11-27.e2-literature.md`, es decir, desde el mapa de la primera pasada.

### H2 — Los marcadores `[N]` del cuerpo coinciden con los flags «Citada en el informe» (derivada)

Estado de la evidencia: **coinciden en seis entradas, con cinco desajustes de campo**. Coinciden [1] (`sí`, con `[1]` en §19), [9], [14], [26] y [29] (`sí`, con marcadores en §71.6) y [40]/[41] (`sí` institucionales, sin marcador pero con mención nominal). Los desajustes son: los calificadores «sin marcador numérico» de [9], [14], [26] y [29], que dejaron de ser ciertos en esta iteración; y el flag `no` de [18], que tiene `[18]` en §34. Ningún otro marcador aparece en prosa de cuerpo: §17 tiene 0 marcadores y las demás entradas solo comparecen en la tabla de §71.14.

### H3 — Los flags por campo están completos y actualizados en las 41 entradas (derivada)

Estado de la evidencia: **no del todo**. Hay un campo ausente ([39] no registra `Citada en el informe`), cinco campos desactualizados ([9], [14], [18], [26] y [29] en el sentido de H2), una ubicación incompleta en [1], una contradicción de estado entre el flag de [39] y §18/§70, y una generalización en §70 que no se sostiene campo por campo (solo [1], [10], [12] y [39] llevan `(metadata incomplete)`). Los metadatos bibliográficos propiamente dichos —autores, año, revista, DOI y conteos de citas— no fueron re-verificados en esta iteración y no se ha constatado cambio alguno en ellos.

### H4 — Las fuentes institucionales [39]–[41] están representadas de forma coherente entre §18, §70, §71.14 y el anexo (derivada)

Estado de la evidencia: **[40] y [41] coherentes; [39] parcial**. ANFAC y AEADE aparecen con el mismo tipo de fuente, el mismo estado sin flag y la misma denominación «fuente institucional en §70» en el anexo, y con verificación en vivo declarada en §18; sus glosas omiten otras ubicaciones pero no contradicen ningún campo. DfT/DVLA es la excepción: §18 declara verificación en vivo de la URL profunda y §70 la incluye entre las referencias verificadas externamente, mientras su entrada [39] lleva `(metadata incomplete: URL profunda no confirmada)` y carece del campo `Citada`. La coherencia estructural de las tres es la misma —sin marcador numérico y fuera de la tabla de 38 filas de §71.14—, pero el documento no declara explícitamente que [39]–[41] sean un bloque aparte. No se re-fetchó ninguna URL en esta pasada.

## Sources used

- WebSearch queries: 0 (re-visación dirigida; sin búsquedas temáticas nuevas).
- WebFetch URLs: 0 en esta iteración; no se re-verificaron en vivo GOV.UK, anfac.com ni aeade.net.
- Semantic Scholar API hits: 0.
- OpenAlex API hits: 0 nuevos; los conteos y verificaciones se reutilizan del mapa E2 de la pasada 1 (fetched 2026-11-27) y de `Data/referencias.md`.
- Archivos locales inspeccionados: `Data/referencias.md` (líneas 3–6, entradas [1]–[41]); copia en caché `.playground/audit-cache/informe-tecnico-2026-11-28-iter4/informe-tecnico-2026-11-28-iter4.text.md` (§17, líneas 811–832; §18, líneas 834–853; §19, línea 861; §34, línea 1080; §70, líneas 1495–1499; §71.6, línea 1549; §71.14, líneas 1557–1600); `reviews/informe-tecnico-2026-11-28-iter4.plan.md` (22 líneas); `reviews/informe-tecnico-2026-11-27-iter3.e2-literature.md` (nota de entrada, H2 y lista de obras ausentes).
- Degradación: `degraded: false` para el mandato recibido —las 41 entradas, los marcadores de las secciones pedidas, los flags por campo y las tres fuentes institucionales quedaron resueltos por inspección directa—. Limitación declarada: sin búsqueda bibliográfica nueva, sin re-lectura de resúmenes y sin re-fetch de URLs; este mapa sirve para coherencia interna de marcadores y flags, no para proponer obras adicionales ni para certificar enlaces.

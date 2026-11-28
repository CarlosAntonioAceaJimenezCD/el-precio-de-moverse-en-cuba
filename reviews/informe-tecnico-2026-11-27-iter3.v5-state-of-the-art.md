---
type: audit-artifact
phase: v5-state-of-the-art
slug: informe-tecnico-2026-11-27-iter3
generated_at: 2026-11-28T02:30:00-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter3/informe-tecnico-2026-11-27-iter3.text.md
language: es
level: master
---

- Cobertura: 5 de 38 trabajos citados por nombre (13,2 %, frente a 1/38 en la iteración 2); los cuatro clústeres principales y adyacentes tienen al menos una mención y solo el de frontera queda en 0/3, lejos del tramo 25–60 de `V5.coverage_breadth.master`.
- Actualidad: 18 de 38 referencias (47,4 %) son de 2022–2026 y 3 de 5 menciones en el cuerpo (60 %) son de 2024–2026, por encima del 40 % de `V5.recency.master`, pero concentradas en §71.6.
- Peso y ausencias: 10 de 16 afirmaciones load-bearing sin cita externa y 0 marcadores `[N]`; la lista de ausencias probables baja de 8 a 7 y 21 de los 23 trabajos del top-5 por clúster siguen fuera del texto.

### F-V5-001 — Cobertura por clúster — 5 de 38 trabajos citados por nombre; solo el clúster de frontera sin representación

El mapa E2 vigente reparte 38 trabajos en cinco clústeres: asimetría de información y calidad (8), modelos de precio, regresión hedónica y depreciación (12), ética/legalidad/procedencia/calidad de datos (8), Cuba/divisas/movilidad/asequibilidad (7) y señales de precio en marketplaces (3). Tras la §71.6 (L1518–1520) el cuerpo nombra cinco: Akerlof [1] en §17 (L797), §19 (L841) y §70 (L1477); Gegić [14] y Du [9] en §71.6 (L1520), del clúster de modelos de precio; Muça [26] en el mismo párrafo, del clúster de ética/procedencia; y Vidal Alejandro [29], del clúster de Cuba. La distribución es 1/8, 2/12, 1/8, 1/7 y 0/3: 5 de 38 (13,2 %) frente a 1 de 38 (2,6 %) en la iteración 2.

E2 de esta iteración define «Cited in document» como mención nominal (L16), de modo que la presencia de las 38 entradas en `Data/referencias.md` no equivale a cobertura en el argumento. El criterio `V5.coverage_breadth.master` se lee: «Main + adjacent clusters covered (25–60 papers)». Cinco menciones nominales quedan por debajo del tramo incluso antes de descontar el clúster 5, que es de frontera y no exigible en nivel master. El cambio estructural frente a la iteración 2 es que los cuatro clústeres principales y adyacentes pasan de 0–1 menciones a al menos una cada uno; la magnitud absoluta no cambia de régimen.

— polarity: negative · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#F-V5-003]] · criteria: V5.coverage_breadth.master

### F-V5-002 — Actualidad — 18 de 38 referencias de los últimos cinco años y 3 de 5 menciones en el cuerpo

La tabla de distribución de E2 iter3 (L78–85) registra en la bibliografía numerada seis entradas de 2026 ([9], [10], [11], [24], [26], [35]), una de 2025 ([22]), seis de 2024 ([18], [25], [28], [29], [30], [32]), cuatro de 2023 ([15], [23], [27], [34]), una de 2022 ([17]) y veinte de 2021 o antes. El tramo 2022–2026 suma 18 de 38 (47,4 %), por encima del 40 % del criterio `V5.recency.master` —«At least 40% from the last 5 years; foundational classics balanced»—; esta proporción es idéntica a la de la iteración 2 porque el aparato numerado no se modificó.

En el cuerpo, las cinco menciones nominales son Akerlof 1970 [1] y las cuatro de §71.6: Muça [26] y Du [9] de 2026, Vidal Alejandro [29] de 2024 y Gegić [14] de 2019. Tres de cinco (60 %) son de los últimos cinco años, frente a 0 de 1 (0 %) en la iteración 2; los dos clásicos —1970 y 2019— aportan el equilibrio que el mismo criterio describe. La mejora se localiza en un apartado de cumplimiento de estándares (§71.6, L1518–1520) situado al final del documento: las secciones analíticas §17–§20 (L787–871), §34 (L1016–1052) y §59–§60 (L1377–1391) no incorporan a estas cuatro obras. El seguimiento de preprints de los últimos 18 meses no es exigible en nivel master; [24] (Hohensinner et al. 2026, arXiv:2601.14311) permanece en la bibliografía sin mención en el cuerpo.

— polarity: positive · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#F-V5-005]] · criteria: V5.recency.master

### F-V5-003 — Peso de la citación — cuatro vecinos académicos con autor y año en un apartado propio

§71.6 (L1520) abre un apartado titulado «Posicionamiento frente a trabajos cercanos / Positioning against prior work» con cuatro cláusulas contrastivas, una por trabajo: «Frente a Gegić, Isaković, Keco, Mašetić y Kevrić (2019)…», «Frente a Muça, Bani y Alla (2026)…», «Frente a Du, Yang, Zhang, Li y Liu (2026)…» y «Frente a Vidal Alejandro, Muñiz-Cuza y Calas Torres (2024)…». Cada cláusula describe el trabajo ajeno y enuncia un diferenciador propio —procedencia y normalización, conversión con TRMI fechada, no estimación de tasa anual, tasa informal como convención—. El criterio `V5.citation_weight.master` exige «Load-bearing claims cite source + author named in body at first mention»: los cuatro autores quedan identificados por nombre en su primera mención, y E1 registra el bloque como afirmación load-bearing C016 (L199–209).

La calificación es parcial: las cuatro comparaciones comparten un único párrafo, sin marcadores `[14]`, `[26]`, `[9]` ni `[29]`, y la búsqueda de marcadores `[N]` en el cuerpo devuelve 0 coincidencias (E2 iter3, L87). §70 (L1477) enumera como «referencias citadas y verificadas externamente» solo Akerlof y tres fuentes institucionales, de modo que los cuatro vecinos figuran en el anexo numerado pero no en esa enumeración. E2 (H3, L116–118) describe el apartado como discusión dedicada de forma, sin cifras de los trabajos ajenos ni discusión de resultados o limitaciones.

— polarity: positive · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#C016]] · criteria: V5.citation_weight.master

### F-V5-004 — Peso de la citación — 10 de 16 afirmaciones load-bearing sin cita externa y ningún marcador numérico en el cuerpo

El inventario de E1 de esta iteración contiene 126 afirmaciones, 16 de ellas load-bearing (L13–14). Diez conservan «External evidence cited: — (sin citas numeradas)» —C001–C006, C008, C010, C013 y C015 (L27, L39, L51, L63, L75, L87, L111, L135, L171, L195)—. Cinco remiten a fuentes institucionales o de ingeniería —C007 y C009 a DfT/DVLA, ANFAC y AEADE; C011, C012 y C014 al repositorio `Egyptian-Used-Cars`— y solo C016 nombra a los cuatro pares académicos de §71.6. La proporción sin evidencia externa es 10/16 (62,5 %), frente a 9/13 (69,2 %) en la iteración 2.

El aparato numerado de 38 entradas no se enlaza al texto: 0 marcadores `[N]` en las 1.523 líneas (E2 iter3, L87), y los cuatro flags actualizados a «sí (mención nominal en §71.6, sin marcador numérico)» (L24, L34, L58, L64) consignan esa misma ausencia en la ficha. El criterio `V5.citation_weight.master` —«Load-bearing claims cite source + author named in body at first mention»— queda satisfecho en su mitad nominal para C016 y sin satisfacer en las diez afirmaciones sin cita externa.

— polarity: negative · confidence: high · related: [[#C001]], [[#C016]], [[#F-V5-003]] · criteria: V5.citation_weight.master

### F-V5-005 — Ausencias probables — la lista baja de ocho a siete obras; Gegić queda dentro y las siete restantes fuera del cuerpo

E2 iter3 reduce la lista de «Likely missing important works» de ocho a siete (L98–100): retira Gegić et al. 2019 [14], que tiene comparación nominal en §71.6, y conserva Lewis 2011 [2] (342 citas), Englmaier et al. 2017 [4] (50), Krotov et al. 2020 [21] (224), Priestley et al. 2023 [23] (153), Brown et al. 2025 [22] (118), Guerra 2015 [33] (113) y Hohensinner et al. 2026 [24] (13). Las siete mantienen «Citada en el informe: no» en `Data/referencias.md` (L10, L14, L48, L50, L52, L54, L72) y ninguna aparece en el cuerpo.

La relación con afirmaciones cargadas se mantiene: Lewis es el eslabón empírico entre Akerlof y la captura de defectos y tipo de vendedor (E2 pasada 1, L495); Englmaier advierte sobre saltos en umbrales de año y 10.000 km frente a la retirada de la pendiente anual en §59–§60 (L1381, L1389); Krotov y Brown corresponden a la regla de no eludir anti-automatización de §10 (L118); Priestley a la arquitectura de colas y cuarentena de la fase 7; Guerra a `asequibilidad = precio / salario`; Hohensinner a la distinción entre procedencia y linaje. El criterio `V5.missing_important_work.master` se lee: «Top-5 most-cited of each adjacent cluster expected». De las 23 obras distintas que forman los top-5 por clúster, dos están citadas por nombre —Akerlof [1] y Gegić [14]— y 21 ausentes (91,3 %), frente a 22 (95,7 %) en la iteración 2.

— polarity: negative · confidence: high · related: [[#P001]], [[#F-V5-001]] · criteria: V5.missing_important_work.master

### F-V5-006 — Flags por campo — cuatro fichas de citación alineadas con §71.6 y tres marcadores con el campo nominal

`Data/referencias.md` actualiza las fichas [9], [14], [26] y [29] a «Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)» (L24, L34, L58, L64), en correspondencia con el campo definido en L6 como «mención nominal en el informe». E2 (H2, L112–114) constata que los cuatro flags estaban desactualizados porque el archivo se generó antes de existir §71.6 y que autores, año, revista, DOI y conteo de citas permanecen verificados.

Los tres marcadores `(metadata incomplete)` restantes nombran el campo ausente: «resumen indexado no sustantivo» en [1] (L8), «resumen no indexado; campos bibliográficos verificados» en [10] (L26) y «resumen no indexado en OpenAlex; discrepancia de año documentada» en [38] (L82). Las notas de discrepancia de año de [2], [19] y [38] permanecen. Frente a los seis marcadores genéricos sin campo de la iteración 2, la ficha distingue ahora entre dato ausente y dato recuperado: [18], [19] y [20] consignan conteos de citas verificados y versión publicada (L42, L44, L46). Esta distinción es la que permite ponderar el peso de cada entrada del aparato al calibrar `V5.citation_weight.master`.

— polarity: positive · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#F-V5-004]] · criteria: V5.citation_weight.master

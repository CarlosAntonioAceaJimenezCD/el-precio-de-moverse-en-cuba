---
type: audit-artifact
phase: v5-state-of-the-art
slug: informe-tecnico-2026-11-28-iter4
generated_at: 2026-11-28T03:13:16-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-28-iter4/informe-tecnico-2026-11-28-iter4.text.md
language: es
level: master
---

- Cobertura: seis de 38 trabajos del mapa llevan marcador en prosa de cuerpo (15,8 %, frente a cinco en la iteración 3); los cuatro clústeres principales y adyacentes tienen al menos una mención, pero el de señales sigue en 0/3 y el total queda lejos del tramo 25–60 de `V5.coverage_breadth.master`.
- Actualidad: 18 de 38 referencias fechadas (47,4 %) son de 2022–2026 y cuatro de seis citas en cuerpo (66,7 %) son recientes, por encima del 40 % de `V5.recency.master`, con clásicos balanceados.
- Peso y ausencias: §71.6 incorpora cuatro marcadores y satisface «fuente + autor» en C013, pero 12 de 15 afirmaciones load-bearing (80 %) siguen sin cita externa; las siete ausencias probables se mantienen y el anexo queda en 9 fichas `sí` / 32 `no`.

### F-V5-001 — Cobertura por clúster — seis de 38 trabajos con marcador en el cuerpo; el clúster de señales permanece en 0/3

La tabla de §71.14 (L1559–L1600) reparte 38 trabajos numerados en cinco clústeres: asimetría de información 8 ([1]–[8]), modelos de precio, regresión hedónica y depreciación 12 ([9]–[20]), ética/legalidad/procedencia/calidad de datos 8 ([21]–[28]), Cuba/divisas informales/movilidad/asequibilidad 7 ([29]–[35]) y señales de precio en marketplaces 3 ([36]–[38]). En prosa de cuerpo aparecen seis con marcador: [1] en §19 (L861) y mención nominal en §17 (L817); [9], [14], [26] y [29] en §71.6 (L1549); y [18] en §34 (L1080). La distribución es 1/8, 3/12, 1/8, 1/7 y 0/3: 6 de 38 (15,8 %), frente a 5 de 38 (13,2 %) en la iteración 3.

El criterio `V5.coverage_breadth.master` exige «Main + adjacent clusters covered (25–60 papers)». Seis menciones quedan por debajo del tramo incluso descontando el clúster 5, que es de frontera y no exigible en nivel master. El cambio respecto de la iteración 3 es de régimen interno, no de escala: los cuatro clústeres principales y adyacentes pasan a estar todos representados y [18] se suma al recuento, pero ningún trabajo nuevo entra en el argumento. El E2 de esta iteración es una re-verificación dirigida —nueve entradas re-visadas, cero búsquedas nuevas (L16, L227–234)—, por lo que hereda los recuentos de clúster y no puede ampliar la cobertura. La tensión estructural señalada en E2 (L200) persiste: §71.14 se titula «Obras del mapa literario citadas en el cuerpo» y cierra diciendo que «el resto se registra aquí con su marcador numérico», mientras el anexo registra 32 entradas con `Citada: no`; tabla y flag describen estados distintos. El anexo tiene además 41 entradas, aunque §70 (L1497, L1499) hable de «38 referencias» y la tabla se detenga en [38].

— polarity: negative · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#P005]], [[#P006]], [[#F-V5-004]] · criteria: V5.coverage_breadth.master

### F-V5-002 — Actualidad — 18 de 38 referencias de los últimos cinco años y 4 de 6 citas en el cuerpo

La distribución de E2 iter4 (L160–170) coincide con `Data/referencias.md`: seis entradas de 2026 ([9], [10], [11], [24], [26], [35]), una de 2025 ([22]), seis de 2024 ([18], [25], [28], [29], [30], [32]), cuatro de 2023 ([15], [23], [27], [34]), una de 2022 ([17]) y veinte de 2021 o antes; tres institucionales ([39]–[41]) no tienen año. El tramo 2022–2026 suma 18 de 38 referencias fechadas (47,4 %) y 18 de 41 entradas del anexo (43,9 %). El criterio `V5.recency.master` —«At least 40% from the last 5 years; foundational classics balanced»— queda satisfecho por ambas medidas. El equilibrio de clásicos también se sostiene: 20 de 38 entradas fechadas son de 2021 o antes, entre ellas Akerlof 1970 [1], Hulten 2003 [12], Wolf 2005 [6], Ritter 2004 [31] y Guerra 2015 [33].

En el cuerpo, de las seis obras con marcador, cuatro son recientes —Du [9] 2026, Muça [26] 2026, Madhusudhanan [18] 2024 y Vidal Alejandro [29] 2024— y dos son los contrapesos clásicos —Akerlof [1] 1970 y Gegić [14] 2019—: 4 de 6 (66,7 %). La mejora se concentra en §71.6 y en el marcador añadido en §34; las secciones analíticas §17–§20, §59–§60 siguen sin incorporar la literatura reciente. [24] (Hohensinner et al. 2026, arXiv:2601.14311) está en el anexo y cae dentro de los últimos 18 meses, pero no se discute en el cuerpo; el seguimiento de preprints recientes es exigible en nivel phd, no en master, de modo que no se emite hallazgo por ese hecho.

— polarity: positive · confidence: high · related: [[#P001]], [[#P003]], [[#P004]], [[#P006]], [[#C013]], [[#F-V5-005]] · criteria: V5.recency.master

### F-V5-003 — Peso de la citación — §71.6 convierte cuatro comparaciones en citas load-bearing con autor y marcador

El párrafo de §71.6 (L1549) lleva ahora los marcadores `[14]`, `[26]`, `[9]` y `[29]` junto al nombre de cada autor en su primera mención. E1 lo inventaría como C013 (L163–L171), afirmación load-bearing de tipos `novelty` y `citation-grounded`, con evidencia externa explícita: «[14] Gegić (2019), [26] Muça (2026), [9] Du (2026), [29] Vidal Alejandro (2024), según las fichas de §71.14». Cada cláusula describe el trabajo ajeno y enuncia un diferenciador propio —procedencia y normalización frente a Gegić, conversión con TRMI fechada frente a Muça, no estimación de tasa anual frente a Du, tasa informal como convención frente a Vidal Alejandro—. En §34 (L1080), los marcadores `[14]` e `[18]` respaldan la frase sobre los antecedentes de predicción sobre catálogos estructurados.

El criterio `V5.citation_weight.master` —«Load-bearing claims cite source + author named in body at first mention»— queda satisfecho para C013 y para la remisión de §34: la mitad nominal ya estaba cubierta en la iteración 3 y en esta se añade la mitad numérica. Es el cambio sustantivo de la iteración y constituye un hallazgo positivo de calibración de peso, no solo de formato: las cuatro obras vecinas funcionan como comparación load-bearing y no como entrada decorativa de una lista.

— polarity: positive · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#C013]], [[#F-V5-004]] · criteria: V5.citation_weight.master

### F-V5-004 — Peso de la citación — 12 de 15 afirmaciones load-bearing sin cita externa y 38 marcadores que operan como registro

El resumen de E1 iter4 (L13–15) contabiliza 125 afirmaciones, 15 de ellas load-bearing. De esas 15, doce —C001–C008, C010, C011, C014 y C015— registran «External evidence cited: — (sin citas numeradas)» o equivalente (L27, L39, L51, L63, L75, L87, L99, L111, L135, L147, L183, L195): 12/15 (80 %). Solo C009 remite a [1] y a las tres fuentes institucionales según §70 (L123), C012 a DfT/DVLA y ANFAC/AEADE declarados en §18 (L159), y C013 a los cuatro vecinos de §71.6 (L171). Las afirmaciones cargadas de contenido analítico —hipótesis H1, cifras de la corrida, ablación, intervalo bootstrap, semilla, novedad declarada— siguen apoyadas únicamente en evidencia interna.

Los 38 marcadores de la tabla de §71.14 son un registro, no una discusión: ninguna de las 32 entradas con `Citada: no` se analiza en el cuerpo y §17 (L811–L832) tiene cero marcadores. El anexo fue actualizado a las 03:04, después de que se generara E2 a las 03:02: [9], [14], [26] y [29] pasan a «sí (§71.6 y §71.14)», [18] a «sí (§71.14)» y [39] gana el campo «sí (§70 y §71.14)». La alineación mejora la ponderación, pero quedan dos imprecisiones de ubicación: la ficha de [18] omite §34, donde tiene marcador, y la de [39] invoca §71.14 aunque la tabla termina en [38]. Además, §70 generaliza que «las fuentes restantes figuran con estado `(metadata incomplete)`» cuando solo cuatro entradas ([1], [10], [12] y [39]) llevan esa marca. Con el criterio `V5.citation_weight.master` aplicado al conjunto, la condición de «fuente + autor» se cumple en tres de quince afirmaciones y falta en el resto.

— polarity: negative · confidence: high · related: [[#C001]], [[#C009]], [[#C012]], [[#C013]], [[#F-V5-001]], [[#F-V5-003]] · criteria: V5.citation_weight.master

### F-V5-005 — Ausencias probables — siete obras siguen fuera del cuerpo y el criterio master espera el top-5 por clúster adyacente

E2 iter4 (L203–205) mantiene las siete obras arrastradas de la iteración 3 —Lewis 2011 [2], Englmaier et al. 2017 [4], Krotov et al. 2020 [21], Priestley et al. 2023 [23], Brown et al. 2025 [22], Guerra 2015 [33] y Hohensinner et al. 2026 [24]— y no propone adicionales. Las siete conservan `Citada en el informe: no` en `Data/referencias.md` (L10, L14, L48, L50, L52, L54, L72) y ninguna aparece en el cuerpo; Gegić [14] queda fuera de la lista porque sí tiene comparación en §71.6 y marcadores en §71.6 y §34.

La relación con afirmaciones load-bearing se mantiene: Lewis es el eslabón empírico entre Akerlof y la captura de defectos y tipo de vendedor (C009); Englmaier advierte sobre saltos en umbrales de año y 10.000 km frente a la retirada de la pendiente anual en §59–§60 (C003); Krotov y Brown corresponden a la regla de no eludir anti-automatización de §10; Priestley a la arquitectura de colas y cuarentena de la fase 7; Guerra a la operacionalización de `asequibilidad = precio / salario`; y Hohensinner a la distinción entre procedencia y linaje que §71.15 declara como aporte. El criterio `V5.missing_important_work.master` exige «Top-5 most-cited of each adjacent cluster expected»; la medición de la iteración 3 —última con búsquedas temáticas— situaba 21 de 23 obras del top-5 por clúster (91,3 %) fuera del texto. Esta iteración no ejecutó búsquedas ni re-lectura de resúmenes, por lo que la lista se hereda sin verificación independiente y la ausencia de obras adicionales se afirma con confianza media.

— polarity: negative · confidence: medium · related: [[#P001]], [[#P003]], [[#F-V5-002]], [[#F-V5-004]] · criteria: V5.missing_important_work.master

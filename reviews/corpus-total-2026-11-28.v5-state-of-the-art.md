---
type: audit-artifact
phase: v5-state-of-the-art
slug: corpus-total-2026-11-28
generated_at: 2026-11-28T21:25:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/corpus-total-2026-11-28/corpus-total-2026-11-28.text.md
language: es
level: master
---

- Cobertura: 41/41 obras del anexo presentes en el corpus (100 %) y 7 clústers representados, dentro del tramo 25–60 de `V5.coverage_breadth.master`; la tabla §71.14 cubre 38/41.
- Actualidad: 18/41 (43,9 %) de 2022–2026 —47,4 % de las 38 fechadas— por encima del 40 % de `V5.recency.master`; 20/41 son clásicos ≤2021.
- Peso y ausencias: 5/41 discutidas en §71.6 y 8/41 nombradas en prosa; 33/41 solo en listas; E2 sin búsquedas nuevas deja 0 obras externas verificables y dos ausencias internas ([12], [39]).

### F-V5-001 — Cobertura — 41 de 41 obras del anexo presentes en el corpus, frente a 0/41 de la pasada anterior

El README enumera las 41 entradas `[1]`–`[41]` en las líneas 1716–1757 del cache, y E2 certifica correspondencia **41/41** prefijo-a-prefijo contra `Data/referencias.md` (E2 L19, L509–L522): mismos números, autores, títulos y años visibles, sin reordenación, duplicados ni huecos. El anexo (L2505–L2584) conserva la resolución completa de DOI y URL que el README trunca en 38 de 41 casos. Con la incorporación del README al corpus, las 41 obras pasan de estar ausentes del texto a formar parte de la bibliografía del documento auditado: la medición anterior registraba 0/41 (`corpus-documentacion-2026-11-28.v5-state-of-the-art.md` L11, L15–L21).

El criterio `V5.coverage_breadth.master` se lee: «Main + adjacent clusters covered (25–60 papers)». El valor observado, 41, cae dentro del tramo y duplica el mínimo; el cambio respecto de la pasada anterior es de régimen de citas —un anexo desconectado del texto pasa a ser una lista pública numerada—, no de incorporación de obras nuevas. La cobertura se mide aquí como presencia en la bibliografía; el peso argumental se mide en F-V5-004 y F-V5-005.

— polarity: positive · confidence: high · related: [[#P001]], [[#P041]], [[#F-V5-002]], [[#F-V5-005]] · criteria: V5.coverage_breadth.master

### F-V5-002 — Cobertura por clúster — siete clústers representados; 20 main, 18 adyacentes y 3 de frontera

Los siete clústers del mapa E2 (L21–L508) están cubiertos sin huecos: asimetría de información 8/8 (`[1]`–`[8]`), modelos de precio y predicción 12/12 (`[9]`–`[20]`), ética/legalidad/procedencia 8/8 (`[21]`–`[28]`), Cuba/divisas 4/4 (`[29]`–`[32]`), propiedad y asequibilidad 3/3 (`[33]`–`[35]`), señales de marketplace 3/3 (`[36]`–`[38]`) y fuentes institucionales foráneas 3/3 (`[39]`–`[41]`). La distribución es 20/41 main (48,8 %), 18/41 adyacente (43,9 %) y 3/41 de frontera (7,3 %).

La tabla «Obras del mapa literario citadas en el cuerpo» (§71.14, L1568–L1607) tabula únicamente `[1]`–`[38]`; los tres ítems institucionales están en §70 (L1504–L1508) y en el README (L1755–L1757), pero no en esa tabla. En nivel master la presencia del clúster de frontera no es exigible —lo es en phd—, de modo que su inclusión se registra como exceso de cobertura sobre el criterio, y la ausencia de `[39]`–`[41]` de la tabla como discrepancia de alcance, no de cobertura.

— polarity: neutral · confidence: high · related: [[#P012]], [[#P039]], [[#P040]], [[#P041]], [[#F-V5-001]], [[#F-V5-006]] · criteria: V5.coverage_breadth.master

### F-V5-003 — Actualidad — 18 de 41 referencias de los últimos cinco años (43,9 %) y 20 clásicas de 2021 o antes

La distribución de E2 (L524–L536) registra 6 entradas de 2026, 1 de 2025, 6 de 2024, 4 de 2023, 1 de 2022, 20 de 2021 o antes y 3 sin año verificable (`[39]`–`[41]`). El tramo 2022–2026 suma **18/41 = 43,9 %** del total y **18/38 = 47,4 %** de las referencias con año. El bloque fundacional es 20/41 (48,8 % del total; 52,6 % de las fechadas) e incluye Akerlof 1970 `[1]`, Hulten 2003 `[12]`, Ritter 2004 `[31]`, Wolf 2005 `[6]`, Sultan 2009 `[7]` y Tilles 2011 `[8]`.

El criterio `V5.recency.master` exige «At least 40% from the last 5 years; foundational classics balanced». La bibliografía del corpus cumple ambos componentes con cualquiera de las dos denominaciones (43,9 % sobre 41 o 47,4 % sobre 38), y el equilibrio se observa en la convivencia de seis obras de 2026 con seis clásicas anteriores a 2012. La fecha más reciente declarada, 2026, corresponde a `[9]`, `[10]`, `[11]` y `[24]`, y a las tres fuentes institucionales sin año.

— polarity: positive · confidence: high · related: [[#P001]], [[#P009]], [[#P012]], [[#P024]], [[#F-V5-007]] · criteria: V5.recency.master

### F-V5-004 — Peso de la citación — cinco obras load-bearing con autor nombrado en la primera mención en §71.6

El apartado «Posicionamiento frente a trabajos cercanos» (§71.6, L1556–L1558) nombra y contrasta cuatro trabajos en sendas oraciones: «Gegić y otros [14] predicen precios con aprendizaje automático sobre catálogos estructurados; aquí las variables se extraen de anuncios en lenguaje libre», «Muça, Bani y Alla [26] integran datos públicos albaneses por scraping; en este trabajo el énfasis está en la conversión con TRMI fechada», «Du y otros [9] modelan depreciación no lineal y heterogeneidad de marca» y «Vidal Alejandro y otros [29] estudian el mercado informal de divisas en Cuba; aquí esa tasa es una convención de conversión fechada». §70 (L1504–L1508) añade a «Akerlof (1970), *The Market for "Lemons"* (DOI 10.2307/1879431 confirmado en OpenAlex)» entre las referencias verificadas.

El criterio `V5.citation_weight.master` se lee: «Load-bearing claims cite source + author named in body at first mention». En los cinco pasajes de posicionamiento el autor aparece en la primera mención y la obra sostiene una afirmación contrastiva con el aporte propio —procedencia, normalización con TRMI fechada y pérdida de muestra—; el peso está, por tanto, calibrado en el subconjunto que efectivamente argumenta.

— polarity: positive · confidence: high · related: [[#P001]], [[#P009]], [[#P014]], [[#P026]], [[#P029]], [[#F-V5-005]] · criteria: V5.citation_weight.master

### F-V5-005 — Peso de la citación — 33 de 41 obras aparecen solo en enumeraciones y seis se declaran «más próximas» frente a cinco discutidas

Fuera de los cinco trabajos de §71.6 y del bloque verificado de §70 —Akerlof `[1]` y las instituciones `[39]`–`[41]`—, las 33 restantes (80,5 %) comparecen únicamente en la lista numerada del README (L1717–L1757), en la tabla de §71.14 (L1570–L1607) o en ambas, sin mención nominal en prosa. El README declara seis «más próximos» en L1716 —`[1]`, `[9]`, `[12]`, `[14]`, `[26]` y `[29]`— mientras §71.6 discute cinco; el desajuste se localiza en `[12]` Hulten 2003, presente en la tabla (L1581) y ausente del párrafo de posicionamiento.

El criterio `V5.citation_weight.master` no exige que toda obra listada sea load-bearing —esa exigencia aparece en `V5.citation_weight.phd` y `.paper`—, por lo que la concentración del peso en 5/41 (12,2 %) y en 8/41 nombradas (19,5 %) se registra como distribución observada, no como incumplimiento del nivel. La declaración de «41 referencias y trabajos cercanos» (L1716) describe la lista, no el número de obras activadas en el argumento.

— polarity: neutral · confidence: high · related: [[#P012]], [[#P021]], [[#P040]], [[#F-V5-004]], [[#F-V5-006]] · criteria: V5.citation_weight.master

### F-V5-006 — Ausencias probables — cero obras externas verificables y dos ausencias internas en `[12]` y `[39]`

E2 declara `queries_run: 0` y no propone obras externas: «cualquier candidato "ausente de la bibliografía" sería **no verificable** en esta pasada» (L547–L549). Las dos ausencias registradas son de alcance documental. `[39]` DVLA/Vehicle statistics aparece en §70 (L1506/L1508) y en el README (L1755), pero el anexo afirma `Citada en el informe: sí (§70 y §71.14)` mientras la tabla de §71.14 solo contiene `[1]`–`[38]` (E2 L551–L555). `[12]` Hulten 2003 está entre los «más próximos» del README (L1716) y en la tabla (L1581), pero queda fuera de los cinco trabajos que §71.14 dice discutidos en §71.6 (L1609; E2 L557–L561). `[12]` toca el modelo hedónico de §71.2 (L1531) y el clúster 2, el de mayor densidad del mapa.

El criterio `V5.missing_important_work.master` exige «Top-5 most-cited of each adjacent cluster expected». Sin búsqueda temática ni re-fetch, la escala de relevancia de posibles ausencias externas no está verificada en esta pasada, de modo que no se emite hallazgo sobre obras no citadas: las dos anomalías conciernen a la localización de obras ya presentes y su efecto se concentra en el peso de `[12]` (F-V5-005).

— polarity: negative · confidence: medium · related: [[#P012]], [[#P039]], [[#P022]], [[#F-V5-002]], [[#F-V5-005]] · criteria: V5.missing_important_work.master

### F-V5-007 — Preprints — cuatro entradas arXiv, una de enero de 2026, ninguna activada en §71.6 o §70

La bibliografía incluye `[18]` ProbSAINT, arXiv:2403.03812 (2024; 13 citas heredadas según E2 L228), `[19]` arXiv:1711.06970 (2017; 96 citas), `[20]` arXiv:2101.03788 (2021; 9 citas) y `[24]` Tracing the Data Trail, arXiv:2601.14311 (2026; manuscrito enviado, estado no re-verificado en esta pasada, E2 L294–L303). `[24]` cae dentro de los 18 meses anteriores a noviembre de 2026 y `[18]` dentro de los tres años; ninguno de los cuatro figura en el párrafo de posicionamiento de §71.6 ni entre las referencias verificadas de §70.

El criterio `V5.recency.master` no exige seguimiento de preprints —la expectativa de «last 12–18 months of arXiv preprints» aparece en `V5.recency.phd`—, por lo que su sola presencia se registra sin valoración de incumplimiento. La contribución temática de `[24]` (procedencia y trazabilidad) coincide con el diferenciador declarado en L1758, pero permanece como entrada de lista.

— polarity: neutral · confidence: medium · related: [[#P018]], [[#P019]], [[#P020]], [[#P024]], [[#F-V5-003]], [[#F-V5-005]] · criteria: V5.recency.master

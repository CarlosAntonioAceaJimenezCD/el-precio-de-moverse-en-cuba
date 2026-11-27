---
type: audit-artifact
phase: v5-state-of-the-art
slug: informe-tecnico-2026-11-27
generated_at: 2026-11-27T05:53:51Z
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27/informe-tecnico-2026-11-27.text.md
language: es
level: master
---

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

---
type: audit-artifact
phase: v5-state-of-the-art
slug: informe-tecnico-2026-11-27-iter2
generated_at: 2026-11-27T17:25:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter2/informe-tecnico-2026-11-27-iter2.text.md
language: es
level: master
---

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

---
type: audit-artifact
phase: v8-bibliography
slug: informe-tecnico-2026-11-27-iter3
generated_at: 2026-11-28T01:23:04-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter3/informe-tecnico-2026-11-27-iter3.text.md
language: es
level: master
bibliography_entries_total: 38
verified: 36
unverified: 2
---

- 33 DOI y 4 arXiv resuelven y coinciden con el título declarado; sin duplicados ni papers fantasma. Los cuatro flags de §71.6 ya están corregidos en `Data/referencias.md`, con `[1]` en inglés como única desviación de forma.
- La contradicción Akerlof quedó resuelta en §70 ES y en `[1]` (flag por campo: resumen), pero §70 EN y el claim C009 reproducen la versión sin calificar; los conteos de E2 presentan un desfase de +2 en Gegić.
- Dos entradas sin DOI quedan sin verificación de contenido en esta pasada: `[6]` (HTTP 403) y `[31]` (HTTP 404, con la obra identificada en OpenAlex y rutas alternativas).

### F-V8-001 — 33 DOI y cuatro arXiv resuelven; ningún duplicado ni paper fantasma

`Data/referencias.md` contiene 38 entradas numeradas `[1]`–`[38]`, todas con autores nominales y una sola plantilla (autores, título en cursiva, venue, año, DOI/URL, campo `Citada en el informe`). Los 33 tokens `10.\d{4,9}/…` son únicos y pasan el patrón; `https://api.crossref.org/works/<DOI>` devolvió HTTP 200 para los 33 con títulos coincidentes con la ficha, y `https://api.openalex.org/works/doi:<DOI>` devolvió el mismo título en cada caso. Incluye el DOI con punto inicial en el sufijo de `[27]`, `10.54660/.jfmr.2023.4.1.529-538`, que resuelve a «The Ethics of Web Scraping In Research: A Review: Investigating the Boundaries, Legal Implications, and Societal Acceptance of Web Scraping As a Data Collection Method».

Los cuatro identificadores de arXiv también resolvieron y coinciden con la ficha: `2403.03812` (ProbSAINT, enviado el 6/03/2024, con «Journal reference: IEEE BigData 2024 - Industry & Government Track» en la landing page), `1711.06970` («How much is my car worth? A methodology for predicting used cars prices using Random Forest»), `2101.03788` («Second Hand Price Prediction for Tesla Vehicles») y `2601.14311` («Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability in LLMs», prefijo enero 2026, anterior a la fecha del informe, 27/11/2026). Las versiones preprint/publicadas de `[18]` y `[19]` siguen representadas por una ficha cada una; no hay DOI repetido.

— polarity: positive · confidence: high · related: [[#C051]], [[#F-V8-002]]

### F-V8-002 — Los cuatro flags de §71.6 ya reflejan el cuerpo; 5 de 38 en «sí/yes»

E2 de esta iteración (L36, L48, L60, L72 y H2, L112–114) constató que `[9]`, `[14]`, `[26]` y `[29]` conservaban «Citada en el informe: no» pese a que §71.6 (L1518–1520) los nombra. En el archivo vigente, las líneas 24, 34, 58 y 64 de `Data/referencias.md` leen «Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)»; el `mtime` del archivo (28/11/2026 01:05:56 -04:00) es posterior al del artefacto E2 (01:03:37 -04:00). El recuento actual es cinco entradas positivas —`[1]` con `yes` y las cuatro con `sí`— y 33 con `no`, frente a 1/37 en la iteración 2.

La concordancia es con la definición declarada en `Data/referencias.md:6` —«`Citada: sí/no` indica mención nominal en el informe»— y no con una cita numerada: la búsqueda de `[1]`–`[38]` en el texto cacheado devuelve cero marcadores, como consigna E2 iter3 (L87). Cuatro de las cinco menciones nominales se concentran en el único párrafo de §71.6 (L1520); la quinta es Akerlof `[1]`, presente desde antes de esta iteración.

— polarity: positive · confidence: high · related: [[#C051]], [[#F-V8-003]], [[#F-V8-008]]

### F-V8-003 — `[1]` escribe «yes» frente a la convención «sí/no» del propio archivo

La cabecera define «`Citada: sí/no`» (`Data/referencias.md:6`) y las 37 fichas restantes usan `sí` o `no` en español. La entrada `[1]` (L8) es la única que escribe «Citada en el informe: yes.», mientras las cuatro fichas actualizadas en §71.6 escriben «sí (mención nominal en §71.6, sin marcador numérico)». Es una inconsistencia de forma acotada al campo de flag: autores, año, revista, DOI y año de publicación de `[1]` están confirmados en Crossref y OpenAlex (ver F-V8-004).

La marca literal `(metadata incomplete)` aparece solo en `[1]` y `[10]`; `[38]` (L82) registra su limitación en prosa —«Resumen no indexado en OpenAlex; discrepancia de año documentada: 2015 en OpenAlex, 2016 en Crossref (published-print)»— sin la marca. Las dos marcas vigentes son ya por campo: `[1]` «resumen indexado no sustantivo; identidad y DOI verificados en OpenAlex» y `[10]` «resumen no indexado; campos bibliográficos verificados».

— polarity: negative · confidence: high · related: [[#F-V8-002]], [[#F-V8-004]]

### F-V8-004 — Akerlof: contradicción resuelta en §70 ES y en `[1]`, abierta en §70 EN y en C009

La versión española de §70 (L1477) ya nombra el campo: «Akerlof (1970), *The Market for "Lemons"* (DOI 10.2307/1879431 confirmado en OpenAlex; el resumen indexado es solo un índice de secciones, por lo que su flag es `(metadata incomplete: resumen)`)». La ficha `[1]` (L8) coincide: «**(metadata incomplete: resumen indexado no sustantivo; identidad y DOI verificados en OpenAlex)**». La versión inglesa (L1479) conserva en cambio «Akerlof (1970), *The Market for "Lemons"* (Crossref/OpenAlex)» sin la calificación, y el claim C009 de E1 iter3 (L120) reproduce esa frase inglesa como evidencia de «Solo cuatro referencias están verificadas externamente» (L121).

La verificación de esta pasada: `https://api.crossref.org/works/10.2307/1879431` responde HTTP 200 con autor Akerlof, contenedor *The Quarterly Journal of Economics*, volumen 84, número 3, página 488 y `published` 1970-08; el error de transporte de la iteración 2 ya no se reproduce. `https://api.openalex.org/works/W2156109180` devuelve `cited_by_count: 32658` y un `abstract_inverted_index` que contiene solo el índice de secciones («I. Introduction, 488. — II. The model with automobiles as an example, 489. … V. Conclusion, 500.»). Las dos etiquetas —«verificada» y `(metadata incomplete)`— dejan de ser incompatibles cuando el flag alude al resumen y no a la identidad; la mitad inglesa del documento y C009 no registran esa distinción.

— polarity: negative · confidence: high · related: [[#C009]], [[#C051]], [[#F-V8-003]]

### F-V8-005 — Conteos de citas: desfase de dos en Gegić y aumentos de uno en tres fichas del mapa

E2 iter3 reutilizó para las cuatro comparaciones los conteos obtenidos el 27/11/2026: Gegić 188 (L30), Muça 0 (L42), Du 0 (L54) y Vidal Alejandro 1 (L66). La consulta actual a OpenAlex devuelve 190 para `W4288610071` (Gegić, +2), 0 para `W7204683515` (Muça), 0 para `W7225188457` (Du) y 1 para `W4403850866` (Vidal Alejandro). `Data/referencias.md` consigna conteos solo en `[18]` (13), `[19]` (96) y `[20]` (9): los tres se confirman hoy (OpenAlex `W4406461714` 13, `W2770052903` 96 y `arxiv:2101.03788` 9).

Otros desfases respecto del mapa E2 de la pasada 1 son `[10]` 2→3, `[15]` 40→41 y `[27]` 22→23; Akerlof permanece en 32658. Ningún conteo aparece en el documento auditado: la divergencia afecta a los artefactos de auditoría, no a una afirmación del informe. Los conteos son observaciones fechadas y no constantes bibliográficas.

— polarity: neutral · confidence: high · related: [[#C051]], [[#F-V8-002]]

### F-V8-006 — `[31]`: la URL declarada devuelve 404 aunque la obra existe

La entrada `[31]` (L68) declara «http://www.carleton.ca/economics/wp-content/uploads/cep04-12.pdf». Dos clientes independientes devuelven HTTP 404 para esa ruta, incluida la redirección a `https://carleton.ca/economics/wp-content/uploads/cep04-12.pdf` («404 GET https://carleton.ca/economics/wp-content/uploads/cep04-12.pdf»). No es un paper fantasma: `https://api.openalex.org/works/W2188956700` confirma «Cuba's Underground Economy», Ritter, 2004, 20 citas, sin DOI, y registra como ubicaciones alternativas `https://EconPapers.repec.org/RePEc:car:carecp:04-12` y `https://ir.library.carleton.ca/pub/15983`.

— polarity: negative · confidence: high · related: [[#C051]], [[#F-V8-001]]

### F-V8-007 — `[6]` y `[12]`: acceso restringido sin evidencia de error bibliográfico

La URL de `[6]` (L18), `http://aisel.aisnet.org/cgi/viewcontent.cgi?article=1273&context=icis2005`, devuelve HTTP 403 en ambos clientes empleados, respuesta compatible con protección contra automatización. La URL de `[12]` (L30), `https://newyorkfed.org/research/epr/03v09n3/0309hult.pdf`, responde con contenido `application/pdf`; el recurso existe, aunque el texto no se extrajo aquí. Ambas entradas aparecen con autores, título, venue y año en la ficha y fueron cotejadas como fuentes institucionales en el mapa E2 de la pasada 1; en esta pasada no fue posible re-leer su contenido. Se registran como no verificadas en esta pasada, sin marca de paper fantasma.

— polarity: neutral · confidence: medium · related: [[#F-V8-001]]

### F-V8-008 — Las cuatro comparaciones de §71.6 coinciden con el tema de las obras citadas

El párrafo de §71.6 (L1520) describe a Gegić et al. como quienes «predicen precios con machine learning sobre catálogos estructurados», a Muça et al. como quienes «integran datos públicos empresariales albaneses mediante scraping», a Du et al. como quienes «modelan depreciación no lineal y heterogeneidad de marca con evaluación fuera de muestra» y a Vidal Alejandro et al. como quienes «estudian el mercado informal de divisas en Cuba». Los resúmenes de Crossref confirman el núcleo de las tres primeras descripciones —ANN/SVM/Random Forest sobre anuncios de `autopijaca.ba` recogidos con un scraper PHP; integración de registros de contratación pública (APP) y de empresas (QKB) en Albania; 1.000 anuncios, muestra 800/200, término de edad al cuadrado e interacción de marca de lujo con evaluación held-out— y el mapa E2 de la pasada 1 (L342) confirma la cuarta, con el resumen de Crossref vacío para `[29]`. No aparece un marcador `[N]` que vincule estas afirmaciones con las fichas, pero no hay desajuste de contexto entre la descripción y la obra.

Un matiz: «catálogos estructurados» no aparece literalmente en el resumen de Gegić et al., que describe anuncios web recogidos por scraper y atributos examinados; el diferenciador de procedencia y normalización formulado en el propio párrafo sigue describiendo una diferencia real frente al pipeline del informe.

— polarity: positive · confidence: medium · related: [[#F-V8-002]], [[#C051]], [[#P001]], [[#P002]], [[#P003]], [[#P004]]

### F-V8-009 — §70 declara cuatro fuentes verificadas, pero solo una tiene ficha numerada

La lista de §70 (L1477–1479) nombra a Akerlof (1970), DfT/DVLA, ANFAC y AEADE como «referencias citadas y verificadas externamente durante la auditoría». De las cuatro, solo Akerlof tiene entrada en la convención de 38; las tres institucionales figuran en el mapa E2 como fuentes de datos y en el inventario E3 (L156–L158), fuera de `Data/referencias.md`. Ese mismo artefacto (L127) observa que el archivo no lleva etiqueta positiva que distinga a las cuatro. En esta pasada no se re-fetcharon sus páginas: la verificación disponible es la de la iteración 2 a nivel de organismo, con la URL profunda de la colección de estadísticas de vehículos de GOV.UK sin confirmar y la precisión de AEADE como asociación ecuatoriana sin aclarar en §70.

— polarity: neutral · confidence: medium · related: [[#C009]], [[#C051]], [[#F-V8-004]]

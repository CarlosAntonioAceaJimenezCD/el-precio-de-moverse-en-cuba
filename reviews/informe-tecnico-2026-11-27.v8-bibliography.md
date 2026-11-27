---
type: audit-artifact
phase: v8-bibliography
slug: informe-tecnico-2026-11-27
generated_at: 2026-11-27T05:52:29Z
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27/informe-tecnico-2026-11-27.text.md
language: es
bibliography_entries_total: 36
verified: 4
unverified: 32
---

## Resumen

- El informe no contiene bibliografía numerada ni sección de referencias: las 36 fuentes nominales que sostienen sus afirmaciones aparecen dispersas en tablas y prosa, sin convención autor-año ni identificadores.
- Solo cuatro entradas pudieron confirmarse en fuentes externas (Akerlof 1970; DfT/DVLA; ANFAC; AEADE); las 32 restantes quedan marcadas `(metadata incomplete)` por falta de metadatos mínimos o por fallo de acceso en este entorno.
- Se registra un desajuste de contexto entre la atribución del capítulo 13 del anuario 2025 del ONEI como fuente de «parque automotor» (§52) y la corrección posterior que niega esa serie (§56); no se detectaron entradas duplicadas ni identificadores falsos, porque el documento no declara ninguno.

## Alcance y método

No se recibió un artefacto separado `document_bibliography`. Se tomó como bibliografía efectiva el conjunto de fuentes nominales que el texto usa para apoyar afirmaciones: las tablas de «Fuentes académicas y repositorios revisados» (§17, L791–804), «Auditoría de procedencia» (§18, L812–825), el marco normativo (§4, §10), las «fuentes más valiosas» de §52 (L1293–1297) y las menciones dispersas en §15, §19, §20 y §56. Se excluyeron del cómputo los archivos internos del proyecto que funcionan como artefactos de datos (bases SQLite, CSV y PNG), salvo cuando el propio documento los presenta como fuente metodológica.

Las verificaciones se ejecutaron el 2026-11-27 contra Crossref API, OpenAlex API, páginas de publishers/organismos y resolución de URLs. Los intentos de `WebSearch` devolvieron error de ejecución del proveedor, por lo que las normas cubanas y los trabajos locales no pudieron cotejarse por esa vía. Todo dato no confirmado se marca `(metadata incomplete)`; no se ha asignado ningún DOI, ID de arXiv ni venue que no conste en una fuente verificada.

### Inventario auditado

| # | Fuente nominal | Clase | Resultado externo |
|---:|---|---|---|
| 1 | Akerlof, «The Market for "Lemons"», 1970 | Académica | Verificado (Crossref + OpenAlex) |
| 2 | PDF PUCE en `Hombros/01_PDFs/` | Académica local | `(metadata incomplete)` |
| 3 | «Informe de competencia del mercado automotriz ...» / «Mercado automotriz chileno: un análisis empírico» | Informe | `(metadata incomplete)` |
| 4 | `Hombros/RESUMEN_NUEVAS_BUSQUEDAS.md` | Resumen interno | `(metadata incomplete)` |
| 5 | «Inteligencia De Negocios Aplicada Al Sector Automovilístico» (HTML) | Informe | `(metadata incomplete)` |
| 6 | ANFAC | Gremial | Verificado (sitio institucional) |
| 7 | AEADE | Gremial | Verificado (sitio institucional) |
| 8 | EY | Consultoría | `(metadata incomplete)` |
| 9 | INEGI | Oficial | `(metadata incomplete)` |
| 10 | BBVA Research | Consultoría | `(metadata incomplete)` |
| 11 | COIIM | Gremial | `(metadata incomplete)` |
| 12 | Decreto 163/2026 + Gaceta 65 Ordinaria | Norma | `(metadata incomplete)` |
| 13 | Decreto 119/2024 (derogado) | Norma | `(metadata incomplete)` |
| 14 | Resoluciones 104/17/52/171–175/312/340/102 de 2026 | Normas | `(metadata incomplete)` |
| 15 | Resolución 14 (salarios) | Norma | `(metadata incomplete)` |
| 16 | ONEI, anuarios 2014–2025 y Anuario 2025 cap. 13 | Oficial | `(metadata incomplete)` |
| 17 | DfT / DVLA, vehicle licensing statistics data files | Oficial | Verificado (GOV.UK) |
| 18 | VAHAN (India, MoRTH) | Oficial | `(metadata incomplete)` |
| 19 | BCC, API de tasas activas | Oficial | `(metadata incomplete)` |
| 20 | elTOQUE, TRMI | No oficial | `(metadata incomplete)` |
| 21 | Condiciones de Uso de Revolico (23/09/2026) | Términos de uso | `(metadata incomplete)` |
| 22 | Universidades (PUCE, UPS, UPV, UChile, UNAL, etc.) | Académica | `(metadata incomplete)` |
| 23 | CarDekho (Kaggle) | Dataset | `(metadata incomplete)` |
| 24 | UCI Automobile | Dataset | `(metadata incomplete)` |
| 25 | Datasets sintéticos Zimbabwe/Nigeria | Dataset | `(metadata incomplete)` |
| 26 | `spinny-scraper` | Repositorio | `(metadata incomplete)` |
| 27 | `taso-api` | Repositorio | `(metadata incomplete)` |
| 28 | `AutosxCuba` | Repositorio | `(metadata incomplete)` |
| 29 | `guani-saimc` | Repositorio | `(metadata incomplete)` |
| 30 | `IDSE-DATA-SCIENCE-PROJECT-` | Repositorio | `(metadata incomplete)` |
| 31 | `used-cars-price-prediction` | Repositorio | `(metadata incomplete)` |
| 32 | `Iran-Car-Market-Intelligence` | Repositorio | `(metadata incomplete)` |
| 33 | `uk-automotive-transition` | Repositorio | `(metadata incomplete)` |
| 34 | `vahan-india` | Repositorio | `(metadata incomplete)` |
| 35 | `nz-vehicle-market-tracker` / `zimbabwe-used-vehicle-market-analysis` | Repositorios | `(metadata incomplete)` |
| 36 | Womy / Clasificados.st / TecnoTáctil | Portales | `(metadata incomplete)` |

### F-V8-001 — El documento no constituye una bibliografía verificable en el sentido convencional

La búsqueda de una sección de referencias, de citas numeradas `[N]` y de un patrón autor-año dio resultado negativo en el texto cacheado. E1 ya había consignado que «El documento no emplea citas numeradas tipo `[N]`; por eso `External evidence cited` se marca «— (sin citas numeradas)» y las fuentes nombradas se consignan, cuando procede, en `Notes`», y E2 confirma: «el documento no tiene bibliografía numerada, así que `Cited in document` se determina por mención nominal». La consecuencia bibliográfica es concreta: no hay entradas que puedan cotejarse como unidades completas (autor, título, año, venue, identificador), sino menciones de fuentes repartidas entre tablas de procedencia, rutas de archivo y prosa. El encabezado de la tabla de §17 —«| Fuente | Aporte metodológico | Requerimiento para AutoDecide |» (L791)— ilustra el patrón: la columna «Fuente» admite indistintamente un PDF, un repositorio, una asociación gremial y una norma.

— polarity: negativo · confidence: alta · related: [[#C003]], [[#C048]]

### F-V8-002 — Akerlof (1970): metadatos confirmados en fuentes externas, pero sin entrada en el informe

El documento invoca la obra únicamente por apellido: «**Marco teórico y normativo**: asimetría de información (Akerlof), selección adversa, riesgo moral, regulación vigente» (§19, L837), y en la tabla de §17 atribuye al PDF de la PUCE «Asimetría de información (Akerlof)» (L793). No existe ficha bibliográfica propia: `(metadata incomplete)` en el documento.

La verificación externa sí confirma la obra. La consulta a `https://api.crossref.org/works/10.2307/1879431` devolvió `status: ok` con título «The Market for "Lemons": Quality Uncertainty and the Market Mechanism», autor `George A. Akerlof`, `published-print 1970-08`, contenedor «The Quarterly Journal of Economics», volumen 84, número 3, página 488 y DOI `10.2307/1879431`. La consulta a `https://api.openalex.org/works?search=The%20Market%20for%20Lemons%20Quality%20Uncertainty%20and%20the%20Market%20Mechanism&per-page=1` devolvió el registro `W2156109180` con el mismo DOI, año 1970, autor George A. Akerlof y la misma revista. El DOI y la revista se transcriben aquí porque fueron devueltos por esas dos APIs, no por el documento. El registro incluye además un resumen indexado que contiene solo el índice de secciones («I. Introduction, 488. — II. The model with automobiles as an example, 489. ...»), por lo que la comprobación de contexto se apoya en el título y las palabras clave indexadas (`adverse selection`, `information asymmetry`, `used cars`), no en un abstract sustantivo.

La ausencia de ficha es relevante porque el marco teórico de §19 y §20 apoya la captura de defectos y calidad declarada como requerimiento: la alegación teórica queda mediada por un PDF local sin metadatos (véase F-V8-009).

— polarity: negativo · confidence: alta · related: [[#C048]], [[#C052]]

### F-V8-003 — Corpus normativo cubano citado por número, sin URL oficial ni fecha de acceso verificables

El documento sostiene una afirmación cargada (C003) con normas citadas solo por número: «La norma marco es el **Decreto 163/2026** (Gaceta Oficial No. 65 Ordinaria, 04/08/2026, vigente desde el 11/08/2026), que deroga el Decreto 119/2024» (§4, L56), y «Se cotejaron las resoluciones 104/2026 (MINCEX), 17/2026 (MINCIN), 52/2026 (MITRANS), 171–175/2026 (MFP), 312/2026, derogada por 340/2026 (Aduana) y 102/2026 (BCC)» (L56). Más adelante añade la «**Resolución 14**» como fuente de salarios (§19, L847; §20, L863) y el «**Hallazgo normativo crítico:** la **Resolución 312/2026 de la Aduana General fue derogada por la Resolución 340/2026**» (§52, L1299).

Los dos intentos de búsqueda (`"Decreto 163/2026" Cuba Gaceta Oficial importación vehículos` y una consulta equivalente sobre el estudio PUCE) devolvieron `Unable to search the web`, y el documento no incluye URL de la Gaceta Oficial ni fecha de acceso para ninguna de estas normas; remite a `~/Utilidades/Leyes/gaceta_catalog.json`, un índice local (§10, L118). En consecuencia, las entradas 12–15 del inventario quedan `(metadata incomplete)`: se registra lo que el texto afirma, sin atribuir sede, página de publicación ni identificador externo que no haya sido verificado. La coherencia interna de la cadena de derogaciones (163/2026 → 119/2024; 340/2026 → 312/2026) se conserva tal como aparece en L56, L1299 y L185, pero no ha podido cotejarse con una fuente oficial en este entorno.

— polarity: negativo · confidence: media · related: [[#C003]], [[#C016]], [[#C085]]

### F-V8-004 — ONEI: institución y corpus documentados internamente, pero inaccesibles para verificación externa

La entrada 16 se apoya en un inventario interno detallado: «A partir del índice oficial `http://www.onei.gob.cu/cuba` se recorrieron las 12 páginas de anuarios disponibles (2014–2025) y se descargaron **todos los documentos enlazados**: 111 PDF, 7 RAR y 103 archivos Excel extraídos, unos 311 MB en total. El inventario está en `Data/fuentes-oficiales/ONEI/README.md` y, con URL, tamaño y SHA-256 por archivo, en el `INDICE.md` de cada año» (§53, L1309). El acceso a `http://www.onei.gob.cu/cuba` desde este evaluador devolvió `{"error":{"type":"unknown","message":"Transport error (GET http://www.onei.gob.cu/cuba)"}}`.

No se trata de una obra fantasma: el documento declara manifiestos con URL, tamaño y hash por archivo y E3 confirma la existencia del inventario como observación de nivel de documento. Aun así, la ficha bibliográfica sigue siendo `(metadata incomplete)` porque no hay título formal de la serie, fecha de consulta externa verificable ni resolución del sitio desde el entorno de auditoría. La afirmación de §56 —«Se revisaron los 12 anuarios del ONEI y sus 233 archivos» (L1347)— descansa en ese inventario local, no en una comprobación reproducible aquí.

— polarity: neutro · confidence: alta · related: [[#C069]], [[#C072]]

### F-V8-005 — Desajuste de contexto: el capítulo 13 del Anuario 2025 se cita por «parque automotor» y después se corrige

Existe una inconsistencia entre la fuente invocada y el contenido que se le atribuye. En §52, L1295, el documento escribe: «**ONEI, Anuario Estadístico 2025, capítulo 13**: serie oficial más reciente de transporte y parque automotor, ausente hasta ahora en la base». En §53, L1313, refuerza: «la serie más útil es el capítulo 13 (Transporte y Seguridad Vial), que permite incorporar parque automotor, matriculaciones y accidentes con series oficiales 2014–2025». Sin embargo, §56, L1347, concluye: «**No hay series de parque automotor ni de matriculaciones**, por lo que esa laguna signalada en `NECESIDADES.md` no se resuelve con los anuarios; la corrección quedó registrada». E3 confirma la corrección como hallazgo de ausencia de artefacto.

La entrada ONEI (ítem 16) es, por tanto, citada en dos contextos incompatibles: se la presenta como fuente de una serie que, según la verificación interna posterior, no contiene. El uso que sí resiste el cotejo es el de transporte de pasajeros y seguridad vial (L1347). La atribución de «parque automotor» queda `(metadata incomplete)` en el sentido de contexto, no de existencia de la fuente.

— polarity: negativo · confidence: alta · related: [[#C012]], [[#C069]], [[#C072]]

### F-V8-006 — DfT/DVLA: entrada verificada y concordante con su contexto de uso

La fila de §18, L814, dice: «DfT / DVLA (UK), `gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files` | **Oficial gubernamental** | Verificado en vivo: publicado por Department for Transport + DVLA, actualizado 23/09/2026, Open Government Licence | Repos `uk-automotive-transition`: erste Registrierungen por marca/combustible/trimestre».

La descarga de `https://www.gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files` confirmó todos los elementos: título «Vehicle licensing statistics data files», `From: Department for Transport and Driver and Vehicle Licensing Agency`, `Published: 24 May 2022`, `Last updated: 23 September 2026`, licencia `Open Government Licence v3.0`, y datos de `df_VEH0160_GB`/`df_VEH0160_UK` descritos como «Vehicles registered for the first time by body type, make, generic model and model». Es la única entrada del inventario cuyos tres metadatos declarados (organismo, fecha de actualización y licencia) coinciden literalmente con la fuente externa. El contexto de uso declarado —matriculaciones por marca/combustible/trimestre— es compatible con el esquema de esos ficheros CSV.

— polarity: positivo · confidence: alta · related: [[#C050]]

### F-V8-007 — ANFAC y AEADE: organismos confirmados, informes concretos sin ficha

Las filas L818–L819 del §18 afirman verificación en vivo de «ANFAC (España) | **Gremial** (asociación de fabricantes) | Verificado en vivo: anfac.com, cifras de matriculaciones y parque, informe anual» y «AEADE (Ecuador) | **Gremial** | Verificado en vivo: aeade.net, anuarios y boletines de ventas | Fuente declarada por el estudio PUCE de vehículos usados».

`https://www.anfac.com/` resolvió y expone las secciones «Notas de matriculación», «Informe Anual» y «Parque Vehículos», además de cifras de matriculaciones de octubre de 2026. `https://aeade.net/` resolvió y expone «Estadísticas → Anuarios» y «Boletines de prensa: venta de vehículos». La existencia de ambos organismos y de las categorías de datos citadas queda verificada. No obstante, las entradas siguen siendo incompletas en sentido estricto: no se identifica el informe anual concreto, el año del anuario ni la URL profunda de cada documento. Se registran como verificadas a nivel de organismo y `(metadata incomplete)` a nivel de publicación específica.

— polarity: neutro · confidence: alta

### F-V8-008 — VAHAN, BCC y elTOQUE: fallos de acceso declarados por el documento y reproducidos aquí

Tres fuentes nominales tienen verificación explícitamente frustrada. En §18: «VAHAN (India), declarado por `vahan-india-automotive-market-2025` | **Oficial gubernamental** (MoRTH) | No accesible desde este entorno (error de transporte); el repo documenta 12 exportaciones mensuales 2025 y manifiesto de verificacion» (L815); «BCC (Banco Central de Cuba) | **Oficial gubernamental** | No accesible en vivo desde este entorno» (L816). En §52 se da la URL «`https://api.bc.gob.cu/v1/tasas-de-cambio/activas`» (L1293), y en §55: «14 respondieron HTTP 200 y elTOQUE no respondió desde este entorno» (L1333).

La comprobación de `https://api.bc.gob.cu/v1/tasas-de-cambio/activas` devolvió `{"error":{"type":"unknown","message":"Transport error (GET https://api.bc.gob.cu/v1/tasas-de-cambio/activas)"}}`, reproduciendo lo declarado. No se intentó una URL alternativa para VAHAN ni para elTOQUE porque el documento no las aporta. Las tres entradas (18–20) quedan `(metadata incomplete)`: no son invenciones —el propio texto las etiqueta como no verificadas— pero tampoco pueden atribuirse a una edición, fecha o respuesta concreta. El uso analítico declarado (registros por fabricante/combustible, tasa oficial de referencia y TRMI informal) se conserva como atribución del informe, no como hecho verificado.

— polarity: neutro · confidence: alta · related: [[#C051]], [[#C056]], [[#C068]], [[#C071]]

### F-V8-009 — Estudio de la PUCE: ficha sin autores, año, título completo ni identificador

La entrada 2 se cita con una ruta local y una etiqueta institucional: «`Hombros/01_PDFs/Análisis del mercado de vehículos usados y su comercialización en el__73e1773e.pdf` (PUCE) | Asimetría de información (Akerlof); clasificación de calidad por antigüedad (≤5 años alta, >5 años con defectos); encuesta a 130 comerciantes; medición de costos ocultos y margen de reventa» (§17, L793). E3 la inventaría como «PUCE used-vehicle study survey», también sin autor ni año.

El sufijo `__73e1773e` parece un hash de archivo, no un identificador bibliográfico; el documento no declara autores, año, facultad, serie ni DOI. El intento de búsqueda por el título devolvió `Unable to search the web`, por lo que la ficha queda `(metadata incomplete)`. Tiene peso específico: de esta entrada dependen la regla de calidad por antigüedad (§19, L849), la encuesta a 130 comerciantes (C048) y la justificación de «costos ocultos» como requerimiento (§20, L865). Que la fuente sea un PDF local con manifestación de procedencia no sustituye la atribución académica.

— polarity: negativo · confidence: alta · related: [[#C048]], [[#C052]]

### F-V8-010 — Entradas truncadas y agrupadas en las tablas de fuentes

Varias celdas de §17 y §18 condensan múltiples obras en una sola fila o truncan el título, de modo que no constituyen entradas diferenciables: «`Hombros/01_PDFs/PDF Informe de competencia del mercado automotriz ...` / `Mercado automotriz chileno: un análisis empírico`» (L795); «Informes ANFAC / EY / INEGI / BBVA / COIIM en `Hombros/01_PDFs/`» (L797); «Universidades (PUCE, UPS, UPV, UChile, UNAL, etc.) | **Académico** | Repositorios institucionales (.edu / repositorios oficiales) en `Hombros/indice.md`» (L821); «CarDekho (Kaggle), Spinny, OLX, Revolico, Autocubana, Dongfeng» (L822); «UCI Automobile, datasets sintéticos (Zimbabwe/Nigeria) | **Académico/sintético** | Declarado en los propios README» (L825).

En los casos 8–11, 22–25 del inventario no hay título de documento, año, autor ni URL individual; la tabla de §18 añade además la salvedad «Citados en los informes descargados en `Hombros/01_PDFs/`; no todos re-verificados en vivo» (L820) y «No verificados en vivo; elTOQUE es medio independiente, no BCC» (L824). Todas se marcan `(metadata incomplete)`. La agregación no es en sí misma un error —el informe declara que son contexto— pero impide decidir qué obra sostiene cada afirmación y dificulta detectar duplicados internos.

— polarity: negativo · confidence: alta · related: [[#C050]], [[#C051]], [[#C071]]

### F-V8-011 — Repositorios usados como antecedente metodológico sin versión, URL ni compromiso

El documento atribuye decisiones de diseño a código de terceros: «Se adaptó el patrón `output_writer.py` + `diff_runs.py` de `spinny-scraper` como snapshot `Data/Revolico/snapshots/ultimo.json`» (§16, L781); «`Copias/taso-api/src/*` | Tasas de cambio múltiples | Normalizar CUP/USD/MLC/EUR» (§17, L800); «`Copias/AutosxCuba/code/{unir_todo_final,modelo_predictivo,generar_graficos}.py`» (L798); y el bloque «`Auxiliares/Repositorios Referencias/{uk-automotive-transition,vahan-india,nz-vehicle-market-tracker,zimbabwe-used-vehicle-market-analysis}` | Series por período, EDA, viabilidad» (L804).

Ninguna de las entradas 26–35 del inventario incluye URL de repositorio, commit, tag, licencia o fecha de acceso. E3 consigna que no se aportó cloned path y que `repo_clone_status: not-attempted`, por lo que la atribución no pudo cotejarse contra el código. Todas quedan `(metadata incomplete)`. El caso de `Copias/` es además paradójico: §3 declara «`Copias/` no se registra en este informe por decisión explícita» (L52), mientras §17 y §50 sí citan su código como insumo metodológico, de modo que la fuente se usa sin entrar en el inventario de fuentes ni en el de artefactos.

— polarity: negativo · confidence: alta · related: [[#C062]], [[#C083]]

### F-V8-012 — Condiciones de Uso de Revolico citadas sin URL ni copia archivada

La afirmación de permanencia (C040) se apoya en un documento sin ficha: «las Condiciones de Uso de Revolico (23/09/2026) no fijan un plazo de caducidad de los anuncios. Empíricamente, un anuncio con `updated_on_by_user=2024-12-17` seguía en HTTP 200 el 17/11/2026 (~699 días)» (§15, L771). La entrada 21 del inventario tiene fecha pero no URL, título completo, editor ni copia local identificable; el texto sí nombra como fuente alternativa el repositorio de diferencias en §16. Queda `(metadata incomplete)`.

Conviene distinguir los dos componentes: la observación empírica del HTTP 200 es interna al proyecto y no requiere cita externa; la negativa de la fuente a fijar caducidad sí es una afirmación sobre un documento tercero y, tal como está escrita, no puede verificarse sin el texto de las condiciones.

— polarity: negativo · confidence: media · related: [[#C040]]

### F-V8-013 — Convención de formato heterogénea y fuentes que aparecen solo en prosa

Además de las tablas, varias fuentes se mencionan únicamente en el texto y nunca se consolidan: «salarios de la Resolución 14» (§19, L847; §20, L863), «Womy (`https://womy.cu/cars/`)» y «Clasificados.st y TecnoTáctil» (§52, L1296–1297), el «índice oficial `http://www.onei.gob.cu/cuba`» (§53, L1309) y «DfT / DVLA» fuera de la tabla de auditoría. La tabla de §18 usa una columna «Naturaleza» con valores mezclados (`Oficial gubernamental`, `Gremial`, `Académico`, `Marketplace / anuncios`, `Redes sociales`, `No oficial`) y la de §17 mezcla normas, informes, repositorios y rutas de archivo bajo la misma etiqueta «Fuente».

No hay fecha de acceso sistemática, ni separación entre «obra citada» y «archivo descargado», ni normalización de mayúsculas/idioma de títulos (`Inteligencia De Negocios Aplicada Al Sector Automovilístico`, `Mercado automotriz chileno: un análisis empírico`, `Análisis del mercado de vehículos usados y su comercialización en el__73e1773e.pdf`). Para un lector que quiera reconstruir la cadena evidencia→afirmación, la consecuencia es que la procedencia está documentada en el nivel de la fuente pero no en el nivel de la entrada bibliográfica. Las entradas afectadas se mantienen `(metadata incomplete)`.

— polarity: negativo · confidence: alta · related: [[#C068]], [[#C071]]

### F-V8-014 — No hay duplicados ni identificadores espurios en el documento; el mapa E2 queda fuera de la bibliografía auditable

La inspección de las 36 menciones nominales no encontró la misma obra presentada dos veces con identidades distintas dentro del documento. Tampoco hay DOI, ID de arXiv ni venue asignados por el informe a fuente alguna: el único DOI que aparece en este artefacto, `10.2307/1879431`, procede de la respuesta de Crossref/OpenAlex verificada en F-V8-002 y no se atribuye al texto auditado.

El mapa de literatura E2 contiene 38 trabajos con sus propios DOI y URLs, pero es un artefacto generado por el evaluador de literatura, no una bibliografía del informe: E2 lo declara explícitamente —«el documento no tiene bibliografía numerada [...] la única obra académica citada por nombre es P001 (1970)»—. Por extensión, las 37 obras restantes de E2 no se cuentan aquí ni se auditan como entradas del documento; hacerlo equivaldría a atribuir al informe citas que no contiene. Este hallazgo delimita el alcance del cómputo del frontmatter (`bibliography_entries_total: 36`).

— polarity: positivo · confidence: alta

## Nota de cierre

Las verificaciones se registran tal como fueron obtenidas: Crossref y OpenAlex confirmaron la ficha de Akerlof; GOV.UK confirmó organismo, fecha y licencia de DfT/DVLA; los sitios de ANFAC y AEADE confirmaron la existencia de las secciones citadas; ONEI y la API de BCC fallaron con error de transporte; las búsquedas web no estuvieron disponibles. Ningún dato ausente se completó por inferencia. Las 32 entradas `(metadata incomplete)` requieren, para una auditoría completa, acceso a la Gaceta Oficial cubana, a los PDFs de `Hombros/` y a los repositorios referenciados, además de una fecha de consulta declarada por fuente.

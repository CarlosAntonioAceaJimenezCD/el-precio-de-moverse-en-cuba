---
type: audit-artifact
phase: v8-bibliography
slug: corpus-documentacion-2026-11-28
generated_at: 2026-11-28T04:15:00-04:00
audited_document: .playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md
language: es
bibliography_entries_total: 41
verified: 37
unverified: 4
---

# V8 — Integridad bibliográfica — corpus de documentación de usuario

Nota de método y alcance. El mandato recibido es el contraste entre las fuentes citadas en el corpus de ocho archivos de cara al usuario y las 41 entradas de `Data/referencias.md`, más la verificación de URLs oficiales accesibles. En consecuencia: (a) el corpus es documentación de producto y no contiene una bibliografía propia, así que los conteos del frontmatter se refieren al anexo numerado de 41 entradas aportado para el contraste, no a una sección del corpus; (b) `verified: 37` / `unverified: 4` hereda la convención del anexo (L4–L6): son no verificadas las cuatro entradas marcadas `(metadata incomplete)` —[1], [10], [12] y [39]—, no papers inexistentes; (c) en esta pasada sí se re-verificaron en vivo [9], [24], [27] y [39]–[41], además de las sedes oficiales cubanas y las normas citadas en el corpus; el resto de metadatos del anexo se heredan de la verificación del 27/11/2026 consignada en `Data/referencias.md`; (d) los números de línea del corpus corresponden a la copia en caché indicada en el frontmatter; (e) se aplicó el criterio del evaluador de no reclamar enlace roto cuando el fallo es de transporte desde este entorno: esos casos se registran como «no confirmado desde aquí».

## Hallazgos

### F-V8-001 — Intersección vacía: el corpus no usa el anexo numerado de 41 entradas

Búsqueda directa sobre la copia auditada: **0 marcadores `[N]`** y **0 URL `doi.org` o `arxiv.org`** en las 833 líneas. El único `http://` del corpus es interno —«El scraper usa, en orden: `curl_cffi`… y **FlareSolverr** (`http://127.0.0.1:8191/v1`) para páginas como Cybo que devuelven 403 o verificación de seguridad» (L833)—; el resto de enlaces son rutas relativas entre los ocho archivos (L105–L108, L131, L381–L386). `Data/referencias.md` no aparece citado ni enlazado en ningún bloque. El anexo, a su vez, se declara derivado de otro documento: «Generado el 27/11/2026 desde `reviews/informe-tecnico-2026-11-27.e2-literature.md`» (L3), con entradas [1]–[41] (L8–L87).

Contraste entradas por entrada: de las 41, ninguna es citada en el corpus. Recíprocamente, las fuentes con que el corpus respalda sus cifras —«consolidados con fuentes oficiales (ONEI, Gaceta Oficial, BCC) y una serie de entrevistas y encuestas» (L12) y «| Oficiales | ONEI, Gaceta Oficial 65/2026, BCC, elTOQUE | 12 anuarios + normas |» (L71)— no figuran en el anexo. El bloque institucional [39]–[41] (DfT/DVLA, ANFAC, AEADE) es del mismo género documental, pero son instituciones distintas de las que el corpus invoca. Es una diferencia de alcance entre dos artefactos (informe técnico frente a documentación de usuario), no una entrada falsa ni una contradicción de metadatos.

— polarity: neutral · confidence: high · related: corpus L12, L71, L105–L108, L131, L833; `Data/referencias.md` L3, L8–L87

### F-V8-002 — Fuentes citadas por nombre o número sin identificador resoluble

Las atribuciones de carga del corpus no llevan DOI, arXiv, URL de destino ni fecha de consulta verificable. Casos literales: «El marco normativo es el **Decreto 163/2026** y las resoluciones 104, 17, 52, 171–175, 340 (que derogó la 312) y 102/2026» (L112); «El **Decreto 163/2026** abrió el mercado a 17 empresas autorizadas. Las resoluciones 171–175 y 340 —que derogó la 312— fijan valores referenciales, impuestos especiales y reglas aduaneras» (L245); «con la nota del **Ministerio de Finanzas y Precios del 12 de mayo** y la **Circular Especial 03/2026 de CIMEX**» (L179); «según reportes de prensa ha dejado circuitos con más de **60 horas sin electricidad**» (L181). La convención tampoco es uniforme: acrónimos sin enlace (`ONEI`, `BCC`, L12), repositorio entre backticks (`Egyptian-Used-Cars`, L277), corporación con nombre completo (CIMEX S.A., L177), app nombrada sin URL (**Circuitos Habana**, L248) y una referencia colectiva genérica («reportes de prensa», L181).

La consecuencia bibliográfica es operativa, no de existencia: las normas se citan por número y pueden localizarse en la Gaceta, pero desde el documento no hay forma de pasar del número a la norma. La única excepción es FlareSolverr (L833), con URL, aunque sea `localhost` y corresponda a una herramienta, no a una fuente de datos.

— polarity: negative · confidence: high · related: corpus L112, L177–L181, L245, L248, L277, L833; F-V8-004, F-V8-008

### F-V8-003 — Bloque institucional [39]–[41]: las tres URLs resolvieron en esta pasada

Fetch en vivo: `https://www.gov.uk/government/organisations/department-for-transport` → respuesta correcta, con apartado «Research and statistics», noticias fechadas en noviembre de 2026 y licencia «Open Government Licence v3.0», coherente con la entrada «[39] Department for Transport / DVLA. Vehicle statistics. GOV.UK. https://www.gov.uk/government/organisations/department-for-transport. **(metadata incomplete: URL profunda no confirmada)**. Citada en el informe: sí (§70 y §71.14).» (`Data/referencias.md` L83). `https://anfac.com/` → respuesta correcta, con «Cifras clave → Matriculaciones Turismos y Todoterreno» y cuadro de octubre de 2026, coherente con «[40] ANFAC. Informes del sector automotriz español. https://anfac.com/. Citada en el informe: sí (fuente institucional en §70).» (L85). `https://www.aeade.net/` → respuesta correcta, «AEADE – Asociación de Empresas Automotrices del Ecuador», con «Estadísticas → Anuarios» y «Boletines de prensa: venta de vehículos», coherente con «[41] AEADE. Estadísticas de matriculaciones. https://www.aeade.net/. Citada en el informe: sí (fuente institucional en §70).» (L87).

Este resultado revierte los timeouts registrados para [39] y [40] en `reviews/informe-tecnico-2026-11-28-iter4.v8-bibliography.md` (F-V8-003, L35): en la fecha de esta pasada las tres sedes responden. No cambia el flag `(metadata incomplete)` de [39], que se refiere a la URL profunda `gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files` citada en §18 del informe, no a la raíz institucional aquí verificada.

— polarity: positive · confidence: high · related: `Data/referencias.md` L83, L85, L87; informe-tecnico-2026-11-28-iter4.v8-bibliography.md F-V8-003

### F-V8-004 — Fuentes oficiales cubanas: existen y son accesibles, con matices de dominio y esquema

Verificación en vivo de las tres sedes que el corpus nombra sin enlace (L12, L71):

- ONEI: `https://www.onei.gob.cu/` → error de transporte; `http://www.onei.gob.cu/` → respuesta correcta. El sitio expone la serie «Transporte y Seguridad Vial», el catálogo «Anuarios → Anuario Estadístico → Cuba» con portada de «Anuario Estadístico de Cuba 2025», y el índice de publicaciones. El esquema `http` y no `https` es el que responde desde este entorno.
- Gaceta Oficial: `https://gacetaoficial.gob.cu/` → error de transporte; `http://www.gacetaoficial.gob.cu/` → respuesta correcta, con «ÚLTIMA GACETA OFICIAL» No. 98 extraordinaria del 27/11/2026 y buscador de normas. El índice del sitio registra «Decreto 163 de 2026 de Consejo de Ministros. Identificador de norma: GOC-2026-426-O65» bajo la voz «vehículos de motor», lo que acredita la norma que el corpus invoca en L112, L197 y L245 y la pertenencia a la Gaceta 65/2026 de L71.
- BCC: `https://www.bcc.gob.cu/` → error de transporte; la sede que responde es `https://www.bc.gob.cu/`, que se autodenuncia «Sitio oficial del Banco Central de Cuba» y muestra «Tasa de cambio oficial Vigente el sábado, 28 de noviembre» (USD 879,00 CUP). El corpus escribe solo «BCC» (L12, L71), sin URL, de modo que no hay un enlace roto en el documento; la sigla y el dominio real no coinciden.

El resultado es positivo para la atribución institucional: ONEI, Gaceta Oficial y BCC son fuentes reales, identificables y accesibles desde este entorno bajo las formas indicadas. Ninguna de las tres está en las 41 entradas del anexo.

— polarity: positive · confidence: high · related: corpus L12, L71, L112, L197, L245; F-V8-001

### F-V8-005 — elTOQUE: cifra fechada sin enlace ni instantánea verificable

El corpus fija la TRMI con dos redacciones: «La conversión usa la **TRMI informal de elTOQUE (18/11/2026): 930 CUP/USD, 1.000 CUP/EUR y 845,35 CUP/MLC**» (L73) y «la referencia real es la **TRMI informal: 930 CUP por USD** (elTOQUE, noviembre 2026)» (L242). El propio documento registra la limitación: «elTOQUE no responde de forma estable desde este entorno (se usa su última TRMI publicada)» (L114).

Fetch en esta pasada: `https://eltoque.com/`, `https://tasa.eltoque.com/` y `https://eltoque.com/tasas-de-cambio-cuba/mercado-informal` → error de transporte en las tres. El índice de búsqueda sí devuelve páginas vivas del sitio (`eltoque.com/tasas-de-cambio-cuba/dolar`, `/euro`, `/mlc`) con valores del 28/11/2026: «1 USD … 980.00 CUP», «1 EUR … 1045.00 CUP», «1 MLC equivale a 810.43 CUP hoy». El valor de 930 CUP/USD del corpus queda así como una instantánea de fecha declarada, no como dato contradicho: la serie es móvil y la cifra de hoy es distinta. Lo que no puede resolverse desde el corpus es la instantánea concreta del 18/11/2026, porque no se registra URL de la página ni del valor publicado ese día.

— polarity: negative · confidence: medium · related: corpus L73, L114, L242

### F-V8-006 — Spot-check de tres atribuciones de carga: ONEI, `Egyptian-Used-Cars` y Acuerdo 9811

ONEI (L145): «en 2025 se transportaron **781 millones de pasajeros**, un 59 % menos que en 2019. En ómnibus fueron 324 millones, un 71 % menos». El Cuadro 3 (L341–L352) da 781,1 frente a 1.899,9 en 2019 (781,1/1.899,9 = 0,411 → −58,9 %, redondeado 59 %) y 324,0 frente a 1.102,2 (0,294 → −70,6 %, redondeado 71 %). La atribución y el cálculo coinciden, y el sitio de ONEI expone la serie «Transporte y Seguridad Vial» verificada en F-V8-004. El Cuadro 4 (L354–L362) es de la misma fuente y categoría.

`Egyptian-Used-Cars` (L277): «uno de los análisis de mercado automotriz más completos que tenemos: 23.500 anuncios, historial mensual de precios, econometría, SQL, Tableau y Power BI». El repositorio existe en disco (`Auxiliares/Repositorios Referencias/Egyptian-Used-Cars/`); su `README.md` L1–L9 declara «Python**, **SQL**, **Tableau**, and **Power BI**» y «historical price fluctuations, depreciation dynamics», y las L39–L60 detallan OLS log-lineal, VIF, Kruskal-Wallis, CTEs y `LAG/LEAD/RANK`. `data/cleaned/used_cars_cleaned.csv` tiene 23.535 líneas (23.534 registros), compatibles con el redondeo «23.500 anuncios». Es una fuente local atribuible, ausente del anexo de 41 entradas.

Acuerdo 9811/2024 (L177): «el **Acuerdo 9811 de 2024 del Consejo de Ministros**, que fijaba los precios minoristas de los combustibles en CUP y USD». La cobertura oficial indexada (Granma, Cubadebate, `mincin.gob.cu`) lo data el 24/01/2024, publicado en Gaceta Extraordinaria 10, con entrada en vigor el 01/03/2024. La identidad y el objeto de la norma coinciden con el corpus; el corpus no aporta enlace a esa Gaceta.

— polarity: positive · confidence: high · related: corpus L145, L177, L277, L341–L362; `Auxiliares/Repositorios Referencias/Egyptian-Used-Cars/README.md` L1–L9, L39–L60

### F-V8-007 — Tres identificadores de aspecto sospechoso resuelven y coinciden con el anexo

Verificación puntual de los casos que el evaluador marca como prioritarios:

- `[24]` (L54): «arXiv:2601.14311 (manuscrito enviado a ACM Computing Surveys) (2026)». `https://arxiv.org/abs/2601.14311` → página activa, «Submitted on 19 Jan 2026», título «Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability in LLMs» y los seis autores (Hohensinner, Mutlu, Mendoza Estrada, Vukovic, Kopeinik, Kern) coincidentes; «Comments: 35 pages, 6 figures. Manuscript submitted to ACM Computing Surveys (CSUR) on the 12th of December 2025». El prefijo `2601` es anterior a la fecha del corpus (23/11/2026): no hay ID imposible.
- `[27]` (L60): «https://doi.org/10.54660/.jfmr.2023.4.1.529-538». El punto inicial del sufijo (`/.jfmr`) se había registrado como «no verificado en vivo» en la V8 anterior (F-V8-009, L71). El DOI resuelve a Essien, Adebayo, Afuwape, Eboseremen, Oladega y Soneye (2023), *Journal of Frontiers in Multidisciplinary Research* 4(1), 529–538: es un DOI registrado, no uno malformado.
- `[9]` (L24): «https://doi.org/10.54254/2754-1169/2026.38524». Resuelve a Du, Yang, Zhang, Li y Liu (2026), *Advances in Economics, Management and Political Sciences* 313(1), 134–143, con el título y los autores del anexo.

Comprobación estructural del anexo: 41 líneas `^[n]` de [1] a [41], sin huecos ni números repetidos; sin entradas sin autor, sin títulos genéricos de paper fantasma y sin duplicados detectables por título+DOI. Cuatro entradas siguen marcadas `(metadata incomplete)` ([1], [10], [12], [39]), que es la base del `unverified: 4` del frontmatter.

— polarity: positive · confidence: high · related: `Data/referencias.md` L24, L54, L60, L8–L87; informe-tecnico-2026-11-28-iter4.v8-bibliography.md F-V8-009

### F-V8-008 — Normas 171–175/340/102 y Gaceta 65/2026: verificables por búsqueda, no por enlace estable

Además de la ausencia de URL señalada en F-V8-002, el acceso a las normas citadas depende del buscador del sitio y de variantes de archivo. `https://www.gacetaoficial.gob.cu/sites/default/files/goc-2026-o65.pdf` → **404**; la variante indexada `https://www.gacetaoficial.gob.cu/sites/default/files/goc-2026-o65_0.pdf` → el servidor devuelve un `application/pdf` (el fetch solo se rechaza por el tipo de contenido, no por estado HTTP). El número de Gaceta 65/2026 de L71 es, por tanto, correcto, pero la dirección profunda «obvia» del PDF no es la que sirve el archivo.

La Circular Especial 03/2026 de L179 se localiza en cobertura de prensa fechada el 15/05/2026 —«oficializada mediante la Circular Especial 03/2026, firmada por el presidente de Cimex, Héctor Oroza Busutil», con entrada en vigor a las 12:00 del 15/05/2026— y el Acuerdo 9811 en cobertura oficial (F-V8-006), pero ni una ni otra tienen enlace en el corpus. Las resoluciones 104, 17, 52, 171–175, 340 (derogadora de la 312) y 102/2026 de L112 aparecen solo como números: no se registró para ellas una dirección de resolución en el documento ni una entrada en `Data/referencias.md`. La atribución es nominativa, no resoluble desde el texto auditado.

— polarity: negative · confidence: medium · related: corpus L71, L112, L179, L245; F-V8-002, F-V8-004

## Resumen (3 líneas)

1. El corpus no tiene bibliografía: 0 marcadores `[N]`, 0 DOI/arXiv y 0 menciones de `Data/referencias.md`; las 41 entradas y las fuentes del corpus forman dos conjuntos disjuntos, con el matiz de que [39]–[41] son institucionales pero de otros países.
2. Las fuentes oficiales nombradas sí existen: ONEI y Gaceta Oficial responden por `http`, BCC por `bc.gob.cu` (no `bcc.gob.cu`), el Decreto 163/2026 está registrado como GOC-2026-426-O65 en la Gaceta 65/2026, y [39]–[41] resolvieron las tres en esta pasada; elTOQUE no fue alcanzable desde aquí y su cifra de 930 CUP/USD carece de instantánea enlazable.
3. Los spot-checks salen bien (ONEI −59 %/−71 %, 23.534 filas en `Egyptian-Used-Cars`, Acuerdo 9811 de 24/01/2024) y los tres identificadores sospechosos —arXiv:2601.14311, DOI `10.54660/.jfmr…` y DOI de [9]— resuelven y coinciden; queda sin resolución directa el bloque de resoluciones numeradas y la URL profunda inestable del PDF de la Gaceta 65/2026.

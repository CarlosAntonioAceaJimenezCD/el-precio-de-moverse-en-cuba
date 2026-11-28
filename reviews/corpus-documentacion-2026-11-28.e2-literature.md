---
type: audit-artifact
phase: e2-literature
slug: corpus-documentacion-2026-11-28
generated_at: 2026-11-28T13:45:00-05:00
preset: Standard
queries_run: 0
papers_l1: 37
papers_l2: 0
papers_l3: 0
language: es
degraded: false
---

# Literature Map — Corpus de documentación de usuario

Nota de entrada. El plan aprobado (`reviews/corpus-documentacion-2026-11-28.plan.md`, 24 líneas) declara `language: es`, `level: master` y `preset: Standard`, pero **no contiene `queries_planned` ni `hypotheses_planned`**. El mandato recibido para este extractor es estrecho: inventariar los trabajos y fuentes institucionales que cita el corpus de 8 archivos de cara al usuario, cotejarlos con las 41 entradas de `Data/referencias.md` y marcar `(metadata incomplete)` lo no verificable. En consecuencia: (a) no se ejecutaron búsquedas web nuevas —los metadatos se reutilizan de la verificación OpenAlex/Crossref del 27/11/2026 consignada en `Data/referencias.md`—; (b) todos los ítems son L1, sin lectura de resúmenes (L2) ni de texto completo (L3); (c) los IDs `P001`–`P037` designan «fuentes y obras» en sentido amplio, no únicamente artículos académicos, porque el corpus auditado es documentación de usuario; (d) los números de línea corresponden a la copia en caché `.playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md` (833 líneas); (e) `Cited in document` significa «mencionado en el corpus auditado», no «mencionado en el informe técnico»; (f) el campo `Citada en el informe` de `Data/referencias.md` se refiere al informe técnico de la pasada 1 y **no** a este corpus.

**Resultado del cotejo:** cero coincidencias. El corpus no contiene marcadores `[N]`, DOI ni identificadores arXiv; ninguno de los 41 autores, títulos ni fuentes institucionales de `Data/referencias.md` aparece citado. A la inversa, las fuentes que el corpus sí cita (ONEI, Gaceta Oficial, BCC, elTOQUE, CIMEX, ministerios, normativa cubana, repositorios y directorios) no figuran en `Data/referencias.md`. El encaje entre ambos documentos es nulo en los dos sentidos, aunque hay solapamiento temático (mercado de autos usados, divisas cubanas, electromovilidad, scraping).

## Clusters

### Cluster 1 — Fuentes institucionales y estadísticas cubanas

**Query**: `instituciones y estadísticas citadas en el corpus` ∩ `Data/referencias.md` — búsqueda por nombre (ONEI, Gaceta Oficial, BCC, elTOQUE, CIMEX, ministerios) en los 8 archivos y en el anexo de 41 entradas.

El corpus apoya sus cifras en organismos cubanos, citados **por nombre pero sin ficha bibliográfica**: sin DOI, sin URL de destino, sin año de publicación de la edición concreta y sin marcador numérico. Ninguno aparece en `Data/referencias.md`.

#### P001 — ONEI (Oficina Nacional de Estadística e Informática)

- **Authors**: ONEI (organismo oficial)
- **Year**: anuarios 2014–2025 (rango declarado; sin año de edición individual)
- **Venue**: `Data/fuentes-oficiales/ONEI/` (12 anuarios, 233 archivos, índice y SHA-256)
- **Citations**: no aplica; sin conteo posible
- **URL**: no declarada en el corpus → **(metadata incomplete: URL institucional y años de edición individuales no verificables en el corpus ni en `Data/referencias.md`)**
- **Layer**: L1
- **Cited in document**: yes — líneas 12, 21, 53, 71, 131, 145, 341, 354, 579, 624, 648 (Cuadros 3 y 4; −59 % de pasajeros frente a 2019)
- **Document reference**: ninguno — ausente de las 41 entradas
- **source_of_metadata**: corpus, líneas 12/21/145/341/354; contraste con `Data/referencias.md` [1]–[41]
- **Metadata status**: **(metadata incomplete)** — fecha de corte y URL de cada anuario no declaradas

#### P002 — Gaceta Oficial 65/2026

- **Authors**: Gaceta Oficial de la República de Cuba (publicación oficial)
- **Year**: 2026 (número 65)
- **Venue**: Gaceta Oficial (diario oficial)
- **Citations**: no aplica
- **URL**: no declarada en el corpus → **(metadata incomplete: URL de la edición 65/2026 no declarada ni verificable desde el corpus)**
- **Layer**: L1
- **Cited in document**: yes — líneas 12, 71, 177, 293
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — el corpus afirma que no se publicó una resolución numerada nueva para la suspensión de CIMEX (línea 177), pero no enlaza la edición

#### P003 — BCC (Banco Central de Cuba)

- **Authors**: Banco Central de Cuba (organismo oficial)
- **Year**: sin año declarado
- **Venue**: sitio institucional (no declarado en el corpus)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete: sin URL ni documento concreto citado)**
- **Layer**: L1
- **Cited in document**: yes — líneas 12 y 71 (agrupado con ONEI y Gaceta Oficial)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P004 — elTOQUE (TRMI informal)

- **Authors**: elTOQUE (plataforma de medios/tipo de cambio)
- **Year**: 18/11/2026 (fecha de vigencia de la TRMI); «noviembre 2026» en la línea 242
- **Venue**: elTOQUE (publicación en línea)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete: URL de la publicación de la TRMI no verificable desde el corpus)**
- **Layer**: L1
- **Cited in document**: yes — líneas 73, 114, 242 (930 CUP/USD, 1.000 CUP/EUR, 845,35 CUP/MLC)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`. Temáticamente cercana a [29] Vidal Alejandro et al. (2024), que sí está en el anexo pero no es citada aquí
- **Metadata status**: **(metadata incomplete)** — el propio corpus advierte que el sitio «no responde de forma estable» (línea 114)

#### P005 — CIMEX S.A. y plataforma Ticket

- **Authors**: Corporación CIMEX S.A. (empresa estatal)
- **Year**: 2026 (medidas del 07/02/2026 y Circular 03/2026)
- **Venue**: disposición administrativa (no publicada en Gaceta Oficial según el corpus)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 177, 179, 245, 265
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — sin enlace a comunicado ni a la Circular Especial 03/2026

#### P006 — Ministerio de Economía y Planificación (MEP)

- **Authors**: Ministerio de Economía y Planificación (organismo oficial); se menciona al viceministro Oscar Pérez-Oliva Fraga
- **Year**: 2026
- **Venue**: respaldo institucional declarado en el corpus
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 177
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — mención nominal, sin documento de respaldo enlazado

#### P007 — Ministerio de Finanzas y Precios (MFP)

- **Authors**: Ministerio de Finanzas y Precios (organismo oficial)
- **Year**: nota del 12/05/2026
- **Venue**: nota ministerial (no enlazada)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 179
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P008 — Gobierno de Cuba / autorización a actores no estatales

- **Authors**: Gobierno de Cuba (disposición general)
- **Year**: 15/02/2026
- **Venue**: medida gubernamental declarada en el corpus
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 179
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — sin resolución numerada asociada en el texto

### Cluster 2 — Normativa y disposiciones regulatorias

**Query**: `instrumentos normativos citados en el corpus` ∩ `Data/referencias.md` — búsqueda por número de decreto/resolución/acuerdo/circular en los 8 archivos.

El corpus enumera instrumentos legales con identificador propio pero sin enlace a la Gaceta Oficial ni metadatos de publicación. Ninguno está en `Data/referencias.md`.

#### P009 — Acuerdo 9811 de 2024 del Consejo de Ministros

- **Authors**: Consejo de Ministros de Cuba
- **Year**: 2024
- **Venue**: Acuerdo del Consejo de Ministros
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete: texto del acuerdo no verificable desde el corpus)**
- **Layer**: L1
- **Cited in document**: yes — línea 177 (marco de precios de combustibles vigente hasta el 07/02/2026)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P010 — Decreto 163/2026

- **Authors**: Estado cubano (órgano emisor no precisado en el corpus)
- **Year**: 2026
- **Venue**: Decreto-ley / decreto (no se especifica)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 112, 197, 245, 610, 618, 624
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — el corpus atribuye la apertura a 17 empresas autorizadas sin citar el texto normativo

#### P011 — Resoluciones 104, 17, 52 y 102/2026

- **Authors**: Estado cubano (órgano emisor no precisado en el corpus)
- **Year**: 2026 (según el sufijo declarado)
- **Venue**: resoluciones (sin Gaceta identificada)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 112
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — números sueltos, sin título ni fecha de publicación

#### P012 — Resoluciones 171–175 y 340 (derogó la 312)

- **Authors**: Estado cubano (órgano emisor no precisado en el corpus)
- **Year**: 2026 (según el contexto de la línea 245)
- **Venue**: resoluciones referenciales, fiscales y aduaneras
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 112 y 245
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P013 — Circular Especial 03/2026 de CIMEX

- **Authors**: CIMEX S.A.
- **Year**: 2026
- **Venue**: circular especial (disposición interna)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 179
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

### Cluster 3 — Proyectos y repositorios de referencia externa

**Query**: `repositorios y análisis de referencia citados en el corpus` ∩ `Data/referencias.md` — búsqueda por nombre de proyecto en los 8 archivos y en el anexo.

El corpus invoca proyectos externos como referencia de arquitectura o como fuente de datos. Son repositorios, no publicaciones arbitradas; ninguno figura en `Data/referencias.md`.

#### P014 — Egyptian-Used-Cars

- **Authors**: proyecto `Egyptian-Used-Cars` (autoría no declarada en el corpus)
- **Year**: sin año declarado
- **Venue**: repositorio de código / análisis de mercado (no se indica plataforma ni URL)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete: repositorio no enlazado; imposible verificar autoría, licencia o fecha desde el corpus)**
- **Layer**: L1
- **Cited in document**: yes — línea 277 («uno de los análisis de mercado automotriz más completos que tenemos: 23.500 anuncios, historial mensual de precios, econometría, SQL, Tableau y Power BI»)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — cifra de 23.500 anuncios no contrastable con el anexo

#### P015 — Repos ICD

- **Authors**: ICD (Instituto de Cibernética y Computación; denominación ampliada no declarada en el corpus)
- **Year**: sin año declarado
- **Venue**: repositorio de datos citado como fuente
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 70 (3.958 anuncios ICD) y 57
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — sigla sin desglosar ni enlace

#### P016 — AutosxCuba

- **Authors**: AutosxCuba (proyecto/repositorio)
- **Year**: sin año declarado
- **Venue**: repositorio de datos citado como fuente
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 70
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P017 — Mercado-automotriz

- **Authors**: Mercado-automotriz (proyecto/repositorio)
- **Year**: sin año declarado
- **Venue**: repositorio de datos citado como fuente
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 70
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — agrupado bajo «y otros», sin inventario individual

### Cluster 4 — Directorios, geoservicios y herramientas de adquisición

**Query**: `servicios externos citados en el corpus` ∩ `Data/referencias.md` — búsqueda de nombres de directorios, geocodificadores y librerías anti-bot en los 8 archivos.

El corpus atribuye la procedencia de capas del mapa a servicios y librerías. Son fuentes de datos y herramientas, no obras académicas; ninguna está en `Data/referencias.md`.

#### P018 — Circuitos Habana

- **Authors**: aplicación cubana (autoría no declarada)
- **Year**: sin año declarado
- **Venue**: aplicación que reproduce mensajes públicos de la Empresa Eléctrica
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 248 y 307
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P019 — Empresa Eléctrica (reportes de prensa sobre circuitos)

- **Authors**: Empresa Eléctrica (organismo) / prensa (sin medio identificado)
- **Year**: sin año declarado
- **Venue**: «reportes de prensa» genéricos
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete: ningún reporte puntual identificado)**
- **Layer**: L1
- **Cited in document**: yes — línea 181 («según reportes de prensa ha dejado circuitos con más de 60 horas sin electricidad»)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — afirmación cuantitativa sin fuente verificable en el corpus ni en el anexo

#### P020 — KargalaYa

- **Authors**: KargalaYa (directorio de carga)
- **Year**: sin año declarado
- **Venue**: directorio en línea
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 266 y 807 (como «Kargalaya»)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — denominación inconsistente entre archivos (`KargalaYa` / `Kargalaya`)

#### P021 — ChargeFinder

- **Authors**: ChargeFinder (directorio de carga)
- **Year**: sin año declarado
- **Venue**: directorio en línea
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 266
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P022 — Electromaps

- **Authors**: Electromaps (directorio de carga)
- **Year**: sin año declarado
- **Venue**: directorio en línea
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 266 y 807
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P023 — OpenStreetMap / Overpass

- **Authors**: OpenStreetMap contributors / Overpass API (comunidad y servicio)
- **Year**: sin año declarado
- **Venue**: fuente abierta de geodatos (API Overpass)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete: el corpus nombra el servicio pero no enlaza la consulta ni la licencia)**
- **Layer**: L1
- **Cited in document**: yes — línea 806 (capa `gasolinera`)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P024 — Nominatim / Photon

- **Authors**: OpenStreetMap Nominatim / Komoot Photon (servicios de geocodificación)
- **Year**: sin año declarado
- **Venue**: servicios de geocodificación
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 828 (`geocode_elementos.py`)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P025 — Yellocu

- **Authors**: Yellocu (directorio)
- **Year**: sin año declarado
- **Venue**: directorio web
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 808 (capa `concesionario`)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P026 — Cybo

- **Authors**: Cybo (directorio)
- **Year**: sin año declarado
- **Venue**: directorio web (devuelve 403 / verificación de seguridad según el corpus)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 808 y 833
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P027 — Cubisima / NearPlace / Páginas Amarillas / tallermanolito.com

- **Authors**: cuatro directorios y un sitio de taller (agrupados en el corpus)
- **Year**: sin año declarado
- **Venue**: fuentes de la capa `taller`
- **Citations**: no aplica
- **URL**: solo `tallermanolito.com` aparece como dominio; los demás sin enlace → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 809 (y Cubisima además en la línea 67 como marketplace)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — agrupación sin ficha individual

#### P028 — FlareSolverr / curl_cffi / patchright

- **Authors**: proyectos de software (autoría no declarada en el corpus)
- **Year**: sin año declarado
- **Venue**: librerías y servicio local (`http://127.0.0.1:8191/v1`)
- **Citations**: no aplica
- **URL**: solo la URL local de FlareSolverr → **(metadata incomplete: repositorios y versiones no declarados)**
- **Layer**: L1
- **Cited in document**: yes — línea 833 (y `curl_cffi`/`patchright` en la misma línea)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`. Temáticamente cercano a [21] Krotov et al. y [22] Brown et al., ausentes del corpus
- **Metadata status**: **(metadata incomplete)**

### Cluster 5 — Métodos estadísticos invocados sin cita formal

**Query**: `métodos declarados en MODELOS_Y_FUNCIONES.md` ∩ `Data/referencias.md` — búsqueda de modelo hedónico, Kruskal-Wallis, VIF y Welch en los 8 archivos y en el anexo.

El corpus describe y justifica métodos con rigor metodológico, pero **no los atribuye a ninguna obra**. En `Data/referencias.md` existen antecedentes temáticos ([12] Hulten 2003, [13] Francke & Van de Minne 2020, [9] Du et al. 2026), ninguno citado en el corpus.

#### P029 — Modelo hedónico log-lineal (OLS)

- **Authors**: no atribuido (implementado en `Data/analisis_rentabilidad/04_stats.py`)
- **Year**: sin año de referencia bibliográfica
- **Venue**: `MODELOS_Y_FUNCIONES.md` §3.1
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete: sin obra de respaldo citada)**
- **Layer**: L1
- **Cited in document**: yes — líneas 433, 446, 449–452
- **Document reference**: ninguno; antecedente posible [12] y [13] en `Data/referencias.md`, sin marcador en el corpus
- **source_of_metadata**: corpus; contraste con `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — justificación metodológica sí, atribución bibliográfica no

#### P030 — Kruskal-Wallis

- **Authors**: no atribuido
- **Year**: sin año de referencia bibliográfica
- **Venue**: `MODELOS_Y_FUNCIONES.md` §3.3
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 414 y 460–464 (H = 25,741; p = 1e−05)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P031 — VIF (factor de inflación de varianza)

- **Authors**: no atribuido
- **Year**: sin año de referencia bibliográfica
- **Venue**: `MODELOS_Y_FUNCIONES.md` §3.2
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 454–458 (rango 1,13–1,58)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P032 — Welch t-test

- **Authors**: no atribuido
- **Year**: sin año de referencia bibliográfica
- **Venue**: `MODELOS_Y_FUNCIONES.md` §3.4
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 466–470 (codificado, no ejecutado)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

## Cotejo con las 41 entradas de `Data/referencias.md`

Convención: `Citada en el informe` reproduce el flag del anexo (que alude al informe técnico de la pasada 1, **no** a este corpus); `Citada en el corpus` es el resultado de la búsqueda literal de autor/título/DOI en los 8 archivos. Las 41 entradas dan **cero coincidencias** con el corpus. No hay marcadores `[N]`, DOI ni arXiv en ninguno de los 8 archivos (verificado por búsqueda literal en el texto cacheado).

| Entrada | Obra / fuente (abreviada) | Año | `Citada en el informe` | `Citada en el corpus` | Nota |
|---|---|---:|---|---|---|
| [1] | Akerlof — *The Market for "Lemons"* | 1970 | sí | **no** | **(metadata incomplete: resumen indexado no sustantivo; identidad y DOI verificados en OpenAlex)** |
| [2] | Lewis — *Asymmetric Information… eBay Motors* | 2011 | no | **no** | Nota de discrepancia de año (SSRN 2010 / AER 2011) |
| [3] | Peterson & Schneider — *Adverse selection… CEX* | 2014 | no | **no** | — |
| [4] | Englmaier et al. — *Price Discontinuities* | 2017 | no | **no** | — |
| [5] | Che et al. — *Warranty, Seller Reputation…* | 2019 | no | **no** | — |
| [6] | Wolf & Muhanna — *Adverse Selection and Reputation* | 2005 | no | **no** | — |
| [7] | Sultan — *A model of the used car market…* | 2009 | no | **no** | — |
| [8] | Tilles et al. — *A Markovian model market* | 2011 | no | **no** | — |
| [9] | Du et al. — *Nonlinear Depreciation…* | 2026 | sí (§71.6, §71.14) | **no** | Solapamiento temático con la §4 del storytelling (depreciación) |
| [10] | Kang & Fu — *pricing of used electric vehicles* | 2026 | no | **no** | **(metadata incomplete: resumen no indexado; campos bibliográficos verificados)** |
| [11] | Miranda et al. — *Depreciation Patterns in UAE* | 2026 | no | **no** | — |
| [12] | Hulten — *Price Hedonics: A Critical Review* | 2003 | no | **no** | **(metadata incomplete: PDF no extraído)**; antecedente natural de P029 |
| [13] | Francke & Van de Minne — *unobserved heterogeneity* | 2020 | no | **no** | Antecedente natural de P029 |
| [14] | Gegić et al. — *Car Price Prediction using ML* | 2019 | sí (§71.6, §71.14) | **no** | — |
| [15] | Mutİ & Yıldız — *Using Linear Regression…* | 2023 | no | **no** | — |
| [16] | Jin — *Price Prediction of Used Cars* | 2021 | no | **no** | — |
| [17] | Ahtesham & Zulfiqar — *Used Car Price Prediction with Pyspark* | 2022 | no | **no** | — |
| [18] | Madhusudhanan et al. — *ProbSAINT* | 2024 | sí (§71.14) | **no** | 13 citas verificadas el 27/11/2026 |
| [19] | Pal et al. — *How much is my car worth?* | 2017 | no | **no** | Nota de discrepancia de año (preprint 2017 / publicación 2018) |
| [20] | Arefin — *Second Hand Price Prediction for Tesla* | 2021 | no | **no** | 9 citas verificadas el 27/11/2026 |
| [21] | Krotov et al. — *Legality and Ethics of Web Scraping* | 2020 | no | **no** | Solapamiento temático con la línea 112 (términos de uso) y P028 |
| [22] | Brown et al. — *Web scraping for research* | 2025 | no | **no** | Solapamiento temático con la línea 112 y P028 |
| [23] | Priestley et al. — *Data Quality Requirements… ML* | 2023 | no | **no** | Solapamiento con AUTOMATIZACION.md §4 |
| [24] | Hohensinner et al. — *Tracing the Data Trail* | 2026 | no | **no** | Solapamiento con AUTOMATIZACION.md §5 |
| [25] | Wenger et al. — *Data Isotopes for Data Provenance* | 2024 | no | **no** | — |
| [26] | Muça et al. — *Pipeline… Albania* | 2026 | sí (§71.6, §71.14) | **no** | — |
| [27] | Essien et al. — *Ethics of Web Scraping In Research* | 2023 | no | **no** | — |
| [28] | Paige — *Legality and Ethics… Archaeology* | 2024 | no | **no** | — |
| [29] | Vidal Alejandro et al. — *AI in the informal currency market: Cuba* | 2024 | sí (§71.6, §71.14) | **no** | Solapamiento directo con P004 (TRMI informal) |
| [30] | Castro Fernández et al. — *Electromobility and Energy Transition in Cuba* | 2024 | no | **no** | Solapamiento con §§2, 5 y 6 del storytelling |
| [31] | Ritter — *Cuba's Underground Economy* | 2004 | no | **no** | — |
| [32] | Ávila Castellanos — *Currency exchange in post-ordenamiento Cuba* | 2024 | no | **no** | Solapamiento con P004 |
| [33] | Guerra — *geography of car ownership in Mexico City* | 2015 | no | **no** | — |
| [34] | Klein et al. — *Transitions into and out of Car Ownership* | 2023 | no | **no** | — |
| [35] | Srisan et al. — *Auto insurance affordability…* | 2026 | no | **no** | — |
| [36] | Holtz et al. — *Reducing Interference Bias…* | 2020 | no | **no** | — |
| [37] | Etro — *Product Selection in Online Marketplaces* | 2020 | no | **no** | — |
| [38] | Quariguasi Frota Neto et al. — *Market prices… eBay* | 2015 | no | **no** | Nota de discrepancia de año (2015 OpenAlex / 2016 Crossref) |
| [39] | DfT / DVLA — *Vehicle statistics* (GOV.UK) | sin año | campo ausente | **no** | **(metadata incomplete: URL profunda no confirmada)**; fuente institucional foránea, ausente del corpus |
| [40] | ANFAC — *Informes del sector automotriz español* | sin año | sí (institucional §70) | **no** | Fuente institucional foránea, ausente del corpus |
| [41] | AEADE — *Estadísticas de matriculaciones* | sin año | sí (institucional §70) | **no** | Fuente institucional foránea, ausente del corpus |

Cuatro entradas del anexo llevan `(metadata incomplete)` —[1], [10], [12] y [39]— y tres registran discrepancias de año —[2], [19] y [38]—. Esas marcas se conservan tal cual; las 37 fuentes del corpus inventariadas arriba se marcan todas `(metadata incomplete)` porque el corpus no da metadatos verificables y el anexo no las contiene.

## Recency distribution

Convenio: «In map» cuenta los 37 IDs `P001`–`P037`; «In document bibliography» cuenta las 41 entradas de `Data/referencias.md` (38 con año; [39]–[41] sin año). La fila «Rango 2014–2025» corresponde a ONEI (P001), que declara un intervalo y no un año único. Los años del mapa son los declarados en el propio corpus o heredados de las obras ausentes propuestas en «Likely missing».

| Year | In map | In document bibliography |
|---|---:|---:|
| 2026 | 6 | 6 |
| 2025 | 1 | 1 |
| 2024 | 3 | 6 |
| 2023 | 0 | 4 |
| 2022 | 0 | 1 |
| ≤2021 | 2 | 20 |
| Rango 2014–2025 (ONEI) | 1 | 0 |
| Sin año verificable | 24 | 3 |

Las seis entradas 2026 del mapa son [P002] Gaceta Oficial 65/2026, [P004] elTOQUE (18/11/2026), [P010] Decreto 163/2026, [P011] resoluciones /2026, [P012] resoluciones 171–175 y 340 y [P013] Circular 03/2026; la de 2024 es [P009] Acuerdo 9811; la de 2025 es [P036] Brown et al.; las de ≤2021 son [P035] Krotov et al. (2020) y [P037] Hulten (2003).

## Venue distribution

| Venue | Count in map |
|---|---:|
| Instituciones y organismos cubanos (ONEI, Gaceta, BCC, elTOQUE, CIMEX, MEP, MFP, Gobierno) | 8 |
| Instrumentos normativos (acuerdo, decreto, resoluciones, circular) | 5 |
| Repositorios y proyectos de referencia | 4 |
| Directorios, geoservicios y herramientas de adquisición | 11 |
| Métodos estadísticos sin atribución bibliográfica | 4 |
| Revistas / congresos del anexo (obras temáticamente cercanas, no citadas) | 5 |

## Likely missing important works

Criterio adaptado: se listan obras de `Data/referencias.md` que, por solapamiento directo con una afirmación load-bearing del corpus, deberían plausiblemente citarse en la documentación de usuario y no lo están. No se proponen obras nuevas porque no se ejecutaron búsquedas.

### P033 — Using AI in the informal currency market: evidence from Cuba

- Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A. (2024), *Applied Economics*; [29] en `Data/referencias.md`, `Citada en el informe: sí`.
- **Cluster**: Fuentes institucionales y estadísticas cubanas.
- **Why likely missing**: el corpus hace de la TRMI informal (930 CUP/USD, línea 242) una de las «cuatro fuerzas invisibles» y la usa para convertir todos los precios (línea 73); [29] estudia exactamente ese mercado informal de divisas en Cuba y ya está verificada en el anexo, pero no aparece en ninguno de los 8 archivos.

### P034 — Electromobility and Energy Transition in Cuba

- Castro Fernández, M.; Vilaragut Llanes, M.; Hernández, J. C. (2024), *Sustainability*; [30] en `Data/referencias.md`, `Citada en el informe: no`.
- **Cluster**: Métodos y contexto del storytelling.
- **Why likely missing**: las secciones 2, 5 y 6 del storytelling sostienen afirmaciones sobre electrolineras, coste de propiedad eléctrica y red de carga (11 estaciones solares Dongfeng/NWI y 21 de CIMEX+MITRANS, línea 265) sin respaldo bibliográfico; [30] es el antecedente cubano directo.

### P035 — Legality and Ethics of Web Scraping

- Krotov, V.; Johnson, L.; Silva, L. (2020), *Communications of the Association for Information Systems*; [21] en `Data/referencias.md`, `Citada en el informe: no`.
- **Cluster**: Directorios, geoservicios y herramientas de adquisición.
- **Why likely missing**: la línea 112 afirma que el proyecto «respeta los términos de uso de los portales: no elude mecanismos anti-automatización», mientras la línea 833 describe impersonación de Chrome/Safari, `patchright` y FlareSolverr para esquivar 403; [21] es un marco de referencia estándar para esa tensión y está en el anexo sin citar en el corpus.

### P036 — Web scraping for research: Legal, ethical, institutional, and scientific considerations

- Brown, M. A.; Gruen, A.; Maldoff, G.; Messing, S.; Sanderson, Z.; Zimmer, M. T. (2025), *Big Data & Society*; [22] en `Data/referencias.md`, `Citada en el informe: no`.
- **Cluster**: Directorios, geoservicios y herramientas de adquisición.
- **Why likely missing**: misma razón que P035 y además es la obra más reciente (2025) del subárea; el corpus de documentación es la cara pública del proyecto y no registra ninguno de los dos marcos éticos.

### P037 — Price Hedonics: A Critical Review

- Hulten, C. R. (2003), *Federal Reserve Bank of New York Economic Policy Review*; [12] en `Data/referencias.md`, `Citada en el informe: no`, `(metadata incomplete: PDF no extraído)`.
- **Cluster**: Métodos estadísticos invocados sin cita formal.
- **Why likely missing**: `MODELOS_Y_FUNCIONES.md` §3.1 dedica varios párrafos a justificar el modelo hedónico log-lineal (líneas 433–452) y declara explícitamente que «los atributos hedónicos… son los determinantes estándar» (línea 446) sin citar la revisión crítica canónica. La marca `(metadata incomplete)` se hereda del anexo: el PDF no fue extraído en la verificación del 27/11/2026.

## Hypothesis checks (from plan)

El plan no declara hipótesis; las cuatro siguientes se derivan del mandato recibido y son observaciones sin veredicto.

### H1 — Los trabajos académicos citados en el corpus coinciden con las 41 entradas de `Data/referencias.md` (derivada)

Estado de la evidencia: **no hay coincidencia alguna**. La búsqueda literal de los 41 apellidos/títulos en el texto cacheado da cero resultados (los únicos aciertos parciales de cadena —«Che,», «Pal,», «Etro»— resultaron ser falsos positivos dentro de «Chevrolet», «página» y «película»). Tampoco hay marcadores `[N]`, DOI ni `arXiv` en los 8 archivos. Las única menciones de tipo metodológico son «Kruskal-Wallis» y «modelo hedónico», sin atribución. El anexo y el corpus describen, por tanto, dos regímenes de citas distintos: el anexo documenta la literatura del informe técnico; el corpus documenta el proyecto para el usuario.

### H2 — Las fuentes institucionales del corpus están representadas en el bloque [39]–[41] del anexo (derivada)

Estado de la evidencia: **no**. El corpus cita organismos cubanos (ONEI, Gaceta Oficial, BCC, CIMEX, MEP, MFP, Consejo de Ministros, Gobierno) y disposiciones cubanas (Decreto 163/2026, resoluciones 104/17/52/102/2026, 171–175, 340, Acuerdo 9811/2024, Circular 03/2026). El bloque institucional del anexo son tres fuentes foráneas —DfT/DVLA (GOV.UK), ANFAC y AEADE— vinculadas al informe técnico (§§18 y 70) y ausentes del corpus. No hay ni un solo nombre compartido entre ambos conjuntos. [39] además arrastra `(metadata incomplete: URL profunda no confirmada)` y carece del campo `Citada en el informe`.

### H3 — Toda fuente citada en el corpus tiene metadatos verificables (derivada)

Estado de la evidencia: **no; 37 de 37 lo tienen marcado `(metadata incomplete)` en este mapa**. Ninguna de las fuentes del corpus aporta DOI, arXiv, URL de destino y año de publicación a la vez. Solo se verifican localmente identificadores internos —Decreto 163/2026, Gaceta Oficial 65/2026, Acuerdo 9811/2024, Circular 03/2026, TRMI del 18/11/2026— y la URL local de FlareSolverr; ninguno de ellos permite resolver la ficha bibliográfica. El corpus declara explícitamente una limitación de verificabilidad en la línea 114 (elTOQUE «no responde de forma estable») y en la línea 181 («según reportes de prensa» sin medio identificado), coherente con la marca.

### H4 — Los métodos declarados en el corpus están respaldados por bibliografía identificable (derivada)

Estado de la evidencia: **respaldados en el anexo, no en el corpus**. `MODELOS_Y_FUNCIONES.md` justifica el modelo hedónico, VIF, Kruskal-Wallis y Welch con argumentos estadísticos correctos (líneas 433–470), pero sin remitir a obra alguna. En `Data/referencias.md` sí existen [12] Hulten (revisión crítica de precios hedónicos, `(metadata incomplete)`), [13] Francke & Van de Minne (heterogeneidad no observada) y [9] Du et al. (depreciación no lineal y heterogeneidad de marca), todos con `Citada en el informe: no` y ninguno citado en el corpus. La consecuencia observable es una documentación metodológicamente argumentada pero bibliográficamente muda en su cara pública.

## Sources used

- WebSearch queries: 0 (cotejo dirigido; sin búsquedas temáticas nuevas).
- WebFetch URLs: 0; no se re-fetcharon GOV.UK, anfac.com, aeade.net ni ninguna URL del corpus.
- Semantic Scholar API hits: 0.
- OpenAlex API hits: 0 nuevos; los metadatos, conteos de citas y marcas `(metadata incomplete)` se heredan de la verificación del 27/11/2026 consignada en `Data/referencias.md`.
- Archivos locales inspeccionados: `reviews/corpus-documentacion-2026-11-28.plan.md` (24 líneas); `.playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md` (833 líneas; inventario completo de 8 archivos); `Data/referencias.md` (41 entradas, líneas 1–87); `reviews/informe-tecnico-2026-11-28-iter4.e2-literature.md` (convención de formato y tratamiento de `[39]`–`[41]`).
- Degradación: `degraded: false` para el mandato recibido —las 41 entradas, los marcadores `[N]`/DOI/arXiv y las 37 fuentes del corpus quedaron resueltos por inspección directa—. Limitación declarada: sin búsqueda bibliográfica nueva, sin lectura de resúmenes y sin re-fetch de URLs; este mapa sirve para el cotejo de citas entre el corpus y el anexo, no para proponer obras externas nuevas ni para certificar enlaces institucionales.

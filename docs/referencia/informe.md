# Informe técnico / Technical report

**Proyecto / Project:** El precio de moverse en Cuba (antes / formerly *AutoDecide Habana* e *ICD Automotive Market Project*)  
**Autor / Author:** responsable del proyecto / project owner  
**Fecha / Date:** 23 de noviembre de 2026  
**Ubicación / Location:** `~/Proyectos/El precio de moverse en Cuba`  
**Estado / Status:** Fase 6 — scraping y captura de catálogos y anuncios, en curso / Phase 6 — scraping and capture, in progress  
**Idioma / Language:** español e inglés / Spanish and English

---

# Parte I — Español

## 1. Objetivo

El proyecto se llama **El precio de moverse en Cuba**. Su objetivo actual es realizar un **análisis del mercado automotor cubano**: caracterizar estructura, precios, oferta, segmentos, tendencias, asequibilidad y condiciones de rentabilidad. La definición de un producto interactivo que recomiende la compra más rentable según las preocupaciones del usuario queda diferida a una especialización posterior. El análisis se apoya en dos pilares: la base de datos del mercado cubano y un pipeline de scraping reutilizable que se actualiza para adaptarse al momento en que se revise.

Se conservan los nombres anteriores, *AutoDecide Habana* e *ICD Automotive Market Project*, para mantener la trazabilidad de la documentación ya producida.

## 2. Estado y fases

Las fases se redefinieron para que la fase activa sea la sexta. Estado a 17/11/2026:

| Fase | Nombre | Estado |
|---|---|---|
| 1 | Marco normativo y regulatorio | Completada |
| 2 | Descubrimiento y verificación de fuentes | Completada |
| 3 | Infraestructura técnica y herramientas | Completada |
| 4 | Corpus documental y trabajos investigativos | Completada |
| 5 | Diseño del esquema de datos y del pipeline | Completada |
| 6 | **Scraping y captura de catálogos y anuncios** | **En curso** |
| 7 | Unificación, limpieza y control de calidad | Pendiente |
| 8 | Análisis de mercado, comparables y rentabilidad | Pendiente |
| 9 | Documentación final, informe PDF y entrega | Pendiente |

La creación de este informe y del `README.md` es soporte transversal y no cambia la fase activa.

**Nota de actualización (27/11/2026):** esta tabla registra el estado al 17/11/2026. El pipeline de análisis (fase 8) se creó después, el 18/11/2026 (§34), y sus resultados vigentes se documentan en §59–§60.

## 3. Organización de carpetas

```text
ICD Automotive Market Project/
├── README.md
├── INFORME_TECNICO.md / INFORME_TECNICO.pdf
├── .gitignore
├── Anexos/                  # corpus legal y documentos de apoyo
├── Auxiliares/              # .venv, cache, herramientas, Repositorios, Referencias
├── Copias/                  # 4 repos de referencia (excluidos de este informe)
├── Data/                    # investigaciones, verificaciones y SQLite por tienda
└── Hombros/                 # PDFs, HTML, repos y derivadas
```

Decisiones de diseño: todo el material auxiliar vive dentro de `Auxiliares/`; los clones se hicieron con `--depth 1` y se registraron en `~/Utilidades/HerramientasScraping/_clone_log.tsv`; la descubrimiento se separó de la verificación; `Copias/` no se registra en este informe por decisión explícita.

## 4. Fase 1 — Marco normativo y regulatorio

Se documentaron **17 empresas autorizadas** a importar y comercializar vehículos, distribuidores privados (BDC One, Dongfeng, MCV, Finauto, Changan, Chinautos, Envision, ATR Export), precios de referencia (BDC One 14.849–31.478 EUR; Dongfeng desde 21.900 EUR; Finauto desde 15.500 EUR; ATR Export con 46 modelos), aranceles y parque automotor. La norma marco es el **Decreto 163/2026** (Gaceta Oficial No. 65 Ordinaria, 04/08/2026, vigente desde el 11/08/2026), que deroga el Decreto 119/2024. Se cotejaron las resoluciones 104/2026 (MINCEX), 17/2026 (MINCIN), 52/2026 (MITRANS), 171–175/2026 (MFP), 312/2026, derogada por 340/2026 (Aduana) y 102/2026 (BCC). Resultado: `Data/investigacion-mercado-automotor-cuba.md` y `Data/verificacion-marketplaces-tiendas-organismos-2026-11-16.md`.

## 5. Fase 2 — Descubrimiento y verificación de fuentes

Dos búsquedas iniciales en DuckDuckGo, 30 páginas cada una, con bloqueo por CAPTCHA: se cambió a Yahoo y visitas directas. Se consolidaron **409 resultados, 400 únicos**. Se inventariaron **35 sitios** de compraventa en `Data/mercados-compraventa-cuba.md` y repositorios útiles en `Data/github-scraping-repos.md`.

Se verificaron **40 sitios/URLs**. Marketplaces con sección activa: Autocubana (667 vehículos), iTENCEL (951), VentaCuba (801 carros/camionetas), Timbirichi (281 carros), Revolico (112 enlaces en la primera página), Cogetucarro (5.225 anuncios), Cubisima (155 fichas), Apululu y Carros.com Cuba. Se corrigieron clasificaciones: Mercadoba y Fagales Market sin sección real; TuCuevita, Mercubano, Mercandil, Revoltillo, QvaVentas, Casinuevo, Publicid, WAnuncios y AnunciosCuba con categoría vacía; BizneCubano, Katapulk, A la Venta, Pymes Bulevar, MeroliCU y Rico Cuba son de piezas, motos o servicios.

Se documentaron **14 organismos** con competencia sobre el mercado: Consejo de Ministros/Estado, MINCEX, MINCIN, MITRANS, CEMA, MFP, ONAT, Aduana General, BCC, MININT, MINJUS, MEP, MINREX y MINSAP.

## 6. Fase 3 — Infraestructura técnica y herramientas

Se clonaron **61 repositorios** en `Auxiliares/Repositorios` con `--depth 1` (2,2 GB, 61 entradas `OK`). El conjunto cubre scraping general (Firecrawl, browser-use, Scrapling, crawl4ai, Scrapy, SeleniumBase, trafilatura, curl_cffi, Patchright, Playwright), Facebook, WhatsApp, Telegram y CAPTCHA. Se clasificaron **92 proyectos** de CAPTCHA en `Data/github-captcha-repos.md` y se seleccionaron 9.

Se creó `Auxiliares/.venv` con patchright 1.64.4, PyPasser 1.1.0, Scrapling 0.5.1, ddddocr 1.6.1, playwright 1.65.2, curl_cffi 0.17.0, trafilatura, pandas, numpy, onnxruntime 1.32.0, ddgs 9.16.1 y tenacity 9.2.1. Se usa el Chromium del sistema y FlareSolverr 3.5.2 en Docker (`http://127.0.0.1:8191/`).

Herramientas creadas: `ddg_research.py`, `buscar_fallback.py`, `descargar_hombros.py`, `scrape_concesionarios.py`, `resumen_catalogos.py` y `actualizar_informe.py`.

## 7. Fase 4 — Corpus documental y trabajos investigativos

Tres búsquedas con la regla de parar tras 10 páginas sin enlaces útiles (útil = primera aparición de un trabajo investigativo automotriz):

| Búsqueda | Páginas | Resultados | Útiles | Parada |
|---|---:|---:|---:|---|
| `mercado automovilistico trabajos investigativos` | 112 | 1.086 | 11 | página 19 |
| `rentabilidad del precio de automoviles trabajos investigativos` | 24 | 226 | 2 | página 11 |
| `calidad precio mercado automotriz trabajo investigativo` | 23 | 230 | 10 | página 22 |

El material se guardó en `Hombros/`: descarga inicial **93 OK / 17 fallos**, rentabilidad **23 OK / 10 fallos**, calidad/precio **78 OK / 36 fallos**, con `manifest.jsonl` e `indice.md`.

## 8. Fase 5 — Diseño del esquema de datos y del pipeline

Se diseñó una base SQLite por tienda con una tabla `vehiculos`: identificación (`url`, `shop`, `title`, `status`, `scraped_at`), metadatos y 30 campos estructurados (`marca`, `modelo`, `anio`, `precio`, `moneda`, `km`, `combustible`, `transmision`, `potencia`, etc.), además de campos sin normalizar (`tables_json`, `jsonld_json`, `raw_html`, ...). El scraper `scrape_concesionarios.py` usa adaptadores por dominio y renderizado opcional con Playwright.

## 9. Fase 6 — Scraping y captura (en curso)

Se prepararon 11 bases y se obtuvieron **256 filas**:

| Tienda | Filas | Con precio |
|---|---:|---:|
| AGN Motors | 60 | 45 |
| ATR Export | 6 | 5 |
| BDC One | 19 | 3 |
| Changan | 2 | 2 |
| Chinautos Cuba | 70 | 0 |
| ConnectingCuba | 1 | 1 |
| Dongfeng Cuba | 45 | 16 |
| Envision Autos | 1 | 0 |
| Finauto | 45 | 34 |
| MCV Commercial | 4 | 0 |
| La Subasta Cubana | 3 | 3 |

Excluidas por bloqueo técnico: carrosw (HTTP 403 con Bot Verification), LlamaCuba (timeout) y SASA/DIVEP (sin catálogo). Mejor densidad: AGN Motors, Chinautos Cuba, Dongfeng Cuba y Finauto. Esta fase sigue abierta: quedan por ampliar fuentes y completar campos.

## 10. Marco legal para la recolección y el análisis de datos

Solo se incluyen las normas y fuentes relevantes para el contexto del proyecto:

- **Decreto 163/2026**, Gaceta Oficial No. 65 Ordinaria (04/08/2026): regula la importación y comercialización de vehículos; define el marco sobre el que debe trabajar el análisis de precios y oferta.
- **Resolución 104/2026 (MINCEX), 17/2026 (MINCIN), 52/2026 (MITRANS), 171–175/2026 (MFP), 312/2026, derogada por 340/2026 (Aduana) y 102/2026 (BCC)**: desarrollos sectoriales, fiscales y cambiarios que condicionan el mercado.
- **Condiciones de uso de cada portal**: criterio operativo para la recolección. No se eluden mecanismos anti-automatización; los HTTP 403/429 se registran como limitación.
- **Protección de datos personales, ciberseguridad y derechos de autor**: antes de publicar resultados deben verificarse las normas cubanas vigentes y aplicar solo datos agregados, sin nombres, teléfonos ni información personal de anunciantes.
- `~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe, solo se citan las normas anteriores.

## 11. Problemas y soluciones

| Problema | Solución |
|---|---|
| CAPTCHA en paginación DDG | Yahoo + visitas directas; después sesión con `vqd`. |
| HTTP 202 y página “anomaly” | Pausa 7–10 s con jitter, backoff exponencial y cooldown. |
| Falso “anomaly” en HTTP 200 | Detector ajustado para exigir texto real de anomalía. |
| carrosw anti-bot | Registrado como limitación; no se falsificó su contenido. |
| Sitios JS-heavy | Renderizado con Chromium del sistema desde Playwright. |
| Repetidos y mirrors | Deduplicación por título normalizado, prefijo y dominio. |

## 12. Conclusiones

1. El mercado habanero tiene nueve marketplaces con inventario real y una docena con categorías vacías o solo piezas.
2. El marco regulatorio vigente es el Decreto 163/2026 y el paquete de resoluciones citado.
3. El scraping sostenible depende del ritmo, la sesión y la reanudación, no principalmente del fingerprint TLS.
4. La regla de las 10 páginas evitó consumir resultados repetidos.
5. El análisis de mercado y el modelo de rentabilidad (fase 8) están implementados en `Data/analisis_rentabilidad/` y se regeneran de forma automática; la definición del producto interactivo se difiere a una especialización futura.

---

# Part II — English

## 1. Objective

The project is named **El precio de moverse en Cuba**. Its current goal is to analyse the Cuban automotive market —structure, prices, supply, segments, trends, affordability and profitability conditions—. Defining an interactive product that recommends the most profitable purchase is deferred to a later specialisation. The analysis rests on two pillars: the market database and a reusable scraping pipeline that is updated to match the moment of review.

The former name, *ICD Automotive Market Project*, is kept for traceability of existing documentation.

## 2. Status and phases

Phases were redefined so that the active phase is the sixth. Status as of 17 Nov 2026:

| Phase | Name | Status |
|---|---|---|
| 1 | Regulatory framework | Complete |
| 2 | Source discovery and verification | Complete |
| 3 | Technical infrastructure and tools | Complete |
| 4 | Document corpus and research | Complete |
| 5 | Data schema and pipeline design | Complete |
| 6 | **Scraping and capture of catalogues and listings** | **In progress** |
| 7 | Unification, cleaning and QA | Pending |
| 8 | Analysis, profitability model and interactive product | Pending |
| 9 | Final documentation, PDF report and delivery | Pending |

Creating this report and the `README.md` is cross-cutting support and does not change the active phase.

**Update note (27/11/2026):** this table records the status as of 17 Nov 2026. The analysis pipeline (phase 8) was created later, on 18 Nov 2026 (§34), and its current results are documented in §59–§60.

## 3. Folder structure

```text
ICD Automotive Market Project/
├── README.md
├── INFORME_TECNICO.md / INFORME_TECNICO.pdf
├── .gitignore
├── Anexos/                  # legal corpus and supporting documents
├── Auxiliares/              # .venv, cache, tools, cloned repos
├── Copias/                  # 4 reference repos (excluded from this report)
├── Data/                    # research, verification and per-store SQLite
└── Hombros/                 # PDFs, HTML, repos and derivatives
```

Design decisions: all auxiliary material lives under `Auxiliares/`; clones used `--depth 1` and are logged in `~/Utilidades/HerramientasScraping/_clone_log.tsv`; discovery was separated from verification; `Copias/` is excluded from this report by explicit decision.

## 4. Phase 1 — Regulatory framework

**17 authorized companies** were documented, along with private distributors (BDC One, Dongfeng, MCV, Finauto, Changan, Chinautos, Envision, ATR Export), reference prices (BDC One 14,849–31,478 EUR; Dongfeng from 21,900 EUR; Finauto from 15,500 EUR; ATR Export with 46 models), tariffs and the vehicle fleet. The framework is **Decree 163/2026** (Official Gazette No. 65, 04/08/2026, in force since 11/08/2026), which repeals Decree 119/2024. Resolutions 104/2026 (MINCEX), 17/2026 (MINCIN), 52/2026 (MITRANS), 171-175/2026 (MFP), 312/2026, repealed by 340/2026 (Customs) and 102/2026 (BCC) were cross-checked. Results: `Data/investigacion-mercado-automotor-cuba.md` and `Data/verificacion-marketplaces-tiendas-organismos-2026-11-16.md`.

## 5. Phase 2 — Source discovery and verification

Two initial DuckDuckGo searches, 30 pages each, blocked by CAPTCHA: switched to Yahoo and direct visits. **409 results, 400 unique**. A **35-site** inventory was produced in `Data/mercados-compraventa-cuba.md` and useful repos in `Data/github-scraping-repos.md`.

**40 sites/URLs** were verified. Active marketplaces: Autocubana (667 vehicles), iTENCEL (951), VentaCuba (801 cars/pickups), Timbirichi (281 cars), Revolico (112 links on page 1), Cogetucarro (5,225 ads), Cubisima (155 listings), Apululu and Carros.com Cuba. Corrections: Mercadoba and Fagales Market have no real section; several sites have empty categories; others only sell parts or motorcycles.

**14 organizations** with market competence were documented: Council of Ministers/State, MINCEX, MINCIN, MITRANS, CEMA, MFP, ONAT, General Customs, BCC, MININT, MINJUS, MEP, MINREX and MINSAP.

## 6. Phase 3 — Technical infrastructure and tools

**61 repositories** were cloned into `Auxiliares/Repositorios` with `--depth 1` (2.2 GB, 61 `OK` entries), covering general scraping, Facebook, WhatsApp, Telegram and CAPTCHA. **92 CAPTCHA projects** were classified in `Data/github-captcha-repos.md`; 9 were selected.

`Auxiliares/.venv` was created with patchright 1.64.4, PyPasser 1.1.0, Scrapling 0.5.1, ddddocr 1.6.1, playwright 1.65.2, curl_cffi 0.17.0, trafilatura, pandas, numpy, onnxruntime 1.32.0, ddgs 9.16.1 and tenacity 9.2.1. System Chromium and FlareSolverr 3.5.2 in Docker are used.

Tools created: `ddg_research.py`, `buscar_fallback.py`, `descargar_hombros.py`, `scrape_concesionarios.py`, `resumen_catalogos.py` and `actualizar_informe.py`.

## 7. Phase 4 — Document corpus and research

Three searches with a stop rule after 10 pages without useful links (useful = first appearance of an automotive research work):

| Search | Pages | Results | Useful | Stopped at |
|---|---:|---:|---:|---|
| `mercado automovilistico trabajos investigativos` | 112 | 1,086 | 11 | page 19 |
| `rentabilidad del precio de automoviles trabajos investigativos` | 24 | 226 | 2 | page 11 |
| `calidad precio mercado automotriz trabajo investigativo` | 23 | 230 | 10 | page 22 |

Material was saved under `Hombros/`: initial download **93 OK / 17 failures**, profitability **23 OK / 10 failures**, quality/price **78 OK / 36 failures**, with `manifest.jsonl` and `indice.md`.

## 8. Phase 5 — Data schema and pipeline design

A SQLite database per store was designed with a `vehiculos` table: identification (`url`, `shop`, `title`, `status`, `scraped_at`), metadata, 30 structured fields (`brand`, `model`, `year`, `price`, `currency`, `km`, `fuel`, `transmission`, `power`, etc.) and unstructured fields (`tables_json`, `jsonld_json`, `raw_html`, ...). `scrape_concesionarios.py` uses per-domain adapters and optional Playwright rendering.

## 9. Phase 6 — Scraping and capture (in progress)

11 databases were prepared and **256 rows** obtained:

| Store | Rows | With price |
|---|---:|---:|
| AGN Motors | 60 | 45 |
| ATR Export | 6 | 5 |
| BDC One | 19 | 3 |
| Changan | 2 | 2 |
| Chinautos Cuba | 70 | 0 |
| ConnectingCuba | 1 | 1 |
| Dongfeng Cuba | 45 | 16 |
| Envision Autos | 1 | 0 |
| Finauto | 45 | 34 |
| MCV Commercial | 4 | 0 |
| La Subasta Cubana | 3 | 3 |

Excluded due to technical blocks: carrosw (HTTP 403 Bot Verification), LlamaCuba (timeout) and SASA/DIVEP (no catalogue). Best density: AGN Motors, Chinautos Cuba, Dongfeng Cuba and Finauto. This phase is still open: more sources and fields are pending.

## 10. Legal framework for data collection and analysis

Only relevant norms and sources are included:

- **Decree 163/2026**, Official Gazette No. 65 (04/08/2026): regulates vehicle import and sales; defines the framework for price and supply analysis.
- **Resolution 104/2026 (MINCEX), 17/2026 (MINCIN), 52/2026 (MITRANS), 171-175/2026 (MFP), 312/2026, repealed by 340/2026 (Customs), 102/2026 (BCC)**: sectoral, fiscal and exchange-rate conditions.
- **Terms of use of each site**: operational rule for collection. Anti-automation mechanisms are not bypassed; HTTP 403/429 are recorded as limitations.
- **Personal data protection, cybersecurity and copyright**: before publishing results, current Cuban rules must be verified and only aggregated data used, with no names, phone numbers or personal information from advertisers.
- `~/Utilidades/Leyes/gaceta_catalog.json` is the reference index; the full gazette corpus is not logged entry by entry here.

## 11. Problems and solutions

| Problem | Solution |
|---|---|
| CAPTCHA on DDG pagination | Yahoo + direct visits; later a `vqd` session. |
| HTTP 202 and "anomaly" page | 7-10 s pause with jitter, exponential backoff and cooldown. |
| False "anomaly" on HTTP 200 | Detector adjusted to require actual anomaly text. |
| carrosw anti-bot | Recorded as a limitation; content was not faked. |
| JS-heavy sites | Rendering with system Chromium via Playwright. |
| Duplicates and mirrors | Deduplication by normalized title, prefix and domain. |

## 12. Conclusions

1. The Havana market has nine marketplaces with real inventory and a dozen with empty categories or parts only.
2. The current regulatory framework is Decree 163/2026 and the cited resolutions.
3. Sustainable scraping depends on pace, session and resumability, not mainly on TLS fingerprinting.
4. The 10-page rule prevented consuming repeated results.
5. The market analysis and the profitability model (phase 8) are implemented under `Data/analisis_rentabilidad/` and regenerate automatically; the interactive product is deferred to a later specialisation.

---

# 13. Registro de altas / Change log

Registro automático de todo lo que se añade a la carpeta del proyecto. El script `Auxiliares/herramientas/actualizar_informe.py` añade filas debajo del marcador y regenera el PDF. `Copias/` queda excluido por decisión explícita.

Automatic record of everything added to the project folder. The script appends rows below the marker and regenerates the PDF. `Copias/` is excluded by explicit decision.

| Fecha / Date | Ruta / Path | Tipo / Type | Origen / Source | Tamaño / Size | Fase / Phase | Descripción / Description | Estado / Status |
|---|---|---|---|---|---|---|---|
<!-- REGISTRO_ALTAS -->
| 2026-11-17 | `Auxiliares/herramientas/scrape_revolico_pipeline.py` | script / script | — | 19 994 B | 3 / 3 | Pipeline de 3 etapas con colas persistentes para Revolico. | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico` | carpeta / folder | — | carpeta / folder (15 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/.backfill_completo` | archivo / file | — | 122 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/pipeline.sqlite` | base de datos / database | — | 211 513 344 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/progreso.md` | documento / document | — | 422 B | 2 / 2 | Progreso Revolico — 2026-11-18T00:44:26+00:00 | Actualizado / Updated |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 147 716 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `Auxiliares/herramientas/scrape_revolico_pipeline.py` | script / script | — | 19 592 B | 3 / 3 | Pipeline de 3 etapas con colas persistentes para Revolico. | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico` | carpeta / folder | — | carpeta / folder (14 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/pipeline.sqlite` | base de datos / database | — | 190 513 152 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 146 073 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | … | aviso / notice | — | — | — | 175 entradas adicionales no listadas / omitted | Pendiente / Pending |

| 2026-11-17 | `.gitattributes` | archivo / file | — | 184 B | 7 / 7 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `.gitignore` | archivo / file | — | 1 070 B | 9 / 9 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/whatsapp` | carpeta / folder | — | carpeta / folder (5 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/whatsapp/whatsapp_web_scraper.py` | script / script | — | 4 530 B | 3 / 3 | Scraper de WhatsApp Web mediante Playwright (sin WAHA/Docker). | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/limpiar_revolico.py` | script / script | — | 8 049 B | 3 / 3 | Limpieza de la BD de Revolico: solo vehículos de 4+ ruedas con datos útiles. | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico` | carpeta / folder | — | carpeta / folder (10 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/pipeline.sqlite` | base de datos / database | — | 189 161 472 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/progreso.md` | documento / document | — | 422 B | 2 / 2 | Progreso Revolico — 2026-11-18T00:03:55+00:00 | Actualizado / Updated |
| 2026-11-17 | `Data/catalogos_concesionarios/marketplaces/apululu.sqlite` | base de datos / database | — | 132 B | 6 / 6 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/catalogos_concesionarios/marketplaces/autocubana.sqlite` | base de datos / database | — | 132 B | 6 / 6 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/catalogos_concesionarios/marketplaces/carroscom.sqlite` | base de datos / database | — | 132 B | 6 / 6 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/catalogos_concesionarios/marketplaces/cogetucarro.sqlite` | base de datos / database | — | 132 B | 6 / 6 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/catalogos_concesionarios/marketplaces/cubisima.sqlite` | base de datos / database | — | 132 B | 6 / 6 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/catalogos_concesionarios/marketplaces/itencel.sqlite` | base de datos / database | — | 132 B | 6 / 6 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/catalogos_concesionarios/marketplaces/timbirichi.sqlite` | base de datos / database | — | 132 B | 6 / 6 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/catalogos_concesionarios/marketplaces/ventacuba.sqlite` | base de datos / database | — | 132 B | 6 / 6 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/integraciones` | carpeta / folder | — | carpeta / folder (2 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Data/integraciones/telegram/telegram.sqlite` | base de datos / database | — | 131 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/integraciones/whatsapp` | carpeta / folder | — | carpeta / folder (5 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile` | carpeta / folder | — | carpeta / folder (12 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/BrowserMetrics-spare.pma` | archivo / file | — | 4 194 304 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default` | carpeta / folder | — | carpeta / folder (75 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Account Web Data` | archivo / file | — | 75 776 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Affiliation Database` | archivo / file | — | 53 248 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/AutofillAiModelCache` | carpeta / folder | — | carpeta / folder (3 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/AutofillAiModelCache/LOCK` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/AutofillAiModelCache/LOG` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/AutofillAiModelCache/LOG.old` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/AutofillStrikeDatabase` | carpeta / folder | — | carpeta / folder (3 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/AutofillStrikeDatabase/LOCK` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/AutofillStrikeDatabase/LOG` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/AutofillStrikeDatabase/LOG.old` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/BookmarkMergedSurfaceOrdering` | archivo / file | — | 4 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/BudgetDatabase` | carpeta / folder | — | carpeta / folder (3 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/BudgetDatabase/LOCK` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/BudgetDatabase/LOG` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/BudgetDatabase/LOG.old` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache` | carpeta / folder | — | carpeta / folder (2 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data` | carpeta / folder | — | carpeta / folder (45 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/0534abb8afcef528_0` | archivo / file | — | 154 009 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/0d46a4df8ea3d779_0` | archivo / file | — | 1 452 668 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/10a3426a849e3298_0` | archivo / file | — | 156 420 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/165e3a02636e6eb3_0` | archivo / file | — | 55 085 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/21ebd010c526237f_0` | archivo / file | — | 9 784 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/225f98ed89b7c900_0` | archivo / file | — | 8 833 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/295d873d703f7b4e_0` | archivo / file | — | 12 928 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/3874a70916b82ec3_0` | archivo / file | — | 214 664 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/3a1865b322459345_0` | archivo / file | — | 42 172 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/3ad3e165021c726f_0` | archivo / file | — | 215 713 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/3c9edcd2b276b9cd_0` | archivo / file | — | 1 226 397 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/3e334aa8c5fbf113_0` | archivo / file | — | 671 910 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/4151ae2ff762a854_0` | archivo / file | — | 145 248 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/42e3d325839e8a12_0` | archivo / file | — | 168 066 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/44f7b91b29c47eef_0` | archivo / file | — | 219 947 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/4aae27cd75b83f9e_0` | archivo / file | — | 12 900 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/4ab6bb88b8458ee8_0` | archivo / file | — | 11 525 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/532397b41d3f5a17_0` | archivo / file | — | 6 359 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/5efd1b20adc484c6_0` | archivo / file | — | 11 002 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/6276401f1ba03fb7_0` | archivo / file | — | 15 129 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/735c501fb6c55afc_0` | archivo / file | — | 46 754 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/7551616f72e9623f_0` | archivo / file | — | 11 082 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/80ead5ed1f17826b_0` | archivo / file | — | 12 844 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/8b84d9cc85faa32e_0` | archivo / file | — | 35 853 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/8cceb152f1e7f617_0` | archivo / file | — | 395 717 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/93bdd8cc8576346a_0` | archivo / file | — | 86 856 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/9797aca325e8b75c_0` | archivo / file | — | 44 716 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/a3465bb429a981a2_0` | archivo / file | — | 30 764 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/a3509ef4dcf72b4a_0` | archivo / file | — | 8 956 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/a606f1700428cabc_0` | archivo / file | — | 38 548 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/b0dce67085c57612_0` | archivo / file | — | 955 589 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/b8c5aec7109e3661_0` | archivo / file | — | 160 257 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/bd14ffaca8109785_0` | archivo / file | — | 377 862 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/c2bd0d486300e73e_0` | archivo / file | — | 463 301 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/cf17146354e0ac37_0` | archivo / file | — | 10 998 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/d3e4b06676dff2a7_0` | archivo / file | — | 8 518 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/d4ed473104e5d1db_0` | archivo / file | — | 360 712 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/daa1e10c7231f795_0` | archivo / file | — | 584 636 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/e99f8d540942ad5f_0` | archivo / file | — | 87 356 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/f0f6e103b299a641_0` | archivo / file | — | 365 898 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/f4331f95da3bf6dd_0` | archivo / file | — | 181 079 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/f902d83d4befec64_0` | archivo / file | — | 440 207 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/index` | archivo / file | — | 24 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/index-dir` | carpeta / folder | — | carpeta / folder (1 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/index-dir/the-real-index` | archivo / file | — | 1 056 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/Cache_Data/todelete_3c9edcd2b276b9cd_0_1` | archivo / file | — | 655 080 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/No_Vary_Search` | carpeta / folder | — | carpeta / folder (2 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/No_Vary_Search/journal.baj` | archivo / file | — | 4 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cache/No_Vary_Search/snapshot.baf` | archivo / file | — | 20 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/ClientCertificates` | carpeta / folder | — | carpeta / folder (3 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/ClientCertificates/LOCK` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/ClientCertificates/LOG` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/ClientCertificates/LOG.old` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache` | carpeta / folder | — | carpeta / folder (2 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js` | carpeta / folder | — | carpeta / folder (52 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/0640b24501e2f022_0` | archivo / file | — | 83 376 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/0b674450fc8da378_0` | archivo / file | — | 1 122 672 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/0d0e3d5ae4dcce91_0` | archivo / file | — | 361 792 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/0d46c0e43b49149c_0` | archivo / file | — | 283 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/12a83c5e901419df_0` | archivo / file | — | 5 542 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/20791451c446b207_0` | archivo / file | — | 2 287 352 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/26f74181ee50b9fe_0` | archivo / file | — | 299 424 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/3468472199a99167_0` | archivo / file | — | 356 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/34d4697458fe74a7_0` | archivo / file | — | 3 976 688 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/35e251b108e722d9_0` | archivo / file | — | 602 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/3cf8d38a2b7ebf90_0` | archivo / file | — | 457 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/3d8d3b1622e63c6d_0` | archivo / file | — | 1 776 112 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/3e0d9b39a6e6a923_0` | archivo / file | — | 283 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/4286be091fbd2dfe_0` | archivo / file | — | 270 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/4952e9763f261abe_0` | archivo / file | — | 270 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/495e249cf37efc8d_0` | archivo / file | — | 6 518 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/51442ea9034a75d3_0` | archivo / file | — | 3 213 584 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/56ecd7a3df54e112_0` | archivo / file | — | 204 408 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/5df8d2c083abf562_0` | archivo / file | — | 602 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/64afa9e2da01a3df_0` | archivo / file | — | 90 464 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/6a39c46e58561dfd_0` | archivo / file | — | 562 624 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/6f4816904529ada9_0` | archivo / file | — | 402 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/75f0ac3e57f27f0b_0` | archivo / file | — | 602 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/8326e8ca6dc7bf09_0` | archivo / file | — | 281 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/8d555e1b2e151603_0` | archivo / file | — | 265 248 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/9079515fc615d7ed_0` | archivo / file | — | 316 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/915b50612b04f04a_0` | archivo / file | — | 305 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/93b1a17c9373bfc2_0` | archivo / file | — | 530 720 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/94bf6b7bd28cb583_0` | archivo / file | — | 270 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/9aa009ca6ca01f1b_0` | archivo / file | — | 1 665 248 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/9c5bef5d94b4b7d7_0` | archivo / file | — | 602 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/9c8e97dcb569bdd9_0` | archivo / file | — | 356 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/a5d2226cc4dc927c_0` | archivo / file | — | 307 360 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/a6ef2c19adb230af_0` | archivo / file | — | 263 680 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/b400bfe838ee845f_0` | archivo / file | — | 318 248 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/b7f4464b25bedda9_0` | archivo / file | — | 1 158 712 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/bda751f6bac7de81_0` | archivo / file | — | 459 792 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/c35db760beb6e2f6_0` | archivo / file | — | 356 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/c9a3b3e9533d22f1_0` | archivo / file | — | 602 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/ce3abd2532f62cd0_0` | archivo / file | — | 66 288 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/ce6654c2839e6c2a_0` | archivo / file | — | 602 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/d2601ca77bf06636_0` | archivo / file | — | 283 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/db28d04e436322ca_0` | archivo / file | — | 206 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/db4e188ea1702b99_0` | archivo / file | — | 511 648 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/df2be79a566d657b_0` | archivo / file | — | 589 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/e24a863e8d2c07c1_0` | archivo / file | — | 283 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/e35c65fc1d1f6d94_0` | archivo / file | — | 779 992 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/e5017c2f130a03d1_0` | archivo / file | — | 1 278 624 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/f4323e166659fe33_0` | archivo / file | — | 283 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/f5ae0107f3365fa8_0` | archivo / file | — | 602 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/index` | archivo / file | — | 24 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/index-dir` | carpeta / folder | — | carpeta / folder (1 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/js/index-dir/the-real-index` | archivo / file | — | 1 248 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/wasm` | carpeta / folder | — | carpeta / folder (2 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/wasm/index` | archivo / file | — | 24 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/wasm/index-dir` | carpeta / folder | — | carpeta / folder (1 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Code Cache/wasm/index-dir/the-real-index` | archivo / file | — | 48 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Cookies` | archivo / file | — | 20 480 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/DIPS` | archivo / file | — | 36 864 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/DawnGraphiteCache` | carpeta / folder | — | carpeta / folder (5 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/DawnGraphiteCache/data_0` | archivo / file | — | 8 192 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/DawnGraphiteCache/data_1` | archivo / file | — | 270 336 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/DawnGraphiteCache/data_2` | archivo / file | — | 8 192 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/DawnGraphiteCache/data_3` | archivo / file | — | 8 192 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/DawnGraphiteCache/index` | archivo / file | — | 262 512 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/DawnWebGPUCache` | carpeta / folder | — | carpeta / folder (5 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/DawnWebGPUCache/data_0` | archivo / file | — | 8 192 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/DawnWebGPUCache/data_1` | archivo / file | — | 270 336 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/DawnWebGPUCache/data_2` | archivo / file | — | 8 192 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/DawnWebGPUCache/data_3` | archivo / file | — | 8 192 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/DawnWebGPUCache/index` | archivo / file | — | 262 512 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension Rules` | carpeta / folder | — | carpeta / folder (5 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension Rules/000003.log` | archivo / file | — | 38 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension Rules/CURRENT` | archivo / file | — | 16 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension Rules/LOCK` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension Rules/LOG` | archivo / file | — | 377 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension Rules/MANIFEST-000001` | archivo / file | — | 41 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension Scripts` | carpeta / folder | — | carpeta / folder (5 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension Scripts/000003.log` | archivo / file | — | 19 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension Scripts/CURRENT` | archivo / file | — | 16 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension Scripts/LOCK` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension Scripts/LOG` | archivo / file | — | 381 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension Scripts/MANIFEST-000001` | archivo / file | — | 41 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension State` | carpeta / folder | — | carpeta / folder (6 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension State/000003.log` | archivo / file | — | 57 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension State/CURRENT` | archivo / file | — | 16 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension State/LOCK` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension State/LOG` | archivo / file | — | 418 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension State/LOG.old` | archivo / file | — | 418 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Extension State/MANIFEST-000001` | archivo / file | — | 41 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/Favicons` | archivo / file | — | 22 528 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/GPUCache` | carpeta / folder | — | carpeta / folder (5 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/GPUCache/data_0` | archivo / file | — | 45 056 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/GPUCache/data_1` | archivo / file | — | 270 336 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/GPUCache/data_2` | archivo / file | — | 1 056 768 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/GPUCache/data_3` | archivo / file | — | 8 192 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/GPUCache/index` | archivo / file | — | 262 512 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/History` | archivo / file | — | 212 992 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/IndexedDB` | carpeta / folder | — | carpeta / folder (1 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/IndexedDB/https_web.whatsapp.com_0.indexeddb.leveldb` | carpeta / folder | — | carpeta / folder (8 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/IndexedDB/https_web.whatsapp.com_0.indexeddb.leveldb/000030.ldb` | archivo / file | — | 33 289 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/IndexedDB/https_web.whatsapp.com_0.indexeddb.leveldb/000031.log` | archivo / file | — | 273 494 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/IndexedDB/https_web.whatsapp.com_0.indexeddb.leveldb/000033.ldb` | archivo / file | — | 33 492 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/IndexedDB/https_web.whatsapp.com_0.indexeddb.leveldb/CURRENT` | archivo / file | — | 16 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/IndexedDB/https_web.whatsapp.com_0.indexeddb.leveldb/LOCK` | archivo / file | — | 0 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/whatsapp/.browser_profile/Default/IndexedDB/https_web.whatsapp.com_0.indexeddb.leveldb/LOG` | archivo / file | — | 7 838 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |

| 2026-11-17 | `Auxiliares/herramientas` | carpeta / folder | — | carpeta / folder (23 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/descubrir_canales_telegram.py` | script / script | — | 6 017 B | 3 / 3 | Descubre canales de Telegram referentes al mercado cubano hasta 100. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/scraper_telegram_publico.py` | script / script | — | 6 740 B | 3 / 3 | Scraper de canales públicos de Telegram sin credenciales MTProto. | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/telegram_db.py` | script / script | — | 3 972 B | 3 / 3 | Base SQLite compartida para datos de Telegram (canales + anuncios). | Añadido / Added |
| 2026-11-17 | `Data/Revolico` | carpeta / folder | — | carpeta / folder (12 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/pipeline.sqlite` | base de datos / database | — | 104 624 128 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/progreso.md` | documento / document | — | 429 B | 2 / 2 | Progreso Revolico — 2026-11-17T18:09:58+00:00 | Actualizado / Updated |
| 2026-11-17 | `Data/integraciones/telegram` | carpeta / folder | — | carpeta / folder (5 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Data/integraciones/telegram/canales_referencia.jsonl` | archivo / file | — | 42 199 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/telegram/telegram.sqlite` | base de datos / database | — | 135 168 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 93 240 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `Auxiliares/herramientas` | carpeta / folder | — | carpeta / folder (21 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/aviso_revolico.py` | script / script | — | 4 560 B | 3 / 3 | Aviso de progreso del scraper de Revolico cada 10 minutos. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/scrape_revolico_pipeline.py` | script / script | — | 16 481 B | 3 / 3 | Pipeline de 3 etapas con colas persistentes para Revolico. | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/scraper_telegram_publico.py` | script / script | — | 6 556 B | 3 / 3 | Scraper de canales públicos de Telegram sin credenciales MTProto. | Añadido / Added |
| 2026-11-17 | `Data` | carpeta / folder | — | carpeta / folder (12 entradas) | 7 / 7 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico` | carpeta / folder | — | carpeta / folder (14 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/pipeline.sqlite` | base de datos / database | — | 18 001 920 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/progreso.md` | documento / document | — | 433 B | 2 / 2 | Progreso Revolico — 2026-11-17T17:09:56+00:00 | Actualizado / Updated |
| 2026-11-17 | `Data/integraciones` | carpeta / folder | — | carpeta / folder (1 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/telegram` | carpeta / folder | — | carpeta / folder (3 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/integraciones/telegram/anuncios.csv` | datos / data | — | 58 097 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/telegram/anuncios.jsonl` | archivo / file | — | 66 888 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/integraciones/telegram/estado.json` | datos / data | — | 186 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 89 696 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `Auxiliares/herramientas/scrape_revolico_pipeline.py` | script / script | — | 16 200 B | 3 / 3 | Pipeline de 3 etapas con colas persistentes para Revolico. | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico` | carpeta / folder | — | carpeta / folder (10 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/partes` | carpeta / folder | — | carpeta / folder (48 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/pipeline.sqlite` | base de datos / database | — | 15 765 504 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/resumen.md` | documento / document | — | 412 B | 2 / 2 | Revolico — base de datos completa de la categoría Vehículos | Actualizado / Updated |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 86 136 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `Auxiliares/herramientas/actualizar_revolico.py` | script / script | — | 6 532 B | 3 / 3 | Actualización incremental de la BD de Revolico y subida por partes a Git. | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico` | carpeta / folder | — | carpeta / folder (11 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/partes` | carpeta / folder | — | carpeta / folder (47 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/Revolico/pipeline.sqlite` | base de datos / database | — | 10 625 024 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/resumen.md` | documento / document | — | 412 B | 2 / 2 | Revolico — base de datos completa de la categoría Vehículos | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt` | carpeta / folder | — | carpeta / folder (28 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part001` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part002` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part003` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part004` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part005` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part006` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part007` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part008` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part009` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part010` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part011` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part012` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part013` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part014` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part015` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part016` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part017` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part018` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part019` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part020` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part021` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part022` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part023` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part024` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part025` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part026` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part027` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/revolico_parts_9qprzigt/revolico.sqlite.part028` | archivo / file | — | 16 777 216 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 77 264 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `Auxiliares/herramientas/analisis_mercado.py` | script / script | — | 13 794 B | 3 / 3 | Análisis descriptivo inicial del mercado de autos usados en La Habana. | Actualizado / Updated |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 76 824 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 75 373 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `Auxiliares/herramientas` | carpeta / folder | — | carpeta / folder (19 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/analisis_mercado.py` | script / script | — | 12 282 B | 3 / 3 | Análisis descriptivo inicial del mercado de autos usados en La Habana. | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/graficos_mercado.py` | script / script | — | 9 312 B | 3 / 3 | Funciones para generar todas las gráficas del análisis de mercado. | Añadido / Added |
| 2026-11-17 | `Data/analisis` | carpeta / folder | — | carpeta / folder (11 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Data/analisis/cobertura.csv` | datos / data | — | 174 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/analisis/dashboard.html` | HTML / HTML | — | 16 086 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/analisis/graficos` | carpeta / folder | — | carpeta / folder (9 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/analisis/graficos/01_histograma_precios.png` | archivo / file | — | 59 758 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/graficos/02_boxplot_marcas.png` | archivo / file | — | 64 227 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/graficos/03_barras_municipios.png` | archivo / file | — | 68 628 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/graficos/04_precios_por_anio.png` | archivo / file | — | 90 044 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/graficos/05_serie_precio_vs_tasa.png` | archivo / file | — | 99 874 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/graficos/06_variaciones_tasa_precio.png` | archivo / file | — | 94 796 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/graficos/07_outliers.png` | archivo / file | — | 53 770 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/graficos/08_cobertura.png` | archivo / file | — | 36 886 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/graficos/dashboard_interactivo.html` | HTML / HTML | — | 24 245 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/informe_descriptivo.md` | documento / document | — | 9 592 B | 2 / 2 | Análisis descriptivo inicial — mercado de autos usados en La Habana | Actualizado / Updated |
| 2026-11-17 | `Data/analisis/outliers.csv` | datos / data | — | 768 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/analisis/precios_por_anio.csv` | datos / data | — | 879 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/analisis/precios_por_marca.csv` | datos / data | — | 803 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/analisis/precios_por_municipio.csv` | datos / data | — | 741 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/analisis/resumen_general.csv` | datos / data | — | 102 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Data/analisis/serie_precio_vs_tasa.csv` | datos / data | — | 544 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/serie_precio_vs_tasa_mensual.csv` | datos / data | — | 152 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 68 735 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `Auxiliares/herramientas` | carpeta / folder | — | carpeta / folder (18 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/analisis_mercado.py` | script / script | — | 8 816 B | 3 / 3 | Análisis descriptivo inicial del mercado de autos usados en La Habana. | Añadido / Added |
| 2026-11-17 | `Data` | carpeta / folder | — | carpeta / folder (11 entradas) | 7 / 7 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Data/analisis` | carpeta / folder | — | carpeta / folder (8 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/analisis/cobertura.csv` | datos / data | — | 174 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/dashboard.html` | HTML / HTML | — | 14 753 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/informe_descriptivo.md` | documento / document | — | 6 498 B | 2 / 2 | Análisis descriptivo inicial — mercado de autos usados en La Habana | Añadido / Added |
| 2026-11-17 | `Data/analisis/outliers.csv` | datos / data | — | 768 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/precios_por_anio.csv` | datos / data | — | 728 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/precios_por_marca.csv` | datos / data | — | 803 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/precios_por_municipio.csv` | datos / data | — | 741 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/analisis/resumen_general.csv` | datos / data | — | 102 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 65 081 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 63 764 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |
| 2026-11-17 | `README.md` | documento / document | — | 16 116 B | 9 / 9 | AutoDecide Habana / AutoDecide Habana | Actualizado / Updated |

| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 62 338 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 59 613 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 56 770 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 53 268 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `Auxiliares/herramientas` | carpeta / folder | — | carpeta / folder (17 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/scrape_revolico_pipeline.py` | script / script | — | 14 401 B | 3 / 3 | Pipeline de 3 etapas con colas persistentes para Revolico. | Añadido / Added |
| 2026-11-17 | `Data/Revolico` | carpeta / folder | — | carpeta / folder (7 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Data/Revolico/pipeline.sqlite` | base de datos / database | — | 10 625 024 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Data/Revolico/snapshots` | carpeta / folder | — | carpeta / folder (1 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Data/Revolico/snapshots/ultimo.json` | datos / data | — | 101 344 B | 2 / 2 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 48 537 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `Auxiliares/herramientas/limpiar_revolico.py` | script / script | — | 7 655 B | 3 / 3 | Limpieza de la BD de Revolico: solo vehículos de 4+ ruedas con datos útiles. | Actualizado / Updated |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 46 466 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 45 634 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `Data/Revolico` | carpeta / folder | — | carpeta / folder (5 entradas) | 2 / 2 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 44 625 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `Auxiliares/herramientas/sincronizar_github.py` | script / script | — | 2 193 B | 3 / 3 | Sincroniza con GitHub SOLO los archivos del proyecto ya definidos. | Actualizado / Updated |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 43 591 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `Auxiliares/herramientas` | carpeta / folder | — | carpeta / folder (16 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/actualizar_revolico.py` | script / script | — | 6 406 B | 3 / 3 | Actualización incremental de la BD de Revolico y subida por partes a Git. | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/limpiar_revolico.py` | script / script | — | 7 610 B | 3 / 3 | Limpieza de la BD de Revolico: solo vehículos de 4+ ruedas con datos útiles. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/sincronizar_github.py` | script / script | — | 2 038 B | 3 / 3 | Sincroniza con GitHub SOLO los archivos del proyecto ya definidos. | Añadido / Added |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 42 639 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 42 490 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 42 341 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `Auxiliares/herramientas` | carpeta / folder | — | carpeta / folder (14 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/integraciones` | carpeta / folder | — | carpeta / folder (7 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/README.md` | documento / document | — | 2 827 B | 3 / 3 | Integraciones / Integrations | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook` | carpeta / folder | — | carpeta / folder (8 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_gql_scraper` | carpeta / folder | — | carpeta / folder (10 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_gql_scraper/__init__.py` | script / script | — | 1 316 B | 3 / 3 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_gql_scraper/exceptions.py` | script / script | — | 3 042 B | 3 / 3 | Base for all errors raised by this library. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_gql_scraper/facebookConsolidater.py` | script / script | — | 4 012 B | 3 / 3 | Recursively merge dictionaries, extend lists. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_gql_scraper/facebookGraphql.py` | script / script | — | 45 585 B | 3 / 3 | Facebook request context. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_gql_scraper/facebookNoiseRemoval.py` | script / script | — | 5 090 B | 3 / 3 | Recursively remove UI/React/Relay garbage from data | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_gql_scraper/facebookOperationDiscovery.py` | script / script | — | 22 550 B | 3 / 3 | var __registry = {}; | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_gql_scraper/parserModels.py` | script / script | — | 14 357 B | 3 / 3 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_gql_scraper/structures.py` | script / script | — | 122 555 B | 3 / 3 | Facebook photo. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_gql_scraper/unifiedFacebookParser.py` | script / script | — | 72 729 B | 3 / 3 | Wrap a ParserMedia in a ParserMediaPost. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_page_scraper` | carpeta / folder | — | carpeta / folder (7 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_page_scraper/__init__.py` | script / script | — | 314 B | 3 / 3 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_page_scraper/driver_initialization.py` | script / script | — | 3 798 B | 3 / 3 | adds capabilities to the driver | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_page_scraper/driver_utilities.py` | script / script | — | 7 902 B | 3 / 3 | expects driver's instance, closes the driver | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_page_scraper/element_finder.py` | script / script | — | 22 200 B | 3 / 3 | Holds the collections of methods that finds element of the facebook's posts using selenium's webdriver's methods | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_page_scraper/scraper.py` | script / script | — | 17 678 B | 3 / 3 | changes the class member __driver value to driver on call | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_page_scraper/scraping_utilities.py` | script / script | — | 5 450 B | 3 / 3 | expects string and returns numbers from them as integer type, | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_scraper` | carpeta / folder | — | carpeta / folder (10 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_scraper/__init__.py` | script / script | — | 20 243 B | 3 / 3 | Get a Facebook user's profile information | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_scraper/__main__.py` | script / script | — | 6 624 B | 3 / 3 | facebook-scraper entry point when used as a script | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_scraper/constants.py` | script / script | — | 285 B | 3 / 3 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_scraper/exceptions.py` | script / script | — | 636 B | 3 / 3 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_scraper/extractors.py` | script / script | — | 62 499 B | 3 / 3 | Class for Extracting fields from a FacebookPost | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_scraper/facebook_scraper.py` | script / script | — | 51 259 B | 3 / 3 | Class for creating FacebookScraper Iterators | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_scraper/fb_types.py` | script / script | — | 340 B | 3 / 3 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_scraper/page_iterators.py` | script / script | — | 10 774 B | 3 / 3 | Class for Parsing a single page on a Page | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/facebook_scraper/utils.py` | script / script | — | 14 155 B | 3 / 3 | Strip invalid XML characters that `lxml` cannot parse. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/marketplace_gui.py` | script / script | — | 1 982 B | 3 / 3 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/marketplace_scraper.py` | script / script | — | 9 640 B | 3 / 3 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper` | carpeta / folder | — | carpeta / folder (17 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/__init__.py` | script / script | — | 637 B | 3 / 3 | Facebook scraper package. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/auth.py` | script / script | — | 1 263 B | 3 / 3 | Authentication helpers: cookie parsing and cURL parsing. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/comments.py` | script / script | — | 14 175 B | 3 / 3 | Comment and reply scraping with full metadata (author, IDs, reactions). | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/config.py` | script / script | — | 2 694 B | 3 / 3 | Central runtime configuration shared by all scraper modules. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/extractors.py` | script / script | — | 8 202 B | 3 / 3 | Field extractors for Facebook Story nodes (counts, names, media checks). | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/group_posts.py` | script / script | — | 7 869 B | 3 / 3 | Group post scraping (posts + media, batched via callback). | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/http.py` | script / script | — | 4 202 B | 3 / 3 | HTTP helpers: retry logic with proxy rotation and Facebook response parsing. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/logging_utils.py` | script / script | — | 726 B | 3 / 3 | Thread-aware logging for scrapers. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/media.py` | script / script | — | 7 634 B | 3 / 3 | Media extraction and image downloading (with optional album traversal). | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/page_posts.py` | script / script | — | 11 528 B | 3 / 3 | Page/profile post scraping (posts + media, batched via callback). | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/proxy_utils.py` | script / script | — | 4 048 B | 3 / 3 | Lazy import to avoid a circular dependency (config imports this module). | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/resolvers.py` | script / script | — | 3 685 B | 3 / 3 | Resolve Facebook URLs into the IDs the scrapers need. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/run.py` | script / script | — | 1 668 B | 3 / 3 | Facebook Scraper — Flask web GUI. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/single_post.py` | script / script | — | 1 847 B | 3 / 3 | Single post scraping: comments + optional album image download. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/storage.py` | script / script | — | 9 826 B | 3 / 3 | Storage layer: everything under the project's data/ directory. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/post_comment_scraper/tasks.py` | script / script | — | 5 973 B | 3 / 3 | High-level scrape operations used by the web app (and usable from CLI). | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/facebook/selenium_car_scraper.py` | script / script | — | 28 921 B | 3 / 3 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/fuentes_cubanas` | carpeta / folder | — | carpeta / folder (8 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/fuentes_cubanas/scrape_autocubana.py` | script / script | — | 22 277 B | 3 / 3 | Script de Web Scraping para extraer el catálogo de vehículos en venta | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/fuentes_cubanas/scraper_cubamerica.py` | script / script | — | 12 187 B | 3 / 3 | Scraper de CubAmerica (envioscubamerica.com). | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/fuentes_cubanas/scraper_itencel.py` | script / script | — | 15 220 B | 3 / 3 | Scraper de iTENCEL (itencel.com). | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/fuentes_cubanas/scraper_revolico.py` | script / script | — | 26 644 B | 3 / 3 | scraper_revolico.py | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/fuentes_cubanas/scraper_telegram.py` | script / script | — | 3 344 B | 3 / 3 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/fuentes_cubanas/scraper_vedca.py` | script / script | — | 12 563 B | 3 / 3 | Scraper de la tienda VEDCA dentro de Islagrande. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/fuentes_cubanas/scraping_dongfeng.py` | script / script | — | 16 155 B | 3 / 3 | Scraping del catalogo de vehiculos de https://dongfengqba.com/ | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/requirements-integraciones.txt` | texto / text | — | 258 B | 3 / 3 | Dependencias de los scripts integrados (instalar solo las que se vayan a usar) | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/spinny` | carpeta / folder | — | carpeta / folder (10 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/spinny/captcha_solver.py` | script / script | — | 33 515 B | 3 / 3 | captcha_solver.py | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/spinny/diff_runs.py` | script / script | — | 19 098 B | 3 / 3 | diff_runs.py | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/spinny/env_config.py` | script / script | — | 8 828 B | 3 / 3 | env_config.py | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/spinny/fingerprint_client.py` | script / script | — | 18 748 B | 3 / 3 | fingerprint_client.py | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/spinny/output_writer.py` | script / script | — | 38 158 B | 3 / 3 | output_writer.py | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/spinny/page_flow.py` | script / script | — | 38 393 B | 3 / 3 | page_flow.py | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/spinny/playwright_scraper.py` | script / script | — | 89 998 B | 3 / 3 | spinny-scraper — Playwright edition (primary engine) | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/spinny/product_parser.py` | script / script | — | 90 678 B | 3 / 3 | product_parser.py | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/spinny/proxy_pool.py` | script / script | — | 13 938 B | 3 / 3 | proxy_pool.py | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/telegram` | carpeta / folder | — | carpeta / folder (1 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/telegram/telegraphite` | carpeta / folder | — | carpeta / folder (10 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/telegram/telegraphite/__init__.py` | script / script | — | 105 B | 3 / 3 | TeleGraphite - A tool to fetch and save posts from public Telegram channels. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/telegram/telegraphite/cli.py` | script / script | — | 11 392 B | 3 / 3 | Command-line interface for TeleGraphite. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/telegram/telegraphite/client.py` | script / script | — | 3 090 B | 3 / 3 | Client module for TeleGraphite. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/telegram/telegraphite/config.py` | script / script | — | 4 552 B | 3 / 3 | Configuration module for TeleGraphite. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/telegram/telegraphite/contact_extractor.py` | script / script | — | 735 B | 3 / 3 | Contact Extractor module for TeleGraphite. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/telegram/telegraphite/errors.py` | script / script | — | 2 170 B | 3 / 3 | Error handling module for TeleGraphite. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/telegram/telegraphite/fetcher.py` | script / script | — | 9 093 B | 3 / 3 | Fetcher module for TeleGraphite. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/telegram/telegraphite/logging_config.py` | script / script | — | 4 598 B | 3 / 3 | Logging configuration module for TeleGraphite. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/telegram/telegraphite/store.py` | script / script | — | 11 976 B | 3 / 3 | Store module for TeleGraphite. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/whatsapp` | carpeta / folder | — | carpeta / folder (4 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/whatsapp/waha_client.py` | script / script | — | 4 212 B | 3 / 3 | Cliente Python para WAHA (WhatsApp HTTP API) orientado a AutoDecide Habana. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/whatsapp/whatsapp_mcp_reader.py` | script / script | — | 24 712 B | 3 / 3 | Determine if chat is a group based on JID pattern. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/integraciones/whatsapp/whatsapp_web_example.js` | archivo / file | — | 30 417 B | 3 / 3 | Añadido al proyecto; pendiente de descripción / Added; description pending | Añadido / Added |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 22 664 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |

| 2026-11-17 | `.gitignore` | archivo / file | — | 1 107 B | 9 / 9 | Añadido al proyecto; pendiente de descripción / Added; description pending | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas` | carpeta / folder | — | carpeta / folder (13 entradas) | 3 / 3 | Carpeta añadida al proyecto / Folder added to the project | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/actualizar_informe.py` | script / script | — | 14 283 B | 3 / 3 | Registra altas nuevas del proyecto en INFORME_TECNICO.md y regenera el PDF. | Actualizado / Updated |
| 2026-11-17 | `Auxiliares/herramientas/actualizar_revolico.py` | script / script | — | 6 408 B | 3 / 3 | Actualización incremental de la BD de Revolico y subida por partes a Git. | Añadido / Added |
| 2026-11-17 | `Auxiliares/herramientas/reconstruir_revolico.py` | script / script | — | 1 812 B | 3 / 3 | Reconstruye revolico.sqlite a partir de las partes versionadas en Git. | Añadido / Added |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | 21 391 B | 9 / 9 | Informe técnico / Technical report | Actualizado / Updated |
| 2026-11-17 | `README.md` | documento / document | — | 15 804 B | 9 / 9 | AutoDecide Habana / AutoDecide Habana | Actualizado / Updated |

| 2026-11-17 | `README.md` | documento / document | — | 7,6 KB | 9 | Nombre del proyecto, estado, fases y marco para GitHub / Project name, status, phases and GitHub framework | Creado / Created |
| 2026-11-17 | `INFORME_TECNICO.md` | documento / document | — | — | 9 | Informe técnico redefinido en 9 fases, bilingüe y con marco legal / Technical report redefined into 9 phases, bilingual, with legal framework | Actualizado / Updated |
| 2026-11-17 | `INFORME_TECNICO.pdf` | PDF / PDF | generado desde MD / generated from MD | — | 9 | Entregable en PDF / PDF deliverable | Generado / Generated |
| 2026-11-17 | `Auxiliares/herramientas/actualizar_informe.py` | script / script | — | — | 3 | Registro automático de altas y regeneración del PDF / Automatic change log and PDF regeneration | Creado / Created |
| 2026-11-17 | `.gitignore` | configuración / config | — | — | 3 | Exclusiones para GitHub / GitHub exclusions | Creado / Created |

## 14. Sincronización automática de Revolico / Automatic Revolico sync

La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**. Cada 10 minutos un timer de systemd ejecuta `Auxiliares/herramientas/actualizar_revolico.py`: corre el scraper incremental, divide la BD en partes de 16 MiB dentro de `Data/Revolico/partes/`, sube solo las partes que cambiaron y actualiza esta fila. Para recuperar el archivo completo se usa `Auxiliares/herramientas/reconstruir_revolico.py`, que verifica el hash.

The database is **not versioned as a single file**. Every 10 minutes a systemd timer runs `actualizar_revolico.py`: it runs the incremental scraper, splits the DB into 16 MiB chunks under `Data/Revolico/partes/`, uploads only changed chunks and updates this row. Use `reconstruir_revolico.py` to rebuild the full file and verify its hash.

| Última ejecución / Last run | Tamaño / Size | Partes / Chunks | SHA-256 (inicio) | Reconstrucción / Rebuild |
|---|---|---|---|---|
<!-- SYNC_REVOLICO -->
| 2026-11-17T15:47:42+00:00 | 795373568 B | 48 partes de 16 MiB | `dadd2bffba615d8a…` | Reconstruir con `reconstruir_revolico.py` / Rebuild with `reconstruir_revolico.py` |

## 15. Eficiencia de Telegram, WhatsApp y Facebook / Efficiency of Telegram, WhatsApp and Facebook

**ES.** Para obtener más datos del mercado habanero, la ruta más eficiente es Telegram MTProto (`telethon`, ya integrado): sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`. Le sigue Facebook GQL (`facebook_gql_scraper`): llamadas GraphQL con sesión autenticada y normalización con `price-parser`/`iso4217parse`, más rápido que Selenium. Para grupos de WhatsApp no existe API pública personal; la opción operativa es un servidor WAHA auto-hospedado y su REST (`/api/sessions`, `/api/{session}/chats`, `/api/{session}/chats/{chatId}/messages`) con deduplicación por id, que es lo que hace `whatsapp/waha_client.py`. Playwright/Selenium quedan como último recurso para páginas JS. La salida de las tres fuentes debe convergir en un esquema común (`fuente`, `id`, `chat/página`, `timestamp`, `texto`, `precio`, `moneda`, `url`) con dedup por `hash(fuente,id)` y sin datos personales.

**EN.** For more Havana market data, the most efficient route is Telegram MTProto (`telethon`, already integrated): no browser, incremental cursor, server-side search and `FloodWaitError` handling. Next is Facebook GQL: authenticated GraphQL calls with `price-parser`/`iso4217parse`, faster than Selenium. WhatsApp has no public personal API; the practical option is self-hosted WAHA REST with id deduplication, implemented in `waha_client.py`. Playwright/Selenium remain a last resort. All three should converge into a common schema with source-based deduplication and no personal data.

**Nota / Note (17/11/2026):** se detuvo manualmente `revolico-scrape.timer` y su servicio a petición del usuario. El scraper había ampliado la BD de 3.682 a **6.332 anuncios** (520,6 MB) antes de detenerse; no se generaron partes (`estado.json` ausente) porque se detuvo antes de la fase de división. `revolico-git.timer` sigue activo para no perder cambios ya versionados. / The scrape timer and its service were stopped manually at the user's request. The scraper had grown the DB from 3,682 to **6,332 ads** (520.6 MB) before stopping; no chunks were produced because it was stopped before the split phase. `revolico-git.timer` remains active so versioned changes are not lost.

**Limpieza ejecutada / Cleaning run (17/11/2026):** sobre los 6.332 anuncios actuales, `limpiar_revolico.py` conservó **304 autos** en la tabla `autos` y registró **6.028 exclusiones** en `revision` (5.983 no vehículo 4+ ruedas, 45 sin datos necesarios, 0 páginas sin datos suficientes). No se borraron filas originales: `anuncios` conserva las columnas de auditoría `es_auto`, `motivo_exclusion`, `pagina_revisada` y `datos_necesarios`. Se añadieron `microbús/guagua/ómnibus/bus` a los patrones de inclusión. / On the current 6,332 ads, 304 cars were kept and 6,028 exclusions logged; no original rows were deleted and microbus terms were added to the inclusion patterns.

**Permanencia / Retention:** las Condiciones de Uso de Revolico (23/09/2026) no fijan un plazo de caducidad de los anuncios. Empíricamente, un anuncio con `updated_on_by_user=2024-12-17` seguía en HTTP 200 el 17/11/2026 (~699 días), por lo que no puede asumirse una expiración de 30 días. El 99,3 % de los anuncios tiene `updated_on_by_user` en los últimos 7 días (mediana 1 día en los 189 autos), lo que indica renovación frecuente por parte del vendedor. Revolico's Terms (23/09/2026) set no fixed expiry; an ad last updated 2024-12-17 was still HTTP 200 on 2026-11-17 (~699 days), while 99.3% of ads were updated within 7 days, suggesting frequent seller renewal.

## 16. Pipeline de colas / Queue-based pipeline (18/11/2026)

`Auxiliares/herramientas/scrape_revolico_pipeline.py` separa el trabajo en tres etapas simultáneas con colas persistentes en `Data/Revolico/pipeline.sqlite`:

1. **Descubrimiento**: recorre página por página y guarda enlace, `ad_id` y firma de listado en `url_queue`.
2. **Descarga**: workers toman URLs pendientes y guardan **todos** los campos parseados (`raw_html`, `apollo_full`, `meta_json`, imágenes, teléfonos, etc.) en `download_queue`.
3. **Procesamiento**: workers clasifican cada anuncio con `limpiar_revolico.clasificar` y escriben la decisión en `process_queue`. Cada **25 anuncios procesados** (aceptados o rechazados) se hace un commit por lotes en `anuncios`/`autos`/`imagenes`/`telefonos` o en `revision`.

Se adaptó el patrón `output_writer.py` + `diff_runs.py` de `spinny-scraper` como snapshot `Data/Revolico/snapshots/ultimo.json` (`{id: firma}`). El campo `updatedOnToOrder` del listado resultó ser un marcador de ranking y no de edición, así que el salto de descarga queda desactivado por defecto (`--skip-unchanged`); el snapshot se conserva como registro de diferencias.

Prueba con 1 página: **119 enlaces** descubiertos y procesados, 7 lotes de 25, BD principal de 6.332 a **6.334 anuncios** y de 304 a **317 autos**. Todo queda auditado; no se descarta información.

**EN.** The new pipeline runs three concurrent stages with persistent queues, committing every 25 processed ads. The spinny diff pattern was adapted as a snapshot, but skipping downloads is disabled by default because the listing timestamp is a ranking signal, not an edit signal. Test run: 119 links, 6,334 ads and 317 cars in the main DB.

## 17. Guía de análisis de mercado / Market-analysis guide (18/11/2026)

Fuentes académicas y repositorios revisados para definir los requerimientos del análisis (Fases 7-8):

| Fuente | Aporte metodológico | Requerimiento para AutoDecide |
|---|---|---|
| `Hombros/01_PDFs/Análisis del mercado de vehículos usados y su comercialización en el__73e1773e.pdf` (PUCE) | Asimetría de información (Akerlof); clasificación de calidad por antigüedad (≤5 años alta, >5 años con defectos); encuesta a 130 comerciantes; medición de costos ocultos y margen de reventa | Capturar año/antigüedad, estado, costos de reacondicionamiento y margen; comparar precio por calidad |
| `Hombros/RESUMEN_NUEVAS_BUSQUEDAS.md` (variaciones de precio, 2 trabajos útiles) | Variación de precios en seminuevos | Serie temporal de precio y depreciación por año |
| `Hombros/01_PDFs/PDF Informe de competencia del mercado automotriz ...` / `Mercado automotriz chileno: un análisis empírico` | Estructura y concentración del mercado | Cuota por marca/segmento, comparables |
| `Hombros/02_HTML/Inteligencia De Negocios Aplicada Al Sector Automovilístico__5e5a32a5.html` | ETL + dashboard | Pipeline, métricas y visualización |
| Informes ANFAC / EY / INEGI / BBVA / COIIM en `Hombros/01_PDFs/` | Indicadores macro: matriculaciones, parque, electrificación, combustible | Contexto: tipo de combustible, años, normativa |
| `Copias/AutosxCuba/code/{unir_todo_final,modelo_predictivo,generar_graficos}.py` | Unificación multi-fuente, predicción de precios, gráficos | Unificar fuentes, modelo de precio, visualizaciones |
| `Copias/guani-saimc/src/saimc/*` | Precio por producto/provincia con trazabilidad | Procedencia y geografía (provincia/municipio) |
| `Copias/taso-api/src/*` | Tasas de cambio múltiples | Normalizar CUP/USD/MLC/EUR |
| `Auxiliares/Repositorios Referencias/IDSE-DATA-SCIENCE-PROJECT-/{car_features,predict,server}.py` | Feature engineering, XGBoost, SHAP, Flask | Explicabilidad de la recomendación |
| `Auxiliares/Repositorios Referencias/used-cars-price-prediction/app.py` | Producto interactivo con Gradio | Interfaz de "preocupaciones del usuario" |
| `Auxiliares/Repositorios Referencias/Iran-Car-Market-Intelligence/src/icmi/analytics/*` | Comparables, estadística y dashboard | Metodología de comparables y rentabilidad |
| `Auxiliares/Repositorios Referencias/{uk-automotive-transition,vahan-india,nz-vehicle-market-tracker,zimbabwe-used-vehicle-market-analysis}` | Series por período, EDA, viabilidad | Tendencias y segmentación |

**Requerimientos derivados:** (1) esquema común con precio+moneda normalizada, año/km/combustible/transmisión/marca/modelo/provincia/tipo de vendedor y procedencia; (2) clasificación de calidad y estimación de costos ocultos; (3) comparables por marca-modelo-año-provincia; (4) modelo de rentabilidad = precio de reventa esperado − precio de compra − costos − impuestos; (5) serie temporal con snapshots; (6) dashboard de mercado; (7) validación, dedup y sin datos personales. La ponderación de preferencias del usuario y el producto interactivo quedan para la especialización futura.

**EN.** Academic sources and integrated repositories were reviewed to define the Fase 7-8 requirements: common schema with normalized currency, quality classification and hidden costs, comparables, profitability model, user-preference weighting, time series, interactive product, and validation/provenance.

## 18. Auditoría de procedencia / Source audit (18/11/2026)

| Fuente | Naturaleza | Verificación | Uso en el análisis |
|---|---|---|---|
| DfT / DVLA (UK), `gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files` | **Oficial gubernamental** | Verificado en vivo: publicado por Department for Transport + DVLA, actualizado 23/09/2026, Open Government Licence | Repos `uk-automotive-transition`: erste Registrierungen por marca/combustible/trimestre |
| VAHAN (India), declarado por `vahan-india-automotive-market-2025` | **Oficial gubernamental** (MoRTH) | No accesible desde este entorno (error de transporte); el repo documenta 12 exportaciones mensuales 2025 y manifiesto de verificacion | Registros por fabricante/combustible |
| BCC (Banco Central de Cuba) | **Oficial gubernamental** | No accesible en vivo desde este entorno; citado en `Data/investigacion-mercado-automotor-cuba.md` y Resolución 102/2026 | Tasa oficial |
| Gaceta Oficial / MINCEX / MITRANS / MININT | **Oficial gubernamental** | Verificado en investigacion previa (Gaceta 65/2026, Decreto 163/2026) | Marco legal y normativo |
| ANFAC (España) | **Gremial** (asociación de fabricantes) | Verificado en vivo: anfac.com, cifras de matriculaciones y parque, informe anual | Contexto sectorial, no precio de Cuba |
| AEADE (Ecuador) | **Gremial** | Verificado en vivo: aeade.net, anuarios y boletines de ventas | Fuente declarada por el estudio PUCE de vehículos usados |
| INEGI (México), EY, BBVA Research, COIIM, OICA | **Oficial / consultoría / gremio internacional** | Citados en los informes descargados en `Hombros/01_PDFs/`; no todos re-verificados en vivo | Contexto macro y tendencias |
| Universidades (PUCE, UPS, UPV, UChile, UNAL, etc.) | **Académico** | Repositorios institucionales (.edu / repositorios oficiales) en `Hombros/indice.md` | Metodología, encuestas, EDA |
| CarDekho (Kaggle), Spinny, OLX, Revolico, Autocubana, Dongfeng | **Marketplace / anuncios** | No son estadísticas oficiales; son precios **pedidos**, no transaccionados | Señal de precios; requiere dedup, verificación y sesgo declarado |
| WhatsApp / Telegram / Facebook groups | **Redes sociales** | No verificables como fuente estadística; requieren consentimiento y sin datos personales | Precios reportados por usuarios |
| elTOQUE, QvaPay, Binance (en `taso-api`) | **No oficial** (medios/P2P/crypto) | No verificados en vivo; elTOQUE es medio independiente, no BCC | Tasa informal/P2P, separada de la oficial |
| UCI Automobile, datasets sintéticos (Zimbabwe/Nigeria) | **Académico/sintético** | Declarado en los propios README | Solo referencia metodológica, nunca precio real de Cuba |

**Conclusión:** las fuentes oficiales y gremiales sirven de **contexto y validación**; los anuncios y redes son la **señal de precio** pero no sustituyen estadísticas oficiales. El análisis debe etiquetar cada métrica con su procedencia y nivel de confianza, y no mezclar tasas oficiales e informales ni precios anunciados con precios de transacción.

**EN.** Official/governmental and industry sources are used for context and validation; marketplaces and social platforms provide advertised-price signals only. Every metric must carry provenance and confidence level, keeping official vs informal rates and asking vs transaction prices separate.

## 19. Marco de análisis de mercado y su adaptación / Market-analysis framework and adaptation (18/11/2026)

### Marco general (8 pasos, derivado de los trabajos revisados)

1. **Pregunta y decisión**: qué se decide, para quién y en qué horizonte (PUCE: funcionamiento del mercado de usados; Chile: variables que influyen en tener automóvil).
2. **Delimitación**: geografía, producto, canal y unidad de análisis.
3. **Marco teórico y normativo**: asimetría de información (Akerlof), selección adversa, riesgo moral, regulación vigente.
4. **Diseño de datos**: fuentes primarias (encuestas/entrevistas) y secundarias (registros, anuncios), esquema común, muestreo y sesgos.
5. **Recolección y curación**: captura, deduplicación, validación y trazabilidad (ETL + BI).
6. **Descriptivo y segmentación**: distribución de precios, participación por marca/segmento, series temporales.
7. **Analítico**: comparables, depreciación, costos ocultos, margen de reventa, modelos explicables.
8. **Entrega y monitoreo**: dashboard de mercado, limitaciones y actualización periódica.

### Adaptación a Cuba / La Habana

- **Delimitación**: La Habana; autos de 4+ ruedas; canales formal e informal; precios anunciados en CUP/USD/MLC/EUR **sin mezclar**.
- **Fuentes**: Revolico (BD propia, 6.334 anuncios / 317 autos), concesionarios (Autocubana, Dongfeng, BDC One…), Gaceta/Decreto 163/2026, BCC (oficial) y elTOQUE (informal), salarios de la Resolución 14, y señales de Telegram/WhatsApp/Facebook sin datos personales.
- **Variables**: precio+moneda, año/antigüedad, km, combustible, transmisión, marca/modelo, provincia/municipio, tipo de vendedor, imágenes, estado y palabras de defecto en el texto (para estimar costos ocultos).
- **Métodos adaptados**: descriptivo por marca-modelo-año; clases de calidad (≤5 años alta, >5 años con defectos, según PUCE); bandera de asimetría por ocultamiento; comparables por modelo ±2 años y municipio; rentabilidad = reventa esperada − compra − reacondicionamiento − impuestos (Decreto 163/2026); asequibilidad = precio / salario; series con snapshots.
- **Entregables**: tabla `autos` + `revision`, dashboard de mercado, informe técnico. El recomendador interactivo se difiere a la especialización futura.
- **Límites**: precios pedidos no transaccionados, sesgo de supervivencia de anuncios, sin datos personales, vigencia normativa a verificar.

**EN.** An eight-step generic framework was adapted to Havana: scope, regulatory/theoretical frame, data design, curation, descriptive analysis, comparables and profitability, affordability, and an explainable interactive recommender, with explicit provenance and limitations.

## 20. Marco analítico detallado / Detailed analytical framework (18/11/2026)

**ES.** El marco operativo completo consta de nueve bloques:

1. **Objetivo del análisis**: caracterizar el mercado de autos usados en La Habana (estructura, precios, oferta, segmentos, tendencias, asequibilidad y rentabilidad), sin recomendar aún una compra concreta.
2. **Alcance**: La Habana, autos 4+ ruedas, canales formal e informal, precios anunciados separados por moneda.
3. **Marco teórico**: asimetría de información, selección adversa, riesgo moral, diferenciación de precios y calidad por antigüedad.
4. **Marco normativo**: Decreto 163/2026, resoluciones 104/17/52/171-175/312/102 de 2026, Gaceta 65/2026; impedimentos legales para recolección y uso de datos.
5. **Arquitectura de datos**: fuentes (Revolico, concesionarios, tasas BCC/elTOQUE, salarios Resolución 14, redes), esquema común con IDs, precio+moneda, geografía, timestamps y procedencia; pipeline de 3 colas con commit cada 25 procesados; limpieza a `autos`/`revision`.
6. **Descriptivo**: distribuciones (mediana, IQR, outliers), segmentación por marca-modelo-año, precio/km, geografía municipal, series con snapshots.
7. **Analítico**: comparables por modelo ±2 años y municipio, depreciación, clasificación de calidad y costos ocultos, regresión hedónica, margen de rentabilidad, asequibilidad precio/salario, ponderación de preferencias, explicabilidad tipo SHAP.
8. **Entregables del análisis**: tablas limpias, dashboard de mercado, informe bilingüe y trazabilidad de cada cifra. El producto interactivo de recomendación se difiere a una especialización posterior.
9. **Validación y entrega**: dedup, manejo de missing, sensibilidad a moneda y supuestos, pruebas con datos conocidos, informe bilingüe, limitaciones y monitoreo continuo.

**Lo que ya existe:** BD de 6.334 anuncios / 317 autos, esquema con 30 campos + auditoría, imágenes/teléfonos, snapshots de precios, normativa documentada, tasas y salarios referenciados, repositorios de modelos y dashboards.

**Lo que falta por conseguir:** extracción estructurada de año/km/marca/modelo/combustible/transmisión desde `ad_json`/`apollo_full`; montos de costos ocultos; precios de transacción reales; estadísticas oficiales cubanas de parque y matriculaciones; encuestas a compradores habaneros; series históricas de tasas y salarios digitalizadas; geocodificación de ubicaciones; validación en vivo de anuncios.

**EN.** The detailed framework covers nine blocks: decision, scope, theory, regulation, data architecture, descriptive analytics, causal/comparable analytics, interactive product, and validation/delivery. Existing assets and missing data needs are listed explicitly.

## 21. Cambio de objetivo / Objective change (18/11/2026)

A petición del usuario, el objetivo inmediato deja de ser la recomendación interactiva de compra y pasa a ser **un análisis de mercado**. En consecuencia:

- La fase 8 pasa a llamarse **Análisis de mercado, comparables y rentabilidad**.
- Se eliminan del alcance actual la ponderación de preferencias del usuario y el recomendador interactivo.
- Quedan como **especialización futura**: el producto que traduzca preocupaciones del usuario en una recomendación explicada.
- El marco detallado de la sección 20 se mantiene, pero sus bloques 1 y 8 se interpretan ahora como *objetivo del análisis* y *entregables del análisis*, respectivamente.

**EN.** At the user's request, the immediate objective becomes market analysis instead of interactive purchase recommendation. Phase 8 is renamed; user-preference weighting and the recommender are deferred to a later specialization.

## 22. Análisis descriptivo inicial / Initial descriptive analysis (18/11/2026)

Se creó `Auxiliares/herramientas/analisis_mercado.py`, que genera en `Data/analisis/`: `resumen_general.csv`, `precios_por_marca.csv`, `precios_por_municipio.csv`, `precios_por_anio.csv`, `outliers.csv`, `cobertura.csv`, `informe_descriptivo.md` y `dashboard.html`.

Resultados sobre 323 autos: 248 precios USD válidos (≥500 USD); 74 precios <500 USD marcados como inválidos y 1 en CUP excluidos. Precio mediano **22.000 USD**, media 24.416,59 USD, IQR 11.375–35.000 USD, rango 600–95.000 USD. Marca más frecuente: Hyundai (n=75); municipio con más oferta: Playa (n=53). Cobertura de campos derivados: marca 68,4 %, año 63,5 %, km 6,2 % (heurísticos, extraídos solo de título/descripción). Detectados 5 outliers por IQR.

**EN.** Initial descriptive analysis: 323 cars, 248 valid USD prices, median 22,000 USD, IQR 11,375–35,000, Hyundai and Playa leading, 5 IQR outliers. Derived year/km fields remain partial and heuristic.

## 23. Conversión elTOQUE, serie temporal y gráficas (18/11/2026)

Se amplió `analisis_mercado.py`:

- **Por año del vehículo**: `precios_por_anio.csv` con n, mediana USD, mediana CUP y tasa promedio; la conversión usa `precio_USD × TRMI elTOQUE` del día del anuncio (columna `Mediana` de `Anexos/Investigacion Cambios/trmi_USD.csv`). **Aclaración vigente:** el pipeline de `Data/analisis_rentabilidad/` usa la TRMI fija de 930 CUP/USD del 18/11/2026 (`config.py`); la serie diaria es referencia histórica, no insumo del modelo actual.
- **Supuesto de anuncio activo**: todos los registros tienen `status=PUBLISHED` y página verificada en la captura, por lo que se asume que son comprables; no se comprueba disponibilidad en tiempo real.
- **Serie precio vs tasa**: `serie_precio_vs_tasa.csv` y `serie_precio_vs_tasa_mensual.csv`, con variación % diaria de la TRMI, del precio CUP y del precio USD. Ejemplo histórico: la TRMI pasó de 680 CUP/USD (09/07/2026) a 920 (16-17/11/2026), valor ya sustituido por la convención fija de 930 del 18/11/2026 que usa el pipeline; la mediana mensual CUP subió de 12,58 M (julio) a 20,7 M (noviembre).
- **Gráficas**: `Auxiliares/herramientas/graficos_mercado.py` usa matplotlib, seaborn y plotly (instalados) y genera 8 PNG + `dashboard_interactivo.html` en `Data/analisis/graficos/`.

**EN.** Prices converted to CUP with elTOQUE daily TRMI, divided by vehicle year, with a daily/monthly price-vs-rate series and a full plotting module (matplotlib/seaborn/plotly). Active ads are assumed purchasable.

## 24. Estado del scrapeo y procesamiento de diccionarios (18/11/2026)

**Diccionarios/JSON guardados** (6.334/6.334 anuncios): `meta_json`, `ad_json` y `apollo_full`. En `ad_json` hay 21 claves, entre ellas `price`, `currency`, `status`, `updatedOnByUser`, `province`, `municipality`, `subcategory`, `imagesCount`, `viewCount`, `permalink`. En `apollo_full` hay cinco tipos: `ImageType`, `CategoryType`, `ProvinceType`, `MunicipalityType`, `AdType` y `ROOT_QUERY`. **No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**: por eso `anio_est`, `marca_est` y `km_est` se derivan con regex del texto visible (cobertura 63,5 %, 68,4 % y 6,2 %). Los diccionarios se usan hoy para precio/moneda/estado/fecha/geografía y como respaldo de trazabilidad; `autos` no guarda esas columnas y se hace `JOIN` con `anuncios` para el análisis.

**Reporte de scrapeo:** `anuncios` 6.334 · `autos` 323 · `revision` 6.085 · `imagenes` 13.932 · `telefonos` 7.699 · BD 520,6 MB. Colas: `url_queue` 141 (125 done, 3 downloading, 13 pending); `download_queue` 125 (123 processed, 1 processing, 1 pending); `process_queue` 123 (107 committed, 16 pending). Los pendientes quedaron de una corrida interrumpida por reinicio del servidor. Snapshot `ultimo.json` de 17/11 04:44 (6.334 entradas); partes generadas: 0. `revolico-git.timer` activo (última ejecución 10:12). El análisis descriptivo y las 8 gráficas + dashboard ya están en `Data/analisis/`.

**EN.** JSON dictionaries hold price/currency/status/date/geography but no structured year/km/brand; those remain heuristic. Scrape report: 6,334 ads, 323 cars, 6,085 rejections, queues with pending items from an interrupted run, no DB chunks uploaded yet.

## 25. Reanudación, resiliencia y supuesto de catálogos (18/11/2026)

- **Librerías de mapas instaladas:** `geopandas 1.2.0`, `shapely 2.2.0`, `pyproj`, `folium 1.0.0`, `mapclassify`, `geopy` (además de matplotlib/seaborn/plotly ya instaladas).
- **Reinicio automático:** `revolico-scrape.service` ahora tiene `Restart=on-failure`, `RestartSec=30`, `StartLimitIntervalSec=300` y `StartLimitBurst=20`, de modo que una pérdida de conexión que detenga el proceso provoca su relanzamiento.
- **Supuesto de catálogos:** en `analisis_mercado.py` se añadió `add_publication_assumption()`. Para concesionarios y páginas similares (`CATALOGOS`) se asume que todo el catálogo está disponible salvo que la página indique lo contrario y que se publicó el día de la captura (`fecha_publicacion = scraped_at`); el año del vehículo no es clave. Para clasificados se mantiene el supuesto de anuncio activo = comprable, con `fecha_publicacion = updated_on_by_user`.
- **Reanudación:** se reanuda el pipeline desde las colas pendientes (13 URLs, 1 descarga y 16 decisiones pendientes) con `revolico-scrape.timer` activo e indefinido.

**EN.** Map libraries installed, systemd auto-restart added, catalog availability/publication-date assumption encoded, and the pipeline resumed from pending queues.

## 26. Orden corregido: enlace → clasificación → BD (17/11/2026)

Se identificó la causa del retraso en la clasificación: el timer ejecutaba `actualizar_revolico.py`, que solo corre el scraper y divide la BD, sin escribir nunca `autos`/`revision`. El servicio ahora ejecuta `scrape_revolico_pipeline.py`, que sigue el orden pedido:

1. **Descubrimiento**: obtiene el enlace y, con el título del listado, aplica `clasificar_enlace()`; los que claramente no son vehículos 4+ ruedas se marcan `rechazado` y se registran en `revision` sin descargarlos.
2. **Descarga**: solo procesa enlaces con `es_auto_candidato=1`.
3. **Procesamiento**: clasificación definitiva con la página completa y commit cada 25 procesados a `autos`/`revision`.
4. **Partes**: al terminar, genera `estado.json` y las partes de la BD para `revolico-git.timer`.

Prueba con 1 página: 120 enlaces descubiertos, 63 descartados tempranamente y 185 candidatos descargados; `autos` pasó de 323 a 326 y `revision` de 6.085 a 6.134.

**EN.** Root cause fixed: the timer now runs the queue pipeline, which classifies each link at discovery time before downloading, so only car candidates reach the database. Early test: 120 links, 63 rejected early, 185 candidates, autos 323→326.

## 27. Aviso periódico y umbral de revisión (17/11/2026)

- `revolico-aviso.timer` avisa **cada 10 minutos** mediante `revolico-aviso.py`: escribe `Data/Revolico/progreso.md`, envía `notify-send` al escritorio y registra en el journal.
- El aviso incluye anuncios, autos, revisiones, sin revisar, estado del servicio, colas, partes y fecha de `estado.json`.
- **Umbral:** cuando `anuncios WHERE pagina_revisada=0`llega a **4.000** (configurable con `REVISAR_UMBRAL`), el aviso lanza `revolico-revisar.service`, que ejecuta el pipeline con `--solo-colas`: drena descargas y decisiones pendientes **sin descubrir páginas nuevas**. Se omite si el scrapeo o la revisión ya están activos.
- Estado actual: 3.623 sin revisar, por debajo del umbral; 266 URLs, 11 descargas y 24 decisiones pendientes en colas.

**EN.** A 10-minute timer reports progress via desktop notification and a markdown file. At 4,000 unreviewed ads it triggers a queue-draining service that classifies pending items without new page discovery.

## 28. Primeros datos de Telegram (17/11/2026)

No hay credenciales MTProto (`TELEGRAM_API_ID`/`TELEGRAM_API_HASH` vacías), así que se implementó `Auxiliares/herramientas/scraper_telegram_publico.py`, que lee la vista pública `t.me/s/<canal>` y pagina con `?before=<id>`. No requiere login, redacta teléfonos y guarda `Data/integraciones/telegram/{anuncios.jsonl,anuncios.csv,estado.json}`.

Corrida final (50 páginas): **152 mensajes**, **54 anuncios de autos** del canal `goldenbullbusinessfamilycars`, 45 con año detectable y **ninguno con precio explícito** (el canal expresa kilómetros como `25500K`, `40K`, etc.). Esta fuente sirve hoy para señal de oferta/modelo/año, no de precio.

**Búsqueda de más canales:** se probaron `Revolico_Cuba_Oficial`, `Ventas_Revolico_Holguin_Cuba`, `revolico_baracoa`, `timbirichi_compra_y_venta_cuba`, `PiezasdeCarrosCU`, `directoriocubano`, `eltoquecom`, `coventcuba`, `APublished`, `GEEKSCUBANS_PLUS` y `lachopivaraderooo`. Ninguno publicó anuncios de autos accesibles sin unirse: son noticias, eventos, compra-venta general, repuestos o grupos con invitación. Quedan documentados en `CANALES_DESCUBIERTOS` del scraper para no repetir la búsqueda.

**EN.** Final run: 152 messages, 54 car ads from one channel, 45 with year, no prices. Eleven additional Cuban channels were checked and found unusable without joining (news, events, general trading, parts or invite-only).

## 29. Base de datos de Telegram (17/11/2026)

Se creó `Auxiliares/herramientas/telegram_db.py` con `Data/integraciones/telegram/telegram.sqlite` y tres tablas: `canales`, `anuncios` y `estado`. Ambos scripts escriben en ella **mientras corren**: `descubrir_canales_telegram.py` guarda cada canal validado y `scraper_telegram_publico.py` guarda cada anuncio de auto.

Backfill inicial completado:

| Tabla | Registros |
|---|---:|
| `canales` | 119 |
| `canales` con contexto automotriz | 4 |
| `anuncios` | 54 |
| `anuncios` marcados `es_auto` | 54 |

Objetivo de 100 canales de referencia superado (119). El descubrimiento usa 26 búsquedas en tgden.com y valida cada usuario con `t.me/s/`, filtrando por contexto cubano. Los JSONL originales se conservan como respaldo.

**EN.** A shared SQLite DB now stores Telegram channels and car ads as they are discovered/scraped: 119 channels, 54 ads, with JSONL backups.

## 30. Gestión de bases de datos con Git LFS (17/11/2026)

Se instaló **Git LFS 3.8.1** y se activó en el repositorio. `.gitattributes` marca `*.sqlite`, `*.sqlite-wal` y `*.sqlite-shm` con `filter=lfs diff=lfs merge=lfs -text`; se retiraron las reglas de `.gitignore` que excluían `revolico.sqlite` y los SQLite de concesionarios.

Se detuvieron temporalmente los timers de scrapeo y sincronización para tomar estados consistentes. Las bases pasan a gestionarse con LFS: `revolico.sqlite` (~803 MB), `pipeline.sqlite` (~117 MB), los catálogos de concesionarios y `telegram.sqlite`. El esquema de **partes de Revolico se conserva** como respaldo auditable; LFS no lo sustituye.

**Advertencia:** la cuota LFS del plan gratuito es limitada; una BD que cambia cada 10 minutos genera un blob nuevo por commit. Vigilar el consumo con `git lfs ls-files` y `git lfs env`.

**EN.** Git LFS 3.8.1 installed and configured for all SQLite files; the Revolico chunk scheme remains as an auditable backup. LFS quota must be monitored because active DBs create a new blob per change.

## 31. Rango temporal de anuncios Revolico (17/11/2026)

Se fijó el rango permitido de `updated_on_by_user` entre **2021-01-01 y la fecha actual** en `limpiar_revolico.py` (`FECHA_MINIMA`). Los anuncios fuera de rango van a `revision` con motivo `fuera de rango temporal`.

Estado actual: anuncio más antiguo **2024-12-17**, más reciente **2026-11-17**; por tanto **0 exclusiones por fecha**. La limpieza general sobre 9.957 anuncios conservó **548 autos** y registró 9.409 exclusiones (9.316 no vehículo 4+ ruedas, 93 sin datos necesarios). El rango quedó aplicado para futuras corridas.

**EN.** Revolico ads are bounded to 2021-01-01..today. Current oldest ad is 2024-12-17, so no ad was excluded by date; 548 cars were kept from 9,957 ads.

## 32. Backfill de descubrimiento sin procesamiento (17/11/2026)

Se añadió `--solo-descubrimiento` a `scrape_revolico_pipeline.py`. En ese modo:
- se recorren las páginas de búsqueda desde la 1 hacia atrás;
- se guardan todos los enlaces en `url_queue` con estado `descubierto`;
- **no hay descarga de anuncios, ni clasificación definitiva, ni inserción en `anuncios`/`autos`/`revision`**;
- se detiene al llegar a `FECHA_MINIMA = 2021-01-01`, al agotarse las páginas (página repetida/sin anuncios) o por límite de seguridad;
- escribe el marcador `Data/Revolico/.backfill_completo` con motivo, páginas y enlaces.

Se desactivó `revolico-scrape.timer` y se creó `revolico-backfill.service` (oneshot, `Restart=on-failure`) para ejecutar este único objetivo. Cuando el modo normal vuelva a arrancar, los enlaces `descubierto` pasan a `pending` para su descarga y clasificación.

**EN.** A discovery-only mode now walks pages back to 2021-01-01 (or page exhaustion) and queues links without downloading or writing to the database; normal processing is disabled until it finishes.

## 33. Parada por repetición y procesamiento de anuncios (17/11/2026)

Se modificó `descubrir_hasta_fecha()` para que se detenga en cuanto una página no aporte **ningún enlace nuevo** (todos sus anuncios ya fueron vistos), además de las condiciones de fecha mínima, fin de páginas y límite de seguridad. El contador `total` ahora acumula solo enlaces nuevos.

Se reinició `revolico-backfill.service` con la regla actualizada. Con el backfill en marcha, se inició `revolico-revisar.service` (`--solo-colas`) para pasar los enlaces `descubierto` a `pending`, descargarlos y aplicar la clasificación definitiva: los anuncios que cumplan los requisitos entran en `anuncios`/`autos`; el resto queda trazado en `revision`.

**EN.** Discovery now stops when a page yields zero new links. The queue-draining service was started to download and classify the discovered links into the car database.

---

## 34. Esqueleto de análisis de rentabilidad inspirado en Egyptian-Used-Cars (18/11/2026)

Creé `Data/analisis_rentabilidad/` siguiendo la arquitectura del repositorio **Egyptian-Used-Cars** (ingesta → limpieza → EDA → estadística → benchmark), pero adaptada a nuestras fuentes y preparada para crecer:

```text
Data/analisis_rentabilidad/
├── config.py                 # marcas, tiers, FX, umbrales (configurable)
├── scripts/
│   ├── 01_ingest.py          # Revolico + 11 concesionarios + marketplaces -> Parquet
│   ├── 02_clean.py           # limpieza y features; rechazos registrados en CSV
│   ├── 03_eda.py             # KPIs y 6 gráficos Plotly HTML
│   ├── 04_stats.py           # OLS log-precio, VIF, Kruskal-Wallis, anomalías
│   ├── 05_benchmark.py       # benchmark por marca/modelo/año e infravalorados
│   └── run_all.py
├── sql/analysis.sql          # CTEs y window functions
├── notebooks/01_exploracion.ipynb
├── data/                     # listings_raw.parquet, listings_clean.parquet
├── outputs/charts/           # HTML interactivos
├── outputs/tables/           # kpis, benchmark, modelo, vif, tests, anomalías
├── NECESIDADES.md
└── README.md
```

Instalé además `statsmodels 0.15`, `pyarrow 26`, `kaleido`, `nbformat` y `nbconvert`. `duckdb` se desinstaló porque produce `Illegal instruction` en esta CPU; se usa Parquet + Pandas en su lugar.

### Línea base real de la primera ejecución

| Métrica | Valor |
|---|---:|
| Filas ingeridas | 972 (716 Revolico + 256 concesionarios) |
| Filas limpias | 499 (497 usados, 2 nuevos) |
| Rechazos | 376 (registrados, no descartados) |
| Marcas | 32 |
| Precio mediano usado | 24.000 USD |
| Antigüedad media | 5,9 años |
| Observaciones del modelo OLS | 328 |
| Grupos de benchmark | 21 |
| Infravalorados | 30 |
| Anomalías | 17 |

El modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` da una depreciación media de **−5,43 % anual** (p<0,001), con primas de +21 % para premium y −22 % para tier medio frente al desconocido.

### Brecha frente a Egipto

Egipto tiene 23.500 anuncios, historial mensual de precios, HP y kilometraje estructurados, ANOVA/OLS/VIF, Tableau y Power BI. Nosotros tenemos el pipeline y las técnicas cubiertas, pero solo 497 usados, un único snapshot, HP/kilometraje mayormente ausentes y un solo benchmark de auto nuevo. El detalle y la priorización están en `Data/analisis_rentabilidad/NECESIDADES.md`.

**EN.** Built a scalable analysis skeleton mirroring Egyptian-Used-Cars. First run: 972 ingested, 499 clean, 497 used cars, 32 brands, −5.43%/year depreciation. Main gap versus Egypt: listing volume, price history and structured vehicle specs.

---

## 35. App de circuitos eléctricos de Apklis (18/11/2026)

Descargué tres APKs desde la API de Apklis (`api.apklis.cu/v2/application/` + `POST /v2/release/get_url/`): **Circuitos Habana** (`com.ermetic.circuitoshabana`, v2.2), **Apagones Habana** y **Donde Hay Luz Habana**. Con **jadx 1.5.6** descompilé la primera y encontré el mecanismo que buscábamos:

- La app **no usa una API privada**: hace scraping del canal público de Telegram `https://t.me/s/EmpresaElectricaDeLaHabana` con Jsoup y User-Agent de Chrome.
- Paginación con `?before=<message_id>`, hasta 16 páginas / 300 mensajes / 8 días, con sincronización incremental.
- Parsea `div.tgme_widget_message`, `time[datetime]` y `div.tgme_widget_message_text`; convierte timestamps UTC a hora de Cuba con +1 h de horario de verano.
- Filtra por palabras clave (afectación, déficit, avería, disparo, restablecido, energizado, apagón, traspasos…) y extrae circuitos, bloques, duraciones y causas.
- Guarda el historial en SQLite local, dispara notificaciones y dibuja los circuitos sobre teselas OpenStreetMap.

Evidencia y APKs en `Data/apklis/`. Detalle completo en `Data/apklis/analisis_circuitos_habana.md`.

**EN.** Downloaded and decompiled the Cuban app `Circuitos Habana`. It scrapes the public Telegram channel of the Havana electric company (`t.me/s/EmpresaElectricaDeLaHabana`) with Jsoup, paginating via `?before=<id>` and parsing affectation messages into a local SQLite history. This gives us a free, real-time power-outage data source for cross-analysis with EV infrastructure.

---

## 36. Mapa offline, talleres e infraestructura EV (18/11/2026)

- Se intentó usar `google-maps-scraper` en Docker, pero **el daemon Docker no arranca sin root** en este entorno (`dockerd needs to be started with root privileges`), por lo que se descartó esa vía.
- Overpass/OSM fue consultado dos veces; no devuelve `shop=car`, `shop=car_repair` ni `charging_station` etiquetados en Cuba, así que no hay datos geográficos útiles de ahí.
- Se extrajeron coordenadas de los **mapas incrustados en las propias webs** de los concesionarios (BDC One: 23.1155203,-82.3596368 y 23.0992805,-82.3050631; Dongfeng: 23.1250339,-82.4227564) y se geocodificó una dirección adicional con Nominatim.
- Se generó `Data/mapas/mapa_ofline.html`: contorno de Cuba embebido + marcadores + Plotly incluido, funciona sin internet. También `concesionarios.csv`.
- Se investigó infraestructura EV: Dongfeng/NWI 11 estaciones solares (2026), CIMEX+MITRANS 21 estaciones (2025), primera estación rápida en Santa Clara (08/2026), conectores CCS2 y directorios KargalaYa/ChargeFinder/Electromaps. Detalle en `Data/mapas/infraestructura_ev_cuba.md`.

Pendiente: scrapear KargalaYa/Electromaps para cargadores y las páginas de contacto de los concesionarios restantes para completar el mapa con talleres.

**EN.** Docker could not start without root, so the Google Maps scraper was unavailable. OSM/Overpass had no Cuban car-repair tags. Built an offline Plotly map from coordinates embedded in dealership websites and researched EV charging infrastructure sources for Cuba.

---

## 37. Optimización de pipelines (18/11/2026)

Para acortar los tiempos de finalización:

1. **Revolico:** `scrape_revolico.py` ahora usa una **sesión curl_cffi por hilo** (`threading.local`) con impersonación Chrome, reutilizando conexiones TLS en vez de crear una por petición. El servicio `revolico-revisar.service` pasó de 8 descargadores/4 procesadores a **20/8** con `--batch-size 100`, `TimeoutStartSec=0` y `Restart=on-failure` para sobrevivir reinicios.
2. **Marketplaces:** `scrape_marketplaces.py` acepta `--workers`; el nuevo servicio `marketplaces-scrape.service` corre **6 tiendas en paralelo** con `--delay 0.8`, cada una escribiendo su propia SQLite (sin bloqueos entre ellas).
3. **Efecto medido:** en minutos, los anuncios de Revolico pasaron de 10.117 a **10.149** y los autos de 716 a **814**; quedan 3.351 URLs pendientes y 1.940 rechazadas. Los marketplaces ya completaron Cubisima, Apululu, Carros.com, Autocubana y VentaCuba y siguen con iTENCEL/Timbirichi.

Los servicios de usuario (`revolico-revisar`, `marketplaces-scrape`, `revolico-snapshot`) se reinician automáticamente tras fallo, de modo que los reinicios del servidor ya no detienen el trabajo.

**EN.** Optimized both pipelines: per-thread TLS sessions, 20 downloaders/8 processors for Revolico, and 6 parallel marketplace workers with separate SQLite files. Added systemd services with automatic restart.

---

## 38. Reporte automático de progreso (18/11/2026)

Creé `Auxiliares/herramientas/reporte_progreso.py` y el timer de usuario `progreso-report.timer`, que actualiza **`Data/progreso_reporte.md` cada 5 minutos** con:

- conteos de `revolico.sqlite` (anuncios, autos, revisiones, imágenes, teléfonos, historial de precios);
- estado de las colas de `pipeline.sqlite` (pendientes, descargando, procesadas, fallidas);
- anuncios/comentarios/vendedores por marketplace;
- estado de los servicios systemd.

El timer es persistente (`Persistent=true`) y arranca 1 minuto después del boot. De este modo el seguimiento sobrevive a los reinicios del servidor.

**EN.** Added a 5-minute systemd timer that writes `Data/progreso_reporte.md` with download/processing counts and service status.

---

## 39. Continuación del scrapeo y presentación narrativa (18/11/2026)

- Se ampliaron los límites de `scrape_marketplaces.py`: Cogetucarro de 200 → **5.008**, Autocubana y Timbirichi a 40 páginas. El servicio `marketplaces-scrape.service` se relanzó con 6 workers; en minutos Autocubana pasó de 400 a **566** y Timbirichi de 110 a **170**, totalizando **2.121 anuncios**.
- El pipeline de Revolico se reinició con **12 descargadores / 8 procesadores** y se añadió reintento explícito ante `database is locked` (`_retry_exec`). Quedan **3.351 URLs pendientes**; autos: **814**.
- `reporte_progreso.py` + `progreso-report.timer` actualizan `Data/progreso_reporte.md` cada 5 minutos.
- Se redactó `Data/analisis_rentabilidad/PRESENTACION_STORYTELLING.md`: relato en 10 actos con personajes, conflicto, hallazgos, comparación con Egipto y llamada a la acción.

**EN.** Raised marketplace caps and restarted both pipelines; added SQLite lock retries. Created a 10-act storytelling presentation of the market analysis.

---

## 40. Renombre del repositorio en GitHub (18/11/2026)

Con `gh repo rename` se cambió el nombre del repositorio remoto:

```text
antes: CarlosAntonioAceaJimenezCD/autodecide-habana
ahora: CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba
```

GitHub no permite espacios en los nombres de repositorio, por lo que se usó el slug `el-precio-de-moverse-en-cuba`. `gh` actualizó automáticamente el remoto `origin` del clon local. La carpeta local sigue siendo `~/Proyectos/ICD Automotive Market Project` para no romper las rutas absolutas de los servicios systemd ni los enlaces desde AutoDecide.

Descripción actual del repo: *"Minimizar los gastos de la compra de coches en La Habana Cuba"*.

---

## 41. Gasolineras, estaciones de carga y serie de precios del combustible (18/11/2026)

- Búsqueda en DuckDuckGo (`gasolineras cuba`) y en Yahoo/ddgs: se identificaron WhereFUEL, Directorio Cubano, D-Cuba, encuba.net, DailyFuels, GlobalPetrolPrices, ChargeFinder, Electromaps y Kargalaya.
- **Overpass/OSM devolvió 137 gasolineras en La Habana** con coordenadas, marca, dirección y tipos de combustible. WhereFUEL usa esa misma base OSM (110 puntos en radio de 12 km).
- **Kargalaya** aportó 9 estaciones de carga con coordenadas y precio por hora (Super48, Battery Lab, SOLGUARA, Parqueo M y 25, Universidad de Ciencias Médicas, Trisolinera Habana, PDL Campeño, ADT64, Automovion SRL). **Electromaps** añadió 3 referencias sin coordenadas. ChargeFinder respondió 403 en su API.
- Se crearon `Data/mapas/gasolineras.csv` (137) y `Data/mapas/estaciones_carga.csv` (12), y se regeneró `mapa_ofline.html` con tres capas: concesionarios (3), carga eléctrica (9) y gasolineras (137).
- Se creó `Data/combustible/precios_combustible.sqlite` con **18 observaciones** entre 20/08/2026 y 18/11/2026, diferenciando mercado oficial CIMEX, informal elToque y precios publicados, sin convertir monedas automáticamente.
- El script `Auxiliares/herramientas/scrape_infraestructura.py` es idempotente y el timer `precio-combustible.timer` lo ejecuta mensualmente para alimentar la serie histórica.

Hallazgo relevante: desde 07/02/2026 la venta oficial en CUP está suspendida y el combustible se vende en USD vía Ticket; desde mayo cada importador fija su precio. La B94 informal pasó de 3.500–5.000 CUP (ago) a 7.000–8.000 CUP (sep 2026).

**EN.** Added 137 Havana fuel stations from OSM, 12 EV charging references, and an 18-row historical fuel-price SQLite database with a monthly update timer. Regenerated the offline map with three layers.

---

## 42. Base unificada del mapa y talleres (18/11/2026)

Se creó `Data/mapas/mapa_elementos.sqlite` como **fuente única** del mapa offline, con tablas `tipos` y `elementos`. Cada elemento guarda coordenadas, dirección, fuente, URL, teléfono, horario, precio, estado y detalle crudo en JSON. Colores asignados:

| Tipo | Color | Símbolo |
|---|---|---|
| Gasolinera | negro | círculo |
| Estación de carga | verde | diamante |
| Concesionario | azul | cuadrado |
| Taller | rojo | triángulo |

`generar_mapa_ofline.py --tipos all|gasolinera,estacion_carga|concesionario,taller` permite elegir qué capas generar; el HTML incluye Plotly embebido. Estado final: **131 gasolineras, 12 estaciones de carga, 25 concesionarios (17 con coords) y 22 talleres (todos con coords)**. Los 8 concesionarios sin coords se exportan a `elementos_sin_coordenadas.csv`.

Para los talleres se usaron las webs de BDC One (schema.org Place + mapa incrustado) y Dongfeng (postventa/showrooms), Cubisima, NearPlace, Páginas Amarillas, tallermanolito.com, Yellocu y Cybo. **Cybo devolvió 403 con curl_cffi**, por lo que se aplicó el stack anti-bot disponible: `patchright` (Chromium con fingerprint de Chrome) y FlareSolverr en `http://127.0.0.1:8191/v1`. Las direcciones se geocodificaron con Nominatim y Photon (`geocode_elementos.py`); las tres referencias de Electromaps sin dirección de calle quedaron marcadas como aproximadas al centro de La Habana.

**EN.** Created a unified SQLite source for the offline map with selectable layers and required colors (black fuel, green charging, blue dealerships, red workshops). Added workshops from dealership sites and directories; used patchright/FlareSolverr for anti-bot pages and Nominatim/Photon for geocoding.

---

## 43. Apartado de “cuánto costaría moverse” en el storytelling (18/11/2026)

Se amplió la sección 2 del storytelling con el bloque **¿Cuánto costaría moverse?**, desarrollado a partir del borrador del usuario y con los vacíos completados mediante verificación web:

- **Marco previo:** Acuerdo **9811 de 2024** del Consejo de Ministros, que fijaba precios minoristas de combustibles en CUP y USD.
- **7/02/2026:** CIMEX anunció medidas temporales —respaldadas por el MEP y el viceministro Oscar Pérez-Oliva Fraga— que suspendieron la venta en CUP y activaron **Ticket** (20 L por turno, 24 h para usarlo). No se localizó una resolución numerada nueva en la Gaceta Oficial; fue una disposición administrativa.
- **15/02/2026:** el Gobierno autorizó a **mipymes, cooperativas y otros actores económicos no estatales** a importar combustible directamente.
- **12–15/05/2026:** nota del MFP y **Circular Especial 03/2026 de CIMEX**; desde el 15/05 cada importador habilitado fija su precio según costo real de importación (1,80–2,60 USD/L).
- Se incorporaron también la insuficiencia prevista de electrolineras, la carga en casa condicionada por los circuitos eléctricos, las rotaciones con más de 60 h sin luz y la dependencia de los surtidores de energía.

Fuentes: Cubadebate (07/02/2026), Directorio Cubano (12 y 15/05/2026), CubaTrámite (Circular 03/2026) y D-Cuba (20/02/2026).

**EN.** Expanded the storytelling with a “cost of getting around” section, verified against the 2024 price agreement, the 7 Feb 2026 CIMEX measures, the 15 Feb 2026 private-import authorization and the 15 May 2026 pricing liberalization.

---

## 44. Reescritura de mantenimiento y retorno en el storytelling (18/11/2026)

Se reescribieron los dos párrafos restantes de la sección 2 con el mismo nivel de detalle que el apartado del combustible:

- **¿Quién lo mantiene?**: incorpora los **22 talleres** y **25 concesionarios** geolocalizados, las redes formales (BDC One, Dongfeng, ATR, SASA) y los talleres independientes (CarFix, Taller Calle 8, Taller VÉLO, Trisolinera Habana, Tecni-Motos, Taller Manolito), además del costo de inmovilización por piezas importadas.
- **¿Qué devuelve la inversión?**: incorpora el uso del vehículo como **taxi formal o informal** para ingresos estables, en continuidad con taxis, triciclos y gacelas; la depreciación de **−5,43 % anual** obtenida en la primera corrida (p < 0,001; §34), cifra que la corrida vigente ya no sostiene, junto con las primas premium de **+21 %**, los descuentos del **−22 %** para tier medio, **30 infravalorados**, **66 anomalías** y el marco del **Decreto 163/2026**.

**EN.** Rewrote the maintenance and ROI storytelling sections with mapped workshops/dealerships, immobilization costs, taxi-income use, depreciation metrics and the 2026 regulatory framework.

---

## 45. Reescritura de la sección 3 del storytelling (18/11/2026)

Se transformó la sección **Lo que encontramos** de una tabla de datos en una narrativa de hallazgos (cifras de la corrida del 18/11/2026, posteriores a las que se recogen en §59): la proporción de anuncios que resisten el filtro de auto real, la mediana de 23.000 USD, la antigüedad media de 6,3 años, las 34 marcas, la depreciación de −5,43 % anual, los 27 grupos comparables y las 30 oportunidades infravaloradas. El cierre deja la idea central: un mercado pequeño pero con estructura suficiente para dejar de improvisar.

**EN.** Rewrote the findings section of the storytelling as a narrative: signal-to-noise ratio, median price, fleet age, brands, depreciation curve and undervalued opportunities.

---

## 46. Apertura de la sección 3 del storytelling (18/11/2026)

Se añadió una apertura que hace explícita la división del mercado en dos capas —marketplaces y concesionarios/tiendas oficiales— y una nota que define el propósito de la sección: mostrar la forma real del mercado después de separar el ruido, sin explicar el proceso de adquisición de datos.

**EN.** Added an opening that frames the market as two layers (marketplaces vs. official dealerships) and states the purpose of the findings section.

---

## 47. Reescritura de la sección 4 del storytelling (18/11/2026)

Se transformó **La curva de valor** en una narrativa sobre el envejecimiento desigual del parque: premium frente a autos de uso medio, combinación de antigüedad con kilometraje, estado y marca, y la idea de la marca como “seguro de valor”. Se eliminaron los porcentajes repetidos de la sección 3 para que la curva se sienta como continuación y no como repetición.

**EN.** Rewrote the depreciation section as a narrative of unequal aging, avoiding repetition of the percentages already presented in section 3.

---

## 48. Definición de marcas premium y no premium (18/11/2026)

Se fijó el criterio de segmentación de marcas para el storytelling y el análisis:

- **Premium:** Mercedes-Benz, BMW, Audi, Lexus, Volvo, Porsche, Land Rover, Jaguar, Cadillac, Infiniti y Acura.
- **No premium:** Hyundai, Kia, Toyota, Lada, Fiat, Chevrolet, Peugeot, Honda, Nissan, MG, Dongfeng, Moskvich, Volkswagen, Mitsubishi, Geely, Ford, Jeep, Foton, GMC, SEAT, Renault, Buick, Mazda, BYD, Changan, JAC, Plymouth, Suzuki y Pontiac, más las marcas de catálogo oficial sin volumen en la muestra (Maxus, Voyah, MHERO, FUSO, KGM/SsangYong, Chery, Haval, Great Wall e Isuzu).

La lista completa, con evidencia y conteos, está en `Data/analisis_rentabilidad/marcas_cuba.md`. Se incorporó un resumen en la sección 4 del storytelling. El modelo econométrico conserva sus tres niveles (`premium`, `medio`, `economico`); la narrativa usa solo dos grupos para ser legible.

**EN.** Defined premium vs. non-premium brands for Cuba based on observed listings and dealer catalogs, with a reference table and a summary in the storytelling.

---

## 49. Búsqueda de repositorios cubanos de automoción (19/11/2026)

Se buscaron repositorios en GitHub con la API (`gh api search/repositories`) usando 31 consultas en español e inglés: mercado automotriz cubano, carros/autos/vehículos en Cuba, Revolico, motos/triciclos, precios y divisas. Tras deduplicar se obtuvieron **648 repos**, de los que se depuraron **36 con relación directa o instrumental** al mercado automotor cubano.

La lista, ordenada por fecha de actualización y con la descripción de qué contiene cada uno, está en `Data/github-repos-automotriz-cuba-2026-11-19.md`. Incluye proyectos de análisis de mercado (ICD-Mercado-Automotriz, AutosxCuba, Mercado-automotriz, autos-cuba), motos y triciclos, tiendas de repuestos, scrapers de Revolico, bots de Telegram, clasificadores de anuncios, observatorios de precios y fuentes de divisa informal.

Se excluyeron falsos positivos de la búsqueda amplia (GTA, proyectos genéricos “Taller 1”, repos sin relación con Cuba o automoción). El repositorio `kremondherranz-lgtm/Mercado-automotriz` ya había sido clonado en `Auxiliares/Repositorios Referencias`.

**EN.** Searched GitHub for Cuban automotive-market repositories: 31 queries, 648 unique results, 36 relevant repos documented with contents and update dates.

---

## 50. Consolidación de bases de los repositorios de autos (19/11/2026)

Se filtraron los 36 repositorios del listado anterior para conservar solo los dedicados a **autos** (se descartaron motos, triciclos, patinetes, tiendas de repuestos, bots de Revolico y divisas) y se clonaron los que faltaban. De los 7 resultantes, los dos repos de `randoloc` son duplicados en código (mismo proyecto CubAutosFinder).

Se compararon 233 archivos de datos por hash y 76 CSV por contenido ordenado. Se detectaron 12 grupos de duplicados bytes y 11 de duplicados por contenido: anuncios repetidos dentro de `Mercado-automotriz`, `anuncios_limpios` = `mercado_havana`, `DATASET_COMPLETO_MEJORADO` = `DATASET_PARA_GRAFICOS`, catálogos MCV/Dongfeng/Womy/BDC repetidos entre `Mercado-automotriz` y `autos-cuba`, snapshots parciales de la encuesta, copias de entrevistas y tablas de reporte.

Se creó `Data/repos-autos-referencias/referencias_autos.sqlite` con **25 tablas** (3.958 anuncios de Revolico, 3.566 limpios, catálogos de comercializadoras, 33 respuestas de encuesta, 30 + 30 + 8 entrevistas, datasets de AutosxCuba) y una tabla `provenancia`. De los 3.958 anuncios, **369 ya estaban en nuestra base** (marcados con `en_nuestro_proyecto=1`) y 3.589 son nuevos; no se modificó `revolico.sqlite` para preservar el historial de precios. Script reproducible en `Auxiliares/herramientas/consolidar_repos_autos.py`.

La documentación de encuestas y entrevistas está en `Data/repos-autos-referencias/ENCUESTAS_Y_ENTREVISTAS.md`: la encuesta con datos reales fue un Google Forms de 32 preguntas aplicado a 33 personas de 4 segmentos en un barrio de La Habana (17 de 18–25 prefieren eléctrico, pero 16 de 18 no pagarían más de 4.000 USD por uno); los otros dos cuestionarios son solo instrumentos sin respuestas. Las entrevistas (30 + 30 + 8) son cualitativas, anónimas salvo el grupo de AutosxCuba —que incluye nombres y requiere cuidado— y aportan precios de combustible 2,00–2,70 USD/L, mantenimientos de 200 a 3.000 USD y percepciones sobre repuestos y clásicos.

**EN.** Filtered the 36 repos down to 7 automotive-only ones, compared 233 data files, discarded 23 duplicate groups, and consolidated 25 non-duplicate tables into a provenance-tracked SQLite. Documented the surveys and interviews: one 33-respondent demand survey with data, two questionnaire instruments only, and 68 qualitative interviews.

---

## 51. Mejoras del proyecto (20/11/2026)

Se ejecutó una tanda de mejoras una por una, sin borrar archivos. Ninguna modificó las bases fuente: todas actúan sobre código, documentación y outputs derivados, con respaldos en `/tmp/opencode/`.

1. **Deduplicación de `autos`**. La tabla se reconstruyó desde `anuncios` (fuente canónica): 814 filas con 748 IDs únicos → **744 autos únicos**. Se excluyeron 4 anuncios que no son autos (`58867937`, `53777554`, `53843413`, `58886962`), marcados en `anuncios` con `es_auto=0` y motivo `no es auto: servicio/combustible`. Se creó el índice único `idx_autos_id` y `limpiar_revolico.py` incorporó `EXCLUDE_IDS`, `INSERT OR REPLACE` y el índice para que no reaparezcan.
2. **Regeneración del análisis**. `run_all.py` volvió a correr sobre la base de 744 autos: 3.222 registros crudos y 744 limpios, frente a los 680 anteriores.
3. **Reparación de la ingesta de marketplaces**. `parse_price` ahora interpreta separadores de miles (973 anuncios recuperados: 872 de iTENCEL, 99 de Cubisima, 2 de VentaCuba). Los precios vacíos de Autocubana se recuperan del JSON-LD (614 anuncios, mediana 17.000 USD) y los títulos de interfaz (“Reportar este anuncio”, “Administrar mis anuncios”, “Comprar carros…”) se reconstruyen desde el JSON-LD o el slug de la URL. Se añadieron filtros auditables para no-autos, spam, precios que en realidad son modelo/año (116 casos en Cogetucarro) y marcadores de precio (11 en VentaCuba), todos volcados a `descartes_marketplaces.csv`. Se incorporó la columna `canal`: **1.301 anuncios locales y 672 de importación** (iTENCEL), con `kpis_canal.csv` e `importacion_por_marca.csv` separados. La mediana local quedó en 21.000 USD.
4. **Kilometraje**. `parse_specs` y `parse_title` convertían `80,000 km` en 80 km. Se extrajo `parse_number()` con la lógica de separadores ya usada en `parse_price`. El código está aplicado y probado (`80,000` → 80.000); la regeneración final de los outputs se registra al cierre de la tanda.
5. **Marcas**. `config.py` incorporó Land Rover, Jaguar, Infiniti, Acura, BAIC, Daewoo, Opel, Volga, GAC, Bestune, Maxus, SsangYong y VW, con sus alias y tiers (premium/medio), para reducir los 442 anuncios en tier “desconocido”.

Además se reconcilió la encuesta: el cruce filtra ahora `interes=1`, dando **28 interesados** (14 eléctrico, 10 combustión, 4 híbrido) en lugar de los 29 que contaba el script anterior; `PRODUCTOS_VS_GUSTOS.md` tiene precios y propulsiones corregidos (`friday-ev`/`sky-ev` ya figuran como eléctricos). Se actualizó la identidad del proyecto en README, informe, storytelling (cuarta fuerza “expectativas”) y NECESIDADES, y se corrigieron las rutas de 11 unidades systemd.

**EN.** Executed a one-by-one improvement batch without deleting files: deduplicated `autos` to 744 unique cars, regenerated the analysis, repaired marketplace prices and titles (1,973 listings split into 1,301 local and 672 imported), fixed kilometre parsing, expanded brand configuration, reconciled the survey to 28 interested respondents, and updated documentation and systemd paths.

---

## 52. Ampliación de fuentes de datos (20/11/2026)

Se amplió la búsqueda de fuentes más allá de los repositorios y portales ya integrados, con prioridad en fuentes oficiales, compraventa, concesionarios, divisas y datos abiertos. El resultado está en `Data/fuentes-adicionales-2026-11-20.md`: **25 fuentes** verificadas, organizadas por tipo con URL, datos expuestos, viabilidad de scraping y aporte al proyecto.

Las cinco más valiosas son:

1. **API de tasas del Banco Central de Cuba** (`https://api.bc.gob.cu/v1/tasas-de-cambio/activas`): JSON diario con fecha embebida, útil como referencia oficial contrastada. La conversión del proyecto sigue usando la **TRMI informal** de elTOQUE (930 CUP/USD, fijada el 18/11/2026 en `config.py`), nunca la oficial; la serie diaria de `trmi_USD.csv` se conserva como referencia histórica.
2. **Gaceta Oficial No. 65/2026** (paquete Decreto 163 y Resoluciones 171–175): valores referenciales, impuestos y tarifas que explican la brecha entre precio anunciado y precio final.
3. **ONEI, Anuario Estadístico 2025, capítulo 13**: serie oficial más reciente de transporte y parque automotor, ausente hasta ahora en la base.
4. **Womy** (`https://womy.cu/cars/`): catálogo web vivo de Toyota y Lexus con precios en EUR y scraping trivial; ya existía una tabla `cat_womy` en el repo de referencias.
5. **Clasificados.st y TecnoTáctil**: el primero aporta 1.623 anuncios con paginación simple (frescura baja, útil como serie histórica) y el segundo histórico de precios de Revolico, Porlalivre y Ofertas.cu.

**Hallazgo normativo crítico:** la **Resolución 312/2026 de la Aduana General fue derogada por la Resolución 340/2026**. Se actualizaron las referencias en `README.md`, en este informe y en `Data/verificacion-marketplaces-tiendas-organismos-2026-11-16.md` para conservar la trazabilidad sin citar 312 como norma vigente.

También se descartaron fuentes sin valor verificable: `cubamotor.com` (dominio estacionado), agregadores de divisas con cifras contradictorias, datasets genéricos de Kaggle/UCI, Marketplace de Facebook (login obligatorio) y MININT/Dirección de Tránsito (sin estadísticas públicas de matriculaciones).

**EN.** Expanded source discovery to 25 verified sources, prioritizing official data, classifieds, dealers, FX and open data. Top additions: BCC rates API, Gaceta Oficial 2026, ONEI 2025, Womy, and Clasificados.st/TecnoTáctil. Critical finding: Customs Resolution 312/2026 was repealed by Resolution 340/2026; references were updated.

---

## 53. Descarga completa de los anuarios del ONEI (20/11/2026)

A partir del índice oficial `http://www.onei.gob.cu/cuba` se recorrieron las 12 páginas de anuarios disponibles (2014–2025) y se descargaron **todos los documentos enlazados**: 111 PDF, 7 RAR y 103 archivos Excel extraídos, unos 311 MB en total. El inventario está en `Data/fuentes-oficiales/ONEI/README.md` y, con URL, tamaño y SHA-256 por archivo, en el `INDICE.md` de cada año.

La estructura es `Anuario_Estadistico_AAAA/{PDF,Archivo,Excel}/`. Los años 2014–2016, 2018 y 2019 solo publican un PDF íntegro; 2020–2025 publican capítulos en PDF más un RAR de cuadros. Los RAR se extrajeron y se conservaron sin modificar. Los 117 enlaces de documento encontrados se descargaron todos; solo se omitieron CSS y favicon. La validación por tipo MIME dio 0 archivos sospechosos.

Para el proyecto, la serie más útil es el capítulo 13 (Transporte y Seguridad Vial), que permite incorporar parque automotor, matriculaciones y accidentes con series oficiales 2014–2025, hoy ausentes del análisis.

**EN.** Downloaded every document linked from all 12 ONEI statistical yearbooks (2014–2025): 111 PDFs, 7 RAR archives and 103 extracted Excel files (~311 MB), organised per year with checksums and source URLs.

---

## 54. Base de datos distribuida en chunks (20/11/2026)

`Data/Revolico/revolico.sqlite` (849.465.344 bytes) se dividió en **82 chunks de 10 MB** en `Data/Revolico/chunks/`, con un `MANIFEST.json` que guarda el SHA-256 del archivo completo, el orden, el offset y el hash de cada fragmento. La verificación de los 82 chunks dio OK.

Se añadió `Auxiliares/herramientas/db_chunks.py` con tres comandos (`split`, `verify`, `assemble`); la reconstrucción valida todos los hashes antes de escribir y no reemplaza un archivo existente salvo `--force`. `.gitattributes` gestiona los `.bin` con Git LFS. `config.py` expone `REVOLICO_CHUNKS`, `REVOLICO_MANIFEST` y `DB_CHUNKS_TOOL`, y `scripts/01_ingest.py` reconstruye la base desde los chunks si el SQLite no existe. El archivo original se conserva en el árbol de trabajo.

El objetivo operativo es que una subida interrumpida no pierda todo el progreso: con fragmentos de 10 MB solo se reintenta el chunk en curso. Como el historial de `main` referencia aún el objeto LFS de 804 MB, los chunks se publican en la rama huérfana `chunked-db`, sin ese objeto en su historia; `main` queda intacto hasta decidir su sustitución.

**EN.** Split the 811 MiB Revolico database into 82 verified 10 MB chunks with a SHA-256 manifest, added split/verify/assemble tooling, adapted config and ingest to rebuild the DB automatically, and prepared a chunk-only orphan branch for resumable uploads.

---

## 55. Auditoría de fuentes, README y verificación final (23/11/2026)

Se consultaron **15 fuentes web** (8 marketplaces, 7 fuentes oficiales y complementarias): 14 respondieron HTTP 200 y elTOQUE no respondió desde este entorno. Las fechas más recientes en las bases son 17–18/11/2026. El detalle está en `Data/auditoria-fuentes-2026-11-23.md`, generado por `Auxiliares/herramientas/auditar_fuentes.py` con datos calculados en cada ejecución. Las 8 semillas de marketplaces también se descargaron y se contaron sus enlaces de anuncio en `Data/auditoria-fuentes-contenido.md`; todas seguían publicando listados.

Se revisaron los 33 repositorios auxiliares. De los **7 cubanos**, solo `AutosxCuba` tiene ref remoto atrasada (24 commits), pero los 7 tienen cambios locales sin commitear; no se hizo `pull` para no sobrescribir trabajo. Se encontraron dos repos nuevos por la API de GitHub: `danielzamoramato/CubAutos` y `gtrcubautos-blip/GTR-CUBAUTOS-R.S.L`, ambos de baja señal.

Se reescribió `README.md` como página de entrada: descripción de una frase, quickstart ejecutable, estructura, tabla de fuentes, configuración, enlaces por tipo de documento y marco legal. Se añadió `requirements.txt` y un entorno `Auxiliares/.venv-py` funcional. Las skills `technical-writing`, `readme-writing`, `diataxis-docs`, `marketing-copy` y `pptx` quedaron instaladas y activas para redacción y presentación.

La verificación del código detectó un `NameError` en `scripts/01_ingest.py` (`cfg` usado antes de importarse); se corrigió y se revalidó la importación y las funciones `parse_price`/`parse_number`. El informe de debug fue revisado y sus observaciones sobre afirmaciones no calculadas se aplicaron al generador de la auditoría.

**EN.** Audited 15 web sources (14 HTTP 200), reviewed 33 auxiliary repos (7 Cuban, 1 with stale remote ref but all with local changes), rewrote the README to current standards, added a working environment and writing/presentation skills, and fixed a real import-order bug found during verification.

---

## 56. Análisis de los anuarios y estructura de GitHub (23/11/2026)

Se revisaron los 12 anuarios del ONEI y sus 233 archivos. Las series útiles se extrajeron en `Data/fuentes-oficiales/ONEI/series_oficiales.csv` y se interpretan en `ANALISIS_DATO.md`: el transporte de pasajeros cayó un 59 % entre 2019 y 2025 y el ómnibus un 71 %; los accidentes bajaron pero la gravedad aumentó (9,9 fallecidos por cada 100 accidentes en 2025). **No hay series de parque automotor ni de matriculaciones**, por lo que esa laguna signalada en `NECESIDADES.md` no se resuelve con los anuarios; la corrección quedó registrada.

Se documentó además la estructura versionada en `Data/estructura_github.md`: 1.288 archivos, 157 objetos LFS, distribuidos en `Data` (836), `Hombros` (280), `Auxiliares` (110) y `Anexos` (56), con el detalle de extensiones por carpeta y la lista de repositorios no versionados.

**EN.** Analysed all 12 ONEI yearbooks: extracted passenger and road-safety series, confirmed no vehicle-fleet or registration data exists in them, and documented the GitHub tree (1,288 files, 157 LFS objects) with formats per directory.

---

## 57. Reclassificación de páginas y novedades detectadas (23/11/2026)

Se volvieron a descargar las dos primeras páginas de los 8 marketplaces y se compararon sus enlaces con las BDs, normalizando `www.`, query, Unicode NFC y barras finales. Resultado: 7 fuentes sin enlaces nuevos; **iTENCEL mostró 10 anuncios nuevos** (`gmc-sierra-2022-add`, `honda-acord-2025-add`, entre otros), tras descartar una página de agrupación falsa. El detalle está en `Data/novedades-fuentes-2026-11-23.md`, generado por `revisar_novedades.py` sin modificar las bases. El informe de debug fue revisado y sus correcciones aplicadas.

**EN.** Re-fetched the first two listing pages of all 8 marketplaces and compared normalized URLs against the stored databases: 7 sources had no new links, iTENCEL had 10 uncaptured ads after filtering one aggregation page. No database was modified.

---

## 58. Incorporación de anuncios nuevos de iTENCEL (23/11/2026)

Se scrapearon e insertaron los 10 anuncios detectados en la reclasificación: GMC Sierra 2022, Honda Accord 2025, Hyundai Santa Cruz 2022, Hyundai Santa Fe 2024, Kia Forte GT Line 2020, Maxus G10 2015, Mercedes Sprinter 211 2020, Nissan Titan 2017, Sonata 2021 SEL y Van Nissan 2020. Se hizo copia de seguridad de `itencel.sqlite` antes de escribir (`itencel.sqlite.bak-20261123`), se canonizaron las URLs con barra final para no duplicar y se reparó un título de interfaz usando el JSON-LD.

La BD pasó de 951 a **961 anuncios** (961 URLs únicas, `integrity_check=ok`). El pipeline se regeneró con el entorno `Auxiliares/.venv-py` (añadido `pyarrow` a `requirements.txt`): **2.014 anuncios limpios**, de ellos 1.323 locales y 691 de importación; mediana local 21.000 USD y mediana de kilometraje 44.125 km. Se dejó listo el terreno para volver a trabajar con Revolico.

**EN.** Scraped and inserted 10 new iTENCEL ads after backing up the database and canonicalizing URLs; the database has 961 unique ads and the regenerated analysis has 2,014 clean listings (1,323 local + 691 imported).

---

## 59. Storytelling alineado con los datos finales (23/11/2026)

Se actualizó `PRESENTACION_STORYTELLING.md` con la narrativa vigente, conservando la voz y la estructura originales. El relato ahora usa **772 autos únicos**, **2.029 anuncios limpios** (1.338 locales y 691 de importación), mediana local de **21.000 USD**, kilometraje mediano de **43.000 km**, 50 marcas, 101 grupos comparables y 81 anomalías (corrida vigente del 27/11/2026; los valores se actualizan solos en `outputs/tables/kpis.csv`). La caída del transporte de pasajeros según el ONEI y los diez anuncios nuevos de iTENCEL entraron en la historia sin convertirla en una explicación técnica.

La depreciación se reformuló con honestidad: el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra. El modelo con todos los términos dispone de **<!-- kpi:modelo_n_completo -->28 observaciones completas** de <!-- kpi:modelo_candidatas -->981 candidatas (R² = <!-- kpi:modelo_r2_completo -->0,277; p del F = <!-- kpi:modelo_pf_completo -->0,411), límite que se registra explícitamente en `MODELOS_Y_FUNCIONES.md`. Se aplicaron las skills de marketing y SEO para cifras concretas y enlaces internos, y las de voz propia y edición quirúrgica para preservar el estilo del autor. Se añadió además un **apéndice visual** con cinco cuadros y seis gráficos reales; el texto solo deja referencias discretas entre paréntesis, de modo que las tablas y figuras puedan insertarse sin romper la narrativa.

**EN.** Updated the storytelling to the final dataset while preserving the author's voice: 744 unique cars, 2,014 clean listings, 21,000 USD median and a statistically honest depreciation narrative.

---

## 60. Inventario de funciones y modelos (23/11/2026)

Se documentó en `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md` cada transformación y cada estimación del pipeline, con su justificación: normalización sintáctica y TRMI, features derivados, mediana y cuartiles, modelo hedónico log-lineal, VIF, Kruskal-Wallis, Welch t-test y detección de anomalías. El respaldo es metodológico y empírico: se explica por qué cada forma encaja con datos asimétricos y por qué la corrida actual **no** sostiene una tasa de depreciación ni una prima premium significativa (p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05).

**EN.** Documented every function and statistical model in the pipeline with its rationale and current evidence, including the honest non-significance of the hedonic OLS coefficients.

---

## 61. Sitio MkDocs del proyecto (23/11/2026)

Se montó un sitio de documentación con MkDocs Material cuya fuente es `docs/`, generada desde los Markdown y CSV vigentes por `Auxiliares/herramientas/generar_sitio_mkdocs.py`. La navegación sigue Diátaxis: **Historia** (9 secciones del storytelling más introducción y apéndice visual), **Referencia** (funciones y modelos, KPIs e informe técnico), **Cómo** (regeneración del análisis y del sitio) y **Fuentes** (auditoría, anuarios y estructura de GitHub).

Los seis gráficos Plotly se copian a `docs/graficos/` y se enlazan desde el apéndice; las tablas del apéndice y la página de KPIs se generan desde los CSV. `mkdocs build --strict` termina sin errores ni enlaces rotos. `site/` queda ignorado por Git y `mkdocs.yml` contiene la configuración.

**EN.** Built a MkDocs Material site generated from the project's Markdown and CSV: storytelling split by section, visual appendix, model reference, how-to guide and sources. Strict build passes with no broken links.

---

## 62. Factibilidad del timelapse eléctrico (23/11/2026)

Se verificó que el canal público de Telegram de la Empresa Eléctrica de La Habana (`t.me/s/EmpresaElectricaDeLaHabana`) responde HTTP 200 y publica mensajes fechados el 23/11/2026. El APK de `Circuitos Habana` ya documenta la paginación por `?before=`, el filtro por palabras clave y la conversión UTC+1. Del APK se extrajeron 2.473 puntos, 244 circuitos y 166 polígonos de zonas a `Data/mapas/circuitos/`. El plan de captura, parseo, mapa temporal y límites está en `Data/mapas/TIMELAPSE_CIRCUITOS.md`. Se implementó además `Auxiliares/herramientas/scraper_circuitos.py`: en su primera corrida real capturó 40 mensajes, deduplicó por ID y dejó 35 circuitos sin luz, 23 mixtos y 2 con luz en `Data/mapas/circuitos_estado.sqlite`. Un informe de debug corrigió tres fallos (fecha local, filtro de relevancia y palabras de afectación) y las filas existentes se migraron sin borrarse.

**EN.** Confirmed the public Telegram channel is accessible and extracted circuit geometry from the existing APK; documented a feasible capture-and-timelapse architecture with its history and rate-limit caveats.

---

## 63. Calidad del storytelling como puerta de entrada (23/11/2026)

Se revisó el relato como introducción para visitantes nuevos. El contenido es sólido, pero antes de la revisión tenía fricción inicial (metadatos antes de la promesa), un H2 genérico, el dato fuerte enterrado y ninguna llamada a la acción. Se aplicaron correcciones quirúrgicas: titular centrado en «cuánto cuesta un carro en Cuba en 2026», gancho de tres datos al inicio, enlaces de entrada y CTA de retorno al cierre; se corrigió además un carácter cirílico en «largo».

La estimación de retención (`Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md`) es **inferencia de diseño, no medición**: de cada 100 visitantes, ~58 leerían el primer párrafo, ~16 llegarían al cierre y ~5 volverían con intención de consulta. Con promesa, CTA y artefacto actualizable, la proyección condicionada es ~22–25 finalizaciones y ~18–22 retornos. Se documentaron cinco acciones de alcance y tres de retorno, con métricas.

**EN.** Audited the storytelling as a landing narrative, applied surgical fixes and documented an explicit, non-measured retention estimate plus reach and return actions.

---

## 64. Automatización hacia una fuente auditable a dos años (23/11/2026)

Se diseñó `Data/AUTOMATIZACION.md`: tres carriles desacoplados (recolectar, procesar, publicar), periodicidad realista en UTC, idempotencia por clave de fuente, marcas de agua, escrituras atómicas, cuarentena de datos inválidos, `SALUD.md` como dead-man's switch y manifiestos con hashes para reconstruir qué se sabía en cualquier fecha. Ya se activó `linger` y se detuvo el servicio `push-final` que reiniciaba 8 veces sin progreso. Queda implementar los timers `precio-*` y el envoltorio `run_step.sh` por fases.

**EN.** Designed a phased, idempotent automation architecture with health checks and immutable manifests so the project remains auditable two years later; enabled linger and stopped a runaway push service.

---

## 65. Automatización operativa y coste de red (23/11/2026)

Se activaron cinco timers `precio-*` (circuitos, calidad, salud, análisis y sitio) con `Linger=yes`, envoltorio `run_step.sh` con `flock` y estado atómico, validación con cuarentena y `SALUD.md`. Un informe de debug confirmó dos fallos latentes y ya están corregidos: `salud.py` ahora distingue `SIN DATOS` de `STALE` (antes generaba 10 alertas falsas) y el capturador escribe el ETag solo después del `commit` en SQLite (antes un 304 podía saltarse mensajes si una corrida moría a mitad de paginación). También se cerró el descriptor del `flock` en los hijos. Estimación de red: **5–10 MB/mes** si no hay cambios y **50–90 MB/mes** con novedades. Sin internet no se puede scrapear, pero sí ejecutar sin presencia del usuario; si falla la red, `SALUD.md` marca el periodo perdido y el siguiente ciclo `Persistent=true` lo recupera.

**EN.** Activated five unattended timers with locking, atomic state, validation and health reporting; added conditional HTTP requests to minimize bandwidth (estimated 5–10 MB/month idle, 50–90 MB/month with changes).

---

## 66. Extracción continua de Revolico y arquitectura de datos (23/11/2026)

Se activó `precio-revolico.timer` cada 10 minutos con `--max-pages 3`, 2 descargadores, 2 procesadores y lotes de 50, sin `git push`. El job usa `flock` y un timeout de 45 min con 5 min de margen frente al de systemd. El primer debug reveló que 3.351 enlaces `es_auto_candidato=0` quedaban `pending` para siempre: se marcan `rechazado` y se excluyen del conteo de salida; se añadió `SIGTERM → STOP` para que el cierre guarde lote, snapshot y partes. En la primera corrida corregida los anuncios `done` pasaron de 6.783 a 6.955.

Se documentó la arquitectura de procesamiento en `ARQUITECTURA_DATOS.md`: Parquet particionado por `year/month`, watermark, rollups mensuales y evaluación de DuckDB/Polars/Arrow. En esta CPU `import duckdb` falla con `SIGILL`, así que la Fase 1 se hará con pyarrow/pandas, ya disponibles.

**EN.** Enabled a 10-minute Revolico capture job with locking and graceful shutdown, fixed an unreachable exit condition in the pipeline, and documented a phased storage architecture (partitioned Parquet + watermarks + monthly rollups); DuckDB is blocked by a CPU SIGILL.

---

## 67. Optimización de espacio (23/11/2026)

Con autorización explícita se quitaron: el entorno de Python antiguo e inservible (1,7 GB), dos versiones viejas de archivos grandes que ya no se usaban (1,7 GB), la copia de seguridad de iTENCEL creada durante la inserción (53 MB), los restos de sesión de WhatsApp (56 MB) y 10 archivos repetidos (66 MB). Las leyes y las herramientas de scraping **no se borraron**: se mudaron a `~/Utilidades/Leyes` y `~/Utilidades/HerramientasScraping`. El repositorio pasó de 20 GB a 10 GB.

**EN.** With explicit authorization, removed a broken Python environment, old file copies, a temporary database backup, browser session data and duplicate files; moved laws and scraping tools to ~/Utilidades. Repository size dropped from 20 GB to 10 GB.

---

## 68. Peso en GitHub y mapa de espacio (23/11/2026)

La API de GitHub reporta **205.002 KB (0,20 GB)** para el historial normal; los archivos grandes se guardan aparte y su consumo en GitHub no lo expone la API. En local, esa copia ocupa 3,3 GB con 174 archivos. El mapa completo y los candidatos a optimizar están en `Data/ESTRUCTURA_ESPACIO.md`: las tres copias partidas de Revolico (2,1 GB), el historial normal (1,0 GB), bibliotecas quizá innecesarias (66 MB de DuckDB, que además falla en esta CPU), repos de referencia (606 MB) y documentos descargados (261 MB).

**EN.** GitHub reports 0.20 GB for Git history; large-file storage is not exposed by the API (3.3 GB locally). Documented a plain-language space map and optimization candidates.

---

---

## 69. Declaración de uso de inteligencia artificial / AI-use declaration

**ES.** Las herramientas de inteligencia artificial (OpenCode/Claude Code con las skills `review` de MatCom, `deep-research` y `technical-writing`) se utilizaron en cuatro fases: investigación y verificación de fuentes, redacción y edición de la narrativa, generación y revisión de código, y traducción bilingüe. El protocolo de supervisión consiste en contrastar toda cifra contra los CSV y bases versionados, ejecutar las pruebas automatizadas y conservar el registro de auditoría en `reviews/`; ninguna salida de IA se aceptó sin ese contraste. Las cifras, los modelos estadísticos y las decisiones de diseño provienen de los datos y del código versionados en este repositorio; ninguna afirmación empírica se originó en una salida de IA sin contraste contra los archivos. La auditoría completa de este documento se realizó con la skill `review` de MatCom y sus resultados se conservan en `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` junto con los trece artefactos de fase.

**EN.** AI tools (OpenCode/Claude Code with MatCom's `review` skill, `deep-research` and `technical-writing`) were used in four phases: research and source verification, drafting and editing, code generation and review, and bilingual translation. The supervision protocol requires every figure to be checked against versioned CSVs and databases, the automated tests to be run, and the audit trail to be kept under `reviews/`; no AI output was accepted without that verification. All figures, statistical models and design decisions derive from the data and code versioned in this repository; no empirical claim was taken from an AI output without verification against the files. The full audit was carried out with MatCom's `review` skill and is preserved in `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` together with thirteen phase artifacts.

---

## 70. Referencias verificadas / Verified references

**ES.** Referencias citadas y verificadas externamente durante la auditoría: Akerlof (1970), *The Market for "Lemons"* (DOI 10.2307/1879431 confirmado en OpenAlex; el resumen indexado es solo un índice de secciones, por lo que su flag es `(metadata incomplete: resumen)`); UK Department for Transport / DVLA, estadísticas de vehículos (GOV.UK); ANFAC, informes del sector automotriz español (sitio oficial); AEADE, estadísticas de matriculaciones (sitio oficial). Las fuentes restantes figuran con estado `(metadata incomplete)` en `reviews/informe-tecnico-2026-11-27.e2-literature.md` y no se presentan como referencias verificadas. La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`; la correspondencia entre afirmación y fuente se documenta en el expediente forense.

**EN.** Externally verified references cited during the audit: Akerlof (1970), *The Market for "Lemons"* (Crossref/OpenAlex); UK Department for Transport / DVLA vehicle statistics (GOV.UK); ANFAC Spanish automotive reports (official site); AEADE registration statistics (official site). Remaining sources are marked `(metadata incomplete)` in `reviews/informe-tecnico-2026-11-27.e2-literature.md` and are not presented as verified references. A numbered list of 38 references and their verification status is available in `Data/referencias.md`; claim-to-source correspondence is documented in the forensic assembly.

---

---

## 71. Cumplimiento de estándares de nivel master / Master-level standards

### 71.1 Bases de comparación / Baselines

| Base / Baseline | Descripción | Métrica observada |
|---|---|---|
| Mediana global ( ingenua ) | Predice la mediana de los usados locales | MAE 18.220,46 USD sobre 1.444 anuncios |
| Egyptian-Used-Cars | Referencia de ingeniería del campo: 23.500 anuncios y series mensuales | Contraste cualitativo de cobertura y frescura |
| Modelo principal propio | OLS de log-precio con antigüedad, km, condición y tier | R² 0,101 sobre 584 observaciones |

**EN.** Baseline 1 is the naive global median (MAE 18,220.46 USD on 1,444 listings); baseline 2 is the Egyptian-Used-Cars engineering reference (23,500 listings, monthly series); the local principal model is reported alongside both.

### 71.2 Ablación explícita / Explicit ablation

`modelo_muestra.csv` documenta la ablación del término `hp`: al retirarlo, la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² baja de 0,274 a 0,101. El cambio de especificación y el cambio de muestra se informan juntos. La pendiente positiva de antigüedad en el modelo principal se atribuye a la selección de anuncios con kilometraje declarado y no se interpreta como una tasa de depreciación.

**EN.** Removing `hp` changes the sample from 28 to 584 observations and R² from 0.274 to 0.101; both changes are reported together. The positive age slope in the principal model is attributed to selection into the mileage-reported subsample, not to a depreciation rate.

### 71.3 Pruebas y tamaño muestral / Tests and sample size

No hay diseño pareado: los anuncios son observaciones independientes, por lo que no se aplican Wilcoxon de pares ni t de diferencias; se usan Kruskal-Wallis y Welch para grupos independientes. El tamaño se mide en anuncios (981 candidatas de 8 marketplaces), no en ensayos experimentales.

### 71.4 Amenazas a la validez / Threats to validity

- **Externa:** solo La Habana y anuncios en línea; los precios son pedidos, no transaccionados.
- **De constructo:** kilometraje y potencia faltan en la mayoría de los anuncios; la condición se infiere del texto.
- **Interna:** no hay asignación aleatoria; la ablación es observacional.
- **Estadística conclusiva:** el modelo completo usa 28 observaciones y ningún coeficiente alcanza p < 0,05; el principal tiene mejor cobertura pero su signo de antigüedad refleja selección.

### 71.5 Protocolo, semillas y reproducción / Protocol, seeds and reproduction

La semilla `SEED = 20261127` está declarada en `run_all.py` y en este documento. Comando único: `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py`. Puntos de entrada con argumentos: `generar_dashboard.py --solo-si-cambia`, `exportar_parquet_compacto.py --tablas ...`, `db_chunks.py split|verify|assemble` y `generar_sitio_mkdocs.py`. Las dependencias están fijadas a serie menor en `requirements.txt`. Prueba de humo: `python3 Auxiliares/herramientas/test_smoke_pipeline.py`.

### 71.6 Posicionamiento frente a trabajos cercanos / Positioning against prior work

Frente a Gegić, Isaković, Keco, Mašetić y Kevrić (2019), que predicen precios con machine learning sobre catálogos estructurados, este trabajo parte de anuncios en lenguaje libre y construye las variables por análisis del texto: la contribución es de procedencia y normalización, no de algoritmo. Frente a Muça, Bani y Alla (2026), que integran datos públicos empresariales albaneses mediante scraping, el énfasis aquí es la conversión con TRMI fechada y la auditoría de procedencia, no el pipeline de integración. Frente a Du, Yang, Zhang, Li y Liu (2026), que modelan depreciación no lineal y heterogeneidad de marca con evaluación fuera de muestra, este trabajo no estima una tasa anual: reporta la no significancia de los coeficientes y la pérdida de muestra como hallazgo. Frente a Vidal Alejandro, Muñiz-Cuza y Calas Torres (2024), que estudian el mercado informal de divisas en Cuba, la tasa informal se usa aquí como convención de conversión fechada, no como objeto de estudio.

**Firma / Signature:** responsable del proyecto / project owner.  
**Última actualización / Last update:** 27/11/2026.

---
type: audit-artifact
phase: e3-artifacts
slug: informe-tecnico-2026-11-27
generated_at: 2026-11-27T05:30:54Z
repo_url: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba
repo_clone_status: not-attempted
language: es
---

# Artifact Inventory

Repository: not-declared / not-cloned (no local `repo_path` was supplied for this extraction; §40 declares the remote repository `CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba`, reproduced in frontmatter but not cloned or verified here). All entries below are document-level observations only.

## Datasets

| Name | Source | ID | Publicly accessible | Notes |
|---|---|---|---|---|
| Revolico scraped ads database | custom (own scrape) | `Data/Revolico/revolico.sqlite` | unknown | §54 reports 849,465,344 bytes split into 82 chunks; §66 reports 6,955 `done` ads; §14 states it is not versioned as a single file. |
| Revolico pipeline queues | custom | `Data/Revolico/pipeline.sqlite` | unknown | §16 defines `url_queue`, `download_queue`, `process_queue`; §30 gives ~117 MB; §24 lists pending items from an interrupted run. |
| Dealer and marketplace catalogues | custom | `Data/catalogos_concesionarios/` (per-store `.sqlite`) | unknown | §9 reports 11 prepared databases and 256 rows; §30 places them under Git LFS. |
| Telegram public-channel database | custom | `Data/integraciones/telegram/telegram.sqlite` | unknown | §29: tables `canales` (119), `anuncios` (54), `estado`; §30 places it under Git LFS. |
| ONEI statistical yearbooks 2014–2025 | official/government (ONEI Cuba) | `Data/fuentes-oficiales/ONEI/` | yes | §53: 111 PDF, 7 RAR, 103 extracted Excel files (~311 MB) downloaded from `onei.gob.cu`, with URL, size and SHA-256 per file in `INDICE.md`. §56 reports 233 files. |
| UK DfT/DVLA vehicle licensing statistics | official/government | `gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files` | yes | §18: verified live, updated 23/09/2026, Open Government Licence. |
| VAHAN (India, MoRTH) | official/government | `vahan-india-automotive-market-2025` | no | §18: «No accesible desde este entorno (error de transporte)»; the repo documents 12 monthly exports for 2025. |
| BCC exchange rates | official/government | `https://api.bc.gob.cu/v1/tasas-de-cambio/activas` | no | §52 declares the daily JSON API; §18 records «No accesible en vivo desde este entorno». |
| elTOQUE TRMI | non-official (independent media) | `Anexos/Investigacion Cambios/trmi_USD.csv` | unknown | §23 uses its daily TRMI for CUP conversion; §55 records «elTOQUE no respondió desde este entorno». |
| CarDekho (Kaggle) | Kaggle | not declared in the document | unknown | §18: marketplace/advertised price signal, not official statistics; requires dedup and bias declaration. |
| UCI Automobile | UCI | not declared in the document | unknown | §18: academic/synthetic, methodological reference only, never real Cuban prices. |
| PUCE used-vehicle study survey | academic | `Hombros/01_PDFs/Análisis del mercado de vehículos usados y su comercialización en el__73e1773e.pdf` | unknown | §17: survey of 130 merchants; source of the ≤5-year quality classification. |
| Consolidated reference-repository tables | custom (derived) | `Data/repos-autos-referencias/referencias_autos.sqlite` | unknown | §50: 25 tables including 3,958 Revolico ads, 33 survey responses, 30+30+8 interviews and a `provenancia` table. |
| Fuel price series | custom | `Data/combustible/precios_combustible.sqlite` | unknown | §41: 18 observations between 20/08/2026 and 18/11/2026, official CIMEX / informal elToque / published prices kept separate. |
| OSM/Overpass geodata | custom (OpenStreetMap) | `Data/mapas/gasolineras.csv` | yes | §41: 137 Havana fuel stations; §42 folds them into `Data/mapas/mapa_elementos.sqlite`. |
| EV charging references | marketplace/directory | `Data/mapas/estaciones_carga.csv` | unknown | §41: 12 references (9 from Kargalaya with coordinates, 3 from Electromaps without coordinates). |
| Circuitos Habana APK extracts | custom (APK decompilation) | `Data/mapas/circuitos/` | unknown | §62: 2,473 points, 244 circuits and 166 polygons extracted; plan in `TIMELAPSE_CIRCUITOS.md`. |

## Tables

Tables: none-detected (no numbered `Tabla N` / `Table N` captions occur in the document). The unnumbered Markdown tables actually present are inventoried below; captions are taken verbatim from the header row. Page numbers are unavailable in the text-only cache.

### Table (unnumbered) — «Fase | Nombre | Estado» (§2, ES)
- **Section**: §2 Estado y fases (p. n/a)
- **Lines**: 24–34
- **Columns**: Fase, Nombre, Estado
- **Rows**: 9
- **Claims supported** (preliminary): phase status; active phase 6, phases 7–9 pending. No claim IDs occur in the document.

### Table (unnumbered) — «Búsqueda | Páginas | Resultados | Útiles | Parada» (§7, ES)
- **Section**: §7 Fase 4 — Corpus documental (p. n/a)
- **Lines**: 78–82
- **Columns**: Búsqueda, Páginas, Resultados, Útiles, Parada
- **Rows**: 3
- **Claims supported** (preliminary): search effort and the 10-page stopping rule.

### Table (unnumbered) — «Tienda | Filas | Con precio» (§9, ES)
- **Section**: §9 Fase 6 — Scraping y captura (p. n/a)
- **Lines**: 94–106
- **Columns**: Tienda, Filas, Con precio
- **Rows**: 11
- **Claims supported** (preliminary): «11 bases» and «256 filas»; price density per store.

### Table (unnumbered) — «Problema | Solución» (§11, ES)
- **Section**: §11 Problemas y soluciones (p. n/a)
- **Lines**: 122–129
- **Columns**: Problema, Solución
- **Rows**: 6
- **Claims supported** (preliminary): CAPTCHA, HTTP 202/429, anti-bot and dedup handling.

### Table (unnumbered) — «Phase | Name | Status» (§2, EN)
- **Section**: §2 Status and phases (p. n/a)
- **Lines**: 153–163
- **Columns**: Phase, Name, Status
- **Rows**: 9
- **Claims supported** (preliminary): English parallel of the phase-status table.

### Table (unnumbered) — «Search | Pages | Results | Useful | Stopped at» (§7, EN)
- **Section**: §7 Phase 4 — Document corpus and research (p. n/a)
- **Lines**: 207–211
- **Columns**: Search, Pages, Results, Useful, Stopped at
- **Rows**: 3
- **Claims supported** (preliminary): English parallel of the search-effort table.

### Table (unnumbered) — «Store | Rows | With price» (§9, EN)
- **Section**: §9 Phase 6 — Scraping and capture (p. n/a)
- **Lines**: 223–235
- **Columns**: Store, Rows, With price
- **Rows**: 11
- **Claims supported** (preliminary): English parallel of the per-store row counts.

### Table (unnumbered) — «Problem | Solution» (§11, EN)
- **Section**: §11 Problems and solutions (p. n/a)
- **Lines**: 251–258
- **Columns**: Problem, Solution
- **Rows**: 6
- **Claims supported** (preliminary): English parallel of the problem/solution table.

### Table (unnumbered) — «Fecha / Date | Ruta / Path | Tipo / Type | Origen / Source | Tamaño / Size | Fase / Phase | Descripción / Description | Estado / Status» (§13)
- **Section**: §13 Registro de altas / Change log (p. n/a)
- **Lines**: 276–748 (marker `<!-- REGISTRO_ALTAS -->` at 278; multiple dated snapshots)
- **Columns**: Fecha/Date, Ruta/Path, Tipo/Type, Origen/Source, Tamaño/Size, Fase/Phase, Descripción/Description, Estado/Status
- **Rows**: varies (line 291 explicitly states «175 entradas adicionales no listadas / omitted»)
- **Claims supported** (preliminary): automatic inventory of added files, sizes and phases; regenerated by `actualizar_informe.py`.

### Table (unnumbered) — «Última ejecución / Last run | Tamaño / Size | Partes / Chunks | SHA-256 (inicio) | Reconstrucción / Rebuild» (§14)
- **Section**: §14 Sincronización automática de Revolico (p. n/a)
- **Lines**: 756–759 (marker `<!-- SYNC_REVOLICO -->` at 758)
- **Columns**: Última ejecución/Last run, Tamaño/Size, Partes/Chunks, SHA-256 (inicio), Reconstrucción/Rebuild
- **Rows**: 1
- **Claims supported** (preliminary): 795,373,568 B, 48 chunks of 16 MiB, truncated SHA-256 prefix.

### Table (unnumbered) — «Fuente | Aporte metodológico | Requerimiento para AutoDecide» (§17)
- **Section**: §17 Guía de análisis de mercado (p. n/a)
- **Lines**: 791–804
- **Columns**: Fuente, Aporte metodológico, Requerimiento para AutoDecide
- **Rows**: 12
- **Claims supported** (preliminary): methodological provenance of Fases 7–8 requirements (PUCE, Chile, spinny, taso-api, etc.).

### Table (unnumbered) — «Fuente | Naturaleza | Verificación | Uso en el análisis» (§18)
- **Section**: §18 Auditoría de procedencia (p. n/a)
- **Lines**: 812–825
- **Columns**: Fuente, Naturaleza, Verificación, Uso en el análisis
- **Rows**: 12
- **Claims supported** (preliminary): source nature, live-verification status and permitted analytical use; distinguishes official/industry context from advertised-price signals.

### Table (unnumbered) — «Tabla | Registros» (§29)
- **Section**: §29 Base de datos de Telegram (p. n/a)
- **Lines**: 960–965
- **Columns**: Tabla, Registros
- **Rows**: 4
- **Claims supported** (preliminary): `canales` 119, 4 with automotive context, `anuncios` 54, 54 marked `es_auto`.

### Table (unnumbered) — «Métrica | Valor» (§34)
- **Section**: §34 Esqueleto de análisis de rentabilidad (p. n/a)
- **Lines**: 1039–1050
- **Columns**: Métrica, Valor
- **Rows**: 10
- **Claims supported** (preliminary): first-run baseline (972 ingested, 499 clean, 376 rejections, 32 brands, 24,000 USD median, −5.43 %/year OLS depreciation).

### Table (unnumbered) — «Tipo | Color | Símbolo» (§42)
- **Section**: §42 Base unificada del mapa (p. n/a)
- **Lines**: 1166–1171
- **Columns**: Tipo, Color, Símbolo
- **Rows**: 4
- **Claims supported** (preliminary): required map layer styling (fuel, charging, dealership, workshop).

## Figures

Figures: none-detected (no numbered `Figura N` / `Figure N` captions occur in the document). Referenced figure artifacts:

### Figure (unnumbered) — eight PNG charts under `Data/analisis/graficos/` (§23, §24)
- **Section**: §23 Conversión elTOQUE, serie temporal y gráficas (p. n/a); §24 (p. n/a)
- **Files named**: `01_histograma_precios.png`, `02_boxplot_marcas.png`, `03_barras_municipios.png`, `04_precios_por_anio.png`, `05_serie_precio_vs_tasa.png`, `06_variaciones_tasa_precio.png`, `07_outliers.png`, `08_cobertura.png`
- **Rendered in document**: no (text-only cache; files named, not embedded)
- **Type**: histogram, boxplot, bar chart, yearly-price plot, time-series plots, outlier and coverage charts
- **Claims supported** (preliminary): price distribution, brand/municipality segmentation, price-vs-rate series, outliers and field coverage.

### Figure (unnumbered) — `Data/analisis/graficos/dashboard_interactivo.html` and `Data/analisis/dashboard.html` (§22, §23)
- **Section**: §22 Análisis descriptivo inicial; §23 (p. n/a)
- **Rendered in document**: no
- **Type**: interactive HTML dashboard
- **Claims supported** (preliminary): descriptive market indicators produced by `analisis_mercado.py`.

### Figure (unnumbered) — six Plotly HTML charts of the profitability pipeline (§34, §59, §61)
- **Section**: §34 (p. n/a), §59 (p. n/a), §61 Sitio MkDocs (p. n/a)
- **Paths named**: `Data/analisis_rentabilidad/outputs/charts/`; copies in `docs/graficos/`; visual appendix with «cinco cuadros y seis gráficos reales»
- **Rendered in document**: no
- **Type**: Plotly HTML charts
- **Claims supported** (preliminary): KPIs, benchmark, hedonic model and anomaly results; appendix references kept discrete in the narrative.

### Figure (unnumbered) — `Data/mapas/mapa_ofline.html` (§36, §41, §42)
- **Section**: §36 Mapa offline, talleres e infraestructura EV; §41; §42 (p. n/a)
- **Rendered in document**: no
- **Type**: offline Plotly map with embedded Plotly and Cuba outline; layers for dealerships, charging stations, fuel stations and workshops
- **Claims supported** (preliminary): geolocated infrastructure counts (§42: 131 fuel stations, 12 charging stations, 25 dealerships with 17 coordinates, 22 workshops).

### Figure (unnumbered) — circuit timelapse assets (§62)
- **Section**: §62 Factibilidad del timelapse eléctrico (p. n/a)
- **Paths named**: `Data/mapas/circuitos/`, `Data/mapas/circuitos_estado.sqlite`, `Data/mapas/TIMELAPSE_CIRCUITOS.md`
- **Rendered in document**: no
- **Type**: geospatial circuit geometry and planned temporal map
- **Claims supported** (preliminary): 2,473 points, 244 circuits, 166 polygons; first scrape produced 35 circuits without power, 23 mixed, 2 with power.

## Missing artifacts

### Full Revolico SQLite file in the main branch
- **Mentioned in document**: §14 (p. n/a): «La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**.»; §54: «`main` queda intacto hasta decidir su sustitución.»
- **Found in repo**: no (no local clone supplied; document-level statement only)
- **Observation**: The document describes the full database as deliberately absent from normal versioning: an earlier 16 MiB chunk scheme (§14) and a later 82-chunk 10 MB scheme with `MANIFEST.json` (§54) are used instead, and the chunks are published on the orphan branch `chunked-db` while `main` still references the ~804 MB LFS object. Git LFS is described in §30 as managing the `.sqlite` files. No single authoritative file is therefore inventoryable from the versioned history described.

### Official Cuban vehicle-fleet and registration series
- **Mentioned in document**: §56 (p. n/a): «**No hay series de parque automotor ni de matriculaciones**, por lo que esa laguna signalada en `NECESIDADES.md` no se resuelve con los anuarios»; §20 lists «estadísticas oficiales cubanas de parque y matriculaciones» among outstanding needs.
- **Found in repo**: no (no local clone supplied; document-level statement only)
- **Observation**: The ONEI yearbooks were downloaded in full (§53), but §56 states that the transport and road-safety series extracted into `series_oficiales.csv` do not include fleet size or registrations. The document records this gap as unresolved and notes the correction was logged, while §52 had earlier presented ONEI chapter 13 as a source that would fill it.

### VAHAN (India) dataset
- **Mentioned in document**: §18 (p. n/a): «No accesible desde este entorno (error de transporte)»; the row classifies it as official MoRTH data with 12 monthly 2025 exports.
- **Found in repo**: no (no local clone supplied; document-level statement only)
- **Observation**: The dataset is named as a benchmark input for registrations by manufacturer and fuel, but the document records that it could not be retrieved in this environment and that only the repository's own verification manifest was available.

### BCC live exchange-rate endpoint
- **Mentioned in document**: §18 (p. n/a): «No accesible en vivo desde este entorno»; §52 declares `https://api.bc.gob.cu/v1/tasas-de-cambio/activas`.
- **Found in repo**: no (no local clone supplied; document-level statement only)
- **Observation**: The official rate is cited via `Data/investigacion-mercado-automotor-cuba.md` and Resolution 102/2026, but §18 marks live retrieval as unavailable; the project's conversion continues to use the informal elTOQUE TRMI (§23, §52), and §55 records that elTOQUE itself did not respond from this environment in the final audit.

### Full gazette corpus
- **Mentioned in document**: §10 (p. n/a): «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe»; §67 states laws were moved to `~/Utilidades/Leyes`.
- **Found in repo**: no (no local clone supplied; document-level statement only)
- **Observation**: Only named decrees and resolutions (163/2026, 104, 17, 52, 171–175, 340, 102) are cited; the reference index and corpus live outside the project tree after the space-optimization step, so the underlying legal documents are not inventoried here.

### Rendered figures for the descriptive and profitability analyses
- **Mentioned in document**: §23 (p. n/a): «genera 8 PNG + `dashboard_interactivo.html` en `Data/analisis/graficos/`»; §59: «un **apéndice visual** con cinco cuadros y seis gráficos reales».
- **Found in repo**: no (no local clone supplied; paths named in document only)
- **Observation**: The cached document text names the eight PNG files, the interactive dashboards and the six Plotly charts copied to `docs/graficos/`, but embeds none of them. The visual appendix is described as leaving only discrete in-text references so tables and figures can be inserted without breaking the narrative.

### Docker daemon for the Google Maps scraper
- **Mentioned in document**: §36 (p. n/a): «el daemon Docker no arranca sin root en este entorno (`dockerd needs to be started with root privileges`)».
- **Found in repo**: no (no local clone supplied; document-level statement only)
- **Observation**: The `google-maps-scraper` route was discarded; §6 does report FlareSolverr 3.5.2 running in Docker at `http://127.0.0.1:8191/`, so the document records both a working containerized service and an unavailable daemon for a different tool.

### Structured vehicle specifications and real transaction prices
- **Mentioned in document**: §24 (p. n/a): «**No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**»; §20 lists «precios de transacción reales» and «montos de costos ocultos» as outstanding.
- **Found in repo**: no (no local clone supplied; document-level statement only)
- **Observation**: `ad_json` (21 keys) and `apollo_full` (five types plus `ROOT_QUERY`) are stored for all 6,334 ads, but year, km, brand, model, fuel and transmission are derived by regex with 63.5 %, 6.2 % and 68.4 % coverage (§22, §24). §59–§60 further state that the current model does not support a significant annual depreciation slope or a premium brand premium, so the earlier −5.43 %/year and +21 % figures (§34) are not carried into the final narrative.

### `Copias/` reference repositories
- **Mentioned in document**: §3 (p. n/a): «`Copias/` no se registra en este informe por decisión explícita»; §17 cites code from `Copias/AutosxCuba/code/{unir_todo_final,modelo_predictivo,generar_graficos}.py`.
- **Found in repo**: no (excluded by explicit decision; no local clone supplied)
- **Observation**: Four reference repositories are listed in the folder structure but deliberately excluded from the report; nevertheless, §17 and §50 use their code and data as methodological inputs, so those artifacts are cited without being inventoried.

## Declared environment (document-level; not verified in a clone)

- §6 `Auxiliares/.venv`: patchright 1.64.4, PyPasser 1.1.0, Scrapling 0.5.1, ddddocr 1.6.1, playwright 1.65.2, curl_cffi 0.17.0, trafilatura, pandas, numpy, onnxruntime 1.32.0, ddgs 9.16.1, tenacity 9.2.1; system Chromium; FlareSolverr 3.5.2 in Docker at `http://127.0.0.1:8191/` (§42 uses `/v1`).
- §23: matplotlib, seaborn and plotly described as installed for chart generation.
- §25: geopandas 1.2.0, shapely 2.2.0, pyproj, folium 1.0.0, mapclassify, geopy.
- §34: statsmodels 0.15, pyarrow 26, kaleido, nbformat, nbconvert; `duckdb` uninstalled because it raises `Illegal instruction` on this CPU (§66 repeats `SIGILL`).
- §30: Git LFS 3.8.1 installed and enabled; `.gitattributes` marks `*.sqlite`, `*.sqlite-wal`, `*.sqlite-shm` with LFS filters; §54 adds `.bin` handling.
- §55: `requirements.txt` added and a functional `Auxiliares/.venv-py` created; §58 adds `pyarrow` to requirements.
- §61: MkDocs Material site with `mkdocs.yml`; `mkdocs build --strict` reported without errors; `site/` ignored by Git.
- §35: jadx 1.5.6 used to decompile the Circuitos Habana APK.
- §55: skills `technical-writing`, `readme-writing`, `diataxis-docs`, `marketing-copy` and `pptx` described as installed and active.
- systemd units named in the document: `revolico-scrape.timer`, `revolico-git.timer`, `revolico-revisar.service`, `revolico-aviso.timer`, `revolico-backfill.service`, `marketplaces-scrape.service`, `revolico-snapshot`, `progreso-report.timer`, `precio-combustible.timer`, five `precio-*` timers (§65), `revolico-revisar`/`marketplaces-scrape`/`revolico-snapshot` with automatic restart (§37). §64–§65 add `linger`, `run_step.sh` with `flock`, `SALUD.md` and atomic state.
- §40: remote renamed from `CarlosAntonioAceaJimenezCD/autodecide-habana` to `CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba`; the local folder is stated as `~/Proyectos/ICD Automotive Market Project`, while the report header (line 6) states `~/Proyectos/El precio de moverse en Cuba`.

## Code-to-document mapping (when discernible)

Paths below are the locations declared in the document; with no clone available, none were verified on disk.

| Document component | Repo location (document-declared) |
|---|---|
| Revolico scraper / incremental updates | `Auxiliares/herramientas/scrape_revolico.py`, `Auxiliares/herramientas/actualizar_revolico.py`, `Auxiliares/herramientas/actualizar_informe.py` |
| Queue pipeline and early link classification | `Auxiliares/herramientas/scrape_revolico_pipeline.py`, `Auxiliares/herramientas/limpiar_revolico.py` |
| Database reconstruction / chunking | `Auxiliares/herramientas/reconstruir_revolico.py`, `Auxiliares/herramientas/db_chunks.py` |
| Dealer/marketplace scraping | `Auxiliares/herramientas/scrape_concesionarios.py`, `Auxiliares/herramientas/integraciones/fuentes_cubanas/*`, `scrape_marketplaces.py` (§37) |
| Telegram / WhatsApp integrations | `Auxiliares/herramientas/scraper_telegram_publico.py`, `Auxiliares/herramientas/descubrir_canales_telegram.py`, `Auxiliares/herramientas/telegram_db.py`, `Auxiliares/herramientas/integraciones/whatsapp/waha_client.py` |
| Descriptive analysis and charts | `Auxiliares/herramientas/analisis_mercado.py`, `Auxiliares/herramientas/graficos_mercado.py`, `Data/analisis/` |
| Profitability pipeline | `Data/analisis_rentabilidad/config.py`, `scripts/01_ingest.py` … `05_benchmark.py`, `run_all.py`, `sql/analysis.sql` |
| Reference-repo consolidation | `Auxiliares/herramientas/consolidar_repos_autos.py`, `Data/repos-autos-referencias/` |
| Maps and infrastructure | `Auxiliares/herramientas/scrape_infraestructura.py`, `geocode_elementos.py`, `generar_mapa_ofline.py`, `Auxiliares/herramientas/scraper_circuitos.py`, `Data/mapas/` |
| Progress reporting / source audit | `Auxiliares/herramientas/reporte_progreso.py`, `auditar_fuentes.py`, `revisar_novedades.py`, `Data/progreso_reporte.md`, `Data/auditoria-fuentes-2026-11-23.md` |
| Documentation site | `docs/`, `mkdocs.yml`, `Auxiliares/herramientas/generar_sitio_mkdocs.py` |
| Report and changelog generator | `INFORME_TECNICO.md` / `INFORME_TECNICO.pdf`, `README.md`, `Auxiliares/herramientas/actualizar_informe.py` |
| Tests (`test_*.py`, `*_test.py`, `tests/`) | not located (no test files or test framework named in the document) |

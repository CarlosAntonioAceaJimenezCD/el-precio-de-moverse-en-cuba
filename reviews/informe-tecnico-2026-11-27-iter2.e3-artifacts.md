---
type: audit-artifact
phase: e3-artifacts
slug: informe-tecnico-2026-11-27-iter2
generated_at: 2026-11-27T17:15:00-05:00
repo_url: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba
repo_clone_status: success
language: es
---

# Artifact Inventory

Iteración 2. A diferencia de la iteración 1, en esta pasada sí se dispuso del repositorio local (`repo_path` efectivo: `/home/thony70807/Proyectos/El precio de moverse en Cuba`), por lo que la sección Repository se verificó en disco con `git` y `find`. Las path declaradas en el documento se contrastaron con el árbol real; cuando una ruta citada no existe se indica expresamente.

## Repository

- **URL**: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba
- **Clone status**: success (checkout local existente, 190 commits; no se realizó un clonado nuevo)
- **Languages**: Python: 41.689 LOC propias (excluye `.venv*`, `Auxiliares/Repositorios Referencias`, `Copias`, `site`); Markdown: 59.110 LOC en todo el repo, de las cuales 2.456 LOC en `docs/`; HTML: panel autocontenido y 6 gráficos Plotly (ver Figures)
- **Commits**: 190
- **Authors**: CarlosAntonioAceaJimenezCD <CarlosAntonioAceaJimenezCD@users.noreply.github.com>
- **First commit**: 2026-11-17
- **Last commit**: 2026-11-27 (`99c7065 viz: refrescar panel con el ultimo estado de circuitos`)
- **Default branch**: main
- **Git LFS**: 157 objetos referenciados (`*.sqlite`, `*.bin` de chunks) según `.gitattributes`; `Data/PROGRESO_PUSH.md` (20:58 UTC) informa 175 objetos en disco y `origin/main` en `99c7065`

### Structure

```tree
./
├── Anexos/                  # Investigacion Cambios, Investigacion Combustible
├── Auxiliares/              # cache, herramientas (scripts propios), Repositorios Referencias, .venv*
├── Copias/                  # 4 repos de referencia (excluidos por decisión del §3)
├── Data/                    # investigaciones y bases por tienda
│   ├── analisis/            # 8 PNG + dashboards descriptivos
│   ├── analisis_rentabilidad/  # config.py, scripts/, sql/, data/, outputs/{charts,tables}/, *.md
│   ├── Revolico/            # revolico.sqlite, pipeline.sqlite, chunks/, partes/
│   ├── mapas/               # mapa_ofline.html, circuitos/, CSV de infraestructura
│   ├── fuentes-oficiales/   # anuarios ONEI, series_oficiales.csv
│   ├── repos-autos-referencias/  # referencias_autos.sqlite
│   └── dashboard.html       # panel interactivo autocontenido (nuevo en la iteración 2)
├── docs/                    # historia, referencia, guias, fuentes, graficos/, dashboard.html
├── Hombros/                 # 01_PDFs … 06_Calidad_precio_mercado
├── reviews/                 # informe + forensic iteración 1, 13 artefactos de fase, plan iter2
├── site/                    # salida MkDocs (ignorada por Git)
├── INFORME_TECNICO.md / .pdf, README.md, requirements.txt, mkdocs.yml
└── .playground/audit-cache/ # cachés de texto de las iteraciones 26/27 y 27-iter2
```

### Entry points

| Path | LOC | Args documented | Notes |
|---|---|---|---|
| `Data/analisis_rentabilidad/scripts/run_all.py` | 45 | no | Orquestador; docstring «Cada etapa es reanudable e idempotente»; invoca las 5 etapas y los generadores de KPI, dashboard y Parquet. |
| `Data/analisis_rentabilidad/scripts/01_ingest.py` | 409 | no | Ingesta Revolico + concesionarios + marketplaces → Parquet. |
| `Data/analisis_rentabilidad/scripts/02_clean.py` | 57 | no | Limpieza y features. |
| `Data/analisis_rentabilidad/scripts/03_eda.py` | 80 | no | KPIs y 6 gráficos Plotly HTML. |
| `Data/analisis_rentabilidad/scripts/04_stats.py` | 133 | no | OLS, VIF, Kruskal-Wallis, anomalías; escribe `modelo_muestra.csv` y `modelo_resumen.txt`. |
| `Data/analisis_rentabilidad/scripts/05_benchmark.py` | 67 | no | Benchmark por marca/modelo/año e infravalorados. |
| `Auxiliares/herramientas/actualizar_informe.py` | 416 | yes | Docstring con `Uso:`, `--inicializar` y `--regenerar`; registro de altas y regeneración del PDF. |
| `Auxiliares/herramientas/generar_dashboard.py` | 402 | no | Genera `Data/dashboard.html` sin CDN; invocado por `run_all.py`, el job de circuitos y `sitio_build.sh`. |
| `Auxiliares/herramientas/actualizar_numeros.py` | 153 | no | Actualiza los marcadores `<!-- kpi:… -->` del informe (§59). |
| `Auxiliares/herramientas/generar_sitio_mkdocs.py` | 242 | no | Regenera `docs/` y copia los gráficos y el dashboard. |

### Tests

- Files: `Auxiliares/herramientas/test_dashboard.py` (92 LOC), `Auxiliares/herramientas/test_parquet_compacto.py` (83 LOC), `Auxiliares/herramientas/test_modelo.py` (84 LOC)
- Total LOC: 259
- Framework: scripts (no usan `pytest`; no hay `pytest.ini`/`conftest.py` propios; se ejecutan con `Auxiliares/.venv-py/bin/python …`)
- Tests cover (named): `test_modelo.py` verifica el esquema y la coherencia de `modelo_muestra.csv`, los coeficientes legacy, la ausencia de afirmaciones de depreciación significativa y la idempotencia de `04_stats.py`; además hay suites de tests en repositorios de referencia (`Auxiliares/Repositorios Referencias/…/tests/`), ajenas al código propio.

### Documentation

| File | LOC |
|---|---|
| README.md | 105 |
| INFORME_TECNICO.md | 1.484 (la caché de texto de la iteración 2 tiene 1.481) |
| docs/ (32 archivos) | 2.456 LOC en Markdown + 6 HTML de gráficos + `dashboard.html` |
| Data/referencias.md | 82 (38 referencias numeradas) |
| reviews/ (19 archivos) | informe y forensic de la iteración 1, 13 artefactos de fase, y plan + artefactos e1/e2/e3 de la iteración 2 |

### Environment

- requirements.txt: present, 12 líneas útiles (pandas, numpy, plotly, statsmodels, scipy, beautifulsoup4, curl_cffi, tenacity, trafilatura, pyarrow, mkdocs, mkdocs-material)
- pyproject.toml: absent
- environment.yml: absent
- Dockerfile: absent (FlareSolverr se declara como servicio Docker externo en §6)
- Other: `.gitattributes` con filtros LFS; `mkdocs.yml`; `Auxiliares/.venv` y `Auxiliares/.venv-py`; `Auxiliares/herramientas/integraciones/README.md`; systemd timers (`precio-*`, `revolico-*`) documentados fuera del repo

### Heavy artifacts in repo

| Path | Size | Type |
|---|---|---|
| `Data/Revolico/revolico.sqlite` | 834,5 MB | sqlite (LFS) |
| `Data/Revolico/pipeline.sqlite` | 736,2 MB | sqlite (LFS) |
| `Data/catalogos_concesionarios/bdc_one.sqlite` | 73,3 MB | sqlite |
| `Data/catalogos_concesionarios/changan.sqlite` | 57,5 MB | sqlite |
| `Data/catalogos_concesionarios/marketplaces/autocubana.sqlite` | 56,2 MB | sqlite |
| `Data/catalogos_concesionarios/marketplaces/itencel.sqlite` | 56,1 MB | sqlite |
| `Data/analisis_rentabilidad/data/compacto/anuncios/year=2026/month=11/parte-000.parquet` | 24,0 MB | parquet |
| `Hombros/01_PDFs/PDF EY Highlights Automotive 2025__2e4f0d88.pdf` | 14,8 MB | pdf |
| `Data/fuentes-oficiales/ONEI/Anuario_Estadistico_2023/Archivo/aec-2023.rar` | 14,0 MB | rar |

## Datasets

| Name | Source | ID | Publicly accessible | Notes |
|---|---|---|---|---|
| Revolico scraped ads database | custom (own scrape) | `Data/Revolico/revolico.sqlite` | unknown | §14/§54: no se versiona como archivo único (chunks LFS); §66 reporta 6.955 anuncios `done`. |
| Revolico pipeline queues | custom | `Data/Revolico/pipeline.sqlite` | unknown | §16, §24, §30: colas `url_queue`, `download_queue`, `process_queue`. |
| Dealer and marketplace catalogues | custom | `Data/catalogos_concesionarios/` | unknown | §9: 11 bases y 256 filas; §30: bajo Git LFS. |
| Telegram public-channel database | custom | `Data/integraciones/telegram/telegram.sqlite` | unknown | §28–§29: `canales` 119, `anuncios` 54. |
| ONEI statistical yearbooks 2014–2025 | official (ONEI Cuba) | `Data/fuentes-oficiales/ONEI/` | yes | §53: 12 anuarios, 233 archivos (§56); `series_oficiales.csv` (§56). |
| UK DfT/DVLA vehicle statistics | official | gov.uk/…/vehicle-licensing-statistics-data-files | yes | §18: verificado en vivo, Open Government Licence. |
| VAHAN (India, MoRTH) | official | no ID declarado | no | §18: «No accesible desde este entorno (error de transporte)». |
| BCC exchange rates | official | `https://api.bc.gob.cu/v1/tasas-de-cambio/activas` | no | §52/§18: API declarada pero no accesible en vivo desde el entorno. |
| elTOQUE TRMI | non-official | `Anexos/Investigacion Cambios/trmi_USD.csv` | unknown | §23/§52: serie diaria de referencia; el modelo usa TRMI fija 930 CUP/USD de `config.py`. |
| UCI Automobile / CarDekho (Kaggle) | UCI / Kaggle | not declared in document | unknown | §18: referencias metodológicas, no precios cubanos reales. |
| PUCE used-vehicle survey | academic | `Hombros/01_PDFs/…73e1773e.pdf` | unknown | §17: 130 comerciantes; base de la clasificación de calidad ≤5 años. |
| Consolidated reference-repository tables | custom (derived) | `Data/repos-autos-referencias/referencias_autos.sqlite` | unknown | §50: 25 tablas, 3.958 anuncios, encuestas y entrevistas. |
| Fuel price series | custom | `Data/combustible/precios_combustible.sqlite` | unknown | §41: 18 observaciones (20/08–18/11/2026). |
| OSM/Overpass geodata | OpenStreetMap | `Data/mapas/gasolineras.csv` | yes | §41/§42: 137 gasolineras. |
| EV charging references | marketplace/directory | `Data/mapas/estaciones_carga.csv` | unknown | §41: 12 referencias (9 con coordenadas). |
| Circuitos Habana APK extracts | custom (APK decompilation) | `Data/mapas/circuitos/` | unknown | §62: 2.473 puntos, 244 circuitos, 166 polígonos. |
| Profitability-model sample (**new**) | derivado del pipeline | `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` | yes (en repo) | Detalle en New artifacts; respalda las cifras del modelo en §59. |
| Numbered reference list (**new**) | bibliographic (OpenAlex/Crossref) | `Data/referencias.md` | yes (en repo) | 38 entradas; detalle en New artifacts y §70. |

## New artifacts (iteración 2)

Inventario explícito de los cuatro artefactos señalados por el coordinador, contrastados en disco.

### `Data/referencias.md` — referenced in §70

- **Found in repo**: yes — 9.634 B, 82 líneas, 38 entradas numeradas `[1]`…`[38]`; generado el 27/11/2026 desde `reviews/informe-tecnico-2026-11-27.e2-literature.md`.
- **Content**: una línea por referencia con autores, título, revista, año, DOI/URL, campo `Citada en el informe: yes/no` y marca `(metadata incomplete)` cuando algún metadato no se confirmó (aparece en [1], [10] y [38] entre otras).
- **Claims supported (preliminary)**: §70 «La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`»; el propio §70 distingue cuatro referencias verificadas en vivo (Akerlof 1970, DfT/DVLA, ANFAC, AEADE) del resto.
- **Observation**: las cuatro fuentes verificadas que nombra §70 no se distinguen dentro de `referencias.md` mediante una etiqueta positiva explícita — solo aparece la marca negativa `(metadata incomplete)` —, por lo que la condición de «verificadas» debe cotejarse con `e2-literature.md`, como el propio §70 indica.

### `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` — backs §59

- **Found in repo**: yes — 265 B, cabecera + 2 filas; columnas `modelo,candidatas,observaciones,r2,p_f,terminos`.
- **Content**: `principal`: 981 candidatas / 584 observaciones / R² 0,101 / p_f 0,0; `completo`: 981 candidatas / 28 observaciones / R² 0,2744 / p_f 0,4114; términos `log_price ~ car_age + np.log1p(mileage_km) + condition_score + C(brand_tier)` y la variante con `hp`.
- **Claims supported (preliminary)**: §59 «28 observaciones completas» de «981 candidatas», R² 0,277 y p del F 0,411; coincides en observaciones, candidatas y p, aunque el R² archivado es 0,2744.
- **Observation**: existen tres estados distintos del mismo artefacto en el repositorio. `MODELOS_Y_FUNCIONES.md` (56) y sus copias en `docs/referencia/modelos.md` y `PRESENTACION_STORYTELLING.md` (257) describen 572/22 observaciones de 897 candidatas (R² 0,106 / 0,277; p 0,623), cifras que ya no coinciden con el CSV actual; el plan de esta iteración (línea 20) repite 572/22; en cambio §59 y el CSV coinciden en 28/981. El test `test_modelo.py` comprueba la estructura y la coherencia interna del CSV, no la igualdad con esas cifras documentadas.
- **Companion outputs**: `modelo_depreciacion.csv` (423 B), `modelo_resumen.txt` (2.621 B, OLS de 28 observaciones, R² 0,274, p del F 0,411), `vif.csv` (85 B), `tests.csv` (67 B), `kpis.csv` (285 B).

### `reviews/` — audit artifacts cited in §69–§70

- **Found in repo**: yes — 19 archivos `.md` al cierre de este inventario. Los trece artefactos de fase que §69 denomina «los trece artefactos de fase» están presentes: `informe-tecnico-2026-11-27.plan.md`, `.e1-claims.md`, `.e2-literature.md`, `.e3-artifacts.md`, `.v1-structure.md`, `.v2-methodology.md`, `.v3-results-evidence.md`, `.v4-novelty.md`, `.v5-state-of-the-art.md`, `.v6-reproducibility.md`, `.v7-writing.md`, `.v8-bibliography.md` y `.v9-ethics.md`.
- **Also present**: `informe-tecnico-2026-11-27.md` (45,6 KB), `.forensic.md` (343 KB) y, de la iteración 2, `informe-tecnico-2026-11-27-iter2.plan.md` (1,2 KB) junto con los artefactos `…iter2.e1-claims.md`, `…iter2.e2-literature.md` y este `…iter2.e3-artifacts.md`, escritos en paralelo durante la auditoría.
- **Claims supported (preliminary)**: §69 «sus resultados se conservan en `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` junto con los trece artefactos de fase»; §70 « Las fuentes restantes figuran con estado `(metadata incomplete)` en `reviews/informe-tecnico-2026-11-27.e2-literature.md`».
- **Observation**: las rutas citadas existen y el conteo de artefactos de fase es correcto. El informe narrativo y el expediente forensic de la iteración 2 aún no eran visibles al cerrar este inventario; la afirmación de §69 sobre «los trece artefactos» se refiere a la iteración 1, no a la 2.

### Panel interactivo — `Data/dashboard.html`

- **Found in repo**: yes — 109.929 B, título «Panel interactivo — El precio de moverse en Cuba», actualizado el 27/11/2026 (commit `99c7065`); copia en `docs/dashboard.html` (109.970 B); generado por `Auxiliares/herramientas/generar_dashboard.py` (402 LOC).
- **Type**: HTML autocontenido (vanilla JS + SVG, sin CDN ni peticiones externas) con gráficos, mapa de servicios y mapa de circuitos; fecha derivada de los datos para idempotencia.
- **Rendered in document**: no (el texto cacheado no lo incrusta ni lo nombra por esa ruta; §22/§23 citan `Data/analisis/dashboard.html` y `Data/analisis/graficos/dashboard_interactivo.html`, y §59 describe un «apéndice visual con cinco cuadros y seis gráficos reales»).
- **Documented outside the report**: `Data/AUTOMATIZACION.md`, apartado «Panel interactivo autocontenido»: un solo archivo de ~107 KB en lugar de los 6 HTML de Plotly (168 KB) más ~4,5 MB de JavaScript remoto por visita; funciona por `file://` y en 3G.
- **Claims supported (preliminary)**: «dashboard de mercado» y «entrega y monitoreo» (§17–§20), visualización de los KPIs y del estado de circuitos; probado por `Auxiliares/herramientas/test_dashboard.py`.
- **Observation**: el panel existe, está versionado y se regenera desde `run_all.py`, el job de circuitos y `sitio_build.sh`, pero el informe no declara su ruta: un lector que siga solo `INFORME_TECNICO.md` encontrará los dashboards antiguos de `Data/analisis/` y no este artefacto vigente.

## Tables

Tables: none-detected (no aparecen marcadores numerados `Tabla N` / `Table N`). Se inventarían las tablas Markdown sin numerar, con las leyendas taken verbatim de la fila de cabecera; los números de página no están disponibles en la caché de texto.

### Table (unnumbered) — «Fase | Nombre | Estado» (§2, ES)
- **Section**: §2 Estado y fases (p. n/a)
- **Lines**: 24–34
- **Columns**: Fase, Nombre, Estado
- **Rows**: 9
- **Claims supported** (preliminary): estado de fases; fase activa 6, fases 7–9 pendientes.

### Table (unnumbered) — «Búsqueda | Páginas | Resultados | Útiles | Parada» (§7, ES)
- **Section**: §7 Fase 4 — Corpus documental (p. n/a)
- **Lines**: 78–82
- **Columns**: Búsqueda, Páginas, Resultados, Útiles, Parada
- **Rows**: 3

### Table (unnumbered) — «Tienda | Filas | Con precio» (§9, ES)
- **Section**: §9 Fase 6 — Scraping y captura (p. n/a)
- **Lines**: 94–106
- **Columns**: Tienda, Filas, Con precio
- **Rows**: 11
- **Claims supported** (preliminary): «11 bases» y «256 filas»; densidad de precio por tienda.

### Table (unnumbered) — «Problema | Solución» (§11, ES)
- **Section**: §11 Problemas y soluciones (p. n/a)
- **Lines**: 122–129
- **Columns**: Problema, Solución
- **Rows**: 6

### Table (unnumbered) — «Phase | Name | Status» / «Search | Pages | Results | Useful | Stopped at» / «Store | Rows | With price» / «Problem | Solution» (§2, §7, §9, §11, EN)
- **Section**: espejo inglés de las cuatro tablas anteriores (p. n/a)
- **Lines**: 153–163, 207–211, 223–235, 251–258
- **Rows**: 9, 3, 11, 6
- **Observation**: el espejo inglés de §12 (§264–270) no reproduce la conclusión 5 del original: donde el texto español afirma que el modelo de rentabilidad está implementado (§139), la versión inglesa afirma «The interactive product and profitability model (phase 8) are not implemented yet» (§270). Es una divergencia de contenido entre tablas/parrafos paralelos, no solo de traducción.

### Table (unnumbered) — «Fecha / Date | Ruta / Path | Tipo / Type | Origen / Source | Tamaño / Size | Fase / Phase | Descripción / Description | Estado / Status» (§13)
- **Section**: §13 Registro de altas / Change log (p. n/a)
- **Lines**: 276–748 (marcador `<!-- REGISTRO_ALTAS -->` en 278; múltiples instantáneas fechadas)
- **Columns**: ocho columnas según la cabecera
- **Rows**: varies; la línea 291 declara «175 entradas adicionales no listadas / omitted»
- **Claims supported** (preliminary): inventario automático de altas, tamaños y fases; regenerado por `actualizar_informe.py`.

### Table (unnumbered) — «Última ejecución / Last run | Tamaño / Size | Partes / Chunks | SHA-256 (inicio) | Reconstrucción / Rebuild» (§14)
- **Section**: §14 Sincronización automática de Revolico (p. n/a)
- **Lines**: 756–759 (marcador `<!-- SYNC_REVOLICO -->` en 758)
- **Rows**: 1

### Table (unnumbered) — «Fuente | Aporte metodológico | Requerimiento para AutoDecide» (§17)
- **Section**: §17 Guía de análisis de mercado (p. n/a)
- **Lines**: 791–804
- **Rows**: 12

### Table (unnumbered) — «Fuente | Naturaleza | Verificación | Uso en el análisis» (§18)
- **Section**: §18 Auditoría de procedencia (p. n/a)
- **Lines**: 812–825
- **Rows**: 12

### Table (unnumbered) — «Tabla | Registros» (§29)
- **Section**: §29 Base de datos de Telegram (p. n/a)
- **Lines**: 960–965
- **Rows**: 4
- **Claims supported** (preliminary): `canales` 119, `anuncios` 54.

### Table (unnumbered) — «Métrica | Valor» (§34)
- **Section**: §34 Esqueleto de análisis de rentabilidad (p. n/a)
- **Lines**: 1041–1055
- **Rows**: 10
- **Claims supported** (preliminary): línea base de la primera ejecución (972 ingeridas, 499 limpias, 376 rechazos, 32 marcas, mediana 24.000 USD, −5,43 %/año). Es una cifra histórica: §59–§60 ya no sostienen esa pendiente.

### Table (unnumbered) — «Tipo | Color | Símbolo» (§42)
- **Section**: §42 Base unificada del mapa (p. n/a)
- **Lines**: 1166–1171
- **Rows**: 4

## Figures

Figures: none-detected (no hay marcadores `Figura N` / `Figure N`). Se inventarían los artefactos gráficos citados.

### Figure (unnumbered) — ocho PNG en `Data/analisis/graficos/` (§23, §24)
- **Section**: §23 Conversión elTOQUE, serie temporal y gráficas; §24 (p. n/a)
- **Files named**: `01_histograma_precios.png`, `02_boxplot_marcas.png`, `03_barras_municipios.png`, `04_precios_por_anio.png`, `05_serie_precio_vs_tasa.png`, `06_variaciones_tasa_precio.png`, `07_outliers.png`, `08_cobertura.png`
- **Rendered in document**: no
- **Type**: histograma, boxplots, barras, series temporales, outliers y cobertura

### Figure (unnumbered) — dashboards descriptivos (§22, §23)
- **Paths named**: `Data/analisis/dashboard.html`, `Data/analisis/graficos/dashboard_interactivo.html`
- **Rendered in document**: no
- **Type**: dashboard HTML interactivo
- **Observation**: son los dashboards que el informe cita; el panel vigente (`Data/dashboard.html`) es un artefacto distinto, descrito en New artifacts.

### Figure (unnumbered) — seis gráficos Plotly del pipeline de rentabilidad (§34, §59, §61)
- **Paths named**: `Data/analisis_rentabilidad/outputs/charts/{01_precios,02_anios,03_marcas,04_tiers,05_km_precio,06_edad_precio}.html` (23,7–51,2 KB), copias idénticas en `docs/graficos/`
- **Rendered in document**: no (§59 describe un «apéndice visual con cinco cuadros y seis gráficos reales» con referencias discretas entre paréntesis)
- **Type**: gráficos Plotly interactivos

### Figure (unnumbered) — `Data/mapas/mapa_ofline.html` (§36, §41, §42)
- **Rendered in document**: no
- **Type**: mapa Plotly sin conexión con contorno de Cuba embebido; capas de concesionarios, carga, gasolineras y talleres

### Figure (unnumbered) — activos del timelapse de circuitos (§62)
- **Paths named**: `Data/mapas/circuitos/`, `Data/mapas/circuitos_estado.sqlite`, `Data/mapas/TIMELAPSE_CIRCUITOS.md`
- **Rendered in document**: no

## Missing artifacts

### Cifras de `modelo_muestra.csv` citadas en la narrativa técnica
- **Mentioned in document**: §59 (p. n/a): «28 observaciones completas» de «981 candidatas» (R² 0,277; p del F 0,411); en paralelo, `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md` (56): «572 observaciones de 897 candidatas … el completo usa 22 (R² = 0,277; p del F = 0,623)».
- **Found in repo**: yes (el CSV existe), pero parcialmente desincronizado
- **Observation**: el archivo vigente registra 584/28 observaciones sobre 981 candidatas (R² 0,101/0,2744; p 0,0/0,4114). El escenario 572/22 de 897 candidatas que describen el plan de la iteración 2 y tres documentos derivados ya no existe en disco. No se puede reconstruir de qué corrida provienen esas cifras sin una versión anterior del CSV, y el R² de §59 (0,277) tampoco es el redondeo de 0,2744.

### Ruta del panel interactivo en el informe
- **Mentioned in document**: §17 (p. n/a): «(6) dashboard de mercado»; §19: «dashboard de mercado, limitaciones y actualización periódica»; §59: «apéndice visual con cinco cuadros y seis gráficos reales».
- **Found in repo**: yes (`Data/dashboard.html`, 109.929 B) pero no citado por esa ruta
- **Observation**: el informe nombra los dashboards de `Data/analisis/` generados el 18/11/2026, pero no el panel autocontenido que sustituye a los seis HTML de Plotly y que fue refrescado el 27/11/2026 con el estado de circuitos. El artefacto está documentado en `Data/AUTOMATIZACION.md` y se prueba en `test_dashboard.py`, pero queda fuera de la cadena de citas del documento auditado.

### `Data/referencias.md` y labellling de referencias verificadas
- **Mentioned in document**: §70 (p. n/a): «Referencias citadas y verificadas externamente durante la auditoría: Akerlof (1970) … DfT/DVLA … ANFAC … AEADE».
- **Found in repo**: yes
- **Observation**: el archivo existe con 38 entradas, pero no porta una marca positiva de «verificada» para esas cuatro; la única marca es `(metadata incomplete)` para las entradas incompletas. La distinción entre verificadas y no verificadas vive en `reviews/…e2-literature.md`, por lo que el estado que afirma §70 no es autónomo dentro del artefacto citado.

### Full Revolico SQLite file in the main branch
- **Mentioned in document**: §14 (p. n/a): «La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**»; §54: «`main` queda intacto hasta decidir su sustitución».
- **Found in repo**: yes en local (834,5 MB), no como archivo único en el historial versionado
- **Observation**: el documento describe esquemas de 48 chunks de 16 MiB (§14) y de 82 chunks de 10 MB con `MANIFEST.json` (§54) publicados en la rama huérfana `chunked-db`; `.gitattributes` confirma el manejo LFS de `*.sqlite` y `*.bin`, y `git lfs ls-files` reporta 157 objetos referenciados.

### Official Cuban vehicle-fleet and registration series
- **Mentioned in document**: §56 (p. n/a): «**No hay series de parque automotor ni de matriculaciones**».
- **Found in repo**: no
- **Observation**: los 12 anuarios ONEI están descargados, pero `series_oficiales.csv` solo contiene transporte de pasajeros y accidentes; la laguna sigue registrada como no resuelta.

### VAHAN (India) y endpoint vivo del BCC
- **Mentioned in document**: §18 (p. n/a): «No accesible desde este entorno (error de transporte)» / «No accesible en vivo desde este entorno».
- **Found in repo**: no
- **Observation**: se documentan como fuentes de referencia, sin datos recuperados; la conversión del modelo sigue usando la TRMI informal de elTOQUE fijada en `config.py`.

### Full gazette corpus
- **Mentioned in document**: §10 (p. n/a): «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe»; §67: mudanza a `~/Utilidades/Leyes`.
- **Found in repo**: no (fuera del árbol del proyecto)
- **Observation**: solo se inventarian las normas citadas por su número; el índice y los PDFs quedan fuera del repositorio después de la optimización de espacio.

### Docker daemon para el Google Maps scraper
- **Mentioned in document**: §36 (p. n/a): «el daemon Docker no arranca sin root en este entorno».
- **Found in repo**: no
- **Observation**: convive con el FlareSolverr 3.5.2 en Docker que sí se declara operativo en §6 (`http://127.0.0.1:8191/`).

### Especificaciones estructuradas y precios de transacción reales
- **Mentioned in document**: §24 (p. n/a): «**No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**»; §59–§60: pendiente anual y prima premium no significativas.
- **Found in repo**: parcial (`ad_json`, `apollo_full`, features derivados por regex)
- **Observation**: los campos se derivan con cobertura incompleta y el modelo completo solo reúne 28 observaciones; la afirmación de −5,43 %/año de §34 queda como línea base histórica, no como resultado vigente.

### `Copias/` reference repositories
- **Mentioned in document**: §3 (p. n/a): «`Copias/` no se registra en este informe por decisión explícita»; §17 cita código de `Copias/AutosxCuba/code/…`.
- **Found in repo**: yes, excluidas por decisión explícita
- **Observation**: cuatro repositorios de referencia existen en disco pero se excluyen del informe, aunque sus rutas aparecen en la tabla metodológica de §17.

## Code-to-document mapping (when discernible)

| Document component | Repo location |
|---|---|
| Revolico scraper / incremental updates | `Auxiliares/herramientas/scrape_revolico.py`, `actualizar_revolico.py`, `actualizar_informe.py` |
| Queue pipeline / classification | `Auxiliares/herramientas/scrape_revolico_pipeline.py`, `limpiar_revolico.py` |
| Dealer/marketplace scraping | `Auxiliares/herramientas/scrape_concesionarios.py`, `scrape_marketplaces.py` |
| Telegram / WhatsApp integrations | `Auxiliares/herramientas/scraper_telegram_publico.py`, `descubrir_canales_telegram.py`, `telegram_db.py` |
| Descriptive analysis and charts | `Auxiliares/herramientas/analisis_mercado.py`, `graficos_mercado.py`, `Data/analisis/` |
| Profitability pipeline | `Data/analisis_rentabilidad/config.py`, `scripts/01_ingest.py` … `05_benchmark.py`, `run_all.py`, `sql/analysis.sql` |
| Model sample backing §59 | `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` (plus `modelo_depreciacion.csv`, `modelo_resumen.txt`) |
| Panel interactivo / market dashboard | `Data/dashboard.html` and its copy `docs/dashboard.html`; generator `Auxiliares/herramientas/generar_dashboard.py`; not path-cited in the report |
| KPI markers in §59 | `Data/analisis_rentabilidad/outputs/tables/kpis.csv`; `Auxiliares/herramientas/actualizar_numeros.py` |
| Numbered references (§70) | `Data/referencias.md`; source `reviews/informe-tecnico-2026-11-27.e2-literature.md` |
| Audit artifacts (§69–§70) | `reviews/informe-tecnico-2026-11-27.{md,forensic.md}`, `.e*.md`, `.v*.md`, `.plan.md`, `informe-tecnico-2026-11-27-iter2.plan.md` |
| Reference-repo consolidation | `Auxiliares/herramientas/consolidar_repos_autos.py`, `Data/repos-autos-referencias/` |
| Maps and infrastructure | `Auxiliares/herramientas/geocode_elementos.py`, `generar_mapa_ofline.py`, `scraper_circuitos.py`, `Data/mapas/` |
| Documentation site | `docs/`, `mkdocs.yml`, `Auxiliares/herramientas/generar_sitio_mkdocs.py` |
| AI-use declaration (§69) | procedimental, sin artefacto de código asociado |

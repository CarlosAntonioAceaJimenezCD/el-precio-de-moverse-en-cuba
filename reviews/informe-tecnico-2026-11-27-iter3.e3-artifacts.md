---
type: audit-artifact
phase: e3-artifacts
slug: informe-tecnico-2026-11-27-iter3
generated_at: 2026-11-28T00:15:00-05:00
repo_url: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba
repo_clone_status: success
language: es
---

# Artifact Inventory

Iteración 3. Se inventarían los artefactos materiales que respaldan las afirmaciones del informe auditado, contrastando la caché de texto (`informe-tecnico-2026-11-27-iter3.text.md`, 1.523 líneas) con el checkout local efectivo `/home/thony70807/Proyectos/El precio de moverse en Cuba`. Se verifican en disco los siete artefactos señalados por el coordinador (dependencias fijadas, semilla, prueba de humo, CSV del modelo, bibliografía, panel y carpeta `reviews/`). Los números de línea citados corresponden a la caché de texto; en ella no hay marcadores numerados `Tabla N` / `Figura N`, por lo que las tablas se inventarían sin numerar, como en la iteración 2.

## Repository

- **URL**: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba
- **Clone status**: success (checkout local existente, 191 commits; no se realizó un clonado nuevo)
- **Languages**: Python: 40.367 LOC propias (excluye `.venv*`, `Auxiliares/Repositorios Referencias`, `Copias`, `Hombros`, `site`); Markdown: 95.706 LOC en todo el repo, de las cuales 2.495 LOC en `docs/`; HTML: panel autocontenido y 6 gráficos Plotly (ver Figures)
- **Commits**: 191
- **Authors**: CarlosAntonioAceaJimenezCD <CarlosAntonioAceaJimenezCD@users.noreply.github.com>
- **First commit**: 2026-11-17
- **Last commit**: 2026-11-27 (`ee994cd review: iteracion 2 y estandares de nivel master`)
- **Default branch**: main
- **Git LFS**: objetos grandes (`*.sqlite`, chunks) según `.gitattributes`; ver §68 y `Data/ESTRUCTURA_ESPACIO.md`

### Structure

```tree
./
├── Anexos/                  # Investigacion Cambios, Investigacion Combustible
├── Auxiliares/              # .venv*, herramientas (scripts propios), Repositorios Referencias
├── Copias/                  # 4 repos de referencia (excluidos por decisión del §3)
├── Data/                    # investigaciones, SQLite por tienda, bases y derivadas
│   ├── analisis_rentabilidad/  # config.py, scripts/, sql/, data/, outputs/{charts,tables}/, *.md
│   ├── Revolico/            # revolico.sqlite, pipeline.sqlite, chunks/, partes/
│   ├── repos-autos-referencias/  # referencias_autos.sqlite
│   ├── mapas/               # mapa_ofline.html, circuitos/, CSV de infraestructura
│   ├── dashboard.html       # panel interactivo autocontenido (vigente)
│   └── referencias.md       # 38 referencias numeradas
├── docs/ / site/            # fuente y salida MkDocs; dashboard.html, graficos/, apendice
├── reviews/                 # informes y forensic de iteraciones 1–2, artefactos de fase, plan iter3
├── Hombros/                 # PDFs, HTML, repos y derivadas
├── INFORME_TECNICO.md / .pdf, README.md, requirements.txt, mkdocs.yml
└── .playground/audit-cache/ # cachés de texto de las tres iteraciones de auditoría
```

### Entry points

| Path | LOC | Args documented | Notes |
|---|---|---|---|
| `Data/analisis_rentabilidad/scripts/run_all.py` | 58 | no | Orquestador; declara `SEED = 20261127` (líneas 16–18); invoca 5 etapas, `actualizar_numeros.py`, `generar_dashboard.py --solo-si-cambia` y `exportar_parquet_compacto.py`. |
| `Auxiliares/herramientas/generar_dashboard.py` | 402 | no | Genera `Data/dashboard.html` sin CDN; citado en §71.5 solo por su flag. |
| `Auxiliares/herramientas/actualizar_numeros.py` | 153 | no | Actualiza los marcadores `<!-- kpi:… -->` del informe (§59). |
| `Auxiliares/herramientas/generar_sitio_mkdocs.py` | 242 | no | Regenera `docs/` y copia gráficos y panel (§61, §71.5). |
| `Auxiliares/herramientas/actualizar_informe.py` | 416 | yes | Docstring con `Uso:`, `--inicializar` y `--regenerar` (§13). |
| `Auxiliares/herramientas/test_smoke_pipeline.py` | 66 | yes | Docstring con comando de ejecución; ver Tests. |

### Tests

- Files: `Auxiliares/herramientas/test_dashboard.py` (92 LOC), `Auxiliares/herramientas/test_parquet_compacto.py` (83 LOC), `Auxiliares/herramientas/test_modelo.py` (84 LOC), `Auxiliares/herramientas/test_smoke_pipeline.py` (66 LOC)
- Total LOC: 325
- Framework: scripts (`main()` propio; no usan `pytest`; no hay `pytest.ini`/`conftest.py` propios; se ejecutan con `python3 …`)
- Tests cover (named): el nuevo `test_smoke_pipeline.py` cubre compilación de los scripts, existencia de 7 artefactos, legibilidad de 4 CSV y coherencia del comando único (`SEED = 20261127` presente en `run_all.py`); los otros tres cubren panel, Parquet compacto y esquema/coherencia de `modelo_muestra.csv`. §71.5 cita expresamente la prueba de humo.

### Documentation

| File | LOC |
|---|---|
| README.md | 105 |
| INFORME_TECNICO.md | 1.523 (la caché de texto de la iteración 3 tiene 1.523) |
| docs/ (32 archivos) | 2.495 LOC en Markdown + 6 HTML de gráficos + `dashboard.html` |
| Data/referencias.md | 82 (38 referencias numeradas) |
| reviews/ (31 archivos `.md`) | informe y forensic de la iteración 1, 13 artefactos de fase, artefactos y veredictos de la iteración 2, y plan de la iteración 3 |

### Environment

- requirements.txt: present, 14 líneas (2 comentarios + 12 dependencias), todas fijadas con `~=X.Y.0`; detalle en Declared artifacts
- pyproject.toml: absent
- environment.yml: absent
- Dockerfile: absent (FlareSolverr se declara como servicio Docker externo en §6)
- Other: `.gitattributes` con filtros LFS; `mkdocs.yml`; `Auxiliares/.venv` y `Auxiliares/.venv-py`; `Auxiliares/herramientas/integraciones/README.md`; systemd timers `precio-*` documentados en §64–§66
- Observation: §34 afirma «Instalé además `statsmodels 0.15`, `pyarrow 26`», mientras `requirements.txt` fija `statsmodels~=0.14.0` y `pyarrow~=14.0.0`. La declaración de reproducibilidad de §71.5 («dependencias fijadas a serie menor») se cumple sintácticamente, pero la serie fijada no coincide con la que §34 dice haber instalado.

### Heavy artifacts in repo

| Path | Size | Type |
|---|---|---|
| `Data/Revolico/revolico.sqlite` | 836 MB | sqlite (LFS) |
| `Data/Revolico/pipeline.sqlite` | 745 MB | sqlite (LFS) |
| `Data/dashboard.html` | 107,4 KB | html (panel autocontenido) |
| `Data/referencias.md` | 9,9 KB | markdown |
| `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` | 265 B | csv |

## Declared artifacts verified on disk (iteración 3)

### `requirements.txt` — fijación `~=X.Y.0` (§71.5)

- **Found in repo**: yes — 356 B, 14 líneas, 12 dependencias; todas con operador compatible `~=X.Y.0` (pandas 2.2.0, numpy 1.26.0, plotly 5.18.0, statsmodels 0.14.0, scipy 1.11.0, beautifulsoup4 4.12.0, curl_cffi 0.7.0, tenacity 8.2.0, trafilatura 1.6.0, pyarrow 14.0.0, mkdocs 1.6.0, mkdocs-material 9.5.0).
- **Claims supported (preliminary)**: §71.5 «Las dependencias están fijadas a serie menor en `requirements.txt`».
- **Observation**: el encabezado del propio archivo declara «Fijadas a versiones menores (criterio de reproducibilidad de nivel master)». La forma `~=X.Y.0` fija la serie menor y admite parches, tal como afirma el documento; la discrepancia de series respecto de §34 se registra en Environment.

### `SEED = 20261127` en `run_all.py` (§71.5)

- **Found in repo**: yes — `Data/analisis_rentabilidad/scripts/run_all.py` líneas 16–18: `SEED = 20261127`, `random.seed(SEED)`, `np.random.seed(SEED)`. El docstring (líneas 2–7) explica que la semilla se declara también en el informe como criterio de determinismo.
- **Claims supported (preliminary)**: §71.5 «La semilla `SEED = 20261127` está declarada en `run_all.py` y en este documento»; el propio §71.5 la reproduce con el mismo valor.
- **Observation**: `test_smoke_pipeline.py::test_comando_unico` verifica literalmente la cadena `SEED = 20261127` en el orquestador, de modo que la afirmación está respaldada por código y por prueba. Ninguna de las cinco etapas (`01_ingest.py` … `05_benchmark.py`) consume la semilla directamente; el docstring lo anticipa al describir las etapas como deterministas.

### `Auxiliares/herramientas/test_smoke_pipeline.py` (§71.5)

- **Found in repo**: yes — 66 LOC, cuatro funciones (`test_compila`, `test_artefactos`, `test_csv_legibles`, `test_comando_unico`) y `main()` que imprime «4 pruebas superadas».
- **Claims supported (preliminary)**: §71.5 «Prueba de humo: `python3 Auxiliares/herramientas/test_smoke_pipeline.py`».
- **Observation**: la ruta y el intérprete citados coinciden con el docstring del script. Las siete rutas que exige `test_artefactos` incluyen `kpis.csv`, `modelo_muestra.csv`, `modelo_depreciacion.csv`, `Data/dashboard.html`, `MANIFEST.json`, `Data/referencias.md` e `INFORME_TECNICO.md`; por tanto la prueba de humo es, en parte, una comprobación de existencia de los artefactos inventariados aquí.

### `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` (§59, §71.2)

- **Found in repo**: yes — 265 B, cabecera + 2 filas; columnas `modelo,candidatas,observaciones,r2,p_f,terminos`.
- **Content**: `principal`: 981 candidatas / 584 observaciones / R² 0,101 / p_f 0,0; `completo`: 981 candidatas / 28 observaciones / R² 0,2744 / p_f 0,4114; términos `log_price ~ car_age + np.log1p(mileage_km) + condition_score + C(brand_tier)` y la variante con `hp`.
- **Claims supported (preliminary)**: §59 «28 observaciones completas» de «981 candidatas», R² 0,277 y p del F 0,411; §71.2 «la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² baja de 0,274 a 0,101». Coinciden candidatas, observaciones y p; el R² del modelo completo se redondea en el texto (0,2744 → 0,274 / 0,277).
- **Observation**: el CSV respalda la ablación descrita en §71.2 sin ambigüedad de muestra. Compañeros: `modelo_depreciacion.csv`, `modelo_resumen.txt`, `vif.csv`, `tests.csv` y `kpis.csv` en el mismo directorio.

### `Data/referencias.md` (§70)

- **Found in repo**: yes — 10.121 B, 82 líneas, 38 entradas numeradas `[1]`…`[38]`; generado el 27/11/2026 desde `reviews/informe-tecnico-2026-11-27.e2-literature.md`.
- **Content**: una línea por referencia con autores, título, revista, año, DOI/URL, campo `Citada en el informe: yes/no` y marca `(metadata incomplete)` cuando un campo no se confirmó; la entrada [38] consigna además una discrepancia de año entre OpenAlex y Crossref.
- **Claims supported (preliminary)**: §70 «La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`».
- **Observation**: el propio §70 distingue cuatro fuentes verificadas en vivo (Akerlof 1970, DfT/DVLA, ANFAC, AEADE) y remite el resto a `e2-literature.md`. Dentro de `referencias.md` solo aparece la marca negativa `(metadata incomplete)`; no hay etiqueta positiva que distinga esas cuatro, por lo que la condición «verificadas» debe cotejarse con el artefacto E2, como el texto indica.

### Panel interactivo — `Data/dashboard.html` (§61, §71.5)

- **Found in repo**: yes — 109.929 B, `<title>Panel interactivo — El precio de moverse en Cuba</title>`; copia idéntica en `docs/dashboard.html` y salida en `site/dashboard.html`; generado por `Auxiliares/herramientas/generar_dashboard.py` (402 LOC).
- **Type**: HTML autocontenido (vanilla JS + SVG, sin CDN ni peticiones externas) con gráficos, mapa de servicios y mapa de circuitos; §71.5 registra su regeneración con `--solo-si-cambia`.
- **Rendered in document**: no (la caché de texto no incrusta ni nombra esta ruta; §22/§23 citan los dashboards antiguos de `Data/analisis/`, mientras §59 describe un «apéndice visual con cinco cuadros y seis gráficos reales»).
- **Claims supported (preliminary)**: visualización de KPIs y estado de circuitos; probado por `Auxiliares/herramientas/test_dashboard.py` y por la prueba de humo.
- **Observation**: el panel existe, está versionado y se regenera desde `run_all.py`, el job de circuitos y el generador del sitio, pero el informe solo lo nombra de forma indirecta al citar a su generador en §71.5. Un lector que siga únicamente el informe encontrará primero los dashboards históricos de `Data/analisis/`.

### `reviews/` — registro de auditoría (§69–§70)

- **Found in repo**: yes — 31 archivos `.md` al cierre de este inventario.
- **Content**: informe narrativo y forensic de la iteración 1, los trece artefactos de fase que §69 denomina «los trece artefactos de fase», el informe/forensic/artefactos de la iteración 2 y, de la iteración 3, `informe-tecnico-2026-11-27-iter3.plan.md`. Este archivo `…iter3.e3-artifacts.md` se escribe en paralelo; no había veredictos ni informe de la iteración 3 al cerrar el inventario.
- **Claims supported (preliminary)**: §69 «sus resultados se conservan en `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` junto con los trece artefactos de fase»; §70 «Las fuentes restantes figuran con estado `(metadata incomplete)` en `reviews/informe-tecnico-2026-11-27.e2-literature.md`».
- **Observation**: ambas rutas existen y el conteo de artefactos de fase es correcto para la iteración 1, que es a la que se refiere §69. La frase «el registro de auditoría en `reviews/`» de §69 describe una práctica vigente, no un estado ya completo para la iteración 3.

## Datasets

| Name | Source | ID | Publicly accessible | Notes |
|---|---|---|---|---|
| Revolico scraped ads database | custom (own scrape) | `Data/Revolico/revolico.sqlite` | unknown | §66 reporta 6.955 anuncios `done`; §68: tres copias partidas. |
| Revolico pipeline queues | custom | `Data/Revolico/pipeline.sqlite` | unknown | Colas y clasificación; §66 regla de rechazo de candidatos. |
| Dealer and marketplace catalogues | custom | `Data/catalogos_concesionarios/` | unknown | §9: 11 bases y 256 filas. |
| Compact Parquet listings | derivado del pipeline | `Data/analisis_rentabilidad/data/compacto/` + `MANIFEST.json` | yes (en repo) | Usado por la prueba de humo y por `exportar_parquet_compacto.py`. |
| Profitability-model sample | derivado del pipeline | `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` | yes (en repo) | Respalda §59 y §71.2. |
| Numbered reference list | bibliográfico (OpenAlex/Crossref) | `Data/referencias.md` | yes (en repo) | 38 entradas; respalda §70. |
| Consolidated reference-repository tables | custom (derived) | `Data/repos-autos-referencias/referencias_autos.sqlite` | unknown | §50: 25 tablas, 3.958 anuncios. |
| elTOQUE TRMI | non-official | `Anexos/Investigacion Cambios/trmi_USD.csv` | unknown | §23/§52: serie diaria; el modelo usa TRMI fija de 930 CUP/USD de `config.py`. |
| ONEI statistical yearbooks | official (ONEI Cuba) | `Data/fuentes-oficiales/ONEI/` | yes | §53/§56: 12 anuarios. |
| UK DfT/DVLA vehicle statistics | official | gov.uk | yes | §18/§70: verificado en vivo. |

## Tables

Tables: none-detected (no aparecen marcadores numerados `Tabla N` / `Table N` en la caché de texto). Se inventarían las tablas Markdown sin numerar.

### Table (unnumbered) — «Fase | Nombre | Estado» (§2, ES)

- **Section**: §2 Estado y fases (p. n/a)
- **Lines**: 24–34
- **Columns**: Fase, Nombre, Estado
- **Rows**: 9
- **Claims supported** (preliminary): fase activa 6; fases 7–9 pendientes; nota de actualización de 27/11 en línea 38.

### Table (unnumbered) — «Búsqueda | Páginas | Resultados | Útiles | Parada» (§7, ES)

- **Section**: §7 Fase 4 — Corpus documental (p. n/a)
- **Lines**: 80–84
- **Columns**: Búsqueda, Páginas, Resultados, Útiles, Parada
- **Rows**: 3

### Table (unnumbered) — «Tienda | Filas | Con precio» (§9, ES)

- **Section**: §9 Fase 6 — Scraping y captura (p. n/a)
- **Lines**: 96–108
- **Columns**: Tienda, Filas, Con precio
- **Rows**: 11
- **Claims supported** (preliminary): «11 bases» y «256 filas».

### Table (unnumbered) — «Problema | Solución» (§11, ES)

- **Section**: §11 Problemas y soluciones (p. n/a)
- **Lines**: 124–131
- **Columns**: Problema, Solución
- **Rows**: 6

### Table (unnumbered) — espejo inglés de §2/§7/§9/§11

- **Section**: §2, §7, §9, §11 EN (p. n/a)
- **Lines**: 155–165, 211–215, 227–239, 255–262
- **Rows**: 9, 3, 11, 6
- **Observation**: el espejo inglés de §12 no reproduce la conclusión 5 del original: donde §139 afirma que el modelo de rentabilidad está implementado, la línea 270 afirma «The interactive product and profitability model (phase 8) are not implemented yet».

### Table (unnumbered) — «Fecha / Date | Ruta / Path | … | Estado / Status» (§13)

- **Section**: §13 Registro de altas / Change log (p. n/a)
- **Lines**: 280–682+ (marcador `<!-- REGISTRO_ALTAS -->` en 282; múltiples instantáneas)
- **Columns**: ocho columnas según la cabecera
- **Rows**: varies; la línea 295 declara «175 entradas adicionales no listadas / omitted»
- **Claims supported** (preliminary): inventario automático de altas, tamaños y fases; regenerado por `actualizar_informe.py`.

### Table (unnumbered) — «Tabla | Registros» (§29)

- **Section**: §29 Base de datos de Telegram (p. n/a)
- **Lines**: 964–968
- **Rows**: 4

### Table (unnumbered) — «Métrica | Valor» (§34)

- **Section**: §34 Esqueleto de análisis de rentabilidad (p. n/a)
- **Lines**: 1043–1054
- **Rows**: 10
- **Claims supported** (preliminary): línea base histórica (972 ingeridas, 499 limpias, 376 rechazos, 32 marcas, mediana 24.000 USD, −5,43 %/año); §59–§60 ya no sostienen esa pendiente.

### Table (unnumbered) — «Base / Baseline | Descripción | Métrica observada» (§71.1)

- **Section**: §71.1 Bases de comparación (p. n/a)
- **Lines**: 1489–1493
- **Rows**: 3
- **Claims supported** (preliminary): mediana global (MAE 18.220,46 USD sobre 1.444 anuncios), Egyptian-Used-Cars y modelo principal propio (R² 0,101 sobre 584 observaciones).

## Figures

Figures: none-detected (no aparecen marcadores numerados `Figura N` / `Figure N` en la caché de texto). Los gráficos reales se inventarían como artefactos:

- §59 (línea 1381) declara «un apéndice visual con cinco cuadros y seis gráficos reales»; §61 (línea 1399) declara que los seis gráficos Plotly se copian a `docs/graficos/` y se enlazan desde el apéndice, y que las tablas se generan desde los CSV. En disco: `docs/graficos/`, `docs/historia/apendice/` y `site/historia/apendice/`, además de `Data/analisis/graficos/` (8 PNG históricos).
- Panel interactivo: ver el artefacto `Data/dashboard.html` más arriba. No está incrustado ni nombrado por su ruta en el texto cacheado.
- **Rendered in document**: no (solo referencias discretas entre paréntesis, según §59).

## Missing artifacts

### Apéndice visual (cinco cuadros y seis gráficos)

- **Mentioned in document**: §59 (p. n/a): «Se añadió además un **apéndice visual** con cinco cuadros y seis gráficos reales».
- **Found in repo**: yes (`docs/graficos/`, `docs/historia/apendice/`, `site/historia/apendice/`)
- **Observation**: el apéndice existe como artefacto generado y el texto lo declara, pero la caché de texto auditada no contiene sus cuadros ni sus gráficos: solo la mención. Las cifras del apéndice dependen de los CSV y del HTML generados, que quedan fuera del documento texto y deben cotejarse con el sitio o con `outputs/tables/`.

### Ruta `Data/dashboard.html`

- **Mentioned in document**: §71.5 (p. n/a): «Puntos de entrada con argumentos: `generar_dashboard.py --solo-si-cambia`…».
- **Found in repo**: yes (109.929 B, con copia en `docs/`)
- **Observation**: el documento cita el generador y su flag, pero nunca declara la ruta del panel que produce. Las únicas rutas HTML explícitas en la caché pertenecen a `Data/analisis/` (líneas 578, 604, 892), derivadas de una etapa anterior. La existencia del artefacto vigente es verificable, pero no desde la lectura literal del informe.

### Series de dependencias declaradas en §34

- **Mentioned in document**: §34 (p. n/a): «Instalé además `statsmodels 0.15`, `pyarrow 26`…».
- **Found in repo**: partial (`requirements.txt` fija `statsmodels~=0.14.0`, `pyarrow~=14.0.0`)
- **Observation**: el entorno declarado en §71.5 existe y está fijado, pero las series que §34 atribuye a la instalación real no coinciden con las del archivo de dependencias. No es un archivo ausente: es una divergencia entre dos artefactos que describen el mismo entorno.

## Code-to-document mapping (when discernible)

| Document component | Repo location |
|---|---|
| Semilla declarada y comando único (§71.5) | `Data/analisis_rentabilidad/scripts/run_all.py` |
| Dependencias fijadas a serie menor (§71.5) | `requirements.txt` |
| Prueba de humo (§71.5) | `Auxiliares/herramientas/test_smoke_pipeline.py` |
| Ablación de `hp` (§59, §71.2) | `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` |
| Inventario de funciones y modelos (§60) | `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md` |
| 38 referencias y su estado (§70) | `Data/referencias.md` |
| Fuentes con `metadata incomplete` (§70) | `reviews/informe-tecnico-2026-11-27.e2-literature.md` |
| Registro de auditoría (§69) | `reviews/` |
| Panel regenerado (§61, §71.5) | `Data/dashboard.html` <- `Auxiliares/herramientas/generar_dashboard.py` |
| Esqueleto del pipeline (§34) | `Data/analisis_rentabilidad/` |
| Línea base de 972/499 filas (§34) | `Data/analisis_rentabilidad/` (tablas históricas) |
| Sitio MkDocs y apéndice (§61) | `docs/`, `site/`, `mkdocs.yml` |

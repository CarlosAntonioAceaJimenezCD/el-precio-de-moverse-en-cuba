---
type: audit-artifact
phase: v6-reproducibility
slug: informe-tecnico-2026-11-27-iter3
generated_at: 2026-11-28T01:10:42-04:00
audited_document: .playground/audit-cache/informe-tecnico-2026-11-27-iter3/informe-tecnico-2026-11-27-iter3.text.md
language: es
level: master
---

## Resumen

- `V6.documentation.master` y `V6.entry_points.master` quedan cubiertos: README con quickstart, dependencias y ejemplos, y puntos de entrada con argumentos verificados en los docstrings; dos huellas de mapeo (apéndice visual y panel vigente) no aparecen declaradas en el texto cacheado.
- `V6.environment.master` y `V6.determinism.master` quedan cubiertos en forma sintáctica: doce dependencias con `~=X.Y.0` y `SEED = 20261127` coincide entre `run_all.py` y §71.5; §34 consigna dos series distintas y la semilla no es consumida por las cinco etapas.
- `V6.tests.master` y `V6.data_availability.master` tienen infraestructura presente: la prueba de humo pasa 4/4 y los conjuntos están nombrados con rutas, aunque las dos bases SQLite principales figuran solo como rutas locales LFS.

### F-V6-001 — README con quickstart, dependencias y ejemplos de uso

`README.md` (105 líneas) contiene el quickstart de las líneas 15–33: creación de `Auxiliares/.venv-py`, `pip install -r requirements.txt` y `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py`, seguido de la lista de salidas esperadas. Las secciones «Estructura» (35–50), «Fuentes de datos» (54–64) y «Configuración» (66–80) declaran rutas de datos y de herramientas, y el apartado «Documentación» (94–99) remite a `INFORME_TECNICO.md`, `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md` y otros índices. El criterio `V6.documentation.master` se lee «README + lista de dependencias + ejemplos breves de uso»; los tres elementos están presentes, y §60, §61 y §71.5 (líneas 1405, 1399 y 1516) añaden mapeos componente→repositorio dentro del propio informe.

— polarity: positive · confidence: high · related: [] · criteria: V6.documentation.master

### F-V6-002 — Apéndice visual anunciado en §59 pero ausente en la caché de texto

§59 (línea 1381) afirma «Se añadió además un **apéndice visual** con cinco cuadros y seis gráficos reales» y §61 (línea 1401) declara «Los seis gráficos Plotly se copian a `docs/graficos/` y se enlazan desde el apéndice; las tablas del apéndice y la página de KPIs se generan desde los CSV». El inventario E3 lo registra como `Missing artifact`: en disco existen `docs/graficos/`, `docs/historia/apendice/` y `site/historia/apendice/`, pero la caché auditada conserva solo la mención, sin los cinco cuadros ni los seis gráficos. La única ruta de mapeo declarada en el texto es la carpeta genérica `docs/graficos/`; las cifras del apéndice dependen de los CSV de `outputs/tables/`, que quedan fuera del documento texto.

— polarity: neutral · confidence: high · related: [[#F-V6-003]] · criteria: V6.documentation.master

### F-V6-003 — Ruta `Data/dashboard.html` no declarada en el informe

§71.5 (línea 1516) cita `generar_dashboard.py --solo-si-cambia` entre los puntos de entrada y §61 describe el sitio MkDocs, pero ningún pasaje de la caché nombra la ruta `Data/dashboard.html` que ese generador produce. E3 la consigna como `Missing artifact`: 109.929 B en disco, con copias idénticas en `docs/dashboard.html` y `site/dashboard.html` y generación desde `Auxiliares/herramientas/generar_dashboard.py` (402 LOC). Las únicas rutas HTML explícitas en el texto son las de `Data/analisis/` (líneas 578, 604 y 892), derivadas de una etapa anterior; la existencia del panel vigente es verificable en el repo, no desde la lectura literal del informe.

— polarity: neutral · confidence: high · related: [[#F-V6-002]] · criteria: V6.entry_points.master

### F-V6-004 — Doce dependencias fijadas a serie menor en `requirements.txt`

`requirements.txt` tiene 14 líneas (2 comentarios y 12 dependencias), todas con el operador compatible `~=X.Y.0`: pandas 2.2.0, numpy 1.26.0, plotly 5.18.0, statsmodels 0.14.0, scipy 1.11.0, beautifulsoup4 4.12.0, curl_cffi 0.7.0, tenacity 8.2.0, trafilatura 1.6.0, pyarrow 14.0.0, mkdocs 1.6.0 y mkdocs-material 9.5.0. Su encabezado declara «Fijadas a versiones menores (criterio de reproducibilidad de nivel master)» y §71.5 (línea 1516) afirma «Las dependencias están fijadas a serie menor en `requirements.txt`». El criterio `V6.environment.master` se lee «Dependencias fijadas a versiones menores»; queda satisfecho. No hay `pyproject.toml`, `environment.yml`, lockfile ni Dockerfile en el checkout; lockfile, versión de Python declarada y congelación por contenedor pertenecen a `V6.environment.phd` y `V6.environment.paper`, y `README.md:17` consigna Python 3.10+ como requisito.

— polarity: positive · confidence: high · related: [[#F-V6-005]] · criteria: V6.environment.master

### F-V6-005 — §34 registra series de dependencias divergentes de las fijadas

§34 (línea 1039) consigna «Instalé además `statsmodels 0.15`, `pyarrow 26`, `kaleido`, `nbformat` y `nbconvert`», mientras `requirements.txt:6` fija `statsmodels~=0.14.0` y `requirements.txt:12` fija `pyarrow~=14.0.0`. E3 lo consigna como `Missing artifact` con estado `partial`: no falta un archivo, sino que dos artefactos describen el mismo entorno con series distintas. La afirmación de §71.5 sobre la fijación a serie menor es sintácticamente correcta para el archivo, pero no describe las versiones que §34 atribuye a la instalación efectivamente utilizada.

— polarity: negative · confidence: high · related: [[#F-V6-004]] · criteria: V6.environment.master

### F-V6-006 — Semilla `SEED = 20261127` declarada en código y en §71.5, con el mismo valor

`Data/analisis_rentabilidad/scripts/run_all.py:16–18` contiene `SEED = 20261127`, `random.seed(SEED)` y `np.random.seed(SEED)`; su docstring (líneas 2–7) declara que la semilla «se declara aqui y en el informe para cumplir el criterio de determinismo de nivel master». §71.5 (línea 1516) reproduce literalmente «La semilla `SEED = 20261127` está declarada en `run_all.py` y en este documento». `Auxiliares/herramientas/test_smoke_pipeline.py:54` comprueba la cadena `SEED = 20261127` en el orquestador. El criterio `V6.determinism.master` exige semillas declaradas en código y documento y consistentes entre sí; los tres puntos coinciden.

— polarity: positive · confidence: high · related: [[#F-V6-007]] · criteria: V6.determinism.master

### F-V6-007 — Las cinco etapas no consumen la semilla declarada

`run_all.py:25` define `STEPS = ["01_ingest.py", "02_clean.py", "03_eda.py", "04_stats.py", "05_benchmark.py"]` y `run_all.py:29–35` las invoca con `subprocess.run([PY, str(HERE / step)], …)` sin propagar `SEED`; ninguna de las cinco etapas importa la variable ni declara una semilla propia, y el docstring del orquestador describe las etapas como deterministas. Bajo `V6.determinism.master` («semillas declaradas en código y documento, consistentes») la declaración existe y coincide; en la ejecución actual la semilla opera como marca documental sin consumo directo por las etapas.

— polarity: neutral · confidence: high · related: [[#F-V6-006]] · criteria: V6.determinism.master

### F-V6-008 — Puntos de entrada con argumentos y comando único documentados

§71.5 (línea 1516) declara el comando único `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py` y cuatro puntos de entrada con argumentos. La verificación en disco coincide: `Auxiliares/herramientas/generar_dashboard.py:11` documenta `--solo-si-cambia`, `exportar_parquet_compacto.py:10` documenta `--tablas`, `db_chunks.py:5–7` documenta `split`, `assemble` y `verify`, y `generar_sitio_mkdocs.py` carece de argumentos de línea de comandos y se cita sin ellos. `README.md:19–23` reproduce instalación y comando único, `:77–80` los comandos `db_chunks.py verify|assemble` y `:86–90` los del sitio. El criterio `V6.entry_points.master` («puntos de entrada documentados con argumentos») queda cubierto; el comando único y el mapeo script→tabla del inventario E3, propios de niveles superiores, también están presentes en el repo.

— polarity: positive · confidence: high · related: [] · criteria: V6.entry_points.master

### F-V6-009 — Prueba de humo del componente central presente y ejecutable

`Auxiliares/herramientas/test_smoke_pipeline.py` (66 LOC, cuatro funciones y `main()`) es citado en §71.5 (línea 1516) como `python3 Auxiliares/herramientas/test_smoke_pipeline.py`; su docstring (línea 7) reproduce ese comando. Ejecutado en este checkout imprime «4 pruebas superadas»: 7 scripts compilan, 7 artefactos exigidos existen, 4 CSV son legibles y el comando único contiene la cadena de semilla. La cobertura se limita a compilación, existencia y consistencia textual: no ejecuta el pipeline completo ni comprueba valores numéricos del modelo. El criterio `V6.tests.master` exige «al menos pruebas de humo del componente central»; queda satisfecho. El checkout no contiene `.github/workflows`, configuración correspondiente a `V6.tests.paper`.

— polarity: positive · confidence: high · related: [[#F-V6-006]] · criteria: V6.tests.master

### F-V6-010 — Conjuntos nombrados con rutas de acceso; SQLite crudos sin URL ni DOI

El informe nombra las fuentes en §§9, 52–53, 66 y 70, y `README.md:54–64` las organiza en una tabla con URLs y rutas (`Data/fuentes-oficiales/ONEI/`, GOV.UK, Gaceta Oficial, BCC), con `README.md:75–80` declarando la reconstrucción de `revolico.sqlite` desde chunks. El inventario E3 lista diez datasets: los derivados (`compacto/`, `modelo_muestra.csv`, `referencias.md`) figuran como `yes (en repo)` y fuentes oficiales como accesibles; en cambio `Data/Revolico/revolico.sqlite`, `Data/Revolico/pipeline.sqlite`, `Data/catalogos_concesionarios/` y `Data/repos-autos-referencias/referencias_autos.sqlite` aparecen con accesibilidad pública `unknown` y solo como rutas locales gestionadas con Git LFS. El criterio `V6.data_availability.master` pide nombres más ruta de acceso (URL, DOI o «disponible bajo petición»): la primera condición está cubierta en el texto y en el README; para las dos bases principales la ruta local está documentada, sin URL, DOI ni declaración de disponibilidad en el informe.

— polarity: neutral · confidence: high · related: [[#F-V6-001]] · criteria: V6.data_availability.master

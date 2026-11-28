---
type: audit-artifact
phase: v6-reproducibility
slug: informe-tecnico-2026-11-28-iter4
generated_at: 2026-11-28T07:13:06Z
audited_document: .playground/audit-cache/informe-tecnico-2026-11-28-iter4/informe-tecnico-2026-11-28-iter4.text.md
language: es
level: master
---

# V6 — Reproducibilidad (nivel master)

## Resumen (3 líneas)

1. Los seis subcriterios V6 quedan cubiertos en nivel master: README con quickstart, `requirements.txt` con doce pinos `~=X.Y.0`, semilla coherente entre §71.5 y el código, puntos de entrada con argumentos, prueba de humo ejecutada y declaración de disponibilidad en §71.5/§71.15.
2. Verificación directa en el checkout (`main`, HEAD `77ab644`, `repo_clone_status: success`): `run_all.py` declara y exporta `PROYECTO_SEED`, `test_smoke_pipeline.py` pasa 4/4 y el panel interactivo existe en `Data/`, `docs/` y `site/` con 109.929 B.
3. Como límites descriptivos —no exigidos en master— quedan la ausencia de lockfile, Dockerfile y versión de Python fijada, la licencia pendiente declarada, dos archivos modificados sin commitear y tres CSV con recuentos divergentes del texto.

### F-V6-001 — README con quickstart, dependencias y mapeo de componentes

`README.md` (105 líneas) satisface la combinación pedida por `V6.documentation.master`: nombre y ubicación del proyecto (l. 1–5), «Quickstart» con creación de venv, `pip install -r requirements.txt` y ejecución de `Data/analisis_rentabilidad/scripts/run_all.py` (l. 15–33), «Estructura» (l. 35–52), «Fuentes de datos» (l. 54–64), «Configuración» (l. 66–80) y «Documentación» (l. 94–99), que remite a `INFORME_TECNICO.md`, `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md` y `Data/analisis_rentabilidad/README.md`. Este último (41 líneas) declara el flujo script→artefacto: `01_ingest.py` → `listings_raw.parquet`, `02_clean.py` → `listings_clean.parquet`, `03_eda.py` → `kpis.csv`, `04_stats.py` → `modelo_depreciacion.csv`/`vif.csv`/`tests.csv`, `05_benchmark.py` → `benchmark.csv`.

En el documento, §71.5 (l. 1543) declara las ubicaciones de la semilla, el panel, las bases crudas, el comando único y las dependencias; la tabla «Code-to-document mapping» de E3 (l. 198–215) inventaria catorce correspondencias adicionales. El criterio `V6.documentation.master` se lee «README + dependencies list + brief usage examples» y queda cubierto; el mapeo script→tabla completo es una exigencia de `phd`.

— polarity: positive · confidence: high · related: [[#F-V6-005]], [[#F-V6-007]] · criteria: V6.documentation.master

### F-V6-002 — Dependencias fijadas a series menores con operador `~=X.Y.0`

`requirements.txt` contiene doce líneas de dependencias activas, todas con operador compatible y parche `.0`: `pandas~=2.2.0` (l. 3), `numpy~=1.26.0` (l. 4), `plotly~=5.18.0` (l. 5), `statsmodels~=0.14.0` (l. 6), `scipy~=1.11.0` (l. 7), `beautifulsoup4~=4.12.0` (l. 8), `curl_cffi~=0.7.0` (l. 9), `tenacity~=8.2.0` (l. 10), `trafilatura~=1.6.0` (l. 11), `pyarrow~=14.0.0` (l. 12), `mkdocs~=1.6.0` (l. 13) y `mkdocs-material~=9.5.0` (l. 14). La cabecera (l. 2) reza «Fijadas a versiones menores (criterio de reproducibilidad de nivel master)» y §71.5 (l. 1543) declara «Las dependencias están fijadas a serie menor en `requirements.txt`».

Las importaciones de los siete scripts del pipeline (`pandas`, `numpy`, `scipy`, `plotly`, `bs4` y el módulo local `config`) quedan cubiertas por ese archivo. El criterio `V6.environment.master`, «Dependencies pinned to minor versions», queda satisfecho.

— polarity: positive · confidence: high · related: [[#F-V6-003]] · criteria: V6.environment.master

### F-V6-003 — Sin lockfile, Dockerfile ni versión de Python fijada en el checkout

No hay `pyproject.toml`, `environment.yml`, `Dockerfile` ni archivo de lock versionado en la raíz; E3 «Environment» (l. 75–81) registra esas cuatro ausencias. `README.md:17` declara «Requiere Python 3.10+» y el entorno local `Auxiliares/.venv-py/` corresponde a Python 3.14, sin que el repositorio fije una de las dos. §6 declara FlareSolverr 3.5.2 desplegado en Docker sin Dockerfile versionado.

Estos elementos pertenecen a `V6.environment.phd` («Dependencies fully pinned + lockfile + Python/R version declared») y `V6.environment.paper`; el nivel `master` se satisface con el pinado de serie menor de F-V6-002. La fijación `~=X.Y.0` admite cualquier parche dentro de la serie, de modo que dos entornos construidos en fechas distintas pueden resolver versiones de parche diferentes.

— polarity: neutral · confidence: high · related: [[#F-V6-002]] · criteria: V6.environment.phd

### F-V6-004 — Semilla declarada y propagada por `PROYECTO_SEED`, coherente con §71.5

El documento afirma en §71.5 (l. 1543): «La semilla `SEED = 20261127` está declarada en `run_all.py` y se propaga a cada etapa por la variable de entorno `PROYECTO_SEED`; antes se declaraba sin efecto». En el checkout, `Data/analisis_rentabilidad/scripts/run_all.py` contiene `SEED = 20261127` (l. 16), `random.seed(SEED)` (l. 17), `np.random.seed(SEED)` (l. 18) y `ENTORNO["PROYECTO_SEED"] = str(SEED)` (l. 23), entorno que se pasa a cada subprocess en la l. 39. El consumo se verifica en `03c_comparaciones.py`: `SEED = int(os.environ.get("PROYECTO_SEED", "20261127"))` (l. 20) y `rng = np.random.default_rng(SEED)` (l. 37). Un barrido de `*.py` en `Data/` y `Auxiliares/` encuentra `PROYECTO_SEED` solo en esos dos archivos, y `03c_comparaciones.py` es la única etapa del pipeline que usa un generador aleatorio: la propagación alcanza la etapa estocástica y las restantes son deterministas.

E3 registra esta verificación como «Semilla y reproducción — verificación positiva» (l. 183–186) y concluye «No hay brecha de artefacto». No hay framework de deep learning ni GPU en el pipeline, por lo que no aplican flags de determinismo cuDNN. El criterio `V6.determinism.master`, «Seeds declared in code and in document, consistent», queda satisfecho.

— polarity: positive · confidence: high · related: [[#F-V6-006]], [[#F-V6-010]] · criteria: V6.determinism.master

### F-V6-005 — Puntos de entrada documentados con argumentos y comando único

§71.5 (l. 1543) enumera el comando único `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py` y los puntos de entrada con argumentos `generar_dashboard.py --solo-si-cambia`, `exportar_parquet_compacto.py --tablas ...`, `db_chunks.py split|verify|assemble` y `generar_sitio_mkdocs.py`. `README.md:19–33` reproduce el comando único y su resultado esperado. Los argumentos se confirman en el código: `generar_dashboard.py:388–389` (`--solo-si-cambia`, `--salida`), `exportar_parquet_compacto.py:114–116` (`--db`, `--salida`, `--tablas`) y `db_chunks.py:128–136` (subcomandos `split`, `verify`, `assemble` y `--force`).

`run_all.py:27–55` encadena siete etapas y tres herramientas (actualizar números, dashboard y exportación compacta), de modo que un solo comando regenera tablas, KPIs y panel: esto excede `V6.entry_points.master` («Entry points documented with arguments») y alcanza la forma descrita en `V6.entry_points.phd`. La tabla de entry points de E3 (l. 43–53) marca «Args documented: no» para `run_all.py`, pero la documentación de argumentos reside en §71.5 y en `README.md`, y `test_smoke_pipeline.py:52–57` comprueba esa presencia.

— polarity: positive · confidence: high · related: [[#F-V6-001]], [[#F-V6-006]] · criteria: V6.entry_points.master

### F-V6-006 — Prueba de humo del componente central ejecutada con resultado positivo

§71.5 (l. 1543) cita «Prueba de humo: `python3 Auxiliares/herramientas/test_smoke_pipeline.py`». El archivo (68 líneas) contiene cuatro pruebas: `test_compila` compila nueve scripts con `py_compile`, `test_artefactos` verifica siete rutas (entre ellas `Data/dashboard.html` y `INFORME_TECNICO.md`), `test_csv_legibles` abre cinco CSV y exige al menos dos filas de `baselines.csv`, y `test_comando_unico` comprueba que `README.md` cite `run_all.py` y que el código contenga `SEED = 20261127`, `generar_dashboard.py` y `exportar_parquet_compacto.py`.

Ejecuté `python3 Auxiliares/herramientas/test_smoke_pipeline.py` sobre el checkout: las cuatro pruebas imprimieron `OK` y la salida final «4 pruebas superadas», con código de salida 0. E3 «Tests» (l. 55–60) inventaria cuatro archivos y 327 LOC, con framework de scripts y sin `pytest.ini`/`conftest.py`. La cobertura es de compilación, existencia y legibilidad; no verifica reproducibilidad bit a bit de un resultado principal, que es la exigencia de `V6.tests.paper`. El criterio `V6.tests.master`, «At least smoke tests of the central component», queda satisfecho.

— polarity: positive · confidence: high · related: [[#F-V6-004]], [[#F-V6-005]] · criteria: V6.tests.master

### F-V6-007 — Panel interactivo declarado y presente en tres rutas del repositorio

§71.5 (l. 1543) declara «El panel vigente es `Data/dashboard.html` (copiado a `docs/dashboard.html`)»; §59 (l. 1419) añade que los gráficos se copian a `docs/graficos/` y las tablas se generan desde los CSV; el Resumen (l. 19) lo describe como «panel interactivo autocontenido». En el checkout los tres archivos `Data/dashboard.html`, `docs/dashboard.html` y `site/dashboard.html` existen con 109.929 bytes cada uno. E3 «Figures» (l. 154–159) lo inventaria como artefacto HTML autocontenido y lo asocia al claim del Resumen.

`run_all.py:25` y `:53` regeneran el panel mediante `generar_dashboard.py --solo-si-cambia`, de modo que el artefacto declarado está enlazado al comando único. La copia en `site/` no aparece citada en §71.5 y está ignorada por Git. Este mapeo componente→archivo corresponde al ámbito de `V6.documentation.master`.

— polarity: positive · confidence: high · related: [[#F-V6-001]], [[#F-V6-005]] · criteria: V6.documentation.master

### F-V6-008 — Declaración de disponibilidad de datos y código, con licencia pendiente declarada

§71.5 (l. 1543) declara el repositorio público `https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba`, la ubicación de las bases crudas en `Data/Revolico/` gestionadas con Git LFS, su reconstrucción desde `chunks/MANIFEST.json`, el comando único y la prueba de humo. §71.15 (l. 1553 y su versión EN en l. 1555) cierra: «La disponibilidad de datos y código se documenta en §71.5; la licencia queda pendiente de declaración». La tabla «Datasets» de E3 (l. 96–104) nombra cinco grupos de datos con su ruta de acceso y señala los binarios como públicos vía Git LFS.

No existe `LICENSE` ni `LICENCIA` en la raíz del checkout, en coincidencia con lo declarado en §71.5 y §71.15: la ausencia aparece consignada en el documento y en E3 (l. 193–196), no como brecha oculta. El criterio `V6.data_availability.master`, «Datasets named + access path documented (URL / DOI / "available on request")», queda satisfecho; versión fijada y licencia son exigencias de `V6.data_availability.phd`.

— polarity: positive · confidence: high · related: [[#F-V6-003]] · criteria: V6.data_availability.master

### F-V6-009 — Checkout con dos archivos modificados sin commitear frente a HEAD

E3 declara `repo_clone_status: success` (l. 7) sobre la copia local en `~/Proyectos/El precio de moverse en Cuba`. La rama activa es `main` y HEAD es `77ab644` («audit: corregir los 28 hallazgos neutros de la iteracion 3»). `git status --short` muestra `M Data/referencias.md`, `M INFORME_TECNICO.md` y los cuatro artefactos de la iteración 4 sin trackear. El diff se limita a metadatos bibliográficos: el paso de «38 referencias» a «41 referencias» en §70 y el cambio de «mención nominal en §71.6, sin marcador numérico» a «§71.6 y §71.14» en las entradas [9], [14], [18] y [26]. El código del pipeline aparece sin modificaciones.

El texto en caché auditado corresponde al árbol de trabajo modificado; un clon limpio en `77ab644` entregaría el texto con la cifra «38 referencias» de §70. La declaración de disponibilidad de §71.5 no fija commit, tag ni DOI de la versión que produjo los resultados, elemento propio de `V9.code_availability_statement.phd` y no del nivel master.

— polarity: neutral · confidence: high · related: [[#F-V6-008]]

### F-V6-010 — CSV de salida presentes con recuentos divergentes del texto

Tres entradas de «Missing artifacts» de E3 (l. 163–176) se resuelven como desajustes código→documento y no como ausencia de archivos: `outputs/tables/comparaciones.csv` registra `precio por tier de marca,1462` frente a las «981 candidatas» citadas en §71.3; `outputs/tables/modelo_muestra.csv` registra `principal,993,586,0.1008` frente a las 584/572 observaciones de §71.1, §71.2 y `docs/historia/apendice.md:77`; y `outputs/tables/baselines.csv` contiene dos filas (`mediana_global`, `mediana_por_marca`) sin la fila «Modelo principal propio» que muestra la Tabla 3 de §71.1. Los tres archivos existen en `Data/analisis_rentabilidad/outputs/tables/` y son legibles, como confirma `test_csv_legibles` de F-V6-006.

Una tercera persona que ejecute el comando único obtiene los valores de esos CSV, que no coinciden exactamente con las cifras del texto. La semilla y la propagación de F-V6-004 no explican la diferencia: los desacuerdos están en los denominadores y en la composición de las filas, no en la variación estocástica.

— polarity: neutral · confidence: high · related: [[#F-V6-004]], [[#F-V6-006]]

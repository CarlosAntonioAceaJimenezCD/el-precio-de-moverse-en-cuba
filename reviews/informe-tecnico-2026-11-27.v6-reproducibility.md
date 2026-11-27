---
type: audit-artifact
phase: v6-reproducibility
slug: informe-tecnico-2026-11-27
generated_at: 2026-11-27T05:53:52Z
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27/informe-tecnico-2026-11-27.text.md
language: es
level: master
---

# V6 — Reproducibilidad (nivel master / maestría)

## Resumen

- El inventario de E3 se produjo sin clon local (`repo_clone_status: not-attempted`); esta pasada V6 sí dispuso de un checkout en `~/Proyectos/El precio de moverse en Cuba` y verificó `README.md`, `requirements.txt`, `Data/AUTOMATIZACION.md`, los scripts de análisis y los archivos de prueba contra el texto cacheado.
- La infraestructura reproducible declarada en §55 y §61 aparece en disco: README de 105 líneas con quickstart y ejemplos, `requirements.txt` con cotas `>=`, un orquestador `run_all.py` de un solo comando y 17 funciones `test_*` en tres scripts independientes; el criterio `master` de dependencias fijadas a versiones menores y de semillas declaradas no se satisface literalmente.
- Se registran dos desajustes de código a documento con efecto directo sobre la reproducción de cifras: los KPIs del README (772 autos, 2.029 anuncios) difieren de §59 (744 autos, 2.014 anuncios), y la conversión diaria por TRMI descrita en §23 corresponde en el código a un tipo de cambio fijo `FX=930` en `Data/analisis_rentabilidad/config.py:25`.

### F-V6-001 — README sustancial con nombre del proyecto, quickstart ejecutable y ejemplos de uso

`README.md` está presente con 105 líneas: abre con `# El precio de moverse en Cuba` (`README.md:1`), declara ubicación y repositorio (`README.md:5`), y contiene una sección `## Quickstart` (`README.md:15`) con tres comandos encadenados —creación de `Auxiliares/.venv-py`, `pip install -r requirements.txt` y ejecución de `Data/analisis_rentabilidad/scripts/run_all.py` (`README.md:19–23`)— seguidos de la lista de salidas esperadas (`README.md:25–33`). Incluye además ejemplos de uso para verificar y ensamblar chunks (`README.md:77–80`) y para construir y servir el sitio MkDocs (`README.md:86–90`). El texto cacheado registra la reescritura en §55, línea 1337: «Se reescribió `README.md` como página de entrada: descripción de una frase, quickstart ejecutable, estructura, tabla de fuentes, configuración, enlaces por tipo de documento y marco legal». El criterio `V6.documentation.master` —«README + dependencies list + brief usage examples»— se satisface en el checkout examinado, a diferencia del inventario de E3, que solo consignó el README a nivel de documento.

— polarity: positive · confidence: high · related: [[#F-V6-009]] · criteria: V6.documentation.master

### F-V6-002 — `requirements.txt` con cotas inferiores, sin fijación a versiones menores

El archivo `requirements.txt` existe con 13 líneas y declara diez dependencias mediante cotas inferiores —`pandas>=2.2`, `numpy>=1.26`, `plotly>=5.18`, `statsmodels>=0.14`, `scipy>=1.11`, `curl_cffi>=0.7`, `tenacity>=8.2`, `trafilatura>=1.6`, `pyarrow>=14.0`, `mkdocs>=1.6`, `mkdocs-material>=9.5` (`requirements.txt:2–12`)— sin cotas superiores ni versiones exactas. Existe también `Auxiliares/herramientas/integraciones/requirements-integraciones.txt`. En paralelo, el informe declara versiones concretas instaladas en §6, línea 70: «patchright 1.64.4, PyPasser 1.1.0, Scrapling 0.5.1, ddddocr 1.6.1, playwright 1.65.2, curl_cffi 0.17.0 [...] onnxruntime 1.32.0, ddgs 9.16.1 y tenacity 9.2.1»; §25 añade geopandas 1.2.0 y shapely 2.2.0, y §34 cita statsmodels 0.15 y pyarrow 26. Estas versiones exactas no se reflejan en el archivo de dependencias, que además difiere en `curl_cffi` (`>=0.7` frente a 0.17.0 declarada) y en `tenacity` (`>=8.2` frente a 9.2.1). No se encuentran `pyproject.toml`, lockfiles ni `Dockerfile` en el árbol. El criterio `V6.environment.master` —«Dependencies pinned to minor versions»— no se cumple en `requirements.txt`; la declaración de versiones queda confinada al texto de §6, §25 y §34 y a la sección «Declared environment» de E3.

— polarity: negative · confidence: high · related: [[#F-V6-001]], [[#F-V6-009]] · criteria: V6.environment.master

### F-V6-003 — Ausencia de semillas aleatorias declaradas, con idempotencia verificada en pruebas

La búsqueda de `semilla`, `seed`, `random_state`, `np.random` y `RandomState` en el texto cacheado devuelve solo dos coincidencias, ambas con sentido de URL de partida: §50, línea 1263, «Script reproducible en `Auxiliares/herramientas/consolidar_repos_autos.py`» y §55, línea 1333, «Las 8 semillas de marketplaces también se descargaron». La misma búsqueda sobre `Data/analisis_rentabilidad/scripts/*.py` no devuelve ninguna coincidencia: los cinco scripts de `01_ingest.py` a `05_benchmark.py` no invocan generadores aleatorios, muestreos ni divisiones entrenamiento/prueba con semilla. En su lugar, la determinación de salidas se apoya en idempotencia declarada y probada: `run_all.py:2` describe el orquestador como «reanudable e idempotente», `Auxiliares/herramientas/test_dashboard.py:60–70` comprueba `test_idempotente()` comparando hashes SHA-256 de tres generaciones consecutivas, y `Auxiliares/herramientas/probar_actualizar_numeros.py:40–46` declara `test_idempotente_en_disco()`. El criterio `V6.determinism.master` —«Seeds declared in code and in document, consistent»— no encuentra semillas que cotejar en ninguno de los dos lugares; la observación es neutra porque el componente central es regresión OLS y agregaciones deterministas.

— polarity: neutral · confidence: high · related: [[#F-V6-005]], [[#F-V6-006]] · criteria: V6.determinism.master

### F-V6-004 — Punto de entrada único documentado y comandos con argumentos

`README.md:19–23` documenta un único comando de reproducción para el análisis (`Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py`), y `run_all.py:12` declara la secuencia `["01_ingest.py", "02_clean.py", "03_eda.py", "04_stats.py", "05_benchmark.py"]`, seguida de `actualizar_numeros.py`, `generar_dashboard.py --solo-si-cambia` y `exportar_parquet_compacto.py` (`run_all.py:23–40`). `Data/analisis_rentabilidad/README.md:21–37` mapea cada etapa a sus tablas y gráficos de salida y da una segunda forma de invocación desde `Auxiliares/`. Los argumentos aparecen documentados en los comandos de reconstrucción `db_chunks.py verify <MANIFEST.json>` y `db_chunks.py assemble <MANIFEST.json> <destino>` (`README.md:78–79`) y en los comandos de MkDocs (`README.md:87–89`). El informe añade banderas por herramienta: `--solo-colas` en §33, línea 939, `--skip-unchanged` en §16, línea 781, y `--max-pages 3` en §66, línea 1437. El criterio `V6.entry_points.master` —«Entry points documented with arguments»— se cubre para las herramientas de chunks y para el orquestador en modo sin argumentos; la presencia de un comando único supera el umbral de este nivel.

— polarity: positive · confidence: high · related: [[#F-V6-001]], [[#F-V6-010]] · criteria: V6.entry_points.master

### F-V6-005 — Diecisiete funciones de prueba presentes en el checkout, no inventariadas por E3

El inventario de E3 cierra su tabla de mapeo con «Tests (`test_*.py`, `*_test.py`, `tests/`) | not located (no test files or test framework named in the document)». El checkout contiene tres scripts ejecutables con un total de 17 funciones `test_*`: `Auxiliares/herramientas/test_dashboard.py` (6 funciones, líneas 22–78, ejecuta 5 en `main()`), `Auxiliares/herramientas/test_parquet_compacto.py` (5 funciones, líneas 21–68) y `Auxiliares/herramientas/probar_actualizar_numeros.py` (6 funciones, líneas 17–60, descubiertas por prefijo en `main():64`). Cada archivo declara su propia línea de ejecución en la docstring —«Ejecutar: python3 Auxiliares/herramientas/test_dashboard.py» (:4), «Ejecutar: Auxiliares/.venv-py/bin/python [...] test_parquet_compacto.py» (:4) y «Ejecutar: python3 [...] probar_actualizar_numeros.py» (:4)—. Son scripts autónomos con `assert` y `main()`, sin `pytest.ini`, `tox.ini`, `setup.cfg` ni directorio `.github/`. `Data/AUTOMATIZACION.md:29` y `:33` nombran dos de ellos como «pruebas» del panel y del actualizador de cifras.

— polarity: positive · confidence: high · related: [[#F-V6-006]], [[#F-V6-009]] · criteria: V6.tests.master

### F-V6-006 — Las pruebas existentes no cubren el componente central del análisis

Las 17 funciones detectadas ejercitan tres artefactos periféricos: la generación del panel HTML (`test_dashboard.py:22–78`), la exportación compacta a Parquet (`test_parquet_compacto.py:21–68`) y el reemplazo de marcadores `<!-- kpi:clave -->` en documentos (`probar_actualizar_numeros.py:17–60`). Ningún archivo importa o invoca `Data/analisis_rentabilidad/scripts/01_ingest.py` … `05_benchmark.py`, ni `Auxiliares/herramientas/scrape_revolico_pipeline.py` o `limpiar_revolico.py`. En consecuencia no hay prueba de regresión para la deduplicación de 814 filas a 744 autos (§51, línea 1275; [[#C064]]), para los totales de 2.014 anuncios limpios (§58, línea 1367; [[#C010]]), ni para los coeficientes de −5,43 % anual y su posterior retirada (§34 y §59; [[#C009]], [[#C011]]). El criterio `V6.tests.master` —«At least smoke tests of the central component»— encuentra pruebas del entorno de publicación y del exportador, pero no del pipeline de rentabilidad ni del pipeline de limpieza que producen las cifras cargadas del informe.

— polarity: negative · confidence: high · related: [[#C009]], [[#C010]], [[#C011]], [[#C064]], [[#F-V6-005]] · criteria: V6.tests.master

### F-V6-007 — Divergencia de KPIs entre el informe cacheado y el README regenerado

§59, línea 1375, fija el relato final en «**744 autos únicos**, **2.014 anuncios limpios** (1.323 locales y 691 de importación), mediana local de **21.000 USD**, kilometraje mediano de **44.125 km**», cifra repetida en §58, línea 1367 y resumida en [[#C010]]. El README vigente declara en cambio «**<!-- kpi:autos_revolico -->772 autos únicos** de Revolico, **<!-- kpi:anuncios_marketplaces -->2.232 anuncios** de 8 marketplaces» (`README.md:3`), «10.177 anuncios, 772 autos» (:10) y «**Resultado esperado:** 2.029 anuncios limpios (1.338 locales + 691 de importación)» (:33). El propio `Auxiliares/herramientas/probar_actualizar_numeros.py:23–24` codifica la transición: el texto de prueba pasa de `744 autos` a `772 autos`, y `actualizar_numeros.py` reescribe los marcadores al terminar `run_all.py` (`README.md:31–33`; `Data/AUTOMATIZACION.md:33`). El desajuste impide obtener del texto cacheado los números que el pipeline actual produce, y afecta a [[#C010]], [[#C032]], [[#C066]] y a la tabla de fuentes de `README.md:56–62`.

— polarity: negative · confidence: high · related: [[#C010]], [[#C032]], [[#C066]], [[#F-V6-004]] · criteria: V6.documentation.master

### F-V6-008 — Conversión por TRMI diaria descrita en §23 frente a tipo de cambio fijo en el código

§23, línea 898, describe: «la conversión usa `precio_USD × TRMI elTOQUE` del día del anuncio (columna `Mediana` de `Anexos/Investigacion Cambios/trmi_USD.csv`)», y la misma línea 900 reporta una serie donde la TRMI «pasó de 680 CUP/USD (09/07/2026) a 920 (16-17/11/2026)» ([[#C056]], [[#C058]]). El checkout muestra otro mecanismo: `Data/analisis_rentabilidad/config.py:22–26` fija `FX = {"USD": 1.0, "CUP": 1 / 930.0, "EUR": 1000.0 / 930.0, "MLC": 845.35 / 930.0}` con `FX_NOTE = "TRMI elTOQUE 18/11/2026: USD 930 CUP..."`, y `01_ingest.py:398` convierte cada precio con `cfg.to_usd(p, c)` —función definida en `config.py:102–110`— sin leer `trmi_USD.csv`. La búsqueda de `trmi`, `FX`, `to_usd`, `930` y `Mediana` en los cinco scripts de análisis devuelve esa única coincidencia. `README.md:64` y `Data/analisis_rentabilidad/README.md:41` reproducen el valor fijo 930 CUP/USD, y `Data/AUTOMATIZACION.md:17–18` registra «Evita el `FX=930` clavado en `config.py`» como trabajo de la fase siguiente. La afirmación de conversión diaria de §23 no se reproduce desde el pipeline vigente.

— polarity: negative · confidence: high · related: [[#C056]], [[#C058]], [[#F-V6-007]] · criteria: V6.data_availability.master

### F-V6-009 — E3 registró el repositorio como no clonado; V6 operó sobre un checkout local

El frontmatter de E3 consigna `repo_url: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba` y `repo_clone_status: not-attempted`, y el cuerpo abre con «Repository: not-declared / not-cloned (no local `repo_path` was supplied for this extraction; §40 declares the remote repository [...], reproduced in frontmatter but not cloned or verified here). All entries below are document-level observations only» (`informe-tecnico-2026-11-27.e3-artifacts.md:6–13`). En esta pasada V6 el checkout local `~/Proyectos/El precio de moverse en Cuba` estuvo disponible y se inspeccionaron `README.md`, `requirements.txt`, `Data/AUTOMATIZACION.md`, `Data/analisis_rentabilidad/config.py`, los cinco scripts de `run_all.py`, tres scripts de prueba y el estado de seguimiento de Git. El criterio de nivel `master` presupone que los puntos de entrada, dependencias y rutas de datos constan en el repositorio; la verificación de E3 no pudo realizarse contra esos archivos y varias de sus entradas —tests, figuras, archivo SQLite— quedaron registradas como «Found in repo: no (no local clone supplied)» y son reinterpretadas en [[#F-V6-005]], [[#F-V6-010]] y [[#F-V6-015]].

— polarity: neutral · confidence: high · related: [[#F-V6-001]], [[#F-V6-005]], [[#F-V6-010]], [[#F-V6-015]]

### F-V6-010 — Base de Revolico no versionada como archivo único; chunks y LFS como forma de acceso

E3 registra como artifact ausente el «Full Revolico SQLite file in the main branch», citando §14, línea 752 —«La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**»— y §54, línea 1321, donde «`main` queda intacto hasta decidir su sustitución». En el checkout, `Data/Revolico/revolico.sqlite` y `pipeline.sqlite` existen en el árbol de trabajo, pero `git check-ignore` los resolve a `.gitignore:34` y `git ls-files --error-unmatch` devuelve código 1: no están versionados. La forma declarada de acceso son los manifiestos `Data/Revolico/chunks/MANIFEST.json` (82 fragmentos de 10 MB, §54) y `Data/Revolico/pipeline_chunks/MANIFEST.json` (52 fragmentos, `README.md:73`), con hashes SHA-256; `README.md:75–80` documenta `db_chunks.py verify` y `db_chunks.py assemble`. `Data/AUTOMATIZACION.md:41–42` describe el ledger LFS y el empuje del ref solo sin pendientes, y :81 lo deja como tarea de la fase siguiente. El criterio `V6.data_availability.master` —«datasets named + access path documented»— se satisface mediante los manifiestos, no mediante un archivo canónico rastreable en el historial.

— polarity: neutral · confidence: high · related: [[#C037]], [[#C070]], [[#F-V6-004]] · criteria: V6.data_availability.master

### F-V6-011 — Series oficiales de parque automotor y matriculaciones ausentes de los anuarios descargados

E3 lista como artifact ausente las «Official Cuban vehicle-fleet and registration series». §56, línea 1347, declara: «**No hay series de parque automotor ni de matriculaciones**, por lo que esa laguna signalada en `NECESIDADES.md` no se resuelve con los anuarios; la corrección quedó registrada» ([[#C012]]), a pesar de que §53, línea 1309, describe la descarga completa de los 12 anuarios del ONEI (2014–2025). El inventario de E3 observa que `series_oficiales.csv` contiene series de transporte y seguridad vial, sin parque ni matriculaciones, y que §52 había presentado el capítulo 13 del ONEI como fuente que cubriría la laguna. La fuente está nombrada y su ruta documentada, pero la variable requerida por el marco de asequibilidad (§17, línea 806; [[#C049]]) no existe entre los datos descargados.

— polarity: negative · confidence: high · related: [[#C012]], [[#C049]] · criteria: V6.data_availability.master

### F-V6-012 — Conjunto VAHAN (India) nombrado pero no accesible desde el entorno

E3 incluye «VAHAN (India) dataset» entre los artifacts ausentes. §18, línea 816, registra «No accesible desde este entorno (error de transporte)» para una fuente oficial del MoRTH de la que el repositorio documenta «12 exportaciones mensuales 2025» ([[#C051]]). El inventario de E3 la clasifica con `Publicly accessible: no` y observa que solo se dispuso del manifiesto de verificación del propio repositorio. La fuente aparece nombrada como benchmark de matriculaciones por fabricante y combustible, sin ruta de acceso utilizable en este entorno.

— polarity: negative · confidence: high · related: [[#C051]] · criteria: V6.data_availability.master

### F-V6-013 — Endpoint vivo del BCC declarado como URL pero no recuperable

E3 registra «BCC live exchange-rate endpoint» como artifact ausente. §52 declara `https://api.bc.gob.cu/v1/tasas-de-cambio/activas` como API diaria de tasas activas, mientras §18, línea 815–816, anota «No accesible en vivo desde este entorno» ([[#C051]]). El inventario de E3 marca `Publicly accessible: no` y señala que la tasa oficial se cita de forma indirecta en `Data/investigacion-mercado-automotor-cuba.md` y en la Resolución 102/2026; §55, línea 1333, añade que elTOQUE tampoco respondió en la auditoría final. `README.md:64` documenta el uso de la TRMI informal de elTOQUE de 18/11/2026 en lugar del endpoint oficial. La ruta de acceso está declarada como URL, con disponibilidad observacional ausente en este entorno.

— polarity: negative · confidence: high · related: [[#C051]], [[#C056]], [[#F-V6-008]] · criteria: V6.data_availability.master

### F-V6-014 — Corpus completo de gacetas ubicado fuera del árbol del proyecto

E3 incluye «Full gazette corpus» entre los artifacts ausentes, con cita de §10: «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe», y de §67, que sitúa las leyes en `~/Utilidades/Leyes` tras el paso de optimización de espacio. Solo se nombran Decreto 163/2026 y las resoluciones 104, 17, 52, 171–175, 340 y 102/2026 ([[#C003]], [[#C016]]). El índice de referencia y los documentos subyacentes residen fuera del proyecto, de modo que las afirmaciones normativas no se apoyan en archivos inventariables dentro del repositorio.

— polarity: negative · confidence: high · related: [[#C003]], [[#C016]] · criteria: V6.data_availability.master

### F-V6-015 — Figuras del informe sí presentes en el checkout, aunque no embebidas en el texto cacheado

E3 listó «Rendered figures for the descriptive and profitability analyses» como artifact no localizado, con «Found in repo: no (no local clone supplied; paths named in document only)», y su sección de figuras marca «Rendered in document: no» para cada entrada. El checkout contradice la primera parte: `Data/analisis/graficos/` contiene los ocho PNG nombrados en §23, línea 901 (`01_histograma_precios.png` … `08_cobertura.png`), y `docs/graficos/` contiene seis HTML de Plotly (`01_precios.html` … `06_edad_precio.html`), copias descritas en §61, línea 1395. La caché textual en cambio no incrusta ninguna imagen y §59, línea 1377, se limita a «un **apéndice visual** con cinco cuadros y seis gráficos reales; el texto solo deja referencias discretas entre paréntesis». La entrada de E3 queda así resuelta en el plano de disco y pendiente solo en el plano del texto auditado.

— polarity: neutral · confidence: high · related: [[#F-V6-009]] · criteria: V6.documentation.master

### F-V6-016 — Daemon Docker no disponible para la ruta de google-maps-scraper

E3 recoge «Docker daemon for the Google Maps scraper» como artifact ausente, citando §36: «el daemon Docker no arranca sin root en este entorno (`dockerd needs to be started with root privileges`)». La misma entrada observa que §6 sí reporta FlareSolverr 3.5.2 funcionando en Docker en `http://127.0.0.1:8191/` y que la ruta `google-maps-scraper` fue descartada. El entorno presentado en la declaración de E3 contiene por tanto un servicio contenedorizado operativo y un daemon inaccesible para otra herramienta; la segunda ruta no forma parte de los componentes reproducibles del checkout.

— polarity: negative · confidence: high · related: [[#C024]] · criteria: V6.environment.master

### F-V6-017 — Especificaciones estructuradas de vehículo y precios transados ausentes de los datos

E3 consigna «Structured vehicle specifications and real transaction prices» entre los artifacts ausentes. §24, línea 907, declara que los 6.334 anuncios conservan `meta_json`, `ad_json` y `apollo_full`, pero «**No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**» ([[#C059]]); §22, línea 890, cuantifica la cobertura derivada por regex en marca 68,4 %, año 63,5 % y km 6,2 %. §20 enumera «precios de transacción reales» y «montos de costos ocultos» entre necesidades pendientes. En `config.py:31–32` el umbral de precio válido es `PRICE_MIN_USD = 200`, distinto de los 500 USD declarados en §22, línea 890 ([[#C053]]). La combinación de campos derivados, cobertura parcial y umbral distinto condiciona la réplica de las estimaciones hedónicas de [[#C009]] y [[#C011]] a partir de los datos publicados.

— polarity: negative · confidence: high · related: [[#C009]], [[#C011]], [[#C053]], [[#C059]] · criteria: V6.data_availability.master

### F-V6-018 — `Copias/` excluidas del informe pero citadas como insumo metodológico

E3 incluye «`Copias/` reference repositories» entre los artifacts ausentes. §3 declara «`Copias/` no se registra en este informe por decisión explícita», mientras §17 cita código de `Copias/AutosxCuba/code/{unir_todo_final,modelo_predictivo,generar_graficos}.py` y §50, línea 1263, describe la tabla `provenancia` construida a partir de repositorios externos. `README.md:48–52` confirma que `Auxiliares/Repositorios Referencias/` y `Copias/` se conservan en disco pero quedan excluidos de Git. La procedencia metodológica de esas funciones y tablas queda documentada por mención, sin que los archivos citados formen parte del inventario versionado.

— polarity: neutral · confidence: high · related: [[#C048]], [[#C063]] · criteria: V6.data_availability.master

### F-V6-019 — Fuentes con ruta, URL, checksums y licencia declarados

Varias entradas del inventario de E3 cumplen el umbral `master` de «datasets named + access path documented». Los 12 anuarios del ONEI están en `Data/fuentes-oficiales/ONEI/` con URL, tamaño y SHA-256 por archivo en el `INDICE.md` de cada año (§53, líneas 1309–1311); `README.md:44` y `:96` señalan la ruta y el índice. La serie DfT/DVLA se cita en §18, línea 814, con URL de `gov.uk`, fecha de actualización 23/09/2026 y licencia «Open Government Licence» ([[#C050]]). La geolocalización de 137 gasolineras se apoya en Overpass/OSM en `Data/mapas/gasolineras.csv` (§41), marcada como públicamente accesible por E3. Los chunks de `revolico.sqlite` y `pipeline.sqlite` publican `source_sha256`, offsets y generador en sus manifiestos (`Data/AUTOMATIZACION.md:62`). El criterio `V6.data_availability.master` se satisface para este conjunto, con las excepciones registradas en [[#F-V6-012]], [[#F-V6-013]] y [[#F-V6-014]].

— polarity: positive · confidence: high · related: [[#C050]], [[#F-V6-010]] · criteria: V6.data_availability.master

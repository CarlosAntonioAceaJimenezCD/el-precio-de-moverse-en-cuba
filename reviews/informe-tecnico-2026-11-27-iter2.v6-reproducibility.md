---
type: audit-artifact
phase: v6-reproducibility
slug: informe-tecnico-2026-11-27-iter2
generated_at: 2026-11-27T21:18:12Z
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter2/informe-tecnico-2026-11-27-iter2.text.md
language: es
level: master
---

# V6 — Reproducibilidad (nivel master / maestría)

## Resumen

- El checkout sí contiene las mejoras pedidas: `requirements.txt` usa `~=`, `Data/analisis_rentabilidad/scripts/run_all.py` declara `SEED = 20261127` y `Auxiliares/herramientas/test_smoke_pipeline.py` existe y pasa sus 4 pruebas; E3, sin embargo, no inventarió este último y todas las mejoras están sin commitear en `99c7065`.
- La calibración `master` queda parcial: el README y el comando único cubren documentación y puntos de entrada, pero `~=X.Y` fija la serie mayor (no la versión menor), la semilla no aparece en el informe y no se propaga a los cinco subprocesos, y el panel, las cifras del modelo y los KPIs del texto cacheado están desincronizados del disco.
- Las lagunas de disponibilidad de datos de la iteración 1 persisten (parque/matriculaciones, VAHAN, BCC, gacetas, campos estructurados), mitigadas solo por los manifiestos con SHA-256 de Revolico y por las fuentes oficiales con URL y licencia.

### F-V6-001 — README sustancial con quickstart, salidas esperadas y mapeo de componentes

`README.md` tiene 105 líneas y abre con `# El precio de moverse en Cuba` (`README.md:1`); la sección `## Quickstart` (`README.md:15–23`) da tres comandos ejecutables —creación de `Auxiliares/.venv-py`, `pip install -r requirements.txt` y `python Data/analisis_rentabilidad/scripts/run_all.py`—, seguidos de las tres salidas esperadas (`README.md:25–33`). La tabla `## Configuración` (`README.md:66–73`) asocia cada archivo de configuración con lo que controla y la sección `## Documentación` (`README.md:94–99`) enlaza informe, guías y datos por tipo. E3 consigna `README.md | 105` en su tabla de Documentation (`informe-tecnico-2026-11-27-iter2.e3-artifacts.md:76`) y el texto registra la reescritura en §55, línea 1341. El criterio `V6.documentation.master` —«README + dependencies list + brief usage examples»— se satisface en el checkout; la divergencia de cifras se trata por separado en [[#F-V6-007]].

— polarity: positive · confidence: high · related: [[#F-V6-004]], [[#F-V6-007]] · criteria: V6.documentation.master

### F-V6-002 — `requirements.txt` paso de `>=` a `~=`, pero sin fijación real a versiones menores

El archivo cambió respecto de la iteración 1: las doce dependencias usan ahora operadores compatibles (`pandas~=2.2`, `numpy~=1.26`, `plotly~=5.18`, `statsmodels~=0.14`, `scipy~=1.11`, `beautifulsoup4~=4.12`, `curl_cffi~=0.7`, `tenacity~=8.2`, `trafilatura~=1.6`, `pyarrow~=14.0`, `mkdocs~=1.6`, `mkdocs-material~=9.5`; `requirements.txt:3–14`) y la línea 2 afirma «Fijadas a versiones menores (criterio de reproducibilidad de nivel master)». En PEP 440, `~=2.2` equivale a `>=2.2, ==2.*` y `~=0.7` a `>=0.7, ==0.*`: la cota fija la serie mayor, no el número menor, por lo que la afirmación de la línea 2 no es exacta. Además las restricciones contradicen versiones declaradas en el propio informe: `tenacity~=8.2` excluye la 9.2.1 de §6 (L72) y `pyarrow~=14.0` excluye la 26 de §34 (L1039). No hay `pyproject.toml`, lockfile ni `Dockerfile` (E3, Environment, líneas 84–88), y la versión de Python solo aparece como `3.10+` en `README.md:17`. El criterio `V6.environment.master` —«Dependencies pinned to minor versions»— no se cumple literalmente, aunque el cambio reduce la ambigüedad respecto de `>=`.

— polarity: negative · confidence: high · related: [[#F-V6-006]], [[#C023]] · criteria: V6.environment.master

### F-V6-003 — `SEED = 20261127` declarada en el orquestador, pero ausente en el informe y sin efecto en los subprocesos

`Data/analisis_rentabilidad/scripts/run_all.py:9–18` importa `random` y `numpy`, define `SEED = 20261127` y llama a `random.seed(SEED)` y `np.random.seed(SEED)`; el docstring (`run_all.py:4–7`) afirma explícitamente «La semilla se declara aqui y en el informe para cumplir el criterio de determinismo de nivel master». La búsqueda de `SEED`, `20261127`, `semilla aleatoria`, `determinismo` y `determinist` en la caché del informe y en `INFORME_TECNICO.md` no devuelve esa semilla: las únicas «semillas» del texto son las ocho URLs de partida de marketplaces de §55 (L1337), ajenas a los generadores aleatorios. Hay un segundo problema técnico: los cinco pasos se lanzan con `subprocess.run([PY, ...])` (`run_all.py:29–35`), es decir, intérpretes nuevos que no heredan el estado de los generadores del proceso padre; la semilla del orquestador no alcanza a `01_ingest.py` … `05_benchmark.py`. En sentido favorable, esos cinco scripts no contienen llamadas a `random`, `np.random` ni muestreos con semilla (búsqueda negativa en `Data/analisis_rentabilidad/scripts/*.py`) y `run_all.py:2` declara las etapas «reanudable e idempotente», de modo que el resultado actual es determinista por agregación y OLS, no por la semilla. El criterio `V6.determinism.master` —«Seeds declared in code and in document, consistent»— queda incumplido por el lado del documento y por la afirmación del docstring.

— polarity: negative · confidence: high · related: [[#F-V6-005]], [[#F-V6-006]] · criteria: V6.determinism.master

### F-V6-004 — Comando único y puntos de entrada identificables; argumentos documentados de forma desigual

`README.md:19–23` documenta un solo comando de reproducción del análisis, y `run_all.py:25` fija la secuencia `["01_ingest.py", "02_clean.py", "03_eda.py", "04_stats.py", "05_benchmark.py"]`, seguida de `actualizar_numeros.py`, `generar_dashboard.py --solo-si-cambia` y `exportar_parquet_compacto.py` (`run_all.py:36–53`). E3 inventaria diez puntos de entrada con sus LOC en la tabla `### Entry points` (`…e3-artifacts.md:50–63`) y `Data/analisis_rentabilidad/README.md:21–37` mapea cada etapa a sus tablas y gráficos. Los argumentos constan para `db_chunks.py verify|assemble` (`README.md:77–80`) y para MkDocs (`README.md:86–89`); en cambio `run_all.py` carece de docstring de uso o de banderas propias, y el propio E3 marca «Args documented: no» para las diez entradas. El criterio `V6.entry_points.master` —«Entry points documented with arguments»— se cubre para las herramientas auxiliares y para la invocación sin argumentos del orquestador, que además satisface el umbral superior de un solo comando; la documentación de argumentos del componente central queda como punto débil menor.

— polarity: positive · confidence: high · related: [[#F-V6-001]], [[#F-V6-005]] · criteria: V6.entry_points.master

### F-V6-005 — Nueva prueba de humo del componente central, ejecutada con éxito y no inventariada por E3

`Auxiliares/herramientas/test_smoke_pipeline.py` (66 líneas) declara cuatro pruebas: `test_compila()` compila los siete scripts Python del pipeline, `test_artefactos()` existe siete salidas (`kpis.csv`, `modelo_muestra.csv`, `modelo_depreciacion.csv`, `Data/dashboard.html`, `MANIFEST.json` de Parquet, `Data/referencias.md`, `INFORME_TECNICO.md`), `test_csv_legibles()` lee cuatro CSV y `test_comando_unico()` verifica que el README cite `run_all.py` y que el código contenga `SEED = 20261127` (`test_smoke_pipeline.py:22–55`). Ejecutado en este checkout con `python3 Auxiliares/herramientas/test_smoke_pipeline.py`, terminó con «4 pruebas superadas». E3, cerrado a las 17:15, solo registra tres archivos de prueba y 259 LOC (`…e3-artifacts.md:65–70`), por lo que omite este cuarto archivo; en el momento de la revisión aparece como `??` en `git status`. El criterio `V6.tests.master` —«At least smoke tests of the central component»— queda cubierto por primera vez, si bien la prueba comprueba presencia y compilación, no la reproducción numérica de los KPIs ni la ejecución completa del pipeline.

— polarity: positive · confidence: high · related: [[#F-V6-003]], [[#F-V6-006]] · criteria: V6.tests.master

### F-V6-006 — Las mejoras de reproducibilidad viven en el árbol de trabajo, no en el commit declarado

`git status --short` muestra como modificados `requirements.txt`, `Data/analisis_rentabilidad/scripts/run_all.py`, `README.md`, `Auxiliares/herramientas/actualizar_numeros.py` y tres documentos derivados, y como no rastreado `Auxiliares/herramientas/test_smoke_pipeline.py`. El HEAD sigue siendo `99c7065` (27/11/2026, «viz: refrescar panel con el ultimo estado de circuitos»), que es también el commit citado por E3 en su sección Repository (`…e3-artifacts.md:23`). En consecuencia, un clon limpio de `main` no encuentra ni las cotas `~=`, ni la semilla, ni la prueba de humo. §69 (L1469) afirma que «las cifras, los modelos estadísticos y las decisiones de diseño provienen de los datos y del código versionados en este repositorio», y §55 (L1341) da por añadido `requirements.txt`; ambas afirmaciones describen un estado posterior al commit. El criterio `V6.documentation.master`, que presupone que dependencias, puntos de entrada y rutas constan en el repositorio, no se cumple para un tercero que reproduzca desde `main`.

— polarity: negative · confidence: high · related: [[#F-V6-002]], [[#F-V6-003]], [[#F-V6-005]] · criteria: V6.documentation.master

### F-V6-007 — KPIs del texto cacheado contra KPIs regenerados en README y `kpis.csv`

§59 (L1379) fija la corrida vigente en «772 autos únicos, 2.029 anuncios limpios (1.338 locales y 691 de importación) […] kilometraje mediano de 43.000 km» y añade que «los valores se actualizan solos en `outputs/tables/kpis.csv`». En el checkout, `Data/analisis_rentabilidad/outputs/tables/kpis.csv` registra `anuncios_totales=2156`, `anuncios_locales=1465`, `anuncios_importacion=691`, `km_medianos=33256`, y `README.md:3,10,33` repite 952 autos y 2.156 anuncios. §58 (L1371) conserva además el estado intermedio de 2.014 anuncios y 44.125 km. El marcador `<!-- kpi:autos_revolico -->` se actualizó en el README (de 947 a 952 según el diff), pero la caché de texto auditada no se regeneró: el lector no puede obtener del documento las cifras que el comando único produce. Afecta a [[#C003]] y al criterio `V6.documentation.master` en su faceta de correspondencia documento↔repositorio.

— polarity: negative · confidence: high · related: [[#C003]], [[#F-V6-001]] · criteria: V6.documentation.master

### F-V6-008 — Cifras del modelo hedónico desincronizadas entre §59 y `modelo_muestra.csv`

E3 registra como artifact ausente «Cifras de `modelo_muestra.csv` citadas en la narrativa técnica» (`…e3-artifacts.md:268–271`). §59 (L1381) reporta 28 observaciones de 981 candidatas con R² 0,277 y p del F 0,411. El archivo vigente contiene `principal,981,584,0.101,0.0` y `completo,981,28,0.2744,0.4114`: coinciden candidatas, observaciones y p, pero no el R² (0,2744 frente a 0,277, que no es su redondeo). En paralelo, `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md` y sus copias describen 572/22 observaciones de 897 candidatas, un estado que ya no existe en disco. [[#C005]] no puede verificarse byte a byte desde el artefacto citado sin elegir entre tres versiones del mismo resultado, y `test_smoke_pipeline.py:43–47` solo comprueba que el CSV sea legible, no que concuerde con la narrativa.

— polarity: negative · confidence: high · related: [[#C005]], [[#F-V6-005]], [[#F-V6-007]] · criteria: V6.documentation.master

### F-V6-009 — Panel interactivo vigente documentado fuera del informe

E3 incluye «Ruta del panel interactivo en el informe» entre los artifacts ausentes (`…e3-artifacts.md:273–276`). El checkout contiene `Data/dashboard.html` (109.929 B, regenerado en `99c7065`) y su copia en `docs/dashboard.html`, generadas por `Auxiliares/herramientas/generar_dashboard.py` y probadas en `test_dashboard.py`. El informe cita en cambio los dashboards antiguos de `Data/analisis/` (§22, §23) y en §59 se limita a «un apéndice visual con cinco cuadros y seis gráficos reales». La ruta actual del panel aparece en `Data/AUTOMATIZACION.md`, no en `INFORME_TECNICO.md`; un lector que siga solo el documento no encuentra el artefacto que `run_all.py:42–47` regenera. El criterio `V6.documentation.master` no satisface aquí el mapeo entre componente y ubicación en el repositorio.

— polarity: negative · confidence: high · related: [[#F-V6-001]], [[#F-V6-004]] · criteria: V6.documentation.master

### F-V6-010 — Cuatro referencias «verificadas» sin marca positiva en `Data/referencias.md`

§70 (L1477) declara verificadas externamente a Akerlof (1970), DfT/DVLA, ANFAC y AEADE y remite a `Data/referencias.md` para la convención de 38 entradas. E3 observa que el archivo solo porta la marca negativa `(metadata incomplete)` (`…e3-artifacts.md:278–281`). La lectura directa confirma que el encabezado (`Data/referencias.md:4–6`) define esa marca y que la entrada `[1] Akerlof` (`referencias.md:8`) aparece precisamente como `(metadata incomplete)`, en contradicción con la lista de §70. La distinción entre verificadas y no verificadas vive en `reviews/informe-tecnico-2026-11-27.e2-literature.md`, por lo que el estado afirmado en el documento no es autónomo dentro del artefacto citado; afecta a [[#C048]] y [[#C009]].

— polarity: negative · confidence: high · related: [[#C009]], [[#C048]] · criteria: V6.documentation.master

### F-V6-011 — Revolico no se versiona como archivo único, pero sí con manifiestos verificables

E3 mantiene el artifact ausente «Full Revolico SQLite file in the main branch» (`…e3-artifacts.md:283–286`). §14 declara que `Data/Revolico/revolico.sqlite` «no se versiona como archivo único» y §54 (L1325–1329) describe 82 fragmentos de 10 MB con SHA-256 del archivo completo, offsets y hashes por parte, publicados en la rama huérfana `chunked-db` mientras `main` conserva el objeto LFS grande. En disco los SQLite existen y `README.md:71–80` documenta `db_chunks.py verify <MANIFEST.json>` y `db_chunks.py assemble <MANIFEST.json> <destino>`; `01_ingest.py` reconstruye la base si falta. El criterio `V6.data_availability.master` —«datasets named + access path documented»— se cumple por la vía de los manifiestos, no mediante un archivo canónico rastreable en el historial; la observación es neutra porque la propia laguna está declarada.

— polarity: neutral · confidence: high · related: [[#C042]], [[#F-V6-004]] · criteria: V6.data_availability.master

### F-V6-012 — Series de parque automotor y matriculaciones siguen ausentes tras descargar los anuarios

E3 conserva «Official Cuban vehicle-fleet and registration series» como artifact no localizado (`…e3-artifacts.md:288–291`). §53 (L1317) presentaba el capítulo 13 del anuario 2025 como fuente que permitiría incorporar parque automotor y matriculaciones, pero §56 (L1351) corrige: «**No hay series de parque automotor ni de matriculaciones**». El checkout confirma que `Data/fuentes-oficiales/ONEI/series_oficiales.csv` solo cubre transporte de pasajeros y accidentes. La fuente está nombrada y su ruta documentada, pero la variable requerida por el marco de asequibilidad no existe entre los datos descargados; [[#C041]] no es reproducible desde el repositorio.

— polarity: negative · confidence: high · related: [[#C041]], [[#C096]] · criteria: V6.data_availability.master

### F-V6-013 — VAHAN y el endpoint vivo del BCC: fuentes nombradas sin ruta utilizable

E3 agrupa «VAHAN (India) y endpoint vivo del BCC» (`…e3-artifacts.md:293–296`). §18 (L819–820) registra «No accesible desde este entorno (error de transporte)» para VAHAN y «No accesible en vivo desde este entorno» para `https://api.bc.gob.cu/v1/tasas-de-cambio/activas`; el modelo usa en su lugar la TRMI fija de 930 CUP/USD de `Data/analisis_rentabilidad/config.py`, como aclara §52 (L1297) y [[#C010]]. La URL está declarada, pero no hay datos recuperados ni ruta de acceso operativa en este entorno, de modo que la comparación con matriculaciones por fabricante y la tasa oficial no pueden recalcularse.

— polarity: negative · confidence: high · related: [[#C010]], [[#C090]] · criteria: V6.data_availability.master

### F-V6-014 — Corpus de gacetas fuera del árbol del proyecto

E3 lista «Full gazette corpus» (`…e3-artifacts.md:298–301`). §10 (L120) sitúa el índice en `~/Utilidades/Leyes/gaceta_catalog.json` y §67 (L1451) confirma que leyes y herramientas se mudaron fuera del repositorio durante la optimización de espacio. Solo se nombran en el texto Decreto 163/2026 y las resoluciones 104, 17, 52, 171–175, 340 y 102/2026 ([[#C020]], [[#C021]]); ni el índice ni los PDFs son inventariables dentro del checkout, por lo que las afirmaciones normativas no pueden cotejarse con los documentos fuente que las sustentan.

— polarity: negative · confidence: high · related: [[#C020]], [[#C021]], [[#C073]] · criteria: V6.data_availability.master

### F-V6-015 — Docker: FlareSolverr operativo pero daemon inaccesible para `google-maps-scraper`

E3 recoge «Docker daemon for the Google Maps scraper» (`…e3-artifacts.md:303–306`). §36 (L1084) explica que el daemon «no arranca sin root en este entorno» y que esa vía se descartó, mientras §6 (L72) declara FlareSolverr 3.5.2 funcionando en `http://127.0.0.1:8191/`. El entorno reproducible presentado contiene por tanto un servicio contenedorizado operativo y un daemon inaccesible para otra herramienta; la ruta descartada no forma parte de los componentes centrales, pero la convivencia de ambas declaraciones excluye una descripción uniforme del entorno en `V6.environment.master`.

— polarity: negative · confidence: high · related: [[#C065]] · criteria: V6.environment.master

### F-V6-016 — Especificaciones estructuradas y precios de transacción: cobertura parcial y umbral distinto

E3 consigna «Especificaciones estructuradas y precios de transacción reales» (`…e3-artifacts.md:308–311`). §24 (L911) declara que no hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión y que los campos se derivan con regex; §22 (L894) cuantifica la cobertura en marca 68,4 %, año 63,5 % y km 6,2 %, y fija el precio válido en ≥500 USD, mientras `Data/analisis_rentabilidad/config.py:31` usa `PRICE_MIN_USD = 200`. A ello se añade la ausencia de precios transados declarada en §20 ([[#C096]], [[#C105]]). La combinación de campos derivados, cobertura incompleta y umbral distinto condiciona la réplica de las estimaciones hedónicas desde los datos publicados.

— polarity: negative · confidence: high · related: [[#C096]], [[#C105]] · criteria: V6.data_availability.master

### F-V6-017 — `Copias/` excluidas del informe pero citadas como insumo metodológico

E3 mantiene «`Copias/` reference repositories» (`…e3-artifacts.md:313–316`). §3 (L54) declara que `Copias/` no se registra «por decisión explícita», mientras la tabla metodológica de §17 cita código de `Copias/AutosxCuba/code/…` y §50 (L1267) describe la tabla `provenancia` construida a partir de repositorios externos. Los cuatro repositorios existen en disco y `README.md:48–52` confirma que quedan fuera de Git, así que la procedencia de esas funciones y tablas queda documentada por mención, sin que los archivos citados formen parte del inventario versionado.

— polarity: neutral · confidence: high · related: [[#C046]], [[#C059]] · criteria: V6.data_availability.master

### F-V6-018 — Fuentes con ruta, URL, checksum y licencia declarados

Varias entradas del inventario superan el umbral `master`. Los 12 anuarios del ONEI están en `Data/fuentes-oficiales/ONEI/` con URL, tamaño y SHA-256 por archivo en el `INDICE.md` de cada año (§53, L1313–1315; `README.md:12,44`); la serie DfT/DVLA se cita en §18 (L818) con URL de GOV.UK, fecha de actualización 23/09/2026 y licencia Open Government Licence ([[#C088]]); las 137 gasolineras de `Data/mapas/gasolineras.csv` se apoyan en Overpass/OSM; los manifiestos de `revolico.sqlite` y `pipeline.sqlite` publican `source_sha256`, offsets y generador. El criterio `V6.data_availability.master` se satisface para este conjunto, con las excepciones de [[#F-V6-012]], [[#F-V6-013]] y [[#F-V6-014]].

— polarity: positive · confidence: high · related: [[#C040]], [[#C088]], [[#F-V6-011]] · criteria: V6.data_availability.master

---
type: audit-artifact
phase: v6-reproducibility
slug: corpus-total-2026-11-28
generated_at: 2026-11-28T05:44:45-04:00
audited_document: .playground/audit-cache/corpus-total-2026-11-28/corpus-total-2026-11-28.text.md
language: es
level: master
---

# V6 — Reproducibilidad (`level=master`)

Alcance: los seis subcriterios V6 (`documentation`, `environment`, `determinism`, `entry_points`, `tests`, `data_availability`) cotejados contra el inventario `reviews/corpus-total-2026-11-28.e3-artifacts.md` y contra el checkout local. Los cuatro artefactos nuevos se abrieron y se verificó su contenido byte a byte, su estado en Git y su fecha de modificación. Las referencias `L…` corresponden al texto cacheado; las citas de criterio a `Utilidades/ai-skills/skills/review/level-criteria.md`.

## Infraestructura reproducible declarada

### F-V6-001 — README con nombre, dependencias y ejemplo de ejecución

`README.md` (~116 LOC) nombra el proyecto, declara «Requiere Python 3.10+ y Git LFS» y ofrece bajo «Quickstart» tres comandos ejecutables (`python3 -m venv Auxiliares/.venv-py`, `pip install -r requirements.txt`, `python Data/analisis_rentabilidad/scripts/run_all.py`), seguidos de las salidas esperadas (`listings_clean.parquet`, `kpis.csv`, `kpis_canal.csv`) y de una tabla «Fuentes de datos». El §71.5 (L1552) añade el mapeo explícito de puntos de entrada a salidas. El criterio `V6.documentation.master` —«README + dependencies list + brief usage examples»— se cumple en los tres componentes.

— polarity: positive · confidence: high · related: [[#F-V6-002]], [[#F-V6-004]] · criteria: V6.documentation.master

### F-V6-002 — Dependencias fijadas a series menores, coherentes con el documento

`requirements.txt` (356 B) emplea el operador `~=` en sus 12 entradas (`pandas~=2.2.0`, `numpy~=1.26.0`, `plotly~=5.18.0`, `pyarrow~=14.0.0`, entre otras) y lleva la nota «Fijadas a versiones menores (criterio de reproducibilidad de nivel master)». El §71.5 (L1552) afirma «Las dependencias están fijadas a serie menor en `requirements.txt`»; el §71.5 en inglés (L1554) repite la declaración. Esta es la calibración exacta de `V6.environment.master` («Dependencies pinned to minor versions»). No hay lockfile ni Dockerfile; ambos aparecen recién en los criterios phd y paper.

— polarity: positive · confidence: high · related: [[#F-V6-001]], [[#F-V6-008]] · criteria: V6.environment.master

### F-V6-003 — Semilla `SEED = 20261127` declarada en código y documento, consistente

El §71.5 (L1552) y el §2 de `AUTOMATIZACION` (L2313) declaran «La semilla `SEED = 20261127` está declarada en `run_all.py` y se propaga por la variable de entorno `PROYECTO_SEED`». En `Data/analisis_rentabilidad/scripts/run_all.py:16-18,23` figuran `SEED = 20261127`, `random.seed(SEED)`, `np.random.seed(SEED)` y `ENTORNO["PROYECTO_SEED"] = str(SEED)`. Valor y mecanismo coinciden entre documento y código, que es lo que pide `V6.determinism.master` («Seeds declared in code and in document, consistent»). El propio §71.5 acota el alcance: «solo el bootstrap de `03c_comparaciones.py` la consume, porque las demás etapas son deterministas».

— polarity: positive · confidence: high · related: [[#F-V6-009]], [[#F-V6-004]] · criteria: V6.determinism.master

### F-V6-004 — Puntos de entrada documentados con argumentos y comando único

El §71.5 (L1552) enumera el comando único (`Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py`) y los puntos de entrada con argumentos: `generar_dashboard.py --solo-si-cambia`, `exportar_parquet_compacto.py --tablas ...`, `db_chunks.py split|verify|assemble` y `generar_sitio_mkdocs.py`. El inventario E3 confirma los argumentos documentados para `run_all.py` (60 LOC), `db_chunks.py` (147 LOC), `generar_dashboard.py` (402 LOC), `actualizar_numeros.py` (192 LOC) y `run_step.sh` (68 LOC), y verifica `db_chunks.py verify` con `OK (82 chunks)` y `OK (52 chunks)`. Corresponde a `V6.entry_points.master` («Entry points documented with arguments»).

— polarity: positive · confidence: high · related: [[#F-V6-001]], [[#F-V6-011]] · criteria: V6.entry_points.master

### F-V6-005 — Prueba de humo y cobertura del componente central

El §71.5 (L1552) registra «Prueba de humo: `python3 Auxiliares/herramientas/test_smoke_pipeline.py`» y el §71.5 inglés (L1554) la describe como «a smoke test checks the central component». En disco hay cuatro archivos de prueba —`test_dashboard.py`, `test_parquet_compacto.py`, `test_modelo.py` y `test_smoke_pipeline.py`— con 327 LOC en total según E3, que cubren el panel autocontenido, el Parquet compacto, el modelo econométrico y el recorrido completo del pipeline. No hay `pytest.ini` ni `conftest.py`: son scripts ejecutables, formato que `V6.tests.master` («At least smoke tests of the central component») admite.

— polarity: positive · confidence: high · related: [[#F-V6-004]] · criteria: V6.tests.master

### F-V6-006 — Fuentes nombradas con rutas de acceso; licencia sin declarar

`README.md` («Fuentes de datos») y el §71.5 (L1552) nombran Revolico, ocho marketplaces, once concesionarios, los 12 anuarios del ONEI y el repositorio público `https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba`, con rutas locales como `Data/Revolico/chunks/MANIFEST.json` y `Data/fuentes-oficiales/ONEI/`. El inventario E3 marca la accesibilidad pública como `yes` solo para ONEI y `unknown` para Revolico, marketplaces, circuitos y `price_history`. El §71.5 (L1552) declara «No se ha declarado todavía una licencia de datos o código» y el §71.15 (L1562) repite «la licencia queda pendiente de declaración». `V6.data_availability.master` exige nombre y ruta de acceso documentados, presentes para los conjuntos locales; la licencia pertenece a la calibración phd.

— polarity: neutral · confidence: high · related: [[#F-V6-012]] · criteria: V6.data_availability.master

## Los cuatro artefactos nuevos frente a lo que el documento les atribuye

### F-V6-007 — `benchmark_result.csv` es un marcador de 95 B, no la línea base de rendimiento

El §4 de `ARQUITECTURA_DATOS` (L2207) fija como criterio de «listo» de la Fase 0: «Cronometrar `run_all.py` hoy: tiempo, bytes leídos, RAM, nº de archivos y filas por año», y el §6 (L2224) cierra: «la línea base de rendimiento se guardará en `benchmark_result.csv` antes de tocar el pipeline». El archivo real, `Data/analisis_rentabilidad/outputs/tables/benchmark_result.csv`, contiene 95 B y una sola fila: `benchmark_actual,114,ingresado en benchmark.csv,114`. No hay tiempo, bytes, RAM ni conteo de archivos. `benchmark.csv` y `benchmark_nuevos.csv` existen, pero registran benchmarks de precios por marca/modelo/año, no la medición de ejecución descrita. Una búsqueda directa no encuentra `benchmark_result.csv` en ningún script de `Data/analisis_rentabilidad/scripts/` ni de `Auxiliares/herramientas/`: el artefacto no es producido por el pipeline. El expediente E3 lo registró como ausente en la auditoría previa de las 03:41 y aparece con mtime 28/11/2026 05:17:17.

— polarity: negative · confidence: high · related: [[#F-V6-011]], [[#F-V6-013]] · criteria: V6.documentation.master

### F-V6-008 — `VERSIONES.json` registra commit y Python, pero no dependencias ni hash de `config.py`

El §5 de `AUTOMATIZACION` (L2346) describe: «`VERSIONES.json`: dependencias y hash de `config.py`». El contenido real de `Data/analisis_rentabilidad/outputs/VERSIONES.json` (102 B) es `{"fecha":"2026-11-28","commit":"6c6aa6c","python":"3.14","config_hash":"verificado en MANIFEST.json"}`. Dos de los tres campos son verificables: `6c6aa6c` coincide con `git rev-parse --short HEAD` en el checkout y `3.14` con `Auxiliares/.venv-py/`. En cambio, `config_hash` contiene una cadena literal y no un valor calculado; `MANIFEST.json` de chunks no guarda hash de `config.py` (E3), y `requirements.txt` no se referencia desde el JSON. El archivo está bajo `outputs/`, ignorado por `.gitignore:45`. La trazabilidad de versiones que el documento reserva para 2028 queda materializada solo en parte, frente a `V6.environment.master`.

— polarity: negative · confidence: high · related: [[#F-V6-002]], [[#F-V6-011]] · criteria: V6.environment.master

### F-V6-009 — `manifiesto_ejecucion.jsonl` tiene una línea y omite commit, SHA, filas y watermarks

El §5 (L2345) promete «una línea por corrida con commit, SHA de scripts, Python, entradas/salidas, filas, métricas de calidad y watermark antes/después», y la «regla de oro» del mismo apartado (L2353) afirma: «Así se puede reconstruir qué se sabía en cualquier fecha». `Data/analisis_rentabilidad/outputs/manifiesto_ejecucion.jsonl` contiene 86 B y una única línea: `{"fecha":"2026-11-28","comando":"run_all.py","salida":"outputs/tables","estado":"ok"}`. Están presentes fecha, comando, salida y estado; faltan los otros siete campos enumerados en L2345, incluida la semilla que sí se declara en `run_all.py:16` (§71.5, L1552). No hay histórico de corridas previas, de modo que la reconstrucción en fecha descrita en L2353 no se apoya en este archivo. Está ignorado por `.gitignore:45`.

— polarity: negative · confidence: high · related: [[#F-V6-003]], [[#F-V6-010]], [[#F-V6-011]] · criteria: V6.documentation.master

### F-V6-010 — `watermarks.json` reduce la idempotencia a dos fechas y queda sin seguimiento

El §3 (L2326) define «Claves por fuente: Revolico `id`; marketplaces URL canónica; Telegram `tg_<canal>_<id>`; snapshots `(id, fecha_lectura)`; LFS SHA-256 del chunk» y la línea siguiente (L2327) sitúa «Marcas de agua en `Data/_state/watermarks.json`, escritas solo tras verificar la salida»; el §5 (L2347) vuelve a citar el archivo. Su contenido real (61 B) es `{"listings_clean":"2026-11-28","price_history":"2026-11-28"}`: dos fechas, sin claves por fuente, identificadores ni offsets. `git status --short` devuelve `?? Data/_state/watermarks.json`, mientras los scripts de `Data/_state/` sí están versionados (E3). La garantía de idempotencia y reanudación descrita en §3 y §5 no se puede verificar con este estado.

— polarity: negative · confidence: high · related: [[#F-V6-009]], [[#F-V6-011]] · criteria: V6.documentation.master

### F-V6-011 — Los cuatro artefactos aparecieron el 28/11 y no son regenerables ni versionados

Los cuatro ficheros comparten mtime 2026-11-28 05:17:17: los tres de `Data/analisis_rentabilidad/outputs/` están excluidos por `.gitignore:45` (`git check-ignore -v` lo confirma) y `Data/_state/watermarks.json` figura como `??`. El inventario E3 registra que la auditoría previa de las 03:41 los dio por ausentes. El comando único documentado en §71.5 (L1552) produce `INGESTA`, `LIMPIEZA`, `EDA`, `STATS` y `BENCHMARK` y actualiza `listings_clean.parquet`, `kpis.csv` y `kpis_canal.csv`, pero no enumera ninguno de los cuatro artefactos entre sus salidas; ningún script referencia `benchmark_result.csv`. En un checkout limpio, por tanto, los cuatro ficheros no se reconstruyen ni se recuperan de Git, a pesar de que el Resumen (L28, L170) los cuenta dentro del «expediente de auditoría con 13 artefactos».

— polarity: negative · confidence: high · related: [[#F-V6-004]], [[#F-V6-007]], [[#F-V6-008]], [[#F-V6-009]], [[#F-V6-010]] · criteria: V6.entry_points.master

## Desajustes adicionales código–documento

### F-V6-012 — El expediente a dos años carece de snapshots semanales, diccionario y ledger LFS

El §5 de `AUTOMATIZACION` (L2348–2351) describe «Un snapshot Parquet inmutable por semana (`snapshots/YYYY-Www/`) con puntero `LATEST.json`. 104 semanas ≈ 2 años», además de `DICCIONARIO.md`, `LIMITACIONES.md` y los `MANIFEST.json` de chunks. En el checkout, `Data/Revolico/snapshots/` contiene únicamente `ultimo.json`, un mapa de offsets de enlaces, sin directorios `YYYY-Www` ni `LATEST.json`; no hay `DICCIONARIO.md`, `LIMITACIONES.md` ni `_state/lfs_push_ledger.jsonl`. El propio §6 (L2369) declara el ledger como pendiente. `salud.json` y `alertas.jsonl` sí existen, pero en `Data/_estado/`, ignorado por Git. El componente de auditoría a largo plazo del «expediente con 13 artefactos» (L28, L170) no está materializado.

— polarity: negative · confidence: high · related: [[#F-V6-006]] · criteria: V6.documentation.master

### F-V6-013 — `estado.duckdb` y los rollups `kpi_mes`/`benchmark_result` son arquitectura propuesta

El §3 (L2192, L2198) ubica en el diseño un `estado.duckdb` con «watermark + kpi_mes + benchmark_result» y define los rollups keyed por `(year, month, dataset_version)`; la Fase 3 (L2210) habla de «Materializar `kpi_mes` y `benchmark_result`». El §6 (L2224) explica el bloqueo: «`import duckdb` falla con `SIGILL` (Instrucción ilegal) en esta CPU» y que «Este documento es la Fase 0–1 de diseño». No existe `estado.duckdb` en el checkout, y el `benchmark_result.csv` presente es el marcador descrito en F-V6-007, no un rollup mensual. El documento distingue explícitamente diseño de implementación, pero la tabla de fases (L2205–2212) y el inventario de artefactos no reflejan ese desajuste en el mismo lugar.

— polarity: negative · confidence: high · related: [[#F-V6-007]] · criteria: V6.documentation.master

### F-V6-014 — El entorno ejecutable queda ligado a la máquina local

El §71.5 (L1552) declara el repositorio público y el entorno `Auxiliares/.venv-py/`, que no está versionado y corre Python 3.14, frente al «Python 3.10+» del `README.md`. Los diez timers `precio-*`, `loginctl enable-linger` (L2330, L2360) y los wrappers de `~/.config/systemd/user/` viven fuera del checkout; E3 los confirma activos. `Data/Revolico/revolico.sqlite` (839 MB) y `pipeline.sqlite` (758 MB) tampoco están versionados, aunque son reconstruibles desde los chunks verificados (82 y 52 `.bin`). La reproducción automática describe un entorno local operativo, no un estado recuperable del repositorio; `V6.environment.master` se satisface en el archivo de dependencias, no en el congelamiento del entorno.

— polarity: neutral · confidence: medium · related: [[#F-V6-002]], [[#F-V6-011]] · criteria: V6.environment.master

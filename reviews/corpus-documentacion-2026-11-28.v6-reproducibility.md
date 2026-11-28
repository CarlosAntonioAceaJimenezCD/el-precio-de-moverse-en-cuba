---
type: audit-artifact
phase: v6-reproducibility
slug: corpus-documentacion-2026-11-28
generated_at: 2026-11-28T03:54:01-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md
language: es
level: master
---

# V6 — Reproducibilidad

Alcance: se evaluó el corpus unificado de 8 archivos (L1–833) contra los criterios `V6.*.master` de `level-criteria.md`, leyó íntegramente `reviews/corpus-documentacion-2026-11-28.e3-artifacts.md` y contrastó cada ruta citada con el checkout real `/home/thony70807/Proyectos/El precio de moverse en Cuba` (HEAD `77ab644`, 28/11/2026). Las referencias `L…` son del texto cacheado. Las verificaciones de ejecución se hicieron con `Auxiliares/.venv-py/bin/python`.

## Hallazgos

### F-V6-001 — README completo con quickstart, dependencias y ejemplos de uso

El corpus incluye el `README.md` íntegro (L8–116): nombre y ubicación del proyecto (L10–14), contenido (L16–22), Quickstart (L24–42), estructura (L44–61), fuentes (L63–73), configuración (L75–89), sitio MkDocs (L91–101), documentación de referencia (L103–108) y límites (L110–115). El nivel master exige README + lista de dependencias + ejemplos breves de uso: los tres están presentes y verificados en disco (`README.md` de 116 líneas, `requirements.txt`, `mkdocs.yml`). El mapeo componente→repositorio además está explicitado en `E3 §Code-to-document mapping`, donde 10 de 11 componentes se localizan; confirmé la existencia de `Data/analisis_rentabilidad/config.py`, ambos `MANIFEST.json`, `INFORME_TECNICO.md` y `docs/`.

— polarity: positive · confidence: high · related: [[#C076]] [[#C078]] [[#C080]] · criteria: V6.documentation.master

### F-V6-002 — Dependencias fijadas a serie menor

`requirements.txt` tiene 14 líneas y 12 dependencias activas con operador `~=` (`pandas~=2.2.0`, `numpy~=1.26.0`, `plotly~=5.18.0`, `statsmodels~=0.14.0`, `scipy~=1.11.0`, `beautifulsoup4~=4.12.0`, `curl_cffi~=0.7.0`, `tenacity~=8.2.0`, `trafilatura~=1.6.0`, `pyarrow~=14.0.0`, `mkdocs~=1.6.0`, `mkdocs-material~=9.5.0`), con comentario explícito: «Fijadas a versiones menores (criterio de reproducibilidad de nivel master)». El README declara Python 3.10+ y Git LFS (L26) y el entorno en uso es `Auxiliares/.venv-py` (verificado: `bin/python`, `bin/pip`, `bin/mkdocs`). No hay lockfile ni `pyproject.toml`, pero el nivel master no los exige (`V6.environment.phd`). La laguna de dependencias del pipeline de mapas se evalúa en F-V6-009.

— polarity: positive · confidence: high · related: [[#C076]] · criteria: V6.environment.master

### F-V6-003 — Comando único de reproducción y puntos de entrada documentados

El Quickstart (L28–32) da una sola secuencia: crear `Auxiliares/.venv-py`, instalar `requirements.txt` y ejecutar `Data/analisis_rentabilidad/scripts/run_all.py`. Verifiqué los 7 scripts que orquesta (`01_ingest.py`, `02_clean.py`, `03_eda.py`, `03b_baselines.py`, `03c_comparaciones.py`, `04_stats.py`, `05_benchmark.py`) y las tres llamadas finales (`actualizar_numeros.py`, `generar_dashboard.py --solo-si-cambia`, `exportar_parquet_compacto.py`). El corpus también documenta argumentos de `db_chunks.py verify|assemble` (L87–88) y de `mkdocs build|serve` (L96–98). `run_all.py` (60 líneas) imprime `ANALISIS COMPLETO` al terminar. Un comando único es criterio de nivel phd (`V6.entry_points.phd`), por lo que el corpus supera lo exigido en master.

— polarity: positive · confidence: high · related: [[#C076]] [[#C077]] [[#C081]] [[#C082]] · criteria: V6.entry_points.master

### F-V6-004 — Prueba de humo del componente central, ejecutada y superada

`E3 §Tests` inventaría cinco pruebas; verifiqué que las cinco existen en `Auxiliares/herramientas/`: `test_dashboard.py` (92 líneas), `test_parquet_compacto.py` (83), `test_modelo.py` (84), `test_smoke_pipeline.py` (68) y `probar_actualizar_numeros.py` (74). Ejecuté la de humo con el entorno del repo: `Auxiliares/.venv-py/bin/python Auxiliares/herramientas/test_smoke_pipeline.py` → `4 pruebas superadas` (9 scripts compilan, 7 artefactos existen, CSV legibles, comando único documentado), código de salida 0. No hay `pytest.ini` ni `conftest.py`: son scripts autónomos, suficiente para el criterio master (smoke test del componente central), no para el de nivel phd.

— polarity: positive · confidence: high · related: [[#C074]] · criteria: V6.tests.master

### F-V6-005 — Bases reconstruibles desde chunks y salidas verificables

El corpus declara 82 fragmentos de 10 MB con SHA-256 (L81) y 52 de `pipeline.sqlite` (L82), y describe `db_chunks.py verify|assemble` para reconstruir las SQLite si faltan (L84–89). En disco hay 82 y 52 `.bin` respectivamente, ambos `MANIFEST.json` versionados y los cuatro scripts de chunking citados en L824–829. También están presentes `listings_clean.parquet`, los 6 CSV/TXT citados por nombre en `outputs/tables/` (21 archivos en total) y los 6 HTML de `outputs/charts/`. Las SQLite originales (839 MB y 755 MB) existen localmente pero están excluidas por `.gitignore`; la ruta de reconstrucción documentada cubre el criterio master de «access path».

— polarity: positive · confidence: high · related: [[#C073]] [[#C074]] [[#C081]] · criteria: V6.data_availability.master

### F-V6-006 — Semilla declarada en código pero ausente del corpus auditado

En las 833 líneas del corpus no aparece `semilla`, `seed`, `SEED` ni `PROYECTO_SEED`: L399–403 usan «preparación determinista» solo en el sentido de normalización sintáctica (`parse_price`, `parse_number`, deduplicación), no de aleatoriedad controlada. En cambio el código sí la declara: `Data/analisis_rentabilidad/scripts/run_all.py:16-23` define `SEED = 20261127`, llama a `random.seed` y `np.random.seed` y exporta `PROYECTO_SEED`; `03c_comparaciones.py:20,37` la consume con `np.random.default_rng(SEED)` para el bootstrap. `INFORME_TECNICO.md:1541-1545` (§71.5) documenta la semilla, pero ese archivo **no** es uno de los 8 bloques del corpus (encabezados `# ARCHIVO:` en L8, 119, 395, 493, 571, 629, 735 y 793): quien reproduzca solo desde los documentos auditados no puede fijar el bootstrap. Además la frase de §71.5 «se propaga a cada etapa» es imprecisa: solo `03c_comparaciones.py` lee la variable. El criterio master exige semilla en código **y** documento, consistente; aquí solo se cumple la mitad.

— polarity: negative · confidence: high · related: [[#C111]] · criteria: V6.determinism.master

### F-V6-007 — Línea base de rendimiento `benchmark_result.csv` no materializada

`ARQUITECTURA_DATOS.md` define la Fase 0 como «Línea base documentada» (L549) y afirma: «la línea base de rendimiento se guardará en `benchmark_result.csv` antes de tocar el pipeline» (L566), presentando el documento como «Fase 0–1 de diseño». Verifiqué que `Data/analisis_rentabilidad/outputs/tables/` contiene 21 archivos (KPIs, benchmarks, anomalías, modelo) pero ningún `benchmark_result.csv`, y que no existe en otra ruta del checkout; `E3 §Missing artifacts` lo registra. Sin esa medición previa no es verificable la comparación antes/después que motiva la adopción de DuckDB/Polars (L518–527, L551–554).

— polarity: negative · confidence: high · related: [[#C113]] [[#C114]] · criteria: V6.documentation.master

### F-V6-008 — Trazabilidad de «auditoría a dos años» descrita como implementada, pero sin artefactos

`AUTOMATIZACION.md` §5 dice «Se guarda, en UTC y con hashes» (L685) y enumera `manifiesto_ejecucion.jsonl` (L687), `VERSIONES.json` (L688), `watermarks.json` (L669), `_state/lfs_push_ledger.jsonl` (L671), `snapshots/YYYY-Www/` con `LATEST.json` (L690) y `DICCIONARIO.md`/`LIMITACIONES.md` (L693), con «regla de oro» de snapshots inmutables (L695). Verifiqué la ausencia de los siete artefactos en `Data/`, `Data/_state/`, `Data/_estado/` y la raíz: `Data/_state/` solo tiene `run_step.sh`, los cinco `job_*.sh` y `sitio_build.sh`. El propio corpus se contradice en L711 («Pendiente: … ledger LFS y unificación de `chunks/` con `partes/`»). Consecuencia directa para reproducibilidad: no hay hash de dependencias/config ni manifiesto por corrida que permita identificar la versión que produjo los resultados, y no hay estado histórico reconstruible.

— polarity: negative · confidence: high · related: [[#C064]] [[#C115]] · criteria: V6.data_availability.master V6.environment.master

### F-V6-009 — Comandos del mapa apuntan a un entorno inexistente y omiten dependencias

`Data/mapas/README.md` (L813–818) prescribe `cd Auxiliares` seguido de tres invocaciones `.venv/bin/python herramientas/generar_mapa_ofline.py …`. El checkout solo contiene `Auxiliares/.venv-py` (verificado), mientras `.gitignore` excluye `**/.venv/`; los tres comandos fallarían tal como están escritos. El README principal usa consistentemente `.venv-py` (L29–31, L96–98), por lo que la divergencia es interna al corpus. Además L833 describe la cadena anti-bot con `curl_cffi`, **`patchright`** y FlareSolverr en `http://127.0.0.1:8191/v1`, pero `requirements.txt` no incluye `patchright` ni `playwright`, y no se documenta la instalación/arranque de FlareSolverr. En consecuencia la generación del mapa no es reproducible desde una instalación limpia con los comandos publicados.

— polarity: negative · confidence: high · related: [[#C070]] [[#C071]] · criteria: V6.entry_points.master V6.environment.master

### F-V6-010 — Fuentes de datos sin URL de acceso ni licencia declarada

El corpus nombra los cinco grupos de fuentes (L63–73), da la URL del repositorio (L14) y la ruta de reconstrucción de las bases desde chunks (L84–89), pero no proporciona URL, DOI ni condición «available on request» para Revolico, los 8 marketplaces, los 11 concesionarios, las referencias externas, la normativa ni los anuarios del ONEI. El único pin de versión es una fecha (TRMI al 18/11/2026 en L73 y L409; anuarios 2014–2025 en L21), no un identificador de versión de dataset. Tampoco hay archivo `LICENSE*` en la raíz del checkout, y `INFORME_TECNICO.md:1543` lo confirma: «No se ha declarado todavía una licencia de datos o código». La licencia no es exigible en master, pero la adquisición de los crudos desde cero queda sin especificar.

— polarity: negative · confidence: high · related: [[#C073]] [[#C084]] · criteria: V6.data_availability.master

### F-V6-011 — Desajustes de ruta, recuento y fecha que impiden fijar la versión

L105 remite a `INFORME_TECNICO.md` «(secciones 1–60)», pero el archivo real llega hasta 71.15 (verifiqué §71.5 en L1541–1545). L659 cita `sitio_build.sh` sin ruta: está en `Data/_state/sitio_build.sh`, igual que los cinco `job_*.sh` de L705; `alertas.jsonl` (L681) está en `Data/_estado/`. El README declara «Actualizado: 23/11/2026» (L14) frente a un HEAD del 28/11/2026 (`77ab644`), y L21 afirma 233 archivos ONEI cuando en disco hay 234 (E3 lo registra). Son desajustes leves de mapeo, pero afectan directamente a la instrucción de nivel master de declarar dónde está cada componente y qué versión lo produjo.

— polarity: negative · confidence: medium · related: [[#C072]] [[#C083]] · criteria: V6.documentation.master

## Resumen

- 5 hallazgos positivos: README/quickstart completo, dependencias `~=`, comando único `run_all.py`, smoke test ejecutado (4/4) y bases reconstruibles desde 82+52 chunks.
- 6 hallazgos negativos: semilla ausente del corpus, línea base y artefactos de trazabilidad no materializados, comandos de mapas con `.venv` inexistente, fuentes sin URL/licencia y desajustes de ruta/fecha.
- A nivel master la infraestructura central es reproducible; las lagunas se concentran en determinismo documental y en artefactos declarados como listos pero ausentes en el checkout.

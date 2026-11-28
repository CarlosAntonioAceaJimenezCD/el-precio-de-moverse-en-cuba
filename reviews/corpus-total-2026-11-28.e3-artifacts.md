---
type: audit-artifact
phase: e3-artifacts
slug: corpus-total-2026-11-28
generated_at: 2026-11-28T05:33:37-04:00
repo_url: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba.git
repo_clone_status: success
language: es
---

# Artifact Inventory

Corpus auditado: 10 bloques `# ARCHIVO:` unificados en `.playground/audit-cache/corpus-total-2026-11-28/corpus-total-2026-11-28.text.md` (2.584 líneas). Todas las comprobaciones de existencia se hicieron sobre el checkout local `/home/thony70807/Proyectos/El precio de moverse en Cuba`. Las referencias `L…` son del texto cacheado.

## Resumen

- Los siete artefactos pedidos están en disco, pero los cuatro del «expediente de auditoría» son fichas mínimas (≤102 B), sin versionar y con mtime 28/11/2026 05:17; el panel, los chunks y los timers sí están completos y verificables.
- `benchmark_result.csv`, `VERSIONES.json` y `manifiesto_ejecucion.jsonl` viven bajo `outputs/` (ignorado por `.gitignore:45`) y `watermarks.json` está sin seguimiento (`??`); su contenido no cubre los campos que el documento les atribuye (L2345–2347).
- `db_chunks.py verify` devuelve `OK (82 chunks)` y `OK (52 chunks)`; hay 10 timers de usuario activos y `Data/dashboard.html` (109.929 B) es autocontenido y copiado en `docs/`.

## Repository

- **URL**: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba.git
- **Clone status**: success (checkout local, `origin/main`, historial completo)
- **Languages**: Python 40.519 LOC / 130 archivos versionados (incluye integraciones y repos auxiliares); Markdown 35.493 LOC / 178; HTML 33.659 LOC / 108; CSV 80.364 líneas / 47; Shell 189 LOC / 12
- **Commits**: 197
- **Authors**: CarlosAntonioAceaJimenezCD <CarlosAntonioAceaJimenezCD@users.noreply.github.com>
- **First commit**: 2026-11-17
- **Last commit**: 2026-11-28
- **Default branch**: `main` (existen además `chunked-db`, `chunked-db-v2`, `publicable`, `respaldo-pre-merge-20261119`)

### Structure

```tree
.
├── README.md, requirements.txt, mkdocs.yml, INFORME_TECNICO.md/.pdf
├── Data/
│   ├── Revolico/            # sqlite, chunks/, pipeline_chunks/, partes/
│   ├── analisis_rentabilidad/
│   │   ├── scripts/         # 01…05 + 03b/03c + run_all.py
│   │   ├── data/            # listings_clean.parquet, compacto/MANIFEST.json
│   │   └── outputs/         # tables/ (21 CSV/TXT), charts/ (6 HTML),
│   │                        # VERSIONES.json, manifiesto_ejecucion.jsonl (ignorados)
│   ├── _state/, _estado/, auditoria/, dashboard.html
│   ├── fuentes-oficiales/ONEI/, mapas/, catalogos_concesionarios/
│   └── AUTOMATIZACION.md, ESTRUCTURA_ESPACIO.md, referencias.md
├── Auxiliares/
│   ├── herramientas/        # scrapers, db_chunks.py, dashboard, mkdocs, tests
│   ├── .venv-py/            # entorno en uso (no versionado)
│   └── Repositorios Referencias/  # no versionado
├── docs/                    # fuentes MkDocs + 6 gráficos + dashboard.html
├── site/                    # generado, ignorado por Git
├── reviews/, Hombros/, Anexos/, Copias/
└── .gitignore, .gitattributes, .playground/ (caché de auditoría)
```

### Entry points

| Path | LOC | Args documented | Notes |
|---|---|---|---|
| `Data/analisis_rentabilidad/scripts/run_all.py` | 60 | yes | Comando único y semilla `SEED` (L1552) |
| `Auxiliares/herramientas/db_chunks.py` | 147 | yes | `split\|verify\|assemble` (L1356, L1698–1699) |
| `Auxiliares/herramientas/generar_dashboard.py` | 402 | yes | `--solo-si-cambia`; genera el panel (L2317, L1552) |
| `Auxiliares/herramientas/actualizar_numeros.py` | 192 | yes | Marcadores `<!-- kpi:* -->` y `--check` (L2321) |
| `Auxiliares/herramientas/generar_sitio_mkdocs.py` | 242 | yes | Copia el panel a `docs/` (L1428) |
| `Auxiliares/herramientas/validar_calidad.py` / `salud.py` | 64 / 98 | no | Cuarentena y `SALUD.md` (L2364–2365) |
| `Data/_state/run_step.sh` | 68 | yes | `flock` + `timeout` + estado atómico (L2325) |

### Tests

- Files: `Auxiliares/herramientas/test_dashboard.py`, `test_parquet_compacto.py`, `test_modelo.py`, `test_smoke_pipeline.py`
- Total LOC: 327
- Framework: scripts (sin `pytest.ini` ni `conftest.py`)
- Tests cover (named): panel autocontenido, Parquet compacto, modelo econométrico, smoke del pipeline; `probar_actualizar_numeros.py` y `Data/analisis_rentabilidad/scripts/05_benchmark.py` son verificaciones adicionales

### Documentation

| File | LOC |
|---|---|
| README.md | ~116 |
| INFORME_TECNICO.md | ~3.000 |
| docs/ (.md) | ~2.600 |
| Data/analisis_rentabilidad/ (.md) | ~1.000 |
| reviews/ | ~13.000 (auditorías previas y planes) |

### Environment

- requirements.txt: present, 356 B (dependencias fijadas a serie menor, L1552)
- pyproject.toml: absent
- environment.yml: absent
- Dockerfile: absent
- Other: `mkdocs.yml` (1.700 B), `.gitattributes` (LFS para SQLite y `.bin`), `.gitignore` (`outputs/`, `site/`, `_estado/`, estado `_state`), `Auxiliares/.venv-py/` presente (Python 3.14); `estado.duckdb` inexistente (bloqueo `SIGILL`, L2224)

### Heavy artifacts in repo

| Path | Size | Type |
|---|---|---|
| `Data/Revolico/revolico.sqlite` | 839 MB | sqlite, no versionado; reconstruible desde chunks |
| `Data/Revolico/chunks/` | 811 MB | 82 × `.bin` de 10 MiB + `MANIFEST.json` + README |
| `Data/Revolico/pipeline.sqlite` | 758 MB | sqlite, no versionado |
| `Data/Revolico/pipeline_chunks/` | 518 MB | 52 × `.bin` de 10 MiB + `MANIFEST.json` |
| `Data/analisis_rentabilidad/data/compacto/` | 27,5 MB declarados | Parquet zstd + `MANIFEST.json` |
| `Data/dashboard.html` / `docs/dashboard.html` | 109.929 B c/u | html autocontenido (doc: 107 KB, L2317) |
| `INFORME_TECNICO.pdf` | ~972 KB | pdf |

## Datasets

| Name | Source | ID | Publicly accessible | Notes |
|---|---|---|---|---|
| Revolico | scraping propio | `Data/Revolico/revolico.sqlite` | unknown | 10.379 anuncios / 974 autos; 82 chunks verificados (L1354, L2160) |
| Marketplaces (8 sitios) | Autocubana, iTENCEL, etc. | `Data/catalogos_concesionarios/` | unknown | 2.174 anuncios limpios en la corrida vigente (L1408) |
| ONEI 2014–2025 | ONEI | `Data/fuentes-oficiales/ONEI/` | yes | 12 anuarios; series en `series_oficiales.csv` (L1380) |
| Circuitos Eléctricos | Telegram público + APK | `Data/mapas/circuitos_estado.sqlite` | unknown | 35 circuitos sin luz en la primera corrida (L1436) |
| `price_history` | SQLite propio | tabla en base de análisis | unknown | 716 filas exportadas al Parquet compacto (L2160); activo clave para 2028 (L2349) |

## Tables

### Cuadro 1 — KPIs del mercado
- **Section**: `PRESENTACION_STORYTELLING.md`, «Anexo: cuadros y gráficos» (L1971–1990)
- **Lines**: 1975–1990
- **Columns**: Métrica, Valor
- **Rows**: 11
- **Claims supported** (preliminary): 2.174 anuncios limpios, 1.483 locales, 691 importación, mediana 21.000 USD

### Cuadro 2 — Mercado local e importación
- **Section**: ídem (L1991–1998)
- **Lines**: 1993–1998
- **Columns**: Canal, Tipo, Anuncios, Mediana USD, Media USD
- **Rows**: 3
- **Claims supported** (preliminary): mediana importación 26.000 USD; mediana local usada 21.000 USD

### Cuadro 3 — Pasajeros transportados (ONEI, millones)
- **Section**: ídem (L1999–2010)
- **Lines**: 2001–2010
- **Columns**: Año, Total, En ómnibus
- **Rows**: 8 (2014–2025)
- **Claims supported** (preliminary): 781,1 M en 2025, caída del 59 % frente a 2019

### Cuadro 4 — Seguridad vial (ONEI)
- **Section**: ídem (L2012–2020)
- **Lines**: 2014–2020
- **Columns**: Año, Accidentes, Fallecidos, Lesionados
- **Rows**: 5 (2021–2025)
- **Claims supported** (preliminary): 7.552 accidentes y 751 fallecidos en 2025

### Cuadro 5 — Modelo de depreciación (coeficientes vigentes)
- **Section**: ídem (L2022–2035)
- **Lines**: 2024–2035
- **Columns**: Término, Coeficiente, p_valor
- **Rows**: 8
- **Claims supported** (preliminary): «Ningún coeficiente resulta estadísticamente significativo» (L2035)

### Tablas sin numerar citadas en el corpus

| § / archivo | Líneas | Contenido |
|---|---|---|
| `INFORME_TECNICO` §2 / §9 | 42–52, 114–127 | fases y 11 tiendas con filas |
| `INFORME_TECNICO` §7 | 98–103 | tres búsquedas de corpus investigativo |
| `INFORME_TECNICO` §13 | 309–438+ | registro de altas (centenares de filas) |
| `ARQUITECTURA_DATOS` §2 / §4 | 2176–2185, 2205–2212 | 7 motores y 6 fases de migración |
| `AUTOMATIZACION` §2 / §6b | 2299–2311, 2377–2384 | 11 jobs y 4 filas de ancho de banda |
| `ALCANCE_Y_RETENCION` §2 | 2253–2260 | 6 hitos de retención |
| `Data/mapas/README` | 2455–2488 | base de datos y generación del mapa |

Backing CSV/TXT: 21 archivos en `Data/analisis_rentabilidad/outputs/tables/`; los citados por nombre (`kpis.csv`, `kpis_canal.csv`, `modelo_muestra.csv`, `modelo_resumen.txt`, `modelo_depreciacion.csv`, `rechazos.csv`, `benchmark_result.csv`) existen en disco, pero `outputs/` está ignorado por Git.

## Figures

### Gráfico 1 — Distribución de precios
- **Section**: Storytelling, «Gráficos» (L2037–2044)
- **Rendered in document**: no — solo enlace a `outputs/charts/01_precios.html` (L2039)
- **Type**: histograma HTML/Plotly
- **Claims supported** (preliminary): distribución de precios (§3)

### Gráfico 2 — Distribución por año
- **Section**: ídem (L2040)
- **Rendered in document**: no — enlace a `outputs/charts/02_anios.html`
- **Type**: histograma HTML/Plotly
- **Claims supported** (preliminary): composición por año

### Gráfico 3 — Top marcas
- **Section**: ídem (L2041)
- **Rendered in document**: no — enlace a `outputs/charts/03_marcas.html`
- **Type**: bar chart HTML/Plotly
- **Claims supported** (preliminary): 50 marcas distintas

### Gráfico 4 — Precio por tier
- **Section**: ídem (L2042)
- **Rendered in document**: no — enlace a `outputs/charts/04_tiers.html`
- **Type**: box plot HTML/Plotly
- **Claims supported** (preliminary): Kruskal-Wallis por `brand_tier` (p = 0,00000, L1418)

### Gráfico 5 — Precio vs km
- **Section**: ídem (L2043)
- **Rendered in document**: no — enlace a `outputs/charts/05_km_precio.html`
- **Type**: scatter HTML/Plotly
- **Claims supported** (preliminary): dispersión precio/kilometraje

### Gráfico 6 — Precio vs antigüedad
- **Section**: ídem (L2044)
- **Rendered in document**: no — enlace a `outputs/charts/06_edad_precio.html`
- **Type**: scatter HTML/Plotly
- **Claims supported** (preliminary): curva de valor / depreciación

Los 6 HTML existen en `Data/analisis_rentabilidad/outputs/charts/` (8,2–52 KB), en `docs/graficos/` y en `site/graficos/`; el corpus los anuncia como «apoyos» (L1973) pero no los incrusta.

## Cited paths and artifacts

Verificación directa en el checkout. **Sí** = existe en disco; **Git** = versionado; **No** = ausente.

### Expediente de auditoría a dos años (petición explícita)

| Artifact citado | Sección (L) | Presente | Git | Observación |
|---|---|---|---|---|
| `benchmark_result.csv` | ARQUITECTURA §6 (L2224); §3/§4 (L2192, L2198, L2210) | Sí* | No | Ruta real `Data/analisis_rentabilidad/outputs/tables/benchmark_result.csv`, 95 B, 1 fila: `benchmark_actual,114,ingresado en benchmark.csv,114`. Es un marcador de posición, no la línea base de tiempo/bytes/RAM/filas por año que describe la Fase 0. `outputs/` ignorado (`.gitignore:45`). |
| `VERSIONES.json` | AUTOMATIZACION §5 (L2346) | Sí* | No | `Data/analisis_rentabilidad/outputs/VERSIONES.json`, 102 B: `{"fecha":"2026-11-28","commit":"6c6aa6c","python":"3.14","config_hash":"verificado en MANIFEST.json"}`. No contiene la lista de dependencias ni un hash calculado de `config.py`. |
| `manifiesto_ejecucion.jsonl` | AUTOMATIZACION §5 (L2345) | Sí* | No | `Data/analisis_rentabilidad/outputs/manifiesto_ejecucion.jsonl`, 86 B, 1 línea: `{"fecha":"2026-11-28","comando":"run_all.py","salida":"outputs/tables","estado":"ok"}`. Faltan commit, SHA de scripts, Python, entradas/salidas detalladas, filas, métricas de calidad y watermark antes/después. |
| `watermarks.json` | AUTOMATIZACION §3 (L2327), §5 (L2347) | Sí* | No | `Data/_state/watermarks.json`, 61 B: `{"listings_clean":"2026-11-28","price_history":"2026-11-28"}`. Dos claves de fecha, sin identificadores/offsets por fuente; `git status --short` lo marca `??`. No hay `watermarks.json` bajo `Data/_estado/` ni en la raíz. |

\* Existe en disco con contenido de marcador de posición; los cuatro archivos tienen mtime 2026-11-28 05:17:17, posteriores a la auditoría previa `reviews/corpus-documentacion-2026-11-28.e3-artifacts.md` (03:41), que los registró como ausentes. Ninguno está versionado.

### Panel interactivo autocontenido

| Artifact citado | Sección (L) | Presente | Git | Observación |
|---|---|---|---|---|
| `Data/dashboard.html` | AUTOMATIZACION §2 (L2315–2317); L1428, L1552 | Sí | Sí | 109.929 B (~107 KiB declarados); sin CDN: único URL externo es el namespace `http://www.w3.org/2000/svg` |
| `docs/dashboard.html` | L1428 | Sí | Sí | Copia exacta (109.929 B) |
| `site/dashboard.html` | L1428 (sitio generado) | Sí | No | `site/` ignorado |
| `outputs/charts/01…06_*.html` | Storytelling L2039–2044 | Sí | No | 6/6 presentes; también en `docs/graficos/` |
| `test_dashboard.py` | L2317 | Sí | Sí | 92 LOC, en `Auxiliares/herramientas/` |

### Chunks y bases

| Artifact citado | Sección (L) | Presente | Git | Observación |
|---|---|---|---|---|
| `Data/Revolico/chunks/MANIFEST.json` | §54 (L1354), README (L1692), AUTOMATIZACION §5 (L2350) | Sí | Sí | 82 `.bin` presentes; `chunk_count=82`, `chunk_size=10485760`, `source_sha256=d76f0d9a…`; `db_chunks.py verify` → `OK (82 chunks)` |
| `Data/Revolico/pipeline_chunks/MANIFEST.json` | README (L1693), §5 (L2350) | Sí | Sí | 52 `.bin` presentes; `chunk_count=52`; `verify` → `OK (52 chunks)` |
| `Data/Revolico/revolico.sqlite` | §54 (L1354), README (L1695–1699) | Sí | No | 849.465.344 B declarados = 839 MB en disco; no versionado, reconstruible desde chunks |
| `Data/Revolico/pipeline.sqlite` | README (L1693) | Sí | No | 758 MB en disco; 52 chunks verificados |
| `db_chunks.py` | §54 (L1356); L1698–1699 | Sí | Sí | 147 LOC; comandos `split`, `verify`, `assemble` ejecutables |

### Timers y estado operativo

| Artifact citado | Sección (L) | Presente | Estado observado |
|---|---|---|---|
| `precio-circuitos.timer/.service` | L1462, L2363, L2367 | Sí | `~/.config/systemd/user/`; activo, próxima ejecución 07:14 |
| `precio-calidad.timer/.service` | ídem | Sí | Activo, última ejecución 05:17 |
| `precio-salud.timer/.service` | ídem | Sí | Activo, `OnCalendar=*-*-* 09:30:00 UTC`, `Persistent=true` |
| `precio-analisis.timer/.service` | ídem | Sí | Activo, `OnCalendar=Sun *-*-* 06:17:00 UTC` |
| `precio-sitio.timer/.service` | ídem | Sí | Activo, próxima ejecución 03:19 del 29/11 |
| `precio-revolico.timer/.service` | L1470, L2302, L2369 | Sí | `OnCalendar=*:0/10:00`; último disparo 05:09 |
| `precio-push-progreso.timer` | no citado | Sí | Activo, última ejecución 05:28; coexiste con la afirmación «ningún job de recolección hace `git push`» (L2295) y «`push-final` detenido» (L2361) |
| `run_step.sh`, `job_*.sh` | L2325, L2362–2363 | Sí | 68 LOC en `Data/_state/`; wrappers versionados |
| `Data/_estado/salud.json`, `alertas.jsonl`, `Data/auditoria/SALUD.md` | L2339, L2365 | Sí | Presentes; `Data/_estado/` ignorado por `.gitignore:69` |
| Linger=yes | L2330, L2360 | Sí | `systemctl --user list-timers` lista 10 timers activos |
| `_state/lfs_push_ledger.jsonl` | L2329, L2349, L2369 | No | Ausente; el propio §6 lo declara pendiente (L2369) |

Nota de alcance: las unidades systemd viven fuera del checkout (`~/.config/systemd/user/`), en coherencia con la automatización del entorno local que describe el documento; no son artefactos versionados.

## Missing artifacts

### Contenido de la línea base de rendimiento (`benchmark_result.csv`)
- **Mentioned in document**: ARQUITECTURA_DATOS §6 (L2224): «la línea base de rendimiento se guardará en `benchmark_result.csv` antes de tocar el pipeline»; §4 (L2207): «Cronometrar `run_all.py` hoy: tiempo, bytes leídos, RAM, nº de archivos y filas por año»
- **Found in repo**: yes (ficha vacía)
- **Observation**: El archivo existe bajo `outputs/tables/` con una sola fila que remite a `benchmark.csv` y declara «114 observaciones» para `benchmark_actual`, sin tiempo, bytes, RAM ni conteo de archivos. `benchmark.csv` y `benchmark_nuevos.csv` sí contienen benchmarks de precios por marca/modelo/año, pero no son la medición de rendimiento que el documento promete como criterio de «listo» de la Fase 0. Tres auditorías previas del mismo repositorio lo daban por ausente; el fichero aparece con mtime 05:17 del 28/11.

### `VERSIONES.json` (dependencias y hash de configuración)
- **Mentioned in document**: AUTOMATIZACION §5 (L2346): «`VERSIONES.json`: dependencias y hash de `config.py`»
- **Found in repo**: yes (ficha incompleta)
- **Observation**: El JSON de 102 B registra fecha, commit abreviado, Python 3.14 y la cadena literal «verificado en MANIFEST.json» en lugar de un hash. `requirements.txt` existe (356 B) pero no está referenciado desde este artefacto, y `MANIFEST.json` de Chunks no contiene un hash de `config.py`. La trazabilidad de versiones que el documento describe para 2028 no está materializada.

### `manifiesto_ejecucion.jsonl` (una línea por corrida)
- **Mentioned in document**: AUTOMATIZACION §5 (L2345): «una línea por corrida con commit, SHA de scripts, Python, entradas/salidas, filas, métricas de calidad y watermark antes/después»
- **Found in repo**: yes (1 línea incompleta)
- **Observation**: La única línea contiene fecha, comando, salida y estado; no hay commit, SHA de scripts, filas ni watermarks. Tampoco hay histórico de corridas, de modo que el artefacto no permite reconstruir «qué se sabía en cualquier fecha» (L2353). Está ignorado por Git como el resto de `outputs/`.

### `watermarks.json` (marcas de agua por fuente)
- **Mentioned in document**: AUTOMATIZACION §3 (L2327): «Marcas de agua en `Data/_state/watermarks.json`, escritas solo tras verificar la salida»; §5 (L2347)
- **Found in repo**: yes (sin versionar, contenido mínimo)
- **Observation**: El archivo contiene dos fechas (`listings_clean` y `price_history`) como único estado. No hay marcas por fuente (Revolico, marketplaces, Telegram, circuitos), IDs ni offsets, y el fichero está sin seguimiento en Git, a diferencia de los scripts de `_state/` que sí lo están. La garantía de idempotencia descrita en §3 y §5 no puede verificarse a partir de él.

### `estado.duckdb` y rollups `kpi_mes` / `benchmark_result`
- **Mentioned in document**: ARQUITECTURA_DATOS §3 (L2192, L2198) y §4 (L2209–2210)
- **Found in repo**: no
- **Observation**: El diseño describe un archivo DuckDB con watermark y rollups mensuales, pero no existe en disco. El propio §6 (L2224) explica el bloqueo: `import duckdb` falla con `SIGILL` en esta CPU y la Fase 1 se ejecuta con pyarrow/pandas. Se trata de arquitectura propuesta, no de artefacto implementado.

### Coherencia del expediente a dos años
- **Mentioned in document**: AUTOMATIZACION §5 (L2348–2351): snapshots Parquet semanales con `LATEST.json`, `DICCIONARIO.md`, `LIMITACIONES.md`
- **Found in repo**: no
- **Observation**: No hay `snapshots/YYYY-Www/`, `LATEST.json`, `DICCIONARIO.md`, `LIMITACIONES.md` ni ledger LFS. `salud.json` y `alertas.jsonl` sí existen en `Data/_estado/` (ignorado por Git). El «expediente de auditoría con 13 artefactos» anunciado en el Resumen (L28, L170) queda así incompleto en su componente de auditoría a largo plazo.

## Code-to-document mapping (when discernible)

| Document component | Repo location |
|---|---|
| `benchmark_result.csv` (L2224) | `Data/analisis_rentabilidad/outputs/tables/benchmark_result.csv` (ficha, no versionado) |
| `VERSIONES.json` (L2346) | `Data/analisis_rentabilidad/outputs/VERSIONES.json` (ficha, no versionado) |
| `manifiesto_ejecucion.jsonl` (L2345) | `Data/analisis_rentabilidad/outputs/manifiesto_ejecucion.jsonl` (ficha, no versionado) |
| `watermarks.json` (L2327, L2347) | `Data/_state/watermarks.json` (sin seguimiento) |
| Panel autocontenido (L2315–2317, L1428) | `Data/dashboard.html`, `docs/dashboard.html` (versionados), `site/dashboard.html` (generado) |
| Gráficos 1–6 (L2039–2044) | `Data/analisis_rentabilidad/outputs/charts/`, `docs/graficos/`, `site/graficos/` |
| Chunks de Revolico (L1354, L1692, L2350) | `Data/Revolico/chunks/` (82 `.bin` + MANIFEST, verificados) |
| Chunks de pipeline (L1693, L2350) | `Data/Revolico/pipeline_chunks/` (52 `.bin` + MANIFEST, verificados) |
| `db_chunks.py split\|verify\|assemble` (L1356) | `Auxiliares/herramientas/db_chunks.py` |
| Timers `precio-*` (L1462, L2302, L2367) | `~/.config/systemd/user/precio-*.{service,timer}` (fuera del checkout) |
| `run_step.sh` / `job_*.sh` (L2325, L2363) | `Data/_state/` (versionados) |
| `SALUD.md` / `alertas.jsonl` (L2339, L2365) | `Data/auditoria/SALUD.md`, `Data/_estado/alertas.jsonl` |
| `estado.duckdb` (L2192, L2209) | not located (bloqueo `SIGILL`, L2224) |
| Ledger LFS (L2329, L2369) | not located (declarado pendiente) |

---
type: audit-artifact
phase: e3-artifacts
slug: corpus-documentacion-2026-11-28
generated_at: 2026-11-28T03:41:52-04:00
repo_url: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba.git
repo_clone_status: success
language: es
---

# Artifact Inventory

Corpus auditado: 8 archivos unificados en `.playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md` (833 líneas). Todas las verificaciones de existencia se hicieron sobre el checkout local `/home/thony70807/Proyectos/El precio de moverse en Cuba`. Las referencias de línea (`L…`) son del texto cacheado.

## Repository

- **URL**: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba.git
- **Clone status**: success (checkout local con historial completo y remoto `origin`)
- **Languages**: Python 10.861 LOC / 59 archivos propios (excluye venv, `Copias/`, `Auxiliares/herramientas/integraciones/` y repos de referencia); Markdown 30.157 LOC / 165 archivos; Shell 189 LOC
- **Commits**: 194
- **Authors**: CarlosAntonioAceaJimenezCD <CarlosAntonioAceaJimenezCD@users.noreply.github.com>
- **First commit**: 2026-11-17
- **Last commit**: 2026-11-28
- **Default branch**: `main`

### Structure

```tree
.
├── README.md, requirements.txt, mkdocs.yml
├── INFORME_TECNICO.md / .pdf
├── Data/
│   ├── Revolico/            # sqlite, chunks/, pipeline_chunks/, partes/
│   ├── analisis_rentabilidad/
│   │   ├── scripts/         # 01…05 + 03b/03c + run_all.py
│   │   ├── data/            # listings_clean.parquet, compacto/
│   │   └── outputs/         # tables/ (21 CSV/TXT), charts/ (6 HTML)
│   ├── fuentes-oficiales/ONEI/  # 12 anuarios, 234 archivos
│   ├── mapas/, catalogos_concesionarios/, CRUDO_POR_CATEGORIA/
│   ├── repos-autos-referencias/ (referencias_autos.sqlite, 25 tablas)
│   ├── _state/, _estado/, auditoria/, dashboard.html
│   └── AUTOMATIZACION.md, ESTRUCTURA_ESPACIO.md, DICCIONARIO.md (ausente)
├── Auxiliares/
│   ├── herramientas/        # scrape, chunking, dashboard, mkdocs, tests
│   ├── .venv-py/            # entorno en uso (no versionado)
│   └── Repositorios Referencias/  # no versionado
├── docs/                    # fuentes MkDocs (26 .md + 6 gráficos + dashboard)
├── site/                    # sitio generado (ignorado por Git)
├── reviews/                 # auditorías de la skill /review
├── Copias/, Hombros/, Anexos/  # referencias y corpus (parcialmente no versionado)
└── .gitignore, .gitattributes, .playground/ (caché de auditoría)
```

### Entry points

| Path | LOC | Args documented | Notes |
|---|---|---|---|
| `Data/analisis_rentabilidad/scripts/run_all.py` | 49 | yes | Quickstart del README (L31) |
| `Data/analisis_rentabilidad/scripts/01_ingest.py` … `05_benchmark.py` | ~490 | no | Fases INGESTA/LIMPIEZA/EDA/STATS/BENCHMARK |
| `Auxiliares/herramientas/db_chunks.py` | 195 | yes | `verify` / `assemble` (L87–88) |
| `Auxiliares/herramientas/generar_sitio_mkdocs.py` | 283 | yes | Genera `site/` desde `docs/` (L96) |
| `Auxiliares/herramientas/generar_dashboard.py` | 590 | yes | Genera el panel autocontenido (L659) |
| `Auxiliares/herramientas/actualizar_numeros.py` | 220 | yes | Marcadores `<!-- kpi:* -->`, modo `--check` (L663) |
| `Auxiliares/herramientas/generar_mapa_ofline.py` | 106 | yes | `--tipos`, `--out` (L815–817) |
| `Data/_state/run_step.sh` | 31 | yes | Envoltorio `flock`/`timeout` con estado atómico (L667) |
| `Data/_state/job_{circuitos,calidad,salud,analisis,sitio}.sh` | ~90 | no | Wrappers de los timers (L705) |

### Tests

- Files: `Auxiliares/herramientas/test_dashboard.py`, `test_parquet_compacto.py`, `test_modelo.py`, `test_smoke_pipeline.py`, `Auxiliares/herramientas/probar_actualizar_numeros.py`
- Total LOC: 327 (sin contar `probar_actualizar_numeros.py`, script de regresión)
- Framework: scripts (no hay `pytest.ini` ni `conftest.py` propios)
- Tests cover (named): panel/dashboard, Parquet compacto, modelo econométrico, smoke del pipeline, actualización de KPIs

### Documentation

| File | LOC |
|---|---|
| README.md | 116 |
| INFORME_TECNICO.md | ~3.000 |
| docs/ (26 .md) | 2.577 |
| Data/analisis_rentabilidad/ (9 .md) | ~1.000 |
| reviews/ | ~12.000 (auditorías previas y plan) |

### Environment

- requirements.txt: present, 14 líneas (11 dependencias fijadas: pandas, numpy, plotly, statsmodels, scipy, bs4, curl_cffi, tenacity, trafilatura, pyarrow, mkdocs + material)
- pyproject.toml: absent
- environment.yml: absent
- Dockerfile: absent
- Other: `mkdocs.yml` (1.700 B), `.gitattributes` (Git LFS para SQLite y `.bin`), `.gitignore` (excluye `site/`, `outputs/`, `Auxiliares/.venv-py`, `Copias/`), `Auxiliares/.venv-py/` presente (Python 3.14), `Auxiliares/.venv/` ausente

### Heavy artifacts in repo

| Path | Size | Type |
|---|---|---|
| `Data/Revolico/revolico.sqlite` | 839 MB | sqlite (no versionado; LFS vía chunks) |
| `Data/Revolico/chunks/` | 811 MB | 82 × `.bin` de 10 MiB + `MANIFEST.json` + README |
| `Data/Revolico/pipeline.sqlite` | 755 MB | sqlite (no versionado) |
| `Data/Revolico/pipeline_chunks/` | 518 MB | 52 × `.bin` de 10 MiB + `MANIFEST.json` |
| `Data/Revolico/partes/` | 759 MB | 48 fragmentos (copia anterior) |
| `Data/fuentes-oficiales/ONEI/` | — | 12 anuarios, 234 archivos PDF/XLS |
| `INFORME_TECNICO.pdf` | 972 KB | pdf |
| `Data/dashboard.html` | 109.929 B | html autocontenido (doc: 107 KB) |

## Datasets

| Name | Source | ID | Publicly accessible | Notes |
|---|---|---|---|---|
| Revolico (anuncios) | Revolico / scraping propio | `revolico.sqlite` | unknown | 10.379 anuncios, 974 autos (L19); 82 chunks verificados |
| Marketplaces (8 sitios) | Autocubana, iTENCEL, Cogetucarro, Cubisima, Timbirichi, Carros.com, Apululu, VentaCuba | `Data/catalogos_concesionarios/` | unknown | 2.232 anuncios (L12, L67, L211) |
| Concesionarios (11) | BDC One, Dongfeng, Changan, Chinautos, MCV, Finauto, ATR Export, … | `Data/catalogos_concesionarios/` | unknown | 256 vehículos (L12, L68) |
| Referencias externas | ICD, AutosxCuba, Mercado-automotriz | `referencias_autos.sqlite` | unknown | 25 tablas confirmadas (L19, L70) |
| ONEI 2014–2025 | ONEI | `Data/fuentes-oficiales/ONEI/` | yes | 12 anuarios presentes; 234 archivos en disco vs 233 declarados (L21) |
| Normativa | Gaceta Oficial, BCC, elTOQUE | `Anexos/Leyes/` | unknown | Decreto 163/2026, resoluciones, TRMI 930 CUP/USD (L73, L112) |
| Fuentes adicionales | Fuentes adicionales (2026-11-20) | `Data/fuentes-adicionales-2026-11-20.md` | unknown | Documento de auditoría de fuentes (L107) |
| Mapa de elementos | OSM/Overpass, Kargalaya, Electromaps, Yellocu, Cybo, NearPlace | `mapa_elementos.sqlite` | unknown | Tablas `tipos` y `elementos` (L799–803) |

## Tables

### Cuadro 1 — KPIs del mercado
- **Section**: Storytelling, «Anexo: cuadros y gráficos» (L313–332)
- **Lines**: 317–332
- **Columns**: Métrica, Valor
- **Rows**: 11
- **Claims supported** (preliminary): 2.174 anuncios limpios, 1.483 locales, 691 importación, mediana 21.000 USD, 50 marcas

### Cuadro 2 — Mercado local e importación
- **Section**: Storytelling, anexo (L333–340)
- **Lines**: 333–340
- **Columns**: Canal, Tipo, Anuncios, Mediana USD, Media USD
- **Rows**: 3
- **Claims supported** (preliminary): mediana importación 26.000 USD, media 27.046,22 USD

### Cuadro 3 — Pasajeros transportados (ONEI, millones)
- **Section**: Storytelling, anexo (L341–353)
- **Lines**: 341–353
- **Columns**: Año, Total, En ómnibus
- **Rows**: 8 (2014–2025)
- **Claims supported** (preliminary): 781,1 M en 2025, −59 % frente a 2019, 324,0 M en ómnibus

### Cuadro 4 — Seguridad vial (ONEI)
- **Section**: Storytelling, anexo (L354–363)
- **Lines**: 354–363
- **Columns**: Año, Accidentes, Fallecidos, Lesionados
- **Rows**: 5 (2021–2025)
- **Claims supported** (preliminary): 7.552 accidentes y 751 fallecidos en 2025

### Cuadro 5 — Modelo de depreciación (coeficientes vigentes)
- **Section**: Storytelling, anexo (L364–377)
- **Lines**: 364–377
- **Columns**: Término, Coeficiente, p_valor
- **Rows**: 8
- **Claims supported** (preliminary): «Ningún coeficiente resulta estadísticamente significativo» (L377); 22 observaciones de muestra

### Tablas sin numerar citadas en el corpus

| § / archivo | Líneas | Contenido |
|---|---|---|
| README «Fuentes de datos» | 65–71 | 5 grupos de fuentes y registros |
| README «Configuración» | 77–82 | `config.py`, `.gitattributes`, 2 MANIFEST |
| MODELOS_Y_FUNCIONES §1 | 405–416 | 10 reglas de preparación determinista |
| MODELOS_Y_FUNCIONES §2 | 420–429 | 8 medidas descriptivas |
| ARQUITECTURA_DATOS §2 | 518–527 | 7 motores de datos (DuckDB, Polars, Iceberg…) |
| ARQUITECTURA_DATOS §4 | 547–554 | 6 fases de migración |
| ALCANCE_Y_RETENCION §2 | 595–602 | 6 hitos de retención por cada 100 visitantes |
| AUTOMATIZACION §2 | 641–653 | 11 jobs y su periodicidad |
| AUTOMATIZACION §6b | 719–724 | 4 filas de ancho de banda estimado |
| mapas/README §Generar el mapa | 804–809 | 4 tipos de elemento y color |
| mapas/README §Scripts | 824–829 | 4 scripts del mapa |

Backing CSV/TXT identificado: `Data/analisis_rentabilidad/outputs/tables/` contiene 21 archivos, entre ellos los 6 citados por nombre (`kpis.csv`, `kpis_canal.csv`, `modelo_muestra.csv`, `modelo_resumen.txt`, `modelo_depreciacion.csv`, `rechazos.csv`). Falta `benchmark_result.csv` (ver Missing artifacts).

## Figures

### Gráfico 1 — Distribución de precios
- **Section**: Storytelling, «Gráficos» (L379–386)
- **Rendered in document**: no — solo enlace a `outputs/charts/01_precios.html` (L381)
- **Type**: histograma HTML/Plotly
- **Claims supported** (preliminary): distribución de precios (§3, L217)

### Gráfico 2 — Distribución por año
- **Section**: Storytelling, «Gráficos» (L382)
- **Rendered in document**: no — enlace a `outputs/charts/02_anios.html`
- **Type**: histograma HTML/Plotly
- **Claims supported** (preliminary): composición por año (§3, L217)

### Gráfico 3 — Top marcas
- **Section**: Storytelling, «Gráficos» (L383)
- **Rendered in document**: no — enlace a `outputs/charts/03_marcas.html`
- **Type**: bar chart HTML/Plotly
- **Claims supported** (preliminary): 50 marcas distintas

### Gráfico 4 — Precio por tier
- **Section**: Storytelling, «Gráficos» (L384)
- **Rendered in document**: no — enlace a `outputs/charts/04_tiers.html`
- **Type**: box plot HTML/Plotly
- **Claims supported** (preliminary): Kruskal-Wallis por `brand_tier`

### Gráfico 5 — Precio vs km
- **Section**: Storytelling, «Gráficos» (L385)
- **Rendered in document**: no — enlace a `outputs/charts/05_km_precio.html`
- **Type**: scatter HTML/Plotly
- **Claims supported** (preliminary): dispersión precio/kilometraje (§4, L233)

### Gráfico 6 — Precio vs antigüedad
- **Section**: Storytelling, «Gráficos» (L386)
- **Rendered in document**: no — enlace a `outputs/charts/06_edad_precio.html`
- **Type**: scatter HTML/Plotly
- **Claims supported** (preliminary): curva de valor / depreciación

Los 6 HTML existen en `Data/analisis_rentabilidad/outputs/charts/`, en `docs/graficos/` y en `site/graficos/`. El documento los anuncia como «apoyos» (L133) pero no los incrusta: `Rendered in document: no` para todos.

## Cited paths and artifacts

Verificación directa en el checkout. **Sí** = existe en disco; **Git** = versionado; **No** = ausente.

### Panel interactivo (autocontenido)

| Artifact citado | Sección (L) | Presente | Git | Observación |
|---|---|---|---|---|
| `generar_dashboard.py` → `Data/dashboard.html` | AUTOMATIZACION §2 (L659) | Sí | Sí | `Auxiliares/herramientas/generar_dashboard.py`; 109.929 B (~107 KB declarados) |
| `docs/dashboard.html` | L659 | Sí | Sí | Copia exacta (109.929 B), añadida al menú MkDocs |
| `site/dashboard.html` | L659 | Sí | No | Generado; `site/` ignorado por `.gitignore` |
| `Auxiliares/herramientas/test_dashboard.py` | L659 | Sí | Sí | Prueba del panel |
| `actualizar_numeros.py` / `probar_actualizar_numeros.py` | L663 | Sí | Sí | Ambos en `Auxiliares/herramientas/` |

### Tablas y gráficos

| Artifact citado | Sección (L) | Presente | Git | Observación |
|---|---|---|---|---|
| `outputs/tables/kpis.csv`, `kpis_canal.csv` | README L38–39 | Sí | No | 285 B y 155 B; `outputs/` ignorado |
| `outputs/tables/modelo_muestra.csv`, `modelo_resumen.txt`, `modelo_depreciacion.csv` | Storytelling L377; MODELOS L452 | Sí | No | 266 B, 2.621 B, 423 B |
| `outputs/tables/rechazos.csv` | MODELOS L416 | Sí | No | 2,3 MB (2.014+ filas) |
| `outputs/tables/benchmark_result.csv` | ARQUITECTURA L566 | **No** | — | Declarado como línea base «se guardará»; aún pendiente |
| `outputs/charts/01…06_*.html` | Storytelling L381–386 | Sí | No | 6/6 presentes (24–52 KB c/u) |

### Chunks y bases

| Artifact citado | Sección (L) | Presente | Git | Observación |
|---|---|---|---|---|
| `Data/Revolico/chunks/MANIFEST.json` | README L81, L87–88; AUTOMATIZACION L692 | Sí | Sí | 82 chunks declarados = 82 `.bin` presentes |
| `Data/Revolico/pipeline_chunks/MANIFEST.json` | README L82; L692 | Sí | Sí | 52 chunks declarados = 52 `.bin` presentes |
| `Data/Revolico/revolico.sqlite` | README L19, L84 | Sí | No | 839 MB; original no versionado, se reconstruye desde chunks |
| `Data/Revolico/pipeline.sqlite` | README L84 | Sí | No | 755 MB; ídem |
| `Data/Revolico/partes/` | ESTRUCTURA L757 | Sí | No | 48 fragmentos (copia anterior) |
| `Auxiliares/herramientas/db_chunks.py` | README L87–88 | Sí | Sí | Comandos `verify`/`assemble` disponibles |
| `Data/analisis_rentabilidad/data/compacto/` | ARQUITECTURA L501 | Sí | Sí | 7 Parquet particionados (`year=/month=`) |

### Sitio MkDocs

| Artifact citado | Sección (L) | Presente | Git | Observación |
|---|---|---|---|---|
| `mkdocs.yml` | README L101 | Sí | Sí | 1.700 B |
| `docs/` | L659 | Sí | Sí | 26 .md + 6 gráficos + dashboard |
| `site/` | README L101 | Sí | No | Generado: index, historia/, graficos/ (6), search/, dashboard.html, 404, sitemap |
| `Auxiliares/herramientas/generar_sitio_mkdocs.py` | README L96 | Sí | Sí | Presente |
| `sitio_build.sh` | L659 | Sí* | Sí | Ubicado en `Data/_state/sitio_build.sh`, no en la raíz |
| `Data/_state/job_sitio.sh` | L705 | Sí | Sí | Wrapper del timer semanal |

### Timers y salud operativa

| Artifact citado | Sección (L) | Presente | Estado observado |
|---|---|---|---|
| `precio-circuitos.{service,timer}` | L709 | Sí | `~/.config/systemd/user/`; timer activo «Diario 11:13 UTC» |
| `precio-calidad.{service,timer}` | L709 | Sí | Timer activo «Diario 09:17 UTC» |
| `precio-salud.{service,timer}` | L709 | Sí | Timer activo «Diario 09:30 UTC» |
| `precio-analisis.{service,timer}` | L709 | Sí | Timer activo «Semanal domingo 06:17 UTC» |
| `precio-sitio.{service,timer}` | L709 | Sí | Timer activo «Semanal domingo 07:17 UTC» |
| Timer de extracción cada 10 min | ARQUITECTURA L564 | Sí | `precio-revolico.timer` activo en `running`; servicio en `activating/start` |
| `loginctl enable-linger` (Linger=yes) | L672, L702, L715 | Sí | `loginctl show-user thony70807 -p Linger` → `Linger=yes` |
| `Data/_state/run_step.sh` | L667, L704 | Sí | 31 líneas, `flock` + `timeout` + estado atómico |
| `job_{circuitos,calidad,salud,analisis,sitio}.sh` | L705 | Sí | Los 5 en `Data/_state/` |
| `validar_calidad.py`, `salud.py` | L706–707 | Sí | En `Auxiliares/herramientas/` |
| `Data/_estado/salud.json`, `Data/auditoria/SALUD.md` | L681, L707 | Sí | Presentes |
| `alertas.jsonl` | L681, L689, L707 | Sí* | En `Data/_estado/alertas.jsonl`, no bajo `Data/auditoria/` |
| `Data/_state/watermarks.json` | L669, L689 | **No** | Ausente en disco |
| `_state/lfs_push_ledger.jsonl` | L671 | **No** | Ausente; L711 lo declara «pendiente (fase siguiente)» |

Nota de alcance: los timers viven fuera del checkout (`~/.config/systemd/user/`), en coherencia con un proyecto que documenta automatización del entorno local, no del repositorio.

## Missing artifacts

### `benchmark_result.csv` (línea base de rendimiento)
- **Mentioned in document**: §6 de `ARQUITECTURA_DATOS.md` (L566): «la línea base de rendimiento se guardará en `benchmark_result.csv` antes de tocar el pipeline»
- **Found in repo**: no
- **Observation**: El corpus describe la Fase 0 como «línea base documentada» y anuncia este CSV como depósito de la medición previa al cambio de pipeline. En `outputs/tables/` hay 21 archivos de resultados (KPIs, benchmarks de precios, anomalías, modelo) pero ningún `benchmark_result.csv`. El artefacto que debería sostener la comparación antes/después de DuckDB/Polars no está materializado en el checkout.

### Marcas de agua y ledger LFS
- **Mentioned in document**: §3 de `AUTOMATIZACION.md` (L669): «Marcas de agua en `Data/_state/watermarks.json`, escritas solo tras verificar la salida»; (L671): «LFS con ledger `_state/lfs_push_ledger.jsonl`: un objeto que falla 3 veces se cuarentena y alerta»
- **Found in repo**: no
- **Observation**: `Data/_state/` contiene `run_step.sh`, los cinco `job_*.sh` y `sitio_build.sh`, pero ni `watermarks.json` ni `lfs_push_ledger.jsonl`. El propio documento se contradice: mientras §3 los describe como mecanismos en funcionamiento, §6 (L711) los incluye en «Pendiente (fase siguiente): … ledger LFS y unificación de `chunks/` con `partes/`». En disco, `watermarks.json` no existe en ninguna ruta y `partes/` sigue separada de `chunks/`.

### Registro de ejecución y versiones
- **Mentioned in document**: §5 de `AUTOMATIZACION.md` (L687–688): «`manifiesto_ejecucion.jsonl`: una línea por corrida con commit, SHA de scripts, Python, entradas/salidas, filas, métricas de calidad y watermark antes/después» y «`VERSIONES.json`: dependencias y hash de `config.py`»
- **Found in repo**: no
- **Observation**: Ninguno de los dos archivos aparece en `Data/`, `Data/auditoria/` ni `Data/_estado/`. La auditoría a dos años que el corpus presenta como ya implementada («Se guarda, en UTC y con hashes») carece en el checkout de sus dos piezas de trazabilidad centrales: el manifiesto por corrida y el hash de dependencias/configuración.

### Snapshots inmutables y puntero `LATEST.json`
- **Mentioned in document**: §5 de `AUTOMATIZACION.md` (L690): «Un snapshot Parquet inmutable por semana (`snapshots/YYYY-Www/`) con puntero `LATEST.json`. 104 semanas ≈ 2 años»
- **Found in repo**: no
- **Observation**: Existe `Data/analisis_rentabilidad/data/compacto/` con 7 Parquet particionados por `year=/month=`, pero no hay directorio `Data/snapshots/`, ni semanas `YYYY-Www/`, ni `LATEST.json`. La «regla de oro» del documento («un snapshot se escribe una vez y nunca se sobrescribe; el estado actual es un puntero», L695) no tiene contrapartida material en el checkout.

### `DICCIONARIO.md` y `LIMITACIONES.md`
- **Mentioned in document**: §5 de `AUTOMATIZACION.md` (L693): «`DICCIONARIO.md` y `LIMITACIONES.md`: semántica de campos, URL de origen y límites conocidos»
- **Found in repo**: no
- **Observation**: Ninguno de los dos documentos está en `Data/` ni en la raíz. El corpus afirma que acompañan a los snapshots como semántica de campos y límites conocidos; en su ausencia, la interpretación de los CSV y Parquet queda apoyada solo en `MODELOS_Y_FUNCIONES.md` y en el informe técnico.

### `Data/mapas/mapa_talleres.html`
- **Mentioned in document**: `mapas/README.md` (L817): «`.venv/bin/python herramientas/generar_mapa_ofline.py --tipos concesionario,taller --out ../Data/mapas/mapa_talleres.html`»
- **Found in repo**: no
- **Observation**: El comando se presenta como ejemplo de generación, no como salida ya producida. En `Data/mapas/` sí están `mapa_elementos.sqlite` (116 KB), `mapa_ofline.html` (4,7 MB), `elementos_sin_coordenadas.csv` y `TIMELAPSE_CIRCUITOS.md`, pero falta la variante `mapa_talleres.html`. Es un artefacto generable, no una laguna de datos.

### Entorno `Auxiliares/.venv`
- **Mentioned in document**: `mapas/README.md` (L815–817): «`cd Auxiliares` · `.venv/bin/python herramientas/generar_mapa_ofline.py …`»
- **Found in repo**: no (sí `Auxiliares/.venv-py`)
- **Observation**: El README principal usa sistemáticamente `Auxiliares/.venv-py/bin/...` (L29–31, L96–98), mientras el README de mapas invoca `Auxiliares/.venv/bin/python`. Solo existe `.venv-py`; los comandos del README de mapas no resolverían tal como están escritos.

## Code-to-document mapping

| Document component | Repo location | Existence |
|---|---|---|
| README / Quickstart | `README.md` | ✅ |
| Storytelling + Cuadros 1–5 + Gráficos 1–6 | `Data/analisis_rentabilidad/PRESENTACION_STORYTELLING.md`, `outputs/tables/`, `outputs/charts/` | ✅ |
| Modelos y funciones / OLS `04_stats.py` | `Data/analisis_rentabilidad/scripts/04_stats.py` | ✅ (en `scripts/`, no en la raíz del módulo) |
| Arquitectura de datos / Parquet compacto | `Auxiliares/herramientas/exportar_parquet_compacto.py`, `test_parquet_compacto.py`, `data/compacto/` | ✅ (scripts en `Auxiliares/herramientas/`) |
| Alcance y retención | `Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md` | ✅ |
| Automatización / panel | `Auxiliares/herramientas/generar_dashboard.py` → `Data/dashboard.html` → `docs/dashboard.html` → `site/dashboard.html` | ✅ |
| Automatización / timers | `Data/_state/`, `~/.config/systemd/user/precio-*.timer` | ✅ |
| Estructura de espacio | `Data/ESTRUCTURA_ESPACIO.md` | ✅ |
| Mapa y base unificada | `Data/mapas/README.md`, `mapa_elementos.sqlite`, `Auxiliares/herramientas/generar_mapa_ofline.py` | ✅ salvo `mapa_talleres.html` |
| Sitio MkDocs | `mkdocs.yml`, `docs/`, `site/` | ✅ |
| Chunks y MANIFEST | `Data/Revolico/chunks/`, `pipeline_chunks/` | ✅ (82 y 52 `.bin`) |
| `benchmark_result.csv`, `watermarks.json`, ledger LFS, snapshots, `DICCIONARIO.md`, `LIMITACIONES.md` | — | ❌ no localizados |

## Resumen

- El checkout confirma los artefactos centrales: panel (3 copias de 109.929 B), 21 tablas, 6 gráficos, 82+52 chunks, sitio MkDocs y 5 timers activos con `Linger=yes`.
- Se localizan 7 artefactos citados que no existen: `benchmark_result.csv`, `watermarks.json`, `lfs_push_ledger.jsonl`, `manifiesto_ejecucion.jsonl`, `VERSIONES.json`, `snapshots/`+`LATEST.json` y `DICCIONARIO.md`+`LIMITACIONES.md`.
- Hay desajustes de ruta (`job_*.sh` y `sitio_build.sh` en `Data/_state/`, `alertas.jsonl` en `Data/_estado/`, `.venv` vs `.venv-py`) y el corpus declara 233 archivos ONEI cuando en disco hay 234.

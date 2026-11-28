---
type: audit-artifact
phase: e3-artifacts
slug: informe-tecnico-2026-11-28-iter4
generated_at: 2026-11-28T07:00:39Z
repo_url: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba
repo_clone_status: success
language: es
---

# Artifact Inventory

## Repository

- **URL**: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba
- **Clone status**: success (copia local íntegra; comandos `git` ejecutados sobre `~/Proyectos/El precio de moverse en Cuba`)
- **Languages**: Python ~40.500 LOC (propio, excluyendo `.venv-py`, clones de referencia, `Copias/`, `site/`); Markdown ~35.323 LOC (ídem)
- **Commits**: 194
- **Authors**: CarlosAntonioAceaJimenezCD <CarlosAntonioAceaJimenezCD@users.noreply.github.com>
- **First commit**: 2026-11-17
- **Last commit**: 2026-11-28
- **Default branch**: main

### Structure

```tree
.
├── README.md / INFORME_TECNICO.md / INFORME_TECNICO.pdf
├── requirements.txt / mkdocs.yml / .gitattributes / .gitignore
├── Anexos/            # corpus legal y documentos de apoyo
├── Auxiliares/        # .venv-py, cache, herramientas, Repositorios Referencias
├── Copias/            # 4 repos de referencia (excluidos por decisión explícita)
├── Data/              # analisis_rentabilidad, Revolico, catalogos, fuentes, mapas, auditoria, ...
├── docs/              # fuente MkDocs: historia/, referencia/, guias/, fuentes/, graficos/, dashboard.html
├── Hombros/           # PDFs, HTML, repos y derivadas (01–06)
├── reviews/           # 3 pasadas de auditoría completas + plan iter4
├── site/              # generado, ignorado por Git
└── .playground/audit-cache/  # texto en caché del documento auditado
```

### Entry points

| Path | LOC | Args documented | Notes |
|---|---|---|---|
| `Data/analisis_rentabilidad/scripts/run_all.py` | 60 | no | Comando único; declara `SEED = 20261127` (l. 16), siembra `random`/`numpy` y exporta `ENTORNO["PROYECTO_SEED"] = str(SEED)` (l. 23). |
| `Data/analisis_rentabilidad/scripts/03b_baselines.py` | — | no | Calcula los MAE publicados en `baselines.csv` (§71.1). |
| `Auxiliares/herramientas/generar_dashboard.py` | — | yes | `--solo-si-cambia`. |
| `Auxiliares/herramientas/exportar_parquet_compacto.py` | — | yes | `--tablas ...`. |
| `Auxiliares/herramientas/db_chunks.py` | — | yes | `split|verify|assemble`. |
| `Auxiliares/herramientas/generar_sitio_mkdocs.py` | — | no | Regenera `docs/` desde Markdown y CSV. |
| `Auxiliares/herramientas/scrape_concesionarios.py` | — | no | Adaptadores por dominio + Playwright opcional (§8). |
| `Auxiliares/herramientas/actualizar_informe.py` | — | no | Actualiza el registro de altas y regenera el PDF (§13). |
| `Auxiliares/herramientas/test_smoke_pipeline.py` | 68 | no | Prueba de humo del pipeline central (§71.5). |

### Tests

- Files: `Auxiliares/herramientas/test_dashboard.py`, `Auxiliares/herramientas/test_parquet_compacto.py`, `Auxiliares/herramientas/test_modelo.py`, `Auxiliares/herramientas/test_smoke_pipeline.py`
- Total LOC: 327
- Framework: scripts (pytest-style, sin `pytest.ini`/`conftest.py` detectados)
- Tests cover (named): dashboard, exportación Parquet compacto, modelo hedónico, humo del pipeline

### Documentation

| File | LOC |
|---|---|
| README.md | 105 |
| INFORME_TECNICO.md | 1605 |
| Data/analisis_rentabilidad/README.md | 41 |
| Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md | 92 |
| Data/analisis_rentabilidad/NECESIDADES.md | 45 |
| Data/AUTOMATIZACION.md | 100 |
| docs/ (total) | incluido en los ~35.323 LOC Markdown |
| reviews/ (45 artefactos de auditoría + plan iter4) | 3 pasadas × 15 archivos = 45, más `informe-tecnico-2026-11-28-iter4.plan.md` en curso |

### Environment

- requirements.txt: presente, 12 líneas de dependencias (`pandas~=2.2.0`, `numpy~=1.26.0`, `plotly~=5.18.0`, `statsmodels~=0.14.0`, `scipy~=1.11.0`, `pyarrow~=14.0.0`, `mkdocs~=1.6.0`, `mkdocs-material~=9.5.0`, …)
- pyproject.toml: ausente
- environment.yml: ausente
- Dockerfile: ausente
- Other: `mkdocs.yml` (1700 B), `.gitattributes` (Git LFS), `.gitignore`, `Auxiliares/.venv-py/` (Python 3.14); FlareSolverr 3.5.2 en Docker (declarado en §6, sin Dockerfile versionado)

### Heavy artifacts in repo

| Path | Size | Type |
|---|---|---|
| `Data/Revolico/revolico.sqlite` | 838,0 MB | data/sqlite (LFS) |
| `Data/Revolico/pipeline.sqlite` | 753,4 MB | data/sqlite (LFS) |
| `Data/catalogos_concesionarios/bdc_one.sqlite` | 69,9 MB | data/sqlite |
| `Data/catalogos_concesionarios/changan.sqlite` | 54,8 MB | data/sqlite |
| `Data/catalogos_concesionarios/marketplaces/autocubana.sqlite` | 53,6 MB | data/sqlite |
| `Data/catalogos_concesionarios/marketplaces/itencel.sqlite` | 53,5 MB | data/sqlite |
| `Data/analisis_rentabilidad/data/compacto/anuncios/year=2026/month=11/parte-000.parquet` | 23,0 MB | data/parquet |
| `Data/analisis_rentabilidad/data/listings_raw.parquet` | 2,1 MB | data/parquet |

## Datasets

| Name | Source | ID | Publicly accessible | Notes |
|---|---|---|---|---|
| Revolico | custom (scraping propio) | `Data/Revolico/*.sqlite` + `chunks/MANIFEST.json` | yes (repo público, binarios vía Git LFS) | Base cruda y pipeline; reconstruible desde el manifiesto (§71.5). |
| Catálogos de concesionarios y marketplaces | custom (scraping propio) | `Data/catalogos_concesionarios/` (11 bases + 8 marketplaces) | yes | 256 filas de la primera captura (§9); 8 fuentes declaradas en §71.1. |
| ONEI (anuarios) | fuente oficial cubana | `Data/fuentes-oficiales/`, `Data/fuentes_oficiales/` | yes | Cuadros 3 y 4 del apéndice visual. |
| TRMI elTOQUE | fuente externa (tipo de cambio informal) | `Data/analisis_rentabilidad/config.py` | yes | Serie temporal y conversión fechada (§23). |
| Telegram / WhatsApp / Facebook | custom (integraciones) | `Data/integraciones/` | yes | Contexto y canal de circuitos eléctricos (§62, §66). |

## Tables

El texto en caché no contiene marcadores `Tabla N` / `Figura N`: las tablas del cuerpo son markdown sin numerar y el apéndice visual usa `Cuadro N` / `Gráfico N`. Se inventarían los apoyos referidos por el documento.

### Tabla 1 — «Fase | Nombre | Estado» (§2, p. 7 y §2 EN)
- **Section**: §2 (Estado y fases)
- **Lines**: 33–43 / 175–185
- **Columns**: Fase, Nombre, Estado
- **Rows**: 9
- **Claims supported** (preliminary): estado de fase 6 «en curso» y fase 8 «pendiente» con nota de actualización 27/11/2026

### Tabla 2 — «Tienda | Filas | Con precio» (§9)
- **Section**: §9 (Fase 6 — Scraping y captura)
- **Lines**: 105–117 / 247–259
- **Columns**: Tienda, Filas, Con precio
- **Rows**: 11
- **Claims supported** (preliminary): 256 filas y densidad por tienda

### Tabla 3 — «Base / Baseline | Descripción | Métrica observada» (§71.1)
- **Section**: §71.1 (Bases de comparación)
- **Lines**: 1509–1516
- **Columns**: Base/Baseline, Descripción, Métrica observada
- **Rows**: 4 (3 en la tabla markdown + una fila «Modelo principal propio» añadida después del párrafo EN)
- **Claims supported** (preliminary): MAE 18.188,34 y 16.603,28 USD sobre 1.462 anuncios; R² 0,101 sobre 584 observaciones
- **Respaldo CSV**: `outputs/tables/baselines.csv` (2 filas: `mediana_global`, `mediana_por_marca`); la fila del modelo principal **no está** en el CSV.

### Tabla 4 — «Ref. | Clúster | Autor (año) | Obra» (§71.14)
- **Section**: §71.14 (Obras del mapa literario citadas en el cuerpo)
- **Lines**: 1559–1598
- **Columns**: Ref., Clúster, Autor (año), Obra
- **Rows**: 38
- **Claims supported** (preliminary): correspondencia [1]–[38] con `Data/referencias.md`

### Cuadros 1–5 — apéndice visual (§59)
- **Section**: `docs/historia/apendice.md` (enlazado desde el sitio MkDocs)
- **Lines**: 7–77 del apéndice; títulos: «KPIs del mercado», «Mercado local e importación», «Pasajeros transportados (ONEI, millones)», «Seguridad vial (ONEI)», «Modelo de depreciación (coeficientes vigentes)»
- **Rendered in document**: no en el texto en caché (solo referidos en §59); sí en `docs/`/`site/`
- **Claims supported** (preliminary): cifras de KPIs, series ONEI y coeficientes del modelo

## Figures

### Gráficos 1–6 — apéndice visual (§59, §61)
- **Section**: §59 (Storytelling alineado con los datos finales), §61 (Sitio MkDocs)
- **Caption (verbatim)**: «Gráfico 1. Distribución de precios», «Gráfico 2. Distribución por año», «Gráfico 3. Top marcas», «Gráfico 4. Precio por tier», «Gráfico 5. Precio vs km», «Gráfico 6. Precio vs antigüedad»
- **Rendered in document**: no en el texto en caché (enlaces relativos); sí como HTML interactivo en `docs/graficos/01_precios.html` … `06_edad_precio.html` y copias en `site/graficos/`
- **Type**: gráficos Plotly interactivos
- **Claims supported** (preliminary): distribución de precios, año, marcas, tiers, kilometraje y antigüedad

### Panel interactivo — `Data/dashboard.html`
- **Section**: §61, §71.5
- **Caption (verbatim)**: «El panel interactivo vigente es `Data/dashboard.html`, copiado a `docs/dashboard.html`»
- **Rendered in document**: no (artefacto HTML autocontenido, 109.929 B ≈ 107,4 KB, copiado también en `site/dashboard.html`)
- **Type**: dashboard interactivo autocontenido
- **Claims supported** (preliminary): «panel interactivo autocontenido» del Resumen/Abstract

## Missing artifacts

### CSV de comparaciones — coherencia de la muestra
- **Mentioned in document**: §71.3 (p. «Tests and sample size»): «El tamaño se mide en anuncios (981 candidatas de 8 marketplaces)… (`comparaciones.csv`, 2.000 réplicas)», mientras `contraste,n` en el CSV es `precio por tier de marca,1462`.
- **Found in repo**: yes — `Data/analisis_rentabilidad/outputs/tables/comparaciones.csv` (184 B; 1 fila de datos; columnas `contraste,n,estadistico,p_valor,ic_bajo,ic_alto,metodo`).
- **Observation**: el CSV existe y contiene H = 44,313, p = 0.0, IC 10.000–29.500 USD y el método bootstrap de 2.000 réplicas, en coincidencia con §71.3. El denominador de la fila es 1.462 anuncios, distinto de las «981 candidatas» citadas en el mismo párrafo y en §71.2; el inventario registra la diferencia sin resolverla.

### CSV de ablación — recuentos divergentes
- **Mentioned in document**: §71.2: «la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² baja de 0,274 a 0,101»; §71.1: «R² 0,101 sobre 584 observaciones»; §59: «993 candidatas».
- **Found in repo**: yes — `outputs/tables/modelo_muestra.csv` (266 B; columnas `modelo,candidatas,observaciones,r2,p_f,terminos`).
- **Observation**: el CSV registra `principal,993,586,0.1008,0.0` y `completo,993,28,0.2744,0.4114`. Coinciden 28, 993 y los R² redondeados (0,101 y 0,274); no coinciden 586 vs. 584/572 del texto (§71.2, §71.1 y `docs/historia/apendice.md` l. 77, que dice «22 observaciones … frente a 572»). La fila del modelo principal con `hp` incluido no aparece como tercera fila.

### CSV de baselines — fila no presente
- **Mentioned in document**: §71.1: «Los MAE se calculan en `scripts/03b_baselines.py` y se publican en `outputs/tables/baselines.csv`» y la tabla incluye «Modelo principal propio | OLS de log-precio … | R² 0,101 sobre 584 observaciones».
- **Found in repo**: yes — `outputs/tables/baselines.csv` (129 B; 2 filas de datos).
- **Observation**: el CSV contiene únicamente `mediana_global,1462,18188.34` y `mediana_por_marca,1462,16603.28`. La fila «Modelo principal propio» mostrada en la tabla del documento no tiene respaldo en este CSV; el R² 0,101 se respalda en cambio en `modelo_muestra.csv`.

### Lista numerada de referencias — 38 vs. 41
- **Mentioned in document**: §70: «La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`»; §71.14 enumera [1]–[38].
- **Found in repo**: yes — `Data/referencias.md` (87 líneas, entradas [1]–[41]).
- **Observation**: el archivo añade [39] Department for Transport/DVLA, [40] ANFAC y [41] AEADE, que son justamente las tres fuentes institucionales que §70 declara verificadas. La cifra «38» del texto queda desactualizada frente al artefacto versionado (41).

### Semilla y reproducción — verificación positiva
- **Mentioned in document**: §71.5: «La semilla `SEED = 20261127` está declarada en `run_all.py` y se propaga a cada etapa por la variable de entorno `PROYECTO_SEED`; antes se declaraba sin efecto.»
- **Found in repo**: yes — `Data/analisis_rentabilidad/scripts/run_all.py` (60 LOC).
- **Observation**: confirmado en el código: `SEED = 20261127` (l. 16), `random.seed(SEED)` (l. 17), `np.random.seed(SEED)` (l. 18) y `ENTORNO["PROYECTO_SEED"] = str(SEED)` (l. 23). No hay brecha de artefacto.

### Artefactos de auditoría
- **Mentioned in document**: §69: «la huella queda en `reviews/`… El registro de la tercera pasada está en `reviews/informe-tecnico-2026-11-27-iter3.{md,forensic.md}` y sus 13 artefactos.»
- **Found in repo**: yes — `reviews/` contiene 46 archivos: 3 pasadas completas de 15 archivos cada una (45 artefactos: `e1-claims`, `e2-literature`, `e3-artifacts`, `forensic`, `md`, `plan`, `v1`–`v9`) más el plan en curso de la iteración 4.
- **Observation**: la huella declarada existe y es verificable. La iteración 4 solo tiene `informe-tecnico-2026-11-28-iter4.plan.md` hasta el momento de este inventario.

### Licencia de datos y código
- **Mentioned in document**: §71.5: «No se ha declarado todavía una licencia de datos o código»; §71.15: «la licencia queda pendiente de declaración».
- **Found in repo**: no — sin `LICENSE`/`LICENCIA` en la raíz.
- **Observation**: el documento declara explícitamente la ausencia; el repositorio coincide, por lo que no es una brecha oculta sino una limitación documentada.

## Code-to-document mapping (when discernible)

| Document component | Repo location |
|---|---|
| H1 / Kruskal-Wallis H = 44.313, IC bootstrap (§71.3) | `outputs/tables/comparaciones.csv`, `scripts/04_stats.py` |
| Baselines MAE global / por marca (§71.1) | `outputs/tables/baselines.csv`, `scripts/03b_baselines.py` |
| Ablación `hp` y R² 0,274 → 0,101 (§71.2) | `outputs/tables/modelo_muestra.csv` |
| Semilla `SEED` / `PROYECTO_SEED` (§71.5) | `scripts/run_all.py` |
| Panel interactivo (§61, §71.5) | `Data/dashboard.html` → `docs/dashboard.html` → `site/dashboard.html` |
| Seis gráficos Plotly (§59, §61) | `docs/graficos/01_precios.html` … `06_edad_precio.html` |
| Cinco cuadros del apéndice (§59) | `docs/historia/apendice.md` |
| KPIs con marcadores `<!-- kpi:... -->` (§59–§71) | `outputs/tables/kpis.csv` |
| 41 referencias numeradas (§70, §71.14) | `Data/referencias.md` |
| Huella de auditoría (§69) | `reviews/` (45 artefactos + plan iter4) |
| 256 filas / 11 tiendas (§9) | `Data/catalogos_concesionarios/*.sqlite` |
| Bases crudas LFS y manifiesto (§71.5) | `Data/Revolico/`, `chunks/MANIFEST.json`, `.gitattributes` |
| Sitio MkDocs estricto (§61) | `mkdocs.yml`, `docs/`, `Auxiliares/herramientas/generar_sitio_mkdocs.py` |
| Prueba de humo (§71.5) | `Auxiliares/herramientas/test_smoke_pipeline.py` |

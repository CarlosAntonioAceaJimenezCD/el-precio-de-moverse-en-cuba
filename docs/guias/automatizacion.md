# Automatización sin mantenimiento diario (23/11/2026)

Objetivo: que una persona abra el proyecto **dos años después** y lo encuentre como fuente confiable, sin haber tenido que hacer mantenimiento diario.

## 1. Principio: tres carriles desacoplados

**Recolectar → procesar → publicar.** Ningún job de recolección hace `git push`; ningún push dispara scrapers. Así un fallo de red no contamina los datos y un fallo de datos no bloquea la publicación.

## 2. Periodicidad realista

| Job | Frecuencia | Por qué |
|---|---|---|
| Radar Telegram (circuitos y anuncios, 2–3 páginas) | Diario | La vista pública solo conserva mensajes recientes |
| Revolico incremental | Cada 10 minutos | Timer `precio-revolico.timer`, sin `git push` |
| Snapshots de precio (`price_history`) | Semanal, tras Revolico | series mensuales previstas; aún no hay estimación temporal publicada |
| Marketplaces (8 sitios) | Semanal | Más frecuencia aumenta bloqueos sin señal nueva |
| TRMI / tipo de cambio | Semanal, con fecha de vigencia | Evita el `FX=930` clavado en `config.py` |
| ONEI | Trimestral | Los anuarios son estáticos |
| `run_all.py` | Semanal, tras los snapshots | Recomputa desde Parquet y actualiza los números de los documentos |
| Sitio MkDocs | Semanal, tras el análisis | Publica auditoría junto a los KPIs |
| Validación de calidad + `SALUD.md` | Diario | Dead-man's switch visible en el repo |
| Metadatos pequeños a Git | Diario | Separado de los binarios grandes |
| Publicación LFS | Bajo demanda | Chunks de 10 MiB reanudables; push por bloques cuando hay cambios |

Todo se programa en **UTC**, con `Persistent=true` y `RandomizedDelaySec=5m` para recuperarse tras apagones sin picos de carga.

### Panel interactivo autocontenido

`generar_dashboard.py` produce un único `Data/dashboard.html` con gráficos, mapa de servicios y mapa de circuitos. No usa CDN ni bibliotecas externas: vanilla JS + SVG, con fecha tomada de los datos para que sea idempotente. Medición antes/después: antes hacían falta los 6 HTML de Plotly (168 KB) más ~4,5 MB de JavaScript remoto por visita, y el mapa suelto pesaba 4,7 MB sin publicar en el sitio; ahora un solo archivo de **107 KB** sin peticiones externas funciona por `file://` y en 3G. Se regenera desde `run_all.py`, desde el job de circuitos y desde `sitio_build.sh`; `generar_sitio_mkdocs.py` lo copia a `docs/dashboard.html` y lo añade al menú. Pruebas: `Auxiliares/herramientas/test_dashboard.py`.

### Números que se actualizan solos

`README.md`, el storytelling, el análisis de alcance y el inventario de modelos llevan un marcador oculto `<!-- kpi:clave -->` justo antes de cada cifra. Al terminar `run_all.py`, `actualizar_numeros.py` lee los CSV y las bases vigentes y reemplaza **solo el número**, conservando las palabras de alrededor. El modo `--check` avisa sin escribir, y las pruebas de regresión viven en `probar_actualizar_numeros.py`. No hay que editar las cifras a mano.

## 3. Idempotencia y reanudación

- Envoltorio único `Data/_state/run_step.sh <job> <comando>` con `flock`, `timeout`, estado atómico (`tmp` + `mv`) y `heartbeat_utc`.
- Claves por fuente: Revolico `id`; marketplaces URL canónica; Telegram `tg_<canal>_<id>`; snapshots `(id, fecha_lectura)`; LFS SHA-256 del chunk.
- Marcas de agua en `Data/_state/watermarks.json`, escritas solo tras verificar la salida.
- SQLite copiado con `Connection.backup()`, nunca con `cp` si hay WAL.
- LFS con ledger `_state/lfs_push_ledger.jsonl`: un objeto que falla 3 veces se cuarentena y alerta, pero no detiene a los demás. El push del ref solo cuando no queden pendientes.
- `loginctl enable-linger` **ya ejecutado** (Linger=yes) y timers `Persistent=true`: los jobs sobreviven al logout y recuperan el ciclo perdido tras un apagón.
- `StartLimitBurst=3` y `OnFailure` para que un job roto no se convierta en un `Restart=always` infinito (el servicio `push-final` con 8 reinicios fue detenido).

## 4. Calidad y alertas

1. **Ingesta:** columnas obligatorias, tipos, `price_usd > 0`, año 1990–`YEAR_MAX`, km ≤ 600.000, monedas permitidas, claves únicas.
2. **Entre etapas:** conteos por fuente dentro de ±40 % de la mediana de las últimas 8 corridas; frescura < 10 días; presencia de las 8 marketplaces y Revolico.
3. **Publicación:** `mkdocs build --strict`, KPIs no vacíos, snapshot semanal reciente.

Los registros inválidos van a **cuarentena** (`Data/_cuarentena/<fecha>/`), nunca se borran. Si el ratio de rechazo > 10 % el job falla; entre 5 y 10 % solo avisa. `Data/_estado/salud.json` y `Data/auditoria/SALUD.md` muestran el estado por job; `alertas.jsonl` deduplica por job/día. Si un job supera 2× su periodo sin éxito, aparece `ALERTA.stale`: quien abra el repo en 2028 lo ve sin correo ni webhook.

## 5. Auditoría a dos años

Se guarda, en UTC y con hashes:

- `manifiesto_ejecucion.jsonl`: una línea por corrida con commit, SHA de scripts, Python, entradas/salidas, filas, métricas de calidad y watermark antes/después.
- `VERSIONES.json`: dependencias y hash de `config.py`.
- `watermarks.json`, `salud.json`, `alertas.jsonl`.
- Un snapshot Parquet inmutable por semana (`snapshots/YYYY-Www/`) con puntero `LATEST.json`. 104 semanas ≈ 2 años.
- `price_history` en SQLite: el activo más valioso para 2028.
- `chunks/MANIFEST.json` y `pipeline_chunks/MANIFEST.json` con `source_sha256`, offsets y generador.
- `DICCIONARIO.md` y `LIMITACIONES.md`: semántica de campos, URL de origen y límites conocidos.

**Regla de oro:** un snapshot se escribe una vez y nunca se sobrescribe; el estado actual es un puntero. Así se puede reconstruir qué se sabía en cualquier fecha.

## 6. Estado de implementación

## 6. Estado de implementación

**Ya hecho (23/11/2026):**
- `loginctl enable-linger thony70807` → **Linger=yes**: los timers corren aunque cierres sesión.
- Servicio `push-final` con 8 reinicios sin progreso: **detenido**.
- `Data/_state/run_step.sh`: `flock` por job, `timeout`, estado JSON atómico con `last_success`, `last_failure` y `fallos_consecutivos`.
- Wrappers `job_circuitos.sh`, `job_calidad.sh`, `job_salud.sh`, `job_analisis.sh`, `job_sitio.sh`.
- `validar_calidad.py`: 6 reglas, cuarentena en `Data/_cuarentena/`, umbral 10 %. Corrida real: 2.014 filas, 0 inválidos.
- `salud.py`: `Data/_estado/salud.json`, `Data/auditoria/SALUD.md`, `alertas.jsonl` y `ALERTA.stale`.
- Capturador de circuitos con **ETag / Last-Modified** (HTTP 304 = sin descarga) y evidencia en estado HTTP.
- Timers `precio-{circuitos,calidad,salud,analisis,sitio}.{service,timer}` creados, verificados con `systemd-analyze verify`, habilitados y activos.

**Pendiente (fase siguiente):** ledger LFS, unificación de `chunks/` con `partes/` y estimación temporal con la serie mensual; los timers de Revolico y circuitos ya están activos y no hacen push.

## 6b. Internet y ancho de banda

**Sin internet no se puede scrapear**: la recolección necesita red. Lo que sí es posible es que ocurra **sin que tú estés presente ni conectado a la sesión**: `linger=yes` mantiene el gestor de usuario y los timers son `Persistent=true`, así que si el equipo estaba apagado o sin red, systemd dispara el ciclo pendiente al volver y `SALUD.md` registra el periodo perdido.

Consumo estimado con las peticiones condicionales ya implementadas:

| Job | Frecuencia | Sin cambios (304) | Con cambios |
|---|---|---:|---:|
| Circuitos (2 páginas) | Diario | ~2–5 KB/día | ~220 KB/día |
| Marketplaces (8 sitios, 2 páginas) | Semanal | ~20–50 KB/semana | ~1,5 MB/semana |
| Revolico incremental | Semanal | ~0,5 MB/semana | ~10–20 MB/semana |
| **Total estimado** | — | **~2–3 MB/mes** | **~56–100 MB/mes** |

Son estimaciones de diseño, no mediciones de facturación. El punto clave: con ETag/Last-Modified el coste de **comprobar** si hay novedades es despreciable; el ancho de banda se gasta solo cuando el contenido cambia. Para reducirlo más: limitar páginas por sitio, programar de madrugada y guardar solo HTML que cambió. Cada fase tiene criterio de «listo» medible en el informe técnico.

## 7. Límites que hay que aceptar

La vista pública de Telegram es un **radar de novedades**, no una serie histórica: ~20 mensajes por página, ventana de ~8 días, sin garantía de ediciones o borrados. Los selectores y la tasa de cambio envejecen: la automatización avisa y degrada con elegancia, pero no sustituye una revisión trimestral de 30 minutos. Eso, escrito aquí, es parte de que el proyecto sea confiable en 2028.

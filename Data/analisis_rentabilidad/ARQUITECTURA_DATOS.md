# Arquitectura de datos para crecer durante años (23/11/2026)

## 0. Formato compacto ya implementado

`exportar_parquet_compacto.py` copia **todas** las tablas y columnas de
`revolico.sqlite` a Parquet particionado por `year=/month=` y comprimido con
Zstandard, en `Data/analisis_rentabilidad/data/compacto/`. Medición real:
**849 MB → 27,5 MB** (10.379 anuncios, 974 autos, 23.697 imágenes, **14.546** (recuento al 28/11; la base sigue creciendo)
revisiones, 12.538 teléfonos y 716 precios), con las mismas filas, columnas
y valores; `MANIFEST.json` guarda recuentos y SHA-256 por archivo. La SQLite
sigue siendo la base de trabajo del capturador; el Parquet es la copia
compacta para analizar y publicar. Se regenera al final de `run_all.py` y se
verifica con `test_parquet_compacto.py`. Las fases siguientes (watermark y
solo el delta) se apoyan en esta misma capa.

## 1. El problema real

Hoy `run_all.py` lee el **100 % del histórico** en cada corrida. Con 2–5 años de datos, el tiempo crece linealmente con el tamaño total. El objetivo no es "comprar un motor más rápido", sino cambiar la complejidad por ejecución de `O(total)` a `O(nuevo + particiones consultadas)`.

Cuatro medidas atacan el crecimiento: particionar, guardar un watermark, pre-agregar KPIs por mes y compactar archivos. El diseño es observacional: no hay grupos asignados al azar, por lo que las dos líneas base publicadas son predictivas (mediana global y mediana por marca, con MAE en `baselines.csv`), no experimentales. El mapa de trabajos académicos está en `Data/referencias.md` (41 entradas); el corpus de documentación de usuario cita sobre todo fuentes oficiales cubanas, por lo que la cobertura académica de README y storytelling sigue siendo parcial.

## 2. Comparativa de motores (investigación con documentación oficial)

| Opción | Cuándo conviene | Adopción | Veredicto |
|---|---|---|---|
| **DuckDB** sobre Parquet | Motor evaluado pero bloqueado por `SIGILL` en esta CPU; se usa pyarrow/pandas | — | **Bloqueado** |
| **Polars** lazy/streaming | Cuando el cuello sea limpieza/transformación; ~1,15–1,33× más rápido que DuckDB en benchmarks de proveedor | Media: reescribir transforms | Segundo motor, solo con medición |
| **PyArrow dataset / Parquet particionado** | Capa de almacenamiento común; `write_dataset` con `partitioning` y row groups grandes | Muy baja: ya está vía pandas | Base de la Fase 1 |
| **Iceberg / Delta Lake** | ACID, time travel y correcciones de histórico; con writer concurrente | Alta: catálogo, snapshots, compactación | No ahora |
| **DuckLake** | Punto intermedio: snapshots y CDC con sintaxis DuckDB y catálogo en SQLite | Media-baja | Fase opcional 4 |
| **ClickHouse / chDB** | KPIs como servicio con consultas concurrentes y baja latencia | Alta (servidor), media (`chdb`) | Sobrekill para batch local |

Reglas de tamaño recogidas de la documentación: archivos Parquet de 100 MB a 10 GB, row groups de 100K–1M filas, al menos 100 MB por partición, evitar particiones diarias si cada día pesa poco y evitar más de ~2.000 archivos.

## 3. Diseño propuesto

```text
Data/analisis_rentabilidad/data/
  anuncios/year=2026/month=11/part-....parquet   # histórico inmutable, zstd
  estado.duckdb                                  # watermark + kpi_mes + benchmark_result
outputs/tables/...                               # se regeneran desde kpi_mes
```

- **Escritura**: cada corrida añade solo el delta (`id`/`fecha` posteriores al watermark) con `COPY ... (PARTITION_BY, APPEND, FILENAME_PATTERN 'part_{uuid}')`.
- **Lectura**: `read_parquet(..., hive_partitioning=true, union_by_name=true)`; las consultas recientes tocan solo las particiones del mes.
- **Rollups**: `kpi_mes` y `benchmark_result` keyed por `(year, month, dataset_version)`. La corrida diaria solo recalcula el mes corriente; una validación semanal recalcula el todo.
- **Idempotencia**: el watermark se actualiza en la misma transacción que el KPI. Si la corrida muere, el watermark no avanza.
- **Esquema evolutivo**: `union_by_name=true` tolera columnas nuevas en años futuros.
- **Higiene**: job mensual que alerta si hay más de 2.000 archivos o particiones menores de 100 MB, y compacta.

## 4. Ruta de migración por fases

| Fase | Acción | Criterio de «listo» |
|---|---|---|
| **0** | Cronometrar `run_all.py` hoy: tiempo, bytes leídos, RAM, nº de archivos y filas por año. Guardar 5 consultas KPI como suite de regresión | Línea base documentada |
| **1** | Partir Parquet por `year=/month=` con `pyarrow.write_dataset`; probar `pd.read_parquet(..., filters=...)` | KPIs idénticos (diff = 0); un mes lee solo su carpeta |
| **2** | Introducir DuckDB y `estado.duckdb` con watermark; ingestión solo del delta | Tiempo casi constante al duplicar datos sintéticos |
| **3** | Materializar `kpi_mes` y `benchmark_result`; recalcular solo el mes corriente | Corrida diaria independiente del histórico |
| **4** | Higiene y, solo si aparecen correcciones/concurrencia, DuckLake/Iceberg | Archivos acotados y snapshots auditables |
| **5** | Evaluar Polars con medición antes/después antes de reescribir transforms | Mejora demostrable, sin regresiones |

## 5. Riesgos

- **Archivos pequeños**: particionar por día genera miles de archivos y el listing domina el tiempo. Partir por mes.
- **Watermark desincronizado**: actualizarlo antes del cómputo pierde datos; después, duplica. Debe ir en la misma transacción.
- **Overkill**: Iceberg/Delta/ClickHouse solo si aparecen escritura concurrente o KPIs como servicio.

## 6. Estado actual

Extracción continua de Revolico activa (timer cada 10 minutos, 2 descargadores y 2 procesadores, lote 50, sin git push). El debug detectó que 3.351 enlaces no-auto quedaban `pending` para siempre y el bucle nunca cerraba: se corrigió marcándolos `rechazado` y excluyéndolos del conteo de salida; además se añadió manejo de SIGTERM para que el `finally` guarde lote, snapshot y partes.

**Bloqueo para DuckDB:** en esta CPU, `import duckdb` falla con `SIGILL` (Instrucción ilegal) con las versiones probadas. Mientras no se fije una compilación compatible, la Fase 1 se hará con **pyarrow/pandas particionado** (`write_dataset` + `pd.read_parquet(filters=...)`), que ya está instalado, y DuckDB queda como opción a reevaluar. Este documento es la Fase 0–1 de diseño; la línea base de rendimiento se guardará en `benchmark_result.csv` antes de tocar el pipeline.

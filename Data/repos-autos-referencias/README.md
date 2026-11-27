# Bases de los repositorios de referencia (solo autos)

Consolidación del 19/11/2026 de los 7 repositorios de GitHub dedicados al mercado
automotor cubano. Script reproducible: `Auxiliares/herramientas/consolidar_repos_autos.py`.

Base resultante: **`referencias_autos.sqlite`** (25 tablas). Tabla `provenancia`:
archivo de origen, filas, clave y nota de cada conjunto.

## Repositorios comparados

| Repositorio | Aporte principal |
|---|---|
| `kremondherranz-lgtm/Mercado-automotriz` | Encuesta de demanda (33 respuestas), catálogos de 4 comercializadoras, metodología e informe interpretado |
| `aRandomFool/ICD-Mercado-Automotriz` | 3.958 anuncios de Revolico, 3.566 limpios, 30 entrevistas, 8 audios, catálogos y regresión |
| `anapaula65/AutosxCuba` | 157 autos, 80 anuncios Revolico, 20 chats de Telegram, 24 de Autocubana, 8 entrevistas estructuradas |
| `JoReRgEr/Proyecto-Mercado-Automotriz` | 30 entrevistas declarativas sobre clásicos y eléctricos |
| `jhernandezd95/autos-cuba` | Catálogos unificados y cuestionario de compradores (instrumento) |
| `randoloc/AppCubAutosScrapper_QMLQt` y `randoloc/scrapper_autos_electricos` | Scrapers (CubAutosFinder). **Duplicados entre sí en código**: se conservan los repos, no aportan bases nuevas |

## Duplicados detectados y descartados

Comparación por hash de bytes (12 grupos) y por contenido ordenado (11 grupos).

| Duplicado | Conservado | Descartado |
|---|---|---|
| 100 anuncios Revolico repetidos 3 veces dentro de `Mercado-automotriz` | `cat_`/`anuncios` del repo | `Anexo_4revolico_cars.csv`, `oferta_de_revolico.csv` |
| 3.566 anuncios | `anuncios_limpios_icd` | `data/processed/mercado_havana.csv` (contenido idéntico) |
| 157 autos de AutosxCuba | `dataset_autosxcuba_157` | `DATASET_PARA_GRAFICOS.csv` (idéntico a `DATASET_COMPLETO_MEJORADO.csv`) |
| Catálogos MCV (43), Dongfeng (22), Womy (17), BDC One (13) | copia en `Mercado-automotriz` | copias en `autos-cuba/data/raw` |
| Encuesta: 11 respuestas | snapshot final de 33 | `data/processed/survey.csv` y snapshots parciales (12, 16, 19, 27, 30) |
| `entrevistas.json` = `entrevistas_final.json` | `entrevistas_mercado_30` | copia en `data/processed_final/` |
| `mercado_formal_processed.json` | versión procesada | copia `*_backup_pre_fase4.1.json` |
| Tablas de reportes repetidas (q1, q2, q4) | una copia | sufijos `_grafico` y equivalentes |
| Cuestionario Anexo 2 | copia en `docs/methodology/` | copia en `Anexos/` |

**No se descartaron** los datasets de `AutosxCuba` de distinto tamaño (142, 123, 62,
49 filas): al comparar claves (marca, modelo, precio, año) resultaron muestras de
fuentes diferentes, no versiones recortadas unas de otras. Se conservaron los dos
más completos (157 filas cada uno) y las fuentes específicas.

## Solapamiento con nuestra base

Los 3.958 anuncios del repo ICD tienen IDs únicos. **369 ya estaban en
`Data/Revolico/revolico.sqlite`**; los otros **3.589 son nuevos**. La columna
`en_nuestro_proyecto` de `anuncios_revolico_icd` lo marca (1 = ya presente,
0 = nuevo). No se alteró la base propia para no romper el historial de precios.

## Tablas incluidas

`anuncios_revolico_icd`, `verificacion_anuncios_icd`, `anuncios_limpios_icd`,
`cat_mcv`, `cat_dongfeng_nwi`, `cat_womy`, `cat_bdcone`,
`comercializadoras_icd`, `catalogo_dongfeng_icd`, `catalogo_bdcone_icd`,
`catalogo_cimex_icd`, `estado_comercializadoras_icd`, `tasas_cambio_icd`,
`regresion_dataset_icd`, `encuesta_demanda_33`, `entrevistas_icd`,
`entrevistas_mercado_30`, `entrevistas_estructuradas_autosxcuba`,
`dataset_autosxcuba_157`, `dataset_oficial_autosxcuba_157`,
`revolico_80_autosxcuba`, `telegram_autosxcuba`, `autocubana_autosxcuba`,
`dongfeng_catalogo_autosxcuba`, `provenancia`.

## Documentación y evidencias copiadas

- `documentacion/`: 7 snapshots del Google Forms, cuestionarios, leyenda de
  códigos, metodología, informe con interpretaciones, 4 hojas de cálculo de
  gráficas, guiones de encuesta y entrevista, metodologías y contexto.
- `audios/`: 8 grabaciones originales (m4a/mp3) de las entrevistas del repo ICD.

Detalle de cómo se aplicaron encuestas y entrevistas: `ENCUESTAS_Y_ENTREVISTAS.md`.

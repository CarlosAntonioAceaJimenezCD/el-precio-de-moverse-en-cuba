# El precio de moverse en Cuba

Análisis reproducible del mercado automotor cubano: **<!-- kpi:autos_revolico -->772 autos únicos** de Revolico, **<!-- kpi:anuncios_marketplaces -->2.232 anuncios** de 8 marketplaces y **256 vehículos** de 11 concesionarios, consolidados con fuentes oficiales (ONEI, Gaceta Oficial, BCC) y una serie de entrevistas y encuestas.

*Ubicación:* `~/Proyectos/El precio de moverse en Cuba` · *Repositorio:* `el-precio-de-moverse-en-cuba` · *Actualizado:* 23/11/2026.

## Qué incluye

- **Datos crudos y auditables**: anuncios, enlaces, colas de descarga y descartes exportados por categoría en `Data/CRUDO_POR_CATEGORIA/`.
- **Base consolidada**: `Data/Revolico/revolico.sqlite` (<!-- kpi:anuncios_revolico -->10.177 anuncios, <!-- kpi:autos_revolico -->772 autos) y `Data/repos-autos-referencias/referencias_autos.sqlite` (25 tablas).
- **Análisis regenerable**: KPIs, benchmarks, depreciación y gráficos en `Data/analisis_rentabilidad/`.
- **Fuentes oficiales**: los 12 anuarios del ONEI (2014–2025), 233 archivos, en `Data/fuentes-oficiales/ONEI/`.
- **Documentación**: informe técnico, storytelling, auditoría de fuentes e índices de datos.

## Quickstart

Requiere Python 3.10+ y Git LFS. Desde la carpeta del proyecto:

```bash
python3 -m venv Auxiliares/.venv-py
Auxiliares/.venv-py/bin/pip install -r requirements.txt
Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py
```

Al terminar verás `INGESTA`, `LIMPIEZA`, `EDA`, `STATS` y `BENCHMARK`, y se habrán actualizado:

```text
Data/analisis_rentabilidad/data/listings_clean.parquet
Data/analisis_rentabilidad/outputs/tables/kpis.csv
Data/analisis_rentabilidad/outputs/tables/kpis_canal.csv
```

**Resultado esperado:** <!-- kpi:anuncios_totales -->2.029 anuncios limpios (<!-- kpi:anuncios_locales -->1.338 locales + <!-- kpi:anuncios_importacion -->691 de importación), mediana local <!-- kpi:precio_mediano_usd -->21.000 USD.

## Estructura

```text
.
├── README.md, requirements.txt, INFORME_TECNICO.md
├── Data/
│   ├── Revolico/                 # base principal, colas, chunks de 10 MB y snapshot
│   ├── catalogos_concesionarios/ # 11 concesionarios + 8 marketplaces
│   ├── repos-autos-referencias/  # base consolidada de repos externos
│   ├── fuentes-oficiales/ONEI/   # anuarios 2014–2025 con índice y SHA-256
│   ├── CRUDO_POR_CATEGORIA/      # export CSV de enlaces y anuncios sin procesar
│   └── analisis_rentabilidad/    # pipeline, KPIs, gráficos y storytelling
├── Auxiliares/herramientas/      # scrapers, exportadores y auditoría de fuentes
├── Auxiliares/Repositorios Referencias/  # repos clonados (no versionados)
└── Copias/, Hombros/, Anexos/    # referencias y corpus (no versionados)
```

Los repositorios auxiliares y `Copias/` se conservan en disco pero **no se suben**: están excluidos en `.gitignore`.

## Fuentes de datos

| Grupo | Fuentes | Registros |
|---|---|---:|
| Marketplaces | Autocubana, iTENCEL, Cogetucarro, Cubisima, Timbirichi, Carros.com, Apululu, VentaCuba | 2.222 anuncios |
| Concesionarios | BDC One, Dongfeng, Changan, Chinautos, MCV, Finauto, ATR Export y otros | 256 vehículos |
| Revolico | `autos` (tabla canónica) | <!-- kpi:autos_revolico -->772 autos únicos |
| Referencias externas | Repos ICD, AutosxCuba, Mercado-automotriz y otros | 3.958 anuncios ICD |
| Oficiales | ONEI, Gaceta Oficial 65/2026, BCC, elTOQUE | 12 anuarios + normas |

La conversión usa la **TRMI informal de elTOQUE (18/11/2026): 930 CUP/USD, 1.000 CUP/EUR y 845,35 CUP/MLC**. Nunca se usa la tasa oficial para los precios del mercado.

## Configuración

| Archivo | Qué controla |
|---|---|
| `Data/analisis_rentabilidad/config.py` | Rutas, umbrales de precio/año, TRMI, marcas y tiers |
| `.gitattributes` | Archivos SQLite y chunks `.bin` gestionados con Git LFS |
| `Data/Revolico/chunks/MANIFEST.json` | 82 fragmentos de 10 MB y sus SHA-256 |
| `Data/Revolico/pipeline_chunks/MANIFEST.json` | 52 fragmentos de `pipeline.sqlite` |

Si `revolico.sqlite` o `pipeline.sqlite` no existen, los scripts los reconstruyen desde sus chunks:

```bash
python3 Auxiliares/herramientas/db_chunks.py verify Data/Revolico/chunks/MANIFEST.json
python3 Auxiliares/herramientas/db_chunks.py assemble Data/Revolico/chunks/MANIFEST.json Data/Revolico/revolico.sqlite
```

## Sitio de documentación

El storytelling, los cuadros, los gráficos y el inventario de modelos se publican como un sitio MkDocs:

```bash
Auxiliares/.venv-py/bin/python Auxiliares/herramientas/generar_sitio_mkdocs.py
Auxiliares/.venv-py/bin/mkdocs build
Auxiliares/.venv-py/bin/mkdocs serve
```

El resultado queda en `site/` (ignorado por Git) y la configuración en `mkdocs.yml`.

## Documentación

- **Referencia:** `INFORME_TECNICO.md` (secciones 1–60), `Data/CRUDO_POR_CATEGORIA/INDICE.md`, `Data/fuentes-oficiales/ONEI/README.md`, `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md`.
- **Cómo hacerlo:** `Data/analisis_rentabilidad/README.md`, `Data/Revolico/chunks/README.md`.
- **Explicación:** `Data/analisis_rentabilidad/PRESENTACION_STORYTELLING.md`, `Data/auditoria-fuentes-2026-11-23.md`, `Data/auditoria-fuentes-contenido.md`, `Data/novedades-fuentes-2026-11-23.md`, `Data/fuentes-adicionales-2026-11-20.md`, `Data/fuentes-oficiales/ONEI/ANALISIS_DATO.md`, `Data/estructura_github.md`, `Data/mapas/TIMELAPSE_CIRCUITOS.md`.
- **Necesidades pendientes:** `Data/analisis_rentabilidad/NECESIDADES.md`.

## Marco legal y límites

El proyecto respeta los términos de uso de los portales: no elude mecanismos anti-automatización, no recopila datos personales de anunciantes y conserva la procedencia de cada dato. El marco normativo es el **Decreto 163/2026** y las resoluciones 104, 17, 52, 171–175, 340 (que derogó la 312) y 102/2026.

Limitaciones actuales: elTOQUE no responde de forma estable desde este entorno (se usa su última TRMI publicada); `carrosw` está detrás de verificación de bots; parte del catálogo de BDC One y Changan solo está en PDF; la trueque de roles entre canales local e importación se mantiene separada con la columna `canal`.

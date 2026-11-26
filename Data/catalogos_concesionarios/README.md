# Catálogos scrapeados de concesionarios online

Cada tienda tiene su **propia base SQLite** en esta carpeta. El scraper está en
`Auxiliares/herramientas/scrape_concesionarios.py`.

```bash
cd Auxiliares
.venv/bin/python herramientas/scrape_concesionarios.py            # todas las tiendas
.venv/bin/python herramientas/scrape_concesionarios.py --shops bdc_one finauto
```

## Esquema de cada base

Tabla `vehiculos`, una fila por URL scrapeada (ficha o página de catálogo):

- **Identificación:** `url`, `shop`, `shop_name`, `title`, `final_url`, `scraped_at`, `status`.
- **Metadatos:** `meta_description`, `og_image`, `headings`, `text`.
- **Campos estructurados:** `marca`, `modelo`, `version`, `anio`, `anho`, `year`, `precio`, `moneda`, `km`, `kilometraje`, `combustible`, `transmision`, `traccion`, `motor`, `potencia`, `cilindrada`, `color`, `puertas`, `asientos`, `carroceria`, `garantia`, `ubicacion`, `estado`, `condicion`, `matricula`, `chasis`, `vin`, `consumo`, `etiqueta`, `categoria`.
- **Datos completos sin normalizar:** `tables_json` (tablas), `jsonld_json` (schema.org), `microdata_json`, `images_json`, `links_json`, `prices_json`, `emails_json`, `phones_json`, `raw_json` (todo junto) y `raw_html` (HTML íntegro).

Los campos se extraen de JSON-LD, microdatos, metatags, tablas y texto visible mediante patrones;
cuando la página es JS-heavy se renderiza con Chromium del sistema antes de extraer.

## Tiendas incluidas

| Base de datos | Tienda |
|---|---|
| `bdc_one.sqlite` | BDC One |
| `dongfeng_cuba.sqlite` | Dongfeng Cuba |
| `mcv_commercial.sqlite` | MCV Commercial |
| `finauto.sqlite` | Finauto International |
| `changan.sqlite` | Changan Automotive |
| `chinautos_cuba.sqlite` | Chinautos Cuba (LXWY) |
| `envision_autos.sqlite` | Envision Autos Cuba |
| `atr_export.sqlite` | ATR Export |
| `connectingcuba.sqlite` | ConnectingCuba |
| `subasta_cubana.sqlite` | La Subasta Cubana |
| `agn_motors.sqlite` | AGN Motors Cuba |

### No incluidas por bloqueo técnico

- **carrosw** — responde HTTP 403 con “Bot Verification” incluso con navegador automatizado y FlareSolverr.
- **LlamaCuba** — timeout de conexión en `https`, `http` y `www`.
- **SASA / DIVEP** — no publican catálogo de coches en su web (venta presencial/importación MLC).

## Consultas útiles

```bash
sqlite3 bdc_one.sqlite "SELECT modelo, anio, precio, moneda FROM vehiculos WHERE modelo<>'' LIMIT 20;"
sqlite3 dongfeng_cuba.sqlite "SELECT COUNT(*) FROM vehiculos;"
sqlite3 chinautos_cuba.sqlite "SELECT title, prices_json FROM vehiculos LIMIT 5;"
```

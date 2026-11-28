# Mapa y base unificada de elementos

## Base de datos

`mapa_elementos.sqlite` es la fuente única. Tablas:

- `tipos`: catálogo de capas y colores.
- `elementos`: nombre, coordenadas, dirección, fuente, URL, teléfono, horario, precio, estado y detalle crudo en JSON.

| Tipo | Color en el mapa | Símbolo | Fuente principal |
|---|---|---|---|
| `gasolinera` | **negro** | círculo | OpenStreetMap/Overpass |
| `estacion_carga` | **verde** | diamante | Kargalaya, Electromaps |
| `concesionario` | **azul** | cuadrado | webs, Yellocu, Cybo |
| `taller` | **rojo** | triángulo | webs de concesionarios, Cubisima, NearPlace, Páginas Amarillas, tallermanolito.com |

## Generar el mapa

```bash
cd Auxiliares
.venv-py/bin/python herramientas/generar_mapa_ofline.py --tipos all
.venv/bin/python herramientas/generar_mapa_ofline.py --tipos gasolinera,estacion_carga
.venv/bin/python herramientas/generar_mapa_ofline.py --tipos concesionario,taller --out ../Data/mapas/mapa_talleres.html
```

`mapa_ofline.html` incluye Plotly embebido, así que funciona sin internet. Los elementos sin coordenadas se exportan a `elementos_sin_coordenadas.csv`.

## Scripts relacionados

| Script | Función |
|---|---|
| `mapa_db.py` | crea la BD e importa los CSV históricos |
| `scrape_talleres.py` | scrapeador de talleres/directorios con fallback anti-bot |
| `geocode_elementos.py` | completa coordenadas desde direcciones (Nominatim → Photon) |
| `generar_mapa_ofline.py` | genera el HTML con colores y capas seleccionables |

## Anti-bot

El scraper usa, en orden: `curl_cffi` con impersonación de Chrome/Safari, **`patchright`** (navegador real con fingerprint de Chrome) y **FlareSolverr** (`http://127.0.0.1:8191/v1`) para páginas como Cybo que devuelven 403 o verificación de seguridad.

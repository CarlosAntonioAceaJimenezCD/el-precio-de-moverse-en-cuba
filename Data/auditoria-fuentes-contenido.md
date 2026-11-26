# Comprobación de contenido en semillas (23/11/2026)

Se descarga la primera página de listado de cada fuente y se cuentan los enlaces que coinciden con su patrón de anuncio.

| Fuente | Patrón | Enlaces en página | Anuncios en BD |
|---|---|---:|---:|
| apululu | `/anuncio/` | 14 (200) | 33 |
| autocubana | `/vehicle_listings/anuncio-` | 17 (200) | 667 |
| carroscom | `/car/` | 18 (200) | 15 |
| cogetucarro | `view\.php\?id=\d+` | 3 (200) | 200 |
| cubisima | `/carros/.+\.htm` | 1 (200) | 155 |
| itencel | `/anuncio/` | 24 (200) | 951 |
| timbirichi | `/vehiculos-y-piezas/carros/.+` | 51 (200) | 170 |
| ventacuba | `_i\d+` | 24 (200) | 31 |

Nota: el número de enlaces de una sola página no equivale al total del sitio; sirve para detectar si la fuente sigue publicando anuncios.

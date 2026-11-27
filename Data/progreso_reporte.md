# Reporte de progreso — 2026-11-21 07:15:15 UTC

## Revolico

| Tabla / cola | Registros |
|---|---:|
| revolico.sqlite : anuncios | 10149 |
| revolico.sqlite : autos | 744 |
| revolico.sqlite : revision | 9692 |
| revolico.sqlite : imagenes | 22856 |
| revolico.sqlite : telefonos | 12258 |
| revolico.sqlite : price_history | 716 |
| pipeline.sqlite : url_queue | 11968 |
| pipeline.sqlite : download_queue | 6621 |
| pipeline.sqlite : process_queue | 6620 |

### Colas por estado

- **url_queue**: done=6610, pending=3351, rechazado=1940, failed=52, downloading=15
- **download_queue**: processed=6616, failed=4, processing=1
- **process_queue**: committed=6602, pending=18

## Marketplaces

| Sitio | Anuncios | Comentarios | Vendedores |
|---|---:|---:|---:|
| apululu | 33 | 0 | 16 |
| autocubana | 667 | 638 | 0 |
| carroscom | 15 | 0 | 1 |
| cogetucarro | 200 | 0 | 0 |
| cubisima | 155 | 0 | 0 |
| itencel | 951 | 0 | 0 |
| timbirichi | 170 | 50 | 50 |
| ventacuba | 31 | 0 | 0 |

**Total marketplaces: 2222**

## Servicios

- `revolico-revisar.service`: **inactive**
- `marketplaces-scrape.service`: **inactive**
- `revolico-snapshot.timer`: **active**

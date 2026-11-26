# Datos crudos separados por categoría

Enlaces y anuncios sin procesar, exportados sin mover ni borrar las fuentes. 21/11/2026.

| Categoría | Archivo | Filas | Qué contiene |
|---|---|---:|---|
| enlaces_revolico | `01_enlaces_revolico.csv` | 11,968 | Enlaces descubiertos con estado y motivo. |
| muestra_paginas | `02_muestra_paginas_descargadas_revolico.csv` | 200 | Muestra de páginas en cola; total en progreso.md. |
| decisiones_revolico | `03_decisiones_revolico.csv` | 6,620 | Clasificación accept/reject de cada anuncio. |
| anuncios_revolico_crudos | `04_anuncios_revolico_crudos.csv` | 10,149 | Anuncios Revolico con flags de auto y datos. |
| revisiones_revolico | `05_revisiones_revolico.csv` | 9,692 | Anuncios en revisión con categoría y motivo. |
| anuncios_marketplaces | `06_anuncios_marketplaces.csv` | 2,222 | Anuncios crudos de 8 marketplaces, con `fuente`. |
| vehiculos_concesionarios | `07_vehiculos_concesionarios.csv` | 256 | Vehículos de 11 concesionarios, con `fuente`. |
| anuncios_icd_referencia | `08_anuncios_icd_referencia.csv` | 3,958 | Anuncios del repo ICD con bandera propia. |
| enlaces_urls_txt | `09_enlaces_urls_txt.csv` | 9,995 | Enlaces históricos (muchos son bicis/motos). |

## Notas

- Textos largos recortados a 600 caracteres; el contenido íntegro sigue en las bases.
- `02_paginas_descargadas_revolico.csv` es un export interrumpido: ignorarlo.
- `url_queue` mezcla categorías; `es_auto_candidato` es el filtro preliminar.
- `telegram.sqlite` no es una base válida y queda fuera.

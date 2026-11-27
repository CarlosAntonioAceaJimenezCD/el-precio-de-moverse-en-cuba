# ONEI — Anuarios Estadísticos de Cuba (descarga completa)

Fuente: Oficina Nacional de Estadística e Información (ONEI), Cuba.
Índice de anuarios: http://www.onei.gob.cu/cuba
Descarga: 20/11/2026.

## Qué hay aquí

Los **12 anuarios disponibles (2014–2025)**, con todos los documentos enlazados desde cada página oficial. No se descartó ningún archivo de documento; los únicos enlaces omitidos son CSS y el favicon del sitio.

| Año | PDF | RAR | Excel extraídos | Tamaño | Página oficial |
|---|---:|---:|---:|---:|---|
| 2014 | 1 | 0 | 0 | 4,1 M | `/anuario-estadistico-de-cuba-ano-2014` |
| 2015 | 1 | 0 | 0 | 5,5 M | `/anuario-estadistico-de-cuba-ano-2015` |
| 2016 | 1 | 0 | 0 | 4,4 M | `/anuario-estadistico-de-cuba-2016` |
| 2017 | 23 | 0 | 0 | 16 M | `/anuario-estadistico-de-cuba-ano-2017` |
| 2018 | 1 | 0 | 0 | 3,8 M | `/anuario-estadistico-de-cuba-ano-2018` |
| 2019 | 1 | 0 | 0 | 8,1 M | `/anuario-estadistico-de-cuba-2019` |
| 2020 | 1 | 1 | 1 | 65 M | `/anuario-estadistico-de-cuba-ano-2020` |
| 2021 | 1 | 1 | 23 | 33 M | `/anuario-2021` |
| 2022 | 23 | 1 | 22 | 53 M | `/anuario-estadistico-de-cuba-2022` |
| 2023 | 23 | 1 | 22 | 78 M | `/anuario-estadistico-de-cuba-2023` |
| 2024 | 22 | 1 | 22 | 23 M | `/anuario-estadistico-de-cuba-2024` |
| 2025 | 13 | 1 | 13 | 17 M | `/anuario-estadistico-de-cuba-2025` |
| **Total** | **111** | **7** | **103** | **~311 M** | — |

## Estructura

```text
Data/fuentes-oficiales/ONEI/
├── README.md                       ← este archivo
└── Anuario_Estadistico_AAAA/
    ├── INDICE.md                   ← inventario con URL, tamaño y SHA-256 por archivo
    ├── PDF/                        ← documentos de consulta (o PDF íntegro en años antiguos)
    ├── Archivo/                    ← RAR original, conservado sin modificar
    └── Excel/                      ← cuadros extraídos del RAR (cuando existe)
```

Notas:

- En 2014–2016, 2018 y 2019 la página oficial solo publica un **PDF íntegro**; no hay RAR.
- En 2022 la página también enlazaba el PDF íntegro y el RAR de **2021**; se deduplicaron por URL y quedaron bajo `Anuario_Estadistico_2021`.
- Los RAR se extrajeron con `unrar x -o+`; los originales se conservan en `Archivo/`.
- Todos los archivos fueron validados por tipo MIME (`file`): 0 formatos sospechosos.

## Uso en el proyecto

Para el análisis del mercado automotor, el archivo más relevante es el **capítulo 13 (Transporte y Seguridad Vial)** de cada año: parque automotor, matriculaciones y accidentes. Los capítulos de población, empleo y sector externo aportan contexto de demanda y poder adquisitivo. La serie 2014–2025 permite construir tendencias oficiales, que hoy faltan en la base del proyecto.

La conversión monetaria del proyecto sigue usando la **TRMI informal de elTOQUE (930 CUP/USD, 18/11/2026)**; las tasas del BCC se conservan solo como referencia oficial contrastada.

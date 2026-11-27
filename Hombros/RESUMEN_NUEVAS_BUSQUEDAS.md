# Hombros — nuevas búsquedas (rentabilidad y calidad/precio)

Fecha: 16/11/2026. Mismos criterios de utilidad que la búsqueda inicial:
se cuenta solo la **primera aparición** de un trabajo investigativo automotriz
(tesis, TFG/TFM, artículo, estudio de mercado o informe académico/oficial).
**No cuentan** repetidos, mirrors (ResearchGate/Academia/Dialnet del mismo trabajo),
subpáginas de un resultado ya visto, noticias, guías genéricas, empleo, vídeos ni foros.

## 1. Rentabilidad del precio de automóviles — trabajos investigativos

- Consulta: `rentabilidad del precio de automoviles trabajos investigativos`
- Fuente: DDG bloqueó la página 1 con HTTP 202, por lo que se usó el índice de **Yahoo** para las primeras páginas y DDG paginado con `vqd` para el resto.
- Páginas revisadas: **24** · Resultados: **226**
- Trabajos únicos y útiles: **2**
- **Parada en la página 11**: racha **2–11**, 10 páginas consecutivas sin ningún enlace útil.
- El índice DDG se agotó sin resultados en la página 25.
- Analisis: `05_Rentabilidad_precio_autos/analisis.md`
- Descargas: `05_Rentabilidad_precio_autos/` — 23 OK / 10 fallos · 13 PDF, 10 HTML, 3 derivadas.

### Enlaces útiles

1. **(PDF) Estudio de las variaciones de precios en la comercialización de automóviles seminuevos** — https://www.researchgate.net/publication/397440188_Estudio_de_las_variaciones_de_precios_en_la_comercializacion_de_automoviles_seminuevos
2. **Propuesta de un plan… (Trabajo Final de Graduación, UNITEC)** — https://repositorio.unitec.edu/bitstream/handle/123456789/13127/Documento%20final%20TESIS%20Ambar%20Recarte%20-%20Francielly%20Osorio%202024.pdf?sequence=1

## 2. Calidad precio mercado automotriz — trabajo investigativo

- Consulta: `calidad precio mercado automotriz trabajo investigativo`
- La URL de Google proporcionada devuelve una página sin resultados (bloqueo/JS) tanto por `curl_cffi` como por el fetcher externo; se usó **DDG** (endpoint HTML + `vqd`) y se cotejó con Yahoo.
- Páginas revisadas: **23** · Resultados: **230**
- Trabajos únicos y útiles: **10**
- **Parada en la página 22**: racha **13–22**, 10 páginas consecutivas sin ningún enlace útil.
- Analisis: `06_Calidad_precio_mercado/analisis.md`
- Descargas: `06_Calidad_precio_mercado/` — 78 OK / 36 fallos · 44 PDF, 34 HTML, 25 derivadas.

### Enlaces útiles

1. Trabajo Final de Grado (Universidad Nacional de Colombia) — https://repositorio.unal.edu.co/bitstreams/e9462291-a045-45a5-bdb0-bafe34cf4483/download
2. Identificación de problemas y oportunidades en investigación de mercado (sector automotriz) — https://www.researchgate.net/publication/378692386_IDENTIFICACION_DE_PROBLEMAS_Y_OPORTUNIDADES_EN_LA_INVESTIGACION_DE_MERCADO_CASOS_EN_EMPRESAS_DEL_SECTOR_AUTOMOTRIZ
3. TESIS (TecNM) — https://rinacional.tecnm.mx/bitstream/TecNM/5454/1/2016_MA_DIANA%20LUCIA_ACU%C3%91A_FIMBRES.pdf.pdf
4. Análisis sectorial industria automotriz (UTDT) — https://repositorio.utdt.edu/bitstreams/811e3aad-c203-49d8-9228-356b841346de/download
5. Estudio de mercado automotriz en los sectores productivos de Loja (UPS) — https://dspace.ups.edu.ec/bitstream/123456789/24525/1/UPS-CT010401.pdf
6. Informe de competencia del mercado automotriz — https://moot.up.edu.pe/Informe-de-competencia.pdf
7. Mercado automotriz chileno: un análisis empírico — https://repositorio.uchile.cl/handle/2250/116653
8. Investigación de Mercado para una Empresa del Sector Automotor (UNT) — https://face.unt.edu.ar/web/iadmin/wp-content/uploads/sites/2/2024/05/T55-Investigacion-de-mercado-para-una-empresa-del-sector-automotor_compressed.pdf
9. Tesis de Maestría (BUAP) — https://repositorioinstitucional.buap.mx/bitstream/handle/20.500.12371/5647/399514T.pdf?sequence=1
10. Estudio de mercado del sector automotriz como herramienta… (Dialnet) — https://dialnet.unirioja.es/servlet/articulo?codigo=7915375

## Estructura final en Hombros

| Ruta | Contenido |
|---|---|
| `01_PDFs/`, `02_HTML/`, `03_Repositorios/`, `04_Derivadas/` | Descarga de la búsqueda original (93 OK / 17 fallos), incluye el clon `TFG-2026` |
| `05_Rentabilidad_precio_autos/` | Análisis + descargas de la búsqueda de rentabilidad |
| `06_Calidad_precio_mercado/` | Análisis + descargas de la búsqueda de calidad/precio |
| `indice.md`, `manifest.jsonl` | Registro de cada descarga |
| `RESUMEN_NUEVAS_BUSQUEDAS.md` | Este resumen |

Los fallos se deben principalmente a HTTP 403/429, timeouts y dominios caídos; quedan registrados con su motivo en cada `manifest.jsonl` y `indice.md`.

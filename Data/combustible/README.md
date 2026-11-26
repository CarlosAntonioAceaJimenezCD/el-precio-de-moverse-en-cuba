# Precios del combustible en Cuba — serie histórica

Base: `precios_combustible.sqlite`, tabla `precios`.

| Campo | Significado |
|---|---|
| `fecha` | Fecha de la referencia publicada |
| `tipo` | Gasolina B100/B94/B90/B83, Diesel, Gasolina/Diesel genérico |
| `mercado` | `oficial CIMEX`, `informal`, `informal elToque`, `publicado` |
| `precio_min` / `precio_max` | Rango cuando la fuente da un rango; iguales cuando da un único valor |
| `moneda` | USD o CUP |
| `fuente` | Medio o sitio |
| `url` | Enlace original |
| `nota` | Contexto (moneda, vigencia, etc.) |

El script `Auxiliares/herramientas/scrape_infraestructura.py` vuelve a consultar las fuentes y añade nuevas observaciones sin duplicar las existentes. El timer `precio-combustible.timer` lo ejecuta cada mes.

## Fuentes actuales

- encuba.net (tarifa CIMEX vigente desde 15/05/2026, publicada 14/10/2026)
- Directorio Cubano (11/09/2026, mercado informal elToque + oficial CIMEX)
- D-Cuba (20/08/2026, mercado informal e importado)
- DailyFuels (18/11/2026)
- GlobalPetrolPrices (16/11/2026)

## Observación metodológica

Cada fuente usa un tipo de cambio distinto para expresar el precio en CUP. Por eso la serie guarda la moneda original y no convierte automáticamente: la comparación debe hacerse con la TRMI informal (930 CUP/USD, 18/11/2026) cuando se analice el costo real para el conductor cubano.

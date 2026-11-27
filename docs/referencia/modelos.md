# Funciones y modelos del análisis, y por qué están respaldados

Inventario de todo lo que transforma o estima el pipeline de `Data/analisis_rentabilidad`. Se separa en tres bloques: preparación determinista, estadística descriptiva e inferencia. La justificación es metodológica y también empírica: se dice qué se calculó, por qué esa forma y qué límite tiene con los datos actuales.

## 1. Preparación determinista (sin inferencia)

Estas funciones no "descubren" nada: hacen que los valores sean comparables. Su respaldo es la reproducibilidad y la trazabilidad.

| Función / regla | Qué hace | Por qué está respaldada |
|---|---|---|
| `parse_price` | Convierte `"13.000 USD"` en 13.000, `"2,300"` en 2300 y `"1.234,56"` en 1234,56. | Los portales mezclan coma de miles y punto decimal. Sin esta regla, un auto de 13.000 USD entraba como 13 USD y era rechazado. Es una normalización sintáctica, no una estimación. |
| `parse_number` | Igual que `parse_price`, pero para km y potencia. | `"80,000 km"` se leía como 80 km. Corregirlo cambió la mediana de kilometraje de 80 a <!-- kpi:km_medianos -->43.000 km. |
| `to_usd(precio, moneda)` | `precio × FX[moneda]` con TRMI informal: USD 1, CUP 1/930, EUR 1000/930, MLC 845,35/930. | En Cuba la tasa oficial no representa la transacción cotidiana. Usar una sola tasa declarada y fechada (18/11/2026) permite comparar anuncios en USD, EUR y CUP. No es un modelo: es una convención monetaria explícita. |
| `parse_title` / `parse_specs` | Extraen marca, modelo, año, km, potencia, combustible y transmisión del texto libre. | Los anuncios no traen columnas estructuradas. El regex es auditable y se aplica igual a todas las fuentes. |
| `slug_title` / `repair_title` | Reconstruyen títulos de interfaz desde el slug o el JSON-LD. | Evita que páginas como "Reportar este anuncio" se conviertan en autos. |
| `is_non_car` | Descarta triciclos, motos, repuestos y piezas por palabras clave. | El objetivo del proyecto son solo autos. Es una regla conservadora: se aplica al inicio del título para no perder anuncios que mencionan una moto en el cuerpo. |
| `condition_score` | `min(5, palabras positivas) − min(5, palabras negativas)`. | Convierte adjetivos del anuncio en una señal ordinal acotada. Es un **heurístico léxico**, no una medición validada: sirve como control, no como prueba. |
| `brand_tier` | `premium / medio / económico / desconocido`, según listas declaradas en `config.py`. | Ordena marcas por segmento sin inventar precios. Es una clasificación previa, contrastada después con Kruskal-Wallis. |
| Deduplicación | Clave `(brand, model, year, mileage_km, price_usd, source_type, canal)`, se conserva la última fila. | Evita contar dos veces el mismo anuncio repetido por el scraper, sin mezclar canal local con importación. |
| Filtros de rango | Precio 200–250.000 USD, año 1990–2027, km ≤ 600.000, título ≥ 6 caracteres. | Eliminan errores de captura y anuncios de servicios. Los rechazos se guardan en `rechazos.csv`, nunca se descartan sin registro. |

## 2. Estadística descriptiva

| Medida | Dónde se usa | Por qué está respaldada |
|---|---|---|
| Mediana | KPI principal de precio, benchmarks y canal. | El precio del auto usado cubano es asimétrico y tiene valores extremos; la mediana resiste mejor esos valores que la media. |
| Media | KPI secundario y `media_usd` por canal. | Se conserva para comparar con la mediana; la diferencia entre ambas revela la cola derecha de la distribución. |
| Cuartiles (p25, p75) | Benchmarks por marca/modelo/año e importación. | Dan un rango robusto sin suponer normalidad. Con `n ≥ 2` por grupo se evita sobreinterpretar un solo anuncio. |
| `car_age = 2026 − año` | Feature y filtro 0–40 años. | Es la edad observable del vehículo. Se acota a 40 porque fuera de ese rango hay clásicos con lógica de precio distinta. |
| `km_per_year = km / car_age` | Anomalías. | Normaliza el uso por año; un auto de 15 años con 30.000 km y uno de 3 años con 30.000 km no son iguales. |
| `price_per_1000km` | Feature derivado. | Permite comparar precio por desgaste, no solo precio absoluto. |
| `descuento_pct = (mediana_grupo − precio) / mediana_grupo × 100` | Infravalorados. | Mide distancia relativa al comparable, no solo dólares absolutos. Solo se calcula con grupos de al menos 2 anuncios. |
| `gap_vs_nuevo_pct` | Diferencia usado vs nuevo por modelo. | Expresa la depreciación como porcentaje del precio nuevo, comparable entre marcas. |

## 3. Inferencia y modelos

### 3.1 Modelo hedónico log-lineal (OLS)

Fórmula vigente en `04_stats.py`:

```
log(price_usd) ~ car_age + log1p(mileage_km) + hp + condition_score + C(brand_tier)
```

Se estima por mínimos cuadrados ordinarios sobre **usados del canal local**, con precio > 0, año presente y `car_age` entre 0 y 40. Solo se incluye un término si hay más de 30 observaciones no nulas, y el modelo exige más de 30 filas.

**Por qué está respaldado:**
- **Logaritmo del precio:** los precios son positivos y muy asimétricos; el log estabiliza la varianza y permite leer coeficientes como aproximaciones de cambio porcentual.
- **`log1p(km)`:** el kilometraje también es asimétrico y `log(0)` no existe; `log1p` admite autos con 0 km.
- **Atributos hedónicos:** precio, antigüedad, km, potencia, condición y marca son los determinantes estándar de un modelo hedónico de autos usados.
- **Dummies de marca (`C(brand_tier)`):** permiten que cada segmento tenga su propio intercepto sin imponer una relación lineal entre "categoría" y precio.
- **Muestreo restringido:** mezclar importación con mercado local, o nuevos con usados, introduciría dos regímenes de precios distintos; por eso se separaron en `canal` y `source_type`.

**Resultado actual y su límite:** con **22 observaciones completas** de 897 candidatas ningún coeficiente alcanza significancia (el p_valor más bajo es 0,165, de potencia; antigüedad tiene p = 0,237). La muestra se reduce a 22 porque `hp` solo está presente en 52 filas y `mileage_km` en 572; al exigir todos los términos a la vez se descarta el 97,5 % de las candidatas (R² = 0,277; p del F = 0,623). El modelo está correctamente especificado para la forma de los datos, pero **no permite afirmar una tasa de depreciación anual ni una prima premium** con esta muestra transversal. Decirlo es parte del respaldo: el método sostiene la conclusión de que no hay conclusión numérica estable.

### 3.2 VIF (factor de inflación de varianza)

Para cada variable `j`: se regresa `X_j` contra el resto y se calcula `VIF_j = 1 / (1 − R²_j)`.

**Por qué está respaldado:** detecta multicolinealidad antes de interpretar coeficientes. Valores cercanos a 1 (los actuales van de 1,13 a 1,58) indican que los regresores no se explican entre sí; por tanto, la falta de significancia no se atribuye a colinealidad.

### 3.3 Kruskal-Wallis

Se aplica a los precios por `brand_tier` (grupos con más de 5 observaciones). Resultado vigente: H = 25,741, p = 1e−05.

**Por qué está respaldado:** es la alternativa no paramétrica a ANOVA; no exige normalidad y compara distribuciones completas, no solo medias. Encaja con precios asimétricos y con tres grupos de distinto tamaño. Permite afirmar que **los tiers no provienen de la misma distribución de precios**, aunque el OLS no asigne un coeficiente significativo a cada dummy.

### 3.4 Welch t-test (codificado, no ejecutado en la corrida actual)

Compara precios usados vs nuevos con varianzas desiguales (`equal_var=False`).

**Por qué está respaldado:** Welch no supone varianzas iguales, condición que rara vez se cumple cuando los tamaños de grupo son muy distintos. En la corrida actual no se dispara porque el subconjunto del modelo contiene solo autos usados (`is_new` no varía); queda disponible para Cuando se integren catálogos de nuevos al mismo marco.

### 3.5 Detección de anomalías

- `km_anormal`: `km_per_year > 40.000` o `< 500`.
- `precio_atipico`: precio por debajo del percentil 1 o por encima del percentil 99.
- Se reportan <!-- kpi:anomalias -->81 anomalías en la corrida vigente.

**Por qué está respaldado:** los umbrales de km/año son criterios de uso extremo, y los percentiles 1/99 son una regla robusta de colas. No eliminan filas del análisis principal: solo las señalan para revisión.

## 4. Lo que NO se hace (y por eso el análisis es honesto)

- No se usa la tasa oficial de cambio.
- No se imputan precios ni kilómetros faltantes.
- No se afirma causalidad: el modelo es de asociación sobre un corte transversal.
- No se presenta una curva de depreciación temporal: hace falta una serie mensual de 6–12 meses.
- No se mezclan mercados: local e importación se reportan por separado.

Los números y tablas que alimentan estas funciones están en `outputs/tables/`; el detalle del OLS está en `outputs/tables/modelo_resumen.txt`.

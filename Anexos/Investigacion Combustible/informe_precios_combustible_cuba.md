# Precio del combustible en Cuba: investigación y marco normativo

**Fecha del informe:** 16 de noviembre de 2026
**Ámbito:** precios minoristas y mayoristas de gasolinas y diésel, serie histórica 2021-2026, fuentes oficiales, prensa independiente, agregadores y mercado informal.
**Archivos asociados:** `precios_combustible_cuba.csv` (tabla normalizada por fecha, combustible, moneda y ámbito), `mapa_fuentes.csv` (origen y fiabilidad de cada dato), carpeta `fuentes/` (texto extraído de cada nota).

---

## 1. Conclusión ejecutiva

1. **No existe una tarifa única oficial en divisas desde el 15 de mayo de 2026.** El Ministerio de Finanzas y Precios (MFP) anunció el 12 de mayo de 2026 que, a partir del 15 de mayo a las 00:00, los precios de venta en divisas se actualizan **al alza o a la baja según el costo real de cada operación de importación**. Coexisten precios minoristas distintos según el operador (proveedor, fletes, ruta, seguros y riesgos). El comunicado oficial **no incluye tabla de precios**.
2. **La referencia oficial dolarizada más citada es la Circular Especial 03/2026 de Cimex**, vigente desde el 15 de mayo de 2026 a las 12:00: B100 **2,60 USD/L**, B94 **2,00 USD/L**, B90 **1,90 USD/L**, B83 **1,80 USD/L**, diésel especial **2,20 USD/L** y diésel regular **2,00 USD/L**. CiberCuba publicó el documento y confirmó su veracidad con fuentes internas. No se localizó esta circular en la Gaceta Oficial; es un acto corporativo, no una norma jurídica publicada.
3. **Los precios en pesos cubanos (CUP) fijados por norma jurídica siguen siendo los del Acuerdo 9810 del Consejo de Ministros** (Gaceta Oficial GOC-2024-EX10, 1 de marzo de 2024): gasolina 100 octanos **198,00 CUP/L**, 94 octanos **156,00 CUP/L**, 90 octanos **132,00 CUP/L**, 83 octanos **114,00 CUP/L** y diésel regular **132,00 CUP/L**. El mismo acuerdo fijó precios en USD de 1,65 / 1,30 / 1,10 / 0,95 / 1,10 USD/L para la red inicial de servicentros en divisas.
4. **El mercado informal opera muy por encima de la tarifa oficial:** en septiembre de 2026, elToque (vía Directorio Cubano) registró B94 a **7.000-8.000 CUP/L**, B90 a **3.200-4.000 CUP/L**, B83 a **3.300 CUP/L** y petróleo/diésel a **1.600-2.000 CUP/L**. En abril-mayo de 2026 CiberCuba registró gasolina a **4.000-6.000 CUP/L**. Estos valores son observaciones de mercado, **no precios oficiales**.
5. **Los agregadores divergen entre sí y de la norma:** GlobalPetrolPrices (9-nov-2026) da 240,96 CUP/L y 2,00 USD/L; Numbeo (6-nov-2026) da 1,26 USD/L (rango 1,00-1,40; 253 entradas de 21 contribuyentes). Deben tratarse como referencias de conversión/percepción, no como tarifas.

---

## 2. Serie histórica de precios oficiales

### 2.1 Vigente desde el 1 de enero de 2021 (Acuerdo 8957/2020, GOC-2020-EX68)

| Producto | Precio minorista (CUP/L) |
|---|---:|
| Gasolina 100 octanos | 37,50 |
| Gasolina 94 octanos | 30,00 |
| Gasolina 90 octanos | 25,00 |
| Gasolina 83 octanos | 20,00 |
| Diésel regular | 25,00 |

El acuerdo fijó además gas licuado a 21,30 CUP/kg y gas manufacturado a 2,50 CUP/m³. Estos precios rigieron hasta el 29 de febrero de 2024.

### 2.2 Vigente desde el 1 de marzo de 2024 (Acuerdo 9810/2024, GOC-2024-EX10)

| Producto | Precio minorista CUP/L | Precio minorista USD/L |
|---|---:|---:|
| Gasolina 100 octanos | 198,00 | 1,65 |
| Gasolina 94 octanos | 156,00 | 1,30 |
| Gasolina 90 octanos | 132,00 | 1,10 |
| Gasolina 83 octanos | 114,00 | 0,95 |
| Diésel regular | 132,00 | 1,10 |

El Acuerdo 9810 dejó sin efecto los precios del Anexo I del Acuerdo 8957/2020. El Acuerdo 9811 (misma edición) complementa el paquete. El alza se anunció el 9 de enero de 2024, se aplazó el 31 de enero por un incidente de ciberseguridad en los sistemas de comercialización de Cimex y finalmente se aplicó el 1 de marzo de 2024, con los precios mayoristas sin modificación para transportistas.

### 2.3 Desde el 15 de mayo de 2026 (liberalización y circular de Cimex)

Comunicado del MFP (12-may-2026): el precio único y fijo "no se puede sostener económicamente en las presentes condiciones"; en lo adelante coexisten diferentes precios minoristas publicados en las estaciones de servicio según el costo real de importación de cada actor económico.

**Circular Especial 03/2026 de Cimex, S.A. (15-may-2026, 12:00), precios minoristas USD/L:**

| Producto | USD/L | Precio anterior aproximado |
|---|---:|---:|
| Gasolina especial B100 | 2,60 | ~1,30 |
| Gasolina especial B94 | 2,00 | — |
| Gasolina regular B90 | 1,90 | — |
| Gasolina motor B83 | 1,80 | — |
| Diésel especial | 2,20 | — |
| Diésel regular | 2,00 | — |

**Tabla posterior de Cimex con fecha de datos 11-sep-2026** (Directorio Cubano, captura de noviembre de 2026), precios USD/L:

| Producto | Mayorista | Minorista |
|---|---:|---:|
| Gasolina especial B100 | 2,50 | 2,60 |
| Gasolina especial B94 | 1,90 | 2,00 |
| Gasolina regular B90 | 1,80 | 2,50 (*) |
| Gasolina motor B83 | 1,70 | 1,80 |
| Diésel especial | 2,10 | 2,20 |
| Diésel regular | 1,90 | 2,00 |

(*) Valor publicado por la fuente. Es llamativo que el minorista de B90 (2,50) supere al de B94 (2,00); se conserva tal cual aparece en la tabla y conviene verificarlo contra el servicentro concreto, sobre todo después de la liberalización de precios.

---

## 3. Mercado informal y referencias externas

### 3.1 Mercado informal (no oficial)

| Fecha de dato | Producto | Rango CUP/L | Fuente |
|---|---|---:|---|
| sep-2026 | Gasolina especial B94 | 7.000 - 8.000 | elToque vía Directorio Cubano |
| sep-2026 | Gasolina regular B90 | 3.200 - 4.000 | elToque vía Directorio Cubano |
| sep-2026 | Gasolina motor B83 | 3.300 | elToque vía Directorio Cubano |
| sep-2026 | Petróleo / diésel | 1.600 - 2.000 | elToque vía Directorio Cubano |
| abr-may-2026 | Gasolina (general) | 4.000 - 6.000 | CiberCuba (≈7-12 USD/L al cambio informal) |
| oct-2025 | Gasolina regular (fuera de cuota) | > 450 | elToque |
| mar-2026 | Gasolina (general) | 30 USD/galón (≈7,93 USD/L) | BBC News Mundo, citada en el expediente |

La brecha entre el precio oficial dolarizado (~2,00-2,60 USD/L) y el informal (hasta ~7-12 USD/L en 2026) explica que la tarifa oficial sea solo un punto de referencia para quienes tienen acceso a divisas.

### 3.2 Agregadores y encuestas

| Fuente | Fecha | Valor | Observación |
|---|---|---:|---|
| GlobalPetrolPrices | 09-nov-2026 | 240,96 CUP/L; 2,00 USD/L; 1,791 EUR/L | Conversión propia de la fuente |
| Numbeo | 06-nov-2026 | 1,26 USD/L (1,00-1,40) | 253 entradas de 21 contribuyentes |

La API de precios y el sitio de CUPET no proporcionan una lista de precios de combustibles; CUPET solo publica servicios y contactos.

---

## 4. Cronología de los cambios

| Fecha | Hecho |
|---|---|
| 25-nov-2020 | Consejo de Ministros aprueba el Acuerdo 8957 (publicado 10-dic-2020). |
| 01-ene-2021 | Entran en vigor los precios en CUP del Acuerdo 8957. |
| 09-ene-2024 | El MFP anuncia una fuerte actualización de precios de combustibles, gas licuado y tarifa eléctrica; rango difundido 114-198 CUP/L. |
| 31-ene-2024 | Se aplaza la entrada en vigor por un incidente de ciberseguridad en los sistemas de Cimex. |
| 01-mar-2024 | Entra en vigor el Acuerdo 9810/2024 (GOC-2024-EX10): nuevos precios en CUP y los primeros precios minoristas oficiales en USD. |
| 12-feb-2026 | Resolución 1/2026 (GOC-2026-EX22) faculta al director de la Unión Cubapetróleo a aprobar precios mayoristas de combustibles en USD. |
| 12-may-2026 | El MFP anuncia el fin del precio único en divisas y la liberalización según costo real de cada operación, vigente el 15 de mayo. |
| 15-may-2026 | Circular Especial 03/2026 de Cimex fija la nueva escala minorista en USD (B100 hasta 2,60 USD/L). |
| 11-sep-2026 | Fecha de los datos de la tabla oficial mayorista/minorista y del mercado informal recogida por Directorio Cubano/elToque. |
| 06-09-nov-2026 | Actualizaciones de Numbeo y GlobalPetrolPrices. |

---

## 5. Metodología, fuentes y salvedades

- **Fuentes oficiales**: Gaceta Oficial de Cuba (PDF íntegro, extraído con `pdftotext`), Granma y Cubadebate (texto del comunicado del MFP). Son la base de las tablas normativas de 2021 y 2024.
- **Acceso a la prensa**: Cubadebate, CiberCuba, Diario de Cuba y otros medios cubanos bloquean las conexiones TLS directas desde este entorno. Se recuperaron las notas mediante la Wayback Machine (`http://web.archive.org/web/<timestamp>id_/<url>`) y su API CDX. Los textos extraídos se conservan en `fuentes/`.
- **Google News**: el RSS entregó 48 titulares, pero sus enlaces redirigen a imágenes; se usaron los titulares solo como mapa y se resolvieron las URL definitivas mediante CDX. Bing/Mojeek no aportaron resultados útiles.
- **Búsqueda en la Gaceta**: el endpoint de texto completo (`getdata`/`texto_norma`) responde HTTP 500. Por ello se rastreó el catálogo local de 4.748 ediciones por organismo (MFP) y se sondearon directamente los PDF candidatos de 2020, 2024 y 2026 con `pdftotext`.
- **No se encontró** ninguna resolución de la Gaceta que fije los precios minoristas de mayo de 2026; el cambio se instrumentó por comunicado del MFP y circular de Cimex. Las resoluciones del MFP de 2026 revisadas tratan otros temas (facultades de precios, gas licuado, comercio, etc.).
- **Etiquetas de fiabilidad**: "Alta" = norma o medio oficial; "Media-Alta" = medio independiente que reproduce un documento con verificación; "Media" = prensa independiente; "Baja-Media"/"Baja" = agregadores y encuestas. El mercado informal siempre se marca como **no oficial**.
- **Descarga de la Gaceta**: al cierre de este informe la descarga masiva de todas las ediciones continúa en segundo plano (véase `../Leyes/estado_descarga.json`). Los PDF normativos citados se descargaron además de forma puntual para esta investigación.

---

## 6. Uso sugerido para el proyecto

- Para modelar costos de importación o ventas en divisas: usar la serie **Cimex USD** de 2024, mayo de 2026 y septiembre de 2026, con la salvedad de que desde mayo de 2026 puede haber **múltiples precios simultáneos** por operador.
- Para costos en moneda nacional: usar los precios **CUP oficiales del Acuerdo 9810** y, separadamente, los rangos **informales de elToque** como escenario alto.
- No mezclar en una sola serie los valores de GlobalPetrolPrices/Numbeo con las tarifas normativas; son referencias de conversión y percepción, no precios regulados.

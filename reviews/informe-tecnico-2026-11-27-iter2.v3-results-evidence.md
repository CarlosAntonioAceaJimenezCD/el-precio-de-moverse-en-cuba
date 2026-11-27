---
type: audit-artifact
phase: v3-results-evidence
slug: informe-tecnico-2026-11-27-iter2
generated_at: 2026-11-27T19:15:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter2/informe-tecnico-2026-11-27-iter2.text.md
language: es
---

# V3 — Resultados ↔ evidencia

Se recorren los claims de tipo `result` y los claims metodológicos con contenido numérico del inventario E1 de la iteración 2, contrastados contra los CSV vigentes en `Data/analisis_rentabilidad/outputs/tables/` y contra el inventario E3 de esta misma iteración. Los números del modelo se leen de `modelo_muestra.csv` (principal: 981 candidatas / 584 observaciones / R² 0,101 / p_f 0,0; completo: 981 / 28 / 0,2744 / 0,4114).

### F-V3-001 — «2.029 anuncios limpios» y «43.000 km» en §59 contra 2.156 y 33.256 km en el `kpis.csv` que cita

El §59 (L1379) afirma: «El relato ahora usa **772 autos únicos**, **2.029 anuncios limpios** (1.338 locales y 691 de importación), mediana local de **21.000 USD**, kilometraje mediano de **43.000 km**, 50 marcas, 101 grupos comparables y 81 anomalías (corrida vigente del 27/11/2026; los valores se actualizan solos en `outputs/tables/kpis.csv`)». El archivo citado, `Data/analisis_rentabilidad/outputs/tables/kpis.csv`, registra `anuncios_totales=2156.0`, `anuncios_locales=1465.0`, `anuncios_importacion=691.0`, `precio_mediano_usd=21000.0`, `marcas_distintas=50.0` y `km_medianos=33256.0`; `benchmark.csv` contiene 113 filas de datos y `anomalias.csv` 89. Coinciden tres de las nueve cifras (691, 21.000 USD, 50); difieren las otras seis: 772/952 autos (el marcador `<!-- kpi:autos_revolico -->` de `PRESENTACION_STORYTELLING.md:3,75` vale 952), 2.029/2.156, 1.338/1.465, 43.000/33.256 km, 101/113 grupos y 81/89 anomalías.

La cláusula «los valores se actualizan solos en `outputs/tables/kpis.csv`» no se sostiene en el estado contrastado: `Auxiliares/herramientas/actualizar_numeros.py:49–86` deriva precisamente `anuncios_totales`, `anuncios_locales`, `km_medianos`, `grupos_benchmark` (longitud de `benchmark.csv`) y `anomalias` (longitud de `anomalias.csv`) de esos CSV, y son los valores del párrafo anterior los que allí figuran. El propio `PRESENTACION_STORYTELLING.md:75–77,201–211`, que §59 dice haber actualizado con la narrativa vigente, lleva los marcadores resueltos 952 / 2.156 / 1.465 / 33.256 km / 113 / 89, no los del informe. El inventario E3 (§Missing artifacts, líneas 268–271) ya anticipó esta desincronización parcial del artefacto.

— polarity: negative · confidence: high · related: [[#C003]], [[#C050]], [[#C036]]

### F-V3-002 — Tres estados de la misma corrida conviven entre §58, §59 español y §59 inglés

El §59 español (L1379) describe la «corrida vigente del 27/11/2026» con 772 autos, 2.029 anuncios y 43.000 km; el párrafo **EN.** inmediatamente posterior (L1383) presenta esa misma sección con «744 unique cars, 2,014 clean listings, 21,000 USD median»; y §58 (L1371) atribuye a la regeneración anterior «**2.014 anuncios limpios**, de ellos 1.323 locales y 691 de importación; mediana local 21.000 USD y mediana de kilometraje 44.125 km». El espejo inglés no reproduce la cifra de su párrafo español, sino el estado previo. §51 (L1279) añade 744 autos únicos y §45 (L1214) una cuarta versión con mediana de 23.000 USD, 6,3 años, 34 marcas, 27 grupos y −5,43 %/año, sin marca de vigencia. Solo §59 español rotula su estado como vigente; los pasajes paralelos sostienen cifras distintas sin señalar la fecha de referencia que las diferencia.

— polarity: negative · confidence: high · related: [[#C003]], [[#C036]], [[#C049]], [[#C050]], [[#C006]]

### F-V3-003 — R² 0,277 en §59 frente a 0,274 en `modelo_muestra.csv` y en `MODELOS_Y_FUNCIONES.md`

El §59 (L1381) escribe, con marcadores automáticos: «El modelo con todos los términos dispone de **<!-- kpi:modelo_n_completo -->28 observaciones completas** de <!-- kpi:modelo_candidatas -->981 candidatas (R² = <!-- kpi:modelo_r2_completo -->0,277; p del F = <!-- kpi:modelo_pf_completo -->0,411)». En `modelo_muestra.csv` la fila `completo` registra `r2=0.2744`, y `modelo_resumen.txt` muestra «R-squared: 0.274»; `Auxiliares/herramientas/actualizar_numeros.py:80` formata esa clave con tres decimales, lo que da `0,274`. El mismo marcador en `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md` está resuelto como `<!-- kpi:modelo_r2_completo -->0,274`. El valor 0,277 no es el redondeo de 0,2744 y coincide con el estado retirado de 22 observaciones de 897 candidatas que describe el inventario E3 (línea 143). Los otros tres marcadores de la frase sí concuerdan con el CSV: `observaciones=28`, `candidatas=981` y `p_f=0.4114` → 0,411.

— polarity: negative · confidence: high · related: [[#C003]], [[#C004]], [[#C005]]

### F-V3-004 — «p mínimo 0,165» y «VIF 1,13–1,58» de §60 no aparecen en los CSV de la corrida vigente

El §60 (L1389) afirma que «la corrida actual **no** sostiene una tasa de depreciación ni una prima premium significativa (p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05)». En `modelo_depreciacion.csv` el menor `p_valor` de los coeficientes no intercepto es 0,0941 (`C(brand_tier)[T.medio]`), `car_age` vale 0,1504 y `hp` 0,1403; en `vif.csv` el rango va de 1,12 (`hp`) a 1,40 (`mileage_km`); y `tests.csv` registra el Kruskal-Wallis con `p_valor=0.0`, sin la precisión `1e−05` que consigna el texto. Las tres cifras del paréntesis sí se encuentran en la fuente citada por §60, `MODELOS_Y_FUNCIONES.md` (líneas 56 y 62: «el p_valor más bajo es 0,165, de potencia; antigüedad tiene p = 0,237» y «los actuales van de 1,13 a 1,58»), de modo que la cadena claim → documento citado → CSV se rompe en el último eslabón: esas cifras son de una corrida anterior. La afirmación cualitativa de fondo, en cambio, se sostiene con los archivos vigentes: los siete coeficientes no intercepto tienen p ≥ 0,0941 y ninguno alcanza 0,05.

— polarity: negative · confidence: high · related: [[#C004]], [[#C005]]

### F-V3-005 — El modelo principal de 584 observaciones queda fuera del relato de «no significancia» de §59

El §59 (L1381) sintetiza: «la depreciación se reformuló con honestidad: el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje». `modelo_muestra.csv` contiene una segunda especificación, `principal` (981 candidatas, 584 observaciones, R² 0,101, `p_f=0.0`), que el párrafo no menciona: el único modelo cuantificado en la frase es el `completo`, de 28 observaciones y `p_f=0.4114`. El propio `MODELOS_Y_FUNCIONES.md`, en el bloque «Modelo principal frente a modelo completo», registra que «en el modelo principal el coeficiente de antigüedad es positivo y alcanza p < 0,05» y lo atribuye a «un artefacto de selección, no una tasa anual» de la submuestra que declaró kilometraje. La frase en singular «el modelo actual» describe por tanto una de las dos especificaciones archivadas, y `actualizar_numeros.py:82–86` expone explícitamente los marcadores del modelo omitido (`modelo_n_principal`, `modelo_r2_principal`, `modelo_pf_principal`) que §59 no usa. La cobertura del relato es parcial respecto de la evidencia del propio pipeline.

— polarity: negative · confidence: high · related: [[#C004]], [[#C005]]

### F-V3-006 — La retirada de la depreciación y de la prima premium coincide con los coeficientes archivados

El §59 (L1381) sostiene que «la depreciación se reformuló con honestidad: el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra», y §60 (L1389) que «la corrida actual **no** sostiene una tasa de depreciación ni una prima premium significativa». En `modelo_depreciacion.csv` el coeficiente de `car_age` es −0,0632 con `p_valor=0.1504` y el de `C(brand_tier)[T.premium]` es +0,1146 con `p_valor=0.8753`; `modelo_resumen.txt` reproduce la misma estimación (28 observaciones, R² 0,274, F 1,081, p del F 0,411). Ninguno de los siete coeficientes no intercepto alcanza p < 0,05. La retirada del −5,43 %/año y del +21 % de prima de la §34 (L1056) como cifras vigentes queda respaldada por los archivos de la corrida, con la salvedad de la especificación principal de 584 observaciones descrita en [[#F-V3-005]]. Los marcadores `28`, `981` y `0,411` de §59 también coinciden con `modelo_muestra.csv`; el que no coincide es el R² (ver [[#F-V3-003]]).

— polarity: positive · confidence: high · related: [[#C004]], [[#C005]], [[#C006]], [[#F-V3-003]]

## Resumen

- Seis hallazgos: cinco negativos y uno positivo; ninguno depende de un juicio de nivel, sino de cotejo claim ↔ CSV.
- §59 cita `kpis.csv` como fuente autoactualizada pero seis de sus nueve cifras difieren de los CSV vigentes (2.029/2.156; 43.000/33.256 km; 101/113; 81/89).
- El R² 0,277, el p mínimo 0,165 y el VIF 1,13–1,58 de §59–§60 corresponden a una corrida anterior; la no significancia cualitativa sí se sostiene, aunque el modelo principal de 584 observaciones queda fuera del relato.

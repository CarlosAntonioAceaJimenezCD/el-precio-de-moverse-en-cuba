---
type: audit-artifact
phase: v3-results-evidence
slug: informe-tecnico-2026-11-27-iter3
generated_at: 2026-11-28T01:24:14-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter3/informe-tecnico-2026-11-27-iter3.text.md
language: es
---

# V3 — Resultados frente a evidencia

Se contrastan los enunciados de resultado de la caché auditada (§59, §60, §71.1–§71.3) con los CSV vigentes en `Data/analisis_rentabilidad/outputs/tables/` —`kpis.csv`, `kpis_canal.csv`, `modelo_muestra.csv`, `modelo_depreciacion.csv`, `vif.csv`, `tests.csv`, `anomalias.csv`, `benchmark.csv`— y con el generador `Auxiliares/herramientas/actualizar_numeros.py`. La caché no contiene marcadores `Tabla N` / `Figura N`; las tablas se citan por sección y líneas.

### F-V3-001 — Las cifras canónicas de §59 divergen entre el texto español y su espejo inglés

El párrafo español de §59 (línea 1379) afirma: «El relato ahora usa **772 autos únicos**, **2.029 anuncios limpios** (1.338 locales y 691 de importación), mediana local de **21.000 USD**, kilometraje mediano de **43.000 km**, 50 marcas, 101 grupos comparables y 81 anomalías». El espejo inglés de la misma sección (línea 1383) declara: «Updated the storytelling to the final dataset while preserving the author's voice: 744 unique cars, 2,014 clean listings, 21,000 USD median and a statistically honest depreciation narrative». Las dos versiones coinciden solo en 691 anuncios de importación y en la mediana de 21.000 USD; 772 frente a 744 y 2.029 frente a 2.014 son cantidades distintas para la misma corrida «vigente del 27/11/2026». La cifra inglesa de 744 coincide con la deduplicación documentada en §51 (línea 1279: «814 filas con 748 IDs únicos → **744 autos únicos**»); la española de 2.014 coincide con el estado anterior de §58 (línea 1371: «**2.014 anuncios limpios**, de ellos 1.323 locales y 691 de importación»). Relación: inconsistencia interna entre dos secciones que presentan los mismos datos como definitivos.

— polarity: negative · confidence: high · related: [[#C003]], [[#C039]], [[#C053]]

### F-V3-002 — «2.029 anuncios limpios / 1.338 locales» no coincide con `kpis.csv`, y las cifras carecen de marcador automático

La afirmación de §59 (línea 1379) «**2.029 anuncios limpios** (1.338 locales y 691 de importación)» se presenta como parte de una corrida cuyos «valores se actualizan solos en `outputs/tables/kpis.csv`». El CSV vigente registra `anuncios_totales,2156.0`, `anuncios_locales,1465.0` y `anuncios_importacion,691.0`: solo el componente de importación coincide; el total y el componente local difieren en 127 anuncios cada uno. El generador `Auxiliares/herramientas/actualizar_numeros.py` (líneas 23–29 y 49–70) actualiza únicamente los números precedidos por `<!-- kpi:clave -->`, y el relato generado `Data/analisis_rentabilidad/PRESENTACION_STORYTELLING.md` (líneas 75 y 201–203) lleva los marcadores con los valores del CSV: «<!-- kpi:anuncios_totales -->2.156 anuncios limpios: <!-- kpi:anuncios_locales -->1.465 del mercado local». Los tres números del párrafo de §59 están escritos a mano, sin marcador. Relación: desajuste numérico entre texto y la tabla que el propio texto designa como fuente, junto con una descripción del mecanismo de actualización que no alcanza esas cifras.

— polarity: negative · confidence: high · related: [[#C003]], [[#C008]]

### F-V3-003 — Kilometraje, grupos comparables y anomalías de §59 difieren de los CSV vigentes

El mismo párrafo de §59 (línea 1379) reporta «kilometraje mediano de **43.000 km**, 50 marcas, 101 grupos comparables y 81 anomalías». `kpis.csv` registra `km_medianos,33256.0`; `benchmark.csv` contiene 113 filas de grupos de marca/modelo/año y `anomalias.csv` contiene 89 filas de datos, no 101 ni 81. El propio generador calcula `salida["grupos_benchmark"] = es_espana(len(filas_csv(TABLAS / "benchmark.csv")))` y `salida["anomalias"] = es_espana(len(filas_csv(TABLAS / "anomalias.csv")))` (actualizar_numeros.py, líneas 71–72), y el relato generado (PRESENTACION_STORYTELLING.md, línea 77) muestra los marcadores resueltos: «<!-- kpi:grupos_benchmark -->113 grupos de marca, modelo y año comparables, detectamos <!-- kpi:infravalorados -->30 oportunidades infravaloradas y <!-- kpi:anomalias -->89 anomalías». `MODELOS_Y_FUNCIONES.md` (línea 80) también consigna 89. Las 50 marcas sí coinciden con `marcas_distintas,50.0`. Relación: tres desajustes numéricos contra la evidencia citada, con un cuarto valor (50 marcas) plenamente respaldado.

— polarity: negative · confidence: high · related: [[#C003]]

### F-V3-004 — R² 0,277 del modelo completo no es redondeable desde `modelo_muestra.csv` y su marcador no se actualiza

§59 (línea 1381) escribe «(R² = <!-- kpi:modelo_r2_completo -->0,277; p del F = <!-- kpi:modelo_pf_completo -->0,411)». `modelo_muestra.csv` registra para `completo`: `981,28,0.2744,0.4114`. El valor 0,277 no es el redondeo a tres decimales de 0,2744, que es 0,274 —cifra que sí aparece en §71.2 (línea 1499: «el R² baja de 0,274 a 0,101»)—, de modo que el documento da dos valores distintos al mismo coeficiente. El marcador `<!-- kpi:modelo_r2_completo -->` permanece en 0,277 incluso tras ejecutar `python3 Auxiliares/herramientas/actualizar_numeros.py --check`: la expresión `MARCADOR = re.compile(r"(<!-- kpi:([a-z_]+) -->)(...)")` (línea 35) admite solo letras y guion bajo en la clave, mientras que `modelo_r2_completo` contiene el dígito «2»; el patrón no reconoce ese marcador y `valores()` (línea 80, `es_espana(float(fila["r2"]), 3)`) nunca lo reescribe. El p del F 0,411, en cambio, coincide con 0,4114 redondeado. Relación: desajuste numérico e inconsistencia interna, con una causa mecánica verificable en el código del actualizador.

— polarity: negative · confidence: high · related: [[#C005]], [[#C014]], [[#C015]]

### F-V3-005 — «p mínimo 0,165, de potencia» no aparece en `modelo_depreciacion.csv`

§60 (línea 1389) sostiene: «la corrida actual **no** sostiene una tasa de depreciación ni una prima premium significativa (p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05)». En `modelo_depreciacion.csv`, el p_valor de `hp` es 0,1403 y el de `car_age` es 0,1504; el menor p_valor entre los términos no intercepto es 0,0941, correspondiente a `C(brand_tier)[T.medio]`. El número 0,165 consta como texto fijo en `MODELOS_Y_FUNCIONES.md` (línea 54: «el p_valor más bajo es 0,165, de potencia; antigüedad tiene p = 0,237»), documento que además afirma «La muestra se reduce a 22», mientras `modelo_muestra.csv` registra 28 observaciones completas. La conclusión cualitativa de no significancia se mantiene —todos los p_valores no intercepto del CSV superan 0,05—, pero la cifra puntual citada y su atribución al término `hp` no se derivan del CSV vigente. Relación: desajuste entre la cifra narrada y la tabla que la sostiene, por interpolación de un valor incrustado en otro documento.

— polarity: negative · confidence: high · related: [[#C004]], [[#C061]]

### F-V3-006 — Rango de VIF 1,13–1,58 frente a 1,12–1,40 en `vif.csv`

La misma frase de §60 (línea 1389) declara «VIF 1,13–1,58». `vif.csv` contiene cinco registros: `car_age,1.38`, `mileage_km,1.4`, `price_usd,1.16`, `hp,1.12`, `condition_score,1.14`. El rango observado es 1,12–1,40: el extremo inferior difiere en 0,01 y el superior en 0,18. `MODELOS_Y_FUNCIONES.md` (línea 62) repite el mismo intervalo «los actuales van de 1,13 a 1,58». La interpretación del texto —«los regresores no se explican entre sí»— no cambia con el rango real, pero la cifra citada no corresponde a la tabla. Relación: desajuste numérico entre texto y tabla.

— polarity: negative · confidence: high · related: [[#C004]]

### F-V3-007 — Kruskal-Wallis p = 1e−05 no consta en `tests.csv`

§60 (línea 1389) cierra la frase con «Kruskal-Wallis p = 1e−05». `tests.csv` contiene una sola fila: `Kruskal-Wallis precio por tier,31.232,0.0`, es decir, estadístico 31,232 y p_valor 0,0. `MODELOS_Y_FUNCIONES.md` (línea 66) registra «Resultado vigente: H = 25,741, p = 1e−05», con un estadístico distinto del del CSV. Ninguno de los dos CSV vigentes (`tests.csv`, `modelo_depreciacion.csv`) contiene el valor 1e−05; la precisión de cinco decimales declarada en el texto excede la resolución del archivo citado, que trunca el p_valor a 0,0. Relación: evidencia insuficiente para la cifra afirmada y divergencia del estadístico entre el documento metodológico y el CSV.

— polarity: negative · confidence: high · related: [[#C004]], [[#C060]]

### F-V3-008 — MAE 18.220,46 USD de §71.1: denominador respaldado, métrica sin evidencia en los CSV

La tabla sin numerar de §71.1 (líneas 1489–1493) registra «| Mediana global ( ingenua ) | Predice la mediana de los usados locales | MAE 18.220,46 USD sobre 1.444 anuncios |». El denominador 1.444 coincide exactamente con `anuncios_usados_locales,1444.0` en `kpis.csv`. El MAE 18.220,46 no aparece en ninguno de los archivos de `outputs/tables/` ni en los scripts de `Data/analisis_rentabilidad/scripts/`; la única aparición del número en el repositorio es el propio informe y su copia generada en `docs/referencia/informe.md` (línea 1491). La misma tabla atribuye al modelo principal «R² 0,101 sobre 584 observaciones», valores que sí coinciden con la fila `principal` de `modelo_muestra.csv`. Relación: claim compuesto con un componente plenamente respaldado y otro sin evidencia interna verificable.

— polarity: negative · confidence: medium · related: [[#C014]]

### F-V3-009 — Ablación de `hp` y no significancia del modelo completo: respaldo consistente

§71.2 (línea 1499) afirma: «`modelo_muestra.csv` documenta la ablación del término `hp`: al retirarlo, la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² baja de 0,274 a 0,101. El cambio de especificación y el cambio de muestra se informan juntos». El CSV contiene exactamente dos filas —`completo,981,28,0.2744,0.4114` con `hp` en los términos, y `principal,981,584,0.101,0.0` sin `hp`—, de modo que candidatas, observaciones y R² coinciden y la salvedad sobre el cambio simultáneo de muestra y especificación está escrita en el propio texto. §71.4 (línea 1512) añade: «el modelo completo usa 28 observaciones y ningún coeficiente alcanza p < 0,05», afirmación coherente con `modelo_depreciacion.csv`, cuyos p_valores no intercepto van de 0,0941 a 0,8753. Relación: respaldo múltiple y consistente, con matización explícita de la limitación muestral.

— polarity: positive · confidence: high · related: [[#C015]], [[#C061]]

### F-V3-010 — «981 candidatas de 8 marketplaces»: el número se sostiene, el origen no consta en el CSV citado

§71.3 (línea 1505) declara: «El tamaño se mide en anuncios (981 candidatas de 8 marketplaces), no en ensayos experimentales». `modelo_muestra.csv` confirma `candidatas = 981` en ambas filas, pero no registra procedencia por marketplace. `NECESIDADES.md` (línea 24) enumera ocho bases —Cogetucarro, iTENCEL, VentaCuba, Autocubana, Timbirichi, Cubisima, Carros.com y Apululu— y añade «además de los 744 de Revolico», mientras el relato generado (PRESENTACION_STORYTELLING.md, línea 91) reporta `anuncios_marketplaces` = 2.232. La cifra 981 y la adscripción a ocho marketplaces no pueden cotejarse con el archivo que el texto invoca como evidencia. Relación: claim parcialmente respaldado, con un componente de procedencia sin evidencia en la tabla citada.

— polarity: negative · confidence: medium · related: [[#C060]]

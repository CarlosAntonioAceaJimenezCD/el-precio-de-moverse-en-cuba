---
type: audit-artifact
phase: v3-results-evidence
slug: corpus-documentacion-2026-11-28
generated_at: 2026-11-28T04:10:00-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md
language: es
---

# V3 — Resultados frente a evidencia

Se contrastan todas las cifras del corpus unificado (833 líneas; bloques `README.md`, `PRESENTACION_STORYTELLING.md`, `MODELOS_Y_FUNCIONES.md`, `ARQUITECTURA_DATOS.md`, `ALCANCE_Y_RETENCION.md`, `AUTOMATIZACION.md`, `ESTRUCTURA_ESPACIO.md` y `Data/mapas/README.md`) con los CSV/TXT vigentes de `Data/analisis_rentabilidad/outputs/tables/` (`kpis.csv`, `kpis_canal.csv`, `modelo_muestra.csv`, `modelo_depreciacion.csv`, `modelo_resumen.txt`, `tests.csv`, `comparaciones.csv`, `vif.csv`, `anomalias.csv`, `infravalorados.csv`, `benchmark.csv`, `baselines.csv`), con `Data/analisis_rentabilidad/data/compacto/MANIFEST.json`, con las bases SQLite que alimentan los marcadores y con `INFORME_TECNICO.md`. Las referencias `L…` son del texto cacheado, que coincide con la numeración de cada archivo de origen; la evidencia externa se cita con `archivo:línea`. Los marcadores `<!-- kpi:… -->` se resuelven en `Auxiliares/herramientas/actualizar_numeros.py:46–118`, de modo que su valor se contrasta con la fuente real y no solo con el texto que lo muestra.

## Resumen

- Doce divergencias numéricas localizadas: dos en recuentos de anuncios/autos, cinco en el bloque del modelo econométrico, una en VIF, una en Kruskal-Wallis, una de vigencia temporal de corrida y una de aritmética de ancho de banda.
- El núcleo de KPI (2.174 / 1.483 / 691 / 21.000 / 28.201,06 / 32.569 / 8,1 / 50 / 114 / 30 / 89) y la serie del ONEI están respaldados sin desajuste por los CSV y por `INFORME_TECNICO.md`.
- La divergencia más extendida es la del modelo: `modelo_muestra.csv` y `modelo_depreciacion.csv` dan 28/993, 586/993, R² 0,274 y p mínimo 0,0941, mientras el corpus conserva 22/572, 584/981, p 0,165 y ocho coeficientes de una corrida anterior.

### F-V3-001 — Los KPI canónicos y la desagregación por canal coinciden con los CSV vigentes

`README.md` (L42) afirma «**Resultado esperado:** 2.174 anuncios limpios (1.483 locales + 691 de importación), mediana local 21.000 USD»; `PRESENTACION_STORYTELLING.md` (L195, L213) añade «media de 28.201,06 USD; la antigüedad promedio es de 8,1 años y el kilometraje mediano, de 32.569 km» y «El canal importado —691 anuncios— corre en paralelo, con una mediana de 26.000 USD»; el Cuadro 1 (L321–331) y el Cuadro 2 (L337–339) repiten once y doce valores respectivamente. `kpis.csv:2-12` contiene `anuncios_totales,2174.0`, `anuncios_locales,1483.0`, `anuncios_importacion,691.0`, `anuncios_usados_locales,1462.0`, `anuncios_nuevos_locales,21.0`, `marcas_distintas,50.0`, `precio_medio_usd,28201.06`, `precio_mediano_usd,21000.0`, `anio_mediano,2020.0`, `km_medianos,32569.0` y `antiguedad_media,8.1`; `kpis_canal.csv:2-4` da fila por fila 691/26.000/27.046,22, 21/24.623,66/24.729,59 y 1.462/21.000/28.201,06. La frase de L197 —«50 marcas», «114 grupos», «30 oportunidades infravaloradas» y «89 anomalías»— se apoya en `benchmark.csv` (114 filas de datos), `infravalorados.csv` (30) y `anomalias.csv` (89), y los marcadores se leen de esos archivos en `actualizar_numeros.py:71-73`. La descomposición aritmética (1.462+21=1.483; 1.483+691=2.174) es cerrada. Relación: respaldo múltiple y coherente.

— polarity: positive · confidence: high · related: [[#C002]], [[#C004]], [[#C005]], [[#C028]], [[#C036]], [[#C037]]

### F-V3-002 — 2.222 frente a 2.232 anuncios de marketplaces: la tabla del README queda diez anuncios atrás

`README.md` (L12) muestra el marcador «2.232 anuncios de 8 marketplaces» y su tabla «Fuentes de datos» (L67) registra «2.222 anuncios»; `PRESENTACION_STORYTELLING.md` (L211) repite «2.232 anuncios en los marketplaces especializados; en la última revisión aparecieron diez anuncios nuevos en iTENCEL». `actualizar_numeros.py:115-118` calcula `anuncios_marketplaces` sumando `select count(*) from anuncios` en los ocho `*.sqlite` de `Data/catalogos_concesionarios/marketplaces/`; la consulta vigente devuelve 2.232 (itencel.sqlite 961, cubisima 155, timbirichi 170, autocubana 667, cogetucarro 200, apululu 33, carroscom 15, ventacuba 31). `INFORME_TECNICO.md:1381` documenta «iTENCEL mostró 10 anuncios nuevos» y `INFORME_TECNICO.md:1391` «La BD pasó de 951 a 961 anuncios». El 2.222 de L67 corresponde al estado anterior a esa inserción y no aparece ya en ninguna fuente vigente; el 2.232 de L12 y L211 sí coincide con las bases y con el informe técnico. Ninguna de las dos cifras tiene un CSV en `outputs/tables/`: el marker no se resuelve desde esa carpeta. Relación: divergencia interna de diez anuncios, con el valor anterior localizado en una tabla estática.

— polarity: negative · confidence: high · related: [[#C001]], [[#C016]], [[#C027]]

### F-V3-003 — La base Revolico se reporta con dos recuentos incompatibles a igual fecha: 10.379/974 frente a 10.217/812

`README.md` (L19) afirma «10.379 anuncios, 974 autos»; `ARQUITECTURA_DATOS.md` (L502) describe la misma base y la misma fecha (23/11/2026) como «849 MB → 27,5 MB (10.217 anuncios, 812 autos, 23.143 imágenes, 11.620 revisiones, 12.338 teléfonos y 716 precios)». La consulta directa a `Data/Revolico/revolico.sqlite` devuelve 10.379 en `anuncios` y 974 en `autos`, y `Data/analisis_rentabilidad/data/compacto/MANIFEST.json:6,19` registra `filas: 10379` y `filas: 974` para esas mismas tablas; el propio `INFORME_TECNICO.md:1345` confirma el tamaño (849.465.344 bytes). Tres de los cuatro recuentos restantes de L502 también divergen del MANIFEST: imágenes 23.143 frente a 23.697 (`MANIFEST.json:58`), revisiones 11.620 frente a 14.487 (`:32`), teléfonos 12.338 frente a 12.538 (`:71`); solo precios coincide (716, `:45`). El 974, en cambio, es estable en el corpus (L12, L69, L123, L195, L211) y coincide con la BD. Relación: cifras de una exportación anterior conservadas en prosa junto a un MANIFEST ya regenerado.

— polarity: negative · confidence: high · related: [[#C011]], [[#C014]]

### F-V3-004 — Cuadro 5 y la prosa de MODELOS conservan ocho coeficientes y ocho p_valores de una corrida previa

`PRESENTACION_STORYTELLING.md` rotula el Cuadro 5 (L364) como «coeficientes vigentes» y enumera (L368–375): Intercepto 12,4469 (p 0,000), Económico −1,1228 (0,328), Medio −1,2332 (0,239), Premium 0,0662 (0,947), Antigüedad −0,0708 (0,237), log(km) −0,0226 (0,740), Potencia −0,0046 (0,165) y Condición −0,0340 (0,802). `MODELOS_Y_FUNCIONES.md` (L450) refuerza «el p_valor más bajo es 0,165, de potencia; antigüedad tiene p = 0,237». `modelo_depreciacion.csv:2-9` regresa, en el mismo orden, 12.0884/0.0, −1.0208/0.1421, −0.978/0.0941, 0.1146/0.8753, −0.0632/0.1504, −0.0333/0.4711, −0.0036/0.1403 y −0.0254/0.8168, con coincidencia con `modelo_resumen.txt`. Los ocho coeficientes y los ocho p_valores difieren; el p mínimo nointercepto vigente es 0,0941 (`modelo_depreciacion.csv:4`), no 0,165, y es el que `INFORME_TECNICO.md:1409` publica mediante el marcador `modelo_p_min` (`actualizar_numeros.py:88-91`). La conclusión cualitativa de L377 —«Ningún coeficiente resulta estadísticamente significativo con la base actual»— sigue siendo válida con el CSV, pero la tabla rotulada como vigente no reproduce sus números. Relación: desajuste entre la evidencia citada y la tabla que dice alimentarla.

— polarity: negative · confidence: high · related: [[#C006]], [[#C007]], [[#C030]], [[#C039]], [[#F-V3-005]]

### F-V3-005 — Tres recuentos de muestra para un mismo modelo: 28/993 en el CSV, 22/572 en el Cuadro 5 y 584/981 en el informe técnico

`MODELOS_Y_FUNCIONES.md` (L450) enuncia «28 observaciones completas de 993 candidatas» y acto seguido «La muestra se reduce a 22 porque `hp` solo está presente en 52 filas y `mileage_km` en 572; al exigir todos los términos a la vez se descarta el 97,5 % de las candidatas (R² = 0,274; p del F = 0,411)»; (L452) da después «586 observaciones de 993 candidatas (R² = 0,101; p del F 0,000) y el completo usa 28 (R² = 0,274; p del F = 0,411)». `modelo_muestra.csv:2-3` contiene exactamente `principal,993,586,0.1008,0.0` y `completo,993,28,0.2744,0.4114`. El Cuadro 5 (L377) afirma «las 22 observaciones de este modelo frente a las 572 del modelo principal», cifras ausentes del CSV citado en la misma frase. `INFORME_TECNICO.md:1516` registra «R² 0,101 sobre 584 observaciones» y `:1522` «la muestra pasa de 28 a 584 observaciones de 981 candidatas», mientras `:1528` habla de «981 candidatas» y `:1401` de 993/28; `INFORME_TECNICO.md:1489` documenta además que un R² citado como 0,277 se corrigió a 0,274, valor que el corpus ya usa. La regla declarada en L441 («el modelo exige más de 30 filas») queda por debajo de las 28 observaciones del propio CSV. Relación: una misma cantidad reportada con 22, 28, 572, 584 y 586 observaciones, y con 981 y 993 candidatas.

— polarity: negative · confidence: high · related: [[#C007]], [[#C008]], [[#C040]], [[#C046]], [[#F-V3-004]]

### F-V3-006 — Rango de VIF declarado 1,13–1,58 frente a 1,12–1,40 en vif.csv

`MODELOS_Y_FUNCIONES.md` (L458) sostiene «Valores cercanos a 1 (los actuales van de 1,13 a 1,58) indican que los regresores no se explican entre sí». `vif.csv:2-6` contiene cinco valores —car_age 1.38, mileage_km 1.4, price_usd 1.16, hp 1.12, condition_score 1.14—, cuyo mínimo es 1,12 y su máximo 1,40; `INFORME_TECNICO.md:1409` publica «VIF 1,12–1,40» a través de `actualizar_numeros.py:92-95`. Ninguno de los dos extremos del corpus coincide con el archivo que invoca como respaldo, y el CSV incluye `price_usd`, variable ausente de la fórmula citada en L438. Relación: desajuste numérico entre el texto metodológico y su tabla.

— polarity: negative · confidence: high · related: [[#C047]], [[#F-V3-004]]

### F-V3-007 — Kruskal-Wallis: tres estadísticos para el mismo contraste (25,741 / 32,818 / 44,313)

`MODELOS_Y_FUNCIONES.md` (L462) afirma «Resultado vigente: H = 25,741, p = 1e−05». `tests.csv:2` registra `Kruskal-Wallis precio por tier,32.818,0.0`; `comparaciones.csv:2` registra `precio por tier de marca,1462,44.313,0.0,10000.0,29500.0,…`; e `INFORME_TECNICO.md:1528` cuantifica «H = 44,313». El p del corpus (1e−05) tampoco coincide con el `p_valor=0.0` de ambas tablas, que `actualizar_numeros.py:96-100` despliega como «0,00000» en `INFORME_TECNICO.md:1409`. La conclusión cualitativa de L464 —«los tiers no provienen de la misma distribución de precios»— se mantiene con cualquiera de los tres estadísticos, pero el número atribuido al test no se deriva de la tabla citada ni del informe técnico. Relación: inconsistencia numérica entre evidencias de un mismo contraste.

— polarity: negative · confidence: high · related: [[#C048]], [[#C005]]

### F-V3-008 — «104 observaciones en 2 años bastan para depreciación» frente al límite de serie mensual declarado

`AUTOMATIZACION.md` (L645) afirma en su tabla de periodicidad «Snapshots de precio (`price_history`) | Semanal, tras Revolico | 104 observaciones en 2 años bastan para depreciación», y (L690) repite «104 semanas ≈ 2 años». `MODELOS_Y_FUNCIONES.md` (L485) establece como límite explícito «No se presenta una curva de depreciación temporal: hace falta una serie mensual de 6–12 meses»; `PRESENTACION_STORYTELLING.md` (L290) sitúa la «serie de precios de 6–12 meses» en «Lo que viene» e `INFORME_TECNICO.md:1401` registra que el modelo actual «no encuentra una pendiente anual significativa tras corregir el kilometraje». La cifra 104 se presenta como suficiencia en un documento y como trabajo futuro en los otros dos; no hay en `outputs/tables/` ninguna estimación de depreciación temporal que la sostenga (`modelo_depreciacion.csv` es un corte transversal de 28 filas). Relación: sobreafirmación de un resultado frente al límite metodológico citado.

— polarity: negative · confidence: high · related: [[#C003]], [[#C010]], [[#C051]], [[#C064]]

### F-V3-009 — La corrida de calidad de 2.014 filas se describe como corrida real junto a un KPI vigente de 2.174

`AUTOMATIZACION.md` (L706) registra «`validar_calidad.py`: 6 reglas, cuarentena en `Data/_cuarentena/`, umbral 10 %. Corrida real: 2.014 filas, 0 inválidos», dentro de un apartado rotulado «Ya hecho (23/11/2026)». `INFORME_TECNICO.md:1391` sitúa ese 2.014 en la corrida del 23/11/2026 («2.014 anuncios limpios, de ellos 1.323 locales y 691 de importación»), anterior a la regeneración que `INFORME_TECNICO.md:1399` describe con 2.174/1.483/691. `kpis.csv:2-4` y el propio corpus (README L42, storytelling L123 y L195) usan ya 2.174. El corpus no marca el 2.014 como corrida histórica, de modo que dos recuentos de la misma magnitud conviven sin jerarquía temporal explícita. Relación: desajuste de vigencia entre una medición citada como real y el KPI actual.

— polarity: negative · confidence: high · related: [[#C065]], [[#C002]]

### F-V3-010 — Cuadro 3, Cuadro 4 y la referencia egipcia: respaldo convergente en el informe técnico

`PRESENTACION_STORYTELLING.md` (L145) afirma «en 2025 se transportaron 781 millones de pasajeros, un 59 % menos que en 2019. En ómnibus fueron 324 millones, un 71 % menos»; el Cuadro 3 (L346, L352) da 1.899,9 → 781,1 y 1.102,2 → 324,0, y el Cuadro 4 (L362) da 7.552 accidentes y 751 fallecidos en 2025. `INFORME_TECNICO.md:1371` confirma «los 12 anuarios del ONEI y sus 233 archivos», la caída del 59 % y del 71 % y «9,9 fallecidos por cada 100 accidentes en 2025»; 751/7.552 = 9,94 por 100, coherente con esa razón. La cifra de 23.500 anuncios de `Egyptian-Used-Cars` (L277) aparece también en `INFORME_TECNICO.md:1080` y `:1518`. Los porcentajes del texto son redondeos correctos de las cifras del cuadro y del informe. Relación: respaldo externo e interno consistente.

— polarity: positive · confidence: high · related: [[#C022]], [[#C035]], [[#C038]]

### F-V3-011 — Cifras de cobertura y de espacio sin contrapartida en `outputs/tables/` ni en el informe técnico

Varios enunciados numéricos del corpus no tienen fila en los CSV vigentes ni registro en `INFORME_TECNICO.md`: «3.958 anuncios ICD» (`README.md`, L70); «256 vehículos» de 11 concesionarios (`README.md`, L12 y L68) frente a «25 concesionarios» y «22 talleres» geolocalizados (`PRESENTACION_STORYTELLING.md`, L187); la encuesta «28 personas», «14», «16 de 18», «4.000 USD», «10.000 USD», «28 y 25 de 30 entrevistas» (L251); «11 estaciones solares» y «21 estaciones de CIMEX+MITRANS» (L265); «205.002 KB ≈ 0,20 GB», «3,3 GB (174 archivos)» y los quince subtotales del mapa de carpetas (`ESTRUCTURA_ESPACIO.md`, L741–764), de los que el informe solo documenta «pasó de 20 GB a 10 GB» (`INFORME_TECNICO.md:1471`). El panel de «107 KB» (`AUTOMATIZACION.md`, L659) sí es consistente con los 109.929 bytes que el inventario E3 midió para `Data/dashboard.html`. La cifra «233 archivos» de `README.md:21`, en cambio, coincide literalmente con `INFORME_TECNICO.md:1371`. Relación: ausencia de evidencia verificable en las fuentes de contraste, sin que ello establezca la falsedad de las cifras.

— polarity: negative · confidence: medium · related: [[#C017]], [[#C018]], [[#C026]], [[#C033]], [[#C034]], [[#C060]], [[#C068]], [[#C069]]

### F-V3-012 — El total de ancho de banda «sin cambios» no surge de la suma de las filas de su propia tabla

`AUTOMATIZACION.md` (L721–724) tabula «Circuitos (2 páginas) | Diario | ~2–5 KB/día», «Marketplaces (8 sitios, 2 páginas) | Semanal | ~20–50 KB/semana», «Revolico incremental | Semanal | ~0,5 MB/semana» y cierra con «**Total estimado** | — | **~5–10 MB/mes** | **~50–90 MB/mes**». La conversión de las tres filas al escenario sin cambios da ~0,06–0,15 MB/mes, ~0,09–0,22 MB/mes y ~2,15 MB/mes, es decir ~2,3–2,5 MB/mes, por debajo del total declarado; con cambios las filas suman ~56–100 MB/mes, del orden del intervalo publicado. El párrafo de L726 califica explícitamente el cuadro como «estimaciones de diseño, no mediciones de facturación», y no hay serie de facturación en `outputs/tables/` ni en el informe técnico que permita dirimir el total. Relación: divergencia aritmética interna en una tabla presentada como estimación.

— polarity: negative · confidence: medium · related: [[#C066]]

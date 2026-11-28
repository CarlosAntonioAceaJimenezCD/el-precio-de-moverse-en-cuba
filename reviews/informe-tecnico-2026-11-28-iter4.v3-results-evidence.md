---
type: audit-artifact
phase: v3-results-evidence
slug: informe-tecnico-2026-11-28-iter4
generated_at: 2026-11-28T03:14:23-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-28-iter4/informe-tecnico-2026-11-28-iter4.text.md
language: es
---

# V3 — Resultados frente a evidencia

Se contrastan los enunciados de resultado de la caché auditada (Resumen/Abstract, §59, §60, §71.1–§71.5) con los CSV vigentes en `Data/analisis_rentabilidad/outputs/tables/` —`kpis.csv`, `kpis_canal.csv`, `modelo_muestra.csv`, `modelo_depreciacion.csv`, `comparaciones.csv`, `baselines.csv`, `vif.csv`, `tests.csv`, `benchmark.csv`, `anomalias.csv`—, con el generador `Auxiliares/herramientas/actualizar_numeros.py` y con los artefactos citados `docs/historia/apendice.md` y `MODELOS_Y_FUNCIONES.md`. Los marcadores `<!-- kpi:... -->` se resuelven desde varias fuentes, no desde un único CSV. La caché no contiene marcadores `Tabla N` / `Figura N`; las tablas se citan por sección y líneas.

### F-V3-001 — H1 se enuncia «controlando por antigüedad y kilometraje», pero el contraste citado es univariate

El Resumen (L21) declara: «**Hipótesis falsable (H1):** «los precios de los tres tiers de marca en el mercado local provienen de la misma distribución, controlando por antigüedad y kilometraje». Se contrasta con Kruskal-Wallis; se rechaza con p < 0,001 en la corrida vigente»; el Abstract (L163) repite «rejected at p < 0.001 in the current run». La evidencia invocada en §71.3 (L1528) es `comparaciones.csv`, cuya única fila es `precio por tier de marca,1462,44.313,0.0,10000.0,29500.0,Kruskal-Wallis + bootstrap de mediana premium-economico (2000 replicas)`: un contraste de precio por tier sin covariables. El modelo que sí incluye antigüedad y kilometraje, `modelo_depreciacion.csv`, reporta coeficientes de tier con p = 0,1421 (`economico`), 0,0941 (`medio`) y 0,8753 (`premium`), ninguno inferior a 0,05; §60 (L1409) describe esa corrida como la que «no sostiene una tasa de depreciación ni una prima premium significativa». El rechazo con p < 0,001 está respaldado como prueba marginal, pero la cláusula «controlando por antigüedad y kilometraje» no se deriva del contraste citado ni del modelo con covariables. Relación: sobreafirmación del alcance del test.

— polarity: negative · confidence: high · related: [[#C001]], [[#C005]], [[#C085]]

### F-V3-002 — Las nueve cifras canónicas de §59 coinciden con los CSV y la base vigentes

§59 (L1399) enuncia «**<!-- kpi:autos_revolico -->974 autos únicos**, **<!-- kpi:anuncios_totales -->2.174 anuncios limpios** (<!-- kpi:anuncios_locales -->1.483 locales y <!-- kpi:anuncios_importacion -->691 de importación), mediana local de **<!-- kpi:precio_mediano_usd -->21.000 USD**, kilometraje mediano de **<!-- kpi:km_medianos -->32.569 km**, <!-- kpi:marcas_distintas -->50 marcas, <!-- kpi:grupos_benchmark -->114 grupos comparables y <!-- kpi:anomalias -->89 anomalías (corrida vigente del 27/11/2026)». `kpis.csv` contiene `anuncios_totales,2174.0`, `anuncios_locales,1483.0`, `anuncios_importacion,691.0`, `anuncios_usados_locales,1462.0`, `anuncios_nuevos_locales,21.0`, `precio_mediano_usd,21000.0`, `km_medianos,32569.0` y `marcas_distintas,50.0`; `kpis_canal.csv` da `local,usado,1462,21000.0` para la mediana local; `benchmark.csv` tiene 114 filas de datos y `anomalias.csv` 89; `SELECT count(*) FROM autos` sobre `Data/Revolico/revolico.sqlite` devuelve 974. Las nueve cifras y su descomposición interna (1.462 + 21 = 1.483; 1.483 + 691 = 2.174) están respaldadas sin desajuste. Relación: respaldo múltiple y coherente.

— polarity: positive · confidence: high · related: [[#C002]], [[#C015]]

### F-V3-003 — «Los valores se actualizan solos en kpis.csv» atribuye a ese archivo marcadores que se leen de otras fuentes

La misma frase de §59 (L1399) cierra con «los valores se actualizan solos en `outputs/tables/kpis.csv`», y §71.1 (L1515) remite «las 981 candidatas y las 8 fuentes» a `config.py`, `01_ingest.py` y `kpis_canal.csv`. `kpis.csv` contiene once métricas, entre ellas las seis primeras de §59, pero no `autos_revolico`, `grupos_benchmark` ni `anomalias`. `actualizar_numeros.py` obtiene esos valores de fuentes distintas: `benchmark.csv` (L71), `anomalias.csv` (L72), `modelo_muestra.csv` (L75–86), `modelo_depreciacion.csv` (L88–91), `vif.csv` (L92–95), `tests.csv` (L96–100), `comparaciones.csv` (L101–103), `baselines.csv` (L104–107) y la tabla `autos` de `revolico.sqlite` (L109–110). De los diecisiete marcadores desplegados en §59–§71.3, seis provienen de `kpis.csv`. Relación: desajuste entre la descripción del mecanismo de actualización y el origen real de los datos, sin que ello invalide las cifras comparadas en F-V3-002.

— polarity: negative · confidence: high · related: [[#C002]], [[#C084]]

### F-V3-004 — MAE 18.188,34 y 16.603,28 USD sobre 1.462 anuncios: respaldo exacto en baselines.csv

La tabla sin numerar de §71.1 (L1511–L1512) registra «| Mediana global ( ingenua ) | Predice la mediana de los usados locales | MAE <!-- kpi:mae_mediana_global -->18.188,34 USD sobre <!-- kpi:n_mediana_global -->1.462 anuncios |» y «| Mediana por marca | Predice la mediana de cada marca | MAE <!-- kpi:mae_mediana_por_marca -->16.603,28 USD sobre <!-- kpi:n_mediana_por_marca -->1.462 anuncios |». `baselines.csv` contiene exactamente `mediana_global,1462,18188.34,mediana fija 21000 USD` y `mediana_por_marca,1462,16603.28,50 marcas`, y `kpis.csv` confirma `anuncios_usados_locales,1462.0`. Los cuatro números, el denominador y la nota de 50 marcas coinciden con los archivos que el propio párrafo designa como fuente. Relación: respaldo directo y sin sobreafirmación.

— polarity: positive · confidence: high · related: [[#C084]]

### F-V3-005 — La fila «Modelo principal propio» de §71.1 no tiene fila en baselines.csv y su n=584 no consta en los CSV

Tras el párrafo que afirma «los MAE se calculan en `scripts/03b_baselines.py` y se publican en `outputs/tables/baselines.csv`» (L1515), §71.1 añade una fila separada (L1516): «| Modelo principal propio | OLS de log-precio con antigüedad, km, condición y tier | R² 0,101 sobre 584 observaciones |». `baselines.csv` solo contiene las dos filas de medianas comparadas en F-V3-004; no registra modelo propio, R² ni observaciones. El R² 0,101 es el redondeo de `r2=0.1008` de la fila `principal` de `modelo_muestra.csv`, pero esa fila declara `observaciones=586`, no 584. En la propia caché, §71.2 (L1522) repite 584 y §59 (L1401) usa 993 candidatas con 28 observaciones completas. Relación: claim compuesto con un componente respaldado en otro CSV y un componente numérico sin respaldo en la tabla citada.

— polarity: negative · confidence: high · related: [[#C084]], [[#C004]], [[#F-V3-008]]

### F-V3-006 — p mínimo 0,0941, VIF 1,12–1,40 y no significancia de la edad: respaldo convergente

§60 (L1409) sostiene que la corrida «no sostiene una tasa de depreciación ni una prima premium significativa (p mínimo <!-- kpi:modelo_p_min -->0,0941; VIF <!-- kpi:vif_min -->1,12–<!-- kpi:vif_max -->1,40; Kruskal-Wallis p = <!-- kpi:kw_p -->0,00000)»; §71.4 (L1537) añade «el modelo completo usa 28 observaciones y ningún coeficiente alcanza p < 0,05». `modelo_depreciacion.csv` confirma que el menor p_valor no intercepto es 0,0941 (`C(brand_tier)[T.medio]`) y que los ocho términos no intercepto van de 0,0941 a 0,8753; `car_age` tiene p = 0,1504 y `np.log1p(mileage_km)` p = 0,4711, coherentes con la frase de §59 (L1401) sobre la ausencia de pendiente anual significativa tras corregir el kilometraje. `vif.csv` registra cinco valores cuyo mínimo es 1,12 (`hp`) y máximo 1,40 (`mileage_km`). Tres tablas y dos secciones coinciden; la precisión de «0,00000» se trata aparte en F-V3-007. Relación: respaldo múltiple con matización explícita de la limitación muestral.

— polarity: positive · confidence: high · related: [[#C003]], [[#C077]], [[#C086]]

### F-V3-007 — Estadístico H divergente: 44,313 en §71.3 y comparaciones.csv frente a 32,818 en tests.csv

§71.3 (L1528) cuantifica «El contraste central se cuantifica con H = 44,313». `comparaciones.csv` coincide con `estadistico=44.313`, pero `tests.csv` contiene una sola fila, `Kruskal-Wallis precio por tier,32.818,0.0`, es decir un estadístico 32,818 para el mismo contraste «precio por tier». Ambos archivos guardan `p_valor=0.0`, y §60 (L1409) muestra «Kruskal-Wallis p = <!-- kpi:kw_p -->0,00000», valor que `actualizar_numeros.py` (L96–100) toma de `tests.csv` con cinco decimales; el texto toma H de `comparaciones.csv` y p de `tests.csv`, dos fuentes que no coinciden en el estadístico y que no registran precisión de cinco decimales para el p. Relación: inconsistencia numérica entre la evidencia citada para un mismo test.

— polarity: negative · confidence: high · related: [[#C001]], [[#C005]], [[#C077]]

### F-V3-008 — Ablación de `hp`: R² y n=28 coinciden, pero 584 candidatas y observaciones no

§71.2 (L1522) afirma: «`modelo_muestra.csv` documenta la ablación del término `hp`: al retirarlo, la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² baja de 0,274 a 0,101». `modelo_muestra.csv` contiene dos filas: `completo,993,28,0.2744,0.4114` y `principal,993,586,0.1008,0.0`. Coinciden 28, 993, 0,2744 (→ 0,274), 0,1008 (→ 0,101) y 0,4114 (→ 0,411, citado en §59 L1401). No coinciden 584 frente a 586 ni 981 frente a 993. §59 (L1401) emplea 993, mientras §71.1 (L1516) y §71.2 (L1522) emplean 584 y §71.3 (L1528) emplea 981: una misma cantidad se reporta con tres valores distintos dentro del documento y un cuarto en el CSV. Relación: desajuste parcial entre el texto y la tabla que lo invoca como evidencia.

— polarity: negative · confidence: high · related: [[#C004]], [[#C084]], [[#F-V3-005]]

### F-V3-009 — «981 candidatas de 8 marketplaces» no consta en kpis_canal.csv ni en los CSV vigentes

§71.3 (L1528) declara «El tamaño se mide en anuncios (981 candidatas de 8 marketplaces), no en ensayos experimentales» y §71.1 (L1515) remite «las 981 candidatas y las 8 fuentes» a `config.py`, `01_ingest.py` y `outputs/tables/kpis_canal.csv`. `kpis_canal.csv` tiene las columnas `canal,source_type,anuncios,mediana_usd,media_usd` y tres filas (691, 21 y 1.462 anuncios; total 2.174), sin campo `candidatas` ni desglose por ocho fuentes. En los CSV vigentes, `candidatas` vale 993 en `modelo_muestra.csv` y `n` vale 1.462 en `comparaciones.csv` y `baselines.csv`; 981 no aparece en ninguno de ellos ni en los scripts de `Data/analisis_rentabilidad/scripts/`. Relación: claim parcialmente respaldado en su forma («se mide en anuncios») pero sin evidencia en el archivo citado para la cifra y su procedencia.

— polarity: negative · confidence: high · related: [[#C085]], [[#C084]], [[#C004]]

### F-V3-010 — Intervalo bootstrap 10.000–29.500 USD y 2.000 réplicas: respaldo literal en comparaciones.csv

§71.3 (L1528) describe «un intervalo bootstrap de la diferencia de medianas premium−económico de <!-- kpi:ci_bajo -->10.000 a <!-- kpi:ci_alto -->29.500 USD (`comparaciones.csv`, 2.000 réplicas)». La fila de `comparaciones.csv` registra `ic_bajo=10000.0`, `ic_alto=29500.0` y `metodo=Kruskal-Wallis + bootstrap de mediana premium-economico (2000 replicas)`. Los extremos, la magnitud comparada y el número de réplicas coinciden literalmente con la tabla citada; es el único intervalo numérico del documento y las bases de §71.1 no llevan IC asociado, como señala la propia C005. Relación: respaldo directo.

— polarity: positive · confidence: high · related: [[#C005]]

### F-V3-011 — Cuadro 5 y MODELOS_Y_FUNCIONES.md conservan coeficientes y muestras de una corrida previa

§59 (L1401) remite el límite del modelo completo a «`MODELOS_Y_FUNCIONES.md`» y anuncia «un apéndice visual con cinco cuadros y seis gráficos reales»; §61 (L1419) afirma que «las tablas del apéndice y la página de KPIs se generan desde los CSV». Sin embargo, `docs/historia/apendice.md` (L64–L77) rotula «Cuadro 5. Modelo de depreciación (coeficientes vigentes)» con Intercepto 12,4469, Económico −1,1228 (p 0,328), Medio −1,2332 (0,239), Premium 0,0662 (0,947), Antigüedad −0,0708 (0,237), log(km) −0,0226 (0,740), Potencia −0,0046 (0,165) y Condición −0,0340 (0,802), y cierra «las 22 observaciones de este modelo frente a las 572 del modelo principal». `modelo_depreciacion.csv` regresa coeficientes distintos (Intercept 12.0884, economico −1.0208, medio −0.978, premium 0.1146, car_age −0.0632, mileage −0.0333, hp −0.0036, condition −0.0254; p mínimo 0,0941) y `modelo_muestra.csv` registra 28 y 586. `MODELOS_Y_FUNCIONES.md` (L54) mantiene en prosa «el p_valor más bajo es 0,165, de potencia; antigüedad tiene p = 0,237. La muestra se reduce a 22», aunque sus marcadores ya muestran 993/28/586. Relación: contradicción entre la tabla y el documento metodológico citados como respaldo y los CSV que el texto dice alimentarlos.

— polarity: negative · confidence: high · related: [[#C077]], [[#C015]], [[#F-V3-006]], [[#F-V3-008]]

### F-V3-012 — «13 artefactos» frente a los 15 archivos por pasada presentes en reviews/

El Resumen (L19) y el Abstract (L161) incluyen entre las contribuciones «un expediente de auditoría con 13 artefactos» y §69 (L1489) precisa «El registro de la tercera pasada está en `reviews/informe-tecnico-2026-11-27-iter3.{md,forensic.md}` y sus 13 artefactos». El inventario E3 contabiliza 3 pasadas × 15 archivos = 45 artefactos, y el directorio contiene 15 archivos con el prefijo `informe-tecnico-2026-11-27-iter3` (e1–e3, forensic, md, plan y v1–v9). El número 13 coincide con el subconjunto e1–e3 + forensic + v1–v9, que excluye el relato `.md` y el `.plan.md`, convención que el texto no declara. Relación: cifra verificable solo bajo una regla de conteo implícita.

— polarity: negative · confidence: low · related: [[#C015]], [[#C124]]

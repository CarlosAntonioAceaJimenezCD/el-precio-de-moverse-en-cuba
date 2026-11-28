---
type: audit-forensic
slug: informe-tecnico-2026-11-27-iter3
generated_at: 2026-11-28T09:00:00-05:00
audited_document: INFORME_TECNICO.md
audited_document_title: Informe técnico / Technical report — El precio de moverse en Cuba
language: es
level: master
preset: Standard
phases_executed: [0, 1, 2, 3]
dimensions_run: [V1, V2, V3, V4, V5, V6, V7, V8, V9]
dimensions_skipped: []
phase1_failures: []
phase2_failures: []
phase_artifacts:
  plan: informe-tecnico-2026-11-27-iter3.plan.md
  e1: informe-tecnico-2026-11-27-iter3.e1-claims.md
  e2: informe-tecnico-2026-11-27-iter3.e2-literature.md
  e3: informe-tecnico-2026-11-27-iter3.e3-artifacts.md
  v1: informe-tecnico-2026-11-27-iter3.v1-structure.md
  v2: informe-tecnico-2026-11-27-iter3.v2-methodology.md
  v3: informe-tecnico-2026-11-27-iter3.v3-results-evidence.md
  v4: informe-tecnico-2026-11-27-iter3.v4-novelty.md
  v5: informe-tecnico-2026-11-27-iter3.v5-state-of-the-art.md
  v6: informe-tecnico-2026-11-27-iter3.v6-reproducibility.md
  v7: informe-tecnico-2026-11-27-iter3.v7-writing.md
  v8: informe-tecnico-2026-11-27-iter3.v8-bibliography.md
  v9: informe-tecnico-2026-11-27-iter3.v9-ethics.md
  forensic: informe-tecnico-2026-11-27-iter3.forensic.md
previous_iterations: [reviews/informe-tecnico-2026-11-27.md, reviews/informe-tecnico-2026-11-27-iter2.md]
---
# Auditoría forense — Iteración 3

## §0 — Resumen del documento

El documento auditado es el *Informe técnico / Technical report — El precio de moverse en Cuba*, firmado por «responsable del proyecto / project owner» sin nombre propio, fechado el 23/11/2026 con «Última actualización / Last update: 27/11/2026». La copia cacheada tiene 1.523 líneas bilingües (Parte I en español, Parte II en inglés), sin paginación, con 96 encabezados y una cabecera de seis campos. El encabezado fija el estado en «Fase 6 — scraping y captura de catálogos y anuncios, en curso», mientras la nota de actualización de §2 remite los resultados vigentes de la fase 8 a §59–§60. El alcance declarado en §1 es «un análisis del mercado automotor cubano: caracterizar estructura, precios, oferta, segmentos, tendencias, asequibilidad y condiciones de rentabilidad», apoyado en dos pilares —la base de datos del mercado cubano y un pipeline de scraping reutilizable—, con el producto interactivo diferido a una especialización posterior.

El inventario E1 registra 126 afirmaciones, 16 de ellas load-bearing. Las que sostienen el relato son: el objetivo y la cobertura de dos partes (C001–C002), las cifras de §59 (C003), la retirada de la depreciación anual y la no significancia de los coeficientes (C004), la ablación del término `hp` (C005), la adopción adaptada de la arquitectura `Egyptian-Used-Cars` (C011) y su contraste por escala (C012), el benchmark de comparables (C014) y el diferenciador de procedencia y normalización enunciado en §71.6 (C016). Diez de las dieciséis afirmaciones portantes conservan «External evidence cited: — (sin citas numeradas)»; cinco remiten a fuentes institucionales o de ingeniería y una nombra a los cuatro pares académicos del mapa.

Los artefactos del repositorio `CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba` incluyen `Data/analisis_rentabilidad/` con cinco etapas y punto de entrada único, ocho tablas CSV en `outputs/tables/`, semilla `SEED = 20261127`, doce dependencias fijadas a serie menor, prueba de humo de cuatro comprobaciones, panel `Data/dashboard.html`, apéndice visual y un aparato de 38 referencias numeradas en `Data/referencias.md`. El texto cacheado no incorpora los cinco cuadros ni los seis gráficos del apéndice, no imprime la ruta del panel y no contiene marcadores `[N]` en sus 1.523 líneas. Las cifras canónicas de §59 y §60 se cotejan contra `kpis.csv`, `modelo_muestra.csv`, `modelo_depreciacion.csv`, `vif.csv`, `tests.csv`, `anomalias.csv` y `benchmark.csv` a través del generador `Auxiliares/herramientas/actualizar_numeros.py`.

La auditoría ejecutó E1–E3 y las nueve dimensiones V1–V9 bajo preset `Standard`, nivel `master` e idioma `es`, sobre las dos versiones del documento. No se registra fallo de subagentes en el material ensamblado; V9 consigna que no recibió `v7_ai_density_hint` y emitió sus hallazgos sin contraste cruzado, mientras V7 entregó su tabla de densidad por secciones con el contraste iteración 1 → 2 → 3. La síntesis de §10 reúne los patrones que aparecen solo al leer dos o más dimensiones juntas y, a pedido del plan, la lista de lo que permanece por debajo del criterio master.

Respecto de la iteración 2, el corpus pasó de 29.106 a 29.870 palabras (+764): §69 creció de 179 a 271 y se incorporó la sección §71 (606 palabras), con cinco apartados de estándares master y un párrafo de posicionamiento. En §69 desaparecieron los tres adjetivos sin ancla —«quirúrgica», «asistida», «sistemática»— y se nombraron herramientas, skills, cuatro fases y tres pasos de supervisión. Se cerraron la divergencia de §12 entre las dos partes y el flag de cuatro fichas bibliográficas, actualizado en disco después de E2. La numeración 1–12, las cifras de §59 y la coexistencia de dos especificaciones de modelo permanecen en el estado de la pasada anterior.

## §1 — v1-structure


# V1 — Structure (findings)

### F-V1-001 — Persiste la ausencia de resumen VSN-C, hipótesis falsable y sección de contribuciones

El encabezado mantiene los seis campos de las iteraciones anteriores —«**Proyecto / Project:**», «**Autor / Author:**», «**Fecha / Date:**», «**Ubicación / Location:**», «**Estado / Status:**», «**Idioma / Language:**» (L3–8)— con la autoría y la firma consignadas por rol («responsable del proyecto / project owner», L4 y L1522) y «**Última actualización / Last update:** 27/11/2026» (L1523). Entre los 96 encabezados del texto (L1–L1523) no figura «Resumen» ni «Abstract», y tampoco dedicatoria, agradecimientos ni dictamen de tutor. §69 (L1467–1471) y §70 (L1475–1479) aportan declaración de uso de IA y aparato de referencias verificadas, sin función de resumen.

El material más cercano a un resumen sigue distribuido entre §1 ES (L16–18) y §1 EN (L147–149): allí aparecen Vision —«caracterizar estructura, precios, oferta, segmentos, tendencias, asequibilidad y condiciones de rentabilidad»— y Steps —«dos pilares: la base de datos del mercado cubano y un pipeline de scraping reutilizable»—, pero no hay elemento de novedad ni cifras en la apertura. Las cinco conclusiones de §12 (L135–139 y L266–270) enumera hallazgos sin encabezado de «Contribuciones», y la única formulación explícita queda dentro de un párrafo de posicionamiento en §71.6: «la contribución es de procedencia y normalización, no de algoritmo» (L1520). No aparece la cadena «hipótesis» ni «hypothesis» en ningún punto del texto: §34 reporta «una depreciación media de **−5,43 % anual** (p<0,001)» (L1056) sin proposición previa sometida a contraste, y §59–§60 retiran esa pendiente (L1381, L1389). §70 anuncia «La convención numerada de 38 referencias» (L1477–1479), pero el cuerpo no contiene citas numeradas `[N]`; la contribución y el aparato bibliográfico quedan, por tanto, fuera de una sección de contribuciones.

— polarity: negative · confidence: high · related: [[#C001]], [[#C008]], [[#C009]], [[#C011]], [[#C016]]

### F-V1-002 — Objetivo alineado en ambas partes y contrastado en §19–§71; la fila de la fase 8 sigue divergiendo

La divergencia de introducciones de la iteración 2 queda cerrada: §1 ES (L16) y §1 EN (L147) enuncian el mismo objetivo —«un análisis del mercado automotor cubano» / «to analyse the Cuban automotive market»— con el producto interactivo diferido, y §12 ES (L139) y §12 EN (L270) coinciden ahora en que «El análisis de mercado y el modelo de rentabilidad (fase 8) están implementados… y se regeneran de forma automática» / «are implemented under `Data/analisis_rentabilidad/` and regenerate automatically». El objetivo se corresponde con secciones ejecutadas: el marco de ocho pasos (§19, L837–846), los nueve bloques (§20, L861–871), el pipeline de rentabilidad (§34, L1016–1062), los resultados vigentes (§59–§60, L1377–1391) y los estándares de §71 (L1485–1520).

Subsiste una divergencia acotada: la fila 8 de la tabla de fases dice «Análisis de mercado, comparables y rentabilidad» en español (L33) pero «Analysis, profitability model and interactive product» en inglés (L164), denominación que §21 retiró al disponer «La fase 8 pasa a llamarse **Análisis de mercado, comparables y rentabilidad**» (L883). Las notas de actualización de §2 (L38, L169) remiten el estado vigente a «§59–§60», y esos dos destinos existen y contienen las cifras y la justificación del modelo actual.

— polarity: neutral · confidence: high · related: [[#C001]], [[#C002]], [[#C032]], [[#C059]]

### F-V1-003 — Numeración 1–12 duplicada, salto de nivel en §13 y referencias cruzadas sin marcadores rotos

La numeración se reinicia igual que en iteraciones previas: dos secciones «1.» (L14, L145), dos «12. Conclusiones» (L133, L264) y una secuencia única desde §13 (L274) hasta §71 (L1485), de modo que «§1»–«§12» designan dos destinos posibles según la parte. El bloque §13 «Registro de altas / Change log» (L274–752) emplea encabezado de nivel 1 mientras §14–§71 usan nivel 2 (L754, L1016, L1485), y queda fuera de «# Parte I — Español» (L12) y «# Part II — English» (L143) pese a continuar su numeración. De las 58 secciones §14–§71, 53 llevan fecha en el título; §14, §15, §69, §70 y §71 no la llevan, y §69 aparece precedido de dos reglas horizontales consecutivas (L1481, L1483).

En integridad de referencias cruzadas no hay marcadores `??` ni comandos `\ref{}`: los cuatro apuntadores `§` del texto —«(§34)» y «§59–§60» (L38, L169), «(§34)» (L1206) y «§59» (L1214)— tienen encabezado destinatario (L1016, L1377, L1387). Persisten los cuatro marcadores de plantilla de §59 —`<!-- kpi:modelo_n_completo -->`, `<!-- kpi:modelo_candidatas -->`, `<!-- kpi:modelo_r2_completo -->` y `<!-- kpi:modelo_pf_completo -->` (L1381)—, insertados en la prosa y no resueltos en el texto cacheado. Los títulos de edición señalados antes continúan —§45, §46, §47 «Reescritura de la sección 3 / Apertura de la sección 3 / Reescritura de la sección 4 del storytelling» (L1212, L1220, L1228)—, frente a títulos instructivos como §26 «Orden corregido: enlace → clasificación → BD» (L926) y §39 «Continuación del scrapeo y presentación narrativa» (L1125).

— polarity: neutral · confidence: high · related: [[#C003]], [[#C011]], [[#C016]], [[#C059]]

## Resumen

- Sin resumen VSN-C, sin hipótesis falsable y sin sección de contribuciones; las aportaciones quedan en §12 y en el posicionamiento de §71.6.
- §1 coincide en ambas partes y §12 ya no diverge, pero la fila 8 de la tabla de fases conserva un nombre retirado por §21 en la versión inglesa.
- La numeración 1–12 continúa duplicada y §13 rompe el nivel de encabezado; las cuatro referencias `§` resuelven y no hay marcadores `??` ni `\ref{}`.


## §2 — v2-methodology


# V2 — Methodology (findings)

### F-V2-001 — Las bases de comparación no incluyen un enfoque adyacente al estado del arte operacionalizado

La nueva §71.1 (L1489–1495) enumera tres filas: la mediana global ingenua (MAE 18.220,46 USD sobre 1.444 anuncios), `Egyptian-Used-Cars` como «referencia de ingeniería del campo» con «contraste cualitativo de cobertura y frescura», y el «Modelo principal propio» (R² 0,101 sobre 584 observaciones). El criterio `V2.baselines` para `level=master` se lee: «≥2 baselines, one of which corresponds to a SOTA-adjacent approach in the field». La primera fila es un baseline trivial; la segunda es un contraste cualitativo de cobertura sin métrica calculada sobre los datos propios; la tercera es el modelo propuesto, no una base externa. Los trabajos más cercanos citados en §71.6 (Gegić et al. 2019, Muça et al. 2026, Du et al. 2026) se usan para posicionamiento argumentativo, no se operacionalizan como bases con métrica comparable. La sección declara tres filas, pero no dos bases en el sentido del criterio.

— polarity: negative · confidence: high · related: [[#C014]], [[#C011]], [[#C012]], [[#C016]] · criteria: V2.baselines.master

### F-V2-002 — Ablación explícita del término `hp`, con especificación y muestra informadas conjuntamente

La §71.2 (L1499) declara la ablación del término `hp` apoyada en `modelo_muestra.csv`: al retirarlo, la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² de 0,274 a 0,101, e informa explícitamente que «el cambio de especificación y el cambio de muestra se informan juntos». El criterio `V2.ablations` para `level=master` se lee: «Explicit ablation of at least one component». La ablación existe, está etiquetada como tal y cuantifica el efecto, por lo que supera el estándar de nivel. Como matiz observacional, la retirada del componente y el cambio de tamaño muestral están confundidos en el mismo contraste, de modo que el texto no aísla la contribución del término de la contribución de la selección de anuncios con kilometraje declarado; el propio párrafo atribuye a esa selección el signo positivo de antigüedad.

— polarity: positive · confidence: high · related: [[#C015]], [[#C004]], [[#C005]] · criteria: V2.ablations.master

### F-V2-003 — Tests declarados para grupos independientes, sin test del contraste central

La §71.3 (L1505) afirma que no hay diseño pareado y que se usan Kruskal-Wallis y Welch para grupos independientes; la §60 (L1389) reporta p mínimo 0,165, VIF 1,13–1,58 y Kruskal-Wallis p = 1e−05. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)». Dado que el documento declara observaciones independientes, los tests pareados no son aplicables y la elección de tests de grupos independientes es coherente con el criterio. Sin embargo, los dos contrastes comparativos centrales —la caída de R² de 0,274 a 0,101 en la ablación de §71.2 y el paso de −5,43 % anual con p<0,001 en §34 (L1056) a la no significancia actual de §59— se presentan sin test de diferencia ni intervalo de confianza que acompañe la comparación. El criterio de nivel master se satisface en la forma (tests declarados y elegidos según el diseño), pero queda sin cuantificar la incertidumbre de esos dos contrastes.

— polarity: neutral · confidence: medium · related: [[#C004]], [[#C006]], [[#C015]], [[#C060]] · criteria: V2.statistical_tests.master

### F-V2-004 — Tamaño expresado en anuncios, con una especificación completa de 28 observaciones y ocho marketplaces

La §71.3 (L1505) fija el tamaño en 981 candidatas de 8 marketplaces; la §71.1 (L1493) reporta 584 observaciones para el modelo principal y la §59 (L1381) reporta 28 observaciones completas de 981 candidatas para el modelo con todos los términos. El criterio `V2.sample_size` para `level=master` se lee: «≥20 trials; ≥10 datasets/instances». La unidad declarada son anuncios observacionales, no ensayos: el modelo principal (584) supera holgadamente el umbral numérico de 20, pero el modelo completo se apoya en 28 observaciones y ningún coeficiente alcanza p < 0,05 (§71.4, L1512), y el número de fuentes/instancias declaradas es 8, por debajo de 10. La propia §71.4 registra la limitación, de modo que la desviación está documentada aunque no corregida. No hay análisis de potencia; el criterio de nivel master no lo exige.

— polarity: neutral · confidence: high · related: [[#C005]], [[#C060]], [[#C061]] · criteria: V2.sample_size.master

### F-V2-005 — Subsección dedicada que cubre los cuatro tipos de amenaza a la validez

La §71.4 (L1509–1512) dedica una subsección explícita a amenazas externa (solo La Habana, precios pedidos), de constructo (kilometraje y potencia ausentes en la mayoría de los anuncios, condición inferida del texto), interna (sin asignación aleatoria, ablación observacional) y estadística conclusiva (28 observaciones, ningún coeficiente con p < 0,05, signo de antigüedad reflejo de selección). El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations». El documento no solo cumple sino que enumera las cuatro categorías que el nivel doctoral exige como sección dedicada, aunque sin mitigaciones explícitas ni declaración de replicabilidad, que son requisitos de nivel `paper`. La subsección además reformula límites ya presentes en §18 y §19, lo que refuerza la coherencia interna del apartado.

— polarity: positive · confidence: high · related: [[#C061]], [[#C013]], [[#C007]] · criteria: V2.threats_to_validity.master

### F-V2-006 — Protocolo de reproducción con semilla, comando único, dependencias fijadas y prueba de humo

La §71.5 (L1516) declara `SEED = 20261127` en `run_all.py`, el comando único `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py`, cuatro puntos de entrada con argumentos, dependencias fijadas a serie menor en `requirements.txt` y la prueba de humo `python3 Auxiliares/herramientas/test_smoke_pipeline.py`. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced». Los tres elementos están presentes y se refiere al código versionado; la declaración de dependencias y la prueba de humo exceden el mínimo del nivel. No se declaran versiones de los datasets ni un commit/DOI pinnado, requisitos propios de los niveles `phd` y `paper`, no del nivel evaluado.

— polarity: positive · confidence: high · related: [[#C059]], [[#C008]] · criteria: V2.reproducibility_protocol.master

### F-V2-007 — Coexistencia de dos especificaciones y dos valores de R² sin reconciliación explícita en la sección 71

La §59 (L1381) describe «el modelo con todos los términos» con 28 observaciones, R² 0,277 y p del F 0,411; la §71.1 (L1493) presenta como «Modelo principal propio» un OLS con 584 observaciones y R² 0,101; la §71.2 (L1499) atribuye R² 0,274 a la especificación de 28 observaciones. La sección nueva no identifica explícitamente ambos ajustes como dos especificaciones separadas ni explica la diferencia entre 0,277 y 0,274 para la misma muestra de 28, pese a que ambos valores se presentan como resultados de la corrida vigente del 27/11/2026. Bajo el criterio `V2.reproducibility_protocol` para `level=master` —«Protocol fully described + seeds mentioned + code referenced»—, la coherencia entre declaraciones de distintas secciones forma parte del protocolo descripto; la falta de reconciliación deja ambiguo cuál de los dos modelos es el principal y cuál es el de referencia para la ablación.

— polarity: negative · confidence: medium · related: [[#C003]], [[#C005]], [[#C014]], [[#C015]], [[#F-V2-004]], [[#F-V2-006]] · criteria: V2.reproducibility_protocol.master


## §3 — v3-results-evidence


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


## §4 — v4-novelty


## Resumen

- E1 pasa de una a dos afirmaciones `novelty` (C011, §34; C016, §71.6): la nueva §71.6 enuncia cuatro diferenciadores frente a los vecinos académicos del mapa, no solo frente al repositorio egipcio.
- F-V10-006 queda **resuelta en el eje de diferenciación** (`V4.differentiation_from_prior_art.master`) y **parcialmente resuelta en el de engagement**: hay cita nominal, contraste y subsección propia, pero sin marcadores numéricos ni discusión de resultados o limitaciones más allá de una frase por trabajo.
- Las fichas [9], [14], [26] y [29] ya figuran corregidas en disco (`Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)`), de modo que H2 de E2 quedó desactualizada; sin búsquedas nuevas ni lectura L3 no corresponde declarar novedad confirmada.

### F-V4-001 — §71.6 resuelve el núcleo de F-V10-006: cuatro contrastes argumentativos con los vecinos académicos

El inventario de esta iteración registra «By type: result 62 · methodological 48 · novelty 2 · contextual 45 · definitional 6 · citation-grounded 12» (e1-claims, línea 15), frente al `novelty 1` de la iteración 2. El claim nuevo es C016 (e1-claims, líneas 199–209), que cita verbatim en §71.6 (L1520): «Frente a Gegić, Isaković, Keco, Mašetić y Kevrić (2019), que predicen precios con machine learning sobre catálogos estructurados, este trabajo parte de anuncios en lenguaje libre y construye las variables por análisis del texto: la contribución es de procedencia y normalización, no de algoritmo». El mismo párrafo añade tres cláusulas contrastivas: frente a Muça, Bani y Alla (2026), «el énfasis aquí es la conversión con TRMI fechada y la auditoría de procedencia, no el pipeline de integración»; frente a Du, Yang, Zhang, Li y Liu (2026), «este trabajo no estima una tasa anual: reporta la no significancia de los coeficientes y la pérdida de muestra como hallazgo»; frente a Vidal Alejandro, Muñiz-Cuza y Calas Torres (2024), «la tasa informal se usa aquí como convención de conversión fechada, no como objeto de estudio».

Los cuatro vecinos son los trabajos más cercanos del mapa: P001 en este artefacto (P014 / [14] en la pasada 1) — Gegić, E.; Isaković, B.; Keco, D.; Mašetić, Z.; Kevrić, J. (2019), «Car Price Prediction using Machine Learning Techniques», *TEM Journal*, DOI 10.18421/tem81-16, «el antecedente más directo de la combinación scraping + modelado de precios» (E2 pasada 1, L176); P002 (P026 / [26]) — Muça, M.; Bani, K.; Alla, A. (2026), «A Pipeline for Integrating and Analyzing Public Business Data in Albania Using Web Scraping and Machine Learning», *IJACSA*, DOI 10.14569/ijacsa.2026.0170845; P003 (P009 / [9]) — Du, Z.; Yang, Z.; Zhang, Y.; Li, S.; Liu, Y. (2026), «Nonlinear Depreciation and Brand Heterogeneity in Chinese Used-Car Listing Prices: An Interpretable Hedonic Regression and Out-of-Sample Evaluation», DOI 10.54254/2754-1169/2026.38524, «el paralelo metodológico más cercano al informe» (L123); y P004 (P029 / [29]) — Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A. (2024), «Using AI in the informal currency market: evidence from Cuba», *Applied Economics*, DOI 10.1080/00036846.2024.2416091. E2 de iter3 confirma en H1 (L106–110) que las cuatro comparecen como menciones nominales con autor y año y que cada una recibe «una cláusula contrastiva que describe el trabajo ajeno y enuncia el diferenciador propio», y en H3 (L116–118) que hay «un apartado propio con cuatro párrafos comparativos nominales, uno por vecino académico».

El criterio `V4.differentiation_from_prior_art` para `level=master` exige «Differentiator articulated with at least one explicit comparison paragraph to one closest prior work» (level-criteria.md, línea 88). Esa condición ahora se cumple —y se supera en número— con trabajos del mapa, frente a la iteración 2, donde el único pasaje comparativo era «Brecha frente a Egipto» (§34, L1058–1060) contra una fuente de ingeniería ajena al mapa. En consecuencia, el núcleo de F-V10-006 («diferenciación solo contra el repositorio egipcio: NO RESUELTA», e1-claims iter2, L849) queda resuelto: el diferenciador declarado es de procedencia y normalización, con la conversión con TRMI fechada y la auditoría de procedencia como ejes concretos, y el contraste se dirige a los cuatro vecinos académicos.

— polarity: positive · confidence: high · related: [[#C011]], [[#C012]], [[#C016]], [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#F-V10-006]] · criteria: V4.differentiation_from_prior_art.master

### F-V4-002 — V4.prior_art_engagement: cita nominal, contraste y subsección propia, pero discusión de una sola frase

El criterio `V4.prior_art_engagement` para `level=master` exige tres condiciones conjuntas: «Closest prior works cited, contrasted, and discussed in their own subsection» (level-criteria.md, línea 106). La iteración 3 satisface la segunda y la tercera de forma inequívoca —§71.6 (L1518–1520) es una subsección dedicada con un contraste por vecino— y la primera en su forma mínima: H1 constata «sí, como menciones nominales con autor y año» para los cuatro (E2 iter3, L106). La calificación es, empero, parcial: H1 añade que «las menciones no van acompañadas de marcador numérico `[14]`, `[26]`, `[9]` ni `[29]`, el documento no contiene ningún marcador `[N]` en su cuerpo, y la lista de «referencias citadas y verificadas externamente» de §70 no incluye a estas cuatro obras» (L110), y H3 observa que «el apartado no incorpora marcadores numéricos, cifras de los trabajos ajenos ni discusión de sus resultados o limitaciones más allá de la descripción de una frase» (L118).

La tercera condición —«discussed»— queda, por tanto, sólo en el umbral formal: cada vecino recibe una caracterización de una frase («predicen precios con machine learning sobre catálogos estructurados», «integran datos públicos empresariales albaneses mediante scraping», «modelan depreciación no lineal y heterogeneidad de marca», «estudian el mercado informal de divisas en Cuba»), sin exponer sus métodos, resultados ni limitaciones. El estándar `phd` del mismo criterio («All closest prior works engaged with substantively (methods, results, limitations of each)», línea 107) está claramente fuera de alcance; el de master se cumple en la forma pero no en la sustancia de la discusión. La lectura calibrada es: F-V10-006 resuelta en diferenciación (F-V4-001), **parcialmente resuelta en engagement**; para cerrarla del todo harían falta los marcadores `[9]`/`[14]`/`[26]`/`[29]` en el cuerpo y, al menos, un resultado o limitación discutidos por trabajo.

— polarity: neutral · confidence: high · related: [[#C016]], [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#F-V10-006]], [[#F-V4-001]], [[#F-V4-004]] · criteria: V4.prior_art_engagement.master

### F-V4-003 — Alcance local declarado sin sobreclaim: procedencia y normalización, no algoritmo ni tasa de depreciación

C011 conserva el diferenciador de integración —«Creé `Data/analisis_rentabilidad/` siguiendo la arquitectura del repositorio Egyptian-Used-Cars [...] pero adaptada a nuestras fuentes y preparada para crecer» (§34, L1018; e1-claims, línea 144)—, ahora explícitamente ampliado por C016 en §71.6: «la contribución es de procedencia y normalización, no de algoritmo», «este trabajo no estima una tasa anual» y «la tasa informal se usa aquí como convención de conversión fechada, no como objeto de estudio». El objetivo vigente sigue excluyendo la novedad de producto: «La definición de un producto interactivo que recomiende la compra más rentable según las preocupaciones del usuario queda diferida a una especialización posterior» (§1, L16; C001). No aparecen verbos de primacía («primero», «nuevo método», «contribución original») que contradigan el mapa: la única reclamación de escala, «Brecha frente a Egipto» (C012, §34, L1060), se enuncia en dirección desfavorable al propio proyecto. No se detecta, por tanto, sobreclaim que corregir.

El criterio `V4.scope_of_novelty_claim` para `level=master` pide «Component novelty + integration novelty: one of the two should be substantive» (level-criteria.md, línea 97). El lado de integración es ahora sustantivo **en su declaración** frente a P001 —cuya `abstract_analysis` (E2 pasada 1, L176) señala que Gegić «no documenta deduplicación, procedencia por fuente ni separación de monedas, que son justamente los ejes del informe»— y frente a P004 —donde «el informe toma la tasa publicada como insumo y no construye su propio estimador» (L342)—. No se reclama novedad de componente ni se contrasta el método propio con cifras de esos trabajos, así que la sustantividad queda en el plano de lo enunciado, no demostrado. El alcance es local y está declarado como tal; en ese marco, la calibración master se satisface en el eje de integración.

— polarity: positive · confidence: high · related: [[#C001]], [[#C011]], [[#C012]], [[#C016]], [[#P001]], [[#P004]] · criteria: V4.scope_of_novelty_claim.master

### F-V4-004 — Fichas [9], [14], [26] y [29] corregidas en disco; H2 de E2 quedó desactualizada

El mapa E2 de esta iteración (generado a las 01:03:37 -04:00 del 28/11/2026) consigna en P001–P004 que las fichas correspondientes conservan `Citada en el informe: no` y que «debe pasar a `sí` con calificación «mención nominal en §71.6, sin marcador numérico» (L36, L48, L60, L72), y H2 resume: «no para cuatro campos» (L112–114). Sin embargo, `Data/referencias.md` en disco —modificado a las 01:05:56 -04:00, es decir, después de E2— ya registra para [9], [14], [26] y [29] la línea «Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)» (L24, L34, L58, L64 del archivo). La inconsistencia de campo que H2 atribuía a cuatro fichas está, por tanto, cerrada en el estado actual, y la calibración de V4 debe usar el archivo vigente, no la afirmación de H2.

La corrección es de aparato bibliográfico, no de novedad: §70 (L1477) sigue enumerando como «referencias citadas y verificadas externamente» sólo a Akerlof (1970), DfT/DVLA, ANFAC y AEADE, y el cuerpo mantiene cero marcadores `[N]` (E2 iter3, L87). Que las cuatro fichas digan `sí` respalda F-V10-006 en el plano formal —las obras ya no figuran como no citadas— pero no sustituye la discusión sustantiva pendiente de F-V4-002.

— polarity: neutral · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#F-V10-006]], [[#F-V4-002]] · criteria: V4.prior_art_engagement.master

### F-V4-005 — Sin novedad confirmada: mapa reutilizado, cero búsquedas temáticas y sin lectura L3

El frontmatter de E2 iter3 declara `queries_run: 0`, `papers_l1: 4`, `papers_l2: 4`, `papers_l3: 0`, y la nota de entrada aclara que «no se ejecutaron búsquedas web nuevas —los metadatos se reutilizan del mapa completo de 38 trabajos de la pasada 1—» (L16). La sección `Likely missing important works` pasa de ocho a siete obras porque «Gegić et al. (2019) sale de la lista porque ya no está ausente del cuerpo» (L100), sin que se propongan obras nuevas. En consecuencia no hay antecedente capaz de desplazar a P001–P004 como vecinos más cercanos, pero tampoco lectura L3 que permita refinar el solapamiento: P001–P004 están re-visados en cuerpo (`Layer: L2`, «sin nueva lectura de resumen en esta iteración», L32, L44, L56, L68).

Una conclusión de «novedad confirmada» excedería esta evidencia. Bajo `V4.prior_art_engagement.master` (level-criteria.md, línea 106), los cuatro vecinos están ahora nombrados, contrastados y ubicados en subsección propia —un cambio real frente a la iteración 2, donde F-V4-005 podía afirmar que «los trabajos más cercanos no están citados en el cuerpo, contrastados ni discutidos en su propia subsección»—, pero la lectura permitida sigue siendo «sin antecedente nuevo añadido en esta pasada», no ausencia de arte previo ni validación de originalidad.

— polarity: neutral · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#C016]], [[#F-V4-001]], [[#F-V4-002]] · criteria: V4.prior_art_engagement.master

## Estado de F-V10-006 según V4

**Resuelta en diferenciación; parcialmente resuelta en engagement.** La §71.6 sustituye el único contraste por escala contra el repositorio egipcio por cuatro contrastes argumentativos con los vecinos académicos del mapa, y las fichas [9], [14], [26] y [29] ya reflejan su mención nominal en el cuerpo. Queda como salvedad de forma, no de novedad, la ausencia de marcadores numéricos y de discusión de resultados o limitaciones de esos cuatro trabajos.


## §5 — v5-state-of-the-art


- Cobertura: 5 de 38 trabajos citados por nombre (13,2 %, frente a 1/38 en la iteración 2); los cuatro clústeres principales y adyacentes tienen al menos una mención y solo el de frontera queda en 0/3, lejos del tramo 25–60 de `V5.coverage_breadth.master`.
- Actualidad: 18 de 38 referencias (47,4 %) son de 2022–2026 y 3 de 5 menciones en el cuerpo (60 %) son de 2024–2026, por encima del 40 % de `V5.recency.master`, pero concentradas en §71.6.
- Peso y ausencias: 10 de 16 afirmaciones load-bearing sin cita externa y 0 marcadores `[N]`; la lista de ausencias probables baja de 8 a 7 y 21 de los 23 trabajos del top-5 por clúster siguen fuera del texto.

### F-V5-001 — Cobertura por clúster — 5 de 38 trabajos citados por nombre; solo el clúster de frontera sin representación

El mapa E2 vigente reparte 38 trabajos en cinco clústeres: asimetría de información y calidad (8), modelos de precio, regresión hedónica y depreciación (12), ética/legalidad/procedencia/calidad de datos (8), Cuba/divisas/movilidad/asequibilidad (7) y señales de precio en marketplaces (3). Tras la §71.6 (L1518–1520) el cuerpo nombra cinco: Akerlof [1] en §17 (L797), §19 (L841) y §70 (L1477); Gegić [14] y Du [9] en §71.6 (L1520), del clúster de modelos de precio; Muça [26] en el mismo párrafo, del clúster de ética/procedencia; y Vidal Alejandro [29], del clúster de Cuba. La distribución es 1/8, 2/12, 1/8, 1/7 y 0/3: 5 de 38 (13,2 %) frente a 1 de 38 (2,6 %) en la iteración 2.

E2 de esta iteración define «Cited in document» como mención nominal (L16), de modo que la presencia de las 38 entradas en `Data/referencias.md` no equivale a cobertura en el argumento. El criterio `V5.coverage_breadth.master` se lee: «Main + adjacent clusters covered (25–60 papers)». Cinco menciones nominales quedan por debajo del tramo incluso antes de descontar el clúster 5, que es de frontera y no exigible en nivel master. El cambio estructural frente a la iteración 2 es que los cuatro clústeres principales y adyacentes pasan de 0–1 menciones a al menos una cada uno; la magnitud absoluta no cambia de régimen.

— polarity: negative · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#F-V5-003]] · criteria: V5.coverage_breadth.master

### F-V5-002 — Actualidad — 18 de 38 referencias de los últimos cinco años y 3 de 5 menciones en el cuerpo

La tabla de distribución de E2 iter3 (L78–85) registra en la bibliografía numerada seis entradas de 2026 ([9], [10], [11], [24], [26], [35]), una de 2025 ([22]), seis de 2024 ([18], [25], [28], [29], [30], [32]), cuatro de 2023 ([15], [23], [27], [34]), una de 2022 ([17]) y veinte de 2021 o antes. El tramo 2022–2026 suma 18 de 38 (47,4 %), por encima del 40 % del criterio `V5.recency.master` —«At least 40% from the last 5 years; foundational classics balanced»—; esta proporción es idéntica a la de la iteración 2 porque el aparato numerado no se modificó.

En el cuerpo, las cinco menciones nominales son Akerlof 1970 [1] y las cuatro de §71.6: Muça [26] y Du [9] de 2026, Vidal Alejandro [29] de 2024 y Gegić [14] de 2019. Tres de cinco (60 %) son de los últimos cinco años, frente a 0 de 1 (0 %) en la iteración 2; los dos clásicos —1970 y 2019— aportan el equilibrio que el mismo criterio describe. La mejora se localiza en un apartado de cumplimiento de estándares (§71.6, L1518–1520) situado al final del documento: las secciones analíticas §17–§20 (L787–871), §34 (L1016–1052) y §59–§60 (L1377–1391) no incorporan a estas cuatro obras. El seguimiento de preprints de los últimos 18 meses no es exigible en nivel master; [24] (Hohensinner et al. 2026, arXiv:2601.14311) permanece en la bibliografía sin mención en el cuerpo.

— polarity: positive · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#F-V5-005]] · criteria: V5.recency.master

### F-V5-003 — Peso de la citación — cuatro vecinos académicos con autor y año en un apartado propio

§71.6 (L1520) abre un apartado titulado «Posicionamiento frente a trabajos cercanos / Positioning against prior work» con cuatro cláusulas contrastivas, una por trabajo: «Frente a Gegić, Isaković, Keco, Mašetić y Kevrić (2019)…», «Frente a Muça, Bani y Alla (2026)…», «Frente a Du, Yang, Zhang, Li y Liu (2026)…» y «Frente a Vidal Alejandro, Muñiz-Cuza y Calas Torres (2024)…». Cada cláusula describe el trabajo ajeno y enuncia un diferenciador propio —procedencia y normalización, conversión con TRMI fechada, no estimación de tasa anual, tasa informal como convención—. El criterio `V5.citation_weight.master` exige «Load-bearing claims cite source + author named in body at first mention»: los cuatro autores quedan identificados por nombre en su primera mención, y E1 registra el bloque como afirmación load-bearing C016 (L199–209).

La calificación es parcial: las cuatro comparaciones comparten un único párrafo, sin marcadores `[14]`, `[26]`, `[9]` ni `[29]`, y la búsqueda de marcadores `[N]` en el cuerpo devuelve 0 coincidencias (E2 iter3, L87). §70 (L1477) enumera como «referencias citadas y verificadas externamente» solo Akerlof y tres fuentes institucionales, de modo que los cuatro vecinos figuran en el anexo numerado pero no en esa enumeración. E2 (H3, L116–118) describe el apartado como discusión dedicada de forma, sin cifras de los trabajos ajenos ni discusión de resultados o limitaciones.

— polarity: positive · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#C016]] · criteria: V5.citation_weight.master

### F-V5-004 — Peso de la citación — 10 de 16 afirmaciones load-bearing sin cita externa y ningún marcador numérico en el cuerpo

El inventario de E1 de esta iteración contiene 126 afirmaciones, 16 de ellas load-bearing (L13–14). Diez conservan «External evidence cited: — (sin citas numeradas)» —C001–C006, C008, C010, C013 y C015 (L27, L39, L51, L63, L75, L87, L111, L135, L171, L195)—. Cinco remiten a fuentes institucionales o de ingeniería —C007 y C009 a DfT/DVLA, ANFAC y AEADE; C011, C012 y C014 al repositorio `Egyptian-Used-Cars`— y solo C016 nombra a los cuatro pares académicos de §71.6. La proporción sin evidencia externa es 10/16 (62,5 %), frente a 9/13 (69,2 %) en la iteración 2.

El aparato numerado de 38 entradas no se enlaza al texto: 0 marcadores `[N]` en las 1.523 líneas (E2 iter3, L87), y los cuatro flags actualizados a «sí (mención nominal en §71.6, sin marcador numérico)» (L24, L34, L58, L64) consignan esa misma ausencia en la ficha. El criterio `V5.citation_weight.master` —«Load-bearing claims cite source + author named in body at first mention»— queda satisfecho en su mitad nominal para C016 y sin satisfacer en las diez afirmaciones sin cita externa.

— polarity: negative · confidence: high · related: [[#C001]], [[#C016]], [[#F-V5-003]] · criteria: V5.citation_weight.master

### F-V5-005 — Ausencias probables — la lista baja de ocho a siete obras; Gegić queda dentro y las siete restantes fuera del cuerpo

E2 iter3 reduce la lista de «Likely missing important works» de ocho a siete (L98–100): retira Gegić et al. 2019 [14], que tiene comparación nominal en §71.6, y conserva Lewis 2011 [2] (342 citas), Englmaier et al. 2017 [4] (50), Krotov et al. 2020 [21] (224), Priestley et al. 2023 [23] (153), Brown et al. 2025 [22] (118), Guerra 2015 [33] (113) y Hohensinner et al. 2026 [24] (13). Las siete mantienen «Citada en el informe: no» en `Data/referencias.md` (L10, L14, L48, L50, L52, L54, L72) y ninguna aparece en el cuerpo.

La relación con afirmaciones cargadas se mantiene: Lewis es el eslabón empírico entre Akerlof y la captura de defectos y tipo de vendedor (E2 pasada 1, L495); Englmaier advierte sobre saltos en umbrales de año y 10.000 km frente a la retirada de la pendiente anual en §59–§60 (L1381, L1389); Krotov y Brown corresponden a la regla de no eludir anti-automatización de §10 (L118); Priestley a la arquitectura de colas y cuarentena de la fase 7; Guerra a `asequibilidad = precio / salario`; Hohensinner a la distinción entre procedencia y linaje. El criterio `V5.missing_important_work.master` se lee: «Top-5 most-cited of each adjacent cluster expected». De las 23 obras distintas que forman los top-5 por clúster, dos están citadas por nombre —Akerlof [1] y Gegić [14]— y 21 ausentes (91,3 %), frente a 22 (95,7 %) en la iteración 2.

— polarity: negative · confidence: high · related: [[#P001]], [[#F-V5-001]] · criteria: V5.missing_important_work.master

### F-V5-006 — Flags por campo — cuatro fichas de citación alineadas con §71.6 y tres marcadores con el campo nominal

`Data/referencias.md` actualiza las fichas [9], [14], [26] y [29] a «Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)» (L24, L34, L58, L64), en correspondencia con el campo definido en L6 como «mención nominal en el informe». E2 (H2, L112–114) constata que los cuatro flags estaban desactualizados porque el archivo se generó antes de existir §71.6 y que autores, año, revista, DOI y conteo de citas permanecen verificados.

Los tres marcadores `(metadata incomplete)` restantes nombran el campo ausente: «resumen indexado no sustantivo» en [1] (L8), «resumen no indexado; campos bibliográficos verificados» en [10] (L26) y «resumen no indexado en OpenAlex; discrepancia de año documentada» en [38] (L82). Las notas de discrepancia de año de [2], [19] y [38] permanecen. Frente a los seis marcadores genéricos sin campo de la iteración 2, la ficha distingue ahora entre dato ausente y dato recuperado: [18], [19] y [20] consignan conteos de citas verificados y versión publicada (L42, L44, L46). Esta distinción es la que permite ponderar el peso de cada entrada del aparato al calibrar `V5.citation_weight.master`.

— polarity: positive · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#F-V5-004]] · criteria: V5.citation_weight.master


## §6 — v6-reproducibility


## Resumen

- `V6.documentation.master` y `V6.entry_points.master` quedan cubiertos: README con quickstart, dependencias y ejemplos, y puntos de entrada con argumentos verificados en los docstrings; dos huellas de mapeo (apéndice visual y panel vigente) no aparecen declaradas en el texto cacheado.
- `V6.environment.master` y `V6.determinism.master` quedan cubiertos en forma sintáctica: doce dependencias con `~=X.Y.0` y `SEED = 20261127` coincide entre `run_all.py` y §71.5; §34 consigna dos series distintas y la semilla no es consumida por las cinco etapas.
- `V6.tests.master` y `V6.data_availability.master` tienen infraestructura presente: la prueba de humo pasa 4/4 y los conjuntos están nombrados con rutas, aunque las dos bases SQLite principales figuran solo como rutas locales LFS.

### F-V6-001 — README con quickstart, dependencias y ejemplos de uso

`README.md` (105 líneas) contiene el quickstart de las líneas 15–33: creación de `Auxiliares/.venv-py`, `pip install -r requirements.txt` y `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py`, seguido de la lista de salidas esperadas. Las secciones «Estructura» (35–50), «Fuentes de datos» (54–64) y «Configuración» (66–80) declaran rutas de datos y de herramientas, y el apartado «Documentación» (94–99) remite a `INFORME_TECNICO.md`, `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md` y otros índices. El criterio `V6.documentation.master` se lee «README + lista de dependencias + ejemplos breves de uso»; los tres elementos están presentes, y §60, §61 y §71.5 (líneas 1405, 1399 y 1516) añaden mapeos componente→repositorio dentro del propio informe.

— polarity: positive · confidence: high · related: [] · criteria: V6.documentation.master

### F-V6-002 — Apéndice visual anunciado en §59 pero ausente en la caché de texto

§59 (línea 1381) afirma «Se añadió además un **apéndice visual** con cinco cuadros y seis gráficos reales» y §61 (línea 1401) declara «Los seis gráficos Plotly se copian a `docs/graficos/` y se enlazan desde el apéndice; las tablas del apéndice y la página de KPIs se generan desde los CSV». El inventario E3 lo registra como `Missing artifact`: en disco existen `docs/graficos/`, `docs/historia/apendice/` y `site/historia/apendice/`, pero la caché auditada conserva solo la mención, sin los cinco cuadros ni los seis gráficos. La única ruta de mapeo declarada en el texto es la carpeta genérica `docs/graficos/`; las cifras del apéndice dependen de los CSV de `outputs/tables/`, que quedan fuera del documento texto.

— polarity: neutral · confidence: high · related: [[#F-V6-003]] · criteria: V6.documentation.master

### F-V6-003 — Ruta `Data/dashboard.html` no declarada en el informe

§71.5 (línea 1516) cita `generar_dashboard.py --solo-si-cambia` entre los puntos de entrada y §61 describe el sitio MkDocs, pero ningún pasaje de la caché nombra la ruta `Data/dashboard.html` que ese generador produce. E3 la consigna como `Missing artifact`: 109.929 B en disco, con copias idénticas en `docs/dashboard.html` y `site/dashboard.html` y generación desde `Auxiliares/herramientas/generar_dashboard.py` (402 LOC). Las únicas rutas HTML explícitas en el texto son las de `Data/analisis/` (líneas 578, 604 y 892), derivadas de una etapa anterior; la existencia del panel vigente es verificable en el repo, no desde la lectura literal del informe.

— polarity: neutral · confidence: high · related: [[#F-V6-002]] · criteria: V6.entry_points.master

### F-V6-004 — Doce dependencias fijadas a serie menor en `requirements.txt`

`requirements.txt` tiene 14 líneas (2 comentarios y 12 dependencias), todas con el operador compatible `~=X.Y.0`: pandas 2.2.0, numpy 1.26.0, plotly 5.18.0, statsmodels 0.14.0, scipy 1.11.0, beautifulsoup4 4.12.0, curl_cffi 0.7.0, tenacity 8.2.0, trafilatura 1.6.0, pyarrow 14.0.0, mkdocs 1.6.0 y mkdocs-material 9.5.0. Su encabezado declara «Fijadas a versiones menores (criterio de reproducibilidad de nivel master)» y §71.5 (línea 1516) afirma «Las dependencias están fijadas a serie menor en `requirements.txt`». El criterio `V6.environment.master` se lee «Dependencias fijadas a versiones menores»; queda satisfecho. No hay `pyproject.toml`, `environment.yml`, lockfile ni Dockerfile en el checkout; lockfile, versión de Python declarada y congelación por contenedor pertenecen a `V6.environment.phd` y `V6.environment.paper`, y `README.md:17` consigna Python 3.10+ como requisito.

— polarity: positive · confidence: high · related: [[#F-V6-005]] · criteria: V6.environment.master

### F-V6-005 — §34 registra series de dependencias divergentes de las fijadas

§34 (línea 1039) consigna «Instalé además `statsmodels 0.15`, `pyarrow 26`, `kaleido`, `nbformat` y `nbconvert`», mientras `requirements.txt:6` fija `statsmodels~=0.14.0` y `requirements.txt:12` fija `pyarrow~=14.0.0`. E3 lo consigna como `Missing artifact` con estado `partial`: no falta un archivo, sino que dos artefactos describen el mismo entorno con series distintas. La afirmación de §71.5 sobre la fijación a serie menor es sintácticamente correcta para el archivo, pero no describe las versiones que §34 atribuye a la instalación efectivamente utilizada.

— polarity: negative · confidence: high · related: [[#F-V6-004]] · criteria: V6.environment.master

### F-V6-006 — Semilla `SEED = 20261127` declarada en código y en §71.5, con el mismo valor

`Data/analisis_rentabilidad/scripts/run_all.py:16–18` contiene `SEED = 20261127`, `random.seed(SEED)` y `np.random.seed(SEED)`; su docstring (líneas 2–7) declara que la semilla «se declara aqui y en el informe para cumplir el criterio de determinismo de nivel master». §71.5 (línea 1516) reproduce literalmente «La semilla `SEED = 20261127` está declarada en `run_all.py` y en este documento». `Auxiliares/herramientas/test_smoke_pipeline.py:54` comprueba la cadena `SEED = 20261127` en el orquestador. El criterio `V6.determinism.master` exige semillas declaradas en código y documento y consistentes entre sí; los tres puntos coinciden.

— polarity: positive · confidence: high · related: [[#F-V6-007]] · criteria: V6.determinism.master

### F-V6-007 — Las cinco etapas no consumen la semilla declarada

`run_all.py:25` define `STEPS = ["01_ingest.py", "02_clean.py", "03_eda.py", "04_stats.py", "05_benchmark.py"]` y `run_all.py:29–35` las invoca con `subprocess.run([PY, str(HERE / step)], …)` sin propagar `SEED`; ninguna de las cinco etapas importa la variable ni declara una semilla propia, y el docstring del orquestador describe las etapas como deterministas. Bajo `V6.determinism.master` («semillas declaradas en código y documento, consistentes») la declaración existe y coincide; en la ejecución actual la semilla opera como marca documental sin consumo directo por las etapas.

— polarity: neutral · confidence: high · related: [[#F-V6-006]] · criteria: V6.determinism.master

### F-V6-008 — Puntos de entrada con argumentos y comando único documentados

§71.5 (línea 1516) declara el comando único `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py` y cuatro puntos de entrada con argumentos. La verificación en disco coincide: `Auxiliares/herramientas/generar_dashboard.py:11` documenta `--solo-si-cambia`, `exportar_parquet_compacto.py:10` documenta `--tablas`, `db_chunks.py:5–7` documenta `split`, `assemble` y `verify`, y `generar_sitio_mkdocs.py` carece de argumentos de línea de comandos y se cita sin ellos. `README.md:19–23` reproduce instalación y comando único, `:77–80` los comandos `db_chunks.py verify|assemble` y `:86–90` los del sitio. El criterio `V6.entry_points.master` («puntos de entrada documentados con argumentos») queda cubierto; el comando único y el mapeo script→tabla del inventario E3, propios de niveles superiores, también están presentes en el repo.

— polarity: positive · confidence: high · related: [] · criteria: V6.entry_points.master

### F-V6-009 — Prueba de humo del componente central presente y ejecutable

`Auxiliares/herramientas/test_smoke_pipeline.py` (66 LOC, cuatro funciones y `main()`) es citado en §71.5 (línea 1516) como `python3 Auxiliares/herramientas/test_smoke_pipeline.py`; su docstring (línea 7) reproduce ese comando. Ejecutado en este checkout imprime «4 pruebas superadas»: 7 scripts compilan, 7 artefactos exigidos existen, 4 CSV son legibles y el comando único contiene la cadena de semilla. La cobertura se limita a compilación, existencia y consistencia textual: no ejecuta el pipeline completo ni comprueba valores numéricos del modelo. El criterio `V6.tests.master` exige «al menos pruebas de humo del componente central»; queda satisfecho. El checkout no contiene `.github/workflows`, configuración correspondiente a `V6.tests.paper`.

— polarity: positive · confidence: high · related: [[#F-V6-006]] · criteria: V6.tests.master

### F-V6-010 — Conjuntos nombrados con rutas de acceso; SQLite crudos sin URL ni DOI

El informe nombra las fuentes en §§9, 52–53, 66 y 70, y `README.md:54–64` las organiza en una tabla con URLs y rutas (`Data/fuentes-oficiales/ONEI/`, GOV.UK, Gaceta Oficial, BCC), con `README.md:75–80` declarando la reconstrucción de `revolico.sqlite` desde chunks. El inventario E3 lista diez datasets: los derivados (`compacto/`, `modelo_muestra.csv`, `referencias.md`) figuran como `yes (en repo)` y fuentes oficiales como accesibles; en cambio `Data/Revolico/revolico.sqlite`, `Data/Revolico/pipeline.sqlite`, `Data/catalogos_concesionarios/` y `Data/repos-autos-referencias/referencias_autos.sqlite` aparecen con accesibilidad pública `unknown` y solo como rutas locales gestionadas con Git LFS. El criterio `V6.data_availability.master` pide nombres más ruta de acceso (URL, DOI o «disponible bajo petición»): la primera condición está cubierta en el texto y en el README; para las dos bases principales la ruta local está documentada, sin URL, DOI ni declaración de disponibilidad en el informe.

— polarity: neutral · confidence: high · related: [[#F-V6-001]] · criteria: V6.data_availability.master


## §7 — v7-writing


# V7 — Writing and AI patterns (findings)

Resumen (tres líneas):
- El corpus pasa de 29.106 a 29.870 palabras (+764): §69 crece de 179 a 271 y §71 es nuevo (606 palabras), sin que suban los tics estrictos — 0 atenuadores, 0 «not just…but», 0 Don't 4, 0 adjetivos sin ancla.
- En §69 desaparecen los tres adjetivos sin ancla de la iteración 2 («quirúrgica», «asistida», «sistemática») y se nombran por fin herramientas, fases y pasos de supervisión; persisten dos triadas de cola larga y el cierre Don't 8, con densidad media.
- §71 se escribe en registro enumerativo y anclado (tablas, listas, comandos, cifras); su densidad media se concentra en §71.6, con cuatro openers «Frente a…», cuatro cierres contrastivos «X, no Y» y cuatro oraciones largas consecutivas, sin alcanzar `ai-pattern-density: high`.

Alcance y método. Conteo directo sobre los textos cacheados de la iteración 1 (`informe-tecnico-2026-11-27.text.md`, 1.462 líneas), iteración 2 (`informe-tecnico-2026-11-27-iter2.text.md`, 1.484) e iteración 3 (`informe-tecnico-2026-11-27-iter3.text.md`, 1.523). «Palabra» sigue el criterio `wc -w` de los informes V7 anteriores, que incluye identificadores, rutas y celdas de tabla; el §13 (registro generado por script) queda fuera del denominador de densidades de prosa. Para metaconceptos se usa la róbrica estrecha de Pinker aplicada en los informes previos (`análisis`, `proceso`, `evaluación`, `consideración`, `implementación`, `auditoría`, `herramientas`, `decisiones`, `resultados`, `apoyo`, `edición`, `revisión`, `cifras`, `modelos`, `afirmación`, `salida`, `estructura`, `marco`, `procesamiento`, `señal`, `arquitectura`); cuando se amplía la róbrica se dice expresamente. Winston, Pinker y Romero §13 se citan como rótulos de las róbricas aplicadas. El artefacto describe patrones y densidades, sin emitir juicio de autoría.

### F-V7-001 — §69: se cierran las tres lagunas de nombrado de la iteración 2, pero la huella sigue apuntando a la iteración 1

La declaración de la iteración 2 (L1469–L1471 de aquel texto) empleaba «Las herramientas de inteligencia artificial» como genérico, nombraba solo la skill `review` y enunciaba la supervisión como principio. La versión de la iteración 3 (L1469, duplicada en L1471) nombra «OpenCode/Claude Code con las skills `review` de MatCom, `deep-research` y `technical-writing`»; declara cuatro fases —«investigación y verificación de fuentes, redacción y edición de la narrativa, generación y revisión de código, y traducción bilingüe»—, de modo que research, drafting, code generation y translation quedan explícitos; y convierte el principio en tres pasos designados: «contrastar toda cifra contra los CSV y bases versionados, ejecutar las pruebas automatizadas y conservar el registro de auditoría en `reviews/`». Son las tres carencias que F-V7-002 y el hook para V7 de la iteración 2 dejaron registradas. Un dato descriptivo persiste: la huella citada sigue siendo `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` «junto con los trece artefactos de fase» (L1469), es decir, los artefactos de la iteración 1, no los `-iter2` ni los `-iter3`; el propio inventario E3 de esta iteración confirma que no había informe de la iteración 3 al cerrarse. Ninguno de estos cambios introduce hedging ni openers de fórmula: las cuatro oraciones abren con sustantivos («Las herramientas», «El protocolo», «Las cifras», «La auditoría»).

— polarity: positive · confidence: high · related: [[#F-V7-002]], [[#F-V7-003]], [[#F-V7-006]]

### F-V7-002 — Romero §13 Don't 5: los tres adjetivos sin ancla de §69 desaparecen y §71 no añade ninguno

Es el cambio más medible de la iteración. Los tres modificadores sin ancla que la iteración 2 introdujo en §69 —«edición **quirúrgica** de la narrativa», «revisión bibliográfica **asistida**» y «auditoría **sistemática** del propio informe» (L1469 de aquel texto, repetidos en L1471)— ya no están: la iteración 3 escribe «redacción y edición de la narrativa», «investigación y verificación de fuentes» y «auditoría **completa** de este documento … y sus resultados se conservan en `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` junto con los trece artefactos de fase» (L1469, L1471). «Completa» queda anclado por la ruta y el recuento; los otros modificadores nuevos del pasaje («bilingüe», «automatizadas», «versionados») son técnicos y están anclados por el propio documento bilingüe, por el comando de prueba de humo de §71.5 (L1516) y por la ruta `reviews/`. En §71 ocurre lo mismo con los tres únicos modificadores valorativos/comparativos presentes: «mediana global ( ingenua )» lleva en la misma celda «MAE 18.220,46 USD sobre 1.444 anuncios» (L1491); «Contraste cualitativo de cobertura y frescura» va acompañado de «23.500 anuncios y series mensuales» (L1492); y «mejor cobertura» (L1512) se apoya en los 584 frente a 28 observaciones de §71.2 (L1499). Los cuatro adjetivos preexistentes con ancla que inventarió la iteración 2 permanecen intactos —«pendiente anual significativa» con p mínimo 0,165 (L1389), «significativa» con p < 0,001 (L1381), «correcciones quirúrgicas» seguidas de cuatro cambios (L1415) y «bibliotecas quizá innecesarias» con 66 MB (L1459)—. Resultado: el subconjunto Don't 5 sin ancla cae de 3 (todos en §69) a 0 en el corpus.

— polarity: positive · confidence: high · related: [[#F-V7-003]], [[#F-V7-009]]

### F-V7-003 — Romero §13 Don't 3 en §69: dos triadas de cola larga (una heredada, una nueva) frente a una enumeración de cola corta

§69 conserva la triada que ya estaba en la iteración 2 —«Las cifras, los modelos estadísticos y las decisiones de diseño» (L1469; «All figures, statistical models and design decisions», L1471)—, cuyo tercer término es el más largo y más abstracto. Añade una segunda, correspondiente al protocolo nuevo: «contrastar toda cifra contra los CSV y bases versionados, ejecutar las pruebas automatizadas y conservar el registro de auditoría en `reviews/`» (L1469; «every figure to be checked … the automated tests to be run … the audit trail to be kept under `reviews/`», L1471), también con el tercer miembro más extenso. En sentido inverso, la enumeración de cuatro fases termina en «traducción bilingüe», el miembro más corto, y la serie de skills («`review` de MatCom, `deep-research` y `technical-writing`») es una lista de nombres sin cola abstracta. El recuento de d3 en §69 se mantiene en 2, pero baja su densidad por el crecimiento de la sección: 2 por 179 palabras en la iteración 2 frente a 2 por 271 en la iteración 3. Fuera de §69 las triadas largas siguen en las 2–3 instancias históricas (L117, L145, L765).

— polarity: neutral · confidence: high · related: [[#F-V7-001]], [[#F-V7-002]], [[#F-V7-005]]

### F-V7-004 — §71, sección nueva: densidad media localizada en 71.6, baja en 71.1–71.5

La sección «Cumplimiento de estándares de nivel master / Master-level standards» (L1485–L1520, 606 palabras) no existía en las iteraciones 1 ni 2, donde el informe cerraba en §70. Sus cinco primeros apartados son enumerativos y están anclados: tabla de bases (L1489–L1493), ablación con cifras (L1499), pruebas y tamaño muestral (L1505), lista de cuatro amenazas (L1509–L1512) y comandos de reproducción (L1516). Con la róbrica estrecha hay 5 metaconceptos en 606 palabras (8,3/1k), 0 atenuadores, 0 openers de fórmula y 0 adjetivos Don't 5 sin ancla; la densidad de esos cinco apartados es baja. El repunte se produce en 71.6, que por sí solo justifica la calificación media de la sección completa. Bajo Winston, los seis títulos (71.1–71.6) son instructivos y nombran el estándar que desarrollan, no rótulos vacíos.

— polarity: neutral · confidence: high · related: [[#F-V7-005]], [[#F-V7-007]], [[#F-V7-009]]

### F-V7-005 — Romero §13 Don't 3 y openers de fórmula en §71.6: cuatro marcos «Frente a…» y cuatro cierres contrastivos

El único párrafo de 71.6 (L1520, 168 palabras) repite cuatro veces el marco «Frente a <apellidos> (<año>), que <descripción del trabajo ajeno>, …» —Gegić et al. (2019), Muça et al. (2026), Du et al. (2026) y Vidal Alejandro et al. (2024)—, con el tercer miembro («este trabajo parte de…», «el énfasis aquí es…», «este trabajo no estima…», «la tasa informal se usa aquí…») sistemáticamente más largo y más abstracto: cuatro instancias de d3 concentradas en 168 palabras. Cada marco se cierra con una negación contrastiva —«no de algoritmo», «no el pipeline de integración», «no estima una tasa anual … no como objeto de estudio»—; se cuentan cuatro. No se registran como Don't 2: la negación discrimina la contribución propia frente a la ajena y hace trabajo argumentativo, a diferencia del «not just X, but Y» redundante (0 instancias en todo el corpus). La uniformidad es de oraciones largas, no de la banda 18–25 palabras: los cuatro períodos miden 44, 34, 44 y 34 palabras, en alternancia estricta, sin cortes cortos intercalados. El párrafo está anclado a autores y años y, en el tercer caso, a la no significancia y la pérdida de muestra de §71.2 y §60; esa es la contrapartida que mantiene el patrón en densidad media y no alta.

— polarity: neutral · confidence: high · related: [[#F-V7-003]], [[#F-V7-004]], [[#F-V7-009]]

### F-V7-006 — Metaconceptos: §69 baja su densidad relativa aunque crece 92 palabras; §71 no la eleva

Con la róbrica estrecha, §69 registra 12 metaconceptos en la iteración 2 (67,0 por 1.000 palabras) y 12 en la iteración 3 (44,3 por 1.000 palabras): el recuento absoluto se mantiene porque las 92 palabras añadidas son sobre todo nombres de herramientas, fases, rutas y comandos, no nuevos sustantivos abstractos. Al ampliar la róbrica con «protocolo», «supervisión», «registro», «verificación» y «fuentes», el total sube de 13 a 18 (de 72,6 a 66,4 por 1.000 palabras) —un aumento de apariciones, no de densidad—. En §71 la róbrica estrecha da 5/606 (8,3/1k). Los sustantivos abstractos que se agrupan en 71.6 («contribución», «procedencia», «normalización», «heterogeneidad», «integración») son términos técnicos vinculados a autores y años, no metaconceptos Pinker sueltos. Las dos zonas que la iteración 1 calificó como densidad alta —§17–21 (≈13,8/1k) y §59–63— permanecen sin cambio.

— polarity: neutral · confidence: high · related: [[#F-V7-001]], [[#F-V7-004]], [[#F-V7-005]]

### F-V7-007 — Winston: paralelismo parcial en §71 y repetición del doble separador superior

El bloque §14–68 mantenía glosa inglesa en 54 de 55 secciones. En §71 ese hábito se interrumpe: solo 71.1 (L1495) y 71.2 (L1501) llevan etiqueta «**EN.**»; 71.3, 71.4, 71.5 y 71.6 carecen de paralelo inglés. El cambio de ritmo es propio de la sección nueva y se suma al dispositivo ya observado en la iteración 2: dos reglas horizontales consecutivas preceden tanto a §69 (L1463, L1465) como a §71 (L1481, L1483). Bajo Winston (section-closing summaries; structure-of-prose), los apartados 71.3–71.6 cierran con dato o lista en lugar de glosa, y no hay resumen de cierre para la sección; se registra como observación de estructura, no como corrección pendiente.

— polarity: neutral · confidence: high · related: [[#F-V7-004]], [[#F-V7-005]]

### F-V7-008 — Romero §13 Don't 2, Don't 4, Don't 8 y Pinker hedging: continuidad sin cambios

«No solo… sino», «not just… but» y equivalentes registran 0 instancias en las tres iteraciones. Las negaciones de salvaguarda de §69 («ninguna salida de IA se aceptó sin ese contraste», «ninguna afirmación empírica se originó en una salida de IA sin contraste contra los archivos», L1469) y las de §71 («los precios son pedidos, no transaccionados», L1509; «no hay asignación aleatoria», L1511) siguen funcionando como constancia de límites, no como énfasis retórico. La forma estricta de Don't 4 mantiene una sola coincidencia, «cada transformación y cada estimación del pipeline» (L1389), referida a transformación de datos; no aparecen «ecosistema», «paradigma» ni «landscape». El único hedging del corpus continúa siendo «bibliotecas quizá innecesarias» (L1459), 0 en §69 y en §71; «relativamente», «somewhat», «perhaps» y «presumably» siguen en 0. Don't 8 persiste en §69: «La auditoría completa de este documento se realizó con la skill `review` de MatCom y sus resultados se conservan en … junto con los trece artefactos de fase» (L1469, L1471) enuncia el resultado sin mostrar hallazgo, densidad ni fragmento; es el mismo mecanismo que el V7 de la iteración 2 registró en este pasaje y en §43–47 y §59–63, sin nuevas apariciones en §71.

— polarity: neutral · confidence: high · related: [[#F-V7-001]], [[#F-V7-002]]

### F-V7-009 — Pinker: densidad de anclaje concreto sostenida en §71

El síntoma «definiciones sin instancias» no aparece en la sección nueva. Cada estándar de nivel master va seguido de su dato: «MAE 18.220,46 USD sobre 1.444 anuncios» (L1491), «23.500 anuncios y series mensuales» (L1492), «R² 0,101 sobre 584 observaciones» (L1493), «28 a 584 observaciones de 981 candidatas» y «R² baja de 0,274 a 0,101» (L1499), «981 candidatas de 8 marketplaces» (L1505), «ningún coeficiente alcanza p < 0,05» (L1512), y en L1516 la semilla `SEED = 20261127`, el comando único, `requirements.txt` y `python3 Auxiliares/herramientas/test_smoke_pipeline.py`. La comparación de 71.6 lleva autor y año en los cuatro casos. Esta densidad de anclajes es la contrapartida de las triadas y de la uniformidad de longitud de F-V7-005 y explica que el patrón general siga siendo de baja densidad de tics pese a las dos secciones nuevas.

— polarity: positive · confidence: high · related: [[#F-V7-002]], [[#F-V7-005]], [[#F-V7-006]]

## AI-pattern density by section

Valores aproximados sobre los textos cacheados, con `wc -w` y la róbrica estrecha de metaconceptos descrita en Alcance. La columna compara iteración 1 → iteración 2 → iteración 3; «—» significa que la sección no existía.

| Section | Density (it1 → it2 → it3) | Notes (iteración 3) |
|---|---|---|
| §1–3 — Objetivo, estados, carpetas (L14–53) | low → low → low | Sin cambio; 0 triadas; openers «Se + verbo» |
| §4–9 — Fases 1–6 (L54–108) | low → low → low | Sin cambio; tablas y listas; 0 atenuadores |
| §10–12 — Marco legal, problemas, conclusiones (L110–139) | medium → medium → medium | «marco» 3; triada en L117; conclusión 5 con ruta (L139) |
| Parte II §1–12 — Objective…Conclusions (L145–270) | low → low → low | Sin cambio salvo nota de actualización; 0 hedges |
| §13 — Registro de altas (L274–748) | n/a → n/a → n/a | Tabla generada por script; excluida del denominador |
| §14–33 — Sincronización, eficiencia, colas, marcos (L750–1008) | medium → medium → medium | Sin cambio; openers «Se…» y bloques EN |
| §17–21 — Guía, auditoría y marcos analíticos (L787–884) | high → high → high | Sin cambio; ≈13,8 metaconceptos/1k; escaleras de pasos |
| §34–48 — Rentabilidad, APK, mapas, storytelling (L1012–1242) | medium → medium → medium | Sin cambio; ancla TRMI 930 y `config.py`; 0 hedges |
| §49–58 — Repos, mejoras, fuentes, ONEI, chunks (L1245–1369) | medium → medium → medium | Sin cambio; negaciones de salvaguarda; d5 con ancla |
| §59–63 — Storytelling final, modelos, sitio, retención (L1373–1415) | high → high → high | Sin cambio en d8/d5; 28/981, R² 0,277, p 0,411 (L1381) |
| §64–68 — Automatización y espacio (L1419–1461) | low–medium → low–medium → low–medium | «quizá» en L1459, único hedge del corpus |
| §69 — Declaración de uso de IA (L1467–1471) | — → medium → **medium** | 271 palabras; d3 ×2, d5 sin ancla 3 → **0**, d8 ×1; 12 metaconceptos/271 (44,3/1k); 0 hedges, 0 openers de fórmula |
| §70 — Referencias verificadas (L1475–1479) | — → low → low | Lista enumerativa con procedencia externa; añade flag `(metadata incomplete: resumen)` para Akerlof (L1477) |
| §71.1–71.5 — Bases, ablación, pruebas, amenazas, reproducción (L1487–1516) | — → — → low | Tablas, listas y comandos; 5 metaconceptos/606 (8,3/1k en toda §71); 0 tics estrictos |
| §71.6 — Posicionamiento frente a trabajos cercanos (L1518–1520) | — → — → **medium** | d3 ×4, openers «Frente a…» ×4, negaciones contrastivas ×4, oraciones de 44/34/44/34 palabras; sin ancla numérica propia pero con autor y año |

Totales de prosa (texto completo, `wc -w`): 28.586 → 29.106 → 29.870 palabras; hedging 1 → 1 → 1; openers de fórmula 0 → 0 → 0; «not just X, but Y» 0 → 0 → 0; Don't 4 estricto 1 → 1 → 1; modificadores de la róbrica Don't 5 4 → 7 → 4 instancias, con el subconjunto sin ancla en 0 → 3 → 0 (los tres que añade §71 —«ingenua», «cualitativo», «mejor cobertura»— son técnicos o comparativos y llevan cifra en la misma celda o sección).

## Hook para V9

Ninguna sección de esta iteración alcanza `ai-pattern-density: high`: §69 y §71.6 son `medium`, §70 y §71.1–71.5 son `low`. Los dos bloques que permanecen en `high` —§17–21 y §59–63— son idénticos a los de la iteración 1 y su anclaje numérico es incompatible con un tic de atenuación. La tabla que V9 declaró no haber recibido en la iteración 2 queda así consignada también para la 3. Para el contraste con `V9.ai_use_declaration.master`, la novedad relevante es que §69 ya nombra herramientas (OpenCode/Claude Code), skills (`review`, `deep-research`, `technical-writing`), las cuatro fases del criterio y tres pasos de supervisión; la densidad media de la sección se debe ahora a dispositivos de superficie —dos triadas de cola larga, metaconceptos y el cierre Don't 8— y no a adjetivos sin ancla ni a hedging, que son 0. Se mantiene el dato descriptivo de que la huella citada apunta a los artefactos de la iteración 1, no a los de esta.


## §8 — v8-bibliography


- 33 DOI y 4 arXiv resuelven y coinciden con el título declarado; sin duplicados ni papers fantasma. Los cuatro flags de §71.6 ya están corregidos en `Data/referencias.md`, con `[1]` en inglés como única desviación de forma.
- La contradicción Akerlof quedó resuelta en §70 ES y en `[1]` (flag por campo: resumen), pero §70 EN y el claim C009 reproducen la versión sin calificar; los conteos de E2 presentan un desfase de +2 en Gegić.
- Dos entradas sin DOI quedan sin verificación de contenido en esta pasada: `[6]` (HTTP 403) y `[31]` (HTTP 404, con la obra identificada en OpenAlex y rutas alternativas).

### F-V8-001 — 33 DOI y cuatro arXiv resuelven; ningún duplicado ni paper fantasma

`Data/referencias.md` contiene 38 entradas numeradas `[1]`–`[38]`, todas con autores nominales y una sola plantilla (autores, título en cursiva, venue, año, DOI/URL, campo `Citada en el informe`). Los 33 tokens `10.\d{4,9}/…` son únicos y pasan el patrón; `https://api.crossref.org/works/<DOI>` devolvió HTTP 200 para los 33 con títulos coincidentes con la ficha, y `https://api.openalex.org/works/doi:<DOI>` devolvió el mismo título en cada caso. Incluye el DOI con punto inicial en el sufijo de `[27]`, `10.54660/.jfmr.2023.4.1.529-538`, que resuelve a «The Ethics of Web Scraping In Research: A Review: Investigating the Boundaries, Legal Implications, and Societal Acceptance of Web Scraping As a Data Collection Method».

Los cuatro identificadores de arXiv también resolvieron y coinciden con la ficha: `2403.03812` (ProbSAINT, enviado el 6/03/2024, con «Journal reference: IEEE BigData 2024 - Industry & Government Track» en la landing page), `1711.06970` («How much is my car worth? A methodology for predicting used cars prices using Random Forest»), `2101.03788` («Second Hand Price Prediction for Tesla Vehicles») y `2601.14311` («Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability in LLMs», prefijo enero 2026, anterior a la fecha del informe, 27/11/2026). Las versiones preprint/publicadas de `[18]` y `[19]` siguen representadas por una ficha cada una; no hay DOI repetido.

— polarity: positive · confidence: high · related: [[#C051]], [[#F-V8-002]]

### F-V8-002 — Los cuatro flags de §71.6 ya reflejan el cuerpo; 5 de 38 en «sí/yes»

E2 de esta iteración (L36, L48, L60, L72 y H2, L112–114) constató que `[9]`, `[14]`, `[26]` y `[29]` conservaban «Citada en el informe: no» pese a que §71.6 (L1518–1520) los nombra. En el archivo vigente, las líneas 24, 34, 58 y 64 de `Data/referencias.md` leen «Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)»; el `mtime` del archivo (28/11/2026 01:05:56 -04:00) es posterior al del artefacto E2 (01:03:37 -04:00). El recuento actual es cinco entradas positivas —`[1]` con `yes` y las cuatro con `sí`— y 33 con `no`, frente a 1/37 en la iteración 2.

La concordancia es con la definición declarada en `Data/referencias.md:6` —«`Citada: sí/no` indica mención nominal en el informe»— y no con una cita numerada: la búsqueda de `[1]`–`[38]` en el texto cacheado devuelve cero marcadores, como consigna E2 iter3 (L87). Cuatro de las cinco menciones nominales se concentran en el único párrafo de §71.6 (L1520); la quinta es Akerlof `[1]`, presente desde antes de esta iteración.

— polarity: positive · confidence: high · related: [[#C051]], [[#F-V8-003]], [[#F-V8-008]]

### F-V8-003 — `[1]` escribe «yes» frente a la convención «sí/no» del propio archivo

La cabecera define «`Citada: sí/no`» (`Data/referencias.md:6`) y las 37 fichas restantes usan `sí` o `no` en español. La entrada `[1]` (L8) es la única que escribe «Citada en el informe: yes.», mientras las cuatro fichas actualizadas en §71.6 escriben «sí (mención nominal en §71.6, sin marcador numérico)». Es una inconsistencia de forma acotada al campo de flag: autores, año, revista, DOI y año de publicación de `[1]` están confirmados en Crossref y OpenAlex (ver F-V8-004).

La marca literal `(metadata incomplete)` aparece solo en `[1]` y `[10]`; `[38]` (L82) registra su limitación en prosa —«Resumen no indexado en OpenAlex; discrepancia de año documentada: 2015 en OpenAlex, 2016 en Crossref (published-print)»— sin la marca. Las dos marcas vigentes son ya por campo: `[1]` «resumen indexado no sustantivo; identidad y DOI verificados en OpenAlex» y `[10]` «resumen no indexado; campos bibliográficos verificados».

— polarity: negative · confidence: high · related: [[#F-V8-002]], [[#F-V8-004]]

### F-V8-004 — Akerlof: contradicción resuelta en §70 ES y en `[1]`, abierta en §70 EN y en C009

La versión española de §70 (L1477) ya nombra el campo: «Akerlof (1970), *The Market for "Lemons"* (DOI 10.2307/1879431 confirmado en OpenAlex; el resumen indexado es solo un índice de secciones, por lo que su flag es `(metadata incomplete: resumen)`)». La ficha `[1]` (L8) coincide: «**(metadata incomplete: resumen indexado no sustantivo; identidad y DOI verificados en OpenAlex)**». La versión inglesa (L1479) conserva en cambio «Akerlof (1970), *The Market for "Lemons"* (Crossref/OpenAlex)» sin la calificación, y el claim C009 de E1 iter3 (L120) reproduce esa frase inglesa como evidencia de «Solo cuatro referencias están verificadas externamente» (L121).

La verificación de esta pasada: `https://api.crossref.org/works/10.2307/1879431` responde HTTP 200 con autor Akerlof, contenedor *The Quarterly Journal of Economics*, volumen 84, número 3, página 488 y `published` 1970-08; el error de transporte de la iteración 2 ya no se reproduce. `https://api.openalex.org/works/W2156109180` devuelve `cited_by_count: 32658` y un `abstract_inverted_index` que contiene solo el índice de secciones («I. Introduction, 488. — II. The model with automobiles as an example, 489. … V. Conclusion, 500.»). Las dos etiquetas —«verificada» y `(metadata incomplete)`— dejan de ser incompatibles cuando el flag alude al resumen y no a la identidad; la mitad inglesa del documento y C009 no registran esa distinción.

— polarity: negative · confidence: high · related: [[#C009]], [[#C051]], [[#F-V8-003]]

### F-V8-005 — Conteos de citas: desfase de dos en Gegić y aumentos de uno en tres fichas del mapa

E2 iter3 reutilizó para las cuatro comparaciones los conteos obtenidos el 27/11/2026: Gegić 188 (L30), Muça 0 (L42), Du 0 (L54) y Vidal Alejandro 1 (L66). La consulta actual a OpenAlex devuelve 190 para `W4288610071` (Gegić, +2), 0 para `W7204683515` (Muça), 0 para `W7225188457` (Du) y 1 para `W4403850866` (Vidal Alejandro). `Data/referencias.md` consigna conteos solo en `[18]` (13), `[19]` (96) y `[20]` (9): los tres se confirman hoy (OpenAlex `W4406461714` 13, `W2770052903` 96 y `arxiv:2101.03788` 9).

Otros desfases respecto del mapa E2 de la pasada 1 son `[10]` 2→3, `[15]` 40→41 y `[27]` 22→23; Akerlof permanece en 32658. Ningún conteo aparece en el documento auditado: la divergencia afecta a los artefactos de auditoría, no a una afirmación del informe. Los conteos son observaciones fechadas y no constantes bibliográficas.

— polarity: neutral · confidence: high · related: [[#C051]], [[#F-V8-002]]

### F-V8-006 — `[31]`: la URL declarada devuelve 404 aunque la obra existe

La entrada `[31]` (L68) declara «http://www.carleton.ca/economics/wp-content/uploads/cep04-12.pdf». Dos clientes independientes devuelven HTTP 404 para esa ruta, incluida la redirección a `https://carleton.ca/economics/wp-content/uploads/cep04-12.pdf` («404 GET https://carleton.ca/economics/wp-content/uploads/cep04-12.pdf»). No es un paper fantasma: `https://api.openalex.org/works/W2188956700` confirma «Cuba's Underground Economy», Ritter, 2004, 20 citas, sin DOI, y registra como ubicaciones alternativas `https://EconPapers.repec.org/RePEc:car:carecp:04-12` y `https://ir.library.carleton.ca/pub/15983`.

— polarity: negative · confidence: high · related: [[#C051]], [[#F-V8-001]]

### F-V8-007 — `[6]` y `[12]`: acceso restringido sin evidencia de error bibliográfico

La URL de `[6]` (L18), `http://aisel.aisnet.org/cgi/viewcontent.cgi?article=1273&context=icis2005`, devuelve HTTP 403 en ambos clientes empleados, respuesta compatible con protección contra automatización. La URL de `[12]` (L30), `https://newyorkfed.org/research/epr/03v09n3/0309hult.pdf`, responde con contenido `application/pdf`; el recurso existe, aunque el texto no se extrajo aquí. Ambas entradas aparecen con autores, título, venue y año en la ficha y fueron cotejadas como fuentes institucionales en el mapa E2 de la pasada 1; en esta pasada no fue posible re-leer su contenido. Se registran como no verificadas en esta pasada, sin marca de paper fantasma.

— polarity: neutral · confidence: medium · related: [[#F-V8-001]]

### F-V8-008 — Las cuatro comparaciones de §71.6 coinciden con el tema de las obras citadas

El párrafo de §71.6 (L1520) describe a Gegić et al. como quienes «predicen precios con machine learning sobre catálogos estructurados», a Muça et al. como quienes «integran datos públicos empresariales albaneses mediante scraping», a Du et al. como quienes «modelan depreciación no lineal y heterogeneidad de marca con evaluación fuera de muestra» y a Vidal Alejandro et al. como quienes «estudian el mercado informal de divisas en Cuba». Los resúmenes de Crossref confirman el núcleo de las tres primeras descripciones —ANN/SVM/Random Forest sobre anuncios de `autopijaca.ba` recogidos con un scraper PHP; integración de registros de contratación pública (APP) y de empresas (QKB) en Albania; 1.000 anuncios, muestra 800/200, término de edad al cuadrado e interacción de marca de lujo con evaluación held-out— y el mapa E2 de la pasada 1 (L342) confirma la cuarta, con el resumen de Crossref vacío para `[29]`. No aparece un marcador `[N]` que vincule estas afirmaciones con las fichas, pero no hay desajuste de contexto entre la descripción y la obra.

Un matiz: «catálogos estructurados» no aparece literalmente en el resumen de Gegić et al., que describe anuncios web recogidos por scraper y atributos examinados; el diferenciador de procedencia y normalización formulado en el propio párrafo sigue describiendo una diferencia real frente al pipeline del informe.

— polarity: positive · confidence: medium · related: [[#F-V8-002]], [[#C051]], [[#P001]], [[#P002]], [[#P003]], [[#P004]]

### F-V8-009 — §70 declara cuatro fuentes verificadas, pero solo una tiene ficha numerada

La lista de §70 (L1477–1479) nombra a Akerlof (1970), DfT/DVLA, ANFAC y AEADE como «referencias citadas y verificadas externamente durante la auditoría». De las cuatro, solo Akerlof tiene entrada en la convención de 38; las tres institucionales figuran en el mapa E2 como fuentes de datos y en el inventario E3 (L156–L158), fuera de `Data/referencias.md`. Ese mismo artefacto (L127) observa que el archivo no lleva etiqueta positiva que distinga a las cuatro. En esta pasada no se re-fetcharon sus páginas: la verificación disponible es la de la iteración 2 a nivel de organismo, con la URL profunda de la colección de estadísticas de vehículos de GOV.UK sin confirmar y la precisión de AEADE como asociación ecuatoriana sin aclarar en §70.

— polarity: neutral · confidence: medium · related: [[#C009]], [[#C051]], [[#F-V8-004]]


## §9 — v9-ethics


## Resumen

- §69 (L1467–L1471) ya satisface `V9.ai_use_declaration.master`: nombra OpenCode/Claude Code con las skills `review`, `deep-research` y `technical-writing`, declara cuatro fases y explica el protocolo de supervisión.
- La calibración cierra F-V9-002 y F-V9-003 de la iteración 2 (herramientas genéricas; generación de código y traducción omitidas); E3 confirma el repositorio versionado que la declaración invoca.
- Sin `v7_ai_density_hint` ni artefacto V7 de esta iteración no se emite hallazgo cruzado de densidad; los demás criterios V9 se registran en nivel master sin incumplimiento exigible.

### F-V9-001 — Declaración de uso de IA completa en §69: herramientas nominales, cuatro fases y protocolo de supervisión

§69 lleva por título «Declaración de uso de inteligencia artificial / AI-use declaration» (L1467). La versión ES declara: «Las herramientas de inteligencia artificial (OpenCode/Claude Code con las skills `review` de MatCom, `deep-research` y `technical-writing`) se utilizaron en cuatro fases: investigación y verificación de fuentes, redacción y edición de la narrativa, generación y revisión de código, y traducción bilingüe» (L1469). La versión EN reproduce la declaración: «AI tools (OpenCode/Claude Code with MatCom's `review` skill, `deep-research` and `technical-writing`) were used in four phases: research and source verification, drafting and editing, code generation and review, and bilingual translation» (L1471). El protocolo de supervisión se explicita en el mismo párrafo: «contrastar toda cifra contra los CSV y bases versionados, ejecutar las pruebas automatizadas y conservar el registro de auditoría en `reviews/`; ninguna salida de IA se aceptó sin ese contraste» (L1469), con equivalente en L1471. La procedencia se refuerza: «Las cifras, los modelos estadísticos y las decisiones de diseño provienen de los datos y del código versionados en este repositorio; ninguna afirmación empírica se originó en una salida de IA sin contraste contra los archivos» (L1469). El criterio `V9.ai_use_declaration.master` exige: «Declaration expected; should name tools, phases (research, drafting, code generation, translation), and supervision protocol». Aquí concurren los tres elementos: herramientas nominales, las cuatro fases del criterio y un protocolo con criterio de aceptación verificable. La firma de cierre (L1522), «responsable del proyecto / project owner», atribuye la declaración. Este hallazgo sustituye la calibración de la iteración 2, donde F-V9-002 señalaba herramientas genéricas y F-V9-003 omitía código y traducción (`reviews/informe-tecnico-2026-11-27-iter2.v9-ethics.md`).

— polarity: positive · confidence: high · related: [[#F-V9-002]] · criteria: V9.ai_use_declaration.master

### F-V9-002 — Las cuatro fases declaradas corresponden a evidencia interna del documento y a la infraestructura de E3

La fase de generación y revisión de código (L1469/L1471) corresponde a las herramientas creadas que enumera §6: «`ddg_research.py`, `buscar_fallback.py`, `descargar_hombros.py`, `scrape_concesionarios.py`, `resumen_catalogos.py` y `actualizar_informe.py`» (L74), al scraper con adaptadores por dominio de §8 (L90) y al comando único y semilla de §71.5 (L1516). La investigación y verificación de fuentes corresponde a §5 (L62, 409 resultados) y §7 (L78–L86), y la traducción bilingüe a las dos versiones ES/EN de cada sección, incluidas las de §69 (L1469, L1471). E3 registra `repo_url: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba`, `repo_clone_status: success` y último commit `ee994cd` (`reviews/informe-tecnico-2026-11-27-iter3.e3-artifacts.md`, L6–L23), coherente con la procedencia «versionados en este repositorio» y con el registro de auditoría bajo `reviews/` invocado en L1469. No se recibió `v7_ai_density_hint`: no hay sección marcada con densidad `high` pendiente de cobertura, por lo que no se emite hallazgo cruzado con V7.

— polarity: positive · confidence: high · related: [[#F-V9-001]] · criteria: V9.ai_use_declaration.master

### F-V9-003 — Protección de datos personales declarada como requerimiento; sin sujetos humanos ni comité de ética aplicables

El documento registra la restricción en forma explícita: «antes de publicar resultados deben verificarse las normas cubanas vigentes y aplicar solo datos agregados, sin nombres, teléfonos ni información personal de anunciantes» (L119; equivalente EN en L250), y la reitera para fuentes sociales: «No verificables como fuente estadística; requieren consentimiento y sin datos personales» (L827) y «sin datos personales» (L851, L855). La búsqueda de «IRB», «comité de ética» y «ethics committee» no devuelve coincidencias; el criterio `V9.data_ethics.master` condiciona consentimiento y aprobación a que sean aplicables. El corpus son anuncios públicos de compraventa y series agregadas, no sujetos humanos reclutados, por lo que no se observa incumplimiento exigible en este nivel, aunque el documento no describe un procedimiento de anonimización ejecutado más allá de la exclusión declarada de datos personales.

— polarity: neutral · confidence: high · related: [] · criteria: V9.data_ethics.master

### F-V9-004 — Conflicto de intereses: ausencia registrada, no requerida en nivel master

Búsqueda de «conflicto de intereses», «conflicts of interest», «sponsor», «financiación» y «funding» en el documento: sin declaración formal. La única coincidencia de «conflicto» es narrativa —«relato en 10 actos con personajes, conflicto, hallazgos» (L1130)—. El criterio `V9.coi_statement.master` indica «Not required; tutor/advisor relationship implicit», por lo que la ausencia no constituye hallazgo negativo; se registra solo para completar el barrido de declaraciones.

— polarity: neutral · confidence: high · related: [] · criteria: V9.coi_statement.master

### F-V9-005 — Impacto / doble uso: tema no sensible en el sentido del criterio, con salvedad de datos personales y copyright

El objeto del informe (precios de automóviles en Cuba, conversiones y análisis estadístico) no figura entre los temas sensibles enumerados en `V9.dual_use` (LLMs, vigilancia, biosecuridad, armas autónomas, diagnóstico clínico). En nivel master la discusión se «encourage[d]», y el documento registra la salvedad de «Protección de datos personales, ciberseguridad y derechos de autor» (L119/L250) además de las amenazas a la validez de §71.4 (L1507–L1512). No hay declaración formal de impacto social; no es exigible en este nivel.

— polarity: neutral · confidence: high · related: [] · criteria: V9.dual_use.master

### F-V9-006 — Disponibilidad de datos y código: ubicaciones versionadas documentadas, sin licencia ni commit fijados en el informe

Para `V9.data_availability_statement.master` («Brief statement: where the data lives, how to obtain»), el documento cumple en lo esencial: §56 documenta el árbol versionado en `Data/estructura_github.md` (1.288 archivos, 157 objetos LFS; L1353), §68 remite a `Data/ESTRUCTURA_ESPACIO.md` (L1459) y E3 inventaria las bases en `Data/Revolico/revolico.sqlite`, `Data/analisis_rentabilidad/data/compacto/` y `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` (L148–L154). Para `V9.code_availability_statement.master` («"Code available at" statement with URL and brief description»), §40 consigna el renombre a `el-precio-de-moverse-en-cuba` (L1138–L1145) y E3 da la URL completa y el commit `ee994cd`, pero el informe no imprime la URL ni fija commit/DOI en una sección formal de disponibilidad. Licencia de datos/código no declarada. Se trata de una precisión deseable, no de un incumplimiento del nivel master.

— polarity: neutral · confidence: medium · related: [[#F-V9-001]] · criteria: V9.data_availability_statement.master, V9.code_availability_statement.master



## §10 — Observaciones transversales

*Nota de numeración: los IDs `F-V10-001`…`005` de esta pasada se numeran desde cero, como en la iteración 2; los estados `F-V10-001`…`008` citados por E1 y por el artefacto V4 pertenecen a la pasada 1.*

### F-V10-001 — La declaración de §69 queda completa en forma y sigue concentrando los dispositivos de superficie

V9 cierra las dos calibraciones pendientes de la iteración 2: §69 nombra «OpenCode/Claude Code con las skills `review` de MatCom, `deep-research` y `technical-writing`» y declara «cuatro fases: investigación y verificación de fuentes, redacción y edición de la narrativa, generación y revisión de código, y traducción bilingüe» (L1469, L1471), con tres pasos de supervisión y firma de cierre (L1522). V7 constata que ese mismo bloque, ahora de 271 palabras, conserva densidad `medium` por dos triadas de cola larga —«Las cifras, los modelos estadísticos y las decisiones de diseño»—, doce metaconceptos (44,3/1.000 palabras) y el cierre Don't 8, aunque los tres adjetivos sin ancla desaparecieron y el único hedging del corpus sigue siendo «bibliotecas quizá innecesarias» (L1459). La huella que la propia declaración invoca —«sus resultados se conservan en `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` junto con los trece artefactos de fase» (L1469)— designa los artefactos de la iteración 1, no los de esta. Las fases de generación de código y traducción, ahora nominalmente declaradas, corresponden a los seis scripts de §6 (L74), a la semilla de §71.5 (L1516) y a las dos versiones de cada sección (F-V9-002). Declaración, densidad y apuntador a artefactos no se reparten entre secciones: coinciden en el mismo párrafo.

— polarity: neutral · confidence: high · related: [[#F-V7-001]], [[#F-V7-003]], [[#F-V7-008]], [[#F-V9-001]], [[#F-V9-002]] · criteria: V9.ai_use_declaration.master

### F-V10-002 — Tres lecturas del mismo objeto: la caché, el espejo inglés y los CSV con un marcador que no se reescribe

§59 (L1379) fija «772 autos únicos», «2.029 anuncios limpios» (1.338 locales) y «43.000 km» y afirma que «los valores se actualizan solos en `outputs/tables/kpis.csv`»; el espejo inglés (L1383) escribe «744 unique cars, 2,014 clean listings» y `kpis.csv` registra 2.156/1.465/33.256, con el relato generado llevando los marcadores resueltos (F-V3-001, F-V3-002, F-V3-003). En paralelo, §59 da R² 0,277 para el modelo de 28 observaciones, §71.2 da 0,274 y `modelo_muestra.csv` da 0,2744; el marcador `<!-- kpi:modelo_r2_completo -->` no se reescribe porque la expresión regular de `actualizar_numeros.py:35` admite solo letras y guion bajo en la clave (F-V3-004). V2 registra que §71 no identifica ambos ajustes como especificaciones separadas (F-V2-007), que la ablación de `hp`, aunque etiquetada y cuantificada, informa juntos el cambio de especificación y el de muestra (F-V2-002), y que §71.5 declara protocolo con semilla y código (F-V2-006). V1 constata la numeración duplicada que hace de «§59» un destino ambiguo según la parte (F-V1-003). La declaración de autoactualización, la coherencia entre secciones y la resolución efectiva del marcador describen tres estados distintos del mismo objeto.

— polarity: negative · confidence: high · related: [[#F-V1-003]], [[#F-V2-002]], [[#F-V2-006]], [[#F-V2-007]], [[#F-V3-001]], [[#F-V3-002]], [[#F-V3-004]] · criteria: V2.reproducibility_protocol.master

### F-V10-003 — Cuatro vecinos nombrados, fichas alineadas y un párrafo sin marcadores: la novedad se juega en el aparato, no en el argumento

§71.6 (L1520) sustituye el contraste por escala contra el repositorio egipcio por cuatro cláusulas «Frente a…» y cierra la diferenciación exigida por `V4.differentiation_from_prior_art.master` (F-V4-001); V5 contabiliza cinco menciones nominales sobre 38 entradas y tres de ellas de 2024–2026 (F-V5-001, F-V5-002, F-V5-003), y V8 confirma por Crossref que las descripciones coinciden con el tema de las obras (F-V8-008). Los tres evaluadores coinciden en el mismo límite: cero marcadores `[N]` en el cuerpo, un solo párrafo para las cuatro comparaciones y caracterizaciones de una frase sin resultados ni limitaciones (F-V4-002, F-V5-004); §70 (L1477) sigue enumerando solo cuatro fuentes verificadas. Las fichas [9], [14], [26] y [29] se actualizaron en disco a «Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)» después de que E2 las registrara como desactualizadas (F-V4-004, F-V5-006, F-V8-002): el campo ya coincide con el cuerpo, pero la convención numerada sigue sin enlazarse a él. El posicionamiento se acumula en un apartado de cumplimiento al final del documento: las secciones analíticas §17–§20, §34 y §59–§60 no incorporan a estos cuatro trabajos (F-V5-002).

— polarity: neutral · confidence: high · related: [[#F-V4-001]], [[#F-V4-002]], [[#F-V4-004]], [[#F-V5-001]], [[#F-V5-002]], [[#F-V5-003]], [[#F-V5-004]], [[#F-V5-006]], [[#F-V8-002]] · criteria: V4.prior_art_engagement.master

### F-V10-004 — Reproducibilidad declarada en §71.5 y entorno ejecutado en §34: dos series de dependencias y una semilla sin consumir

§71.5 (L1516) declara comando único, `SEED = 20261127`, dependencias fijadas a serie menor y prueba de humo; V6 verifica esos extremos en `run_all.py:16–18`, `requirements.txt` (doce dependencias `~=X.Y.0`) y `test_smoke_pipeline.py` (4/4) (F-V6-004, F-V6-006, F-V6-008, F-V6-009), y V2 califica el protocolo como cubierto y por encima del mínimo de nivel (F-V2-006). Dos desajustes comparten el mismo bloque: §34 (L1039) consigna «statsmodels 0.15, pyarrow 26» frente a `statsmodels~=0.14.0` y `pyarrow~=14.0.0` (F-V6-005), y `run_all.py:29–35` lanza las cinco etapas con `subprocess.run` sin propagar `SEED`, de modo que la semilla opera como marca documental (F-V6-007). Bajo `V2.reproducibility_protocol.master` —«Protocol fully described + seeds mentioned + code referenced»— la declaración se satisface; las versiones efectivamente invocadas y el consumo de la semilla quedan del lado del repositorio, y las huellas de mapeo del apéndice visual y del panel vigente no figuran en el texto cacheado (F-V6-002, F-V6-003).

— polarity: neutral · confidence: high · related: [[#F-V2-006]], [[#F-V6-002]], [[#F-V6-003]], [[#F-V6-004]], [[#F-V6-005]], [[#F-V6-006]], [[#F-V6-007]], [[#F-V6-008]] · criteria: V2.reproducibility_protocol.master

### F-V10-005 — Estándares master concentrados en una sección añadida al final, sin resumen, hipótesis ni contribuciones

La sección nueva §71 (L1485–L1520, 606 palabras) reúne los cinco apartados de cumplimiento —bases, ablación, pruebas, amenazas y reproducción— más el posicionamiento de 71.6; V7 la describe como enumerativa y anclada, con densidad `low` en 71.1–71.5 y `medium` en 71.6 (F-V7-004, F-V7-005, F-V7-009). V1 constata que entre los 96 encabezados no figuran «Resumen» ni «Abstract», que no aparece la cadena «hipótesis» en ningún punto del texto y que la contribución queda en las cinco conclusiones de §12 y en un párrafo de 71.6 —«la contribución es de procedencia y normalización, no de algoritmo»—, sin sección de contribuciones (F-V1-001); la numeración 1–12 duplicada y el salto de nivel de §13 (F-V1-003) hacen que los apuntadores a estándares convivan con dos destinos posibles para §1–§12. V2 localiza en 71.1 el único intento de base comparable —una mediana ingenua y un contraste cualitativo— (F-V2-001), y V5 ubica las cinco menciones nominales en §71.6, fuera de las secciones analíticas (F-V5-001, F-V5-002). La cobertura de nivel master se acumula en el cierre del texto y no modifica la arquitectura de resumen, hipótesis o contribuciones.

— polarity: neutral · confidence: high · related: [[#F-V1-001]], [[#F-V1-003]], [[#F-V2-001]], [[#F-V5-001]], [[#F-V5-002]], [[#F-V7-004]], [[#F-V7-005]], [[#F-V7-009]] · criteria: V2.baselines.master

### Lista explícita de lo que permanece por debajo del criterio master

**V1 — Estructura**
- **F-V1-001** — No aparece «hipótesis»/«hypothesis»; sin resumen VSN-C ni sección de contribuciones.
- **F-V1-002** — Fila 8 de la tabla de fases: «Análisis de mercado, comparables y rentabilidad» (ES) vs «Analysis, profitability model and interactive product» (EN), nombre retirado por §21.
- **F-V1-003** — Dos secciones «1.» y dos «12. Conclusiones»; §13 usa nivel 1 y persisten cuatro marcadores de plantilla.

**V2 — Metodología**
- **F-V2-001** — Segunda base es contraste cualitativo sin métrica calculada sobre datos propios.
- **F-V2-003** — Dos contrastes comparativos sin test de diferencia ni intervalo de confianza.
- **F-V2-004** — 8 fuentes/instancias, por debajo de 10; modelo completo con 28 observaciones sin coeficiente p<0,05.
- **F-V2-007** — §71 no identifica ambos ajustes como especificaciones separadas ni explica 0,277 vs 0,2744.

**V3 — Resultados frente a evidencia**
- **F-V3-001** — 772/744 y 2.029/2.014 son cantidades distintas para la misma corrida «vigente del 27/11/2026» (ES/EN).
- **F-V3-002** — Total y componente local difieren en 127 anuncios frente a `kpis.csv`; tres números escritos a mano, sin marcador.
- **F-V3-003** — `km_medianos=33256.0`, `benchmark.csv` 113 filas y `anomalias.csv` 89, no 101 ni 81.
- **F-V3-004** — 0,277 no es el redondeo de 0,2744 (es 0,274); el marcador con dígito en la clave no es reconocido por el actualizador.
- **F-V3-005** — 0,165 fijo en `MODELOS_Y_FUNCIONES.md`; p mínimo no intercepto real 0,0941.
- **F-V3-006** — VIF real 1,12–1,40 frente a «1,13–1,58».
- **F-V3-007** — `tests.csv` tiene una fila con p 0,0; ningún CSV contiene 1e−05.
- **F-V3-008** — MAE 18.220,46 sin evidencia en `outputs/tables/` ni en scripts.
- **F-V3-010** — Cifra 981 y atribución a ocho marketplaces no cotejables con el archivo invocado.

**V4 — Novedad**
- **F-V4-002** — §71.6 sin marcadores numéricos, cifras de los trabajos ajenos ni discusión de resultados/limitaciones.
- **F-V4-004** — Cero marcadores `[N]` en el cuerpo.
- **F-V4-005** — `queries_run: 0`, `papers_l3: 0`; sin novedad confirmada.

**V5 — Estado del arte**
- **F-V5-001** — Cinco menciones nominales de 38 (13,2 %), lejos del tramo 25–60.
- **F-V5-003** — Cuatro comparaciones en un solo párrafo, sin marcadores `[14]`, `[26]`, `[9]`, `[29]`.
- **F-V5-004** — Diez de 16 afirmaciones load-bearing sin cita externa; 0 marcadores `[N]`.
- **F-V5-005** — 21 de 23 obras del top-5 por clúster ausentes (91,3 %).

**V6 — Reproducibilidad**
- **F-V6-002** — Caché sin los cinco cuadros ni seis gráficos del apéndice.
- **F-V6-003** — Ningún pasaje nombra la ruta `Data/dashboard.html`.
- **F-V6-005** — §34 (statsmodels 0.15, pyarrow 26) vs `requirements.txt` (0.14.0, 14.0.0).
- **F-V6-007** — `SEED` no se propaga por `subprocess.run`; las cinco etapas no declaran semilla propia.
- **F-V6-010** — Bases SQLite con accesibilidad `unknown`, sin URL/DOI ni disponibilidad declarada.

**V7 — Escritura y patrones de IA**
- **F-V7-001** — Huella citada apunta a los artefactos de la iteración 1.
- **F-V7-003** — Dos triadas de cola larga en §69 (271 palabras).
- **F-V7-004/005** — §71.6 concentra densidad media: cuatro «Frente a…» y cuatro cierres contrastivos.
- **F-V7-006** — §17–21 y §59–63 permanecen en densidad alta.
- **F-V7-007** — §71.3–71.6 sin paralelo inglés.
- **F-V7-008** — Don't 8 persiste en §69.

**V8 — Bibliografía**
- **F-V8-003** — `[1]` escribe «yes» frente a la convención `sí/no`.
- **F-V8-004** — Contradicción Akerlof abierta en el espejo EN.
- **F-V8-005** — Conteo Gegić 188→190 desactualizado en artefactos.
- **F-V8-006/007** — `[31]` HTTP 404 y `[6]` HTTP 403; contenido no verificado.
- **F-V8-009** — DfT/DVLA, ANFAC y AEADE fuera de `Data/referencias.md`.

**V9 — Ética y declaraciones**
- **F-V9-003** — Sin procedimiento de anonimización ejecutado declarado (no exigible sin sujetos reclutados).
- **F-V9-006** — Sin URL formal, commit/DOI ni licencia de datos/código declarada.

*Quedan fuera los hallazgos de polaridad positiva —F-V2-002, F-V2-005, F-V2-006, F-V3-009, F-V4-001, F-V4-003, F-V5-002, F-V5-006, F-V6-001, F-V6-004, F-V6-006, F-V6-008, F-V6-009, F-V7-002, F-V7-009, F-V8-001, F-V8-002, F-V8-008, F-V9-001, F-V9-002— por registrar criterio cubierto o superado, y F-V9-004/005 por no ser exigibles en nivel master.*

## Apéndice A — Plan

# Plan de auditoría — Iteración 3

Tercera pasada sobre `INFORME_TECNICO.md` (1.523 líneas) tras la sección 71
de estándares master, la semilla declarada, las dependencias fijadas, la
prueba de humo y la bibliografía con flags por campo.

Objetivo declarado por el usuario: entregar una lista de todo lo que sigue
por debajo de lo aceptable. Se re-ejecutan E1–E3 y V1–V9 y se calibran los
hallazgos contra `level-criteria.md` (nivel master).


## Apéndice B — Claims

# Claim Inventory

## Summary
- Total: 126
- Load-bearing: 16 · Supporting: 45 · Contextual: 65
- By type: result 62 · methodological 48 · novelty 2 · contextual 45 · definitional 6 · citation-grounded 12

## Load-bearing claims

### C001 — Objetivo vigente: análisis de mercado, recomendador diferido

- **Section**: §1 Objetivo (L16); §21 Cambio de objetivo (L881–886); Parte II §1 (L147)
- **Lines**: 16–18
- **Types**: definitional, contextual
- **Excerpt**: «Su objetivo actual es realizar un **análisis del mercado automotor cubano**: caracterizar estructura, precios, oferta, segmentos, tendencias, asequibilidad y condiciones de rentabilidad.»
- **Restated**: El objetivo declarado es el análisis del mercado automotor cubano y no la recomendación interactiva, que queda diferida a una especialización futura.
- **Internal evidence cited**: §21 (L881–886), §20 (L863, L870), Parte II §12 (L270, en sentido opuesto)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: la conclusión 5 de la Parte II (L270) sigue afirmando que el modelo y el producto interactivo «are not implemented yet», en contradicción con §12 español (L139).

### C002 — Fase 8 implementada y regenerada automáticamente

- **Section**: §12 Conclusiones (L139); §2 nota de actualización (L38); §34 (L1016–1037)
- **Lines**: 139
- **Types**: result, methodological
- **Excerpt**: «El análisis de mercado y el modelo de rentabilidad (fase 8) están implementados en `Data/analisis_rentabilidad/` y se regeneran de forma automática; la definición del producto interactivo se difiere a una especialización futura.»
- **Restated**: El pipeline de análisis y rentabilidad existe en `Data/analisis_rentabilidad/` y puede regenerarse automáticamente.
- **Internal evidence cited**: §34 (L1018–1037), §38 (L1112), §59–§60 (L1377–1391)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: cierra la contradicción principal de la iteración 1 en la Parte I; permanece en la Parte II (L164, L270).

### C003 — Cifras canónicas de la corrida vigente

- **Section**: §59 Storytelling alineado con los datos finales (L1379–1381)
- **Lines**: 1379
- **Types**: result
- **Excerpt**: «**772 autos únicos**, **2.029 anuncios limpios** (1.338 locales y 691 de importación), mediana local de **21.000 USD**, kilometraje mediano de **43.000 km**, 50 marcas, 101 grupos comparables y 81 anomalías»
- **Restated**: La corrida vigente del 27/11/2026 produce 772 autos únicos, 2.029 anuncios limpios, mediana local de 21.000 USD y 43.000 km, 50 marcas, 101 grupos y 81 anomalías.
- **Internal evidence cited**: §59 (L1379, `outputs/tables/kpis.csv` con marcadores automáticos en L1381), §58 (L1371, estado anterior)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: §45 (L1214) conserva 23.000 USD, 6,3 años, 34 marcas y 27 grupos; §58 (L1371) conserva 2.014 anuncios y 44.125 km; el paralelo inglés de §59 (L1383) declara 744 autos y 2.014 anuncios.

### C004 — Modelo vigente sin pendiente anual significativa ni prima premium

- **Section**: §59 (L1381); §60 (L1389); §44 (L1206)
- **Lines**: 1381
- **Types**: result, methodological
- **Excerpt**: «La depreciación se reformuló con honestidad: el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra.»
- **Restated**: En la corrida vigente el coeficiente de edad del modelo hedónico no es significativo tras controlar por kilometraje.
- **Internal evidence cited**: §60 (L1389: p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05), §44 (L1206), §71.4 (L1512)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: retirada declarada del −5,43 % de §34; sin ablación ni test pareado entre corridas hasta §71.2 (L1499).

### C005 — Muestra del modelo completo: 28 observaciones de 981 candidatas

- **Section**: §59 (L1381)
- **Lines**: 1381
- **Types**: result
- **Excerpt**: «**<!-- kpi:modelo_n_completo -->28 observaciones completas** de <!-- kpi:modelo_candidatas -->981 candidatas (R² = <!-- kpi:modelo_r2_completo -->0,277; p del F = <!-- kpi:modelo_pf_completo -->0,411)»
- **Restated**: La estimación completa usa 28 observaciones, con R² 0,277 y p del estadístico F 0,411, y la limitación está documentada.
- **Internal evidence cited**: §60 (L1389), `MODELOS_Y_FUNCIONES.md` (mencionado en L1381), §71.2 (L1499)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: §71.1–71.2 (L1493, L1499) reportan un «modelo principal» distinto con 584 observaciones y R² 0,101; el texto no identifica explícitamente ambos como especificaciones separadas.

### C006 — Primera ejecución: depreciación −5,43 % anual (p<0,001)

- **Section**: §34 Línea base real de la primera ejecución (L1041–1056)
- **Lines**: 1056
- **Types**: result
- **Excerpt**: «El modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` da una depreciación media de **−5,43 % anual** (p<0,001), con primas de +21 % para premium y −22 % para tier medio frente al desconocido.»
- **Restated**: La primera corrida estimó −5,43 % anual de depreciación, +21 % de prima premium y −22 % para el tier medio.
- **Internal evidence cited**: §34 tabla «Línea base real de la primera ejecución» (L1043–1054)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: cifra retirada en §59–§60 pero reutilizada en §44 (L1206, con salvedad) y §45 (L1214, sin salvedad).

### C007 — Procedencia: anuncios como precios pedidos, no transaccionados

- **Section**: §18 Auditoría de procedencia (L826, L831–833)
- **Lines**: 831
- **Types**: methodological, definitional
- **Excerpt**: «los anuncios y redes son la **señal de precio** pero no sustituyen estadísticas oficiales. El análisis debe etiquetar cada métrica con su procedencia y nivel de confianza, y no mezclar tasas oficiales e informales ni precios anunciados con precios de transacción.»
- **Restated**: El análisis trata los anuncios como señal de precio pedido y prohíbe mezclar tasas oficiales con informales.
- **Internal evidence cited**: §18 tabla de procedencia (L816–829), §19 (L850, L855), §20 (L864), §71.4 (L1509)
- **External evidence cited**: DfT/DVLA y ANFAC/AEADE, verificados en vivo según §18 (L818, L822–823) y §70 (L1477)
- **Novelty signals**: ninguno.
- **Notes**: —

### C008 — Declaración de uso de inteligencia artificial

- **Section**: §69 Declaración de uso de inteligencia artificial (L1467–1471)
- **Lines**: 1469–1471
- **Types**: methodological
- **Excerpt**: «Las cifras, los modelos estadísticos y las decisiones de diseño provienen de los datos y del código versionados en este repositorio; ninguna afirmación empírica se originó en una salida de IA sin contraste contra los archivos.»
- **Restated**: Toda afirmación empírica del informe fue contrastada contra archivos versionados y la auditoría con la skill `review` quedó registrada.
- **Internal evidence cited**: §69 (L1469–1471), `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` y trece artefactos de fase
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: cierra la ausencia de declaración de la iteración 1; nombra skills y fase pero no detalla herramientas ni umbrales de supervisión.

### C009 — Referencias verificadas y estado del resto del aparato

- **Section**: §70 Referencias verificadas (L1475–1479)
- **Lines**: 1477–1479
- **Types**: citation-grounded
- **Excerpt**: «Akerlof (1970), *The Market for "Lemons"* (Crossref/OpenAlex); UK Department for Transport / DVLA vehicle statistics (GOV.UK); ANFAC Spanish automotive reports (official site); AEADE registration statistics (official site).»
- **Restated**: Solo cuatro referencias están verificadas externamente; las restantes figuran como `(metadata incomplete)` y la convención numerada reúne 38 entradas.
- **Internal evidence cited**: §70 (L1477–1479), `Data/referencias.md`, `reviews/informe-tecnico-2026-11-27.e2-literature.md`
- **External evidence cited**: Crossref, OpenAlex, GOV.UK, sitios oficiales de ANFAC y AEADE (según declara L1477)
- **Novelty signals**: ninguno.
- **Notes**: atiende parcialmente la ausencia de aparato crítico; el cuerpo del informe sigue sin citas numeradas.

### C010 — Conversión TRMI: serie diaria referencial, 930 fijo en el modelo

- **Section**: §23 Conversión elTOQUE (L902); §52 (L1297); Parte II §23 (L907)
- **Lines**: 902
- **Types**: methodological
- **Excerpt**: «**Aclaración vigente:** el pipeline de `Data/analisis_rentabilidad/` usa la TRMI fija de 930 CUP/USD del 18/11/2026 (`config.py`); la serie diaria es referencia histórica, no insumo del modelo actual.»
- **Restated**: La conversión del modelo usa 930 CUP/USD fijos y la serie diaria de elTOQUE no alimenta la estimación vigente.
- **Internal evidence cited**: §23 (L902), §52 (L1297), `config.py` (mencionado en L902)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: aclara la dualidad 920/930 en español; L904 mantiene el 920 histórico y L907 (inglés) sigue describiendo conversión diaria.

### C011 — Arquitectura del esqueleto inspirada en Egyptian-Used-Cars

- **Section**: §34 (L1018–1039)
- **Lines**: 1018
- **Types**: methodological, novelty
- **Excerpt**: «Creé `Data/analisis_rentabilidad/` siguiendo la arquitectura del repositorio **Egyptian-Used-Cars** (ingesta → limpieza → EDA → estadística → benchmark), pero adaptada a nuestras fuentes y preparada para crecer:»
- **Restated**: La arquitectura del pipeline de rentabilidad deriva de Egyptian-Used-Cars y fue adaptada a las fuentes cubanas.
- **Internal evidence cited**: §34 (L1018–1039), §60 (L1387–1390)
- **External evidence cited**: repositorio `Egyptian-Used-Cars` (fuente de ingeniería, sin ficha académica en el documento)
- **Novelty signals**: «Creé» (L1018), «adaptada a nuestras fuentes» (L1018), «preparada para crecer» (L1018).
- **Notes**: diferenciación declarada por arquitectura, ampliada en §71.6 (L1520) por procedencia y normalización.

### C012 — Brecha frente a Egipto

- **Section**: §34 Brecha frente a Egipto (L1058–1060)
- **Lines**: 1060
- **Types**: result, contextual
- **Excerpt**: «Egipto tiene 23.500 anuncios, historial mensual de precios, HP y kilometraje estructurados, ANOVA/OLS/VIF, Tableau y Power BI. Nosotros tenemos el pipeline y las técnicas cubiertas, pero solo 497 usados, un único snapshot, HP/kilometraje mayormente ausentes y un solo benchmark de auto nuevo.»
- **Restated**: Frente a 23.500 anuncios del repositorio egipcio, el proyecto dispone de 497 usados, una sola instantánea y campos mayormente ausentes.
- **Internal evidence cited**: §34 tabla de la primera ejecución (L1045–1054), `NECESIDADES.md`, §71.1 (L1492)
- **External evidence cited**: repositorio `Egyptian-Used-Cars` (sin verificación académica en el documento)
- **Novelty signals**: ninguno.
- **Notes**: diferenciación por escala y cobertura, no por método.

### C013 — Límites declarados del marco analítico

- **Section**: §19 Adaptación a Cuba / La Habana (L848–855)
- **Lines**: 855
- **Types**: definitional, methodological
- **Excerpt**: «- **Límites**: precios pedidos no transaccionados, sesgo de supervivencia de anuncios, sin datos personales, vigencia normativa a verificar.»
- **Restated**: El análisis declara como límites los precios pedidos, el sesgo de supervivencia, la ausencia de datos personales y la vigencia normativa pendiente.
- **Internal evidence cited**: §19 (L850–855), §18 (L831), §20 (L871), §71.4 (L1509–1512)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: —

### C014 — Bases de comparación y métricas observadas

- **Section**: §71.1 Bases de comparación / Baselines (L1487–1495)
- **Lines**: 1491–1493
- **Types**: result, methodological
- **Excerpt**: «| Mediana global ( ingenua ) | Predice la mediana de los usados locales | MAE 18.220,46 USD sobre 1.444 anuncios |» / «| Modelo principal propio | OLS de log-precio con antigüedad, km, condición y tier | R² 0,101 sobre 584 observaciones |»
- **Restated**: La línea base ingenua alcanza MAE 18.220,46 USD sobre 1.444 anuncios y el modelo principal propio reporta R² 0,101 sobre 584 observaciones.
- **Internal evidence cited**: §71.1 tabla (L1489–1493), §71.2 (L1499), §59 (L1381)
- **External evidence cited**: Egyptian-Used-Cars como referencia de ingeniería (L1492), sin ficha académica en el documento
- **Novelty signals**: «Modelo principal propio» (L1493).
- **Notes**: sección incorporada en esta iteración; el R² 0,101 / 584 observaciones convive con el R² 0,277 / 28 observaciones de §59 (L1381).

### C015 — Ablación del término `hp` y atribución del signo de antigüedad

- **Section**: §71.2 Ablación explícita / Explicit ablation (L1497–1501)
- **Lines**: 1499
- **Types**: result, methodological
- **Excerpt**: «`modelo_muestra.csv` documenta la ablación del término `hp`: al retirarlo, la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² baja de 0,274 a 0,101. El cambio de especificación y el cambio de muestra se informan juntos. La pendiente positiva de antigüedad en el modelo principal se atribuye a la selección de anuncios con kilometraje declarado y no se interpreta como una tasa de depreciación.»
- **Restated**: Retirar `hp` eleva la muestra de 28 a 584 observaciones y reduce el R² de 0,274 a 0,101, y el signo positivo de antigüedad se atribuye a selección muestral, no a depreciación.
- **Internal evidence cited**: §71.2 (L1499), `modelo_muestra.csv`, §71.1 (L1493), §59 (L1381)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: primera ablación declarada en el documento; satisface parcialmente la retirada del −5,43 % de §34 (L1056) señalada en la iteración 2.

### C016 — Posicionamiento argumentativo frente a cuatro trabajos cercanos

- **Section**: §71.6 Posicionamiento frente a trabajos cercanos / Positioning against prior work (L1518–1520)
- **Lines**: 1520
- **Types**: novelty, citation-grounded, contextual
- **Excerpt**: «Frente a Gegić, Isaković, Keco, Mašetić y Kevrić (2019), que predicen precios con machine learning sobre catálogos estructurados, este trabajo parte de anuncios en lenguaje libre y construye las variables por análisis del texto: la contribución es de procedencia y normalización, no de algoritmo.»
- **Restated**: La contribución declarada frente a cuatro trabajos previos es de procedencia y normalización de anuncios en lenguaje libre, no de algoritmo predictivo ni de tasa de depreciación.
- **Internal evidence cited**: §71.6 (L1520), §70 (L1475–1479), §18 (L816–829)
- **External evidence cited**: Gegić, Isaković, Keco, Mašetić y Kevrić (2019); Muça, Bani y Alla (2026); Du, Yang, Zhang, Li y Liu (2026); Vidal Alejandro, Muñiz-Cuza y Calas Torres (2024) — citados en L1520, sin fichas verificadas en el documento
- **Novelty signals**: «este trabajo parte de anuncios en lenguaje libre» (L1520), «la contribución es de procedencia y normalización, no de algoritmo» (L1520), «este trabajo no estima una tasa anual» (L1520).
- **Notes**: amplía el único contraste previo (§34, Egipto) a cuatro pares académicos; las fichas de verificación se remiten a `Data/referencias.md` (§70, L1477).

## Supporting claims (45)

### C017 — Fase 6: 11 bases y 256 filas
- **Section**, **Lines**: §9 (L94–110), 94–108
- **Types**: result
- **Excerpt**: «Se prepararon 11 bases y se obtuvieron **256 filas**:»
- **Restated**: La fase 6 produjo 256 filas distribuidas en 11 tiendas.
- **Internal/External evidence**: tabla de tiendas (L96–108); sin citas numeradas.
- **Notes**: las once filas suman 256 (AGN 60, ATR 6, BDC 19, Changan 2, Chinautos 70, ConnectingCuba 1, Dongfeng 45, Envision 1, Finauto 45, MCV 4, Subasta 3).

### C018 — Fuentes excluidas por bloqueo técnico
- **Section**, **Lines**: §9 (L110), 110
- **Types**: result, contextual
- **Excerpt**: «Excluidas por bloqueo técnico: carrosw (HTTP 403 con Bot Verification), LlamaCuba (timeout) y SASA/DIVEP (sin catálogo).»
- **Restated**: Tres fuentes quedaron fuera de la captura por 403, timeout o ausencia de catálogo.
- **Internal/External evidence**: §9 (L110), §11 (L129); sin citas numeradas.
- **Notes**: —

### C019 — Descubrimiento: 409 resultados, 400 únicos
- **Section**, **Lines**: §5 (L62), 62
- **Types**: result
- **Excerpt**: «Se consolidaron **409 resultados, 400 únicos**.»
- **Restated**: La consolidación inicial produjo 409 resultados, de los cuales 400 son únicos.
- **Internal/External evidence**: §5 (L62); sin citas numeradas.
- **Notes**: —

### C020 — Inventario y verificación de sitios
- **Section**, **Lines**: §5 (L62, L64), 62–64
- **Types**: result
- **Excerpt**: «Se inventariaron **35 sitios** de compraventa en `Data/mercados-compraventa-cuba.md`» / «Se verificaron **40 sitios/URLs**.»
- **Restated**: Se inventariaron 35 sitios de compraventa y se verificaron 40 sitios o URLs.
- **Internal/External evidence**: §5 (L62, L64); sin citas numeradas.
- **Notes**: —

### C021 — Organismos con competencia sobre el mercado
- **Section**, **Lines**: §5 (L66), 66
- **Types**: result, contextual
- **Excerpt**: «Se documentaron **14 organismos** con competencia sobre el mercado: Consejo de Ministros/Estado, MINCEX, MINCIN, MITRANS, CEMA, MFP, ONAT, Aduana General, BCC, MININT, MINJUS, MEP, MINREX y MINSAP.»
- **Restated**: El documento identifica 14 organismos con competencia sobre el mercado automotor.
- **Internal/External evidence**: §5 (L66); sin citas numeradas.
- **Notes**: —

### C022 — Empresas autorizadas y precios de referencia
- **Section**, **Lines**: §4 (L58), 58
- **Types**: result, citation-grounded
- **Excerpt**: «Se documentaron **17 empresas autorizadas** a importar y comercializar vehículos, distribuidores privados (BDC One, Dongfeng, MCV, Finauto, Changan, Chinautos, Envision, ATR Export), precios de referencia (BDC One 14.849–31.478 EUR; Dongfeng desde 21.900 EUR; Finauto desde 15.500 EUR»
- **Restated**: El marco normativo registra 17 empresas autorizadas y precios de referencia por distribuidor.
- **Internal/External evidence**: §4 (L58), `Data/investigacion-mercado-automotor-cuba.md`; sin citas numeradas.
- **Notes**: el equivalente inglés (L189) usa separadores de miles con coma.

### C023 — Marco normativo: Decreto 163/2026 y resoluciones
- **Section**, **Lines**: §4 (L58), §10 (L116–117), 58/116–117
- **Types**: citation-grounded
- **Excerpt**: «La norma marco es el **Decreto 163/2026** (Gaceta Oficial No. 65 Ordinaria, 04/08/2026, vigente desde el 11/08/2026), que deroga el Decreto 119/2024.»
- **Restated**: El Decreto 163/2026 es la norma marco vigente y deroga el Decreto 119/2024.
- **Internal/External evidence**: §4 (L58), §10 (L116–118); Gaceta Oficial No. 65/2026 citada sin numeración.
- **Notes**: —

### C024 — Derogación de la Resolución 312/2026
- **Section**, **Lines**: §52 (L1303), 1303
- **Types**: citation-grounded, result
- **Excerpt**: «la **Resolución 312/2026 de la Aduana General fue derogada por la Resolución 340/2026**.»
- **Restated**: La Resolución 340/2026 deroga a la 312/2026, que no debe citarse como norma vigente.
- **Internal/External evidence**: §52 (L1303), §4 (L58), §10 (L117); sin citas numeradas.
- **Notes**: corrección documentada en README, informe y verificación de marketplaces.

### C025 — Clonación de repositorios y clasificación CAPTCHA
- **Section**, **Lines**: §6 (L70), 70
- **Types**: result
- **Excerpt**: «Se clonaron **61 repositorios** en `Auxiliares/Repositorios` con `--depth 1` (2,2 GB, 61 entradas `OK`).»
- **Restated**: Se clonaron 61 repositorios (2,2 GB) y se clasificaron 92 proyectos CAPTCHA, de los que se seleccionaron 9.
- **Internal/External evidence**: §6 (L70); sin citas numeradas.
- **Notes**: —

### C026 — Entorno y dependencias instaladas
- **Section**, **Lines**: §6 (L72), 72
- **Types**: contextual
- **Excerpt**: «Se creó `Auxiliares/.venv` con patchright 1.64.4, PyPasser 1.1.0, Scrapling 0.5.1, ddddocr 1.6.1, playwright 1.65.2, curl_cffi 0.17.0, trafilatura, pandas, numpy, onnxruntime 1.32.0, ddgs 9.16.1 y tenacity 9.2.1.»
- **Restated**: El entorno virtual contiene las versiones declaradas de once dependencias.
- **Internal/External evidence**: §6 (L72); sin citas numeradas.
- **Notes**: —

### C027 — Regla de parada en la búsqueda documental
- **Section**, **Lines**: §7 (L78–86), 78–84
- **Types**: methodological, result
- **Excerpt**: «Tres búsquedas con la regla de parar tras 10 páginas sin enlaces útiles (útil = primera aparición de un trabajo investigativo automotriz):»
- **Restated**: Las tres búsquedas se detuvieron tras diez páginas sin enlaces útiles, con 159 páginas y 1.542 resultados en total.
- **Internal/External evidence**: tabla de búsquedas (L80–84); sin citas numeradas.
- **Notes**: las paradas declaradas fueron páginas 19, 11 y 22.

### C028 — Esquema SQLite por tienda
- **Section**, **Lines**: §8 (L90), 90
- **Types**: definitional, methodological
- **Excerpt**: «Se diseñó una base SQLite por tienda con una tabla `vehiculos`: identificación (`url`, `shop`, `title`, `status`, `scraped_at`), metadatos y 30 campos estructurados»
- **Restated**: El diseño prevé una base SQLite por tienda con 30 campos estructurados y campos sin normalizar.
- **Internal/External evidence**: §8 (L90); sin citas numeradas.
- **Notes**: —

### C029 — Conclusión: nueve marketplaces con inventario real
- **Section**, **Lines**: §12 (L135), 135
- **Types**: result, contextual
- **Excerpt**: «El mercado habanero tiene nueve marketplaces con inventario real y una docena con categorías vacías o solo piezas.»
- **Restated**: El mercado habanero cuenta con nueve marketplaces con inventario real y alrededor de una docena sin inventario de autos.
- **Internal/External evidence**: §5 (L64), §12 (L135); sin citas numeradas.
- **Notes**: el expediente de la iteración 1 observó quince sitios en esa categoría.

### C030 — Causalidad declarada del scraping sostenible
- **Section**, **Lines**: §12 (L137), 137
- **Types**: methodological
- **Excerpt**: «El scraping sostenible depende del ritmo, la sesión y la reanudación, no principalmente del fingerprint TLS.»
- **Restated**: El ritmo, la sesión y la reanudación son los factores decisivos del scraping sostenible, por encima del fingerprint TLS.
- **Internal/External evidence**: §11 (L126–131), §37 (L1100), §65 (L1433); sin comparación de condiciones.
- **Notes**: atribución causal sin contraste experimental.

### C031 — Regla de las 10 páginas
- **Section**, **Lines**: §12 (L138), 138
- **Types**: methodological, result
- **Excerpt**: «La regla de las 10 páginas evitó consumir resultados repetidos.»
- **Restated**: La regla de parada de diez páginas impidió procesar resultados repetidos.
- **Internal/External evidence**: §7 (L78–84), §33 (L1008); sin citas numeradas.
- **Notes**: —

### C032 — Nota de actualización de fases
- **Section**, **Lines**: §2 (L38); Parte II §2 (L169), 38
- **Types**: contextual, result
- **Excerpt**: «El pipeline de análisis (fase 8) se creó después, el 18/11/2026 (§34), y sus resultados vigentes se documentan en §59–§60.»
- **Restated**: La tabla de fases refleja el estado al 17/11/2026 y la fase 8 se creó el 18/11/2026.
- **Internal/External evidence**: §2 (L22–38), §34 (L1016), §59–§60; sin citas numeradas.
- **Notes**: atenúa pero no elimina la contradicción con la tabla de la Parte II (L164).

### C033 — Permanencia empírica de anuncios en Revolico
- **Section**, **Lines**: §15 (L775), 775
- **Types**: result
- **Excerpt**: «un anuncio con `updated_on_by_user=2024-12-17` seguía en HTTP 200 el 17/11/2026 (~699 días), por lo que no puede asumirse una expiración de 30 días.»
- **Restated**: Un anuncio con 699 días de antigüedad seguía accesible, de modo que no se puede asumir caducidad a los 30 días.
- **Internal/External evidence**: §15 (L775), Condiciones de Uso de Revolico (23/09/2026) citadas sin numeración.
- **Notes**: —

### C034 — Limpieza de la BD de Revolico
- **Section**, **Lines**: §15 (L773), 773
- **Types**: result
- **Excerpt**: «`limpiar_revolico.py` conservó **304 autos** en la tabla `autos` y registró **6.028 exclusiones** en `revision` (5.983 no vehículo 4+ ruedas, 45 sin datos necesarios, 0 páginas sin datos suficientes).»
- **Restated**: Sobre 6.332 anuncios se conservaron 304 autos y se registraron 6.028 exclusiones.
- **Internal/External evidence**: §15 (L771–773), §16 (L787); sin citas numeradas.
- **Notes**: 304 + 6.028 = 6.332.

### C035 — Eficiencia relativa de las fuentes
- **Section**, **Lines**: §15 (L767–769), 767
- **Types**: methodological
- **Excerpt**: «la ruta más eficiente es Telegram MTProto (`telethon`, ya integrado): sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`. Le sigue Facebook GQL»
- **Restated**: Telegram MTProto es la fuente más eficiente, seguida de Facebook GQL, WAHA para WhatsApp y Playwright/Selenium como último recurso.
- **Internal/External evidence**: §15 (L767–769), §28 (L950); sin citas numeradas.
- **Notes**: jerarquía declarada sin medición comparativa de rendimiento.

### C036 — Pipeline de tres colas persistentes
- **Section**, **Lines**: §16 (L779–783), 779–783
- **Types**: methodological
- **Excerpt**: «separa el trabajo en tres etapas simultáneas con colas persistentes en `Data/Revolico/pipeline.sqlite`»
- **Restated**: El pipeline separa descubrimiento, descarga y procesamiento con colas persistentes y commit cada 25 anuncios.
- **Internal/External evidence**: §16 (L779–787), §26 (L928–933); sin citas numeradas.
- **Notes**: —

### C037 — Prueba inicial del pipeline por colas
- **Section**, **Lines**: §16 (L787), 787
- **Types**: result
- **Excerpt**: «Prueba con 1 página: **119 enlaces** descubiertos y procesados, 7 lotes de 25, BD principal de 6.332 a **6.334 anuncios** y de 304 a **317 autos**.»
- **Restated**: La prueba con una página procesó 119 enlaces y elevó la BD a 6.334 anuncios y 317 autos.
- **Internal/External evidence**: §16 (L787, L789); sin citas numeradas.
- **Notes**: el número de lotes completos de 25 es cuatro, no siete (coherencia interna no verificada).

### C038 — Rango temporal de anuncios
- **Section**, **Lines**: §31 (L987–989), 987–989
- **Types**: methodological, result
- **Excerpt**: «Se fijó el rango permitido de `updated_on_by_user` entre **2021-01-01 y la fecha actual** en `limpiar_revolico.py` (`FECHA_MINIMA`).»
- **Restated**: Los anuncios se acotan entre 2021-01-01 y la fecha de ejecución, sin exclusiones en la corrida declarada.
- **Internal/External evidence**: §31 (L987–991); sin citas numeradas.
- **Notes**: anuncio más antiguo 2024-12-17, más reciente 2026-11-17; 548 autos de 9.957 anuncios.

### C039 — Deduplicación de `autos`
- **Section**, **Lines**: §51 (L1279), 1279
- **Types**: result
- **Excerpt**: «La tabla se reconstruyó desde `anuncios` (fuente canónica): 814 filas con 748 IDs únicos → **744 autos únicos**.»
- **Restated**: La deduplicación redujo 814 filas a 744 autos únicos y creó el índice `idx_autos_id`.
- **Internal/External evidence**: §51 (L1279), §59 (L1379, 772 autos en la corrida vigente); sin citas numeradas.
- **Notes**: cuatro anuncios se marcaron como no-auto.

### C040 — Reparación de precios y títulos de marketplaces
- **Section**, **Lines**: §51 (L1281), 1281
- **Types**: result, methodological
- **Excerpt**: «`parse_price` ahora interpreta separadores de miles (973 anuncios recuperados: 872 de iTENCEL, 99 de Cubisima, 2 de VentaCuba).»
- **Restated**: La corrección del parseo recuperó 973 precios y 614 precios de Autocubana desde JSON-LD.
- **Internal/External evidence**: §51 (L1281), `descartes_marketplaces.csv`; sin citas numeradas.
- **Notes**: mediana local declarada de 21.000 USD.

### C041 — Corrección del kilometraje con separador de miles
- **Section**, **Lines**: §51 (L1282), 1282
- **Types**: methodological, result
- **Excerpt**: «`parse_specs` y `parse_title` convertían `80,000 km` en 80 km. Se extrajo `parse_number()` con la lógica de separadores ya usada en `parse_price`.»
- **Restated**: La nueva función `parse_number()` convierte correctamente `80,000 km` en 80.000 km.
- **Internal/External evidence**: §51 (L1282); sin citas numeradas.
- **Notes**: —

### C042 — Reconciliación de la encuesta de demanda
- **Section**, **Lines**: §51 (L1285), 1285
- **Types**: result
- **Excerpt**: «el cruce filtra ahora `interes=1`, dando **28 interesados** (14 eléctrico, 10 combustión, 4 híbrido) en lugar de los 29 que contaba el script anterior»
- **Restated**: El cruce vigente cuenta 28 interesados, frente a 29 del script anterior.
- **Internal/External evidence**: §50 (L1269), §51 (L1285); sin citas numeradas.
- **Notes**: —

### C043 — Descarga de los anuarios del ONEI
- **Section**, **Lines**: §53 (L1313–1315), 1313–1315
- **Types**: result
- **Excerpt**: «se descargaron **todos los documentos enlazados**: 111 PDF, 7 RAR y 103 archivos Excel extraídos, unos 311 MB en total.»
- **Restated**: Se descargaron los 117 enlaces de los 12 anuarios del ONEI (2014–2025), con 111 PDF, 7 RAR y 103 Excel.
- **Internal/External evidence**: §53 (L1313–1315), `Data/fuentes-oficiales/ONEI/INDICE.md`; sin citas numeradas.
- **Notes**: validación MIME sin archivos sospechosos.

### C044 — Hallazgos de los anuarios y laguna de parque automotor
- **Section**, **Lines**: §56 (L1351), 1351
- **Types**: result
- **Excerpt**: «el transporte de pasajeros cayó un 59 % entre 2019 y 2025 y el ómnibus un 71 %; los accidentes bajaron pero la gravedad aumentó (9,9 fallecidos por cada 100 accidentes en 2025). **No hay series de parque automotor ni de matriculaciones**»
- **Restated**: Las series del ONEI muestran caídas del 59 % y 71 %, pero no contienen parque automotor ni matriculaciones.
- **Internal/External evidence**: §53 (L1317), §56 (L1351), `ANALISIS_DATO.md`; sin citas numeradas.
- **Notes**: corrige la expectativa registrada en §53 (L1317).

### C045 — Fragmentación de la BD con manifiesto
- **Section**, **Lines**: §54 (L1325–1329), 1325
- **Types**: methodological, result
- **Excerpt**: «`Data/Revolico/revolico.sqlite` (849.465.344 bytes) se dividió en **82 chunks de 10 MB** en `Data/Revolico/chunks/`, con un `MANIFEST.json` que guarda el SHA-256 del archivo completo, el orden, el offset y el hash de cada fragmento.»
- **Restated**: La BD de 849.465.344 bytes se dividió en 82 fragmentos verificados con manifiesto SHA-256.
- **Internal/External evidence**: §54 (L1325–1329), §14 (L756–763); sin citas numeradas.
- **Notes**: los chunks se publican en la rama huérfana `chunked-db`.

### C046 — Gestión con Git LFS
- **Section**, **Lines**: §30 (L977–981), 977–981
- **Types**: methodological
- **Excerpt**: «Se instaló **Git LFS 3.8.1** y se activó en el repositorio. `.gitattributes` marca `*.sqlite`, `*.sqlite-wal` y `*.sqlite-shm` con `filter=lfs diff=lfs merge=lfs -text`»
- **Restated**: Las bases SQLite se gestionan con Git LFS y se advierte sobre el consumo de cuota.
- **Internal/External evidence**: §30 (L977–983), §54 (L1327); sin citas numeradas.
- **Notes**: —

### C047 — Fuentes adicionales verificadas
- **Section**, **Lines**: §52 (L1293), 1293
- **Types**: result
- **Excerpt**: «El resultado está en `Data/fuentes-adicionales-2026-11-20.md`: **25 fuentes** verificadas, organizadas por tipo con URL, datos expuestos, viabilidad de scraping y aporte al proyecto.»
- **Restated**: Se verificaron 25 fuentes adicionales organizadas por tipo.
- **Internal/External evidence**: §52 (L1293–1305); sin citas numeradas.
- **Notes**: —

### C048 — Repositorios cubanos de automoción
- **Section**, **Lines**: §49 (L1251), 1251
- **Types**: result
- **Excerpt**: «Tras deduplicar se obtuvieron **648 repos**, de los que se depuraron **36 con relación directa o instrumental** al mercado automotor cubano.»
- **Restated**: La búsqueda produjo 648 repositorios únicos y 36 con relación directa o instrumental.
- **Internal/External evidence**: §49 (L1251–1255), `Data/github-repos-automotriz-cuba-2026-11-19.md`; sin citas numeradas.
- **Notes**: —

### C049 — Consolidación de bases de repositorios de referencia
- **Section**, **Lines**: §50 (L1267), 1267
- **Types**: result
- **Excerpt**: «Se creó `Data/repos-autos-referencias/referencias_autos.sqlite` con **25 tablas** (3.958 anuncios de Revolico, 3.566 limpios, catálogos de comercializadoras, 33 respuestas de encuesta, 30 + 30 + 8 entrevistas, datasets de AutosxCuba) y una tabla `provenancia`.»
- **Restated**: La base consolidada reúne 25 tablas con procedencia declarada.
- **Internal/External evidence**: §50 (L1263–1269); sin citas numeradas.
- **Notes**: 369 anuncios ya estaban en la base propia y 3.589 son nuevos.

### C050 — Detección de duplicados entre repositorios
- **Section**, **Lines**: §50 (L1265), 1265
- **Types**: result
- **Excerpt**: «Se compararon 233 archivos de datos por hash y 76 CSV por contenido ordenado. Se detectaron 12 grupos de duplicados bytes y 11 de duplicados por contenido»
- **Restated**: La comparación detectó 23 grupos de duplicados entre los archivos de los repositorios referencia.
- **Internal/External evidence**: §50 (L1265); sin citas numeradas.
- **Notes**: —

### C051 — Convención de 38 referencias con estado de verificación
- **Section**, **Lines**: §70 (L1477), 1477
- **Types**: result, citation-grounded
- **Excerpt**: «Las fuentes restantes figuran con estado `(metadata incomplete)` en `reviews/informe-tecnico-2026-11-27.e2-literature.md` y no se presentan como referencias verificadas. La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`»
- **Restated**: Existen 38 referencias numeradas con estado de verificación, cuatro de ellas confirmadas externamente.
- **Internal/External evidence**: §70 (L1477–1479), `Data/referencias.md`; Crossref/OpenAlex según el propio texto.
- **Notes**: —

### C052 — Incorporación de diez anuncios de iTENCEL
- **Section**, **Lines**: §58 (L1369–1371), 1371
- **Types**: result
- **Excerpt**: «La BD pasó de 951 a **961 anuncios** (961 URLs únicas, `integrity_check=ok`).»
- **Restated**: La base de iTENCEL pasó de 951 a 961 anuncios únicos tras insertar diez anuncios nuevos.
- **Internal/External evidence**: §57 (L1361), §58 (L1369–1373); sin citas numeradas.
- **Notes**: se realizó copia de seguridad `itencel.sqlite.bak-20261123` antes de escribir.

### C053 — Estado previo de los anuncios limpios
- **Section**, **Lines**: §58 (L1371), 1371
- **Types**: result
- **Excerpt**: «**2.014 anuncios limpios**, de ellos 1.323 locales y 691 de importación; mediana local 21.000 USD y mediana de kilometraje 44.125 km.»
- **Restated**: Tras la incorporación de iTENCEL, la regeneración produjo 2.014 anuncios limpios y 44.125 km de mediana.
- **Internal/External evidence**: §58 (L1371), §59 (L1379, cifras vigentes 2.029 y 43.000 km); sin citas numeradas.
- **Notes**: estado intermedio sustituido por §59.

### C054 — Capas del mapa offline
- **Section**, **Lines**: §41 (L1154–1157), §42 (L1177), 1177
- **Types**: result
- **Excerpt**: «Estado final: **131 gasolineras, 12 estaciones de carga, 25 concesionarios (17 con coords) y 22 talleres (todos con coords)**.»
- **Restated**: El mapa unificado contiene 131 gasolineras, 12 estaciones de carga, 25 concesionarios y 22 talleres.
- **Internal/External evidence**: §41 (L1154–1157, 137 gasolineras iniciales), §42 (L1168–1179); sin citas numeradas.
- **Notes**: el descenso de 137 a 131 gasolineras no se explica en el texto.

### C055 — Serie de precios del combustible
- **Section**, **Lines**: §41 (L1157–1160), 1157–1160
- **Types**: result, citation-grounded
- **Excerpt**: «Se creó `Data/combustible/precios_combustible.sqlite` con **18 observaciones** entre 20/08/2026 y 18/11/2026, diferenciando mercado oficial CIMEX, informal elToque y precios publicados, sin convertir monedas automáticamente.»
- **Restated**: La serie de combustible tiene 18 observaciones y separa mercado oficial, informal y precios publicados.
- **Internal/External evidence**: §41 (L1157–1160), §43 (L1189–1195, hitos normativos); sin citas numeradas.
- **Notes**: la B94 informal pasó de 3.500–5.000 CUP (agosto) a 7.000–8.000 CUP (septiembre 2026).

### C056 — Estimación de retención como inferencia de diseño
- **Section**, **Lines**: §63 (L1417), 1417
- **Types**: methodological
- **Excerpt**: «La estimación de retención (`Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md`) es **inferencia de diseño, no medición**»
- **Restated**: Las cifras de retención son una proyección de diseño, no una medición observada.
- **Internal/External evidence**: §63 (L1415–1419), `ALCANCE_Y_RETENCION.md`; sin citas numeradas.
- **Notes**: el propio texto rotula la naturaleza no empírica de la estimación.

### C057 — Compilación estricta del sitio
- **Section**, **Lines**: §61 (L1399), 1399
- **Types**: methodological, result
- **Excerpt**: «`mkdocs build --strict` termina sin errores ni enlaces rotos.»
- **Restated**: La compilación estricta del sitio MkDocs termina sin errores ni enlaces rotos.
- **Internal/External evidence**: §61 (L1397–1401), `mkdocs.yml`, `docs/`; sin citas numeradas.
- **Notes**: —

### C058 — Primera corrida real del scraper de circuitos
- **Section**, **Lines**: §62 (L1407), 1407
- **Types**: result
- **Excerpt**: «en su primera corrida real capturó 40 mensajes, deduplicó por ID y dejó 35 circuitos sin luz, 23 mixtos y 2 con luz en `Data/mapas/circuitos_estado.sqlite`.»
- **Restated**: El primer scrapeo de circuitos produjo 60 registros clasificados a partir de 40 mensajes.
- **Internal/External evidence**: §62 (L1405–1409), `TIMELAPSE_CIRCUITOS.md`; sin citas numeradas.
- **Notes**: 35 + 23 + 2 = 60, cifra superior a los 40 mensajes declarados.

### C059 — Protocolo, semilla y reproducción
- **Section**, **Lines**: §71.5 Protocolo, semillas y reproducción / Protocol, seeds and reproduction (L1514–1516), 1516
- **Types**: methodological
- **Excerpt**: «La semilla `SEED = 20261127` está declarada en `run_all.py` y en este documento. Comando único: `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py`. Puntos de entrada con argumentos: `generar_dashboard.py --solo-si-cambia`, `exportar_parquet_compacto.py --tablas ...`, `db_chunks.py split|verify|assemble` y `generar_sitio_mkdocs.py`.»
- **Restated**: La reproducción del análisis usa la semilla 20261127 declarada, un comando único y dependencias fijadas a serie menor.
- **Internal/External evidence**: §71.5 (L1516), `run_all.py`, `requirements.txt`, `test_smoke_pipeline.py` (mencionados en L1516)
- **Notes**: sección incorporada en esta iteración; no se verifica el contenido de los archivos citados.

### C060 — Diseño sin pareado y tamaño muestral en anuncios
- **Section**, **Lines**: §71.3 Pruebas y tamaño muestral / Tests and sample size (L1503–1505), 1505
- **Types**: methodological, definitional
- **Excerpt**: «No hay diseño pareado: los anuncios son observaciones independientes, por lo que no se aplican Wilcoxon de pares ni t de diferencias; se usan Kruskal-Wallis y Welch para grupos independientes. El tamaño se mide en anuncios (981 candidatas de 8 marketplaces), no en ensayos experimentales.»
- **Restated**: El diseño treatment los anuncios como observaciones independientes y mide el tamaño en 981 candidatas de ocho marketplaces.
- **Internal/External evidence**: §71.3 (L1505), §59 (L1381), §60 (L1389)
- **Notes**: sección incorporada en esta iteración.

### C061 — Amenazas a la validez declaradas
- **Section**, **Lines**: §71.4 Amenazas a la validez / Threats to validity (L1507–1512), 1509–1512
- **Types**: contextual, methodological
- **Excerpt**: «- **Externa:** solo La Habana y anuncios en línea; los precios son pedidos, no transaccionados.» / «- **Estadística conclusiva:** el modelo completo usa 28 observaciones y ningún coeficiente alcanza p < 0,05; el principal tiene mejor cobertura pero su signo de antigüedad refleja selección.»
- **Restated**: El documento declara amenazas externa, de constructo, interna y estadística, incluida la no significancia de los coeficientes del modelo completo.
- **Internal/External evidence**: §71.4 (L1509–1512), §59 (L1381), §60 (L1389)
- **Notes**: sección incorporada en esta iteración; reformula límites ya presentes en §19 (L855) y §18 (L831).

## Contextual claims (65)

### C062 — Fase activa redefinida como sexta
- **Section**, **Lines**: §2 (L22), 22
- **Types**: contextual
- **Excerpt**: «Las fases se redefinieron para que la fase activa sea la sexta. Estado a 17/11/2026:»

### C063 — Informe y README como soporte transversal
- **Section**, **Lines**: §2 (L36), 36
- **Types**: contextual
- **Excerpt**: «La creación de este informe y del `README.md` es soporte transversal y no cambia la fase activa.»

### C064 — Decisiones de organización de carpetas
- **Section**, **Lines**: §3 (L54), 54
- **Types**: methodological, contextual
- **Excerpt**: «todo el material auxiliar vive dentro de `Auxiliares/`; los clones se hicieron con `--depth 1` y se registraron en `~/Utilidades/HerramientasScraping/_clone_log.tsv`; la descubrimiento se separó de la verificación»

### C065 — Exclusión de `Copias/`
- **Section**, **Lines**: §3 (L54), 54
- **Types**: contextual
- **Excerpt**: «`Copias/` no se registra en este informe por decisión explícita.»

### C066 — Decreto 163/2026 y Gaceta Oficial
- **Section**, **Lines**: §4 (L58), 58
- **Types**: citation-grounded
- **Excerpt**: «La norma marco es el **Decreto 163/2026** (Gaceta Oficial No. 65 Ordinaria, 04/08/2026, vigente desde el 11/08/2026), que deroga el Decreto 119/2024.»

### C067 — Cambio de motor de búsqueda
- **Section**, **Lines**: §5 (L62), 62
- **Types**: contextual
- **Excerpt**: «Dos búsquedas iniciales en DuckDuckGo, 30 páginas cada una, con bloqueo por CAPTCHA: se cambió a Yahoo y visitas directas.»

### C068 — Correcciones de clasificación de sitios
- **Section**, **Lines**: §5 (L64), 64
- **Types**: result, contextual
- **Excerpt**: «Se corrigieron clasificaciones: Mercadoba y Fagales Market sin sección real; TuCuevita, Mercubano, Mercandil, Revoltillo, QvaVentas, Casinuevo, Publicid, WAnuncios y AnunciosCuba con categoría vacía»

### C069 — Inventario de marketplaces activos
- **Section**, **Lines**: §5 (L64), 64
- **Types**: result
- **Excerpt**: «Marketplaces con sección activa: Autocubana (667 vehículos), iTENCEL (951), VentaCuba (801 carros/camionetas), Timbirichi (281 carros), Revolico (112 enlaces en la primera página), Cogetucarro (5.225 anuncios), Cubisima (155 fichas)»

### C070 — Cobertura temática de los repositorios clonados
- **Section**, **Lines**: §6 (L70), 70
- **Types**: contextual
- **Excerpt**: «El conjunto cubre scraping general (Firecrawl, browser-use, Scrapling, crawl4ai, Scrapy, SeleniumBase, trafilatura, curl_cffi, Patchright, Playwright), Facebook, WhatsApp, Telegram y CAPTCHA.»

### C071 — Chromium del sistema y FlareSolverr
- **Section**, **Lines**: §6 (L72), 72
- **Types**: contextual
- **Excerpt**: «Se usa el Chromium del sistema y FlareSolverr 3.5.2 en Docker (`http://127.0.0.1:8191/`).»

### C072 — Herramientas creadas en la fase 3
- **Section**, **Lines**: §6 (L74), 74
- **Types**: contextual
- **Excerpt**: «Herramientas creadas: `ddg_research.py`, `buscar_fallback.py`, `descargar_hombros.py`, `scrape_concesionarios.py`, `resumen_catalogos.py` y `actualizar_informe.py`.»

### C073 — Definición operativa de «útil»
- **Section**, **Lines**: §7 (L78), 78
- **Types**: definitional, methodological
- **Excerpt**: «útil = primera aparición de un trabajo investigativo automotriz»

### C074 — Resultados de descarga del corpus
- **Section**, **Lines**: §7 (L86), 86
- **Types**: result
- **Excerpt**: «descarga inicial **93 OK / 17 fallos**, rentabilidad **23 OK / 10 fallos**, calidad/precio **78 OK / 36 fallos**, con `manifest.jsonl` e `indice.md`.»

### C075 — Adaptadores por dominio y renderizado opcional
- **Section**, **Lines**: §8 (L90), 90
- **Types**: methodological
- **Excerpt**: «El scraper `scrape_concesionarios.py` usa adaptadores por dominio y renderizado opcional con Playwright.»

### C076 — Filtro de normas relevantes
- **Section**, **Lines**: §10 (L114), 114
- **Types**: contextual
- **Excerpt**: «Solo se incluyen las normas y fuentes relevantes para el contexto del proyecto:»

### C077 — No elusión de anti-automatización
- **Section**, **Lines**: §10 (L118), 118
- **Types**: methodological, contextual
- **Excerpt**: «No se eluden mecanismos anti-automatización; los HTTP 403/429 se registran como limitación.»

### C078 — Condiciones para publicar resultados
- **Section**, **Lines**: §10 (L119), 119
- **Types**: methodological, contextual
- **Excerpt**: «antes de publicar resultados deben verificarse las normas cubanas vigentes y aplicar solo datos agregados, sin nombres, teléfonos ni información personal de anunciantes.»

### C079 — Índice de gacetas fuera del árbol
- **Section**, **Lines**: §10 (L120), 120
- **Types**: contextual
- **Excerpt**: «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe»

### C080 — Solución al CAPTCHA de paginación
- **Section**, **Lines**: §11 (L126), 126
- **Types**: methodological, contextual
- **Excerpt**: «CAPTCHA en paginación DDG | Yahoo + visitas directas; después sesión con `vqd`.»

### C081 — Manejo de HTTP 202 y página anomaly
- **Section**, **Lines**: §11 (L127–128), 127–128
- **Types**: methodological, contextual
- **Excerpt**: «HTTP 202 y página “anomaly” | Pausa 7–10 s con jitter, backoff exponencial y cooldown.»

### C082 — Registro de carrosw como limitación
- **Section**, **Lines**: §11 (L129), 129
- **Types**: methodological, contextual
- **Excerpt**: «carrosw anti-bot | Registrado como limitación; no se falsificó su contenido.»

### C083 — Deduplicación por título, prefijo y dominio
- **Section**, **Lines**: §11 (L131), 131
- **Types**: methodological, contextual
- **Excerpt**: «Repetidos y mirrors | Deduplicación por título normalizado, prefijo y dominio.»

### C084 — Conclusión sobre marketplaces y categorías vacías
- **Section**, **Lines**: §12 (L135), 135
- **Types**: result, contextual
- **Excerpt**: «El mercado habanero tiene nueve marketplaces con inventario real y una docena con categorías vacías o solo piezas.»

### C085 — Registro automático de altas
- **Section**, **Lines**: §13 (L276), 276
- **Types**: contextual
- **Excerpt**: «El script `Auxiliares/herramientas/actualizar_informe.py` añade filas debajo del marcador y regenera el PDF.»

### C086 — Entradas omitidas en el registro
- **Section**, **Lines**: §13 (L295), 295
- **Types**: contextual
- **Excerpt**: «175 entradas adicionales no listadas / omitted»

### C087 — Sincronización de Revolico en partes
- **Section**, **Lines**: §14 (L756), 756
- **Types**: methodological
- **Excerpt**: «La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**. Cada 10 minutos un timer de systemd ejecuta `Auxiliares/herramientas/actualizar_revolico.py»»

### C088 — Última ejecución registrada de sincronización
- **Section**, **Lines**: §14 (L763), 763
- **Types**: result, contextual
- **Excerpt**: «2026-11-17T15:47:42+00:00 | 795373568 B | 48 partes de 16 MiB | `dadd2bffba615d8a…`»

### C089 — Detención manual del timer de scrapeo
- **Section**, **Lines**: §15 (L771), 771
- **Types**: result, contextual
- **Excerpt**: «se detuvo manualmente `revolico-scrape.timer` y su servicio a petición del usuario. El scraper había ampliado la BD de 3.682 a **6.332 anuncios** (520,6 MB) antes de detenerse»

### C090 — Renovación reciente de anuncios
- **Section**, **Lines**: §15 (L775), 775
- **Types**: result
- **Excerpt**: «El 99,3 % de los anuncios tiene `updated_on_by_user` en los últimos 7 días (mediana 1 día en los 189 autos)»

### C091 — Marcador `updatedOnToOrder` desactivado
- **Section**, **Lines**: §16 (L785), 785
- **Types**: methodological
- **Excerpt**: «El campo `updatedOnToOrder` del listado resultó ser un marcador de ranking y no de edición, así que el salto de descarga queda desactivado por defecto (`--skip-unchanged`)»

### C092 — Fuentes revisadas para requerimientos de fases 7–8
- **Section**, **Lines**: §17 (L793), 793
- **Types**: contextual
- **Excerpt**: «Fuentes académicas y repositorios revisados para definir los requerimientos del análisis (Fases 7-8):»

### C093 — Requerimientos derivados
- **Section**, **Lines**: §17 (L810), 810
- **Types**: methodological
- **Excerpt**: «La ponderación de preferencias del usuario y el producto interactivo quedan para la especialización futura.»

### C094 — Verificación en vivo de DfT/DVLA
- **Section**, **Lines**: §18 (L818), 818
- **Types**: citation-grounded
- **Excerpt**: «Verificado en vivo: publicado por Department for Transport + DVLA, actualizado 23/09/2026, Open Government Licence»

### C095 — VAHAN no accesible desde el entorno
- **Section**, **Lines**: §18 (L819), 819
- **Types**: contextual, citation-grounded
- **Excerpt**: «No accesible desde este entorno (error de transporte); el repo documenta 12 exportaciones mensuales 2025 y manifiesto de verificacion»

### C096 — BCC no accesible en vivo
- **Section**, **Lines**: §18 (L820), 820
- **Types**: contextual, citation-grounded
- **Excerpt**: «No accesible en vivo desde este entorno; citado en `Data/investigacion-mercado-automotor-cuba.md` y Resolución 102/2026»

### C097 — Redes sociales como fuente no estadística
- **Section**, **Lines**: §18 (L827), 827
- **Types**: contextual
- **Excerpt**: «No verificables como fuente estadística; requieren consentimiento y sin datos personales»

### C098 — Marco general de ocho pasos
- **Section**, **Lines**: §19 (L837–846), 837–846
- **Types**: contextual, methodological
- **Excerpt**: «Marco general (8 pasos, derivado de los trabajos revisados)»

### C099 — Fuentes de la adaptación a La Habana
- **Section**, **Lines**: §19 (L851), 851
- **Types**: result, contextual
- **Excerpt**: «Revolico (BD propia, 6.334 anuncios / 317 autos), concesionarios (Autocubana, Dongfeng, BDC One…), Gaceta/Decreto 163/2026, BCC (oficial) y elTOQUE (informal), salarios de la Resolución 14»

### C100 — Métodos adaptados del marco
- **Section**, **Lines**: §19 (L853), 853
- **Types**: methodological
- **Excerpt**: «comparables por modelo ±2 años y municipio; rentabilidad = reventa esperada − compra − reacondicionamiento − impuestos (Decreto 163/2026); asequibilidad = precio / salario; series con snapshots.»

### C101 — Activos existentes según el marco detallado
- **Section**, **Lines**: §20 (L873), 873
- **Types**: result, contextual
- **Excerpt**: «BD de 6.334 anuncios / 317 autos, esquema con 30 campos + auditoría, imágenes/teléfonos, snapshots de precios, normativa documentada, tasas y salarios referenciados, repositorios de modelos y dashboards.»

### C102 — Datos pendientes según el marco detallado
- **Section**, **Lines**: §20 (L875), 875
- **Types**: contextual
- **Excerpt**: «extracción estructurada de año/km/marca/modelo/combustible/transmisión desde `ad_json`/`apollo_full`; montos de costos ocultos; precios de transacción reales; estadísticas oficiales cubanas de parque y matriculaciones»

### C103 — Renombre de la fase 8
- **Section**, **Lines**: §21 (L883), 883
- **Types**: contextual
- **Excerpt**: «La fase 8 pasa a llamarse **Análisis de mercado, comparables y rentabilidad**.»

### C104 — Salidas del análisis descriptivo inicial
- **Section**, **Lines**: §22 (L892), 892
- **Types**: contextual
- **Excerpt**: «genera en `Data/analisis/`: `resumen_general.csv`, `precios_por_marca.csv`, `precios_por_municipio.csv`, `precios_por_anio.csv`, `outliers.csv`, `cobertura.csv`, `informe_descriptivo.md` y `dashboard.html`.»

### C105 — Resultados del análisis descriptivo inicial
- **Section**, **Lines**: §22 (L894), 894
- **Types**: result
- **Excerpt**: «Precio mediano **22.000 USD**, media 24.416,59 USD, IQR 11.375–35.000 USD, rango 600–95.000 USD.»

### C106 — Cobertura de campos derivados
- **Section**, **Lines**: §22 (L894), 894
- **Types**: result
- **Excerpt**: «Cobertura de campos derivados: marca 68,4 %, año 63,5 %, km 6,2 % (heurísticos, extraídos solo de título/descripción). Detectados 5 outliers por IQR.»

### C107 — Conversión diaria por año del vehículo
- **Section**, **Lines**: §23 (L902), 902
- **Types**: result, methodological
- **Excerpt**: «la conversión usa `precio_USD × TRMI elTOQUE` del día del anuncio (columna `Mediana` de `Anexos/Investigacion Cambios/trmi_USD.csv`)»

### C108 — Serie histórica de TRMI y precios
- **Section**, **Lines**: §23 (L904), 904
- **Types**: result
- **Excerpt**: «Ejemplo histórico: la TRMI pasó de 680 CUP/USD (09/07/2026) a 920 (16-17/11/2026), valor ya sustituido por la convención fija de 930 del 18/11/2026 que usa el pipeline»

### C109 — Supuesto de anuncio activo
- **Section**, **Lines**: §23 (L903), 903
- **Types**: methodological
- **Excerpt**: «todos los registros tienen `status=PUBLISHED` y página verificada en la captura, por lo que se asume que son comprables; no se comprueba disponibilidad en tiempo real.»

### C110 — Generación de gráficas
- **Section**, **Lines**: §23 (L905), 905
- **Types**: contextual
- **Excerpt**: «usa matplotlib, seaborn y plotly (instalados) y genera 8 PNG + `dashboard_interactivo.html` en `Data/analisis/graficos/`.»

### C111 — Ausencia de campos estructurados en los JSON
- **Section**, **Lines**: §24 (L911), 911
- **Types**: result
- **Excerpt**: «**No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**: por eso `anio_est`, `marca_est` y `km_est` se derivan con regex del texto visible»

### C112 — Reporte de scrapeo y colas
- **Section**, **Lines**: §24 (L913), 913
- **Types**: result
- **Excerpt**: «`anuncios` 6.334 · `autos` 323 · `revision` 6.085 · `imagenes` 13.932 · `telefonos` 7.699 · BD 520,6 MB.»

### C113 — Reinicio automático del servicio
- **Section**, **Lines**: §25 (L920), 920
- **Types**: methodological
- **Excerpt**: «`revolico-scrape.service` ahora tiene `Restart=on-failure`, `RestartSec=30`, `StartLimitIntervalSec=300` y `StartLimitBurst=20`»

### C114 — Supuesto de disponibilidad de catálogos
- **Section**, **Lines**: §25 (L921), 921
- **Types**: methodological
- **Excerpt**: «Para concesionarios y páginas similares (`CATALOGOS`) se asume que todo el catálogo está disponible salvo que la página indique lo contrario y que se publicó el día de la captura (`fecha_publicacion = scraped_at`)»

### C115 — Causa del retraso en la clasificación
- **Section**, **Lines**: §26 (L928), 928
- **Types**: methodological
- **Excerpt**: «el timer ejecutaba `actualizar_revolico.py`, que solo corre el scraper y divide la BD, sin escribir nunca `autos`/`revision`.»

### C116 — Umbral de revisión de 4.000 anuncios
- **Section**, **Lines**: §27 (L943), 943
- **Types**: methodological
- **Excerpt**: «cuando `anuncios WHERE pagina_revisada=0`llega a **4.000** (configurable con `REVISAR_UMBRAL`), el aviso lanza `revolico-revisar.service`»

### C117 — Scraper de Telegram sin credenciales MTProto
- **Section**, **Lines**: §28 (L950), 950
- **Types**: contextual
- **Excerpt**: «No hay credenciales MTProto (`TELEGRAM_API_ID`/`TELEGRAM_API_HASH` vacías), así que se implementó `Auxiliares/herramientas/scraper_telegram_publico.py`, que lee la vista pública `t.me/s/<canal>`»

### C118 — Primera corrida de Telegram
- **Section**, **Lines**: §28 (L952), 952
- **Types**: result
- **Excerpt**: «Corrida final (50 páginas): **152 mensajes**, **54 anuncios de autos** del canal `goldenbullbusinessfamilycars`, 45 con año detectable y **ninguno con precio explícito»»

### C119 — Base de datos de Telegram y descubrimiento de canales
- **Section**, **Lines**: §29 (L960, L966–971), 960–971
- **Types**: result
- **Excerpt**: «`canales` | 119» / «`anuncios` | 54» / «El descubrimiento usa 26 búsquedas en tgden.com y valida cada usuario con `t.me/s/`, filtrando por contexto cubano.»

### C120 — Modo de descubrimiento sin procesamiento
- **Section**, **Lines**: §32 (L995–1000), 995–1000
- **Types**: methodological
- **Excerpt**: «**no hay descarga de anuncios, ni clasificación definitiva, ni inserción en `anuncios`/`autos`/`revision`**» / «se detiene al llegar a `FECHA_MINIMA = 2021-01-01`»

### C121 — Parada por página sin enlaces nuevos
- **Section**, **Lines**: §33 (L1008), 1008
- **Types**: methodological
- **Excerpt**: «se detenga en cuanto una página no aporte **ningún enlace nuevo** (todos sus anuncios ya fueron vistos)»

### C122 — Mecanismo de la app Circuitos Habana
- **Section**, **Lines**: §35 (L1068–1074), 1068–1074
- **Types**: result, citation-grounded
- **Excerpt**: «La app **no usa una API privada**: hace scraping del canal público de Telegram `https://t.me/s/EmpresaElectricaDeLaHabana` con Jsoup y User-Agent de Chrome.»

### C123 — Restricciones de Docker y Overpass
- **Section**, **Lines**: §36 (L1084–1085), 1084–1085
- **Types**: contextual
- **Excerpt**: «**el daemon Docker no arranca sin root** en este entorno (`dockerd needs to be started with root privileges`), por lo que se descartó esa vía.»

### C124 — Optimización de pipelines y efecto medido
- **Section**, **Lines**: §37 (L1100–1102), 1100–1102
- **Types**: methodological, result
- **Excerpt**: «los anuncios de Revolico pasaron de 10.117 a **10.149** y los autos de 716 a **814**; quedan 3.351 URLs pendientes y 1.940 rechazadas.»

### C125 — Reporte automático de progreso
- **Section**, **Lines**: §38 (L1112), 1112
- **Types**: contextual
- **Excerpt**: «actualiza **`Data/progreso_reporte.md` cada 5 minutos** con:»

### C126 — Ampliación de límites de marketplaces
- **Section**, **Lines**: §39 (L1127), 1127
- **Types**: result
- **Excerpt**: «en minutos Autocubana pasó de 400 a **566** y Timbirichi de 110 a **170**, totalizando **2.121 anuncios**.»


## Apéndice C — Literatura

# Literature Map — iteración 3 (re-verificación dirigida de flags)

Nota de entrada. El plan aprobado (`reviews/informe-tecnico-2026-11-27-iter3.plan.md`, 23 líneas) declara `level: master` y `preset: Standard`, pero no contiene `queries_planned` ni `hypotheses_planned`. El mandato recibido para este extractor es estrecho: re-visar `Data/referencias.md` y la §71.6 del informe para determinar si las comparaciones con Gegić, Muça, Du y Vidal Alejandro están en el cuerpo con cita, y verificar los flags campo por campo. En consecuencia: (a) no se ejecutaron búsquedas web nuevas —los metadatos se reutilizan del mapa completo de 38 trabajos de la pasada 1 y de la verificación OpenAlex/Crossref del 27/11/2026 consignada en `Data/referencias.md`—; (b) el mapa de 38 obras sigue vigente en `reviews/informe-tecnico-2026-11-27.e2-literature.md`; (c) los IDs `P001`–`P004` de este artefacto son propios y se mapean a los IDs de la pasada 1 y a las entradas numeradas; (d) `Cited in document` significa mención nominal en el cuerpo del informe, y se reporta por separado la presencia de marcador numérico `[N]`.

## Clusters

### Cluster 1 — Posicionamiento frente a trabajos cercanos (§71.6)

**Query**: `§71.6` ∩ `Data/referencias.md` — búsqueda en el cuerpo por apellido y año (Gegić 2019; Muça 2026; Du 2026; Vidal Alejandro 2024) y contraste campo por campo con el flag «Citada en el informe» de las entradas [14], [26], [9] y [29].

Los cuatro trabajos aparecen juntos en un único párrafo de la §71.6 (`INFORME_TECNICO.md`, líneas 1518–1520; idéntico en la copia en caché de la iteración 3, líneas 1518–1520). Cada comparación tiene la forma «Frente a <apellidos> (<año>), que <descripción del trabajo ajeno>, este trabajo <diferenciador>». Ninguna de las cuatro lleva marcador numérico de cita.

#### P001 — Car Price Prediction using Machine Learning Techniques
- **Authors**: Gegić, E.; Isaković, B.; Keco, D.; Mašetić, Z.; Kevrić, J.
- **Year**: 2019
- **Venue**: TEM Journal
- **Citations**: 188 (source: OpenAlex, fetched 2026-11-27T05:15:00Z; mapa E2 pasada 1, P014)
- **URL**: https://doi.org/10.18421/tem81-16
- **Layer**: L2 (re-visado en cuerpo; sin nueva lectura de resumen en esta iteración)
- **Cited in document**: yes — mención nominal en §71.6, línea 1520: «Frente a Gegić, Isaković, Keco, Mašetić y Kevrić (2019), que predicen precios con machine learning sobre catálogos estructurados…».
- **Document reference**: [14] en `Data/referencias.md` (marcador `[14]` ausente en el cuerpo).
- **source_of_metadata**: OpenAlex W4288610071 (mapa E2 pasada 1) + `Data/referencias.md` [14].
- **Flag verificado**: `Citada en el informe: no` en [14] → **desactualizado**; el propio archivo define el flag como «mención nominal en el informe» (línea 6). Debe pasar a `sí` con calificación «mención nominal en §71.6, sin marcador numérico».

#### P002 — A Pipeline for Integrating and Analyzing Public Business Data in Albania Using Web Scraping and Machine Learning
- **Authors**: Muça, M.; Bani, K.; Alla, A.
- **Year**: 2026
- **Venue**: International Journal of Advanced Computer Science and Applications (IJACSA)
- **Citations**: 0 (source: OpenAlex, fetched 2026-11-27T05:15:00Z; mapa E2 pasada 1, P026)
- **URL**: https://doi.org/10.14569/ijacsa.2026.0170845
- **Layer**: L2 (re-visado en cuerpo; sin nueva lectura de resumen en esta iteración)
- **Cited in document**: yes — mención nominal en §71.6, línea 1520: «Frente a Muça, Bani y Alla (2026), que integran datos públicos empresariales albaneses mediante scraping…».
- **Document reference**: [26] en `Data/referencias.md` (marcador `[26]` ausente en el cuerpo).
- **source_of_metadata**: OpenAlex W7204683515 (mapa E2 pasada 1) + `Data/referencias.md` [26].
- **Flag verificado**: `Citada en el informe: no` en [26] → **desactualizado**; debe pasar a `sí` con la misma calificación.

#### P003 — Nonlinear Depreciation and Brand Heterogeneity in Chinese Used-Car Listing Prices: An Interpretable Hedonic Regression and Out-of-Sample Evaluation
- **Authors**: Du, Z.; Yang, Z.; Zhang, Y.; Li, S.; Liu, Y.
- **Year**: 2026
- **Venue**: Advances in Economics, Management and Political Sciences
- **Citations**: 0 (source: OpenAlex, fetched 2026-11-27T05:15:00Z; mapa E2 pasada 1, P009)
- **URL**: https://doi.org/10.54254/2754-1169/2026.38524
- **Layer**: L2 (re-visado en cuerpo; sin nueva lectura de resumen en esta iteración)
- **Cited in document**: yes — mención nominal en §71.6, línea 1520: «Frente a Du, Yang, Zhang, Li y Liu (2026), que modelan depreciación no lineal y heterogeneidad de marca con evaluación fuera de muestra…».
- **Document reference**: [9] en `Data/referencias.md` (marcador `[9]` ausente en el cuerpo).
- **source_of_metadata**: OpenAlex W7225188457 (mapa E2 pasada 1) + `Data/referencias.md` [9].
- **Flag verificado**: `Citada en el informe: no` en [9] → **desactualizado**; debe pasar a `sí` con la misma calificación.

#### P004 — Using AI in the informal currency market: evidence from Cuba
- **Authors**: Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A.
- **Year**: 2024
- **Venue**: Applied Economics
- **Citations**: 1 (source: OpenAlex, fetched 2026-11-27T05:15:00Z; mapa E2 pasada 1, P029)
- **URL**: https://doi.org/10.1080/00036846.2024.2416091
- **Layer**: L2 (re-visado en cuerpo; sin nueva lectura de resumen en esta iteración)
- **Cited in document**: yes — mención nominal en §71.6, línea 1520: «Frente a Vidal Alejandro, Muñiz-Cuza y Calas Torres (2024), que estudian el mercado informal de divisas en Cuba…».
- **Document reference**: [29] en `Data/referencias.md` (marcador `[29]` ausente en el cuerpo).
- **source_of_metadata**: OpenAlex W4403850866 (mapa E2 pasada 1) + `Data/referencias.md` [29].
- **Flag verificado**: `Citada en el informe: no` en [29] → **desactualizado**; debe pasar a `sí` con la misma calificación.

## Recency distribution

Convenio: «In map» cuenta las cuatro entradas re-visadas en este artefacto; «In document bibliography» cuenta las 38 entradas presentes en `Data/referencias.md` (no menciones en el cuerpo); «Nominal mention in body» cuenta los apellidos efectivamente presentes en el texto del informe tras la §71.6.

| Year | In map | In document bibliography | Nominal mention in body |
|---|---:|---:|---:|
| 2026 | 2 | 6 | 2 (Muça [26], Du [9]) |
| 2025 | 0 | 1 | 0 |
| 2024 | 1 | 6 | 1 (Vidal Alejandro [29]) |
| 2023 | 0 | 4 | 0 |
| 2022 | 0 | 1 | 0 |
| ≤2021 | 1 | 20 | 1 (Gegić [14]) |

Las menciones nominales totales en el cuerpo son 5 de 38: Akerlof [1] —ya marcada `yes` y presente desde antes de la iteración 3— más las cuatro de §71.6. Los Marcadores `[N]` siguen siendo 0 en el texto (búsqueda de `[1]`–`[38]` en el cuerpo: sin coincidencias). La §70 («Referencias verificadas», línea 1477) enumera como citadas y verificadas solo Akerlof y tres fuentes institucionales (DfT/DVLA, ANFAC, AEADE); las cuatro obras de §71.6 no figuran en esa enumeración aunque sí lo están en el anexo numerado.

## Venue distribution

| Venue | Count in map |
|---|---:|
| TEM Journal | 1 |
| International Journal of Advanced Computer Science and Applications | 1 |
| Advances in Economics, Management and Political Sciences | 1 |
| Applied Economics | 1 |

## Likely missing important works

La lista de ocho obras probablemente decisivas de la pasada 1 (E2 iter1, líneas 490–530; reafirmada sin cambios en la iteración 2, línea 168) queda en siete para esta iteración: P002 Lewis (2011), P004 Englmaier et al. (2017), P021 Krotov et al. (2020), P023 Priestley et al. (2023), P022 Brown et al. (2025), P033 Guerra (2015) y P024 Hohensinner et al. (2026). Gegić et al. (2019) sale de la lista porque ya no está ausente del cuerpo: tiene comparación nominal explícita en §71.6. No se proponen obras nuevas: no se ejecutaron búsquedas temáticas en esta iteración y los metadatos se reutilizan de fuentes verificadas el 27/11/2026.

## Hypothesis checks (from plan)

El plan no declara hipótesis. Las tres comprobaciones siguientes se derivan del mandato recibido y son observaciones sin veredicto.

### H1 — Las comparaciones con Gegić, Muça, Du y Vidal Alejandro están en el cuerpo con cita (derivada)

Estado de la evidencia: **sí, como menciones nominales con autor y año**. Las cuatro comparecen en la §71.6, un apartado específico titulado «Posicionamiento frente a trabajos cercanos / Positioning against prior work» (líneas 1518–1520), y cada una recibe una cláusula contrastiva que describe el trabajo ajeno y enuncia el diferenciador propio. Es un cambio sustantivo frente a la iteración 2, donde el expediente forense constataba que «no hay párrafo comparativo con el trabajo académico más cercano» (`informe-tecnico-2026-11-27-iter2.forensic.md`, línea 247) y el informe iter2 resumía que los cuatro «figuran en la lista numerada sin citas en el cuerpo» (`informe-tecnico-2026-11-27-iter2.md`, línea 109).

La calificación de «con cita» es sin embargo parcial: las menciones no van acompañadas de marcador numérico `[14]`, `[26]`, `[9]` ni `[29]`, el documento no contiene ningún marcador `[N]` en su cuerpo, y la lista de «referencias citadas y verificadas externamente» de §70 no incluye a estas cuatro obras. La forma es, por tanto, cita nominal en el argumento, no cita numerada enlazada al anexo.

### H2 — Los flags por campo de `Data/referencias.md` reflejan el estado actual del cuerpo (derivada)

Estado de la evidencia: **no para cuatro campos**. El archivo define en su línea 6 que «`Citada: sí/no` indica mención nominal en el informe», y fue generado el 27/11/2026 desde el mapa E2 de la primera iteración, es decir, antes de que existiera la §71.6. Las fichas [9], [14], [26] y [29] conservan `Citada en el informe: no` mientras el cuerpo sí las nombra. Son cuatro flags desactualizados por campo, no un problema de metadatos bibliográficos: autores, año, revista, DOI y conteo de citas permanecen verificados. La actualización que corresponde, sin alterar otros campos, es `Citada en el informe: sí (mención nominal en §71.6; sin marcador numérico)`. Los marcadores `(metadata incomplete)` de [1], [10] y [38] y las notas de discrepancia de año de [2], [19] y [38] no fueron re-verificados en esta iteración y se dejan como están.

### H3 — La §71.6 satisface la condición de discusión dedicada de trabajos cercanos (derivada)

Estado de la evidencia: hay un apartado propio con cuatro párrafos comparativos nominales, uno por vecino académico, y cada uno formula una diferencia de procedencia, conversión, estimación u objeto de estudio. La observación se limita a la forma: el apartado no incorpora marcadores numéricos, cifras de los trabajos ajenos ni discusión de sus resultados o limitaciones más allá de la descripción de una frase. Corresponde a V4 y V5 decidir cómo ponderar este cambio respecto del criterio de nivel master.

## Sources used

- WebSearch queries: 0 (re-visación dirigida; sin búsquedas temáticas nuevas).
- WebFetch URLs: 0 en esta iteración.
- Semantic Scholar API hits: 0.
- OpenAlex API hits: 0 nuevos; los conteos de citas se reutilizan del mapa E2 de la pasada 1 (OpenAlex, fetched 2026-11-27T05:15:00Z) y de la verificación consignada en `Data/referencias.md` (27/11/2026).
- Archivos locales inspeccionados: `INFORME_TECNICO.md` (§70, línea 1477; §71.6, líneas 1518–1520); copia en caché `.playground/audit-cache/informe-tecnico-2026-11-27-iter3/informe-tecnico-2026-11-27-iter3.text.md` (mismo contenido); `Data/referencias.md` (líneas 3–6 y entradas [1], [9], [14], [26], [29]); `reviews/informe-tecnico-2026-11-27.e2-literature.md` (P009, P014, P026, P029; lista de obras ausentes); `reviews/informe-tecnico-2026-11-27-iter2.e2-literature.md` (nota de entrada y línea 168); `reviews/informe-tecnico-2026-11-27-iter2.forensic.md` ( línea 247) y `reviews/informe-tecnico-2026-11-27-iter2.md` (línea 109).
- Degradación: `degraded: false` para el mandato recibido —las cuatro comparaciones y sus cuatro flags quedaron resueltos por inspección directa del cuerpo—. Limitación declarada: no se re-verificaron los otros 34 flags ni se ejecutó búsqueda bibliográfica nueva; este mapa no debe usarse para proponer obras adicionales.


## Apéndice D — Artefactos

# Artifact Inventory

Iteración 3. Se inventarían los artefactos materiales que respaldan las afirmaciones del informe auditado, contrastando la caché de texto (`informe-tecnico-2026-11-27-iter3.text.md`, 1.523 líneas) con el checkout local efectivo `/home/thony70807/Proyectos/El precio de moverse en Cuba`. Se verifican en disco los siete artefactos señalados por el coordinador (dependencias fijadas, semilla, prueba de humo, CSV del modelo, bibliografía, panel y carpeta `reviews/`). Los números de línea citados corresponden a la caché de texto; en ella no hay marcadores numerados `Tabla N` / `Figura N`, por lo que las tablas se inventarían sin numerar, como en la iteración 2.

## Repository

- **URL**: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba
- **Clone status**: success (checkout local existente, 191 commits; no se realizó un clonado nuevo)
- **Languages**: Python: 40.367 LOC propias (excluye `.venv*`, `Auxiliares/Repositorios Referencias`, `Copias`, `Hombros`, `site`); Markdown: 95.706 LOC en todo el repo, de las cuales 2.495 LOC en `docs/`; HTML: panel autocontenido y 6 gráficos Plotly (ver Figures)
- **Commits**: 191
- **Authors**: CarlosAntonioAceaJimenezCD <CarlosAntonioAceaJimenezCD@users.noreply.github.com>
- **First commit**: 2026-11-17
- **Last commit**: 2026-11-27 (`ee994cd review: iteracion 2 y estandares de nivel master`)
- **Default branch**: main
- **Git LFS**: objetos grandes (`*.sqlite`, chunks) según `.gitattributes`; ver §68 y `Data/ESTRUCTURA_ESPACIO.md`

### Structure

```tree
./
├── Anexos/                  # Investigacion Cambios, Investigacion Combustible
├── Auxiliares/              # .venv*, herramientas (scripts propios), Repositorios Referencias
├── Copias/                  # 4 repos de referencia (excluidos por decisión del §3)
├── Data/                    # investigaciones, SQLite por tienda, bases y derivadas
│   ├── analisis_rentabilidad/  # config.py, scripts/, sql/, data/, outputs/{charts,tables}/, *.md
│   ├── Revolico/            # revolico.sqlite, pipeline.sqlite, chunks/, partes/
│   ├── repos-autos-referencias/  # referencias_autos.sqlite
│   ├── mapas/               # mapa_ofline.html, circuitos/, CSV de infraestructura
│   ├── dashboard.html       # panel interactivo autocontenido (vigente)
│   └── referencias.md       # 38 referencias numeradas
├── docs/ / site/            # fuente y salida MkDocs; dashboard.html, graficos/, apendice
├── reviews/                 # informes y forensic de iteraciones 1–2, artefactos de fase, plan iter3
├── Hombros/                 # PDFs, HTML, repos y derivadas
├── INFORME_TECNICO.md / .pdf, README.md, requirements.txt, mkdocs.yml
└── .playground/audit-cache/ # cachés de texto de las tres iteraciones de auditoría
```

### Entry points

| Path | LOC | Args documented | Notes |
|---|---|---|---|
| `Data/analisis_rentabilidad/scripts/run_all.py` | 58 | no | Orquestador; declara `SEED = 20261127` (líneas 16–18); invoca 5 etapas, `actualizar_numeros.py`, `generar_dashboard.py --solo-si-cambia` y `exportar_parquet_compacto.py`. |
| `Auxiliares/herramientas/generar_dashboard.py` | 402 | no | Genera `Data/dashboard.html` sin CDN; citado en §71.5 solo por su flag. |
| `Auxiliares/herramientas/actualizar_numeros.py` | 153 | no | Actualiza los marcadores `<!-- kpi:… -->` del informe (§59). |
| `Auxiliares/herramientas/generar_sitio_mkdocs.py` | 242 | no | Regenera `docs/` y copia gráficos y panel (§61, §71.5). |
| `Auxiliares/herramientas/actualizar_informe.py` | 416 | yes | Docstring con `Uso:`, `--inicializar` y `--regenerar` (§13). |
| `Auxiliares/herramientas/test_smoke_pipeline.py` | 66 | yes | Docstring con comando de ejecución; ver Tests. |

### Tests

- Files: `Auxiliares/herramientas/test_dashboard.py` (92 LOC), `Auxiliares/herramientas/test_parquet_compacto.py` (83 LOC), `Auxiliares/herramientas/test_modelo.py` (84 LOC), `Auxiliares/herramientas/test_smoke_pipeline.py` (66 LOC)
- Total LOC: 325
- Framework: scripts (`main()` propio; no usan `pytest`; no hay `pytest.ini`/`conftest.py` propios; se ejecutan con `python3 …`)
- Tests cover (named): el nuevo `test_smoke_pipeline.py` cubre compilación de los scripts, existencia de 7 artefactos, legibilidad de 4 CSV y coherencia del comando único (`SEED = 20261127` presente en `run_all.py`); los otros tres cubren panel, Parquet compacto y esquema/coherencia de `modelo_muestra.csv`. §71.5 cita expresamente la prueba de humo.

### Documentation

| File | LOC |
|---|---|
| README.md | 105 |
| INFORME_TECNICO.md | 1.523 (la caché de texto de la iteración 3 tiene 1.523) |
| docs/ (32 archivos) | 2.495 LOC en Markdown + 6 HTML de gráficos + `dashboard.html` |
| Data/referencias.md | 82 (38 referencias numeradas) |
| reviews/ (31 archivos `.md`) | informe y forensic de la iteración 1, 13 artefactos de fase, artefactos y veredictos de la iteración 2, y plan de la iteración 3 |

### Environment

- requirements.txt: present, 14 líneas (2 comentarios + 12 dependencias), todas fijadas con `~=X.Y.0`; detalle en Declared artifacts
- pyproject.toml: absent
- environment.yml: absent
- Dockerfile: absent (FlareSolverr se declara como servicio Docker externo en §6)
- Other: `.gitattributes` con filtros LFS; `mkdocs.yml`; `Auxiliares/.venv` y `Auxiliares/.venv-py`; `Auxiliares/herramientas/integraciones/README.md`; systemd timers `precio-*` documentados en §64–§66
- Observation: §34 afirma «Instalé además `statsmodels 0.15`, `pyarrow 26`», mientras `requirements.txt` fija `statsmodels~=0.14.0` y `pyarrow~=14.0.0`. La declaración de reproducibilidad de §71.5 («dependencias fijadas a serie menor») se cumple sintácticamente, pero la serie fijada no coincide con la que §34 dice haber instalado.

### Heavy artifacts in repo

| Path | Size | Type |
|---|---|---|
| `Data/Revolico/revolico.sqlite` | 836 MB | sqlite (LFS) |
| `Data/Revolico/pipeline.sqlite` | 745 MB | sqlite (LFS) |
| `Data/dashboard.html` | 107,4 KB | html (panel autocontenido) |
| `Data/referencias.md` | 9,9 KB | markdown |
| `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` | 265 B | csv |

## Declared artifacts verified on disk (iteración 3)

### `requirements.txt` — fijación `~=X.Y.0` (§71.5)

- **Found in repo**: yes — 356 B, 14 líneas, 12 dependencias; todas con operador compatible `~=X.Y.0` (pandas 2.2.0, numpy 1.26.0, plotly 5.18.0, statsmodels 0.14.0, scipy 1.11.0, beautifulsoup4 4.12.0, curl_cffi 0.7.0, tenacity 8.2.0, trafilatura 1.6.0, pyarrow 14.0.0, mkdocs 1.6.0, mkdocs-material 9.5.0).
- **Claims supported (preliminary)**: §71.5 «Las dependencias están fijadas a serie menor en `requirements.txt`».
- **Observation**: el encabezado del propio archivo declara «Fijadas a versiones menores (criterio de reproducibilidad de nivel master)». La forma `~=X.Y.0` fija la serie menor y admite parches, tal como afirma el documento; la discrepancia de series respecto de §34 se registra en Environment.

### `SEED = 20261127` en `run_all.py` (§71.5)

- **Found in repo**: yes — `Data/analisis_rentabilidad/scripts/run_all.py` líneas 16–18: `SEED = 20261127`, `random.seed(SEED)`, `np.random.seed(SEED)`. El docstring (líneas 2–7) explica que la semilla se declara también en el informe como criterio de determinismo.
- **Claims supported (preliminary)**: §71.5 «La semilla `SEED = 20261127` está declarada en `run_all.py` y en este documento»; el propio §71.5 la reproduce con el mismo valor.
- **Observation**: `test_smoke_pipeline.py::test_comando_unico` verifica literalmente la cadena `SEED = 20261127` en el orquestador, de modo que la afirmación está respaldada por código y por prueba. Ninguna de las cinco etapas (`01_ingest.py` … `05_benchmark.py`) consume la semilla directamente; el docstring lo anticipa al describir las etapas como deterministas.

### `Auxiliares/herramientas/test_smoke_pipeline.py` (§71.5)

- **Found in repo**: yes — 66 LOC, cuatro funciones (`test_compila`, `test_artefactos`, `test_csv_legibles`, `test_comando_unico`) y `main()` que imprime «4 pruebas superadas».
- **Claims supported (preliminary)**: §71.5 «Prueba de humo: `python3 Auxiliares/herramientas/test_smoke_pipeline.py`».
- **Observation**: la ruta y el intérprete citados coinciden con el docstring del script. Las siete rutas que exige `test_artefactos` incluyen `kpis.csv`, `modelo_muestra.csv`, `modelo_depreciacion.csv`, `Data/dashboard.html`, `MANIFEST.json`, `Data/referencias.md` e `INFORME_TECNICO.md`; por tanto la prueba de humo es, en parte, una comprobación de existencia de los artefactos inventariados aquí.

### `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` (§59, §71.2)

- **Found in repo**: yes — 265 B, cabecera + 2 filas; columnas `modelo,candidatas,observaciones,r2,p_f,terminos`.
- **Content**: `principal`: 981 candidatas / 584 observaciones / R² 0,101 / p_f 0,0; `completo`: 981 candidatas / 28 observaciones / R² 0,2744 / p_f 0,4114; términos `log_price ~ car_age + np.log1p(mileage_km) + condition_score + C(brand_tier)` y la variante con `hp`.
- **Claims supported (preliminary)**: §59 «28 observaciones completas» de «981 candidatas», R² 0,277 y p del F 0,411; §71.2 «la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² baja de 0,274 a 0,101». Coinciden candidatas, observaciones y p; el R² del modelo completo se redondea en el texto (0,2744 → 0,274 / 0,277).
- **Observation**: el CSV respalda la ablación descrita en §71.2 sin ambigüedad de muestra. Compañeros: `modelo_depreciacion.csv`, `modelo_resumen.txt`, `vif.csv`, `tests.csv` y `kpis.csv` en el mismo directorio.

### `Data/referencias.md` (§70)

- **Found in repo**: yes — 10.121 B, 82 líneas, 38 entradas numeradas `[1]`…`[38]`; generado el 27/11/2026 desde `reviews/informe-tecnico-2026-11-27.e2-literature.md`.
- **Content**: una línea por referencia con autores, título, revista, año, DOI/URL, campo `Citada en el informe: yes/no` y marca `(metadata incomplete)` cuando un campo no se confirmó; la entrada [38] consigna además una discrepancia de año entre OpenAlex y Crossref.
- **Claims supported (preliminary)**: §70 «La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`».
- **Observation**: el propio §70 distingue cuatro fuentes verificadas en vivo (Akerlof 1970, DfT/DVLA, ANFAC, AEADE) y remite el resto a `e2-literature.md`. Dentro de `referencias.md` solo aparece la marca negativa `(metadata incomplete)`; no hay etiqueta positiva que distinga esas cuatro, por lo que la condición «verificadas» debe cotejarse con el artefacto E2, como el texto indica.

### Panel interactivo — `Data/dashboard.html` (§61, §71.5)

- **Found in repo**: yes — 109.929 B, `<title>Panel interactivo — El precio de moverse en Cuba</title>`; copia idéntica en `docs/dashboard.html` y salida en `site/dashboard.html`; generado por `Auxiliares/herramientas/generar_dashboard.py` (402 LOC).
- **Type**: HTML autocontenido (vanilla JS + SVG, sin CDN ni peticiones externas) con gráficos, mapa de servicios y mapa de circuitos; §71.5 registra su regeneración con `--solo-si-cambia`.
- **Rendered in document**: no (la caché de texto no incrusta ni nombra esta ruta; §22/§23 citan los dashboards antiguos de `Data/analisis/`, mientras §59 describe un «apéndice visual con cinco cuadros y seis gráficos reales»).
- **Claims supported (preliminary)**: visualización de KPIs y estado de circuitos; probado por `Auxiliares/herramientas/test_dashboard.py` y por la prueba de humo.
- **Observation**: el panel existe, está versionado y se regenera desde `run_all.py`, el job de circuitos y el generador del sitio, pero el informe solo lo nombra de forma indirecta al citar a su generador en §71.5. Un lector que siga únicamente el informe encontrará primero los dashboards históricos de `Data/analisis/`.

### `reviews/` — registro de auditoría (§69–§70)

- **Found in repo**: yes — 31 archivos `.md` al cierre de este inventario.
- **Content**: informe narrativo y forensic de la iteración 1, los trece artefactos de fase que §69 denomina «los trece artefactos de fase», el informe/forensic/artefactos de la iteración 2 y, de la iteración 3, `informe-tecnico-2026-11-27-iter3.plan.md`. Este archivo `…iter3.e3-artifacts.md` se escribe en paralelo; no había veredictos ni informe de la iteración 3 al cerrar el inventario.
- **Claims supported (preliminary)**: §69 «sus resultados se conservan en `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` junto con los trece artefactos de fase»; §70 «Las fuentes restantes figuran con estado `(metadata incomplete)` en `reviews/informe-tecnico-2026-11-27.e2-literature.md`».
- **Observation**: ambas rutas existen y el conteo de artefactos de fase es correcto para la iteración 1, que es a la que se refiere §69. La frase «el registro de auditoría en `reviews/`» de §69 describe una práctica vigente, no un estado ya completo para la iteración 3.

## Datasets

| Name | Source | ID | Publicly accessible | Notes |
|---|---|---|---|---|
| Revolico scraped ads database | custom (own scrape) | `Data/Revolico/revolico.sqlite` | unknown | §66 reporta 6.955 anuncios `done`; §68: tres copias partidas. |
| Revolico pipeline queues | custom | `Data/Revolico/pipeline.sqlite` | unknown | Colas y clasificación; §66 regla de rechazo de candidatos. |
| Dealer and marketplace catalogues | custom | `Data/catalogos_concesionarios/` | unknown | §9: 11 bases y 256 filas. |
| Compact Parquet listings | derivado del pipeline | `Data/analisis_rentabilidad/data/compacto/` + `MANIFEST.json` | yes (en repo) | Usado por la prueba de humo y por `exportar_parquet_compacto.py`. |
| Profitability-model sample | derivado del pipeline | `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` | yes (en repo) | Respalda §59 y §71.2. |
| Numbered reference list | bibliográfico (OpenAlex/Crossref) | `Data/referencias.md` | yes (en repo) | 38 entradas; respalda §70. |
| Consolidated reference-repository tables | custom (derived) | `Data/repos-autos-referencias/referencias_autos.sqlite` | unknown | §50: 25 tablas, 3.958 anuncios. |
| elTOQUE TRMI | non-official | `Anexos/Investigacion Cambios/trmi_USD.csv` | unknown | §23/§52: serie diaria; el modelo usa TRMI fija de 930 CUP/USD de `config.py`. |
| ONEI statistical yearbooks | official (ONEI Cuba) | `Data/fuentes-oficiales/ONEI/` | yes | §53/§56: 12 anuarios. |
| UK DfT/DVLA vehicle statistics | official | gov.uk | yes | §18/§70: verificado en vivo. |

## Tables

Tables: none-detected (no aparecen marcadores numerados `Tabla N` / `Table N` en la caché de texto). Se inventarían las tablas Markdown sin numerar.

### Table (unnumbered) — «Fase | Nombre | Estado» (§2, ES)

- **Section**: §2 Estado y fases (p. n/a)
- **Lines**: 24–34
- **Columns**: Fase, Nombre, Estado
- **Rows**: 9
- **Claims supported** (preliminary): fase activa 6; fases 7–9 pendientes; nota de actualización de 27/11 en línea 38.

### Table (unnumbered) — «Búsqueda | Páginas | Resultados | Útiles | Parada» (§7, ES)

- **Section**: §7 Fase 4 — Corpus documental (p. n/a)
- **Lines**: 80–84
- **Columns**: Búsqueda, Páginas, Resultados, Útiles, Parada
- **Rows**: 3

### Table (unnumbered) — «Tienda | Filas | Con precio» (§9, ES)

- **Section**: §9 Fase 6 — Scraping y captura (p. n/a)
- **Lines**: 96–108
- **Columns**: Tienda, Filas, Con precio
- **Rows**: 11
- **Claims supported** (preliminary): «11 bases» y «256 filas».

### Table (unnumbered) — «Problema | Solución» (§11, ES)

- **Section**: §11 Problemas y soluciones (p. n/a)
- **Lines**: 124–131
- **Columns**: Problema, Solución
- **Rows**: 6

### Table (unnumbered) — espejo inglés de §2/§7/§9/§11

- **Section**: §2, §7, §9, §11 EN (p. n/a)
- **Lines**: 155–165, 211–215, 227–239, 255–262
- **Rows**: 9, 3, 11, 6
- **Observation**: el espejo inglés de §12 no reproduce la conclusión 5 del original: donde §139 afirma que el modelo de rentabilidad está implementado, la línea 270 afirma «The interactive product and profitability model (phase 8) are not implemented yet».

### Table (unnumbered) — «Fecha / Date | Ruta / Path | … | Estado / Status» (§13)

- **Section**: §13 Registro de altas / Change log (p. n/a)
- **Lines**: 280–682+ (marcador `<!-- REGISTRO_ALTAS -->` en 282; múltiples instantáneas)
- **Columns**: ocho columnas según la cabecera
- **Rows**: varies; la línea 295 declara «175 entradas adicionales no listadas / omitted»
- **Claims supported** (preliminary): inventario automático de altas, tamaños y fases; regenerado por `actualizar_informe.py`.

### Table (unnumbered) — «Tabla | Registros» (§29)

- **Section**: §29 Base de datos de Telegram (p. n/a)
- **Lines**: 964–968
- **Rows**: 4

### Table (unnumbered) — «Métrica | Valor» (§34)

- **Section**: §34 Esqueleto de análisis de rentabilidad (p. n/a)
- **Lines**: 1043–1054
- **Rows**: 10
- **Claims supported** (preliminary): línea base histórica (972 ingeridas, 499 limpias, 376 rechazos, 32 marcas, mediana 24.000 USD, −5,43 %/año); §59–§60 ya no sostienen esa pendiente.

### Table (unnumbered) — «Base / Baseline | Descripción | Métrica observada» (§71.1)

- **Section**: §71.1 Bases de comparación (p. n/a)
- **Lines**: 1489–1493
- **Rows**: 3
- **Claims supported** (preliminary): mediana global (MAE 18.220,46 USD sobre 1.444 anuncios), Egyptian-Used-Cars y modelo principal propio (R² 0,101 sobre 584 observaciones).

## Figures

Figures: none-detected (no aparecen marcadores numerados `Figura N` / `Figure N` en la caché de texto). Los gráficos reales se inventarían como artefactos:

- §59 (línea 1381) declara «un apéndice visual con cinco cuadros y seis gráficos reales»; §61 (línea 1399) declara que los seis gráficos Plotly se copian a `docs/graficos/` y se enlazan desde el apéndice, y que las tablas se generan desde los CSV. En disco: `docs/graficos/`, `docs/historia/apendice/` y `site/historia/apendice/`, además de `Data/analisis/graficos/` (8 PNG históricos).
- Panel interactivo: ver el artefacto `Data/dashboard.html` más arriba. No está incrustado ni nombrado por su ruta en el texto cacheado.
- **Rendered in document**: no (solo referencias discretas entre paréntesis, según §59).

## Missing artifacts

### Apéndice visual (cinco cuadros y seis gráficos)

- **Mentioned in document**: §59 (p. n/a): «Se añadió además un **apéndice visual** con cinco cuadros y seis gráficos reales».
- **Found in repo**: yes (`docs/graficos/`, `docs/historia/apendice/`, `site/historia/apendice/`)
- **Observation**: el apéndice existe como artefacto generado y el texto lo declara, pero la caché de texto auditada no contiene sus cuadros ni sus gráficos: solo la mención. Las cifras del apéndice dependen de los CSV y del HTML generados, que quedan fuera del documento texto y deben cotejarse con el sitio o con `outputs/tables/`.

### Ruta `Data/dashboard.html`

- **Mentioned in document**: §71.5 (p. n/a): «Puntos de entrada con argumentos: `generar_dashboard.py --solo-si-cambia`…».
- **Found in repo**: yes (109.929 B, con copia en `docs/`)
- **Observation**: el documento cita el generador y su flag, pero nunca declara la ruta del panel que produce. Las únicas rutas HTML explícitas en la caché pertenecen a `Data/analisis/` (líneas 578, 604, 892), derivadas de una etapa anterior. La existencia del artefacto vigente es verificable, pero no desde la lectura literal del informe.

### Series de dependencias declaradas en §34

- **Mentioned in document**: §34 (p. n/a): «Instalé además `statsmodels 0.15`, `pyarrow 26`…».
- **Found in repo**: partial (`requirements.txt` fija `statsmodels~=0.14.0`, `pyarrow~=14.0.0`)
- **Observation**: el entorno declarado en §71.5 existe y está fijado, pero las series que §34 atribuye a la instalación real no coinciden con las del archivo de dependencias. No es un archivo ausente: es una divergencia entre dos artefactos que describen el mismo entorno.

## Code-to-document mapping (when discernible)

| Document component | Repo location |
|---|---|
| Semilla declarada y comando único (§71.5) | `Data/analisis_rentabilidad/scripts/run_all.py` |
| Dependencias fijadas a serie menor (§71.5) | `requirements.txt` |
| Prueba de humo (§71.5) | `Auxiliares/herramientas/test_smoke_pipeline.py` |
| Ablación de `hp` (§59, §71.2) | `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` |
| Inventario de funciones y modelos (§60) | `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md` |
| 38 referencias y su estado (§70) | `Data/referencias.md` |
| Fuentes con `metadata incomplete` (§70) | `reviews/informe-tecnico-2026-11-27.e2-literature.md` |
| Registro de auditoría (§69) | `reviews/` |
| Panel regenerado (§61, §71.5) | `Data/dashboard.html` <- `Auxiliares/herramientas/generar_dashboard.py` |
| Esqueleto del pipeline (§34) | `Data/analisis_rentabilidad/` |
| Línea base de 972/499 filas (§34) | `Data/analisis_rentabilidad/` (tablas históricas) |
| Sitio MkDocs y apéndice (§61) | `docs/`, `site/`, `mkdocs.yml` |

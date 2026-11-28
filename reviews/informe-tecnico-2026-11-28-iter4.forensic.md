---
type: audit-forensic
slug: informe-tecnico-2026-11-28-iter4
generated_at: 2026-11-28T12:00:00-05:00
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
  plan: informe-tecnico-2026-11-28-iter4.plan.md
  e1: informe-tecnico-2026-11-28-iter4.e1-claims.md
  e2: informe-tecnico-2026-11-28-iter4.e2-literature.md
  e3: informe-tecnico-2026-11-28-iter4.e3-artifacts.md
  v1: informe-tecnico-2026-11-28-iter4.v1-structure.md
  v2: informe-tecnico-2026-11-28-iter4.v2-methodology.md
  v3: informe-tecnico-2026-11-28-iter4.v3-results-evidence.md
  v4: informe-tecnico-2026-11-28-iter4.v4-novelty.md
  v5: informe-tecnico-2026-11-28-iter4.v5-state-of-the-art.md
  v6: informe-tecnico-2026-11-28-iter4.v6-reproducibility.md
  v7: informe-tecnico-2026-11-28-iter4.v7-writing.md
  v8: informe-tecnico-2026-11-28-iter4.v8-bibliography.md
  v9: informe-tecnico-2026-11-28-iter4.v9-ethics.md
  forensic: informe-tecnico-2026-11-28-iter4.forensic.md
previous_iterations: [reviews/informe-tecnico-2026-11-27.md, reviews/informe-tecnico-2026-11-27-iter2.md, reviews/informe-tecnico-2026-11-27-iter3.md]
---
# Auditoría forense — Iteración 4

## §0 — Resumen del documento

El documento auditado es `INFORME_TECNICO.md`, «Informe técnico / Technical report — El precio de moverse en Cuba», con autoría por rol («responsable del proyecto / project owner»), fecha 23/11/2026 y estado «Fase 6 — scraping y captura de catálogos y anuncios, en curso». Es bilingüe, con 1.605 líneas y 31.305 palabras en la copia cacheada. El objetivo declarado es caracterizar estructura, precios, oferta, segmentos, tendencias, asequibilidad y rentabilidad del mercado automotor cubano, con el producto interactivo diferido.

El resumen VSN-C (L14–19) enuncia visión, pasos, novedad y cuatro contribuciones; la hipótesis H1 (L21/L163) se declara rechazada con Kruskal-Wallis a p<0,001. §59 fija las cifras canónicas vigentes (974 autos, 2.174 anuncios, mediana 21.000 USD, 32.569 km, 50 marcas, 114 grupos, 89 anomalías); §60 reporta no significancia con p mínimo 0,0941 y VIF 1,12–1,40; §71.2 documenta la ablación de `hp` y §71.3 el contraste con IC bootstrap. El diferenciador se formula en §71.6: procedencia y normalización, no algoritmo.

Los artefactos son verificables en `main` (HEAD `77ab644`): bases crudas bajo LFS reconstruibles, panel autocontenido de 109.929 bytes, 41 referencias numeradas y 45 artefactos de auditoría previos. La cuarta pasada re-ejecuta E1–E3 y V1–V9 sin dimensiones omitidas ni fallos de subagentes. Frente a la iteración 3 se añaden resumen y abstract VSN-C, H1 con desenlace, dos bases con MAE e IC, semilla propagada por `PROYECTO_SEED`, marcadores `[N]` en §71.6, sección §71.15 de declaraciones y paralelos ingleses; §69 se comprime de 271 a 147 palabras y los marcadores `<!-- kpi:… -->` suben de 4 a 29.

## §1 — v1-structure


# V1 — Structure (findings)

### F-V1-001 — Resumen VSN-C e hipótesis H1 incorporados en ambas partes; contribuciones solo en el resumen

La iteración 4 incorpora «## Resumen (VSN-C)» (L14–19) y «## Abstract (VSN-C)» (L156–161), con los cuatro rótulos «**Visión» / «**Pasos» / «**Novedad» / «**Contribuciones» y «**Vision» / «**Steps» / «**News» / «**Contributions»; en la iteración 3 no figuraban resumen ni abstract (revisión V1 de aquella iteración, F-V1-001). La novedad se enuncia como objeto de auditoría —«la procedencia y la normalización se tratan como objeto de auditoría; la pérdida de muestra por variables ausentes se reporta como hallazgo y no se oculta» (L18; «provenance and normalisation are treated as an audit object», L160)— y las contribuciones quedan enumeradas en una línea por parte: «base compacta reproducible, panel interactivo autocontenido, pipeline con timers y un expediente de auditoría con 13 artefactos» (L19) / «a reproducible compact database, a self-contained interactive dashboard, a timer-driven pipeline and an audit trail with 13 artifacts» (L161). No hay sección autónoma «Contribuciones»: §12 sigue siendo una lista de cinco conclusiones (L144–148, L286–290) y §71.6 conserva «el aporte es de procedencia y normalización, no de algoritmo» (L1549; texto ya presente en la iteración 3, L1520). El encabezado mantiene seis campos (L3–8) y la firma por rol (L1604–1605), sin dedicatoria, agradecimientos ni dictamen de tutor.

H1 se formula en ambas partes —«los precios de los tres tiers de marca en el mercado local provienen de la misma distribución, controlando por antigüedad y kilometraje» (L21) / «prices across the three brand tiers in the local market come from the same distribution, controlling for age and mileage» (L163)—, con contraste y desenlace declarados: «Se contrasta con Kruskal-Wallis; se rechaza con p < 0,001 en la corrida vigente». La proposición de igualdad de distribuciones admite refutación, y la cadena «hipótesis / hypothesis» pasa de cero ocurrencias en la iteración 3 a dos en la 4. El respaldo numérico aparece sin apuntador de sección: §60 registra «Kruskal-Wallis p = <!-- kpi:kw_p -->0,00000» (L1409) y §71.3 «H = 44,313» (L1528), mientras la depreciación «−5,43 % anual (p<0,001)» de §34 (L1076) queda rotulada «Línea base real de la primera ejecución» (L1061).

— polarity: positive · confidence: high · related: [[#F-V1-003]]

### F-V1-002 — Duplicidad 1–12 declarada, salto de nivel de §13 cerrado e inversión 71.15/71.14 en la sección final

La numeración se reinicia en «# Part II — English» (L152): dos «1. Objetivo / Objective» (L23, L165) y dos «12. Conclusiones / Conclusions» (L142, L284), con una secuencia única §13–§71 (L294, L1505). La iteración 4 añade «*Nota: la numeración de secciones se reinicia en esta parte; las referencias cruzadas se interpretan dentro de cada parte.*» (L154), ausente en la iteración 3 (L143). El salto de nivel de §13 señalado en aquella revisión queda cerrado: `# 13. Registro de altas / Change log` (iteración 3, L274) pasa a `## 13. Registro de altas / Change log` (L294), aunque el bloque bilingüe sigue situado entre las dos partes y fuera de ellas.

La sección 71 enumera 71.1–71.6 en orden (L1507, L1520, L1526, L1532, L1541, L1547) y continúa con «### 71.15 Declaraciones / Declarations» (L1551) antes de «### 71.14 Obras del mapa literario citadas en el cuerpo» (L1557): ambas subsecciones son nuevas frente a la iteración 3, que cerraba en 71.6 (L1522), y la secuencia 71.15 → 71.14 invierte la numeración. En 71.1, la fila «| Modelo principal propio | OLS de log-precio con antigüedad, km, condición y tier | R² 0,101 sobre 584 observaciones |» (L1516) aparece separada de la tabla de tres filas (L1509–L1513) y detrás del párrafo de cierre (L1515). Persisten los títulos de bitácora —«Reescritura de la sección 3 del storytelling» / «Apertura de la sección 3 del storytelling» / «Reescritura de la sección 4 del storytelling» (L1232, L1240, L1248)—.

— polarity: negative · confidence: high · related: []

### F-V1-003 — Apuntadores § con destino existente y cero marcadores `??`; 29 etiquetas `kpi` sin resolver en prosa

Los diez apuntadores § del texto tienen encabezado destinatario: «§34» y «§59–§60» en las notas de actualización de §2 de ambas partes (L47, L189), «(§34)» en §44 y «§59» en §45 (L1226, L1234), «§71.5» en la declaración de §69 (L1553, L1555) y «§71.6» en el cierre de §70 (L1600). Los destinos existen en §34 (L1036), §59 (L1397), §60 (L1407), §71.5 (L1541) y §71.6 (L1547); el apuntador de §44 añade además una advertencia de vigencia —«cifra que la corrida vigente ya no sostiene» (L1226)—. La búsqueda de `??`, `\ref{}`, `Tabla ?` y `Figure ?` da cero coincidencias tanto en la iteración 4 como en la 3.

Frente a cuatro marcadores `<!-- kpi:... -->` en la iteración 3 (L1381), la iteración 4 conserva 29 apariciones —23 etiquetas distintas— intercaladas en la prosa: 13 en §59 (L1399, L1401), 3 en el resumen EN de §59 (L1403), 4 en §60 (L1409), 2 en cada fila de la tabla de baselines de §71.1 (L1511–L1512), 3 en el resumen EN de §71.1 (L1518) y 2 en §71.3 (L1528). Los valores numéricos aparecen a continuación de la etiqueta —«<!-- kpi:kw_p -->0,00000» (L1409), «<!-- kpi:ci_bajo -->10.000» (L1528)—, de modo que el marcador de plantilla queda visible en el texto cacheado y en los resúmenes bilingües de §59 y §71.1.

— polarity: neutral · confidence: high · related: [[#F-V1-001]]

## Resumen

- El resumen VSN-C, la hipótesis H1 falsable y las cuatro contribuciones aparecen ahora en ambas partes; no hay sección autónoma de contribuciones ni dedicatoria, agradecimientos o dictamen de tutor.
- La duplicidad 1–12 se declara explícitamente y §13 ya no rompe el nivel de encabezado, pero §71.15 precede a §71.14 y una fila de la tabla de baselines queda fuera de la tabla.
- Los diez apuntadores § resuelven y no hay `??` ni `\ref{}`; los marcadores `<!-- kpi:... -->` pasan de 4 en la iteración 3 a 29 en la 4.


## §2 — v2-methodology


# V2 — Methodology (findings)

### F-V2-001 — Dos bases triviales con MAE publicado, sin base adyacente al estado del arte operacionalizada

La §71.1 (L1509–L1518) enumera tres entradas: «Mediana global ( ingenua )» (MAE 18.188,34 USD sobre 1.462 anuncios), «Mediana por marca» (MAE 16.603,28 USD sobre 1.462 anuncios) y «Egyptian-Used-Cars» como «Referencia de ingeniería del campo: 23.500 anuncios y series mensuales» con «Contraste cualitativo de cobertura y frescura». Ambas medianas sí están calculadas sobre los datos propios y publicadas en `Data/analisis_rentabilidad/outputs/tables/baselines.csv` (dos filas, n=1462, `mae_usd` 18188.34 y 16603.28), generadas por `scripts/03b_baselines.py:16–37`. La referencia egipcia no aparece en ese CSV ni lleva métrica calculada sobre la muestra local; la cuarta fila de la sección es el modelo propio, no una base externa. El espejo inglés de §71.3 (L1530) consigna: «an operationalised SOTA baseline is still missing», y los trabajos cercanos de §71.6 (L1549: [14] Gegić, [26] Muça, [9] Du) se usan para posicionamiento argumentativo, sin métrica reproducible. El criterio `V2.baselines` para `level=master` se lee: «≥2 baselines, one of which corresponds to a SOTA-adjacent approach in the field». El recuento de dos bases se satisface; la condición de adyacencia al estado del arte no queda operacionalizada en la sección ni en los artefactos citados.

— polarity: negative · confidence: high · related: [[#C013]], [[#C011]] · criteria: V2.baselines.master

### F-V2-002 — Ablación explícita del término `hp`, con especificación y muestra informadas conjuntamente

La §71.2 (L1520–L1524) etiqueta como ablación la retirada de `hp` y declara que «la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² baja de 0,274 a 0,101», con la salvedad de que «el cambio de especificación y el cambio de muestra se informan juntos». `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` registra dos ajustes diferenciados por ese término: `completo` (28 observaciones, R² 0,2744, p_f 0,4114, con `hp`) y `principal` (586 observaciones, R² 0,1008, sin `hp`), ambos sobre 993 candidatas. El criterio `V2.ablations` para `level=master` se lee: «Explicit ablation of at least one component». La ablación existe, está nombrada como tal y cuantifica el efecto, de modo que el estándar de nivel queda cubierto. Como matiz observacional, la retirada del componente coincide con un cambio de muestra (28 frente a 584 en el texto, 28 frente a 586 en el CSV vigente), de modo que el contraste presentado no separa el efecto del término del efecto de la selección de anuncios con kilometraje declarado; el propio párrafo atribuye a esa selección el signo positivo de antigüedad.

— polarity: positive · confidence: high · related: [[#C004]], [[#C005]], [[#C014]], [[#F-V2-007]] · criteria: V2.ablations.master

### F-V2-003 — H1 declara control por antigüedad y kilometraje sin contraste ajustado en los artefactos

El enunciado de H1 (L21 y L163) afirma que «los precios de los tres tiers de marca en el mercado local provienen de la misma distribución, controlando por antigüedad y kilometraje» y que se rechaza con Kruskal-Wallis. `outputs/tables/comparaciones.csv` contiene una sola fila: n=1462, `estadistico` 44.313, `p_valor` 0.0, IC 10.000–29.500 y método «Kruskal-Wallis + bootstrap de mediana premium-economico (2000 replicas)». En `scripts/03c_comparaciones.py:31–48` el test compara únicamente `price_usd` entre grupos de `brand_tier` y el bootstrap remuestrea solo esas medianas; ni el test ni el intervalo incluyen antigüedad ni kilometraje como covariables. La única evidencia ajustada del checkout, `outputs/tables/modelo_depreciacion.csv`, da coeficientes de tier con p=0,1421 (económico), p=0,0941 (medio) y p=0,8753 (premium), y coeficientes de `car_age` (p=0,1504) y `np.log1p(mileage_km)` (p=0,4711) sin significancia. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)». La §71.3 (L1528) declara diseño no pareado, de modo que los tests pareados del criterio no son aplicables y el bootstrap CI sí está presente; la condición «controlando por antigüedad y kilometraje» del enunciado no tiene, sin embargo, contraste ajustado que la sostenga entre las tablas publicadas.

— polarity: negative · confidence: high · related: [[#C001]], [[#C003]], [[#C005]] · criteria: V2.statistical_tests.master

### F-V2-004 — El Kruskal-Wallis citado incluye cuatro grupos, uno de ellos `desconocido`

La §71.3 (L1528) cuantifica «el contraste central» con H = 44,313 en el marco de los tres tiers de H1. `scripts/03c_comparaciones.py:25–35` filtra anuncios usados, locales, con precio positivo y `brand_tier` no nulo, y construye los grupos con `len(g) > 5`. Sobre el `data/listings_clean.parquet` vigente, esos grupos son `desconocido` (248), `economico` (133), `medio` (949) y `premium` (132): cuatro categorías, una de las cuales es la clase de marca faltante definida en `config.py:91–99`, no un tier de marca. El bootstrap del mismo script (L37–L48) sí usa solo `premium` y `economico`. El texto de §71.3 no consigna la presencia de la categoría `desconocido` en el estadístico omnibus. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)»; la elección de un test de grupos independientes es coherente con el diseño declarado, mientras que la composición de los grupos del contraste informado no se corresponde con los tres tiers enunciados.

— polarity: negative · confidence: high · related: [[#C001]], [[#C005]], [[#C012]] · criteria: V2.statistical_tests.master

### F-V2-005 — Dos valores de Kruskal-Wallis publicados para el mismo contraste

`outputs/tables/comparaciones.csv` informa `contraste=precio por tier de marca`, H=44.313 y n=1462; `outputs/tables/tests.csv` informa `test=Kruskal-Wallis precio por tier`, estadístico 32.818 y p_valor 0.0. Ambos archivos proceden de la misma regeneración (marcas de tiempo 28/11/2026 02:44 y 02:46) y aplican `stats.kruskal` (`scripts/03c_comparaciones.py:35` y `scripts/04_stats.py:105–109`), pero sobre marcos distintos: `04_stats.py` filtra además `car_age.notna()` y `car_age.between(0, 40)` antes de agrupar. La §71.3 (L1528) cita solo H = 44,313 y remite a `comparaciones.csv`; la §60 (L1409) reporta «Kruskal-Wallis p = 0,00000», valor compatible con ambas corridas. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)»; bajo ese criterio, la coexistencia de dos estadísticos con la misma etiqueta y la ausencia de una distinción explícita entre sus subamuestras queda como observación de consistencia entre declaraciones y artefactos.

— polarity: neutral · confidence: high · related: [[#C001]], [[#C005]] · criteria: V2.statistical_tests.master

### F-V2-006 — Welch declarado en §71.3 sin fila en `tests.csv` de la corrida vigente

La §71.3 (L1528) afirma: «se usan Kruskal-Wallis y Welch para grupos independientes», y la §60 (L1409) incluye el Welch t-test entre las funciones documentadas. En `scripts/04_stats.py:43` el marco `d` queda restringido a `source_type == "usado"`, y el bloque L110–L115 emite la fila «Welch t-test usado vs nuevo» solo si `d["is_new"].nunique() > 1` y ambos grupos superan cinco observaciones; con esa restricción la condición no se cumple. En consecuencia, `outputs/tables/tests.csv` contiene una única fila, la de Kruskal-Wallis. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)»: el test declarado en prosa no aparece en la tabla de tests de la corrida que el documento describe como vigente.

— polarity: negative · confidence: high · related: [[#C005]], [[#C011]] · criteria: V2.statistical_tests.master

### F-V2-007 — Recuentos de candidatas y observaciones divergen entre §59, §71 y `modelo_muestra.csv`

La §59 (L1401) reporta «28 observaciones completas de 993 candidatas»; la §71.1 (L1515–L1516) habla de «Las 981 candidatas» y de un modelo principal con «R² 0,101 sobre 584 observaciones»; la §71.2 (L1522) repite «de 981 candidatas» y «de 28 a 584 observaciones»; la §71.3 (L1528) fija «981 candidatas de 8 marketplaces». En el checkout, `outputs/tables/modelo_muestra.csv` (regenerado el 28/11/2026 a las 02:46) contiene `principal,993,586,0.1008` y `completo,993,28,0.2744`, mientras que `baselines.csv` y `comparaciones.csv` trabajan sobre 1462 anuncios. El criterio `V2.sample_size` para `level=master` se lee: «≥20 trials; ≥10 datasets/instances». La unidad declarada es el anuncio observacional, no el ensayo, y la propia §71.3 explica esa reconversión; el modelo principal supera el umbral numérico de 20, el completo se apoya en 28 observaciones y las fuentes declaradas son ocho, por debajo de diez. La asimetría entre 28, 586 y 1462 observaciones, junto con los dos recuentos de candidatas (981 frente a 993), permanece sin reconciliar dentro de la sección que declara los estándares de nivel.

— polarity: negative · confidence: high · related: [[#C002]], [[#C004]], [[#C005]] · criteria: V2.sample_size.master

### F-V2-008 — Subsección dedicada que cubre las cuatro categorías de amenaza a la validez

La §71.4 (L1532–L1539) dedica un apartado explícito a amenazas externas («solo La Habana y anuncios en línea; los precios son pedidos, no transaccionados»), de constructo («kilometraje y potencia faltan en la mayoría de los anuncios; la condición se infiere del texto»), internas («no hay asignación aleatoria; la ablación es observacional») y de conclusión estadística («el modelo completo usa 28 observaciones y ningún coeficiente alcanza p < 0,05»). El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations». El documento no solo cubre el mínimo de nivel sino que enumera las cuatro categorías reservadas al nivel `phd`, aunque sin mitigaciones ni declaración de replicabilidad, que son elementos del nivel `paper`. El apartado reformula además límites ya presentes en §18 y §19, lo que refuerza su coherencia con el resto del informe.

— polarity: positive · confidence: high · related: [[#C003]], [[#C012]], [[#C008]] · criteria: V2.threats_to_validity.master

### F-V2-009 — Protocolo de reproducción declarado con semilla, comando único y código referenciado

La §71.5 (L1541–L1545) consigna la semilla `SEED = 20261127`, el comando único `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py`, cuatro puntos de entrada con argumentos, dependencias «fijadas a serie menor en `requirements.txt`», la prueba de humo `python3 Auxiliares/herramientas/test_smoke_pipeline.py`, el repositorio público y la reconstrucción de las bases desde `chunks/MANIFEST.json`. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced». Los tres elementos están presentes y anclados a archivos del repositorio; la prueba de humo y el manifiesto de fragmentos exceden el mínimo del nivel. La propia sección declara «No se ha declarado todavía una licencia de datos o código», y no figura un commit o DOI fijado ni una versión de los datasets, elementos correspondientes a los niveles `phd` y `paper`.

— polarity: positive · confidence: high · related: [[#C006]], [[#C008]] · criteria: V2.reproducibility_protocol.master

### F-V2-010 — `PROYECTO_SEED` pasa a ser consumido por el bootstrap de `comparaciones.csv`

La §71.5 (L1543) afirma que la semilla «se propaga a cada etapa por la variable de entorno `PROYECTO_SEED`; antes se declaraba sin efecto». `scripts/run_all.py:16,23` fija `SEED = 20261127` y escribe `ENTORNO["PROYECTO_SEED"]`, que se entrega a los subprocesos mediante `env=ENTORNO` (L39). `scripts/03c_comparaciones.py:20` lee esa variable con valor por defecto 20261127 y L37 inicializa `np.random.default_rng(SEED)` para las 2000 réplicas del intervalo bootstrap publicado en `comparaciones.csv`. La búsqueda de `PROYECTO_SEED` en `scripts/*.py` encuentra ese único consumo; las llamadas `random.seed` y `np.random.seed` de `run_all.py:17–18` actúan en el proceso orquestador, mientras cada etapa se ejecuta en un intérprete nuevo. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced»: la declaración y el código coinciden y el contraste con intervalo es reproducible por la semilla declarada, con la salvedad de que el único consumidor de la variable es la etapa de comparaciones.

— polarity: positive · confidence: high · related: [[#C006]], [[#C005]], [[#F-V2-009]] · criteria: V2.reproducibility_protocol.master


## §3 — v3-results-evidence


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


## §4 — v4-novelty


## Resumen

- El cambio sustantivo de la iteración 4 es de aparato, no de novedad: §71.6 incorpora los marcadores `[14]`, `[26]`, `[9]` y `[29]` que faltaban en la iteración 3, con lo que el diferenciador declarado queda anclado a cuatro trabajos del mapa y se cierra la mitad formal de F-V10-006.
- `V4.differentiation_from_prior_art.master` y `V4.scope_of_novelty_claim.master` se satisfacen en el plano declarado (alcance local, sin primacías); `V4.prior_art_engagement.master` sigue en el umbral formal: una cláusula por trabajo, sin resultados ni limitaciones de los ajenos.
- No hay novedad confirmada ni sobreclaim: E2 reutiliza metadatos con `queries_run: 0` y `papers_l3: 0`, y siete obras del mapa continúan ausentes como discusión en el cuerpo.

### F-V4-001 — §71.6 ancla el diferenciador a cuatro trabajos del mapa con marcador numérico

El claim C013 (e1-claims, líneas 163–173; tipos `novelty`, `citation-grounded`) cita §71.6 (L1549): «Gegić y otros [14] predicen precios con aprendizaje automático sobre catálogos estructurados; aquí las variables se extraen de anuncios en lenguaje libre, así que el aporte es de procedencia y normalización, no de algoritmo». El mismo párrafo añade tres cláusulas contrastivas con marcadores: «Muça, Bani y Alla [26] integran datos públicos albaneses por scraping; en este trabajo el énfasis está en la conversión con TRMI fechada y en auditar la procedencia»; «Du y otros [9] modelan depreciación no lineal y heterogeneidad de marca con evaluación fuera de muestra; este informe no estima una tasa anual y reporta la pérdida de muestra como hallazgo»; «Vidal Alejandro y otros [29] estudian el mercado informal de divisas en Cuba; aquí esa tasa es una convención de conversión fechada, no el objeto de estudio». E2 (cluster 1, L20–24) constata que esas cuatro comparaciones «ahora sí llevan marcador numérico: `[14]`, `[26]`, `[9]` y `[29]`» y lo identifica como «el cambio sustantivo frente a la iteración 3, donde el mismo párrafo no tenía marcadores».

Los cuatro vecinos son los trabajos más cercanos del mapa E2 iter4: P001 / [9] — Du, Z.; Yang, Z.; Zhang, Y.; Li, S.; Liu, Y. (2026), «Nonlinear Depreciation and Brand Heterogeneity in Chinese Used-Car Listing Prices», *Advances in Economics, Management and Political Sciences*, DOI 10.54254/2754-1169/2026.38524; P002 / [14] — Gegić, E.; Isaković, B.; Keco, D.; Mašetić, Z.; Kevrić, J. (2019), «Car Price Prediction using Machine Learning Techniques», *TEM Journal*, DOI 10.18421/tem81-16; P003 / [26] — Muça, M.; Bani, K.; Alla, A. (2026), «A Pipeline for Integrating and Analyzing Public Business Data in Albania Using Web Scraping and Machine Learning», *IJACSA*, DOI 10.14569/ijacsa.2026.0170845; P004 / [29] — Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A. (2024), «Using AI in the informal currency market: evidence from Cuba», *Applied Economics*, DOI 10.1080/00036846.2024.2416091. E2 los marca `Cited in document: yes` con esas mismas ubicaciones. El contraste de §34 (L1080) añade `antecedentes [14], [18]` —P006 / [18]: Madhusudhanan, K.; Behrens, G.; Stubbemann, M.; Schmidt-Thieme, L. (2024), «ProbSAINT: Probabilistic Tabular Regression for Used Car Pricing», arXiv:2403.03812— dentro de la «Brecha frente a Egipto».

El criterio `V4.differentiation_from_prior_art` para `level=master` se lee: «Differentiator articulated with at least one explicit comparison paragraph to one closest prior work» (level-criteria.md, línea 88). El párrafo de §71.6 cumple esa condición y la supera en número, con un diferenciador declarado por vecino: procedencia y normalización frente a P002, conversión con TRMI fechada y auditoría de procedencia frente a P003, ausencia de tasa anual y reporte de pérdida de muestra frente a P001, y tasa informal como convención frente a P004. Queda corregida la mitad formal de F-V10-006, que en la iteración 3 se cerraba «parcialmente resuelta en engagement» por ausencia de marcadores (V4 iter3, F-V4-002); la mitad sustantiva —discusión de resultados o limitaciones de los trabajos ajenos— permanece abierta (F-V4-002).

— polarity: positive · confidence: high · related: [[#C013]], [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#P006]], [[#F-V10-006]], [[#F-V4-002]] · criteria: V4.differentiation_from_prior_art.master

### F-V4-002 — Engagement calibrado: marcadores ya presentes, pero una sola cláusula por trabajo y atribución errónea de [1]

El criterio `V4.prior_art_engagement` para `level=master` exige tres condiciones conjuntas: «Closest prior works cited, contrasted, and discussed in their own subsection» (level-criteria.md, línea 106). §71.6 (L1547–1549) es una subsección propia titulada «Posicionamiento frente a trabajos cercanos» y las tres condiciones aparecen: citados con marcador numérico, contrastados campo por campo y ubicados en apartado dedicado. La condición «discussed» queda sin embargo en el umbral formal: cada vecino recibe una caracterización de una frase («predicen precios con aprendizaje automático sobre catálogos estructurados», «integran datos públicos albaneses por scraping», «modelan depreciación no lineal y heterogeneidad de marca», «estudian el mercado informal de divisas en Cuba»), sin exposición de métodos, resultados ni limitaciones de esos trabajos. E2 (cluster 1, L24) registra que los cuatro flags de `Data/referencias.md` conservan el calificador «sin marcador numérico» pese a la presencia de los marcadores, y el cierre de §71.14 (L1600) afirma que «Los trabajos [1], [9], [14], [26] y [29] se discuten además en §71.6»: de los cinco, [1] no comparece en ese párrafo —Akerlof aparece sin marcador en la tabla de §17 (L817) y con `[1]` en §19 (L861)—, según constata E2 en P005 (L96). El estándar `phd` del mismo criterio («All closest prior works engaged with substantively (methods, results, limitations of each)», línea 107) queda fuera de alcance; el de master se cumple en la forma, no en la sustantividad de la discusión.

La discusión de resultados y limitaciones del documento —§59 (L1399–1401), §60 (L1409), §71.2 (L1522) y §71.4 (L1534–1537)— no enlaza sus hallazgos con las obras vecinas: la pérdida de muestra de 28 a 584 observaciones y el descenso de R² de 0,274 a 0,101 (§71.2, L1522) y las cuatro clases de amenazas (§71.4, L1534–1537) se enuncian sin marcador `[N]`. Además, el apartado de novedades no tiene paralelo inglés: tras §71.6 (L1549) viene directamente §71.15 (L1551), de modo que el posicionamiento solo existe en la Parte I. La lectura calibrada es: diferenciación resuelta (F-V4-001), engagement satisfecho en la forma con dos salvedades de registro —la atribución de [1] a §71.6 y la ausencia de resultados o limitaciones ajenos discutidos—.

— polarity: neutral · confidence: high · related: [[#C013]], [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#P005]], [[#F-V4-001]], [[#F-V4-004]] · criteria: V4.prior_art_engagement.master

### F-V4-003 — Alcance local sostenido: novedad de auditoría sin reclamación de primacía ni de componente

El claim C014 (e1-claims, líneas 175–185; tipos `novelty`, `methodological`) cita el Resumen VSN-C (L18): «**Novedad:** la procedencia y la normalización se tratan como objeto de auditoría; la pérdida de muestra por variables ausentes se reporta como hallazgo y no se oculta». C015 (L19) enumera «base compacta reproducible, panel interactivo autocontenido, pipeline con timers y un expediente de auditoría con 13 artefactos», cifra apoyada en la huella de la iteración 3 (L1489). El enunciado no contiene verbos de primacía («primero», «nuevo método», «contribución original»); las únicas comparaciones de escala —§34 (L1080), «solo 497 usados, un único snapshot, HP/kilometraje mayormente ausentes y un solo benchmark de auto nuevo»; §71.4 (L1534–1537)— se enuncian en dirección desfavorable al propio proyecto. Tampoco aparece sobreclaim contradicho por P001–P004: §71.6 renuncia explícitamente a novedad de algoritmo y a tasa de depreciación, y §1 (L25) difiere el producto interactivo.

El criterio `V4.scope_of_novelty_claim` para `level=master` se lee: «Component novelty + integration novelty: one of the two should be substantive» (level-criteria.md, línea 97). El lado de integración es sustantivo en su declaración frente a P002 —anuncios en lenguaje libre frente a catálogos estructurados— y frente a P004 —la tasa informal como convención de conversión fechada, no como objeto de estudio—; el reporte de pérdida de muestra tiene soporte interno verificable en §71.2 (L1522), §59 (L1401) y §60 (L1409), que documentan el cambio de especificación y la no significancia de los coeficientes. No se reclama novedad de componente ni se contrastan cifras del propio método contra las de los vecinos, de modo que la sustantividad queda en el plano de lo enunciado, no demostrado comparativamente. El alcance es local y así se declara; en ese marco la calibración master se satisface en el eje de integración, sin novedad confirmada en sentido fuerte.

— polarity: positive · confidence: high · related: [[#C014]], [[#C015]], [[#P001]], [[#P002]], [[#P004]], [[#F-V4-001]] · criteria: V4.scope_of_novelty_claim.master

### F-V4-004 — Inventario de marcadores [N]: §17 sin marcadores, §34 y §71.6 con remisiones, §71.14 completo hasta [38]

La verificación dirigida pedida arroja cuatro estados distintos. §17 (L811–832) contiene **0 marcadores numéricos**: Akerlof se menciona por nombre en la tabla de fuentes (L817) sin `[1]`, que aparece sí en §19 (L861). §34 (L1080) contiene `[14]` e `[18]` en la frase «La predicción de precios sobre catálogos estructurados tiene antecedentes [14], [18], ausentes del contraste original». §71.6 (L1549) contiene `[14]`, `[26]`, `[9]` y `[29]`, uno por vecino. §71.14 (L1557–1600) despliega 38 filas con marcadores `[1]`–`[38]` (L1561–1598) y repite `[1]`, `[9]`, `[14]`, `[26]` y `[29]` en el cierre (L1600). En prosa de cuerpo, las obras con marcador son seis: [1], [9], [14], [18], [26] y [29], coincidiendo con el inventario de E2 (cluster 2, L78–82; H2, L215–217).

E2 (H3, L219–221) constata cinco campos desactualizados en `Data/referencias.md` —[9], [14], [18], [26] y [29]—, un campo ausente en [39] y una contradicción de estado entre el flag de [39] y §18/§70; también observa que §70 generaliza el estado `(metadata incomplete)` a «las fuentes restantes» cuando solo cuatro entradas lo llevan (L201). Son desajustes del aparato de flags, no de la reclamación de novedad: los marcadores existen en el cuerpo auditado y sostienen el contraste de §71.6. La salvedad que sí toca al engagement es la atribución de [1] a §71.6 en L1600, ya consignada en F-V4-002.

— polarity: neutral · confidence: high · related: [[#C009]], [[#C013]], [[#P001]], [[#P002]], [[#P005]], [[#P006]], [[#F-V4-002]] · criteria: V4.prior_art_engagement.master

### F-V4-005 — Sin novedad confirmada: mapa reutilizado, sin búsquedas nuevas ni lectura L3

El frontmatter de E2 iter4 declara `queries_run: 0`, `papers_l1: 9`, `papers_l2: 9`, `papers_l3: 0`, y la nota de entrada (L16) precisa que «no se ejecutaron búsquedas web nuevas ni re-lecturas de resúmenes —los metadatos se reutilizan del mapa E2 de la pasada 1 y de la verificación OpenAlex/Crossref del 27/11/2026—», con capas L1/L2 «heredadas, no nuevas». La limitación declarada al cierre (L234) es explícita: «sin búsqueda bibliográfica nueva, sin re-lectura de resúmenes y sin re-fetch de URLs; este mapa sirve para coherencia interna de marcadores y flags, no para proponer obras adicionales ni para certificar enlaces». En consecuencia no hay antecedente nuevo capaz de desplazar a P001–P004 como vecinos más cercanos, pero tampoco lectura L3 que permita afinar el solapamiento: los cuatro figuran como `Layer: L2` «sin nueva lectura de resumen».

La sección `Likely missing important works` (L203–205) mantiene siete obras arrastradas de la iteración 3 —Lewis (2011) [2], Englmaier et al. (2017) [4], Krotov et al. (2020) [21], Priestley et al. (2023) [23], Brown et al. (2025) [22], Guerra (2015) [33] y Hohensinner et al. (2026) [24]—, presentes en `Data/referencias.md` con `Citada: no` y ausentes como discusión en el cuerpo; Gegić [14] queda fuera de la lista «porque sí tiene discusión comparativa en §71.6 y marcadores en §71.6 y §34». Bajo `V4.prior_art_engagement.master` (level-criteria.md, línea 106) la lectura permitida es «sin antecedente nuevo añadido en esta pasada», no ausencia de arte previo ni validación de originalidad; una conclusión de «novedad confirmada» excedería esta evidencia.

— polarity: neutral · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#P005]], [[#C013]], [[#C014]], [[#F-V4-001]], [[#F-V4-003]] · criteria: V4.prior_art_engagement.master


## §5 — v5-state-of-the-art


- Cobertura: seis de 38 trabajos del mapa llevan marcador en prosa de cuerpo (15,8 %, frente a cinco en la iteración 3); los cuatro clústeres principales y adyacentes tienen al menos una mención, pero el de señales sigue en 0/3 y el total queda lejos del tramo 25–60 de `V5.coverage_breadth.master`.
- Actualidad: 18 de 38 referencias fechadas (47,4 %) son de 2022–2026 y cuatro de seis citas en cuerpo (66,7 %) son recientes, por encima del 40 % de `V5.recency.master`, con clásicos balanceados.
- Peso y ausencias: §71.6 incorpora cuatro marcadores y satisface «fuente + autor» en C013, pero 12 de 15 afirmaciones load-bearing (80 %) siguen sin cita externa; las siete ausencias probables se mantienen y el anexo queda en 9 fichas `sí` / 32 `no`.

### F-V5-001 — Cobertura por clúster — seis de 38 trabajos con marcador en el cuerpo; el clúster de señales permanece en 0/3

La tabla de §71.14 (L1559–L1600) reparte 38 trabajos numerados en cinco clústeres: asimetría de información 8 ([1]–[8]), modelos de precio, regresión hedónica y depreciación 12 ([9]–[20]), ética/legalidad/procedencia/calidad de datos 8 ([21]–[28]), Cuba/divisas informales/movilidad/asequibilidad 7 ([29]–[35]) y señales de precio en marketplaces 3 ([36]–[38]). En prosa de cuerpo aparecen seis con marcador: [1] en §19 (L861) y mención nominal en §17 (L817); [9], [14], [26] y [29] en §71.6 (L1549); y [18] en §34 (L1080). La distribución es 1/8, 3/12, 1/8, 1/7 y 0/3: 6 de 38 (15,8 %), frente a 5 de 38 (13,2 %) en la iteración 3.

El criterio `V5.coverage_breadth.master` exige «Main + adjacent clusters covered (25–60 papers)». Seis menciones quedan por debajo del tramo incluso descontando el clúster 5, que es de frontera y no exigible en nivel master. El cambio respecto de la iteración 3 es de régimen interno, no de escala: los cuatro clústeres principales y adyacentes pasan a estar todos representados y [18] se suma al recuento, pero ningún trabajo nuevo entra en el argumento. El E2 de esta iteración es una re-verificación dirigida —nueve entradas re-visadas, cero búsquedas nuevas (L16, L227–234)—, por lo que hereda los recuentos de clúster y no puede ampliar la cobertura. La tensión estructural señalada en E2 (L200) persiste: §71.14 se titula «Obras del mapa literario citadas en el cuerpo» y cierra diciendo que «el resto se registra aquí con su marcador numérico», mientras el anexo registra 32 entradas con `Citada: no`; tabla y flag describen estados distintos. El anexo tiene además 41 entradas, aunque §70 (L1497, L1499) hable de «38 referencias» y la tabla se detenga en [38].

— polarity: negative · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#P005]], [[#P006]], [[#F-V5-004]] · criteria: V5.coverage_breadth.master

### F-V5-002 — Actualidad — 18 de 38 referencias de los últimos cinco años y 4 de 6 citas en el cuerpo

La distribución de E2 iter4 (L160–170) coincide con `Data/referencias.md`: seis entradas de 2026 ([9], [10], [11], [24], [26], [35]), una de 2025 ([22]), seis de 2024 ([18], [25], [28], [29], [30], [32]), cuatro de 2023 ([15], [23], [27], [34]), una de 2022 ([17]) y veinte de 2021 o antes; tres institucionales ([39]–[41]) no tienen año. El tramo 2022–2026 suma 18 de 38 referencias fechadas (47,4 %) y 18 de 41 entradas del anexo (43,9 %). El criterio `V5.recency.master` —«At least 40% from the last 5 years; foundational classics balanced»— queda satisfecho por ambas medidas. El equilibrio de clásicos también se sostiene: 20 de 38 entradas fechadas son de 2021 o antes, entre ellas Akerlof 1970 [1], Hulten 2003 [12], Wolf 2005 [6], Ritter 2004 [31] y Guerra 2015 [33].

En el cuerpo, de las seis obras con marcador, cuatro son recientes —Du [9] 2026, Muça [26] 2026, Madhusudhanan [18] 2024 y Vidal Alejandro [29] 2024— y dos son los contrapesos clásicos —Akerlof [1] 1970 y Gegić [14] 2019—: 4 de 6 (66,7 %). La mejora se concentra en §71.6 y en el marcador añadido en §34; las secciones analíticas §17–§20, §59–§60 siguen sin incorporar la literatura reciente. [24] (Hohensinner et al. 2026, arXiv:2601.14311) está en el anexo y cae dentro de los últimos 18 meses, pero no se discute en el cuerpo; el seguimiento de preprints recientes es exigible en nivel phd, no en master, de modo que no se emite hallazgo por ese hecho.

— polarity: positive · confidence: high · related: [[#P001]], [[#P003]], [[#P004]], [[#P006]], [[#C013]], [[#F-V5-005]] · criteria: V5.recency.master

### F-V5-003 — Peso de la citación — §71.6 convierte cuatro comparaciones en citas load-bearing con autor y marcador

El párrafo de §71.6 (L1549) lleva ahora los marcadores `[14]`, `[26]`, `[9]` y `[29]` junto al nombre de cada autor en su primera mención. E1 lo inventaría como C013 (L163–L171), afirmación load-bearing de tipos `novelty` y `citation-grounded`, con evidencia externa explícita: «[14] Gegić (2019), [26] Muça (2026), [9] Du (2026), [29] Vidal Alejandro (2024), según las fichas de §71.14». Cada cláusula describe el trabajo ajeno y enuncia un diferenciador propio —procedencia y normalización frente a Gegić, conversión con TRMI fechada frente a Muça, no estimación de tasa anual frente a Du, tasa informal como convención frente a Vidal Alejandro—. En §34 (L1080), los marcadores `[14]` e `[18]` respaldan la frase sobre los antecedentes de predicción sobre catálogos estructurados.

El criterio `V5.citation_weight.master` —«Load-bearing claims cite source + author named in body at first mention»— queda satisfecho para C013 y para la remisión de §34: la mitad nominal ya estaba cubierta en la iteración 3 y en esta se añade la mitad numérica. Es el cambio sustantivo de la iteración y constituye un hallazgo positivo de calibración de peso, no solo de formato: las cuatro obras vecinas funcionan como comparación load-bearing y no como entrada decorativa de una lista.

— polarity: positive · confidence: high · related: [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#C013]], [[#F-V5-004]] · criteria: V5.citation_weight.master

### F-V5-004 — Peso de la citación — 12 de 15 afirmaciones load-bearing sin cita externa y 38 marcadores que operan como registro

El resumen de E1 iter4 (L13–15) contabiliza 125 afirmaciones, 15 de ellas load-bearing. De esas 15, doce —C001–C008, C010, C011, C014 y C015— registran «External evidence cited: — (sin citas numeradas)» o equivalente (L27, L39, L51, L63, L75, L87, L99, L111, L135, L147, L183, L195): 12/15 (80 %). Solo C009 remite a [1] y a las tres fuentes institucionales según §70 (L123), C012 a DfT/DVLA y ANFAC/AEADE declarados en §18 (L159), y C013 a los cuatro vecinos de §71.6 (L171). Las afirmaciones cargadas de contenido analítico —hipótesis H1, cifras de la corrida, ablación, intervalo bootstrap, semilla, novedad declarada— siguen apoyadas únicamente en evidencia interna.

Los 38 marcadores de la tabla de §71.14 son un registro, no una discusión: ninguna de las 32 entradas con `Citada: no` se analiza en el cuerpo y §17 (L811–L832) tiene cero marcadores. El anexo fue actualizado a las 03:04, después de que se generara E2 a las 03:02: [9], [14], [26] y [29] pasan a «sí (§71.6 y §71.14)», [18] a «sí (§71.14)» y [39] gana el campo «sí (§70 y §71.14)». La alineación mejora la ponderación, pero quedan dos imprecisiones de ubicación: la ficha de [18] omite §34, donde tiene marcador, y la de [39] invoca §71.14 aunque la tabla termina en [38]. Además, §70 generaliza que «las fuentes restantes figuran con estado `(metadata incomplete)`» cuando solo cuatro entradas ([1], [10], [12] y [39]) llevan esa marca. Con el criterio `V5.citation_weight.master` aplicado al conjunto, la condición de «fuente + autor» se cumple en tres de quince afirmaciones y falta en el resto.

— polarity: negative · confidence: high · related: [[#C001]], [[#C009]], [[#C012]], [[#C013]], [[#F-V5-001]], [[#F-V5-003]] · criteria: V5.citation_weight.master

### F-V5-005 — Ausencias probables — siete obras siguen fuera del cuerpo y el criterio master espera el top-5 por clúster adyacente

E2 iter4 (L203–205) mantiene las siete obras arrastradas de la iteración 3 —Lewis 2011 [2], Englmaier et al. 2017 [4], Krotov et al. 2020 [21], Priestley et al. 2023 [23], Brown et al. 2025 [22], Guerra 2015 [33] y Hohensinner et al. 2026 [24]— y no propone adicionales. Las siete conservan `Citada en el informe: no` en `Data/referencias.md` (L10, L14, L48, L50, L52, L54, L72) y ninguna aparece en el cuerpo; Gegić [14] queda fuera de la lista porque sí tiene comparación en §71.6 y marcadores en §71.6 y §34.

La relación con afirmaciones load-bearing se mantiene: Lewis es el eslabón empírico entre Akerlof y la captura de defectos y tipo de vendedor (C009); Englmaier advierte sobre saltos en umbrales de año y 10.000 km frente a la retirada de la pendiente anual en §59–§60 (C003); Krotov y Brown corresponden a la regla de no eludir anti-automatización de §10; Priestley a la arquitectura de colas y cuarentena de la fase 7; Guerra a la operacionalización de `asequibilidad = precio / salario`; y Hohensinner a la distinción entre procedencia y linaje que §71.15 declara como aporte. El criterio `V5.missing_important_work.master` exige «Top-5 most-cited of each adjacent cluster expected»; la medición de la iteración 3 —última con búsquedas temáticas— situaba 21 de 23 obras del top-5 por clúster (91,3 %) fuera del texto. Esta iteración no ejecutó búsquedas ni re-lectura de resúmenes, por lo que la lista se hereda sin verificación independiente y la ausencia de obras adicionales se afirma con confianza media.

— polarity: negative · confidence: medium · related: [[#P001]], [[#P003]], [[#F-V5-002]], [[#F-V5-004]] · criteria: V5.missing_important_work.master


## §6 — v6-reproducibility


# V6 — Reproducibilidad (nivel master)

## Resumen (3 líneas)

1. Los seis subcriterios V6 quedan cubiertos en nivel master: README con quickstart, `requirements.txt` con doce pinos `~=X.Y.0`, semilla coherente entre §71.5 y el código, puntos de entrada con argumentos, prueba de humo ejecutada y declaración de disponibilidad en §71.5/§71.15.
2. Verificación directa en el checkout (`main`, HEAD `77ab644`, `repo_clone_status: success`): `run_all.py` declara y exporta `PROYECTO_SEED`, `test_smoke_pipeline.py` pasa 4/4 y el panel interactivo existe en `Data/`, `docs/` y `site/` con 109.929 B.
3. Como límites descriptivos —no exigidos en master— quedan la ausencia de lockfile, Dockerfile y versión de Python fijada, la licencia pendiente declarada, dos archivos modificados sin commitear y tres CSV con recuentos divergentes del texto.

### F-V6-001 — README con quickstart, dependencias y mapeo de componentes

`README.md` (105 líneas) satisface la combinación pedida por `V6.documentation.master`: nombre y ubicación del proyecto (l. 1–5), «Quickstart» con creación de venv, `pip install -r requirements.txt` y ejecución de `Data/analisis_rentabilidad/scripts/run_all.py` (l. 15–33), «Estructura» (l. 35–52), «Fuentes de datos» (l. 54–64), «Configuración» (l. 66–80) y «Documentación» (l. 94–99), que remite a `INFORME_TECNICO.md`, `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md` y `Data/analisis_rentabilidad/README.md`. Este último (41 líneas) declara el flujo script→artefacto: `01_ingest.py` → `listings_raw.parquet`, `02_clean.py` → `listings_clean.parquet`, `03_eda.py` → `kpis.csv`, `04_stats.py` → `modelo_depreciacion.csv`/`vif.csv`/`tests.csv`, `05_benchmark.py` → `benchmark.csv`.

En el documento, §71.5 (l. 1543) declara las ubicaciones de la semilla, el panel, las bases crudas, el comando único y las dependencias; la tabla «Code-to-document mapping» de E3 (l. 198–215) inventaria catorce correspondencias adicionales. El criterio `V6.documentation.master` se lee «README + dependencies list + brief usage examples» y queda cubierto; el mapeo script→tabla completo es una exigencia de `phd`.

— polarity: positive · confidence: high · related: [[#F-V6-005]], [[#F-V6-007]] · criteria: V6.documentation.master

### F-V6-002 — Dependencias fijadas a series menores con operador `~=X.Y.0`

`requirements.txt` contiene doce líneas de dependencias activas, todas con operador compatible y parche `.0`: `pandas~=2.2.0` (l. 3), `numpy~=1.26.0` (l. 4), `plotly~=5.18.0` (l. 5), `statsmodels~=0.14.0` (l. 6), `scipy~=1.11.0` (l. 7), `beautifulsoup4~=4.12.0` (l. 8), `curl_cffi~=0.7.0` (l. 9), `tenacity~=8.2.0` (l. 10), `trafilatura~=1.6.0` (l. 11), `pyarrow~=14.0.0` (l. 12), `mkdocs~=1.6.0` (l. 13) y `mkdocs-material~=9.5.0` (l. 14). La cabecera (l. 2) reza «Fijadas a versiones menores (criterio de reproducibilidad de nivel master)» y §71.5 (l. 1543) declara «Las dependencias están fijadas a serie menor en `requirements.txt`».

Las importaciones de los siete scripts del pipeline (`pandas`, `numpy`, `scipy`, `plotly`, `bs4` y el módulo local `config`) quedan cubiertas por ese archivo. El criterio `V6.environment.master`, «Dependencies pinned to minor versions», queda satisfecho.

— polarity: positive · confidence: high · related: [[#F-V6-003]] · criteria: V6.environment.master

### F-V6-003 — Sin lockfile, Dockerfile ni versión de Python fijada en el checkout

No hay `pyproject.toml`, `environment.yml`, `Dockerfile` ni archivo de lock versionado en la raíz; E3 «Environment» (l. 75–81) registra esas cuatro ausencias. `README.md:17` declara «Requiere Python 3.10+» y el entorno local `Auxiliares/.venv-py/` corresponde a Python 3.14, sin que el repositorio fije una de las dos. §6 declara FlareSolverr 3.5.2 desplegado en Docker sin Dockerfile versionado.

Estos elementos pertenecen a `V6.environment.phd` («Dependencies fully pinned + lockfile + Python/R version declared») y `V6.environment.paper`; el nivel `master` se satisface con el pinado de serie menor de F-V6-002. La fijación `~=X.Y.0` admite cualquier parche dentro de la serie, de modo que dos entornos construidos en fechas distintas pueden resolver versiones de parche diferentes.

— polarity: neutral · confidence: high · related: [[#F-V6-002]] · criteria: V6.environment.phd

### F-V6-004 — Semilla declarada y propagada por `PROYECTO_SEED`, coherente con §71.5

El documento afirma en §71.5 (l. 1543): «La semilla `SEED = 20261127` está declarada en `run_all.py` y se propaga a cada etapa por la variable de entorno `PROYECTO_SEED`; antes se declaraba sin efecto». En el checkout, `Data/analisis_rentabilidad/scripts/run_all.py` contiene `SEED = 20261127` (l. 16), `random.seed(SEED)` (l. 17), `np.random.seed(SEED)` (l. 18) y `ENTORNO["PROYECTO_SEED"] = str(SEED)` (l. 23), entorno que se pasa a cada subprocess en la l. 39. El consumo se verifica en `03c_comparaciones.py`: `SEED = int(os.environ.get("PROYECTO_SEED", "20261127"))` (l. 20) y `rng = np.random.default_rng(SEED)` (l. 37). Un barrido de `*.py` en `Data/` y `Auxiliares/` encuentra `PROYECTO_SEED` solo en esos dos archivos, y `03c_comparaciones.py` es la única etapa del pipeline que usa un generador aleatorio: la propagación alcanza la etapa estocástica y las restantes son deterministas.

E3 registra esta verificación como «Semilla y reproducción — verificación positiva» (l. 183–186) y concluye «No hay brecha de artefacto». No hay framework de deep learning ni GPU en el pipeline, por lo que no aplican flags de determinismo cuDNN. El criterio `V6.determinism.master`, «Seeds declared in code and in document, consistent», queda satisfecho.

— polarity: positive · confidence: high · related: [[#F-V6-006]], [[#F-V6-010]] · criteria: V6.determinism.master

### F-V6-005 — Puntos de entrada documentados con argumentos y comando único

§71.5 (l. 1543) enumera el comando único `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py` y los puntos de entrada con argumentos `generar_dashboard.py --solo-si-cambia`, `exportar_parquet_compacto.py --tablas ...`, `db_chunks.py split|verify|assemble` y `generar_sitio_mkdocs.py`. `README.md:19–33` reproduce el comando único y su resultado esperado. Los argumentos se confirman en el código: `generar_dashboard.py:388–389` (`--solo-si-cambia`, `--salida`), `exportar_parquet_compacto.py:114–116` (`--db`, `--salida`, `--tablas`) y `db_chunks.py:128–136` (subcomandos `split`, `verify`, `assemble` y `--force`).

`run_all.py:27–55` encadena siete etapas y tres herramientas (actualizar números, dashboard y exportación compacta), de modo que un solo comando regenera tablas, KPIs y panel: esto excede `V6.entry_points.master` («Entry points documented with arguments») y alcanza la forma descrita en `V6.entry_points.phd`. La tabla de entry points de E3 (l. 43–53) marca «Args documented: no» para `run_all.py`, pero la documentación de argumentos reside en §71.5 y en `README.md`, y `test_smoke_pipeline.py:52–57` comprueba esa presencia.

— polarity: positive · confidence: high · related: [[#F-V6-001]], [[#F-V6-006]] · criteria: V6.entry_points.master

### F-V6-006 — Prueba de humo del componente central ejecutada con resultado positivo

§71.5 (l. 1543) cita «Prueba de humo: `python3 Auxiliares/herramientas/test_smoke_pipeline.py`». El archivo (68 líneas) contiene cuatro pruebas: `test_compila` compila nueve scripts con `py_compile`, `test_artefactos` verifica siete rutas (entre ellas `Data/dashboard.html` y `INFORME_TECNICO.md`), `test_csv_legibles` abre cinco CSV y exige al menos dos filas de `baselines.csv`, y `test_comando_unico` comprueba que `README.md` cite `run_all.py` y que el código contenga `SEED = 20261127`, `generar_dashboard.py` y `exportar_parquet_compacto.py`.

Ejecuté `python3 Auxiliares/herramientas/test_smoke_pipeline.py` sobre el checkout: las cuatro pruebas imprimieron `OK` y la salida final «4 pruebas superadas», con código de salida 0. E3 «Tests» (l. 55–60) inventaria cuatro archivos y 327 LOC, con framework de scripts y sin `pytest.ini`/`conftest.py`. La cobertura es de compilación, existencia y legibilidad; no verifica reproducibilidad bit a bit de un resultado principal, que es la exigencia de `V6.tests.paper`. El criterio `V6.tests.master`, «At least smoke tests of the central component», queda satisfecho.

— polarity: positive · confidence: high · related: [[#F-V6-004]], [[#F-V6-005]] · criteria: V6.tests.master

### F-V6-007 — Panel interactivo declarado y presente en tres rutas del repositorio

§71.5 (l. 1543) declara «El panel vigente es `Data/dashboard.html` (copiado a `docs/dashboard.html`)»; §59 (l. 1419) añade que los gráficos se copian a `docs/graficos/` y las tablas se generan desde los CSV; el Resumen (l. 19) lo describe como «panel interactivo autocontenido». En el checkout los tres archivos `Data/dashboard.html`, `docs/dashboard.html` y `site/dashboard.html` existen con 109.929 bytes cada uno. E3 «Figures» (l. 154–159) lo inventaria como artefacto HTML autocontenido y lo asocia al claim del Resumen.

`run_all.py:25` y `:53` regeneran el panel mediante `generar_dashboard.py --solo-si-cambia`, de modo que el artefacto declarado está enlazado al comando único. La copia en `site/` no aparece citada en §71.5 y está ignorada por Git. Este mapeo componente→archivo corresponde al ámbito de `V6.documentation.master`.

— polarity: positive · confidence: high · related: [[#F-V6-001]], [[#F-V6-005]] · criteria: V6.documentation.master

### F-V6-008 — Declaración de disponibilidad de datos y código, con licencia pendiente declarada

§71.5 (l. 1543) declara el repositorio público `https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba`, la ubicación de las bases crudas en `Data/Revolico/` gestionadas con Git LFS, su reconstrucción desde `chunks/MANIFEST.json`, el comando único y la prueba de humo. §71.15 (l. 1553 y su versión EN en l. 1555) cierra: «La disponibilidad de datos y código se documenta en §71.5; la licencia queda pendiente de declaración». La tabla «Datasets» de E3 (l. 96–104) nombra cinco grupos de datos con su ruta de acceso y señala los binarios como públicos vía Git LFS.

No existe `LICENSE` ni `LICENCIA` en la raíz del checkout, en coincidencia con lo declarado en §71.5 y §71.15: la ausencia aparece consignada en el documento y en E3 (l. 193–196), no como brecha oculta. El criterio `V6.data_availability.master`, «Datasets named + access path documented (URL / DOI / "available on request")», queda satisfecho; versión fijada y licencia son exigencias de `V6.data_availability.phd`.

— polarity: positive · confidence: high · related: [[#F-V6-003]] · criteria: V6.data_availability.master

### F-V6-009 — Checkout con dos archivos modificados sin commitear frente a HEAD

E3 declara `repo_clone_status: success` (l. 7) sobre la copia local en `~/Proyectos/El precio de moverse en Cuba`. La rama activa es `main` y HEAD es `77ab644` («audit: corregir los 28 hallazgos neutros de la iteracion 3»). `git status --short` muestra `M Data/referencias.md`, `M INFORME_TECNICO.md` y los cuatro artefactos de la iteración 4 sin trackear. El diff se limita a metadatos bibliográficos: el paso de «38 referencias» a «41 referencias» en §70 y el cambio de «mención nominal en §71.6, sin marcador numérico» a «§71.6 y §71.14» en las entradas [9], [14], [18] y [26]. El código del pipeline aparece sin modificaciones.

El texto en caché auditado corresponde al árbol de trabajo modificado; un clon limpio en `77ab644` entregaría el texto con la cifra «38 referencias» de §70. La declaración de disponibilidad de §71.5 no fija commit, tag ni DOI de la versión que produjo los resultados, elemento propio de `V9.code_availability_statement.phd` y no del nivel master.

— polarity: neutral · confidence: high · related: [[#F-V6-008]]

### F-V6-010 — CSV de salida presentes con recuentos divergentes del texto

Tres entradas de «Missing artifacts» de E3 (l. 163–176) se resuelven como desajustes código→documento y no como ausencia de archivos: `outputs/tables/comparaciones.csv` registra `precio por tier de marca,1462` frente a las «981 candidatas» citadas en §71.3; `outputs/tables/modelo_muestra.csv` registra `principal,993,586,0.1008` frente a las 584/572 observaciones de §71.1, §71.2 y `docs/historia/apendice.md:77`; y `outputs/tables/baselines.csv` contiene dos filas (`mediana_global`, `mediana_por_marca`) sin la fila «Modelo principal propio» que muestra la Tabla 3 de §71.1. Los tres archivos existen en `Data/analisis_rentabilidad/outputs/tables/` y son legibles, como confirma `test_csv_legibles` de F-V6-006.

Una tercera persona que ejecute el comando único obtiene los valores de esos CSV, que no coinciden exactamente con las cifras del texto. La semilla y la propagación de F-V6-004 no explican la diferencia: los desacuerdos están en los denominadores y en la composición de las filas, no en la variación estocástica.

— polarity: neutral · confidence: high · related: [[#F-V6-004]], [[#F-V6-006]]


## §7 — v7-writing


# V7 — Writing and AI patterns (findings)

Resumen (tres líneas):
- §69 se comprime de 271 a 147 palabras (−124): desaparecen sus dos triadas de cola larga y sus dos negaciones de salvaguarda, la huella se actualiza a los artefactos `-iter3` y el ejemplo del R² 0,277 → 0,274 repara en parte el Don't 8, sin adjetivos sin ancla ni hedging.
- §71 pasa de 606 a 1.763 palabras, 821 de ellas en la tabla nueva de 71.14: la prosa baja su densidad (metaconceptos 8,3 → ~2,1/1k) y mantiene 0 tics estrictos, con 9 marcadores `<!-- kpi:… -->` como firma de plantilla.
- En 71.6 los cuatro openers «Frente a…» se sustituyen por referencias `[n]`, las triadas se vuelven dyadas con cola más corta (44/34/44/34 → 34/28/32/27 palabras) y los paralelos EN suben de 2/6 a 6/8, con asimetrías en 71.3 y 71.5; ninguna sección alcanza `high`.

Alcance y método. Conteo directo sobre los textos cacheados de la iteración 3 (`informe-tecnico-2026-11-27-iter3.text.md`, 1.523 líneas, 29.870 palabras `wc -w`) y de la iteración 4 (`informe-tecnico-2026-11-28-iter4.text.md`, 1.605 líneas, 31.305 palabras `wc -w`). Se mantienen el criterio de palabra y la róbrica estrecha de metaconceptos del V7 anterior (`análisis`, `proceso`, `evaluación`, `consideración`, `implementación`, `auditoría`, `herramientas`, `decisiones`, `resultados`, `apoyo`, `edición`, `revisión`, `cifras`, `modelos`, `afirmación`, `salida`, `estructura`, `marco`, `procesamiento`, `señal`, `arquitectura`), con la salvedad de que en tablas se separa el rótulo de clúster del uso en prosa. §13 (registro generado por script) queda fuera del denominador de densidades. Winston, Pinker y Romero §13 se citan como rótulos de las róbricas aplicadas. El artefacto describe patrones y densidades, sin emitir juicio de autoría.

### F-V7-001 — §69: compresión de 271 a 147 palabras y retirada de las dos triadas de cola larga

La declaración de la iteración 3 (L1469/1471 de aquel texto) desplegaba cuatro fases con nombres compuestos —«investigación y verificación de fuentes, redacción y edición de la narrativa, generación y revisión de código, y traducción bilingüe»— y dos construcciones de Romero §13 Don't 3: «Las cifras, los modelos estadísticos y las decisiones de diseño» y «contrastar toda cifra … , ejecutar las pruebas automatizadas y conservar el registro de auditoría en `reviews/`». La versión actual (L1489/1491) reduce las fases a cuatro sustantivos sueltos —«investigación, redacción, código y traducción»—, funde el protocolo en una dyada («los CSV versionados y las pruebas automatizadas») y deja la lista de skills como tres nombres propios cortos. Recuento de d3 en §69: 2 → 0; longitud media de las oraciones ES: 41/36/36/28 → 22/17/23/13 palabras, con un corte corto final que rompe la uniformidad. Se retiran también las dos negaciones de salvaguarda («ninguna salida de IA se aceptó sin ese contraste», «ninguna afirmación empírica se originó en una salida de IA sin contraste contra los archivos»), que no eran Don't 2 —hacían trabajo argumentativo— pero sí sostenían la parte más explícita de la declaración; el contraste queda ahora implícito en «Cada cifra se contrastó…». La huella, que el V7 anterior señalaba como apuntando a los artefactos de la iteración 1, se corrige a `reviews/informe-tecnico-2026-11-27-iter3.{md,forensic.md}` y sus 13 artefactos: el dato descriptivo queda saldado. Coste de la compresión: «Cada cifra se contrastó contra los CSV versionados y las pruebas automatizadas» coordina mal dos operaciones distintas (contrastar cifras / ejecutar pruebas) que en la iteración 3 iban separadas por «y ejecutar».

— polarity: positive · confidence: high · related: [[#F-V7-003]], [[#F-V7-007]]

### F-V7-002 — Romero §13 Don't 5: cero adjetivos sin ancla también en la iteración 4

El subconjunto sin ancla sigue en 0. Los tres modificadores que §71 heredó de la iteración 3 continúan anclados: «Mediana global ( ingenua )» lleva MAE 18.188,34 USD sobre 1.462 anuncios en la misma celda (L1511); «Contraste cualitativo de cobertura y frescura» va precedido de «23.500 anuncios y series mensuales» (L1513); y «mejor cobertura» (L1537) se apoya en los 28 frente a 584 observaciones de 71.2. Los añadidos de esta iteración son técnicos o llevan salvedad explícita: «bootstrap» cuantificado con H = 44,313 y un intervalo de 10.000 a 29.500 USD sobre 2.000 réplicas (L1528), y «no se considera de doble uso sensible, con la salvedad de que los anuncios contienen datos de contacto que se excluyen de la publicación» (L1553). En §69, «versionados» y «automatizadas» siguen anclados por las rutas y el comando de prueba de humo de 71.5 (L1543). Fuera del alcance comparativo, el corpus mantiene los mismo casos ancorados que en la iteración 3: «significativa» con p del F = 0,411 (L1401) y con p mínimo 0,0941 (L1409), y «bibliotecas quizá innecesarias» con 66 MB (L1479).

— polarity: neutral · confidence: high · related: [[#F-V7-004]], [[#F-V7-009]]

### F-V7-003 — Romero §13 Don't 8: el ejemplo del R² repara parcialmente el cierre de §69

El V7 de la iteración 3 registró que «La auditoría completa de este documento … y sus resultados se conservan en … junto con los trece artefactos de fase» (L1469 de aquel texto) enunciaba el resultado sin mostrar hallazgo. La versión actual intercala antes de ese cierre una instancia concreta: «Un ejemplo del contraste: la revisión detectó un R² citado como 0,277 que el CSV daba como 0,274 y se corrigió con marcadores» (L1489; «For instance, an R² quoted as 0,277 was corrected to 0,274 after comparison with the CSV», L1491). Es una muestra, no una glosa: el lector ve el dato anterior, el dato contrastado y la acción. Queda, sin embargo, la segunda mitad del mecanismo —«El registro de la tercera pasada está en … y sus 13 artefactos» (L1489/1491)— como puntero a un expediente que no se abre aquí; el paralelo EN además omite «con marcadores». Se registra como remedio parcial: 1 instancia de showing donde antes había 0, con el cierre de registro todavía en modo telling.

— polarity: positive · confidence: high · related: [[#F-V7-001]], [[#F-V7-009]]

### F-V7-004 — §71: crece 1.157 palabras, pero casi la mitad es la tabla nueva de 71.14

La sección (L1505–1600) pasa de 606 a 1.763 palabras. El incremento no es prosa: 821 palabras corresponden a 71.14, la tabla de 38 obras del mapa literario (L1557–1599) con su cierre (L1600), y 145 a 71.15; §71.1–71.6 suma 785 palabras, frente a 606 en la iteración 3. Los cinco primeros apartados siguen siendo enumerativos y anclados —tabla con dos líneas base en lugar de una (L1511–1512), ablación con cifras (L1522), contraste con H y bootstrap nuevos (L1528), lista de cuatro amenazas (L1534–1537) y comandos de reproducción ampliados (L1543)—. Bajo Winston, los ocho títulos numerados son instructivos y nombran el estándar que desarrollan; la novedad estructural es el desorden de numeración (71.15 precede a 71.14, L1551 y L1557) y la ausencia de resumen de cierre para la sección. Densidad de los apartados 71.1–71.5 y 71.15: baja.

— polarity: neutral · confidence: high · related: [[#F-V7-005]], [[#F-V7-006]], [[#F-V7-007]]

### F-V7-005 — 71.6: de cuatro openers «Frente a…» a cuatro referencias `[n]`, y de triadas a dyadas

El párrafo único de 71.6 (L1549, 133 palabras) ya no abre cuatro veces con «Frente a <autores> (<año>), que <trabajo ajeno>, …»: ahora enmarca cada contraste con el apellido y el marcador —«Gegić y otros [14]», «Muça, Bani y Alla [26]», «Du y otros [9]», «Vidal Alejandro y otros [29]»—, con lo que desaparecen los cuatro openers de fórmula y se acortan las listas de coautores. La métrica de Romero §13 Don't 3 cambia de forma: las cuatro triadas con tercer miembro largo se convierten en cuatro dyadas de «trabajo ajeno; aporte propio», con el segundo miembro todavía más extenso y abstracto en tres de los cuatro casos (12/22, 11/17, 17/15, 13/14 palabras por cláusula). Las oraciones completas bajan de 44/34/44/34 a 34/28/32/27 palabras: se acorta la uniformidad, pero no entra en la banda 18–25. Las negaciones contrastivas de cierre caen de cuatro («no de algoritmo», «no el pipeline de integración», «no estima una tasa anual», «no como objeto de estudio») a dos («no de algoritmo», «no el objeto de estudio»), más la autolimitación «no estima una tasa anual»; el total de «no» del párrafo baja de 6 a 4. Como en la iteración 3, no se cuentan como Don't 2: discriminan la contribución propia frente a la ajena. El anclaje se refuerza con los marcadores `[14]`, `[26]`, `[9]` y `[29]`, que ahora enlazan con la tabla de 71.14 (L1600).

— polarity: positive · confidence: high · related: [[#F-V7-004]], [[#F-V7-006]]

### F-V7-006 — Paralelos EN: de 2/6 a 6/8 apartados con glosa, con tres asimetrías nuevas

En la iteración 3 solo 71.1 y 71.2 llevaban glosa «**EN.**»; en la actual la llevan 71.1 (L1518), 71.2 (L1524), 71.3 (L1530), 71.4 (L1539), 71.5 (L1545) y 71.15 (L1555), es decir 6 de 8 apartados numerados. Siguen sin paralelo 71.6 —el párrafo de mayor densidad de dispositivos— y 71.14, donde la bilateralidad se agota en el encabezado y la tabla es compartida. Tres asimetrías merecen constancia: (i) la glosa de 71.3 añade «an operationalised SOTA baseline is still missing», afirmación ausente del texto ES de L1528; (ii) la glosa de 71.5 reduce un párrafo ES de unas 131 palabras a 22, omitiendo la ruta del panel, Git LFS y `MANIFEST.json`, la URL pública y la licencia pendiente (esta última se recoge en 71.15); (iii) en 71.1 la glosa introduce las etiquetas «baseline 1», «baseline 1b» y «baseline 2» que la tabla ES no rotula. En §69 el paralelo ES/EN se mantiene con cuatro oraciones por lado, con la pérdida menor de «con marcadores» en la versión inglesa (L1491). Bajo Winston (parallel structure), el balance es claramente positivo.

— polarity: positive · confidence: high · related: [[#F-V7-004]], [[#F-V7-005]]

### F-V7-007 — Metaconceptos: §69 baja de 44,3 a 13,6 por 1.000 palabras y §71 se diluye con la tabla

Con la róbrica estrecha del informe anterior, §69 pasa de 12/271 palabras (44,3/1k) a 2/147 (13,6/1k): solo sobreviven «herramientas» y «revisión»; desaparecen «auditoría» (2), «salida» (2), «cifras», «modelos», «decisiones», «afirmación», «resultados» y «edición». La caída es de densidad y de recuento, no solo de denominador. En §71 el descenso es similar si se excluyen los rótulos técnicos: de 5/606 (8,3/1k) a 2/942 (2,1/1k) en la prosa de 71.1–71.6 y 71.15 —«herramientas» y «evaluación», esta última dentro del marco con autor y año de 71.6—. Si se incluyen los rótulos de tabla «Modelos de precio, reg» (L1569–1578) y «Señales de precio en m…» (L1596–1598), el total asciende a 20/1.763 (11,3/1k), pero ese repunte es un artefacto de la lista de 38 filas, no de la prosa: los sustantivos van acompañados de autor, año y título. Las dos zonas que el V7 anterior calificó `high` —§17–21 y §59–63— permanecen sin cambios relevantes en esta dimensión.

— polarity: neutral · confidence: high · related: [[#F-V7-001]], [[#F-V7-004]]

### F-V7-008 — Winston y superficie de generación: fila huérfana, marcadores `<!-- kpi:… -->` y doble separador

Tres observaciones de superficie en los bloques comparados. (i) En 71.1 la fila «Modelo principal propio» (L1516) queda separada de la tabla L1509–1513 por el párrafo de registro de L1515, de modo que se presenta como una tabla de una sola fila; en la iteración 3 esa fila estaba dentro de la tabla (L1493). (ii) Los marcadores de plantilla `<!-- kpi:… -->` pasan de 4 en todo el documento a 29, con 9 concentrados en §71 (L1511–1512, L1518, L1528, L1543); son comentarios HTML invisibles en renderizado, pero dejan una firma de composición automatizada en el texto cacheado. (iii) Se conserva el doble separador `---` que precede a §69 (L1483, L1485) y a §71 (L1501, L1503), ya registrado en la iteración 3, y persisten celdas truncadas en la tabla de 71.14 («Asimetría de informaci», L1561–1568; «The Market for "Lemons": Quality Uncertainty and the Market Mech», L1561). Se anotan como observaciones de estructura, no como correcciones pendientes de este evaluador.

— polarity: neutral · confidence: high · related: [[#F-V7-004]], [[#F-V7-006]]

### F-V7-009 — Romero §13 Don't 2, Don't 4, hedging y openers de fórmula: continuidad

«No solo… sino», «not just… but» y equivalentes siguen en 0 en los dos bloques. La forma estricta de Don't 4 mantiene su única coincidencia histórica fuera de alcance —«cada transformación y cada estimación del pipeline» (L1409), referida a transformación de datos—; no aparecen «ecosistema», «paradigma» ni «landscape». El hedge del corpus continúa siendo «bibliotecas quizá innecesarias» (L1479, con 66 MB de ancla); «relativamente», «somewhat», «perhaps» y «presumably» están en 0, al igual que «Este trabajo demuestra…», «Es importante notar…» y «En los últimos años…». El único cambio neto en esta róbrica es la desaparición de los cuatro openers «Frente a…» de 71.6, ya contados en F-V7-005.

— polarity: neutral · confidence: high · related: [[#F-V7-002]], [[#F-V7-003]], [[#F-V7-005]]

## AI-pattern density by section

Valores aproximados sobre los textos cacheados, con `wc -w` y la róbrica estrecha descrita en Alcance. La columna compara iteración 3 → iteración 4; las secciones no comparadas se consignan por continuidad.

| Section | Density (it3 → it4) | Notes (iteración 4) |
|---|---|---|
| §1–68 — Prosa narrativa y histórica | low → low | Sin cambio en esta dimensión; §59–63 y §17–21 siguen `high` por su anclaje numérico, no por atenuación |
| §69 — Declaración de uso de IA (L1487–1491) | medium → **low** | 147 palabras; d3 2 → 0, d5 sin ancla 0, d8 parcial (1 ejemplo mostrado), 2 metaconceptos/147 (13,6/1k), 0 hedges, 0 openers |
| §70 — Referencias verificadas (L1495–1499) | low → low | Lista enumerativa con procedencia externa; sin cambios de patrón |
| §71.1–71.5 — Bases, ablación, pruebas, amenazas, reproducción (L1507–1545) | low → **low** | Tablas, cifras y comandos; 9 marcadores `<!-- kpi:… -->`; 1 fila de tabla huérfana (L1516); glosa EN en los cinco apartados |
| §71.6 — Posicionamiento frente a trabajos cercanos (L1547–1549) | medium → **low–medium** | d3 4 → 0 (dyadas con cola larga 3/4), openers «Frente a…» 4 → 0, negaciones contrastivas 4 → 2, oraciones 44/34/44/34 → 34/28/32/27; sin glosa EN |
| §71.15 — Declaraciones (L1551–1555) | — → **low** | Sección nueva; pares ES/EN paralelos; salvedad sobre datos de contacto con ancla concreta; 0 tics estrictos |
| §71.14 — Obras del mapa literario (L1557–1600) | — → **n/a** | Tabla de 38 filas con autor, año y título; excluida del denominador de densidad de prosa; numeración posterior a 71.15 |

Totales de prosa comparada (`wc -w`): §69 271 → 147 palabras; §71 606 → 1.763 (de ellas, 821 en la tabla de 71.14). Modificadores de la róbrica Don't 5 sin ancla: 0 → 0 en ambos bloques; hedging 0 → 0; openers de fórmula 4 → 0 (todos en 71.6).

## Hook para V9

Ninguna sección de esta iteración alcanza `ai-pattern-density: high`: §69 baja a `low`, §71.6 queda en `low–medium`, §71.1–71.5 y §71.15 en `low`, y §71.14 se excluye por ser tabla. Para el contraste con `V9.ai_use_declaration.master`, la novedad relevante es doble: §69 ya no contiene la huella apuntada a los artefactos de la iteración 1 —ahora nombra los de `-iter3`— e incorpora una instancia verificada (R² 0,277 → 0,274), mientras que la supresión de las dos negaciones de salvaguarda deja la afirmación de supervisión menos explícita en el texto. La densidad media residual de 71.6 se debe ahora a dispositivos de superficie —dyadas con cola abstracta, uniformidad de oraciones largas y ausencia de glosa EN— y no a adjetivos sin ancla, hedging u openers, que son 0. La tabla de densidades queda consignada para V9 del mismo modo que en la iteración 3.


## §8 — v8-bibliography


# V8 — Integridad bibliográfica — iteración 4

Nota de método y alcance. El mandato recibido es estrecho: verificar la convención `sí/no`, los flags campo por campo, el bloque institucional [39]–[41] y la contradicción de Akerlof en ambas partes. En consecuencia: (a) no se re-ejecutaron búsquedas OpenAlex/Crossref ni se re-leyeron resúmenes; los metadatos, DOIs y conteos de citas se heredan de la verificación del 27/11/2026 consignada en `Data/referencias.md` (L3–L6), igual que en E2 iter4; (b) se intentó únicamente un fetch de las tres URLs institucionales, con los resultados consignados en F-V8-003; (c) los números de línea corresponden a la copia en caché indicada en el frontmatter, que E2 iter4 declara idéntica en contenido al informe auditado; (d) `verified: 37` / `unverified: 4` cuenta como no verificadas las cuatro entradas que el anexo marca explícitamente `(metadata incomplete)` —[1], [10], [12] y [39]—, no papers inexistentes. No se encontró ningún ghost paper ni entrada duplicada.

## Hallazgos

### F-V8-001 — Los cinco desajustes de flag registrados por E2 ya están corregidos; [18] conserva una ubicación incompleta

E2 iter4 (H2 y P006) registró que [18] llevaba `Citada en el informe: no` en la línea 42 del anexo pese a tener marcador numérico en §34. La entrada actual de `Data/referencias.md` dice literalmente: «[18] Madhusudhanan, K.; Behrens, G.; Stubbemann, M.; Schmidt-Thieme, L.. *ProbSAINT: Probabilistic Tabular Regression for Used Car Pricing*. arXiv:2403.03812; IEEE BigData 2024, Industry & Government Track (2024). https://arxiv.org/abs/2403.03812 · https://doi.org/10.1109/bigdata62323.2024.10825740. Citada en el informe: sí (§71.14). 13 citas verificadas en OpenAlex el 27/11/2026; versión publicada en IEEE BigData 2024.». El valor `sí` es correcto: §34 (L1080) afirma «La predicción de precios sobre catálogos estructurados tiene antecedentes [14], [18], ausentes del contraste original». Pero la ubicación consignada es incompleta: solo registra §71.14 (fila L1578) y omite el marcador en prosa de §34, que es precisamente la evidencia que E2 propuso consignar como `sí (§34, con marcador numérico)`. Lo mismo vale para [9], [14], [26] y [29]: sus antiguos calificadores «sin marcador numérico» ya no aparecen y ahora leen «Citada en el informe: sí (§71.6 y §71.14).», coincidente con L1549 y con las filas 1569, 1574, 1586 y 1589. Balance positivo con una residual.

— polarity: positive with residual issue · confidence: high · related: §34 (L1080), §71.6 (L1549), §71.14 (L1578), E2 iter4 H2/P006

### F-V8-002 — [39] declara una ubicación inexistente (§71.14) y omite §18, donde está la verificación en vivo

Entrada verificada verbatim: «[39] Department for Transport / DVLA. Vehicle statistics. GOV.UK. https://www.gov.uk/government/organisations/department-for-transport. **(metadata incomplete: URL profunda no confirmada)**. Citada en el informe: sí (§70 y §71.14).». §71.14 (L1559–L1598) se detiene en [38] —«| [38] | Señales de precio en m | Quariguasi Frota Neto (2015) | Market prices of remanufactured, used and new items: Evidence fr |» (L1598)—; ni [39], [40] ni [41] figuran en esa tabla. Por tanto «§71.14» es una ubicación falsa para [39]. La mención sustantiva está en §18 (L838): «| DfT / DVLA (UK), `gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files` | **Oficial gubernamental** | Verificado en vivo: publicado por Department for Transport + DVLA, actualizado 23/09/2026, Open Government Licence | Repos `uk-automotive-transition`: erste Registrierungen por marca/combustible/trimestre |», y en §70 (L1497/L1499). E2 iter4 (P007) encontró que [39] carecía del campo `Citada`; el campo ya existe, pero apunta a una sección que no contiene la entrada.

— polarity: negative · confidence: high · related: §18 (L838), §70 (L1497/L1499), §71.14 (L1598), E2 iter4 P007

### F-V8-003 — Bloque institucional [39]–[41]: formato divergente y contradicción de estado en [39]

Entradas verificadas verbatim: «[39] Department for Transport / DVLA. Vehicle statistics. GOV.UK. https://www.gov.uk/government/organisations/department-for-transport. **(metadata incomplete: URL profunda no confirmada)**. Citada en el informe: sí (§70 y §71.14).»; «[40] ANFAC. Informes del sector automotriz español. https://anfac.com/. Citada en el informe: sí (fuente institucional en §70).»; «[41] AEADE. Estadísticas de matriculaciones. https://www.aeade.net/. Citada en el informe: sí (fuente institucional en §70).». Las tres se apartan del patrón del bloque [1]–[38] (`Apellido, A.; …. *Título*. Revista (Año). DOI/URL.`): ninguna italiza el título, ninguna tiene campo de año y [39]/[40] no cierran el título con punto. Es una desviación de formato, aunque esperable en fuentes institucionales. Más sustantiva es la contradicción de estado en [39]: el anexo la marca `(metadata incomplete: URL profunda no confirmada)` mientras §18 (L838) declara «Verificado en vivo: … actualizado 23/09/2026, Open Government Licence» con esa misma URL profunda y §70 (L1497/L1499) la incluye entre las «Referencias citadas y verificadas externamente durante la auditoría». El encabezado del anexo (L4–L6) dispone que las entradas con `metadata incomplete` «no se presentan como referencias verificadas». [40] y [41] no llevan esa marca y son coherentes con §18 (L842–L843) y §70; sus glosas omiten §17/§18 pero no contradicen ningún campo.

Verificación externa intentada en esta pasada: `https://www.gov.uk/government/organisations/department-for-transport` → timeout; `https://anfac.com/` → timeout; `https://www.aeade.net/` → respuesta correcta, «AEADE - Asociación de Empresas Automotrices del Ecuador», con sección «Estadísticas — Anuarios, Boletines de prensa: venta de vehículos», coherente con [41] y con §18 (L843: «Verificado en vivo: aeade.net, anuarios y boletines de ventas»). Los timeouts no acreditan enlaces rotos: solo indican que [39] y [40] no se confirmaron desde este entorno.

— polarity: negative (format and status), positive for [41] · confidence: high for the internal contradiction, medium for URL status · related: §18 (L838, L842–L843), §70 (L1497/L1499), anexo L4–L6, E2 iter4 P007–P009

### F-V8-004 — Akerlof [1]: la contradicción se reproduce en ambas versiones de §70 entre «referencia verificada» y `(metadata incomplete)`

L1497 (ES): «Referencias citadas y verificadas externamente durante la auditoría: Akerlof (1970), *The Market for "Lemons"* (DOI 10.2307/1879431 confirmado en OpenAlex; el resumen indexado es solo un índice de secciones, por lo que su flag es `(metadata incomplete: resumen)`); UK Department for…». L1499 (EN): «Externally verified references cited during the audit: Akerlof (1970), *The Market for "Lemons"* (DOI 10.2307/1879431 confirmed in OpenAlex; the indexed abstract is only a section index, so its flag is `(metadata incomplete: abstract)`); UK Department for Transport / DVLA vehicle statistics…». Ambas versiones encuadran a Akerlof dentro de las referencias «verificadas externamente durante la auditoría» y, en la misma oración, le asignan un flag que según la convención del anexo (L4–L6) significa que la entrada «no se presentan como referencias verificadas». Es la misma contradicción duplicada en los dos textos del apartado bilingüe —las «ambas partes» del mandato—. La entrada [1] del anexo confirma la marca: «[1] Akerlof, G. A.. *The Market for "Lemons": Quality Uncertainty and the Market Mechanism*. The Quarterly Journal of Economics (1970). https://doi.org/10.2307/1879431. Citada en el informe: sí. **(metadata incomplete: resumen indexado no sustantivo; identidad y DOI verificados en OpenAlex)**». La incoherencia es de etiquetado, no de identidad: autor, año, revista y DOI están verificados desde el 27/11 y el propio anexo lo dice.

— polarity: negative · confidence: high · related: §70 (L1497/L1499), anexo [1] (L8), anexo L4–L6, C009

### F-V8-005 — Akerlof [1]: §71.14 atribuye su discusión a §71.6, donde no aparece

L1600: «Los trabajos [1], [9], [14], [26] y [29] se discuten además en §71.6; el resto se registra aquí con su marcador numérico y se enlaza a `Data/referencias.md`.». Pero §71.6 (L1549) contiene únicamente cuatro oraciones con marcadores `[14]`, `[26]`, `[9]` y `[29]`; Akerlof no comparece en ese párrafo. Sus únicas apariciones nominales sustantivas están en §17 (L817, sin marcador: «Asimetría de información (Akerlof); clasificación de calidad por antigüedad (≤5 años alta, >5 años con defectos); encuesta a 130 comerciantes; medición de costos ocultos y margen de reventa») y en §19 (L861, con marcador: «Marco teórico y normativo: asimetría de información (Akerlof [1]), selección adversa, riesgo moral, regulación vigente»), además de la fila [1] de la tabla de §71.14 (L1561) y de §70 (L1497/L1499). E2 iter4 (P005) ya había detectado esta atribución errónea; se confirma en la copia auditada. Consecuencia: el flag `sí` de [1] es correcto, pero la guía de ubicación de §71.14 no lo es, y el «Internal evidence cited: §71.6 (L1549)» de E1 C009 hereda el error. Es un mismatch de contexto de citación: el marcador existe, pero no donde la tabla dice.

— polarity: negative · confidence: high · related: §17 (L817), §19 (L861), §71.6 (L1549), §71.14 (L1600), C009, E2 iter4 P005

### F-V8-006 — Convención `Citada`: 32 flags `no` frente a un §71.14 titulado «Obras … citadas en el cuerpo»

El anexo define el campo en L6: «`Citada: sí/no` indica mención nominal en el informe». Recuento directo: 41 entradas, 9 con `sí` ([1], [9], [14], [18], [26], [29], [39], [40] y [41]) y 32 con `no`. Sin embargo §71.14 se titula «Obras del mapa literario citadas en el cuerpo / Prior work cited in the body» (L1557) y su cierre afirma que «el resto se registra aquí con su marcador numérico» (L1600), mientras 32 de las 38 filas de esa tabla ([1]–[38]) llevan `no` en el anexo. Las dos convenciones describen estados distintos: el flag registra mención nominal en prosa de cuerpo, la tabla registra entrada numerada del mapa literario. El documento no declara esta distinción, de modo que un lector de §71.14 leerá 32 contradicciones aparentes. E2 iter4 (observación agregada 1) ya lo señaló con 33 `no`; el cambio de [18] a `sí` reduce el desajuste a 32 sin resolverlo.

— polarity: negative (ambiguity of convention) · confidence: high · related: anexo L6, §71.14 (L1557/L1600), E2 iter4 observación 1

### F-V8-007 — §70 afirma «38 referencias» en ambas versiones; el anexo numerado tiene 41

L1497 (ES): «La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`»; L1499 (EN): «A numbered list of 38 references and their verification status is available in `Data/referencias.md`». El anexo al que apuntan tiene 41 líneas numeradas, de [1] a [41] sin huecos; las tres ausentes de la cifra son precisamente las institucionales [39]–[41], que tampoco están en la tabla de 38 filas de §71.14 (L1598). El documento nunca declara explícitamente que [39]–[41] formen un bloque aparte —su inclusión en el anexo es de hecho posterior al armado de la tabla—, de modo que la cifra 38 es falsa para la fuente citada. E2 iter4 (H1) lo detectó y se confirma aquí.

— polarity: negative · confidence: high · related: §70 (L1497/L1499), anexo [1]–[41], §71.14 (L1598), E2 iter4 H1, C009

### F-V8-008 — §70 generaliza `(metadata incomplete)` a «las fuentes restantes» en ambas versiones; solo cuatro entradas lo llevan

L1497: «Las fuentes restantes figuran con estado `(metadata incomplete)` en `reviews/informe-tecnico-2026-11-27.e2-literature.md` y no se presentan como referencias verificadas»; L1499: «Remaining sources are marked `(metadata incomplete)` in `reviews/informe-tecnico-2026-11-27.e2-literature.md` and are not presented as verified references». En `Data/referencias.md` solo cuatro de 41 entradas llevan efectivamente esa marca: [1] (resumen indexado no sustantivo), [10] (resumen no indexado), [12] (PDF no extraido) y [39] (URL profunda no confirmada). Las notas de discrepancia de año de [2], [19] y [38] pertenecen a otro campo distinto. Además, el archivo enlazado es el mapa de la primera pasada (27/11), no el de esta iteración (28/11). La frase generaliza un estado que el anexo no sostiene campo por campo. E2 iter4 (observación agregada 2) coincide.

— polarity: negative · confidence: high · related: §70 (L1497/L1499), anexo [1]/[10]/[12]/[39], E2 iter4 observación 2

### F-V8-009 — Integridad estructural del anexo: 41 entradas continuas, sin autor ausente ni duplicado detectable; verificación externa heredada

Comprobación directa: 41 líneas `^[n]`, de [1] a [41] sin huecos ni números repetidos; los 38 trabajos con año tienen autores, título, venue e identificador (DOI o arXiv); los tres institucionales [39]–[41] tienen autor institucional y URL. No se detectaron ghost papers por título genérico sin fuente, ni IDs arXiv con prefijo de fecha imposible respecto de la fecha del informe (23/11/2026): el más reciente es `arXiv:2601.14311` [24] (enero 2026), anterior al informe. Los DOIs siguen el patrón `10\.\d{4,9}/…`; se observa un punto inicial inusual en el sufijo de [27] (`10.54660/.jfmr.2023.4.1.529-538`), no verificado en vivo en esta pasada y por eso no calificado como roto. Salvedad de método: no se re-ejecutaron búsquedas OpenAlex/Crossref ni se re-leyeron resúmenes; los metadatos y conteos de citas se heredan de la verificación del 27/11 consignada en el anexo, igual que en E2 iter4. Por eso `verified: 37` / `unverified: 4`: los cuatro no verificados son los que el anexo marca `(metadata incomplete)`, no papers inexistentes.

— polarity: positive (with method caveat) · confidence: medium-high · related: anexo [1]–[41], E2 iter4 nota de entrada

## Resumen (3 líneas)

1. `Data/referencias.md` tiene 41 entradas continuas y los cinco desajustes de flag que E2 registró están corregidos ([9], [14], [18], [26], [29]); queda [18] con la ubicación incompleta, pues omite el marcador de §34.
2. Los tres focos pedidos convergen en [39]: flag que cita un §71.14 donde no aparece, contradicción entre `(metadata incomplete)` y el «verificado en vivo» de §18/§70, y formato divergente; [41] resolvió en vivo, [39] y [40] dieron timeout desde este entorno.
3. La contradicción de Akerlof se reproduce en las dos versiones de §70 («verificada» con flag `metadata incomplete`) y §71.14 (L1600) atribuye erróneamente [1] a §71.6, cuando está en §17/§19; la convención de «38 referencias» y el campo `Citada` siguen sin cuadrar con el anexo de 41.


## §9 — v9-ethics


## Resumen

- §69 (L1487–L1491) conserva los tres elementos de `V9.ai_use_declaration.master`: herramientas nominales, cuatro fases y protocolo de supervisión; la huella citada apunta ahora a la iteración 3, verificada en E3.
- La declaración se comprime respecto de la iteración 3 (fases en sustantivos sueltos, sin criterio de aceptación explícito); no hay artefacto V7 de esta iteración, así que no se emite hallazgo cruzado de densidad.
- §71.15 (L1551–L1555) declara COI, doble uso y disponibilidad; la tensión entre «no se reclutaron sujetos humanos» y la encuesta a 33 personas con entrevistas que incluyen nombres (L1287–L1289) queda registrada; la licencia sigue pendiente y coincide con el repositorio.

### F-V9-001 — §69 satisface el criterio master de declaración de uso de IA: herramientas, cuatro fases y supervisión

La sección se titula «Declaración de uso de inteligencia artificial / AI-use declaration» (L1487). La versión ES declara: «Las herramientas de IA (OpenCode/Claude Code con las skills `review`, `deep-research` y `technical-writing`) se usaron en investigación, redacción, código y traducción» (L1489); la EN reproduce la declaración: «AI tools (OpenCode/Claude Code with `review`, `deep-research` and `technical-writing`) were used for research, drafting, code and translation» (L1491). El protocolo de supervisión figura en el mismo párrafo: «Cada cifra se contrastó contra los CSV versionados y las pruebas automatizadas; la huella queda en `reviews/`» (L1489), con equivalente en L1491, y se ilustra con el caso «un R² citado como 0,277 que el CSV daba como 0,274 y se corrigió con marcadores» (L1489). El criterio `V9.ai_use_declaration.master` exige: «Declaration expected; should name tools, phases (research, drafting, code generation, translation), and supervision protocol». Los tres componentes concurren: herramientas con nombre, las cuatro fases que enumera el criterio y una supervisión con acciones verificables (contraste contra CSV, pruebas y registro bajo `reviews/`). El cierre «El registro de la tercera pasada está en `reviews/informe-tecnico-2026-11-27-iter3.{md,forensic.md}` y sus 13 artefactos» (L1489) atribuye la huella y coincide con el inventario E3 (L188–L191: 45 artefactos de tres pasadas más el plan de la iteración 4).

— polarity: positive · confidence: high · related: [[#F-V9-002]] · criteria: V9.ai_use_declaration.master

### F-V9-002 — Granularidad reducida en §69 respecto de la iteración 3; la huella se desplaza de la pasada 1 a la pasada 3

La declaración de la iteración 3 nombraba «las skills `review` de MatCom, `deep-research` y `technical-writing`» y desplegaba las fases como «investigación y verificación de fuentes, redacción y edición de la narrativa, generación y revisión de código, y traducción bilingüe» (`reviews/informe-tecnico-2026-11-27-iter3.text.md`, L1469). En esta iteración las mismas cuatro fases aparecen como sustantivos sueltos —«investigación, redacción, código y traducción» (L1489)—: se conservan las cuatro categorías del criterio, pero desaparecen los calificadores «generación y revisión de», «bilingüe» y «y verificación de fuentes». El protocolo también se comprime: la formulación previa «contrastar toda cifra contra los CSV y bases versionados, ejecutar las pruebas automatizadas y conservar el registro de auditoría en `reviews/`; ninguna salida de IA se aceptó sin ese contraste» (iteración 3, L1469) pasa a «Cada cifra se contrastó contra los CSV versionados y las pruebas automatizadas; la huella queda en `reviews/`» (L1489), donde las pruebas se leen como término de comparación y se retiran tanto el criterio de aceptación como la frase de procedencia «ninguna afirmación empírica se originó en una salida de IA sin contraste contra los archivos». El cambio es de detalle, no de cobertura: `V9.ai_use_declaration.master` sigue satisfecho según F-V9-001. En sentido inverso, la huella mejora: la iteración 3 citaba los artefactos de la pasada 1, mientras L1489 cita los de la pasada 3, que E3 confirma presentes (L188–L191). No se recibió `v7_ai_density_hint` y `reviews/` no contiene artefacto V7 de esta iteración, por lo que no se emite hallazgo cruzado de densidad; la verificación cruzada disponible es la de E3.

— polarity: neutral · confidence: high · related: [[#F-V9-001]] · criteria: V9.ai_use_declaration.master

### F-V9-003 — §71.15 declara ausencia de sujetos humanos y de anonimización ejecutada; §50 documenta 33 encuestados y entrevistas con nombres

La declaración reza: «No se reclutaron sujetos humanos: la encuesta de 33 respuestas y las entrevistas se tratan como documentación de contexto, no como datos experimentales; no se requirió un procedimiento de anonimización ejecutado» (L1553; «No human subjects were recruited: the 33-response survey and interviews are context documentation, not experimental data, so no executed anonymisation procedure was required», L1555). El propio informe documenta en §50 que la base consolidada contiene «33 respuestas de encuesta, 30 + 30 + 8 entrevistas» (L1287) y que «la encuesta con datos reales fue un Google Forms de 32 preguntas aplicado a 33 personas de 4 segmentos en un barrio de La Habana»; sobre las entrevistas añade: «son cualitativas, anónimas salvo el grupo de AutosxCuba —que incluye nombres y requiere cuidado—» (L1289). En §7 también se consigna para redes sociales: «No verificables como fuente estadística; requieren consentimiento y sin datos personales» (L847), y en §10 la restricción «aplicar solo datos agregados, sin nombres, teléfonos ni información personal de anunciantes» (L128, equivalente en L270). La búsqueda de «IRB», «comité de ética» y «ethics committee» en el texto en caché no devuelve coincidencias. El criterio `V9.data_ethics.master` condiciona el consentimiento y la aprobación a que sean aplicables; la declaración de no aplicabilidad la establece el documento, mientras el corpus que describe incluye respuestas de 33 personas y un grupo de entrevistas con nombres. No se nombra consentimiento de esos respondientes ni aprobación de comité.

— polarity: negative · confidence: medium · related: [] · criteria: V9.data_ethics.master

### F-V9-004 — Conflicto de intereses: declaración de ausencia presente en §71.15, con equivalente inglés ambiguo

§71.15 registra «Se declara ausencia de conflicto de intereses» (L1553), formulación que cubre el barrido que en la iteración 3 no encontraba declaración formal (`reviews/informe-tecnico-2026-11-27-iter3.v9-ethics.md`, L37). La versión EN, «No conflict of interest is declared» (L1555), admite dos lecturas: la de una declaración que niega el conflicto y la de la ausencia de tal declaración; el texto ES es inequívoco. No se nombran tutores, asesores ni patrocinadores; la única otra coincidencia de «conflicto» es narrativa —«relato en 10 actos con personajes, conflicto, hallazgos» (L1150)—. El criterio `V9.coi_statement.master` indica «Not required; tutor/advisor relationship implicit», de modo que la declaración presente supera lo exigible en este nivel y su ausencia no constituiría hallazgo negativo.

— polarity: positive · confidence: medium · related: [] · criteria: V9.coi_statement.master

### F-V9-005 — Doble uso: fuera de la lista sensible, con salvedad de datos de contacto registrada

La declaración señala: «El tema no se considera de doble uso sensible, con la salvedad de que los anuncios contienen datos de contacto que se excluyen de la publicación» (L1553; «The topic is not considered sensitive dual-use, except that listing contact details are excluded from publication», L1555). El objeto del informe —precios de automóviles usados en Cuba, conversiones con TRMI y análisis estadístico— no figura entre los temas que `V9.dual_use` enumera como sensibles (LLMs, vigilancia, biosecuridad, armas autónomas, diagnóstico clínico). En nivel master la discusión se «encourage[d]»; el documento ofrece una discusión breve con la salvedad de contactos y respalda la restricción en §10 con «Protección de datos personales, ciberseguridad y derechos de autor» (L128/L270) y en §71.4 con las amenazas a la validez (L1532–L1539). No hay declaración formal de impacto social; no es exigible en este nivel.

— polarity: neutral · confidence: high · related: [] · criteria: V9.dual_use.master

### F-V9-006 — Disponibilidad de datos y código remitida a §71.5; licencia pendiente y sin commit fijado en el informe

§71.15 remite: «La disponibilidad de datos y código se documenta en §71.5; la licencia queda pendiente de declaración» (L1553; equivalente en L1555). §71.5 consigna la ubicación y la vía de obtención —«Las bases crudas están en `Data/Revolico/` gestionadas con Git LFS y reconstruibles desde `chunks/MANIFEST.json`; el repositorio público es `https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba`» (L1543)— junto al comando único, los puntos de entrada con argumentos, las dependencias fijadas en `requirements.txt` y la prueba de humo (L1543). `V9.data_availability_statement.master` («Brief statement: where the data lives, how to obtain») y `V9.code_availability_statement.master` («"Code available at" statement with URL and brief description») quedan cubiertos por esa remisión y por la URL impresa. La licencia no aparece declarada: «No se ha declarado todavía una licencia de datos o código» (L1543), y E3 confirma que no hay archivo `LICENSE`/`LICENCIA` en la raíz del repositorio (L193–L196), de modo que la limitación está documentada y no es una brecha oculta. El informe no fija commit, etiqueta ni DOI para la versión que produjo los resultados, aunque E3 registra 194 commits y último commit del 28/11/2026 (L18–L21); esa fijación y la licencia formal son precisiones del nivel doctoral, no requisitos del nivel master.

— polarity: positive · confidence: high · related: [[#F-V9-001]] · criteria: V9.data_availability_statement.master, V9.code_availability_statement.master



## §10 — Observaciones transversales

### F-V10-001 — Criterios master cubiertos con evidencia convergente

Quedan cubiertos `V2.ablations.master`, `V2.threats_to_validity.master`, `V2.reproducibility_protocol.master`, `V4.differentiation_from_prior_art.master`, `V4.scope_of_novelty_claim.master`, `V4.prior_art_engagement.master` en su lectura formal, `V5.recency.master`, los seis subcriterios V6 y `V9.ai_use_declaration.master`, `V9.coi_statement.master`, `V9.dual_use.master` y `V9.data/code_availability_statement.master`. La prueba de humo del pipeline se ejecutó 4/4 y la semilla declarada en §71.5 coincide con `run_all.py` y `03c_comparaciones.py`.

— polarity: positive · confidence: high · criteria: V2.ablations.master, V2.threats_to_validity.master, V2.reproducibility_protocol.master, V4.*.master, V5.recency.master, V6.*.master, V9.*.master

### F-V10-002 — Desfase entre la caché y los CSV regenerados por el capturador

Varios hallazgos numéricos nacen del desfase entre el texto cacheado y las tablas que el pipeline regenera mientras la fase 6 sigue «en curso». Las nueve cifras de §59 ya coinciden con los CSV vigentes del momento, pero `modelo_muestra.csv` pasó de 981/584 a 993/586 y `comparaciones.csv` registra H=44,313 frente a H=32,818 en `tests.csv` para el mismo contraste. También quedan fuera del texto la fila del modelo en `baselines.csv` y el recuento de `docs/historia/apendice.md:77`. No son ausencias de método, sino desajustes de consistencia de la corrida que el texto dice vigente.

— polarity: negative · confidence: high · criteria: V2.sample_size.master

### F-V10-003 — Umbrales master por debajo cuya causa no es el desfase

Permanecen por debajo `V2.baselines.master` (dos medianas triviales; la referencia egipcia sin métrica local), `V2.statistical_tests.master` (H1 enuncia control por edad y km mientras el contraste es univariate; Welch declarado pero ausente de `tests.csv`), `V2.sample_size.master` (ocho fuentes, 28 observaciones en el modelo completo), `V5.coverage_breadth.master` (6/38 marcadores frente al tramo 25–60), `V5.citation_weight.master` (12/15 afirmaciones portantes sin cita), `V5.missing_important_work.master` (siete ausencias), `V4.prior_art_engagement.master` (una cláusula por obra, sin resultados ni limitaciones ajenas) y `V9.data_ethics.master` (tensión entre «sin sujetos humanos» y la encuesta de 33 respuestas con entrevistas nominadas). El aparato bibliográfico aporta además contradicciones en [39], Akerlof [1], el recuento de referencias y los flags `no`, y la inversión 71.15→71.14.

— polarity: negative · confidence: high · criteria: V2.baselines.master, V2.statistical_tests.master, V2.sample_size.master, V4.prior_art_engagement.master, V5.coverage_breadth.master, V5.citation_weight.master, V5.missing_important_work.master, V9.data_ethics.master

### F-V10-004 — Declaración de IA aligerada y posicionamiento sin espejo inglés

§69 satisface el criterio master con herramientas, fases y supervisión, y su huella apunta a los artefactos vigentes, pero se comprime de 271 a 147 palabras y pierde las negaciones de salvaguarda; la densidad de metaconceptos cae de 44,3 a 13,6 por 1.000 palabras. En §71.6 los cuatro «Frente a…» se sustituyen por marcadores `[N]` y baja la densidad, pero el párrafo sigue sin glosa «EN.» mientras 71.1–71.5 y 71.15 sí la tienen.

— polarity: neutral · confidence: high · criteria: V9.ai_use_declaration.master

## Apéndice A — Plan

# Plan de auditoría — Iteración 4

Cuarta pasada tras corregir los 48 hallazgos de neutral hacia abajo de la
iteración 3: resumen VSN-C, hipótesis falsable, bases con métrica e IC,
semilla propagada, 41 referencias, declaraciones y paralelos ingleses.

Objetivo: verificar si queda algo por debajo del criterio master. Se
re-ejecutan E1–E3 y V1–V9 y se calibran contra `level-criteria.md`.


## Apéndice B — Claims

# Claim Inventory

## Summary
- Total: 125
- Load-bearing: 15 · Supporting: 72 · Contextual: 38
- By type: result 66 · methodological 45 · novelty 3 · contextual 43 · definitional 9 · citation-grounded 5

## Load-bearing claims

### C001 — Hipótesis falsable H1 y rechazo con Kruskal-Wallis

- **Section**: Resumen (VSN-C) (L14–21); Abstract (VSN-C) (L156–163)
- **Lines**: 21, 163
- **Types**: result, methodological
- **Excerpt**: «**Hipótesis falsable (H1):** «los precios de los tres tiers de marca en el mercado local provienen de la misma distribución, controlando por antigüedad y kilometraje». Se contrasta con Kruskal-Wallis; se rechaza con p < 0,001 en la corrida vigente.»
- **Restated**: En la corrida vigente se rechaza con p < 0,001 la hipótesis de que los tres tiers de marca provienen de la misma distribución de precios, controlando por antigüedad y kilometraje.
- **Internal evidence cited**: §71.3 (L1528: H = 44,313; IC bootstrap 10.000–29.500 USD), §60 (L1409: Kruskal-Wallis p = 0,00000), §71.2 (L1522)
- **External evidence cited**: — (sin citas numeradas en el enunciado)
- **Novelty signals**: «Hipótesis falsable (H1)» (L21), «Falsifiable hypothesis (H1)» (L163)
- **Notes**: el paralelo inglés (L163) declara el mismo rechazo con la notación «p < 0.001»; §60 y §71.3 usan «0,00000» y H = 44,313.

### C002 — Cifras canónicas de la corrida vigente del 27/11/2026

- **Section**: §59 Storytelling alineado con los datos finales (L1397–1403)
- **Lines**: 1399
- **Types**: result
- **Excerpt**: «El relato ahora usa **<!-- kpi:autos_revolico -->974 autos únicos**, **<!-- kpi:anuncios_totales -->2.174 anuncios limpios** (<!-- kpi:anuncios_locales -->1.483 locales y <!-- kpi:anuncios_importacion -->691 de importación), mediana local de **<!-- kpi:precio_mediano_usd -->21.000 USD**,…»
- **Restated**: La corrida vigente produce 974 autos únicos, 2.174 anuncios limpios (1.483 locales y 691 de importación), mediana local 21.000 USD, kilometraje mediano 32.569 km, 50 marcas, 114 grupos comparables y 89 anomalías.
- **Internal evidence cited**: §59 (L1403, espejo inglés con 974/2.174/21.000 USD), §58 (L1391, estado previo 2.014 anuncios y 44.125 km), §71.1 (L1511–1512, 1.462 anuncios en las bases)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: los marcadores `<!-- kpi:... -->` forman parte del texto cacheado; la frase «los valores se actualizan solos» remite al actualizador de `outputs/tables/kpis.csv`.

### C003 — Depreciación anual y prima premium retiradas en la corrida vigente

- **Section**: §59 (L1401); §60 Inventario de funciones y modelos (L1409)
- **Lines**: 1401
- **Types**: result, methodological
- **Excerpt**: «La depreciación se reformuló con honestidad: el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra.»
- **Restated**: En la corrida vigente el coeficiente de edad del modelo hedónico no es significativo tras controlar por kilometraje y no se reporta una prima premium cuantificada.
- **Internal evidence cited**: §60 (L1409: p mínimo 0,0941; VIF 1,12–1,40; Kruskal-Wallis p = 0,00000), §71.2 (L1522), §71.4 (L1537), §34 (L1076: cifra retirada de −5,43 % anual)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: §44 (L1226)conserva −5,43 %, +21 % y −22 % con la salvedad explícita de que la corrida vigente ya no los sostiene; §45 (L1234) conserva −5,43 % sin esa salvedad.

### C004 — Ablación del término `hp`: muestra y R²

- **Section**: §71.2 Ablación explícita / Explicit ablation (L1520–1524)
- **Lines**: 1522
- **Types**: result, methodological
- **Excerpt**: «`modelo_muestra.csv` documenta la ablación del término `hp`: al retirarlo, la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² baja de 0,274 a 0,101. El cambio de especificación y el cambio de muestra se informan juntos.»
- **Restated**: Retirar `hp` reduce el R² de 0,274 a 0,101 y amplía la muestra de 28 a 584 de 981 candidatas, informando ambos cambios conjuntamente.
- **Internal evidence cited**: §59 (L1401: 28 observaciones, R² 0,274, p del F 0,411), §71.1 (L1516: modelo principal con 584 observaciones y R² 0,101)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: el propio apartado atribuye la pendiente positiva de antigüedad a la selección de anuncios con kilometraje declarado, no a una tasa de depreciación (L1522).

### C005 — Intervalo bootstrap de la diferencia de medianas premium−económico

- **Section**: §71.3 Pruebas y tamaño muestral / Tests and sample size (L1526–1530)
- **Lines**: 1528
- **Types**: result, methodological
- **Excerpt**: «El contraste central se cuantifica con H = 44,313 y un intervalo bootstrap de la diferencia de medianas premium−económico de <!-- kpi:ci_bajo -->10.000 a <!-- kpi:ci_alto -->29.500 USD (`comparaciones.csv`, 2.000 réplicas).»
- **Restated**: El contraste central se cuantifica con H = 44,313 y un intervalo bootstrap de 10.000 a 29.500 USD para la diferencia de medianas entre premium y económico, con 2.000 réplicas.
- **Internal evidence cited**: §71.1 (L1511–1512: bases informan solo MAE), §60 (L1409), §71.4 (L1537)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: es el único intervalo numérico declarado en el documento; las bases de comparación de §71.1 no llevan intervalo asociado a su MAE.

### C006 — Semilla declarada y propagada a cada etapa

- **Section**: §71.5 Protocolo, semillas y reproducción / Protocol, seeds and reproduction (L1541–1545)
- **Lines**: 1543
- **Types**: methodological
- **Excerpt**: «La semilla `SEED = 20261127` está declarada en `run_all.py` y se propaga a cada etapa por la variable de entorno `PROYECTO_SEED`; antes se declaraba sin efecto.»
- **Restated**: La semilla 20261127 está declarada en el orquestador y se propaga a las etapas mediante la variable de entorno `PROYECTO_SEED`, frente a la declaración anterior sin efecto.
- **Internal evidence cited**: §71.5 (L1543: comando único, puntos de entrada, dependencias fijadas y prueba de humo), §69 (L1489: registro de auditoría)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: el enunciado consigna explícitamente el cambio de estado respecto de la declaración sin propagación.

### C007 — Declaración de uso de inteligencia artificial

- **Section**: §69 Declaración de uso de inteligencia artificial / AI-use declaration (L1487–1491)
- **Lines**: 1489
- **Types**: methodological
- **Excerpt**: «Las herramientas de IA (OpenCode/Claude Code con las skills `review`, `deep-research` y `technical-writing`) se usaron en investigación, redacción, código y traducción. Cada cifra se contrastó contra los CSV versionados y las pruebas automatizadas; la huella queda en `reviews/`. Un ejemplo…»
- **Restated**: Las herramientas de IA se usaron en cuatro labores declaradas y cada cifra fue contrastada contra CSV versionados y pruebas automatizadas, con un ejemplo concreto de corrección de R².
- **Internal evidence cited**: §59 (L1401: R² 0,274), §70 (L1497), mención de `reviews/informe-tecnico-2026-11-27-iter3.{md,forensic.md}` y sus 13 artefactos (L1489)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: el texto de esta iteración ya no enumera las cuatro fases ni los tres pasos de supervisión registrados en la iteración 3; conserva el ejemplo de corrección y el apuntador a la pasada anterior.

### C008 — Declaraciones éticas, de doble uso y de disponibilidad

- **Section**: §71.15 Declaraciones / Declarations (L1551–1555)
- **Lines**: 1553
- **Types**: methodological, definitional
- **Excerpt**: «No se reclutaron sujetos humanos: la encuesta de 33 respuestas y las entrevistas se tratan como documentación de contexto, no como datos experimentales; no se requirió un procedimiento de anonimización ejecutado. Se declara ausencia de conflicto de intereses. El tema no se considera de…»
- **Restated**: El documento declara ausencia de sujetos reclutados, de procedimiento de anonimización ejecutado, de conflicto de intereses y de doble uso sensible, con datos y código disponibles según §71.5 y licencia pendiente.
- **Internal evidence cited**: §71.5 (L1543: repositorio público, comando único y Git LFS), §50 (L1289: 33 respuestas y entrevistas)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: el apartado se numera 71.15 y antecede al 71.14 (L1557).

### C009 — Referencias verificadas y convención numérica

- **Section**: §70 Referencias verificadas / Verified references (L1495–1499); §71.14 Obras del mapa literario citadas en el cuerpo (L1557–1600)
- **Lines**: 1497, 1499
- **Types**: citation-grounded
- **Excerpt**: «Referencias citadas y verificadas externamente durante la auditoría: Akerlof (1970), *The Market for "Lemons"* (DOI 10.2307/1879431 confirmado en OpenAlex; el resumen indexado es solo un índice de secciones, por lo que su flag es `(metadata incomplete: resumen)`); UK Department for…»
- **Restated**: El documento declara cuatro referencias verificadas externamente, con el resto marcado como `(metadata incomplete)`, y remite la convención numerada a `Data/referencias.md`.
- **Internal evidence cited**: §18 (L838–849: tabla de procedencia), §71.6 (L1549), §71.14 (L1561–1598: fichas [1]–[38])
- **External evidence cited**: [1] Akerlof (1970), DOI 10.2307/1879431 confirmado en OpenAlex; DfT/DVLA (GOV.UK); ANFAC (sitio oficial); AEADE (sitio oficial) — todos según L1497
- **Novelty signals**: ninguno.
- **Notes**: la convención declarada es de «38 referencias» (L1497, L1499) y la tabla de §71.14 llega a [38] (L1598); el resto se remite a `reviews/informe-tecnico-2026-11-27.e2-literature.md`.

### C010 — Objetivo vigente: análisis de mercado; recomendador diferido

- **Section**: §1 Objetivo (L23–27); §21 Cambio de objetivo (L899–908); Parte II §1 (L165–169); Parte II §12 (L284–290)
- **Lines**: 25
- **Types**: definitional, contextual
- **Excerpt**: «El proyecto se llama **El precio de moverse en Cuba**. Su objetivo actual es realizar un **análisis del mercado automotor cubano**: caracterizar estructura, precios, oferta, segmentos, tendencias, asequibilidad y condiciones de rentabilidad. La definición de un producto interactivo que…»
- **Restated**: El objetivo declarado es el análisis del mercado automotor cubano y no la recomendación interactiva, diferida a una especialización futura.
- **Internal evidence cited**: §21 (L903–905), Parte II §12 (L290), Parte II §1 (L167)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: la conclusión 5 inglesa (L290) declara ahora el mismo diferimiento que la Parte I (L148), sin la contradicción registrada en la iteración 3.

### C011 — Fase 8 implementada y regenerada automáticamente

- **Section**: §12 Conclusiones (L142–148); §2 nota de actualización (L47); §61 Sitio MkDocs (L1415–1421)
- **Lines**: 148
- **Types**: result, methodological
- **Excerpt**: «El análisis de mercado y el modelo de rentabilidad (fase 8) están implementados en `Data/analisis_rentabilidad/` y se regeneran de forma automática; la definición del producto interactivo se difiere a una especialización futura.»
- **Restated**: El pipeline de análisis y rentabilidad existe en `Data/analisis_rentabilidad/` y puede regenerarse automáticamente.
- **Internal evidence cited**: §34 (L1036–1057), §59 (L1399), §61 (L1417–1419)
- **External evidence cited**: —
- **Novelty signals**: ninguno.
- **Notes**: la nota de §2 (L47) data la creación del pipeline el 18/11/2026 y remite sus resultados vigentes a §59–§60.

### C012 — Procedencia de los datos y separación de tasas y precios

- **Section**: §18 Auditoría de procedencia (L834–853); §23 (L922); §71.4 (L1534)
- **Lines**: 851
- **Types**: methodological, definitional
- **Excerpt**: «**Conclusión:** las fuentes oficiales y gremiales sirven de **contexto y validación**; los anuncios y redes son la **señal de precio** pero no sustituyen estadísticas oficiales. El análisis debe etiquetar cada métrica con su procedencia y nivel de confianza, y no mezclar tasas oficiales e…»
- **Restated**: El análisis trata los anuncios como señal de precio pedido, etiqueta cada métrica con procedencia y confianza, y prohíbe mezclar tasas oficiales con informales o precios anunciados con transaccionados.
- **Internal evidence cited**: §18 (L838–849: tabla de procedencia), §23 (L922: TRMI fija de 930 CUP/USD), §52 (L1317: API del BCC como referencia oficial)
- **External evidence cited**: DfT/DVLA y ANFAC/AEADE, declarados verificados en vivo en §18 (L838, L842–843) y §70 (L1497)
- **Novelty signals**: ninguno.
- **Notes**: el par inglés (L853) repite la misma restricción con «advertised-price signals only».

### C013 — Posicionamiento frente a trabajos cercanos con remisiones [14], [26], [9], [29]

- **Section**: §71.6 Posicionamiento frente a trabajos cercanos / Positioning against prior work (L1547–1549)
- **Lines**: 1549
- **Types**: novelty, citation-grounded
- **Excerpt**: «Gegić y otros [14] predicen precios con aprendizaje automático sobre catálogos estructurados; aquí las variables se extraen de anuncios en lenguaje libre, así que el aporte es de procedencia y normalización, no de algoritmo. Muça, Bani y Alla [26] integran datos públicos albaneses por…»
- **Restated**: El aporte se diferencia de cuatro trabajos cercanos por procedencia y normalización, conversión con TRMI fechada, ausencia de tasa anual y tratamiento de la divisa informal como convención.
- **Internal evidence cited**: §70 (L1497), §71.14 (L1569 [9], L1574 [14], L1586 [26], L1589 [29])
- **External evidence cited**: [14] Gegić (2019), [26] Muça (2026), [9] Du (2026), [29] Vidal Alejandro (2024), según las fichas de §71.14
- **Novelty signals**: «el aporte es de procedencia y normalización, no de algoritmo» (L1549); «el énfasis está en la conversión con TRMI fechada» (L1549)
- **Notes**: el pasaje incorpora marcadores numéricos [14], [26], [9] y [29]; L1600 enlaza las fichas con `Data/referencias.md`.

### C014 — Novedad declarada: procedencia y normalización como objeto de auditoría

- **Section**: Resumen (VSN-C) (L18); Abstract (VSN-C) (L160)
- **Lines**: 18
- **Types**: novelty, methodological
- **Excerpt**: «**Novedad:** la procedencia y la normalización se tratan como objeto de auditoría; la pérdida de muestra por variables ausentes se reporta como hallazgo y no se oculta.»
- **Restated**: La novedad reclamada es el tratamiento de la procedencia y la normalización como objeto de auditoría y el reporte explícito de la pérdida de muestra por variables ausentes.
- **Internal evidence cited**: §18 (L834–853), §60 (L1409), §71.2 (L1522), §71.4 (L1535)
- **External evidence cited**: —
- **Novelty signals**: «Novedad» (L18), «News» (L160), «no se oculta» (L18), «is reported as a finding» (L160)
- **Notes**: el resumen inglés (L160) llama «News» a este apartado y usa «sample loss from missing variables is reported as a finding».

### C015 — Contribuciones declaradas en el resumen VSN-C

- **Section**: Resumen (VSN-C) (L19); Abstract (VSN-C) (L161); §69 (L1489)
- **Lines**: 19
- **Types**: result, novelty
- **Excerpt**: «**Contribuciones:** base compacta reproducible, panel interactivo autocontenido, pipeline con timers y un expediente de auditoría con 13 artefactos.»
- **Restated**: Las contribuciones declaradas son una base compacta reproducible, un panel interactivo autocontenido, un pipeline con timers y un expediente de auditoría de 13 artefactos.
- **Internal evidence cited**: §54 (L1345: chunks y manifiesto), §61 (L1419: `Data/dashboard.html`), §65 (L1453: cinco timers), §69 (L1489: 13 artefactos de la pasada anterior)
- **External evidence cited**: —
- **Novelty signals**: «Contribuciones» (L19), «Contributions» (L161)
- **Notes**: la cifra 13 se apoya en la huella de la iteración 3 citada en L1489, no en una enumeración de esta sección.

## Supporting claims (72)

### C016 — Diecisiete empresas autorizadas y Decreto 163/2026
- **Section**, **Lines**: §4 Marco normativo y regulatorio (L65–67), 67
- **Types**: result, contextual
- **Excerpt**: «Se documentaron **17 empresas autorizadas** a importar y comercializar vehículos, distribuidores privados (BDC One, Dongfeng, MCV, Finauto, Changan, Chinautos, Envision, ATR Export), precios de referencia (BDC One 14.849–31.478 EUR; Dongfeng desde 21.900 EUR; Finauto desde 15.500 EUR; ATR…»
- **Restated**: La fase 1 documentó 17 empresas autorizadas, precios de referencia y el Decreto 163/2026 como norma vigente.
- **Internal/External evidence**: §4 (L67), §4 inglés (L209), §10 (L125); sin citas numeradas en el cuerpo.
- **Notes**: la derogación de la Resolución 312/2026 por la 340/2026 se registra en §52 (L1323).

### C017 — Descubrimiento de fuentes: 409 resultados, 400 únicos y 35 sitios
- **Section**, **Lines**: §5 Descubrimiento y verificación de fuentes (L69–71), 71
- **Types**: result
- **Excerpt**: «Se consolidaron **409 resultados, 400 únicos**. Se inventariaron **35 sitios** de compraventa en `Data/mercados-compraventa-cuba.md` y repositorios útiles en `Data/github-scraping-repos.md`.»
- **Restated**: La fase 2 consolidó 409 resultados, 400 únicos, e inventarió 35 sitios de compraventa.
- **Internal/External evidence**: §5 (L71, L213 en inglés); sin citas numeradas.
- **Notes**: el cambio de DuckDuckGo a Yahoo por CAPTCHA se registra en la misma línea.

### C018 — Cuarenta URLs verificadas y marketplaces con inventario real
- **Section**, **Lines**: §5 (L73)
- **Types**: result
- **Excerpt**: «Se verificaron **40 sitios/URLs**. Marketplaces con sección activa: Autocubana (667 vehículos), iTENCEL (951), VentaCuba (801 carros/camionetas), Timbirichi (281 carros), Revolico (112 enlaces en la primera página), Cogetucarro (5.225 anuncios), Cubisima (155 fichas), Apululu y Carros.com Cuba.»
- **Restated**: Se verificaron 40 sitios y nueve marketplaces presentaban sección activa con los recuentos declarados.
- **Internal/External evidence**: §5 (L73, L215), §12 (L144).
- **Notes**: la misma línea registra correcciones de clasificación de sitios sin sección real o con categoría vacía.

### C019 — Catorce organismos con competencia sobre el mercado
- **Section**, **Lines**: §5 (L75)
- **Types**: result
- **Excerpt**: «Se documentaron **14 organismos** con competencia sobre el mercado: Consejo de Ministros/Estado, MINCEX, MINCIN, MITRANS, CEMA, MFP, ONAT, Aduana General, BCC, MININT, MINJUS, MEP, MINREX y MINSAP.»
- **Restated**: La fase 2 documentó 14 organismos con competencia sobre el mercado automotor.
- **Internal/External evidence**: §5 (L75, L217).
- **Notes**: —
### C020 — Sesenta y un repositorios, 92 proyectos de CAPTCHA y 9 seleccionados
- **Section**, **Lines**: §6 Infraestructura técnica y herramientas (L77–79), 79
- **Types**: result
- **Excerpt**: «Se clonaron **61 repositorios** en `Auxiliares/Repositorios` con `--depth 1` (2,2 GB, 61 entradas `OK`). El conjunto cubre scraping general (Firecrawl, browser-use, Scrapling, crawl4ai, Scrapy, SeleniumBase, trafilatura, curl_cffi, Patchright, Playwright), Facebook, WhatsApp, Telegram y…»
- **Restated**: La fase 3 clonó 61 repositorios, clasificó 92 proyectos de CAPTCHA y seleccionó 9.
- **Internal/External evidence**: §6 (L79, L221).
- **Notes**: el entorno virtual y sus versiones se detallan en L81.

### C021 — Seis herramientas creadas en la fase 3
- **Section**, **Lines**: §6 (L83)
- **Types**: result
- **Excerpt**: «Herramientas creadas: `ddg_research.py`, `buscar_fallback.py`, `descargar_hombros.py`, `scrape_concesionarios.py`, `resumen_catalogos.py` y `actualizar_informe.py`.»
- **Restated**: La fase 3 produjo seis scripts nominales para búsqueda, descarga, scraping y actualización del informe.
- **Internal/External evidence**: §6 (L83, L225).
- **Notes**: —
### C022 — Corpus documental: tres búsquedas y regla de parada
- **Section**, **Lines**: §7 Corpus documental y trabajos investigativos (L85–95), 91–95
- **Types**: result, methodological
- **Excerpt**: «El material se guardó en `Hombros/`: descarga inicial **93 OK / 17 fallos**, rentabilidad **23 OK / 10 fallos**, calidad/precio **78 OK / 36 fallos**, con `manifest.jsonl` e `indice.md`.»
- **Restated**: La regla de parar tras 10 páginas sin enlaces útiles se aplicó a tres búsquedas y produjo los recuentos de descargas declarados.
- **Internal/External evidence**: §7 (L89–95 tabla y texto; L231–237 en inglés).
- **Notes**: la tabla registra 112/1.086/11, 24/226/2 y 23/230/10 páginas/resultados/útiles.

### C023 — Esquema SQLite por tienda con 30 campos estructurados
- **Section**, **Lines**: §8 Diseño del esquema de datos y del pipeline (L97–99), 99
- **Types**: result, definitional
- **Excerpt**: «Se diseñó una base SQLite por tienda con una tabla `vehiculos`: identificación (`url`, `shop`, `title`, `status`, `scraped_at`), metadatos y 30 campos estructurados (`marca`, `modelo`, `anio`, `precio`, `moneda`, `km`, `combustible`, `transmision`, `potencia`, etc.), además de campos sin…»
- **Restated**: La fase 5 definió una base SQLite por tienda con 30 campos estructurados y campos sin normalizar.
- **Internal/External evidence**: §8 (L99, L241).
- **Notes**: §24 (L931) precisa que los campos estructurados de año/km/marca no existen en los JSON de Revolico y se derivan por regex.

### C024 — Once bases preparadas y 256 filas en la fase 6
- **Section**, **Lines**: §9 Scraping y captura (L101–119), 103
- **Types**: result
- **Excerpt**: «Se prepararon 11 bases y se obtuvieron **256 filas**:»
- **Restated**: La fase 6 preparó 11 bases de tienda con 256 filas en total, según la tabla de L105–L117.
- **Internal/External evidence**: §9 (L105–117 tabla; L245–259 en inglés).
- **Notes**: la tabla suma 60+6+19+2+70+1+45+1+45+4+3 = 256 filas.

### C025 — Exclusiones técnicas y densidad de la fase 6
- **Section**, **Lines**: §9 (L119)
- **Types**: result
- **Excerpt**: «Excluidas por bloqueo técnico: carrosw (HTTP 403 con Bot Verification), LlamaCuba (timeout) y SASA/DIVEP (sin catálogo). Mejor densidad: AGN Motors, Chinautos Cuba, Dongfeng Cuba y Finauto. Esta fase sigue abierta: quedan por ampliar fuentes y completar campos.»
- **Restated**: Tres tiendas quedaron excluidas por bloqueo técnico y cuatro se señalan como de mejor densidad, con la fase aún abierta.
- **Internal/External evidence**: §9 (L119, L261).
- **Notes**: Chinautos Cuba aporta 70 filas pero 0 con precio (L111).

### C026 — No elusión anti-automatización y datos agregados
- **Section**, **Lines**: §10 Marco legal (L121–129), 127–128
- **Types**: methodological, definitional
- **Excerpt**: «**Condiciones de uso de cada portal**: criterio operativo para la recolección. No se eluden mecanismos anti-automatización; los HTTP 403/429 se registran como limitación.»
- **Restated**: La recolección declara no eludir mecanismos anti-automatización y registrar los HTTP 403/429 como limitación.
- **Internal/External evidence**: §10 (L127, L269), §11 (L138).
- **Notes**: L128 añade la condición de publicar solo datos agregados, sin nombres, teléfonos ni información personal.

### C027 — Cuatro primeras conclusiones del informe
- **Section**, **Lines**: §12 Conclusiones (L142–148), 144–147
- **Types**: result, contextual
- **Excerpt**: «1. El mercado habanero tiene nueve marketplaces con inventario real y una docena con categorías vacías o solo piezas. / 2. El marco regulatorio vigente es el Decreto 163/2026 y el paquete de resoluciones citado. / 3. El scraping sostenible depende del ritmo, la sesión y la reanudación, no…»
- **Restated**: Las conclusiones 1–4 afirman nueve marketplaces reales, el Decreto 163/2026, la primacía del ritmo y la sesión sobre el fingerprint TLS, y la eficacia de la regla de 10 páginas.
- **Internal/External evidence**: §5 (L71–75), §10 (L125), §11 (L135–140), §7 (L87).
- **Notes**: la conclusión 5 se inventaría por separado (C011).

### C028 — Sincronización de Revolico en fragmentos de 16 MiB
- **Section**, **Lines**: §14 Sincronización automática de Revolico (L774–783), 776
- **Types**: methodological, result
- **Excerpt**: «La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**. Cada 10 minutos un timer de systemd ejecuta `Auxiliares/herramientas/actualizar_revolico.py`: corre el scraper incremental, divide la BD en partes de 16 MiB dentro de `Data/Revolico/partes/`, sube solo las partes…»
- **Restated**: La base de Revolico se sincroniza cada 10 minutos en partes de 16 MiB, con reconstrucción verificada por hash.
- **Internal/External evidence**: §14 (L778–783 tabla: última ejecución 2026-11-17T15:47:42+00:00, 795373568 B, 48 partes).
- **Notes**: §54 (L1345) describe un esquema posterior de 82 chunks de 10 MB sobre 849.465.344 bytes.

### C029 — Eficiencia comparada de Telegram, Facebook, WhatsApp y Playwright
- **Section**, **Lines**: §15 Eficiencia de Telegram, WhatsApp y Facebook (L785–789), 787
- **Types**: methodological
- **Excerpt**: «Para obtener más datos del mercado habanero, la ruta más eficiente es Telegram MTProto (`telethon`, ya integrado): sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`. Le sigue Facebook GQL (`facebook_gql_scraper`): llamadas GraphQL…»
- **Restated**: El documento ordena las rutas de captura por eficiencia, con Telegram MTProto primero, Facebook GQL después y Playwright/Selenium como último recurso.
- **Internal/External evidence**: §15 (L787, L789).
- **Notes**: para WhatsApp declara «no existe API pública personal» y propone WAHA auto-hospedado.

### C030 — Limpieza de 6.332 anuncios: 304 autos y 6.028 exclusiones
- **Section**, **Lines**: §15 (L791–793), 793
- **Types**: result
- **Excerpt**: «**Limpieza ejecutada / Cleaning run (17/11/2026):** sobre los 6.332 anuncios actuales, `limpiar_revolico.py` conservó **304 autos** en la tabla `autos` y registró **6.028 exclusiones** en `revision` (5.983 no vehículo 4+ ruedas, 45 sin datos necesarios, 0 páginas sin datos suficientes).»
- **Restated**: La limpieza del 17/11 conservó 304 autos y registró 6.028 exclusiones sin borrar filas originales.
- **Internal/External evidence**: §15 (L791–793), §31 (L1009: corrida posterior sobre 9.957 anuncios).
- **Notes**: la columna de auditoría `es_auto`, `motivo_exclusion`, `pagina_revisada` y `datos_necesarios` se declara conservada en `anuncios`.

### C031 — Permanencia empírica de los anuncios de Revolico
- **Section**, **Lines**: §15 (L795)
- **Types**: result
- **Excerpt**: «Empíricamente, un anuncio con `updated_on_by_user=2024-12-17` seguía en HTTP 200 el 17/11/2026 (~699 días), por lo que no puede asumirse una expiración de 30 días. El 99,3 % de los anuncios tiene `updated_on_by_user` en los últimos 7 días (mediana 1 día en los 189 autos), lo que indica…»
- **Restated**: Un anuncio con 699 días de antigüedad seguía accesible y el 99,3 % fue actualizado en los últimos 7 días, lo que descarta asumir expiración de 30 días.
- **Internal/External evidence**: §15 (L795), §31 (L1009: anuncio más antiguo 2024-12-17).
- **Notes**: las Condiciones de Uso de Revolico (23/09/2026) no fijan plazo de caducidad según el mismo renglón.

### C032 — Pipeline de colas con commit cada 25 anuncios
- **Section**, **Lines**: §16 Pipeline de colas (L797–809), 803
- **Types**: methodological, result
- **Excerpt**: «3. **Procesamiento**: workers clasifican cada anuncio con `limpiar_revolico.clasificar` y escriben la decisión en `process_queue`. Cada **25 anuncios procesados** (aceptados o rechazados) se hace un commit por lotes en `anuncios`/`autos`/`imagenes`/`telefonos` o en `revision`.»
- **Restated**: El pipeline separa descubrimiento, descarga y procesamiento con colas persistentes y hace commit cada 25 anuncios procesados.
- **Internal/External evidence**: §16 (L799–809), §26 (L948–955: orden corregido), §66 (L1461: lotes de 50 en la corrida posterior).
- **Notes**: L805 registra que `--skip-unchanged` quedó desactivado porque `updatedOnToOrder` es marcador de ranking, no de edición.

### C033 — Prueba del pipeline de colas con una página
- **Section**, **Lines**: §16 (L807)
- **Types**: result
- **Excerpt**: «Prueba con 1 página: **119 enlaces** descubiertos y procesados, 7 lotes de 25, BD principal de 6.332 a **6.334 anuncios** y de 304 a **317 autos**. Todo queda auditado; no se descarta información.»
- **Restated**: La prueba con una página procesó 119 enlaces en 7 lotes y elevó la base de 6.332 a 6.334 anuncios y de 304 a 317 autos.
- **Internal/External evidence**: §16 (L807, L809), §19 (L871: 6.334/317).
- **Notes**: §26 (L955) registra una prueba distinta con 120 enlaces, 63 rechazos tempranos y 326 autos.

### C034 — Siete requerimientos derivados de las fuentes revisadas
- **Section**, **Lines**: §17 Guía de análisis de mercado (L811–832), 830
- **Types**: methodological
- **Excerpt**: «**Requerimientos derivados:** (1) esquema común con precio+moneda normalizada, año/km/combustible/transmisión/marca/modelo/provincia/tipo de vendedor y procedencia; (2) clasificación de calidad y estimación de costos ocultos; (3) comparables por marca-modelo-año-provincia; (4) modelo de…»
- **Restated**: El marco de análisis deriva siete requerimientos, desde esquema común hasta dashboard y validación sin datos personales.
- **Internal/External evidence**: §17 (L815–827 tabla de fuentes; L830), §19 (L868–875), §20 (L881–895).
- **Notes**: la ponderación de preferencias y el producto interactivo quedan fuera de alcance (L830).

### C035 — Clasificación de fuentes por naturaleza y confianza
- **Section**, **Lines**: §18 Auditoría de procedencia (L834–849), 838–849
- **Types**: methodological, contextual
- **Excerpt**: «CarDekho (Kaggle), Spinny, OLX, Revolico, Autocubana, Dongfeng | **Marketplace / anuncios** | No son estadísticas oficiales; son precios **pedidos**, no transaccionados | Señal de precios; requiere dedup, verificación y sesgo declarado»
- **Restated**: La tabla de procedencia clasifica doce tipos de fuente y asigna a los anuncios el papel de señal de precio, no de estadística oficial.
- **Internal/External evidence**: §18 (L838–849), §70 (L1497).
- **Notes**: DfT/DVLA y ANFAC/AEADE figuran como verificados en vivo (L838, L842–843); VAHAN y BCC como no accesibles desde el entorno (L839–840).

### C036 — Adaptación a La Habana: fuentes, variables y límites
- **Section**, **Lines**: §19 Marco de análisis de mercado (L855–877), 871–875
- **Types**: methodological
- **Excerpt**: «- **Fuentes**: Revolico (BD propia, 6.334 anuncios / 317 autos), concesionarios (Autocubana, Dongfeng, BDC One…), Gaceta/Decreto 163/2026, BCC (oficial) y elTOQUE (informal), salarios de la Resolución 14, y señales de Telegram/WhatsApp/Facebook sin datos personales.»
- **Restated**: La adaptación a La Habana declara fuentes, variables, métodos y límites, con precios anunciados separados por moneda.
- **Internal/External evidence**: §19 (L871–875), §20 (L883–891).
- **Notes**: las clases de calidad «≤5 años alta, >5 años con defectos» se atribuyen a PUCE (L873) y a la tabla de §17 (L817).

### C037 — Activos existentes y datos pendientes del marco detallado
- **Section**, **Lines**: §20 Marco analítico detallado (L879–897), 893–895
- **Types**: result
- **Excerpt**: «**Lo que ya existe:** BD de 6.334 anuncios / 317 autos, esquema con 30 campos + auditoría, imágenes/teléfonos, snapshots de precios, normativa documentada, tasas y salarios referenciados, repositorios de modelos y dashboards.»
- **Restated**: El marco detallado enumera activos disponibles y, en la línea siguiente, datos aún pendientes como costos ocultos y precios de transacción.
- **Internal/External evidence**: §20 (L893–895), §56 (L1371: los anuarios no resuelven la laguna de parque y matriculaciones).
- **Notes**: la lista de pendientes incluye año/km/marca/modelo estructurados, series históricas de tasas y salarios y geocodificación (L895).

### C038 — Análisis descriptivo inicial sobre 323 autos
- **Section**, **Lines**: §22 Análisis descriptivo inicial (L910–916), 914
- **Types**: result
- **Excerpt**: «Resultados sobre 323 autos: 248 precios USD válidos (≥500 USD); 74 precios <500 USD marcados como inválidos y 1 en CUP excluidos. Precio mediano **22.000 USD**, media 24.416,59 USD, IQR 11.375–35.000 USD, rango 600–95.000 USD. Marca más frecuente: Hyundai (n=75); municipio con más oferta:…»
- **Restated**: El análisis descriptivo inicial sobre 323 autos halló 248 precios USD válidos, mediana 22.000 USD y predominio de Hyundai y Playa.
- **Internal/External evidence**: §22 (L912–916), §24 (L933: 323 autos).
- **Notes**: es una corrida anterior a la vigente documentada en §59; la mediana allí es 21.000 USD (L1399).

### C039 — Cobertura de campos derivados por heurística
- **Section**, **Lines**: §22 (L914)
- **Types**: result
- **Excerpt**: «Cobertura de campos derivados: marca 68,4 %, año 63,5 %, km 6,2 % (heurísticos, extraídos solo de título/descripción). Detectados 5 outliers por IQR.»
- **Restated**: Los campos derivados por regex cubren 68,4 % de marca, 63,5 % de año y 6,2 % de kilometraje, con 5 outliers por IQR.
- **Internal/External evidence**: §22 (L914, L916), §24 (L931), §71.4 (L1535).
- **Notes**: la baja cobertura de km se vuelve eje de la ablación de §71.2 (L1522).

### C040 — Conversión elTOQUE diaria frente a TRMI fija del modelo
- **Section**, **Lines**: §23 Conversión elTOQUE, serie temporal y gráficas (L918–927), 922
- **Types**: methodological
- **Excerpt**: «**Aclaración vigente:** el pipeline de `Data/analisis_rentabilidad/` usa la TRMI fija de 930 CUP/USD del 18/11/2026 (`config.py`); la serie diaria es referencia histórica, no insumo del modelo actual.»
- **Restated**: El pipeline vigente convierte con TRMI fija de 930 CUP/USD del 18/11/2026 y usa la serie diaria solo como referencia histórica.
- **Internal/External evidence**: §23 (L922, L924), §52 (L1317: API del BCC como referencia oficial).
- **Notes**: L924 registra la TRMI pasando de 680 CUP/USD (09/07/2026) a 920 (16–17/11/2026), ya sustituida por la convención fija.

### C041 — Serie mensual de precios y tasa
- **Section**, **Lines**: §23 (L924)
- **Types**: result
- **Excerpt**: «Ejemplo histórico: la TRMI pasó de 680 CUP/USD (09/07/2026) a 920 (16-17/11/2026), valor ya sustituido por la convención fija de 930 del 18/11/2026 que usa el pipeline; la mediana mensual CUP subió de 12,58 M (julio) a 20,7 M (noviembre).»
- **Restated**: La serie histórica muestra TRMI de 680 a 920 CUP/USD y mediana mensual CUP de 12,58 M a 20,7 M entre julio y noviembre.
- **Internal/External evidence**: §23 (L924, L925).
- **Notes**: L925 registra 8 PNG y `dashboard_interactivo.html` generados por `graficos_mercado.py`.

### C042 — Supuesto de anuncio activo = comprable
- **Section**, **Lines**: §23 (L923); §25 (L941)
- **Types**: methodological, definitional
- **Excerpt**: «**Supuesto de anuncio activo**: todos los registros tienen `status=PUBLISHED` y página verificada en la captura, por lo que se asume que son comprables; no se comprueba disponibilidad en tiempo real.»
- **Restated**: El análisis asume que los anuncios con `status=PUBLISHED` y página verificada son comprables, sin comprobación de disponibilidad en tiempo real.
- **Internal/External evidence**: §23 (L923), §25 (L941: supuesto distinto para catálogos), §19 (L875: sesgo de supervivencia).
- **Notes**: es un supuesto operativo declarado, no una verificación de transaccionalidad.

### C043 — Ausencia de campos estructurados en los JSON de Revolico
- **Section**, **Lines**: §24 Estado del scrapeo y procesamiento de diccionarios (L929–935), 931
- **Types**: result
- **Excerpt**: «**No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**: por eso `anio_est`, `marca_est` y `km_est` se derivan con regex del texto visible (cobertura 63,5 %, 68,4 % y 6,2 %).»
- **Restated**: Los diccionarios `ad_json` y `apollo_full` no contienen claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión.
- **Internal/External evidence**: §24 (L931), §22 (L914), §51 (L1302).
- **Notes**: los JSON sí guardan precio, moneda, estado, fecha y geografía (L931).

### C044 — Reporte de scrapeo y estado de colas
- **Section**, **Lines**: §24 (L933)
- **Types**: result
- **Excerpt**: «**Reporte de scrapeo:** `anuncios` 6.334 · `autos` 323 · `revision` 6.085 · `imagenes` 13.932 · `telefonos` 7.699 · BD 520,6 MB. Colas: `url_queue` 141 (125 done, 3 downloading, 13 pending); `download_queue` 125 (123 processed, 1 processing, 1 pending); `process_queue` 123 (107 committed,…»
- **Restated**: El reporte de scrapeo declara 6.334 anuncios, 323 autos, 6.085 revisiones, 13.932 imágenes y 7.699 teléfonos, con colas pendientes de una corrida interrumpida.
- **Internal/External evidence**: §24 (L933, L935), §27 (L964).
- **Notes**: los pendientes se atribuyen a un reinicio del servidor (L933).

### C045 — Reinicio automático del servicio de scrapeo
- **Section**, **Lines**: §25 Reanudación, resiliencia y supuesto de catálogos (L937–944), 940
- **Types**: methodological
- **Excerpt**: «**Reinicio automático:** `revolico-scrape.service` ahora tiene `Restart=on-failure`, `RestartSec=30`, `StartLimitIntervalSec=300` y `StartLimitBurst=20`, de modo que una pérdida de conexión que detenga el proceso provoca su relanzamiento.»
- **Restated**: El servicio de scrapeo se relanza automáticamente tras fallo con los parámetros systemd declarados.
- **Internal/External evidence**: §25 (L940), §37 (L1124), §65 (L1453).
- **Notes**: —
### C046 — Supuesto de disponibilidad de catálogos
- **Section**, **Lines**: §25 (L941)
- **Types**: methodological, definitional
- **Excerpt**: «Para concesionarios y páginas similares (`CATALOGOS`) se asume que todo el catálogo está disponible salvo que la página indique lo contrario y que se publicó el día de la captura (`fecha_publicacion = scraped_at`); el año del vehículo no es clave.»
- **Restated**: Para catálogos se asume disponibilidad total y fecha de publicación igual a la captura, salvo indicación contraria.
- **Internal/External evidence**: §25 (L941), §9 (L117).
- **Notes**: para clasificados se mantiene `fecha_publicacion = updated_on_by_user` (L941).

### C047 — Causa del retraso en clasificación y orden corregido
- **Section**, **Lines**: §26 Orden corregido (L946–957), 948
- **Types**: result, methodological
- **Excerpt**: «Se identificó la causa del retraso en la clasificación: el timer ejecutaba `actualizar_revolico.py`, que solo corre el scraper y divide la BD, sin escribir nunca `autos`/`revision`. El servicio ahora ejecuta `scrape_revolico_pipeline.py`, que sigue el orden pedido:»
- **Restated**: El retraso se atribuyó a que el timer ejecutaba un script que no escribía `autos`/`revision`, y se corrigió ejecutando el pipeline de colas.
- **Internal/External evidence**: §26 (L948–955), §16 (L799–807).
- **Notes**: la prueba posterior registra 120 enlaces, 63 descartados tempranamente y autos 323→326 (L955).

### C048 — Umbral de 4.000 anuncios sin revisar
- **Section**, **Lines**: §27 Aviso periódico y umbral de revisión (L959–966), 961–964
- **Types**: methodological, result
- **Excerpt**: «**Umbral:** cuando `anuncios WHERE pagina_revisada=0`llega a **4.000** (configurable con `REVISAR_UMBRAL`), el aviso lanza `revolico-revisar.service`, que ejecuta el pipeline con `--solo-colas`: drena descargas y decisiones pendientes **sin descubrir páginas nuevas**.»
- **Restated**: Un timer de 10 minutos avisa el progreso y lanza el drenaje de colas cuando los anuncios sin revisar alcanzan 4.000.
- **Internal/External evidence**: §27 (L961–964), §33 (L1030).
- **Notes**: el estado declarado es 3.623 sin revisar, por debajo del umbral (L964).

### C049 — Primera corrida del scraper público de Telegram
- **Section**, **Lines**: §28 Primeros datos de Telegram (L968–976), 970–974
- **Types**: result
- **Excerpt**: «Corrida final (50 páginas): **152 mensajes**, **54 anuncios de autos** del canal `goldenbullbusinessfamilycars`, 45 con año detectable y **ninguno con precio explícito** (el canal expresa kilómetros como `25500K`, `40K`, etc.). Esta fuente sirve hoy para señal de oferta/modelo/año, no de precio.»
- **Restated**: La corrida de 50 páginas obtuvo 152 mensajes y 54 anuncios de autos sin precio explícito, útiles solo como señal de oferta/modelo/año.
- **Internal/External evidence**: §28 (L972–974), §29 (L988–991).
- **Notes**: once canales adicionales probados resultaron no aprovechables sin unirse (L974).

### C050 — Base de datos de Telegram y descubrimiento de canales
- **Section**, **Lines**: §29 Base de datos de Telegram (L978–993), 986–991
- **Types**: result
- **Excerpt**: «| `canales` | 119 | ... | `anuncios` | 54 | ... | `anuncios` marcados `es_auto` | 54 | ... / Objetivo de 100 canales de referencia superado (119). El descubrimiento usa 26 búsquedas en tgden.com y valida cada usuario con `t.me/s/`, filtrando por contexto cubano.»
- **Restated**: La base de Telegram consolidó 119 canales, 4 con contexto automotriz y 54 anuncios marcados como autos, superando el objetivo de 100 canales.
- **Internal/External evidence**: §29 (L984–991), §28 (L972).
- **Notes**: los JSONL originales se conservan como respaldo (L991).

### C051 — Git LFS 3.8.1 para SQLite
- **Section**, **Lines**: §30 Gestión de bases de datos con Git LFS (L995–1003), 997–999
- **Types**: methodological
- **Excerpt**: «Se instaló **Git LFS 3.8.1** y se activó en el repositorio. `.gitattributes` marca `*.sqlite`, `*.sqlite-wal` y `*.sqlite-shm` con `filter=lfs diff=lfs merge=lfs -text`; se retiraron las reglas de `.gitignore` que excluían `revolico.sqlite` y los SQLite de concesionarios.»
- **Restated**: Las bases SQLite pasaron a gestionarse con Git LFS 3.8.1, conservando el esquema de partes de Revolico como respaldo auditable.
- **Internal/External evidence**: §30 (L997–1001), §54 (L1347), §71.5 (L1543).
- **Notes**: L1001 advierte sobre el consumo de cuota LFS por blobs nuevos cada 10 minutos.

### C052 — Rango temporal de anuncios y limpieza sobre 9.957
- **Section**, **Lines**: §31 Rango temporal de anuncios Revolico (L1005–1011), 1007–1009
- **Types**: result, methodological
- **Excerpt**: «Se fijó el rango permitido de `updated_on_by_user` entre **2021-01-01 y la fecha actual** en `limpiar_revolico.py` (`FECHA_MINIMA`). Los anuncios fuera de rango van a `revision` con motivo `fuera de rango temporal`.»
- **Restated**: El rango permitido arranca el 01/01/2021; con el anuncio más antiguo del 17/12/2024 no hubo exclusiones por fecha y la limpieza conservó 548 de 9.957 anuncios.
- **Internal/External evidence**: §31 (L1007–1009), §15 (L795).
- **Notes**: —
### C053 — Línea base real de la primera ejecución del pipeline
- **Section**, **Lines**: §34 Esqueleto de análisis de rentabilidad (L1036–1082), 1065–1076
- **Types**: result
- **Excerpt**: «| Filas ingeridas | 972 (716 Revolico + 256 concesionarios) | ... | Filas limpias | 499 (497 usados, 2 nuevos) | ... | Marcas | 32 | ... | Precio mediano usado | 24.000 USD | ... | Antigüedad media | 5,9 años | ... | Observaciones del modelo OLS | 328 | ... | Grupos de benchmark | 21 | ...…»
- **Restated**: La primera ejecución ingirió 972 filas, conservó 499 limpias, reportó 32 marcas, mediana 24.000 USD y 5,9 años de antigüedad media.
- **Internal/External evidence**: §34 (L1063–1074 tabla), §34 (L1082 en inglés).
- **Notes**: L1076 atribuye a esa corrida la depreciación de −5,43 % anual (p<0,001) y primas de +21 %/−22 %.

### C054 — Brecha frente al repositorio egipcio
- **Section**, **Lines**: §34 (L1078–1080), 1080
- **Types**: result, contextual
- **Excerpt**: «Egipto tiene 23.500 anuncios, historial mensual de precios, HP y kilometraje estructurados, ANOVA/OLS/VIF, Tableau y Power BI. La predicción de precios sobre catálogos estructurados tiene antecedentes [14], [18], ausentes del contraste original. Nosotros tenemos el pipeline y las técnicas…»
- **Restated**: El texto declara una brecha de cobertura y frescura frente a Egyptian-Used-Cars y cita como antecedentes [14] y [18].
- **Internal/External evidence**: §34 (L1080), §71.1 (L1513: Egyptian-Used-Cars como referencia cualitativa), §71.14 (L1574 [14], L1578 [18]).
- **Notes**: es un contraste cualitativo sin métrica calculada sobre datos propios.

### C055 — Mecanismo de la app Circuitos Habana
- **Section**, **Lines**: §35 App de circuitos eléctricos de Apklis (L1086–1098), 1088–1093
- **Types**: result
- **Excerpt**: «Con **jadx 1.5.6** descompilé la primera y encontré el mecanismo que buscábamos: - La app **no usa una API privada**: hace scraping del canal público de Telegram `https://t.me/s/EmpresaElectricaDeLaHabana` con Jsoup y User-Agent de Chrome. - Paginación con `?before=<message_id>`, hasta 16…»
- **Restated**: La app descompilada scrapea el canal público de Telegram con Jsoup, pagina con `?before=` y convierte timestamps UTC a hora de Cuba con +1 h de horario de verano.
- **Internal/External evidence**: §35 (L1088–1096), §62 (L1427).
- **Notes**: evidencia y APKs en `Data/apklis/` (L1096).

### C056 — Mapa offline, coordenadas e infraestructura EV
- **Section**, **Lines**: §36 Mapa offline, talleres e infraestructura EV (L1102–1112), 1104–1108
- **Types**: result
- **Excerpt**: «Se extrajeron coordenadas de los **mapas incrustados en las propias webs** de los concesionarios (BDC One: 23.1155203,-82.3596368 y 23.0992805,-82.3050631; Dongfeng: 23.1250339,-82.4227564) y se geocodificó una dirección adicional con Nominatim.»
- **Restated**: Ante la imposibilidad de usar Docker y la ausencia de datos OSM útiles, se extrajeron coordenadas de los mapas incrustados en webs de concesionarios y se documentaron fuentes de infraestructura EV.
- **Internal/External evidence**: §36 (L1104–1108), §41 (L1175), §42 (L1197).
- **Notes**: L1108 registra Dongfeng/NWI 11 estaciones solares (2026) y CIMEX+MITRANS 21 estaciones (2025), con detalle en `Data/mapas/infraestructura_ev_cuba.md`.

### C057 — Optimización de pipelines y efecto medido
- **Section**, **Lines**: §37 Optimización de pipelines (L1116–1126), 1120–1122
- **Types**: result, methodological
- **Excerpt**: «**Efecto medido:** en minutos, los anuncios de Revolico pasaron de 10.117 a **10.149** y los autos de 716 a **814**; quedan 3.351 URLs pendientes y 1.940 rechazadas. Los marketplaces ya completaron Cubisima, Apululu, Carros.com, Autocubana y VentaCuba y siguen con iTENCEL/Timbirichi.»
- **Restated**: La optimización elevó los anuncios de 10.117 a 10.149 y los autos de 716 a 814, con 3.351 URLs pendientes.
- **Internal/External evidence**: §37 (L1120–1122), §39 (L1147–1148), §66 (L1461).
- **Notes**: L1120 atribuye la mejora a sesiones curl_cffi por hilo y al paso de 8/4 a 20/8 descargadores/procesadores.

### C058 — Ampliación de límites de marketplaces
- **Section**, **Lines**: §39 Continuación del scrapeo y presentación narrativa (L1145–1152), 1147
- **Types**: result
- **Excerpt**: «Se ampliaron los límites de `scrape_marketplaces.py`: Cogetucarro de 200 → **5.008**, Autocubana y Timbirichi a 40 páginas. El servicio `marketplaces-scrape.service` se relanzó con 6 workers; en minutos Autocubana pasó de 400 a **566** y Timbirichi de 110 a **170**, totalizando **2.121 anuncios**.»
- **Restated**: Los límites de captura se ampliaron y, en minutos, Autocubana pasó de 400 a 566 y Timbirichi de 110 a 170 anuncios.
- **Internal/External evidence**: §39 (L1147), §9 (L105–117).
- **Notes**: L1148 registra además reintento explícito ante `database is locked` (`_retry_exec`).

### C059 — Gasolineras, cargadores y serie de precios del combustible
- **Section**, **Lines**: §41 Gasolineras, estaciones de carga y serie de precios del combustible (L1171–1182), 1174–1177
- **Types**: result
- **Excerpt**: «**Overpass/OSM devolvió 137 gasolineras en La Habana** con coordenadas, marca, dirección y tipos de combustible. ... Se crearon `Data/mapas/gasolineras.csv` (137) y `Data/mapas/estaciones_carga.csv` (12), y se regeneró `mapa_ofline.html` con tres capas: concesionarios (3), carga eléctrica…»
- **Restated**: Overpass/OSM devolvió 137 gasolineras y se creó una base con 18 observaciones de precios de combustible entre el 20/08/2026 y el 18/11/2026.
- **Internal/External evidence**: §41 (L1174–1178), §42 (L1197: 131 gasolineras en la base unificada).
- **Notes**: Kargalaya aportó 9 estaciones con coordenadas, Electromaps 3 sin coordenadas y ChargeFinder respondió 403 (L1175).

### C060 — Marco normativo del combustible en el storytelling
- **Section**, **Lines**: §43 Apartado de “cuánto costaría moverse” (L1205–1217), 1209–1215
- **Types**: result, contextual
- **Excerpt**: «**7/02/2026:** CIMEX anunció medidas temporales —respaldadas por el MEP y el viceministro Oscar Pérez-Oliva Fraga— que suspendieron la venta en CUP y activaron **Ticket** (20 L por turno, 24 h para usarlo). No se localizó una resolución numerada nueva en la Gaceta Oficial; fue una disposición…»
- **Restated**: El bloque de “cuánto costaría moverse” fecha el Acuerdo 9811 de 2024, las medidas de CIMEX del 07/02/2026, la autorización de importación del 15/02/2026 y la liberalización de precios del 15/05/2026.
- **Internal/External evidence**: §43 (L1209–1215: Cubadebate, Directorio Cubano, CubaTrámite y D-Cuba), §41 (L1180).
- **Notes**: el 15/05/2026 cada importador habilitado fija su precio según costo real de importación (1,80–2,60 USD/L, L1212).

### C061 — Base unificada del mapa con 131/12/25/22 elementos
- **Section**, **Lines**: §42 Base unificada del mapa y talleres (L1186–1201), 1197
- **Types**: result
- **Excerpt**: «Estado final: **131 gasolineras, 12 estaciones de carga, 25 concesionarios (17 con coords) y 22 talleres (todos con coords)**. Los 8 concesionarios sin coords se exportan a `elementos_sin_coordenadas.csv`.»
- **Restated**: La base unificada del mapa contiene 131 gasolineras, 12 estaciones de carga, 25 concesionarios y 22 talleres, con 8 concesionarios sin coordenadas.
- **Internal/External evidence**: §42 (L1188–1199), §41 (L1176).
- **Notes**: L1199 registra el uso de patchright y FlareSolverr tras un 403 de Cybo con curl_cffi.

### C062 — Cifras de la corrida del 18/11 conservadas en el storytelling
- **Section**, **Lines**: §45 Reescritura de la sección 3 del storytelling (L1232–1236), 1234
- **Types**: result
- **Excerpt**: «Se transformó la sección **Lo que encontramos** de una tabla de datos en una narrativa de hallazgos (cifras de la corrida del 18/11/2026, posteriores a las que se recogen en §59): la proporción de anuncios que resisten el filtro de auto real, la mediana de 23.000 USD, la antigüedad media de…»
- **Restated**: El storytelling conserva cifras de la corrida del 18/11/2026 —23.000 USD, 6,3 años, 34 marcas, −5,43 %, 27 grupos y 30 oportunidades— posteriores a las de §59.
- **Internal/External evidence**: §45 (L1234), §59 (L1399–1401), §34 (L1069–1076).
- **Notes**: la depreciación de −5,43 % aparece aquí sin la salvedad que sí se registra en §44 (L1226).

### C063 — Definición de marcas premium y no premium
- **Section**, **Lines**: §48 Definición de marcas premium y no premium (L1256–1265), 1260–1263
- **Types**: definitional
- **Excerpt**: «**Premium:** Mercedes-Benz, BMW, Audi, Lexus, Volvo, Porsche, Land Rover, Jaguar, Cadillac, Infiniti y Acura. - **No premium:** Hyundai, Kia, Toyota, Lada, Fiat, Chevrolet, Peugeot, Honda, Nissan, MG, Dongfeng, Moskvich, Volkswagen, Mitsubishi, Geely, Ford, Jeep, Foton, GMC, SEAT, Renault,…»
- **Restated**: El documento fija una segmentación de dos grupos de marcas para la narrativa, mientras el modelo econométrico conserva tres niveles.
- **Internal/External evidence**: §48 (L1260–1263), §1 (L21: tres tiers de marca), §71.3 (L1528: premium−económico).
- **Notes**: la lista completa con evidencia y conteos se remite a `Data/analisis_rentabilidad/marcas_cuba.md` (L1263).

### C064 — Treinta y seis repositorios cubanos de automoción
- **Section**, **Lines**: §49 Búsqueda de repositorios cubanos de automoción (L1269–1277), 1271
- **Types**: result
- **Excerpt**: «Se buscaron repositorios en GitHub con la API (`gh api search/repositories`) usando 31 consultas en español e inglés: mercado automotriz cubano, carros/autos/vehículos en Cuba, Revolico, motos/triciclos, precios y divisas. Tras deduplicar se obtuvieron **648 repos**, de los que se depuraron…»
- **Restated**: Treinta y y una consultas a la API de GitHub produjeron 648 repositorios únicos, de los que 36 se depuraron como relacionados.
- **Internal/External evidence**: §49 (L1271–1275), §55 (L1359).
- **Notes**: la lista se remite a `Data/github-repos-automotriz-cuba-2026-11-19.md` (L1273).

### C065 — Consolidación de 25 tablas de repositorios de referencia
- **Section**, **Lines**: §50 Consolidación de bases de los repositorios de autos (L1281–1291), 1285–1289
- **Types**: result
- **Excerpt**: «Se creó `Data/repos-autos-referencias/referencias_autos.sqlite` con **25 tablas** (3.958 anuncios de Revolico, 3.566 limpios, catálogos de comercializadoras, 33 respuestas de encuesta, 30 + 30 + 8 entrevistas, datasets de AutosxCuba) y una tabla `provenancia`. De los 3.958 anuncios, **369…»
- **Restated**: La consolidación produjo 25 tablas con 3.958 anuncios, de los que 369 ya estaban en la base propia y 3.589 son nuevos.
- **Internal/External evidence**: §50 (L1283–1289), §71.15 (L1553: 33 respuestas).
- **Notes**: L1285 registra 12 grupos de duplicados bytes y 11 por contenido entre 233 archivos y 76 CSV.

### C066 — Encuesta de 33 respuestas y entrevistas cualitativas
- **Section**, **Lines**: §50 (L1289)
- **Types**: result
- **Excerpt**: «la encuesta con datos reales fue un Google Forms de 32 preguntas aplicado a 33 personas de 4 segmentos en un barrio de La Habana (17 de 18–25 prefieren eléctrico, pero 16 de 18 no pagarían más de 4.000 USD por uno); los otros dos cuestionarios son solo instrumentos sin respuestas. Las…»
- **Restated**: La documentación de encuestas reporta una encuesta con 33 respuestas y 68 entrevistas cualitativas, con un grupo que incluye nombres.
- **Internal/External evidence**: §50 (L1289), §51 (L1305: 28 interesados tras reconciliar), §71.15 (L1553).
- **Notes**: el cruce posterior filtra `interes=1` y da 28 interesados (L1305).

### C067 — Deduplicación de `autos` a 744 únicos
- **Section**, **Lines**: §51 Mejoras del proyecto (L1295–1307), 1299
- **Types**: result
- **Excerpt**: «La tabla se reconstruyó desde `anuncios` (fuente canónica): 814 filas con 748 IDs únicos → **744 autos únicos**. Se excluyeron 4 anuncios que no son autos (`58867937`, `53777554`, `53843413`, `58886962`), marcados en `anuncios` con `es_auto=0` y motivo `no es auto: servicio/combustible`.»
- **Restated**: La deduplicación redujo 814 filas con 748 IDs únicos a 744 autos únicos tras excluir cuatro anuncios reclasificados.
- **Internal/External evidence**: §51 (L1299–1300), §59 (L1399: 974 autos únicos en la corrida vigente).
- **Notes**: se creó el índice único `idx_autos_id` y se incorporaron `EXCLUDE_IDS` e `INSERT OR REPLACE` en `limpiar_revolico.py` (L1299).

### C068 — Reparación de precios y separación por canal en marketplaces
- **Section**, **Lines**: §51 (L1301)
- **Types**: result, methodological
- **Excerpt**: «`parse_price` ahora interpreta separadores de miles (973 anuncios recuperados: 872 de iTENCEL, 99 de Cubisima, 2 de VentaCuba). Los precios vacíos de Autocubana se recuperan del JSON-LD (614 anuncios, mediana 17.000 USD) ... Se incorporó la columna `canal`: **1.301 anuncios locales y 672 de…»
- **Restated**: La reparación recuperó 973 precios y 614 de Autocubana, separó 1.301 anuncios locales de 672 de importación y fijó la mediana local en 21.000 USD.
- **Internal/External evidence**: §51 (L1301), §58 (L1391: 1.323 locales y 691 de importación), §59 (L1399: 1.483 locales y 691 de importación).
- **Notes**: L1301 también registra 116 casos de precios que en realidad son modelo/año en Cogetucarro y 11 marcadores de precio en VentaCuba.

### C069 — Corrección del parseo de kilometraje y ampliación de marcas
- **Section**, **Lines**: §51 (L1302–1303)
- **Types**: result
- **Excerpt**: «`parse_specs` y `parse_title` convertían `80,000 km` en 80 km. Se extrajo `parse_number()` con la lógica de separadores ya usada en `parse_price`. El código está aplicado y probado (`80,000` → 80.000); la regeneración final de los outputs se registra al cierre de la tanda.»
- **Restated**: El parseo de kilometraje corrige los separadores de miles y `config.py` incorpora catorce marcas adicionales con sus alias y tiers.
- **Internal/External evidence**: §51 (L1302–1303), §59 (L1399: mediana de kilometraje 32.569 km).
- **Notes**: el objetivo declarado era reducir los 442 anuncios en tier «desconocido» (L1303).

### C070 — Veinticinco fuentes adicionales y derogación de la Resolución 312/2026
- **Section**, **Lines**: §52 Ampliación de fuentes de datos (L1311–1327), 1313–1323
- **Types**: result, methodological
- **Excerpt**: «El resultado está en `Data/fuentes-adicionales-2026-11-20.md`: **25 fuentes** verificadas, organizadas por tipo con URL, datos expuestos, viabilidad de scraping y aporte al proyecto.»
- **Restated**: La ampliación verificó 25 fuentes y registró que la Resolución 312/2026 fue derogada por la 340/2026, actualizando las referencias.
- **Internal/External evidence**: §52 (L1313–1325), §10 (L126), §4 (L67).
- **Notes**: las cinco fuentes más valiosas se enumeran en L1317–L1321, con la API del BCC como referencia oficial frente a la TRMI informal (L1317).

### C071 — Descarga completa de los anuarios del ONEI
- **Section**, **Lines**: §53 Descarga completa de los anuarios del ONEI (L1331–1339), 1333
- **Types**: result
- **Excerpt**: «A partir del índice oficial `http://www.onei.gob.cu/cuba` se recorrieron las 12 páginas de anuarios disponibles (2014–2025) y se descargaron **todos los documentos enlazados**: 111 PDF, 7 RAR y 103 archivos Excel extraídos, unos 311 MB en total.»
- **Restated**: Se descargaron todos los documentos enlazados de los 12 anuarios del ONEI 2014–2025: 111 PDF, 7 RAR y 103 Excel, unos 311 MB.
- **Internal/External evidence**: §53 (L1333–1337), §56 (L1371).
- **Notes**: L1335 registra 117 enlaces de documento descargados, 0 archivos sospechosos por MIME y conservación sin modificar de los RAR.

### C072 — Base de Revolico distribuida en 82 fragmentos
- **Section**, **Lines**: §54 Base de datos distribuida en chunks (L1343–1351), 1345
- **Types**: result, methodological
- **Excerpt**: «`Data/Revolico/revolico.sqlite` (849.465.344 bytes) se dividió en **82 chunks de 10 MB** en `Data/Revolico/chunks/`, con un `MANIFEST.json` que guarda el SHA-256 del archivo completo, el orden, el offset y el hash de cada fragmento. La verificación de los 82 chunks dio OK.»
- **Restated**: La base de 849.465.344 bytes se dividió en 82 fragmentos de 10 MB con manifiesto SHA-256 y verificación OK.
- **Internal/External evidence**: §54 (L1345–1349), §71.5 (L1543: reconstruible desde `chunks/MANIFEST.json`).
- **Notes**: los fragmentos se publican en la rama huérfana `chunked-db` para no arrastrar el objeto LFS de 804 MB en `main` (L1349).

### C073 — Auditoría de 15 fuentes web y hallazgo de código
- **Section**, **Lines**: §55 Auditoría de fuentes, README y verificación final (L1355–1365), 1357–1363
- **Types**: result
- **Excerpt**: «Se consultaron **15 fuentes web** (8 marketplaces, 7 fuentes oficiales y complementarias): 14 respondieron HTTP 200 y elTOQUE no respondió desde este entorno. Las fechas más recientes en las bases son 17–18/11/2026.»
- **Restated**: La auditoría consultó 15 fuentes, 14 respondieron HTTP 200 y elTOQUE no respondió; la verificación del código detectó y corrigió un `NameError` en `01_ingest.py`.
- **Internal/External evidence**: §55 (L1357–1363), §57 (L1381).
- **Notes**: L1359 registra 33 repositorios auxiliares, 7 cubanos, uno con ref remota atrasada 24 commits y todos con cambios locales sin commitear.

### C074 — Análisis de los anuarios: series útiles y laguna sin resolver
- **Section**, **Lines**: §56 Análisis de los anuarios y estructura de GitHub (L1369–1375), 1371
- **Types**: result
- **Excerpt**: «el transporte de pasajeros cayó un 59 % entre 2019 y 2025 y el ómnibus un 71 %; los accidentes bajaron pero la gravedad aumentó (9,9 fallecidos por cada 100 accidentes en 2025). **No hay series de parque automotor ni de matriculaciones**, por lo que esa laguna signalada en `NECESIDADES.md`…»
- **Restated**: Los anuarios permiten extraer series de transporte y accidentalidad, pero no contienen series de parque automotor ni de matriculaciones.
- **Internal/External evidence**: §56 (L1371), §37 (L895: laguna declarada), §53 (L1337).
- **Notes**: la serie útil se remite a `Data/fuentes-oficiales/ONEI/series_oficiales.csv` y su lectura a `ANALISIS_DATO.md` (L1371).

### C075 — Estructura versionada del repositorio
- **Section**, **Lines**: §56 (L1373)
- **Types**: result
- **Excerpt**: «Se documentó además la estructura versionada en `Data/estructura_github.md`: 1.288 archivos, 157 objetos LFS, distribuidos en `Data` (836), `Hombros` (280), `Auxiliares` (110) y `Anexos` (56), con el detalle de extensiones por carpeta y la lista de repositorios no versionados.»
- **Restated**: El repositorio versiona 1.288 archivos y 157 objetos LFS, distribuidos entre cuatro carpetas con los recuentos declarados.
- **Internal/External evidence**: §56 (L1373), §68 (L1479).
- **Notes**: —
### C076 — Reclasificación de páginas y diez anuncios nuevos en iTENCEL
- **Section**, **Lines**: §57 Reclassificación de páginas y novedades detectadas (L1379–1383), 1381; §58 (L1389–1391)
- **Types**: result
- **Excerpt**: «Resultado: 7 fuentes sin enlaces nuevos; **iTENCEL mostró 10 anuncios nuevos** (`gmc-sierra-2022-add`, `honda-acord-2025-add`, entre otros), tras descartar una página de agrupación falsa.»
- **Restated**: La comparación de enlaces normalizados encontró 7 fuentes sin novedades y 10 anuncios nuevos en iTENCEL, que luego se scrapearon e insertaron.
- **Internal/External evidence**: §57 (L1381), §58 (L1389–1391: 951→961 anuncios, `integrity_check=ok`).
- **Notes**: la normalización incluyó `www.`, query, Unicode NFC y barras finales (L1381).

### C077 — Inventario de transformaciones y estimaciones
- **Section**, **Lines**: §60 Inventario de funciones y modelos (L1407–1411), 1409
- **Types**: methodological, result
- **Excerpt**: «El respaldo es metodológico y empírico: se explica por qué cada forma encaja con datos asimétricos y por qué la corrida actual **no** sostiene una tasa de depreciación ni una prima premium significativa (p mínimo <!-- kpi:modelo_p_min -->0,0941; VIF <!-- kpi:vif_min -->1,12–<!-- kpi:vif_max…»
- **Restated**: El inventario declara p mínimo 0,0941, VIF 1,12–1,40 y Kruskal-Wallis p = 0,00000 para la corrida vigente.
- **Internal/External evidence**: §60 (L1409), §59 (L1401), §71.3 (L1528).
- **Notes**: las tres cifras van en marcadores `<!-- kpi:... -->` del texto cacheado.

### C078 — Sitio MkDocs con compilación estricta
- **Section**, **Lines**: §61 Sitio MkDocs del proyecto (L1415–1421), 1417–1419
- **Types**: result, methodological
- **Excerpt**: «El panel interactivo vigente es `Data/dashboard.html`, copiado a `docs/dashboard.html`; los seis gráficos Plotly se copian a `docs/graficos/` y se enlazan desde el apéndice; las tablas del apéndice y la página de KPIs se generan desde los CSV. `mkdocs build --strict` termina sin errores ni…»
- **Restated**: El sitio MkDocs Material se genera desde Markdown y CSV, incluye el panel y seis gráficos, y compila con `--strict` sin errores ni enlaces rotos.
- **Internal/External evidence**: §61 (L1417–1419), §71.5 (L1543: ruta del panel).
- **Notes**: la navegación sigue Diátaxis con cuatro secciones (L1417).

### C079 — Factibilidad del timelapse de circuitos eléctricos
- **Section**, **Lines**: §62 Factibilidad del timelapse eléctrico (L1425–1429), 1427
- **Types**: result
- **Excerpt**: «Del APK se extrajeron 2.473 puntos, 244 circuitos y 166 polígonos de zonas a `Data/mapas/circuitos/`. El plan de captura, parseo, mapa temporal y límites está en `Data/mapas/TIMELAPSE_CIRCUITOS.md`. Se implementó además `Auxiliares/herramientas/scraper_circuitos.py`: en su primera corrida…»
- **Restated**: El canal público responde HTTP 200 con mensajes del 23/11/2026 y la primera corrida del capturador produjo 35 circuitos sin luz, 23 mixtos y 2 con luz.
- **Internal/External evidence**: §62 (L1427), §35 (L1088–1096).
- **Notes**: un informe de debug corrigió tres fallos —fecha local, filtro de relevancia y palabras de afectación— sin borrar filas (L1427).

### C080 — Estimación de retención declarada como inferencia
- **Section**, **Lines**: §63 Calidad del storytelling como puerta de entrada (L1433–1439), 1435–1437
- **Types**: result, methodological
- **Excerpt**: «La estimación de retención (`Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md`) es **inferencia de diseño, no medición**: de cada 100 visitantes, ~58 leerían el primer párrafo, ~16 llegarían al cierre y ~5 volverían con intención de consulta. Con promesa, CTA y artefacto actualizable, la…»
- **Restated**: La retención estimada es una inferencia de diseño no medida, con 58/16/5 de cada 100 visitantes y una proyección condicionada de 22–25 finalizaciones y 18–22 retornos.
- **Internal/External evidence**: §63 (L1437).
- **Notes**: la propia línea distingue explícitamente inferencia de medición.

### C081 — Cinco timers operativos y coste de red estimado
- **Section**, **Lines**: §65 Automatización operativa y coste de red (L1451–1455), 1453
- **Types**: result, methodological
- **Excerpt**: «Estimación de red: **5–10 MB/mes** si no hay cambios y **50–90 MB/mes** con novedades. Sin internet no se puede scrapear, pero sí ejecutar sin presencia del usuario; si falla la red, `SALUD.md` marca el periodo perdido y el siguiente ciclo `Persistent=true` lo recupera.»
- **Restated**: Se activaron cinco timers `precio-*` con `Linger=yes`, bloqueo `flock`, validación con cuarentena y `SALUD.md`, con un coste de red estimado de 5–10 o 50–90 MB/mes.
- **Internal/External evidence**: §65 (L1453), §64 (L1445).
- **Notes**: el mismo renglón registra dos fallos latentes corregidos: `salud.py` distinguía mal `SIN DATOS` de `STALE` y el ETag se escribía antes del `commit`.

### C082 — Captura continua de Revolico y arquitectura de datos
- **Section**, **Lines**: §66 Extracción continua de Revolico y arquitectura de datos (L1459–1465), 1461–1463
- **Types**: result, methodological
- **Excerpt**: «Se activó `precio-revolico.timer` cada 10 minutos con `--max-pages 3`, 2 descargadores, 2 procesadores y lotes de 50, sin `git push`. ... En la primera corrida corregida los anuncios `done` pasaron de 6.783 a 6.955.»
- **Restated**: El timer de Revolico corre cada 10 minutos con 2 descargadores, 2 procesadores y lotes de 50; tras corregir los enlaces `pending` irreversibles, los anuncios `done` pasaron de 6.783 a 6.955.
- **Internal/External evidence**: §66 (L1461–1463), §37 (L1122), §39 (L1148).
- **Notes**: L1463 documenta Parquet particionado por `year/month`, watermark y rollups mensuales, con DuckDB bloqueado por `SIGILL`.

### C083 — Optimización de espacio y peso en GitHub
- **Section**, **Lines**: §67 Optimización de espacio (L1469–1473), 1471; §68 (L1477–1479), 1479
- **Types**: result
- **Excerpt**: «El repositorio pasó de 20 GB a 10 GB. ... La API de GitHub reporta **205.002 KB (0,20 GB)** para el historial normal; los archivos grandes se guardan aparte y su consumo en GitHub no lo expone la API. En local, esa copia ocupa 3,3 GB con 174 archivos.»
- **Restated**: La limpieza redujo el repositorio de 20 GB a 10 GB, y la API de GitHub reporta 205.002 KB para el historial normal frente a 3,3 GB locales de objetos LFS.
- **Internal/External evidence**: §67 (L1471), §68 (L1479), §56 (L1373).
- **Notes**: leyes y herramientas de scraping se movieron a `~/Utilidades/Leyes` y `~/Utilidades/HerramientasScraping` sin borrarse (L1471).

### C084 — Bases de comparación y sus métricas observadas
- **Section**, **Lines**: §71.1 Bases de comparación / Baselines (L1507–1518), 1511–1516
- **Types**: result, methodological
- **Excerpt**: «| Mediana global ( ingenua ) | Predice la mediana de los usados locales | MAE <!-- kpi:mae_mediana_global -->18.188,34 USD sobre <!-- kpi:n_mediana_global -->1.462 anuncios | ... | Modelo principal propio | OLS de log-precio con antigüedad, km, condición y tier | R² 0,101 sobre 584 observaciones |»
- **Restated**: La mediana global ingenua tiene MAE 18.188,34 USD y la mediana por marca 16.603,28 USD, ambas sobre 1.462 anuncios; el modelo principal reporta R² 0,101 sobre 584 observaciones.
- **Internal/External evidence**: §71.1 (L1511–1518), §71.2 (L1522), §71.3 (L1528).
- **Notes**: las bases llevan MAE sin intervalo asociado; el único IC del documento está en §71.3 (L1528).

### C085 — Diseño independiente y tamaño muestral en anuncios
- **Section**, **Lines**: §71.3 (L1528–1530), 1528
- **Types**: methodological
- **Excerpt**: «No hay diseño pareado: los anuncios son observaciones independientes, por lo que no se aplican Wilcoxon de pares ni t de diferencias; se usan Kruskal-Wallis y Welch para grupos independientes. El tamaño se mide en anuncios (981 candidatas de 8 marketplaces), no en ensayos experimentales.»
- **Restated**: El diseño es independiente, sin pruebas pareadas, y el tamaño se mide en 981 candidatas de 8 marketplaces.
- **Internal/External evidence**: §71.3 (L1528), §71.2 (L1522).
- **Notes**: el par inglés (L1530) declara que falta una línea base SOTA operacionalizada.

### C086 — Amenazas a la validez declaradas
- **Section**, **Lines**: §71.4 Amenazas a la validez / Threats to validity (L1532–1539), 1534–1537
- **Types**: contextual, methodological
- **Excerpt**: «- **Externa:** solo La Habana y anuncios en línea; los precios son pedidos, no transaccionados. - **De constructo:** kilometraje y potencia faltan en la mayoría de los anuncios; la condición se infiere del texto. - **Interna:** no hay asignación aleatoria; la ablación es observacional.…»
- **Restated**: El documento declara amenazas externa, de constructo, interna y estadística, incluida la no significancia de los coeficientes del modelo completo.
- **Internal/External evidence**: §71.4 (L1534–1537), §59 (L1401), §71.2 (L1522), §22 (L914).
- **Notes**: sección incorporada en la iteración 3 y conservada en esta pasada.

### C087 — Comando único, puntos de entrada y prueba de humo
- **Section**, **Lines**: §71.5 (L1543)
- **Types**: methodological
- **Excerpt**: «Comando único: `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py`. Puntos de entrada con argumentos: `generar_dashboard.py --solo-si-cambia`, `exportar_parquet_compacto.py --tablas ...`, `db_chunks.py split|verify|assemble` y `generar_sitio_mkdocs.py`. Las…»
- **Restated**: La sección declara un comando único, cuatro puntos de entrada con argumentos, dependencias fijadas a serie menor y una prueba de humo.
- **Internal/External evidence**: §71.5 (L1543), §55 (L1361: `requirements.txt` y `.venv-py`).
- **Notes**: la disponibilidad pública se declara en la misma línea con la URL del repositorio y la ausencia de licencia (C008).

## Contextual claims (38)

### C088 — Nombres anteriores conservados por trazabilidad
- **Section**, **Lines**: §1 Objetivo (L27), 27
- **Types**: contextual
- **Excerpt**: «Se conservan los nombres anteriores, *AutoDecide Habana* e *ICD Automotive Market Project*, para mantener la trazabilidad de la documentación ya producida.»

### C089 — Nota de actualización sobre fases y resultados vigentes
- **Section**, **Lines**: §2 Estado y fases (L47), 47
- **Types**: contextual
- **Excerpt**: «**Nota de actualización (27/11/2026):** esta tabla registra el estado al 17/11/2026. El pipeline de análisis (fase 8) se creó después, el 18/11/2026 (§34), y sus resultados vigentes se documentan en §59–§60.»

### C090 — Decisiones de diseño de carpetas y clones
- **Section**, **Lines**: §3 Organización de carpetas (L63), 63
- **Types**: contextual, methodological
- **Excerpt**: «Decisiones de diseño: todo el material auxiliar vive dentro de `Auxiliares/`; los clones se hicieron con `--depth 1` y se registraron en `~/Utilidades/HerramientasScraping/_clone_log.tsv`; la descubrimiento se separó de la verificación; `Copias/` no se registra en este informe por decisión…»
### C091 — Índice de gacetas como referencia
- **Section**, **Lines**: §10 Marco legal (L129), 129
- **Types**: contextual
- **Excerpt**: «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe, solo se citan las normas anteriores.»

### C092 — Problemas y soluciones de la captura
- **Section**, **Lines**: §11 Problemas y soluciones (L135–140), 135–140
- **Types**: contextual, methodological
- **Excerpt**: «| CAPTCHA en paginación DDG | Yahoo + visitas directas; después sesión con `vqd`. | ... | Repetidos y mirrors | Deduplicación por título normalizado, prefijo y dominio. |»

### C093 — Registro automático de altas y exclusión de `Copias/`
- **Section**, **Lines**: §13 Registro de altas / Change log (L294–298), 296
- **Types**: contextual
- **Excerpt**: «Registro automático de todo lo que se añade a la carpeta del proyecto. El script `Auxiliares/herramientas/actualizar_informe.py` añade filas debajo del marcador y regenera el PDF. `Copias/` queda excluido por decisión explícita.»

### C094 — Entradas omitidas en el registro de altas
- **Section**, **Lines**: §13 (L315), 315
- **Types**: contextual
- **Excerpt**: «| 2026-11-17 | … | aviso / notice | — | — | — | 175 entradas adicionales no listadas / omitted | Pendiente / Pending |»

### C095 — Última ejecución registrada de sincronización
- **Section**, **Lines**: §14 (L783), 783
- **Types**: contextual
- **Excerpt**: «| 2026-11-17T15:47:42+00:00 | 795373568 B | 48 partes de 16 MiB | `dadd2bffba615d8a…` | Reconstruir con `reconstruir_revolico.py` / Rebuild with `reconstruir_revolico.py` |»

### C096 — Detención manual del temporizador de Revolico
- **Section**, **Lines**: §15 (L791), 791
- **Types**: contextual
- **Excerpt**: «**Nota / Note (17/11/2026):** se detuvo manualmente `revolico-scrape.timer` y su servicio a petición del usuario. El scraper había ampliado la BD de 3.682 a **6.332 anuncios** (520,6 MB) antes de detenerse; no se generaron partes (`estado.json` ausente) porque se detuvo antes de la fase de división.»

### C097 — Adaptación del patrón de diferencias de `spinny-scraper`
- **Section**, **Lines**: §16 (L805), 805
- **Types**: contextual, methodological
- **Excerpt**: «Se adaptó el patrón `output_writer.py` + `diff_runs.py` de `spinny-scraper` como snapshot `Data/Revolico/snapshots/ultimo.json` (`{id: firma}`).»

### C098 — Fuentes académicas y repositorios revisados para fases 7–8
- **Section**, **Lines**: §17 (L813), 813
- **Types**: contextual
- **Excerpt**: «Fuentes académicas y repositorios revisados para definir los requerimientos del análisis (Fases 7-8):»

### C099 — Verificación en vivo y accesibilidad de fuentes oficiales
- **Section**, **Lines**: §18 (L838–840), 838–840
- **Types**: contextual, citation-grounded
- **Excerpt**: «VAHAN (India), declarado por `vahan-india-automotive-market-2025` | **Oficial gubernamental** (MoRTH) | No accesible desde este entorno (error de transporte); el repo documenta 12 exportaciones mensuales 2025 y manifiesto de verificacion | Registros por fabricante/combustible»

### C100 — Marco general de ocho pasos derivado de trabajos revisados
- **Section**, **Lines**: §19 Marco general (L857–866), 857
- **Types**: contextual
- **Excerpt**: «### Marco general (8 pasos, derivado de los trabajos revisados)»

### C101 — Límites declarados de la adaptación
- **Section**, **Lines**: §19 (L875), 875
- **Types**: contextual
- **Excerpt**: «- **Límites**: precios pedidos no transaccionados, sesgo de supervivencia de anuncios, sin datos personales, vigencia normativa a verificar.»

### C102 — Cambio de objetivo a petición del usuario
- **Section**, **Lines**: §21 (L901), 901
- **Types**: contextual
- **Excerpt**: «A petición del usuario, el objetivo inmediato deja de ser la recomendación interactiva de compra y pasa a ser **un análisis de mercado**.»

### C103 — Generación de gráficas del análisis descriptivo
- **Section**, **Lines**: §23 (L925), 925
- **Types**: contextual
- **Excerpt**: «**Gráficas**: `Auxiliares/herramientas/graficos_mercado.py` usa matplotlib, seaborn y plotly (instalados) y genera 8 PNG + `dashboard_interactivo.html` en `Data/analisis/graficos/`.»

### C104 — Librerías de mapas instaladas
- **Section**, **Lines**: §25 (L939), 939
- **Types**: contextual
- **Excerpt**: «**Librerías de mapas instaladas:** `geopandas 1.2.0`, `shapely 2.2.0`, `pyproj`, `folium 1.0.0`, `mapclassify`, `geopy` (además de matplotlib/seaborn/plotly ya instaladas).»

### C105 — Búsqueda de canales adicionales de Telegram
- **Section**, **Lines**: §28 (L974), 974
- **Types**: contextual
- **Excerpt**: «**Búsqueda de más canales:** se probaron `Revolico_Cuba_Oficial`, `Ventas_Revolico_Holguin_Cuba`, `revolico_baracoa`, `timbirichi_compra_y_venta_cuba`, `PiezasdeCarrosCU`, `directoriocubano`, `eltoquecom`, `coventcuba`, `APublished`, `GEEKSCUBANS_PLUS` y `lachopivaraderooo`. Ninguno publicó…»
### C106 — Advertencia sobre la cuota de Git LFS
- **Section**, **Lines**: §30 (L1001), 1001
- **Types**: contextual
- **Excerpt**: «**Advertencia:** la cuota LFS del plan gratuito es limitada; una BD que cambia cada 10 minutos genera un blob nuevo por commit. Vigilar el consumo con `git lfs ls-files` y `git lfs env`.»

### C107 — Modo de descubrimiento sin procesamiento
- **Section**, **Lines**: §32 (L1015–1020), 1015–1020
- **Types**: contextual, methodological
- **Excerpt**: «Se añadió `--solo-descubrimiento` a `scrape_revolico_pipeline.py`. En ese modo: - se recorren las páginas de búsqueda desde la 1 hacia atrás; - se guardan todos los enlaces en `url_queue` con estado `descubierto`; - **no hay descarga de anuncios, ni clasificación definitiva, ni inserción en…»
### C108 — Parada por página sin enlaces nuevos
- **Section**, **Lines**: §33 (L1028), 1028
- **Types**: contextual, methodological
- **Excerpt**: «Se modificó `descubrir_hasta_fecha()` para que se detenga en cuanto una página no aporte **ningún enlace nuevo** (todos sus anuncios ya fueron vistos), además de las condiciones de fecha mínima, fin de páginas y límite de seguridad.»

### C109 — DuckDB desinstalado por fallo de CPU
- **Section**, **Lines**: §34 (L1059), 1059
- **Types**: contextual
- **Excerpt**: «`duckdb` se desinstaló porque produce `Illegal instruction` en esta CPU; se usa Parquet + Pandas en su lugar.»

### C110 — Descarga y descompilación de tres APKs de Apklis
- **Section**, **Lines**: §35 (L1088), 1088
- **Types**: contextual
- **Excerpt**: «Descargué tres APKs desde la API de Apklis (`api.apklis.cu/v2/application/` + `POST /v2/release/get_url/`): **Circuitos Habana** (`com.ermetic.circuitoshabana`, v2.2), **Apagones Habana** y **Donde Hay Luz Habana**. Con **jadx 1.5.6** descompilé la primera y encontré el mecanismo que buscábamos:»

### C111 — Restricciones de Docker y Overpass
- **Section**, **Lines**: §36 (L1104–1105), 1104–1105
- **Types**: contextual
- **Excerpt**: «Se intentó usar `google-maps-scraper` en Docker, pero **el daemon Docker no arranca sin root** en este entorno (`dockerd needs to be started with root privileges`), por lo que se descartó esa vía. - Overpass/OSM fue consultado dos veces; no devuelve `shop=car`, `shop=car_repair` ni…»
### C112 — Servicios de usuario con reinicio automático
- **Section**, **Lines**: §37 (L1124), 1124
- **Types**: contextual
- **Excerpt**: «Los servicios de usuario (`revolico-revisar`, `marketplaces-scrape`, `revolico-snapshot`) se reinician automáticamente tras fallo, de modo que los reinicios del servidor ya no detienen el trabajo.»

### C113 — Temporizador persistente de progreso
- **Section**, **Lines**: §38 Reporte automático de progreso (L1130–1141), 1139
- **Types**: contextual, methodological
- **Excerpt**: «El timer es persistente (`Persistent=true`) y arranca 1 minuto después del boot. De este modo el seguimiento sobrevive a los reinicios del servidor.»

### C114 — Renombre del repositorio en GitHub
- **Section**, **Lines**: §40 Renombre del repositorio en GitHub (L1156–1167), 1161–1165
- **Types**: contextual
- **Excerpt**: «antes: CarlosAntonioAceaJimenezCD/autodecide-habana / ahora: CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba» / «GitHub no permite espacios en los nombres de repositorio, por lo que se usó el slug `el-precio-de-moverse-en-cuba`.»

### C115 — Fuentes de estaciones de carga y respuesta 403
- **Section**, **Lines**: §41 (L1175), 1175
- **Types**: contextual
- **Excerpt**: «**Kargalaya** aportó 9 estaciones de carga con coordenadas y precio por hora (Super48, Battery Lab, SOLGUARA, Parqueo M y 25, Universidad de Ciencias Médicas, Trisolinera Habana, PDL Campeño, ADT64, Automovion SRL). **Electromaps** añadió 3 referencias sin coordenadas. ChargeFinder…»
### C116 — Colores y símbolos asignados en el mapa
- **Section**, **Lines**: §42 (L1188–1195), 1190–1195
- **Types**: definitional
- **Excerpt**: «| Gasolinera | negro | círculo | ... | Estación de carga | verde | diamante | ... | Concesionario | azul | cuadrado | ... | Taller | rojo | triángulo |»

### C117 — Uso de patchright y FlareSolverr tras un 403
- **Section**, **Lines**: §42 (L1199), 1199
- **Types**: contextual
- **Excerpt**: «**Cybo devolvió 403 con curl_cffi**, por lo que se aplicó el stack anti-bot disponible: `patchright` (Chromium con fingerprint de Chrome) y FlareSolverr en `http://127.0.0.1:8191/v1`. Las direcciones se geocodificaron con Nominatim y Photon (`geocode_elementos.py`); las tres referencias de…»
### C118 — Apertura del storytelling en dos capas de mercado
- **Section**, **Lines**: §46 Apertura de la sección 3 del storytelling (L1240–1244), 1242
- **Types**: contextual
- **Excerpt**: «Se añadió una apertura que hace explícita la división del mercado en dos capas —marketplaces y concesionarios/tiendas oficiales— y una nota que define el propósito de la sección: mostrar la forma real del mercado después de separar el ruido, sin explicar el proceso de adquisición de datos.»

### C119 — Curva de valor como narrativa de envejecimiento desigual
- **Section**, **Lines**: §47 Reescritura de la sección 4 del storytelling (L1248–1252), 1250
- **Types**: contextual
- **Excerpt**: «Se transformó **La curva de valor** en una narrativa sobre el envejecimiento desigual del parque: premium frente a autos de uso medio, combinación de antigüedad con kilometraje, estado y marca, y la idea de la marca como “seguro de valor”. Se eliminaron los porcentajes repetidos de la…»
### C120 — Exclusión de falsos positivos en la búsqueda de repositorios
- **Section**, **Lines**: §49 (L1275), 1275
- **Types**: contextual
- **Excerpt**: «Se excluyeron falsos positivos de la búsqueda amplia (GTA, proyectos genéricos “Taller 1”, repos sin relación con Cuba o automoción). El repositorio `kremondherranz-lgtm/Mercado-automotriz` ya había sido clonado en `Auxiliares/Repositorios Referencias`.»

### C121 — Grupos de duplicados detectados al consolidar repositorios
- **Section**, **Lines**: §50 (L1285), 1285
- **Types**: result
- **Excerpt**: «Se compararon 233 archivos de datos por hash y 76 CSV por contenido ordenado. Se detectaron 12 grupos de duplicados bytes y 11 de duplicados por contenido: anuncios repetidos dentro de `Mercado-automotriz`, `anuncios_limpios` = `mercado_havana`, `DATASET_COMPLETO_MEJORADO` =…»
### C122 — Convención de la tabla de obras del mapa literario
- **Section**, **Lines**: §71.14 (L1559–1560, L1600), 1559–1560, 1600
- **Types**: contextual, citation-grounded
- **Excerpt**: «| Ref. | Clúster | Autor (año) | Obra | ... / Los trabajos [1], [9], [14], [26] y [29] se discuten además en §71.6; el resto se registra aquí con su marcador numérico y se enlaza a `Data/referencias.md`.»

### C123 — Convención de referencias numeradas y su estado de verificación
- **Section**, **Lines**: §70 (L1497, L1499), 1497, 1499
- **Types**: contextual, citation-grounded
- **Excerpt**: «La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`; la correspondencia entre afirmación y fuente se documenta en el expediente forense.»

### C124 — Registro de la tercera pasada y sus 13 artefactos
- **Section**, **Lines**: §69 (L1489), 1489
- **Types**: contextual
- **Excerpt**: «El registro de la tercera pasada está en `reviews/informe-tecnico-2026-11-27-iter3.{md,forensic.md}` y sus 13 artefactos.»

### C125 — Firma y última actualización del informe
- **Section**, **Lines**: cierre del documento (L1604–1605), 1604–1605
- **Types**: contextual
- **Excerpt**: «**Firma / Signature:** responsable del proyecto / project owner. / **Última actualización / Last update:** 27/11/2026.»


## Apéndice C — Literatura

# Literature Map — iteración 4 (re-verificación dirigida de marcadores y flags)

Nota de entrada. El plan aprobado (`reviews/informe-tecnico-2026-11-28-iter4.plan.md`, 22 líneas) declara `level: master` y `preset: Standard`, pero no contiene `queries_planned` ni `hypotheses_planned`. El mandato recibido para este extractor es estrecho: verificar `Data/referencias.md` (41 entradas), los marcadores `[N]` en §71.6, §71.14, §17 y §34, la coherencia de los flags campo por campo y la representación de las fuentes institucionales [39]–[41]. En consecuencia: (a) no se ejecutaron búsquedas web nuevas ni re-lecturas de resúmenes —los metadatos se reutilizan del mapa E2 de la pasada 1 y de la verificación OpenAlex/Crossref del 27/11/2026 consignada en `Data/referencias.md`—; (b) las capas L1/L2 indicadas son heredadas, no nuevas; (c) los IDs `P001`–`P009` son propios de este artefacto y se mapean a las entradas numeradas; (d) los números de línea corresponden a la copia en caché `.playground/audit-cache/informe-tecnico-2026-11-28-iter4/informe-tecnico-2026-11-28-iter4.text.md`, idéntica en contenido al informe auditado; (e) `Cited in document` significa mención en el cuerpo, y se reporta por separado la presencia de marcador numérico `[N]`.

## Clusters

### Cluster 1 — Posicionamiento frente a trabajos cercanos (§71.6) y sus flags

**Query**: `§71.6` ∩ `Data/referencias.md` — búsqueda por apellido y año (Du 2026; Gegić 2019; Muça 2026; Vidal Alejandro 2024) y contraste campo por campo con el flag «Citada en el informe» de [9], [14], [26] y [29].

Las cuatro comparaciones siguen en un único párrafo (línea 1549) y ahora **sí llevan marcador numérico**: `[14]`, `[26]`, `[9]` y `[29]`. Es el cambio sustantivo frente a la iteración 3, donde el mismo párrafo no tenía marcadores. Los cuatro flags conservan sin embargo la calificación «sin marcador numérico» que se les asignó en la iteración 4 anterior.

#### P001 — Nonlinear Depreciation and Brand Heterogeneity in Chinese Used-Car Listing Prices

- **Authors**: Du, Z.; Yang, Z.; Zhang, Y.; Li, S.; Liu, Y.
- **Year**: 2026
- **Venue**: Advances in Economics, Management and Political Sciences
- **Citations**: no re-contadas en esta iteración; DOI 10.54254/2754-1169/2026.38524 verificado el 27/11/2026 según `Data/referencias.md` [9].
- **URL**: https://doi.org/10.54254/2754-1169/2026.38524
- **Layer**: L2 (heredada del mapa E2 de la pasada 1; sin nueva lectura de resumen)
- **Cited in document**: yes — línea 1549: «Du y otros [9] modelan depreciación no lineal y heterogeneidad de marca con evaluación fuera de muestra».
- **Document reference**: [9] (marcador presente en §71.6).
- **source_of_metadata**: mapa E2 pasada 1 (OpenAlex, fetched 2026-11-27) + `Data/referencias.md` [9].
- **Flag verificado**: `Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)` en la línea 24 → **el calificador ya no corresponde**: el marcador `[9]` está presente. La forma correcta sería `sí (§71.6, con marcador numérico)`.

#### P002 — Car Price Prediction using Machine Learning Techniques

- **Authors**: Gegić, E.; Isaković, B.; Keco, D.; Mašetić, Z.; Kevrić, J.
- **Year**: 2019
- **Venue**: TEM Journal
- **Citations**: no re-contadas en esta iteración; DOI 10.18421/tem81-16 verificado el 27/11/2026 según `Data/referencias.md` [14].
- **URL**: https://doi.org/10.18421/tem81-16
- **Layer**: L2 (heredada; sin nueva lectura de resumen)
- **Cited in document**: yes — línea 1549 (`Gegić y otros [14]`) y línea 1080 (`antecedentes [14], [18]`).
- **Document reference**: [14] (dos marcadores en el cuerpo: §71.6 y §34).
- **source_of_metadata**: mapa E2 pasada 1 (OpenAlex) + `Data/referencias.md` [14].
- **Flag verificado**: `Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)` en la línea 34 → **el calificador ya no corresponde** y además omite §34.

#### P003 — A Pipeline for Integrating and Analyzing Public Business Data in Albania Using Web Scraping and Machine Learning

- **Authors**: Muça, M.; Bani, K.; Alla, A.
- **Year**: 2026
- **Venue**: International Journal of Advanced Computer Science and Applications
- **Citations**: no re-contadas en esta iteración; DOI 10.14569/ijacsa.2026.0170845 verificado el 27/11/2026 según `Data/referencias.md` [26].
- **URL**: https://doi.org/10.14569/ijacsa.2026.0170845
- **Layer**: L2 (heredada; sin nueva lectura de resumen)
- **Cited in document**: yes — línea 1549: «Muça, Bani y Alla [26] integran datos públicos albaneses por scraping».
- **Document reference**: [26] (marcador presente en §71.6).
- **source_of_metadata**: mapa E2 pasada 1 (OpenAlex) + `Data/referencias.md` [26].
- **Flag verificado**: `Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)` en la línea 58 → **el calificador ya no corresponde**.

#### P004 — Using AI in the informal currency market: evidence from Cuba

- **Authors**: Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A.
- **Year**: 2024
- **Venue**: Applied Economics
- **Citations**: no re-contadas en esta iteración; DOI 10.1080/00036846.2024.2416091 verificado el 27/11/2026 según `Data/referencias.md` [29].
- **URL**: https://doi.org/10.1080/00036846.2024.2416091
- **Layer**: L2 (heredada; sin nueva lectura de resumen)
- **Cited in document**: yes — línea 1549: «Vidal Alejandro y otros [29] estudian el mercado informal de divisas en Cuba».
- **Document reference**: [29] (marcador presente en §71.6).
- **source_of_metadata**: mapa E2 pasada 1 (OpenAlex) + `Data/referencias.md` [29].
- **Flag verificado**: `Citada en el informe: sí (mención nominal en §71.6, sin marcador numérico)` en la línea 64 → **el calificador ya no corresponde**.

### Cluster 2 — Citas numeradas en §19, §17 y §34

**Query**: `§17` ∪ `§19` ∪ `§34` ∩ `Data/referencias.md` — inventario de marcadores `[N]` presentes fuera de §71.6 y contraste con los flags de [1] y [18].

Resultado del inventario: §17 (líneas 811–832) contiene **0 marcadores**; §19 (línea 861) contiene `[1]`; §34 (línea 1080) contiene `[14]` e `[18]`; §71.14 (líneas 1561–1598) contiene 38 marcadores de tabla `[1]`–`[38]` y la línea 1600 repite `[1]`, `[9]`, `[14]`, `[26]` y `[29]`. En prosa de cuerpo, las obras con marcador son seis: [1], [9], [14], [18], [26] y [29].

#### P005 — The Market for "Lemons": Quality Uncertainty and the Market Mechanism

- **Authors**: Akerlof, G. A.
- **Year**: 1970
- **Venue**: The Quarterly Journal of Economics
- **Citations**: no re-contadas; DOI 10.2307/1879431 confirmado en OpenAlex el 27/11/2026 según `Data/referencias.md` [1].
- **URL**: https://doi.org/10.2307/1879431
- **Layer**: L2 (heredada; sin nueva lectura de resumen)
- **Cited in document**: yes — línea 861 (`asimetría de información (Akerlof [1])`), línea 817 (mención nominal sin marcador en §17) y línea 1561 (tabla de §71.14).
- **Document reference**: [1].
- **source_of_metadata**: mapa E2 pasada 1 (OpenAlex) + `Data/referencias.md` [1].
- **Abstract analysis** (L2 heredada): el resumen indexado es un índice de secciones, no un resumen sustantivo; por eso la entrada lleva `(metadata incomplete: resumen indexado no sustantivo; identidad y DOI verificados en OpenAlex)`, coherente con la glosa `(metadata incomplete: resumen)` / `(metadata incomplete: abstract)` de §70 (líneas 1497 y 1499).
- **Flag verificado**: `Citada en el informe: sí` → correcto, aunque no registra las tres ubicaciones. Incidencia aparte: la línea 1600 afirma que [1] «se discute además en §71.6», pero el párrafo de §71.6 (línea 1549) no incluye a Akerlof; su discusión está en §17 y §19.

#### P006 — ProbSAINT: Probabilistic Tabular Regression for Used Car Pricing

- **Authors**: Madhusudhanan, K.; Behrens, G.; Stubbemann, M.; Schmidt-Thieme, L.
- **Year**: 2024
- **Venue**: arXiv:2403.03812 / IEEE BigData 2024, Industry & Government Track
- **Citations**: 13 verificadas en OpenAlex el 27/11/2026 según `Data/referencias.md` [18]; no re-contadas.
- **URL**: https://arxiv.org/abs/2403.03812
- **Layer**: L2 (heredada; sin nueva lectura de resumen)
- **Cited in document**: yes — línea 1080: «La predicción de precios sobre catálogos estructurados tiene antecedentes [14], [18]».
- **Document reference**: [18] (marcador presente en §34).
- **source_of_metadata**: mapa E2 pasada 1 (OpenAlex) + `Data/referencias.md` [18].
- **Flag verificado**: `Citada en el informe: no` en la línea 42 → **desactualizado**: [18] tiene marcador numérico en §34. Debe pasar a `sí (§34, con marcador numérico)`. Esta es la única entrada del bloque [1]–[38] cuyo flag `no` contradice directamente un marcador en prosa.

### Cluster 3 — Fuentes institucionales [39]–[41] (§18 / §70)

**Query**: `§18` ∪ `§70` ∩ `Data/referencias.md` [39]–[41] — contraste de flags, campo «Citada en el informe» y tipo de fuente declarado.

Ninguna de las tres fuentes tiene marcador numérico en el cuerpo y ninguna figura en la tabla de §71.14, que se detiene en [38]. Su presencia se documenta por nombre en §18 y §70.

#### P007 — Vehicle statistics (Department for Transport / DVLA)

- **Authors**: Department for Transport / DVLA (institucional)
- **Year**: sin campo de año en la entrada
- **Venue**: GOV.UK (sitio institucional)
- **Citations**: no aplica; sin re-verificación en vivo en esta iteración.
- **URL**: https://www.gov.uk/government/organisations/department-for-transport
- **Layer**: L1 (metadatos institucionales heredados; sin fetch nuevo)
- **Cited in document**: yes — línea 838 (§18, con URL profunda `gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files`) y línea 1497 (§70).
- **Document reference**: [39] (sin marcador numérico en el cuerpo).
- **source_of_metadata**: `Data/referencias.md` [39] + informe §18 y §70.
- **Flag verificado**: dos incidencias. (i) Es la **única de las 41 entradas sin campo `Citada en el informe`**; por el contenido del cuerpo debería ser `sí (fuente institucional en §18 y §70)`. (ii) Lleva `(metadata incomplete: URL profunda no confirmada)` mientras §18 declara «Verificado en vivo: publicado por Department for Transport + DVLA, actualizado 23/09/2026, Open Government Licence» con esa URL profunda y §70 la enumera entre las «Referencias citadas y verificadas externamente durante la auditoría». No se re-fetchó la URL en esta pasada, así que solo se constata la contradicción interna, no la validez del enlace.

#### P008 — Informes del sector automotriz español (ANFAC)

- **Authors**: ANFAC (asociación gremial)
- **Year**: sin campo de año en la entrada
- **Venue**: anfac.com (sitio institucional)
- **Citations**: no aplica; sin re-verificación en vivo en esta iteración.
- **URL**: https://anfac.com/
- **Layer**: L1 (metadatos institucionales heredados; sin fetch nuevo)
- **Cited in document**: yes — línea 821 (§17, mención nominal agrupada con EY/INEGI/BBVA/COIIM), línea 842 (§18, «Verificado en vivo») y línea 1497 (§70, «sitio oficial»).
- **Document reference**: [40] (sin marcador numérico en el cuerpo).
- **source_of_metadata**: `Data/referencias.md` [40] + informe §17, §18 y §70.
- **Flag verificado**: `Citada en el informe: sí (fuente institucional en §70)` y sin `(metadata incomplete)` → coherente con §18 y §70. La glosa omite §17 y §18, pero no contradice ningún campo. La ausencia de marcador `[40]` es consecuencia de que §17 no usa marcadores y de que §71.14 no incluye a [39]–[41].

#### P009 — Estadísticas de matriculaciones (AEADE)

- **Authors**: AEADE (gremial, Ecuador)
- **Year**: sin campo de año en la entrada
- **Venue**: aeade.net (sitio institucional)
- **Citations**: no aplica; sin re-verificación en vivo en esta iteración.
- **URL**: https://www.aeade.net/
- **Layer**: L1 (metadatos institucionales heredados; sin fetch nuevo)
- **Cited in document**: yes — línea 843 (§18, «Verificado en vivo: aeade.net, anuarios y boletines de ventas; fuente declarada por el estudio PUCE») y línea 1497 (§70, «sitio oficial»).
- **Document reference**: [41] (sin marcador numérico en el cuerpo; no aparece en §17).
- **source_of_metadata**: `Data/referencias.md` [41] + informe §18 y §70.
- **Flag verificado**: `Citada en el informe: sí (fuente institucional en §70)` y sin `(metadata incomplete)` → coherente. Como en [40], la glosa no menciona §18, donde está la verificación en vivo.

## Recency distribution

Convenio: «In document bibliography» cuenta las 41 entradas de `Data/referencias.md`; 38 tienen año y las tres institucionales ([39]–[41]) no lo tienen. «In map» cuenta las nueve entradas re-visadas en este artefacto.

| Year | In map | In document bibliography |
|---|---:|---:|
| 2026 | 2 | 6 |
| 2025 | 0 | 1 |
| 2024 | 2 | 6 |
| 2023 | 0 | 4 |
| 2022 | 0 | 1 |
| ≤2021 | 2 | 20 |
| Sin año (institucionales [39]–[41]) | 3 | 3 |

Las nueve entradas re-visadas son [1], [9], [14], [18], [26], [29], [39], [40] y [41]. El conteo de años coincide con el consignado en la iteración 3 para el bloque [1]–[38].

## Venue distribution

| Venue | Count in map |
|---|---:|
| The Quarterly Journal of Economics | 1 |
| Advances in Economics, Management and Political Sciences | 1 |
| TEM Journal | 1 |
| arXiv / IEEE BigData 2024 | 1 |
| International Journal of Advanced Computer Science and Applications | 1 |
| Applied Economics | 1 |
| Sitio institucional (GOV.UK / ANFAC / AEADE) | 3 |

## Auditoría de flags por campo

| Entrada | Campo | Estado en `Data/referencias.md` | Evidencia en el informe | Observación |
|---|---|---|---|---|
| [1] | `Citada` / `metadata incomplete` | `sí` / resumen indexado no sustantivo | §17 (nominal), §19 (`[1]`), §71.14 | Coherente; la línea 1600 de §71.14 lo atribuye erróneamente a §71.6 |
| [9] | `Citada` | `sí (…sin marcador numérico)` | §71.6 `[9]` | Calificador desactualizado |
| [14] | `Citada` | `sí (…sin marcador numérico)` | §71.6 `[14]`, §34 `[14]` | Calificador desactualizado y ubicación incompleta |
| [18] | `Citada` | `no` | §34 `[18]` | Flag desactualizado |
| [26] | `Citada` | `sí (…sin marcador numérico)` | §71.6 `[26]` | Calificador desactualizado |
| [29] | `Citada` | `sí (…sin marcador numérico)` | §71.6 `[29]` | Calificador desactualizado |
| [39] | `Citada` / `metadata incomplete` | campo ausente / URL profunda no confirmada | §18 (URL profunda «verificada en vivo»), §70 («verificada externamente») | Flag y campo en contradicción con el cuerpo |
| [40] | `Citada` | `sí (fuente institucional en §70)` | §17, §18, §70 | Coherente; ubicación incompleta |
| [41] | `Citada` | `sí (fuente institucional en §70)` | §18, §70 | Coherente; ubicación incompleta |

Dos observaciones agregadas sobre el campo `Citada`:

1. El archivo define ese campo como «indicación de mención nominal en el informe» (línea 6) y 33 de las 41 entradas lo tienen en `no`. Sin embargo, §71.14 se titula «Obras del mapa literario citadas en el cuerpo» (línea 1557) y su cierre dice que «el resto se registra aquí con su marcador numérico» (línea 1600), mientras 33 de las 38 filas de esa tabla llevan `no` en `Data/referencias.md`. El título/cierre de la sección y el campo de flag describen estados distintos; no se ha re-escrito ninguno de los dos en esta pasada.
2. §70 afirma que «las fuentes restantes figuran con estado `(metadata incomplete)` en `reviews/informe-tecnico-2026-11-27.e2-literature.md`» (líneas 1497 y 1499). En `Data/referencias.md` solo cuatro entradas llevan efectivamente esa marca —[1], [10], [12] y [39]— y el archivo enlazado es el mapa de la primera pasada, no el de esta iteración. La frase de §70 generaliza un estado que el anexo no sostiene campo por campo; las notas de discrepancia de año de [2], [19] y [38] son otro campo distinto del flag `(metadata incomplete)`.

## Likely missing important works

Sin búsquedas nuevas en esta iteración, se mantienen las siete obras arrastradas de la iteración 3 (presentes en `Data/referencias.md` con `Citada: no`, ausentes como discusión en el cuerpo): Lewis (2011) [2], Englmaier et al. (2017) [4], Krotov et al. (2020) [21], Priestley et al. (2023) [23], Brown et al. (2025) [22], Guerra (2015) [33] y Hohensinner et al. (2026) [24]. Gegić et al. (2019) [14] sigue fuera de la lista porque sí tiene discusión comparativa en §71.6 y marcadores en §71.6 y §34. No se proponen obras adicionales.

## Hypothesis checks (from plan)

El plan no declara hipótesis; las cuatro siguientes se derivan del mandato recibido y son observaciones sin veredicto.

### H1 — `Data/referencias.md` contiene 41 entradas numeradas de forma continua, en coherencia con el plan (derivada)

Estado de la evidencia: **sí para el archivo y el plan**. La comprobación directa da 41 líneas `^[n]`, de [1] a [41] sin huecos, y el plan (línea 19) declara «41 referencias». La incoherencia está aguas abajo: §70 (líneas 1497 y 1499) dice «La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`», cifra que coincide con las 38 filas de la tabla de §71.14 pero no con el anexo al que apunta. Las tres entradas sobrantes son precisamente las institucionales [39]–[41], que no están en esa tabla. El encabezado del anexo (línea 3) indica además que fue generado el 27/11/2026 desde `reviews/informe-tecnico-2026-11-27.e2-literature.md`, es decir, desde el mapa de la primera pasada.

### H2 — Los marcadores `[N]` del cuerpo coinciden con los flags «Citada en el informe» (derivada)

Estado de la evidencia: **coinciden en seis entradas, con cinco desajustes de campo**. Coinciden [1] (`sí`, con `[1]` en §19), [9], [14], [26] y [29] (`sí`, con marcadores en §71.6) y [40]/[41] (`sí` institucionales, sin marcador pero con mención nominal). Los desajustes son: los calificadores «sin marcador numérico» de [9], [14], [26] y [29], que dejaron de ser ciertos en esta iteración; y el flag `no` de [18], que tiene `[18]` en §34. Ningún otro marcador aparece en prosa de cuerpo: §17 tiene 0 marcadores y las demás entradas solo comparecen en la tabla de §71.14.

### H3 — Los flags por campo están completos y actualizados en las 41 entradas (derivada)

Estado de la evidencia: **no del todo**. Hay un campo ausente ([39] no registra `Citada en el informe`), cinco campos desactualizados ([9], [14], [18], [26] y [29] en el sentido de H2), una ubicación incompleta en [1], una contradicción de estado entre el flag de [39] y §18/§70, y una generalización en §70 que no se sostiene campo por campo (solo [1], [10], [12] y [39] llevan `(metadata incomplete)`). Los metadatos bibliográficos propiamente dichos —autores, año, revista, DOI y conteos de citas— no fueron re-verificados en esta iteración y no se ha constatado cambio alguno en ellos.

### H4 — Las fuentes institucionales [39]–[41] están representadas de forma coherente entre §18, §70, §71.14 y el anexo (derivada)

Estado de la evidencia: **[40] y [41] coherentes; [39] parcial**. ANFAC y AEADE aparecen con el mismo tipo de fuente, el mismo estado sin flag y la misma denominación «fuente institucional en §70» en el anexo, y con verificación en vivo declarada en §18; sus glosas omiten otras ubicaciones pero no contradicen ningún campo. DfT/DVLA es la excepción: §18 declara verificación en vivo de la URL profunda y §70 la incluye entre las referencias verificadas externamente, mientras su entrada [39] lleva `(metadata incomplete: URL profunda no confirmada)` y carece del campo `Citada`. La coherencia estructural de las tres es la misma —sin marcador numérico y fuera de la tabla de 38 filas de §71.14—, pero el documento no declara explícitamente que [39]–[41] sean un bloque aparte. No se re-fetchó ninguna URL en esta pasada.

## Sources used

- WebSearch queries: 0 (re-visación dirigida; sin búsquedas temáticas nuevas).
- WebFetch URLs: 0 en esta iteración; no se re-verificaron en vivo GOV.UK, anfac.com ni aeade.net.
- Semantic Scholar API hits: 0.
- OpenAlex API hits: 0 nuevos; los conteos y verificaciones se reutilizan del mapa E2 de la pasada 1 (fetched 2026-11-27) y de `Data/referencias.md`.
- Archivos locales inspeccionados: `Data/referencias.md` (líneas 3–6, entradas [1]–[41]); copia en caché `.playground/audit-cache/informe-tecnico-2026-11-28-iter4/informe-tecnico-2026-11-28-iter4.text.md` (§17, líneas 811–832; §18, líneas 834–853; §19, línea 861; §34, línea 1080; §70, líneas 1495–1499; §71.6, línea 1549; §71.14, líneas 1557–1600); `reviews/informe-tecnico-2026-11-28-iter4.plan.md` (22 líneas); `reviews/informe-tecnico-2026-11-27-iter3.e2-literature.md` (nota de entrada, H2 y lista de obras ausentes).
- Degradación: `degraded: false` para el mandato recibido —las 41 entradas, los marcadores de las secciones pedidas, los flags por campo y las tres fuentes institucionales quedaron resueltos por inspección directa—. Limitación declarada: sin búsqueda bibliográfica nueva, sin re-lectura de resúmenes y sin re-fetch de URLs; este mapa sirve para coherencia interna de marcadores y flags, no para proponer obras adicionales ni para certificar enlaces.


## Apéndice D — Artefactos

# Artifact Inventory

## Repository

- **URL**: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba
- **Clone status**: success (copia local íntegra; comandos `git` ejecutados sobre `~/Proyectos/El precio de moverse en Cuba`)
- **Languages**: Python ~40.500 LOC (propio, excluyendo `.venv-py`, clones de referencia, `Copias/`, `site/`); Markdown ~35.323 LOC (ídem)
- **Commits**: 194
- **Authors**: CarlosAntonioAceaJimenezCD <CarlosAntonioAceaJimenezCD@users.noreply.github.com>
- **First commit**: 2026-11-17
- **Last commit**: 2026-11-28
- **Default branch**: main

### Structure

```tree
.
├── README.md / INFORME_TECNICO.md / INFORME_TECNICO.pdf
├── requirements.txt / mkdocs.yml / .gitattributes / .gitignore
├── Anexos/            # corpus legal y documentos de apoyo
├── Auxiliares/        # .venv-py, cache, herramientas, Repositorios Referencias
├── Copias/            # 4 repos de referencia (excluidos por decisión explícita)
├── Data/              # analisis_rentabilidad, Revolico, catalogos, fuentes, mapas, auditoria, ...
├── docs/              # fuente MkDocs: historia/, referencia/, guias/, fuentes/, graficos/, dashboard.html
├── Hombros/           # PDFs, HTML, repos y derivadas (01–06)
├── reviews/           # 3 pasadas de auditoría completas + plan iter4
├── site/              # generado, ignorado por Git
└── .playground/audit-cache/  # texto en caché del documento auditado
```

### Entry points

| Path | LOC | Args documented | Notes |
|---|---|---|---|
| `Data/analisis_rentabilidad/scripts/run_all.py` | 60 | no | Comando único; declara `SEED = 20261127` (l. 16), siembra `random`/`numpy` y exporta `ENTORNO["PROYECTO_SEED"] = str(SEED)` (l. 23). |
| `Data/analisis_rentabilidad/scripts/03b_baselines.py` | — | no | Calcula los MAE publicados en `baselines.csv` (§71.1). |
| `Auxiliares/herramientas/generar_dashboard.py` | — | yes | `--solo-si-cambia`. |
| `Auxiliares/herramientas/exportar_parquet_compacto.py` | — | yes | `--tablas ...`. |
| `Auxiliares/herramientas/db_chunks.py` | — | yes | `split|verify|assemble`. |
| `Auxiliares/herramientas/generar_sitio_mkdocs.py` | — | no | Regenera `docs/` desde Markdown y CSV. |
| `Auxiliares/herramientas/scrape_concesionarios.py` | — | no | Adaptadores por dominio + Playwright opcional (§8). |
| `Auxiliares/herramientas/actualizar_informe.py` | — | no | Actualiza el registro de altas y regenera el PDF (§13). |
| `Auxiliares/herramientas/test_smoke_pipeline.py` | 68 | no | Prueba de humo del pipeline central (§71.5). |

### Tests

- Files: `Auxiliares/herramientas/test_dashboard.py`, `Auxiliares/herramientas/test_parquet_compacto.py`, `Auxiliares/herramientas/test_modelo.py`, `Auxiliares/herramientas/test_smoke_pipeline.py`
- Total LOC: 327
- Framework: scripts (pytest-style, sin `pytest.ini`/`conftest.py` detectados)
- Tests cover (named): dashboard, exportación Parquet compacto, modelo hedónico, humo del pipeline

### Documentation

| File | LOC |
|---|---|
| README.md | 105 |
| INFORME_TECNICO.md | 1605 |
| Data/analisis_rentabilidad/README.md | 41 |
| Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md | 92 |
| Data/analisis_rentabilidad/NECESIDADES.md | 45 |
| Data/AUTOMATIZACION.md | 100 |
| docs/ (total) | incluido en los ~35.323 LOC Markdown |
| reviews/ (45 artefactos de auditoría + plan iter4) | 3 pasadas × 15 archivos = 45, más `informe-tecnico-2026-11-28-iter4.plan.md` en curso |

### Environment

- requirements.txt: presente, 12 líneas de dependencias (`pandas~=2.2.0`, `numpy~=1.26.0`, `plotly~=5.18.0`, `statsmodels~=0.14.0`, `scipy~=1.11.0`, `pyarrow~=14.0.0`, `mkdocs~=1.6.0`, `mkdocs-material~=9.5.0`, …)
- pyproject.toml: ausente
- environment.yml: ausente
- Dockerfile: ausente
- Other: `mkdocs.yml` (1700 B), `.gitattributes` (Git LFS), `.gitignore`, `Auxiliares/.venv-py/` (Python 3.14); FlareSolverr 3.5.2 en Docker (declarado en §6, sin Dockerfile versionado)

### Heavy artifacts in repo

| Path | Size | Type |
|---|---|---|
| `Data/Revolico/revolico.sqlite` | 838,0 MB | data/sqlite (LFS) |
| `Data/Revolico/pipeline.sqlite` | 753,4 MB | data/sqlite (LFS) |
| `Data/catalogos_concesionarios/bdc_one.sqlite` | 69,9 MB | data/sqlite |
| `Data/catalogos_concesionarios/changan.sqlite` | 54,8 MB | data/sqlite |
| `Data/catalogos_concesionarios/marketplaces/autocubana.sqlite` | 53,6 MB | data/sqlite |
| `Data/catalogos_concesionarios/marketplaces/itencel.sqlite` | 53,5 MB | data/sqlite |
| `Data/analisis_rentabilidad/data/compacto/anuncios/year=2026/month=11/parte-000.parquet` | 23,0 MB | data/parquet |
| `Data/analisis_rentabilidad/data/listings_raw.parquet` | 2,1 MB | data/parquet |

## Datasets

| Name | Source | ID | Publicly accessible | Notes |
|---|---|---|---|---|
| Revolico | custom (scraping propio) | `Data/Revolico/*.sqlite` + `chunks/MANIFEST.json` | yes (repo público, binarios vía Git LFS) | Base cruda y pipeline; reconstruible desde el manifiesto (§71.5). |
| Catálogos de concesionarios y marketplaces | custom (scraping propio) | `Data/catalogos_concesionarios/` (11 bases + 8 marketplaces) | yes | 256 filas de la primera captura (§9); 8 fuentes declaradas en §71.1. |
| ONEI (anuarios) | fuente oficial cubana | `Data/fuentes-oficiales/`, `Data/fuentes_oficiales/` | yes | Cuadros 3 y 4 del apéndice visual. |
| TRMI elTOQUE | fuente externa (tipo de cambio informal) | `Data/analisis_rentabilidad/config.py` | yes | Serie temporal y conversión fechada (§23). |
| Telegram / WhatsApp / Facebook | custom (integraciones) | `Data/integraciones/` | yes | Contexto y canal de circuitos eléctricos (§62, §66). |

## Tables

El texto en caché no contiene marcadores `Tabla N` / `Figura N`: las tablas del cuerpo son markdown sin numerar y el apéndice visual usa `Cuadro N` / `Gráfico N`. Se inventarían los apoyos referidos por el documento.

### Tabla 1 — «Fase | Nombre | Estado» (§2, p. 7 y §2 EN)
- **Section**: §2 (Estado y fases)
- **Lines**: 33–43 / 175–185
- **Columns**: Fase, Nombre, Estado
- **Rows**: 9
- **Claims supported** (preliminary): estado de fase 6 «en curso» y fase 8 «pendiente» con nota de actualización 27/11/2026

### Tabla 2 — «Tienda | Filas | Con precio» (§9)
- **Section**: §9 (Fase 6 — Scraping y captura)
- **Lines**: 105–117 / 247–259
- **Columns**: Tienda, Filas, Con precio
- **Rows**: 11
- **Claims supported** (preliminary): 256 filas y densidad por tienda

### Tabla 3 — «Base / Baseline | Descripción | Métrica observada» (§71.1)
- **Section**: §71.1 (Bases de comparación)
- **Lines**: 1509–1516
- **Columns**: Base/Baseline, Descripción, Métrica observada
- **Rows**: 4 (3 en la tabla markdown + una fila «Modelo principal propio» añadida después del párrafo EN)
- **Claims supported** (preliminary): MAE 18.188,34 y 16.603,28 USD sobre 1.462 anuncios; R² 0,101 sobre 584 observaciones
- **Respaldo CSV**: `outputs/tables/baselines.csv` (2 filas: `mediana_global`, `mediana_por_marca`); la fila del modelo principal **no está** en el CSV.

### Tabla 4 — «Ref. | Clúster | Autor (año) | Obra» (§71.14)
- **Section**: §71.14 (Obras del mapa literario citadas en el cuerpo)
- **Lines**: 1559–1598
- **Columns**: Ref., Clúster, Autor (año), Obra
- **Rows**: 38
- **Claims supported** (preliminary): correspondencia [1]–[38] con `Data/referencias.md`

### Cuadros 1–5 — apéndice visual (§59)
- **Section**: `docs/historia/apendice.md` (enlazado desde el sitio MkDocs)
- **Lines**: 7–77 del apéndice; títulos: «KPIs del mercado», «Mercado local e importación», «Pasajeros transportados (ONEI, millones)», «Seguridad vial (ONEI)», «Modelo de depreciación (coeficientes vigentes)»
- **Rendered in document**: no en el texto en caché (solo referidos en §59); sí en `docs/`/`site/`
- **Claims supported** (preliminary): cifras de KPIs, series ONEI y coeficientes del modelo

## Figures

### Gráficos 1–6 — apéndice visual (§59, §61)
- **Section**: §59 (Storytelling alineado con los datos finales), §61 (Sitio MkDocs)
- **Caption (verbatim)**: «Gráfico 1. Distribución de precios», «Gráfico 2. Distribución por año», «Gráfico 3. Top marcas», «Gráfico 4. Precio por tier», «Gráfico 5. Precio vs km», «Gráfico 6. Precio vs antigüedad»
- **Rendered in document**: no en el texto en caché (enlaces relativos); sí como HTML interactivo en `docs/graficos/01_precios.html` … `06_edad_precio.html` y copias en `site/graficos/`
- **Type**: gráficos Plotly interactivos
- **Claims supported** (preliminary): distribución de precios, año, marcas, tiers, kilometraje y antigüedad

### Panel interactivo — `Data/dashboard.html`
- **Section**: §61, §71.5
- **Caption (verbatim)**: «El panel interactivo vigente es `Data/dashboard.html`, copiado a `docs/dashboard.html`»
- **Rendered in document**: no (artefacto HTML autocontenido, 109.929 B ≈ 107,4 KB, copiado también en `site/dashboard.html`)
- **Type**: dashboard interactivo autocontenido
- **Claims supported** (preliminary): «panel interactivo autocontenido» del Resumen/Abstract

## Missing artifacts

### CSV de comparaciones — coherencia de la muestra
- **Mentioned in document**: §71.3 (p. «Tests and sample size»): «El tamaño se mide en anuncios (981 candidatas de 8 marketplaces)… (`comparaciones.csv`, 2.000 réplicas)», mientras `contraste,n` en el CSV es `precio por tier de marca,1462`.
- **Found in repo**: yes — `Data/analisis_rentabilidad/outputs/tables/comparaciones.csv` (184 B; 1 fila de datos; columnas `contraste,n,estadistico,p_valor,ic_bajo,ic_alto,metodo`).
- **Observation**: el CSV existe y contiene H = 44,313, p = 0.0, IC 10.000–29.500 USD y el método bootstrap de 2.000 réplicas, en coincidencia con §71.3. El denominador de la fila es 1.462 anuncios, distinto de las «981 candidatas» citadas en el mismo párrafo y en §71.2; el inventario registra la diferencia sin resolverla.

### CSV de ablación — recuentos divergentes
- **Mentioned in document**: §71.2: «la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² baja de 0,274 a 0,101»; §71.1: «R² 0,101 sobre 584 observaciones»; §59: «993 candidatas».
- **Found in repo**: yes — `outputs/tables/modelo_muestra.csv` (266 B; columnas `modelo,candidatas,observaciones,r2,p_f,terminos`).
- **Observation**: el CSV registra `principal,993,586,0.1008,0.0` y `completo,993,28,0.2744,0.4114`. Coinciden 28, 993 y los R² redondeados (0,101 y 0,274); no coinciden 586 vs. 584/572 del texto (§71.2, §71.1 y `docs/historia/apendice.md` l. 77, que dice «22 observaciones … frente a 572»). La fila del modelo principal con `hp` incluido no aparece como tercera fila.

### CSV de baselines — fila no presente
- **Mentioned in document**: §71.1: «Los MAE se calculan en `scripts/03b_baselines.py` y se publican en `outputs/tables/baselines.csv`» y la tabla incluye «Modelo principal propio | OLS de log-precio … | R² 0,101 sobre 584 observaciones».
- **Found in repo**: yes — `outputs/tables/baselines.csv` (129 B; 2 filas de datos).
- **Observation**: el CSV contiene únicamente `mediana_global,1462,18188.34` y `mediana_por_marca,1462,16603.28`. La fila «Modelo principal propio» mostrada en la tabla del documento no tiene respaldo en este CSV; el R² 0,101 se respalda en cambio en `modelo_muestra.csv`.

### Lista numerada de referencias — 38 vs. 41
- **Mentioned in document**: §70: «La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`»; §71.14 enumera [1]–[38].
- **Found in repo**: yes — `Data/referencias.md` (87 líneas, entradas [1]–[41]).
- **Observation**: el archivo añade [39] Department for Transport/DVLA, [40] ANFAC y [41] AEADE, que son justamente las tres fuentes institucionales que §70 declara verificadas. La cifra «38» del texto queda desactualizada frente al artefacto versionado (41).

### Semilla y reproducción — verificación positiva
- **Mentioned in document**: §71.5: «La semilla `SEED = 20261127` está declarada en `run_all.py` y se propaga a cada etapa por la variable de entorno `PROYECTO_SEED`; antes se declaraba sin efecto.»
- **Found in repo**: yes — `Data/analisis_rentabilidad/scripts/run_all.py` (60 LOC).
- **Observation**: confirmado en el código: `SEED = 20261127` (l. 16), `random.seed(SEED)` (l. 17), `np.random.seed(SEED)` (l. 18) y `ENTORNO["PROYECTO_SEED"] = str(SEED)` (l. 23). No hay brecha de artefacto.

### Artefactos de auditoría
- **Mentioned in document**: §69: «la huella queda en `reviews/`… El registro de la tercera pasada está en `reviews/informe-tecnico-2026-11-27-iter3.{md,forensic.md}` y sus 13 artefactos.»
- **Found in repo**: yes — `reviews/` contiene 46 archivos: 3 pasadas completas de 15 archivos cada una (45 artefactos: `e1-claims`, `e2-literature`, `e3-artifacts`, `forensic`, `md`, `plan`, `v1`–`v9`) más el plan en curso de la iteración 4.
- **Observation**: la huella declarada existe y es verificable. La iteración 4 solo tiene `informe-tecnico-2026-11-28-iter4.plan.md` hasta el momento de este inventario.

### Licencia de datos y código
- **Mentioned in document**: §71.5: «No se ha declarado todavía una licencia de datos o código»; §71.15: «la licencia queda pendiente de declaración».
- **Found in repo**: no — sin `LICENSE`/`LICENCIA` en la raíz.
- **Observation**: el documento declara explícitamente la ausencia; el repositorio coincide, por lo que no es una brecha oculta sino una limitación documentada.

## Code-to-document mapping (when discernible)

| Document component | Repo location |
|---|---|
| H1 / Kruskal-Wallis H = 44.313, IC bootstrap (§71.3) | `outputs/tables/comparaciones.csv`, `scripts/04_stats.py` |
| Baselines MAE global / por marca (§71.1) | `outputs/tables/baselines.csv`, `scripts/03b_baselines.py` |
| Ablación `hp` y R² 0,274 → 0,101 (§71.2) | `outputs/tables/modelo_muestra.csv` |
| Semilla `SEED` / `PROYECTO_SEED` (§71.5) | `scripts/run_all.py` |
| Panel interactivo (§61, §71.5) | `Data/dashboard.html` → `docs/dashboard.html` → `site/dashboard.html` |
| Seis gráficos Plotly (§59, §61) | `docs/graficos/01_precios.html` … `06_edad_precio.html` |
| Cinco cuadros del apéndice (§59) | `docs/historia/apendice.md` |
| KPIs con marcadores `<!-- kpi:... -->` (§59–§71) | `outputs/tables/kpis.csv` |
| 41 referencias numeradas (§70, §71.14) | `Data/referencias.md` |
| Huella de auditoría (§69) | `reviews/` (45 artefactos + plan iter4) |
| 256 filas / 11 tiendas (§9) | `Data/catalogos_concesionarios/*.sqlite` |
| Bases crudas LFS y manifiesto (§71.5) | `Data/Revolico/`, `chunks/MANIFEST.json`, `.gitattributes` |
| Sitio MkDocs estricto (§61) | `mkdocs.yml`, `docs/`, `Auxiliares/herramientas/generar_sitio_mkdocs.py` |
| Prueba de humo (§71.5) | `Auxiliares/herramientas/test_smoke_pipeline.py` |

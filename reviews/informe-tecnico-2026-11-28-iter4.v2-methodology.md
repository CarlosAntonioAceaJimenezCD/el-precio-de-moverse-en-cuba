---
type: audit-artifact
phase: v2-methodology
slug: informe-tecnico-2026-11-28-iter4
generated_at: 2026-11-28T03:14:50-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-28-iter4/informe-tecnico-2026-11-28-iter4.text.md
language: es
level: master
---

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

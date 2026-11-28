---
type: audit-artifact
phase: v2-methodology
slug: corpus-total-2026-11-28
generated_at: 2026-11-28T05:43:43-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/corpus-total-2026-11-28/corpus-total-2026-11-28.text.md
language: es
level: master
---

# V2 — Methodology (findings)

### F-V2-001 — Dos bases triviales con MAE publicado y una referencia egipcia sin operacionalizar

La §71.1 (L1516–L1527) enumera tres entradas: «Mediana global ( ingenua )» (MAE 18.188,34 USD sobre 1.462 anuncios), «Mediana por marca» (MAE 16.603,28 USD sobre 1.462 anuncios) y «Egyptian-Used-Cars» como «Referencia de ingeniería del campo: 23.500 anuncios y series mensuales» con «Contraste cualitativo de cobertura y frescura». Las dos medianas están calculadas sobre datos propios y publicadas en `Data/analisis_rentabilidad/outputs/tables/baselines.csv` (`mediana_global,1462,18188.34`; `mediana_por_marca,1462,16603.28`), generadas por `scripts/03b_baselines.py`. La referencia egipcia no figura en ese CSV ni lleva métrica calculada sobre la muestra local; la cuarta fila de la sección es el modelo propio. El espejo inglés de §71.3 (L1539) consigna: «an operationalised SOTA baseline is still missing», y los trabajos de §71.6 (L1558: [14] Gegić, [26] Muça, [9] Du) se usan para posicionamiento argumentativo, sin métrica reproducible. Los MAE se informan sobre 1.462 anuncios, mientras el modelo principal se reporta sobre 586 de 993 candidatas (`modelo_muestra.csv`) y la narrativa de §71.1 usa 584 de 981; §71.1 no declara una partición de entrenamiento y prueba para esas bases. El criterio `V2.baselines` para `level=master` se lee: «≥2 baselines, one of which corresponds to a SOTA-adjacent approach in the field». El recuento de dos bases se satisface; la condición de adyacencia al estado del arte no queda operacionalizada en la sección ni en los artefactos citados.

— polarity: negative · confidence: high · related: [[#C059]], [[#C031]], [[#C062]] · criteria: V2.baselines.master

### F-V2-002 — Ablación explícita del término `hp` con especificación y muestra informadas conjuntamente

La §71.2 (L1529–L1533) etiqueta como ablación la retirada de `hp` y declara que «la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² baja de 0,274 a 0,101», con la salvedad de que «el cambio de especificación y el cambio de muestra se informan juntos». `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` registra dos ajustes diferenciados por ese término: `completo,993,28,0.2744,0.4114` y `principal,993,586,0.1008,0.0`. El criterio `V2.ablations` para `level=master` se lee: «Explicit ablation of at least one component». La ablación existe, está nombrada como tal y cuantifica el efecto, de modo que el estándar de nivel queda cubierto. Como matiz observacional, la retirada del componente coincide con un cambio de muestra (28 frente a 584 en el texto, 28 frente a 586 en el CSV vigente), de modo que el contraste presentado no separa el efecto del término del efecto de la selección de anuncios con kilometraje declarado; el propio párrafo atribuye a esa selección el signo positivo de antigüedad.

— polarity: positive · confidence: high · related: [[#C060]], [[#C008]], [[#F-V2-007]] · criteria: V2.ablations.master

### F-V2-003 — H1 declara control por antigüedad y kilometraje sin contraste ajustado que lo sostenga

El enunciado de H1 (L30 y L172) afirma que «los precios de los tres tiers de marca en el mercado local provienen de la misma distribución, controlando por antigüedad y kilometraje» y que «Se contrasta con Kruskal-Wallis; se rechaza con p < 0,001 en la corrida vigente». `outputs/tables/comparaciones.csv` contiene una sola fila: `precio por tier de marca,1462,44.313,0.0,10000.0,29500.0,Kruskal-Wallis + bootstrap de mediana premium-economico (2000 replicas)`. `scripts/03c_comparaciones.py:25–35` filtra usados locales con precio positivo y agrupa únicamente por `brand_tier`; ni el test ni el bootstrap incluyen `car_age` ni `mileage_km` como covariables. La §3.3 (L2118–L2122) describe el estadístico como alternativa no paramétrica a ANOVA que «no exige normalidad y compara distribuciones completas, no solo medias», sin mención a ajuste por covariables. La única evidencia multi-variable publicada, `outputs/tables/modelo_depreciacion.csv`, da coeficientes de tier con p=0,1421 (`económico`), p=0,0941 (`medio`) y p=0,8753 (`premium`), además de `car_age` (p=0,1504) y `np.log1p(mileage_km)` (p=0,4711) sin significancia. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)». La §71.3 declara diseño no pareado, de modo que los tests pareados del criterio no son aplicables y el bootstrap CI sí está presente; la cláusula «controlando por antigüedad y kilometraje» del enunciado no tiene, sin embargo, contraste ajustado que la sostenga entre las tablas publicadas.

— polarity: negative · confidence: high · related: [[#C001]], [[#C007]], [[#C062]], [[#F-V2-004]] · criteria: V2.statistical_tests.master

### F-V2-004 — El Kruskal-Wallis citado agrupa cuatro categorías, una de ellas `desconocido`

La §3.3 (L2120) aclara que el test se aplica «a los precios por `brand_tier` (grupos con más de 5 observaciones)» y la §71.3 (L1537) cuantifica «el contraste central» con H = 44.313 en el marco de los tres tiers de H1. `scripts/03c_comparaciones.py:31` construye los grupos con `d.groupby("brand_tier")` y `len(g) > 5`, sin excluir la categoría de marca no identificada. Sobre `Data/analisis_rentabilidad/data/listings_clean.parquet` en la corrida vigente, los grupos son `medio` (949), `desconocido` (248), `economico` (133) y `premium` (132), con n=1.462: cuatro categorías, una de las cuales es la clase de marca faltante definida en `config.py`, no un tier de marca. El bootstrap del mismo script (L38–L49) sí remuestrea solo `premium` y `economico`. Ni la §3.3 ni la §71.3 consignan la presencia de `desconocido` en el estadístico omnibus ni cuantifican su contribución al rechazo. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)»; la elección de un test de grupos independientes es coherente con el diseño declarado, mientras que la composición de los grupos del contraste informado no se corresponde con los tres tiers enunciados.

— polarity: negative · confidence: high · related: [[#C001]], [[#C007]], [[#F-V2-003]] · criteria: V2.statistical_tests.master

### F-V2-005 — Intervalo bootstrap positivo frente a coeficiente premium no significativo, sin reconciliación

La §71.3 (L1537) reporta «un intervalo bootstrap de la diferencia de medianas premium−económico de 10.000 a 29.500 USD (`comparaciones.csv`, 2.000 réplicas)», valores que coinciden con `outputs/tables/comparaciones.csv` (`ic_bajo=10000.0`, `ic_alto=29500.0`). En paralelo, la §3.1 (L2108) informa que en el modelo completo «ningún coeficiente alcanza significancia (el p_valor más bajo es 0,0941)» y el Cuadro 5 (L2027–L2029) da `C(brand_tier)[T.premium]` con coeficiente 0,1146 y p=0,875, confirmado en `modelo_depreciacion.csv` (p=0,8753). El corpus no explicita que ambos números estiman cantidades distintas —diferencia de medianas no ajustada sobre 1.462 anuncios frente a coeficiente log-lineal ajustado sobre 28 observaciones— ni consigna comparaciones por pares con corrección. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)»: el intervalo por remuestreo está presente, y la convivencia de ambas conclusiones permanece como observación de consistencia entre declaraciones y artefactos.

— polarity: neutral · confidence: high · related: [[#C006]], [[#C061]], [[#F-V2-003]] · criteria: V2.statistical_tests.master

### F-V2-006 — Diseño declarado como no pareado, con tests de grupos independientes y bootstrap

La §71.3 (L1535–L1539) declara: «No hay diseño pareado: los anuncios son observaciones independientes, por lo que no se aplican Wilcoxon de pares ni t de diferencias; se usan Kruskal-Wallis y Welch para grupos independientes», y añade el intervalo bootstrap de 2.000 réplicas. La §3.4 (L2124–L2128) precisa que Welch está «codificado, no ejecutado en la corrida actual» porque `is_new` no varía en el subconjunto del modelo; `outputs/tables/tests.csv` contiene en consecuencia una sola fila, la de Kruskal-Wallis. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)». Bajo ese criterio, la ausencia de tests pareados se corresponde con el diseño observacional declarado y la técnica de remuestreo empleada figura entre las enumeradas; la ejecución efectiva se limita al contraste omnibus y al intervalo de medianas.

— polarity: positive · confidence: high · related: [[#C062]], [[#F-V2-005]] · criteria: V2.statistical_tests.master

### F-V2-007 — Unidad de muestra reconvertida a anuncios, con asimetrías y dos recuentos de candidatas

La §71.3 (L1537) fija la unidad: «El tamaño se mide en anuncios (981 candidatas de 8 marketplaces), no en ensayos experimentales». La §71.1 (L1524–L1525) repite «Las 981 candidatas» y reporta el modelo principal con «R² 0,101 sobre 584 observaciones»; la §71.2 (L1531) habla de «28 a 584 observaciones de 981 candidatas». Frente a esos valores, la §59 (L1410) y la §60 (L1418), y después la §3.1 (L2108–L2110), documentan 28 completas y 586 principales «de 993 candidatas». En los artefactos, `modelo_muestra.csv` registra `principal,993,586` y `completo,993,28`, mientras `baselines.csv` y `comparaciones.csv` trabajan sobre 1.462 anuncios. El criterio `V2.sample_size` para `level=master` se lee: «≥20 trials; ≥10 datasets/instances». La unidad declarada es el anuncio observacional, no el ensayo, y la propia sección explica esa reconversión; el modelo principal supera el umbral numérico de 20, el completo se apoya en 28 observaciones y las fuentes declaradas son ocho, por debajo de diez. La asimetría entre 28, 586 y 1.462 observaciones, junto con los dos recuentos de candidatas (981 frente a 993), permanece sin reconciliar dentro de la sección que declara los estándares de nivel; no se declara análisis de potencia, elemento correspondiente al nivel `phd`.

— polarity: negative · confidence: high · related: [[#C008]], [[#C009]], [[#F-V2-002]] · criteria: V2.sample_size.master

### F-V2-008 — Subsección dedicada que cubre las cuatro categorías de amenaza a la validez

La §71.4 (L1541–L1548) dedica un apartado explícito a amenazas externas («solo La Habana y anuncios en línea; los precios son pedidos, no transaccionados»), de constructo («kilometraje y potencia faltan en la mayoría de los anuncios; la condición se infiere del texto»), internas («no hay asignación aleatoria; la ablación es observacional») y de conclusión estadística («el modelo completo usa 28 observaciones y ningún coeficiente alcanza p < 0,05»). El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations». El documento cubre el mínimo de nivel y enumera además las cuatro categorías reservadas al nivel `phd`, aunque sin mitigaciones ni declaración de replicabilidad, que son elementos del nivel `paper`. El apartado reformula límites ya presentes en §18 y §19 (L855, L860), lo que refuerza su coherencia con el resto del informe.

— polarity: positive · confidence: high · related: [[#C013]], [[#C015]] · criteria: V2.threats_to_validity.master

### F-V2-009 — La convención de conversión TRMI fija no figura entre las amenazas declaradas

La §71.4 (L1543–L1546) enumera las amenazas de constructo en términos de kilometraje, potencia y condición inferida del texto. La conversión monetaria se rige, en cambio, por una convención explícita: la §23 (L931) señala que «el pipeline de `Data/analisis_rentabilidad/` usa la TRMI fija de 930 CUP/USD del 18/11/2026 (`config.py`); la serie diaria es referencia histórica, no insumo del modelo actual», y la tabla de funciones (L2067) la describe como «una convención monetaria explícita». El README (L1684) y el storytelling (L1900) repiten el valor 930 CUP/USD. Ninguna de las cuatro viñetas de §71.4 menciona esa fijación de la tasa ni su efecto sobre la comparabilidad de precios anunciados a lo largo del periodo. El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations»: la subsección existe y es breve; la observación se refiere a la cobertura de una convención declarada en otras secciones.

— polarity: neutral · confidence: medium · related: [[#C010]], [[#F-V2-008]] · criteria: V2.threats_to_validity.master

### F-V2-010 — Protocolo de reproducción declarado con semilla, comando único y código referenciado

La §71.5 (L1550–L1554) consigna la semilla `SEED = 20261127`, el comando único `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py`, cuatro puntos de entrada con argumentos, dependencias «fijadas a serie menor en `requirements.txt`», la prueba de humo `python3 Auxiliares/herramientas/test_smoke_pipeline.py`, el repositorio público y la reconstrucción de las bases desde `chunks/MANIFEST.json`. `scripts/run_all.py:16,23,39` fija la semilla, la escribe en `ENTORNO["PROYECTO_SEED"]` y la entrega a cada subproceso. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced». Los tres elementos están presentes y anclados a archivos del repositorio; la prueba de humo y el manifiesto de fragmentos exceden el mínimo del nivel. La propia sección declara «No se ha declarado todavía una licencia de datos o código», y no figuran un commit fijado ni una versión de los datos, elementos correspondientes a los niveles `phd` y `paper`.

— polarity: positive · confidence: high · related: [[#C063]], [[#C067]] · criteria: V2.reproducibility_protocol.master

### F-V2-011 — `PROYECTO_SEED` se propaga a todas las etapas, con un único consumidor declarado al detalle

La §71.5 (L1552) afirma que la semilla «se propaga a cada etapa por la variable de entorno `PROYECTO_SEED`; antes se declaraba sin efecto». `AUTOMATIZACION.md` (L2313) matiza: «solo el bootstrap de `03c_comparaciones.py` la consume, porque las demás etapas son deterministas». En el checkout, `scripts/run_all.py:22–39` copia el entorno y añade la variable para los siete subprocesos de `STEPS`, mientras `scripts/03c_comparaciones.py:20,37` es el único archivo que la lee e inicializa `np.random.default_rng(SEED)` para las 2.000 réplicas. Ambas declaraciones describen operaciones distintas —propagación del entorno frente a consumo efectivo— y el código confirma la segunda. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced»: la semilla declarada sostiene la reproducibilidad del único resultado estocástico publicado, el intervalo bootstrap.

— polarity: neutral · confidence: high · related: [[#C063]], [[#F-V2-010]] · criteria: V2.reproducibility_protocol.master

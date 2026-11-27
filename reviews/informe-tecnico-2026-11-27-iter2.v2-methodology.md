---
type: audit-artifact
phase: v2-methodology
slug: informe-tecnico-2026-11-27-iter2
generated_at: 2026-11-27T17:18:09-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter2/informe-tecnico-2026-11-27-iter2.text.md
language: es
level: master
---

# V2 — Methodology (findings)

## Resumen

La ablación `principal`/`completo` existe en el CSV del pipeline pero no se declara como tal en el documento y confunde el cambio de especificación con una caída de 584 a 28 observaciones: no satisface `V2.ablations.master`.
No hay semillas aleatorias: las únicas «semillas» del texto son ocho URLs de marketplaces en §55, frente a la cláusula «seeds mentioned» de `V2.reproducibility_protocol.master`.
Sí se registran límites dedicados, pruebas estadísticas y código referenciado; persisten la ausencia de test pareado y tres estados incompatibles del mismo modelo.

### F-V2-001 — El «benchmark» sigue siendo descriptivo, sin comparador SOTA-adjacente

El esqueleto de rentabilidad declara `05_benchmark.py` como «benchmark por marca/modelo/año e infravalorados» (§34, L1028) y la línea base consigna «Grupos de benchmark | 21» e «Infravalorados | 30» (§34, L1052–1053), pero no compare el desempeño del modelo hedónico contra otro enfoque. El único contraste nombrado es de escala: «Egipto tiene 23.500 anuncios [...] Nosotros tenemos el pipeline y las técnicas cubiertas, pero solo 497 usados, un único snapshot» (§34, L1060; [[#C012]]), presentado como «Brecha frente a Egipto» y no como línea base reproducible; la arquitectura se describe como «inspirada en Egyptian-Used-Cars» ([[#C011]]). El contexto de la iteración 2 mantiene F-V10-006 como «NO RESUELTA» en cuanto a diferenciación. El criterio `V2.baselines` para `level=master` se lee: «≥2 baselines, one of which corresponds to a SOTA-adjacent approach in the field».

— polarity: neutral · confidence: high · related: [[#C011]], [[#C012]], [[#F-V10-006]] · criteria: V2.baselines.master

### F-V2-002 — Ablación `principal`/`completo` presente en el artefacto, no declarada en el documento

El CSV que respalda §59 contiene dos configuraciones: `principal` con 981 candidatas, 584 observaciones, R² 0,101 y p del F 0,0; `completo` con 981 candidatas, 28 observaciones, R² 0,2744 y p del F 0,4114, con la formulación `log_price ~ car_age + np.log1p(mileage_km) + condition_score + C(brand_tier)` y la variante con `hp` (E3, «New artifacts», líneas 138–144). El documento, en cambio, nombra una sola: «El modelo con todos los términos dispone de 28 observaciones completas de 981 candidatas (R² = 0,277; p del F = 0,411)» (§59, L1381), sin citar `modelo_muestra.csv` — la búsqueda de esa ruta en la caché del documento no devuelve coincidencias— y sin presentar la comparación entre configuraciones como ablación. Las dos especificaciones no difieren solo en un término: el n pasa de 584 a 28 y el p del F de 0,0 a 0,4114, de modo que el efecto del componente queda confundido con la selección muestral. El inventario E1 registra «sin ablación ni test pareado entre corridas» ([[#C004]]) y F-V10-002 permanece «PARCIALMENTE RESUELTA». El criterio `V2.ablations` para `level=master` se lee: «Explicit ablation of at least one component».

— polarity: negative · confidence: high · related: [[#C004]], [[#C005]], [[#C006]], [[#F-V10-002]], [[#F-V2-003]] · criteria: V2.ablations.master

### F-V2-003 — Sensibilidad al kilometraje sin aislamiento de componentes

La primera corrida atribuye al modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` una «depreciación media de −5,43 % anual (p<0,001)» (§34, L1056; [[#C006]]), mientras que la narrativa vigente afirma que «el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje» (§59, L1381; [[#C004]]), con «p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05» (§60, L1389). La corrección del campo se documenta como `parse_number()` para separadores de miles (§51, L1282), pero el texto no separa el efecto de esa reparación del efecto de cambiar la especificación ni del cambio de muestra; la retirada de la cifra se reitera en §44 (L1206) y §45 (L1214) sin un contraste controlado. Es una comprobación de sensibilidad declarada, no una ablación explícita de un componente. El criterio `V2.ablations` para `level=master` se lee: «Explicit ablation of at least one component».

— polarity: neutral · confidence: high · related: [[#C004]], [[#C006]], [[#F-V10-002]], [[#F-V2-002]] · criteria: V2.ablations.master

### F-V2-004 — Pruebas estadísticas y diagnósticos declarados, con decisión de no significancia

El inventario de funciones enumera «modelo hedónico log-lineal, VIF, Kruskal-Wallis, Welch t-test y detección de anomalías» y explica «por qué la corrida actual **no** sostiene una tasa de depreciación ni una prima premium significativa (p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05)» (§60, L1389). La arquitectura ya reservaba `04_stats.py` para «OLS log-precio, VIF, Kruskal-Wallis, anomalías» (§34, L1027) y la estimación vigente acompaña el p del F de 0,411 con la limitación de n (§59, L1381; [[#C005]]). La presencia de pruebas y de diagnósticos de colinealidad, junto con la decisión de retirar una afirmación de significancia, constituye una observación positiva dentro de este criterio. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)».

— polarity: positive · confidence: high · related: [[#C004]], [[#C005]], [[#C011]] · criteria: V2.statistical_tests.master

### F-V2-005 — Comparaciones entre configuraciones y corridas sin test pareado

La comparación que sostiene el cambio de conclusión —de «−5,43 % anual (p<0,001)» (§34, L1056) a «no encuentra una pendiente anual significativa» (§59, L1381)— enfrenta dos ejecuciones sobre estados de datos distintos, sin prueba pareada ni intervalo de la diferencia; el propio [[#C004]] lo anota. Lo mismo ocurre entre `principal` y `completo` en el CSV descrito por E3: el Welch t-test aparece en el inventario de §60 (L1389), pero no se registra como contraste pareado entre esas dos especificaciones ni se declara qué comparación realiza. No hay declaración de Wilcoxon, test de signos, t-test de diferencias ni intervalo bootstrap para estos pares. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)».

— polarity: neutral · confidence: high · related: [[#C004]], [[#C005]], [[#C006]], [[#F-V2-002]], [[#F-V2-003]] · criteria: V2.statistical_tests.master

### F-V2-006 — Tamaños muestrales e instancias declarados en cada etapa

El documento explicita n en todas las fases: «11 bases» y 256 filas (§9, L94–108), «Resultados sobre 323 autos: 248 precios USD válidos» (§22, L894), «Filas ingeridas 972 [...] Filas limpias 499 [...] Observaciones del modelo OLS 328» (§34, L1045–1051), «33 respuestas de encuesta» y entrevistas «30 + 30 + 8» (E3, Datasets; §50), «15 fuentes web» con «8 semillas de marketplaces» (§55, L1337) y «981 candidatas» con 28 observaciones completas (§59, L1381). El número de instancias y de observaciones supera los umbrales numéricos del criterio. El criterio `V2.sample_size` para `level=master` se lee: «≥20 trials; ≥10 datasets/instances».

— polarity: positive · confidence: high · related: [[#C014]], [[#C035]], [[#C040]], [[#C005]], [[#C100]] · criteria: V2.sample_size.master

### F-V2-007 — Un único snapshot, sin repeticiones y cobertura desigual entre fuentes

Los recuentos son abundantes pero no constituyen repeticiones: la propia comparación declara «un único snapshot, HP/kilometraje mayormente ausentes» (§34, L1060), sin corridas independientes por condición. La cobertura de variables es heterogénea —«marca 68,4 %, año 63,5 %, km 6,2 % (heurísticos, extraídos solo de título/descripción)» (§22, L894; [[#C100]])— y la tabla de tiendas registra «Chinautos Cuba | 70 | 0» y «Envision Autos | 1 | 0» frente a «AGN Motors | 60 | 45» (§9, L96–108). En el modelo, la condición `completo` reduce el n de 584 a 28 (E3, líneas 138–144), apenas sobre el umbral de veinte observaciones. El criterio `V2.sample_size` para `level=master` se lee: «≥20 trials; ≥10 datasets/instances».

— polarity: neutral · confidence: high · related: [[#C014]], [[#C100]], [[#C105]], [[#F-V2-002]], [[#F-V2-006]] · criteria: V2.sample_size.master

### F-V2-008 — Subsección «Límites» dedicada y auditoría de procedencia

El marco de análisis incluye el apartado específico «**Límites**: precios pedidos no transaccionados, sesgo de supervivencia de anuncios, sin datos personales, vigencia normativa a verificar» (§19, L855; [[#C013]]). La auditoría de procedencia lo refuerza: «No son estadísticas oficiales; son precios **pedidos**, no transaccionados» y «las fuentes oficiales y gremiales sirven de **contexto y validación**; los anuncios y redes son la **señal de precio** pero no sustituyen estadísticas oficiales» (§18, L826, L831; [[#C007]]). Se añaden supuestos operativos —«no se comprueba disponibilidad en tiempo real» (§23, L903; [[#C103]])— y la distinción «inferencia de diseño, no medición» para la retención (§63, L1417; [[#C053]]). El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations».

— polarity: positive · confidence: high · related: [[#C007]], [[#C013]], [[#C053]], [[#C103]], [[#C108]] · criteria: V2.threats_to_validity.master

### F-V2-009 — Atribuciones causales sin diseño comparativo

Tres afirmaciones conservan forma causal sin contraste de condiciones: «El scraping sostenible depende del ritmo, la sesión y la reanudación, no principalmente del fingerprint TLS» (§12, L137; [[#C027]]), «La regla de las 10 páginas evitó consumir resultados repetidos» (§12, L138; [[#C028]]) y la jerarquía «la ruta más eficiente es Telegram MTProto [...] Le sigue Facebook GQL» (§15, L767–769; [[#C032]]), y el inventario E1 anota «jerarquía declarada sin medición comparativa de rendimiento». Las dos primeras se apoyan en reglas y conteos (§7, L78–84; §11, L126–131), no en condiciones comparadas. El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations».

— polarity: neutral · confidence: high · related: [[#C027]], [[#C028]], [[#C032]], [[#F-V2-008]] · criteria: V2.threats_to_validity.master

### F-V2-010 — Protocolo con puntos de entrada, manifiestos con hash y regeneración documentada

La arquitectura declara `config.py` y `01_ingest.py` a `05_benchmark.py`, además de `run_all.py` (§34, L1020–1036); la regeneración se registra en «`run_all.py` volvió a correr sobre la base de 744 autos» (§51, L1280) y «El pipeline se regeneró con el entorno `Auxiliares/.venv-py`» (§58, L1371). La integridad se documenta con «un `MANIFEST.json` que guarda el SHA-256 del archivo completo, el orden, el offset y el hash de cada fragmento. La verificación de los 82 chunks dio OK» (§54, L1325), con reconstrucción por hash también en la sincronización por timer (§14, L756). E3 inventaría los entry points y `test_modelo.py` comprueba la idempotencia de `04_stats.py`; la compilación «`mkdocs build --strict` termina sin errores ni enlaces rotos» (§61, L1399). La parte «Protocol fully described» y «code referenced» del criterio queda cubierta; la cláusula de semillas se evalúa por separado. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced».

— polarity: positive · confidence: high · related: [[#C002]], [[#C033]], [[#C042]], [[#C054]], [[#F-V2-011]] · criteria: V2.reproducibility_protocol.master

### F-V2-011 — Semillas: solo URLs de entrada, ninguna semilla aleatoria declarada

La única aparición de «semillas» en el documento es «Las 8 semillas de marketplaces también se descargaron y se contaron sus enlaces de anuncio» (§55, L1337): son URLs de partida del crawl, no semillas de generación aleatoria. No hay `seed`, `random_state` ni declaración equivalente en §34 (L1018–1039), §59 (L1379–1381) ni §60 (L1387–1389), y el inventario E1 no registra ningún claim de semillas. Los elementos estocásticos declarados —«Pausa 7–10 s con jitter» (§11, L127) y las «26 búsquedas en tgden.com» para descubrir canales ([[#C113]])— se describen sin semilla asociada. Las estimaciones reportadas (OLS, medianas, IQR, VIF, pruebas de rangos) son deterministas dado el dataset, pero la conjunción literal del criterio no se satisface. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced».

— polarity: neutral · confidence: high · related: [[#C002]], [[#C005]], [[#C074]], [[#C075]], [[#C113]], [[#F-V2-010]] · criteria: V2.reproducibility_protocol.master

### F-V2-012 — Tres estados incompatibles del mismo modelo sin marcador de versión

El estado vigente de §59 es «28 observaciones completas de 981 candidatas (R² = 0,277; p del F = 0,411)» (L1381), con marcadores `<!-- kpi:modelo_* -->` que se actualizan desde `kpis.csv`. El CSV archivado registra, para esa misma `completo`, R² 0,2744 y p 0,4114, y para `principal` 584 observaciones con R² 0,101 y p 0,0 (E3, líneas 138–144); en paralelo, `MODELOS_Y_FUNCIONES.md` y sus copias describen «572 observaciones de 897 candidatas [...] el completo usa 22 (R² = 0,277; p del F = 0,623)» (E3, línea 143). El paralelo inglés de §59 añade otro estado: «744 unique cars, 2,014 clean listings» (L1383) frente a «772 autos únicos, 2.029 anuncios limpios» del español (L1379). E1 califica F-V10-001 como «PARCIALMENTE RESUELTA» y F-V10-008 como «RESUELTA», pero las tres versiones del modelo no llevan etiqueta que indique cuál produce cada cifra. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced»; la coherencia interna entre secciones queda sin resolución.

— polarity: negative · confidence: high · related: [[#C003]], [[#C005]], [[#C050]], [[#F-V10-001]], [[#F-V10-008]], [[#F-V2-002]], [[#F-V2-011]] · criteria: V2.reproducibility_protocol.master

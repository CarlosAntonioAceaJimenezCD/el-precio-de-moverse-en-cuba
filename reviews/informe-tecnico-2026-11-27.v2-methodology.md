---
type: audit-artifact
phase: v2-methodology
slug: informe-tecnico-2026-11-27
generated_at: 2026-11-27T05:55:07Z
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27/informe-tecnico-2026-11-27.text.md
language: es
level: master
---

# V2 — Methodology (findings)

## Resumen

El documento declara tamaños muestrales, pruebas estadísticas y un protocolo con scripts, hashes y regeneración documentada, en el nivel de maestría.
No registra baseline SOTA-adjacente, ablación de componentes ni medición comparada de la eficiencia de las fuentes de captura.
Persisten la ausencia de semillas, la falta de tests pareados entre corridas y cifras incompatibles del mismo objeto sin marcador de versión.

### F-V2-001 — Modelo hedónico sin comparador SOTA-adjacente; el «benchmark» es descriptivo

El único componente comparativo del esqueleto de rentabilidad es `05_benchmark.py`, descrito como «benchmark por marca/modelo/año e infravalorados» (§34, líneas 1019–1025), con 21 «Grupos de benchmark» y 30 «Infravalorados» en la línea base (§34, líneas 1047–1050). El contraste con el estudio egipcio se presenta como brecha de volumen —«Egipto tiene 23.500 anuncios, historial mensual de precios, HP y kilometraje estructurados [...] Nosotros tenemos el pipeline y las técnicas cubiertas, pero solo 497 usados, un único snapshot» (§34, líneas 1054–1056)—, no como un comparador reproducible de desempeño. No se declara una comparación del modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` frente a un predictor trivial, a otra especificación o a un enfoque vecino al estado del arte. El criterio `V2.baselines` para `level=master` se lee: «≥2 baselines, one of which corresponds to a SOTA-adjacent approach in the field».

— polarity: neutral · confidence: high · related: [[#C009]], [[#C011]], [[#C123]], [[#F-V2-002]] · criteria: V2.baselines.master

### F-V2-002 — Orden de eficiencia de Telegram, Facebook y WAHA sin medición comparada

El informe establece un orden de eficiencia entre rutas de captura: «la ruta más eficiente es Telegram MTProto (`telethon`, ya integrado): sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`. Le sigue Facebook GQL [...] Playwright/Selenium quedan como último recurso» (§15, líneas 763–765). El inventario de claims registra la salvedad de que «el texto no adjunta una medición de tiempo por fuente» ([[#C007]]); la propia corrida pública de Telegram reporta «152 mensajes, 54 anuncios de autos [...] y ninguno con precio explícito» (§28, línea 948), mientras que el descubrimiento de canales suma 119 entradas (§29, líneas 962–967). La jerarquía se apoya en propiedades de las herramientas, sin tiempos, tasas de éxito ni tamaños de muestra comparables por ruta. El criterio `V2.baselines` para `level=master` se lee: «≥2 baselines, one of which corresponds to a SOTA-adjacent approach in the field».

— polarity: neutral · confidence: high · related: [[#C007]], [[#C092]], [[#C093]], [[#C113]], [[#F-V2-001]] · criteria: V2.baselines.master

### F-V2-003 — Sensibilidad al kilometraje como ablación implícita, sin ablación de componentes declarada

La primera ejecución reporta «El modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` da una depreciación media de **−5,43 % anual** (p<0,001), con primas de +21 % para premium y −22 % para tier medio» (§34, línea 1052); la narrativa final consigna que «el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra» (§59, línea 1377), con «p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05» (§60, línea 1385). Esta variación de especificación funciona como comprobación de sensibilidad de un covariable, no como ablación de los componentes declarados como aporte. Las mejoras posteriores se ejecutaron «una por una, sin borrar archivos» (§51, línea 1273), incluida la corrección del parseo de kilometraje (§51, línea 1278), sin que el texto aísle el efecto de cada cambio sobre la estimación. El mapa literario registra [[#P009]] (Du et al., 2026, DOI: 10.54254/2754-1169/2026.38524) con especificación log-lineal anidada casi idéntica y conclusión de no linealidad edad–precio, trabajo que el documento no cita. El criterio `V2.ablations` para `level=master` se lee: «Explicit ablation of at least one component».

— polarity: neutral · confidence: high · related: [[#C009]], [[#C011]], [[#C165]], [[#C067]], [[#P009]], [[#F-V2-005]] · criteria: V2.ablations.master

### F-V2-004 — Pruebas estadísticas y diagnósticos declarados en el pipeline final

El inventario de funciones y modelos enumera «normalización sintáctica y TRMI, features derivados, mediana y cuartiles, modelo hedónico log-lineal, VIF, Kruskal-Wallis, Welch t-test y detección de anomalías» y reporta «p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05» (§60, línea 1385). La arquitectura del esqueleto ya declaraba `04_stats.py` como «OLS log-precio, VIF, Kruskal-Wallis, anomalías» (§34, línea 1023) y la primera corrida acompañó el coeficiente de depreciación de `p<0,001` (§34, línea 1052). En el nivel de maestría, la presencia de pruebas y de diagnósticos de multicolinealidad, con la decisión de no sostener la significancia, constituye una observación positiva sobre la práctica estadística del documento. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)».

— polarity: positive · confidence: high · related: [[#C011]], [[#C176]], [[#C009]] · criteria: V2.statistical_tests.master

### F-V2-005 — Contrastes múltiples y cambio de corrida sin test pareado ni corrección declarada

Los tres coeficientes de la primera corrida —pendiente anual y dos contrastes de `brand_tier` (+21 % y −22 % frente al desconocido)— comparten un `p<0,001` sin que se declare ajuste por comparaciones múltiples (§34, línea 1052); la corrida final enuncia un «p mínimo 0,165» entre varias pruebas (§60, línea 1385) sin ajuste descrito. El paso de una depreciación significativa a su retirada compara dos ejecuciones sobre estados de datos distintos ([[#C009]], [[#C011]]), sin test pareado ni intervalo de diferencia. La reconciliación de la encuesta, de 29 a 28 interesados (§51, línea 1281), tampoco se acompaña de prueba estadística. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)».

— polarity: neutral · confidence: high · related: [[#C009]], [[#C011]], [[#C167]], [[#F-V2-003]], [[#F-V2-004]] · criteria: V2.statistical_tests.master

### F-V2-006 — Tamaños muestrales y cobertura declarados en cada etapa del análisis

El documento explicita el n en cada etapa: «Resultados sobre 323 autos: 248 precios USD válidos (≥500 USD); 74 precios <500 USD marcados como inválidos y 1 en CUP excluidos» (§22, línea 890); «Filas ingeridas 972 (716 Revolico + 256 concesionarios); Filas limpias 499; Observaciones del modelo OLS 328» (§34, líneas 1041–1047); «744 autos únicos» (§51, línea 1275); «2.014 anuncios limpios, de ellos 1.323 locales y 691 de importación» (§58, línea 1367); encuesta de «33 personas de 4 segmentos» y entrevistas «30 + 30 + 8» (§50, línea 1265). El número de instancias declaradas supera diez (11 bases por tienda en §9, 8 marketplaces en §55) y las observaciones del modelo superan veinte. El criterio `V2.sample_size` para `level=master` se lee: «≥20 trials; ≥10 datasets/instances».

— polarity: positive · confidence: high · related: [[#C053]], [[#C032]], [[#C010]], [[#C063]], [[#C164]] · criteria: V2.sample_size.master

### F-V2-007 — Cobertura de precio desigual entre tiendas y de kilometraje al 6,2 %

La tabla de la fase 6 muestra asimetrías de cobertura del campo de precio entre las 11 bases: «Chinautos Cuba | 70 | 0», «Envision Autos | 1 | 0», «MCV Commercial | 4 | 0», frente a «AGN Motors | 60 | 45» y «Finauto | 45 | 34» (§9, líneas 94–106). En el análisis descriptivo la cobertura declarada es «marca 68,4 %, año 63,5 %, km 6,2 % (heurísticos, extraídos solo de título/descripción)» (§22, línea 890), y el estado del scrapeo precisa que «No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión» (§24, línea 907). El texto añade que la línea base dispone de «un único snapshot» (§34, línea 1056): los recuentos son abundantes, pero la densidad de variables y la repetición temporal no son uniformes entre fuentes. El criterio `V2.sample_size` para `level=master` se lee: «≥20 trials; ≥10 datasets/instances».

— polarity: neutral · confidence: high · related: [[#C033]], [[#C055]], [[#C059]], [[#C123]], [[#F-V2-006]] · criteria: V2.sample_size.master

### F-V2-008 — Subsección «Límites» dedicada y auditoría de procedencia

El marco de análisis incluye un apartado específico: «**Límites**: precios pedidos no transaccionados, sesgo de supervivencia de anuncios, sin datos personales, vigencia normativa a verificar» (§19, línea 851). La auditoría de procedencia refuerza esa sección al clasificar las fuentes y sentenciar «No son estadísticas oficiales; son precios **pedidos**, no transaccionados» (§18, línea 822) y «las fuentes oficiales y gremiales sirven de **contexto y validación**; los anuncios y redes son la **señal de precio** pero no sustituyen estadísticas oficiales» (§18, línea 827). Se declaran además supuestos operativos —«se asume que son comprables; no se comprueba disponibilidad en tiempo real» (§23, línea 899) y el supuesto de catálogos de §25 (línea 917)— y la retención como «inferencia de diseño, no medición» (§63, línea 1413). El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations».

— polarity: positive · confidence: high · related: [[#C008]], [[#C057]], [[#C061]], [[#C097]], [[#C013]], [[#C123]] · criteria: V2.threats_to_validity.master

### F-V2-009 — Atribuciones causales y diagnósticos sin diseño comparativo

Tres conclusiones y diagnósticos del informe tienen forma causal sin comparación explícita: «El scraping sostenible depende del ritmo, la sesión y la reanudación, no principalmente del fingerprint TLS» (§12, línea 135; [[#C006]]), «La regla de las 10 páginas evitó consumir resultados repetidos» (§12, línea 136; [[#C014]]), y «Se identificó la causa del retraso en la clasificación: el timer ejecutaba `actualizar_revolico.py`, que solo corre el scraper y divide la BD, sin escribir nunca `autos`/`revision`» (§26, línea 924; [[#C062]]). La primera y la segunda se apoyan en reglas y conteos de las búsquedas (§7, líneas 76–84; §11, líneas 124–129), no en un contraste de condiciones. El propio texto deja «vigencia normativa a verificar» (§19, línea 851) y condiciona la publicación a la verificación de normas cubanas (§10, línea 117); el mapa literario concluye que la evidencia revisada «no permite pronunciarse sobre el cumplimiento legal en Cuba» (E2, comprobación H4). Las cuatro categorías clásicas de validez no aparecen nombradas en el documento. El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations».

— polarity: neutral · confidence: high · related: [[#C006]], [[#C014]], [[#C062]], [[#C005]], [[#F-V2-008]] · criteria: V2.threats_to_validity.master

### F-V2-010 — Protocolo reproducible con scripts, manifiestos con hash y regeneración documentada

La arquitectura de rentabilidad declara puntos de entrada numerados (`01_ingest.py` a `05_benchmark.py`, `run_all.py`) y `config.py` (§34, líneas 1016–1033). La integridad de datos se documenta con «un `MANIFEST.json` que guarda el SHA-256 del archivo completo, el orden, el offset y el hash de cada fragmento. La verificación de los 82 chunks dio OK» (§54, línea 1321), con herramienta `db_chunks.py` de `split`, `verify` y `assemble` (§54, línea 1323) y reconstrucción verificada por hash también en la sincronización por timer (§14, líneas 752–759). La regeneración se registra en dos puntos —«`run_all.py` volvió a correr sobre la base de 744 autos» (§51, línea 1276) y «El pipeline se regeneró con el entorno `Auxiliares/.venv-py`» (§58, línea 1367)—, junto a `requirements.txt` (§55, línea 1337), commits por lotes de 25 (§16, línea 779) y compilación `mkdocs build --strict` sin errores (§61, línea 1395). El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced».

— polarity: positive · confidence: high · related: [[#C121]], [[#C170]], [[#C176]], [[#C049]], [[#C024]], [[#C091]] · criteria: V2.reproducibility_protocol.master

### F-V2-011 — Semillas no declaradas en un protocolo por lo demás determinista

No aparece ninguna semilla aleatoria en el documento: la búsqueda textual solo devuelve «Las 8 semillas de marketplaces también se descargaron» (§55, línea 1333), referida a URLs semilla, no a `seed` o `random_state`. El inventario de modelos enumera transformaciones y estimaciones (§60, línea 1385) sin declarar semillas, al igual que la arquitectura de rentabilidad (§34, líneas 1016–1035) y la configuración del temporizador de captura (§66, línea 1437). Las estimaciones reportadas —OLS, medianas, IQR, VIF, pruebas de rangos— son deterministas dado el dataset; la selección de canales (§29, línea 967: 26 búsquedas en tgden.com) y las reglas de parada (§7, línea 76) se describen sin semilla asociada. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced».

— polarity: neutral · confidence: high · related: [[#C176]], [[#C121]], [[#C025]], [[#C187]] · criteria: V2.reproducibility_protocol.master

### F-V2-012 — Cifras incompatibles del mismo objeto sin marcador de versión entre secciones

Varios estados del mismo conjunto se presentan sin etiqueta que los distinga: «Se prepararon 11 bases y se obtuvieron **256 filas**» (§9, línea 92), «`anuncios` 6.334» (§24, línea 909), «**744 autos únicos**» (§51, línea 1275) y «**2.014 anuncios limpios**» (§58, línea 1367). La mediana de precio adoptada oscila entre «22.000 USD» (§22, línea 890), «24.000 USD» (§34, línea 1045), «23.000 USD» (§45, línea 1210) y «21.000 USD» (§59, línea 1375). La depreciación pasa de «−5,43 % anual (p<0,001)» (§34, línea 1052) y de su reiteración en el relato (§44, línea 1202) a «no encuentra una pendiente anual significativa tras corregir el kilometraje» (§59, línea 1377), sin que el texto marque qué corrida produce cada cifra. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced»; la coherencia entre declaraciones de distintas secciones queda así sin resolución interna.

— polarity: negative · confidence: high · related: [[#C032]], [[#C010]], [[#C054]], [[#C075]], [[#C009]], [[#C011]], [[#F-V2-005]] · criteria: V2.reproducibility_protocol.master

### F-V2-013 — Encuesta de demanda con n declarado pero marco de muestreo local

La encuesta de demanda se describe como «un Google Forms de 32 preguntas aplicado a 33 personas de 4 segmentos en un barrio de La Habana (17 de 18–25 prefieren eléctrico, pero 16 de 18 no pagarían más de 4.000 USD por uno)» (§50, línea 1265), y su reconciliación reduce a «28 interesados (14 eléctrico, 10 combustión, 4 híbrido)» (§51, línea 1281). El documento no declara marco de muestreo, tasa de respuesta ni intervalos de confianza para esas proporciones, y las «entrevistas (30 + 30 + 8) son cualitativas» (§50, línea 1265). La proyección de alcance se presenta como «inferencia de diseño, no medición» (§63, línea 1413), distinción que el texto explicita para la retención pero no para las preferencias de pago de la encuesta. El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations».

— polarity: neutral · confidence: high · related: [[#C063]], [[#C167]], [[#C164]], [[#C013]], [[#F-V2-008]] · criteria: V2.threats_to_validity.master

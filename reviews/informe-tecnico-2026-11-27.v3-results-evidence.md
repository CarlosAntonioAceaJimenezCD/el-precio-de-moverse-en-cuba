---
type: audit-artifact
phase: v3-results-evidence
slug: informe-tecnico-2026-11-27
generated_at: 2026-11-27T06:10:00Z
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27/informe-tecnico-2026-11-27.text.md
language: es
---

# V3 — Resultados y evidencia

## Resumen

Las afirmaciones de resultado con contenido numérico se contrastaron con las tablas internas del documento y con los CSV reales de `Data/analisis_rentabilidad/outputs/tables/`.
El respaldo más sólido aparece en los desgloses aritméticos internos, en 50 marcas / 81 anomalías / 30 infravalorados / mediana de 21.000 USD y en la no significancia actual del modelo hedónico.
Las discrepancias se concentran en el relato final (2.014 frente a 2.029 anuncios; 44.125 frente a 43.000 km), en la depreciación de −5,43 % anual y en cifras de infraestructura y fechas no reconciliadas entre secciones.

### F-V3-001 — La conclusión declara la fase 8 no implementada mientras las secciones 34–60 documentan su ejecución

La conclusión de §12 (línea 137) afirma: «El análisis de mercado y el modelo de rentabilidad (fase 8) aún no están implementados; el producto interactivo se difiere a una especialización futura». La misma afirmación se repite en la Parte II (§12 EN, línea 266) y en §1 (línea 16). Sin embargo, §34 (líneas 1012–1058) describe la creación de `Data/analisis_rentabilidad/` con `01_ingest.py` a `05_benchmark.py`, `sql/analysis.sql` y una «Línea base real de la primera ejecución» con 972 filas ingeridas, 499 limpias y un modelo OLS; §59 (líneas 1375–1377) y §60 (línea 1385) reportan resultados finales del mismo pipeline. La tabla real `outputs/tables/modelo_resumen.txt` contiene una regresión OLS fechada el 23/11/2026. El texto sostiene simultáneamente la inexistencia y la existencia del modelo sin una declaración que separe «modelo de apoyo exploratorio» de «modelo de rentabilidad entregado».

— polarity: negative · confidence: high · related: [[#C001]], [[#C009]], [[#C010]], [[#C011]], [[#C121]]

### F-V3-002 — «Nueve marketplaces con inventario real» y «una docena» frente al desglose de §5

La conclusión de §12 (línea 133) dice: «El mercado habanero tiene nueve marketplaces con inventario real y una docena con categorías vacías o solo piezas». La evidencia citada, §5 (líneas 60–64), enumera siete marketplaces con cifra (Autocubana 667, iTENCEL 951, VentaCuba 801, Timbirichi 281, Revolico 112 enlaces de primera página, Cogetucarro 5.225 y Cubisima 155) más dos sin cifra (Apululu y Carros.com Cuba): nueve en total, por lo que el primer conteo coincide con la enumeración. El segundo no coincide: la misma línea 62 reclasifica nueve sitios con «categoría vacía» y seis «de piezas, motos o servicios», es decir 15 sitios en las dos categorías que la conclusión resume como «una docena»; los dos sitios «sin sección real» quedan fuera de esa suma. La cifra de la conclusión no se desglosa en una tabla ni en §5 ni en §12.

— polarity: negative · confidence: high · related: [[#C004]], [[#C019]], [[#C020]]

### F-V3-003 — «Mejor densidad» incluye a Chinautos Cuba con cero filas con precio

§9 (línea 108) afirma: «Mejor densidad: AGN Motors, Chinautos Cuba, Dongfeng Cuba y Finauto». La tabla «Tienda | Filas | Con precio» de §9 (líneas 94–106) registra a Chinautos Cuba con 70 filas y 0 con precio, mientras que AGN Motors tiene 45/60, Finauto 34/45 y Dongfeng Cuba 16/45. La tabla de la Parte II (líneas 223–235) repite los mismos valores. Si «densidad» se lee como densidad de precio —la única columna derivada de la tabla— Chinautos Cuba es el extremo inferior de las cuatro tiendas citadas; si se lee como volumen, la etiqueta no distingue esa dimensión de la precedente. El texto no define el criterio.

— polarity: negative · confidence: high · related: [[#C032]], [[#C033]]

### F-V3-004 — Desgloses internos aritméticamente consistentes en seis secciones

Varios desgloses citados en el documento cuadran exactamente con sus totales: las 11 filas de §9 (líneas 94–106) suman 256, igual a la cifra de la línea 92; en §15 (línea 769), 304 autos + 6.028 exclusiones = 6.332 anuncios, y 5.983 + 45 + 0 = 6.028; en §31 (línea 985), 548 autos + 9.409 exclusiones = 9.957 anuncios, y 9.316 + 93 = 9.409; en §50 (línea 1263), 369 anuncios ya presentes + 3.589 nuevos = 3.958; en §51 (línea 1275), 748 identificadores únicos − 4 anuncios excluidos = 744 autos; en §51 (línea 1277), 872 + 99 + 2 = 973 anuncios recuperados. Estas cadenas aparecen con las mismas cifras en las versiones en inglés de cada sección.

— polarity: positive · confidence: high · related: [[#C032]], [[#C033]], [[#C042]], [[#C064]], [[#C065]], [[#C163]]

### F-V3-005 — El relato final reporta 2.014 anuncios y 1.323 locales; el CSV vigente registra 2.029 y 1.338

§59 (línea 1375) afirma: «El relato ahora usa **744 autos únicos**, **2.014 anuncios limpios** (1.323 locales y 691 de importación)», cifra que repite §58 (línea 1367) tras la inserción de diez anuncios de iTENCEL y que en §51 (línea 1277) aparecía como 1.301 locales y 672 de importación. El archivo real `Data/analisis_rentabilidad/outputs/tables/kpis.csv` (generado el 23/11/2026 a las 16:17) registra `anuncios_totales,2029.0`, `anuncios_locales,1338.0` y `anuncios_importacion,691.0`; `kpis_canal.csv` desglosa 1.317 locales usados + 21 locales nuevos = 1.338 y 691 de importación. La cifra de importación coincide; el total y el canal local difieren en 15 anuncios. El documento no consigna los 2.029 ni los 1.338 en ninguna sección.

— polarity: negative · confidence: high · related: [[#C010]], [[#C066]], [[#C074]]

### F-V3-006 — Kilometraje mediano: 44.125 km en el relato frente a 43.000 km en `kpis.csv`

La misma frase de §59 (línea 1375) y de §58 (línea 1367) fija «mediana de kilometraje 44.125 km». El CSV `Data/analisis_rentabilidad/outputs/tables/kpis.csv` registra `km_medianos,43000.0`. La diferencia es de 1.125 km. Ninguna sección del documento reporta 43.000 km ni describe un recálculo del kilometraje posterior al 23/11 que explique ambas cifras; §51 (línea 1278) documenta la corrección de `parse_number()` para `80,000 km`, sin adjuntar el valor agregado resultante.

— polarity: negative · confidence: high · related: [[#C010]], [[#C067]], [[#C074]]

### F-V3-007 — Cinco cifras del relato final coinciden con los CSV reales de rentabilidad

La frase de §59 (línea 1375) «50 marcas, 100 grupos comparables y 81 anomalías» y la mediana de 21.000 USD encuentran respaldo directo en los archivos reales: `kpis.csv` registra `marcas_distintas,50.0` y `precio_mediano_usd,21000.0`; `benchmark.csv` contiene 101 filas de datos de grupos; `anomalias.csv` contiene 81 filas. La cifra de 30 infravalorados, presente en la tabla de §34 (línea 1049) y en §44 (línea 1202), coincide con las 30 filas de `infravalorados.csv`; `importacion_por_marca.csv` y `kpis_canal.csv` coinciden en los 691 anuncios de importación. La única divergencia menor de este conjunto es de una fila en `benchmark.csv` (101 frente a 100 grupos).

— polarity: positive · confidence: high · related: [[#C010]], [[#C066]], [[#C074]], [[#C156]]

### F-V3-008 — −5,43 % anual con p<0,001 convive con la retirada del coeficiente en §59–§60

§34 (línea 1052) afirma: «El modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` da una depreciación media de **−5,43 % anual** (p<0,001), con primas de +21 % para premium y −22 % para tier medio frente al desconocido». La cifra se reutiliza en §44 (línea 1202), §45 (línea 1210) y en el resumen EN de §34 (línea 1058). En sentido opuesto, §59 (línea 1377) declara que «el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra», y §60 (línea 1385) confirma la no significancia. El archivo real `outputs/tables/modelo_depreciacion.csv` registra `car_age,-0.0708,0.237` y `C(brand_tier)[T.premium],0.0662,0.9474`; el único p_valor igual a 0,0 en esa tabla corresponde a `Intercept`, no a la edad. La revisión bibliográfica independiente describe el mismo patrón de inestabilidad en especificaciones log-lineales anidadas ([[#P009]], [[#P011]]).

— polarity: negative · confidence: high · related: [[#C009]], [[#C011]], [[#C075]], [[#C156]]

### F-V3-009 — Tres tablas reales sostienen la formulación cautelosa de §59–§60

La afirmación de §60 (línea 1385) —«la corrida actual **no** sostiene una tasa de depreciación ni una prima premium significativa (p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05)»— coincide con tres archivos reales: `modelo_depreciacion.csv` y `modelo_resumen.txt` muestran el menor p_valor no intercepto en `hp` (0,1648 / 0,165), `car_age` con p = 0,237 y `C(brand_tier)[T.premium]` con p = 0,9474; `vif.csv` contiene 1,54, 1,58, 1,17, 1,13 y 1,13; `tests.csv` contiene `Kruskal-Wallis precio por tier,26.518,1e-05`. Las tres líneas de evidencia concuerdan entre sí y con el lenguaje de la conclusión, que retira la cifra en lugar de mantenerla con cautela.

— polarity: positive · confidence: high · related: [[#C011]], [[#C176]], [[#P009]], [[#P013]]

### F-V3-010 — El modelo citado como «actual» se ajusta sobre 22 observaciones, cifra ausente del relato

`outputs/tables/modelo_regresion.txt` no existe; el respaldo es `modelo_resumen.txt`, que registra «No. Observations: 22», «R-squared: 0.277», «Adj. R-squared: -0.084», «F-statistic: 0.7674» y «Prob (F-statistic): 0.623». La narrativa de §59 (líneas 1375–1377) enmarca la reformulación dentro del conjunto final de «744 autos únicos» y «2.014 anuncios limpios», y §60 (línea 1385) habla de «la corrida actual» sin declarar el tamaño de la muestra estimada. La tabla interna de §34 (línea 1047) sí declaraba «Observaciones del modelo OLS | 328» para la primera ejecución; ninguna sección registra el paso de 328 a 22 observaciones. La base empírica de la afirmación de no significancia queda así sin dimensión muestral en el texto.

— polarity: negative · confidence: high · related: [[#C009]], [[#C010]], [[#C011]], [[#C123]]

### F-V3-011 — «7 lotes de 25» no cuadra con los 119 enlaces de la prueba de §16

§16 (línea 783) describe: «Prueba con 1 página: **119 enlaces** descubiertos y procesados, 7 lotes de 25, BD principal de 6.332 a **6.334 anuncios** y de 304 a **317 autos**». La regla de commit declarada en la línea 779 es «Cada **25 anuncios procesados** [...] se hace un commit por lotes». Con 119 enlaces procesados, el número máximo de lotes completos es cuatro y el de lotes con commit es cinco; siete lotes de 25 implican al menos 151 decisiones. El texto no explica si los lotes incluyen reprocesamientos de la corrida interrumpida descrita en la línea 909.

— polarity: negative · confidence: medium · related: [[#C045]], [[#C047]], [[#C060]]

### F-V3-012 — 120 enlaces descubiertos menos 63 descartados no dan 185 candidatos descargados

§26 (línea 931) registra: «Prueba con 1 página: 120 enlaces descubiertos, 63 descartados tempranamente y 185 candidatos descargados; `autos` pasó de 323 a 326 y `revision` de 6.085 a 6.134». Los propios términos de la frase dan 57 enlaces restantes tras el descarte temprano (120 − 63), frente a los 185 candidatos declarados. El orden corregido descrito en las líneas 926–928 establece que solo se descargan enlaces con `es_auto_candidato=1`, por lo que 185 descargas no pueden proceder de esos 57 enlaces sin una fuente adicional no declarada. El resumen EN de la línea 933 repite las tres cifras sin reconciliarlas.

— polarity: negative · confidence: high · related: [[#C062]], [[#C108]], [[#C044]]

### F-V3-013 — Tres conteos distintos para el corpus del ONEI: 117 enlaces, 118 documentos, 221 archivos y 233 archivos

§53 (líneas 1309–1311) afirma: «se descargaron **todos los documentos enlazados**: 111 PDF, 7 RAR y 103 archivos Excel extraídos» y añade que «Los 117 enlaces de documento encontrados se descargaron todos; solo se omitieron CSS y favicon». Los dos tipos de documento descargados suman 118 (111 PDF + 7 RAR), no 117; con los Excel extraídos el total es 221. §56 (línea 1347), en cambio, se refiere a «los 12 anuarios del ONEI y sus 233 archivos». El inventario de E3 (§53 y §56) ya consigna ambas cifras. El documento no explica la diferencia entre 221 y 233 ni entre 117 y 118.

— polarity: negative · confidence: high · related: [[#C069]], [[#C169]], [[#C174]]

### F-V3-014 — El número de gasolineras cambia de 137 en §41 a 131 en §42 sin registro del ajuste

§41 (líneas 1150 y 1152) reporta «**Overpass/OSM devolvió 137 gasolineras en La Habana**» y la creación de `Data/mapas/gasolineras.csv` con 137 registros, cifra repetida en la línea 1152 al regenerar `mapa_ofline.html` con tres capas. §42 (línea 1173) cierra con «Estado final: **131 gasolineras, 12 estaciones de carga, 25 concesionarios (17 con coords) y 22 talleres (todos con coords)»; el inventario de figuras de E3 reproduce ambos valores. Ni §41 ni §42 consignan una depuración, fusión o exclusión de seis gasolineras que explique el tránsito de 137 a 131.

— polarity: negative · confidence: high · related: [[#C143]], [[#C145]], [[#C149]]

### F-V3-015 — La TRMI informal aparece como 920 CUP/USD en §23 y como 930 CUP/USD en §52

§23 (línea 900) describe la serie con «la TRMI pasó de 680 CUP/USD (09/07/2026) a 920 (16-17/11/2026)» y en la línea 898 fija el procedimiento: «la conversión usa `precio_USD × TRMI elTOQUE` del día del anuncio (columna `Mediana` de `Anexos/Investigacion Cambios/trmi_USD.csv`)». §52 (línea 1293), fechado tres días después, afirma: «La conversión del proyecto sigue usando la **TRMI informal** de elTOQUE (930 CUP/USD), nunca la oficial». Las dos cifras corresponden al mismo concepto en fechas próximas y el documento no registra el valor del 20/11 ni una actualización de la serie; además, una expresión describe una tasa diaria por anuncio y la otra una tasa única.

— polarity: negative · confidence: medium · related: [[#C056]], [[#C058]], [[#C068]]

### F-V3-016 — «No se eluden mecanismos anti-automatización» frente al uso declarado de stack anti-bot e impersonación TLS

§10 (línea 116) establece: «No se eluden mecanismos anti-automatización; los HTTP 403/429 se registran como limitación», y §11 (línea 127) añade para carrosw: «Registrado como limitación; no se falsificó su contenido». Otras secciones describen medidas técnicas sobre bloqueos: §37 (línea 1096) reporta «una sesión curl_cffi por hilo (`threading.local`) con impersonación Chrome», y §42 (línea 1175) declara: «**Cybo devolvió 403 con curl_cffi**, por lo que se aplicó el stack anti-bot disponible: `patchright` [...] y FlareSolverr en `http://127.0.0.1:8191/v1`». El texto no distingue entre registrar un bloqueo como limitación y desplegar un stack anti-bot tras ese bloqueo; ambas formulaciones conviven sin una delimitación explícita de la regla operativa.

— polarity: negative · confidence: medium · related: [[#C005]], [[#C006]], [[#C150]]

### F-V3-017 — Telegram MTProto se presenta como «ya integrado» y «la ruta más eficiente» sin medición y sin credenciales

§15 (línea 763) afirma: «Para obtener más datos del mercado habanero, la ruta más eficiente es Telegram MTProto (`telethon`, ya integrado): sin navegador [...] Le sigue Facebook GQL [...] más rápido que Selenium». §28 (línea 946) registra lo contrario sobre la integración: «No hay credenciales MTProto (`TELEGRAM_API_ID`/`TELEGRAM_API_HASH` vacías), así que se implementó `Auxiliares/herramientas/scraper_telegram_publico.py`, que lee la vista pública `t.me/s/<canal>`». La corrida de esa alternativa (línea 948) produjo 54 anuncios «y **ninguno con precio explícito**». El orden de eficiencia se enuncia sin tiempos de ejecución, tasas de éxito ni comparación pareada entre las tres vías; E1 ya consigna la ausencia de medición en las notas de C007.

— polarity: negative · confidence: high · related: [[#C007]], [[#C092]], [[#C093]], [[#C112]], [[#C113]]

### F-V3-018 — §53 anuncia que el capítulo 13 incorporará parque y matriculaciones; §56 confirma que no existen

§53 (línea 1313) presenta el capítulo 13 como «la serie más útil [...] que permite incorporar parque automotor, matriculaciones y accidentes con series oficiales 2014–2025, hoy ausentes del análisis». §56 (línea 1347), tras revisar los 12 anuarios, corrige: «**No hay series de parque automotor ni de matriculaciones**, por lo que esa laguna signalada en `NECESIDADES.md` no se resuelve con los anuarios; la corrección quedó registrada». El inventario de E3 clasifica ambas series como artefactos ausentes. La expectativa de §53 permanece en el documento junto a su corrección, sin que la primera se marque como superada dentro de la propia sección.

— polarity: negative · confidence: high · related: [[#C012]], [[#C069]], [[#C072]]

### F-V3-019 — Mediana de 22.000 USD en el análisis inicial frente a 21.000 USD en el relato final

§22 (línea 890) reporta «Precio mediano **22.000 USD**, media 24.416,59 USD, IQR 11.375–35.000 USD» sobre 323 autos y 248 precios USD válidos. El cierre de §51 (línea 1277), §58 (línea 1367) y §59 (línea 1375) fija la mediana local en 21.000 USD sobre el conjunto regenerado, valor que coincide con `precio_mediano_usd,21000.0` y con `mediana_usd` de `local,usado` en `kpis_canal.csv`. La diferencia de 1.000 USD entre ambas etapas no se comenta en el texto; §51 (línea 1276) documenta la regeneración, pero no presenta una tabla de transición entre los 323 autos iniciales y los 744 finales.

— polarity: neutral · confidence: high · related: [[#C054]], [[#C010]], [[#C075]]

### F-V3-020 — Salvedades de procedencia y proyección formuladas con lenguaje no medido

La tabla de §18 (línea 822) clasifica los precios de marketplaces como «precios **pedidos**, no transaccionados», y la conclusión de la línea 827 añade que las fuentes oficiales sirven de «**contexto y validación**» sin sustituir a la señal de precio. §23 (línea 899) declara explícitamente el supuesto de anuncio activo y que «no se comprueba disponibilidad en tiempo real», y §19 (línea 851) enumera los límites. En la misma línea, §63 (línea 1413) rotula la retención como «**inferencia de diseño, no medición**» antes de dar las proyecciones. El léxico de estas cuatro afirmaciones no excede el tipo de evidencia disponible.

— polarity: positive · confidence: high · related: [[#C008]], [[#C013]], [[#C057]], [[#C097]], [[#P021]]

### F-V3-021 — «99,3 %» y mediana de un día en 189 autos sin tabla ni archivo citado

§15 (línea 771) afirma: «El 99,3 % de los anuncios tiene `updated_on_by_user` en los últimos 7 días (mediana 1 día en los 189 autos), lo que indica renovación frecuente por parte del vendedor». La afirmación se apoya en la misma línea en un caso empírico individual (un anuncio de 2024-12-17 en HTTP 200) y en las Condiciones de Uso de Revolico, pero no cita archivo, consulta SQL ni tabla para el 99,3 % ni para el subconjunto de 189 autos. El inventario de E3 no registra ningún artefacto de frescor de anuncios, y E1 consigna la ausencia de evidencia interna para C041. El denominador de 189 autos tampoco aparece en los recuentos de autos de §15 (304), §16 (317), §22 (323), §51 (744) ni §59 (744).

— polarity: negative · confidence: medium · related: [[#C040]], [[#C041]]

### F-V3-022 — Conteos de marketplaces de §5 y §39 difieren para las mismas tiendas sin reconciliación

§5 (línea 62) registra «Autocubana (667 vehículos), iTENCEL (951), VentaCuba (801 carros/camionetas), Timbirichi (281 carros) [...] Cogetucarro (5.225 anuncios)». §39 (línea 1123), fechado al día siguiente, reporta «Cogetucarro de 200 → **5.008**, Autocubana y Timbirichi a 40 páginas [...] Autocubana pasó de 400 a **566** y Timbirichi de 110 a **170**, totalizando **2.121 anuncios**». §58 (línea 1367) eleva iTENCEL de 951 a 961. Los valores para Cogetucarro (5.225 frente a 5.008), Autocubana (667 frente a 566) y Timbirichi (281 frente a 170) se refieren a las mismas tiendas y no incluyen una nota que identifique cuál de los dos recuentos es el vigente ni qué cambió entre uno y otro. Las unidades también difieren: la línea 62 mezcla vehículos, anuncios y enlaces de primera página, y la línea 1123 usa «anuncios».

— polarity: negative · confidence: high · related: [[#C019]], [[#C074]], [[#C137]]

### F-V3-023 — La estimación de tráfico de §65 se presenta como estimación, no como medición

§65 (línea 1429) cierra con «Estimación de red: **5–10 MB/mes** si no hay cambios y **50–90 MB/mes** con novedades». El resumen EN de la línea 1431 mantiene el calificativo «estimated». La frase no adjunta mediciones de transferencia ni contadores de `precio-*`, y el propio texto las presenta como proyección condicionada a la existencia de novedades. El alcance de la afirmación queda limitado por el léxico empleado.

— polarity: positive · confidence: high · related: [[#C077]], [[#C184]]

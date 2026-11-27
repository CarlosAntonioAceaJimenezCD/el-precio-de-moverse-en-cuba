---
type: audit-artifact
phase: v7-writing
slug: informe-tecnico-2026-11-27
generated_at: 2026-11-27T05:45:00Z
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27/informe-tecnico-2026-11-27.text.md
language: es
---

# V7 — Writing and AI patterns (findings)

Resumen (tres líneas):
- El corpus es un informe técnico bilingüe de 1.462 líneas: dos partes paralelas (§1–12), 55 secciones fechadas (§14–68) y un registro de altas generado por script (§13); la prosa se apoya en cifras, rutas y enumeraciones antes que en metadiscurso.
- Los patrones de mayor frecuencia son estructurales —paralelismo ES/EN, apertura «Se + verbo» (51 líneas), bloques «EN.» con participio inicial (53), metaconceptos «análisis» (37) y «marco» (20)—; los ítems estrictos de Romero §13 aparecen en densidad baja y se concentran en dos bloques.
- La densidad se califica como alta en §17–21 y §59–63 y como media en el resto de la prosa; el texto cacheado no contiene declaración de uso de IA, de modo que el contraste queda consignado para V9.

Alcance. Las cifras se obtuvieron por conteo sobre el texto cacheado; «palabra» incluye identificadores y rutas. El §13 (L270–748) se excluye del denominador de densidades por ser un registro automático de tabla, y se inventaría en F-V7-016. Winston, Pinker y Romero §13 se emplean como rótulos de las róbricas aplicadas. El artefacto se limita a describir patrones y densidades.

### F-V7-001 — Paralelismo ES/EN en 54 de 55 secciones y en las Partes I/II

El encabezado declara «Idioma / Language: español e inglés / Spanish and English» (L8). Las Partes I y II repiten íntegramente §1–12 (L14–137 y L143–268). En el bloque §14–68, 54 de 55 secciones llevan un párrafo inglés: 53 con la etiqueta «**EN.**» (§15–39 y §41–68) y §14 con un párrafo inglés sin etiqueta (L754); §40 carece de paralelo. La duplicación opera a nivel de sección, no como glosa puntual: en §18, la «**Conclusión:**» de L827 se enuncia de nuevo en L829, y en §20 el cierre de L873 reitera los nueve bloques de L857–L867. Bajo Winston (structure-of-prose), esta es la característica estructural dominante del documento.

— polarity: neutral · confidence: high · related: [[#F-V7-003]]

### F-V7-002 — Apertura «Se + verbo» en 51 líneas y primera persona aislada

Cincuenta y una líneas comienzan con «Se» seguido de verbo en pretérito, y la construcción «se + verbo» aparece 133 veces en total. La distribución cubre casi todo el rango narrativo: §5 (L60, L62, L64), §29 (L956), §30 (L973, L975), §50 (L1259, L1261, L1263), §55 (L1333, L1335, L1337, L1339), §59 (L1375, L1377) y §66 (L1437, L1439). La voz activa en primera persona se restringe a cuatro pasajes: §34 «Creé `Data/analisis_rentabilidad/`» (L1014) e «Instalé además `statsmodels 0.15`» (L1035), §35 «Descargué tres APKs» (L1064) y §38 «Creé `Auxiliares/herramientas/reporte_progreso.py`» (L1108). Los paralelos ingleses emplean pasiva («was created», «were cloned», «was designed») o participio inicial. Winston sitúa la oración de apertura como oración temática: aquí esa función la cumple de modo regular la construcción impersonal.

— polarity: neutral · confidence: high · related: [[#F-V7-003]]

### F-V7-003 — Bloques «EN.» con participio inicial y función de cierre-resumen (53)

De los 53 bloques etiquetados «**EN.**», la mayoría se abre con un participio pasado seguido de objeto y complemento: «Built a scalable analysis skeleton» (L1058), «Rewrote the findings section» (L1212), «Built a MkDocs Material site» (L1397), «Activated five unattended timers» (L1431), «Audited 15 web sources» (L1341), «Split the 811 MiB Revolico database» (L1327). Dos variantes usan sintagma nominal: «Initial descriptive analysis: 323 cars, 248 valid USD prices» (L892) y «Map libraries installed, systemd auto-restart added» (L920). Cada bloque reemite en forma condensada el resultado del párrafo español precedente: es una glosa sistemática posterior a la exposición, con la regularidad de Romero §13 Don't 8 a escala de sección. Su carácter es declarado por el encabezado bilingüe (L8), por lo que se registra como patrón estructural y no como una ocurrencia aislada.

— polarity: neutral · confidence: high · related: [[#F-V7-001]], [[#F-V7-009]]

### F-V7-004 — Metaconceptos «análisis» (37) y «marco» (20) concentrados en §17–21

El recuento global sobre el texto cacheado da «análisis» 37, «estructura» 22, «marco» 20, «procesamiento» 6, «implement-» 6, «señal» 5, «arquitectura» 5, «proceso» 2, «evaluación» 1 y «consideración» 0. La concentración más alta está en §17–21 (1.671 palabras): «análisis» 14 y «marco» 9, unas 13,8 ocurrencias por 1.000 palabras. Las róbricas nominales se encadenan: «Marco general (8 pasos, derivado de los trabajos revisados)» (L833), «**Conclusión:**» (L827), «El marco operativo completo consta de nueve bloques» (L857), «**Marco teórico:**» (L861), «**Marco normativo:**» (L862), «**Arquitectura de datos:**» (L863). En §10 y §12, «marco» reaparece en «norma marco» (L56), «marco legal» (L112) y «marco regulatorio» (L134). Bajo Pinker (metaconcepts and zombie nouns), estos sustantivos abstractionan la acción que las cifras vecinas concretan. Romero §13 Don't 4, en su forma estricta («landscapes/paradigms/ecosystems/transformations»), no registra ocurrencias: no aparecen «ecosistema», «paradigma» ni «transformación».

— polarity: neutral · confidence: high · related: [[#F-V7-005]], [[#F-V7-010]]

### F-V7-005 — Siglas no desplegadas en primera aparición (Pinker, curse of knowledge)

Varios términos técnicos se introducen ya abreviados y no se despliegan en el documento: «TRMI» (L898, L1293, L1385), «VIF» (L1023, L1385), «OLS» (L1052, L1058), «IQR» (L890, L892), «MLC» (L800, L846, L860), «GQL» (L763), «MTProto» (L763, L946), «WAHA» (L763, L765), «SHAP» (L801, L865), «EDA» (L801), «vqd» (L124) y «NFC» (L1357). La lista de organismos de L64 —«MINCEX, MINCIN, MITRANS, CEMA, MFP, ONAT, Aduana General, BCC, MININT, MINJUS, MEP, MINREX y MINSAP»— sola no expande ninguna sigla; «BCC (Banco Central de Cuba)» aparece recién en L816 y L1293, y «DDG» en L124 depende de «DuckDuckGo» en L60. Pinker clasifica este patrón como curse of knowledge: el texto supone el vocabulario ya conocido en el primer uso.

— polarity: negative · confidence: high · related: [[#F-V7-004]]

### F-V7-006 — Negaciones de salvaguarda «no se…/sin…» — 15 instancias

El texto registra 151 ocurrencias de «no» y «sin», de las cuales un subconjunto se reitera como declaración de lo que no se hizo: «No se eluden mecanismos anti-automatización» (L116), «no se falsificó su contenido» (L127), «no se descarta información» (L783), «sin escribir nunca `autos`/`revision`» (L924), «no hay claves estructuradas» (L907), «no hay descarga de anuncios, ni clasificación definitiva, ni inserción» (L994), «LFS no lo sustituye» (L975), «no se modificó `revolico.sqlite`» (L1263), «sin borrar archivos. Ninguna modificó las bases fuente» (L1273), «no se hizo `pull` para no sobrescribir trabajo» (L1335), «sin modificar las bases» (L1357), «las filas existentes se migraron sin borrarse» (L1403), «sin `git push`» (L1437) y «Las leyes y las herramientas de scraping **no se borraron**» (L1447). En la mayoría hay distinción metodológica efectiva, de modo que Romero §13 Don't 2 («not just X, but Y» sin trabajo para la negación) cuenta 0–2 instancias: las más cercanas son «La app **no usa una API privada**: hace scraping del canal público» (L1066) y «es **inferencia de diseño, no medición**» (L1413). La negación funciona aquí principalmente como constancia de límites, no como énfasis retórico.

— polarity: neutral · confidence: high · related: [[#C005]], [[#C008]]

### F-V7-007 — Romero §13 Don't 3 — triadas con cola larga: 2–3 instancias

Se identifican dos o tres construcciones de tres elementos con tercer término marcadamente más largo o abstracto: «sin nombres, teléfonos ni información personal de anunciantes» (L117); «values, concerns and constraints (budget, reliability, fuel use, maintenance, resale value, spare-part availability, etc.)» (L145); «sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`» (L763). Un caso límite es «requiere dedup, verificación y sesgo declarado» (L822), donde la cola no es sustancialmente más larga, y la enumeración de siete métricas de L1375 —«**744 autos únicos**», «**2.014 anuncios limpios**», «mediana local de **21.000 USD**», «kilometraje mediano de **44.125 km**», «50 marcas, 100 grupos comparables y 81 anomalías»— es una lista de resultados, no una triada. La densidad del patrón es baja en relación con el volumen total de prosa.

— polarity: neutral · confidence: medium · related: [[#F-V7-008]]

### F-V7-008 — Romero §13 Don't 5 — adjetivos valorativos sin ancla en §52 y §63

Los equivalentes de «significant/important/considerable/notable/substantial» como adjetivos sueltos no aparecen: «importante», «notable», «considerable» y «sustancial» registran 0 ocurrencias, y «significativ-» 2 (L1052 y L1385), ambas con ancla estadística explícita («p<0,001»; «p mínimo 0,165»). Los modificadores no numéricos se concentran en dos zonas: §52 «Las cinco más valiosas son» (L1291) y §41 «Hallazgo relevante:» (L1156), seguidos de datos concretos; y §63 «El contenido es sólido, pero antes de la revisión tenía fricción inicial (metadatos antes de la promesa), un H2 genérico, el dato fuerte enterrado y ninguna llamada a la acción» (L1411), con cuatro adjetivos valorativos seguidos. Se suman «con honestidad» (L1377), «a statistically honest depreciation narrative» (L1379), «antiguo e inservible» (L1447) y «bibliotecas quizá innecesarias» (L1455).

— polarity: neutral · confidence: high · related: [[#F-V7-014]]

### F-V7-009 — Romero §13 Don't 8 — reescrituras descritas, no mostradas (§43–47, §59)

Varias secciones informan de una reescritura y exponen su resultado como enunciado, sin incorporar el texto reescrito: «Se transformó la sección **Lo que encontramos** de una tabla de datos en una narrativa de hallazgos» (L1210), con cierre explicitado —«El cierre deja la idea central: un mercado pequeño pero con estructura suficiente para dejar de improvisar»—; «Se transformó **La curva de valor** en una narrativa sobre el envejecimiento desigual del parque» y «la idea de la marca como "seguro de valor"» (L1226); «Se añadió una apertura que hace explícita la división del mercado en dos capas» (L1218). En §59, «los diez anuncios nuevos de iTENCEL entraron en la historia sin convertirla en una explicación técnica» (L1375) y el apéndice «solo deja referencias discretas entre paréntesis» (L1377). §63 califica las intervenciones como «correcciones quirúrgicas» (L1411). El inventario de artefactos consigna que las figuras se nombran pero no se incrustan en el texto cacheado, de modo que la conclusión se da antes que la evidencia mostrada.

— polarity: neutral · confidence: medium · related: [[#C013]], [[#F-V7-001]], [[#F-V7-003]]

### F-V7-010 — Anclaje concreto: cifras, rutas e IDs en cada sección (Pinker)

El síntoma lack of concrete examples no se observa: las definiciones van seguidas de instancias y las afirmaciones de resultados llevan unidad y magnitud. §7 define «útil = primera aparición de un trabajo investigativo automotriz» (L76) y lo aplica en la tabla de L78–82; §9 desglosa 11 tiendas con filas y precios (L94–106); §51 identifica cuatro anuncios por ID (L1275) y enumera cinco mejoras con rutas y recuentos (L1275–L1279); §58 nombra los diez anuncios nuevos de iTENCEL (L1365); §48 lista marcas premium y no premium (L1236–L1237); §41 registra 137 gasolineras, 12 estaciones de carga y 18 observaciones fechadas (L1150–L1154). Esta densidad de anclajes es la contrapartida de los metaconceptos de F-V7-004.

— polarity: positive · confidence: high · related: [[#C010]], [[#F-V7-004]]

### F-V7-011 — Winston: títulos instructivos y fechados; cuatro excepciones genéricas

Los 55 encabezados numerados de §14–68 llevan año entre paréntesis y un nombre que designa la operación: «Sincronización automática de Revolico» (§14, L750), «Esqueleto de análisis de rentabilidad inspirado en Egyptian-Used-Cars» (§34, L1012), «Definición de marcas premium y no premium» (§48, L1232), «Automatización operativa y coste de red» (§65, L1427). Cuatro títulos permanecen en un nivel genérico: «Continuación del scrapeo y presentación narrativa» (§39, L1121), «Mejoras del proyecto» (§51, L1271), «Ampliación de fuentes de datos» (§52, L1287) y «Peso en GitHub y mapa de espacio» (§68, L1453). Bajo Winston (section titles: instructive vs vacuous), la proporción de títulos instructivos es alta.

— polarity: positive · confidence: high · related: []

### F-V7-012 — Winston: listas y tablas en función enumerativa, no sustitutiva de prosa

El documento emplea listas para enumeraciones, requerimientos y alternativas: «Requerimientos derivados» con siete ítems (L806), «Marco general (8 pasos)» (L835–L842), los nueve bloques del marco analítico (L859–L867), las cinco mejoras de §51 (L1275–L1279) y las cinco fuentes más valiosas de §52 (L1293–L1297). Las tablas —14 sin numerar según el inventario de artefactos— sostienen recuentos por fase, búsqueda, tienda, fuente y problema (L24–34, L78–82, L94–106, L122–129, L812–825). No se detecta una lista que reemplace un argumento continuo; el movimiento inverso se describe en §45, donde una tabla se convierte en narrativa (L1210).

— polarity: neutral · confidence: high · related: [[#F-V7-010]]

### F-V7-013 — Pinker: 0 instancias de metadiscurso y de professional narcissism

No aparecen las fórmulas «this section discusses», «we will see that» ni «as discussed above», y tampoco «research in recent years» o «the field has shown». La señalización interna se hace con etiquetas nominales en negrita —«**Requerimientos derivados:**» (L806), «**Conclusión:**» (L827), «**Lo que ya existe:**» (L869), «**Lo que falta por conseguir:**» (L871), «**Advertencia:**» (L977), «**Hallazgo relevante:**» (L1156), «**Hallazgo normativo crítico:**» (L1299)— y con remisiones punctuales: «El marco detallado de la sección 20 se mantiene» (L882), «El detalle y la priorización están en `NECESIDADES.md`» (L1056), «El detalle está en `Data/auditoria-fuentes-2026-11-23.md`» (L1333). Bajo Pinker, el metadiscurso y el professional narcissism figuran en densidad nula.

— polarity: neutral · confidence: high · related: []

### F-V7-014 — Pinker: hedging-as-tic casi ausente — «quizá» 1, «aproximad-» 1

La cuenta de atenuadores es «quizá» 1 —«bibliotecas quizá innecesarias (66 MB de DuckDB)» (L1455)—, «aproximad-» 1 —«marcadas como aproximadas al centro de La Habana» (L1175)— y 0 para «relativamente», «somewhat», «perhaps» y «presumably». Las expresiones «se asume que» (L899, L917) y «supuesto» (L917, L921) funcionan como supuestos metodológicos etiquetados: «se asume que son comprables; no se comprueba disponibilidad en tiempo real» (L899) y «se asume que todo el catálogo está disponible salvo que la página indique lo contrario» (L917). «de modo que las tablas y figuras puedan insertarse sin romper la narrativa» (L1377) declara una intención de diseño. La densidad de hedging-as-tic es baja, aproximadamente 0,7 por 1.000 palabras de prosa.

— polarity: neutral · confidence: high · related: [[#F-V7-008]]

### F-V7-015 — Ritmo: cadenas con punto y coma; baja uniformidad de longitud

Varios párrafos se resuelven en una sola oración larga con cadenas de punto y coma: §4 (L56), §5 (L62), §15 «Para obtener más datos del mercado habanero, la ruta más eficiente es Telegram MTProto» (L763), §17 (L806) y §34 (L1052). No se detectan secuencias de cuatro o más oraciones consecutivas de 18–25 palabras: el ritmo alterna esas frases densas con ítems de lista de pocas palabras (L94–106, L1275–L1279) y con los bloques «EN.» condensados. La uniformidad de longitud se califica como baja.

— polarity: neutral · confidence: medium · related: [[#F-V7-003]]

### F-V7-016 — §13: 473 líneas de registro generado por `actualizar_informe.py`

El §13 se presenta como «Registro automático de todo lo que se añade a la carpeta del proyecto. El script `Auxiliares/herramientas/actualizar_informe.py` añade filas debajo del marcador y regenera el PDF» (L272). Las líneas L276–L748 son filas de tabla con valores repetidos: «Añadido al proyecto; pendiente de descripción / Added; description pending», «Carpeta añadida al proyecto / Folder added to the project» y «Actualizado / Updated»; L291 consigna «175 entradas adicionales no listadas / omitted». La secuencia incluye instantáneas sucesivas del mismo archivo con tamaños decrecientes (por ejemplo, `INFORME_TECNICO.md` en L284, L289, L504, L519, L526 y L562). Se trata de una tabla generada por script y se mantiene fuera del denominador de densidades de prosa.

— polarity: neutral · confidence: high · related: []

## AI-pattern density by section

Valores aproximados sobre el texto cacheado. «Metaconcepto/1k» agrega `análisis`, `marco`, `estructura`, `procesamiento`, `proceso`, `señal`, `arquitectura`, `evaluación` e `implement-` en la acepción de Pinker. «Openers» cuenta fórmulas de apertura («Se + verbo», participio en los bloques «EN.», pasiva inglesa); no aparecen «In recent years…» ni «This study demonstrates that…».

| Section | Density | Notes |
|---|---|---|
| §1–3 — Objetivo, estados, carpetas (L14–53) | low | 0–1 hedges/1k; «análisis» 2 en §1; 0 triadas; openers «Se + verbo»; sin bloque EN |
| §4–9 — Fases 1–6 (L54–108) | low | ≈0,5 metaconceptos/1k; 0 triadas largas; 15 openers «Se…»; tablas y listas; 0 atenuadores |
| §10–12 — Marco legal, problemas, conclusiones (L110–137) | medium | «marco» 3; 7 «no/sin»; triada en L117; cierre numerado en L133–137 |
| Parte II §1–12 — Objective…Conclusions (L143–268) | low | voz pasiva y paralelismo con la Parte I; 0 hedges; 0 triadas largas salvo L145 |
| §13 — Registro de altas (L270–748) | n/a | tabla generada por script; 473 líneas; excluida del denominador (F-V7-016) |
| §14–33 — Sincronización, eficiencia, colas, marcos (L750–1008) | medium | 19 openers «Se…»; 18 bloques EN de participio; 13 «no/sin» en §18 (mayoría en tabla) |
| §17–21 — Guía, auditoría y marcos analíticos (L787–884) | high | 14 «análisis» + 9 «marco» en 1.671 palabras (≈13,8/1k); escaleras de 8 y 9 pasos; triada en L848; 5 glosas EN |
| §34–48 — Rentabilidad, APK, mapas, storytelling (L1012–1242) | medium | 4 pasajes en primera persona; 15 bloques EN; d8 en §43–47; «seguro de valor» entre comillas (L1226); 0 hedges |
| §49–58 — Repos, mejoras, fuentes, ONEI, chunks (L1245–1369) | medium | ≈25 «no/sin»; d5 en L1156 y L1291; ≈25 openers «Se…»; densidad alta de cifras y rutas |
| §59–63 — Storytelling final, modelos, sitio, retención (L1373–1415) | high | d8 en §59 y §63; d5 con 4 adjetivos en L1411 y «honestidad» en L1377/1379; «inferencia de diseño, no medición» (L1413) |
| §64–68 — Automatización y espacio (L1419–1457) | low–medium | «quizá» en L1455; «no se borraron» en L1447; 5 bloques EN de participio; 0 triadas |

## Hook para V9

Dos bloques registran `ai-pattern-density: high`: §17–21 (metaconceptos ≈13,8/1k, escaleras de pasos, glosas «EN.» sistemáticas) y §59–63 (adjetivos valorativos y reescrituras descritas, Romero §13 Don't 5 y Don't 8). El texto cacheado no incluye una sección de declaración de uso de IA; el pasaje más cercano es §55 (L1337), donde se consigna que las skills `technical-writing`, `readme-writing`, `diataxis-docs`, `marketing-copy` y `pptx` «quedaron instaladas y activas para redacción y presentación». Ambos extremos quedan consignados para el contraste de V9.

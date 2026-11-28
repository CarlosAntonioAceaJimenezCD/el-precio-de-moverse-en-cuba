---
type: audit-artifact
phase: v7-writing
slug: informe-tecnico-2026-11-27-iter3
generated_at: 2026-11-28T01:22:56-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter3/informe-tecnico-2026-11-27-iter3.text.md
language: es
level: master
---

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

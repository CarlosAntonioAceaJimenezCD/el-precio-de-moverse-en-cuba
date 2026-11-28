---
type: audit-artifact
phase: v7-writing
slug: informe-tecnico-2026-11-28-iter4
generated_at: 2026-11-28T03:15:17-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-28-iter4/informe-tecnico-2026-11-28-iter4.text.md
language: es
level: master
---

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

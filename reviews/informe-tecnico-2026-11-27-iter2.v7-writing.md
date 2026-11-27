---
type: audit-artifact
phase: v7-writing
slug: informe-tecnico-2026-11-27-iter2
generated_at: 2026-11-27T17:40:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter2/informe-tecnico-2026-11-27-iter2.text.md
language: es
level: master
---

# V7 — Writing and AI patterns (findings)

Resumen (tres líneas):
- La iteración 2 añade 520 palabras y 22 líneas sobre la iteración 1 (28.586 → 29.106 palabras); los patrones estructurales (paralelismo ES/EN, apertura «Se + verbo», bloques «EN.», registro generado del §13) permanecen sin cambio y la densidad global se mantiene baja.
- Las únicas subidas medibles son metaconceptos (197 → 205; 6,89 → 7,04 por 1.000 palabras) y adjetivos valorativos sin ancla (4 → 7; 0,14 → 0,24 por 1.000 palabras), todas ellas introducidas por la nueva §69; hedging (1), openers de fórmula (0), «not just X, but Y» (0) y triadas largas (2–3) no varían.
- La §69 nombra fases como actividades genéricas y enuncia un principio de contraste contra archivos, pero no nombra herramientas generativas (solo el genérico y la skill `review`), no enumera fases por identificador ni las del criterio V9, y no designa un protocolo de supervisión con nombre; densidad de §69 = media, sin disparar el hook de densidad alta.

Alcance y método. Conteo directo sobre los textos cacheados de la iteración 1 (`informe-tecnico-2026-11-27.text.md`, 1.462 líneas) y de la iteración 2 (`informe-tecnico-2026-11-27-iter2.text.md`, 1.484 líneas); «palabra» incluye identificadores, rutas y tablas. El §13 (registro automático) queda fuera del denominador de densidades de prosa, como en el informe V7 de la iteración 1. El diff entre ambas versiones consta de siete pasajes editados, las secciones nuevas §69–§70 y el cambio de fecha de cierre; por eso la comparación se formula como «sin cambio» salvo donde se documenta lo contrario. Winston, Pinker y Romero §13 se citan como rótulos de las róbricas aplicadas; el artefacto describe patrones y densidades, sin emitir juicio de autoría.

### F-V7-001 — Diff acotado: los patrones estructurales de la iteración 1 pasan intactos a la iteración 2

La comparación línea por línea muestra siete reescrituras puntuales —nota de actualización en §2 (L38–L39) y su paralelo inglés (L169–L170), conclusión 5 (L139), aclaración de TRMI (L902), revisión de la depreciación (L1206), conversión (L1297) y cifras del relato (L1379–L1381)— más la inserción de §69–§70 (L1465–L1482) y el cambio de «Última actualización» a 27/11/2026 (L1484). No se modifica ninguno de los rasgos que el V7 de la iteración 1 inventarió como dominantes: el paralelismo ES/EN de §1–12 y de 54 de 55 secciones fechadas, la apertura «Se + verbo», los bloques «**EN.**» de participio inicial ni las 473 líneas de tabla generada del §13. Bajo Winston (structure-of-prose), la estructura de la prosa es la misma; el cambio es de contenido y de una sección nueva, no de ritmo ni de organización.

— polarity: neutral · confidence: high · related: [[#F-V7-005]], [[#F-V7-008]]

### F-V7-002 — §69: herramientas genéricas, fases declaradas como actividades, supervisión enunciada como principio

La sección nueva «Declaración de uso de inteligencia artificial / AI-use declaration» (§69, L1467–L1471) dice en ES: «Las herramientas de inteligencia artificial se utilizaron como apoyo para la redacción, la edición quirúrgica de la narrativa, la revisión bibliográfica asistida y la auditoría sistemática del propio informe» (L1469); el bloque EN reproduce las mismas cuatro actividades (L1471). **Herramientas:** el único nombre propio es `review` —«la skill `review` de MatCom» (L1469)—, que designa el procedimiento de auditoría, no una herramienta generativa; no aparecen nombres de modelos ni de asistentes en L1467–L1471. **Fases:** sí se nombran cuatro actividades (redacción, edición, revisión bibliográfica, auditoría), pero como sustantivos comunes y en prosa corrida: no hay identificadores de fase, ni enumeración, ni las fases que el criterio `V9.ai_use_declaration.master` pide (research, drafting, code generation, translation); el único guiño cuantitativo es «los trece artefactos de fase» (L1469), un conteo sin lista. **Protocolo de supervisión:** aparece como principio —«ninguna afirmación empírica se originó en una salida de IA sin contraste contra los archivos» (L1469) / «no empirical claim was taken from an AI output without verification against the files» (L1471)—, acompañado de procedencia («provienen de los datos y del código versionados en este repositorio») y de huella de auditoría (`reviews/informe-tecnico-2026-11-27.{md,forensic.md}`). No se designa un protocolo con nombre ni se especifican sus pasos. Descriptivamente: fases y supervisión están presentes en forma genérica; herramientas, solo de modo implícito.

— polarity: neutral · confidence: high · related: [[#F-V9-001]], [[#F-V9-002]], [[#F-V9-003]]

### F-V7-003 — Romero §13 Don't 3 en §69: dos enumeraciones con cola creciente

La primera oración de §69 encadena cuatro miembros de longitud creciente: «la redacción, la edición quirúrgica de la narrativa, la revisión bibliográfica asistida y la auditoría sistemática del propio informe» (L1469); el cuarto es el más largo y el más abstracto. La segunda oración abre con otra serie de tres —«Las cifras, los modelos estadísticos y las decisiones de diseño» (L1469)— cuyo tercer término es el de mayor abstracción, y el bloque EN duplica ambas series (L1471). Fuera de §69 el recuento se mantiene en las 2–3 instancias ya registradas en la iteración 1 (L117, L145, L763 en aquella numeración; L118, L147 y L765 en esta). En un bloque de 520 palabras, dos tetradas/triadas de cola larga equivalen a una densidad media del patrón, concentrada íntegramente en la declaración nueva.

— polarity: neutral · confidence: high · related: [[#F-V7-004]]

### F-V7-004 — Romero §13 Don't 5: los tres adjetivos sin ancla nuevos están todos en §69

El recuento global de equivalentes de «significant/important/considerable/notable/substantial» y modificadores afines pasa de 4 (iteración 1) a 7 (iteración 2). Los tres nuevos son «edición **quirúrgica** de la narrativa», «revisión bibliográfica **asistida**» y «auditoría **sistemática** del propio informe» (L1469), repetidos en la versión EN (L1471); ninguno lleva ancla numérica. Los cuatro preexistentes sí la llevan o van seguidos de dato concreto: «pendiente anual significativa» aparece con p mínimo 0,165 (L1389), «correcciones quirúrgicas» con una lista de cuatro cambios (L1415), «significativa» con p < 0,001 (L1206) y «quizá innecesarias» con 66 MB (L1459). La subida de densidad (0,14 → 0,24 por 1.000 palabras) es, por tanto, un efecto local de §69 y no un cambio de hábito en el resto del informe.

— polarity: neutral · confidence: high · related: [[#F-V7-003]], [[#F-V7-005]]

### F-V7-005 — Metaconceptos: 197 → 205, con el incremento localizado en §69–§70

Bajo Pinker (metaconcepts and zombie nouns), la suma de `análisis`, `proceso`, `evaluación`, `consideración`, `implementación`, `auditoría`, `herramientas`, `decisiones`, `resultados` y afines pasa de 197 a 205 ocurrencias (6,89 → 7,04 por 1.000 palabras; +0,15). El incremento se reparte entre §69 —«herramientas», «apoyo», «edición», «revisión», «auditoría», «cifras», «modelos», «decisiones», «afirmación», «salida», «resultados», «artefactos» (L1469, L1471)— y §70 —«referencias», «verificación», «fuentes», «auditoría» (L1477, L1479)—. Las dos zonas que el V7 anterior calificó como densidad alta, §17–21 (≈13,8 metaconceptos/1.000 palabras) y §59–63, no cambian. La lectura descriptiva es de estabilidad global con un repunte local en las secciones declarativas nuevas.

— polarity: neutral · confidence: high · related: [[#F-V7-001]], [[#F-V7-004]]

### F-V7-006 — Las reescrituras de la iteración 2 añaden anclaje concreto, no atenuadores

Las siete pasajes editados fuera de §69–§70 refuerzan el síntoma inverso al de Pinker (lack of concrete examples): «el pipeline de `Data/analisis_rentabilidad/` usa la TRMI fija de 930 CUP/USD del 18/11/2026 (`config.py`)» (L902); «la depreciación de −5,43 % anual obtenida en la primera corrida (p < 0,001; §34), cifra que la corrida vigente ya no sostiene» (L1206); «28 observaciones completas» de «981 candidatas (R² = 0,277; p del F = 0,411)» (L1381); «772 autos únicos», «2.029 anuncios limpios» y «corrida vigente del 27/11/2026» (L1379); «están implementados en `Data/analisis_rentabilidad/` y se regeneran de forma automática» (L139). La expresión «ya no sostiene» funciona como corrección con fecha y cifra, no como hedging-as-tic; el único atenuador del documento sigue siendo «bibliotecas quizá innecesarias» (L1459). Densidad de hedging en la iteración 2: 1 instancia, 0,03 por 1.000 palabras, idéntica a la iteración 1.

— polarity: positive · confidence: high · related: [[#F-V7-010]], [[#F-V7-005]]

### F-V7-007 — §70: título instructivo, lista enumerativa y procedencia verificable

La sección «Referencias verificadas / Verified references» (L1475–L1481) abre con la serie «Akerlof (1970), *The Market for "Lemons"* (Crossref/OpenAlex); UK Department for Transport / DVLA … (GOV.UK); ANFAC … (sitio oficial); AEADE … (sitio oficial)» (L1477) y cierra con `(metadata incomplete)` para el resto y `Data/referencias.md` como convención numerada de 38 referencias. Bajo Winston, el título es instructivo y la lista cumple una función enumerativa (no sustituye un argumento); bajo Pinker, cada fuente lleva ancla externa concreta. No hay metadiscurso («this section discusses»), professional narcissism («research in recent years»), openers de fórmula ni shudder quotes fuera del título citado de Akerlof, que es un título real. Densidad: baja.

— polarity: neutral · confidence: high · related: [[#F-V7-011]], [[#F-V7-012]]

### F-V7-008 — Romero §13 Don't 2, Don't 4, Don't 8 y Pinker (metadiscurso): continuidad sin cambios

«No solo… sino» y «not just… but» registran 0 instancias en ambas iteraciones; las negaciones de salvaguarda («no se eluden mecanismos anti-automatización», L118; «no se falsificó su contenido», L129; «no se borraron», L1451) siguen funcionando como constancia de límites, no como énfasis retórico. La forma estricta de Don't 4 (landscapes/paradigms/ecosystems/transformations) mantiene 3 coincidencias, todas concretas —«cada transformación y cada estimación del pipeline» (L1389) se refiere a transformación de datos—. Don't 8 conserva las mismas reescrituras descritas de §43–47 y §59–63 (L1381, L1415), sin nuevas apariciones. El metadiscurso y el professional narcissism permanecen en 0; la señalización interna sigue haciéndose con etiquetas en negrita y remisiones a rutas. La uniformidad de longitud tampoco cambia: §69 alterna tres oraciones largas (≈30–39 palabras) con los párrafos cortos de §70, sin cadenas de cuatro o más frases de 18–25 palabras.

— polarity: neutral · confidence: high · related: [[#F-V7-001]], [[#F-V7-003]]

### F-V7-009 — Romero §13 Don't 8 en §69: la declaración describe la auditoría, no la muestra

§69 enuncia el resultado de la auditoría —«La auditoría completa de este documento se realizó con la skill `review` de MatCom y sus resultados se conservan en …» (L1469)— y su paralelo EN (L1471) sin incluir ningún hallazgo, densidad ni fragmento del resultado; la conclusión se da antes que la evidencia. Es el mismo mecanismo que el V7 de la iteración 1 registró en §43–47 y §59 (reescrituras descritas, no mostradas), ahora aplicado a la propia declaración de uso de IA. Se consigna como patrón de cierre, no como déficit de evidencia: las cifras de la declaración («trece artefactos de fase») son verificables en el directorio `reviews/`.

— polarity: neutral · confidence: medium · related: [[#F-V7-002]], [[#F-V7-007]]

### F-V7-010 — Pinker: anclaje concreto sostenido en las secciones editadas y en las nuevas

El síntoma «definiciones sin instancias» no aparece en los pasajes nuevos: §69 ancla la procedencia a «los datos y del código versionados en este repositorio» y a la ruta `reviews/informe-tecnico-2026-11-27.{md,forensic.md}`; §70 ancla cada referencia a Crossref/OpenAlex, GOV.UK, ANFAC o AEADE; §59–60 ancla cada cifra a `outputs/tables/kpis.csv` o a `config.py`. Esta densidad de anclajes es la contrapartida de los metaconceptos de F-V7-005 y explica que, pese al repunte local, el patrón global siga siendo de baja densidad de tics.

— polarity: positive · confidence: high · related: [[#F-V7-006]], [[#F-V7-005]]

## AI-pattern density by section

Valores aproximados sobre los textos cacheados; «metaconcepto/1k» agrega las palabras de la róbrica Pinker indicadas en F-V7-005, «openers» cuenta «Se + verbo», participio de los bloques «EN.» y pasiva inglesa, y no incluye «In recent years…» ni «This study demonstrates that…» (0 instancias). La columna «Densidad» compara iteración 1 → iteración 2.

| Section | Density (iter1 → iter2) | Notes |
|---|---|---|
| §1–3 — Objetivo, estados, carpetas (L14–53) | low → low | Sin cambio; 0 triadas; openers «Se + verbo» |
| §4–9 — Fases 1–6 (L54–108) | low → low | Sin cambio; tablas y listas; 0 atenuadores |
| §10–12 — Marco legal, problemas, conclusiones (L110–139) | medium → medium | Conclusión 5 reescrita con ruta y «se regeneran de forma automática» (L139); «marco» 3; triada en L118 |
| Parte II §1–12 — Objective…Conclusions (L145–270) | low → low | Sin cambio salvo la nota de actualización (L169–L170); 0 hedges; 0 triadas nuevas |
| §13 — Registro de altas (L274–748) | n/a → n/a | Tabla generada por script; excluida del denominador |
| §14–33 — Sincronización, eficiencia, colas, marcos (L750–1008) | medium → medium | Sin cambio; 19 openers «Se…»; 18 bloques EN |
| §17–21 — Guía, auditoría y marcos analíticos (L787–884) | high → high | Sin cambio; 14 «análisis» + 9 «marco» en 1.671 palabras (≈13,8/1k); escaleras de 8 y 9 pasos |
| §34–48 — Rentabilidad, APK, mapas, storytelling (L1012–1242) | medium → medium | §37 añade ancla TRMI 930 y `config.py` (L902); 0 hedges |
| §49–58 — Repos, mejoras, fuentes, ONEI, chunks (L1245–1369) | medium → medium | Sin cambio; ≈25 «no/sin»; d5 con ancla en L1291 |
| §59–63 — Storytelling final, modelos, sitio, retención (L1373–1415) | high → high | Sin cambio en d8/d5; se añaden 28/981, R² 0,277, p 0,411 (L1381) y cifras vigentes (L1379); anclaje, no hedging |
| §64–68 — Automatización y espacio (L1419–1461) | low–medium → low–medium | Sin cambio; «quizá» en L1459 (único hedge del corpus); «no se borraron», L1451 |
| §69 — Declaración de uso de IA (L1467–L1473) | n/a → **medium** | Nueva: d3 ×2, d5 ×3, ≈12 metaconceptos en ~200 palabras; 0 hedges, 0 openers de fórmula, 0 «not just…but» |
| §70 — Referencias verificadas (L1475–L1481) | n/a → low | Nueva: lista enumerativa con procedencia externa concreta; 0 tics estrictos de Romero §13 |

Totales comparados (texto completo, incluidas tablas): palabras 28.586 → 29.106; hedging 1 → 1 (0,03/1k en ambos); metaconceptos 197 → 205 (6,89 → 7,04/1k); adjetivos valorativos sin ancla 4 → 7 (0,14 → 0,24/1k); openers de fórmula 0 → 0; «not just X, but Y» 0 → 0; Don't 4 estricto 3 → 3.

## Hook para V9

La tabla de densidad que V9 (§15 de su informe, «No se recibió tabla de densidad de V7») declaró no haber recibido queda aquí consignada: ninguna sección nueva alcanza `ai-pattern-density: high`; §69 es `medium` y §70 es `low`. Los dos bloques que sí permanecen en `high` —§17–21 y §59–63— son idénticos a los de la iteración 1 y su anclaje numérico es incompatible con un tic de atenuación: la declaración de «contraste contra los archivos» (L1469) se corresponde con esas cifras y rutas. Para el contraste con `V9.ai_use_declaration.master`, la densidad media de §69 se debe a dispositivos de superficie (triadas de cola larga, tres adjetivos sin ancla y metaconceptos), no a hedging ni a openers de fórmula; las tres lagunas de nombrado —herramientas genéricas, fases no enumeradas y protocolo sin nombre— se detallan en F-V7-002. Se señala además que la huella de auditoría citada en §69 apunta a `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` (iteración 1), no a los artefactos `-iter2`; dato descriptivo para el alcance de la declaración.

---
type: audit-artifact
phase: v8-bibliography
slug: informe-tecnico-2026-11-28-iter4
generated_at: 2026-11-28T03:12:40-04:00
audited_document: .playground/audit-cache/informe-tecnico-2026-11-28-iter4/informe-tecnico-2026-11-28-iter4.text.md
language: es
bibliography_entries_total: 41
verified: 37
unverified: 4
---

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

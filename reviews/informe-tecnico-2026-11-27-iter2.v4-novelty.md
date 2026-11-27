---
type: audit-artifact
phase: v4-novelty
slug: informe-tecnico-2026-11-27-iter2
generated_at: 2026-11-27T21:18:08Z
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter2/informe-tecnico-2026-11-27-iter2.text.md
language: es
level: master
---

## Resumen

- E1 registra una sola afirmación etiquetada `novelty` (C011, §34): la arquitectura del pipeline adaptada de `Egyptian-Used-Cars`; el diferenciador sigue siendo de integración local, sin componente nuevo.
- La nueva §70 y `Data/referencias.md` **no resuelven F-V10-006**: añaden transparencia bibliográfica (38 referencias, cuatro verificadas) pero ningún contraste argumentativo con los vecinos académicos más cercanos (P014, P026, P009, P029), todos `Cited in document: no`.
- No se detecta sobreclaim de originalidad; tampoco puede declararse «novedad confirmada», porque la iteración 2 fue una re-verificación de metadata (`papers_l3: 0`, consultas no temáticas) y el propio E2 constata que los flags y la contradicción de Akerlof (P001) permanecen.

### F-V4-001 — E1 registra un solo claim `novelty`: la arquitectura adaptada de Egyptian-Used-Cars

El inventario de la iteración 2 consigna «By type: result 60 · methodological 43 · novelty 1 · contextual 43 · definitional 5 · citation-grounded 11» (e1-claims, línea 15). El único objeto de esta evaluación es C011 (líneas 139–149), que cita verbatim en §34 (L1018): «Creé `Data/analisis_rentabilidad/` siguiendo la arquitectura del repositorio **Egyptian-Used-Cars** (ingesta → limpieza → EDA → estadística → benchmark), pero adaptada a nuestras fuentes y preparada para crecer:». El propio E1 anota en C011: «es la única diferenciación comparativa declarada del documento (F-V10-006)». El diferenciador declarado es de integración —adaptación de una arquitectura de ingeniería a las fuentes cubanas y disposición a crecer—, no de componente ni de formulación de problema. La brecha «frente a Egipto» descrita en C012 (§34, L1058–1060) es de escala y cobertura: «solo 497 usados, un único snapshot, HP/kilometraje mayormente ausentes», es decir, una diferencia de datos en contra del propio proyecto.

El criterio `V4.scope_of_novelty_claim` para `level=master` se lee: «Component novelty + integration novelty: one of the two should be substantive» (level-criteria.md, línea 97). La integración aquí es substantiva en términos de ingeniería (adaptadores por dominio, SQLite por tienda, procedencia), pero el texto la presenta como adopción y adaptación de una arquitectura ajena, no como contribución de método; no hay una reclamación de primacía global que cotejar.

— polarity: neutral · confidence: high · related: [[#C011]], [[#C012]], [[#F-V10-006]] · criteria: V4.scope_of_novelty_claim.master

### F-V4-002 — §70 y `Data/referencias.md` no resuelven F-V10-006: transparencia sin contraste

La sección nueva §70 (L1477–1479) declara: «Referencias citadas y verificadas externamente durante la auditoría: Akerlof (1970), *The Market for "Lemons"* (Crossref/OpenAlex); UK Department for Transport / DVLA, estadísticas de vehículos (GOV.UK); ANFAC, informes del sector automotriz español (sitio oficial); AEADE, estadísticas de matriculaciones (sitio oficial)», y remite «La convención numerada de 38 referencias y su estado de verificación [...] en `Data/referencias.md`». El archivo enlazado contiene 38 entradas con `Citada: sí/no` y seis marcadores `(metadata incomplete)`. El propio E1 lo confirma en su contexto de iteración: «**F-V10-006 — Diferenciación solo contra el repositorio egipcio: NO RESUELTA.** §34 (L1018, L1058–1060) sigue siendo el único pasaje comparativo, por escala de datos; §70 (L1477) añade cuatro referencias verificadas pero ningún contraste argumentativo con los vecinos académicos. El inventario registra una sola señal de novedad (C011, L1018)» (L849).

El criterio `V4.prior_art_engagement` para `level=master` exige «Closest prior works cited, contrasted, and discussed in their own subsection» (level-criteria.md, línea 106). §70 satisface la primera condición para Akerlof (P001) y para tres fuentes institucionales (P007–P009), pero no las otras dos: no hay discusión de métodos, resultados o limitaciones de los trabajos más cercanos al claim de C011, ni subsección dedicada a ellos. Los vecinos de ese claim —P014 (Gegić et al., 2019), P026 (Muça et al., 2026), P009 (Du et al., 2026) y P029 (Vidal Alejandro et al., 2024)— figuran en `Data/referencias.md` como [14], [26], [9] y [29] y mantienen «Citada en el informe: no»; aparecer en la lista numerada no equivale a estar citados en el cuerpo. En paralelo, E2 constata en H1 que «mejoró la transparencia formal, no la completitud de los campos señalados» (L176) y en H2 la doble etiqueta de Akerlof: verificada en §70 y `(metadata incomplete)` en [1] (L180). La resolución de F-V10-006 queda, por tanto, en el plano formal/bibliográfico, no en el de la novedad.

— polarity: negative · confidence: high · related: [[#C011]], [[#C009]], [[#C048]], [[#P001]], [[#P007]], [[#P008]], [[#P009]], [[#F-V10-006]], [[#F-V4-003]] · criteria: V4.prior_art_engagement.master

### F-V4-003 — Único párrafo comparativo: repositorio egipcio, no el vecino académico

El pasaje comparativo sigue siendo «Brecha frente a Egipto» (§34, L1058–1060): «Egipto tiene 23.500 anuncios, historial mensual de precios, HP y kilometraje estructurados, ANOVA/OLS/VIF, Tableau y Power BI. Nosotros tenemos el pipeline y las técnicas cubiertas, pero solo 497 usados, un único snapshot, HP/kilometraje mayormente ausentes y un solo benchmark de auto nuevo». El referente es `Egyptian-Used-Cars`, fuente de ingeniería que no figura en el mapa E2; la comparación opone escalas de datos y declara una desventaja, sin discriminar qué hace diferente el método propio.

Los vecinos académicos del claim están en el mapa completo de la pasada 1, que la iteración 2 declara vigente (e2-literature iter2, nota (b), L16): P014 — Gegić, E.; Isaković, B.; Keco, D.; Mašetić, Z.; Kevrić, J. (2019), «Car Price Prediction using Machine Learning Techniques», *TEM Journal*, DOI 10.18421/tem81-16, descrito como «el antecedente más directo de la combinación scraping + modelado de precios» (L176) —; P026 — Muça, M.; Bani, K.; Alla, A. (2026), «A Pipeline for Integrating and Analyzing Public Business Data in Albania Using Web Scraping and Machine Learning», *IJACSA*, DOI 10.14569/ijacsa.2026.0170845 —; y P009 — Du, Z.; Yang, Z.; Zhang, Y.; Li, S.; Liu, Y. (2026), «Nonlinear Depreciation and Brand Heterogeneity in Chinese Used-Car Listing Prices: An Interpretable Hedonic Regression and Out-of-Sample Evaluation», DOI 10.54254/2754-1169/2026.38524, «el paralelo metodológico más cercano al informe» (L123). Los tres están marcados `Cited in document: no`. Bajo `V4.differentiation_from_prior_art.master` («Differentiator articulated with at least one explicit comparison paragraph to one closest prior work», level-criteria.md, línea 88), la forma del criterio se cumple solo respecto de una fuente ajena al mapa: sigue sin haber párrafo comparativo con el trabajo académico más cercano.

— polarity: negative · confidence: high · related: [[#C011]], [[#C012]], [[#P009]], [[#P014]], [[#P026]], [[#F-V10-006]], [[#F-V4-002]] · criteria: V4.differentiation_from_prior_art.master

### F-V4-004 — No se detecta sobreclaim: alcance local declarado y recomendador diferido

El claim evaluado usa verbos de adopción, no de primacía: §34 (L1018) dice «siguiendo la arquitectura del repositorio **Egyptian-Used-Cars** [...] pero adaptada a nuestras fuentes» y el encabezado del §34 (L1016) rotula el trabajo como «inspirado en Egyptian-Used-Cars». El marco analítico se presenta como «**Marco general (8 pasos, derivado de los trabajos revisados)**» (§19, L837) y el objetivo vigente excluye explícitamente la novedad de producto: «La definición de un producto interactivo que recomiende la compra más rentable según las preocupaciones del usuario queda diferida a una especialización posterior» (§1, L16; C001). No aparece en el texto una afirmación de «primero», «nuevo método» o «contribución original» que contradiga a los trabajos del mapa; la única reclamación comparativa, «Brecha frente a Egipto», se enuncia en dirección desfavorable al propio proyecto. Bajo `V4.scope_of_novelty_claim.master`, el alcance es local y está declarado como tal; no se observa sobreclaim que corregir.

— polarity: positive · confidence: high · related: [[#C001]], [[#C011]], [[#C012]], [[#P014]] · criteria: V4.scope_of_novelty_claim.master

### F-V4-005 — Iteración 2 sin búsquedas temáticas ni lectura L3: sin novedad confirmada

El mapa E2 de esta pasada declara `queries_run: 22`, `papers_l1: 6`, `papers_l2: 6`, `papers_l3: 0` (frontmatter) y explica que «las consultas se derivaron del mandato recibido —comprobar si la nueva §70 y `Data/referencias.md` resolvieron los `(metadata incomplete)` de la pasada 1— y no son búsquedas temáticas nuevas» (L16). La sección `likely_missing important works` se limita a declarar «Sin cambios respecto al mapa de la pasada 1» (L168). En consecuencia no se incorporó ningún trabajo capaz de desplazar a P014, P026 o P009 como vecinos más cercanos, y tampoco se leyó texto completo que permita refinar el solapamiento. Los tres flags heredados cuyo motivo era el conteo de citas (P003, P004, P005) «sí se resolvió por OpenAlex (13, 96 y 9 citas respectivamente), pero `Data/referencias.md` no incorporó ni los conteos ni las versiones publicadas con DOI; los marcadores siguen ahí» (H1, L176); P001 conserva el resumen como índice de secciones y P002 el suyo sin indexar.

Una conclusión de «novedad confirmada» excedería esta evidencia: según el criterio `V4.prior_art_engagement.master` (level-criteria.md, línea 106), los trabajos más cercanos no están citados en el cuerpo, contrastados ni discutidos en su propia subsección, y el mapa disponible es el mismo de la pasada 1 con una capa de re-verificación de metadata. La lectura permitida es «sin antecedente nuevo añadido en esta pasada», no ausencia de arte previo ni validación de originalidad.

— polarity: neutral · confidence: high · related: [[#C009]], [[#C048]], [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#P005]], [[#P014]], [[#F-V4-002]] · criteria: V4.prior_art_engagement.master

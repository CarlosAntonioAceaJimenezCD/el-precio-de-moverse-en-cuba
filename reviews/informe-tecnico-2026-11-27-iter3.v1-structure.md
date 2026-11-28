---
type: audit-artifact
phase: v1-structure
slug: informe-tecnico-2026-11-27-iter3
generated_at: 2026-11-28T00:15:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter3/informe-tecnico-2026-11-27-iter3.text.md
language: es
---

# V1 — Structure (findings)

### F-V1-001 — Persiste la ausencia de resumen VSN-C, hipótesis falsable y sección de contribuciones

El encabezado mantiene los seis campos de las iteraciones anteriores —«**Proyecto / Project:**», «**Autor / Author:**», «**Fecha / Date:**», «**Ubicación / Location:**», «**Estado / Status:**», «**Idioma / Language:**» (L3–8)— con la autoría y la firma consignadas por rol («responsable del proyecto / project owner», L4 y L1522) y «**Última actualización / Last update:** 27/11/2026» (L1523). Entre los 96 encabezados del texto (L1–L1523) no figura «Resumen» ni «Abstract», y tampoco dedicatoria, agradecimientos ni dictamen de tutor. §69 (L1467–1471) y §70 (L1475–1479) aportan declaración de uso de IA y aparato de referencias verificadas, sin función de resumen.

El material más cercano a un resumen sigue distribuido entre §1 ES (L16–18) y §1 EN (L147–149): allí aparecen Vision —«caracterizar estructura, precios, oferta, segmentos, tendencias, asequibilidad y condiciones de rentabilidad»— y Steps —«dos pilares: la base de datos del mercado cubano y un pipeline de scraping reutilizable»—, pero no hay elemento de novedad ni cifras en la apertura. Las cinco conclusiones de §12 (L135–139 y L266–270) enumera hallazgos sin encabezado de «Contribuciones», y la única formulación explícita queda dentro de un párrafo de posicionamiento en §71.6: «la contribución es de procedencia y normalización, no de algoritmo» (L1520). No aparece la cadena «hipótesis» ni «hypothesis» en ningún punto del texto: §34 reporta «una depreciación media de **−5,43 % anual** (p<0,001)» (L1056) sin proposición previa sometida a contraste, y §59–§60 retiran esa pendiente (L1381, L1389). §70 anuncia «La convención numerada de 38 referencias» (L1477–1479), pero el cuerpo no contiene citas numeradas `[N]`; la contribución y el aparato bibliográfico quedan, por tanto, fuera de una sección de contribuciones.

— polarity: negative · confidence: high · related: [[#C001]], [[#C008]], [[#C009]], [[#C011]], [[#C016]]

### F-V1-002 — Objetivo alineado en ambas partes y contrastado en §19–§71; la fila de la fase 8 sigue divergiendo

La divergencia de introducciones de la iteración 2 queda cerrada: §1 ES (L16) y §1 EN (L147) enuncian el mismo objetivo —«un análisis del mercado automotor cubano» / «to analyse the Cuban automotive market»— con el producto interactivo diferido, y §12 ES (L139) y §12 EN (L270) coinciden ahora en que «El análisis de mercado y el modelo de rentabilidad (fase 8) están implementados… y se regeneran de forma automática» / «are implemented under `Data/analisis_rentabilidad/` and regenerate automatically». El objetivo se corresponde con secciones ejecutadas: el marco de ocho pasos (§19, L837–846), los nueve bloques (§20, L861–871), el pipeline de rentabilidad (§34, L1016–1062), los resultados vigentes (§59–§60, L1377–1391) y los estándares de §71 (L1485–1520).

Subsiste una divergencia acotada: la fila 8 de la tabla de fases dice «Análisis de mercado, comparables y rentabilidad» en español (L33) pero «Analysis, profitability model and interactive product» en inglés (L164), denominación que §21 retiró al disponer «La fase 8 pasa a llamarse **Análisis de mercado, comparables y rentabilidad**» (L883). Las notas de actualización de §2 (L38, L169) remiten el estado vigente a «§59–§60», y esos dos destinos existen y contienen las cifras y la justificación del modelo actual.

— polarity: neutral · confidence: high · related: [[#C001]], [[#C002]], [[#C032]], [[#C059]]

### F-V1-003 — Numeración 1–12 duplicada, salto de nivel en §13 y referencias cruzadas sin marcadores rotos

La numeración se reinicia igual que en iteraciones previas: dos secciones «1.» (L14, L145), dos «12. Conclusiones» (L133, L264) y una secuencia única desde §13 (L274) hasta §71 (L1485), de modo que «§1»–«§12» designan dos destinos posibles según la parte. El bloque §13 «Registro de altas / Change log» (L274–752) emplea encabezado de nivel 1 mientras §14–§71 usan nivel 2 (L754, L1016, L1485), y queda fuera de «# Parte I — Español» (L12) y «# Part II — English» (L143) pese a continuar su numeración. De las 58 secciones §14–§71, 53 llevan fecha en el título; §14, §15, §69, §70 y §71 no la llevan, y §69 aparece precedido de dos reglas horizontales consecutivas (L1481, L1483).

En integridad de referencias cruzadas no hay marcadores `??` ni comandos `\ref{}`: los cuatro apuntadores `§` del texto —«(§34)» y «§59–§60» (L38, L169), «(§34)» (L1206) y «§59» (L1214)— tienen encabezado destinatario (L1016, L1377, L1387). Persisten los cuatro marcadores de plantilla de §59 —`<!-- kpi:modelo_n_completo -->`, `<!-- kpi:modelo_candidatas -->`, `<!-- kpi:modelo_r2_completo -->` y `<!-- kpi:modelo_pf_completo -->` (L1381)—, insertados en la prosa y no resueltos en el texto cacheado. Los títulos de edición señalados antes continúan —§45, §46, §47 «Reescritura de la sección 3 / Apertura de la sección 3 / Reescritura de la sección 4 del storytelling» (L1212, L1220, L1228)—, frente a títulos instructivos como §26 «Orden corregido: enlace → clasificación → BD» (L926) y §39 «Continuación del scrapeo y presentación narrativa» (L1125).

— polarity: neutral · confidence: high · related: [[#C003]], [[#C011]], [[#C016]], [[#C059]]

## Resumen

- Sin resumen VSN-C, sin hipótesis falsable y sin sección de contribuciones; las aportaciones quedan en §12 y en el posicionamiento de §71.6.
- §1 coincide en ambas partes y §12 ya no diverge, pero la fila 8 de la tabla de fases conserva un nombre retirado por §21 en la versión inglesa.
- La numeración 1–12 continúa duplicada y §13 rompe el nivel de encabezado; las cuatro referencias `§` resuelven y no hay marcadores `??` ni `\ref{}`.

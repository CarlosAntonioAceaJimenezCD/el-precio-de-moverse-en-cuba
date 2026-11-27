---
type: audit-artifact
phase: v1-structure
slug: informe-tecnico-2026-11-27-iter2
generated_at: 2026-11-27T22:20:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter2/informe-tecnico-2026-11-27-iter2.text.md
language: es
---

# V1 — Structure (findings)

### F-V1-001 — Persiste la ausencia de resumen VSN-C, hipótesis y contribuciones

El encabezado conserva los seis campos de la iteración 1 —«**Proyecto / Project:**», «**Autor / Author:**», «**Fecha / Date:**», «**Ubicación / Location:**», «**Estado / Status:**», «**Idioma / Language:**» (L3–8)— con la autoría consignada como rol («responsable del proyecto / project owner», L4) y la firma igualmente por rol (L1483); la fecha de cierre sube a «**Última actualización / Last update:** 27/11/2026» (L1484). Ninguno de los 89 encabezados del texto es «Resumen» o «Abstract», y no aparecen dedicatoria, agradecimientos ni dictamen de tutor. Las dos secciones nuevas respecto a la pasada 1 —§69 «Declaración de uso de inteligencia artificial / AI-use declaration» (L1467–1471) y §70 «Referencias verificadas / Verified references» (L1475–1479), después del antiguo cierre en §68— aportan declaración procedimental y aparato bibliográfico, pero no sustituyen un resumen ni una sección de contribuciones.

El material más cercano a un resumen sigue repartido entre §1 (L14–18) y las cinco conclusiones de §12 (L133–139), sin elemento de novedad ni contribuciones enumeradas. El inventario E1 de esta pasada clasifica una señal de novedad —«Creé `Data/analisis_rentabilidad/`… adaptada a nuestras fuentes y preparada para crecer» (C011, §34 L1018)— frente a `novelty 0` de la pasada 1, aunque el enunciado ya figuraba en el texto anterior (L1014). Tampoco se enuncia una hipótesis central como proposición falsable: §34 (L1056) reporta «una depreciación media de **−5,43 % anual** (p<0,001)» sin proposición previa que la someta a contraste, y §59–§60 (L1381, L1389) retiran esa pendiente; E2 hace constar que el plan no declaró `hypotheses_planned`. E1 C009 consigna además que el cuerpo del informe no lleva citas numeradas.

— polarity: negative · confidence: high · related: [[#C001]], [[#C008]], [[#C011]], [[#C009]]

### F-V1-002 — Objetivo alineado en ambas partes, pero fase 8 y conclusión 5 divergen

La divergencia observada en la iteración 1 entre las dos introducciones queda cerrada: §1 ES (L16) y §1 EN (L147) enuncian ahora el mismo objetivo —«un análisis del mercado automotor cubano» / «to analyse the Cuban automotive market»— con la recomendación interactiva diferida, donde la pasada 1 leía «The project is named **AutoDecide Habana**. Its goal is to define an interactive product…». §21 (L881–886) documenta el cambio —«el objetivo inmediato deja de ser la recomendación interactiva de compra y pasa a ser **un análisis de mercado**»— y la Parte II lo recoge en su §1; ambas partes añaden ahora una nota de actualización en §2 (L38, L169) que remite el estado vigente de la fase 8 a «§59–§60». El objetivo de análisis se corresponde con secciones ejecutadas: el marco de ocho pasos (§19, L837–846), los nueve bloques (§20, L861–871), el pipeline (§34, L1016–1037) y los resultados (§59–§60, L1377–1391).

Persisten, sin embargo, dos puntos de la observación anterior. La fila 8 de la tabla de fases se lee «Análisis de mercado, comparables y rentabilidad» en español (L33) pero «Analysis, profitability model and interactive product» en inglés (L164), nombre que §21 había retirado. La conclusión 5 diverge en el mismo sentido: §12 ES (L139) afirma que «El análisis de mercado y el modelo de rentabilidad (fase 8) están implementados… y se regeneran de forma automática», mientras §12 EN (L270) sostiene «The interactive product and profitability model (phase 8) are not implemented yet». E1 lo registra en C001–C002 y E3 lo describe como divergencia de contenido entre párrafos paralelos (L196), no de traducción.

— polarity: neutral · confidence: high · related: [[#C001]], [[#C002]], [[#C029]]

### F-V1-003 — Numeración 1–12 duplicada y referencias sin anclar en el cuerpo

La numeración se reinicia igual que en la pasada 1: dos secciones «1.» (L14, L145) y dos «12. Conclusiones» (L133, L264), tras las cuales la secuencia continúa hasta §70 (L1479), tres secciones más que el §68 final de la iteración 1. El bloque §13 «Registro de altas / Change log» (L274–748, 475 líneas) usa encabezado de nivel 1 mientras §14–§70 usan nivel 2 (L754, L1467, L1475), y declara «175 entradas adicionales no listadas / omitted» (L295). De las 57 secciones numeradas §14–§70, 53 llevan fecha en el título; §14, §15, §69 y §70 no la llevan, y §69 va precedido de dos reglas horizontales consecutivas (L1463, L1465). Los títulos de edición señalados en la pasada 1 permanecen —§45, §46, §47 «Reescritura de la sección 3 / Apertura de la sección 3 / Reescritura de la sección 4 del storytelling» (L1212, L1220, L1228)—, mientras §69–§70 son títulos descriptivos de contenido.

En integridad de referencias cruzadas no aparecen marcadores `??` ni comandos `\ref{}` en esta iteración, como tampoco en la anterior; E3 consigna «Tables: none-detected» (L164) y «Figures: none-detected» (L239), y las tablas y figuras se localizan por encabezado, sección o ruta de archivo. Lo nuevo es la aparición de cuatro marcadores de plantilla insertados en la prosa de §59 (L1381): `<!-- kpi:modelo_n_completo -->`, `<!-- kpi:modelo_candidatas -->`, `<!-- kpi:modelo_r2_completo -->` y `<!-- kpi:modelo_pf_completo -->`, actualizados por `Auxiliares/herramientas/actualizar_numeros.py` (E3, L62, L330), además del «apéndice visual con cinco cuadros y seis gráficos reales» descrito con «referencias discretas entre paréntesis» (L1381). §70 anuncia «La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`» (L1477–1479), pero el cuerpo no contiene citas `[N]` (E1 C009; E3 L136, L281), y E2 H1–H2 observa que Akerlof figura a la vez como referencia verificada en §70 y con `(metadata incomplete)` en `[1]` (P001).

— polarity: neutral · confidence: high · related: [[#C003]], [[#C009]], [[#P001]]

## Resumen

- Persisten el encabezado con autoría por rol, la ausencia de resumen VSN-C, hipótesis falsable, contribuciones y firma nominativa; §69–§70 son las únicas secciones nuevas.
- §1 coincide ya en ambas partes y §2 añade notas de actualización, pero la fila de la fase 8 y la conclusión 5 siguen divergiendo entre español e inglés.
- La numeración 1–12 continúa duplicada y la bitácora llega a §70; no hay referencias rotas, pero los marcadores KPI y las 38 referencias de §70 no están anclados en el cuerpo.

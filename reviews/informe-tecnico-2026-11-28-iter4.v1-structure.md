---
type: audit-artifact
phase: v1-structure
slug: informe-tecnico-2026-11-28-iter4
generated_at: 2026-11-28T03:12:14-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-28-iter4/informe-tecnico-2026-11-28-iter4.text.md
language: es
---

# V1 — Structure (findings)

### F-V1-001 — Resumen VSN-C e hipótesis H1 incorporados en ambas partes; contribuciones solo en el resumen

La iteración 4 incorpora «## Resumen (VSN-C)» (L14–19) y «## Abstract (VSN-C)» (L156–161), con los cuatro rótulos «**Visión» / «**Pasos» / «**Novedad» / «**Contribuciones» y «**Vision» / «**Steps» / «**News» / «**Contributions»; en la iteración 3 no figuraban resumen ni abstract (revisión V1 de aquella iteración, F-V1-001). La novedad se enuncia como objeto de auditoría —«la procedencia y la normalización se tratan como objeto de auditoría; la pérdida de muestra por variables ausentes se reporta como hallazgo y no se oculta» (L18; «provenance and normalisation are treated as an audit object», L160)— y las contribuciones quedan enumeradas en una línea por parte: «base compacta reproducible, panel interactivo autocontenido, pipeline con timers y un expediente de auditoría con 13 artefactos» (L19) / «a reproducible compact database, a self-contained interactive dashboard, a timer-driven pipeline and an audit trail with 13 artifacts» (L161). No hay sección autónoma «Contribuciones»: §12 sigue siendo una lista de cinco conclusiones (L144–148, L286–290) y §71.6 conserva «el aporte es de procedencia y normalización, no de algoritmo» (L1549; texto ya presente en la iteración 3, L1520). El encabezado mantiene seis campos (L3–8) y la firma por rol (L1604–1605), sin dedicatoria, agradecimientos ni dictamen de tutor.

H1 se formula en ambas partes —«los precios de los tres tiers de marca en el mercado local provienen de la misma distribución, controlando por antigüedad y kilometraje» (L21) / «prices across the three brand tiers in the local market come from the same distribution, controlling for age and mileage» (L163)—, con contraste y desenlace declarados: «Se contrasta con Kruskal-Wallis; se rechaza con p < 0,001 en la corrida vigente». La proposición de igualdad de distribuciones admite refutación, y la cadena «hipótesis / hypothesis» pasa de cero ocurrencias en la iteración 3 a dos en la 4. El respaldo numérico aparece sin apuntador de sección: §60 registra «Kruskal-Wallis p = <!-- kpi:kw_p -->0,00000» (L1409) y §71.3 «H = 44,313» (L1528), mientras la depreciación «−5,43 % anual (p<0,001)» de §34 (L1076) queda rotulada «Línea base real de la primera ejecución» (L1061).

— polarity: positive · confidence: high · related: [[#F-V1-003]]

### F-V1-002 — Duplicidad 1–12 declarada, salto de nivel de §13 cerrado e inversión 71.15/71.14 en la sección final

La numeración se reinicia en «# Part II — English» (L152): dos «1. Objetivo / Objective» (L23, L165) y dos «12. Conclusiones / Conclusions» (L142, L284), con una secuencia única §13–§71 (L294, L1505). La iteración 4 añade «*Nota: la numeración de secciones se reinicia en esta parte; las referencias cruzadas se interpretan dentro de cada parte.*» (L154), ausente en la iteración 3 (L143). El salto de nivel de §13 señalado en aquella revisión queda cerrado: `# 13. Registro de altas / Change log` (iteración 3, L274) pasa a `## 13. Registro de altas / Change log` (L294), aunque el bloque bilingüe sigue situado entre las dos partes y fuera de ellas.

La sección 71 enumera 71.1–71.6 en orden (L1507, L1520, L1526, L1532, L1541, L1547) y continúa con «### 71.15 Declaraciones / Declarations» (L1551) antes de «### 71.14 Obras del mapa literario citadas en el cuerpo» (L1557): ambas subsecciones son nuevas frente a la iteración 3, que cerraba en 71.6 (L1522), y la secuencia 71.15 → 71.14 invierte la numeración. En 71.1, la fila «| Modelo principal propio | OLS de log-precio con antigüedad, km, condición y tier | R² 0,101 sobre 584 observaciones |» (L1516) aparece separada de la tabla de tres filas (L1509–L1513) y detrás del párrafo de cierre (L1515). Persisten los títulos de bitácora —«Reescritura de la sección 3 del storytelling» / «Apertura de la sección 3 del storytelling» / «Reescritura de la sección 4 del storytelling» (L1232, L1240, L1248)—.

— polarity: negative · confidence: high · related: []

### F-V1-003 — Apuntadores § con destino existente y cero marcadores `??`; 29 etiquetas `kpi` sin resolver en prosa

Los diez apuntadores § del texto tienen encabezado destinatario: «§34» y «§59–§60» en las notas de actualización de §2 de ambas partes (L47, L189), «(§34)» en §44 y «§59» en §45 (L1226, L1234), «§71.5» en la declaración de §69 (L1553, L1555) y «§71.6» en el cierre de §70 (L1600). Los destinos existen en §34 (L1036), §59 (L1397), §60 (L1407), §71.5 (L1541) y §71.6 (L1547); el apuntador de §44 añade además una advertencia de vigencia —«cifra que la corrida vigente ya no sostiene» (L1226)—. La búsqueda de `??`, `\ref{}`, `Tabla ?` y `Figure ?` da cero coincidencias tanto en la iteración 4 como en la 3.

Frente a cuatro marcadores `<!-- kpi:... -->` en la iteración 3 (L1381), la iteración 4 conserva 29 apariciones —23 etiquetas distintas— intercaladas en la prosa: 13 en §59 (L1399, L1401), 3 en el resumen EN de §59 (L1403), 4 en §60 (L1409), 2 en cada fila de la tabla de baselines de §71.1 (L1511–L1512), 3 en el resumen EN de §71.1 (L1518) y 2 en §71.3 (L1528). Los valores numéricos aparecen a continuación de la etiqueta —«<!-- kpi:kw_p -->0,00000» (L1409), «<!-- kpi:ci_bajo -->10.000» (L1528)—, de modo que el marcador de plantilla queda visible en el texto cacheado y en los resúmenes bilingües de §59 y §71.1.

— polarity: neutral · confidence: high · related: [[#F-V1-001]]

## Resumen

- El resumen VSN-C, la hipótesis H1 falsable y las cuatro contribuciones aparecen ahora en ambas partes; no hay sección autónoma de contribuciones ni dedicatoria, agradecimientos o dictamen de tutor.
- La duplicidad 1–12 se declara explícitamente y §13 ya no rompe el nivel de encabezado, pero §71.15 precede a §71.14 y una fila de la tabla de baselines queda fuera de la tabla.
- Los diez apuntadores § resuelven y no hay `??` ni `\ref{}`; los marcadores `<!-- kpi:... -->` pasan de 4 en la iteración 3 a 29 en la 4.

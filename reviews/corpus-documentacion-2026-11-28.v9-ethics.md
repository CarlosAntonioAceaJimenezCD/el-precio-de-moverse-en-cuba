---
type: audit-artifact
phase: v9-ethics
slug: corpus-documentacion-2026-11-28
generated_at: 2026-11-28T14:30:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md
language: es
level: master
---

## Resumen

- Los 8 archivos del corpus no contienen declaración de uso de IA: el barrido de «IA generativa», «inteligencia artificial», «ChatGPT», «Claude», «asistencia de», «generado con» y «AI use» da cero coincidencias, mientras el informe sí la consigna en §69.
- La privacidad queda declarada de forma más fuerte en el corpus («no recopila datos personales de anunciantes», L112) que en §71.15 («los anuncios contienen datos de contacto que se excluyen de la publicación», L1553), y el propio corpus registra 12.338 teléfonos y un campo `teléfono` en el mapa.
- Las 33 respuestas y las entrevistas se usan en el storytelling (L251) sin consentimiento, anonimización ni comité; §71.15 las trata como contexto no experimental, pero no enlaza esa decisión con el grupo nominado de §50 ni con la restricción de datos agregados de §10.

### F-V9-001 — Declaración de uso de IA ausente en los ocho archivos del corpus

El barrido del texto cacheado (833 líneas) en busca de «IA generativa», «inteligencia artificial», «uso de IA», «declaración de uso», «ChatGPT», «Claude», «asistencia de», «generado con» y «AI use» devuelve cero coincidencias. Ninguno de los bloques —`README.md` (L8–L115), storytelling (L119–L390), `MODELOS_Y_FUNCIONES.md` (L395–L488), `ARQUITECTURA_DATOS.md` (L493–L566), `ALCANCE_Y_RETENCION.md` (L571–L624), `AUTOMATIZACION.md` (L629–L730), `ESTRUCTURA_ESPACIO.md` (L735–L788) y `Data/mapas/README.md` (L793–L833)— incluye una sección de declaraciones equivalente a la §69 del informe. En contraste, `INFORME_TECNICO.md` sí declara herramientas, cuatro fases y protocolo de supervisión en §69 (L1487–L1491), tal como quedó registrado en `reviews/informe-tecnico-2026-11-28-iter4.v9-ethics.md` (F-V9-001). El criterio `V9.ai_use_declaration.master` se lee: «Declaration expected; should name tools, phases (research, drafting, code generation, translation), and supervision protocol». La documentación de cara al usuario conserva las cifras y los artefactos generados por ese proceso sin trasladar la declaración. No se recibió `v7_ai_density_hint` y `reviews/` no contiene artefacto V7 del corpus, de modo que no se emite hallazgo cruzado de densidad.

— polarity: negative · confidence: high · related: [[#F-V9-005]] · criteria: V9.ai_use_declaration.master

### F-V9-002 — «No recopila datos personales de anunciantes» contradice los teléfonos almacenados y la salvedad de §71.15

`README.md` declara en «Marco legal y límites»: «El proyecto respeta los términos de uso de los portales: no elude mecanismos anti-automatización, no recopila datos personales de anunciantes y conserva la procedencia de cada dato» (L112). El propio corpus describe lo contrario en `ARQUITECTURA_DATOS.md`: la copia compacta contiene «10.217 anuncios, 812 autos, 23.143 imágenes, 11.620 revisiones, 12.338 teléfonos y 716 precios» (L502–L504), y `Data/mapas/README.md` define la tabla `elementos` con «nombre, coordenadas, dirección, fuente, URL, teléfono, horario, precio, estado y detalle crudo en JSON» (L802). La declaración de §71.15 del informe es más precisa: «los anuncios contienen datos de contacto que se excluyen de la publicación» (L1553; «listing contact details are excluded from publication», L1555), en coherencia con la restricción de §10 de «aplicar solo datos agregados, sin nombres, teléfonos ni información personal de anunciantes» (L128). Esa formulación describe una recolección con exclusión en la publicación; la del corpus describe una no recolección. El criterio `V9.data_ethics.master` condiciona consentimiento y aprobación a su aplicabilidad; aquí la divergencia no es de procedimiento sino de hecho declarado sobre los mismos anuncios.

— polarity: negative · confidence: high · related: [[#F-V9-003]] · criteria: V9.data_ethics.master

### F-V9-003 — Encuestas y entrevistas circulan en el storytelling sin declaración de consentimiento, anonimización ni comité

`README.md` enumera entre los insumos «una serie de entrevistas y encuestas» (L12), y el storytelling las convierte en cifras públicas: «Entre las 28 personas a las que les interesaría comprar, 14 prefieren el eléctrico; pero 16 de 18 no pagarían más de 4.000 USD por uno» y «Kia y Hyundai son las marcas modernas más vistas —28 y 25 de 30 entrevistas—» (L251). El barrido de «consentimiento», «anonimización», «anonimas», «comité de ética», «IRB» y «ethics committee» en el corpus devuelve cero coincidencias. §71.15 declara: «No se reclutaron sujetos humanos: la encuesta de 33 respuestas y las entrevistas se tratan como documentación de contexto, no como datos experimentales; no se requirió un procedimiento de anonimización ejecutado» (L1553; equivalente en L1555). El informe documenta en §50 que la encuesta fue «un Google Forms de 32 preguntas aplicado a 33 personas de 4 segmentos en un barrio de La Habana» y que las entrevistas «son cualitativas, anónimas salvo el grupo de AutosxCuba —que incluye nombres y requiere cuidado—» (L1289), además de la restricción de §7 «requieren consentimiento y sin datos personales» para redes sociales (L847). El corpus reproduce los agregados sin la línea de alcance que explique qué se hizo con esas respuestas y por qué no se consideran experimentales; la salvedad del grupo nominado y la restricción de datos agregados de §10 quedan fuera del texto de usuario.

— polarity: negative · confidence: high · related: [[#F-V9-002]] · criteria: V9.data_ethics.master

### F-V9-004 — La declaración de no eludir anti-automatización convive con el anti-bot del propio mapa

La misma frase de `README.md` (L112) afirma «no elude mecanismos anti-automatización». En `Data/mapas/README.md`, el apartado «Anti-bot» describe: «El scraper usa, en orden: `curl_cffi` con impersonación de Chrome/Safari, **`patchright`** (navegador real con fingerprint de Chrome) y **FlareSolverr** (`http://127.0.0.1:8191/v1`) para páginas como Cybo que devuelven 403 o verificación de seguridad» (L831–L833). §71.15 califica el tema como «no se considera de doble uso sensible, con la salvedad de que los anuncios contienen datos de contacto que se excluyen de la publicación» (L1553); ninguna de las tres técnicas queda cubierta por esa salvedad ni por la declaración del README. El criterio `V9.dual_use.master` «encourage[s]» la discusión en temas relevantes; el corpus declara una conformidad que sus propias notas técnicas matizan, sin glosa que relacione ambas afirmaciones.

— polarity: negative · confidence: medium · related: [[#F-V9-002]] · criteria: V9.dual_use.master

### F-V9-005 — Disponibilidad, licencia y COI: remisión de §71.15 sin equivalente en el corpus

§71.15 cierra con «La disponibilidad de datos y código se documenta en §71.5; la licencia queda pendiente de declaración» (L1553; equivalente en L1555) y con «Se declara ausencia de conflicto de intereses» (L1553). En el corpus, `README.md` da el nombre del repositorio —«*Repositorio:* `el-precio-de-moverse-en-cuba`» (L14)— y una lista de rutas de documentación (L103–L108), pero no imprime una URL: el barrido de «https://» en las 833 líneas devuelve cero coincidencias. La licencia aparece solo como tarea futura —«publicar el CSV limpio con licencia» (L611)— y no hay commit, etiqueta ni DOI que fije la versión que produjo las cifras. `V9.data_availability_statement.master` («Brief statement: where the data lives, how to obtain») queda parcialmente cubierto por las rutas y la tabla de fuentes (L63–L71); `V9.code_availability_statement.master` («"Code available at" statement with URL and brief description») no halla la URL en el corpus, aunque `reviews/corpus-documentacion-2026-11-28.e3-artifacts.md` (L6–L17) sí la registra en el lado de la auditoría. La declaración de COI de §71.15 tampoco se reproduce en el corpus; `V9.coi_statement.master` («Not required; tutor/advisor relationship implicit») la declara no exigible en este nivel, de modo que su ausencia no constituye brecha.

— polarity: neutral · confidence: high · related: [[#F-V9-001]] · criteria: V9.data_availability_statement.master, V9.code_availability_statement.master, V9.coi_statement.master

---
type: audit-artifact
phase: v9-ethics
slug: corpus-total-2026-11-28
generated_at: 2026-11-28T21:30:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/corpus-total-2026-11-28/corpus-total-2026-11-28.text.md
language: es
level: master
---

## Resumen

- La declaración de IA está completa en §69 (herramientas, cuatro fases y protocolo de supervisión) y `README.md` la referencia dos veces; los otros ocho bloques del corpus guardan silencio y no se recibió `v7_ai_density_hint` para contraste de densidad.
- Privacidad de anunciantes y anti-automatización quedan declaradas en `README.md` en términos compatibles con §10, §71.15 y el apartado «Anti-bot» del mapa; encuestas y entrevistas tienen declaración de alcance y anonimato, sin consentimiento ni comité.
- Licencia: `README.md` declara MIT + CC BY 4.0 mientras §71.5 y §71.15 la mantienen pendiente; COI y disponibilidad de datos/código sí están declarados y no hay commit fijado.

### F-V9-001 — Declaración de IA completa en §69 y referida desde README, sin equivalente en los otros ocho bloques

§69 (`INFORME_TECNICO.md`, L1496–L1500) contiene la declaración: «Las herramientas de IA (OpenCode/Claude Code con las skills `review`, `deep-research` y `technical-writing`) se usaron en investigación, redacción, código y traducción. Cada cifra se contrastó contra los CSV versionados y las pruebas automatizadas; la huella queda en `reviews/`.» La versión en inglés (L1500) replica herramientas, fases y contraste, y añade el caso del R² 0,277 corregido a 0,274. El criterio `V9.ai_use_declaration.master` exige declaración con herramientas, fases y protocolo de supervisión: los tres componentes están presentes. `README.md` traslada el puntero en dos lugares —«El uso de IA en redacción, código y auditoría se describe en §69 del informe técnico» (L1768) y «El uso de IA en redacción, código y auditoría se declara en §69 del informe técnico» (L1770)—. El barrido de «IA generativa», «uso de IA», «OpenCode», «Claude Code», «ChatGPT» y «AI use» sobre los diez bloques da cuatro coincidencias en `INFORME_TECNICO.md` (L1306 es una ruta `/tmp/opencode`, no una declaración) y dos en `README.md`; cero en storytelling, modelos, arquitectura, alcance, automatización, estructura, mapas y referencias. No se recibió `v7_ai_density_hint` y `reviews/` no contiene artefacto V7 de este slug, de modo que no se emite hallazgo cruzado de densidad.

— polarity: positive · confidence: high · related: [[#F-V9-006]] · criteria: V9.ai_use_declaration.master

### F-V9-002 — Privacidad de anunciantes: «no publica» sustituye a «no recopila» y coincide con §10 y §71.15

`README.md` (L1770) declara ahora: «no publica datos personales de anunciantes —los teléfonos se almacenan en la base de trabajo pero se excluyen de la publicación—». Esa formulación coincide con la restricción de §10, «aplicar solo datos agregados, sin nombres, teléfonos ni información personal de anunciantes» (L137), y con §71.15, «los anuncios contienen datos de contacto que se excluyen de la publicación» (L1562). El almacenamiento declarado también coincide con los inventarios del corpus: 12.338 teléfonos en la copia compacta (`ARQUITECTURA_DATOS.md`, L2161) y el campo `teléfono` de la tabla `elementos` (`Data/mapas/README.md`, L2460), además de los 7.699 teléfonos del reporte de scrapeo (L942). De los diez bloques, solo `INFORME_TECNICO.md` (L137, L1562) y `README.md` (L1770) contienen la declaración de privacidad; los ocho restantes registran campos o cifras sin glosa de publicación. La divergencia de hecho señalada en la pasada anterior (`corpus-documentacion-2026-11-28.v9-ethics.md`, F-V9-002) ya no aparece en el texto cacheado.

— polarity: positive · confidence: high · related: [[#F-V9-004]] · criteria: V9.data_ethics.master

### F-V9-003 — Encuestas y entrevistas: alcance y anonimato declarados, sin declaración de consentimiento ni de comité

§71.15 declara: «No se reclutaron sujetos humanos: la encuesta de 33 respuestas y las entrevistas se tratan como documentación de contexto, no como datos experimentales; no se requirió un procedimiento de anonimización ejecutado» (L1562; «No human subjects were recruited… no executed anonymisation procedure was required», L1564). El storytelling añade una delimitación de publicación: «Las respuestas son agregadas y anónimas; el grupo documentado en `Data/repos-autos-referencias/ENCUESTAS_Y_ENTREVISTAS.md` que incluye nombres se usa solo como contexto interno y no se publica» (L1909). Ambas declaraciones conviven con la descripción de §50: «un Google Forms de 32 preguntas aplicado a 33 personas de 4 segmentos en un barrio de La Habana» y entrevistas «anónimas salvo el grupo de AutosxCuba —que incluye nombres y requiere cuidado—» (L1298), y con la condición de las redes sociales en §4: «No verificables como fuente estadística; requieren consentimiento y sin datos personales» (L856). El barrido de «consentimiento», «anonimización», «comité de ética», «IRB» y «ethics committee» da una sola coincidencia en el corpus (L856, referida a redes sociales) y ninguna declaración de consentimiento para las 33 respuestas ni aprobación de comité. `README.md` solo enumera el insumo —«una serie de entrevistas y encuestas» (L1623)—. El criterio `V9.data_ethics.master` condiciona consentimiento y aprobación a su aplicabilidad; el documento argumenta la no aplicabilidad y registra la exclusión del grupo nominado, sin que conste declaración de consentimiento en ninguno de los diez bloques.

— polarity: neutral · confidence: high · related: [[#F-V9-002]] · criteria: V9.data_ethics.master

### F-V9-004 — Anti-automatización: README declara fingerprint y FlareSolverr para 403 públicos junto a «no se eluden»

`README.md` (L1770) califica la afirmación de conformidad: «no sortea muros de pago ni accede a áreas privadas —para contenido público que devuelve 403 se documenta el bloqueo y se usa navegación con fingerprint de Chrome y FlareSolverr—». Esa glosa cubre las técnicas que el propio corpus describe: §12 registra «No se eluden mecanismos anti-automatización; los HTTP 403/429 se registran como limitación» (L136) y la fila «carrosw anti-bot | Registrado como limitación; no se falsificó su contenido» (L147); §41 consigna «Cybo devolvió 403 con curl_cffi, por lo que se aplicó el stack anti-bot disponible: `patchright` (Chromium con fingerprint de Chrome) y FlareSolverr en `http://127.0.0.1:8191/v1`» (L1208); y `Data/mapas/README.md` abre su apartado «Anti-bot» con «El scraper usa, en orden: `curl_cffi` con impersonación de Chrome/Safari, **`patchright`** (navegador real con fingerprint de Chrome) y **FlareSolverr** (`http://127.0.0.1:8191/v1`) para páginas como Cybo que devuelven 403 o verificación de seguridad» (L2489–L2491). La limitación subsistente se registra además en L1772 («`carrosw` está detrás de verificación de bots»). La declaración de usuario y las notas técnicas coinciden en el alcance —contenido público, sin muros de pago—; la frase absoluta de L136 permanece sin esa calificación en el propio §12. De los diez bloques, tres tratan el tema (informe, README, mapas); los otros siete no lo mencionan.

— polarity: positive · confidence: medium · related: [[#F-V9-002]] · criteria: V9.dual_use.master

### F-V9-005 — Licencia declarada en README pero pendiente en §71.5 y §71.15

`README.md` (L1768) declara: «Licencia: código MIT y datos derivados CC BY 4.0; las fuentes de terceros se rigen por sus propias condiciones». En el mismo corpus, `INFORME_TECNICO.md` afirma lo contrario en dos puntos: «No se ha declarado todavía una licencia de datos o código» (§71.5, L1552) y «la licencia queda pendiente de declaración» / «a license is still pending» (§71.15, L1562 y L1564). `ALCANCE_Y_RETENCION.md` la sitúa entre acciones futuras: «publicar el CSV limpio con licencia y resumen ejecutivo de una página» (L2269). De los diez bloques, solo README declara la licencia, dos secciones del informe la niegan, uno la proyecta y seis guardan silencio. En la raíz del repositorio de trabajo no hay archivo `LICENSE` —los únicos localizados están bajo `Copias/` y pertenecen a repositorios terceros—, aunque `reviews/corpus-total-2026-11-28.e3-artifacts.md` (frontmatter, L6–L7) registra `repo_clone_status: success`. El criterio `V9.data_availability_statement.master` («Brief statement: where the data lives, how to obtain») y `V9.code_availability_statement.master` («"Code available at" statement with URL and brief description») no exigen licencia en este nivel; la observación es de coherencia interna entre declaraciones sobre el mismo repositorio.

— polarity: negative · confidence: high · related: [[#F-V9-006]] · criteria: V9.data_availability_statement.master, V9.code_availability_statement.master

### F-V9-006 — COI declarado en dos bloques; disponibilidad con URL y sin commit fijado

«Se declara ausencia de conflicto de intereses» (§71.15, L1562) y «No conflict of interest is declared» (L1564) se reproducen en `README.md`: «No se declara conflicto de intereses» (L1768). Los ocho bloques restantes no contienen declaración de COI. La disponibilidad consta en §71.5 —«el repositorio público es `https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba`» y las bases crudas «reconstruibles desde `chunks/MANIFEST.json`» (L1552)— y en `README.md` L1625 y L1768, con la misma URL y la nota de reconstrucción desde `Data/Revolico/chunks/MANIFEST.json`. `reviews/corpus-total-2026-11-28.e3-artifacts.md` (L6, L23) registra esa URL y el clonado correcto. No aparece commit, etiqueta ni DOI que fije la versión del código que produjo las cifras; `V9.code_availability_statement.master` pide URL y descripción breve, y la fijación a commit/DOI corresponde al nivel `phd`. El criterio `V9.coi_statement.master` («Not required; tutor/advisor relationship implicit») declara el COI no exigible en `master`, de modo que su presencia es una declaración adicional, no un requisito cubierto.

— polarity: positive · confidence: high · related: [[#F-V9-001]] · criteria: V9.coi_statement.master, V9.data_availability_statement.master, V9.code_availability_statement.master

### F-V9-007 — Doble uso: §71.15 lo descarta con salvedad y el corpus cita cuatro trabajos de ética de scraping

§71.15 declara: «El tema no se considera de doble uso sensible, con la salvedad de que los anuncios contienen datos de contacto que se excluyen de la publicación» (L1562; equivalente en L1564). La discusión se apoya en las entradas [21] Krotov y otros, *Legality and Ethics of Web Scraping*; [22] Brown y otros, *Web scraping for research*; [27] Essien y otros, *The Ethics of Web Scraping In Research*; y [28] Paige, *The Legality and Ethics of Web Scraping in Archaeology* (§71.14, L1590–L1596), todas presentes también en `Data/referencias.md` y `README.md`. La salvedad de contactos se materializa en la exclusión de publicación declarada en L1770 y en el registro de bloqueos de L136–L147. El criterio `V9.dual_use.master` «encourage[s]» la discusión en temas relevantes; el corpus la incluye, acotada a la procedencia y al manejo de datos de anunciantes.

— polarity: positive · confidence: medium · related: [[#F-V9-004]] · criteria: V9.dual_use.master

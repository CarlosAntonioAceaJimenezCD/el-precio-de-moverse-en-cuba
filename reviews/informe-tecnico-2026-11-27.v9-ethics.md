---
type: audit-artifact
phase: v9-ethics
slug: informe-tecnico-2026-11-27
generated_at: 2026-11-27T05:45:00Z
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27/informe-tecnico-2026-11-27.text.md
language: es
level: master
---

## Resumen

- §10 declara una regla operativa de recolección (no elusión de anti-automatización, registro de HTTP 403/429, solo datos agregados sin nombres ni teléfonos); no se localiza una declaración de uso de IA ni una declaración consolidada de disponibilidad de datos o código.
- §50 documenta la encuesta de 33 personas y las 30 + 30 + 8 entrevistas con anonimato parcial; no aparece declarado el consentimiento de los participantes ni una aprobación de comité de ética.
- No se recibió tabla de densidad de V7 para contraste ni clon verificado de E3; ausencia de COI y de declaración de doble uso se registran con el calibrado `master`, sin extenderlo a niveles superiores.

### F-V9-001 — Sin declaración de uso de IA en la investigación o la redacción

Búsqueda de «inteligencia artificial», «IA generativa», «uso de IA», «AI», «ChatGPT», «Claude», «asistencia» y «declaración» en las secciones 1–12 (L14–268), en el registro de altas §13 (L276–748) y en §14–§68 (L750–1462): no se localiza declaración alguna de herramientas de IA, fases de uso ni protocolo de supervisión. El único crédito textual con la sigla es `AutofillAiModelCache` en filas del registro de altas (L317–320), relativo a un directorio de caché del perfil de WhatsApp, no a una declaración de asistencia. §55 (L1341) consigna la instalación de habilidades de escritura y presentación, sin nombrar herramientas de IA. El criterio `V9.ai_use_declaration.master` se lee: «Declaration expected; should name tools, phases (research, drafting, code generation, translation), and supervision protocol». No se recibió el `v7_ai_density_hint`, por lo que no se emite hallazgo cruzado de densidad.

— polarity: negative · confidence: high · related: [] · criteria: V9.ai_use_declaration.master

### F-V9-002 — Regla operativa de recolección y exclusión de datos personales declarada en §10

§10 (L116) registra: «Condiciones de uso de cada portal: criterio operativo para la recolección. No se eluden mecanismos anti-automatización; los HTTP 403/429 se registran como limitación». La misma sección (L117) añade: «Protección de datos personales, ciberseguridad y derechos de autor: antes de publicar resultados deben verificarse las normas cubanas vigentes y aplicar solo datos agregados, sin nombres, teléfonos ni información personal de anunciantes». La versión inglesa reproduce ambos enunciados (§10 EN, L245–246). La regla reaparece como criterio de fuente en §18 (L823): «No verificables como fuente estadística; requieren consentimiento y sin datos personales», y como límite en §19 (L851): «precios pedidos no transaccionados, sesgo de supervivencia de anuncios, sin datos personales, vigencia normativa a verificar». El enunciado es operativo y prospectivo —«antes de publicar resultados»— y no nombra un marco de cumplimiento ni una revisión ya realizada. El criterio `V9.data_ethics.master` se lee: «Consent + IRB/ethics-committee approval named when applicable». La literatura de ética de scraping mapeada en E2 (P021, P022) coincide con el contenido de esta regla sin que el informe la cite.

— polarity: positive · confidence: high · related: [[#F-V9-003]], [[#P021]], [[#P022]] · criteria: V9.data_ethics.master

### F-V9-003 — Sin consentimiento ni aprobación de comité declarados para la encuesta y las entrevistas

§50 (L1265) describe: «la encuesta con datos reales fue un Google Forms de 32 preguntas aplicado a 33 personas de 4 segmentos en un barrio de La Habana». El mismo pasaje consigna: «Las entrevistas (30 + 30 + 8) son cualitativas, anónimas salvo el grupo de AutosxCuba —que incluye nombres y requiere cuidado—». E3 inventaría 33 respuestas de encuesta y 30 + 30 + 8 entrevistas entre las 25 tablas de `Data/repos-autos-referencias/referencias_autos.sqlite` (§50, L1263). La búsqueda de «consentimiento», «consent informado», «IRB», «comité de ética» y «aprobación» en todo el documento solo devuelve la expresión condicional de §18 (L823) —«requieren consentimiento»— y la verificación pendiente de §10 (L117). No hay declaración de consentimiento obtenido, de aprobación de comité ni de procedimiento de anonimización aplicado a los 33 encuestados; la única precisión sobre anonimato es la nota descriptiva de §50 referida a las entrevistas. El criterio `V9.data_ethics.master` se lee: «Consent + IRB/ethics-committee approval named when applicable».

— polarity: negative · confidence: high · related: [[#C063]], [[#F-V9-002]] · criteria: V9.data_ethics.master

### F-V9-004 — Procedencia y anonimato parcial registrados en el consolidado de encuestas y entrevistas

§50 (L1261) registra que la comparación de 233 archivos detectó, entre otros duplicados, «snapshots parciales de la encuesta, copias de entrevistas y tablas de reporte». El consolidado de §50 (L1263) conserva «33 respuestas de encuesta, 30 + 30 + 8 entrevistas» junto a «una tabla `provenancia`», con script reproducible en `Auxiliares/herramientas/consolidar_repos_autos.py`. La nota de §50 (L1265) precisa el estado del anonimato: «anónimas salvo el grupo de AutosxCuba —que incluye nombres y requiere cuidado—». El informe registra así la procedencia de los instrumentos y la excepción de identificación, sin una declaración de tratamiento para ese grupo con nombres. §17 (L793) menciona además una «encuesta a 130 comerciantes» del estudio PUCE como fuente externa, distinta de los 33 encuestados del proyecto.

— polarity: neutral · confidence: high · related: [[#C063]], [[#F-V9-003]] · criteria: V9.data_ethics.master

### F-V9-005 — Sin declaración de conflictos de interés; el nivel `master` no la requiere

La búsqueda de «conflicto de interés», «interés», «patrocinio», «financiación», «tutor», «asesor» y «agradecimientos» en §1–§68 no localiza declaración de COI. El cierre del documento (L1461) consigna únicamente «Firma / Signature: responsable del proyecto / project owner.» Cambios de rumbo se atribuyen a terceros sin identificar como patrocinadores: §15 (L767) «se detuvo manualmente `revolico-scrape.timer` y su servicio a petición del usuario» y §21 (L877) «A petición del usuario, el objetivo inmediato deja de ser la recomendación interactiva de compra». §67 (L1447) registra borrados «Con autorización explícita». El criterio `V9.coi_statement.master` se lee: «Not required; tutor/advisor relationship implicit». La ausencia no constituye una brecha en el calibrado de nivel `master`; tutors, patrocinadores ni financiadores aparecen nombrados.

— polarity: neutral · confidence: high · related: [] · criteria: V9.coi_statement.master

### F-V9-006 — Sin declaración de doble uso o impacto societario; tema fuera de la lista sensible

El objetivo declarado en §1 (L16) es un «análisis del mercado automotor cubano» y un pipeline de scraping; el documento no trata modelos de lenguaje, vigilancia, bioseguridad, armas autónomas ni diagnóstico clínico. §10, §18 y §19 contienen notas éticas y legales operativas, pero no una sección dedicada a impacto societario. La única proyección de alcance público, §63 (L1413), se etiqueta a sí misma: «es **inferencia de diseño, no medición**». El criterio `V9.dual_use.master` se lee: «Discussion encouraged for dual-use-relevant topics».

— polarity: neutral · confidence: medium · related: [[#F-V9-002]] · criteria: V9.dual_use.master

### F-V9-007 — Disponibilidad de datos: rutas, fragmentación y hashes sin declaración consolidada

El documento describe la localización y reconstrucción de los datos sin concentrarlas en un enunciado de disponibilidad. §14 (L752) declara: «La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**», con fragmentos de 16 MiB y `reconstruir_revolico.py`; la tabla de L759 registra 795373568 B, 48 partes y un prefijo SHA-256 `dadd2bffba615d8a…`. §54 (L1321) describe 82 fragmentos de 10 MB con `MANIFEST.json` y verificación de hashes. §53 (L1309–1311) documenta los anuarios del ONEI con URL, tamaño y SHA-256 por archivo en `INDICE.md`; §10 (L118) acota: «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe». No hay sección titulada «Disponibilidad de datos», ni condiciones de acceso o licencia propias consolidadas; la única licencia explícita del documento pertenece a una fuente externa, DfT/DVLA, en §18 (L814): «Open Government Licence». El inventario E3 marca como `unknown` la accesibilidad pública de varias bases propias. El criterio `V9.data_availability_statement.master` se lee: «Brief statement: where the data lives, how to obtain».

— polarity: neutral · confidence: high · related: [[#F-V9-008]] · criteria: V9.data_availability_statement.master

### F-V9-008 — Disponibilidad de código: repositorio nombrado por propietario y slug, sin URL completa ni versión fijada

§40 (L1136–1139) identifica el remoto con un bloque de texto: «antes: CarlosAntonioAceaJimenezCD/autodecide-habana / ahora: CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba»; L1141 añade que `gh` actualizó el remoto `origin`, y L1143 registra la descripción del repositorio. El texto no imprime la URL completa ni un enunciado de tipo «código disponible en», y no fija commit, tag o DOI para la versión que produjo los resultados. E3 consigna en su frontmatter `repo_url: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba` con `repo_clone_status: not-attempted`, y mapea las rutas de scripts declaradas en el documento a ubicaciones no verificadas en disco. El criterio `V9.code_availability_statement.master` se lee: «"Code available at" statement with URL and brief description».

— polarity: neutral · confidence: high · related: [[#F-V9-007]] · criteria: V9.code_availability_statement.master

### F-V9-009 — Única licencia explícita del documento corresponde a una fuente externa

La auditoría de fuentes §18 (L814) registra para DfT/DVLA: «Verificado en vivo: publicado por Department for Transport + DVLA, actualizado 23/09/2026, Open Government Licence». Ninguna otra fila de la tabla de §18 (L812–825) declara licencia, y no aparece licencia para el código propio ni para las bases propias inventariadas en E3 (`revolico.sqlite`, catálogos, `telegram.sqlite`, `referencias_autos.sqlite`). Los términos de uso de los portales se tratan en §10 (L116) como «criterio operativo para la recolección», sin que se registren condiciones de redistribución de los datos capturados. Los criterios `V9.data_availability_statement.master` y `V9.code_availability_statement.master` comprenden respectivamente «how to obtain» y una declaración con URL y descripción; el documento cubre rutas y procedencia, no régimen de licencias propias.

— polarity: neutral · confidence: high · related: [[#F-V9-007]], [[#F-V9-008]] · criteria: V9.data_availability_statement.master

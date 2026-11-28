---
type: audit-artifact
phase: v9-ethics
slug: informe-tecnico-2026-11-27-iter3
generated_at: 2026-11-28T01:10:59-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter3/informe-tecnico-2026-11-27-iter3.text.md
language: es
level: master
---

## Resumen

- §69 (L1467–L1471) ya satisface `V9.ai_use_declaration.master`: nombra OpenCode/Claude Code con las skills `review`, `deep-research` y `technical-writing`, declara cuatro fases y explica el protocolo de supervisión.
- La calibración cierra F-V9-002 y F-V9-003 de la iteración 2 (herramientas genéricas; generación de código y traducción omitidas); E3 confirma el repositorio versionado que la declaración invoca.
- Sin `v7_ai_density_hint` ni artefacto V7 de esta iteración no se emite hallazgo cruzado de densidad; los demás criterios V9 se registran en nivel master sin incumplimiento exigible.

### F-V9-001 — Declaración de uso de IA completa en §69: herramientas nominales, cuatro fases y protocolo de supervisión

§69 lleva por título «Declaración de uso de inteligencia artificial / AI-use declaration» (L1467). La versión ES declara: «Las herramientas de inteligencia artificial (OpenCode/Claude Code con las skills `review` de MatCom, `deep-research` y `technical-writing`) se utilizaron en cuatro fases: investigación y verificación de fuentes, redacción y edición de la narrativa, generación y revisión de código, y traducción bilingüe» (L1469). La versión EN reproduce la declaración: «AI tools (OpenCode/Claude Code with MatCom's `review` skill, `deep-research` and `technical-writing`) were used in four phases: research and source verification, drafting and editing, code generation and review, and bilingual translation» (L1471). El protocolo de supervisión se explicita en el mismo párrafo: «contrastar toda cifra contra los CSV y bases versionados, ejecutar las pruebas automatizadas y conservar el registro de auditoría en `reviews/`; ninguna salida de IA se aceptó sin ese contraste» (L1469), con equivalente en L1471. La procedencia se refuerza: «Las cifras, los modelos estadísticos y las decisiones de diseño provienen de los datos y del código versionados en este repositorio; ninguna afirmación empírica se originó en una salida de IA sin contraste contra los archivos» (L1469). El criterio `V9.ai_use_declaration.master` exige: «Declaration expected; should name tools, phases (research, drafting, code generation, translation), and supervision protocol». Aquí concurren los tres elementos: herramientas nominales, las cuatro fases del criterio y un protocolo con criterio de aceptación verificable. La firma de cierre (L1522), «responsable del proyecto / project owner», atribuye la declaración. Este hallazgo sustituye la calibración de la iteración 2, donde F-V9-002 señalaba herramientas genéricas y F-V9-003 omitía código y traducción (`reviews/informe-tecnico-2026-11-27-iter2.v9-ethics.md`).

— polarity: positive · confidence: high · related: [[#F-V9-002]] · criteria: V9.ai_use_declaration.master

### F-V9-002 — Las cuatro fases declaradas corresponden a evidencia interna del documento y a la infraestructura de E3

La fase de generación y revisión de código (L1469/L1471) corresponde a las herramientas creadas que enumera §6: «`ddg_research.py`, `buscar_fallback.py`, `descargar_hombros.py`, `scrape_concesionarios.py`, `resumen_catalogos.py` y `actualizar_informe.py`» (L74), al scraper con adaptadores por dominio de §8 (L90) y al comando único y semilla de §71.5 (L1516). La investigación y verificación de fuentes corresponde a §5 (L62, 409 resultados) y §7 (L78–L86), y la traducción bilingüe a las dos versiones ES/EN de cada sección, incluidas las de §69 (L1469, L1471). E3 registra `repo_url: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba`, `repo_clone_status: success` y último commit `ee994cd` (`reviews/informe-tecnico-2026-11-27-iter3.e3-artifacts.md`, L6–L23), coherente con la procedencia «versionados en este repositorio» y con el registro de auditoría bajo `reviews/` invocado en L1469. No se recibió `v7_ai_density_hint`: no hay sección marcada con densidad `high` pendiente de cobertura, por lo que no se emite hallazgo cruzado con V7.

— polarity: positive · confidence: high · related: [[#F-V9-001]] · criteria: V9.ai_use_declaration.master

### F-V9-003 — Protección de datos personales declarada como requerimiento; sin sujetos humanos ni comité de ética aplicables

El documento registra la restricción en forma explícita: «antes de publicar resultados deben verificarse las normas cubanas vigentes y aplicar solo datos agregados, sin nombres, teléfonos ni información personal de anunciantes» (L119; equivalente EN en L250), y la reitera para fuentes sociales: «No verificables como fuente estadística; requieren consentimiento y sin datos personales» (L827) y «sin datos personales» (L851, L855). La búsqueda de «IRB», «comité de ética» y «ethics committee» no devuelve coincidencias; el criterio `V9.data_ethics.master` condiciona consentimiento y aprobación a que sean aplicables. El corpus son anuncios públicos de compraventa y series agregadas, no sujetos humanos reclutados, por lo que no se observa incumplimiento exigible en este nivel, aunque el documento no describe un procedimiento de anonimización ejecutado más allá de la exclusión declarada de datos personales.

— polarity: neutral · confidence: high · related: [] · criteria: V9.data_ethics.master

### F-V9-004 — Conflicto de intereses: ausencia registrada, no requerida en nivel master

Búsqueda de «conflicto de intereses», «conflicts of interest», «sponsor», «financiación» y «funding» en el documento: sin declaración formal. La única coincidencia de «conflicto» es narrativa —«relato en 10 actos con personajes, conflicto, hallazgos» (L1130)—. El criterio `V9.coi_statement.master` indica «Not required; tutor/advisor relationship implicit», por lo que la ausencia no constituye hallazgo negativo; se registra solo para completar el barrido de declaraciones.

— polarity: neutral · confidence: high · related: [] · criteria: V9.coi_statement.master

### F-V9-005 — Impacto / doble uso: tema no sensible en el sentido del criterio, con salvedad de datos personales y copyright

El objeto del informe (precios de automóviles en Cuba, conversiones y análisis estadístico) no figura entre los temas sensibles enumerados en `V9.dual_use` (LLMs, vigilancia, biosecuridad, armas autónomas, diagnóstico clínico). En nivel master la discusión se «encourage[d]», y el documento registra la salvedad de «Protección de datos personales, ciberseguridad y derechos de autor» (L119/L250) además de las amenazas a la validez de §71.4 (L1507–L1512). No hay declaración formal de impacto social; no es exigible en este nivel.

— polarity: neutral · confidence: high · related: [] · criteria: V9.dual_use.master

### F-V9-006 — Disponibilidad de datos y código: ubicaciones versionadas documentadas, sin licencia ni commit fijados en el informe

Para `V9.data_availability_statement.master` («Brief statement: where the data lives, how to obtain»), el documento cumple en lo esencial: §56 documenta el árbol versionado en `Data/estructura_github.md` (1.288 archivos, 157 objetos LFS; L1353), §68 remite a `Data/ESTRUCTURA_ESPACIO.md` (L1459) y E3 inventaria las bases en `Data/Revolico/revolico.sqlite`, `Data/analisis_rentabilidad/data/compacto/` y `Data/analisis_rentabilidad/outputs/tables/modelo_muestra.csv` (L148–L154). Para `V9.code_availability_statement.master` («"Code available at" statement with URL and brief description»), §40 consigna el renombre a `el-precio-de-moverse-en-cuba` (L1138–L1145) y E3 da la URL completa y el commit `ee994cd`, pero el informe no imprime la URL ni fija commit/DOI en una sección formal de disponibilidad. Licencia de datos/código no declarada. Se trata de una precisión deseable, no de un incumplimiento del nivel master.

— polarity: neutral · confidence: medium · related: [[#F-V9-001]] · criteria: V9.data_availability_statement.master, V9.code_availability_statement.master

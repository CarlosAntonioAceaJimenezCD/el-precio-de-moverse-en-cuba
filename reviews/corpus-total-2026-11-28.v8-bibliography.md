---
type: audit-artifact
phase: v8-bibliography
slug: corpus-total-2026-11-28
generated_at: 2026-11-28T21:30:00-05:00
audited_document: .playground/audit-cache/corpus-total-2026-11-28/corpus-total-2026-11-28.text.md
language: es
bibliography_entries_total: 41
verified: 37
unverified: 4
---

# V8 — Integridad bibliográfica — corpus total

Nota de método y alcance. El bloque bibliográfico del corpus vive en dos sitios: la sección «Documentación» del README (corpus L1716–L1757; `README.md` L96–L137) y el anexo `Data/referencias.md` reproducido como archivo separado (corpus L2496–L2584). El mandato recibido es el cotejo de las 41 entradas del README contra ese anexo, los flags campo por campo, la entrada [39] y la contradicción de Akerlof. En consecuencia: (a) `verified: 37` / `unverified: 4` sigue la convención declarada por el anexo (L4–L6), que cuenta como no verificadas las cuatro entradas marcadas `(metadata incomplete)` —[1], [10], [12] y [39]—, no papers inexistentes; (b) en esta pasada se ejecutaron ocho fetch en vivo: las dos URL de [39]–[41] y GOV.UK profunda, Crossref de [1], el arXiv de [24] y los DOI de [27] y [9], más ANFAC y AEADE; los restantes metadatos se heredan de la verificación del 27/11/2026 consignada en el anexo; (c) los números de línea del corpus corresponden a la copia en caché del frontmatter y los de `Data/referencias.md` al archivo de trabajo; (d) el criterio del evaluador de no reclamar enlace roto cuando el fallo es de transporte se aplica también aquí.

## Hallazgos

### F-V8-001 — El README reproduce las 41 entradas como prefijos truncados a ~155 caracteres

Cotejo entrada por entrada: las 41 líneas `- [N]` del README (L97–L135) son, tras quitar el viñeta y el salto de línea, **prefijos estrictos** de las 41 líneas `^[N]` de `Data/referencias.md` (L8–L87). No hay ninguna divergencia de contenido: el README no introduce autor, título, año, venue ni identificador que el anexo no tenga. La diferencia es de longitud. 38 de las 41 líneas del README fueron cortadas a 153–155 caracteres, en mitad de una palabra o de un campo; solo [40] (129 caracteres) y [41] (126) están completos, y [20] está completo respecto a la plantilla básica y pierde únicamente la nota «9 citas verificadas en OpenAlex el 27/11/2026».

Los cortes destructivos, citados verbatim: [1] termina en «https://doi.org/10» (L97) frente a «https://doi.org/10.2307/1879431. Citada en el informe: sí. **(metadata incomplete: resumen indexado no sustantivo; identidad y DOI verificados en OpenAlex)**» del anexo (L8); [4] en «https://doi.org/10.» (L100); [14] en «https://doi.» (L110); [18] en «arXiv:2403.038» (L114); [30] en «https://doi.org/» (L126); [12] en «https://newyorkfed.org/research/ep» (L108); [39] en «**(metadata incompl» (L135). El mismo bloque truncado se reproduce en la copia cacheada del corpus (L1717–L1755). Los campos que desaparecen en el README son, según la entrada, el sufijo del DOI, la URL completa, el nombre del venue, el campo `Citada en el informe` y la marca `(metadata incomplete)`. El encabezado «**Referencias y trabajos cercanos (41):** ver `Data/referencias.md`» (L96) remite al anexo completo, de modo que el README funciona como índice severado antes que como bibliografía resoluble.

— polarity: negative · confidence: high · related: [[#F-V8-002]], [[#F-V8-003]], [[#F-V8-004]]

### F-V8-002 — Los cuatro flags del anexo declaran el campo afectado y el resto de matices también son de campo

El anexo no usa una etiqueta genérica: cada una de las cuatro marcas nombra su campo. [1] L8: `(metadata incomplete: resumen indexado no sustantivo; identidad y DOI verificados en OpenAlex)`; [10] L26: `(metadata incomplete: resumen no indexado; campos bibliográficos verificados)`; [12] L30: `(metadata incomplete: PDF no extraido)`; [39] L83: `(metadata incomplete: URL profunda no confirmada)`. La consulta de esta pasada a `https://api.crossref.org/works/10.2307/1879431` devolvió HTTP 200 con autor «George A. Akerlof», contenedor *The Quarterly Journal of Economics*, volumen 84, número 3, página 488, `published` 1970-08 y título coincidente: la identidad y el DOI de [1] quedan confirmados también por Crossref, y el campo abierto es solo el resumen. La marcas de [10] y [12] delimitan, respectivamente, un resumen no indexado y un PDF no extraído; la de [39] quedó resuelta en vivo (F-V8-003).

Cinco entradas sin flag conservan asimismo precisiones de campo que el README no alcanza a mostrar: [2] L10 registra «el registro OpenAlex indexa la versión SSRN de 2010; la publicación AER es de 2011»; [18] L42 anota 13 citas y la versión publicada en IEEE BigData 2024; [19] L44 anota 96 citas y la discrepancia preprint 2017 / publicación 2018; [20] L46 anota 9 citas; [38] L82 anota 2015 en OpenAlex frente a 2016 en Crossref. En el README, las cinco se cortan antes de esas notas (L98, L114–L116, L134), igual que las cuatro marcas del párrafo anterior.

— polarity: positive · confidence: high · related: [[#F-V8-001]], [[#F-V8-005]]

### F-V8-003 — [39]: la URL profunda de estadísticas de vehículos resolvió en esta pasada

El anexo registra: «[39] Department for Transport / DVLA. Vehicle statistics. GOV.UK. https://www.gov.uk/government/organisations/department-for-transport. **(metadata incomplete: URL profunda no confirmada)**. Citada en el informe: sí (§70 y §71.14).» (`Data/referencias.md` L83). Las dos verificaciones en vivo de hoy dan resultado positivo. La sede `https://www.gov.uk/government/organisations/department-for-transport` responde con la página del Department for Transport, el apartado «Research and statistics», noticias hasta el 27/11/2026 —incluida «Tracy Westall OBE appointed as DVLA Chair» del 23/11— y licencia «Open Government Licence v3.0». La URL profunda `https://www.gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files` responde igualmente: «Vehicle licensing statistics data files», «From: Department for Transport and Driver and Vehicle Licensing Agency», publicada el 24/05/2022 y con última actualización el 23/09/2026, con series `df_VEH0120`, `df_VEH0124`, `df_VEH0125` y otras.

El motivo literal del flag de [39] —la URL profunda no confirmada— queda así cerrado por observación directa en la fecha de la auditoría, sin que la entrada haya cambiado de texto. El propio §70 nombra a «UK Department for Transport / DVLA, estadísticas de vehículos (GOV.UK)» en las dos versiones (corpus L1506 y L1508), coherente con la atribución institucional. [40] ANFAC (`https://anfac.com/`) y [41] AEADE (`https://www.aeade.net/`) también responden: la primera como asociación española con matriculaciones de octubre de 2026 y cifras de 2025; la segunda se identifica como «Asociación de Empresas Automotrices del Ecuador», con apartado «Estadísticas → Anuarios» y boletines Ene–sep 2026, precisión nacional que el anexo no declara y que no contradice su ficha.

— polarity: positive · confidence: high · related: [[#F-V8-001]], [[#F-V8-004]]

### F-V8-004 — [39]: el campo `Citada` remite a un §71.14 cuya tabla termina en [38]

La ficha [39] fija su ubicación como «Citada en el informe: sí (§70 y §71.14)» (`Data/referencias.md` L83; corpus L2580). La tabla de §71.14 (corpus L1568–L1607) contiene 38 filas, de [1] a [38], y se cierra con la fila de Quariguasi Frota Neto et al.; [39], [40] y [41] no tienen fila en ella. La mitad §70 de la atribución sí se cumple: L1506 y L1508 nombran a DfT/DVLA, ANFAC y AEADE entre las referencias verificadas. La mitad §71.14 no. El mismo desfase se invierte respecto a la pasada iter4: allí §70 anunciaba «38 referencias» frente a un anexo de 41; aquí §70 ya escribe «La convención numerada de 41 referencias y su estado de verificación están en `Data/referencias.md`» (L1506/L1508), mientras la tabla de §71.14 sigue desplegando 38 filas. El recuento quedó corregido en el texto, no en el cuadro.

— polarity: negative · confidence: high · related: [[#F-V8-003]], [[#F-V8-005]]

### F-V8-005 — Akerlof [1]: la doble etiqueta «verificada» / `(metadata incomplete)` se reproduce en español y en inglés

El corpus escribe en §70 ES: «Referencias citadas y verificadas externamente durante la auditoría: Akerlof (1970), *The Market for "Lemons"* (DOI 10.2307/1879431 confirmado en OpenAlex; el resumen indexado es solo un índice de secciones, por lo que su flag es `(metadata incomplete: resumen)`)» (L1506). El espejo EN repite: «Externally verified references cited during the audit: Akerlof (1970), *The Market for "Lemons"* (DOI 10.2307/1879431 confirmed in OpenAlex; the indexed abstract is only a section index, so its flag is `(metadata incomplete: abstract)`)» (L1508). Ambas versiones encuadran a Akerlof dentro de las referencias «verificadas externamente» y, en la misma oración, le asignan un flag que la convención del anexo define como «algún campo no pudo confirmarse; esas entradas no se presentan como referencias verificadas» (`Data/referencias.md` L4–L6). La ficha [1] (L8) sostiene la marca: «Citada en el informe: sí. **(metadata incomplete: resumen indexado no sustantivo; identidad y DOI verificados en OpenAlex)**».

La contradicción es de etiquetado, no de identidad: el fetch a Crossref de hoy confirma autor, revista, volumen, página y año, y OpenAlex había confirmado el DOI y el carácter de índice de secciones del resumen. La cláusula parentética de §70 ya nombra el campo, de modo que la incompatibilidad queda circunscrita a la clasificación de apertura («verificadas») frente a la convención; se reproduce por duplicado en los dos textos del apartado bilingüe, que es la «ambas partes» del mandato.

— polarity: negative · confidence: high · related: [[#F-V8-002]], [[#F-V8-004]], [[#F-V8-006]]

### F-V8-006 — Akerlof [1]: §71.14 atribuye su discusión a §71.6, donde no comparece

El cierre de §71.14 afirma: «Los trabajos [1], [9], [14], [26] y [29] se discuten además en §71.6; el resto se registra aquí con su marcador numérico y se enlaza a `Data/referencias.md`» (corpus L1609). El párrafo de §71.6 (L1558) contiene cuatro oraciones con marcadores `[14]`, `[26]`, `[9]` y `[29]`; Akerlof no aparece en él. Sus apariciones sustantivas están en la tabla de fuentes (L826, «Asimetría de información (Akerlof)», sin marcador), en el marco teórico (L870, «asimetría de información (Akerlof [1])»), en la ficha [1] de §71.14 (L1570, con el título truncado en «Market Mech») y en §70 (L1506/L1508). El campo `Citada: sí` de [1] es correcto; la guía de ubicación de §71.14 no lo es. Es un mismatch de contexto de citación: el marcador existe, pero no en el apartado que la tabla señala.

— polarity: negative · confidence: high · related: [[#F-V8-005]]

### F-V8-007 — Los tres identificadores de aspecto sospechoso y el bloque institucional resuelven con coincidencia de título y autores

Verificación dirigida de los casos prioritarios del evaluador, todos con resultado positivo en esta pasada:

- `[24]` (`Data/referencias.md` L54): «arXiv:2601.14311 (manuscrito enviado a ACM Computing Surveys) (2026)». `https://arxiv.org/abs/2601.14311` → página activa, «Submitted on 19 Jan 2026», título «Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability in LLMs» y los seis autores Hohensinner, Mutlu, Mendoza Estrada, Vukovic, Kopeinik y Kern coincidentes; «Comments: 35 pages, 6 figures. Manuscript submitted to ACM Computing Surveys (CSUR) on the 12th of December 2025». El prefijo `2601` es anterior a la fecha del corpus: no hay ID imposible.
- `[27]` (L60): «https://doi.org/10.54660/.jfmr.2023.4.1.529-538». El punto inicial del sufijo (`/.jfmr`) resuelve a Essien, Adebayo, Afuwape, Eboseremen, Oladega y Soneye (2023), *Journal of Frontiers in Multidisciplinary Research* 4(1), 529–538, con el título completo del anexo: es un DOI registrado, no malformado.
- `[9]` (L24): «https://doi.org/10.54254/2754-1169/2026.38524». Resuelve a Du, Yang, Zhang, Li y Liu (2026), *Advances in Economics, Management and Political Sciences* 313(1), 134–143, con título y autores coincidentes.

Ningún DOI se repite entre entradas y las tres parejas preprint/publicación —[18] arXiv:2403.03812 con IEEE BigData 2024, [19] arXiv:1711.06970 con Springer 2018, [20] arXiv:2101.03788— están representadas por una sola ficha cada una.

— polarity: positive · confidence: high · related: [[#F-V8-003]], [[#F-V8-008]]

### F-V8-008 — Estructura del anexo: 41 numeraciones sin huecos, sin duplicados y sin entradas fantasma

`Data/referencias.md` contiene 41 líneas `^[n]` de [1] a [41], sin números ausentes ni repetidos; el README replica exactamente la misma serie (L97–L135). Las 41 fichas llevan autor nominal o institución nominal, título en cursiva, venue o sede, año o fecha institucional y un identificador resoluble (DOI, arXiv o URL), con dos únicas excepciones de plantilla —[39]–[41], entradas corporativas sin año— que son la convención del género, no una omisión. No aparece ningún título genérico de paper fantasma, ninguna entrada sin atribución y ningún DOI duplicado. La verificación en vivo de ocho de las entradas más expuestas (F-V8-003, F-V8-005, F-V8-007) coincide en todos los casos con el título, los autores y el venue declarados.

— polarity: positive · confidence: high · related: [[#F-V8-001]], [[#F-V8-007]]

## Resumen (3 líneas)

1. El README copia las 41 entradas como prefijos estrictos del anexo pero corta 38 a ~155 caracteres, con pérdida de sufijos de DOI, URL, venue, campo `Citada` y de las cuatro marcas `(metadata incomplete)`.
2. Los flags son por campo y las ocho verificaciones en vivo los delimitan o cierran: Crossref confirma la identidad de Akerlof (el flag es el resumen), la URL profunda de [39] resuelve hoy, y el arXiv:2601.14311, los DOI `10.54660/.jfmr…` y de [9], ANFAC y AEADE son reales.
3. Quedan tres inconsistencias de etiquetado: la doble clasificación de Akerlof en §70 ES/EN, la atribución errónea de [1] a §71.6 y el campo de [39] que remite a una tabla de §71.14 que se detiene en [38] mientras §70 ya anuncia 41 referencias.

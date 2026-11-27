---
type: audit-artifact
phase: v8-bibliography
slug: informe-tecnico-2026-11-27-iter2
generated_at: 2026-11-27T21:16:29Z
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter2/informe-tecnico-2026-11-27-iter2.text.md
language: es
bibliography_entries_total: 38
verified: 6
unverified: 32
---

## Resumen

- La enumeración `[1]`–`[38]` en `Data/referencias.md` es nueva en esta iteración; los seis marcadores `(metadata incomplete)` concentran todo el flag del aparato y las 32 fichas restantes no se re-verificaron en esta pasada dirigida.
- Los tres conteos recuperados por E2 se confirman en OpenAlex —`[18]` 13, `[19]` 96, `[20]` 9 citas— junto con los DOI de las versiones publicadas de `[18]` y `[19]`, que las fichas no incorporan.
- La contradicción Akerlof entre §70 («verificada externamente (Crossref/OpenAlex)») y `[1]` (`(metadata incomplete)`) subsiste porque la ficha no nombra el campo incompleto: OpenAlex confirma la identidad, el resumen es solo un índice de secciones y Crossref no respondió en esta pasada.

## Alcance y método

Se tomó como bibliografía del documento la lista numerada de 38 entradas de `Data/referencias.md`, anexo enlazado desde la nueva §70 (L1475–1479), y no las 36 menciones nominales dispersas que se auditaron en la iteración 1. La re-verificación se ejecutó el 2026-11-27 contra OpenAlex API (6 registros por ID) y Crossref API (1 registro), con foco en los seis marcadores heredados o nuevos y en las cuatro fuentes institucionales que §70 declara verificadas; E2 de iter2 aporta las verificaciones de páginas institucionales y el historial de la pasada 1. En el frontmatter, `verified: 6` cuenta las fichas re-verificadas en vivo aquí y `unverified: 32` las que quedan fuera de esta pasada dirigida: no es un juicio sobre su existencia ni una declaración de obra fantasma.

Los fetch a `https://api.openalex.org/works/W4406461714`, `W2770052903`, `W3120241027`, `W2156109180`, `W7134932779` y `W1991842457` devolvieron registro completo. El fetch a `https://api.crossref.org/works/10.2307/1879431` devolvió `{"error":{"type":"unknown","message":"Transport error (GET https://api.crossref.org/works/10.2307/1879431)"}}`, reproduciendo el HTTP 429 que E2 consignó para Akerlof. Ningún campo ausente se completó por inferencia.

### F-V8-001 — Seis marcadores genéricos cubren cinco causas de campo distinto

`Data/referencias.md` emplea la misma etiqueta `(metadata incomplete)` en `[1]`, `[10]`, `[18]`, `[19]`, `[20]` y `[38]` sin indicar qué campo falta. La re-verificación muestra que el motivo no es homogéneo y que en tres casos el marker ya no corresponde a ningún campo:

| Entrada | Campo realmente afectado | Hallazgo de esta pasada |
|---|---|---|
| `[1]` Akerlof | resumen: `abstract_inverted_index` solo con índice de secciones; Crossref sin contraste | identidad completa en OpenAlex (DOI `10.2307/1879431`, W2156109180) |
| `[10]` Kang & Fu | resumen: `abstract_inverted_index: null` | título, autores, afiliación, vol. 216/art. 111964 y 3 citas confirmados |
| `[18]` ProbSAINT | ninguno: el motivo (citas no verificables por HTTP 403) quedó resuelto | 13 citas y DOI publicado `10.1109/bigdata62323.2024.10825740` |
| `[19]` Pal et al. | ninguno: motivo resuelto; falta consignar año y DOI de la versión publicada | 96 citas, `2018`, DOI `10.1007/978-3-030-03402-3_28` |
| `[20]` Arefin | ninguno: motivo resuelto | 9 citas, DOI `10.48550/arxiv.2101.03788` |
| `[38]` Quariguasi | resumen no indexado con texto completo accesible; año 2015 vs 2016 | 136 citas, vol. 171(3), 371–380 |

E2 de iter2 lo declaró en H1: el marker «debería ser por campo —por ejemplo `(metadata incomplete: resumen no indexado)`— y no una etiqueta genérica». En la ficha vigente, un lector no puede distinguir entre «resumen ausente», «conteo resuelto pero no transcrito» y «flag nuevo sin justificación», de modo que el estado de verificación no es operable entrada por entrada.

— polarity: negative · confidence: high · related: [[#C009]], [[#P001]], [[#P002]], [[#P003]], [[#P004]], [[#P005]], [[#P006]], [[#F-V8-002]], [[#F-V8-003]], [[#F-V8-004]], [[#F-V8-005]], [[#F-V8-006]]

### F-V8-002 — Los conteos recuperados 13 / 96 / 9 se confirman en OpenAlex

Las tres cifras que E2 recuperó por vía alternativa al HTTP 403 de Semantic Scholar se reproducen en los registros consultados aquí. Para `[18]`, `https://api.openalex.org/works/W4406461714` devuelve `"cited_by_count":13` con `counts_by_year` 2025: 7 y 2026: 6, `updated_date: 2026-11-25T09:40:18.809321`; la obra es `ProbSAINT: Probabilistic Tabular Regression for Used Car Pricing`, con `publication_date: 2024-12-15`, DOI `10.1109/bigdata62323.2024.10825740` y `arxiv: https://arxiv.org/abs/2403.03812`. Para `[19]`, `W2770052903` devuelve `"cited_by_count":96`, DOI `10.1007/978-3-030-03402-3_28`, `publication_year: 2018` y `publication_date: 2018-12-06`, con los cinco autores coincidentes. Para `[20]`, `W3120241027` devuelve `"cited_by_count":9`, DOI `10.48550/arxiv.2101.03788` y `publication_date: 2021-01-11`. Las tres cifras quedan por tanto verificadas en vivo y no dependen de la afirmación de E2.

Estos son los únicos conteos que la lista numerada expone de forma indirecta: ninguna de las tres fichas los incluye, porque el campo de citas no forma parte del formato de `Data/referencias.md`. La verificación es válida para los identificadores citados, no para un conteo declarado por el documento.

— polarity: positive · confidence: high · related: [[#P003]], [[#P004]], [[#P005]], [[#F-V8-003]]

### F-V8-003 — Los flags de `[18]`, `[19]` y `[20]` permanecen tras resolverse su único motivo

Las fichas conservan `(metadata incomplete)` y solo la URL de arXiv para `[18]` («arXiv:2403.03812; IEEE BigData 2024, Industry & Government Track (2024). https://arxiv.org/abs/2403.03812 ... **(metadata incomplete)**»), `[19]` y `[20]`, aunque el único dato que E2 declaró no verificable —el conteo de citas, bloqueado por HTTP 403 de Semantic Scholar— quedó cubierto por OpenAlex (13, 96 y 9; F-V8-002). En `[18]` falta además el DOI de la versión publicada; en `[19]` faltan el DOI `10.1007/978-3-030-03402-3_28` y el año 2018 de la publicación frente al 2017 del preprint declarado, una discrepancia de año que la ficha no consigna; en `[20]` falta el conteo. E2 denominó este estado «resuelto en vivo pero no reflejado» y la comparación de la lista con los registros confirma que el marcador no se actualizó entre el 27/11 y la generación de esta pasada.

— polarity: negative · confidence: high · related: [[#C009]], [[#P003]], [[#P004]], [[#P005]], [[#F-V8-001]], [[#F-V8-002]]

### F-V8-004 — Akerlof: §70 y `[1]` sostienen estados incompatibles sin campo identificado

La §70 (L1477) escribe: «Referencias citadas y verificadas externamente durante la auditoría: Akerlof (1970), *The Market for "Lemons"* (Crossref/OpenAlex) ...», y su versión inglesa (L1479) repite «Externally verified references cited during the audit: Akerlof (1970) ... (Crossref/OpenAlex)». En la misma fecha, `Data/referencias.md` `[1]` cierra con «https://doi.org/10.2307/1879431. Citada en el informe: yes. **(metadata incomplete)**», y añade que «Los metadatos se verificaron en vivo con OpenAlex/Crossref». El claim C009 de E1 reformula: «Solo cuatro referencias están verificadas externamente; las restantes figuran como `(metadata incomplete)`».

La consulta a `https://api.openalex.org/works/W2156109180` confirma todos los campos bibliográficos: DOI `10.2307/1879431`, autor `George A. Akerlof` con ORCID, revista `The Quarterly Journal of Economics`, volumen 84, número 3, `publication_date: 1970-08-01`, páginas 488–500 en el registro RePEc y `"cited_by_count":32658`. El campo `abstract_inverted_index` contiene únicamente «I. Introduction, 488. — II. The model with automobiles as an example, 489. — III. Examples and applications, 492. — IV. Counteracting institutions, 499. — V. Conclusion, 500.», que es el motivo original del flag y sigue sin cambiar. La parte Crossref de la afirmación no pudo contrastarse aquí: la API devolvió error de transporte, igual que el HTTP 429 registrado por E2. Las dos afirmaciones solo se reconcilian si se entiende que el flag alude al resumen y no a la identidad de la obra; la ficha no lo dice, y por eso la contradicción entre «verificada» e «incompleta» queda abierta en el único trabajo que sostiene el marco teórico de asimetría de información (§17, §19, §20).

— polarity: negative · confidence: high · related: [[#C009]], [[#P001]], [[#F-V8-001]], [[#F-V8-002]]

### F-V8-005 — `[10]`: el flag por resumen no indexado se confirma campo por campo

La ficha `[10]` termina en `(metadata incomplete)` y el registro `https://api.openalex.org/works/W7134932779` devuelve `"abstract_inverted_index": null`, de modo que el motivo subsiste exactamente donde E2 lo localizó. El resto de campos sí se confirma en la misma respuesta: título *The pricing of used electric vehicles via machine learning and hedonic price model: A comparative study*, autores Wentao Kang y Xiao Fu con ORCID, afiliación Hangzhou Dianzi University, `Computers & Industrial Engineering` volumen 216, artículo 111964, `publication_date: 2026-03-11` y `"cited_by_count":3` (frente a 2 en la pasada 1). La ficha declara 2026 y el DOI `10.1016/j.cie.2026.111964`; no hay DOI espurio ni ID imposible. Es el segundo caso, con `[1]`, en que el marcador corresponde a un campo real y no a un dato ya recuperado.

— polarity: neutral · confidence: high · related: [[#P002]], [[#P006]], [[#F-V8-001]]

### F-V8-006 — `[38]`: flag nuevo sin justificación y discrepancia de año no consignada

La ficha `[38]` incorpora `(metadata incomplete)` en esta iteración, mientras E2 consigna que en la pasada 1 la misma obra figuraba verificada con 136 citas y sin marker; el propio E2 lo califica como «introducido en la iteración 2 sin justificación explícita». El registro `https://api.openalex.org/works/W1991842457` confirma título, tres autores, `International Journal of Production Economics` vol. 171 parte 3, pp. 371–380, DOI `10.1016/j.ijpe.2015.02.006` y `"cited_by_count":136`. El campo `abstract_inverted_index` es `null`, pero `best_oa_location` apunta al texto completo de la Universidad de Manchester; el `raw_source_name` de esa ubicación registra «Quariguasi Frota Neto, J, Bloemhof, J & Corbett, C 2016», frente al `publication_year: 2015` de OpenAlex y al 2015 de la ficha. La lista no consigna esa discrepancia ni explica el cambio de estado, de modo que `[38]` es la única entrada cuyo flag aparece sin un motivo declarado en ninguno de los dos artefactos.

— polarity: negative · confidence: high · related: [[#P006]], [[#F-V8-001]]

### F-V8-007 — Las cuatro fuentes institucionales de §70 operan fuera de la numeración y DVLA carece de URL profunda

§70 declara como verificadas cuatro fuentes: Akerlof (1970), DfT/DVLA, ANFAC y AEADE. Solo la primera tiene ficha numerada (`[1]`); las tres institucionales aparecen como mención nominal sin número, de modo que el cómputo de 38 entradas de `Data/referencias.md` no las incluye y el claim C009 («Solo cuatro referencias están verificadas externamente») mezcla dos regímenes de cita. E2 iter2 verificó las páginas oficiales de ANFAC (P007), AEADE (P008) y DVLA/GOV.UK (P009) a nivel de organismo: ANFAC expone matriculaciones y cifras 2025, AEADE publica anuarios y boletines de ventas Ene–sep 2026, y GOV.UK confirma la serie «Vehicle licensing statistics data files»; en esta pasada no se re-fetcharon esas tres páginas. El punto no verificado según P009 es la URL profunda de la colección de estadísticas de vehículos: tres intentos directos devolvieron HTTP 404 y el `WebSearch` de apoyo falló a nivel de proveedor, por lo que la afirmación queda contrastada a nivel de organismo, no de enlace concreto. La precisión de atribución de AEADE es además ecuatoriana, no española; §70 no asigna país pero la vecindad de ANFAC en la misma frase puede inducir otra lectura.

— polarity: neutral · confidence: medium · related: [[#C009]], [[#P007]], [[#P008]], [[#P009]], [[#F-V8-004]]

### F-V8-008 — Convención de entrada uniforme en las 38 fichas, sin duplicados ni identificadores espurios

Las 38 entradas siguen una sola plantilla —autores, título en cursiva, venue, año, URL o DOI, «Citada en el informe: sí/no»— y todas incluyen autores nominales. No aparece la misma obra dos veces con identidades distintas: los DOI no se repiten y las tres versiones preprint/publicadas de `[18]`, `[19]` y `[20]` están representadas por una sola ficha cada una. Los DOI declarados se ajustan al patrón `10\.\d{4,9}/.*`; los cuatro identificadores de arXiv (`2403.03812`, `1711.06970`, `2101.03788`, `2601.14311`) tienen prefijo de fecha compatible con un documento de noviembre de 2026 y ninguno resuelve a otra obra en los registros consultados. Dos artefactos tipográficos son sistemáticos y no afectan a la atribución: el doble punto tras las iniciales del último autor en las 38 fichas («Akerlof, G. A..», «Krotov, V.; Johnson, L.; Silva, L..») y los paréntesis anidados en el venue de `[2]` («American Economic Review (2011 (el registro OpenAlex indexa la versión SSRN de 2010; la publicación AER es de 2011))»).

— polarity: positive · confidence: high · related: [[#F-V8-001]]

## Nota de cierre

La iteración 2 cambió el objeto auditable: de 36 menciones nominales sin convención a 38 fichas numeradas con DOI y estado declarado. Los conteos 13, 96 y 9 y los DOI publicados de `[18]` y `[19]` son verificables y no figuran en esas fichas; los flags de `[1]` y `[10]` corresponden a resúmenes no sustantivos o no indexados; el de `[38]` aparece sin motivo declarado. La contradicción entre §70 y `[1]` no es de existencia de la obra sino de etiqueta de estado: la ficha no nombra el campo incompleto y la sección no distingue verificación de identidad de verificación de resumen. Todo dato ausente se registró como no verificado; no se asignó ningún DOI, conteo ni año que no conste en la respuesta de la API consultada.

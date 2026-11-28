---
type: audit-artifact
phase: v1-structure
slug: corpus-documentacion-2026-11-28
generated_at: 2026-11-28T03:52:58-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md
language: es
---

# V1 — Structure (findings)

### F-V1-001 — El índice «Documentación» del README alcanza 2 de los 7 archivos restantes del corpus

El README abre el corpus (L8–L115) y su apartado «## Documentación» (L103–L108) reparte los documentos en «**Referencia:**», «**Cómo hacerlo:**», «**Explicación:**» y «**Necesidades pendientes:**». De los siete archivos no-README del corpus, solo dos figuran en ese índice: `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md` (L105) y `Data/analisis_rentabilidad/PRESENTACION_STORYTELLING.md` (L107). Quedan fuera `Data/analisis_rentabilidad/ARQUITECTURA_DATOS.md`, `Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md`, `Data/AUTOMATIZACION.md`, `Data/ESTRUCTURA_ESPACIO.md` y `Data/mapas/README.md`. El apartado «## Estructura» (L44–L59) enumera carpetas, no esos cinco documentos, y «## Sitio de documentación» (L91–L101) describe la generación MkDocs sin inventario de páginas.

Ninguno de los ocho bloques trae frontmatter YAML ni rótulos VSN-C. La entrada es el párrafo único de L12 —«Análisis reproducible del mercado automotor cubano: 974 autos únicos de Revolico, 2.232 anuncios de 8 marketplaces y 256 vehículos de 11 concesionarios, consolidados con fuentes oficiales (ONEI, Gaceta Oficial, BCC) y una serie de entrevistas y encuestas»—, seguido de «## Qué incluye» (L16–L22). En sentido inverso, el storytelling enlaza de vuelta al informe técnico, la auditoría de fuentes y el análisis de anuarios (L131), pero no a los cinco documentos ausentes del índice del README.

— polarity: negative · confidence: high · related: []

### F-V1-002 — Cifras duplicadas con marcadores `kpi` conviven con copias estáticas divergentes

`Data/AUTOMATIZACION.md` §2, «Números que se actualizan solos» (L661–L663), declara que «`README.md`, el storytelling, el análisis de alcance y el inventario de modelos llevan un marcador oculto `<!-- kpi:clave -->` justo antes de cada cifra» y que `actualizar_numeros.py` «reemplaza **solo el número**, conservando las palabras de alrededor». En efecto, 974 autos se reparte entre README (L12, L19, L69), storytelling (L123, L195, L211) y `ALCANCE_Y_RETENCION.md` (L579, L609, L624); 21.000 USD y 8,1 años aparecen en storytelling L195, en el Cuadro 1 (L328, L331) y en `ALCANCE_Y_RETENCION.md` L579.

La duplicación incluye pares de cifras que no coinciden. Los marketplaces se registran como «2.232 anuncios de 8 marketplaces» en README L12 y como «2.232 anuncios en los marketplaces especializados» en storytelling L211, mientras la tabla «## Fuentes de datos» del README consigna «2.222 anuncios» en la fila «Marketplaces» (L67): diez de diferencia, enunciados en L211 como «en la última revisión aparecieron diez anuncios nuevos en iTENCEL» sin adjudicar la cifra a una u otra columna. La base Revolico se reporta como «10.379 anuncios, 974 autos» en README L19 y como «10.217 anuncios, 812 autos, 23.143 imágenes, 11.620 revisiones, 12.338 teléfonos y 716 precios» en `ARQUITECTURA_DATOS.md` (L502–L503), donde se afirma que la copia Parquet conserva «las mismas filas, columnas y valores» (L503–L504). `ARQUITECTURA_DATOS.md` no figura entre los cuatro archivos con marcadores citados en L663.

— polarity: negative · confidence: high · related: []

### F-V1-003 — Columna vertebral de nueve secciones instructivas y apéndice resuelto, con tres apoyos sin anclaje

El storytelling (L119–L390) secuencia §1–§9 sin saltos ni reinicios: «1. El punto de partida: moverse en Cuba» (L137), «2. La alternativa personal: cuatro preguntas antes de comprar» (L165), «3. Lo que encontramos» (L205), «4. La curva de valor» (L223), «5. Las cuatro fuerzas invisibles» (L237), «6. Dónde está el mercado» (L259), «7. El espejo egipcio» (L275), «8. Lo que viene» (L287) y «9. Cierre» (L299), seguidos de «## Anexo: cuadros y gráficos» (L313). Los títulos anticipan contenido en lugar de funcionar como etiquetas de índice. La convención de L133 remite los «Cuadro» y «Gráfico» citados en el cuerpo al apéndice al final, y los anclajes de L147, L199, L217, L233, L253 y L271 resuelven a los Cuadros 1–5 definidos en L317–L377; no aparecen marcadores `??` ni `\ref{}` en el corpus.

Los desajustes internos son tres. «Cuatro preguntas» se enuncia en el título de §2 (L165), se reitera en L201 («Estas cuatro preguntas tienen respuesta») y en `ALCANCE_Y_RETENCION.md` L612 («FAQ schema con las cuatro preguntas»), pero §2 desarrolla tres subtítulos H3: «¿Cuánto costaría moverse?» (L175), «¿Quién lo mantiene?» (L185) y «¿Qué devuelve la inversión?» (L191). El apéndice enumera seis gráficos (L381–L386) de los que el cuerpo invoca solo los números 1, 2 y 5 (L217, L233); «Gráfico 3. Top marcas», «Gráfico 4. Precio por tier» y «Gráfico 6. Precio vs antigüedad» carecen de anclaje en prosa. El apoyo de §6, dedicado a mapa, estaciones de carga y talleres (L261–L269), remite a «[Cuadro 4](#cuadro-4-seguridad-vial)» (L271), cuyo contenido es «Seguridad vial (ONEI)» (L354–L362), una serie de accidentes, fallecidos y lesionados. §3 incluye además una nota editorial en cursiva que explica la función de la sección (L207).

— polarity: negative · confidence: high · related: []

## Resumen

- El índice «Documentación» del README alcanza 2 de los 7 archivos restantes del corpus; otros cinco quedan sin entrada desde el archivo de entrada.
- Las cifras duplicadas con marcadores `kpi` conviven con copias estáticas divergentes: 2.232/2.222 anuncios de marketplaces y 10.379/974 frente a 10.217/812 en Revolico.
- El storytelling conserva §1–§9 y apoyos resueltos, pero «cuatro preguntas» desarrolla tres subtítulos, tres gráficos del apéndice carecen de anclaje y §6 remite a un cuadro de seguridad vial.

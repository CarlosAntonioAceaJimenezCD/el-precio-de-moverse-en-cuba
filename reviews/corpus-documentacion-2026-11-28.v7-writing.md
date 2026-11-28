---
type: audit-artifact
phase: v7-writing
slug: corpus-documentacion-2026-11-28
generated_at: 2026-11-28T03:57:48-04:00
audited_document: .playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md
language: es
---

# V7 — Writing and AI patterns (findings)

Alcance: se revisaron las 833 líneas del texto cacheado, con foco en `README.md` (L8–L116) y `PRESENTACION_STORYTELLING.md` (L119–L390) como textos de entrada —ganchos, CTA, densidad, adjetivos sin ancla y paradigmas— y se cotejaron los seis bloques restantes con la misma rúbrica. Las referencias `L` corresponden al texto cacheado. Se aplican Winston (estructura), Pinker (estilo académico) y Romero §13 (cinco *Don't* aplicables al registro académico: d2, d3, d4, d5, d8). No se emite juicio sobre autoría: lo que se describe es patrón, densidad y sección.

### F-V7-001 — Ganchos de entrada: tres cifras en el primer bloque del README y del storytelling

El README abre con una frase de datos antes de cualquier metadato: «Análisis reproducible del mercado automotor cubano: **974 autos únicos** de Revolico, **2.232 anuncios** de 8 marketplaces y **256 vehículos** de 11 concesionarios, consolidados con fuentes oficiales (ONEI, Gaceta Oficial, BCC) y una serie de entrevistas y encuestas» (L12); ubicación, repositorio y fecha quedan en L14, en segundo lugar. El storytelling repite el dispositivo en el subtítulo —«Cuánto cuesta un carro en Cuba: 974 autos, 2.174 anuncios y una serie oficial detrás» (L123)— y lo convierte en gancho narrativo en L127: «En Cuba, moverse no se decide por un precio: se decide por cuánto costará mañana», seguido de «salir de casa no empieza cuando uno abre la puerta. Empieza antes: mirando el reloj, calculando cuánto se tarda en llegar a la parada...» (L139). Ambos son casos de *topic sentence* situada al inicio y de concretización temprana (Winston), con la salvedad de que el tercer término de las triadas de L12 y L123 ya es más abstracto que los dos primeros (d3, desarrollado en F-V7-003). La línea de enlaces de L129 —«Empieza por el principio» · «Mira los números» · «Consulta los modelos»— funciona como CTA de entrada con tres destinos nominales.

— polarity: positive · confidence: high · related: [[#F-V7-003]], [[#F-V7-008]]

### F-V7-002 — CTA de retorno: dos destinos resolubles y un índice presentado como vigente que el propio corpus declara pendiente

El cierre del storytelling combina una pregunta —«**¿Cuánto cuesta realmente moverse en Cuba?**» (L305)— con un CTA de regreso anclado a dos artefactos: «el índice por marca, modelo y provincia se actualiza en [KPIs y tablas](outputs/tables/kpis.csv) y el estado eléctrico en el [mapa de circuitos](../mapas/TIMELAPSE_CIRCUITOS.md). Vuelve por un dato puntual, no por un informe entero» (L307). El análisis de alcance registra ese CTA como corrección aplicada —«CTA de retorno al cierre» (L589), «ya añadido: KPIs y mapa de circuitos» (L616)—, de modo que existe correspondencia entre la descripción y el texto. En cambio, el mismo índice aparece como tarea futura en L292 («Publicar un índice de precio por marca, modelo y provincia») y en L617 («Publicar el índice ... con URL estable y fecha de actualización»), mientras L307 lo enuncia en presente con verbo «se actualiza». La promesa de L295 —«El resultado no será un informe. Será un **observatorio del mercado automotor cubano**»— queda igualmente proyectada; d2 opera aquí con fuerza enfática más que informativa, y «observatorio» funciona como paradigma (d4).

— polarity: neutral · confidence: high · related: [[#F-V7-005]], [[#F-V7-006]], [[#F-V7-008]]

### F-V7-003 — Don't 3 — triadas con cola larga: diez instancias, nueve en el storytelling

La lista de tres con último término notablemente más largo o más abstracto aparece nueve veces en el storytelling y una en el README: L12 («974 autos únicos ... 2.232 anuncios de 8 marketplaces y 256 vehículos ... consolidados con fuentes oficiales»), L123 («974 autos, 2.174 anuncios y una serie oficial detrás»), L127 («el combustible cambia con la divisa, el ómnibus ya no llega como antes y el carro propio se volvió infraestructura doméstica»), L141 (cuatro términos: «flotas envejecidas, frecuencias irregulares, largas colas y trayectos que se vuelven inciertos cuando escasea el combustible...»), L161 («el precio, la divisa, el mantenimiento y el futuro del vehículo»), L189 («encontrar quién repare, es conseguir la pieza, esperar la importación y aceptar que, mientras tanto, el vehículo se queda inmovilizado»), L225 («con cada año, con cada kilómetro y con cada vez que aparece en un anuncio con la documentación incompleta»), L279 («ingesta incremental, limpieza y features, análisis exploratorio, modelo econométrico con tests, benchmarks e infravalorados, salidas versionables»), L303 («una familia, un negocio, una decisión de inversión y una pregunta que merece una respuesta con datos») y L604 («promesa arriba, CTA al final y un artefacto actualizable al que regresar»). El patrón se acusa en que los dos primeros miembros son nominales cortos y el tercero se abre en una cláusula o en un metaconcepto. Las triadas de L143 («esperar, adaptarse, llegar tarde»), L197 («de dónde viene el auto, en qué moneda se paga y en qué estado llega») y L637 («Recolectar → procesar → publicar») mantienen longitud paralela y no entran en este conteo.

— polarity: negative · confidence: high · related: [[#F-V7-001]], [[#F-V7-005]]

### F-V7-004 — Don't 5 — adjetivos y cuantificadores sin ancla numérica: doce formulaciones en las secciones de entrada

Se cuentan doce modificadores sin cifra, fuente ni instancia inmediata en el storytelling y el documento de alcance: «Datos reales del mercado automotor cubano» (L125), «márgenes estrechos» (L141), «una parte común del paisaje urbano» (L149), «la señal más clara» (L157), «una fuente de ingresos estable» (L193), «El dato más fuerte» y «miles de dólares» (L215), «uno de los análisis de mercado automotriz más completos que tenemos» (L277), «prueba sólida» (L579), «patrones generales de long-form» (L593), «fuente confiable» (L633 y L730) y «degrada con elegancia» (L730). El contraste dentro del mismo corpus es nítido: los adjetivos del README van acompañados de ruta o magnitud —«anuncios, enlaces, colas de descarga y descartes exportados por categoría en `Data/CRUDO_POR_CATEGORIA/`» (L18), «2.174 anuncios limpios ... mediana local 21.000 USD» (L42)—, y `MODELOS_Y_FUNCIONES.md` acota el suyo: «Es un **heurístico léxico**, no una medición validada: sirve como control, no como prueba» (L413). En L215 el superlativo y la cifra vaga conviven con KPIs exactos en el párrafo anterior (L213), lo que deja el modificador sin función de anclaje.

— polarity: negative · confidence: high · related: [[#F-V7-005]], [[#F-V7-009]]

### F-V7-005 — Don't 4 — paradigmas y metáforas rectoras: marcos con y sin concreción

El storytelling organiza el argumento mediante marcos abstractos: «infraestructura doméstica» (L127 y L159), «una cadena de restricciones que cualquier familia reconoce» (L145), «un segundo sistema de transporte» y «un termómetro de la economía cotidiana» (L151), «el retrato que dejaron» (L207), «apareció el mercado» y «parte del retrato» (L213), «dos vidas» (L193), «se suman al ecosistema» y «reserva de valor» (L193), «seguro de valor» (L231), «fotografía/película» (L225), «cuatro corrientes que mueven el precio» (L239) y «cuatro capas» convertidas en «inteligencia de mercado» (L255), «observatorio» (L295), «puerta de entrada» (L575) y «radar de novedades» (L730). A este conjunto se añaden los términos de marketing de L589, L608–L612 («beneficio-driven», «cluster de contenido», «activo enlazable», «E-E-A-T»). «Ecosistema» (L193) coincide literalmente con el ejemplo de la trampa de abstracción de Romero. No todos operan igual: «infraestructura doméstica» recibe concreción inmediata —«la posibilidad de llegar al trabajo, llevar a los niños a la escuela, trasladar mercancías o aprovechar una oportunidad de negocio» (L159)— y «cuatro capas» se desglosa en divisa, reglas, luz y expectativas (L241–L251); en cambio «inteligencia de mercado» (L255) y «puerta de entrada» (L575) cierran el pasaje sin instancia que las sostenga. La densidad de marcos es alta en §§1–2 y §5, y baja en los bloques procedimentales.

— polarity: neutral · confidence: high · related: [[#F-V7-003]], [[#F-V7-007]], [[#F-V7-009]]

### F-V7-006 — Don't 2 — negación contrastiva: unas veinte instancias, cuatro retóricas

La estructura «no X, sino/es Y» o su variante «ya no X» aparece unas veinte veces en el storytelling. La mayoría realiza trabajo contrastivo y no constituye tic: «no se decide por un precio: se decide por cuánto costará mañana» (L127), «no empieza cuando uno abre la puerta. Empieza antes» (L139), «no hay una sola causa, sino una cadena de restricciones» (L145), «no hay un solo precio del “auto cubano”, sino muchos precios» (L213), «no es solo encontrar quién repare: es conseguir la pieza...» (L189), «no es un adorno: es la vista desde la que se decide...» (L269) y «Vuelve por un dato puntual, no por un informe entero» (L307). Un subconjunto de cuatro añade énfasis sin información nueva: «Esto, además, no es del todo nuevo» (L155), «no es una decisión simple. Es una decisión financiera» (L161), «Y ni siquiera eso agota la lista» (L183) y «El resultado no será un informe. Será un observatorio» (L295). La cadena de «ya no» en L197, L215 y L231 —«ya no se presenta como una cifra única», «ya no es una curva única, sino una división», «ya no podemos ponerle un número fijo»— reparte la misma corrección metodológica en tres secciones. En `MODELOS_Y_FUNCIONES.md` la negación cumple función delimitativa —«No se usa la tasa oficial de cambio. No se imputan precios... No se afirma causalidad» (L481–L487)— y no entra en el conteo de tics.

— polarity: neutral · confidence: high · related: [[#F-V7-002]], [[#F-V7-009]]

### F-V7-007 — Don't 8 — cierres que repiten la conclusión después de los datos

Cinco bloques epígrafos y dos frases de transición reiteran la tesis una vez que el ejemplo ya la ha mostrado: «Encontramos un mercado pequeño, sí, pero con suficiente estructura para dejar de improvisar» (L219, tras los KPIs de §3), «Cruzar estas cuatro capas convierte un catálogo de anuncios en inteligencia de mercado» (L255), «El diseño está listo para crecer igual que crezcan los datos» (L283), «Empezamos hablando de esperar el ómnibus. Terminamos entendiendo el precio de moverse» (L301), «El mapa no es un adorno: es la vista desde la que se decide...» (L269), «Ningún coeficiente resulta estadísticamente significativo ... Es parte de la historia: el mercado no admite una curva única» (L377) y «Eso, escrito aquí, es parte de que el proyecto sea confiable en 2028» (L730). La de L301 opera como cierre narrativo deliberado (devuelve la imagen de apertura de L139); las de L219 y L255 añaden un sustantivo abstracto —«suficiente estructura», «inteligencia de mercado»— que no estaba en los datos precedentes. Winston registra aquí una mezcla de recursos: §§3, 5 y 9 llevan cierre explícito, mientras §§1, 2, 4, 6, 7 y 8 enlazan directamente con la sección siguiente.

— polarity: neutral · confidence: medium · related: [[#F-V7-005]], [[#F-V7-008]]

### F-V7-008 — Metadiscurso y autorreferencia: el H2 diagnósticado como obstáculo en L583 persiste en L137

El metadiscurso (Pinker) está concentrado en `ALCANCE_Y_RETENCION.md` y aparece de forma aislada en el storytelling: «Esta sección responde a una pregunta concreta: ... No explica cómo se obtuvieron los datos; muestra el retrato que dejaron» (L207), «Estos apoyos se insertan aquí para que la narrativa no se detenga» (L315), «Decirlo es parte del respaldo» (L450), «Revisión del relato como **puerta de entrada**: ... Es un análisis de diseño, no una medición» (L575), el bloque «Lo que frenaba al lector antes de la última revisión» (L581–L587), «Correcciones aplicadas al storytelling: titular beneficio-driven, gancho de tres datos...» (L589), «(ya añadido: KPIs y mapa de circuitos)» (L616) y «Eso, escrito aquí...» (L730). En el bloque de frenos se lee: «El H2 «El punto de partida: moverse en Cuba» era una etiqueta de índice, no un beneficio» (L583); la lista de correcciones de L589 no incluye ese encabezado y el texto auditado lo conserva literalmente en L137 —«## 1. El punto de partida: moverse en Cuba»—. Lo que sí cambió fue el titular de L123, que es beneficio-driven. La autorreferencia produce, además, dos proyecciones numéricas sin derivación —«Punto central» 58, 40, 25, 16, 10, 5 (L595–L602) y «finalización 22–25 y retorno 18–22 por cada 100» (L604)— presentadas bajo la salvedad explícita «estimación ... inferencia, no medición» (L591).

— polarity: negative · confidence: high · related: [[#F-V7-001]], [[#F-V7-002]], [[#F-V7-009]]

### F-V7-009 — Densidad de patrones: alta en storytelling §§1–2 y en ALCANCE, sin declaración de uso de IA en el corpus

Conteo por mil palabras y recuento de triadas sitúan `ai-pattern-density: high` en tres bloques: storytelling §1 (≈6 hedges y 3 paradigmas en ≈450 palabras), storytelling §2 (≈11 hedges, 5 instancias de d2 y 3 paradigmas en ≈800 palabras) y `ALCANCE_Y_RETENCION.md` (≈6 marcas de metadiscurso, 6 paradigmas y 3 adjetivos sin ancla en ≈900 palabras). `ai-pattern-density: medium` corresponde a storytelling §§3–5, §6–9 y `AUTOMATIZACION.md`; `low` a README, al anexo de cuadros y a `MODELOS_Y_FUNCIONES.md`, `ARQUITECTURA_DATOS.md`, `ESTRUCTURA_ESPACIO.md` y `Data/mapas/README.md`. No se detectan series de cuatro o más oraciones consecutivas de 18–25 palabras: el storytelling alterna oraciones largas (L141, L153, L159, L177, L213) con frases de transición breves (L143, L171), de modo que el indicador de uniformidad rítmica no sostiene la densidad alta. Las aperturas formulas aparecen sobre todo en §§1–3 —«Aparece el primer problema» (L171), «Aquí también aparece» (L187), «En los últimos años» (L153 y L169), «Con esa muestra apareció el mercado» (L213), «Lo primero que uno debe saber» (L209), «Si la sección anterior era una fotografía» (L225)—. `reviews/corpus-documentacion-2026-11-28.v9-ethics.md` (F-V9-001) registra que ninguno de los ocho archivos contiene declaración de uso de IA, mientras `INFORME_TECNICO.md` §69 sí la consigna; la densidad alta se localiza, por tanto, en los bloques sin declaración. Este hallazgo se emite como enganche para V9, no como atribución de autoría. La medición es aproximada y se apoya en recuento manual, no en un corpus tokenizado.

— polarity: negative · confidence: medium · related: [[#F-V9-001]], [[#F-V7-004]], [[#F-V7-008]]

### F-V7-010 — Siglas y anglicismos sin desplegar en texto de cara al usuario

En documentos de entrada aparecen siglas y préstamos sin apertura en el primer uso: `TRMI` (L73 y L242; `ALCANCE_Y_RETENCION.md` L618 incluye «glosario vivo (TRMI, Decreto 163, Ticket, circuitos, gacelas)» entre las acciones pendientes), `KPIs` (L20), `OLS` en el título de L433 —desplegado solo después como «mínimos cuadrados ordinarios» en L441—, `UTM` (L609), `E-E-A-T` (L612), `CDN` (L659) y `long-form` (L593). El corpus sí despliega otras siglas —`VIF` se abre como «factor de inflación de varianza» en L454, `p_valor` se usa con interpretación en L377 y L450—, de modo que la ausencia no es uniforme. El efecto se concentra en los dos textos que se leen primero (README y storytelling), donde «TRMI informal: 930 CUP por USD» (L242) sostiene una de las cuatro fuerzas del precio.

— polarity: negative · confidence: high · related: [[#F-V7-004]]

### F-V7-011 — Winston — encabezados instructivos, apoyos autocontenidos y listas con función

Los títulos de README son instructivos en su totalidad —«Qué incluye» (L16), «Quickstart» (L24), «Estructura» (L44), «Fuentes de datos» (L63), «Configuración» (L75), «Sitio de documentación» (L91), «Documentación» (L103), «Marco legal y límites» (L110)— y las listas cumplen funciones discretas: enumeración de contenido (L18–L22), árbol de directorios (L46–L59), índice de documentación por rol (L105–L108) y pasos de reconstrucción (L86–L89). En el storytelling, la convención de L133 —«cuando el texto menciona un «Cuadro» o un «Gráfico», el apoyo está en el [apéndice visual](#apoyos), al final»— permite que los apoyos no interrumpan la lectura, y los títulos de los cuadros son autocontenidos —«Cuadro 3. Pasajeros transportados (ONEI, millones)» (L341), «Cuadro 4. Seguridad vial (ONEI)» (L354), «Cuadro 5. Modelo de depreciación (coeficientes vigentes)» (L364)—. La sección «Lo que viene» (L287–L293) usa una enumeración de cinco pasos, no prosa, con la función correcta (Winston). Dos excepciones se apartan del patrón instructivo: «El espejo egipcio» (L275) y «Lo que encontramos» (L205), esta última aclarada por el párrafo en cursiva de L207.

— polarity: positive · confidence: high · related: [[#F-V7-008]]

## AI-pattern density by section

| Section | Density | Notes |
|---|---|---|
| `README.md` (L8–L116) | low | Una triada con cola (L12); 0 hedges; adjetivos anclados a rutas y cifras (L18, L42); siglas sin desplegar (L20, L73). |
| Storytelling §1 «El punto de partida» (L137–L161) | high | `ai-pattern-density: high` — ≈6 hedges/450 palabras; 3 paradigmas (infraestructura doméstica, cadena de restricciones, termómetro); d2 en L139/L145/L155; d3 en L141/L161; d5 en L141/L149/L157. |
| Storytelling §2 «Cuatro preguntas» (L165–L201) | high | `ai-pattern-density: high` — ≈11 hedges/800 palabras (L181 concentra cuatro); d2 ×5, d3 en L189, d4 «ecosistema»/«reserva de valor» (L193), d8 en L201; counterpeso: fechas y montantes verificables en L177–L179. |
| Storytelling §3 «Lo que encontramos» (L205–L219) | medium | Metadiscurso en L207; comillas de scare en L213 («auto cubano»); d2 ×3; d8 en L219; oraciones largas sin uniformidad rítmica. |
| Storytelling §4 «La curva de valor» (L223–L233) | medium | Hedges en L229/L231; d3 en L225; d4 «seguro de valor» (L231); apertura formulada «Si la sección anterior era...». |
| Storytelling §5 «Cuatro fuerzas invisibles» (L237–L255) | medium | Baja penalización por hedging; alta carga de d4 (corrientes/capas/inteligencia de mercado) y d8 en L255; encabezados instructivos en L241–L250. |
| Storytelling §§6–9 (L259–L307) | medium | d2 ×4 (L269, L283, L295, L307); d4 «observatorio» (L295); d8 en L283/L301; CTA de retorno con enlaces en L307. |
| Storytelling «Anexo: cuadros y gráficos» (L311–L390) | low | Predominio tabular; captions autocontenidos; un d8 en L377; metadiscurso leve en L315. |
| `MODELOS_Y_FUNCIONES.md` (L395–L488) | low | Metaconceptos operativos con definición explícita; negación delimitativa en L413/L481–L487; shudder quotes en L403. |
| `ARQUITECTURA_DATOS.md` (L493–L566) | low | Jargon técnico definido al usar; shudder quotes en L512; criterios de «listo» medibles en L547–L554. |
| `ALCANCE_Y_RETENCION.md` (L571–L624) | high | `ai-pattern-density: high` — metadiscurso y autorreferencia en L575–L618; 6 paradigmas; d5 en L579/L589/L593; d3 en L604; proyecciones sin derivación en L595–L604. |
| `AUTOMATIZACION.md` (L629–L730) | medium | Tres paradigmas y tres adjetivos sin ancla; tablas con frecuencias y umbrales compensan la densidad; d8 en L730. |
| `ESTRUCTURA_ESPACIO.md` (L735–L788) | low | Cifras concretas en L741–L765; 3 hedges localizados (L743, L771, L788). |
| `Data/mapas/README.md` (L793–L833) | low | Documentación funcional: tablas, comandos y cadena anti-bot enumerada; sin triadas ni hedges. |

Los tres bloques marcados `ai-pattern-density: high` —storytelling §§1–2 y `ALCANCE_Y_RETENCION.md`— son los que V9 debe contrastar con la declaración de uso de IA: F-V9-001 registra ausencia de declaración en los ocho archivos del corpus y presencia en `INFORME_TECNICO.md` §69.

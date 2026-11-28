---
type: audit-artifact
phase: v1-structure
slug: corpus-total-2026-11-28
generated_at: 2026-11-28T05:48:31-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/corpus-total-2026-11-28/corpus-total-2026-11-28.text.md
language: es
---

# V1 — Structure (findings)

### F-V1-001 — VSN-C completo e H1 falsable en los dos resúmenes del informe

El bloque `INFORME_TECNICO.md` abre con «## Resumen (VSN-C)» (L23) y «## Abstract (VSN-C)» (L165), cada uno con las cuatro etiquetas «Visión / Pasos / Novedad / Contribuciones» y «Vision / Steps / News / Contributions» (L25–L28, L167–L170). La Visión nombra el problema (precios pedidos dispersos, sin series históricas, tasa informal diaria), los Pasos enumeran ocho marketplaces, normalización con TRMI fechada, estadística descriptiva, modelo hedónico y benchmarks, y las Contribuciones listan cuatro entregables: «base compacta reproducible, panel interactivo autocontenido, pipeline con timers y un expediente de auditoría con 13 artefactos» (L28). La hipótesis aparece en ambos resúmenes como «**Hipótesis falsable (H1):** «los precios de los tres tiers de marca en el mercado local provienen de la misma distribución, controlando por antigüedad y kilometraje»» (L30) y su espejo inglés (L172), con el contraste declarado: Kruskal-Wallis y «se rechaza con p < 0,001 en la corrida vigente». El resultado se reitera con cifras en §3.3 (H = 44,313; p = 0,00000, L2118–L2122) y en §71.3 con un intervalo bootstrap de 10.000 a 29.500 USD sobre 2.000 réplicas (L1537). Es la única formulación de hipótesis falsable del corpus.

La condición «controlando por antigüedad y kilometraje» no se opera en el contraste descrito: §3.3 aplica Kruskal-Wallis a los precios por `brand_tier` sin covariables (L2118–L2122), mientras el control por antigüedad y kilometraje aparece en la especificación hedónica de §3.1 (L2096–L2108). Los siete ejes del objetivo de §1 (L34) se reparten después entre los nueve bloques del marco analítico de §20 (L890–L900) y las secciones de resultados §§22–23, 59–60 y 71.1–71.6; «asequibilidad» y «rentabilidad» quedan como fórmulas en §19 (L882) y §20 (L898), sin una sección propia que informe su resultado.

— polarity: positive · confidence: high · related: []

### F-V1-002 — Índice de 10 archivos completo; contribuciones y respaldo editorial sin sección

El corpus declarado como «Corpus total de documentación» (L1–L3) contiene diez bloques `# ARCHIVO:` (L8, L1619, L1777, L2053, L2151, L2229, L2287, L2393, L2451, L2496). El apartado «## Documentación» del README (L1714–L1764) alcanza los nueve archivos restantes: `INFORME_TECNICO.md` y `Data/referencias.md` en «Referencia» (L1761), los cinco documentos de arquitectura, alcance, automatización, estructura de espacio y `Data/mapas/README.md` en «Arquitectura y evolución» (L1760), `MODELOS_Y_FUNCIONES.md` (L1761) y `PRESENTACION_STORYTELLING.md` (L1763). No hay archivo huérfano respecto del README.

Los diez bloques empiezan directamente con un encabezado (L10, L1621, L1779, L2055, L2153, L2231, L2289, L2395, L2453, L2498): ninguno trae frontmatter YAML, dedicatoria, agradecimientos ni dictamen de tutor. El cierre del informe registra «**Firma / Signature:** responsable del proyecto / project owner» (L1613), un rol sin nombre propio. Las declaraciones difieren entre bloques: §71.5 afirma «No se ha declarado todavía una licencia de datos o código» (L1552) y §71.15 que «la licencia queda pendiente de declaración» (L1562), mientras el README consigna «Licencia: código MIT y datos derivados CC BY 4.0» (L1768). La única enumeración de contribuciones sigue siendo la viñeta de cuatro entregables de los resúmenes (L28, L170): no hay una sección titulada «Contribuciones» en §1–§71 ni en los nueve archivos restantes; §71.1–§71.6 (L1516–L1558) se rotula como estándares de nivel master.

— polarity: neutral · confidence: high · related: []

### F-V1-003 — Siete anclas del storytelling sin destino en el corpus y §71.15 antes que §71.14

El storytelling contiene once enlaces internos `](#…)`: L1787, L1791, L1805, L1857 (dos), L1875 (dos), L1891 (dos), L1911 y L1929. Solo `#apoyos` tiene un destino explícito en el propio archivo: `<a id="apoyos"></a>` (L1969), y los anclajes de Cuadro 1 y Cuadro 2 —este último repetido en L1911— coinciden con los encabezados «### Cuadro 1. KPIs del mercado» (L1975) y «### Cuadro 2. Mercado local e importación» (L1991). Los otros siete no tienen destino en el texto auditado: Cuadro 3, Cuadro 4 y Cuadro 5 usan prefijos de encabezados más largos (L1999, L2012, L2022); Gráfico 1, Gráfico 2 y Gráfico 5 remiten a un apartado único «### Gráficos» (L2037) cuyas seis entradas son enlaces a HTML (L2039–L2044), sin encabezados numerados; y «[Empieza por el principio](#1-el-punto-de-partida-moverse-en-cuba)» (L1787) apunta a un título ausente, pues §1 se llama «Por qué moverse en Cuba cuesta más de lo que parece» (L1795). `Auxiliares/herramientas/generar_sitio_mkdocs.py:24-28,62-63` reescribe los anclajes de cuadros, gráficos y apéndice e inyecta `<a id="cuadro-N">` y `<a id="grafico-N">` en la página generada, pero no contempla el anclaje de apertura: la resolución depende de un paso de compilación ajeno al corpus y esa última referencia queda sin destino también en el sitio. No aparecen marcadores `??` ni `\ref{}`.

La numeración presenta tres desajustes. La nota de L163 —«la numeración de secciones se reinicia en esta parte; las referencias cruzadas se interpretan dentro de cada parte»— convive con las notas de actualización de L56 y L198, que remiten a «§34» y «§59–§60», secciones de la secuencia continua posterior a §13 (L303, L1045, L1406). §71.15 «Declaraciones» (L1560) precede a §71.14 «Obras del mapa literario citadas en el cuerpo» (L1566). `Data/AUTOMATIZACION.md` repite «## 6. Estado de implementación» en L2355 y L2357, separado por una línea en blanco.

El índice bibliográfico también diverge: §70 habla de «41 referencias» (L1506), el README de «Referencias y trabajos cercanos (41)» (L1716) y `Data/referencias.md` enumeraba [1]–[41] (L2505–L2584), pero la tabla de §71.14 contiene solo 38 filas, [1]–[38] (L1568–L1607). En el README, las entradas [1]–[39] están cortadas a 156–157 caracteres (L1717–L1755): L1718 termina en «American Economic Review (2011 (el registro » y L1719 en «… Consumer Expenditure S», frente a las formas completas de L2507 y L2509. §70 además envía las fuentes restantes a `reviews/informe-tecnico-2026-11-27.e2-literature.md`, artefacto externo a los diez bloques.

— polarity: negative · confidence: high · related: []

## Resumen

- El informe lleva VSN-C completo e H1 falsable con contraste y cifras en los dos resúmenes; las contribuciones quedan como viñeta de cuatro entregables y sin sección propia.
- El README indexa los diez bloques del corpus, pero ningún archivo trae frontmatter, dedicatoria, agradecimientos ni dictamen de tutor, y la licencia se declara de dos maneras distintas.
- Siete anclas del storytelling carecen de destino en el corpus, §71.15 antecede a §71.14, «6. Estado de implementación» aparece dos veces y 39 entradas bibliográficas del README están truncadas.

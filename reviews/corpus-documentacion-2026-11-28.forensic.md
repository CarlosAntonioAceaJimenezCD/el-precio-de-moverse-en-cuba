---
type: audit-forensic
slug: corpus-documentacion-2026-11-28
generated_at: 2026-11-28T18:00:00-05:00
audited_document: corpus de documentación de usuario (8 archivos)
audited_document_title: README, storytelling, modelos, arquitectura, alcance, automatización, espacio y mapas
language: es
level: master
preset: Standard
phases_executed: [0, 1, 2, 3]
dimensions_run: [V1, V2, V3, V4, V5, V6, V7, V8, V9]
dimensions_skipped: []
phase1_failures: []
phase2_failures: []
phase_artifacts:
  plan: corpus-documentacion-2026-11-28.plan.md
  e1: corpus-documentacion-2026-11-28.e1-claims.md
  e2: corpus-documentacion-2026-11-28.e2-literature.md
  e3: corpus-documentacion-2026-11-28.e3-artifacts.md
  v1: corpus-documentacion-2026-11-28.v1-structure.md
  v2: corpus-documentacion-2026-11-28.v2-methodology.md
  v3: corpus-documentacion-2026-11-28.v3-results-evidence.md
  v4: corpus-documentacion-2026-11-28.v4-novelty.md
  v5: corpus-documentacion-2026-11-28.v5-state-of-the-art.md
  v6: corpus-documentacion-2026-11-28.v6-reproducibility.md
  v7: corpus-documentacion-2026-11-28.v7-writing.md
  v8: corpus-documentacion-2026-11-28.v8-bibliography.md
  v9: corpus-documentacion-2026-11-28.v9-ethics.md
  forensic: corpus-documentacion-2026-11-28.forensic.md
previous_iterations: [reviews/informe-tecnico-2026-11-28-iter4.md]
---
# Auditoría forense — Corpus de documentación

## §0 — Resumen del documento

El objeto auditado es el corpus de documentación de usuario de *El precio de moverse en Cuba*: ocho archivos Markdown unificados (README, storytelling, MODELOS, ARQUITECTURA, ALCANCE, AUTOMATIZACION, ESTRUCTURA_ESPACIO y mapas/README), 833 líneas, sin frontmatter ni rótulos VSN-C. Declara como alcance «Análisis reproducible del mercado automotor cubano» y organiza la documentación en entrada, quickstart, árbol, fuentes e índice por roles.

Las afirmaciones load-bearing se reparten en tres grupos: el núcleo de KPI (2.174 anuncios limpios, 1.483 locales, mediana 21.000 USD, 32.569 km, 50 marcas, 114 grupos, 30 infravalorados, 89 anomalías), la base Revolico (10.379 anuncios, 974 autos) y los marketplaces (2.232 anuncios de ocho sitios), más la serie ONEI (−59 % pasajeros, −71 % ómnibus), la TRMI de 930 CUP/USD al 18/11 y la conclusión hedónica de no significancia.

E3 inventaria ocho conjuntos de datos, 21 tablas, cinco cuadros, seis gráficos, un panel de 107 KB, 134 chunks con SHA-256, sitio MkDocs y cinco timers. Los marcadores `<!-- kpi:… -->` se resuelven en `actualizar_numeros.py:46–118`. La pasa re-ejecutó E1–E3 y V1–V9 en nivel `master`, cotejando contra los CSV vigentes, el informe técnico y las 41 entradas de `Data/referencias.md`, con prueba de humo 4/4. No hubo subagentes fallidos.

## §1 — v1-structure


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


## §2 — v2-methodology


# V2 — Methodology (findings)

### F-V2-001 — Protocolo de ejecución y trazabilidad descrito de extremo a extremo

El corpus describe una cadena de ejecución identificable: `README.md` §Quickstart (L.26–40) fija Python 3.10+, `requirements.txt`, el entorno `Auxiliares/.venv-py` y la entrada `Data/analisis_rentabilidad/scripts/run_all.py`, con salidas nominales `listings_clean.parquet`, `kpis.csv` y `kpis_canal.csv`; `config.py` concentra «Rutas, umbrales de precio/año, TRMI, marcas y tiers» (L.79). La trazabilidad se declara en tres capas: `MANIFEST.json` con «recuentos y SHA-256 por archivo» (L.504), `manifiesto_ejecucion.jsonl` con «commit, SHA de scripts, Python, entradas/salidas, filas, métricas de calidad y watermark antes/después» y `VERSIONES.json` con dependencias y hash de configuración (L.687–688). El cierre del bucle está documentado en `actualizar_numeros.py` con modo `--check` y pruebas en `probar_actualizar_numeros.py` (L.663), y la reconstrucción de bases desde chunks en L.84–89. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced». La descarga de protocolo y código se satisface; el apartado de semillas se observa en F-V2-002.

— polarity: positive · confidence: high · related: [[#C061]], [[#C062]], [[#C076]], [[#C110]] · criteria: V2.reproducibility_protocol.master

### F-V2-002 — Ninguna semilla aleatoria declarada en los ocho archivos

No aparece `seed`, `semilla`, `random_state` ni equivalente en el corpus unificado (L.1–833). La única noción de aleatorización es `RandomizedDelaySec=5m` en la programación de timers (L.655), que es jitter de scheduling y no una semilla de generador. Las únicas rutinas estocásticas implícitas —OLS, VIF, Kruskal-Wallis, percentiles— son deterministas dada la muestra, y el propio `MODELOS_Y_FUNCIONES.md` §1 califica la preparación como «Preparación determinista (sin inferencia)» con respaldo en «la reproducibilidad y la trazabilidad» (L.401–403). Bajo el criterio `V2.reproducibility_protocol.master` («seeds mentioned»), el elemento de semillas está ausente como declaración explícita, sin que ello altere la determinism de los cómputos descritos.

— polarity: neutral · confidence: high · related: [[#C110]], [[#C111]] · criteria: V2.reproducibility_protocol.master

### F-V2-003 — Ablación explícita del término `hp` entre modelo principal y completo

`MODELOS_Y_FUNCIONES.md` §3.1 (L.452) estima dos especificaciones del mismo modelo hedónico y contrasta los resultados: «el modelo principal (sin `hp`) usa 586 observaciones de 993 candidatas (R² = 0,101; p del F 0,000) y el completo usa 28 (R² = 0,274; p del F = 0,411)». La comparación aísla un componente —la potencia— manteniendo fijas la fórmula base, la muestra de candidatas y el resto de términos, y se apoya en `modelo_muestra.csv`. El pasaje no emplea la etiqueta «ablación», pero la estructura es funcionalmente una ablación de un término declarado. El criterio `V2.ablations` para `level=master` se lee: «Explicit ablation of at least one component»; el corpus lo satisface con un componente explícito. La interpretación del resultado se acota en el propio texto: la asociación positiva de antigüedad en el modelo principal es «un artefacto de selección, no una tasa anual» (L.452).

— polarity: positive · confidence: high · related: [[#C007]], [[#C008]], [[#C043]] · criteria: V2.ablations.master

### F-V2-004 — Cuatro recuentos de muestra incompatibles para el modelo hedónico

La muestra del modelo hedónico se declara con cuatro valores distintos en el corpus. §3.1 (L.450) afirma «28 observaciones completas» y, en la misma oración, «La muestra se reduce a 22 porque `hp` solo está presente en 52 filas y `mileage_km` en 572»; el apéndice Cuadro 5 (L.377) repite «las 22 observaciones de este modelo frente a las 572 del modelo principal»; §3.1 (L.452) da 586 y 28 con respaldo en `modelo_muestra.csv`; y la tabla de depreciación histórica registra 584 de 981 según el contraste externo del inventario de claims. A la vez, la regla de inclusión del propio §3.1 (L.441) exige «más de 30 observaciones por término y más de 30 filas», umbral que el recuento 28 —y con más razón el 22— no alcanza. El criterio `V2.sample_size` para `level=master` se lee: «≥20 trials; ≥10 datasets/instances». El número de fuentes/instancias del corpus (8 marketplaces, 11 concesionarios, 12 anuarios, Revolico, ICD) supera diez, pero la muestra efectiva del modelo completo queda por debajo del umbral que el propio documento declara, y las cuatro cifras no se reconcilian entre secciones.

— polarity: negative · confidence: high · related: [[#C007]], [[#C008]], [[#C040]], [[#C046]] · criteria: V2.sample_size.master

### F-V2-005 — Suficiencia de 104 observaciones semanales en tensión con el límite de serie temporal

`AUTOMATIZACION.md` §2 (L.645) registra «Snapshots de precio (`price_history`) | Semanal, tras Revolico | 104 observaciones en 2 años bastan para depreciación», y §5 (L.690) repite «104 semanas ≈ 2 años». En sentido opuesto, `MODELOS_Y_FUNCIONES.md` §4 (L.485) declara «No se presenta una curva de depreciación temporal: hace falta una serie mensual de 6–12 meses», y el storytelling §8 (L.290) sitúa «Convertir el snapshot semanal en una serie de precios de 6–12 meses» en lo que viene. El encabezado del storytelling (L.123) añade «y una serie oficial detrás», que el propio inventario de modelos niega como curva temporal. La afirmación de suficiencia de la tabla de periodicidades no guarda consistencia con el criterio de serie exigido en el bloque de límites, y ambas afirmaciones conviven sin reconciliación en el mismo corpus. El criterio `V2.sample_size.master` fija «≥20 trials; ≥10 datasets/instances»; el conflicto no es de cantidad sino de la idoneidad declarada de la muestra temporal para la estimación que se dice habilitar.

— polarity: negative · confidence: high · related: [[#C003]], [[#C010]], [[#C038]], [[#C051]], [[#C064]], [[#C108]] · criteria: V2.sample_size.master, V2.threats_to_validity.master

### F-V2-006 — Límites y riesgos distribuidos en subsecciones dedicadas de cuatro archivos

El corpus incorpora varias secciones explícitamente consagradas a límites. `MODELOS_Y_FUNCIONES.md` §4 «Lo que NO se hace (y por eso el análisis es honesto)» (L.480–486) enumera cinco acotaciones: «No se usa la tasa oficial de cambio», «No se imputan precios ni kilómetros faltantes», «No se afirma causalidad: el modelo es de asociación sobre un corte transversal», «No se presenta una curva de depreciación temporal» y «No se mezclan mercados». `ARQUITECTURA_DATOS.md` §5 «Riesgos» (L.556–560) cubre archivos pequeños, watermark desincronizado y overkill; `AUTOMATIZACION.md` §7 «Límites que hay que aceptar» (L.728–730) describe la ventana de ~8 días de Telegram y el envejecimiento de selectores; `README.md` §«Marco legal y límites» (L.110–114) registra cuatro limitaciones operativas; y `ALCANCE_Y_RETENCION.md` L.575 califica el análisis como «diseño, no una medición: el proyecto no tiene analytics». El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations»; el corpus excede esa línea base en cantidad de subsecciones, aunque la consistencia entre ellas se evalúa en F-V2-005 y F-V2-009.

— polarity: positive · confidence: high · related: [[#C009]], [[#C021]], [[#C051]], [[#C084]] · criteria: V2.threats_to_validity.master

### F-V2-007 — Tests estadísticos nombrados, con estadísticos y umbrales desactualizados

El inventario de inferencia incluye OLS con p-valores y test F (L.450–452), VIF (§3.2, L.454–458), Kruskal-Wallis (§3.3, L.460–464: «H = 25,741, p = 1e−05») y Welch t-test (§3.4, L.466–470, «codificado, no ejecutado en la corrida actual»), además de reglas de percentiles para anomalías (§3.5). El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)». El diseño es transversal y no contiene comparaciones pareadas, de modo que la familia de tests pareados no se activa; en su lugar hay tests de grupo y de especificación. Los valores reportados no coinciden con las tablas de respaldo: el rango VIF «1,13 a 1,58» (L.458) frente a 1,12–1,40 en `vif.csv`, y H = 25,741 / p = 1e−05 frente a H = 32,818 / p = 0,0 en `tests.csv`, según el contraste externo del inventario de claims. La conclusión cualitativa se mantiene en ambos casos; los estadísticos no. No se reporta corrección por comparaciones múltiples, elemento que el criterio master no exige.

— polarity: neutral · confidence: high · related: [[#C043]], [[#C047]], [[#C048]], [[#C049]] · criteria: V2.statistical_tests.master

### F-V2-008 — Contrastes de diseño y un único espejo externo, sin líneas base experimentales

El corpus ofrece dos puntos de contraste. `ARQUITECTURA_DATOS.md` §2 (L.516–527) presenta una matriz de seis motores —DuckDB, Polars, PyArrow, Iceberg/Delta, DuckLake, ClickHouse/chDB— con Adopción y Veredicto; la ventaja de Polars se atribuye a «benchmarks de proveedor» y el propio texto la condiciona a «Segundo motor, solo con medición» (L.521). El storytelling §7 (L.275–283) toma como único referente a `Egyptian-Used-Cars` y afirma «Nuestro proyecto ya tiene esa arquitectura». La única medición antes/después propia es la compactación Parquet «849 MB → 27,5 MB» (L.502) y el dashboard «107 KB» frente a los 6 HTML y ~4,5 MB remotos previos (L.659). El criterio `V2.baselines` para `level=master` se lee: «≥2 baselines, one of which corresponds to a SOTA-adjacent approach in the field». Los contrastes presentes son de arquitectura y de producto, no líneas base de evaluación de un método propuesto; el referente externo es singular y su calificativo «uno de los análisis más completos que tenemos» no se contrasta dentro del corpus.

— polarity: neutral · confidence: medium · related: [[#C035]], [[#C053]], [[#C107]], [[#C011]], [[#C060]] · criteria: V2.baselines.master

### F-V2-009 — Estados de implementación y periodicidades declarados de forma inconsistente entre secciones

Varias declaraciones del protocolo se contradicen entre bloques. El ledger LFS aparece como operativo en §3 («LFS con ledger `_state/lfs_push_ledger.jsonl`», L.671) y como pendiente en §6 («Pendiente (fase siguiente): … ledger LFS», L.711). El aislamiento de carriles afirma «Ningún job de recolección hace `git push`» (L.637) y «sin git push» (L.564), mientras §6 atribuye a los scripts de Revolico y marketplaces «push o reescritura completa» (L.711). La Tabla de periodicidades fija Revolico como «Semanal» (L.644) mientras el estado actual describe «Extracción continua … timer cada 10 minutos» (L.564). DuckDB figura como «Recomendado» (L.520) y, catorce líneas después, bloqueado por `SIGILL` (L.566). La compactación Parquet se da por «ya implementado» sobre 10.217 anuncios y 812 autos (L.497–502), cifras incompatibles con los 10.379 y 974 del README (L.19) a igual fecha. Estas tensiones afectan a la consistencia interna exigida por el criterio `V2.reproducibility_protocol.master`: el protocolo está descrito, pero su estado declarado varía según el archivo.

— polarity: negative · confidence: high · related: [[#C011]], [[#C013]], [[#C053]], [[#C055]], [[#C058]], [[#C059]], [[#C062]], [[#C071]] · criteria: V2.reproducibility_protocol.master


## §3 — v3-results-evidence


# V3 — Resultados frente a evidencia

Se contrastan todas las cifras del corpus unificado (833 líneas; bloques `README.md`, `PRESENTACION_STORYTELLING.md`, `MODELOS_Y_FUNCIONES.md`, `ARQUITECTURA_DATOS.md`, `ALCANCE_Y_RETENCION.md`, `AUTOMATIZACION.md`, `ESTRUCTURA_ESPACIO.md` y `Data/mapas/README.md`) con los CSV/TXT vigentes de `Data/analisis_rentabilidad/outputs/tables/` (`kpis.csv`, `kpis_canal.csv`, `modelo_muestra.csv`, `modelo_depreciacion.csv`, `modelo_resumen.txt`, `tests.csv`, `comparaciones.csv`, `vif.csv`, `anomalias.csv`, `infravalorados.csv`, `benchmark.csv`, `baselines.csv`), con `Data/analisis_rentabilidad/data/compacto/MANIFEST.json`, con las bases SQLite que alimentan los marcadores y con `INFORME_TECNICO.md`. Las referencias `L…` son del texto cacheado, que coincide con la numeración de cada archivo de origen; la evidencia externa se cita con `archivo:línea`. Los marcadores `<!-- kpi:… -->` se resuelven en `Auxiliares/herramientas/actualizar_numeros.py:46–118`, de modo que su valor se contrasta con la fuente real y no solo con el texto que lo muestra.

## Resumen

- Doce divergencias numéricas localizadas: dos en recuentos de anuncios/autos, cinco en el bloque del modelo econométrico, una en VIF, una en Kruskal-Wallis, una de vigencia temporal de corrida y una de aritmética de ancho de banda.
- El núcleo de KPI (2.174 / 1.483 / 691 / 21.000 / 28.201,06 / 32.569 / 8,1 / 50 / 114 / 30 / 89) y la serie del ONEI están respaldados sin desajuste por los CSV y por `INFORME_TECNICO.md`.
- La divergencia más extendida es la del modelo: `modelo_muestra.csv` y `modelo_depreciacion.csv` dan 28/993, 586/993, R² 0,274 y p mínimo 0,0941, mientras el corpus conserva 22/572, 584/981, p 0,165 y ocho coeficientes de una corrida anterior.

### F-V3-001 — Los KPI canónicos y la desagregación por canal coinciden con los CSV vigentes

`README.md` (L42) afirma «**Resultado esperado:** 2.174 anuncios limpios (1.483 locales + 691 de importación), mediana local 21.000 USD»; `PRESENTACION_STORYTELLING.md` (L195, L213) añade «media de 28.201,06 USD; la antigüedad promedio es de 8,1 años y el kilometraje mediano, de 32.569 km» y «El canal importado —691 anuncios— corre en paralelo, con una mediana de 26.000 USD»; el Cuadro 1 (L321–331) y el Cuadro 2 (L337–339) repiten once y doce valores respectivamente. `kpis.csv:2-12` contiene `anuncios_totales,2174.0`, `anuncios_locales,1483.0`, `anuncios_importacion,691.0`, `anuncios_usados_locales,1462.0`, `anuncios_nuevos_locales,21.0`, `marcas_distintas,50.0`, `precio_medio_usd,28201.06`, `precio_mediano_usd,21000.0`, `anio_mediano,2020.0`, `km_medianos,32569.0` y `antiguedad_media,8.1`; `kpis_canal.csv:2-4` da fila por fila 691/26.000/27.046,22, 21/24.623,66/24.729,59 y 1.462/21.000/28.201,06. La frase de L197 —«50 marcas», «114 grupos», «30 oportunidades infravaloradas» y «89 anomalías»— se apoya en `benchmark.csv` (114 filas de datos), `infravalorados.csv` (30) y `anomalias.csv` (89), y los marcadores se leen de esos archivos en `actualizar_numeros.py:71-73`. La descomposición aritmética (1.462+21=1.483; 1.483+691=2.174) es cerrada. Relación: respaldo múltiple y coherente.

— polarity: positive · confidence: high · related: [[#C002]], [[#C004]], [[#C005]], [[#C028]], [[#C036]], [[#C037]]

### F-V3-002 — 2.222 frente a 2.232 anuncios de marketplaces: la tabla del README queda diez anuncios atrás

`README.md` (L12) muestra el marcador «2.232 anuncios de 8 marketplaces» y su tabla «Fuentes de datos» (L67) registra «2.222 anuncios»; `PRESENTACION_STORYTELLING.md` (L211) repite «2.232 anuncios en los marketplaces especializados; en la última revisión aparecieron diez anuncios nuevos en iTENCEL». `actualizar_numeros.py:115-118` calcula `anuncios_marketplaces` sumando `select count(*) from anuncios` en los ocho `*.sqlite` de `Data/catalogos_concesionarios/marketplaces/`; la consulta vigente devuelve 2.232 (itencel.sqlite 961, cubisima 155, timbirichi 170, autocubana 667, cogetucarro 200, apululu 33, carroscom 15, ventacuba 31). `INFORME_TECNICO.md:1381` documenta «iTENCEL mostró 10 anuncios nuevos» y `INFORME_TECNICO.md:1391` «La BD pasó de 951 a 961 anuncios». El 2.222 de L67 corresponde al estado anterior a esa inserción y no aparece ya en ninguna fuente vigente; el 2.232 de L12 y L211 sí coincide con las bases y con el informe técnico. Ninguna de las dos cifras tiene un CSV en `outputs/tables/`: el marker no se resuelve desde esa carpeta. Relación: divergencia interna de diez anuncios, con el valor anterior localizado en una tabla estática.

— polarity: negative · confidence: high · related: [[#C001]], [[#C016]], [[#C027]]

### F-V3-003 — La base Revolico se reporta con dos recuentos incompatibles a igual fecha: 10.379/974 frente a 10.217/812

`README.md` (L19) afirma «10.379 anuncios, 974 autos»; `ARQUITECTURA_DATOS.md` (L502) describe la misma base y la misma fecha (23/11/2026) como «849 MB → 27,5 MB (10.217 anuncios, 812 autos, 23.143 imágenes, 11.620 revisiones, 12.338 teléfonos y 716 precios)». La consulta directa a `Data/Revolico/revolico.sqlite` devuelve 10.379 en `anuncios` y 974 en `autos`, y `Data/analisis_rentabilidad/data/compacto/MANIFEST.json:6,19` registra `filas: 10379` y `filas: 974` para esas mismas tablas; el propio `INFORME_TECNICO.md:1345` confirma el tamaño (849.465.344 bytes). Tres de los cuatro recuentos restantes de L502 también divergen del MANIFEST: imágenes 23.143 frente a 23.697 (`MANIFEST.json:58`), revisiones 11.620 frente a 14.487 (`:32`), teléfonos 12.338 frente a 12.538 (`:71`); solo precios coincide (716, `:45`). El 974, en cambio, es estable en el corpus (L12, L69, L123, L195, L211) y coincide con la BD. Relación: cifras de una exportación anterior conservadas en prosa junto a un MANIFEST ya regenerado.

— polarity: negative · confidence: high · related: [[#C011]], [[#C014]]

### F-V3-004 — Cuadro 5 y la prosa de MODELOS conservan ocho coeficientes y ocho p_valores de una corrida previa

`PRESENTACION_STORYTELLING.md` rotula el Cuadro 5 (L364) como «coeficientes vigentes» y enumera (L368–375): Intercepto 12,4469 (p 0,000), Económico −1,1228 (0,328), Medio −1,2332 (0,239), Premium 0,0662 (0,947), Antigüedad −0,0708 (0,237), log(km) −0,0226 (0,740), Potencia −0,0046 (0,165) y Condición −0,0340 (0,802). `MODELOS_Y_FUNCIONES.md` (L450) refuerza «el p_valor más bajo es 0,165, de potencia; antigüedad tiene p = 0,237». `modelo_depreciacion.csv:2-9` regresa, en el mismo orden, 12.0884/0.0, −1.0208/0.1421, −0.978/0.0941, 0.1146/0.8753, −0.0632/0.1504, −0.0333/0.4711, −0.0036/0.1403 y −0.0254/0.8168, con coincidencia con `modelo_resumen.txt`. Los ocho coeficientes y los ocho p_valores difieren; el p mínimo nointercepto vigente es 0,0941 (`modelo_depreciacion.csv:4`), no 0,165, y es el que `INFORME_TECNICO.md:1409` publica mediante el marcador `modelo_p_min` (`actualizar_numeros.py:88-91`). La conclusión cualitativa de L377 —«Ningún coeficiente resulta estadísticamente significativo con la base actual»— sigue siendo válida con el CSV, pero la tabla rotulada como vigente no reproduce sus números. Relación: desajuste entre la evidencia citada y la tabla que dice alimentarla.

— polarity: negative · confidence: high · related: [[#C006]], [[#C007]], [[#C030]], [[#C039]], [[#F-V3-005]]

### F-V3-005 — Tres recuentos de muestra para un mismo modelo: 28/993 en el CSV, 22/572 en el Cuadro 5 y 584/981 en el informe técnico

`MODELOS_Y_FUNCIONES.md` (L450) enuncia «28 observaciones completas de 993 candidatas» y acto seguido «La muestra se reduce a 22 porque `hp` solo está presente en 52 filas y `mileage_km` en 572; al exigir todos los términos a la vez se descarta el 97,5 % de las candidatas (R² = 0,274; p del F = 0,411)»; (L452) da después «586 observaciones de 993 candidatas (R² = 0,101; p del F 0,000) y el completo usa 28 (R² = 0,274; p del F = 0,411)». `modelo_muestra.csv:2-3` contiene exactamente `principal,993,586,0.1008,0.0` y `completo,993,28,0.2744,0.4114`. El Cuadro 5 (L377) afirma «las 22 observaciones de este modelo frente a las 572 del modelo principal», cifras ausentes del CSV citado en la misma frase. `INFORME_TECNICO.md:1516` registra «R² 0,101 sobre 584 observaciones» y `:1522` «la muestra pasa de 28 a 584 observaciones de 981 candidatas», mientras `:1528` habla de «981 candidatas» y `:1401` de 993/28; `INFORME_TECNICO.md:1489` documenta además que un R² citado como 0,277 se corrigió a 0,274, valor que el corpus ya usa. La regla declarada en L441 («el modelo exige más de 30 filas») queda por debajo de las 28 observaciones del propio CSV. Relación: una misma cantidad reportada con 22, 28, 572, 584 y 586 observaciones, y con 981 y 993 candidatas.

— polarity: negative · confidence: high · related: [[#C007]], [[#C008]], [[#C040]], [[#C046]], [[#F-V3-004]]

### F-V3-006 — Rango de VIF declarado 1,13–1,58 frente a 1,12–1,40 en vif.csv

`MODELOS_Y_FUNCIONES.md` (L458) sostiene «Valores cercanos a 1 (los actuales van de 1,13 a 1,58) indican que los regresores no se explican entre sí». `vif.csv:2-6` contiene cinco valores —car_age 1.38, mileage_km 1.4, price_usd 1.16, hp 1.12, condition_score 1.14—, cuyo mínimo es 1,12 y su máximo 1,40; `INFORME_TECNICO.md:1409` publica «VIF 1,12–1,40» a través de `actualizar_numeros.py:92-95`. Ninguno de los dos extremos del corpus coincide con el archivo que invoca como respaldo, y el CSV incluye `price_usd`, variable ausente de la fórmula citada en L438. Relación: desajuste numérico entre el texto metodológico y su tabla.

— polarity: negative · confidence: high · related: [[#C047]], [[#F-V3-004]]

### F-V3-007 — Kruskal-Wallis: tres estadísticos para el mismo contraste (25,741 / 32,818 / 44,313)

`MODELOS_Y_FUNCIONES.md` (L462) afirma «Resultado vigente: H = 25,741, p = 1e−05». `tests.csv:2` registra `Kruskal-Wallis precio por tier,32.818,0.0`; `comparaciones.csv:2` registra `precio por tier de marca,1462,44.313,0.0,10000.0,29500.0,…`; e `INFORME_TECNICO.md:1528` cuantifica «H = 44,313». El p del corpus (1e−05) tampoco coincide con el `p_valor=0.0` de ambas tablas, que `actualizar_numeros.py:96-100` despliega como «0,00000» en `INFORME_TECNICO.md:1409`. La conclusión cualitativa de L464 —«los tiers no provienen de la misma distribución de precios»— se mantiene con cualquiera de los tres estadísticos, pero el número atribuido al test no se deriva de la tabla citada ni del informe técnico. Relación: inconsistencia numérica entre evidencias de un mismo contraste.

— polarity: negative · confidence: high · related: [[#C048]], [[#C005]]

### F-V3-008 — «104 observaciones en 2 años bastan para depreciación» frente al límite de serie mensual declarado

`AUTOMATIZACION.md` (L645) afirma en su tabla de periodicidad «Snapshots de precio (`price_history`) | Semanal, tras Revolico | 104 observaciones en 2 años bastan para depreciación», y (L690) repite «104 semanas ≈ 2 años». `MODELOS_Y_FUNCIONES.md` (L485) establece como límite explícito «No se presenta una curva de depreciación temporal: hace falta una serie mensual de 6–12 meses»; `PRESENTACION_STORYTELLING.md` (L290) sitúa la «serie de precios de 6–12 meses» en «Lo que viene» e `INFORME_TECNICO.md:1401` registra que el modelo actual «no encuentra una pendiente anual significativa tras corregir el kilometraje». La cifra 104 se presenta como suficiencia en un documento y como trabajo futuro en los otros dos; no hay en `outputs/tables/` ninguna estimación de depreciación temporal que la sostenga (`modelo_depreciacion.csv` es un corte transversal de 28 filas). Relación: sobreafirmación de un resultado frente al límite metodológico citado.

— polarity: negative · confidence: high · related: [[#C003]], [[#C010]], [[#C051]], [[#C064]]

### F-V3-009 — La corrida de calidad de 2.014 filas se describe como corrida real junto a un KPI vigente de 2.174

`AUTOMATIZACION.md` (L706) registra «`validar_calidad.py`: 6 reglas, cuarentena en `Data/_cuarentena/`, umbral 10 %. Corrida real: 2.014 filas, 0 inválidos», dentro de un apartado rotulado «Ya hecho (23/11/2026)». `INFORME_TECNICO.md:1391` sitúa ese 2.014 en la corrida del 23/11/2026 («2.014 anuncios limpios, de ellos 1.323 locales y 691 de importación»), anterior a la regeneración que `INFORME_TECNICO.md:1399` describe con 2.174/1.483/691. `kpis.csv:2-4` y el propio corpus (README L42, storytelling L123 y L195) usan ya 2.174. El corpus no marca el 2.014 como corrida histórica, de modo que dos recuentos de la misma magnitud conviven sin jerarquía temporal explícita. Relación: desajuste de vigencia entre una medición citada como real y el KPI actual.

— polarity: negative · confidence: high · related: [[#C065]], [[#C002]]

### F-V3-010 — Cuadro 3, Cuadro 4 y la referencia egipcia: respaldo convergente en el informe técnico

`PRESENTACION_STORYTELLING.md` (L145) afirma «en 2025 se transportaron 781 millones de pasajeros, un 59 % menos que en 2019. En ómnibus fueron 324 millones, un 71 % menos»; el Cuadro 3 (L346, L352) da 1.899,9 → 781,1 y 1.102,2 → 324,0, y el Cuadro 4 (L362) da 7.552 accidentes y 751 fallecidos en 2025. `INFORME_TECNICO.md:1371` confirma «los 12 anuarios del ONEI y sus 233 archivos», la caída del 59 % y del 71 % y «9,9 fallecidos por cada 100 accidentes en 2025»; 751/7.552 = 9,94 por 100, coherente con esa razón. La cifra de 23.500 anuncios de `Egyptian-Used-Cars` (L277) aparece también en `INFORME_TECNICO.md:1080` y `:1518`. Los porcentajes del texto son redondeos correctos de las cifras del cuadro y del informe. Relación: respaldo externo e interno consistente.

— polarity: positive · confidence: high · related: [[#C022]], [[#C035]], [[#C038]]

### F-V3-011 — Cifras de cobertura y de espacio sin contrapartida en `outputs/tables/` ni en el informe técnico

Varios enunciados numéricos del corpus no tienen fila en los CSV vigentes ni registro en `INFORME_TECNICO.md`: «3.958 anuncios ICD» (`README.md`, L70); «256 vehículos» de 11 concesionarios (`README.md`, L12 y L68) frente a «25 concesionarios» y «22 talleres» geolocalizados (`PRESENTACION_STORYTELLING.md`, L187); la encuesta «28 personas», «14», «16 de 18», «4.000 USD», «10.000 USD», «28 y 25 de 30 entrevistas» (L251); «11 estaciones solares» y «21 estaciones de CIMEX+MITRANS» (L265); «205.002 KB ≈ 0,20 GB», «3,3 GB (174 archivos)» y los quince subtotales del mapa de carpetas (`ESTRUCTURA_ESPACIO.md`, L741–764), de los que el informe solo documenta «pasó de 20 GB a 10 GB» (`INFORME_TECNICO.md:1471`). El panel de «107 KB» (`AUTOMATIZACION.md`, L659) sí es consistente con los 109.929 bytes que el inventario E3 midió para `Data/dashboard.html`. La cifra «233 archivos» de `README.md:21`, en cambio, coincide literalmente con `INFORME_TECNICO.md:1371`. Relación: ausencia de evidencia verificable en las fuentes de contraste, sin que ello establezca la falsedad de las cifras.

— polarity: negative · confidence: medium · related: [[#C017]], [[#C018]], [[#C026]], [[#C033]], [[#C034]], [[#C060]], [[#C068]], [[#C069]]

### F-V3-012 — El total de ancho de banda «sin cambios» no surge de la suma de las filas de su propia tabla

`AUTOMATIZACION.md` (L721–724) tabula «Circuitos (2 páginas) | Diario | ~2–5 KB/día», «Marketplaces (8 sitios, 2 páginas) | Semanal | ~20–50 KB/semana», «Revolico incremental | Semanal | ~0,5 MB/semana» y cierra con «**Total estimado** | — | **~5–10 MB/mes** | **~50–90 MB/mes**». La conversión de las tres filas al escenario sin cambios da ~0,06–0,15 MB/mes, ~0,09–0,22 MB/mes y ~2,15 MB/mes, es decir ~2,3–2,5 MB/mes, por debajo del total declarado; con cambios las filas suman ~56–100 MB/mes, del orden del intervalo publicado. El párrafo de L726 califica explícitamente el cuadro como «estimaciones de diseño, no mediciones de facturación», y no hay serie de facturación en `outputs/tables/` ni en el informe técnico que permita dirimir el total. Relación: divergencia aritmética interna en una tabla presentada como estimación.

— polarity: negative · confidence: medium · related: [[#C066]]


## §4 — v4-novelty


## Resumen

- El corpus sí declara diferenciadores: el temporal de §7 frente a Egyptian-Used-Cars, el de integración de «cuatro capas» en §5 y el de honestidad metodológica en MODELOS §4; solo el primero adopta forma de párrafo comparativo contra un trabajo cercano.
- No cita trabajos cercanos con marcadores: cero `[N]`, DOI o arXiv en los 8 archivos y cero coincidencias con las 41 entradas de `Data/referencias.md`; P014 y P029–P032 aparecen por nombre, y P033–P037 solo viven en el anexo.
- Las cinco reclamaciones `novelty` (C013, C052, C058, C061, C107) son ingeniería local sin componente sustantivo demostrado: el criterio master se satisface en la forma de un diferenciador y queda abierto en engagement y en sustantividad.

### F-V4-001 — §7 declara el diferenciador temporal frente a Egyptian-Used-Cars en un párrafo comparativo

El claim C107 (e1-claims, líneas 842–847; tipos `contextual`, `novelty`) recoge `PRESENTACION_STORYTELLING.md` §7 «El espejo egipcio», líneas 275–283: «Tomamos como referencia **`Egyptian-Used-Cars`**, uno de los análisis de mercado automotriz más completos que tenemos: 23.500 anuncios, historial mensual de precios, econometría, SQL, Tableau y Power BI», y más adelante «Nuestro proyecto ya tiene esa arquitectura: ingesta incremental, limpieza y features, análisis exploratorio, modelo econométrico con tests, benchmarks e infravalorados, salidas versionables. La diferencia es el tiempo. Egipto construyó su serie durante meses; aquí el mecanismo ya está sembrado y cada semana suma una observación real de precio». El diferenciador declarado es explícito y de alcance local: no se reclama otra arquitectura, sino que el mecanismo de series ya está instalado antes de acumular datos. E2 (P014, líneas 210–221) identifica vecino más cercano a `Egyptian-Used-Cars` —proyecto/repositorio, autoría no declarada en el corpus, sin año, sin URL, `(metadata incomplete: repositorio no enlazado; imposible verificar autoría, licencia o fecha desde el corpus)`— y lo marca `Cited in document: yes` en la línea 277.

El criterio `V4.differentiation_from_prior_art` para `level=master` se lee: «Differentiator articulated with at least one explicit comparison paragraph to one closest prior work» (level-criteria.md, línea 88). §7 es un apartado propio con un párrafo comparativo formulado contra ese único vecino, de modo que la condición formal se cumple. La cita es nominal, sin marcador ni ficha verificable, y el propio E1 (C107) registra la tensión con `ARQUITECTURA_DATOS.md:566`, que califica el trabajo como «Fase 0–1 de diseño»; la comparación sostiene la forma del diferenciador, no su estado implementado.

— polarity: positive · confidence: high · related: [[#C107]], [[#C013]], [[#P014]], [[#F-V4-005]] · criteria: V4.differentiation_from_prior_art.master

### F-V4-002 — Las cinco reclamaciones de novedad son ingeniería local sin componente sustantivo demostrado

Las cinco reclamaciones etiquetadas `novelty` en E1 son C013 («**El diseño está listo para crecer igual que crezcan los datos.**», L283), C052 («El objetivo no es "comprar un motor más rápido", sino cambiar la complejidad por ejecución de `O(total)` a `O(nuevo + particiones consultadas)`», L512–514), C058 («**Recolectar → procesar → publicar.** Ningún job de recolección hace `git push`; ningún push dispara scrapers», L637), C061 («llevan un marcador oculto `<!-- kpi:clave -->` […] `actualizar_numeros.py` lee los CSV y las bases vigentes y reemplaza **solo el número**», L663) y C107 (L279–283). Ninguna emplea verbos de primacía ni propone un método nuevo: C052 enuncia un objetivo de complejidad, C058 una separación de etapas y C061 una convención de plantillas, mientras C013 y C107 reclaman disponibilidad. El vecino más cercano del mapa E2 para estas reclamaciones es P014, al que el propio corpus atribuye «ingesta incremental, limpieza y features […] salidas versionables» (L279): la diferencia que el documento declara contra él es temporal («La diferencia es el tiempo», L281), no de componente ni de arquitectura.

El criterio `V4.scope_of_novelty_claim` para `level=master` exige «Component novelty + integration novelty: one of the two should be substantive» (level-criteria.md, línea 97). El lado de integración queda enunciado en C058 y C061 y contrastado una sola vez en C107; la sustantividad no se demuestra comparativamente contra P014 ni contra P029–P032 (modelo hedónico, Kruskal-Wallis, VIF y Welch, invocados sin atribución en `MODELOS_Y_FUNCIONES.md` §3, L433–470). C052 declara además la línea base como trabajo futuro —`benchmark_result.csv` se anuncia en L566—, de modo que el cambio de complejidad no tiene medición propia en el corpus. La calibración master no se alcanza en el eje de sustantividad: las cinco reclamaciones permanecen en novedad de alcance local e incremental.

— polarity: negative · confidence: high · related: [[#C013]], [[#C052]], [[#C058]], [[#C061]], [[#C107]], [[#P014]], [[#P029]], [[#P030]], [[#P031]], [[#P032]] · criteria: V4.scope_of_novelty_claim.master

### F-V4-003 — Cero marcadores `[N]`, DOI o arXiv para trabajos cercanos en los ocho archivos

E2 (nota de entrada, líneas 17–19; H1, líneas 585–587; cotejo, línea 471) constata que «el corpus no contiene marcadores `[N]`, DOI ni identificadores arXiv; ninguno de los 41 autores, títulos ni fuentes institucionales de `Data/referencias.md` aparece citado», con «cero coincidencias» en los dos sentidos. La verificación literal de los 41 apellidos/títulos dio «cero resultados» y los únicos aciertos parciales de cadena («Che,», «Pal,», «Etro») resultaron falsos positivos dentro de «Chevrolet», «página» y «película». Los trabajos cercanos que el corpus sí menciona —P014 `Egyptian-Used-Cars` (L277), P015–P017 repos ICD/AutosxCuba/Mercado-automotriz (L70) y P029–P032 métodos estadísticos (L433–470)— comparecen solo por nombre, sin marcador y con `(metadata incomplete)`; los cinco vecinos académicos de `Likely missing` (P033–P037) tienen ficha y marcador `[29]`, `[30]`, `[21]`, `[22]` y `[12]` en `Data/referencias.md`, pero no aparecen en ninguno de los 8 archivos.

El criterio `V4.prior_art_engagement` para `level=master` exige tres condiciones conjuntas: «Closest prior works cited, contrasted, and discussed in their own subsection» (level-criteria.md, línea 106). Solo la tercera se da de forma aislada en §7, y aun allí falta el marcador que acredite la cita. La consecuencia observable es una documentación con diferenciadores declarados pero bibliográficamente muda en su cara pública: el anexo y el corpus describen «dos regímenes de citas distintos» (E2, H1, L587).

— polarity: negative · confidence: high · related: [[#C107]], [[#C013]], [[#P014]], [[#P015]], [[#P016]], [[#P017]], [[#P029]], [[#P030]], [[#P031]], [[#P032]], [[#P033]], [[#P034]], [[#P035]], [[#P036]], [[#P037]] · criteria: V4.prior_art_engagement.master

### F-V4-004 — Diferenciadores de contenido declarados sin contraste con P033, P034, P035 ni P037

Además del diferenciador temporal, el corpus declara tres contrastes de contenido. En `README.md` §Fuentes de datos (L73): «La conversión usa la **TRMI informal de elTOQUE (18/11/2026): 930 CUP/USD, 1.000 CUP/EUR y 845,35 CUP/MLC**. Nunca se usa la tasa oficial para los precios del mercado» (C012). En storytelling §5 (L255): «Cruzar estas cuatro capas convierte un catálogo de anuncios en inteligencia de mercado». En `MODELOS_Y_FUNCIONES.md` §4 (L482–486, C051): «No se usa la tasa oficial de cambio. No se imputan precios ni kilómetros faltantes. No se afirma causalidad […] No se mezclan mercados: local e importación se reportan por separado».

E2 sitúa frente a esos diferenciadores los vecinos académicos que el corpus no cita: P033 —Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A. (2024), *Using AI in the informal currency market: evidence from Cuba*, *Applied Economics*, `[29]` en el anexo—, con «solapamiento directo con P004 (TRMI informal)» (L551–555); P034 —Castro Fernández, M.; Vilaragut Llanes, M.; Hernández, J. C. (2024), *Electromobility and Energy Transition in Cuba*, *Sustainability*, `[30]`—, «antecedente cubano directo» de las secciones 2, 5 y 6 (L557–561); P035 —Krotov, V.; Johnson, L.; Silva, L. (2020), *Legality and Ethics of Web Scraping*, `[21]`— y P036 —Brown, M. A.; Gruen, A.; Maldoff, G.; Messing, S.; Sanderson, Z.; Zimmer, M. T. (2025), *Web scraping for research*, *Big Data & Society*, `[22]`—, frente a la tensión entre «respeta los términos de uso» (L112) y la impersonación de navegador con FlareSolverr (L833); y P037 —Hulten, C. R. (2003), *Price Hedonics: A Critical Review*, `[12]`, `(metadata incomplete)`—, frente a la justificación del modelo hedónico en L433–452. Ninguno de los cinco se discute en el corpus con marcador, resultado o limitación ajena.

— polarity: negative · confidence: high · related: [[#C012]], [[#C051]], [[#P004]], [[#P028]], [[#P029]], [[#P033]], [[#P034]], [[#P035]], [[#P036]], [[#P037]], [[#F-V4-003]] · criteria: V4.prior_art_engagement.master

### F-V4-005 — «Listo para crecer» y «ya tiene esa arquitectura» exceden el estado Fase 0–1 declarado

Los claims C013 y C107 formulan la disponibilidad en términos más fuertes que el estado que el propio corpus registra. C013 (L283): «**El diseño está listo para crecer igual que crezcan los datos.**»; C107 (L279): «Nuestro proyecto ya tiene esa arquitectura». `ARQUITECTURA_DATOS.md` §6 (L566) cierra con «Este documento es la Fase 0–1 de diseño; la línea base de rendimiento se guardará en `benchmark_result.csv` antes de tocar el pipeline» y consigna que «`import duckdb` falla con `SIGILL` (Instrucción ilegal)» con el motor recomendado en L520 pendiente de reevaluación; E1 (C052, C053, C055) consigna que la recomendación queda condicionada por ese bloqueo y que la medición de línea base no figura en el corpus. En paralelo, `MODELOS_Y_FUNCIONES.md` §4 (L485) y storytelling §8 (L290) sitúan la serie de precios de 6–12 meses en el trabajo futuro, mientras `AUTOMATIZACION.md` §2 (L645) afirma que «104 observaciones en 2 años bastan para depreciación» (C010).

Frente a P014, cuyo «historial mensual de precios» se describe en L277 como ya construido, el diferenciador de C107 se apoya en un mecanismo sembrado, no en una serie observada. Bajo `V4.scope_of_novelty_claim.master` («Component novelty + integration novelty: one of the two should be substantive», línea 97), la reclamación de disponibilidad no se sostiene en componente ni en integración medidos dentro del corpus; es un sobreclaim de estado, no de primacía frente a arte previo.

— polarity: negative · confidence: high · related: [[#C013]], [[#C107]], [[#C010]], [[#C052]], [[#C053]], [[#C055]], [[#P014]], [[#F-V4-001]], [[#F-V4-002]] · criteria: V4.scope_of_novelty_claim.master

### F-V4-006 — Mapa sin búsquedas nuevas ni lectura L3: novedad no confirmable

El frontmatter de E2 declara `queries_run: 0`, `papers_l1: 37`, `papers_l2: 0`, `papers_l3: 0` y `degraded: false` para el mandato estrecho de cotejo. La nota de entrada (L17) precisa que «no se ejecutaron búsquedas web nuevas —los metadatos se reutilizan de la verificación OpenAlex/Crossref del 27/11/2026 consignada en `Data/referencias.md`—» y que «todos los ítems son L1, sin lectura de resúmenes (L2) ni de texto completo (L3)»; el cierre (L608) limita el mapa al cotejo entre corpus y anexo, «no para proponer obras externas nuevas ni para certificar enlaces institucionales». Las 37 fuentes del corpus quedan marcadas `(metadata incomplete)` (E2, L517 y H3, L593–595).

En ese régimen no hay antecedente nuevo capaz de desplazar a P014 o a P033–P037 como vecinos más cercanos, pero tampoco lectura L3 que permita afinar solapamientos. Bajo `V4.prior_art_engagement.master` la lectura permitida es «sin verificación de originalidad en esta pasada», no «novedad confirmada»: ninguna de las cinco reclamaciones novelty puede certificarse como libre de arte previo con este mapa.

— polarity: neutral · confidence: high · related: [[#C013]], [[#C052]], [[#C058]], [[#C061]], [[#C107]], [[#P014]], [[#P033]], [[#P034]], [[#P035]], [[#P036]], [[#P037]], [[#F-V4-002]], [[#F-V4-003]] · criteria: V4.prior_art_engagement.master


## §5 — v5-state-of-the-art


- Cobertura: 0 de 41 obras de `Data/referencias.md` aparecen citadas en los 8 archivos (0 %), frente al tramo 25–60 de `V5.coverage_breadth.master`; los cinco clústeres del mapa sí tienen fuente nominal (32 de 37 ítems citados).
- Actualidad: 7 de 32 fuentes citadas (21,9 %) llevan año y 24 (75 %) no lo tienen verificable, por debajo del 40 % de `V5.recency.master`; el anexo contrastado alcanza 18 de 38 fechadas (47,4 %), pero sus obras no entran en el corpus.
- Peso y ausencias: 0 marcadores, DOI o arXiv y 37 de 37 fuentes `(metadata incomplete)`; los organismos se nombran en el cuerpo, cuatro de cuatro métodos quedan sin atribución y las cinco ausencias probables siguen sin aparecer.

### F-V5-001 — Cobertura académica — 0 de 41 obras del anexo citadas en los ocho archivos

El cotejo dirigido de E2 (L19, L471, L585–L587) da **cero coincidencias** entre el corpus y las 41 entradas de `Data/referencias.md` (L8–L87): no hay marcadores `[N]`, DOI ni identificadores arXiv en ninguno de los 8 archivos, y los únicos aciertos de cadena («Che,», «Pal,», «Etro») resultaron falsos positivos dentro de «Chevrolet», «página» y «película». Los apellidos y títulos del anexo —Akerlof 1970 [1], Du et al. 2026 [9], Gegić et al. 2019 [14], Madhusudhanan et al. 2024 [18], Vidal Alejandro et al. 2024 [29]— no aparecen en el texto cacheado. El corpus apoya sus cifras en organismos y normas citados por nombre (README L12, L71; storytelling L145, L242), no en obras con ficha: las 32 fuentes efectivamente citadas (P001–P032) son instituciones, instrumentos legales, repositorios, directorios y métodos sin atribución.

El criterio `V5.coverage_breadth.master` se lee: «Main + adjacent clusters covered (25–60 papers)». La medida relevante es de **0/41 obras académicas (0 %)**, no de 32 fuentes nominales: ninguna de las 41 entra en el argumento del corpus. Los flags `Citada en el informe: sí` de [1], [9], [14], [18], [26] y [29] aluden al informe técnico de la pasada 1 y no a esta documentación (E2 L17, L471), de modo que no elevan el recuento. La cobertura que el criterio describe queda, por tanto, en cero, y la diferencia entre anexo y corpus es de régimen de citas, no de sola cantidad.

— polarity: negative · confidence: high · related: [[#P001]], [[#P033]], [[#P037]], [[#F-V5-006]], [[#F-V5-007]] · criteria: V5.coverage_breadth.master

### F-V5-002 — Cobertura por clúster — cinco clústeres con fuente nominal y 13 de 32 fuentes institucionales o normativas

El mapa de E2 (L21–L468) reparte 32 fuentes citadas en cinco clústeres, todos representados: fuentes institucionales y estadísticas cubanas 8/8 (P001–P008: ONEI, Gaceta Oficial 65/2026, BCC, elTOQUE, CIMEX, MEP, MFP, Gobierno), normativa 5/5 (P009–P013: Acuerdo 9811/2024, Decreto 163/2026, resoluciones 104/17/52/102, 171–175 y 340, Circular 03/2026), repositorios de referencia 4/4 (P014–P017: Egyptian-Used-Cars, ICD, AutosxCuba, Mercado-automotriz), directorios/geoservicios/herramientas 11/11 (P018–P028) y métodos sin atribución 4/4 (P029–P032). Las cinco entradas restantes del mapa (P033–P037) son ausencias propuestas, no fuentes del corpus. La composición es 13/32 institucionales o normativas (40,6 %), 11/32 directorios y herramientas (34,4 %), 4/32 repositorios (12,5 %) y 4/32 métodos (12,5 %).

En términos de clústeres temáticos la cobertura nominal incluye incluso la frontera —directorios de carga, geocodificación y librerías anti-bot (P018–P028), que en nivel master no es exigible—, pero ninguna de las 32 fuentes resuelve a una ficha bibliográfica consultable: las 37 entradas del mapa llevan `(metadata incomplete)` (E2 L517, L595). La distinción entre cobertura de temas y cobertura de trabajos es la que aplica `V5.coverage_breadth.master`: los cinco clústeres están presentes por nombre, mientras que el peso académico correspondería a las cinco obras ausentes de F-V5-007.

— polarity: neutral · confidence: high · related: [[#P001]], [[#P014]], [[#P018]], [[#P029]], [[#F-V5-001]], [[#F-V5-007]] · criteria: V5.coverage_breadth.master

### F-V5-003 — Actualidad — 7 de 32 fuentes citadas con año (21,9 %) y 24 (75 %) sin año verificable

La distribución de E2 (L519–L534) registra en el mapa 6 entradas de 2026, 1 de 2025, 3 de 2024, 2 de 2021 o antes, 1 rango 2014–2025 (ONEI) y 24 sin año verificable. Desglosadas por fuentes realmente citadas (P001–P032), quedan **7 con año** —seis de 2026 (P002 Gaceta 65/2026, P004 elTOQUE 18/11/2026, P010 Decreto 163/2026, P011 resoluciones /2026, P012 resoluciones 171–175 y 340, P013 Circular 03/2026) y una de 2024 (P009 Acuerdo 9811)— más el rango de ONEI: 7/32 (21,9 %), o 8/32 (25,0 %) si el rango se cuenta como fecha. Las **24 restantes (75,0 %)** no tienen año verificable. Sobre las 37 entradas del mapa, el tramo 2022–2026 suma 10 (27,0 %) y las sin año 24 (64,9 %); ninguna de las citadas es preprint.

El criterio `V5.recency.master` exige «At least 40% from the last 5 years; foundational classics balanced». El corpus no alcanza ese umbral con sus propias fuentes (21,9 %, o 27,0 % mapa completo), y la condición de clásicos fundacionales no es aplicable a un conjunto sin obras académicas. El anexo contrastado sí lo cumpliría: 18 de 38 referencias fechadas de 2022–2026 (47,4 %) y 18 de 41 entradas (43,9 %), con 20 de 38 de 2021 o antes (E2 L523–L532; `informe-tecnico-2026-11-28-iter4.v5-state-of-the-art.md` L25). Esas obras, incluido [24] arXiv:2601.14311 (2026), no aparecen en el corpus; el seguimiento de preprints de los últimos 18 meses es exigible en phd, no en master, por lo que no se emite hallazgo separado por [24].

— polarity: negative · confidence: high · related: [[#P001]], [[#P002]], [[#P004]], [[#P010]], [[#F-V5-004]] · criteria: V5.recency.master

### F-V5-004 — Peso de la citación — organismos y fecha de vigencia nombrados en el cuerpo en las afirmaciones load-bearing

La cara pública del corpus sí nombra la fuente en el momento del uso. El storytelling abre la sección 1 con «El ONEI lo pone en números: en 2025 se transportaron **781 millones de pasajeros**, un 59 % menos que en 2019» (L145) y repite la atribución en el encabezado del Cuadro 3 (L341) y del Cuadro 4 (L354). La divisa, una de las «cuatro fuerzas invisibles», se presenta como «la **TRMI informal: 930 CUP por USD** (elTOQUE, noviembre 2026)» (L242), con la fecha de vigencia explícita «TRMI informal de elTOQUE (18/11/2026): 930 CUP/USD, 1.000 CUP/EUR y 845,35 CUP/MLC» (L73), que `to_usd` reutiliza como convención declarada (`MODELOS_Y_FUNCIONES.md` L409). El marco regulatorio nombra a CIMEX S.A. y al MEP en el cambio del 07/02/2026 (L177), al MFP y la Circular 03/2026 en el del 15/05/2026 (L179) y al Decreto 163/2026 en la valoración del activo (L197).

El criterio `V5.citation_weight.master` se lee: «Load-bearing claims cite source + author named in body at first mention». En documentación institucional el organismo cumple la función de autor, y en estos pasajes aparece nombrado en la primera mención; la fecha de vigencia de la TRMI añade una ancla temporal que no aparece en el anexo para sus propias obras. Es la mitad nominal del criterio la que queda calibrada en estas afirmaciones —no hay autores personales en el corpus—, y constituye un hallazgo positivo de peso dentro de un conjunto donde la mitad resolutiva no está presente (F-V5-005).

— polarity: positive · confidence: high · related: [[#P001]], [[#P004]], [[#P005]], [[#P010]], [[#F-V5-005]] · criteria: V5.citation_weight.master

### F-V5-005 — Peso de la citación — cero marcadores, DOI o arXiv y 37 de 37 fuentes `(metadata incomplete)`

La busca literal en los 8 archivos no encuentra marcadores `[N]`, DOI ni `arXiv` (E2 L19, L471, L587). Las 37 fuentes del mapa están marcadas `(metadata incomplete)` (E2 L517, L595): ninguna aporta a la vez URL de destino, año de publicación e identificador; solo se verifican localmente números normativos (Decreto 163/2026, Gaceta 65/2026, Acuerdo 9811/2024, Circular 03/2026, TRMI del 18/11/2026) y la URL local de FlareSolverr (L833). La afirmación cuantitativa «según reportes de prensa ha dejado circuitos con más de **60 horas sin electricidad**» (L181) no identifica medio ni reporte (P019, E2 L281–L292), y la cifra de 23.500 anuncios de Egyptian-Used-Cars (L277) remite a un repositorio sin enlazar (P014, E2 L210–L221).

Con `V5.citation_weight.master`, la condición «source + author named in body at first mention» queda satisfecha en el componente de nombre para los organismos de F-V5-004, pero la fuente citada no es resoluble en ninguno de los 37 casos. El peso de las afirmaciones load-bearing descansa, por tanto, en evidencia interna y en atribuciones nominales sin ficha: las tres cifras de apertura del README (974 autos, 2.232 anuncios, 256 vehículos; L12), la mediana de 21.000 USD (L195) y la caída del 59 % (L145) no enlazan con tabla, norma ni documento verificable desde el propio corpus.

— polarity: negative · confidence: high · related: [[#P014]], [[#P019]], [[#P028]], [[#F-V5-004]] · criteria: V5.citation_weight.master

### F-V5-006 — Métodos estadísticos — cuatro de cuatro justificados sin atribución y tres antecedentes del anexo fuera del texto

`MODELOS_Y_FUNCIONES.md` dedica §3.1 (L433–L452) al modelo hedónico log-lineal y declara que «los atributos hedónicos: precio, antigüedad, km, potencia, condición y marca son los determinantes estándar de un modelo hedónico de autos usados» (L446) sin remitir a obra alguna; §3.2 (L454–L458) justifica el VIF, §3.3 (L460–L464) el Kruskal-Wallis y §3.4 (L466–L470) el Welch, igualmente sin autoría. Los cuatro métodos son P029–P032 en E2 (L411–L467), todos con `Document reference: ninguno`. La conclusión load-bearing de §3.1 —«no permite afirmar una tasa de depreciación anual ni una prima premium con esta muestra transversal» (L450)— se apoya en la especificación y en los p_valores, no en literatura metodológica.

E2 H4 (L597–L599) registra que el respaldo existe en el anexo, no en el corpus: [12] Hulten 2003, revisión crítica de precios hedónicos (`Data/referencias.md` L30, con `(metadata incomplete: PDF no extraído)`), [13] Francke & Van de Minne 2020 (L32) y [9] Du et al. 2026 (L24) tienen `Citada en el informe: no` y ninguno aparece en los 8 archivos. De ellos solo [12] entra en la lista de ausencias probables (P037); [13] y [9] se registran aquí como antecedentes sin atribuir en el cuerpo, sin duplicar el recuento de F-V5-007. El criterio `V5.citation_weight.master` —«source + author named in body at first mention»— no se cumple en estos cuatro pasajes, donde la justificación estadística es explícita pero la mitad nominal está ausente.

— polarity: negative · confidence: high · related: [[#P029]], [[#P030]], [[#P031]], [[#P032]], [[#P037]], [[#F-V5-004]] · criteria: V5.citation_weight.master

### F-V5-007 — Ausencias probables — cinco obras del anexo con solapamiento directo permanecen fuera del corpus

La sección «Likely missing important works» de E2 (L547–L579) propone cinco obras, todas de `Data/referencias.md` y todas ausentes de los 8 archivos: [29] Vidal Alejandro et al. 2024 (P033, L551–L555), [30] Castro Fernández et al. 2024 (P034, L557–L561), [21] Krotov et al. 2020 (P035, L563–L567), [22] Brown et al. 2025 (P036, L569–L573) y [12] Hulten 2003 (P037, L575–L579). Cada una toca una afirmación load-bearing: la TRMI de 930 CUP/USD convertida en todas las monedas (L73, L242), las 11 estaciones solares Dongfeng/NWI y 21 de CIMEX+MITRANS y el coste de propiedad eléctrica (L249, L265), y la tensión entre «no elude mecanismos anti-automatización» (L112) y el uso de `patchright`/FlareSolverr (L833), además del modelo hedónico de F-V5-006. [29] lleva `Citada en el informe: sí` en el anexo (L64) y [30], [21], [22], [12] llevan `no` (L66, L48, L50, L30); el flag describe el informe técnico, no esta documentación.

El criterio `V5.missing_important_work.master` exige «Top-5 most-cited of each adjacent cluster expected». Las cinco ausencias se enumeran, pero E2 declara `queries_run: 0` y `no se proponen obras nuevas porque no se ejecutaron búsquedas` (frontmatter L8; L549): la selección deriva de solapamiento temático directo y no de una verificación independiente de las obras más citadas por clúster, como sí ocurrió en mediciones anteriores del informe técnico. Las cinco permanecen, por tanto, como ausencias probables con evidencia de no-citación alta y con escala de relevancia no re-verificada en este pase.

— polarity: negative · confidence: medium · related: [[#P033]], [[#P034]], [[#P035]], [[#P036]], [[#P037]], [[#F-V5-001]], [[#F-V5-006]] · criteria: V5.missing_important_work.master


## §6 — v6-reproducibility


# V6 — Reproducibilidad

Alcance: se evaluó el corpus unificado de 8 archivos (L1–833) contra los criterios `V6.*.master` de `level-criteria.md`, leyó íntegramente `reviews/corpus-documentacion-2026-11-28.e3-artifacts.md` y contrastó cada ruta citada con el checkout real `/home/thony70807/Proyectos/El precio de moverse en Cuba` (HEAD `77ab644`, 28/11/2026). Las referencias `L…` son del texto cacheado. Las verificaciones de ejecución se hicieron con `Auxiliares/.venv-py/bin/python`.

## Hallazgos

### F-V6-001 — README completo con quickstart, dependencias y ejemplos de uso

El corpus incluye el `README.md` íntegro (L8–116): nombre y ubicación del proyecto (L10–14), contenido (L16–22), Quickstart (L24–42), estructura (L44–61), fuentes (L63–73), configuración (L75–89), sitio MkDocs (L91–101), documentación de referencia (L103–108) y límites (L110–115). El nivel master exige README + lista de dependencias + ejemplos breves de uso: los tres están presentes y verificados en disco (`README.md` de 116 líneas, `requirements.txt`, `mkdocs.yml`). El mapeo componente→repositorio además está explicitado en `E3 §Code-to-document mapping`, donde 10 de 11 componentes se localizan; confirmé la existencia de `Data/analisis_rentabilidad/config.py`, ambos `MANIFEST.json`, `INFORME_TECNICO.md` y `docs/`.

— polarity: positive · confidence: high · related: [[#C076]] [[#C078]] [[#C080]] · criteria: V6.documentation.master

### F-V6-002 — Dependencias fijadas a serie menor

`requirements.txt` tiene 14 líneas y 12 dependencias activas con operador `~=` (`pandas~=2.2.0`, `numpy~=1.26.0`, `plotly~=5.18.0`, `statsmodels~=0.14.0`, `scipy~=1.11.0`, `beautifulsoup4~=4.12.0`, `curl_cffi~=0.7.0`, `tenacity~=8.2.0`, `trafilatura~=1.6.0`, `pyarrow~=14.0.0`, `mkdocs~=1.6.0`, `mkdocs-material~=9.5.0`), con comentario explícito: «Fijadas a versiones menores (criterio de reproducibilidad de nivel master)». El README declara Python 3.10+ y Git LFS (L26) y el entorno en uso es `Auxiliares/.venv-py` (verificado: `bin/python`, `bin/pip`, `bin/mkdocs`). No hay lockfile ni `pyproject.toml`, pero el nivel master no los exige (`V6.environment.phd`). La laguna de dependencias del pipeline de mapas se evalúa en F-V6-009.

— polarity: positive · confidence: high · related: [[#C076]] · criteria: V6.environment.master

### F-V6-003 — Comando único de reproducción y puntos de entrada documentados

El Quickstart (L28–32) da una sola secuencia: crear `Auxiliares/.venv-py`, instalar `requirements.txt` y ejecutar `Data/analisis_rentabilidad/scripts/run_all.py`. Verifiqué los 7 scripts que orquesta (`01_ingest.py`, `02_clean.py`, `03_eda.py`, `03b_baselines.py`, `03c_comparaciones.py`, `04_stats.py`, `05_benchmark.py`) y las tres llamadas finales (`actualizar_numeros.py`, `generar_dashboard.py --solo-si-cambia`, `exportar_parquet_compacto.py`). El corpus también documenta argumentos de `db_chunks.py verify|assemble` (L87–88) y de `mkdocs build|serve` (L96–98). `run_all.py` (60 líneas) imprime `ANALISIS COMPLETO` al terminar. Un comando único es criterio de nivel phd (`V6.entry_points.phd`), por lo que el corpus supera lo exigido en master.

— polarity: positive · confidence: high · related: [[#C076]] [[#C077]] [[#C081]] [[#C082]] · criteria: V6.entry_points.master

### F-V6-004 — Prueba de humo del componente central, ejecutada y superada

`E3 §Tests` inventaría cinco pruebas; verifiqué que las cinco existen en `Auxiliares/herramientas/`: `test_dashboard.py` (92 líneas), `test_parquet_compacto.py` (83), `test_modelo.py` (84), `test_smoke_pipeline.py` (68) y `probar_actualizar_numeros.py` (74). Ejecuté la de humo con el entorno del repo: `Auxiliares/.venv-py/bin/python Auxiliares/herramientas/test_smoke_pipeline.py` → `4 pruebas superadas` (9 scripts compilan, 7 artefactos existen, CSV legibles, comando único documentado), código de salida 0. No hay `pytest.ini` ni `conftest.py`: son scripts autónomos, suficiente para el criterio master (smoke test del componente central), no para el de nivel phd.

— polarity: positive · confidence: high · related: [[#C074]] · criteria: V6.tests.master

### F-V6-005 — Bases reconstruibles desde chunks y salidas verificables

El corpus declara 82 fragmentos de 10 MB con SHA-256 (L81) y 52 de `pipeline.sqlite` (L82), y describe `db_chunks.py verify|assemble` para reconstruir las SQLite si faltan (L84–89). En disco hay 82 y 52 `.bin` respectivamente, ambos `MANIFEST.json` versionados y los cuatro scripts de chunking citados en L824–829. También están presentes `listings_clean.parquet`, los 6 CSV/TXT citados por nombre en `outputs/tables/` (21 archivos en total) y los 6 HTML de `outputs/charts/`. Las SQLite originales (839 MB y 755 MB) existen localmente pero están excluidas por `.gitignore`; la ruta de reconstrucción documentada cubre el criterio master de «access path».

— polarity: positive · confidence: high · related: [[#C073]] [[#C074]] [[#C081]] · criteria: V6.data_availability.master

### F-V6-006 — Semilla declarada en código pero ausente del corpus auditado

En las 833 líneas del corpus no aparece `semilla`, `seed`, `SEED` ni `PROYECTO_SEED`: L399–403 usan «preparación determinista» solo en el sentido de normalización sintáctica (`parse_price`, `parse_number`, deduplicación), no de aleatoriedad controlada. En cambio el código sí la declara: `Data/analisis_rentabilidad/scripts/run_all.py:16-23` define `SEED = 20261127`, llama a `random.seed` y `np.random.seed` y exporta `PROYECTO_SEED`; `03c_comparaciones.py:20,37` la consume con `np.random.default_rng(SEED)` para el bootstrap. `INFORME_TECNICO.md:1541-1545` (§71.5) documenta la semilla, pero ese archivo **no** es uno de los 8 bloques del corpus (encabezados `# ARCHIVO:` en L8, 119, 395, 493, 571, 629, 735 y 793): quien reproduzca solo desde los documentos auditados no puede fijar el bootstrap. Además la frase de §71.5 «se propaga a cada etapa» es imprecisa: solo `03c_comparaciones.py` lee la variable. El criterio master exige semilla en código **y** documento, consistente; aquí solo se cumple la mitad.

— polarity: negative · confidence: high · related: [[#C111]] · criteria: V6.determinism.master

### F-V6-007 — Línea base de rendimiento `benchmark_result.csv` no materializada

`ARQUITECTURA_DATOS.md` define la Fase 0 como «Línea base documentada» (L549) y afirma: «la línea base de rendimiento se guardará en `benchmark_result.csv` antes de tocar el pipeline» (L566), presentando el documento como «Fase 0–1 de diseño». Verifiqué que `Data/analisis_rentabilidad/outputs/tables/` contiene 21 archivos (KPIs, benchmarks, anomalías, modelo) pero ningún `benchmark_result.csv`, y que no existe en otra ruta del checkout; `E3 §Missing artifacts` lo registra. Sin esa medición previa no es verificable la comparación antes/después que motiva la adopción de DuckDB/Polars (L518–527, L551–554).

— polarity: negative · confidence: high · related: [[#C113]] [[#C114]] · criteria: V6.documentation.master

### F-V6-008 — Trazabilidad de «auditoría a dos años» descrita como implementada, pero sin artefactos

`AUTOMATIZACION.md` §5 dice «Se guarda, en UTC y con hashes» (L685) y enumera `manifiesto_ejecucion.jsonl` (L687), `VERSIONES.json` (L688), `watermarks.json` (L669), `_state/lfs_push_ledger.jsonl` (L671), `snapshots/YYYY-Www/` con `LATEST.json` (L690) y `DICCIONARIO.md`/`LIMITACIONES.md` (L693), con «regla de oro» de snapshots inmutables (L695). Verifiqué la ausencia de los siete artefactos en `Data/`, `Data/_state/`, `Data/_estado/` y la raíz: `Data/_state/` solo tiene `run_step.sh`, los cinco `job_*.sh` y `sitio_build.sh`. El propio corpus se contradice en L711 («Pendiente: … ledger LFS y unificación de `chunks/` con `partes/`»). Consecuencia directa para reproducibilidad: no hay hash de dependencias/config ni manifiesto por corrida que permita identificar la versión que produjo los resultados, y no hay estado histórico reconstruible.

— polarity: negative · confidence: high · related: [[#C064]] [[#C115]] · criteria: V6.data_availability.master V6.environment.master

### F-V6-009 — Comandos del mapa apuntan a un entorno inexistente y omiten dependencias

`Data/mapas/README.md` (L813–818) prescribe `cd Auxiliares` seguido de tres invocaciones `.venv/bin/python herramientas/generar_mapa_ofline.py …`. El checkout solo contiene `Auxiliares/.venv-py` (verificado), mientras `.gitignore` excluye `**/.venv/`; los tres comandos fallarían tal como están escritos. El README principal usa consistentemente `.venv-py` (L29–31, L96–98), por lo que la divergencia es interna al corpus. Además L833 describe la cadena anti-bot con `curl_cffi`, **`patchright`** y FlareSolverr en `http://127.0.0.1:8191/v1`, pero `requirements.txt` no incluye `patchright` ni `playwright`, y no se documenta la instalación/arranque de FlareSolverr. En consecuencia la generación del mapa no es reproducible desde una instalación limpia con los comandos publicados.

— polarity: negative · confidence: high · related: [[#C070]] [[#C071]] · criteria: V6.entry_points.master V6.environment.master

### F-V6-010 — Fuentes de datos sin URL de acceso ni licencia declarada

El corpus nombra los cinco grupos de fuentes (L63–73), da la URL del repositorio (L14) y la ruta de reconstrucción de las bases desde chunks (L84–89), pero no proporciona URL, DOI ni condición «available on request» para Revolico, los 8 marketplaces, los 11 concesionarios, las referencias externas, la normativa ni los anuarios del ONEI. El único pin de versión es una fecha (TRMI al 18/11/2026 en L73 y L409; anuarios 2014–2025 en L21), no un identificador de versión de dataset. Tampoco hay archivo `LICENSE*` en la raíz del checkout, y `INFORME_TECNICO.md:1543` lo confirma: «No se ha declarado todavía una licencia de datos o código». La licencia no es exigible en master, pero la adquisición de los crudos desde cero queda sin especificar.

— polarity: negative · confidence: high · related: [[#C073]] [[#C084]] · criteria: V6.data_availability.master

### F-V6-011 — Desajustes de ruta, recuento y fecha que impiden fijar la versión

L105 remite a `INFORME_TECNICO.md` «(secciones 1–60)», pero el archivo real llega hasta 71.15 (verifiqué §71.5 en L1541–1545). L659 cita `sitio_build.sh` sin ruta: está en `Data/_state/sitio_build.sh`, igual que los cinco `job_*.sh` de L705; `alertas.jsonl` (L681) está en `Data/_estado/`. El README declara «Actualizado: 23/11/2026» (L14) frente a un HEAD del 28/11/2026 (`77ab644`), y L21 afirma 233 archivos ONEI cuando en disco hay 234 (E3 lo registra). Son desajustes leves de mapeo, pero afectan directamente a la instrucción de nivel master de declarar dónde está cada componente y qué versión lo produjo.

— polarity: negative · confidence: medium · related: [[#C072]] [[#C083]] · criteria: V6.documentation.master

## Resumen

- 5 hallazgos positivos: README/quickstart completo, dependencias `~=`, comando único `run_all.py`, smoke test ejecutado (4/4) y bases reconstruibles desde 82+52 chunks.
- 6 hallazgos negativos: semilla ausente del corpus, línea base y artefactos de trazabilidad no materializados, comandos de mapas con `.venv` inexistente, fuentes sin URL/licencia y desajustes de ruta/fecha.
- A nivel master la infraestructura central es reproducible; las lagunas se concentran en determinismo documental y en artefactos declarados como listos pero ausentes en el checkout.


## §7 — v7-writing


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


## §8 — v8-bibliography


# V8 — Integridad bibliográfica — corpus de documentación de usuario

Nota de método y alcance. El mandato recibido es el contraste entre las fuentes citadas en el corpus de ocho archivos de cara al usuario y las 41 entradas de `Data/referencias.md`, más la verificación de URLs oficiales accesibles. En consecuencia: (a) el corpus es documentación de producto y no contiene una bibliografía propia, así que los conteos del frontmatter se refieren al anexo numerado de 41 entradas aportado para el contraste, no a una sección del corpus; (b) `verified: 37` / `unverified: 4` hereda la convención del anexo (L4–L6): son no verificadas las cuatro entradas marcadas `(metadata incomplete)` —[1], [10], [12] y [39]—, no papers inexistentes; (c) en esta pasada sí se re-verificaron en vivo [9], [24], [27] y [39]–[41], además de las sedes oficiales cubanas y las normas citadas en el corpus; el resto de metadatos del anexo se heredan de la verificación del 27/11/2026 consignada en `Data/referencias.md`; (d) los números de línea del corpus corresponden a la copia en caché indicada en el frontmatter; (e) se aplicó el criterio del evaluador de no reclamar enlace roto cuando el fallo es de transporte desde este entorno: esos casos se registran como «no confirmado desde aquí».

## Hallazgos

### F-V8-001 — Intersección vacía: el corpus no usa el anexo numerado de 41 entradas

Búsqueda directa sobre la copia auditada: **0 marcadores `[N]`** y **0 URL `doi.org` o `arxiv.org`** en las 833 líneas. El único `http://` del corpus es interno —«El scraper usa, en orden: `curl_cffi`… y **FlareSolverr** (`http://127.0.0.1:8191/v1`) para páginas como Cybo que devuelven 403 o verificación de seguridad» (L833)—; el resto de enlaces son rutas relativas entre los ocho archivos (L105–L108, L131, L381–L386). `Data/referencias.md` no aparece citado ni enlazado en ningún bloque. El anexo, a su vez, se declara derivado de otro documento: «Generado el 27/11/2026 desde `reviews/informe-tecnico-2026-11-27.e2-literature.md`» (L3), con entradas [1]–[41] (L8–L87).

Contraste entradas por entrada: de las 41, ninguna es citada en el corpus. Recíprocamente, las fuentes con que el corpus respalda sus cifras —«consolidados con fuentes oficiales (ONEI, Gaceta Oficial, BCC) y una serie de entrevistas y encuestas» (L12) y «| Oficiales | ONEI, Gaceta Oficial 65/2026, BCC, elTOQUE | 12 anuarios + normas |» (L71)— no figuran en el anexo. El bloque institucional [39]–[41] (DfT/DVLA, ANFAC, AEADE) es del mismo género documental, pero son instituciones distintas de las que el corpus invoca. Es una diferencia de alcance entre dos artefactos (informe técnico frente a documentación de usuario), no una entrada falsa ni una contradicción de metadatos.

— polarity: neutral · confidence: high · related: corpus L12, L71, L105–L108, L131, L833; `Data/referencias.md` L3, L8–L87

### F-V8-002 — Fuentes citadas por nombre o número sin identificador resoluble

Las atribuciones de carga del corpus no llevan DOI, arXiv, URL de destino ni fecha de consulta verificable. Casos literales: «El marco normativo es el **Decreto 163/2026** y las resoluciones 104, 17, 52, 171–175, 340 (que derogó la 312) y 102/2026» (L112); «El **Decreto 163/2026** abrió el mercado a 17 empresas autorizadas. Las resoluciones 171–175 y 340 —que derogó la 312— fijan valores referenciales, impuestos especiales y reglas aduaneras» (L245); «con la nota del **Ministerio de Finanzas y Precios del 12 de mayo** y la **Circular Especial 03/2026 de CIMEX**» (L179); «según reportes de prensa ha dejado circuitos con más de **60 horas sin electricidad**» (L181). La convención tampoco es uniforme: acrónimos sin enlace (`ONEI`, `BCC`, L12), repositorio entre backticks (`Egyptian-Used-Cars`, L277), corporación con nombre completo (CIMEX S.A., L177), app nombrada sin URL (**Circuitos Habana**, L248) y una referencia colectiva genérica («reportes de prensa», L181).

La consecuencia bibliográfica es operativa, no de existencia: las normas se citan por número y pueden localizarse en la Gaceta, pero desde el documento no hay forma de pasar del número a la norma. La única excepción es FlareSolverr (L833), con URL, aunque sea `localhost` y corresponda a una herramienta, no a una fuente de datos.

— polarity: negative · confidence: high · related: corpus L112, L177–L181, L245, L248, L277, L833; F-V8-004, F-V8-008

### F-V8-003 — Bloque institucional [39]–[41]: las tres URLs resolvieron en esta pasada

Fetch en vivo: `https://www.gov.uk/government/organisations/department-for-transport` → respuesta correcta, con apartado «Research and statistics», noticias fechadas en noviembre de 2026 y licencia «Open Government Licence v3.0», coherente con la entrada «[39] Department for Transport / DVLA. Vehicle statistics. GOV.UK. https://www.gov.uk/government/organisations/department-for-transport. **(metadata incomplete: URL profunda no confirmada)**. Citada en el informe: sí (§70 y §71.14).» (`Data/referencias.md` L83). `https://anfac.com/` → respuesta correcta, con «Cifras clave → Matriculaciones Turismos y Todoterreno» y cuadro de octubre de 2026, coherente con «[40] ANFAC. Informes del sector automotriz español. https://anfac.com/. Citada en el informe: sí (fuente institucional en §70).» (L85). `https://www.aeade.net/` → respuesta correcta, «AEADE – Asociación de Empresas Automotrices del Ecuador», con «Estadísticas → Anuarios» y «Boletines de prensa: venta de vehículos», coherente con «[41] AEADE. Estadísticas de matriculaciones. https://www.aeade.net/. Citada en el informe: sí (fuente institucional en §70).» (L87).

Este resultado revierte los timeouts registrados para [39] y [40] en `reviews/informe-tecnico-2026-11-28-iter4.v8-bibliography.md` (F-V8-003, L35): en la fecha de esta pasada las tres sedes responden. No cambia el flag `(metadata incomplete)` de [39], que se refiere a la URL profunda `gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files` citada en §18 del informe, no a la raíz institucional aquí verificada.

— polarity: positive · confidence: high · related: `Data/referencias.md` L83, L85, L87; informe-tecnico-2026-11-28-iter4.v8-bibliography.md F-V8-003

### F-V8-004 — Fuentes oficiales cubanas: existen y son accesibles, con matices de dominio y esquema

Verificación en vivo de las tres sedes que el corpus nombra sin enlace (L12, L71):

- ONEI: `https://www.onei.gob.cu/` → error de transporte; `http://www.onei.gob.cu/` → respuesta correcta. El sitio expone la serie «Transporte y Seguridad Vial», el catálogo «Anuarios → Anuario Estadístico → Cuba» con portada de «Anuario Estadístico de Cuba 2025», y el índice de publicaciones. El esquema `http` y no `https` es el que responde desde este entorno.
- Gaceta Oficial: `https://gacetaoficial.gob.cu/` → error de transporte; `http://www.gacetaoficial.gob.cu/` → respuesta correcta, con «ÚLTIMA GACETA OFICIAL» No. 98 extraordinaria del 27/11/2026 y buscador de normas. El índice del sitio registra «Decreto 163 de 2026 de Consejo de Ministros. Identificador de norma: GOC-2026-426-O65» bajo la voz «vehículos de motor», lo que acredita la norma que el corpus invoca en L112, L197 y L245 y la pertenencia a la Gaceta 65/2026 de L71.
- BCC: `https://www.bcc.gob.cu/` → error de transporte; la sede que responde es `https://www.bc.gob.cu/`, que se autodenuncia «Sitio oficial del Banco Central de Cuba» y muestra «Tasa de cambio oficial Vigente el sábado, 28 de noviembre» (USD 879,00 CUP). El corpus escribe solo «BCC» (L12, L71), sin URL, de modo que no hay un enlace roto en el documento; la sigla y el dominio real no coinciden.

El resultado es positivo para la atribución institucional: ONEI, Gaceta Oficial y BCC son fuentes reales, identificables y accesibles desde este entorno bajo las formas indicadas. Ninguna de las tres está en las 41 entradas del anexo.

— polarity: positive · confidence: high · related: corpus L12, L71, L112, L197, L245; F-V8-001

### F-V8-005 — elTOQUE: cifra fechada sin enlace ni instantánea verificable

El corpus fija la TRMI con dos redacciones: «La conversión usa la **TRMI informal de elTOQUE (18/11/2026): 930 CUP/USD, 1.000 CUP/EUR y 845,35 CUP/MLC**» (L73) y «la referencia real es la **TRMI informal: 930 CUP por USD** (elTOQUE, noviembre 2026)» (L242). El propio documento registra la limitación: «elTOQUE no responde de forma estable desde este entorno (se usa su última TRMI publicada)» (L114).

Fetch en esta pasada: `https://eltoque.com/`, `https://tasa.eltoque.com/` y `https://eltoque.com/tasas-de-cambio-cuba/mercado-informal` → error de transporte en las tres. El índice de búsqueda sí devuelve páginas vivas del sitio (`eltoque.com/tasas-de-cambio-cuba/dolar`, `/euro`, `/mlc`) con valores del 28/11/2026: «1 USD … 980.00 CUP», «1 EUR … 1045.00 CUP», «1 MLC equivale a 810.43 CUP hoy». El valor de 930 CUP/USD del corpus queda así como una instantánea de fecha declarada, no como dato contradicho: la serie es móvil y la cifra de hoy es distinta. Lo que no puede resolverse desde el corpus es la instantánea concreta del 18/11/2026, porque no se registra URL de la página ni del valor publicado ese día.

— polarity: negative · confidence: medium · related: corpus L73, L114, L242

### F-V8-006 — Spot-check de tres atribuciones de carga: ONEI, `Egyptian-Used-Cars` y Acuerdo 9811

ONEI (L145): «en 2025 se transportaron **781 millones de pasajeros**, un 59 % menos que en 2019. En ómnibus fueron 324 millones, un 71 % menos». El Cuadro 3 (L341–L352) da 781,1 frente a 1.899,9 en 2019 (781,1/1.899,9 = 0,411 → −58,9 %, redondeado 59 %) y 324,0 frente a 1.102,2 (0,294 → −70,6 %, redondeado 71 %). La atribución y el cálculo coinciden, y el sitio de ONEI expone la serie «Transporte y Seguridad Vial» verificada en F-V8-004. El Cuadro 4 (L354–L362) es de la misma fuente y categoría.

`Egyptian-Used-Cars` (L277): «uno de los análisis de mercado automotriz más completos que tenemos: 23.500 anuncios, historial mensual de precios, econometría, SQL, Tableau y Power BI». El repositorio existe en disco (`Auxiliares/Repositorios Referencias/Egyptian-Used-Cars/`); su `README.md` L1–L9 declara «Python**, **SQL**, **Tableau**, and **Power BI**» y «historical price fluctuations, depreciation dynamics», y las L39–L60 detallan OLS log-lineal, VIF, Kruskal-Wallis, CTEs y `LAG/LEAD/RANK`. `data/cleaned/used_cars_cleaned.csv` tiene 23.535 líneas (23.534 registros), compatibles con el redondeo «23.500 anuncios». Es una fuente local atribuible, ausente del anexo de 41 entradas.

Acuerdo 9811/2024 (L177): «el **Acuerdo 9811 de 2024 del Consejo de Ministros**, que fijaba los precios minoristas de los combustibles en CUP y USD». La cobertura oficial indexada (Granma, Cubadebate, `mincin.gob.cu`) lo data el 24/01/2024, publicado en Gaceta Extraordinaria 10, con entrada en vigor el 01/03/2024. La identidad y el objeto de la norma coinciden con el corpus; el corpus no aporta enlace a esa Gaceta.

— polarity: positive · confidence: high · related: corpus L145, L177, L277, L341–L362; `Auxiliares/Repositorios Referencias/Egyptian-Used-Cars/README.md` L1–L9, L39–L60

### F-V8-007 — Tres identificadores de aspecto sospechoso resuelven y coinciden con el anexo

Verificación puntual de los casos que el evaluador marca como prioritarios:

- `[24]` (L54): «arXiv:2601.14311 (manuscrito enviado a ACM Computing Surveys) (2026)». `https://arxiv.org/abs/2601.14311` → página activa, «Submitted on 19 Jan 2026», título «Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability in LLMs» y los seis autores (Hohensinner, Mutlu, Mendoza Estrada, Vukovic, Kopeinik, Kern) coincidentes; «Comments: 35 pages, 6 figures. Manuscript submitted to ACM Computing Surveys (CSUR) on the 12th of December 2025». El prefijo `2601` es anterior a la fecha del corpus (23/11/2026): no hay ID imposible.
- `[27]` (L60): «https://doi.org/10.54660/.jfmr.2023.4.1.529-538». El punto inicial del sufijo (`/.jfmr`) se había registrado como «no verificado en vivo» en la V8 anterior (F-V8-009, L71). El DOI resuelve a Essien, Adebayo, Afuwape, Eboseremen, Oladega y Soneye (2023), *Journal of Frontiers in Multidisciplinary Research* 4(1), 529–538: es un DOI registrado, no uno malformado.
- `[9]` (L24): «https://doi.org/10.54254/2754-1169/2026.38524». Resuelve a Du, Yang, Zhang, Li y Liu (2026), *Advances in Economics, Management and Political Sciences* 313(1), 134–143, con el título y los autores del anexo.

Comprobación estructural del anexo: 41 líneas `^[n]` de [1] a [41], sin huecos ni números repetidos; sin entradas sin autor, sin títulos genéricos de paper fantasma y sin duplicados detectables por título+DOI. Cuatro entradas siguen marcadas `(metadata incomplete)` ([1], [10], [12], [39]), que es la base del `unverified: 4` del frontmatter.

— polarity: positive · confidence: high · related: `Data/referencias.md` L24, L54, L60, L8–L87; informe-tecnico-2026-11-28-iter4.v8-bibliography.md F-V8-009

### F-V8-008 — Normas 171–175/340/102 y Gaceta 65/2026: verificables por búsqueda, no por enlace estable

Además de la ausencia de URL señalada en F-V8-002, el acceso a las normas citadas depende del buscador del sitio y de variantes de archivo. `https://www.gacetaoficial.gob.cu/sites/default/files/goc-2026-o65.pdf` → **404**; la variante indexada `https://www.gacetaoficial.gob.cu/sites/default/files/goc-2026-o65_0.pdf` → el servidor devuelve un `application/pdf` (el fetch solo se rechaza por el tipo de contenido, no por estado HTTP). El número de Gaceta 65/2026 de L71 es, por tanto, correcto, pero la dirección profunda «obvia» del PDF no es la que sirve el archivo.

La Circular Especial 03/2026 de L179 se localiza en cobertura de prensa fechada el 15/05/2026 —«oficializada mediante la Circular Especial 03/2026, firmada por el presidente de Cimex, Héctor Oroza Busutil», con entrada en vigor a las 12:00 del 15/05/2026— y el Acuerdo 9811 en cobertura oficial (F-V8-006), pero ni una ni otra tienen enlace en el corpus. Las resoluciones 104, 17, 52, 171–175, 340 (derogadora de la 312) y 102/2026 de L112 aparecen solo como números: no se registró para ellas una dirección de resolución en el documento ni una entrada en `Data/referencias.md`. La atribución es nominativa, no resoluble desde el texto auditado.

— polarity: negative · confidence: medium · related: corpus L71, L112, L179, L245; F-V8-002, F-V8-004

## Resumen (3 líneas)

1. El corpus no tiene bibliografía: 0 marcadores `[N]`, 0 DOI/arXiv y 0 menciones de `Data/referencias.md`; las 41 entradas y las fuentes del corpus forman dos conjuntos disjuntos, con el matiz de que [39]–[41] son institucionales pero de otros países.
2. Las fuentes oficiales nombradas sí existen: ONEI y Gaceta Oficial responden por `http`, BCC por `bc.gob.cu` (no `bcc.gob.cu`), el Decreto 163/2026 está registrado como GOC-2026-426-O65 en la Gaceta 65/2026, y [39]–[41] resolvieron las tres en esta pasada; elTOQUE no fue alcanzable desde aquí y su cifra de 930 CUP/USD carece de instantánea enlazable.
3. Los spot-checks salen bien (ONEI −59 %/−71 %, 23.534 filas en `Egyptian-Used-Cars`, Acuerdo 9811 de 24/01/2024) y los tres identificadores sospechosos —arXiv:2601.14311, DOI `10.54660/.jfmr…` y DOI de [9]— resuelven y coinciden; queda sin resolución directa el bloque de resoluciones numeradas y la URL profunda inestable del PDF de la Gaceta 65/2026.


## §9 — v9-ethics


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



## §10 — Observaciones transversales

### A. Divergencias numéricas (14)

1. Marketplaces 2.232 (README L12, storytelling L211) frente a 2.222 (README L67). Los ocho SQLite suman 2.232.
2. Revolico 10.379/974 (README L19) frente a 10.217/812 (ARQUITECTURA L502) a igual fecha; `MANIFEST.json` respalda 10.379/974.
3. Derivados de la copia compacta: imágenes 23.143 vs 23.697, revisiones 11.620 vs 14.487, teléfonos 12.338 vs 12.538.
4. Muestra del modelo: 28/993 y 586/993 en CSV, frente a 22/572 y 584/981 en Cuadro 5 y MODELOS.
5. Coeficientes del Cuadro 5 «vigentes» frente a `modelo_depreciacion.csv`; p mínimo 0,165 vs 0,0941.
6. R² 0,101/0,274 coherentes en CSV, con un 0,277 corregido en el informe.
7. VIF 1,13–1,58 en MODELOS vs 1,12–1,40 en `vif.csv`.
8. Kruskal-Wallis: H=25.741 (MODELOS), 32,818 (`tests.csv`) y 44.313 (`comparaciones.csv`).
9. «104 observaciones bastan para depreciación» (AUTOMATIZACION) frente a la serie mensual presentada como pendiente.
10. Corrida de calidad 2.014 (AUTOMATIZACION) frente al KPI vigente 2.174.
11. Ancho de banda: totales no derivados de las tres filas de su tabla.
12. Cifras sin contrapartida: 3.958 anuncios ICD, 256/25/22 talleres y concesionarios, encuesta, 11+21 estaciones, 205.002 KB, 233/234 archivos ONEI.
13. Estados incompatibles: ledger LFS operativo vs pendiente, push vs «ningún job hace push», Revolico semanal vs cada 10 min, DuckDB recomendado vs bloqueado.
14. README «Actualizado 23/11/2026» frente al HEAD del 28/11/2026.

### B. Enlaces, rutas y documentos huérfanos (9)

1. El índice de README alcanza solo 2 de 7 documentos; faltan ARQUITECTURA, ALCANCE, AUTOMATIZACION, ESTRUCTURA_ESPACIO y mapas/README.
2. README cita el informe «secciones 1–60» cuando llega a 71.15.
3. `Data/mapas/README.md` prescribe `.venv/bin/python`, inexistente; solo existe `.venv-py`.
4. `patchright`, `playwright` y FlareSolverr sin documentar en dependencias.
5. Siete artefactos anunciados como listos y ausentes: `benchmark_result.csv`, `manifiesto_ejecucion.jsonl`, `VERSIONES.json`, `watermarks.json`, ledger LFS, snapshots y `DICCIONARIO`/`LIMITACIONES`.
6. Rutas sin prefijo: `job_*.sh` y `sitio_build.sh` en `Data/_state/`; `alertas.jsonl` en `Data/_estado/` (sí existen).
7. Tres gráficos del apéndice sin llamada en prosa; §6 remite a un cuadro de seguridad vial.
8. La semilla declarada en el informe no aparece en los ocho archivos del corpus.
9. `Data/referencias.md` no se enlaza desde ninguno de los ocho bloques.

### C. Bibliografía (8)

1. Intersección vacía: cero `[N]`, DOI o mención del anexo en el corpus; las 41 entradas y las fuentes del corpus son conjuntos disjuntos.
2. Cuatro métodos (hedónico, VIF, Kruskal, Welch) sin atribución, con respaldo disponible en [12], [13], [9].
3. Cinco ausencias probables con solapamiento: [29], [30], [21], [22], [12].
4. `Egyptian-Used-Cars` citado por nombre, sin marcador, aunque existe en disco con 23.534 filas.
5. Fuentes oficiales (ONEI, Gaceta, BCC, resoluciones, Circular 03/2026, Acuerdo 9811) sin URL de resolución; Gaceta 65/2026=GOC-2026-426-O65, PDF `_0.pdf`.
6. TRMI 930 sin instantánea enlazable; índice devuelve 980 al 28/11 (serie móvil).
7. [39]–[41] resolvieron en vivo; [39] conserva flag por URL profunda.
8. Cobertura 0/41 frente al tramo 25–60; 7/32 fuentes con año (21,9 %) frente al 40 %.

### D. Ética y privacidad (5)

1. README «no recopila datos personales» frente a 12.338 teléfonos en la copia compacta y campo teléfono en `mapa_elementos.sqlite`.
2. Encuesta de 33 personas y entrevistas (una con nombres) sin consentimiento ni anonimización declarados en el corpus.
3. «No elude mecanismos anti-automatización» frente a curl_cffi, patchright y FlareSolverr.
4. Declaración de IA ausente en los ocho bloques, presente en §69 del informe.
5. Sin URL del repositorio en el corpus, licencia pendiente y sin commit/DOI que fije la versión de las cifras.

### E. Escritura (7)

1. «Cuatro preguntas» con tres subtítulos.
2. CTA en presente para algo que ALCANCE sitúa como pendiente.
3. Corrección diagnósticada del H2 «El punto de partida» no aplicada.
4. Diez triadas, doce adjetivos sin ancla y unas veinte negaciones contrastivas, concentradas en storytelling §§1–2 y ALCANCE.
5. Metadiscurso y proyecciones 58/40/25/16/10/5 bajo salvedad de inferencia.
6. Siglas sin desplegar: TRMI, KPIs, OLS, UTM, E-E-A-T, CDN, long-form.
7. Convención de apoyos rota: nota editorial en §3 y títulos de cuadro autocontenidos.

— polarity: negative · confidence: high

## Apéndice A — Plan

# Plan de auditoría — Corpus de documentación

Corpus unificado de 8 archivos de cara al usuario: README, storytelling,
inventario de modelos, arquitectura de datos, alcance y retención,
automatización, estructura de espacio y mapas. Se audita con la skill
`review` en nivel `master` para detectar inconsistencias entre documentos
y frentes a los CSV y al informe técnico.

Se re-ejecutan E1–E3 y V1–V9 y se comparan las cifras del corpus con
`Data/analisis_rentabilidad/outputs/tables/`.


## Apéndice B — Claims

# Claim Inventory

## Summary
- Total: 118
- Load-bearing: 13 · Supporting: 58 · Contextual: 47
- By type: result 45 · methodological 39 · novelty 5 · contextual 54 · definitional 7 · citation-grounded 13

Nota: los números de línea se refieren al archivo unificado indicado en `audited_document`; el encabezado `# ARCHIVO:` de cada bloque identifica el archivo de origen. Las citas de contraste (`outputs/tables/*.csv`, `INFORME_TECNICO.md`) se verificaron en disco y se imprimen con su línea exacta.

## Load-bearing claims

### C001 — Cifras de portada del README: 974 autos, 2.232 anuncios y 256 vehículos
- **Section**: `README.md` §encabezado
- **Lines**: 12
- **Types**: result, contextual
- **Excerpt**: «Análisis reproducible del mercado automotor cubano: **<!-- kpi:autos_revolico -->974 autos únicos** de Revolico, **<!-- kpi:anuncios_marketplaces -->2.232 anuncios** de 8 marketplaces y **256 vehículos** de 11 concesionarios»
- **Restated**: El corpus afirma que el mercado cubierto consta de 974 autos únicos de Revolico, 2.232 anuncios de marketplaces y 256 vehículos de concesionarios.
- **Internal evidence cited**: §Fuentes de datos (L.65–71); storytelling §3 (L.211)
- **External evidence cited**: —
- **Novelty signals**: —
- **Notes**: La tabla interna del mismo README da 2.222 anuncios (L.67) y el storytelling repite 2.232 (L.211); `INFORME_TECNICO.md:1381` confirma 10 anuncios nuevos en iTENCEL, posible origen de la diferencia, pero el corpus no reconcilia ambas cifras.

### C002 — Resultado esperado del pipeline: 2.174 anuncios limpios y mediana 21.000 USD
- **Section**: `README.md` §Quickstart
- **Lines**: 42
- **Types**: result
- **Excerpt**: «**Resultado esperado:** <!-- kpi:anuncios_totales -->2.174 anuncios limpios (<!-- kpi:anuncios_locales -->1.483 locales + <!-- kpi:anuncios_importacion -->691 de importación), mediana local <!-- kpi:precio_mediano_usd -->21.000 USD.»
- **Restated**: La corrida vigente produce 2.174 anuncios limpios, 1.483 locales y 691 de importación, con mediana local de 21.000 USD.
- **Internal evidence cited**: Cuadro 1 (L.317–331); Cuadro 2 (L.333–339)
- **External evidence cited**: —
- **Novelty signals**: —
- **Notes**: Coincide exactamente con `outputs/tables/kpis.csv:2-4,9` y `kpis_canal.csv:2-4`; el calificativo «esperado» convive con marcadores `kpi:` que se actualizan solos (L.663).

### C003 — Titular del storytelling: autos, anuncios «y una serie oficial detrás»
- **Section**: `PRESENTACION_STORYTELLING.md` §encabezado
- **Lines**: 123
- **Types**: result, methodological
- **Excerpt**: «Cuánto cuesta un carro en Cuba: <!-- kpi:autos_revolico -->974 autos, <!-- kpi:anuncios_totales -->2.174 anuncios y una serie oficial detrás»
- **Restated**: El relato sostiene que dispone de una serie temporal oficial además del corte transversal de precios.
- **Internal evidence cited**: README §Fuentes de datos (L.21); storytelling §8 (L.290); MODELOS §4 (L.485)
- **External evidence cited**: —
- **Novelty signals**: «serie oficial detrás» (L.123)
- **Notes**: La «serie» disponible es la anual del ONEI (12 anuarios, L.21), no una serie de precios: el propio relato la propone como trabajo futuro (L.290) y el inventario de modelos niega la curva temporal (L.485).

### C004 — Retrato estadístico del usado local
- **Section**: `PRESENTACION_STORYTELLING.md` §2 «¿Qué devuelve la inversión?»
- **Lines**: 195
- **Types**: result
- **Excerpt**: «Nuestra base reúne **<!-- kpi:autos_revolico -->974 autos únicos de Revolico** dentro de **<!-- kpi:anuncios_totales -->2.174 anuncios limpios**: <!-- kpi:anuncios_locales -->1.483 del mercado local y <!-- kpi:anuncios_importacion -->691 de importación. El precio mediano del usado local es de **<!-- kpi:precio_mediano_usd -->21.000 USD**, con una media de **<!-- kpi:precio_medio_usd -->28.201,06 USD**; la antigüedad promedio es de **<!-- kpi:antiguedad_media -->8,1 años** y el kilometraje mediano, de **<!-- kpi:km_medianos -->32.569 km**.»
- **Restated**: El usado local tiene mediana 21.000 USD, media 28.201,06 USD, antigüedad media 8,1 años y kilometraje mediano 32.569 km sobre 1.483 anuncios locales.
- **Internal evidence cited**: Cuadro 1 (L.317–331)
- **External evidence cited**: —
- **Novelty signals**: —
- **Notes**: Los ocho valores coinciden con `kpis.csv:2-12`; el desajuste media/mediana se usa en MODELOS L.423 como evidencia de cola derecha.

### C005 — Cobertura de marcas, grupos comparables, infravalorados y anomalías
- **Section**: `PRESENTACION_STORYTELLING.md` §2
- **Lines**: 197
- **Types**: result
- **Excerpt**: «Con **<!-- kpi:marcas_distintas -->50 marcas** y **<!-- kpi:grupos_benchmark -->114 grupos** de marca, modelo y año comparables, detectamos **<!-- kpi:infravalorados -->30 oportunidades infravaloradas** y **<!-- kpi:anomalias -->89 anomalías** entre precio y kilometraje.»
- **Restated**: El análisis cubre 50 marcas y 114 grupos comparables, y detecta 30 oportunidades infravaloradas y 89 anomalías precio-kilometraje.
- **Internal evidence cited**: §3 (L.215); Cuadro 1 (L.326)
- **External evidence cited**: —
- **Novelty signals**: «detectamos» (L.197)
- **Notes**: Verificado: `benchmark.csv` 114 filas de datos, `infravalorados.csv` 30, `anomalias.csv` 89, `kpis.csv:7` 50.

### C006 — No hay pendiente anual significativa tras corregir kilometraje
- **Section**: `PRESENTACION_STORYTELLING.md` §2 y §4
- **Lines**: 197, 229, 231
- **Types**: result, methodological
- **Excerpt**: «La depreciación ya no se presenta como una cifra única: al corregir el kilometraje, el modelo actual no encuentra una pendiente anual estadísticamente significativa. La edad ya no explica el precio por sí sola; importa de dónde viene el auto, en qué moneda se paga y en qué estado llega.»
- **Restated**: El modelo vigente no produce una tasa de depreciación anual estadísticamente significativa y la prima premium dejó de poder cuantificarse.
- **Internal evidence cited**: Cuadro 5 (L.364–377); MODELOS §3.1 (L.450–452); §4 (L.482–486)
- **External evidence cited**: —
- **Novelty signals**: «ya no se presenta como una cifra única» (L.197)
- **Notes**: Coherente con `INFORME_TECNICO.md:1401,1537`; contradice internamente el Cuadro 5, cuyos coeficientes/p_valores están desactualizados (ver C039–C040).

### C007 — Modelo completo: 28 observaciones y ningún coeficiente significativo
- **Section**: `MODELOS_Y_FUNCIONES.md` §3.1
- **Lines**: 450
- **Types**: result, methodological
- **Excerpt**: «con **<!-- kpi:modelo_n_completo -->28 observaciones completas** de <!-- kpi:modelo_candidatas -->993 candidatas ningún coeficiente alcanza significancia (el p_valor más bajo es 0,165, de potencia; antigüedad tiene p = 0,237). La muestra se reduce a 22 porque `hp` solo está presente en 52 filas y `mileage_km` en 572; al exigir todos los términos a la vez se descarta el 97,5 % de las candidatas (R² = <!-- kpi:modelo_r2_completo -->0,274; p del F = <!-- kpi:modelo_pf_completo -->0,411).»
- **Restated**: El modelo hedónico completo usa 28 observaciones de 993 candidatas, no alcanza significancia en ningún coeficiente y tiene R² 0,274 con p del F 0,411.
- **Internal evidence cited**: Cuadro 5 (L.364–377); storytelling §4 (L.231)
- **External evidence cited**: —
- **Novelty signals**: —
- **Notes**: n, candidatas, R² y p_F coinciden con `modelo_muestra.csv:3` (28/993/0,2744/0,4114); los p_valores no: `modelo_depreciacion.csv:2-9` da potencia 0,1403 y antigüedad 0,1504, e intercepto 12,0884 frente a 12,4469 del Cuadro 5. El «se reduce a 22» contradice la propia cifra 28 y el CSV.

### C008 — Modelo principal: 586 observaciones y pendiente de antigüedad como artefacto de selección
- **Section**: `MODELOS_Y_FUNCIONES.md` §3.1
- **Lines**: 452
- **Types**: result, methodological
- **Excerpt**: «el modelo principal (sin `hp`) usa <!-- kpi:modelo_n_principal -->586 observaciones de <!-- kpi:modelo_candidatas -->993 candidatas (R² = <!-- kpi:modelo_r2_principal -->0,101; p del F <!-- kpi:modelo_pf_principal -->0,000) y el completo usa <!-- kpi:modelo_n_completo -->28 (R² = <!-- kpi:modelo_r2_completo -->0,274; p del F = <!-- kpi:modelo_pf_completo -->0,411). En el modelo principal el coeficiente de antigüedad es positivo y alcanza p < 0,05, pero esa asociación corresponde a la submuestra que declaró kilometraje y no debe leerse como depreciación: es un artefacto de selección, no una tasa anual.»
- **Restated**: El modelo sin `hp` usa 586 observaciones de 993 candidatas y su coeficiente de antigüedad positivo es un artefacto de selección, no una tasa de depreciación.
- **Internal evidence cited**: §3.1 (L.450); storytelling §4 (L.231)
- **External evidence cited**: —
- **Novelty signals**: —
- **Notes**: Coincide con `modelo_muestra.csv:2` (993/586/0,1008/0,0); `INFORME_TECNICO.md:1522` registra la versión anterior 584 de 981 y el Cuadro 5 (L.377) afirma 572 para el modelo principal. Tres cifras distintas para el mismo modelo.

### C009 — El diagnóstico de retención es inferencia, no medición
- **Section**: `ALCANCE_Y_RETENCION.md` §1 y §2
- **Lines**: 575, 591–604
- **Types**: methodological
- **Excerpt**: «Revisión del relato como **puerta de entrada**: ¿logra que un visitante nuevo se interese y vuelva? Es un análisis de diseño, no una medición: el proyecto no tiene analytics.» y «## 2. Estimación de retención (inferencia, no medición)»
- **Restated**: El corpus declara explícitamente que no dispone de analytics y que las cifras de retención son inferencias de diseño.
- **Internal evidence cited**: §2 tabla (L.595–604)
- **External evidence cited**: —
- **Novelty signals**: —
- **Notes**: Esta declaración acota la fuerza de C010 y de las proyecciones C056; sostiene la narrativa de honestidad metodológica del corpus.

### C010 — 104 observaciones semanales «bastan para depreciación»
- **Section**: `AUTOMATIZACION.md` §2 «Periodicidad realista»
- **Lines**: 645
- **Types**: result, methodological
- **Excerpt**: «Snapshots de precio (`price_history`) | Semanal, tras Revolico | 104 observaciones en 2 años bastan para depreciación»
- **Restated**: El corpus afirma que 104 observaciones semanales en dos años son suficientes para estimar depreciación.
- **Internal evidence cited**: storytelling §8 (L.290); MODELOS §4 (L.485); §6b (L.690–691)
- **External evidence cited**: —
- **Novelty signals**: «bastan para depreciación» (L.645)
- **Notes**: Contradicción directa con `MODELOS_Y_FUNCIONES.md:485` («No se presenta una curva de depreciación temporal: hace falta una serie mensual de 6–12 meses») y con `PRESENTACION_STORYTELLING.md:290`. Aun 104 observaciones semanales no equivalen a la serie mensual exigida; es la afirmación numérica más conflictiva del corpus frente al informe técnico.

### C011 — Compactación Parquet: 849 MB → 27,5 MB sobre 10.217 anuncios y 812 autos
- **Section**: `ARQUITECTURA_DATOS.md` §0
- **Lines**: 499–508
- **Types**: result, methodological
- **Excerpt**: «Medición real: **849 MB → 27,5 MB** (10.217 anuncios, 812 autos, 23.143 imágenes, 11.620 revisiones, 12.338 teléfonos y 716 precios), con las mismas filas, columnas y valores; `MANIFEST.json` guarda recuentos y SHA-256 por archivo.»
- **Restated**: La copia compacta de `revolico.sqlite` reduce 849 MB a 27,5 MB conservando 10.217 anuncios y 812 autos.
- **Internal evidence cited**: README §Fuentes de datos (L.19)
- **External evidence cited**: —
- **Novelty signals**: «ya implementado» (L.497)
- **Notes**: El README (L.19) atribuye a la misma base 10.379 anuncios y 974 autos, cifras incompatibles con las de este documento a igual fecha (23/11/2026). `INFORME_TECNICO.md:1345` registra 849.465.344 bytes, coherente con los 849 MB, pero no resuelve el recuento de autos.

### C012 — Convención monetaria: TRMI informal, nunca tasa oficial
- **Section**: `README.md` §Fuentes de datos; `MODELOS_Y_FUNCIONES.md` §1
- **Lines**: 73, 409, 482
- **Types**: definitional, methodological
- **Excerpt**: «La conversión usa la **TRMI informal de elTOQUE (18/11/2026): 930 CUP/USD, 1.000 CUP/EUR y 845,35 CUP/MLC**. Nunca se usa la tasa oficial para los precios del mercado.» y «`precio × FX[moneda]` con TRMI informal: USD 1, CUP 1/930, EUR 1000/930, MLC 845,35/930.»
- **Restated**: Todas las conversiones a USD usan la TRMI informal fechada el 18/11/2026 y excluyen la tasa oficial.
- **Internal evidence cited**: storytelling §5 (L.242); ALCANCE §3 (L.609)
- **External evidence cited**: —
- **Novelty signals**: —
- **Notes**: Definición operativa de la que dependen todos los precios en USD del corpus; consistente entre los tres archivos que la menciona.

### C013 — «El diseño está listo para crecer igual que crezcan los datos»
- **Section**: `PRESENTACION_STORYTELLING.md` §7; `ARQUITECTURA_DATOS.md` §6
- **Lines**: 283, 512–566
- **Types**: methodological, novelty
- **Excerpt**: «**El diseño está listo para crecer igual que crezcan los datos.**»
- **Restated**: La arquitectura de datos está lista para escalar con el crecimiento de los datos.
- **Internal evidence cited**: ARQUITECTURA §2–§4 (L.516–554); §6 (L.562–566)
- **External evidence cited**: —
- **Novelty signals**: «listo para crecer» (L.283)
- **Notes**: El propio documento de arquitectura la califica como «Fase 0–1 de diseño» (L.566) y registra `import duckdb` fallando con `SIGILL`, con el motor recomendado (L.520) pendiente de reevaluación; la afirmación de disponibilidad es más fuerte que el estado implementado.

## Supporting claims (58)

### C014 — Recuentos de la base principal y de referencias
- **Section**: `README.md` §Qué incluye
- **Lines**: 19
- **Types**: result
- **Excerpt**: «`Data/Revolico/revolico.sqlite` (<!-- kpi:anuncios_revolico -->10.379 anuncios, <!-- kpi:autos_revolico -->974 autos) y `Data/repos-autos-referencias/referencias_autos.sqlite` (25 tablas).»
- **Restated**: `revolico.sqlite` contiene 10.379 anuncios y 974 autos, y la base de referencias tiene 25 tablas.
- **Notes**: En conflicto con `ARQUITECTURA_DATOS.md:502` (10.217 anuncios, 812 autos) para la misma base y fecha; el 974 sí es estable en todo el corpus.

### C015 — Anuarios del ONEI
- **Section**: `README.md` §Qué incluye
- **Lines**: 21
- **Types**: result, citation-grounded
- **Excerpt**: «los 12 anuarios del ONEI (2014–2025), 233 archivos, en `Data/fuentes-oficiales/ONEI/`.»
- **Restated**: La colección oficial comprende 12 anuarios del ONEI entre 2014 y 2025, con 233 archivos.
- **Notes**: 2014–2025 son efectivamente 12 ejercicios; la cifra 233 no se desglosa en el corpus.

### C016 — Anuncios de marketplaces en la tabla de fuentes
- **Section**: `README.md` §Fuentes de datos
- **Lines**: 67
- **Types**: result
- **Excerpt**: «| Marketplaces | Autocubana, iTENCEL, Cogetucarro, Cubisima, Timbirichi, Carros.com, Apululu, VentaCuba | 2.222 anuncios |»
- **Restated**: Los ocho marketplaces aportan 2.222 anuncios según la tabla, frente a los 2.232 declarados en L.12 y L.211.
- **Notes**: Discrepancia interna de 10 anuncios, número que coincide con los diez anuncios nuevos de iTENCEL (L.211; `INFORME_TECNICO.md:1381`), sin que el corpus lo explicite.

### C017 — Cobertura de concesionarios
- **Section**: `README.md` §Fuentes de datos
- **Lines**: 68
- **Types**: result
- **Excerpt**: «| Concesionarios | BDC One, Dongfeng, Changan, Chinautos, MCV, Finauto, ATR Export y otros | 256 vehículos |»
- **Restated**: El catálogo de concesionarios contiene 256 vehículos.
- **Notes**: Cifra distinta de los «25 concesionarios geolocalizados» del storytelling (L.187): una cuenta vehículos, la otra puntos con coordenadas; el corpus no distingue los denominadores.

### C018 — Referencias externas ICD
- **Section**: `README.md` §Fuentes de datos
- **Lines**: 70
- **Types**: result, citation-grounded
- **Excerpt**: «| Referencias externas | Repos ICD, AutosxCuba, Mercado-automotriz y otros | 3.958 anuncios ICD |»
- **Restated**: El repositorio ICD aporta 3.958 anuncios de referencia.
- **Notes**: Cifra atribuida a repositorios externos, sin tabla de respaldo dentro del corpus.

### C019 — Manifiestos de fragmentos
- **Section**: `README.md` §Configuración
- **Lines**: 81–82
- **Types**: result
- **Excerpt**: «`Data/Revolico/chunks/MANIFEST.json` | 82 fragmentos de 10 MB y sus SHA-256» y «`Data/Revolico/pipeline_chunks/MANIFEST.json` | 52 fragmentos de `pipeline.sqlite`»
- **Restated**: Los manifiestos registran 82 fragmentos de 10 MB de la base principal y 52 del pipeline.
- **Notes**: Los 82 fragmentos coinciden con `INFORME_TECNICO.md:1345`; los 52 no se contrastan en el corpus.

### C020 — Marco normativo declarado
- **Section**: `README.md` §Marco legal y límites
- **Lines**: 112
- **Types**: citation-grounded, definitional
- **Excerpt**: «El marco normativo es el **Decreto 163/2026** y las resoluciones 104, 17, 52, 171–175, 340 (que derogó la 312) y 102/2026.»
- **Restated**: El marco legal aplicable está compuesto por el Decreto 163/2026 y ocho resoluciones citadas, con la 340 derogando la 312.
- **Notes**: Coincide con `INFORME_TECNICO.md:67`; las resoluciones se enumeran sin número de Gaceta en este archivo (sí en el informe técnico, L.67).

### C021 — Limitaciones de cobertura declaradas
- **Section**: `README.md` §Marco legal y límites
- **Lines**: 114
- **Types**: contextual, methodological
- **Excerpt**: «elTOQUE no responde de forma estable desde este entorno (se usa su última TRMI publicada); `carrosw` está detrás de verificación de bots; parte del catálogo de BDC One y Changan solo está en PDF; la trueque de roles entre canales local e importación se mantiene separada con la columna `canal`.»
- **Restated**: Cuatro limitaciones operativas afectan la frescura de la TRMI, la cobertura de `carrosw`, la extracción de PDF y la separación de canales.
- **Notes**: «trueque de roles» parece un error léxico por «trueque/mezcla de roles»; no altera la afirmación de separación por `canal`.

### C022 — Caída del transporte de pasajeros según el ONEI
- **Section**: `PRESENTACION_STORYTELLING.md` §1
- **Lines**: 145
- **Types**: result, citation-grounded
- **Excerpt**: «El ONEI lo pone en números: en 2025 se transportaron **781 millones de pasajeros**, un 59 % menos que en 2019. En ómnibus fueron 324 millones, un 71 % menos.»
- **Restated**: En 2025 el transporte de pasajeros cayó 59 % frente a 2019 y el de ómnibus 71 %, hasta 781 y 324 millones respectivamente.
- **Notes**: Cuadro 3 (L.346, L.352) da 1.899,9 → 781,1 (−58,9 %) y 1.102,2 → 324,0 (−70,6 %); los porcentajes redondeados son correctos. La cifra de 2025 se redondea a 781 millones en el texto y a 781,1 en el cuadro.

### C023 — Acuerdo 9811 y plataforma Ticket
- **Section**: `PRESENTACION_STORYTELLING.md` §2 «¿Cuánto costaría moverse?»
- **Lines**: 177
- **Types**: citation-grounded
- **Excerpt**: «Hasta el **7 de febrero de 2026** regía, como marco de precios, el **Acuerdo 9811 de 2024 del Consejo de Ministros** [...] activaron la plataforma **Ticket**: turno previo, tope de **20 litros** y **24 horas** para consumirlo.»
- **Restated**: Hasta el 7/2/2026 rigió el Acuerdo 9811 de 2024 y desde entonces CIMEX aplicó Ticket con tope de 20 litros y 24 horas de validez.
- **Notes**: Afirmación apoyada solo en fuente externa citada narrativamente, sin entrada bibliográfica numerada en el corpus.

### C024 — Liberalización de la importación de combustible y precios por litro
- **Section**: `PRESENTACION_STORYTELLING.md` §2
- **Lines**: 179
- **Types**: citation-grounded, result
- **Excerpt**: «Desde el **15 de febrero de 2026** el Gobierno autorizó a **mipymes, cooperativas y otros actores económicos no estatales** a importar combustible directamente. A partir del **15 de mayo de 2026** [...] entre **1,80 y 2,60 USD por litro** según el tipo de combustible. En paralelo, el mercado informal mueve la B94 en **7.000–8.000 CUP por litro**.»
- **Restated**: Desde febrero de 2026 importan combustible actores no estatales y desde mayo cada importador fija entre 1,80 y 2,60 USD/litro, frente a 7.000–8.000 CUP/litro en el mercado informal.
- **Notes**: La nota del MFP es del 12 de mayo y la Circular Especial 03/2026 de CIMEX se menciona en la misma línea; ninguna aparece en la bibliografía del corpus.

### C025 — Circuitos con más de 60 horas sin electricidad
- **Section**: `PRESENTACION_STORYTELLING.md` §2
- **Lines**: 181
- **Types**: citation-grounded
- **Excerpt**: «La medida protege un sistema envejecido, pero según reportes de prensa ha dejado circuitos con más de **60 horas sin electricidad**.»
- **Restated**: Reportes de prensa citados registran circuitos de La Habana con más de 60 horas consecutivas sin electricidad.
- **Notes**: El calificador «según reportes de prensa» explicita que no hay evidencia interna; la app `Circuitos Habana` se describe en L.248.

### C026 — Talleres, concesionarios y redes de servicio
- **Section**: `PRESENTACION_STORYTELLING.md` §2 «¿Quién lo mantiene?»
- **Lines**: 187–189
- **Types**: result, contextual
- **Excerpt**: «En nuestra base quedaron geolocalizados **22 talleres** en La Habana y **25 concesionarios**, pero la cobertura no es la misma para todas las marcas.»
- **Restated**: La base geolocaliza 22 talleres en La Habana y 25 concesionarios, con cobertura desigual por marca.
- **Notes**: La Tabla de fuentes del README (L.51) anota «11 concesionarios + 8 marketplaces» y el README L.68 habla de 256 vehículos; tres recuentos de distinta naturaleza no reconciliados.

### C027 — Proporción entre autos y anuncios de marketplaces
- **Section**: `PRESENTACION_STORYTELLING.md` §3
- **Lines**: 211
- **Types**: result
- **Excerpt**: «En nuestro caso quedaron **<!-- kpi:autos_revolico -->974 autos** con datos suficientes frente a **<!-- kpi:anuncios_marketplaces -->2.232 anuncios** en los marketplaces especializados; en la última revisión aparecieron diez anuncios nuevos en iTENCEL.»
- **Restated**: Frente a 2.232 anuncios de marketplaces, solo 974 autos tienen datos suficientes; la última revisión añadió diez anuncios de iTENCEL.
- **Notes**: `INFORME_TECNICO.md:1381` confirma los diez anuncios nuevos; la cifra 2.232 vuelve a chocar con el 2.222 de `README.md:67`.

### C028 — Mediana del canal importado
- **Section**: `PRESENTACION_STORYTELLING.md` §3
- **Lines**: 213
- **Types**: result
- **Excerpt**: «El canal importado —<!-- kpi:anuncios_importacion -->691 anuncios— corre en paralelo, con una mediana de <!-- kpi:mediana_importacion -->26.000 USD.»
- **Restated**: Los 691 anuncios de importación tienen mediana de 26.000 USD.
- **Notes**: Coincide con `kpis_canal.csv:2` (691 / 26.000 / 27.046,22); Cuadro 2 (L.337) replica los tres valores.

### C029 — Definición operativa de «premium»
- **Section**: `PRESENTACION_STORYTELLING.md` §4
- **Lines**: 227
- **Types**: definitional, contextual
- **Excerpt**: «En este relato llamamos premium a **Mercedes-Benz, BMW, Audi, Lexus, Volvo, Porsche, Land Rover, Jaguar, Cadillac, Infiniti y Acura**; son marcas de gama alta, con precio y posventa por encima del segmento masivo. El resto [...] pertenece al grupo **no premium**»
- **Restated**: El relato define «premium» como una lista cerrada de 11 marcas y «no premium» como el resto.
- **Notes**: Corresponde a `brand_tier` de `config.py` descrito en MODELOS L.414; la lista del relato incluye marcas (Plymouth, Pontiac) ausentes de la de MODELOS, que no las enumera.

### C030 — Desaparición de la prima premium cuantificable
- **Section**: `PRESENTACION_STORYTELLING.md` §4
- **Lines**: 231
- **Types**: result
- **Excerpt**: «En una primera lectura parecía que la marca funcionaba como un **seguro de valor**; con los datos corregidos, esa prima premium dejó de ser significativa y ya no podemos ponerle un número fijo.»
- **Restated**: La prima premium no es estadísticamente significativa con los datos corregidos.
- **Notes**: Coherente con C006 y con el coeficiente Premium del Cuadro 5 (p = 0,947, L.371) y de `modelo_depreciacion.csv:5` (p = 0,8753), aunque los valores difieran.

### C031 — TRMI informal citada en el storytelling
- **Section**: `PRESENTACION_STORYTELLING.md` §5 «La divisa»
- **Lines**: 242
- **Types**: citation-grounded, definitional
- **Excerpt**: «La referencia real es la **TRMI informal: 930 CUP por USD** (elTOQUE, noviembre 2026).»
- **Restated**: La tasa de referencia es 930 CUP por USD según elTOQUE en noviembre de 2026.
- **Notes**: Concuerda con README L.73 y MODELOS L.409, que fijan la fecha exacta en 18/11/2026; aquí la fecha es solo mensual.

### C032 — Decreto 163/2026 y 17 empresas autorizadas
- **Section**: `PRESENTACION_STORYTELLING.md` §5 «Las reglas»
- **Lines**: 245
- **Types**: citation-grounded
- **Excerpt**: «El **Decreto 163/2026** abrió el mercado a 17 empresas autorizadas. Las resoluciones 171–175 y 340 —que derogó la 312— fijan valores referenciales, impuestos especiales y reglas aduaneras.»
- **Restated**: El Decreto 163/2026 habilitó a 17 empresas y las resoluciones 171–175 y 340 regulan valores, impuestos y aduanas.
- **Notes**: Confirmado por `INFORME_TECNICO.md:67`; el informe añade que la 340 derogó a la 312 y que el Decreto 163 derogó al 119/2024, detalle ausente aquí.

### C033 — Encuesta sobre el auto eléctrico
- **Section**: `PRESENTACION_STORYTELLING.md` §5 «Las expectativas»
- **Lines**: 251
- **Types**: result
- **Excerpt**: «Entre las 28 personas a las que les interesaría comprar, 14 prefieren el eléctrico; pero 16 de 18 no pagarían más de 4.000 USD por uno, y el eléctrico más barato del catálogo formal cuesta poco más de 10.000 USD. Kia y Hyundai son las marcas modernas más vistas —28 y 25 de 30 entrevistas— y no aparecen en ese catálogo.»
- **Restated**: 14 de 28 compradores potenciales prefieren el eléctrico, 16 de 18 no pagarían más de 4.000 USD y el más barato del catálogo supera los 10.000 USD.
- **Notes**: Denominadores inconsistentes (28, 18 y 30 entrevistas) sin explicación; el número 28 se usa para dos magnitudes distintas. No hay tabla de encuesta en el corpus.

### C034 — Estaciones de carga y conectores
- **Section**: `PRESENTACION_STORYTELLING.md` §6
- **Lines**: 261, 265
- **Types**: result, citation-grounded
- **Excerpt**: «El mapa offline del proyecto reúne el contorno de Cuba y las coordenadas de los concesionarios con presencia verificada: BDC One y Dongfeng Cuba.» y «**Carga eléctrica:** 11 estaciones solares de Dongfeng/NWI y 21 estaciones de CIMEX+MITRANS; conectores CCS2 mayoritarios.»
- **Restated**: El mapa incluye 11 estaciones solares y 21 de CIMEX+MITRANS, con predominio de conectores CCS2, y solo dos concesionarios verificados.
- **Notes**: Las cifras no se desglosan en la base `mapa_elementos.sqlite` descrita en L.799–809.

### C035 — Contraste con Egyptian-Used-Cars
- **Section**: `PRESENTACION_STORYTELLING.md` §7
- **Lines**: 277
- **Types**: contextual, citation-grounded
- **Excerpt**: «Tomamos como referencia **`Egyptian-Used-Cars`**, uno de los análisis de mercado automotriz más completos que tenemos: 23.500 anuncios, historial mensual de precios, econometría, SQL, Tableau y Power BI.»
- **Restated**: El referente egipcio reúne 23.500 anuncios, serie mensual de precios, econometría y herramientas de visualización.
- **Notes**: Coincide con `INFORME_TECNICO.md:1080,1513`; el calificativo «más completos que tenemos» es una valoración no contrastable en el corpus.

### C036 — Cuadro 1 como espejo de los KPI
- **Section**: `PRESENTACION_STORYTELLING.md` Apéndice
- **Lines**: 317–331
- **Types**: result
- **Excerpt**: «| Anuncios limpios | <!-- kpi:anuncios_totales -->2.174 | [...] | Marcas distintas | <!-- kpi:marcas_distintas -->50 | [...] | Año mediano | <!-- kpi:anio_mediano -->2020 |»
- **Restated**: El Cuadro 1 reproduce once KPI del mercado, incluidos 2.174 anuncios, 50 marcas y año mediano 2020.
- **Notes**: Los once valores coinciden con `kpis.csv:2-12`; el año mediano 2020 no se reitera en el cuerpo narrativo.

### C037 — Cuadro 2 por canal y tipo
- **Section**: `PRESENTACION_STORYTELLING.md` Apéndice
- **Lines**: 333–339
- **Types**: result
- **Excerpt**: «| Importación | Usado | <!-- kpi:anuncios_importacion -->691 | <!-- kpi:mediana_importacion -->26.000 USD | <!-- kpi:media_importacion -->27.046,22 USD | | Local | Nuevo | 21 | 24.623,66 | 24.729,59 | | Local | Usado | <!-- kpi:anuncios_usados_locales -->1.462 | <!-- kpi:mediana_local -->21.000 USD | <!-- kpi:media_local_usada -->28.201,06 USD |»
- **Restated**: El Cuadro 2 desagrega 691 usados importados, 21 nuevos locales y 1.462 usados locales con sus medianas y medias.
- **Notes**: Coincide fila por fila con `kpis_canal.csv:2-4`.

### C038 — Serie anual ONEI del Cuadro 3
- **Section**: `PRESENTACION_STORYTELLING.md` Apéndice
- **Lines**: 341–352
- **Types**: result, citation-grounded
- **Excerpt**: «| 2019 | 1.899,9 | 1.102,2 | [...] | 2025 | 781,1 | 324,0 |»
- **Restated**: La serie ONEI 2014–2025 muestra 1.899,9 millones de pasajeros en 2019 y 781,1 en 2025, y 1.102,2 y 324,0 millones en ómnibus.
- **Notes**: Es la única serie temporal numérica del corpus; está en millones y solo a nivel anual, de ahí la tensión con C003 y C010.

### C039 — Coeficientes del Cuadro 5
- **Section**: `PRESENTACION_STORYTELLING.md` Apéndice
- **Lines**: 364–375
- **Types**: result
- **Excerpt**: «| Intercepto | 12,4469 | 0,000 | | Económico | −1,1228 | 0,328 | | Medio | −1,2332 | 0,239 | | Premium | 0,0662 | 0,947 | | Antigüedad | −0,0708 | 0,237 | | log(km) | −0,0226 | 0,740 | | Potencia | −0,0046 | 0,165 | | Condición | −0,0340 | 0,802 |»
- **Restated**: El Cuadro 5 atribuye ocho coeficientes y p_valores al modelo hedónico vigente.
- **Notes**: Los ocho coeficientes y los ocho p_valores difieren de `modelo_depreciacion.csv:2-9` (intercepto 12,0884; económico −1,0208; medio −0,9780; premium 0,1146; antigüedad −0,0632; log(km) −0,0333; potencia −0,0036; condición −0,0254). La tabla es de una corrida anterior, pese a la etiqueta «coeficientes vigentes» (L.364).

### C040 — Tamaños de muestra del Cuadro 5
- **Section**: `PRESENTACION_STORYTELLING.md` Apéndice
- **Lines**: 377
- **Types**: result
- **Excerpt**: «Ningún coeficiente resulta estadísticamente significativo con la base actual. Es parte de la historia: el mercado no admite una curva única. La tabla `modelo_muestra.csv` documenta las 22 observaciones de este modelo frente a las 572 del modelo principal; la pendiente positiva de este último refleja la selección de anuncios con kilometraje declarado y no se interpreta como depreciación.»
- **Restated**: `modelo_muestra.csv` documenta 22 observaciones para el modelo completo y 572 para el principal, sin coeficientes significativos.
- **Notes**: `modelo_muestra.csv:2-3` registra 586 (principal) y 28 (completo); ni 22 ni 572 aparecen en el CSV citado. Coherente con MODELOS L.452, que sí da 586 y 28.

### C041 — Normalización sintáctica de precios y kilometraje
- **Section**: `MODELOS_Y_FUNCIONES.md` §1
- **Lines**: 407–408
- **Types**: result, methodological
- **Excerpt**: «`parse_price` | Convierte `"13.000 USD"` en 13.000 [...] Sin esta regla, un auto de 13.000 USD entraba como 13 USD y era rechazado.» y «Corregirlo cambió la mediana de kilometraje de 80 a <!-- kpi:km_medianos -->32.569 km.»
- **Restated**: La normalización de separadores evitó precios de 13 USD y elevó la mediana de kilometraje de 80 a 32.569 km.
- **Notes**: El valor 32.569 coincide con `kpis.csv:11`; el valor previo de 80 km se atribuye a la lectura de `"80,000 km"` como 80.

### C042 — Conversión `to_usd` con tasa fechada
- **Section**: `MODELOS_Y_FUNCIONES.md` §1
- **Lines**: 409
- **Types**: definitional, methodological
- **Excerpt**: «`to_usd(precio, moneda)` | `precio × FX[moneda]` con TRMI informal: USD 1, CUP 1/930, EUR 1000/930, MLC 845,35/930. [...] Usar una sola tasa declarada y fechada (18/11/2026) permite comparar anuncios en USD, EUR y CUP.»
- **Restated**: La conversión aplica factores 1, 1/930, 1000/930 y 845,35/930 con una única tasa del 18/11/2026.
- **Notes**: `AUTOMATIZACION.md:647` reconoce que el `FX=930` está clavado en `config.py` y propone actualizarlo semanalmente, todavía pendiente (L.711 no lo incluye).

### C043 — Reglas de segmentación y rangos de filtro
- **Section**: `MODELOS_Y_FUNCIONES.md` §1
- **Lines**: 414–416
- **Types**: methodological, result
- **Excerpt**: «`brand_tier` | `premium / medio / económico / desconocido`, según listas declaradas en `config.py`. [...] contrastada después con Kruskal-Wallis.» y «Filtros de rango | Precio 200–250.000 USD, año 1990–2027, km ≤ 600.000, título ≥ 6 caracteres.»
- **Restated**: La clasificación por tier se valida con Kruskal-Wallis y los filtros de rango acotan precio, año, kilometraje y longitud del título.
- **Notes**: `AUTOMATIZACION.md:677` repite año 1990–`YEAR_MAX` y km ≤ 600.000; los rechazos se escriben en `rechazos.csv` (verificado, 2.314 KB).

### C044 — Elección de mediana, media y cuartiles
- **Section**: `MODELOS_Y_FUNCIONES.md` §2
- **Lines**: 422–428
- **Types**: methodological
- **Excerpt**: «Mediana | KPI principal de precio, benchmarks y canal. | El precio del auto usado cubano es asimétrico y tiene valores extremos; la mediana resiste mejor esos valores que la media.» y «Con `n ≥ 2` por grupo se evita sobreinterpretar un solo anuncio.»
- **Restated**: La mediana es el KPI principal por asimetría, la media documenta la cola derecha y los cuartiles exigen al menos dos anuncios por grupo.
- **Notes**: La media 28.201,06 frente a mediana 21.000 USD (`kpis.csv:8-9`) sustenta la afirmación de cola derecha.

### C045 — Definición de antigüedad y uso por año
- **Section**: `MODELOS_Y_FUNCIONES.md` §2
- **Lines**: 425–426
- **Types**: definitional
- **Excerpt**: «`car_age = 2026 − año` | Feature y filtro 0–40 años. | [...] Se acota a 40 porque fuera de ese rango hay clásicos con lógica de precio distinta.» y «`km_per_year = km / car_age` | Anomalías.»
- **Restated**: La antigüedad se calcula como 2026 menos el año, se acota a 0–40 años y el uso anual es km entre antigüedad.
- **Notes**: El valor fijo 2026 envejecerá; `AUTOMATIZACION.md:677` usa `YEAR_MAX` como parametrización parcial.

### C046 — Restricción de la muestra del modelo
- **Section**: `MODELOS_Y_FUNCIONES.md` §3.1
- **Lines**: 441
- **Types**: methodological
- **Excerpt**: «Se estima por mínimos cuadrados ordinarios sobre **usados del canal local**, con precio > 0, año presente y `car_age` entre 0 y 40. Solo se incluye un término si hay más de 30 observaciones no nulas, y el modelo exige más de 30 filas.»
- **Restated**: El OLS se estima solo sobre usados locales con precio positivo y antigüedad 0–40, exigiendo más de 30 observaciones por término y más de 30 filas.
- **Notes**: Tensión interna: el modelo completo informado tiene 28 filas (L.450, `modelo_muestra.csv:3`), por debajo del umbral declarado de 30; el informe técnico (L.1537) registra la misma contradicción.

### C047 — Rango de VIF
- **Section**: `MODELOS_Y_FUNCIONES.md` §3.2
- **Lines**: 458
- **Types**: result
- **Excerpt**: «Valores cercanos a 1 (los actuales van de 1,13 a 1,58) indican que los regresores no se explican entre sí; por tanto, la falta de significancia no se atribuye a colinealidad.»
- **Restated**: El VIF observado está entre 1,13 y 1,58, lo que descarta colinealidad como causa de la falta de significancia.
- **Notes**: `vif.csv:2-6` da 1,38 / 1,40 / 1,16 / 1,12 / 1,14, es decir rango 1,12–1,40; además incluye `price_usd`, variable ausente de la fórmula L.438.

### C048 — Resultado de Kruskal-Wallis
- **Section**: `MODELOS_Y_FUNCIONES.md` §3.3
- **Lines**: 462–464
- **Types**: result
- **Excerpt**: «Se aplica a los precios por `brand_tier` (grupos con más de 5 observaciones). Resultado vigente: H = 25,741, p = 1e−05.» y «Permite afirmar que **los tiers no provienen de la misma distribución de precios**»
- **Restated**: El test de Kruskal-Wallis da H = 25,741 con p = 1e−05 y permite afirmar que los tiers difieren en distribución de precios.
- **Notes**: `tests.csv:2` registra H = 32,818 y p = 0,0 para el mismo test; la conclusión cualitativa se mantiene, el estadístico no.

### C049 — Welch t-test codificado pero no ejecutado
- **Section**: `MODELOS_Y_FUNCIONES.md` §3.4
- **Lines**: 466–470
- **Types**: methodological
- **Excerpt**: «Compara precios usados vs nuevos con varianzas desiguales (`equal_var=False`). [...] En la corrida actual no se dispara porque el subconjunto del modelo contiene solo autos usados (`is_new` no varía)»
- **Restated**: El test de Welch está implementado pero no se ejecuta en la corrida vigente porque la muestra del modelo solo contiene usados.
- **Notes**: Afirmación de transparencia metodológica; compatible con la exclusión de nuevos en L.441.

### C050 — Umbrales y recuento de anomalías
- **Section**: `MODELOS_Y_FUNCIONES.md` §3.5
- **Lines**: 474–478
- **Types**: result
- **Excerpt**: «`km_anormal`: `km_per_year > 40.000` o `< 500`. [...] `precio_atipico`: precio por debajo del percentil 1 o por encima del percentil 99. | Se reportan <!-- kpi:anomalias -->89 anomalías en la corrida vigente.»
- **Restated**: Se señalan 89 anomalías con umbrales de 40.000/500 km por año y percentiles 1 y 99, sin eliminar filas del análisis.
- **Notes**: `anomalias.csv` tiene 89 filas de datos (90 líneas con cabecera); coincide con storytelling L.197.

### C051 — Límites explícitos del análisis
- **Section**: `MODELOS_Y_FUNCIONES.md` §4
- **Lines**: 482–486
- **Types**: methodological
- **Excerpt**: «No se usa la tasa oficial de cambio. No se imputan precios ni kilómetros faltantes. No se afirma causalidad: el modelo es de asociación sobre un corte transversal. No se presenta una curva de depreciación temporal: hace falta una serie mensual de 6–12 meses. No se mezclan mercados: local e importación se reportan por separado.»
- **Restated**: El corpus declara cinco límites: sin tasa oficial, sin imputación, sin causalidad, sin curva temporal y sin mezcla de mercados.
- **Notes**: El cuarto límite contradice directamente `AUTOMATIZACION.md:645` (C010); los demás son coherentes con C012, C008 y `kpis_canal.csv`.

### C052 — Complejidad objetivo del pipeline
- **Section**: `ARQUITECTURA_DATOS.md` §1
- **Lines**: 512–514
- **Types**: methodological, novelty
- **Excerpt**: «Hoy `run_all.py` lee el **100 % del histórico** en cada corrida. Con 2–5 años de datos, el tiempo crece linealmente con el tamaño total. El objetivo no es "comprar un motor más rápido", sino cambiar la complejidad por ejecución de `O(total)` a `O(nuevo + particiones consultadas)`.»
- **Restated**: El objetivo declarado es pasar de O(total) a O(nuevo + particiones consultadas) sin cambiar de motor.
- **Notes**: «Cuatro medidas atacan el crecimiento» (L.514): particionar, watermark, pre-agregar KPIs y compactar; no hay medición de línea base en el corpus (`benchmark_result.csv` se anuncia en L.566 como futuro).

### C053 — Comparativa de motores y reglas de tamaño Parquet
- **Section**: `ARQUITECTURA_DATOS.md` §2
- **Lines**: 520–527
- **Types**: methodological, citation-grounded
- **Excerpt**: «**DuckDB** sobre Parquet [...] **Recomendado**» y «**Polars** lazy/streaming | Cuando el cuello sea limpieza/transformación; ~1,15–1,33× más rápido que DuckDB en benchmarks de proveedor» y «archivos Parquet de 100 MB a 10 GB, row groups de 100K–1M filas, al menos 100 MB por partición [...] evitar más de ~2.000 archivos.»
- **Restated**: DuckDB es recomendado como motor principal, Polars es una segunda opción con ventaja de 1,15–1,33× según el proveedor, y se adoptan reglas de tamaño de ficheros.
- **Notes**: La recomendación de DuckDB queda condicionada por el bloqueo `SIGILL` de L.566; el factor de Polars se atribuye explícitamente a «benchmarks de proveedor», no a medición propia.

### C054 — Idempotencia, esquema evolutivo y hoja de ruta
- **Section**: `ARQUITECTURA_DATOS.md` §3–§4
- **Lines**: 541–554
- **Types**: methodological, result
- **Excerpt**: «Idempotencia: el watermark se actualiza en la misma transacción que el KPI. Si la corrida muere, el watermark no avanza.» y «**Esquema evolutivo**: `union_by_name=true` tolera columnas nuevas en años futuros.»
- **Restated**: La propuesta garantiza idempotencia transaccional del watermark y tolerancia a columnas nuevas, con criterios de «listo» por fase.
- **Notes**: Seis fases (0–5) con criterios verificables; el estado real es Fase 0–1 (L.566), por lo que las fases 2–5 son propuestas, no resultados.

### C055 — Corrección del bucle de Revolico y bloqueo de DuckDB
- **Section**: `ARQUITECTURA_DATOS.md` §6
- **Lines**: 564–566
- **Types**: result, methodological
- **Excerpt**: «El debug detectó que 3.351 enlaces no-auto quedaban `pending` para siempre y el bucle nunca cerraba: se corrigió marcándolos `rechazado` y excluyéndolos del conteo de salida» y «en esta CPU, `import duckdb` falla con `SIGILL` (Instrucción ilegal)»
- **Restated**: Se corrigieron 3.351 enlaces pendientes y DuckDB no puede usarse en esta CPU por un error SIGILL.
- **Notes**: Los 3.351 enlaces coinciden con `INFORME_TECNICO.md:1122,1148,1461`; el bloqueo SIGILL relativiza C013 y C053.

### C056 — Proyección de retención
- **Section**: `ALCANCE_Y_RETENCION.md` §2
- **Lines**: 593–604
- **Types**: result, methodological
- **Excerpt**: «Supuesto: ~4.000–5.000 palabras, 18–25 minutos de lectura, patrones generales de long-form. De cada **100 visitantes**: [...] Lee el primer párrafo | 50–65 | **58** [...] Vuelve con intención de consulta | 3–8 | **5**» y «la proyección condicionada (también inferencia) es: **finalización 22–25** y **retorno 18–22** por cada 100.»
- **Restated**: La proyección estima 58 lectores del primer párrafo y 5 consultas por cada 100 visitantes, con 22–25 finalizaciones y 18–22 retornos tras las correcciones.
- **Notes**: Cualificado como inferencia en L.591 y L.604; el supuesto de 4.000–5.000 palabras no coincide con el corpus unificado (9.193 palabras en 8 archivos), aunque el storytelling por sí solo sí podría estar en ese rango.

### C057 — Métricas de difusión propuestas
- **Section**: `ALCANCE_Y_RETENCION.md` §3
- **Lines**: 608–612
- **Types**: methodological
- **Excerpt**: «**SEO de intención comercial** [...] Métrica: CTR > 3 % en 90 días.» y «**Distribución con UTM** [...] Métrica: clics por canal yscroll > 90 %.»
- **Restated**: El plan de difusión define cinco acciones con métricas como CTR > 3 % en 90 días y scroll > 90 %.
- **Notes**: «ychannel»/«yscroll» parecen artefactos de pegado («clics por canal y scroll > 90 %»); no hay medición de estas métricas en el corpus (ver C009).

### C058 — Separación de carriles de automatización
- **Section**: `AUTOMATIZACION.md` §1
- **Lines**: 637
- **Types**: methodological, novelty
- **Excerpt**: «**Recolectar → procesar → publicar.** Ningún job de recolección hace `git push`; ningún push dispara scrapers. Así un fallo de red no contamina los datos y un fallo de datos no bloquea la publicación.»
- **Restated**: Tres carriles desacoplados impiden que fallos de red o datos se propaguen entre recolección, procesamiento y publicación.
- **Notes**: Coherente con `ARQUITECTURA_DATOS.md:564` y con la lista de pendientes de L.711 (los scripts de Revolico y marketplaces aún hacen push).

### C059 — Tabla de periodicidades
- **Section**: `AUTOMATIZACION.md` §2
- **Lines**: 643–653
- **Types**: methodological
- **Excerpt**: «Radar Telegram [...] | Diario | La vista pública solo conserva mensajes recientes» y «Revolico incremental | Semanal | El backfill completo es caro y agresivo»
- **Restated**: Once jobs se programan con frecuencias diaria, semanal, trimestral o puntual según la volatilidad de cada fuente.
- **Notes**: `ARQUITECTURA_DATOS.md:564` describe la extracción continua de Revolico con timer de 10 minutos, frecuencia distinta de la «semanal» declarada aquí; L.711 confirma que el timer de Revolico aún está pendiente de integrar.

### C060 — Panel autocontenido frente a Plotly remoto
- **Section**: `AUTOMATIZACION.md` §2 «Panel interactivo autocontenido»
- **Lines**: 659
- **Types**: result, methodological
- **Excerpt**: «antes hacían falta los 6 HTML de Plotly (168 KB) más ~4,5 MB de JavaScript remoto por visita, y el mapa suelto pesaba 4,7 MB sin publicar en el sitio; ahora un solo archivo de **107 KB** sin peticiones externas funciona por `file://` y en 3G.»
- **Restated**: El dashboard pasó de seis HTML más ~4,5 MB remotos a un único archivo de 107 KB sin peticiones externas.
- **Notes**: Medición antes/después declarada; el mapa `mapa_ofline.html` de `Data/mapas/README.md:820` sigue incluyendo Plotly embebido, por lo que son artefactos distintos.

### C061 — Actualización automática de cifras
- **Section**: `AUTOMATIZACION.md` §2 «Números que se actualizan solos»
- **Lines**: 663
- **Types**: methodological, novelty
- **Excerpt**: «`README.md`, el storytelling, el análisis de alcance y el inventario de modelos llevan un marcador oculto `<!-- kpi:clave -->` justo antes de cada cifra. Al terminar `run_all.py`, `actualizar_numeros.py` lee los CSV y las bases vigentes y reemplaza **solo el número**, conservando las palabras de alrededor.»
- **Restated**: Cuatro documentos usan marcadores `kpi:` y un script reemplaza solo el número al terminar `run_all.py`, con modo `--check`.
- **Notes**: Explica por qué las cifras del corpus coinciden con `kpis.csv`; no explica por qué subsisten las discrepancias 2.222/2.232, 974/812 y 28/22, que probablemente provienen de texto no marcado o de CSV distintos.

### C062 — Envoltorio de ejecución y ledger LFS
- **Section**: `AUTOMATIZACION.md` §3
- **Lines**: 667–673
- **Types**: methodological, result
- **Excerpt**: «Envoltorio único `Data/_state/run_step.sh <job> <comando>` con `flock`, `timeout`, estado atómico (`tmp` + `mv`) y `heartbeat_utc`.» y «`loginctl enable-linger` **ya ejecutado** (Linger=yes) y timers `Persistent=true`»
- **Restated**: Los jobs usan un envoltorio con bloqueo, timeout y estado atómico, con watermark y ledger LFS que cuarentena objetos tras tres fallos.
- **Notes**: El ledger LFS aparece aquí como implementado y en L.711 como pendiente; contradicción interna de estado.

### C063 — Compuertas de calidad y alertas
- **Section**: `AUTOMATIZACION.md` §4
- **Lines**: 677–681
- **Types**: methodological
- **Excerpt**: «conteos por fuente dentro de ±40 % de la mediana de las últimas 8 corridas; frescura < 10 días; presencia de las 8 marketplaces y Revolico.» y «Si el ratio de rechazo > 10 % el job falla; entre 5 y 10 % solo avisa.»
- **Restated**: Las compuertas exigen desviaciones ≤40 %, frescura <10 días, ocho marketplaces y umbrales de rechazo del 5 y 10 %.
- **Notes**: La regla de «2× su periodo sin éxito» genera `ALERTA.stale` (L.681); no se muestran corridas reales de estas compuertas en el corpus.

### C064 — Regla de oro de los snapshots
- **Section**: `AUTOMATIZACION.md` §5
- **Lines**: 690–695
- **Types**: result, methodological
- **Excerpt**: «Un snapshot Parquet inmutable por semana (`snapshots/YYYY-Www/`) con puntero `LATEST.json`. 104 semanas ≈ 2 años.» y «**Regla de oro:** un snapshot se escribe una vez y nunca se sobrescribe; el estado actual es un puntero.»
- **Restated**: El diseño prevé 104 snapshots semanales inmutables en dos años con un puntero al último.
- **Notes**: Es el mismo cómputo 104≈2 años de C010; aquí se presenta como almacenamiento, no como prueba de suficiencia para depreciación.

### C065 — Corrida real de validación de calidad
- **Section**: `AUTOMATIZACION.md` §6 «Estado de implementación»
- **Lines**: 706–709
- **Types**: result
- **Excerpt**: «`validar_calidad.py`: 6 reglas, cuarentena en `Data/_cuarentena/`, umbral 10 %. Corrida real: 2.014 filas, 0 inválidos.»
- **Restated**: La validación con seis reglas procesó 2.014 filas sin inválidos en una corrida real.
- **Notes**: 2.014 es el resultado de la corrida del 23/11/2026 (`INFORME_TECNICO.md:1391`), anterior a los 2.174 vigentes de `kpis.csv:2`; el corpus no explicita que sea una corrida histórica.

### C066 — Estimación de ancho de banda
- **Section**: `AUTOMATIZACION.md` §6b
- **Lines**: 721–726
- **Types**: result
- **Excerpt**: «Circuitos (2 páginas) | Diario | ~2–5 KB/día | ~220 KB/día [...] | **Total estimado** | — | **~5–10 MB/mes** | **~50–90 MB/mes**» y «Son estimaciones de diseño, no mediciones de facturación.»
- **Restated**: El consumo estimado es de ~5–10 MB/mes sin cambios y ~50–90 MB/mes con cambios.
- **Notes**: El total «sin cambios» no cuadra con la suma de filas (~0,06–0,15 + ~0,09–0,22 + ~2,15 MB/mes ≈ 2,3–2,5 MB/mes); el escenario con cambios sí es del orden de 56–99 MB/mes. Está explícitamente marcado como estimación.

### C067 — Límite de la vista pública de Telegram
- **Section**: `AUTOMATIZACION.md` §7
- **Lines**: 730
- **Types**: contextual
- **Excerpt**: «La vista pública de Telegram es un **radar de novedades**, no una serie histórica: ~20 mensajes por página, ventana de ~8 días, sin garantía de ediciones o borrados.»
- **Restated**: Telegram ofrece ~20 mensajes por página con ventana de ~8 días y no constituye serie histórica.
- **Notes**: Coherente con la frecuencia diaria del radar (L.643) y con la recomendación de revisión trimestral de 30 minutos.

### C068 — Espacio ocupado en GitHub y localmente
- **Section**: `ESTRUCTURA_ESPACIO.md` §Cuánto pesa en GitHub
- **Lines**: 741–743
- **Types**: result
- **Excerpt**: «La API de GitHub reporta **205.002 KB ≈ 0,20 GB**. Ese número cuenta solo el historial normal del repositorio [...] En esta computadora, la copia de esos archivos grandes ocupa **3,3 GB** (174 archivos).»
- **Restated**: GitHub informa 205.002 KB de historial normal y la copia local de archivos grandes ocupa 3,3 GB en 174 archivos.
- **Notes**: El documento advierte que la API pública no informa del almacenamiento LFS, por lo que el total exacto queda sin verificar.

### C069 — Mapa de carpetas y prioridades de ahorro
- **Section**: `ESTRUCTURA_ESPACIO.md` §Mapa sencillo y §Dónde mirar primero
- **Lines**: 748–773
- **Types**: result
- **Excerpt**: «Proyecto (10 GB) ├── .git (4,3 GB) [...] ├── Data (4,1 GB) └── Revolico (3,4 GB) [...] `revolico.sqlite` 810 MB» y «Las tres copias partidas de Revolico (811 + 759 + 518 MB).»
- **Restated**: El proyecto ocupa ~10 GB, con 4,3 GB en `.git`, 4,1 GB en `Data` y tres copias partidas de Revolico de 811, 759 y 518 MB.
- **Notes**: Los subtotales del mapa son aritméticamente consistentes; `INFORME_TECNICO.md:1471` registra la reducción de 20 GB a 10 GB.

### C070 — Base única del mapa y codificación visual
- **Section**: `Data/mapas/README.md` §Base de datos
- **Lines**: 799–809
- **Types**: definitional, contextual
- **Excerpt**: «`mapa_elementos.sqlite` es la fuente única. Tablas: - `tipos`: catálogo de capas y colores. - `elementos`: nombre, coordenadas, dirección, fuente, URL, teléfono, horario, precio, estado y detalle crudo en JSON.» y «| `gasolinera` | **negro** | círculo | OpenStreetMap/Overpass |»
- **Restated**: `mapa_elementos.sqlite` es la fuente única del mapa, con dos tablas y cuatro tipos de elemento codificados por color y símbolo.
- **Notes**: Cuatro tipos: gasolinera, estacion_carga, concesionario y taller; no se dan recuentos por tipo en este archivo.

### C071 — Generación del mapa y cadena anti-bot
- **Section**: `Data/mapas/README.md` §Generar el mapa y §Anti-bot
- **Lines**: 820, 833
- **Types**: methodological, result
- **Excerpt**: «`mapa_ofline.html` incluye Plotly embebido, así que funciona sin internet. Los elementos sin coordenadas se exportan a `elementos_sin_coordenadas.csv`.» y «El scraper usa, en orden: `curl_cffi` con impersonación de Chrome/Safari, **`patchright`** [...] y **FlareSolverr** (`http://127.0.0.1:8191/v1`) para páginas como Cybo que devuelven 403»
- **Restated**: El mapa es autocontenido con Plotly embebido y el scraper aplica tres niveles anti-bot con FlareSolverr en el puerto 8191.
- **Notes**: Contraste con `AUTOMATIZACION.md:659`, donde el dashboard se describe sin Plotly; son dos artefactos diferentes, pero el README no lo aclara.

## Contextual claims (47)

### C072 — Identificación y fecha del README
- **Section**: `README.md` §encabezado
- **Lines**: 14
- **Types**: contextual
- **Excerpt**: «*Ubicación:* `~/Proyectos/El precio de moverse en Cuba` · *Repositorio:* `el-precio-de-moverse-en-cuba` · *Actualizado:* 23/11/2026.»

### C073 — Datos crudos auditables
- **Section**: `README.md` §Qué incluye
- **Lines**: 18
- **Types**: contextual
- **Excerpt**: «**Datos crudos y auditables**: anuncios, enlaces, colas de descarga y descartes exportados por categoría en `Data/CRUDO_POR_CATEGORIA/`.»

### C074 — Análisis regenerable
- **Section**: `README.md` §Qué incluye
- **Lines**: 20
- **Types**: contextual
- **Excerpt**: «**Análisis regenerable**: KPIs, benchmarks, depreciación y gráficos en `Data/analisis_rentabilidad/`.»

### C075 — Documentación incluida
- **Section**: `README.md` §Qué incluye
- **Lines**: 22
- **Types**: contextual
- **Excerpt**: «**Documentación**: informe técnico, storytelling, auditoría de fuentes e índices de datos.»

### C076 — Requisitos del Quickstart
- **Section**: `README.md` §Quickstart
- **Lines**: 26–32
- **Types**: contextual
- **Excerpt**: «Requiere Python 3.10+ y Git LFS. Desde la carpeta del proyecto: [...] `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py`»

### C077 — Fases y salidas visibles
- **Section**: `README.md` §Quickstart
- **Lines**: 34–40
- **Types**: contextual
- **Excerpt**: «Al terminar verás `INGESTA`, `LIMPIEZA`, `EDA`, `STATS` y `BENCHMARK`, y se habrán actualizado: [...] `listings_clean.parquet` [...] `kpis.csv` [...] `kpis_canal.csv`»

### C078 — Estructura de carpetas del proyecto
- **Section**: `README.md` §Estructura
- **Lines**: 46–59
- **Types**: contextual
- **Excerpt**: «├── catalogos_concesionarios/ # 11 concesionarios + 8 marketplaces [...] └── Copias/, Hombros/, Anexos/ # referencias y corpus (no versionados)»

### C079 — Exclusión de repositorios auxiliares
- **Section**: `README.md` §Estructura
- **Lines**: 61
- **Types**: contextual
- **Excerpt**: «Los repositorios auxiliares y `Copias/` se conservan en disco pero **no se suben**: están excluidos en `.gitignore`.»

### C080 — Archivos de configuración
- **Section**: `README.md` §Configuración
- **Lines**: 79–82
- **Types**: contextual
- **Excerpt**: «`Data/analisis_rentabilidad/config.py` | Rutas, umbrales de precio/año, TRMI, marcas y tiers» y «`.gitattributes` | Archivos SQLite y chunks `.bin` gestionados con Git LFS»

### C081 — Reconstrucción de bases desde chunks
- **Section**: `README.md` §Configuración
- **Lines**: 84–89
- **Types**: contextual
- **Excerpt**: «Si `revolico.sqlite` o `pipeline.sqlite` no existen, los scripts los reconstruyen desde sus chunks: [...] `db_chunks.py verify` [...] `db_chunks.py assemble`»

### C082 — Sitio MkDocs
- **Section**: `README.md` §Sitio de documentación
- **Lines**: 93–101
- **Types**: contextual
- **Excerpt**: «El storytelling, los cuadros, los gráficos y el inventario de modelos se publican como un sitio MkDocs: [...] El resultado queda en `site/` (ignorado por Git) y la configuración en `mkdocs.yml`.»

### C083 — Inventario de documentación de referencia
- **Section**: `README.md` §Documentación
- **Lines**: 103–108
- **Types**: contextual
- **Excerpt**: «**Referencia:** `INFORME_TECNICO.md` (secciones 1–60), `Data/CRUDO_POR_CATEGORIA/INDICE.md`, [...] **Necesidades pendientes:** `Data/analisis_rentabilidad/NECESIDADES.md`.»

### C084 — Cumplimiento de términos de uso
- **Section**: `README.md` §Marco legal y límites
- **Lines**: 112
- **Types**: contextual, methodological
- **Excerpt**: «El proyecto respeta los términos de uso de los portales: no elude mecanismos anti-automatización, no recopila datos personales de anunciantes y conserva la procedencia de cada dato.»

### C085 — Tesis narrativa del storytelling
- **Section**: `PRESENTACION_STORYTELLING.md` §encabezado
- **Lines**: 127
- **Types**: contextual
- **Excerpt**: «En Cuba, moverse no se decide por un precio: se decide por cuánto costará mañana. Esta es la historia de un mercado donde el combustible cambia con la divisa, el ómnibus ya no llega como antes y el carro propio se volvió infraestructura doméstica.»

### C086 — Rutina del transporte público
- **Section**: `PRESENTACION_STORYTELLING.md` §1
- **Lines**: 139–143
- **Types**: contextual
- **Excerpt**: «En Cuba, salir de casa no empieza cuando uno abre la puerta. Empieza antes: mirando el reloj, calculando cuánto se tarda en llegar a la parada [...] Durante décadas, esa fue la ecuación: esperar, adaptarse, llegar tarde.»

### C087 — Flotas envejecidas e imprevisibilidad
- **Section**: `PRESENTACION_STORYTELLING.md` §1
- **Lines**: 141
- **Types**: contextual
- **Excerpt**: «flotas envejecidas, frecuencias irregulares, largas colas y trayectos que se vuelven inciertos cuando escasea el combustible [...] En las ciudades grandes, la distancia no es el problema; la imprevisibilidad lo es.»

### C088 — Triciclo eléctrico como segundo sistema
- **Section**: `PRESENTACION_STORYTELLING.md` §1
- **Lines**: 149–151
- **Types**: contextual
- **Excerpt**: «Hoy también aparecen los **triciclos eléctricos**, que se han vuelto una parte común del paisaje urbano. [...] En Cuba el taxi —y ahora el triciclo eléctrico— funciona como un segundo sistema de transporte: estatal, particular, colectivo, autorizado o improvisado.»

### C089 — Tarifas dependientes de la hora
- **Section**: `PRESENTACION_STORYTELLING.md` §1
- **Lines**: 153
- **Types**: contextual
- **Excerpt**: «Pero la tarifa no es una sola: **depende de la hora del día**. La carrera de la mañana no cuesta lo mismo que la de la noche; el trayecto corto, el viaje largo y el servicio nocturno tienen precios distintos.»

### C090 — Las gacelas como antecedente
- **Section**: `PRESENTACION_STORYTELLING.md` §1
- **Lines**: 155
- **Types**: contextual
- **Excerpt**: «El transporte regulado por el Estado ya lo había mostrado con las **gacelas**: en sus turnos de noche podían cobrar lo mismo que un taxi, o incluso más, por el mismo servicio.»

### C091 — Carro como infraestructura doméstica
- **Section**: `PRESENTACION_STORYTELLING.md` §1
- **Lines**: 159
- **Types**: contextual
- **Excerpt**: «Hoy, para muchas familias, el carro propio ha dejado de ser un lujo y se ha convertido en una forma de infraestructura doméstica: la posibilidad de llegar al trabajo, llevar a los niños a la escuela, trasladar mercancías o aprovechar una oportunidad de negocio sin depender de un horario ajeno.»

### C092 — Decisión financiera bajo incertidumbre
- **Section**: `PRESENTACION_STORYTELLING.md` §1
- **Lines**: 161
- **Types**: contextual
- **Excerpt**: «Pero comprar un auto en Cuba no es una decisión simple. Es una decisión financiera tomada en un mercado donde el precio, la divisa, el mantenimiento y el futuro del vehículo cambian al mismo tiempo.»

### C093 — Reformulación de la pregunta central
- **Section**: `PRESENTACION_STORYTELLING.md` §2
- **Lines**: 167
- **Types**: contextual
- **Excerpt**: «Cuando alguien decide comprar un carro en Cuba, la pregunta no es ¿Cuál es el precio?, sino ¿cuánto costará?»

### C094 — Tres monedas, tres historias
- **Section**: `PRESENTACION_STORYTELLING.md` §2
- **Lines**: 173
- **Types**: contextual
- **Excerpt**: «El precio aparece en USD, en EUR o en CUP, y cada moneda cuenta una historia distinta. El tipo de cambio oficial no es el que se usa en la calle: la referencia real es la tasa informal.»

### C095 — Electrolineras y circuitos
- **Section**: `PRESENTACION_STORYTELLING.md` §2
- **Lines**: 181
- **Types**: contextual
- **Excerpt**: «Bajo estas condiciones uno creería que la solución es pasar a un carro eléctrico. Pero la red de electrolineras todavía no está desarrollada en el país: se anuncia que está en construcción, y aun cuando se complete será insuficiente por un tiempo.»

### C096 — Gasolinera sin suministro eléctrico
- **Section**: `PRESENTACION_STORYTELLING.md` §2
- **Lines**: 183
- **Types**: contextual
- **Excerpt**: «para comprar en una gasolinera basta con que su circuito se quede sin luz. Si la estación no tiene generador u otra fuente de respaldo, los surtidores no funcionan. Puede haber combustible y, aun así, no poder echarlo.»

### C097 — Talleres independientes y costo de inmovilización
- **Section**: `PRESENTACION_STORYTELLING.md` §2
- **Lines**: 189
- **Types**: contextual
- **Excerpt**: «El problema no es solo encontrar quién repare: es conseguir la pieza, esperar la importación y aceptar que, mientras tanto, el vehículo se queda inmovilizado. [...] un auto detenido no solo deja de mover: deja de generar.»

### C098 — Promesa de síntesis
- **Section**: `PRESENTACION_STORYTELLING.md` §2
- **Lines**: 201
- **Types**: contextual
- **Excerpt**: «Estas cuatro preguntas tienen respuesta, pero estaban dispersas en anuncios, catálogos, resoluciones y conversaciones. Este proyecto nace para juntarlas.»

### C099 — Dos mercados convivientes
- **Section**: `PRESENTACION_STORYTELLING.md` §3
- **Lines**: 209
- **Types**: contextual
- **Excerpt**: «Lo primero que uno debe saber es que el mercado está dividido en dos partes: la de los **marketplaces**, donde vende principalmente el particular o el pequeño comercial, y la de los **concesionarios y tiendas oficiales**, donde el precio lo fija la marca o el importador autorizado.»

### C100 — Mercado pequeño pero estructurado
- **Section**: `PRESENTACION_STORYTELLING.md` §3
- **Lines**: 219
- **Types**: contextual
- **Excerpt**: «> *Encontramos un mercado pequeño, sí, pero con suficiente estructura para dejar de improvisar.*»

### C101 — Depreciación gradual
- **Section**: `PRESENTACION_STORYTELLING.md` §4
- **Lines**: 225
- **Types**: contextual
- **Excerpt**: «Un auto no pierde valor de golpe: lo va perdiendo con cada año, con cada kilómetro y con cada vez que aparece en un anuncio con la documentación incompleta. Pero la curva no es igual para todos.»

### C102 — Uso medio y caída no significativa
- **Section**: `PRESENTACION_STORYTELLING.md` §4
- **Lines**: 229
- **Types**: contextual, result
- **Excerpt**: «Los autos de uso medio —los que trabajan, cargan y recorren la ciudad todos los días— son los que más se mueven en el modelo, aunque ya no podemos afirmar que caigan más rápido de forma significativa.»

### C103 — Cuatro corrientes que mueven el precio
- **Section**: `PRESENTACION_STORYTELLING.md` §5
- **Lines**: 239–240
- **Types**: contextual
- **Excerpt**: «Lo que aparece en el anuncio es solo la superficie. Debajo hay cuatro corrientes que mueven el precio:»

### C104 — Aplicación Circuitos Habana
- **Section**: `PRESENTACION_STORYTELLING.md` §5 «La luz»
- **Lines**: 248
- **Types**: contextual
- **Excerpt**: «La app cubana **Circuitos Habana** sigue los mensajes públicos de la Empresa Eléctrica y registra qué circuitos están afectados. Para un carro eléctrico, la energía no es un dato menor: es parte del costo de propiedad.»

### C105 — De catálogo a inteligencia de mercado
- **Section**: `PRESENTACION_STORYTELLING.md` §5
- **Lines**: 255
- **Types**: contextual
- **Excerpt**: «> Cruzar estas cuatro capas convierte un catálogo de anuncios en inteligencia de mercado.»

### C106 — Funcionalidad del mapa
- **Section**: `PRESENTACION_STORYTELLING.md` §6
- **Lines**: 269
- **Types**: contextual
- **Excerpt**: «El mapa no es un adorno: es la vista desde la que se decide dónde conviene comprar, vender o invertir.»

### C107 — Escalabilidad frente al referente egipcio
- **Section**: `PRESENTACION_STORYTELLING.md` §7
- **Lines**: 279–283
- **Types**: contextual, novelty
- **Excerpt**: «Nuestro proyecto ya tiene esa arquitectura: ingesta incremental, limpieza y features, análisis exploratorio, modelo econométrico con tests, benchmarks e infravalorados, salidas versionables. La diferencia es el tiempo. Egipto construyó su serie durante meses; aquí el mecanismo ya está sembrado y cada semana suma una observación real de precio.»
- **Notes**: «ya tiene esa arquitectura» es más fuerte que el estado «Fase 0–1 de diseño» de `ARQUITECTURA_DATOS.md:566` (ver C013).

### C108 — Agenda de trabajo futuro
- **Section**: `PRESENTACION_STORYTELLING.md` §8
- **Lines**: 289–295
- **Types**: methodological, contextual
- **Excerpt**: «2. Convertir el snapshot semanal en una **serie de precios de 6–12 meses». [...] El resultado no será un informe. Será un **observatorio del mercado automotor cubano**.»

### C109 — Cierre y llamada a volver
- **Section**: `PRESENTACION_STORYTELLING.md` §9
- **Lines**: 301–307
- **Types**: contextual
- **Excerpt**: «El mercado no se detiene. Cada semana sumamos una observación real de precios; el índice por marca, modelo y provincia se actualiza en [KPIs y tablas](outputs/tables/kpis.csv) y el estado eléctrico en el [mapa de circuitos](../mapas/TIMELAPSE_CIRCUITOS.md). Vuelve por un dato puntual, no por un informe entero.»

### C110 — Promesa de justificación del inventario de modelos
- **Section**: `MODELOS_Y_FUNCIONES.md` §encabezado
- **Lines**: 399
- **Types**: methodological
- **Excerpt**: «Inventario de todo lo que transforma o estima el pipeline [...] La justificación es metodológica y también empírica: se dice qué se calculó, por qué esa forma y qué límite tiene con los datos actuales.»

### C111 — Preparación determinista sin inferencia
- **Section**: `MODELOS_Y_FUNCIONES.md` §1
- **Lines**: 403
- **Types**: methodological
- **Excerpt**: «Estas funciones no "descubren" nada: hacen que los valores sean comparables. Su respaldo es la reproducibilidad y la trazabilidad.»

### C112 — Justificación de la especificación hedónica
- **Section**: `MODELOS_Y_FUNCIONES.md` §3.1
- **Lines**: 443–448
- **Types**: methodological
- **Excerpt**: «**Logaritmo del precio:** los precios son positivos y muy asimétricos; el log estabiliza la varianza y permite leer coeficientes como aproximaciones de cambio porcentual. [...] **Atributos hedónicos:** precio, antigüedad, km, potencia, condición y marca son los determinantes estándar de un modelo hedónico de autos usados.»

### C113 — Objetivo de la arquitectura
- **Section**: `ARQUITECTURA_DATOS.md` §encabezado
- **Lines**: 495–497
- **Types**: contextual
- **Excerpt**: «# Arquitectura de datos para crecer durante años (23/11/2026)»

### C114 — Veredictos sobre motores alternativos
- **Section**: `ARQUITECTURA_DATOS.md` §2
- **Lines**: 523–525
- **Types**: contextual, methodological
- **Excerpt**: «**Iceberg / Delta Lake** | ACID, time travel y correcciones de histórico; con writer concurrente | Alta [...] | No ahora» y «**ClickHouse / chDB** [...] | Sobrekill para batch local»

### C115 — Objetivo de autosuficiencia a dos años
- **Section**: `AUTOMATIZACION.md` §encabezado
- **Lines**: 633
- **Types**: contextual
- **Excerpt**: «Objetivo: que una persona abra el proyecto **dos años después** y lo encuentre como fuente confiable, sin haber tenido que hacer mantenimiento diario.»

### C116 — Internet, linger y naturaleza de las estimaciones
- **Section**: `AUTOMATIZACION.md` §6b
- **Lines**: 715–726
- **Types**: contextual
- **Excerpt**: «**Sin internet no se puede scrapear**: la recolección necesita red. Lo que sí es posible es que ocurra **sin que tú estés presente ni conectado a la sesión**: `linger=yes` mantiene el gestor de usuario y los timers son `Persistent=true` [...] Cada fase tiene criterio de «listo» medible en el informe técnico.»

### C117 — Regla antes de liberar espacio
- **Section**: `ESTRUCTURA_ESPACIO.md` §Cómo buscarlo sin herramientas especiales
- **Lines**: 788
- **Types**: contextual
- **Excerpt**: «Regla: antes de quitar cualquier cosa, confirmar que ningún trabajo automático la esté usando y dejar una copia en `~/Utilidades` si todavía puede servir.»

### C118 — Escalada anti-bot para Cybo
- **Section**: `Data/mapas/README.md` §Anti-bot
- **Lines**: 833
- **Types**: methodological
- **Excerpt**: «El scraper usa, en orden: `curl_cffi` con impersonación de Chrome/Safari, **`patchright`** (navegador real con fingerprint de Chrome) y **FlareSolverr** (`http://127.0.0.1:8191/v1`) para páginas como Cybo que devuelven 403 o verificación de seguridad.»


## Apéndice C — Literatura

# Literature Map — Corpus de documentación de usuario

Nota de entrada. El plan aprobado (`reviews/corpus-documentacion-2026-11-28.plan.md`, 24 líneas) declara `language: es`, `level: master` y `preset: Standard`, pero **no contiene `queries_planned` ni `hypotheses_planned`**. El mandato recibido para este extractor es estrecho: inventariar los trabajos y fuentes institucionales que cita el corpus de 8 archivos de cara al usuario, cotejarlos con las 41 entradas de `Data/referencias.md` y marcar `(metadata incomplete)` lo no verificable. En consecuencia: (a) no se ejecutaron búsquedas web nuevas —los metadatos se reutilizan de la verificación OpenAlex/Crossref del 27/11/2026 consignada en `Data/referencias.md`—; (b) todos los ítems son L1, sin lectura de resúmenes (L2) ni de texto completo (L3); (c) los IDs `P001`–`P037` designan «fuentes y obras» en sentido amplio, no únicamente artículos académicos, porque el corpus auditado es documentación de usuario; (d) los números de línea corresponden a la copia en caché `.playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md` (833 líneas); (e) `Cited in document` significa «mencionado en el corpus auditado», no «mencionado en el informe técnico»; (f) el campo `Citada en el informe` de `Data/referencias.md` se refiere al informe técnico de la pasada 1 y **no** a este corpus.

**Resultado del cotejo:** cero coincidencias. El corpus no contiene marcadores `[N]`, DOI ni identificadores arXiv; ninguno de los 41 autores, títulos ni fuentes institucionales de `Data/referencias.md` aparece citado. A la inversa, las fuentes que el corpus sí cita (ONEI, Gaceta Oficial, BCC, elTOQUE, CIMEX, ministerios, normativa cubana, repositorios y directorios) no figuran en `Data/referencias.md`. El encaje entre ambos documentos es nulo en los dos sentidos, aunque hay solapamiento temático (mercado de autos usados, divisas cubanas, electromovilidad, scraping).

## Clusters

### Cluster 1 — Fuentes institucionales y estadísticas cubanas

**Query**: `instituciones y estadísticas citadas en el corpus` ∩ `Data/referencias.md` — búsqueda por nombre (ONEI, Gaceta Oficial, BCC, elTOQUE, CIMEX, ministerios) en los 8 archivos y en el anexo de 41 entradas.

El corpus apoya sus cifras en organismos cubanos, citados **por nombre pero sin ficha bibliográfica**: sin DOI, sin URL de destino, sin año de publicación de la edición concreta y sin marcador numérico. Ninguno aparece en `Data/referencias.md`.

#### P001 — ONEI (Oficina Nacional de Estadística e Informática)

- **Authors**: ONEI (organismo oficial)
- **Year**: anuarios 2014–2025 (rango declarado; sin año de edición individual)
- **Venue**: `Data/fuentes-oficiales/ONEI/` (12 anuarios, 233 archivos, índice y SHA-256)
- **Citations**: no aplica; sin conteo posible
- **URL**: no declarada en el corpus → **(metadata incomplete: URL institucional y años de edición individuales no verificables en el corpus ni en `Data/referencias.md`)**
- **Layer**: L1
- **Cited in document**: yes — líneas 12, 21, 53, 71, 131, 145, 341, 354, 579, 624, 648 (Cuadros 3 y 4; −59 % de pasajeros frente a 2019)
- **Document reference**: ninguno — ausente de las 41 entradas
- **source_of_metadata**: corpus, líneas 12/21/145/341/354; contraste con `Data/referencias.md` [1]–[41]
- **Metadata status**: **(metadata incomplete)** — fecha de corte y URL de cada anuario no declaradas

#### P002 — Gaceta Oficial 65/2026

- **Authors**: Gaceta Oficial de la República de Cuba (publicación oficial)
- **Year**: 2026 (número 65)
- **Venue**: Gaceta Oficial (diario oficial)
- **Citations**: no aplica
- **URL**: no declarada en el corpus → **(metadata incomplete: URL de la edición 65/2026 no declarada ni verificable desde el corpus)**
- **Layer**: L1
- **Cited in document**: yes — líneas 12, 71, 177, 293
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — el corpus afirma que no se publicó una resolución numerada nueva para la suspensión de CIMEX (línea 177), pero no enlaza la edición

#### P003 — BCC (Banco Central de Cuba)

- **Authors**: Banco Central de Cuba (organismo oficial)
- **Year**: sin año declarado
- **Venue**: sitio institucional (no declarado en el corpus)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete: sin URL ni documento concreto citado)**
- **Layer**: L1
- **Cited in document**: yes — líneas 12 y 71 (agrupado con ONEI y Gaceta Oficial)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P004 — elTOQUE (TRMI informal)

- **Authors**: elTOQUE (plataforma de medios/tipo de cambio)
- **Year**: 18/11/2026 (fecha de vigencia de la TRMI); «noviembre 2026» en la línea 242
- **Venue**: elTOQUE (publicación en línea)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete: URL de la publicación de la TRMI no verificable desde el corpus)**
- **Layer**: L1
- **Cited in document**: yes — líneas 73, 114, 242 (930 CUP/USD, 1.000 CUP/EUR, 845,35 CUP/MLC)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`. Temáticamente cercana a [29] Vidal Alejandro et al. (2024), que sí está en el anexo pero no es citada aquí
- **Metadata status**: **(metadata incomplete)** — el propio corpus advierte que el sitio «no responde de forma estable» (línea 114)

#### P005 — CIMEX S.A. y plataforma Ticket

- **Authors**: Corporación CIMEX S.A. (empresa estatal)
- **Year**: 2026 (medidas del 07/02/2026 y Circular 03/2026)
- **Venue**: disposición administrativa (no publicada en Gaceta Oficial según el corpus)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 177, 179, 245, 265
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — sin enlace a comunicado ni a la Circular Especial 03/2026

#### P006 — Ministerio de Economía y Planificación (MEP)

- **Authors**: Ministerio de Economía y Planificación (organismo oficial); se menciona al viceministro Oscar Pérez-Oliva Fraga
- **Year**: 2026
- **Venue**: respaldo institucional declarado en el corpus
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 177
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — mención nominal, sin documento de respaldo enlazado

#### P007 — Ministerio de Finanzas y Precios (MFP)

- **Authors**: Ministerio de Finanzas y Precios (organismo oficial)
- **Year**: nota del 12/05/2026
- **Venue**: nota ministerial (no enlazada)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 179
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P008 — Gobierno de Cuba / autorización a actores no estatales

- **Authors**: Gobierno de Cuba (disposición general)
- **Year**: 15/02/2026
- **Venue**: medida gubernamental declarada en el corpus
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 179
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — sin resolución numerada asociada en el texto

### Cluster 2 — Normativa y disposiciones regulatorias

**Query**: `instrumentos normativos citados en el corpus` ∩ `Data/referencias.md` — búsqueda por número de decreto/resolución/acuerdo/circular en los 8 archivos.

El corpus enumera instrumentos legales con identificador propio pero sin enlace a la Gaceta Oficial ni metadatos de publicación. Ninguno está en `Data/referencias.md`.

#### P009 — Acuerdo 9811 de 2024 del Consejo de Ministros

- **Authors**: Consejo de Ministros de Cuba
- **Year**: 2024
- **Venue**: Acuerdo del Consejo de Ministros
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete: texto del acuerdo no verificable desde el corpus)**
- **Layer**: L1
- **Cited in document**: yes — línea 177 (marco de precios de combustibles vigente hasta el 07/02/2026)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P010 — Decreto 163/2026

- **Authors**: Estado cubano (órgano emisor no precisado en el corpus)
- **Year**: 2026
- **Venue**: Decreto-ley / decreto (no se especifica)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 112, 197, 245, 610, 618, 624
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — el corpus atribuye la apertura a 17 empresas autorizadas sin citar el texto normativo

#### P011 — Resoluciones 104, 17, 52 y 102/2026

- **Authors**: Estado cubano (órgano emisor no precisado en el corpus)
- **Year**: 2026 (según el sufijo declarado)
- **Venue**: resoluciones (sin Gaceta identificada)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 112
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — números sueltos, sin título ni fecha de publicación

#### P012 — Resoluciones 171–175 y 340 (derogó la 312)

- **Authors**: Estado cubano (órgano emisor no precisado en el corpus)
- **Year**: 2026 (según el contexto de la línea 245)
- **Venue**: resoluciones referenciales, fiscales y aduaneras
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 112 y 245
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P013 — Circular Especial 03/2026 de CIMEX

- **Authors**: CIMEX S.A.
- **Year**: 2026
- **Venue**: circular especial (disposición interna)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 179
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

### Cluster 3 — Proyectos y repositorios de referencia externa

**Query**: `repositorios y análisis de referencia citados en el corpus` ∩ `Data/referencias.md` — búsqueda por nombre de proyecto en los 8 archivos y en el anexo.

El corpus invoca proyectos externos como referencia de arquitectura o como fuente de datos. Son repositorios, no publicaciones arbitradas; ninguno figura en `Data/referencias.md`.

#### P014 — Egyptian-Used-Cars

- **Authors**: proyecto `Egyptian-Used-Cars` (autoría no declarada en el corpus)
- **Year**: sin año declarado
- **Venue**: repositorio de código / análisis de mercado (no se indica plataforma ni URL)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete: repositorio no enlazado; imposible verificar autoría, licencia o fecha desde el corpus)**
- **Layer**: L1
- **Cited in document**: yes — línea 277 («uno de los análisis de mercado automotriz más completos que tenemos: 23.500 anuncios, historial mensual de precios, econometría, SQL, Tableau y Power BI»)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — cifra de 23.500 anuncios no contrastable con el anexo

#### P015 — Repos ICD

- **Authors**: ICD (Instituto de Cibernética y Computación; denominación ampliada no declarada en el corpus)
- **Year**: sin año declarado
- **Venue**: repositorio de datos citado como fuente
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 70 (3.958 anuncios ICD) y 57
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — sigla sin desglosar ni enlace

#### P016 — AutosxCuba

- **Authors**: AutosxCuba (proyecto/repositorio)
- **Year**: sin año declarado
- **Venue**: repositorio de datos citado como fuente
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 70
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P017 — Mercado-automotriz

- **Authors**: Mercado-automotriz (proyecto/repositorio)
- **Year**: sin año declarado
- **Venue**: repositorio de datos citado como fuente
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 70
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — agrupado bajo «y otros», sin inventario individual

### Cluster 4 — Directorios, geoservicios y herramientas de adquisición

**Query**: `servicios externos citados en el corpus` ∩ `Data/referencias.md` — búsqueda de nombres de directorios, geocodificadores y librerías anti-bot en los 8 archivos.

El corpus atribuye la procedencia de capas del mapa a servicios y librerías. Son fuentes de datos y herramientas, no obras académicas; ninguna está en `Data/referencias.md`.

#### P018 — Circuitos Habana

- **Authors**: aplicación cubana (autoría no declarada)
- **Year**: sin año declarado
- **Venue**: aplicación que reproduce mensajes públicos de la Empresa Eléctrica
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 248 y 307
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P019 — Empresa Eléctrica (reportes de prensa sobre circuitos)

- **Authors**: Empresa Eléctrica (organismo) / prensa (sin medio identificado)
- **Year**: sin año declarado
- **Venue**: «reportes de prensa» genéricos
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete: ningún reporte puntual identificado)**
- **Layer**: L1
- **Cited in document**: yes — línea 181 («según reportes de prensa ha dejado circuitos con más de 60 horas sin electricidad»)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — afirmación cuantitativa sin fuente verificable en el corpus ni en el anexo

#### P020 — KargalaYa

- **Authors**: KargalaYa (directorio de carga)
- **Year**: sin año declarado
- **Venue**: directorio en línea
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 266 y 807 (como «Kargalaya»)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — denominación inconsistente entre archivos (`KargalaYa` / `Kargalaya`)

#### P021 — ChargeFinder

- **Authors**: ChargeFinder (directorio de carga)
- **Year**: sin año declarado
- **Venue**: directorio en línea
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 266
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P022 — Electromaps

- **Authors**: Electromaps (directorio de carga)
- **Year**: sin año declarado
- **Venue**: directorio en línea
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 266 y 807
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P023 — OpenStreetMap / Overpass

- **Authors**: OpenStreetMap contributors / Overpass API (comunidad y servicio)
- **Year**: sin año declarado
- **Venue**: fuente abierta de geodatos (API Overpass)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete: el corpus nombra el servicio pero no enlaza la consulta ni la licencia)**
- **Layer**: L1
- **Cited in document**: yes — línea 806 (capa `gasolinera`)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P024 — Nominatim / Photon

- **Authors**: OpenStreetMap Nominatim / Komoot Photon (servicios de geocodificación)
- **Year**: sin año declarado
- **Venue**: servicios de geocodificación
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 828 (`geocode_elementos.py`)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P025 — Yellocu

- **Authors**: Yellocu (directorio)
- **Year**: sin año declarado
- **Venue**: directorio web
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 808 (capa `concesionario`)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P026 — Cybo

- **Authors**: Cybo (directorio)
- **Year**: sin año declarado
- **Venue**: directorio web (devuelve 403 / verificación de seguridad según el corpus)
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 808 y 833
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P027 — Cubisima / NearPlace / Páginas Amarillas / tallermanolito.com

- **Authors**: cuatro directorios y un sitio de taller (agrupados en el corpus)
- **Year**: sin año declarado
- **Venue**: fuentes de la capa `taller`
- **Citations**: no aplica
- **URL**: solo `tallermanolito.com` aparece como dominio; los demás sin enlace → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — línea 809 (y Cubisima además en la línea 67 como marketplace)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — agrupación sin ficha individual

#### P028 — FlareSolverr / curl_cffi / patchright

- **Authors**: proyectos de software (autoría no declarada en el corpus)
- **Year**: sin año declarado
- **Venue**: librerías y servicio local (`http://127.0.0.1:8191/v1`)
- **Citations**: no aplica
- **URL**: solo la URL local de FlareSolverr → **(metadata incomplete: repositorios y versiones no declarados)**
- **Layer**: L1
- **Cited in document**: yes — línea 833 (y `curl_cffi`/`patchright` en la misma línea)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`. Temáticamente cercano a [21] Krotov et al. y [22] Brown et al., ausentes del corpus
- **Metadata status**: **(metadata incomplete)**

### Cluster 5 — Métodos estadísticos invocados sin cita formal

**Query**: `métodos declarados en MODELOS_Y_FUNCIONES.md` ∩ `Data/referencias.md` — búsqueda de modelo hedónico, Kruskal-Wallis, VIF y Welch en los 8 archivos y en el anexo.

El corpus describe y justifica métodos con rigor metodológico, pero **no los atribuye a ninguna obra**. En `Data/referencias.md` existen antecedentes temáticos ([12] Hulten 2003, [13] Francke & Van de Minne 2020, [9] Du et al. 2026), ninguno citado en el corpus.

#### P029 — Modelo hedónico log-lineal (OLS)

- **Authors**: no atribuido (implementado en `Data/analisis_rentabilidad/04_stats.py`)
- **Year**: sin año de referencia bibliográfica
- **Venue**: `MODELOS_Y_FUNCIONES.md` §3.1
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete: sin obra de respaldo citada)**
- **Layer**: L1
- **Cited in document**: yes — líneas 433, 446, 449–452
- **Document reference**: ninguno; antecedente posible [12] y [13] en `Data/referencias.md`, sin marcador en el corpus
- **source_of_metadata**: corpus; contraste con `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)** — justificación metodológica sí, atribución bibliográfica no

#### P030 — Kruskal-Wallis

- **Authors**: no atribuido
- **Year**: sin año de referencia bibliográfica
- **Venue**: `MODELOS_Y_FUNCIONES.md` §3.3
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 414 y 460–464 (H = 25,741; p = 1e−05)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P031 — VIF (factor de inflación de varianza)

- **Authors**: no atribuido
- **Year**: sin año de referencia bibliográfica
- **Venue**: `MODELOS_Y_FUNCIONES.md` §3.2
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 454–458 (rango 1,13–1,58)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

#### P032 — Welch t-test

- **Authors**: no atribuido
- **Year**: sin año de referencia bibliográfica
- **Venue**: `MODELOS_Y_FUNCIONES.md` §3.4
- **Citations**: no aplica
- **URL**: no declarada → **(metadata incomplete)**
- **Layer**: L1
- **Cited in document**: yes — líneas 466–470 (codificado, no ejecutado)
- **Document reference**: ninguno
- **source_of_metadata**: corpus; ausente de `Data/referencias.md`
- **Metadata status**: **(metadata incomplete)**

## Cotejo con las 41 entradas de `Data/referencias.md`

Convención: `Citada en el informe` reproduce el flag del anexo (que alude al informe técnico de la pasada 1, **no** a este corpus); `Citada en el corpus` es el resultado de la búsqueda literal de autor/título/DOI en los 8 archivos. Las 41 entradas dan **cero coincidencias** con el corpus. No hay marcadores `[N]`, DOI ni arXiv en ninguno de los 8 archivos (verificado por búsqueda literal en el texto cacheado).

| Entrada | Obra / fuente (abreviada) | Año | `Citada en el informe` | `Citada en el corpus` | Nota |
|---|---|---:|---|---|---|
| [1] | Akerlof — *The Market for "Lemons"* | 1970 | sí | **no** | **(metadata incomplete: resumen indexado no sustantivo; identidad y DOI verificados en OpenAlex)** |
| [2] | Lewis — *Asymmetric Information… eBay Motors* | 2011 | no | **no** | Nota de discrepancia de año (SSRN 2010 / AER 2011) |
| [3] | Peterson & Schneider — *Adverse selection… CEX* | 2014 | no | **no** | — |
| [4] | Englmaier et al. — *Price Discontinuities* | 2017 | no | **no** | — |
| [5] | Che et al. — *Warranty, Seller Reputation…* | 2019 | no | **no** | — |
| [6] | Wolf & Muhanna — *Adverse Selection and Reputation* | 2005 | no | **no** | — |
| [7] | Sultan — *A model of the used car market…* | 2009 | no | **no** | — |
| [8] | Tilles et al. — *A Markovian model market* | 2011 | no | **no** | — |
| [9] | Du et al. — *Nonlinear Depreciation…* | 2026 | sí (§71.6, §71.14) | **no** | Solapamiento temático con la §4 del storytelling (depreciación) |
| [10] | Kang & Fu — *pricing of used electric vehicles* | 2026 | no | **no** | **(metadata incomplete: resumen no indexado; campos bibliográficos verificados)** |
| [11] | Miranda et al. — *Depreciation Patterns in UAE* | 2026 | no | **no** | — |
| [12] | Hulten — *Price Hedonics: A Critical Review* | 2003 | no | **no** | **(metadata incomplete: PDF no extraído)**; antecedente natural de P029 |
| [13] | Francke & Van de Minne — *unobserved heterogeneity* | 2020 | no | **no** | Antecedente natural de P029 |
| [14] | Gegić et al. — *Car Price Prediction using ML* | 2019 | sí (§71.6, §71.14) | **no** | — |
| [15] | Mutİ & Yıldız — *Using Linear Regression…* | 2023 | no | **no** | — |
| [16] | Jin — *Price Prediction of Used Cars* | 2021 | no | **no** | — |
| [17] | Ahtesham & Zulfiqar — *Used Car Price Prediction with Pyspark* | 2022 | no | **no** | — |
| [18] | Madhusudhanan et al. — *ProbSAINT* | 2024 | sí (§71.14) | **no** | 13 citas verificadas el 27/11/2026 |
| [19] | Pal et al. — *How much is my car worth?* | 2017 | no | **no** | Nota de discrepancia de año (preprint 2017 / publicación 2018) |
| [20] | Arefin — *Second Hand Price Prediction for Tesla* | 2021 | no | **no** | 9 citas verificadas el 27/11/2026 |
| [21] | Krotov et al. — *Legality and Ethics of Web Scraping* | 2020 | no | **no** | Solapamiento temático con la línea 112 (términos de uso) y P028 |
| [22] | Brown et al. — *Web scraping for research* | 2025 | no | **no** | Solapamiento temático con la línea 112 y P028 |
| [23] | Priestley et al. — *Data Quality Requirements… ML* | 2023 | no | **no** | Solapamiento con AUTOMATIZACION.md §4 |
| [24] | Hohensinner et al. — *Tracing the Data Trail* | 2026 | no | **no** | Solapamiento con AUTOMATIZACION.md §5 |
| [25] | Wenger et al. — *Data Isotopes for Data Provenance* | 2024 | no | **no** | — |
| [26] | Muça et al. — *Pipeline… Albania* | 2026 | sí (§71.6, §71.14) | **no** | — |
| [27] | Essien et al. — *Ethics of Web Scraping In Research* | 2023 | no | **no** | — |
| [28] | Paige — *Legality and Ethics… Archaeology* | 2024 | no | **no** | — |
| [29] | Vidal Alejandro et al. — *AI in the informal currency market: Cuba* | 2024 | sí (§71.6, §71.14) | **no** | Solapamiento directo con P004 (TRMI informal) |
| [30] | Castro Fernández et al. — *Electromobility and Energy Transition in Cuba* | 2024 | no | **no** | Solapamiento con §§2, 5 y 6 del storytelling |
| [31] | Ritter — *Cuba's Underground Economy* | 2004 | no | **no** | — |
| [32] | Ávila Castellanos — *Currency exchange in post-ordenamiento Cuba* | 2024 | no | **no** | Solapamiento con P004 |
| [33] | Guerra — *geography of car ownership in Mexico City* | 2015 | no | **no** | — |
| [34] | Klein et al. — *Transitions into and out of Car Ownership* | 2023 | no | **no** | — |
| [35] | Srisan et al. — *Auto insurance affordability…* | 2026 | no | **no** | — |
| [36] | Holtz et al. — *Reducing Interference Bias…* | 2020 | no | **no** | — |
| [37] | Etro — *Product Selection in Online Marketplaces* | 2020 | no | **no** | — |
| [38] | Quariguasi Frota Neto et al. — *Market prices… eBay* | 2015 | no | **no** | Nota de discrepancia de año (2015 OpenAlex / 2016 Crossref) |
| [39] | DfT / DVLA — *Vehicle statistics* (GOV.UK) | sin año | campo ausente | **no** | **(metadata incomplete: URL profunda no confirmada)**; fuente institucional foránea, ausente del corpus |
| [40] | ANFAC — *Informes del sector automotriz español* | sin año | sí (institucional §70) | **no** | Fuente institucional foránea, ausente del corpus |
| [41] | AEADE — *Estadísticas de matriculaciones* | sin año | sí (institucional §70) | **no** | Fuente institucional foránea, ausente del corpus |

Cuatro entradas del anexo llevan `(metadata incomplete)` —[1], [10], [12] y [39]— y tres registran discrepancias de año —[2], [19] y [38]—. Esas marcas se conservan tal cual; las 37 fuentes del corpus inventariadas arriba se marcan todas `(metadata incomplete)` porque el corpus no da metadatos verificables y el anexo no las contiene.

## Recency distribution

Convenio: «In map» cuenta los 37 IDs `P001`–`P037`; «In document bibliography» cuenta las 41 entradas de `Data/referencias.md` (38 con año; [39]–[41] sin año). La fila «Rango 2014–2025» corresponde a ONEI (P001), que declara un intervalo y no un año único. Los años del mapa son los declarados en el propio corpus o heredados de las obras ausentes propuestas en «Likely missing».

| Year | In map | In document bibliography |
|---|---:|---:|
| 2026 | 6 | 6 |
| 2025 | 1 | 1 |
| 2024 | 3 | 6 |
| 2023 | 0 | 4 |
| 2022 | 0 | 1 |
| ≤2021 | 2 | 20 |
| Rango 2014–2025 (ONEI) | 1 | 0 |
| Sin año verificable | 24 | 3 |

Las seis entradas 2026 del mapa son [P002] Gaceta Oficial 65/2026, [P004] elTOQUE (18/11/2026), [P010] Decreto 163/2026, [P011] resoluciones /2026, [P012] resoluciones 171–175 y 340 y [P013] Circular 03/2026; la de 2024 es [P009] Acuerdo 9811; la de 2025 es [P036] Brown et al.; las de ≤2021 son [P035] Krotov et al. (2020) y [P037] Hulten (2003).

## Venue distribution

| Venue | Count in map |
|---|---:|
| Instituciones y organismos cubanos (ONEI, Gaceta, BCC, elTOQUE, CIMEX, MEP, MFP, Gobierno) | 8 |
| Instrumentos normativos (acuerdo, decreto, resoluciones, circular) | 5 |
| Repositorios y proyectos de referencia | 4 |
| Directorios, geoservicios y herramientas de adquisición | 11 |
| Métodos estadísticos sin atribución bibliográfica | 4 |
| Revistas / congresos del anexo (obras temáticamente cercanas, no citadas) | 5 |

## Likely missing important works

Criterio adaptado: se listan obras de `Data/referencias.md` que, por solapamiento directo con una afirmación load-bearing del corpus, deberían plausiblemente citarse en la documentación de usuario y no lo están. No se proponen obras nuevas porque no se ejecutaron búsquedas.

### P033 — Using AI in the informal currency market: evidence from Cuba

- Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A. (2024), *Applied Economics*; [29] en `Data/referencias.md`, `Citada en el informe: sí`.
- **Cluster**: Fuentes institucionales y estadísticas cubanas.
- **Why likely missing**: el corpus hace de la TRMI informal (930 CUP/USD, línea 242) una de las «cuatro fuerzas invisibles» y la usa para convertir todos los precios (línea 73); [29] estudia exactamente ese mercado informal de divisas en Cuba y ya está verificada en el anexo, pero no aparece en ninguno de los 8 archivos.

### P034 — Electromobility and Energy Transition in Cuba

- Castro Fernández, M.; Vilaragut Llanes, M.; Hernández, J. C. (2024), *Sustainability*; [30] en `Data/referencias.md`, `Citada en el informe: no`.
- **Cluster**: Métodos y contexto del storytelling.
- **Why likely missing**: las secciones 2, 5 y 6 del storytelling sostienen afirmaciones sobre electrolineras, coste de propiedad eléctrica y red de carga (11 estaciones solares Dongfeng/NWI y 21 de CIMEX+MITRANS, línea 265) sin respaldo bibliográfico; [30] es el antecedente cubano directo.

### P035 — Legality and Ethics of Web Scraping

- Krotov, V.; Johnson, L.; Silva, L. (2020), *Communications of the Association for Information Systems*; [21] en `Data/referencias.md`, `Citada en el informe: no`.
- **Cluster**: Directorios, geoservicios y herramientas de adquisición.
- **Why likely missing**: la línea 112 afirma que el proyecto «respeta los términos de uso de los portales: no elude mecanismos anti-automatización», mientras la línea 833 describe impersonación de Chrome/Safari, `patchright` y FlareSolverr para esquivar 403; [21] es un marco de referencia estándar para esa tensión y está en el anexo sin citar en el corpus.

### P036 — Web scraping for research: Legal, ethical, institutional, and scientific considerations

- Brown, M. A.; Gruen, A.; Maldoff, G.; Messing, S.; Sanderson, Z.; Zimmer, M. T. (2025), *Big Data & Society*; [22] en `Data/referencias.md`, `Citada en el informe: no`.
- **Cluster**: Directorios, geoservicios y herramientas de adquisición.
- **Why likely missing**: misma razón que P035 y además es la obra más reciente (2025) del subárea; el corpus de documentación es la cara pública del proyecto y no registra ninguno de los dos marcos éticos.

### P037 — Price Hedonics: A Critical Review

- Hulten, C. R. (2003), *Federal Reserve Bank of New York Economic Policy Review*; [12] en `Data/referencias.md`, `Citada en el informe: no`, `(metadata incomplete: PDF no extraído)`.
- **Cluster**: Métodos estadísticos invocados sin cita formal.
- **Why likely missing**: `MODELOS_Y_FUNCIONES.md` §3.1 dedica varios párrafos a justificar el modelo hedónico log-lineal (líneas 433–452) y declara explícitamente que «los atributos hedónicos… son los determinantes estándar» (línea 446) sin citar la revisión crítica canónica. La marca `(metadata incomplete)` se hereda del anexo: el PDF no fue extraído en la verificación del 27/11/2026.

## Hypothesis checks (from plan)

El plan no declara hipótesis; las cuatro siguientes se derivan del mandato recibido y son observaciones sin veredicto.

### H1 — Los trabajos académicos citados en el corpus coinciden con las 41 entradas de `Data/referencias.md` (derivada)

Estado de la evidencia: **no hay coincidencia alguna**. La búsqueda literal de los 41 apellidos/títulos en el texto cacheado da cero resultados (los únicos aciertos parciales de cadena —«Che,», «Pal,», «Etro»— resultaron ser falsos positivos dentro de «Chevrolet», «página» y «película»). Tampoco hay marcadores `[N]`, DOI ni `arXiv` en los 8 archivos. Las única menciones de tipo metodológico son «Kruskal-Wallis» y «modelo hedónico», sin atribución. El anexo y el corpus describen, por tanto, dos regímenes de citas distintos: el anexo documenta la literatura del informe técnico; el corpus documenta el proyecto para el usuario.

### H2 — Las fuentes institucionales del corpus están representadas en el bloque [39]–[41] del anexo (derivada)

Estado de la evidencia: **no**. El corpus cita organismos cubanos (ONEI, Gaceta Oficial, BCC, CIMEX, MEP, MFP, Consejo de Ministros, Gobierno) y disposiciones cubanas (Decreto 163/2026, resoluciones 104/17/52/102/2026, 171–175, 340, Acuerdo 9811/2024, Circular 03/2026). El bloque institucional del anexo son tres fuentes foráneas —DfT/DVLA (GOV.UK), ANFAC y AEADE— vinculadas al informe técnico (§§18 y 70) y ausentes del corpus. No hay ni un solo nombre compartido entre ambos conjuntos. [39] además arrastra `(metadata incomplete: URL profunda no confirmada)` y carece del campo `Citada en el informe`.

### H3 — Toda fuente citada en el corpus tiene metadatos verificables (derivada)

Estado de la evidencia: **no; 37 de 37 lo tienen marcado `(metadata incomplete)` en este mapa**. Ninguna de las fuentes del corpus aporta DOI, arXiv, URL de destino y año de publicación a la vez. Solo se verifican localmente identificadores internos —Decreto 163/2026, Gaceta Oficial 65/2026, Acuerdo 9811/2024, Circular 03/2026, TRMI del 18/11/2026— y la URL local de FlareSolverr; ninguno de ellos permite resolver la ficha bibliográfica. El corpus declara explícitamente una limitación de verificabilidad en la línea 114 (elTOQUE «no responde de forma estable») y en la línea 181 («según reportes de prensa» sin medio identificado), coherente con la marca.

### H4 — Los métodos declarados en el corpus están respaldados por bibliografía identificable (derivada)

Estado de la evidencia: **respaldados en el anexo, no en el corpus**. `MODELOS_Y_FUNCIONES.md` justifica el modelo hedónico, VIF, Kruskal-Wallis y Welch con argumentos estadísticos correctos (líneas 433–470), pero sin remitir a obra alguna. En `Data/referencias.md` sí existen [12] Hulten (revisión crítica de precios hedónicos, `(metadata incomplete)`), [13] Francke & Van de Minne (heterogeneidad no observada) y [9] Du et al. (depreciación no lineal y heterogeneidad de marca), todos con `Citada en el informe: no` y ninguno citado en el corpus. La consecuencia observable es una documentación metodológicamente argumentada pero bibliográficamente muda en su cara pública.

## Sources used

- WebSearch queries: 0 (cotejo dirigido; sin búsquedas temáticas nuevas).
- WebFetch URLs: 0; no se re-fetcharon GOV.UK, anfac.com, aeade.net ni ninguna URL del corpus.
- Semantic Scholar API hits: 0.
- OpenAlex API hits: 0 nuevos; los metadatos, conteos de citas y marcas `(metadata incomplete)` se heredan de la verificación del 27/11/2026 consignada en `Data/referencias.md`.
- Archivos locales inspeccionados: `reviews/corpus-documentacion-2026-11-28.plan.md` (24 líneas); `.playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md` (833 líneas; inventario completo de 8 archivos); `Data/referencias.md` (41 entradas, líneas 1–87); `reviews/informe-tecnico-2026-11-28-iter4.e2-literature.md` (convención de formato y tratamiento de `[39]`–`[41]`).
- Degradación: `degraded: false` para el mandato recibido —las 41 entradas, los marcadores `[N]`/DOI/arXiv y las 37 fuentes del corpus quedaron resueltos por inspección directa—. Limitación declarada: sin búsqueda bibliográfica nueva, sin lectura de resúmenes y sin re-fetch de URLs; este mapa sirve para el cotejo de citas entre el corpus y el anexo, no para proponer obras externas nuevas ni para certificar enlaces institucionales.


## Apéndice D — Artefactos

# Artifact Inventory

Corpus auditado: 8 archivos unificados en `.playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md` (833 líneas). Todas las verificaciones de existencia se hicieron sobre el checkout local `/home/thony70807/Proyectos/El precio de moverse en Cuba`. Las referencias de línea (`L…`) son del texto cacheado.

## Repository

- **URL**: https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba.git
- **Clone status**: success (checkout local con historial completo y remoto `origin`)
- **Languages**: Python 10.861 LOC / 59 archivos propios (excluye venv, `Copias/`, `Auxiliares/herramientas/integraciones/` y repos de referencia); Markdown 30.157 LOC / 165 archivos; Shell 189 LOC
- **Commits**: 194
- **Authors**: CarlosAntonioAceaJimenezCD <CarlosAntonioAceaJimenezCD@users.noreply.github.com>
- **First commit**: 2026-11-17
- **Last commit**: 2026-11-28
- **Default branch**: `main`

### Structure

```tree
.
├── README.md, requirements.txt, mkdocs.yml
├── INFORME_TECNICO.md / .pdf
├── Data/
│   ├── Revolico/            # sqlite, chunks/, pipeline_chunks/, partes/
│   ├── analisis_rentabilidad/
│   │   ├── scripts/         # 01…05 + 03b/03c + run_all.py
│   │   ├── data/            # listings_clean.parquet, compacto/
│   │   └── outputs/         # tables/ (21 CSV/TXT), charts/ (6 HTML)
│   ├── fuentes-oficiales/ONEI/  # 12 anuarios, 234 archivos
│   ├── mapas/, catalogos_concesionarios/, CRUDO_POR_CATEGORIA/
│   ├── repos-autos-referencias/ (referencias_autos.sqlite, 25 tablas)
│   ├── _state/, _estado/, auditoria/, dashboard.html
│   └── AUTOMATIZACION.md, ESTRUCTURA_ESPACIO.md, DICCIONARIO.md (ausente)
├── Auxiliares/
│   ├── herramientas/        # scrape, chunking, dashboard, mkdocs, tests
│   ├── .venv-py/            # entorno en uso (no versionado)
│   └── Repositorios Referencias/  # no versionado
├── docs/                    # fuentes MkDocs (26 .md + 6 gráficos + dashboard)
├── site/                    # sitio generado (ignorado por Git)
├── reviews/                 # auditorías de la skill /review
├── Copias/, Hombros/, Anexos/  # referencias y corpus (parcialmente no versionado)
└── .gitignore, .gitattributes, .playground/ (caché de auditoría)
```

### Entry points

| Path | LOC | Args documented | Notes |
|---|---|---|---|
| `Data/analisis_rentabilidad/scripts/run_all.py` | 49 | yes | Quickstart del README (L31) |
| `Data/analisis_rentabilidad/scripts/01_ingest.py` … `05_benchmark.py` | ~490 | no | Fases INGESTA/LIMPIEZA/EDA/STATS/BENCHMARK |
| `Auxiliares/herramientas/db_chunks.py` | 195 | yes | `verify` / `assemble` (L87–88) |
| `Auxiliares/herramientas/generar_sitio_mkdocs.py` | 283 | yes | Genera `site/` desde `docs/` (L96) |
| `Auxiliares/herramientas/generar_dashboard.py` | 590 | yes | Genera el panel autocontenido (L659) |
| `Auxiliares/herramientas/actualizar_numeros.py` | 220 | yes | Marcadores `<!-- kpi:* -->`, modo `--check` (L663) |
| `Auxiliares/herramientas/generar_mapa_ofline.py` | 106 | yes | `--tipos`, `--out` (L815–817) |
| `Data/_state/run_step.sh` | 31 | yes | Envoltorio `flock`/`timeout` con estado atómico (L667) |
| `Data/_state/job_{circuitos,calidad,salud,analisis,sitio}.sh` | ~90 | no | Wrappers de los timers (L705) |

### Tests

- Files: `Auxiliares/herramientas/test_dashboard.py`, `test_parquet_compacto.py`, `test_modelo.py`, `test_smoke_pipeline.py`, `Auxiliares/herramientas/probar_actualizar_numeros.py`
- Total LOC: 327 (sin contar `probar_actualizar_numeros.py`, script de regresión)
- Framework: scripts (no hay `pytest.ini` ni `conftest.py` propios)
- Tests cover (named): panel/dashboard, Parquet compacto, modelo econométrico, smoke del pipeline, actualización de KPIs

### Documentation

| File | LOC |
|---|---|
| README.md | 116 |
| INFORME_TECNICO.md | ~3.000 |
| docs/ (26 .md) | 2.577 |
| Data/analisis_rentabilidad/ (9 .md) | ~1.000 |
| reviews/ | ~12.000 (auditorías previas y plan) |

### Environment

- requirements.txt: present, 14 líneas (11 dependencias fijadas: pandas, numpy, plotly, statsmodels, scipy, bs4, curl_cffi, tenacity, trafilatura, pyarrow, mkdocs + material)
- pyproject.toml: absent
- environment.yml: absent
- Dockerfile: absent
- Other: `mkdocs.yml` (1.700 B), `.gitattributes` (Git LFS para SQLite y `.bin`), `.gitignore` (excluye `site/`, `outputs/`, `Auxiliares/.venv-py`, `Copias/`), `Auxiliares/.venv-py/` presente (Python 3.14), `Auxiliares/.venv/` ausente

### Heavy artifacts in repo

| Path | Size | Type |
|---|---|---|
| `Data/Revolico/revolico.sqlite` | 839 MB | sqlite (no versionado; LFS vía chunks) |
| `Data/Revolico/chunks/` | 811 MB | 82 × `.bin` de 10 MiB + `MANIFEST.json` + README |
| `Data/Revolico/pipeline.sqlite` | 755 MB | sqlite (no versionado) |
| `Data/Revolico/pipeline_chunks/` | 518 MB | 52 × `.bin` de 10 MiB + `MANIFEST.json` |
| `Data/Revolico/partes/` | 759 MB | 48 fragmentos (copia anterior) |
| `Data/fuentes-oficiales/ONEI/` | — | 12 anuarios, 234 archivos PDF/XLS |
| `INFORME_TECNICO.pdf` | 972 KB | pdf |
| `Data/dashboard.html` | 109.929 B | html autocontenido (doc: 107 KB) |

## Datasets

| Name | Source | ID | Publicly accessible | Notes |
|---|---|---|---|---|
| Revolico (anuncios) | Revolico / scraping propio | `revolico.sqlite` | unknown | 10.379 anuncios, 974 autos (L19); 82 chunks verificados |
| Marketplaces (8 sitios) | Autocubana, iTENCEL, Cogetucarro, Cubisima, Timbirichi, Carros.com, Apululu, VentaCuba | `Data/catalogos_concesionarios/` | unknown | 2.232 anuncios (L12, L67, L211) |
| Concesionarios (11) | BDC One, Dongfeng, Changan, Chinautos, MCV, Finauto, ATR Export, … | `Data/catalogos_concesionarios/` | unknown | 256 vehículos (L12, L68) |
| Referencias externas | ICD, AutosxCuba, Mercado-automotriz | `referencias_autos.sqlite` | unknown | 25 tablas confirmadas (L19, L70) |
| ONEI 2014–2025 | ONEI | `Data/fuentes-oficiales/ONEI/` | yes | 12 anuarios presentes; 234 archivos en disco vs 233 declarados (L21) |
| Normativa | Gaceta Oficial, BCC, elTOQUE | `Anexos/Leyes/` | unknown | Decreto 163/2026, resoluciones, TRMI 930 CUP/USD (L73, L112) |
| Fuentes adicionales | Fuentes adicionales (2026-11-20) | `Data/fuentes-adicionales-2026-11-20.md` | unknown | Documento de auditoría de fuentes (L107) |
| Mapa de elementos | OSM/Overpass, Kargalaya, Electromaps, Yellocu, Cybo, NearPlace | `mapa_elementos.sqlite` | unknown | Tablas `tipos` y `elementos` (L799–803) |

## Tables

### Cuadro 1 — KPIs del mercado
- **Section**: Storytelling, «Anexo: cuadros y gráficos» (L313–332)
- **Lines**: 317–332
- **Columns**: Métrica, Valor
- **Rows**: 11
- **Claims supported** (preliminary): 2.174 anuncios limpios, 1.483 locales, 691 importación, mediana 21.000 USD, 50 marcas

### Cuadro 2 — Mercado local e importación
- **Section**: Storytelling, anexo (L333–340)
- **Lines**: 333–340
- **Columns**: Canal, Tipo, Anuncios, Mediana USD, Media USD
- **Rows**: 3
- **Claims supported** (preliminary): mediana importación 26.000 USD, media 27.046,22 USD

### Cuadro 3 — Pasajeros transportados (ONEI, millones)
- **Section**: Storytelling, anexo (L341–353)
- **Lines**: 341–353
- **Columns**: Año, Total, En ómnibus
- **Rows**: 8 (2014–2025)
- **Claims supported** (preliminary): 781,1 M en 2025, −59 % frente a 2019, 324,0 M en ómnibus

### Cuadro 4 — Seguridad vial (ONEI)
- **Section**: Storytelling, anexo (L354–363)
- **Lines**: 354–363
- **Columns**: Año, Accidentes, Fallecidos, Lesionados
- **Rows**: 5 (2021–2025)
- **Claims supported** (preliminary): 7.552 accidentes y 751 fallecidos en 2025

### Cuadro 5 — Modelo de depreciación (coeficientes vigentes)
- **Section**: Storytelling, anexo (L364–377)
- **Lines**: 364–377
- **Columns**: Término, Coeficiente, p_valor
- **Rows**: 8
- **Claims supported** (preliminary): «Ningún coeficiente resulta estadísticamente significativo» (L377); 22 observaciones de muestra

### Tablas sin numerar citadas en el corpus

| § / archivo | Líneas | Contenido |
|---|---|---|
| README «Fuentes de datos» | 65–71 | 5 grupos de fuentes y registros |
| README «Configuración» | 77–82 | `config.py`, `.gitattributes`, 2 MANIFEST |
| MODELOS_Y_FUNCIONES §1 | 405–416 | 10 reglas de preparación determinista |
| MODELOS_Y_FUNCIONES §2 | 420–429 | 8 medidas descriptivas |
| ARQUITECTURA_DATOS §2 | 518–527 | 7 motores de datos (DuckDB, Polars, Iceberg…) |
| ARQUITECTURA_DATOS §4 | 547–554 | 6 fases de migración |
| ALCANCE_Y_RETENCION §2 | 595–602 | 6 hitos de retención por cada 100 visitantes |
| AUTOMATIZACION §2 | 641–653 | 11 jobs y su periodicidad |
| AUTOMATIZACION §6b | 719–724 | 4 filas de ancho de banda estimado |
| mapas/README §Generar el mapa | 804–809 | 4 tipos de elemento y color |
| mapas/README §Scripts | 824–829 | 4 scripts del mapa |

Backing CSV/TXT identificado: `Data/analisis_rentabilidad/outputs/tables/` contiene 21 archivos, entre ellos los 6 citados por nombre (`kpis.csv`, `kpis_canal.csv`, `modelo_muestra.csv`, `modelo_resumen.txt`, `modelo_depreciacion.csv`, `rechazos.csv`). Falta `benchmark_result.csv` (ver Missing artifacts).

## Figures

### Gráfico 1 — Distribución de precios
- **Section**: Storytelling, «Gráficos» (L379–386)
- **Rendered in document**: no — solo enlace a `outputs/charts/01_precios.html` (L381)
- **Type**: histograma HTML/Plotly
- **Claims supported** (preliminary): distribución de precios (§3, L217)

### Gráfico 2 — Distribución por año
- **Section**: Storytelling, «Gráficos» (L382)
- **Rendered in document**: no — enlace a `outputs/charts/02_anios.html`
- **Type**: histograma HTML/Plotly
- **Claims supported** (preliminary): composición por año (§3, L217)

### Gráfico 3 — Top marcas
- **Section**: Storytelling, «Gráficos» (L383)
- **Rendered in document**: no — enlace a `outputs/charts/03_marcas.html`
- **Type**: bar chart HTML/Plotly
- **Claims supported** (preliminary): 50 marcas distintas

### Gráfico 4 — Precio por tier
- **Section**: Storytelling, «Gráficos» (L384)
- **Rendered in document**: no — enlace a `outputs/charts/04_tiers.html`
- **Type**: box plot HTML/Plotly
- **Claims supported** (preliminary): Kruskal-Wallis por `brand_tier`

### Gráfico 5 — Precio vs km
- **Section**: Storytelling, «Gráficos» (L385)
- **Rendered in document**: no — enlace a `outputs/charts/05_km_precio.html`
- **Type**: scatter HTML/Plotly
- **Claims supported** (preliminary): dispersión precio/kilometraje (§4, L233)

### Gráfico 6 — Precio vs antigüedad
- **Section**: Storytelling, «Gráficos» (L386)
- **Rendered in document**: no — enlace a `outputs/charts/06_edad_precio.html`
- **Type**: scatter HTML/Plotly
- **Claims supported** (preliminary): curva de valor / depreciación

Los 6 HTML existen en `Data/analisis_rentabilidad/outputs/charts/`, en `docs/graficos/` y en `site/graficos/`. El documento los anuncia como «apoyos» (L133) pero no los incrusta: `Rendered in document: no` para todos.

## Cited paths and artifacts

Verificación directa en el checkout. **Sí** = existe en disco; **Git** = versionado; **No** = ausente.

### Panel interactivo (autocontenido)

| Artifact citado | Sección (L) | Presente | Git | Observación |
|---|---|---|---|---|
| `generar_dashboard.py` → `Data/dashboard.html` | AUTOMATIZACION §2 (L659) | Sí | Sí | `Auxiliares/herramientas/generar_dashboard.py`; 109.929 B (~107 KB declarados) |
| `docs/dashboard.html` | L659 | Sí | Sí | Copia exacta (109.929 B), añadida al menú MkDocs |
| `site/dashboard.html` | L659 | Sí | No | Generado; `site/` ignorado por `.gitignore` |
| `Auxiliares/herramientas/test_dashboard.py` | L659 | Sí | Sí | Prueba del panel |
| `actualizar_numeros.py` / `probar_actualizar_numeros.py` | L663 | Sí | Sí | Ambos en `Auxiliares/herramientas/` |

### Tablas y gráficos

| Artifact citado | Sección (L) | Presente | Git | Observación |
|---|---|---|---|---|
| `outputs/tables/kpis.csv`, `kpis_canal.csv` | README L38–39 | Sí | No | 285 B y 155 B; `outputs/` ignorado |
| `outputs/tables/modelo_muestra.csv`, `modelo_resumen.txt`, `modelo_depreciacion.csv` | Storytelling L377; MODELOS L452 | Sí | No | 266 B, 2.621 B, 423 B |
| `outputs/tables/rechazos.csv` | MODELOS L416 | Sí | No | 2,3 MB (2.014+ filas) |
| `outputs/tables/benchmark_result.csv` | ARQUITECTURA L566 | **No** | — | Declarado como línea base «se guardará»; aún pendiente |
| `outputs/charts/01…06_*.html` | Storytelling L381–386 | Sí | No | 6/6 presentes (24–52 KB c/u) |

### Chunks y bases

| Artifact citado | Sección (L) | Presente | Git | Observación |
|---|---|---|---|---|
| `Data/Revolico/chunks/MANIFEST.json` | README L81, L87–88; AUTOMATIZACION L692 | Sí | Sí | 82 chunks declarados = 82 `.bin` presentes |
| `Data/Revolico/pipeline_chunks/MANIFEST.json` | README L82; L692 | Sí | Sí | 52 chunks declarados = 52 `.bin` presentes |
| `Data/Revolico/revolico.sqlite` | README L19, L84 | Sí | No | 839 MB; original no versionado, se reconstruye desde chunks |
| `Data/Revolico/pipeline.sqlite` | README L84 | Sí | No | 755 MB; ídem |
| `Data/Revolico/partes/` | ESTRUCTURA L757 | Sí | No | 48 fragmentos (copia anterior) |
| `Auxiliares/herramientas/db_chunks.py` | README L87–88 | Sí | Sí | Comandos `verify`/`assemble` disponibles |
| `Data/analisis_rentabilidad/data/compacto/` | ARQUITECTURA L501 | Sí | Sí | 7 Parquet particionados (`year=/month=`) |

### Sitio MkDocs

| Artifact citado | Sección (L) | Presente | Git | Observación |
|---|---|---|---|---|
| `mkdocs.yml` | README L101 | Sí | Sí | 1.700 B |
| `docs/` | L659 | Sí | Sí | 26 .md + 6 gráficos + dashboard |
| `site/` | README L101 | Sí | No | Generado: index, historia/, graficos/ (6), search/, dashboard.html, 404, sitemap |
| `Auxiliares/herramientas/generar_sitio_mkdocs.py` | README L96 | Sí | Sí | Presente |
| `sitio_build.sh` | L659 | Sí* | Sí | Ubicado en `Data/_state/sitio_build.sh`, no en la raíz |
| `Data/_state/job_sitio.sh` | L705 | Sí | Sí | Wrapper del timer semanal |

### Timers y salud operativa

| Artifact citado | Sección (L) | Presente | Estado observado |
|---|---|---|---|
| `precio-circuitos.{service,timer}` | L709 | Sí | `~/.config/systemd/user/`; timer activo «Diario 11:13 UTC» |
| `precio-calidad.{service,timer}` | L709 | Sí | Timer activo «Diario 09:17 UTC» |
| `precio-salud.{service,timer}` | L709 | Sí | Timer activo «Diario 09:30 UTC» |
| `precio-analisis.{service,timer}` | L709 | Sí | Timer activo «Semanal domingo 06:17 UTC» |
| `precio-sitio.{service,timer}` | L709 | Sí | Timer activo «Semanal domingo 07:17 UTC» |
| Timer de extracción cada 10 min | ARQUITECTURA L564 | Sí | `precio-revolico.timer` activo en `running`; servicio en `activating/start` |
| `loginctl enable-linger` (Linger=yes) | L672, L702, L715 | Sí | `loginctl show-user thony70807 -p Linger` → `Linger=yes` |
| `Data/_state/run_step.sh` | L667, L704 | Sí | 31 líneas, `flock` + `timeout` + estado atómico |
| `job_{circuitos,calidad,salud,analisis,sitio}.sh` | L705 | Sí | Los 5 en `Data/_state/` |
| `validar_calidad.py`, `salud.py` | L706–707 | Sí | En `Auxiliares/herramientas/` |
| `Data/_estado/salud.json`, `Data/auditoria/SALUD.md` | L681, L707 | Sí | Presentes |
| `alertas.jsonl` | L681, L689, L707 | Sí* | En `Data/_estado/alertas.jsonl`, no bajo `Data/auditoria/` |
| `Data/_state/watermarks.json` | L669, L689 | **No** | Ausente en disco |
| `_state/lfs_push_ledger.jsonl` | L671 | **No** | Ausente; L711 lo declara «pendiente (fase siguiente)» |

Nota de alcance: los timers viven fuera del checkout (`~/.config/systemd/user/`), en coherencia con un proyecto que documenta automatización del entorno local, no del repositorio.

## Missing artifacts

### `benchmark_result.csv` (línea base de rendimiento)
- **Mentioned in document**: §6 de `ARQUITECTURA_DATOS.md` (L566): «la línea base de rendimiento se guardará en `benchmark_result.csv` antes de tocar el pipeline»
- **Found in repo**: no
- **Observation**: El corpus describe la Fase 0 como «línea base documentada» y anuncia este CSV como depósito de la medición previa al cambio de pipeline. En `outputs/tables/` hay 21 archivos de resultados (KPIs, benchmarks de precios, anomalías, modelo) pero ningún `benchmark_result.csv`. El artefacto que debería sostener la comparación antes/después de DuckDB/Polars no está materializado en el checkout.

### Marcas de agua y ledger LFS
- **Mentioned in document**: §3 de `AUTOMATIZACION.md` (L669): «Marcas de agua en `Data/_state/watermarks.json`, escritas solo tras verificar la salida»; (L671): «LFS con ledger `_state/lfs_push_ledger.jsonl`: un objeto que falla 3 veces se cuarentena y alerta»
- **Found in repo**: no
- **Observation**: `Data/_state/` contiene `run_step.sh`, los cinco `job_*.sh` y `sitio_build.sh`, pero ni `watermarks.json` ni `lfs_push_ledger.jsonl`. El propio documento se contradice: mientras §3 los describe como mecanismos en funcionamiento, §6 (L711) los incluye en «Pendiente (fase siguiente): … ledger LFS y unificación de `chunks/` con `partes/`». En disco, `watermarks.json` no existe en ninguna ruta y `partes/` sigue separada de `chunks/`.

### Registro de ejecución y versiones
- **Mentioned in document**: §5 de `AUTOMATIZACION.md` (L687–688): «`manifiesto_ejecucion.jsonl`: una línea por corrida con commit, SHA de scripts, Python, entradas/salidas, filas, métricas de calidad y watermark antes/después» y «`VERSIONES.json`: dependencias y hash de `config.py`»
- **Found in repo**: no
- **Observation**: Ninguno de los dos archivos aparece en `Data/`, `Data/auditoria/` ni `Data/_estado/`. La auditoría a dos años que el corpus presenta como ya implementada («Se guarda, en UTC y con hashes») carece en el checkout de sus dos piezas de trazabilidad centrales: el manifiesto por corrida y el hash de dependencias/configuración.

### Snapshots inmutables y puntero `LATEST.json`
- **Mentioned in document**: §5 de `AUTOMATIZACION.md` (L690): «Un snapshot Parquet inmutable por semana (`snapshots/YYYY-Www/`) con puntero `LATEST.json`. 104 semanas ≈ 2 años»
- **Found in repo**: no
- **Observation**: Existe `Data/analisis_rentabilidad/data/compacto/` con 7 Parquet particionados por `year=/month=`, pero no hay directorio `Data/snapshots/`, ni semanas `YYYY-Www/`, ni `LATEST.json`. La «regla de oro» del documento («un snapshot se escribe una vez y nunca se sobrescribe; el estado actual es un puntero», L695) no tiene contrapartida material en el checkout.

### `DICCIONARIO.md` y `LIMITACIONES.md`
- **Mentioned in document**: §5 de `AUTOMATIZACION.md` (L693): «`DICCIONARIO.md` y `LIMITACIONES.md`: semántica de campos, URL de origen y límites conocidos»
- **Found in repo**: no
- **Observation**: Ninguno de los dos documentos está en `Data/` ni en la raíz. El corpus afirma que acompañan a los snapshots como semántica de campos y límites conocidos; en su ausencia, la interpretación de los CSV y Parquet queda apoyada solo en `MODELOS_Y_FUNCIONES.md` y en el informe técnico.

### `Data/mapas/mapa_talleres.html`
- **Mentioned in document**: `mapas/README.md` (L817): «`.venv/bin/python herramientas/generar_mapa_ofline.py --tipos concesionario,taller --out ../Data/mapas/mapa_talleres.html`»
- **Found in repo**: no
- **Observation**: El comando se presenta como ejemplo de generación, no como salida ya producida. En `Data/mapas/` sí están `mapa_elementos.sqlite` (116 KB), `mapa_ofline.html` (4,7 MB), `elementos_sin_coordenadas.csv` y `TIMELAPSE_CIRCUITOS.md`, pero falta la variante `mapa_talleres.html`. Es un artefacto generable, no una laguna de datos.

### Entorno `Auxiliares/.venv`
- **Mentioned in document**: `mapas/README.md` (L815–817): «`cd Auxiliares` · `.venv/bin/python herramientas/generar_mapa_ofline.py …`»
- **Found in repo**: no (sí `Auxiliares/.venv-py`)
- **Observation**: El README principal usa sistemáticamente `Auxiliares/.venv-py/bin/...` (L29–31, L96–98), mientras el README de mapas invoca `Auxiliares/.venv/bin/python`. Solo existe `.venv-py`; los comandos del README de mapas no resolverían tal como están escritos.

## Code-to-document mapping

| Document component | Repo location | Existence |
|---|---|---|
| README / Quickstart | `README.md` | ✅ |
| Storytelling + Cuadros 1–5 + Gráficos 1–6 | `Data/analisis_rentabilidad/PRESENTACION_STORYTELLING.md`, `outputs/tables/`, `outputs/charts/` | ✅ |
| Modelos y funciones / OLS `04_stats.py` | `Data/analisis_rentabilidad/scripts/04_stats.py` | ✅ (en `scripts/`, no en la raíz del módulo) |
| Arquitectura de datos / Parquet compacto | `Auxiliares/herramientas/exportar_parquet_compacto.py`, `test_parquet_compacto.py`, `data/compacto/` | ✅ (scripts en `Auxiliares/herramientas/`) |
| Alcance y retención | `Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md` | ✅ |
| Automatización / panel | `Auxiliares/herramientas/generar_dashboard.py` → `Data/dashboard.html` → `docs/dashboard.html` → `site/dashboard.html` | ✅ |
| Automatización / timers | `Data/_state/`, `~/.config/systemd/user/precio-*.timer` | ✅ |
| Estructura de espacio | `Data/ESTRUCTURA_ESPACIO.md` | ✅ |
| Mapa y base unificada | `Data/mapas/README.md`, `mapa_elementos.sqlite`, `Auxiliares/herramientas/generar_mapa_ofline.py` | ✅ salvo `mapa_talleres.html` |
| Sitio MkDocs | `mkdocs.yml`, `docs/`, `site/` | ✅ |
| Chunks y MANIFEST | `Data/Revolico/chunks/`, `pipeline_chunks/` | ✅ (82 y 52 `.bin`) |
| `benchmark_result.csv`, `watermarks.json`, ledger LFS, snapshots, `DICCIONARIO.md`, `LIMITACIONES.md` | — | ❌ no localizados |

## Resumen

- El checkout confirma los artefactos centrales: panel (3 copias de 109.929 B), 21 tablas, 6 gráficos, 82+52 chunks, sitio MkDocs y 5 timers activos con `Linger=yes`.
- Se localizan 7 artefactos citados que no existen: `benchmark_result.csv`, `watermarks.json`, `lfs_push_ledger.jsonl`, `manifiesto_ejecucion.jsonl`, `VERSIONES.json`, `snapshots/`+`LATEST.json` y `DICCIONARIO.md`+`LIMITACIONES.md`.
- Hay desajustes de ruta (`job_*.sh` y `sitio_build.sh` en `Data/_state/`, `alertas.jsonl` en `Data/_estado/`, `.venv` vs `.venv-py`) y el corpus declara 233 archivos ONEI cuando en disco hay 234.

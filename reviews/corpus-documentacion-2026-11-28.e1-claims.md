---
type: audit-artifact
phase: e1-claims
slug: corpus-documentacion-2026-11-28
generated_at: 2026-11-28T13:05:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md
language: es
---

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

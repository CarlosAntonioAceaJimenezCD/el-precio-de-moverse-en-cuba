---
type: audit-artifact
phase: e1-claims
slug: informe-tecnico-2026-11-27-iter2
generated_at: 2026-11-27T18:00:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter2/informe-tecnico-2026-11-27-iter2.text.md
language: es
---

# Claim Inventory

## Summary
- Total: 120
- Load-bearing: 13 · Supporting: 42 · Contextual: 65
- By type: result 60 · methodological 43 · novelty 1 · contextual 43 · definitional 5 · citation-grounded 11

## Load-bearing claims

### C001 — Objetivo vigente: análisis de mercado, recomendador diferido

- **Section**: §1 Objetivo (L16); §21 Cambio de objetivo (L881–886); Parte II §1 (L147)
- **Lines**: 16–18
- **Types**: definitional, contextual
- **Excerpt**: «Su objetivo actual es realizar un **análisis del mercado automotor cubano**: caracterizar estructura, precios, oferta, segmentos, tendencias, asequibilidad y condiciones de rentabilidad.»
- **Restated**: El objetivo declarado es el análisis del mercado automotor cubano y no la recomendación interactiva, que queda diferida a una especialización futura.
- **Internal evidence cited**: §21 (L881–886), §20 (L863, L870), Parte II §12 (L270, en sentido opuesto)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: la conclusión 5 de la Parte II (L270) sigue afirmando que el modelo y el producto interactivo «are not implemented yet», en contradicción con §12 español (L139).

### C002 — Fase 8 implementada y regenerada automáticamente

- **Section**: §12 Conclusiones (L139); §2 nota de actualización (L38); §34 (L1016–1037)
- **Lines**: 139
- **Types**: result, methodological
- **Excerpt**: «El análisis de mercado y el modelo de rentabilidad (fase 8) están implementados en `Data/analisis_rentabilidad/` y se regeneran de forma automática; la definición del producto interactivo se difiere a una especialización futura.»
- **Restated**: El pipeline de análisis y rentabilidad existe en `Data/analisis_rentabilidad/` y puede regenerarse automáticamente.
- **Internal evidence cited**: §34 (L1018–1037), §38 (L1112), §59–§60 (L1377–1391)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: cierra la contradicción principal de la iteración 1 en la Parte I; permanece en la Parte II (L164, L270).

### C003 — Cifras canónicas de la corrida vigente

- **Section**: §59 Storytelling alineado con los datos finales (L1379–1381)
- **Lines**: 1379
- **Types**: result
- **Excerpt**: «**772 autos únicos**, **2.029 anuncios limpios** (1.338 locales y 691 de importación), mediana local de **21.000 USD**, kilometraje mediano de **43.000 km**, 50 marcas, 101 grupos comparables y 81 anomalías»
- **Restated**: La corrida vigente del 27/11/2026 produce 772 autos únicos, 2.029 anuncios limpios, mediana local de 21.000 USD y 43.000 km, 50 marcas, 101 grupos y 81 anomalías.
- **Internal evidence cited**: §59 (L1379, `outputs/tables/kpis.csv` con marcadores automáticos), §58 (L1371, estado anterior)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: §45 (L1214) conserva 23.000 USD, 6,3 años, 34 marcas y 27 grupos; §58 (L1371) conserva 2.014 anuncios y 44.125 km.

### C004 — Modelo vigente sin pendiente anual significativa ni prima premium

- **Section**: §59 (L1381); §60 (L1389); §44 (L1206)
- **Lines**: 1381
- **Types**: result, methodological
- **Excerpt**: «La depreciación se reformuló con honestidad: el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra.»
- **Restated**: En la corrida vigente el coeficiente de edad del modelo hedónico no es significativo tras controlar por kilometraje.
- **Internal evidence cited**: §60 (L1389: p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05), §44 (L1206)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: retirada declarada del −5,43 % de §34; sin ablación ni test pareado entre corridas.

### C005 — Muestra del modelo completo: 28 observaciones de 981 candidatas

- **Section**: §59 (L1381)
- **Lines**: 1381
- **Types**: result
- **Excerpt**: «28 observaciones completas de <!-- kpi:modelo_candidatas -->981 candidatas (R² = <!-- kpi:modelo_r2_completo -->0,277; p del F = <!-- kpi:modelo_pf_completo -->0,411), límite que se registra explícitamente en `MODELOS_Y_FUNCIONES.md`.»
- **Restated**: La estimación completa usa 28 observaciones, con R² 0,277 y p del estadístico F 0,411, y la limitación está documentada.
- **Internal evidence cited**: §60 (L1389), `MODELOS_Y_FUNCIONES.md` (mencionado en L1381)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: incorpora al relato la dimensión muestral ausente en la iteración 1.

### C006 — Primera ejecución: depreciación −5,43 % anual (p<0,001)

- **Section**: §34 Línea base real de la primera ejecución (L1041–1056)
- **Lines**: 1056
- **Types**: result
- **Excerpt**: «El modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` da una depreciación media de **−5,43 % anual** (p<0,001), con primas de +21 % para premium y −22 % para tier medio frente al desconocido.»
- **Restated**: La primera corrida estimó −5,43 % anual de depreciación, +21 % de prima premium y −22 % para el tier medio.
- **Internal evidence cited**: §34 tabla «Línea base real de la primera ejecución» (L1043–1054)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: cifra retirada en §59–§60 pero reutilizada en §44 (L1206, con salvedad) y §45 (L1214, sin salvedad).

### C007 — Procedencia: anuncios como precios pedidos, no transaccionados

- **Section**: §18 Auditoría de procedencia (L826, L831–833)
- **Lines**: 831
- **Types**: methodological, definitional
- **Excerpt**: «los anuncios y redes son la **señal de precio** pero no sustituyen estadísticas oficiales. El análisis debe etiquetar cada métrica con su procedencia y nivel de confianza, y no mezclar tasas oficiales e informales ni precios anunciados con precios de transacción.»
- **Restated**: El análisis trata los anuncios como señal de precio pedido y prohíbe mezclar tasas oficiales con informales.
- **Internal evidence cited**: §18 tabla de procedencia (L816–829), §19 (L850, L855), §20 (L864)
- **External evidence cited**: DfT/DVLA y ANFAC/AEADE, verificados en vivo según §18 (L818, L822–823) y §70 (L1477)
- **Novelty signals**: ninguno.
- **Notes**: —

### C008 — Declaración de uso de inteligencia artificial

- **Section**: §69 Declaración de uso de inteligencia artificial (L1467–1471)
- **Lines**: 1469–1471
- **Types**: methodological
- **Excerpt**: «Las cifras, los modelos estadísticos y las decisiones de diseño provienen de los datos y del código versionados en este repositorio; ninguna afirmación empírica se originó en una salida de IA sin contraste contra los archivos.»
- **Restated**: Toda afirmación empírica del informe fue contrastada contra archivos versionados y la auditoría con la skill `review` quedó registrada.
- **Internal evidence cited**: §69 (L1469–1471), `reviews/informe-tecnico-2026-11-27.{md,forensic.md}` y trece artefactos de fase
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: sección nueva que cierra la ausencia de declaración de F-V10-003; no nombra herramientas concretas ni protocolo de supervisión.

### C009 — Referencias verificadas y estado del resto del aparato

- **Section**: §70 Referencias verificadas (L1475–1479)
- **Lines**: 1477–1479
- **Types**: citation-grounded
- **Excerpt**: «Akerlof (1970), *The Market for "Lemons"* (Crossref/OpenAlex); UK Department for Transport / DVLA, estadísticas de vehículos (GOV.UK); ANFAC, informes del sector automotriz español (sitio oficial); AEADE, estadísticas de matriculaciones (sitio oficial).»
- **Restated**: Solo cuatro referencias están verificadas externamente; las restantes figuran como `(metadata incomplete)` y la convención numerada reúne 38 entradas.
- **Internal evidence cited**: §70 (L1477–1479), `Data/referencias.md`, `reviews/informe-tecnico-2026-11-27.e2-literature.md`
- **External evidence cited**: Crossref, OpenAlex, GOV.UK, sitios oficiales de ANFAC y AEADE (según declara L1477)
- **Novelty signals**: ninguno.
- **Notes**: atiende parcialmente F-V10-007; el cuerpo del informe sigue sin citas numeradas.

### C010 — Conversión TRMI: serie diaria referencial, 930 fijo en el modelo

- **Section**: §23 Conversión elTOQUE (L902); §52 (L1297); Parte II §23 (L907)
- **Lines**: 902
- **Types**: methodological
- **Excerpt**: «**Aclaración vigente:** el pipeline de `Data/analisis_rentabilidad/` usa la TRMI fija de 930 CUP/USD del 18/11/2026 (`config.py`); la serie diaria es referencia histórica, no insumo del modelo actual.»
- **Restated**: La conversión del modelo usa 930 CUP/USD fijos y la serie diaria de elTOQUE no alimenta la estimación vigente.
- **Internal evidence cited**: §23 (L902), §52 (L1297), `config.py` (mencionado en L902)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: aclara la dualidad 920/930 de F-V10-004 en español; L904 mantiene el 920 histórico y L907 (inglés) sigue describiendo conversión diaria.

### C011 — Arquitectura del esqueleto inspirada en Egyptian-Used-Cars

- **Section**: §34 (L1018–1039)
- **Lines**: 1018
- **Types**: methodological, novelty
- **Excerpt**: «Creé `Data/analisis_rentabilidad/` siguiendo la arquitectura del repositorio **Egyptian-Used-Cars** (ingesta → limpieza → EDA → estadística → benchmark), pero adaptada a nuestras fuentes y preparada para crecer:»
- **Restated**: La arquitectura del pipeline de rentabilidad deriva de Egyptian-Used-Cars y fue adaptada a las fuentes cubanas.
- **Internal evidence cited**: §34 (L1018–1039), §60 (L1387–1390)
- **External evidence cited**: repositorio `Egyptian-Used-Cars` (fuente de ingeniería, sin ficha académica en el documento)
- **Novelty signals**: «Creé» (L1018), «adaptada a nuestras fuentes» (L1018), «preparada para crecer» (L1018).
- **Notes**: es la única diferenciación comparativa declarada del documento (F-V10-006).

### C012 — Brecha frente a Egipto

- **Section**: §34 Brecha frente a Egipto (L1058–1060)
- **Lines**: 1060
- **Types**: result, contextual
- **Excerpt**: «Egipto tiene 23.500 anuncios, historial mensual de precios, HP y kilometraje estructurados, ANOVA/OLS/VIF, Tableau y Power BI. Nosotros tenemos el pipeline y las técnicas cubiertas, pero solo 497 usados, un único snapshot, HP/kilometraje mayormente ausentes y un solo benchmark de auto nuevo.»
- **Restated**: Frente a 23.500 anuncios del repositorio egipcio, el proyecto dispone de 497 usados, una sola instantánea y campos mayormente ausentes.
- **Internal evidence cited**: §34 tabla de la primera ejecución (L1045–1054), `NECESIDADES.md`
- **External evidence cited**: repositorio `Egyptian-Used-Cars` (sin verificación académica en el documento)
- **Novelty signals**: ninguno.
- **Notes**: diferenciación por escala y cobertura, no por método.

### C013 — Límites declarados del marco analítico

- **Section**: §19 Adaptación a Cuba / La Habana (L848–855)
- **Lines**: 855
- **Types**: definitional, methodological
- **Excerpt**: «- **Límites**: precios pedidos no transaccionados, sesgo de supervivencia de anuncios, sin datos personales, vigencia normativa a verificar.»
- **Restated**: El análisis declara como límites los precios pedidos, el sesgo de supervivencia, la ausencia de datos personales y la vigencia normativa pendiente.
- **Internal evidence cited**: §19 (L850–855), §18 (L831), §20 (L871)
- **External evidence cited**: — (sin citas numeradas)
- **Novelty signals**: ninguno.
- **Notes**: —

## Supporting claims (42)

### C014 — Fase 6: 11 bases y 256 filas
- **Section**, **Lines**: §9 (L94–110), 94–108
- **Types**: result
- **Excerpt**: «Se prepararon 11 bases y se obtuvieron **256 filas**:»
- **Restated**: La fase 6 produjo 256 filas distribuidas en 11 tiendas.
- **Internal/External evidence**: tabla de tiendas (L96–108); sin citas numeradas.
- **Notes**: las once filas suman 256 (AGN 60, ATR 6, BDC 19, Changan 2, Chinautos 70, ConnectingCuba 1, Dongfeng 45, Envision 1, Finauto 45, MCV 4, Subasta 3).

### C015 — Fuentes excluidas por bloqueo técnico
- **Section**, **Lines**: §9 (L110), 110
- **Types**: result, contextual
- **Excerpt**: «Excluidas por bloqueo técnico: carrosw (HTTP 403 con Bot Verification), LlamaCuba (timeout) y SASA/DIVEP (sin catálogo).»
- **Restated**: Tres fuentes quedaron fuera de la captura por 403, timeout o ausencia de catálogo.
- **Internal/External evidence**: §9 (L110), §11 (L129); sin citas numeradas.
- **Notes**: —

### C016 — Descubrimiento: 409 resultados, 400 únicos
- **Section**, **Lines**: §5 (L62), 62
- **Types**: result
- **Excerpt**: «Se consolidaron **409 resultados, 400 únicos**.»
- **Restated**: La consolidación inicial produjo 409 resultados, de los cuales 400 son únicos.
- **Internal/External evidence**: §5 (L62); sin citas numeradas.
- **Notes**: —

### C017 — Inventario y verificación de sitios
- **Section**, **Lines**: §5 (L62, L64), 62–64
- **Types**: result
- **Excerpt**: «Se inventariaron **35 sitios** de compraventa en `Data/mercados-compraventa-cuba.md`» / «Se verificaron **40 sitios/URLs**.»
- **Restated**: Se inventariaron 35 sitios de compraventa y se verificaron 40 sitios o URLs.
- **Internal/External evidence**: §5 (L62, L64); sin citas numeradas.
- **Notes**: —

### C018 — Organismos con competencia sobre el mercado
- **Section**, **Lines**: §5 (L66), 66
- **Types**: result, contextual
- **Excerpt**: «Se documentaron **14 organismos** con competencia sobre el mercado: Consejo de Ministros/Estado, MINCEX, MINCIN, MITRANS, CEMA, MFP, ONAT, Aduana General, BCC, MININT, MINJUS, MEP, MINREX y MINSAP.»
- **Restated**: El documento identifica 14 organismos con competencia sobre el mercado automotor.
- **Internal/External evidence**: §5 (L66); sin citas numeradas.
- **Notes**: —

### C019 — Empresas autorizadas y precios de referencia
- **Section**, **Lines**: §4 (L58), 58
- **Types**: result, citation-grounded
- **Excerpt**: «Se documentaron **17 empresas autorizadas** a importar y comercializar vehículos, distribuidores privados (BDC One, Dongfeng, MCV, Finauto, Changan, Chinautos, Envision, ATR Export), precios de referencia (BDC One 14.849–31.478 EUR; Dongfeng desde 21.900 EUR; Finauto desde 15.500 EUR»
- **Restated**: El marco normativo registra 17 empresas autorizadas y precios de referencia por distribuidor.
- **Internal/External evidence**: §4 (L58), `Data/investigacion-mercado-automotor-cuba.md`; sin citas numeradas.
- **Notes**: el equivalente inglés (L189) usa separadores de miles con coma.

### C020 — Marco normativo: Decreto 163/2026 y resoluciones
- **Section**, **Lines**: §4 (L58), §10 (L116–117), 58/116–117
- **Types**: citation-grounded
- **Excerpt**: «La norma marco es el **Decreto 163/2026** (Gaceta Oficial No. 65 Ordinaria, 04/08/2026, vigente desde el 11/08/2026), que deroga el Decreto 119/2024.»
- **Restated**: El Decreto 163/2026 es la norma marco vigente y deroga el Decreto 119/2024.
- **Internal/External evidence**: §4 (L58), §10 (L116–118); Gaceta Oficial No. 65/2026 citada sin numeración.
- **Notes**: —

### C021 — Derogación de la Resolución 312/2026
- **Section**, **Lines**: §52 (L1303), 1303
- **Types**: citation-grounded, result
- **Excerpt**: «la **Resolución 312/2026 de la Aduana General fue derogada por la Resolución 340/2026**.»
- **Restated**: La Resolución 340/2026 deroga a la 312/2026, que no debe citarse como norma vigente.
- **Internal/External evidence**: §52 (L1303), §4 (L58), §10 (L117); sin citas numeradas.
- **Notes**: corrección documentada en README, informe y verificación de marketplaces.

### C022 — Clonación de repositorios y clasificación CAPTCHA
- **Section**, **Lines**: §6 (L70), 70
- **Types**: result
- **Excerpt**: «Se clonaron **61 repositorios** en `Auxiliares/Repositorios` con `--depth 1` (2,2 GB, 61 entradas `OK`).»
- **Restated**: Se clonaron 61 repositorios (2,2 GB) y se clasificaron 92 proyectos CAPTCHA, de los que se seleccionaron 9.
- **Internal/External evidence**: §6 (L70); sin citas numeradas.
- **Notes**: —

### C023 — Entorno y dependencias instaladas
- **Section**, **Lines**: §6 (L72), 72
- **Types**: contextual
- **Excerpt**: «Se creó `Auxiliares/.venv` con patchright 1.64.4, PyPasser 1.1.0, Scrapling 0.5.1, ddddocr 1.6.1, playwright 1.65.2, curl_cffi 0.17.0, trafilatura, pandas, numpy, onnxruntime 1.32.0, ddgs 9.16.1 y tenacity 9.2.1.»
- **Restated**: El entorno virtual contiene las versiones declaradas de once dependencias.
- **Internal/External evidence**: §6 (L72); sin citas numeradas.
- **Notes**: —

### C024 — Regla de parada en la búsqueda documental
- **Section**, **Lines**: §7 (L78–86), 78–84
- **Types**: methodological, result
- **Excerpt**: «Tres búsquedas con la regla de parar tras 10 páginas sin enlaces útiles (útil = primera aparición de un trabajo investigativo automotriz):»
- **Restated**: Las tres búsquedas se detuvieron tras diez páginas sin enlaces útiles, con 159 páginas y 1.542 resultados en total.
- **Internal/External evidence**: tabla de búsquedas (L80–84); sin citas numeradas.
- **Notes**: las paradas declaradas fueron páginas 19, 11 y 22.

### C025 — Esquema SQLite por tienda
- **Section**, **Lines**: §8 (L90), 90
- **Types**: definitional, methodological
- **Excerpt**: «Se diseñó una base SQLite por tienda con una tabla `vehiculos`: identificación (`url`, `shop`, `title`, `status`, `scraped_at`), metadatos y 30 campos estructurados»
- **Restated**: El diseño prevé una base SQLite por tienda con 30 campos estructurados y campos sin normalizar.
- **Internal/External evidence**: §8 (L90); sin citas numeradas.
- **Notes**: —

### C026 — Conclusión: nueve marketplaces con inventario real
- **Section**, **Lines**: §12 (L135), 135
- **Types**: result, contextual
- **Excerpt**: «El mercado habanero tiene nueve marketplaces con inventario real y una docena con categorías vacías o solo piezas.»
- **Restated**: El mercado habanero cuenta con nueve marketplaces con inventario real y alrededor de una docena sin inventario de autos.
- **Internal/External evidence**: §5 (L64), §12 (L135); sin citas numeradas.
- **Notes**: el expediente de la iteración 1 observó quince sitios en esa categoría.

### C027 — Causalidad declarada del scraping sostenible
- **Section**, **Lines**: §12 (L137), 137
- **Types**: methodological
- **Excerpt**: «El scraping sostenible depende del ritmo, la sesión y la reanudación, no principalmente del fingerprint TLS.»
- **Restated**: El ritmo, la sesión y la reanudación son los factores decisivos del scraping sostenible, por encima del fingerprint TLS.
- **Internal/External evidence**: §11 (L126–131), §37 (L1100), §65 (L1433); sin comparación de condiciones.
- **Notes**: atribución causal sin contraste experimental.

### C028 — Regla de las 10 páginas
- **Section**, **Lines**: §12 (L138), 138
- **Types**: methodological, result
- **Excerpt**: «La regla de las 10 páginas evitó consumir resultados repetidos.»
- **Restated**: La regla de parada de diez páginas impidió procesar resultados repetidos.
- **Internal/External evidence**: §7 (L78–84), §33 (L1008); sin citas numeradas.
- **Notes**: —

### C029 — Nota de actualización de fases
- **Section**, **Lines**: §2 (L38); Parte II §2 (L169), 38
- **Types**: contextual, result
- **Excerpt**: «El pipeline de análisis (fase 8) se creó después, el 18/11/2026 (§34), y sus resultados vigentes se documentan en §59–§60.»
- **Restated**: La tabla de fases refleja el estado al 17/11/2026 y la fase 8 se creó el 18/11/2026.
- **Internal/External evidence**: §2 (L22–38), §34 (L1016), §59–§60; sin citas numeradas.
- **Notes**: atenúa pero no elimina la contradicción con la tabla de la Parte II (L164).

### C030 — Permanencia empírica de anuncios en Revolico
- **Section**, **Lines**: §15 (L775), 775
- **Types**: result
- **Excerpt**: «un anuncio con `updated_on_by_user=2024-12-17` seguía en HTTP 200 el 17/11/2026 (~699 días), por lo que no puede asumirse una expiración de 30 días.»
- **Restated**: Un anuncio con 699 días de antigüedad seguía accesible, de modo que no se puede asumir caducidad a los 30 días.
- **Internal/External evidence**: §15 (L775), Condiciones de Uso de Revolico (23/09/2026) citadas sin numeración.
- **Notes**: —

### C031 — Limpieza de la BD de Revolico
- **Section**, **Lines**: §15 (L773), 773
- **Types**: result
- **Excerpt**: «`limpiar_revolico.py` conservó **304 autos** en la tabla `autos` y registró **6.028 exclusiones** en `revision` (5.983 no vehículo 4+ ruedas, 45 sin datos necesarios, 0 páginas sin datos suficientes).»
- **Restated**: Sobre 6.332 anuncios se conservaron 304 autos y se registraron 6.028 exclusiones.
- **Internal/External evidence**: §15 (L771–773), §16 (L787); sin citas numeradas.
- **Notes**: 304 + 6.028 = 6.332.

### C032 — Eficiencia relativa de las fuentes
- **Section**, **Lines**: §15 (L767–769), 767
- **Types**: methodological
- **Excerpt**: «la ruta más eficiente es Telegram MTProto (`telethon`, ya integrado): sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`. Le sigue Facebook GQL»
- **Restated**: Telegram MTProto es la fuente más eficiente, seguida de Facebook GQL, WAHA para WhatsApp y Playwright/Selenium como último recurso.
- **Internal/External evidence**: §15 (L767–769), §28 (L950); sin citas numeradas.
- **Notes**: jerarquía declarada sin medición comparativa de rendimiento.

### C033 — Pipeline de tres colas persistentes
- **Section**, **Lines**: §16 (L779–783), 779–783
- **Types**: methodological
- **Excerpt**: «separa el trabajo en tres etapas simultáneas con colas persistentes en `Data/Revolico/pipeline.sqlite`»
- **Restated**: El pipeline separa descubrimiento, descarga y procesamiento con colas persistentes y commit cada 25 anuncios.
- **Internal/External evidence**: §16 (L779–787), §26 (L928–933); sin citas numeradas.
- **Notes**: —

### C034 — Prueba inicial del pipeline por colas
- **Section**, **Lines**: §16 (L787), 787
- **Types**: result
- **Excerpt**: «Prueba con 1 página: **119 enlaces** descubiertos y procesados, 7 lotes de 25, BD principal de 6.332 a **6.334 anuncios** y de 304 a **317 autos**.»
- **Restated**: La prueba con una página procesó 119 enlaces y elevó la BD a 6.334 anuncios y 317 autos.
- **Internal/External evidence**: §16 (L787, L789); sin citas numeradas.
- **Notes**: el número de lotes completos de 25 es cuatro, no siete (coherencia interna no verificada).

### C035 — Rango temporal de anuncios
- **Section**, **Lines**: §31 (L987–989), 987–989
- **Types**: methodological, result
- **Excerpt**: «Se fijó el rango permitido de `updated_on_by_user` entre **2021-01-01 y la fecha actual** en `limpiar_revolico.py` (`FECHA_MINIMA`).»
- **Restated**: Los anuncios se acotan entre 2021-01-01 y la fecha de ejecución, sin exclusiones en la corrida declarada.
- **Internal/External evidence**: §31 (L987–991); sin citas numeradas.
- **Notes**: anuncio más antiguo 2024-12-17, más reciente 2026-11-17; 548 autos de 9.957 anuncios.

### C036 — Deduplicación de `autos`
- **Section**, **Lines**: §51 (L1279), 1279
- **Types**: result
- **Excerpt**: «La tabla se reconstruyó desde `anuncios` (fuente canónica): 814 filas con 748 IDs únicos → **744 autos únicos**.»
- **Restated**: La deduplicación redujo 814 filas a 744 autos únicos y creó el índice `idx_autos_id`.
- **Internal/External evidence**: §51 (L1279), §59 (L1379, 772 autos en la corrida vigente); sin citas numeradas.
- **Notes**: cuatro anuncios se marcaron como no-auto.

### C037 — Reparación de precios y títulos de marketplaces
- **Section**, **Lines**: §51 (L1281), 1281
- **Types**: result, methodological
- **Excerpt**: «`parse_price` ahora interpreta separadores de miles (973 anuncios recuperados: 872 de iTENCEL, 99 de Cubisima, 2 de VentaCuba).»
- **Restated**: La corrección del parseo recuperó 973 precios y 614 precios de Autocubana desde JSON-LD.
- **Internal/External evidence**: §51 (L1281), `descartes_marketplaces.csv`; sin citas numeradas.
- **Notes**: mediana local declarada de 21.000 USD.

### C038 — Corrección del kilometraje con separador de miles
- **Section**, **Lines**: §51 (L1282), 1282
- **Types**: methodological, result
- **Excerpt**: «`parse_specs` y `parse_title` convertían `80,000 km` en 80 km. Se extrajo `parse_number()` con la lógica de separadores ya usada en `parse_price`.»
- **Restated**: La nueva función `parse_number()` convierte correctamente `80,000 km` en 80.000 km.
- **Internal/External evidence**: §51 (L1282); sin citas numeradas.
- **Notes**: —

### C039 — Reconciliación de la encuesta de demanda
- **Section**, **Lines**: §51 (L1285), 1285
- **Types**: result
- **Excerpt**: «el cruce filtra ahora `interes=1`, dando **28 interesados** (14 eléctrico, 10 combustión, 4 híbrido) en lugar de los 29 que contaba el script anterior»
- **Restated**: El cruce vigente cuenta 28 interesados, frente a 29 del script anterior.
- **Internal/External evidence**: §50 (L1269), §51 (L1285); sin citas numeradas.
- **Notes**: —

### C040 — Descarga de los anuarios del ONEI
- **Section**, **Lines**: §53 (L1313–1315), 1313–1315
- **Types**: result
- **Excerpt**: «se descargaron **todos los documentos enlazados**: 111 PDF, 7 RAR y 103 archivos Excel extraídos, unos 311 MB en total.»
- **Restated**: Se descargaron los 117 enlaces de los 12 anuarios del ONEI (2014–2025), con 111 PDF, 7 RAR y 103 Excel.
- **Internal/External evidence**: §53 (L1313–1315), `Data/fuentes-oficiales/ONEI/INDICE.md`; sin citas numeradas.
- **Notes**: validación MIME sin archivos sospechosos.

### C041 — Hallazgos de los anuarios y laguna de parque automotor
- **Section**, **Lines**: §56 (L1351), 1351
- **Types**: result
- **Excerpt**: «el transporte de pasajeros cayó un 59 % entre 2019 y 2025 y el ómnibus un 71 %; los accidentes bajaron pero la gravedad aumentó (9,9 fallecidos por cada 100 accidentes en 2025). **No hay series de parque automotor ni de matriculaciones**»
- **Restated**: Las series del ONEI muestran caídas del 59 % y 71 %, pero no contienen parque automotor ni matriculaciones.
- **Internal/External evidence**: §53 (L1317), §56 (L1351), `ANALISIS_DATO.md`; sin citas numeradas.
- **Notes**: corrige la expectativa registrada en §53 (L1317).

### C042 — Fragmentación de la BD con manifiesto
- **Section**, **Lines**: §54 (L1325–1329), 1325
- **Types**: methodological, result
- **Excerpt**: «`Data/Revolico/revolico.sqlite` (849.465.344 bytes) se dividió en **82 chunks de 10 MB** en `Data/Revolico/chunks/`, con un `MANIFEST.json` que guarda el SHA-256 del archivo completo, el orden, el offset y el hash de cada fragmento.»
- **Restated**: La BD de 849.465.344 bytes se dividió en 82 fragmentos verificados con manifiesto SHA-256.
- **Internal/External evidence**: §54 (L1325–1329), §14 (L756–763); sin citas numeradas.
- **Notes**: los chunks se publican en la rama huérfana `chunked-db`.

### C043 — Gestión con Git LFS
- **Section**, **Lines**: §30 (L977–981), 977–981
- **Types**: methodological
- **Excerpt**: «Se instaló **Git LFS 3.8.1** y se activó en el repositorio. `.gitattributes` marca `*.sqlite`, `*.sqlite-wal` y `*.sqlite-shm` con `filter=lfs diff=lfs merge=lfs -text`»
- **Restated**: Las bases SQLite se gestionan con Git LFS y se advierte sobre el consumo de cuota.
- **Internal/External evidence**: §30 (L977–983), §54 (L1327); sin citas numeradas.
- **Notes**: —

### C044 — Fuentes adicionales verificadas
- **Section**, **Lines**: §52 (L1293), 1293
- **Types**: result
- **Excerpt**: «El resultado está en `Data/fuentes-adicionales-2026-11-20.md`: **25 fuentes** verificadas, organizadas por tipo con URL, datos expuestos, viabilidad de scraping y aporte al proyecto.»
- **Restated**: Se verificaron 25 fuentes adicionales organizadas por tipo.
- **Internal/External evidence**: §52 (L1293–1305); sin citas numeradas.
- **Notes**: —

### C045 — Repositorios cubanos de automoción
- **Section**, **Lines**: §49 (L1251), 1251
- **Types**: result
- **Excerpt**: «Tras deduplicar se obtuvieron **648 repos**, de los que se depuraron **36 con relación directa o instrumental** al mercado automotor cubano.»
- **Restated**: La búsqueda produjo 648 repositorios únicos y 36 con relación directa o instrumental.
- **Internal/External evidence**: §49 (L1251–1255), `Data/github-repos-automotriz-cuba-2026-11-19.md`; sin citas numeradas.
- **Notes**: —

### C046 — Consolidación de bases de repositorios de referencia
- **Section**, **Lines**: §50 (L1267), 1267
- **Types**: result
- **Excerpt**: «Se creó `Data/repos-autos-referencias/referencias_autos.sqlite` con **25 tablas** (3.958 anuncios de Revolico, 3.566 limpios, catálogos de comercializadoras, 33 respuestas de encuesta, 30 + 30 + 8 entrevistas, datasets de AutosxCuba) y una tabla `provenancia`.»
- **Restated**: La base consolidada reúne 25 tablas con procedencia declarada.
- **Internal/External evidence**: §50 (L1263–1269); sin citas numeradas.
- **Notes**: 369 anuncios ya estaban en la base propia y 3.589 son nuevos.

### C047 — Detección de duplicados entre repositorios
- **Section**, **Lines**: §50 (L1265), 1265
- **Types**: result
- **Excerpt**: «Se compararon 233 archivos de datos por hash y 76 CSV por contenido ordenado. Se detectaron 12 grupos de duplicados bytes y 11 de duplicados por contenido»
- **Restated**: La comparación detectó 23 grupos de duplicados entre los archivos de los repositorios referencia.
- **Internal/External evidence**: §50 (L1265); sin citas numeradas.
- **Notes**: —

### C048 — Convención de 38 referencias con estado de verificación
- **Section**, **Lines**: §70 (L1477), 1477
- **Types**: result, citation-grounded
- **Excerpt**: «Las fuentes restantes figuran con estado `(metadata incomplete)` en `reviews/informe-tecnico-2026-11-27.e2-literature.md` y no se presentan como referencias verificadas. La convención numerada de 38 referencias y su estado de verificación están en `Data/referencias.md`»
- **Restated**: Existen 38 referencias numeradas con estado de verificación, cuatro de ellas confirmadas externamente.
- **Internal/External evidence**: §70 (L1477–1479), `Data/referencias.md`; Crossref/OpenAlex según el propio texto.
- **Notes**: —

### C049 — Incorporación de diez anuncios de iTENCEL
- **Section**, **Lines**: §58 (L1369–1371), 1371
- **Types**: result
- **Excerpt**: «La BD pasó de 951 a **961 anuncios** (961 URLs únicas, `integrity_check=ok`).»
- **Restated**: La base de iTENCEL pasó de 951 a 961 anuncios únicos tras insertar diez anuncios nuevos.
- **Internal/External evidence**: §57 (L1361), §58 (L1369–1373); sin citas numeradas.
- **Notes**: se realizó copia de seguridad `itencel.sqlite.bak-20261123` antes de escribir.

### C050 — Estado previo de los anuncios limpios
- **Section**, **Lines**: §58 (L1371), 1371
- **Types**: result
- **Excerpt**: «**2.014 anuncios limpios**, de ellos 1.323 locales y 691 de importación; mediana local 21.000 USD y mediana de kilometraje 44.125 km.»
- **Restated**: Tras la incorporación de iTENCEL, la regeneración produjo 2.014 anuncios limpios y 44.125 km de mediana.
- **Internal/External evidence**: §58 (L1371), §59 (L1379, cifras vigentes 2.029 y 43.000 km); sin citas numeradas.
- **Notes**: estado intermedio sustituido por §59.

### C051 — Capas del mapa offline
- **Section**, **Lines**: §41 (L1154–1157), §42 (L1177), 1177
- **Types**: result
- **Excerpt**: «Estado final: **131 gasolineras, 12 estaciones de carga, 25 concesionarios (17 con coords) y 22 talleres (todos con coords)**.»
- **Restated**: El mapa unificado contiene 131 gasolineras, 12 estaciones de carga, 25 concesionarios y 22 talleres.
- **Internal/External evidence**: §41 (L1154–1157, 137 gasolineras iniciales), §42 (L1168–1179); sin citas numeradas.
- **Notes**: el descenso de 137 a 131 gasolineras no se explica en el texto.

### C052 — Serie de precios del combustible
- **Section**, **Lines**: §41 (L1157–1160), 1157–1160
- **Types**: result, citation-grounded
- **Excerpt**: «Se creó `Data/combustible/precios_combustible.sqlite` con **18 observaciones** entre 20/08/2026 y 18/11/2026, diferenciando mercado oficial CIMEX, informal elToque y precios publicados, sin convertir monedas automáticamente.»
- **Restated**: La serie de combustible tiene 18 observaciones y separa mercado oficial, informal y precios publicados.
- **Internal/External evidence**: §41 (L1157–1160), §43 (L1189–1195, hitos normativos); sin citas numeradas.
- **Notes**: la B94 informal pasó de 3.500–5.000 CUP (agosto) a 7.000–8.000 CUP (septiembre 2026).

### C053 — Estimación de retención como inferencia de diseño
- **Section**, **Lines**: §63 (L1417), 1417
- **Types**: methodological
- **Excerpt**: «La estimación de retención (`Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md`) es **inferencia de diseño, no medición**»
- **Restated**: Las cifras de retención son una proyección de diseño, no una medición observada.
- **Internal/External evidence**: §63 (L1415–1419), `ALCANCE_Y_RETENCION.md`; sin citas numeradas.
- **Notes**: el propio texto rotula la naturaleza no empírica de la estimación.

### C054 — Compilación estricta del sitio
- **Section**, **Lines**: §61 (L1399), 1399
- **Types**: methodological, result
- **Excerpt**: «`mkdocs build --strict` termina sin errores ni enlaces rotos.»
- **Restated**: La compilación estricta del sitio MkDocs termina sin errores ni enlaces rotos.
- **Internal/External evidence**: §61 (L1397–1401), `mkdocs.yml`, `docs/`; sin citas numeradas.
- **Notes**: —

### C055 — Primera corrida real del scraper de circuitos
- **Section**, **Lines**: §62 (L1407), 1407
- **Types**: result
- **Excerpt**: «en su primera corrida real capturó 40 mensajes, deduplicó por ID y dejó 35 circuitos sin luz, 23 mixtos y 2 con luz en `Data/mapas/circuitos_estado.sqlite`.»
- **Restated**: El primer scrapeo de circuitos produjo 60 registros clasificados a partir de 40 mensajes.
- **Internal/External evidence**: §62 (L1405–1409), `TIMELAPSE_CIRCUITOS.md`; sin citas numeradas.
- **Notes**: 35 + 23 + 2 = 60, cifra superior a los 40 mensajes declarados.

## Contextual claims (65)

### C056 — Fase activa redefinida como sexta
- **Section**, **Lines**: §2 (L22), 22
- **Types**: contextual
- **Excerpt**: «Las fases se redefinieron para que la fase activa sea la sexta. Estado a 17/11/2026:»

### C057 — Informe y README como soporte transversal
- **Section**, **Lines**: §2 (L36), 36
- **Types**: contextual
- **Excerpt**: «La creación de este informe y del `README.md` es soporte transversal y no cambia la fase activa.»

### C058 — Decisiones de organización de carpetas
- **Section**, **Lines**: §3 (L54), 54
- **Types**: methodological, contextual
- **Excerpt**: «todo el material auxiliar vive dentro de `Auxiliares/`; los clones se hicieron con `--depth 1` y se registraron en `~/Utilidades/HerramientasScraping/_clone_log.tsv`; la descubrimiento se separó de la verificación»

### C059 — Exclusión de `Copias/`
- **Section**, **Lines**: §3 (L54), 54
- **Types**: contextual
- **Excerpt**: «`Copias/` no se registra en este informe por decisión explícita.»

### C060 — Decreto 163/2026 y Gaceta Oficial
- **Section**, **Lines**: §4 (L58), 58
- **Types**: citation-grounded
- **Excerpt**: «La norma marco es el **Decreto 163/2026** (Gaceta Oficial No. 65 Ordinaria, 04/08/2026, vigente desde el 11/08/2026), que deroga el Decreto 119/2024.»

### C061 — Cambio de motor de búsqueda
- **Section**, **Lines**: §5 (L62), 62
- **Types**: contextual
- **Excerpt**: «Dos búsquedas iniciales en DuckDuckGo, 30 páginas cada una, con bloqueo por CAPTCHA: se cambió a Yahoo y visitas directas.»

### C062 — Correcciones de clasificación de sitios
- **Section**, **Lines**: §5 (L64), 64
- **Types**: result, contextual
- **Excerpt**: «Se corrigieron clasificaciones: Mercadoba y Fagales Market sin sección real; TuCuevita, Mercubano, Mercandil, Revoltillo, QvaVentas, Casinuevo, Publicid, WAnuncios y AnunciosCuba con categoría vacía»

### C063 — Inventario de marketplaces activos
- **Section**, **Lines**: §5 (L64), 64
- **Types**: result
- **Excerpt**: «Marketplaces con sección activa: Autocubana (667 vehículos), iTENCEL (951), VentaCuba (801 carros/camionetas), Timbirichi (281 carros), Revolico (112 enlaces en la primera página), Cogetucarro (5.225 anuncios), Cubisima (155 fichas)»

### C064 — Cobertura temática de los repositorios clonados
- **Section**, **Lines**: §6 (L70), 70
- **Types**: contextual
- **Excerpt**: «El conjunto cubre scraping general (Firecrawl, browser-use, Scrapling, crawl4ai, Scrapy, SeleniumBase, trafilatura, curl_cffi, Patchright, Playwright), Facebook, WhatsApp, Telegram y CAPTCHA.»

### C065 — Chromium del sistema y FlareSolverr
- **Section**, **Lines**: §6 (L72), 72
- **Types**: contextual
- **Excerpt**: «Se usa el Chromium del sistema y FlareSolverr 3.5.2 en Docker (`http://127.0.0.1:8191/`).»

### C066 — Herramientas creadas en la fase 3
- **Section**, **Lines**: §6 (L74), 74
- **Types**: contextual
- **Excerpt**: «Herramientas creadas: `ddg_research.py`, `buscar_fallback.py`, `descargar_hombros.py`, `scrape_concesionarios.py`, `resumen_catalogos.py` y `actualizar_informe.py`.»

### C067 — Definición operativa de «útil»
- **Section**, **Lines**: §7 (L78), 78
- **Types**: definitional, methodological
- **Excerpt**: «útil = primera aparición de un trabajo investigativo automotriz»

### C068 — Resultados de descarga del corpus
- **Section**, **Lines**: §7 (L86), 86
- **Types**: result
- **Excerpt**: «descarga inicial **93 OK / 17 fallos**, rentabilidad **23 OK / 10 fallos**, calidad/precio **78 OK / 36 fallos**, con `manifest.jsonl` e `indice.md`.»

### C069 — Adaptadores por dominio y renderizado opcional
- **Section**, **Lines**: §8 (L90), 90
- **Types**: methodological
- **Excerpt**: «El scraper `scrape_concesionarios.py` usa adaptadores por dominio y renderizado opcional con Playwright.»

### C070 — Filtro de normas relevantes
- **Section**, **Lines**: §10 (L114), 114
- **Types**: contextual
- **Excerpt**: «Solo se incluyen las normas y fuentes relevantes para el contexto del proyecto:»

### C071 — No elusión de anti-automatización
- **Section**, **Lines**: §10 (L118), 118
- **Types**: methodological, contextual
- **Excerpt**: «No se eluden mecanismos anti-automatización; los HTTP 403/429 se registran como limitación.»

### C072 — Condiciones para publicar resultados
- **Section**, **Lines**: §10 (L119), 119
- **Types**: methodological, contextual
- **Excerpt**: «antes de publicar resultados deben verificarse las normas cubanas vigentes y aplicar solo datos agregados, sin nombres, teléfonos ni información personal de anunciantes.»

### C073 — Índice de gacetas fuera del árbol
- **Section**, **Lines**: §10 (L120), 120
- **Types**: contextual
- **Excerpt**: «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe»

### C074 — Solución al CAPTCHA de paginación
- **Section**, **Lines**: §11 (L126), 126
- **Types**: methodological, contextual
- **Excerpt**: «CAPTCHA en paginación DDG | Yahoo + visitas directas; después sesión con `vqd`.»

### C075 — Manejo de HTTP 202 y página anomaly
- **Section**, **Lines**: §11 (L127–128), 127–128
- **Types**: methodological, contextual
- **Excerpt**: «HTTP 202 y página “anomaly” | Pausa 7–10 s con jitter, backoff exponencial y cooldown.»

### C076 — Registro de carrosw como limitación
- **Section**, **Lines**: §11 (L129), 129
- **Types**: methodological, contextual
- **Excerpt**: «carrosw anti-bot | Registrado como limitación; no se falsificó su contenido.»

### C077 — Deduplicación por título, prefijo y dominio
- **Section**, **Lines**: §11 (L131), 131
- **Types**: methodological, contextual
- **Excerpt**: «Repetidos y mirrors | Deduplicación por título normalizado, prefijo y dominio.»

### C078 — Conclusión sobre marketplaces y categorías vacías
- **Section**, **Lines**: §12 (L135), 135
- **Types**: result, contextual
- **Excerpt**: «El mercado habanero tiene nueve marketplaces con inventario real y una docena con categorías vacías o solo piezas.»

### C079 — Registro automático de altas
- **Section**, **Lines**: §13 (L276), 276
- **Types**: contextual
- **Excerpt**: «El script `Auxiliares/herramientas/actualizar_informe.py` añade filas debajo del marcador y regenera el PDF.»

### C080 — Entradas omitidas en el registro
- **Section**, **Lines**: §13 (L295), 295
- **Types**: contextual
- **Excerpt**: «175 entradas adicionales no listadas / omitted»

### C081 — Sincronización de Revolico en partes
- **Section**, **Lines**: §14 (L756), 756
- **Types**: methodological
- **Excerpt**: «La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**. Cada 10 minutos un timer de systemd ejecuta `Auxiliares/herramientas/actualizar_revolico.py»»

### C082 — Última ejecución registrada de sincronización
- **Section**, **Lines**: §14 (L763), 763
- **Types**: result, contextual
- **Excerpt**: «2026-11-17T15:47:42+00:00 | 795373568 B | 48 partes de 16 MiB | `dadd2bffba615d8a…`»

### C083 — Detención manual del timer de scrapeo
- **Section**, **Lines**: §15 (L771), 771
- **Types**: result, contextual
- **Excerpt**: «se detuvo manualmente `revolico-scrape.timer` y su servicio a petición del usuario. El scraper había ampliado la BD de 3.682 a **6.332 anuncios** (520,6 MB) antes de detenerse»

### C084 — Renovación reciente de anuncios
- **Section**, **Lines**: §15 (L775), 775
- **Types**: result
- **Excerpt**: «El 99,3 % de los anuncios tiene `updated_on_by_user` en los últimos 7 días (mediana 1 día en los 189 autos)»

### C085 — Marcador `updatedOnToOrder` desactivado
- **Section**, **Lines**: §16 (L785), 785
- **Types**: methodological
- **Excerpt**: «El campo `updatedOnToOrder` del listado resultó ser un marcador de ranking y no de edición, así que el salto de descarga queda desactivado por defecto (`--skip-unchanged`)»

### C086 — Fuentes revisadas para requerimientos de fases 7–8
- **Section**, **Lines**: §17 (L793), 793
- **Types**: contextual
- **Excerpt**: «Fuentes académicas y repositorios revisados para definir los requerimientos del análisis (Fases 7-8):»

### C087 — Requerimientos derivados
- **Section**, **Lines**: §17 (L810), 810
- **Types**: methodological
- **Excerpt**: «La ponderación de preferencias del usuario y el producto interactivo quedan para la especialización futura.»

### C088 — Verificación en vivo de DfT/DVLA
- **Section**, **Lines**: §18 (L818), 818
- **Types**: citation-grounded
- **Excerpt**: «Verificado en vivo: publicado por Department for Transport + DVLA, actualizado 23/09/2026, Open Government Licence»

### C089 — VAHAN no accesible desde el entorno
- **Section**, **Lines**: §18 (L819), 819
- **Types**: contextual, citation-grounded
- **Excerpt**: «No accesible desde este entorno (error de transporte); el repo documenta 12 exportaciones mensuales 2025 y manifiesto de verificacion»

### C090 — BCC no accesible en vivo
- **Section**, **Lines**: §18 (L820), 820
- **Types**: contextual, citation-grounded
- **Excerpt**: «No accesible en vivo desde este entorno; citado en `Data/investigacion-mercado-automotor-cuba.md` y Resolución 102/2026»

### C091 — Redes sociales como fuente no estadística
- **Section**, **Lines**: §18 (L827), 827
- **Types**: contextual
- **Excerpt**: «No verificables como fuente estadística; requieren consentimiento y sin datos personales»

### C092 — Marco general de ocho pasos
- **Section**, **Lines**: §19 (L837–846), 837–846
- **Types**: contextual, methodological
- **Excerpt**: «Marco general (8 pasos, derivado de los trabajos revisados)»

### C093 — Fuentes de la adaptación a La Habana
- **Section**, **Lines**: §19 (L851), 851
- **Types**: result, contextual
- **Excerpt**: «Revolico (BD propia, 6.334 anuncios / 317 autos), concesionarios (Autocubana, Dongfeng, BDC One…), Gaceta/Decreto 163/2026, BCC (oficial) y elTOQUE (informal), salarios de la Resolución 14»

### C094 — Métodos adaptados del marco
- **Section**, **Lines**: §19 (L853), 853
- **Types**: methodological
- **Excerpt**: «comparables por modelo ±2 años y municipio; rentabilidad = reventa esperada − compra − reacondicionamiento − impuestos (Decreto 163/2026); asequibilidad = precio / salario; series con snapshots.»

### C095 — Activos existentes según el marco detallado
- **Section**, **Lines**: §20 (L873), 873
- **Types**: result, contextual
- **Excerpt**: «BD de 6.334 anuncios / 317 autos, esquema con 30 campos + auditoría, imágenes/teléfonos, snapshots de precios, normativa documentada, tasas y salarios referenciados, repositorios de modelos y dashboards.»

### C096 — Datos pendientes según el marco detallado
- **Section**, **Lines**: §20 (L875), 875
- **Types**: contextual
- **Excerpt**: «extracción estructurada de año/km/marca/modelo/combustible/transmisión desde `ad_json`/`apollo_full`; montos de costos ocultos; precios de transacción reales; estadísticas oficiales cubanas de parque y matriculaciones»

### C097 — Renombre de la fase 8
- **Section**, **Lines**: §21 (L883), 883
- **Types**: contextual
- **Excerpt**: «La fase 8 pasa a llamarse **Análisis de mercado, comparables y rentabilidad**.»

### C098 — Salidas del análisis descriptivo inicial
- **Section**, **Lines**: §22 (L892), 892
- **Types**: contextual
- **Excerpt**: «genera en `Data/analisis/`: `resumen_general.csv`, `precios_por_marca.csv`, `precios_por_municipio.csv`, `precios_por_anio.csv`, `outliers.csv`, `cobertura.csv`, `informe_descriptivo.md` y `dashboard.html`.»

### C099 — Resultados del análisis descriptivo inicial
- **Section**, **Lines**: §22 (L894), 894
- **Types**: result
- **Excerpt**: «Precio mediano **22.000 USD**, media 24.416,59 USD, IQR 11.375–35.000 USD, rango 600–95.000 USD.»

### C100 — Cobertura de campos derivados
- **Section**, **Lines**: §22 (L894), 894
- **Types**: result
- **Excerpt**: «Cobertura de campos derivados: marca 68,4 %, año 63,5 %, km 6,2 % (heurísticos, extraídos solo de título/descripción). Detectados 5 outliers por IQR.»

### C101 — Conversión diaria por año del vehículo
- **Section**, **Lines**: §23 (L902), 902
- **Types**: result, methodological
- **Excerpt**: «la conversión usa `precio_USD × TRMI elTOQUE` del día del anuncio (columna `Mediana` de `Anexos/Investigacion Cambios/trmi_USD.csv`)»

### C102 — Serie histórica de TRMI y precios
- **Section**, **Lines**: §23 (L904), 904
- **Types**: result
- **Excerpt**: «la TRMI pasó de 680 CUP/USD (09/07/2026) a 920 (16-17/11/2026); la mediana mensual CUP subió de 12,58 M (julio) a 20,7 M (noviembre).»

### C103 — Supuesto de anuncio activo
- **Section**, **Lines**: §23 (L903), 903
- **Types**: methodological
- **Excerpt**: «todos los registros tienen `status=PUBLISHED` y página verificada en la captura, por lo que se asume que son comprables; no se comprueba disponibilidad en tiempo real.»

### C104 — Generación de gráficas
- **Section**, **Lines**: §23 (L905), 905
- **Types**: contextual
- **Excerpt**: «usa matplotlib, seaborn y plotly (instalados) y genera 8 PNG + `dashboard_interactivo.html` en `Data/analisis/graficos/`.»

### C105 — Ausencia de campos estructurados en los JSON
- **Section**, **Lines**: §24 (L911), 911
- **Types**: result
- **Excerpt**: «**No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**: por eso `anio_est`, `marca_est` y `km_est` se derivan con regex del texto visible»

### C106 — Reporte de scrapeo y colas
- **Section**, **Lines**: §24 (L913), 913
- **Types**: result
- **Excerpt**: «`anuncios` 6.334 · `autos` 323 · `revision` 6.085 · `imagenes` 13.932 · `telefonos` 7.699 · BD 520,6 MB.»

### C107 — Reinicio automático del servicio
- **Section**, **Lines**: §25 (L920), 920
- **Types**: methodological
- **Excerpt**: «`revolico-scrape.service` ahora tiene `Restart=on-failure`, `RestartSec=30`, `StartLimitIntervalSec=300` y `StartLimitBurst=20`»

### C108 — Supuesto de disponibilidad de catálogos
- **Section**, **Lines**: §25 (L921), 921
- **Types**: methodological
- **Excerpt**: «Para concesionarios y páginas similares (`CATALOGOS`) se asume que todo el catálogo está disponible salvo que la página indique lo contrario y que se publicó el día de la captura (`fecha_publicacion = scraped_at`)»

### C109 — Causa del retraso en la clasificación
- **Section**, **Lines**: §26 (L928), 928
- **Types**: methodological
- **Excerpt**: «el timer ejecutaba `actualizar_revolico.py`, que solo corre el scraper y divide la BD, sin escribir nunca `autos`/`revision`.»

### C110 — Umbral de revisión de 4.000 anuncios
- **Section**, **Lines**: §27 (L943), 943
- **Types**: methodological
- **Excerpt**: «cuando `anuncios WHERE pagina_revisada=0`llega a **4.000** (configurable con `REVISAR_UMBRAL`), el aviso lanza `revolico-revisar.service`»

### C111 — Scraper de Telegram sin credenciales MTProto
- **Section**, **Lines**: §28 (L950), 950
- **Types**: contextual
- **Excerpt**: «No hay credenciales MTProto (`TELEGRAM_API_ID`/`TELEGRAM_API_HASH` vacías), así que se implementó `Auxiliares/herramientas/scraper_telegram_publico.py», que lee la vista pública `t.me/s/<canal>`»

### C112 — Primera corrida de Telegram
- **Section**, **Lines**: §28 (L952), 952
- **Types**: result
- **Excerpt**: «Corrida final (50 páginas): **152 mensajes**, **54 anuncios de autos** del canal `goldenbullbusinessfamilycars`, 45 con año detectable y **ninguno con precio explícito»»

### C113 — Base de datos de Telegram y descubrimiento de canales
- **Section**, **Lines**: §29 (L960, L966–971), 960–971
- **Types**: result
- **Excerpt**: «`canales` | 119» / «`anuncios` | 54» / «El descubrimiento usa 26 búsquedas en tgden.com y valida cada usuario con `t.me/s/`, filtrando por contexto cubano.»

### C114 — Modo de descubrimiento sin procesamiento
- **Section**, **Lines**: §32 (L995–1000), 995–1000
- **Types**: methodological
- **Excerpt**: «no hay descarga de anuncios, ni clasificación definitiva, ni inserción en `anuncios`/`autos`/`revision`»; «se detiene al llegar a `FECHA_MINIMA = 2021-01-01`»

### C115 — Parada por página sin enlaces nuevos
- **Section**, **Lines**: §33 (L1008), 1008
- **Types**: methodological
- **Excerpt**: «se detenga en cuanto una página no aporte **ningún enlace nuevo** (todos sus anuncios ya fueron vistos)»

### C116 — Mecanismo de la app Circuitos Habana
- **Section**, **Lines**: §35 (L1068–1074), 1068–1074
- **Types**: result, citation-grounded
- **Excerpt**: «La app **no usa una API privada**: hace scraping del canal público de Telegram `https://t.me/s/EmpresaElectricaDeLaHabana` con Jsoup y User-Agent de Chrome.»

### C117 — Restricciones de Docker y Overpass
- **Section**, **Lines**: §36 (L1084–1085), 1084–1085
- **Types**: contextual
- **Excerpt**: «el daemon Docker no arranca sin root en este entorno (`dockerd needs to be started with root privileges`), por lo que se descartó esa vía.»

### C118 — Optimización de pipelines y efecto medido
- **Section**, **Lines**: §37 (L1100–1102), 1100–1102
- **Types**: methodological, result
- **Excerpt**: «los anuncios de Revolico pasaron de 10.117 a **10.149** y los autos de 716 a **814**; quedan 3.351 URLs pendientes y 1.940 rechazadas.»

### C119 — Reporte automático de progreso
- **Section**, **Lines**: §38 (L1112), 1112
- **Types**: contextual
- **Excerpt**: «actualiza **`Data/progreso_reporte.md` cada 5 minutos** con:»

### C120 — Ampliación de límites de marketplaces
- **Section**, **Lines**: §39 (L1127), 1127
- **Types**: result
- **Excerpt**: «en minutos Autocubana pasó de 400 a **566** y Timbirichi de 110 a **170**, totalizando **2.121 anuncios**.»

## Iteration context — estado de F-V10-001..008

Evaluación descriptiva de las ocho observaciones transversales de `reviews/informe-tecnico-2026-11-27.forensic.md` (L991–1037) contra el texto de esta iteración. No se ha verificado el contenido de archivos externos: solo se cita lo que el documento declara.

- **F-V10-001 — KPIs, CSV y README (cuatro estados): PARCIALMENTE RESUELTA.** §59 (L1379) adopta 772 autos, 2.029 anuncios, 1.338 locales, 21.000 USD y 43.000 km, y L1381 incrusta marcadores `<!-- kpi:... -->` que se actualizan solos desde `kpis.csv`. Persisten §45 (L1214: 23.000 USD, 6,3 años, 34 marcas, 27 grupos), §58 (L1371: 2.014 anuncios, 44.125 km), §44 (L1206: 66 anomalías frente a 81) y el paralelo inglés de §59 (L1383: 744 autos, 2.014 anuncios).
- **F-V10-002 — Retirada de −5,43 % sin ablación ni literatura: PARCIALMENTE RESUELTA.** §59 (L1381) y §60 (L1389) explicitan la no significancia (p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05) y la registran en `MODELOS_Y_FUNCIONES.md`; §69 (L1469) declara el uso de IA. §34 (L1056) mantiene la cifra, §44 (L1206) la reutiliza con salvedad y §45 (L1214) sin ella; no hay ablación, test pareado ni contraste con los trabajos sobre no linealidad edad–precio.
- **F-V10-003 — Densidad sin declaración de IA: RESUELTA.** §69 (L1467–1471) añade declaración bilingüe de uso de IA para redacción, edición quirúrgica, revisión bibliográfica y auditoría, y nombra la skill `review` y los artefactos conservados. No detalla herramientas ni protocolo de supervisión.
- **F-V10-004 — TRMI diario frente a fijo, 920 frente a 930: PARCIALMENTE RESUELTA.** §23 (L902) incorpora la «Aclaración vigente»: el pipeline usa 930 CUP/USD fijos de `config.py` y la serie diaria es solo referencia histórica; §52 (L1297) coincide. L904 sigue reportando 920 sin registrar el cambio y el paralelo inglés (L907) continúa describiendo conversión con TRMI diaria.
- **F-V10-005 — Conclusión que niega la fase 8: PARCIALMENTE RESUELTA.** §12 español (L139) afirma la implementación y §2 (L38) añade nota de actualización; la tabla de §2 (L33) mantiene «Pendiente» mitigada por la nota. La Parte II conserva «not implemented yet» (L270) y la fase 8 «Pending» con producto interactivo (L164).
- **F-V10-006 — Diferenciación solo contra el repositorio egipcio: NO RESUELTA.** §34 (L1018, L1058–1060) sigue siendo el único pasaje comparativo, por escala de datos; §70 (L1477) añade cuatro referencias verificadas pero ningún contraste argumentativo con los vecinos académicos. El inventario registra una sola señal de novedad (C011, L1018).
- **F-V10-007 — Fuentes nominales incompletas y artefactos fuera del árbol: PARCIALMENTE RESUELTA.** §70 (L1477–1479) crea la convención de 38 referencias en `Data/referencias.md`, nombra cuatro verificadas y marca el resto como `(metadata incomplete)`; §69 (L1469) sitúa la auditoría en `reviews/`. Persisten la ausencia de citas numeradas en el cuerpo, el índice de gacetas en `~/Utilidades/Leyes/gaceta_catalog.json` (§10, L120) y la inaccesibilidad de VAHAN y BCC (§18, L819–820).
- **F-V10-008 — Muestra de 22 observaciones ausente del relato: RESUELTA.** §59 (L1381) declara 28 observaciones completas de 981 candidatas, R² 0,277 y p del F 0,411, con marcadores automáticos y referencia a `MODELOS_Y_FUNCIONES.md`; §60 (L1389) reitera la no significancia. La cifra sustituye a la omitida en la iteración 1 y queda dentro del relato.

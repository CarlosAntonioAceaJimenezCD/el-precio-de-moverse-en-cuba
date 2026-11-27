---
type: audit-artifact
phase: e1-claims
slug: informe-tecnico-2026-11-27
generated_at: 2026-11-27T05:31:49Z
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27/informe-tecnico-2026-11-27.text.md
language: es
---

# Claim Inventory

## Summary

- Total: 191
- Load-bearing: 14 · Supporting: 65 · Contextual: 112
- By type: result 86 · methodological 66 · novelty 0 · contextual 122 · definitional 16 · citation-grounded 21

Nota de alcance: el documento es bilingüe y varias secciones aparecen duplicadas en inglés (Parte II, L141–268, y bloques `**EN.**` a lo largo de §14–68). El inventario registra cada afirmación una sola vez, usando como excerpt la versión en español cuando existe; la versión inglesa se cita en los campos de evidencia interna. No hay páginas numeradas en el texto cacheado, por lo que `Section` identifica la sección y `Lines` las líneas del archivo. El documento no emplea citas numeradas tipo `[N]`; por eso `External evidence cited` se marca «— (sin citas numeradas)» y las fuentes nombradas se consignan, cuando procede, en `Notes`. Las filas del registro de altas (§13, L276–748) son metadatos de archivos y no se inventarían una por una; solo se registran las que afirman una propiedad verificable de una herramienta.

## Load-bearing claims

### C001 — Análisis y modelo de rentabilidad (fase 8) aún no implementados; producto interactivo diferido

- **Section**: §12. Conclusiones (Parte I); §21. Cambio de objetivo
- **Lines**: 137 (eco en 16, 866, 877–884, 266)
- **Types**: result, contextual
- **Excerpt**: «El análisis de mercado y el modelo de rentabilidad (fase 8) aún no están implementados; el producto interactivo se difiere a una especialización futura.»
- **Restated**: A la fecha de la conclusión no existía un modelo de rentabilidad operativo ni un recomendador interactivo entregado; sería falso si cualquiera de los dos estuviera implementado en ese momento.
- **Internal evidence cited**: §1 (L16), §20.8 (L866), §21 (L877–884), §12 EN (L266), Part II §1 (L145).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: La Parte II (L145) conserva el objetivo anterior de recomendación interactiva; §21 atribuye el cambio a una petición del usuario. Existe tensión con §34, §58 y §59, donde sí se documentan análisis y modelo ejecutados.

### C002 — Fase activa sexta y estado de las nueve fases

- **Section**: §2. Estado y fases (Parte I)
- **Lines**: 22–34
- **Types**: result, contextual
- **Excerpt**: «Las fases se redefinieron para que la fase activa sea la sexta. Estado a 17/11/2026:»
- **Restated**: A 17/11/2026 las fases 1–5 estaban completadas, la 6 en curso y las 7–9 pendientes; sería falso si otra fase estuviera activa.
- **Internal evidence cited**: Tabla de fases (L24–34); §2 EN (L151–163).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: La creación del informe y del README se declara transversal (L36), sin alterar este estado.

### C003 — Marco normativo vigente: Decreto 163/2026 y resolución 312/2026 derogada

- **Section**: §12. Conclusiones (Parte I); §4. Fase 1; §10. Marco legal; §52. Ampliación de fuentes
- **Lines**: 134 (eco en 56, 114–115, 1299)
- **Types**: citation-grounded, contextual
- **Excerpt**: «El marco regulatorio vigente es el Decreto 163/2026 y el paquete de resoluciones citado.»
- **Restated**: La norma rectora de importación y comercialización es el Decreto 163/2026 (Gaceta 65 Ordinaria, 04/08/2026, vigente desde el 11/08/2026), que deroga el Decreto 119/2024, y la Resolución 312/2026 quedó derogada por la 340/2026; sería falso si rigiera otra norma.
- **Internal evidence cited**: §4 (L56), §10 (L114–115), §52 (L1299), §12 EN (L263), §4 EN (L185).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Fuentes nombradas: Gaceta Oficial No. 65 Ordinaria y resoluciones 104/17/52/171–175/312/340/102 de 2026.

### C004 — Nueve marketplaces con inventario real

- **Section**: §12. Conclusiones (Parte I); §5. Fase 2
- **Lines**: 133 (eco en 62)
- **Types**: result
- **Excerpt**: «El mercado habanero tiene nueve marketplaces con inventario real y una docena con categorías vacías o solo piezas.»
- **Restated**: El conteo de marketplaces con inventario real es nueve y el de sitios con categorías vacías o solo piezas es aproximadamente una docena; sería falso si los conteos difirieran.
- **Internal evidence cited**: §5 (L60–64), §12 EN (L262), §5 EN (L189–191).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: La enumeración de L62 da cifras para siete marketplaces y menciona otros dos sin cifra; la cifra «nueve» no se desglosa en una tabla.

### C005 — No elusión de anti-automatización y registro de HTTP 403/429

- **Section**: §10. Marco legal para la recolección y el análisis de datos
- **Lines**: 116 (eco en 127, 245)
- **Types**: methodological, result
- **Excerpt**: «No se eluden mecanismos anti-automatización; los HTTP 403/429 se registran como limitación.»
- **Restated**: La recolección respetó los mecanismos anti-automatización y trató los HTTP 403/429 como limitaciones documentadas, no como obstáculos sorteados.
- **Internal evidence cited**: §9 (L108), §11 (L127), §10 EN (L245).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Se declara además que el contenido de carrosw no se falsificó (L127).

### C006 — Sostenibilidad del scraping: ritmo, sesión y reanudación

- **Section**: §12. Conclusiones (Parte I)
- **Lines**: 135 (eco en 124–129, 264)
- **Types**: methodological, result
- **Excerpt**: «El scraping sostenible depende del ritmo, la sesión y la reanudación, no principalmente del fingerprint TLS.»
- **Restated**: Según el informe, el factor principal de la sostenibilidad del scraping es el ritmo, la sesión y la reanudación, y no el fingerprint TLS; sería falso si el fingerprint TLS fuera el determinante principal.
- **Internal evidence cited**: §11 (L124–129), §6 (L70), §37 (L1096), §12 EN (L264).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Afirmación causal sin diseño comparativo explícito en el texto; se registra como atribución del informe.

### C007 — Eficiencia comparada de Telegram MTProto, Facebook GQL y WAHA

- **Section**: §15. Eficiencia de Telegram, WhatsApp y Facebook
- **Lines**: 763–765
- **Types**: methodological, result, contextual
- **Excerpt**: «Para obtener más datos del mercado habanero, la ruta más eficiente es Telegram MTProto (`telethon`, ya integrado): sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`. Le sigue Facebook GQL»
- **Restated**: El orden de eficiencia declarado es Telegram MTProto, luego Facebook GQL, luego WAHA para WhatsApp, con Playwright/Selenium como último recurso; sería falso si otro orden fuera el sostenido por la evidencia del proyecto.
- **Internal evidence cited**: §15 EN (L765), §28–29 (L946–969), §35 (L1064–1070).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Comparación cualitativa; el texto no adjunta una medición de tiempo por fuente.

### C008 — Anuncios como precios pedidos, no transaccionados

- **Section**: §18. Auditoría de procedencia
- **Lines**: 822, 827 (eco en 829)
- **Types**: methodological, definitional, citation-grounded
- **Excerpt**: «No son estadísticas oficiales; son precios **pedidos**, no transaccionados»
- **Restated**: Las señales de precio de marketplaces y redes son precios anunciados y no sustituyen estadísticas oficiales de transacción; sería falso si se tratara de precios efectivamente transaccionados.
- **Internal evidence cited**: §18 (L822, L827), §19 (L851), §20 (L871), §18 EN (L829).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: La conclusión de L827 añade que las fuentes oficiales y gremiales sirven de contexto y validación.

### C009 — Primera ejecución del modelo hedónico: −5,43 % anual

- **Section**: §34. Esqueleto de análisis de rentabilidad — Línea base real de la primera ejecución
- **Lines**: 1037–1052
- **Types**: result, methodological
- **Excerpt**: «El modelo `log(precio) ~ car_age + condition_score + C(brand_tier)` da una depreciación media de **−5,43 % anual** (p<0,001), con primas de +21 % para premium y −22 % para tier medio frente al desconocido.»
- **Restated**: En esa ejecución el modelo estimó una depreciación anual de −5,43 % con p<0,001 y primas de +21 %/−22 %; sería falso si esos coeficientes no correspondieran a la corrida descrita.
- **Internal evidence cited**: §34 (L1041–1052), §44 (L1202), §45 (L1210), §34 EN (L1058).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Cifra posteriormente reformulada como no significativa en §59 (L1377) y §60 (L1385); ambas versiones coexisten en el documento.

### C010 — Estado final del conjunto de datos al 23/11/2026

- **Section**: §59. Storytelling alineado con los datos finales
- **Lines**: 1375 (eco en 1275–1277, 1365–1369)
- **Types**: result
- **Excerpt**: «El relato ahora usa **744 autos únicos**, **2.014 anuncios limpios** (1.323 locales y 691 de importación), mediana local de **21.000 USD**, kilometraje mediano de **44.125 km**, 50 marcas, 100 grupos comparables y 81 anomalías.»
- **Restated**: El dataset vigente para el relato final tiene 744 autos únicos y 2.014 anuncios limpios, con mediana local de 21.000 USD y kilometraje mediano de 44.125 km; sería falso si el pipeline regenerado produjera otros totales.
- **Internal evidence cited**: §51 (L1275–1277), §58 (L1365–1369), §59 EN (L1379).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: §58 reporta además 961 anuncios en `itencel.sqlite` e `integrity_check=ok`.

### C011 — Depreciación final no significativa tras corregir kilometraje

- **Section**: §59. Storytelling alineado con los datos finales; §60. Inventario de funciones y modelos
- **Lines**: 1377, 1385
- **Types**: result, methodological
- **Excerpt**: «el modelo actual no encuentra una pendiente anual significativa tras corregir el kilometraje, y la prima premium dejó de afirmarse como cifra»
- **Restated**: En la corrida vigente la pendiente anual y la prima premium no son estadísticamente significativas (p mínimo 0,165; VIF 1,13–1,58; Kruskal-Wallis p = 1e−05); sería falso si los coeficientes alcanzaran significancia.
- **Internal evidence cited**: §60 (L1385), §59 (L1377), §60 EN (L1387).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Entra en tensión con C009, correspondiente a una ejecución anterior.

### C012 — Anuarios del ONEI sin series de parque automotor ni matriculaciones

- **Section**: §56. Análisis de los anuarios y estructura de GitHub
- **Lines**: 1347
- **Types**: result, citation-grounded
- **Excerpt**: «**No hay series de parque automotor ni de matriculaciones**, por lo que esa laguna signalada en `NECESIDADES.md` no se resuelve con los anuarios; la corrección quedó registrada.»
- **Restated**: Los 12 anuarios del ONEI revisados no contienen series de parque automotor ni de matriculaciones; sería falso si alguna de esas series estuviera presente.
- **Internal evidence cited**: §52 (L1295), §53 (L1313), §56 (L1347), §56 EN (L1351).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Corrige la expectativa registrada antes en §52 y §53 y la laguna señalada en `NECESIDADES.md`.

### C013 — Estimación de retención: inferencia de diseño, no medición

- **Section**: §63. Calidad del storytelling como puerta de entrada
- **Lines**: 1413
- **Types**: methodological, contextual
- **Excerpt**: «La estimación de retención (`Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md`) es **inferencia de diseño, no medición**: de cada 100 visitantes, ~58 leerían el primer párrafo, ~16 llegarían al cierre y ~5 volverían con intención de consulta.»
- **Restated**: Las cifras de retención son proyecciones de diseño y no datos observados; sería falso si se presentaran como mediciones de tráfico real.
- **Internal evidence cited**: §63 (L1411–1413), §63 EN (L1415).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: La proyección condicionada es de ~22–25 finalizaciones y ~18–22 retornos.

### C014 — Regla de las 10 páginas y resultados repetidos

- **Section**: §12. Conclusiones (Parte I); §7. Fase 4
- **Lines**: 136 (eco en 76, 265)
- **Types**: methodological, result
- **Excerpt**: «La regla de las 10 páginas evitó consumir resultados repetidos.»
- **Restated**: La regla de parar tras 10 páginas sin enlaces útiles tuvo como efecto evitar el consumo de resultados repetidos; sería falso si esa regla no hubiera incidido en la deduplicación.
- **Internal evidence cited**: §7 (L76–84), §12 EN (L265).
- **External evidence cited**: — (sin citas numeradas).
- **Novelty signals**: Ninguno.
- **Notes**: Afirmación causal atribuida al informe; las tres búsquedas pararon en las páginas 19, 11 y 22.

## Supporting claims (65)

### C015 — 17 empresas autorizadas y precios de referencia

- **Section**: §4. Fase 1 — Marco normativo y regulatorio
- **Lines**: 56
- **Types**: result, citation-grounded
- **Excerpt**: «Se documentaron **17 empresas autorizadas** a importar y comercializar vehículos [...] precios de referencia (BDC One 14.849–31.478 EUR; Dongfeng desde 21.900 EUR; Finauto desde 15.500 EUR; ATR Export con 46 modelos)»
- **Restated**: El informe registra 17 empresas autorizadas y rangos de precios de referencia por distribuidor.
- **Internal evidence cited**: §4 (L56), §4 EN (L185).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: `Data/investigacion-mercado-automotor-cuba.md`.

### C016 — Resoluciones sectoriales cotejadas

- **Section**: §4. Fase 1; §10. Marco legal
- **Lines**: 56, 115
- **Types**: citation-grounded, contextual
- **Excerpt**: «Se cotejaron las resoluciones 104/2026 (MINCEX), 17/2026 (MINCIN), 52/2026 (MITRANS), 171–175/2026 (MFP), 312/2026, derogada por 340/2026 (Aduana) y 102/2026 (BCC).»
- **Restated**: El informe declara cotejadas siete resoluciones de 2026, con la 312/2026 marcada como derogada por la 340/2026.
- **Internal evidence cited**: §4 (L56), §10 (L115), §4 EN (L185).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Las fuentes se nombran, no se numeran como citas.

### C017 — Consolidación de resultados de búsqueda

- **Section**: §5. Fase 2 — Descubrimiento y verificación de fuentes
- **Lines**: 60
- **Types**: result
- **Excerpt**: «Se consolidaron **409 resultados, 400 únicos**.»
- **Restated**: La consolidación produjo 409 resultados, de los cuales 400 eran únicos.
- **Internal evidence cited**: §5 (L60), §5 EN (L189).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Dos búsquedas iniciales en DuckDuckGo, 30 páginas cada una, bloqueadas por CAPTCHA.

### C018 — Sitios inventariados y verificados

- **Section**: §5. Fase 2
- **Lines**: 60, 62
- **Types**: result
- **Excerpt**: «Se inventariaron **35 sitios** de compraventa en `Data/mercados-compraventa-cuba.md` [...] Se verificaron **40 sitios/URLs**.»
- **Restated**: El inventario comprendió 35 sitios de compraventa y la verificación cubrió 40 sitios o URLs.
- **Internal evidence cited**: §5 (L60, L62), §5 EN (L189, L191).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C019 — Marketplaces con sección activa y sus conteos

- **Section**: §5. Fase 2
- **Lines**: 62
- **Types**: result
- **Excerpt**: «Marketplaces con sección activa: Autocubana (667 vehículos), iTENCEL (951), VentaCuba (801 carros/camionetas), Timbirichi (281 carros), Revolico (112 enlaces en la primera página), Cogetucarro (5.225 anuncios), Cubisima (155 fichas), Apululu y Carros.com Cuba.»
- **Restated**: Los conteos declarados por marketplace son 667, 951, 801, 281, 112 enlaces, 5.225 y 155 fichas, más dos sitios sin cifra.
- **Internal evidence cited**: §5 (L62), §5 EN (L191), §12 (L133).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Mezcla unidades heterogéneas (vehículos, anuncios, enlaces de primera página).

### C020 — Correcciones de clasificación de sitios

- **Section**: §5. Fase 2
- **Lines**: 62
- **Types**: result
- **Excerpt**: «Se corrigieron clasificaciones: Mercadoba y Fagales Market sin sección real; TuCuevita, Mercubano, Mercandil, Revoltillo, QvaVentas [...] con categoría vacía; BizneCubano, Katapulk, A la Venta, Pymes Bulevar, MeroliCU y Rico Cuba son de piezas, motos o servicios.»
- **Restated**: Diecisiete sitios fueron reclasificados en tres grupos: sin sección real, con categoría vacía y de piezas/motos/servicios.
- **Internal evidence cited**: §5 (L62), §5 EN (L191), §12 (L133).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Sustenta la conclusión C004.

### C021 — 14 organismos con competencia sobre el mercado

- **Section**: §5. Fase 2
- **Lines**: 64
- **Types**: result, contextual
- **Excerpt**: «Se documentaron **14 organismos** con competencia sobre el mercado: Consejo de Ministros/Estado, MINCEX, MINCIN, MITRANS, CEMA, MFP, ONAT, Aduana General, BCC, MININT, MINJUS, MEP, MINREX y MINSAP.»
- **Restated**: El informe enumera 14 organismos con competencia sobre el mercado automotor cubano.
- **Internal evidence cited**: §5 (L64), §5 EN (L193).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C022 — 61 repositorios clonados

- **Section**: §6. Fase 3 — Infraestructura técnica y herramientas
- **Lines**: 68
- **Types**: result
- **Excerpt**: «Se clonaron **61 repositorios** en `Auxiliares/Repositorios` con `--depth 1` (2,2 GB, 61 entradas `OK`).»
- **Restated**: La clonación produjo 61 repositorios, 2,2 GB y 61 entradas registradas como `OK`.
- **Internal evidence cited**: §6 (L68), §6 EN (L197).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C023 — Clasificación y selección de proyectos CAPTCHA

- **Section**: §6. Fase 3
- **Lines**: 68
- **Types**: result
- **Excerpt**: «Se clasificaron **92 proyectos** de CAPTCHA en `Data/github-captcha-repos.md` y se seleccionaron 9.»
- **Restated**: Se clasificaron 92 proyectos de CAPTCHA y se seleccionaron 9.
- **Internal evidence cited**: §6 (L68), §6 EN (L197).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C024 — Versiones del entorno y servicios de renderizado

- **Section**: §6. Fase 3
- **Lines**: 70
- **Types**: result, methodological
- **Excerpt**: «Se creó `Auxiliares/.venv` con patchright 1.64.4, PyPasser 1.1.0, Scrapling 0.5.1, ddddocr 1.6.1, playwright 1.65.2, curl_cffi 0.17.0, trafilatura, pandas, numpy, onnxruntime 1.32.0, ddgs 9.16.1 y tenacity 9.2.1. Se usa el Chromium del sistema y FlareSolverr 3.5.2 en Docker»
- **Restated**: El entorno declara versiones específicas de once paquetes y el uso de Chromium del sistema con FlareSolverr 3.5.2.
- **Internal evidence cited**: §6 (L70), §6 EN (L199).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C025 — Regla de parada tras 10 páginas y definición de «útil»

- **Section**: §7. Fase 4 — Corpus documental y trabajos investigativos
- **Lines**: 76
- **Types**: methodological, definitional
- **Excerpt**: «Tres búsquedas con la regla de parar tras 10 páginas sin enlaces útiles (útil = primera aparición de un trabajo investigativo automotriz)»
- **Restated**: La regla de parada se define como 10 páginas consecutivas sin enlaces útiles, donde «útil» significa la primera aparición de un trabajo investigativo automotriz.
- **Internal evidence cited**: §7 (L76–82), §7 EN (L205–211).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Operacionaliza la conclusión C014.

### C026 — Primera búsqueda de trabajos investigativos

- **Section**: §7. Fase 4
- **Lines**: 80
- **Types**: result
- **Excerpt**: «`mercado automovilistico trabajos investigativos` | 112 | 1.086 | 11 | página 19»
- **Restated**: La primera búsqueda recorrió 112 páginas, devolvió 1.086 resultados, 11 útiles y se detuvo en la página 19.
- **Internal evidence cited**: §7 (L80), §7 EN (L209).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C027 — Segunda búsqueda de trabajos investigativos

- **Section**: §7. Fase 4
- **Lines**: 81
- **Types**: result
- **Excerpt**: «`rentabilidad del precio de automoviles trabajos investigativos` | 24 | 226 | 2 | página 11»
- **Restated**: La segunda búsqueda recorrió 24 páginas, devolvió 226 resultados, 2 útiles y se detuvo en la página 11.
- **Internal evidence cited**: §7 (L81), §7 EN (L210).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C028 — Tercera búsqueda de trabajos investigativos

- **Section**: §7. Fase 4
- **Lines**: 82
- **Types**: result
- **Excerpt**: «`calidad precio mercado automotriz trabajo investigativo` | 23 | 230 | 10 | página 22»
- **Restated**: La tercera búsqueda recorrió 23 páginas, devolvió 230 resultados, 10 útiles y se detuvo en la página 22.
- **Internal evidence cited**: §7 (L82), §7 EN (L211).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C029 — Resultados de descarga del corpus

- **Section**: §7. Fase 4
- **Lines**: 84
- **Types**: result
- **Excerpt**: «descarga inicial **93 OK / 17 fallos**, rentabilidad **23 OK / 10 fallos**, calidad/precio **78 OK / 36 fallos**, con `manifest.jsonl` e `indice.md».
- **Restated**: Las tres tandas de descarga produjeron 93/17, 23/10 y 78/36 aciertos y fallos respectivamente.
- **Internal evidence cited**: §7 (L84), §7 EN (L213).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C030 — Esquema SQLite por tienda

- **Section**: §8. Fase 5 — Diseño del esquema de datos y del pipeline
- **Lines**: 88
- **Types**: methodological, definitional
- **Excerpt**: «Se diseñó una base SQLite por tienda con una tabla `vehiculos`: identificación (`url`, `shop`, `title`, `status`, `scraped_at`), metadatos y 30 campos estructurados [...] además de campos sin normalizar (`tables_json`, `jsonld_json`, `raw_html`, ...)»
- **Restated**: El esquema declarado comprende una tabla `vehiculos` por tienda con cinco campos de identificación, 30 campos estructurados y campos sin normalizar.
- **Internal evidence cited**: §8 (L88), §8 EN (L217).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Los nombres de campos difieren entre la versión española y la inglesa.

### C031 — Adaptadores por dominio y renderizado opcional

- **Section**: §8. Fase 5
- **Lines**: 88
- **Types**: methodological
- **Excerpt**: «El scraper `scrape_concesionarios.py` usa adaptadores por dominio y renderizado opcional con Playwright.»
- **Restated**: El scraper declarado usa un adaptador por dominio y puede activar renderizado con Playwright.
- **Internal evidence cited**: §8 (L88), §8 EN (L217).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C032 — Fase 6: 11 bases y 256 filas

- **Section**: §9. Fase 6 — Scraping y captura (en curso)
- **Lines**: 92
- **Types**: result
- **Excerpt**: «Se prepararon 11 bases y se obtuvieron **256 filas**»
- **Restated**: En el estado descrito se prepararon 11 bases de datos y se capturaron 256 filas.
- **Internal evidence cited**: §9 (L92–106), §9 EN (L221–235).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Cifra de la síntesis inicial; las secciones posteriores reportan volúmenes mucho mayores.

### C033 — Desglose de filas por tienda

- **Section**: §9. Fase 6
- **Lines**: 94–106
- **Types**: result
- **Excerpt**: «| AGN Motors | 60 | 45 | [...] | Chinautos Cuba | 70 | 0 | [...] | Finauto | 45 | 34 |»
- **Restated**: El desglose declara 11 tiendas con sus recuentos de filas totales y filas con precio.
- **Internal evidence cited**: §9 (L94–106), §9 EN (L223–235).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: La suma de las filas del desglose coincide con las 256 declaradas en L92.

### C034 — Exclusiones por bloqueo técnico en Fase 6

- **Section**: §9. Fase 6
- **Lines**: 108
- **Types**: result
- **Excerpt**: «Excluidas por bloqueo técnico: carrosw (HTTP 403 con Bot Verification), LlamaCuba (timeout) y SASA/DIVEP (sin catálogo).»
- **Restated**: Tres fuentes quedaron excluidas por causas técnicas específicas: 403 con verificación de bot, timeout y ausencia de catálogo.
- **Internal evidence cited**: §9 (L108), §11 (L127), §9 EN (L237).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C035 — Cambio de buscador y manejo de HTTP 202

- **Section**: §11. Problemas y soluciones
- **Lines**: 124–125
- **Types**: methodological, result
- **Excerpt**: «CAPTCHA en paginación DDG | Yahoo + visitas directas; después sesión con `vqd`. [...] HTTP 202 y página "anomaly" | Pausa 7–10 s con jitter, backoff exponencial y cooldown.»
- **Restated**: El informe atribuye a Yahoo y a una sesión `vqd` la respuesta al CAPTCHA, y a pausas de 7–10 s con jitter y backoff el manejo de HTTP 202.
- **Internal evidence cited**: §11 (L124–125), §5 (L60), §11 EN (L253–254).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C036 — Deduplicación por título, prefijo y dominio

- **Section**: §11. Problemas y soluciones
- **Lines**: 129
- **Types**: methodological
- **Excerpt**: «Repetidos y mirrors | Deduplicación por título normalizado, prefijo y dominio.»
- **Restated**: La estrategia de deduplicación declarada combina título normalizado, prefijo y dominio.
- **Internal evidence cited**: §11 (L129), §11 EN (L258).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C037 — Esquema de sincronización de Revolico en partes

- **Section**: §14. Sincronización automática de Revolico
- **Lines**: 752
- **Types**: methodological, result
- **Excerpt**: «La BD `Data/Revolico/revolico.sqlite` **no se versiona como archivo único**. Cada 10 minutos un timer de systemd ejecuta `Auxiliares/herramientas/actualizar_revolico.py`: corre el scraper incremental, divide la BD en partes de 16 MiB [...] sube solo las partes que cambiaron»
- **Restated**: La base no se versiona como archivo único sino en fragmentos de 16 MiB actualizados cada 10 minutos, con reconstrucción verificada por hash.
- **Internal evidence cited**: §14 (L752, L754), §14 (L759).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Esquema posteriormente complementado con Git LFS (§30) y con chunks de 10 MB (§54).

### C038 — Última ejecución registrada de la sincronización

- **Section**: §14. Sincronización automática de Revolico
- **Lines**: 759
- **Types**: result
- **Excerpt**: «| 2026-11-17T15:47:42+00:00 | 795373568 B | 48 partes de 16 MiB | `dadd2bffba615d8a…` |»
- **Restated**: La fila de sincronización registra 795.373.568 bytes, 48 partes de 16 MiB y un SHA-256 que comienza con `dadd2bffba615d8a`.
- **Internal evidence cited**: §14 (L756–759).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: El hash aparece truncado en el documento.

### C039 — Parada manual del timer de scrapeo

- **Section**: §15. Eficiencia de Telegram, WhatsApp y Facebook — Nota
- **Lines**: 767
- **Types**: result
- **Excerpt**: «se detuvo manualmente `revolico-scrape.timer` y su servicio a petición del usuario. El scraper había ampliado la BD de 3.682 a **6.332 anuncios** (520,6 MB) antes de detenerse; no se generaron partes»
- **Restated**: El scraper elevó la base de 3.682 a 6.332 anuncios antes de detenerse manualmente, sin producir partes; `revolico-git.timer` permaneció activo.
- **Internal evidence cited**: §15 (L767), §15 EN (L767), §24 (L909).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C040 — Permanencia de anuncios y ausencia de caducidad fija

- **Section**: §15. Eficiencia — Permanencia
- **Lines**: 771
- **Types**: result, citation-grounded
- **Excerpt**: «las Condiciones de Uso de Revolico (23/09/2026) no fijan un plazo de caducidad de los anuncios. Empíricamente, un anuncio con `updated_on_by_user=2024-12-17` seguía en HTTP 200 el 17/11/2026 (~699 días)»
- **Restated**: Las condiciones de uso no establecen caducidad y se observó un anuncio de 2024-12-17 aún accesible 699 días después.
- **Internal evidence cited**: §15 (L771), §15 EN (L771), §31 (L983–985).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: Condiciones de Uso de Revolico (23/09/2026).

### C041 — Frecuencia de renovación de anuncios

- **Section**: §15. Eficiencia — Permanencia
- **Lines**: 771
- **Types**: result
- **Excerpt**: «El 99,3 % de los anuncios tiene `updated_on_by_user` en los últimos 7 días (mediana 1 día en los 189 autos)»
- **Restated**: El 99,3 % de los anuncios tiene fecha de actualización en los últimos siete días y la mediana en los 189 autos es de un día.
- **Internal evidence cited**: §15 (L771), §15 EN (L771).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C042 — Limpieza ejecutada sobre 6.332 anuncios

- **Section**: §15. Eficiencia — Limpieza ejecutada
- **Lines**: 769
- **Types**: result
- **Excerpt**: «`limpiar_revolico.py` conservó **304 autos** en la tabla `autos` y registró **6.028 exclusiones** en `revision` (5.983 no vehículo 4+ ruedas, 45 sin datos necesarios, 0 páginas sin datos suficientes).»
- **Restated**: La limpieza conservó 304 autos y registró 6.028 exclusiones, desglosadas en 5.983, 45 y 0.
- **Internal evidence cited**: §15 (L769), §15 EN (L769), §16 (L783).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C043 — Conservación de filas originales y columnas de auditoría

- **Section**: §15. Eficiencia — Limpieza ejecutada
- **Lines**: 769
- **Types**: methodological, result
- **Excerpt**: «No se borraron filas originales: `anuncios` conserva las columnas de auditoría `es_auto`, `motivo_exclusion`, `pagina_revisada` y `datos_necesarios`. Se añadieron `microbús/guagua/ómnibus/bus` a los patrones de inclusión.»
- **Restated**: Ninguna fila original fue eliminada y la tabla conserva cuatro columnas de auditoría, además de ampliarse la lista de términos de inclusión.
- **Internal evidence cited**: §15 (L769), §15 EN (L769).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C044 — Pipeline de tres etapas con colas persistentes

- **Section**: §16. Pipeline de colas
- **Lines**: 775–779
- **Types**: methodological, result
- **Excerpt**: «`scrape_revolico_pipeline.py` separa el trabajo en tres etapas simultáneas con colas persistentes en `Data/Revolico/pipeline.sqlite`»
- **Restated**: El pipeline declarado ejecuta descubrimiento, descarga y procesamiento como tres etapas simultáneas con colas persistentes.
- **Internal evidence cited**: §16 (L775–779), §16 EN (L785).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C045 — Commit por lotes de 25 anuncios

- **Section**: §16. Pipeline de colas
- **Lines**: 779
- **Types**: methodological
- **Excerpt**: «Cada **25 anuncios procesados** (aceptados o rechazados) se hace un commit por lotes en `anuncios`/`autos`/`imagenes`/`telefonos` o en `revision`.»
- **Restated**: El tamaño de lote declarado para los commits es 25 anuncios procesados, aceptados o rechazados.
- **Internal evidence cited**: §16 (L779), §20 (L863).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C046 — Marcador de fecha del listado y salto de descarga desactivado

- **Section**: §16. Pipeline de colas
- **Lines**: 781
- **Types**: methodological, result
- **Excerpt**: «El campo `updatedOnToOrder` del listado resultó ser un marcador de ranking y no de edición, así que el salto de descarga queda desactivado por defecto (`--skip-unchanged`)»
- **Restated**: El campo `updatedOnToOrder` interpreta como ranking y no como edición, por lo que la opción de omitir descargas permanece desactivada por defecto.
- **Internal evidence cited**: §16 (L781), §16 EN (L785).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C047 — Prueba de una página del pipeline de colas

- **Section**: §16. Pipeline de colas
- **Lines**: 783
- **Types**: result
- **Excerpt**: «Prueba con 1 página: **119 enlaces** descubiertos y procesados, 7 lotes de 25, BD principal de 6.332 a **6.334 anuncios** y de 304 a **317 autos**.»
- **Restated**: La prueba procesó 119 enlaces en siete lotes y elevó la base de 6.332 a 6.334 anuncios y de 304 a 317 autos.
- **Internal evidence cited**: §16 (L783), §16 EN (L785).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C048 — Aporte metodológico del estudio PUCE

- **Section**: §17. Guía de análisis de mercado
- **Lines**: 793
- **Types**: contextual, citation-grounded
- **Excerpt**: «Asimetría de información (Akerlof); clasificación de calidad por antigüedad (≤5 años alta, >5 años con defectos); encuesta a 130 comerciantes; medición de costos ocultos y margen de reventa»
- **Restated**: El trabajo PUCE aporta el marco de asimetría de información, una clasificación por antigüedad y una encuesta a 130 comerciantes.
- **Internal evidence cited**: §17 (L793), §19 (L837), §19 (L849).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: PDF de la PUCE en `Hombros/01_PDFs/`.

### C049 — Requerimientos derivados para el análisis

- **Section**: §17. Guía de análisis de mercado
- **Lines**: 806
- **Types**: methodological, definitional
- **Excerpt**: «**Requerimientos derivados:** (1) esquema común con precio+moneda normalizada [...] (4) modelo de rentabilidad = precio de reventa esperado − precio de compra − costos − impuestos; (5) serie temporal con snapshots; (6) dashboard de mercado; (7) validación, dedup y sin datos personales.»
- **Restated**: El informe deriva siete requerimientos para las fases 7–8, incluida la fórmula del modelo de rentabilidad.
- **Internal evidence cited**: §17 (L806), §19 (L849), §20 (L863–865).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C050 — Verificación en vivo de DfT/DVLA

- **Section**: §18. Auditoría de procedencia
- **Lines**: 814
- **Types**: citation-grounded
- **Excerpt**: «Verificado en vivo: publicado por Department for Transport + DVLA, actualizado 23/09/2026, Open Government Licence»
- **Restated**: La fuente DfT/DVLA fue verificada en vivo, con fecha de actualización 23/09/2026 y licencia Open Government Licence.
- **Internal evidence cited**: §18 (L814), §17 (L804).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: `gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files`.

### C051 — Fuentes oficiales no accesibles desde el entorno

- **Section**: §18. Auditoría de procedencia
- **Lines**: 815–816
- **Types**: citation-grounded, contextual
- **Excerpt**: «VAHAN (India) [...] No accesible desde este entorno (error de transporte); el repo documenta 12 exportaciones mensuales 2025 [...] BCC (Banco Central de Cuba) [...] No accesible en vivo desde este entorno»
- **Restated**: VAHAN y BCC no pudieron verificarse en vivo desde el entorno, aunque el repositorio VAHAN documenta 12 exportaciones mensuales de 2025.
- **Internal evidence cited**: §18 (L815–816), §52 (L1293).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C052 — Clases de calidad y comparables adaptados

- **Section**: §19. Marco de análisis de mercado y su adaptación
- **Lines**: 849
- **Types**: methodological, definitional
- **Excerpt**: «clases de calidad (≤5 años alta, >5 años con defectos, según PUCE); bandera de asimetría por ocultamiento; comparables por modelo ±2 años y municipio; rentabilidad = reventa esperada − compra − reacondicionamiento − impuestos; asequibilidad = precio / salario; series con snapshots.»
- **Restated**: El marco adaptado define clases de calidad por antigüedad, comparables ±2 años y municipio, y fórmulas de rentabilidad y asequibilidad.
- **Internal evidence cited**: §19 (L846–851), §20 (L861–865).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C053 — Análisis descriptivo inicial: muestra y precios válidos

- **Section**: §22. Análisis descriptivo inicial
- **Lines**: 890
- **Types**: result
- **Excerpt**: «Resultados sobre 323 autos: 248 precios USD válidos (≥500 USD); 74 precios <500 USD marcados como inválidos y 1 en CUP excluidos.»
- **Restated**: El análisis se realizó sobre 323 autos, de los que 248 tenían precio USD válido, 74 se marcaron inválidos y uno se excluyó por estar en CUP.
- **Internal evidence cited**: §22 (L888–892), §24 (L909).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C054 — Estadísticos de precio del análisis inicial

- **Section**: §22. Análisis descriptivo inicial
- **Lines**: 890
- **Types**: result
- **Excerpt**: «Precio mediano **22.000 USD**, media 24.416,59 USD, IQR 11.375–35.000 USD, rango 600–95.000 USD.»
- **Restated**: La distribución de precios del análisis inicial tiene mediana 22.000 USD, media 24.416,59 USD, IQR 11.375–35.000 USD y rango 600–95.000 USD.
- **Internal evidence cited**: §22 (L890), §22 EN (L892).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Cifra divergente respecto de la mediana local de 21.000 USD en §51 y §59.

### C055 — Líderes de frecuencia y cobertura de campos derivados

- **Section**: §22. Análisis descriptivo inicial
- **Lines**: 890
- **Types**: result
- **Excerpt**: «Marca más frecuente: Hyundai (n=75); municipio con más oferta: Playa (n=53). Cobertura de campos derivados: marca 68,4 %, año 63,5 %, km 6,2 % (heurísticos, extraídos solo de título/descripción). Detectados 5 outliers por IQR.»
- **Restated**: Hyundai y Playa lideran las frecuencias; la cobertura de campos derivados es 68,4 %, 63,5 % y 6,2 %, con cinco outliers por IQR.
- **Internal evidence cited**: §22 (L890), §24 (L907).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C056 — Conversión con la TRMI diaria de elTOQUE

- **Section**: §23. Conversión elTOQUE, serie temporal y gráficas
- **Lines**: 898
- **Types**: methodological, result
- **Excerpt**: «la conversión usa `precio_USD × TRMI elTOQUE` del día del anuncio (columna `Mediana` de `Anexos/Investigacion Cambios/trmi_USD.csv`).»
- **Restated**: La conversión a CUP aplica la TRMI de elTOQUE correspondiente al día del anuncio, tomada de la columna `Mediana` del CSV indicado.
- **Internal evidence cited**: §23 (L898), §52 (L1293).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: §52 menciona 930 CUP/USD para la TRMI informal, cifra distinta de la de §23.

### C057 — Supuesto de anuncio activo

- **Section**: §23. Conversión elTOQUE, serie temporal y gráficas
- **Lines**: 899
- **Types**: methodological, definitional
- **Excerpt**: «todos los registros tienen `status=PUBLISHED` y página verificada en la captura, por lo que se asume que son comprables; no se comprueba disponibilidad en tiempo real.»
- **Restated**: El análisis asume que los anuncios con `status=PUBLISHED` y página verificada son comprables, sin comprobar disponibilidad en tiempo real.
- **Internal evidence cited**: §23 (L899), §25 (L917), §19 (L851).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Supuesto explícitamente declarado, no medición.

### C058 — Serie precio versus tasa

- **Section**: §23. Conversión elTOQUE, serie temporal y gráficas
- **Lines**: 900
- **Types**: result
- **Excerpt**: «la TRMI pasó de 680 CUP/USD (09/07/2026) a 920 (16-17/11/2026); la mediana mensual CUP subió de 12,58 M (julio) a 20,7 M (noviembre).»
- **Restated**: La TRMI declarada pasó de 680 a 920 CUP/USD entre julio y noviembre de 2026, y la mediana mensual en CUP de 12,58 M a 20,7 M.
- **Internal evidence cited**: §23 (L900), §23 EN (L903).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C059 — Diccionarios JSON completos sin campos estructurados de vehículo

- **Section**: §24. Estado del scrapeo y procesamiento de diccionarios
- **Lines**: 907
- **Types**: result
- **Excerpt**: «**Diccionarios/JSON guardados** (6.334/6.334 anuncios): `meta_json`, `ad_json` y `apollo_full`. [...] **No hay claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión**: por eso `anio_est`, `marca_est` y `km_est` se derivan con regex del texto visible»
- **Restated**: Los 6.334 anuncios conservan tres diccionarios JSON, pero no contienen claves estructuradas de año, kilometraje, marca, modelo, combustible ni transmisión.
- **Internal evidence cited**: §24 (L907), §22 (L890), §24 EN (L911).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C060 — Reporte de scrapeo y estado de colas

- **Section**: §24. Estado del scrapeo y procesamiento de diccionarios
- **Lines**: 909
- **Types**: result
- **Excerpt**: «`anuncios` 6.334 · `autos` 323 · `revision` 6.085 · `imagenes` 13.932 · `telefonos` 7.699 · BD 520,6 MB. Colas: `url_queue` 141 (125 done, 3 downloading, 13 pending)»
- **Restated**: El reporte declara recuentos por tabla, 520,6 MB de base y colas con elementos pendientes de una corrida interrumpida.
- **Internal evidence cited**: §24 (L909), §25 (L918), §24 EN (L911).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C061 — Supuesto de disponibilidad en catálogos

- **Section**: §25. Reanudación, resiliencia y supuesto de catálogos
- **Lines**: 917
- **Types**: methodological, definitional
- **Excerpt**: «Para concesionarios y páginas similares se asume que todo el catálogo está disponible salvo que la página indique lo contrario y que se publicó el día de la captura [...] Para clasificados se mantiene el supuesto de anuncio activo = comprable, con `fecha_publicacion = updated_on_by_user`.»
- **Restated**: El código distingue dos supuestos de publicación: catálogos con fecha de captura y clasificados con fecha de actualización del anuncio.
- **Internal evidence cited**: §25 (L917), §23 (L899).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C062 — Causa del retraso y orden corregido de clasificación

- **Section**: §26. Orden corregido: enlace → clasificación → BD
- **Lines**: 924
- **Types**: methodological, result
- **Excerpt**: «Se identificó la causa del retraso en la clasificación: el timer ejecutaba `actualizar_revolico.py`, que solo corre el scraper y divide la BD, sin escribir nunca `autos`/`revision`. El servicio ahora ejecuta `scrape_revolico_pipeline.py`»
- **Restated**: El informe atribuye el retraso a un timer que no escribía `autos`/`revision` y declara corregido el orden mediante clasificación temprana en el descubrimiento.
- **Internal evidence cited**: §26 (L924–929), §33 (L1004).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Se presenta como diagnóstico de causa raíz.

### C063 — Encuesta de demanda sobre preferencia eléctrica

- **Section**: §50. Consolidación de bases de los repositorios de autos
- **Lines**: 1265
- **Types**: result
- **Excerpt**: «la encuesta con datos reales fue un Google Forms de 32 preguntas aplicado a 33 personas de 4 segmentos en un barrio de La Habana (17 de 18–25 prefieren eléctrico, pero 16 de 18 no pagarían más de 4.000 USD por uno)»
- **Restated**: La encuesta aplicada a 33 personas registró que 17 de 18–25 prefieren eléctrico y que 16 de 18 no pagarían más de 4.000 USD por uno.
- **Internal evidence cited**: §50 (L1265), §51 (L1281), §50 EN (L1267).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: La reconciliación posterior en §51 reduce a 28 los interesados y corrige las propulsiones.

### C064 — Deduplicación de `autos` a 744 registros únicos

- **Section**: §51. Mejoras del proyecto
- **Lines**: 1275
- **Types**: result, methodological
- **Excerpt**: «La tabla se reconstruyó desde `anuncios` (fuente canónica): 814 filas con 748 IDs únicos → **744 autos únicos**. Se excluyeron 4 anuncios que no son autos (`58867937`, `53777554`, `53843413`, `58886962`)»
- **Restated**: La deduplicación redujo 814 filas a 744 autos únicos y excluyó cuatro anuncios identificados por ID.
- **Internal evidence cited**: §51 (L1273–1275), §59 (L1375).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Se creó el índice único `idx_autos_id`.

### C065 — Reparación del análisis de precios en marketplaces

- **Section**: §51. Mejoras del proyecto
- **Lines**: 1277
- **Types**: result, methodological
- **Excerpt**: «`parse_price` ahora interpreta separadores de miles (973 anuncios recuperados: 872 de iTENCEL, 99 de Cubisima, 2 de VentaCuba). Los precios vacíos de Autocubana se recuperan del JSON-LD (614 anuncios, mediana 17.000 USD)»
- **Restated**: La reparación recuperó 973 anuncios con separadores de miles y 614 precios de Autocubana desde JSON-LD, con mediana 17.000 USD.
- **Internal evidence cited**: §51 (L1277), §55 (L1339), §51 EN (L1283).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C066 — Separación por canal local e importación

- **Section**: §51. Mejoras del proyecto
- **Lines**: 1277
- **Types**: result
- **Excerpt**: «Se incorporó la columna `canal`: **1.301 anuncios locales y 672 de importación** (iTENCEL), con `kpis_canal.csv` e `importacion_por_marca.csv` separados. La mediana local quedó en 21.000 USD.»
- **Restated**: El conjunto reparado se divide en 1.301 anuncios locales y 672 de importación, con mediana local de 21.000 USD.
- **Internal evidence cited**: §51 (L1277), §58 (L1367), §59 (L1375).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C067 — Corrección del parseo de kilometraje

- **Section**: §51. Mejoras del proyecto
- **Lines**: 1278
- **Types**: result, methodological
- **Excerpt**: «`parse_specs` y `parse_title` convertían `80,000 km` en 80 km. Se extrajo `parse_number()` con la lógica de separadores ya usada en `parse_price`. El código está aplicado y probado (`80,000` → 80.000)»
- **Restated**: El error de parseo convertía 80.000 km en 80 km y la corrección declarada produce 80.000.
- **Internal evidence cited**: §51 (L1278), §55 (L1339).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: El texto señala que la regeneración final de outputs se registra al cierre de la tanda.

### C068 — 25 fuentes adicionales verificadas y tasa informal empleada

- **Section**: §52. Ampliación de fuentes de datos
- **Lines**: 1289, 1293
- **Types**: result, citation-grounded
- **Excerpt**: «**25 fuentes** verificadas, organizadas por tipo con URL, datos expuestos, viabilidad de scraping y aporte al proyecto. [...] La conversión del proyecto sigue usando la **TRMI informal** de elTOQUE (930 CUP/USD), nunca la oficial.»
- **Restated**: El informe declara 25 fuentes verificadas y que la conversión emplea la TRMI informal de elTOQUE a 930 CUP/USD.
- **Internal evidence cited**: §52 (L1289–1297), §23 (L900).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: `Data/fuentes-adicionales-2026-11-20.md`.

### C069 — Descarga completa de los anuarios del ONEI

- **Section**: §53. Descarga completa de los anuarios del ONEI
- **Lines**: 1309–1311
- **Types**: result, citation-grounded
- **Excerpt**: «se recorrieron las 12 páginas de anuarios disponibles (2014–2025) y se descargaron **todos los documentos enlazados**: 111 PDF, 7 RAR y 103 archivos Excel extraídos, unos 311 MB en total»
- **Restated**: La descarga cubrió 12 anuarios (2014–2025), 111 PDF, 7 RAR y 103 Excel, unos 311 MB.
- **Internal evidence cited**: §53 (L1309–1311), §56 (L1347).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: índice oficial `http://www.onei.gob.cu/cuba`.

### C070 — División de la base de Revolico en chunks verificados

- **Section**: §54. Base de datos distribuida en chunks
- **Lines**: 1321
- **Types**: result, methodological
- **Excerpt**: «`Data/Revolico/revolico.sqlite` (849.465.344 bytes) se dividió en **82 chunks de 10 MB** en `Data/Revolico/chunks/`, con un `MANIFEST.json` que guarda el SHA-256 del archivo completo, el orden, el offset y el hash de cada fragmento. La verificación de los 82 chunks dio OK.»
- **Restated**: La base de 849.465.344 bytes se dividió en 82 fragmentos de 10 MB y los 82 pasaron la verificación de hashes.
- **Internal evidence cited**: §54 (L1321–1325), §14 (L759), §30 (L975).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C071 — Auditoría de fuentes web del 23/11/2026

- **Section**: §55. Auditoría de fuentes, README y verificación final
- **Lines**: 1333
- **Types**: result
- **Excerpt**: «Se consultaron **15 fuentes web** (8 marketplaces, 7 fuentes oficiales y complementarias): 14 respondieron HTTP 200 y elTOQUE no respondió desde este entorno. Las fechas más recientes en las bases son 17–18/11/2026.»
- **Restated**: De 15 fuentes consultadas, 14 respondieron HTTP 200 y elTOQUE no respondió; las fechas más recientes en las bases son 17–18/11/2026.
- **Internal evidence cited**: §55 (L1333), §55 EN (L1341).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: `Data/auditoria-fuentes-2026-11-23.md`.

### C072 — Series del ONEI y su interpretación

- **Section**: §56. Análisis de los anuarios y estructura de GitHub
- **Lines**: 1347
- **Types**: result, citation-grounded
- **Excerpt**: «el transporte de pasajeros cayó un 59 % entre 2019 y 2025 y el ómnibus un 71 %; los accidentes bajaron pero la gravedad aumentó (9,9 fallecidos por cada 100 accidentes en 2025)»
- **Restated**: Las series extraídas muestran caídas del 59 % y 71 % en transporte de pasajeros y ómnibus, y 9,9 fallecidos por cada 100 accidentes en 2025.
- **Internal evidence cited**: §56 (L1347), §56 EN (L1351).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Fuente nombrada: `Data/fuentes-oficiales/ONEI/series_oficiales.csv`.

### C073 — Reclasificación de enlaces y novedades en iTENCEL

- **Section**: §57. Reclassificación de páginas y novedades detectadas
- **Lines**: 1357
- **Types**: result, methodological
- **Excerpt**: «7 fuentes sin enlaces nuevos; **iTENCEL mostró 10 anuncios nuevos** [...] El detalle está en `Data/novedades-fuentes-2026-11-23.md` [...] sin modificar las bases.»
- **Restated**: La comparación de las dos primeras páginas de ocho marketplaces detectó diez anuncios nuevos solo en iTENCEL, sin modificar las bases de datos.
- **Internal evidence cited**: §57 (L1357), §58 (L1365).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: La normalización incluyó `www.`, query, Unicode NFC y barras finales.

### C074 — Incorporación de los diez anuncios nuevos de iTENCEL

- **Section**: §58. Incorporación de anuncios nuevos de iTENCEL
- **Lines**: 1365–1367
- **Types**: result
- **Excerpt**: «La BD pasó de 951 a **961 anuncios** (961 URLs únicas, `integrity_check=ok`). El pipeline se regeneró [...] **2.014 anuncios limpios**, de ellos 1.323 locales y 691 de importación; mediana local 21.000 USD y mediana de kilometraje 44.125 km.»
- **Restated**: La base de iTENCEL pasó de 951 a 961 anuncios únicos y el pipeline regenerado produjo 2.014 anuncios limpios con mediana local de 21.000 USD.
- **Internal evidence cited**: §58 (L1365–1369), §59 (L1375), §10 de la Parte I (L60).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Se realizó copia de seguridad `itencel.sqlite.bak-20261123` antes de escribir.

### C075 — Cifras narrativas de la sección 3 del storytelling

- **Section**: §45. Reescritura de la sección 3 del storytelling
- **Lines**: 1210
- **Types**: contextual, result
- **Excerpt**: «la mediana de 23.000 USD, la antigüedad media de 6,3 años, las 34 marcas, la depreciación de −5,43 % anual, los 27 grupos comparables y las 30 oportunidades infravaloradas»
- **Restated**: La versión intermedia del relato empleaba 23.000 USD de mediana, 6,3 años, 34 marcas, 27 grupos y 30 oportunidades.
- **Internal evidence cited**: §45 (L1210), §59 (L1375), §34 (L1045–1050).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Cifras divergentes de las finales de C010 y C074.

### C076 — Geometría extraída del APK de Circuitos Habana

- **Section**: §62. Factibilidad del timelapse eléctrico
- **Lines**: 1403
- **Types**: result
- **Excerpt**: «Del APK se extrajeron 2.473 puntos, 244 circuitos y 166 polígonos de zonas a `Data/mapas/circuitos/».
- **Restated**: La extracción produjo 2.473 puntos, 244 circuitos y 166 polígonos.
- **Internal evidence cited**: §62 (L1403), §35 (L1070).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

### C077 — Estimación de consumo de red de la automatización

- **Section**: §65. Automatización operativa y coste de red
- **Lines**: 1429
- **Types**: result, methodological
- **Excerpt**: «Estimación de red: **5–10 MB/mes** si no hay cambios y **50–90 MB/mes** con novedades.»
- **Restated**: La estimación declarada de tráfico es 5–10 MB mensuales sin cambios y 50–90 MB con novedades.
- **Internal evidence cited**: §65 (L1429), §65 EN (L1431).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: El texto la presenta como estimación, no como medición.

### C078 — Corrección de estados pendientes en el pipeline de Revolico

- **Section**: §66. Extracción continua de Revolico y arquitectura de datos
- **Lines**: 1437
- **Types**: result, methodological
- **Excerpt**: «3.351 enlaces `es_auto_candidato=0` quedaban `pending` para siempre: se marcan `rechazado` y se excluyen del conteo de salida [...] En la primera corrida corregida los anuncios `done` pasaron de 6.783 a 6.955.»
- **Restated**: El diagnóstico identificó 3.351 enlaces atascados y, tras la corrección, los anuncios `done` pasaron de 6.783 a 6.955.
- **Internal evidence cited**: §66 (L1437), §37 (L1098), §39 (L1124).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: Se presenta como hallazgo de depuración.

### C079 — Reducción de tamaño del repositorio

- **Section**: §67. Optimización de espacio
- **Lines**: 1447
- **Types**: result
- **Excerpt**: «El repositorio pasó de 20 GB a 10 GB.»
- **Restated**: El tamaño del repositorio se redujo de 20 GB a 10 GB tras la eliminación autorizada de archivos.
- **Internal evidence cited**: §67 (L1447), §67 EN (L1449).
- **External evidence cited**: — (sin citas numeradas).
- **Notes**: —.

## Contextual claims (72)

### C080 — Nombres anteriores conservados

- **Section**: §1. Objetivo
- **Lines**: 18
- **Types**: contextual
- **Excerpt**: «Se conservan los nombres anteriores, *AutoDecide Habana* e *ICD Automotive Market Project*, para mantener la trazabilidad de la documentación ya producida.»

### C081 — Clones con profundidad 1 y registro

- **Section**: §3. Organización de carpetas
- **Lines**: 52
- **Types**: contextual, methodological
- **Excerpt**: «los clones se hicieron con `--depth 1` y se registraron en `~/Utilidades/HerramientasScraping/_clone_log.tsv`»

### C082 — Descubrimiento separado de verificación

- **Section**: §3. Organización de carpetas
- **Lines**: 52
- **Types**: contextual, methodological
- **Excerpt**: «la descubrimiento se separó de la verificación»

### C083 — Exclusión de `Copias/` del informe

- **Section**: §3. Organización de carpetas; §13. Registro de altas
- **Lines**: 52, 272, 274
- **Types**: contextual
- **Excerpt**: «`Copias/` no se registra en este informe por decisión explícita.»

### C084 — Alcance restringido del marco legal

- **Section**: §10. Marco legal
- **Lines**: 112
- **Types**: contextual
- **Excerpt**: «Solo se incluyen las normas y fuentes relevantes para el contexto del proyecto»

### C085 — Índice de gacetas y corpus no registrado entrada por entrada

- **Section**: §10. Marco legal
- **Lines**: 118
- **Types**: contextual, citation-grounded
- **Excerpt**: «`~/Utilidades/Leyes/gaceta_catalog.json` es el índice de referencia; el corpus completo de gacetas no se registra entrada por entrada en este informe»

### C086 — Falso «anomaly» en HTTP 200

- **Section**: §11. Problemas y soluciones
- **Lines**: 126
- **Types**: contextual, methodological
- **Excerpt**: «Falso "anomaly" en HTTP 200 | Detector ajustado para exigir texto real de anomalía.»

### C087 — Renderizado de sitios JS-heavy

- **Section**: §11. Problemas y soluciones
- **Lines**: 128
- **Types**: contextual, methodological
- **Excerpt**: «Sitios JS-heavy | Renderizado con Chromium del sistema desde Playwright.»

### C088 — Registro automático de altas y regeneración del PDF

- **Section**: §13. Registro de altas
- **Lines**: 272, 274
- **Types**: contextual, methodological
- **Excerpt**: «El script `Auxiliares/herramientas/actualizar_informe.py` añade filas debajo del marcador y regenera el PDF.»

### C089 — Entradas omitidas en el registro

- **Section**: §13. Registro de altas
- **Lines**: 291
- **Types**: contextual
- **Excerpt**: «175 entradas adicionales no listadas / omitted»

### C090 — Herramientas declaradas en el registro de altas

- **Section**: §13. Registro de altas
- **Lines**: 279, 296, 297, 495, 496, 564
- **Types**: contextual, methodological
- **Excerpt**: «Pipeline de 3 etapas con colas persistentes para Revolico. [...] Scraper de WhatsApp Web mediante Playwright (sin WAHA/Docker). [...] Limpieza de la BD de Revolico: solo vehículos de 4+ ruedas con datos útiles.»

### C091 — Reconstrucción verificada por hash

- **Section**: §14. Sincronización automática de Revolico
- **Lines**: 752, 754
- **Types**: contextual, methodological
- **Excerpt**: «Para recuperar el archivo completo se usa `Auxiliares/herramientas/reconstruir_revolico.py`, que verifica el hash.»

### C092 — Telegram MTProto: sin navegador y cursor incremental

- **Section**: §15. Eficiencia de Telegram, WhatsApp y Facebook
- **Lines**: 763
- **Types**: contextual, methodological
- **Excerpt**: «sin navegador, con cursor incremental `min_id`/`offset_id`, búsqueda server-side y manejo de `FloodWaitError`»

### C093 — Facebook GQL y normalización de precios

- **Section**: §15. Eficiencia de Telegram, WhatsApp y Facebook
- **Lines**: 763
- **Types**: contextual, methodological
- **Excerpt**: «Facebook GQL (`facebook_gql_scraper`): llamadas GraphQL con sesión autenticada y normalización con `price-parser`/`iso4217parse`, más rápido que Selenium.»

### C094 — WhatsApp sin API pública personal

- **Section**: §15. Eficiencia de Telegram, WhatsApp y Facebook
- **Lines**: 763
- **Types**: contextual, citation-grounded
- **Excerpt**: «Para grupos de WhatsApp no existe API pública personal; la opción operativa es un servidor WAHA auto-hospedado y su REST (`/api/sessions`, `/api/{session}/chats`, `/api/{session}/chats/{chatId}/messages`) con deduplicación por id»

### C095 — Esquema común de las tres fuentes

- **Section**: §15. Eficiencia de Telegram, WhatsApp y Facebook
- **Lines**: 763
- **Types**: contextual, definitional
- **Excerpt**: «La salida de las tres fuentes debe convergir en un esquema común (`fuente`, `id`, `chat/página`, `timestamp`, `texto`, `precio`, `moneda`, `url`) con dedup por `hash(fuente,id)` y sin datos personales.»

### C096 — Eliminación de palabras de defecto para costos ocultos

- **Section**: §19. Marco de análisis de mercado
- **Lines**: 848
- **Types**: contextual
- **Excerpt**: «estado y palabras de defecto en el texto (para estimar costos ocultos)»

### C097 — Límites declarados del análisis

- **Section**: §19. Marco de análisis de mercado
- **Lines**: 851
- **Types**: contextual, methodological
- **Excerpt**: «**Límites**: precios pedidos no transaccionados, sesgo de supervivencia de anuncios, sin datos personales, vigencia normativa a verificar.»

### C098 — Marco general de ocho pasos

- **Section**: §19. Marco de análisis de mercado — Marco general
- **Lines**: 833–842
- **Types**: contextual, definitional
- **Excerpt**: «**Marco general (8 pasos, derivado de los trabajos revisados)**»

### C099 — Delimitación geográfica y monetaria

- **Section**: §19. Adaptación a Cuba / La Habana
- **Lines**: 846
- **Types**: contextual, definitional
- **Excerpt**: «La Habana; autos de 4+ ruedas; canales formal e informal; precios anunciados en CUP/USD/MLC/EUR **sin mezclar**.»

### C100 — Marco detallado de nueve bloques

- **Section**: §20. Marco analítico detallado
- **Lines**: 857–867
- **Types**: contextual, definitional
- **Excerpt**: «El marco operativo completo consta de nueve bloques»

### C101 — Regresión hedónica y explicabilidad previstas

- **Section**: §20. Marco analítico detallado
- **Lines**: 865
- **Types**: contextual, methodological
- **Excerpt**: «regresión hedónica, margen de rentabilidad, asequibilidad precio/salario, ponderación de preferencias, explicabilidad tipo SHAP.»

### C102 — Necesidades de datos pendientes

- **Section**: §20. Marco analítico detallado
- **Lines**: 871
- **Types**: contextual
- **Excerpt**: «extracción estructurada de año/km/marca/modelo/combustible/transmisión desde `ad_json`/`apollo_full`; montos de costos ocultos; precios de transacción reales; estadísticas oficiales cubanas de parque y matriculaciones»

### C103 — Cambio de objetivo a petición del usuario

- **Section**: §21. Cambio de objetivo
- **Lines**: 877–884
- **Types**: contextual, definitional
- **Excerpt**: «A petición del usuario, el objetivo inmediato deja de ser la recomendación interactiva de compra y pasa a ser **un análisis de mercado**.»

### C104 — Archivos generados por el análisis descriptivo

- **Section**: §22. Análisis descriptivo inicial
- **Lines**: 888
- **Types**: contextual
- **Excerpt**: «genera en `Data/analisis/`: `resumen_general.csv`, `precios_por_marca.csv`, `precios_por_municipio.csv`, `precios_por_anio.csv`, `outliers.csv`, `cobertura.csv`, `informe_descriptivo.md` y `dashboard.html`.»

### C105 — Módulo de gráficas

- **Section**: §23. Conversión elTOQUE, serie temporal y gráficas
- **Lines**: 901
- **Types**: contextual
- **Excerpt**: «`Auxiliares/herramientas/graficos_mercado.py` usa matplotlib, seaborn y plotly (instalados) y genera 8 PNG + `dashboard_interactivo.html`»

### C106 — Librerías de mapas instaladas

- **Section**: §25. Reanudación, resiliencia y supuesto de catálogos
- **Lines**: 915
- **Types**: contextual
- **Excerpt**: «`geopandas 1.2.0`, `shapely 2.2.0`, `pyproj`, `folium 1.0.0`, `mapclassify`, `geopy`»

### C107 — Reinicio automático del servicio de scrapeo

- **Section**: §25. Reanudación, resiliencia y supuesto de catálogos
- **Lines**: 916
- **Types**: contextual, methodological
- **Excerpt**: «`revolico-scrape.service` ahora tiene `Restart=on-failure`, `RestartSec=30`, `StartLimitIntervalSec=300` y `StartLimitBurst=20`»

### C108 — Prueba del orden corregido

- **Section**: §26. Orden corregido: enlace → clasificación → BD
- **Lines**: 931
- **Types**: contextual, result
- **Excerpt**: «120 enlaces descubiertos, 63 descartados tempranamente y 185 candidatos descargados; `autos` pasó de 323 a 326 y `revision` de 6.085 a 6.134.»

### C109 — Aviso periódico de progreso

- **Section**: §27. Aviso periódico y umbral de revisión
- **Lines**: 937–938
- **Types**: contextual
- **Excerpt**: «`revolico-aviso.timer` avisa **cada 10 minutos** mediante `revolico-aviso.py`: escribe `Data/Revolico/progreso.md`, envía `notify-send` al escritorio y registra en el journal.»

### C110 — Umbral de revisión

- **Section**: §27. Aviso periódico y umbral de revisión
- **Lines**: 939
- **Types**: contextual, methodological
- **Excerpt**: «cuando `anuncios WHERE pagina_revisada=0`llega a **4.000** (configurable con `REVISAR_UMBRAL`), el aviso lanza `revolico-revisar.service`, que ejecuta el pipeline con `--solo-colas`»

### C111 — Estado de colas en §27

- **Section**: §27. Aviso periódico y umbral de revisión
- **Lines**: 940
- **Types**: contextual, result
- **Excerpt**: «Estado actual: 3.623 sin revisar, por debajo del umbral; 266 URLs, 11 descargas y 24 decisiones pendientes en colas.»

### C112 — Scraper público de Telegram sin credenciales

- **Section**: §28. Primeros datos de Telegram
- **Lines**: 946
- **Types**: contextual, methodological
- **Excerpt**: «No hay credenciales MTProto (`TELEGRAM_API_ID`/`TELEGRAM_API_HASH` vacías), así que se implementó [...] que lee la vista pública `t.me/s/<canal>` y pagina con `?before=<id>`. No requiere login, redacta teléfonos»

### C113 — Corrida del scraper de Telegram

- **Section**: §28. Primeros datos de Telegram
- **Lines**: 948
- **Types**: contextual, result
- **Excerpt**: «Corrida final (50 páginas): **152 mensajes**, **54 anuncios de autos** del canal `goldenbullbusinessfamilycars`, 45 con año detectable y **ninguno con precio explícito**»

### C114 — Canales de Telegram descartados

- **Section**: §28. Primeros datos de Telegram
- **Lines**: 950
- **Types**: contextual
- **Excerpt**: «Ninguno publicó anuncios de autos accesibles sin unirse: son noticias, eventos, compra-venta general, repuestos o grupos con invitación.»

### C115 — Base compartida de Telegram

- **Section**: §29. Base de datos de Telegram
- **Lines**: 956, 962–967
- **Types**: contextual, result
- **Excerpt**: «tres tablas: `canales`, `anuncios` y `estado`. Ambos scripts escriben en ella **mientras corren [...] Objetivo de 100 canales de referencia superado (119). El descubrimiento usa 26 búsquedas en tgden.com»

### C116 — Configuración de Git LFS

- **Section**: §30. Gestión de bases de datos con Git LFS
- **Lines**: 973
- **Types**: contextual, methodological
- **Excerpt**: «Se instaló **Git LFS 3.8.1** y se activó en el repositorio. `.gitattributes` marca `*.sqlite`, `*.sqlite-wal` y `*.sqlite-shm` con `filter=lfs diff=lfs merge=lfs -text`»

### C117 — Advertencia sobre cuota de LFS

- **Section**: §30. Gestión de bases de datos con Git LFS
- **Lines**: 977
- **Types**: contextual
- **Excerpt**: «la cuota LFS del plan gratuito es limitada; una BD que cambia cada 10 minutos genera un blob nuevo por commit.»

### C118 — Rango temporal permitido de anuncios

- **Section**: §31. Rango temporal de anuncios Revolico
- **Lines**: 983
- **Types**: contextual, definitional
- **Excerpt**: «Se fijó el rango permitido de `updated_on_by_user` entre **2021-01-01 y la fecha actual** en `limpiar_revolico.py` (`FECHA_MINIMA`).»

### C119 — Modo de descubrimiento sin procesamiento

- **Section**: §32. Backfill de descubrimiento sin procesamiento
- **Lines**: 991–996
- **Types**: contextual, methodological
- **Excerpt**: «**no hay descarga de anuncios, ni clasificación definitiva, ni inserción en `anuncios`/`autos`/`revision`**»

### C120 — Parada por página sin enlaces nuevos

- **Section**: §33. Parada por repetición y procesamiento de anuncios
- **Lines**: 1004
- **Types**: contextual, methodological
- **Excerpt**: «se detenga en cuanto una página no aporte **ningún enlace nuevo** (todos sus anuncios ya fueron vistos) [...] El contador `total` ahora acumula solo enlaces nuevos.»

### C121 — Arquitectura del esqueleto de rentabilidad

- **Section**: §34. Esqueleto de análisis de rentabilidad
- **Lines**: 1014, 1017–1033
- **Types**: contextual, methodological
- **Excerpt**: «Creé `Data/analisis_rentabilidad/` siguiendo la arquitectura del repositorio **Egyptian-Used-Cars** (ingesta → limpieza → EDA → estadística → benchmark)»

### C122 — Paquetes estadísticos y exclusión de DuckDB

- **Section**: §34. Esqueleto de análisis de rentabilidad
- **Lines**: 1035
- **Types**: contextual
- **Excerpt**: «Instalé además `statsmodels 0.15`, `pyarrow 26`, `kaleido`, `nbformat` y `nbconvert`. `duckdb` se desinstaló porque produce `Illegal instruction` en esta CPU»

### C123 — Brecha frente al estudio egipcio

- **Section**: §34. Esqueleto de análisis de rentabilidad — Brecha frente a Egipto
- **Lines**: 1056
- **Types**: contextual
- **Excerpt**: «Egipto tiene 23.500 anuncios, historial mensual de precios, HP y kilometraje estructurados, ANOVA/OLS/VIF, Tableau y Power BI. Nosotros tenemos el pipeline y las técnicas cubiertas, pero solo 497 usados, un único snapshot»

### C124 — Descarga y descompilación de APKs de Apklis

- **Section**: §35. App de circuitos eléctricos de Apklis
- **Lines**: 1064
- **Types**: contextual
- **Excerpt**: «Descargué tres APKs desde la API de Apklis [...] **Circuitos Habana** (`com.ermetic.circuitoshabana`, v2.2) [...] Con **jadx 1.5.6** descompilé la primera»

### C125 — La app Circuitos Habana sin API privada

- **Section**: §35. App de circuitos eléctricos de Apklis
- **Lines**: 1066
- **Types**: contextual, result
- **Excerpt**: «La app **no usa una API privada**: hace scraping del canal público de Telegram `https://t.me/s/EmpresaElectricaDeLaHabana` con Jsoup y User-Agent de Chrome.»

### C126 — Paginación y conversión horaria de la app

- **Section**: §35. App de circuitos eléctricos de Apklis
- **Lines**: 1067–1068
- **Types**: contextual
- **Excerpt**: «Paginación con `?before=<message_id>`, hasta 16 páginas / 300 mensajes / 8 días [...] convierte timestamps UTC a hora de Cuba con +1 h de horario de verano.»

### C127 — Docker sin privilegios de root

- **Section**: §36. Mapa offline, talleres e infraestructura EV
- **Lines**: 1080
- **Types**: contextual
- **Excerpt**: «el daemon Docker no arranca sin root en este entorno (`dockerd needs to be started with root privileges`), por lo que se descartó esa vía.»

### C128 — Ausencia de etiquetas OSM de talleres y carga

- **Section**: §36. Mapa offline, talleres e infraestructura EV
- **Lines**: 1081
- **Types**: contextual, result
- **Excerpt**: «Overpass/OSM fue consultado dos veces; no devuelve `shop=car`, `shop=car_repair` ni `charging_station` etiquetados en Cuba»

### C129 — Coordenadas extraídas de webs de concesionarios

- **Section**: §36. Mapa offline, talleres e infraestructura EV
- **Lines**: 1082
- **Types**: contextual, result
- **Excerpt**: «BDC One: 23.1155203,-82.3596368 y 23.0992805,-82.3050631; Dongfeng: 23.1250339,-82.4227564»

### C130 — Mapa offline sin internet

- **Section**: §36. Mapa offline, talleres e infraestructura EV
- **Lines**: 1083
- **Types**: contextual
- **Excerpt**: «Se generó `Data/mapas/mapa_ofline.html`: contorno de Cuba embebido + marcadores + Plotly incluido, funciona sin internet.»

### C131 — Infraestructura EV documentada

- **Section**: §36. Mapa offline, talleres e infraestructura EV
- **Lines**: 1084
- **Types**: contextual, citation-grounded
- **Excerpt**: «Dongfeng/NWI 11 estaciones solares (2026), CIMEX+MITRANS 21 estaciones (2025), primera estación rápida en Santa Clara (08/2026), conectores CCS2»

### C132 — Sesiones TLS por hilo

- **Section**: §37. Optimización de pipelines
- **Lines**: 1096
- **Types**: contextual, methodological
- **Excerpt**: «`scrape_revolico.py` ahora usa una **sesión curl_cffi por hilo** (`threading.local`) con impersonación Chrome, reutilizando conexiones TLS en vez de crear una por petición.»

### C133 — Aumento de descargadores y procesadores

- **Section**: §37. Optimización de pipelines
- **Lines**: 1096
- **Types**: contextual, methodological
- **Excerpt**: «El servicio `revolico-revisar.service` pasó de 8 descargadores/4 procesadores a **20/8** con `--batch-size 100`, `TimeoutStartSec=0` y `Restart=on-failure`»

### C134 — Marketplaces en paralelo

- **Section**: §37. Optimización de pipelines
- **Lines**: 1097
- **Types**: contextual, methodological
- **Excerpt**: «el nuevo servicio `marketplaces-scrape.service` corre **6 tiendas en paralelo** con `--delay 0.8`, cada una escribiendo su propia SQLite»

### C135 — Reporte periódico de progreso

- **Section**: §38. Reporte automático de progreso
- **Lines**: 1108–1113
- **Types**: contextual
- **Excerpt**: «actualiza **`Data/progreso_reporte.md` cada 5 minutos** con: conteos de `revolico.sqlite` [...] estado de las colas de `pipeline.sqlite` [...] estado de los servicios systemd.»

### C136 — Persistencia del temporizador de progreso

- **Section**: §38. Reporte automático de progreso
- **Lines**: 1115
- **Types**: contextual
- **Excerpt**: «El timer es persistente (`Persistent=true`) y arranca 1 minuto después del boot.»

### C137 — Ampliación de límites de marketplaces

- **Section**: §39. Continuación del scrapeo y presentación narrativa
- **Lines**: 1123
- **Types**: contextual, result
- **Excerpt**: «Cogetucarro de 200 → **5.008**, Autocubana y Timbirichi a 40 páginas [...] Autocubana pasó de 400 a **566** y Timbirichi de 110 a **170**, totalizando **2.121 anuncios**.»

### C138 — Reintento ante bloqueo de SQLite

- **Section**: §39. Continuación del scrapeo y presentación narrativa
- **Lines**: 1124
- **Types**: contextual, methodological
- **Excerpt**: «se añadió reintento explícito ante `database is locked` (`_retry_exec`). Quedan **3.351 URLs pendientes**; autos: **814**.»

### C139 — Presentación narrativa en diez actos

- **Section**: §39. Continuación del scrapeo y presentación narrativa
- **Lines**: 1126
- **Types**: contextual
- **Excerpt**: «Se redactó `Data/analisis_rentabilidad/PRESENTACION_STORYTELLING.md`: relato en 10 actos con personajes, conflicto, hallazgos, comparación con Egipto y llamada a la acción.»

### C140 — Renombre del repositorio en GitHub

- **Section**: §40. Renombre del repositorio en GitHub
- **Lines**: 1134–1141
- **Types**: contextual, result
- **Excerpt**: «antes: CarlosAntonioAceaJimenezCD/autodecide-habana [...] ahora: CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba»

### C141 — Permanencia de la carpeta local

- **Section**: §40. Renombre del repositorio en GitHub
- **Lines**: 1141
- **Types**: contextual
- **Excerpt**: «La carpeta local sigue siendo `~/Proyectos/ICD Automotive Market Project` para no romper las rutas absolutas de los servicios systemd»

### C142 — Descripción actual del repositorio

- **Section**: §40. Renombre del repositorio en GitHub
- **Lines**: 1143
- **Types**: contextual
- **Excerpt**: «Descripción actual del repo: *"Minimizar los gastos de la compra de coches en La Habana Cuba"*.»

### C143 — Gasolineras de Overpass/OSM

- **Section**: §41. Gasolineras, estaciones de carga y serie de precios del combustible
- **Lines**: 1150
- **Types**: contextual, result
- **Excerpt**: «**Overpass/OSM devolvió 137 gasolineras en La Habana** con coordenadas, marca, dirección y tipos de combustible. WhereFUEL usa esa misma base OSM (110 puntos en radio de 12 km).»

### C144 — Fuentes de estaciones de carga

- **Section**: §41. Gasolineras, estaciones de carga y serie de precios del combustible
- **Lines**: 1151
- **Types**: contextual, result
- **Excerpt**: «**Kargalaya** aportó 9 estaciones de carga con coordenadas y precio por hora [...] **Electromaps** añadió 3 referencias sin coordenadas. ChargeFinder respondió 403 en su API.»

### C145 — Capas del mapa regenerado

- **Section**: §41. Gasolineras, estaciones de carga y serie de precios del combustible
- **Lines**: 1152
- **Types**: contextual, result
- **Excerpt**: «Se crearon `Data/mapas/gasolineras.csv` (137) y `Data/mapas/estaciones_carga.csv` (12), y se regeneró `mapa_ofline.html` con tres capas: concesionarios (3), carga eléctrica (9) y gasolineras (137).»

### C146 — Base histórica de precios de combustible

- **Section**: §41. Gasolineras, estaciones de carga y serie de precios del combustible
- **Lines**: 1153–1154
- **Types**: contextual, result
- **Excerpt**: «`Data/combustible/precios_combustible.sqlite` con **18 observaciones** entre 20/08/2026 y 18/11/2026 [...] El script [...] es idempotente y el timer `precio-combustible.timer` lo ejecuta mensualmente»

### C147 — Régimen de combustible desde 2026

- **Section**: §41. Gasolineras, estaciones de carga y serie de precios del combustible
- **Lines**: 1156
- **Types**: contextual, citation-grounded
- **Excerpt**: «desde 07/02/2026 la venta oficial en CUP está suspendida y el combustible se vende en USD vía Ticket; desde mayo cada importador fija su precio. La B94 informal pasó de 3.500–5.000 CUP (ago) a 7.000–8.000 CUP (sep 2026).»

### C148 — Base unificada del mapa

- **Section**: §42. Base unificada del mapa y talleres
- **Lines**: 1164–1171
- **Types**: contextual, definitional
- **Excerpt**: «Se creó `Data/mapas/mapa_elementos.sqlite` como **fuente única** del mapa offline, con tablas `tipos` y `elementos`. Cada elemento guarda coordenadas, dirección, fuente, URL, teléfono, horario, precio, estado y detalle crudo en JSON.»

### C149 — Estado final de capas del mapa

- **Section**: §42. Base unificada del mapa y talleres
- **Lines**: 1173
- **Types**: contextual, result
- **Excerpt**: «Estado final: **131 gasolineras, 12 estaciones de carga, 25 concesionarios (17 con coords) y 22 talleres (todos con coords)».

### C150 — Anti-bot y geocodificación para talleres

- **Section**: §42. Base unificada del mapa y talleres
- **Lines**: 1175
- **Types**: contextual, methodological
- **Excerpt**: «**Cybo devolvió 403 con curl_cffi**, por lo que se aplicó el stack anti-bot disponible: `patchright` [...] y FlareSolverr en `http://127.0.0.1:8191/v1`. Las direcciones se geocodificaron con Nominatim y Photon»

### C151 — Acuerdo 9811 de 2024

- **Section**: §43. Apartado de «cuánto costaría moverse»
- **Lines**: 1185
- **Types**: contextual, citation-grounded
- **Excerpt**: «**Marco previo:** Acuerdo **9811 de 2024** del Consejo de Ministros, que fijaba precios minoristas de combustibles en CUP y USD.»

### C152 — Medidas de CIMEX del 7 de febrero de 2026

- **Section**: §43. Apartado de «cuánto costaría moverse»
- **Lines**: 1186
- **Types**: contextual, citation-grounded
- **Excerpt**: «CIMEX anunció medidas temporales —respaldadas por el MEP y el viceministro Oscar Pérez-Oliva Fraga— que suspendieron la venta en CUP y activaron **Ticket** (20 L por turno, 24 h para usarlo). No se localizó una resolución numerada nueva en la Gaceta Oficial; fue una disposición administrativa.»

### C153 — Autorización a actores no estatales

- **Section**: §43. Apartado de «cuánto costaría moverse»
- **Lines**: 1187
- **Types**: contextual, citation-grounded
- **Excerpt**: «**15/02/2026:** el Gobierno autorizó a **mipymes, cooperativas y otros actores económicos no estatales** a importar combustible directamente.»

### C154 — Circular Especial 03/2026

- **Section**: §43. Apartado de «cuánto costaría moverse»
- **Lines**: 1188
- **Types**: contextual, citation-grounded
- **Excerpt**: «**12–15/05/2026:** nota del MFP y **Circular Especial 03/2026 de CIMEX**; desde el 15/05 cada importador habilitado fija su precio según costo real de importación (1,80–2,60 USD/L).»

### C155 — Fuentes del apartado de combustible

- **Section**: §43. Apartado de «cuánto costaría moverse»
- **Lines**: 1191
- **Types**: contextual, citation-grounded
- **Excerpt**: «Fuentes: Cubadebate (07/02/2026), Directorio Cubano (12 y 15/05/2026), CubaTrámite (Circular 03/2026) y D-Cuba (20/02/2026).»

### C156 — Mantenimiento e infraestructura en el relato

- **Section**: §44. Reescritura de mantenimiento y retorno
- **Lines**: 1201–1202
- **Types**: contextual
- **Excerpt**: «incorpora los **22 talleres** y **25 concesionarios** geolocalizados [...] la depreciación de **−5,43 % anual** (p < 0,001), primas premium de **+21 %**, descuentos del **−22 %** para tier medio, **30 infravalorados**, **66 anomalías**»

### C157 — División del mercado en dos capas

- **Section**: §46. Apertura de la sección 3 del storytelling
- **Lines**: 1218
- **Types**: contextual
- **Excerpt**: «la división del mercado en dos capas —marketplaces y concesionarios/tiendas oficiales—»

### C158 — Envejecimiento desigual del parque

- **Section**: §47. Reescritura de la sección 4 del storytelling
- **Lines**: 1226
- **Types**: contextual
- **Excerpt**: «una narrativa sobre el envejecimiento desigual del parque: premium frente a autos de uso medio, combinación de antigüedad con kilometraje, estado y marca, y la idea de la marca como "seguro de valor".»

### C159 — Criterio de segmentación premium

- **Section**: §48. Definición de marcas premium y no premium
- **Lines**: 1236–1237
- **Types**: contextual, definitional
- **Excerpt**: «**Premium:** Mercedes-Benz, BMW, Audi, Lexus, Volvo, Porsche, Land Rover, Jaguar, Cadillac, Infiniti y Acura.»

### C160 — Niveles del modelo frente a los dos grupos narrativos

- **Section**: §48. Definición de marcas premium y no premium
- **Lines**: 1239
- **Types**: contextual, definitional
- **Excerpt**: «El modelo econométrico conserva sus tres niveles (`premium`, `medio`, `economico`); la narrativa usa solo dos grupos para ser legible.»

### C161 — Búsqueda de repositorios cubanos de automoción

- **Section**: §49. Búsqueda de repositorios cubanos de automoción
- **Lines**: 1247–1251
- **Types**: contextual, result
- **Excerpt**: «usando 31 consultas en español e inglés [...] Tras deduplicar se obtuvieron **648 repos**, de los que se depuraron **36 con relación directa o instrumental**»

### C162 — Duplicados detectados entre repositorios

- **Section**: §50. Consolidación de bases de los repositorios de autos
- **Lines**: 1259–1261
- **Types**: contextual, result
- **Excerpt**: «De los 7 resultantes, los dos repos de `randoloc` son duplicados en código [...] Se compararon 233 archivos de datos por hash y 76 CSV por contenido ordenado. Se detectaron 12 grupos de duplicados bytes y 11 de duplicados por contenido»

### C163 — Consolidación en una base con procedencia

- **Section**: §50. Consolidación de bases de los repositorios de autos
- **Lines**: 1263
- **Types**: contextual, result
- **Excerpt**: «se creó `Data/repos-autos-referencias/referencias_autos.sqlite` con **25 tablas** [...] De los 3.958 anuncios, **369 ya estaban en nuestra base** [...] y 3.589 son nuevos; no se modificó `revolico.sqlite`»

### C164 — Entrevistas cualitativas

- **Section**: §50. Consolidación de bases de los repositorios de autos
- **Lines**: 1265
- **Types**: contextual
- **Excerpt**: «Las entrevistas (30 + 30 + 8) son cualitativas, anónimas salvo el grupo de AutosxCuba —que incluye nombres y requiere cuidado— y aportan precios de combustible 2,00–2,70 USD/L, mantenimientos de 200 a 3.000 USD»

### C165 — Mejoras sin borrar archivos

- **Section**: §51. Mejoras del proyecto
- **Lines**: 1273
- **Types**: contextual, methodological
- **Excerpt**: «Se ejecutó una tanda de mejoras una por una, sin borrar archivos. Ninguna modificó las bases fuente: todas actúan sobre código, documentación y outputs derivados, con respaldos en `/tmp/opencode/`.»

### C166 — Ampliación de marcas en la configuración

- **Section**: §51. Mejoras del proyecto
- **Lines**: 1279
- **Types**: contextual
- **Excerpt**: «`config.py` incorporó Land Rover, Jaguar, Infiniti, Acura, BAIC, Daewoo, Opel, Volga, GAC, Bestune, Maxus, SsangYong y VW, con sus alias y tiers (premium/medio), para reducir los 442 anuncios en tier "desconocido".»

### C167 — Reconciliación de la encuesta

- **Section**: §51. Mejoras del proyecto
- **Lines**: 1281
- **Types**: contextual
- **Excerpt**: «el cruce filtra ahora `interes=1`, dando **28 interesados** (14 eléctrico, 10 combustión, 4 híbrido) en lugar de los 29 que contaba el script anterior»

### C168 — Fuentes descartadas

- **Section**: §52. Ampliación de fuentes de datos
- **Lines**: 1301
- **Types**: contextual
- **Excerpt**: «se descartaron fuentes sin valor verificable: `cubamotor.com` (dominio estacionado), agregadores de divisas con cifras contradictorias, datasets genéricos de Kaggle/UCI, Marketplace de Facebook (login obligatorio) y MININT/Dirección de Tránsito (sin estadísticas públicas de matriculaciones).»

### C169 — Estructura de los anuarios descargados

- **Section**: §53. Descarga completa de los anuarios del ONEI
- **Lines**: 1311
- **Types**: contextual
- **Excerpt**: «La estructura es `Anuario_Estadistico_AAAA/{PDF,Archivo,Excel}/`. Los años 2014–2016, 2018 y 2019 solo publican un PDF íntegro; 2020–2025 publican capítulos en PDF más un RAR de cuadros.»

### C170 — Herramienta de chunks y rama aislada

- **Section**: §54. Base de datos distribuida en chunks
- **Lines**: 1323–1325
- **Types**: contextual, methodological
- **Excerpt**: «Se añadió `Auxiliares/herramientas/db_chunks.py` con tres comandos (`split`, `verify`, `assemble`) [...] los chunks se publican en la rama huérfana `chunked-db`»

### C171 — Revisión de repositorios auxiliares

- **Section**: §55. Auditoría de fuentes, README y verificación final
- **Lines**: 1335
- **Types**: contextual, result
- **Excerpt**: «Se revisaron los 33 repositorios auxiliares. De los **7 cubanos**, solo `AutosxCuba` tiene ref remoto atrasada (24 commits), pero los 7 tienen cambios locales sin commitear»

### C172 — README, entorno y skills

- **Section**: §55. Auditoría de fuentes, README y verificación final
- **Lines**: 1337
- **Types**: contextual
- **Excerpt**: «Se reescribió `README.md` como página de entrada [...] Se añadió `requirements.txt` y un entorno `Auxiliares/.venv-py` funcional.»

### C173 — Corrección de un error de importación

- **Section**: §55. Auditoría de fuentes, README y verificación final
- **Lines**: 1339
- **Types**: contextual, methodological
- **Excerpt**: «La verificación del código detectó un `NameError` en `scripts/01_ingest.py` (`cfg` usado antes de importarse); se corrigió y se revalidó la importación y las funciones `parse_price`/`parse_number`.»

### C174 — Estructura versionada en GitHub

- **Section**: §56. Análisis de los anuarios y estructura de GitHub
- **Lines**: 1349
- **Types**: contextual, result
- **Excerpt**: «1.288 archivos, 157 objetos LFS, distribuidos en `Data` (836), `Hombros` (280), `Auxiliares` (110) y `Anexos` (56)»

### C175 — Copia de seguridad antes de insertar

- **Section**: §58. Incorporación de anuncios nuevos de iTENCEL
- **Lines**: 1365
- **Types**: contextual, methodological
- **Excerpt**: «Se hizo copia de seguridad de `itencel.sqlite` antes de escribir (`itencel.sqlite.bak-20261123`), se canonizaron las URLs con barra final para no duplicar y se reparó un título de interfaz usando el JSON-LD.»

### C176 — Documentación de funciones y modelos

- **Section**: §60. Inventario de funciones y modelos
- **Lines**: 1385
- **Types**: contextual, methodological
- **Excerpt**: «cada transformación y cada estimación del pipeline, con su justificación: normalización sintáctica y TRMI, features derivados, mediana y cuartiles, modelo hedónico log-lineal, VIF, Kruskal-Wallis, Welch t-test y detección de anomalías.»

### C177 — Sitio MkDocs y navegación Diátaxis

- **Section**: §61. Sitio MkDocs del proyecto
- **Lines**: 1393
- **Types**: contextual
- **Excerpt**: «La navegación sigue Diátaxis: **Historia** [...] **Referencia** [...] **Cómo** [...] y **Fuentes**»

### C178 — Compilación estricta del sitio

- **Section**: §61. Sitio MkDocs del proyecto
- **Lines**: 1395
- **Types**: contextual, result
- **Excerpt**: «`mkdocs build --strict` termina sin errores ni enlaces rotos. `site/` queda ignorado por Git»

### C179 — Accesibilidad del canal eléctrico

- **Section**: §62. Factibilidad del timelapse eléctrico
- **Lines**: 1403
- **Types**: contextual, result
- **Excerpt**: «el canal público de Telegram de la Empresa Eléctrica de La Habana (`t.me/s/EmpresaElectricaDeLaHabana`) responde HTTP 200 y publica mensajes fechados el 23/11/2026.»

### C180 — Primera corrida del scraper de circuitos

- **Section**: §62. Factibilidad del timelapse eléctrico
- **Lines**: 1403
- **Types**: contextual, result
- **Excerpt**: «en su primera corrida real capturó 40 mensajes, deduplicó por ID y dejó 35 circuitos sin luz, 23 mixtos y 2 con luz en `Data/mapas/circuitos_estado.sqlite`.»

### C181 — Correcciones de depuración en el timelapse

- **Section**: §62. Factibilidad del timelapse eléctrico
- **Lines**: 1403
- **Types**: contextual, methodological
- **Excerpt**: «Un informe de debug corrigió tres fallos (fecha local, filtro de relevancia y palabras de afectación) y las filas existentes se migraron sin borrarse.»

### C182 — Revisión de la narrativa como puerta de entrada

- **Section**: §63. Calidad del storytelling como puerta de entrada
- **Lines**: 1411
- **Types**: contextual
- **Excerpt**: «antes de la revisión tenía fricción inicial (metadatos antes de la promesa), un H2 genérico, el dato fuerte enterrado y ninguna llamada a la acción.»

### C183 — Arquitectura de automatización propuesta

- **Section**: §64. Automatización hacia una fuente auditable a dos años
- **Lines**: 1421
- **Types**: contextual, methodological
- **Excerpt**: «tres carriles desacoplados (recolectar, procesar, publicar), periodicidad realista en UTC, idempotencia por clave de fuente, marcas de agua, escrituras atómicas, cuarentena de datos inválidos, `SALUD.md` como dead-man's switch»

### C184 — Límite de ejecución sin internet

- **Section**: §65. Automatización operativa y coste de red
- **Lines**: 1429
- **Types**: contextual
- **Excerpt**: «Sin internet no se puede scrapear, pero sí ejecutar sin presencia del usuario; si falla la red, `SALUD.md` marca el periodo perdido y el siguiente ciclo `Persistent=true` lo recupera.»

### C185 — Cinco temporizadores y envoltorio con bloqueo

- **Section**: §65. Automatización operativa y coste de red
- **Lines**: 1429
- **Types**: contextual, methodological
- **Excerpt**: «Se activaron cinco timers `precio-*` [...] envoltorio `run_step.sh` con `flock` y estado atómico, validación con cuarentena y `SALUD.md`.»

### C186 — Distinción entre SIN DATOS y STALE

- **Section**: §65. Automatización operativa y coste de red
- **Lines**: 1429
- **Types**: contextual, methodological
- **Excerpt**: «`salud.py` ahora distingue `SIN DATOS` de `STALE` (antes generaba 10 alertas falsas) y el capturador escribe el ETag solo después del `commit` en SQLite»

### C187 — Configuración del temporizador de Revolico

- **Section**: §66. Extracción continua de Revolico y arquitectura de datos
- **Lines**: 1437
- **Types**: contextual, methodological
- **Excerpt**: «Se activó `precio-revolico.timer` cada 10 minutos con `--max-pages 3`, 2 descargadores, 2 procesadores y lotes de 50, sin `git push`. El job usa `flock` y un timeout de 45 min con 5 min de margen»

### C188 — Arquitectura de almacenamiento por fases

- **Section**: §66. Extracción continua de Revolico y arquitectura de datos
- **Lines**: 1439
- **Types**: contextual, methodological
- **Excerpt**: «Parquet particionado por `year/month`, watermark, rollups mensuales y evaluación de DuckDB/Polars/Arrow. En esta CPU `import duckdb` falla con `SIGILL`, así que la Fase 1 se hará con pyarrow/pandas»

### C189 — Archivos eliminados y mudanzas

- **Section**: §67. Optimización de espacio
- **Lines**: 1447
- **Types**: contextual
- **Excerpt**: «se quitaron: el entorno de Python antiguo e inservible (1,7 GB), dos versiones viejas de archivos grandes [...] Las leyes y las herramientas de scraping **no se borraron**: se mudaron a `~/Utilidades/Leyes` y `~/Utilidades/HerramientasScraping`.»

### C190 — Peso en GitHub y mapa de espacio

- **Section**: §68. Peso en GitHub y mapa de espacio
- **Lines**: 1455
- **Types**: contextual, result
- **Excerpt**: «La API de GitHub reporta **205.002 KB (0,20 GB)** para el historial normal; los archivos grandes se guardan aparte y su consumo en GitHub no lo expone la API. En local, esa copia ocupa 3,3 GB con 174 archivos.»

### C191 — Candidatos a optimización de espacio

- **Section**: §68. Peso en GitHub y mapa de espacio
- **Lines**: 1455
- **Types**: contextual
- **Excerpt**: «las tres copias partidas de Revolico (2,1 GB), el historial normal (1,0 GB), bibliotecas quizá innecesarias (66 MB de DuckDB, que además falla en esta CPU), repos de referencia (606 MB) y documentos descargados (261 MB).»

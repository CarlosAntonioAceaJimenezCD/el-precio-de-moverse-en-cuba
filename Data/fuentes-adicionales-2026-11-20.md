# Fuentes adicionales para El precio de moverse en Cuba (20/11/2026)

Investigación complementaria sobre fuentes oficiales, compraventa, concesionarios, divisas y datos abiertos. Solo autos: se excluyen motos, triciclos, repuestos y servicios. El tipo de cambio se trata solo como contexto de conversión.

> Nota metodológica: `websearch` devolvió HTTP 403; las búsquedas se hicieron con DuckDuckGo Lite/Bing vía `webfetch`. Algunos PDF no se pudieron abrir con la herramienta (504 / tipo no soportado), pero sus URLs y resúmenes sí se verificaron.

## A. Fuentes oficiales cubanas

| # | Fuente y URL | Datos | Scraping | Aporte |
|---|---|---|---|---|
| 1 | **Gaceta Oficial No. 65 Ordinaria de 2026** — https://www.gacetaoficial.gob.cu/es/gaceta-oficial-no-65-ordinaria-de-2026 | Índice de 11 normas del paquete automotor de ago-2026 (PDF por norma) | Fácil (HTML + PDF) | Puerta de entrada al nuevo marco normativo. |
| 2 | **Decreto 163/2026 del Consejo de Ministros** — https://www.gacetaoficial.gob.cu/es/decreto-163-de-2026-de-consejo-de-ministros | Transmisión de propiedad, comercialización e importación; deroga Decreto 119/2024 | Medio | Define quién puede importar/vender y crea el CEMA. Espejo con PDF: https://www.cibercuba.com/s/gacetaoficial/decreto-163-de-2026-de-consejo-de-ministros |
| 3 | **Resoluciones 171, 172 y 173/2026 (MFP)** — https://www.gacetaoficial.gob.cu/es/resolucion-171-de-2026-de-ministerio-de-finanzas-y-precios · .../resolucion-172-de-2026-de-ministerio-de-finanzas-y-precios · .../resolucion-173-de-2026-de-ministerio-de-finanzas-y-precios | 171: valores referenciales mínimos para impuestos; 172: impuesto especial a comercializadoras que venden en USD; 173: formación de precios en CUP de usados | Medio | «Lista de precios oficial» para contrastar precio de mercado vs. valor fiscal. |
| 4 | **Resoluciones 174 y 175/2026 (MFP)** — https://www.gacetaoficial.gob.cu/es/resolucion-174-de-2026-de-ministerio-de-finanzas-y-precios · https://www.gacetaoficial.gob.cu/es/resolucion-175-de-2026-de-ministerio-de-finanzas-y-precios | 174: importación sin carácter comercial; 175: tarifas máximas en USD de servicios aduaneros (22 USD por auto eléctrico) | Medio | Cuantifica el costo fijo de traer un auto. |
| 5 | **Resolución 312/2026 y Resolución 340/2026 de la Aduana** — https://www.gacetaoficial.gob.cu/es/resolucion-312-de-2026-de-aduana-general-de-la-republica · https://www.gacetaoficial.gob.cu/es/resolucion-340-de-2026-de-aduana-general-de-la-republica | 312 modifica el Anexo II de la Res. 175/2022; **340 deroga 175/2022, 170/2024 y la propia 312/2026** | Fácil | ⚠️ La Res. 312 ya está **derogada**: usar 340 como norma vigente. |
| 6 | **Resolución 52/2026 del Ministerio del Transporte** — https://www.gacetaoficial.gob.cu/es/resolucion-52-de-2026-de-ministerio-del-transporte | Comercialización, importación, fabricación/ensamblaje y desarme de vehículos | Medio | Regla operativa no incluida en la lista anterior. |
| 7 | **Resolución 17/2026 del MINCIN (PDF)** — https://www.mincin.gob.cu/sites/mincin/files/documentos/2026-09/Aprobar%20comerc%20veh%C3%ADculos.pdf | Entidades autorizadas a comercializar vehículos | Difícil (PDF escaneado) | Contrasta los 11 concesionarios relevados contra el universo real de vendedores autorizados. |
| 8 | **ONEI — Anuario Estadístico de Cuba 2025, cap. 13 Transporte y Seguridad Vial** — http://www.onei.gob.cu/anuario-estadistico-de-cuba-2025 · PDF: /sites/default/files/publicaciones/2026-10/13-transporte-y-seguridad-vial_aec2025.pdf | Serie oficial de transporte; RAR con cuadros en Excel | Medio (PDF/XLS) | Base oficial más reciente para parque y matriculaciones, hoy ausente. |
| 9 | **ONEI — Transporte: Indicadores Seleccionados, ene–sep 2025** — http://www.onei.gob.cu/transporte-indicadores-seleccionados-enero-septiembre-2025 | 594,3 M de pasajeros ene–sep 2025 (vs. 677,2 M en 2024) | Medio | Contexto de demanda de movilidad; actualizable por trimestre. |
| 10 | **Banco Central de Cuba — API de tasas activas** — https://api.bc.gob.cu/v1/tasas-de-cambio/activas · web: https://www.bc.gob.cu/tasas-de-cambio | JSON diario con tasas oficial, pública y especial. 20-11-2026: USD 24 / 120 / 844 CUP; EUR 26,3784 / 131,892 / 927,6404 | **Fácil (API JSON)** | Normalización monetaria reproducible con fecha embebida. La tasa **informal** sigue siendo la referencia del proyecto. |

## B. Compraventa / clasificados

| # | Fuente y URL | Datos | Scraping | Aporte |
|---|---|---|---|---|
| 11 | **Clasificados.st (Cuba) — Autos/Motor** — https://cu.clasificados.st/motor · paginación `?&st=10`, `st=20`… hasta `st=1620` | 1.623 anuncios; título con marca/modelo/año, precio a veces en el texto, provincia y fecha | Fácil (HTML estático) | Volumen alto. ⚠️ Frescura baja (anuncios de 2024): útil como serie histórica. Filtrar motos/repuestos. |
| 12 | **TecnoTáctil — Clasificados y observatorio de precios** — https://www.tecnotactil.com/clasificados/ · https://www.tecnotactil.com/clasificados/mercado · docs: https://www.tecnotactil.com/api/docs | Agrega precios de Revolico, Porlalivre y Ofertas.cu con histórico por producto | Medio (posible API JSON) | Aporta **histórico de precios** y tres portales nuevos sin scrapearlos por separado. Es agregador, no fuente primaria. |
| 13 | **Dofimall** — https://www.dofimall.com/ · https://www.dofimall.com/topic?topicId=35 | B2B cubano; fichas de JAC T6 4x4 diésel y JAC M3 Plus EV con especificaciones y precio | Medio (endpoints XHR) | Canal formal de marcas chinas ausente de la base. |
| 14 | **Grupos de Facebook de compraventa** — https://www.facebook.com/groups/1428397691506651/ y https://www.facebook.com/groups/480268560990313/ | Autos nuevos/usados con fotos y precios en comentarios | Bloqueado/difícil (login, ToS) | Solo verificación manual; no extracción masiva. |

## C. Concesionarios e importadores nuevos

| # | Fuente y URL | Datos | Scraping | Aporte |
|---|---|---|---|---|
| 15 | **Womy Equipment Supply** — https://womy.cu/cars/ · https://www.womy.equipment/existencias/automoviles/ | Precios EUR (EXW) de Toyota y Lexus: Corolla €24.900, RAV4 €37.500–46.250, Land Cruiser 300 €98.795–104.950, Yaris Cross híbrido €30.750 | Fácil (HTML estático) | Catálogo web vivo y actualizado, ausente en la lista inicial (ya había tabla `cat_womy` en el repo de referencias). |
| 16 | **CarrosW (Cuba/Panamá/Miami)** — https://carrosw.com/ · https://carrosw.com/tipo-de-vehiculo/carros-nuevos/ | Suzuki Jimny 2026 $33.750, Kia Rio 2019 $35.300; financiación en cuotas | Medio (403 al fetch directo) | Precio puesto en Cuba: eslabón entre concesionario y aduana. |
| 17 | **JAC Motors Cuba** — https://www.facebook.com/jaccuba/ · https://www.instagram.com/jac_motors_cuba/ · ventas vía Dofimall | JS2, JS4, JS8 Pro, M4, T8, T6, M3 Plus EV | Difícil (solo redes) | Marca china presente en 2026 que no figura entre los 11 concesionarios. |
| 18 | **Catálogos PDF en Scribd (Womy y MCV 2026)** — https://es.scribd.com/document/1004911448/Catalogo-Womy-Enero-2026 · https://es.scribd.com/document/1050368277/Catalogo-MCV-Comercial-SA-Marzo-2026 | Womy Q1 2026; MCV Marzo 2026: Mercedes-Benz, FAW Bestune, DFSK, USD 13.170–191.015 | Difícil (sin API pública) | Series temporales de precios de catálogo para medir inflación de autos nuevos. |

## D. Divisas (contexto)

| # | Fuente y URL | Datos | Scraping | Aporte |
|---|---|---|---|---|
| 19 | **elTOQUE — tasas e API** — https://eltoque.com/tasas-de-cambio-cuba · https://tasas.eltoque.com/docs | TRMI para USD, EUR y MLC; API con token | Medio | Referencia canónica del mercado informal. Comparador: https://www.cubaradar.com/dollar-today |
| 20 | **Diviza / cubadivisas.com** — https://cubadivisas.com/ · metodología: /sobre-nosotros/metodologia-tasas | 20-11-2026, cada 30 min: USD 945 CUP, EUR 1.016, MLC 848,84, Zelle 918,9 | Fácil | Alternativa verificable y series diarias. ⚠️ No mezclar su «tasa oficial bancos» (855,78) con la del BCC (844 especial). |

## E. Datos abiertos y estudios

| # | Fuente y URL | Datos | Scraping | Aporte |
|---|---|---|---|---|
| 21 | **ICEX — Estudio del mercado del automóvil y sus componentes en Cuba 2026** — https://www.icex.es/content/dam/icex/centros/cuba/documentos/2026/estudio-mercado-automovil-componentes-cuba-2026-resumen.pdf | Parque envejecido, electrificación, demanda de piezas, marcas y canales | Difícil aquí (PDF 504); descarga manual fácil | Único análisis sectorial 2026 con cifras agregadas. |
| 22 | **GitHub — randoloc/AppCubAutosScrapper_QMLQt** — https://github.com/randoloc/AppCubAutosScrapper_QMLQt | 19 commits; scrapers de Revolico, Atrexport, ChinautosCuba, CubaMotor, Dofimall, BDC One, Finauto, Facebook, JACCuba | Fácil (código abierto) | Ahorra implementar parseadores; revela fuentes nuevas. ⚠️ 0 stars: validar selectores. |

## F. Noticias con cifras verificables

| # | Fuente y URL | Datos | Scraping | Aporte |
|---|---|---|---|---|
| 23 | **OnCuba News (4-ago-2026)** — https://oncubanews.com/cuba/economia/cuba-aprueba-nueva-regulacion-para-la-importacion-de-autos-que-favorece-a-vehiculos-electricos/ | Decreto 163: 17 empresas autorizadas (antes 7); impuesto especial 5 % eléctricos vs. 25 % gasolina; 3 %/20 % si se ensamblan en Cuba | Fácil | Traduce el Decreto 163 a cifras citables. |
| 24 | **Directorio Cubano (6-ago-2026)** — https://www.directoriocubano.info/cuba/aduana-cuba-nuevos-aranceles-importacion-vehiculos-autos/ | Aranceles 100/200/300 USD (eléctrico/híbrido/combustión); 500–2.000 USD según valor; despacho 8 USD; servicios 22 USD; vigencia 11-ago-2026 | Fácil | Desglose numérico de aranceles y tasas. |
| 25 | **Prensa Latina (12-nov-2026)** — https://www.prensa-latina.cu/2026/11/12/cuba-impulsa-cambios-para-sostener-transporte-automotor/ | Caída del 47,9 % en movilidad de pasajeros por restricciones de combustible | Fácil | Contexto reciente de demanda y poder adquisitivo. |

## Las 5 más valiosas

1. **BCC API de tasas** — normalización monetaria diaria y programática.
2. **Gaceta Oficial, paquete Res. 171–175 + Decreto 163** — valores fiscales, impuestos y tarifas que explican la brecha entre precio anunciado y final.
3. **ONEI Anuario 2025, cap. 13** — serie oficial más reciente para parque y matriculaciones.
4. **Womy (womy.cu/cars)** — catálogo web vivo con precios EUR de Toyota/Lexus, scraping trivial.
5. **Clasificados.st + TecnoTáctil** — volumen (1.623 anuncios) e histórico de precios de Revolico, Porlalivre y Ofertas.cu.

**Hallazgo crítico:** la **Resolución 312/2026 de Aduana fue derogada por la Resolución 340/2026**. Conviene actualizar las referencias del proyecto a la nueva norma.

## Fuentes descartadas y por qué

- **cubamotor.com** — dominio estacionado en HugeDomains; el scraper del repo aún lo lista, pero no existe.
- **jaccuba.com / dofimall.com (raíz)** — sin respuesta; JAC solo tiene presencia en redes y vende dentro de Dofimall.
- **github.com/jhernandezd95/autos-cuba** — es el propio repo del proyecto; no es fuente nueva (confirmó Womy como concesionario faltante).
- **elvigiadecuba.com, cubaninsights.com, cubaatlas.com, peso-cubano.com** — agregadores con valores contradictorios o desactualizados (665 CUP/USD en cubaninsights vs. 945 en Diviza el 20-11-2026).
- **IndexBox** — informe de pago sin datos abiertos verificables.
- **Datasets genéricos de Kaggle/UCI/Roboflow** — no cubren el mercado cubano.
- **Yellocu, jala-app.com, Facebook Marketplace** — directorio de empresas, descarga sin catálogo y login obligatorio.
- **MININT / Dirección de Tránsito** — no se encontraron estadísticas públicas de matriculaciones; la fuente oficial disponible es ONEI.
- **ICEX PDF** — no descartada: solo fue inaccesible con la herramienta de fetch; mantener la URL para descarga manual.

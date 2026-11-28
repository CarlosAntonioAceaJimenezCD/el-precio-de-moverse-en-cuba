---
type: audit-artifact
phase: v3-results-evidence
slug: corpus-total-2026-11-28
generated_at: 2026-11-28T23:59:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/corpus-total-2026-11-28/corpus-total-2026-11-28.text.md
language: es
---

# V3 — Resultados y evidencia

Resumen (3 líneas): se registran 18 hallazgos, 15 divergencias y 3 respaldos, con cotejo de los 10 archivos contra 21 CSV/TXT de `Data/analisis_rentabilidad/outputs/tables/`, los CSV de `Data/analisis/` y 7 SQLite del checkout. Las divergencias se concentran en §71 (981/584 frente a 993/586), §22 (75/53 frente a 55/46), §58 (44.125 km frente a 32.569 km), los coeficientes del modelo principal sin tabla publicada y los conteos de circuitos/Telegram. Los KPIs vigentes, la no significancia del modelo completo y los conteos de mapa, referencias y líneas base coinciden con sus tablas y SQLite citadas.

Convención: `L###` son líneas absolutas del documento cacheado (10 bloques `# ARCHIVO:`). Los CSV citados son los vigentes al 28/11/2026; las SQLite se consultaron en el checkout local.

### F-V3-001 — H1 enuncia control por antigüedad y kilometraje; la evidencia es un Kruskal-Wallis no ajustado

El claim «**Hipótesis falsable (H1):** «los precios de los tres tiers de marca en el mercado local provienen de la misma distribución, controlando por antigüedad y kilometraje». Se contrasta con Kruskal-Wallis; se rechaza con p < 0,001 en la corrida vigente» aparece en `INFORME_TECNICO.md` §Resumen ES (L30) y §Abstract EN (L172), y se reitera en §60 (L1418) y §71.3 (L1537). La evidencia citada, `tests.csv` (`Kruskal-Wallis precio por tier,44.313,0.0`) y `comparaciones.csv` (`precio por tier de marca,1462,44.313,0.0,10000.0,29500.0,Kruskal-Wallis + bootstrap...`), registra un contraste de tres grupos sin covariables: ni `tests.csv`, ni `comparaciones.csv`, ni `MODELOS_Y_FUNCIONES.md` §3.3 (L2120–2122) incluyen `car_age` o `mileage_km` como control. El rechazo (H=44,313; p=0,0) coincide con ambos CSV; la cláusula «controlando por antigüedad y kilometraje» excede lo que la tabla sostiene. `modelo_depreciacion.csv` es la única tabla con esos términos y pertenece al OLS completo, no al test de tiers.

— polarity: negative · confidence: high · related: [[#C001]], [[#C007]], [[#C062]]

### F-V3-002 — Hyundai (n=75) y Playa (n=53) en §22 frente a n=55 y n=46 en los CSV que se citan

`INFORME_TECNICO.md` §22 (L923) afirma: «Marca más frecuente: Hyundai (n=75); municipio con más oferta: Playa (n=53)», en el mismo párrafo que remite a los productos de `analisis_mercado.py` en `Data/analisis/`. Los archivos generados registran `hyundai,55,28000.0,...` en `Data/analisis/precios_por_marca.csv` y `Playa,46,23750.0,...` en `Data/analisis/precios_por_municipio.csv`; el propio `Data/analisis/informe_descriptivo.md` (L37, L58) repite 55 y 46. El resto del párrafo sí coincide con `resumen_general.csv` (n=248, media 24.416,59, mediana 22.000, p25 11.375, p75 35.000, min 600, max 95.000), `cobertura.csv` (68,4 / 63,5 / 6,2 %) y `outliers.csv` (5 filas). Ninguna tabla del corpus sostiene 75 ni 53.

— polarity: negative · confidence: high · related: [[#C077]]

### F-V3-003 — 981 candidatas y 584 observaciones en §71 frente a 993 y 586 en `modelo_muestra.csv`

`INFORME_TECNICO.md` §71.1 (L1524) escribe «Las 981 candidatas y las 8 fuentes»; §71.1 (L1525) da «R² 0,101 sobre 584 observaciones»; §71.2 (L1531) repite «la muestra pasa de 28 a 584 observaciones de 981 candidatas» y (L1533) «28 a 584 observaciones». La tabla que se cita, `modelo_muestra.csv`, registra `principal,993,586,0.1008,0.0` y `completo,993,28,0.2744,0.4114`. Los propios §59 (L1410) y `MODELOS_Y_FUNCIONES.md` (L2108, L2110) usan 993 y 586. La recomputación de `04_stats.py` sobre `listings_clean.parquet` confirma 993 candidatas y 586 observaciones para el modelo principal. Se trata de una divergencia numérica y de una inconsistencia interna entre secciones del mismo archivo.

— polarity: negative · confidence: high · related: [[#C008]], [[#C060]], [[#C084]]

### F-V3-004 — `kpis_canal.csv` se cita como respaldo de «981 candidatas y 8 fuentes» sin contener esos campos

La frase «Las 981 candidatas y las 8 fuentes se registran en `Data/analisis_rentabilidad/config.py`, `scripts/01_ingest.py` y `outputs/tables/kpis_canal.csv`» (L1524) atribuye a `kpis_canal.csv` un dato que el archivo no contiene: sus cuatro columnas son `canal,source_type,anuncios,mediana_usd,media_usd` y sus tres filas `importacion/usado/691`, `local/nuevo/21`, `local/usado/1462`. No hay campo de candidatas ni conteo de fuentes. La cifra 981 tampoco aparece en `modelo_muestra.csv`, que da 993. La evidencia citada no demuestra el fragmento numérico del claim.

— polarity: negative · confidence: high · related: [[#C008]], [[#C060]]

### F-V3-005 — Pendiente positiva del modelo principal con p<0,05: las tablas citadas muestran el modelo completo con signo negativo

`INFORME_TECNICO.md` §71.2 (L1531) afirma «La pendiente positiva de antigüedad en el modelo principal se atribuye a la selección de anuncios con kilometraje declarado»; `PRESENTACION_STORYTELLING.md` Cuadro 5 (L2035) habla de «la pendiente positiva de este último»; `MODELOS_Y_FUNCIONES.md` (L2110) precisa «En el modelo principal el coeficiente de antigüedad es positivo y alcanza p < 0,05». Las tablas que el propio §71.2 y el Cuadro 5 citan, `modelo_depreciacion.csv` y `modelo_resumen.txt`, están generadas por el modelo **completo** (`04_stats.py`: `fit = modelos["completo"][0]`) y registran `car_age,-0.0632,0.1504` y `car_age -0.0632 0.042 -1.496 0.150`: signo negativo y no significativo. Ningún CSV ni TXT de `outputs/tables/` publica los coeficientes del modelo principal; solo `modelo_muestra.csv` publica su n, R² y p del F. La afirmación es reproducible si se reestima `04_stats.py` (`car_age=+0,0351`, p<0,001, n=586), pero no está respaldada por la evidencia que el texto cita, que además muestra el signo opuesto.

— polarity: negative · confidence: high · related: [[#C005]], [[#C060]], [[#C084]]

### F-V3-006 — Cobertura de `hp` y kilometraje en L2108 (52 y 572) frente a 72 y 586 en los datos

`MODELOS_Y_FUNCIONES.md` (L2108) explica la caída a 28 observaciones: «`hp` solo está presente en 52 filas y `mileage_km` en 572». Aplicando el filtro declarado en `04_stats.py` (usado, canal local, precio>0, `car_age` 0–40) a `Data/analisis_rentabilidad/data/listings_clean.parquet`, los recuentos son 993 candidatas, 72 filas con `hp` no nulo y 586 con `mileage_km` no nulo; este último valor coincide con las 586 observaciones del modelo principal en `modelo_muestra.csv`. Las cifras 52 y 572 no coinciden con la muestra que produce los CSV vigentes.

— polarity: negative · confidence: high · related: [[#C008]], [[#C060]]

### F-V3-007 — §44 presenta +21 % premium, −22 % medio y 66 anomalías sin la salvedad histórica aplicada a la depreciación

`INFORME_TECNICO.md` §44 (L1235) dice: «la depreciación de −5,43 % anual obtenida en la primera corrida (p < 0,001; §34), cifra que la corrida vigente ya no sostiene, junto con las primas premium de +21 %, los descuentos del −22 % para tier medio, 30 infravalorados, 66 anomalías y el marco del Decreto 163/2026». La salvedad «ya no sostiene» alcanza solo a la depreciación; las tres cifras siguientes se enumeran como si fueran vigentes. En `modelo_depreciacion.csv` el coeficiente premium es 0,1146 con p=0,8753 y el de tier medio −0,978 con p=0,0941 (ninguno significativo al 5 %), mientras `anomalias.csv` tiene 89 filas y `infravalorados.csv` 30. Las cifras +21 %/−22 % proceden de la primera corrida (§34, L1085) y 66 anomalías no aparece en ninguna tabla vigente. Hay aquí sobreafirmación por arrastre de una corrida superada.

— polarity: negative · confidence: high · related: [[#C005]], [[#C006]], [[#C079]]

### F-V3-008 — §45 conserva cifras de la corrida del 18/11 y una referencia temporal invertida respecto de §59

`INFORME_TECNICO.md` §45 (L1243) enumera «cifras de la corrida del 18/11/2026, posteriores a las que se recogen en §59»: mediana de 23.000 USD, antigüedad 6,3 años, 34 marcas, depreciación −5,43 % anual, 27 grupos comparables y 30 oportunidades infravaloradas. En la corrida vigente documentada en §59 (L1408) y en `kpis.csv` los valores son 21.000 USD, 8,1 años, 50 marcas, 114 grupos y 30 infravalorados; `modelo_depreciacion.csv` no sostiene la pendiente anual. El pasaje fecha las cifras, pero las presenta como «posteriores» a las de una sección (§59) que registra la corrida del 27/11; la dirección temporal del texto no coincide con las fechas declaradas, y un lector que siga los marcadores `<!-- kpi:* -->` obtiene valores distintos según la sección.

— polarity: negative · confidence: medium · related: [[#C005]], [[#C009]], [[#C079]]

### F-V3-009 — 2.232 anuncios de marketplaces frente a 2.174 limpios en `kpis.csv`

`README.md` (L1623, L1678) y `PRESENTACION_STORYTELLING.md` (L1869) presentan «2.232 anuncios de 8 marketplaces» y «974 autos con datos suficientes frente a 2.232 anuncios en los marketplaces especializados». El mismo README (L1653) y §59 (L1408) anuncian 2.174 anuncios limpios, cifra que coincide con `kpis.csv` (`anuncios_totales,2174.0`) y con `anomalias.csv`/`infravalorados.csv`. El marcador `<!-- kpi:anuncios_marketplaces -->2.232` no tiene fila correspondiente en ningún CSV de `outputs/tables/`, y el corpus no declara si 2.232 es el crudo previo a la limpieza o una población distinta de los 1.483 locales + 691 importación. La comparación «974 autos frente a 2.232 anuncios» mezcla un conteo limpio con un conteo sin calificar.

— polarity: negative · confidence: medium · related: [[#C009]], [[#C018]], [[#C047]]

### F-V3-010 — §58 registra 2.014 anuncios y 44.125 km de mediana, frente a 2.174 y 32.569 km de la corrida vigente

`INFORME_TECNICO.md` §58 (L1400) cierra la incorporación de los diez anuncios de iTENCEL con «**2.014 anuncios limpios**, de ellos 1.323 locales y 691 de importación; mediana local 21.000 USD y mediana de kilometraje 44.125 km». La sección inmediatamente posterior, §59 (L1408), da 2.174 anuncios (1.483 locales + 691 importación) y 32.569 km, coincidentes con `kpis.csv` y `kpis_canal.csv`. La cifra 44.125 km tampoco aparece en ningún CSV vigente; `MODELOS_Y_FUNCIONES.md` (L2066) atribuye el cambio de mediana de km a la corrección de `parse_number`, sin marcar 44.125 como estado superado.

— polarity: negative · confidence: medium · related: [[#C046]], [[#C047]], [[#C079]]

### F-V3-011 — 14.512 revisiones en `ARQUITECTURA_DATOS.md` frente a 14.528 en SQLite y en el manifiesto que se cita

`Data/analisis_rentabilidad/ARQUITECTURA_DATOS.md` (L2160) afirma que la exportación Parquet conserva «las mismas filas, columnas y valores» y enumera «(10.379 anuncios, 974 autos, 23.697 imágenes, 14.512 revisiones, 12.538 teléfonos y 716 precios)». Cinco conteos coinciden con `revolico.sqlite` y con `data/compacto/MANIFEST.json`, pero `SELECT COUNT(*) FROM revision` devuelve 14.528 y el manifiesto registra `"revision": {"filas": 14528, "exportadas": 14528}`. La discrepancia de 16 filas afecta justo a la tabla que sostiene la afirmación de integridad sin pérdida.

— polarity: negative · confidence: high · related: [[#C067]], [[#C068]]

### F-V3-012 — Conteos de circuitos de §62 (35/23/2) frente al estado actual de `circuitos_estado.sqlite`

`INFORME_TECNICO.md` §62 (L1436) describe la «primera corrida real» del capturador: «capturó 40 mensajes, deduplicó por ID y dejó 35 circuitos sin luz, 23 mixtos y 2 con luz en `Data/mapas/circuitos_estado.sqlite`». La SQLite citada contiene, al cotejarla, 213 filas en `estado_circuito` (26 `sin luz`, 96 `mixto`, 4 `con luz`, 87 `sin dato`), 142 filas en `mensajes` y 5 en `capturas`. Los valores 35/23/2 no están presentes en la tabla que se señala como evidencia, y la suma 60 no corresponde a ningún subconjunto identificable del esquema actual; la tabla no registra fecha por fila que permita aislar la primera corrida.

— polarity: negative · confidence: medium · related: [[#C055]]

### F-V3-013 — `telegram.sqlite` citado como base con 119 canales y 54 anuncios es un puntero LFS de 131 bytes

`INFORME_TECNICO.md` §29 (L989–L1000) afirma que `Auxiliares/herramientas/telegram_db.py` creó `Data/integraciones/telegram/telegram.sqlite` con las tablas `canales`, `anuncios` y `estado`, y da los recuentos «`canales` 119», «`canales` con contexto automotriz 4», «`anuncios` 54», «`anuncios` marcados `es_auto` 54». En el checkout, ese archivo tiene 131 bytes y su contenido es `version https://git-lfs.github.com/spec/v1` / `oid sha256:23c7673a...` / `size 135168`: es un puntero de Git LFS, no una base consultable. `sqlite3` devuelve `file is not a database`, por lo que ninguno de los cuatro recuentos puede verificarse contra la SQLite citada.

— polarity: negative · confidence: high · related: [[#C029]], [[#C027]]

### F-V3-014 — Tamaño de `revolico.sqlite` (849.465.344 B) coincide con el manifiesto, no con la SQLite vigente

`INFORME_TECNICO.md` §54 (L1354) registra «`Data/Revolico/revolico.sqlite` (849.465.344 bytes)» y `ARQUITECTURA_DATOS.md` (L2160) habla de 849 MB. El valor 849.465.344 es exactamente `source_size` en `Data/Revolico/chunks/MANIFEST.json`, es decir, el tamaño de la instantánea fragmentada; el archivo en disco al cotejarlo ocupa 878.751.744 bytes y sigue siendo escrito por `precio-revolico.timer` (§66, L1470). La cifra del texto es correcta para el manifiesto que describe, pero no para la SQLite vigente con la que se le pide contrastar; la diferencia es de 29.286.400 bytes.

— polarity: negative · confidence: medium · related: [[#C050]], [[#C067]], [[#C072]]

### F-V3-015 — §71.3 atribuye 981 candidatas al contraste central, cuyo CSV registra n=1.462

`INFORME_TECNICO.md` §71.3 (L1537) sostiene «El tamaño se mide en anuncios (981 candidatas de 8 marketplaces), no en ensayos experimentales. El contraste central se cuantifica con H = 44,313 y un intervalo bootstrap ... de 10.000 a 29.500 USD (`comparaciones.csv`, 2.000 réplicas)». En `comparaciones.csv` la fila es `precio por tier de marca,1462,44.313,0.0,10000.0,29500.0,Kruskal-Wallis + bootstrap de mediana premium-económico (2000 replicas)`: n=1.462, no 981. El H, el intervalo y las réplicas sí coinciden; el tamaño muestral atribuido a ese contraste no coincide ni con su CSV (1.462) ni con `modelo_muestra.csv` (993 candidatas).

— polarity: negative · confidence: high · related: [[#C007]], [[#C008]], [[#C061]]

### F-V3-016 — KPIs vigentes de §59, README y Cuadro 1: respaldo completo y coherente en `kpis.csv`

El bloque «**<!-- kpi:anuncios_totales -->2.174 anuncios limpios** (1.483 locales y 691 de importación), mediana local de 21.000 USD, kilometraje mediano de 32.569 km, 50 marcas, 114 grupos comparables y 89 anomalías» (§59, L1408) y sus réplicas en `README.md` (L1653), `PRESENTACION_STORYTELLING.md` (L1781, L1853, L1979–L1989) y §71.1 (L1520–L1521) coinciden fila por fila con `kpis.csv` (2174, 1483, 691, 1462, 21, 50, 28201.06, 21000, 2020, 32569, 8.1), `kpis_canal.csv`, `benchmark_result.csv` (114), `anomalias.csv` (89) y `infravalorados.csv` (30). Los marcadores `<!-- kpi:* -->` conservan los mismos valores en los diez archivos del corpus. Respaldo múltiple y sin sobreafirmación numérica.

— polarity: positive · confidence: high · related: [[#C009]], [[#C059]], [[#C079]]

### F-V3-017 — No significancia del modelo completo, VIF y Kruskal-Wallis: cifras reproducidas en tres tablas

La afirmación «la corrida actual **no** sostiene una tasa de depreciación ni una prima premium significativa (p mínimo 0,0941; VIF 1,12–1,40; Kruskal-Wallis p = 0,00000)» (§60, L1418) y «28 observaciones de 993 candidatas (R² = 0,274; p del F = 0,411)» (§59, L1410) están respaldadas por `modelo_muestra.csv` (`completo,993,28,0.2744,0.4114`), `modelo_depreciacion.csv` (p mínimo 0,0941 en `C(brand_tier)[T.medio]`; `car_age` −0,0632, p 0,1504; premium p 0,8753), `modelo_resumen.txt` (R² 0,274; F p 0,411; n 28), `vif.csv` (1,12–1,40) y `tests.csv`/`comparaciones.csv` (H 44,313; p 0,0). Cuadro 5 (L2026–L2035) replica los ocho coeficientes con sus p-valores. El lenguaje del corpus («no permite afirmar», «no se interpreta como depreciación») no excede esas tablas.

— polarity: positive · confidence: high · related: [[#C004]], [[#C005]], [[#C006]], [[#C058]], [[#C061]]

### F-V3-018 — Mapa, referencias y líneas base: los conteos declarados coinciden con sus SQLite y CSV

El «estado final: 131 gasolineras, 12 estaciones de carga, 25 concesionarios (17 con coords) y 22 talleres (todos con coords)» (§42, L1206) coincide con `SELECT tipo, COUNT(*), SUM(lat IS NOT NULL) FROM elementos` en `mapa_elementos.sqlite`: 131/131, 12/12, 25/17, 22/22. La consolidación «25 tablas ... 3.958 anuncios ... 369 ya estaban en nuestra base ... 3.589 son nuevos» y «33 respuestas ... 30 + 30 + 8 entrevistas» (§50, L1296–L1298) coincide con `referencias_autos.sqlite` (25 tablas; 3.958; 369/3.589; 33; 30/30/8). Las líneas base «MAE 18.188,34 USD sobre 1.462 anuncios» y «16.603,28 USD sobre 1.462 anuncios» (§71.1, L1520–L1521) coinciden con `baselines.csv`. Los 18 precios de `precios_combustible.sqlite` (§41, L1186) y los 116 descartes por «precio = modelo/año» en Cogetucarro más 11 marcadores en VentaCuba del §51 (L1310) también se verifican en `descartes_marketplaces.csv`.

— polarity: positive · confidence: high · related: [[#C040]], [[#C043]], [[#C059]], [[#C046]]

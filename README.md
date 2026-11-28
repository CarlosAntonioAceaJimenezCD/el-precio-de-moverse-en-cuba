# El precio de moverse en Cuba

Análisis reproducible del mercado automotor cubano: **<!-- kpi:autos_revolico -->974 autos únicos** de Revolico, **<!-- kpi:anuncios_marketplaces -->2.232 anuncios** de 8 marketplaces y **256 vehículos** de 11 concesionarios, consolidados con fuentes oficiales (ONEI, Gaceta Oficial, BCC) y una serie de entrevistas y encuestas.

*Ubicación:* `~/Proyectos/El precio de moverse en Cuba` · *Repositorio:* `el-precio-de-moverse-en-cuba` (https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba) · *Actualizado:* 28/11/2026.

## Qué incluye

- **Datos crudos y auditables**: anuncios, enlaces, colas de descarga y descartes exportados por categoría en `Data/CRUDO_POR_CATEGORIA/`.
- **Base consolidada**: `Data/Revolico/revolico.sqlite` (<!-- kpi:anuncios_revolico -->10.379 anuncios, <!-- kpi:autos_revolico -->974 autos) y `Data/repos-autos-referencias/referencias_autos.sqlite` (25 tablas).
- **Análisis regenerable**: KPIs, benchmarks, depreciación y gráficos en `Data/analisis_rentabilidad/`.
- **Fuentes oficiales**: los 12 anuarios del ONEI (2014–2025), 233 archivos, en `Data/fuentes-oficiales/ONEI/`.
- **Documentación**: informe técnico, storytelling, auditoría de fuentes e índices de datos.

## Quickstart

Requiere Python 3.10+ y Git LFS. Desde la carpeta del proyecto:

```bash
python3 -m venv Auxiliares/.venv-py
Auxiliares/.venv-py/bin/pip install -r requirements.txt
Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py
```

Al terminar verás `INGESTA`, `LIMPIEZA`, `EDA`, `STATS` y `BENCHMARK`, y se habrán actualizado:

```text
Data/analisis_rentabilidad/data/listings_clean.parquet
Data/analisis_rentabilidad/outputs/tables/kpis.csv
Data/analisis_rentabilidad/outputs/tables/kpis_canal.csv
```

**Resultado esperado:** <!-- kpi:anuncios_totales -->2.174 anuncios limpios (<!-- kpi:anuncios_locales -->1.483 locales + <!-- kpi:anuncios_importacion -->691 de importación), mediana local <!-- kpi:precio_mediano_usd -->21.000 USD.

## Estructura

```text
.
├── README.md, requirements.txt, INFORME_TECNICO.md
├── Data/
│   ├── Revolico/                 # base principal, colas, chunks de 10 MB y snapshot
│   ├── catalogos_concesionarios/ # 11 concesionarios + 8 marketplaces
│   ├── repos-autos-referencias/  # base consolidada de repos externos
│   ├── fuentes-oficiales/ONEI/   # anuarios 2014–2025 con índice y SHA-256
│   ├── CRUDO_POR_CATEGORIA/      # export CSV de enlaces y anuncios sin procesar
│   └── analisis_rentabilidad/    # pipeline, KPIs, gráficos y storytelling
├── Auxiliares/herramientas/      # scrapers, exportadores y auditoría de fuentes
├── Auxiliares/Repositorios Referencias/  # repos clonados (no versionados)
└── Copias/, Hombros/, Anexos/    # referencias y corpus (no versionados)
```

Los repositorios auxiliares y `Copias/` se conservan en disco pero **no se suben**: están excluidos en `.gitignore`.

## Fuentes de datos

| Grupo | Fuentes | Registros |
|---|---|---:|
| Marketplaces | Autocubana, iTENCEL, Cogetucarro, Cubisima, Timbirichi, Carros.com, Apululu, VentaCuba | 2.232 anuncios |
| Concesionarios | BDC One, Dongfeng, Changan, Chinautos, MCV, Finauto, ATR Export y otros | 256 vehículos |
| Revolico | `autos` (tabla canónica) | <!-- kpi:autos_revolico -->974 autos únicos |
| Referencias externas | Repos ICD, AutosxCuba, Mercado-automotriz y otros | 3.958 anuncios ICD |
| Oficiales | ONEI, Gaceta Oficial 65/2026, BCC, elTOQUE | 12 anuarios + normas |

La conversión usa la **TRMI informal de elTOQUE (18/11/2026): 930 CUP/USD, 1.000 CUP/EUR y 845,35 CUP/MLC**. Nunca se usa la tasa oficial para los precios del mercado.

## Configuración

| Archivo | Qué controla |
|---|---|
| `Data/analisis_rentabilidad/config.py` | Rutas, umbrales de precio/año, TRMI, marcas y tiers |
| `.gitattributes` | Archivos SQLite y chunks `.bin` gestionados con Git LFS |
| `Data/Revolico/chunks/MANIFEST.json` | 82 fragmentos de 10 MB y sus SHA-256 |
| `Data/Revolico/pipeline_chunks/MANIFEST.json` | 52 fragmentos de `pipeline.sqlite` |

Si `revolico.sqlite` o `pipeline.sqlite` no existen, los scripts los reconstruyen desde sus chunks:

```bash
python3 Auxiliares/herramientas/db_chunks.py verify Data/Revolico/chunks/MANIFEST.json
python3 Auxiliares/herramientas/db_chunks.py assemble Data/Revolico/chunks/MANIFEST.json Data/Revolico/revolico.sqlite
```

## Sitio de documentación

El storytelling, los cuadros, los gráficos y el inventario de modelos se publican como un sitio MkDocs:

```bash
Auxiliares/.venv-py/bin/python Auxiliares/herramientas/generar_sitio_mkdocs.py
Auxiliares/.venv-py/bin/mkdocs build
Auxiliares/.venv-py/bin/mkdocs serve
```

El resultado queda en `site/` (ignorado por Git) y la configuración en `mkdocs.yml`.

## Documentación

- **Referencias y trabajos cercanos (41):** ver `Data/referencias.md`; los discutidos en §71.6 son [14] Gegić et al. (2019), [26] Muça et al. (2026), [9] Du et al. (2026) y [29] Vidal Alejandro et al. (2024); [1] y [12] figuran en el mapa pero no en ese contraste.
- [1] Akerlof, G. A.. *The Market for "Lemons": Quality Uncertainty and the Market Mechanism*. The Quarterly Journal of Economics (1970). https://doi.org/10.2307/1879431. Citada en el informe: sí. **(metadata incomplete: resumen indexado no sustantivo; identidad y DOI verificados en OpenAlex)**
- [2] Lewis, G. M.. *Asymmetric Information, Adverse Selection and Online Disclosure: The Case of eBay Motors*. American Economic Review (2011 (el registro OpenAlex indexa la versión SSRN de 2010; la publicación AER es de 2011)). https://doi.org/10.1257/aer.101.4.1535. Citada en el informe: no.
- [3] Peterson, J. R.; Schneider, H. S.. *Adverse selection in the used-car market: evidence from purchase and repair patterns in the Consumer Expenditure Survey*. The RAND Journal of Economics (2014). https://doi.org/10.1111/1756-2171.12045. Citada en el informe: no.
- [4] Englmaier, F.; Schmöller, A.; Stowasser, T.. *Price Discontinuities in an Online Market for Used Cars*. Management Science (2017). https://doi.org/10.1287/mnsc.2016.2714. Citada en el informe: no.
- [5] Che, X.; Katayama, H.; Lee, P.; Shi, N.. *Warranty, Seller Reputation, and Buyer Experience: Evidence From EBAY Used Car Auctions*. The Journal of Industrial Economics (2019). https://doi.org/10.1111/joie.12213. Citada en el informe: no.
- [6] Wolf, J. R.; Muhanna, W. A.. *Adverse Selection and Reputation Systems in Online Auctions: Evidence from eBay Motors*. ICIS 2005 Proceedings (AIS Electronic Library) (2005). http://aisel.aisnet.org/cgi/viewcontent.cgi?article=1273&context=icis2005. Citada en el informe: no.
- [7] Sultan, A.. *A model of the used car market with lemons and leasing*. Applied Economics (2009). https://doi.org/10.1080/00036840802314556. Citada en el informe: no.
- [8] Tilles, P. F. C.; Ferreira, F. F.; Francisco, G.; Pereira, C. de B.; Sarti, F. M.. *A Markovian model market—Akerlof's lemons and the asymmetry of information*. Physica A: Statistical Mechanics and its Applications (2011). https://doi.org/10.1016/j.physa.2011.03.007. Citada en el informe: no.
- [9] Du, Z.; Yang, Z.; Zhang, Y.; Li, S.; Liu, Y.. *Nonlinear Depreciation and Brand Heterogeneity in Chinese Used-Car Listing Prices: An Interpretable Hedonic Regression and Out-of-Sample Evaluation*. Advances in Economics, Management and Political Sciences (2026). https://doi.org/10.54254/2754-1169/2026.38524. Citada en el informe: sí (§71.6 y §71.14).
- [10] Kang, W.; Fu, X.. *The pricing of used electric vehicles via machine learning and hedonic price model: A comparative study*. Computers & Industrial Engineering (2026). https://doi.org/10.1016/j.cie.2026.111964. Citada en el informe: no. **(metadata incomplete: resumen no indexado; campos bibliográficos verificados)**
- [11] Miranda, A. M.; Alavi, A. B.; Gella, M. A.. *Depreciation Patterns in the UAE Used Car Market: Evidence from Dubizzle Listings*. Journal of Business Insight and Innovation (2026). https://doi.org/10.63544/jbii.v5i6.110. Citada en el informe: no.
- [12] Hulten, C. R.. *Price Hedonics: A Critical Review*. Federal Reserve Bank of New York Economic Policy Review (2003). https://newyorkfed.org/research/epr/03v09n3/0309hult.pdf. **(metadata incomplete: PDF no extraido)**. Citada en el informe: no.
- [13] Francke, M.; Van de Minne, A.. *Modeling unobserved heterogeneity in hedonic price models*. Real Estate Economics (2020). https://doi.org/10.1111/1540-6229.12320. Citada en el informe: no.
- [14] Gegić, E.; Isaković, B.; Keco, D.; Mašetić, Z.; Kevrić, J.. *Car Price Prediction using Machine Learning Techniques*. TEM Journal (2019). https://doi.org/10.18421/tem81-16. Citada en el informe: sí (§71.6 y §71.14).
- [15] Mutİ, S.; Yıldız, K.. *Using Linear Regression For Used Car Price Prediction*. International Journal of Computational and Experimental Science and Engineering (2023). https://doi.org/10.22399/ijcesen.1070505. Citada en el informe: no.
- [16] Jin, C.. *Price Prediction of Used Cars Using Machine Learning*. IEEE International Conference on Emergency Science and Information Technology (ICESIT) (2021). https://doi.org/10.1109/icesit53460.2021.9696839. Citada en el informe: no.
- [17] Ahtesham, M.; Zulfiqar, J.. *Used Car Price Prediction with Pyspark*. Lecture Notes in Networks and Systems (Springer) (2022). https://doi.org/10.1007/978-3-031-01942-5_17. Citada en el informe: no.
- [18] Madhusudhanan, K.; Behrens, G.; Stubbemann, M.; Schmidt-Thieme, L.. *ProbSAINT: Probabilistic Tabular Regression for Used Car Pricing*. arXiv:2403.03812; IEEE BigData 2024, Industry & Government Track (2024). https://arxiv.org/abs/2403.03812 · https://doi.org/10.1109/bigdata62323.2024.10825740. Citada en el informe: sí (§71.14). 13 citas verificadas en OpenAlex el 27/11/2026; versión publicada en IEEE BigData 2024.
- [19] Pal, N.; Arora, P.; Sundararaman, D.; Kohli, P.; Palakurthy, S. S.. *How much is my car worth? A methodology for predicting used cars prices using Random Forest*. arXiv:1711.06970 (FICC, Camera Ready) (2017). https://arxiv.org/abs/1711.06970 · https://doi.org/10.1007/978-3-030-03402-3_28. Citada en el informe: no. 96 citas verificadas en OpenAlex; discrepancia de año documentada: preprint 2017, publicación 2018.
- [20] Arefin, S. E.. *Second Hand Price Prediction for Tesla Vehicles*. arXiv:2101.03788 (2021). https://arxiv.org/abs/2101.03788. Citada en el informe: no. 9 citas verificadas en OpenAlex el 27/11/2026.
- [21] Krotov, V.; Johnson, L.; Silva, L.. *Legality and Ethics of Web Scraping*. Communications of the Association for Information Systems (2020). https://doi.org/10.17705/1cais.04724. Citada en el informe: no.
- [22] Brown, M. A.; Gruen, A.; Maldoff, G.; Messing, S.; Sanderson, Z.; Zimmer, M. T.. *Web scraping for research: Legal, ethical, institutional, and scientific considerations*. Big Data & Society (2025). https://doi.org/10.1177/20539517251381686. Citada en el informe: no.
- [23] Priestley, M.; O'Donnell, F.; Simperl, E. P. B.. *A Survey of Data Quality Requirements That Matter in ML Development Pipelines*. Journal of Data and Information Quality (2023). https://doi.org/10.1145/3592616. Citada en el informe: no.
- [24] Hohensinner, R.; Mutlu, B.; Mendoza Estrada, I. G.; Vukovic, M.; Kopeinik, S.; Kern, R.. *Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability in LLMs*. arXiv:2601.14311 (manuscrito enviado a ACM Computing Surveys) (2026). https://arxiv.org/abs/2601.14311. Citada en el informe: no.
- [25] Wenger, E.; Li, X.; Zhao, B. Y.; Shmatikov, V.. *Data Isotopes for Data Provenance in DNNs*. Proceedings on Privacy Enhancing Technologies (2024). https://doi.org/10.56553/popets-2024-0024. Citada en el informe: no.
- [26] Muça, M.; Bani, K.; Alla, A.. *A Pipeline for Integrating and Analyzing Public Business Data in Albania Using Web Scraping and Machine Learning*. International Journal of Advanced Computer Science and Applications (2026). https://doi.org/10.14569/ijacsa.2026.0170845. Citada en el informe: sí (§71.6 y §71.14).
- [27] Essien, I. A.; Adebayo, A. O.; Afuwape, A. A.; Eboseremen, B. O.; Oladega, F.; Soneye, O. M.. *The Ethics of Web Scraping In Research: A Review*. Journal of Frontiers in Multidisciplinary Research (2023). https://doi.org/10.54660/.jfmr.2023.4.1.529-538. Citada en el informe: no.
- [28] Paige, J.. *The Legality and Ethics of Web Scraping in Archaeology*. Advances in Archaeological Practice (2024). https://doi.org/10.1017/aap.2023.42. Citada en el informe: no.
- [29] Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A.. *Using AI in the informal currency market: evidence from Cuba*. Applied Economics (2024). https://doi.org/10.1080/00036846.2024.2416091. Citada en el informe: sí (§71.6 y §71.14).
- [30] Castro Fernández, M.; Vilaragut Llanes, M.; Hernández, J. C.. *Electromobility and Energy Transition in Cuba*. Sustainability (2024). https://doi.org/10.3390/su16229688. Citada en el informe: no.
- [31] Ritter, A. R. M.. *Cuba's Underground Economy*. RePEc (Carleton Economic Papers) (2004). https://ir.library.carleton.ca/pub/15983. Citada en el informe: no.
- [32] Ávila Castellanos, D. D.. *Currency exchange in post-ordenamiento Cuba: An exploration of institutional waiting for dollar purchases*. Revista Foro Cubano (2024). https://doi.org/10.22518/jour.rfc/2023.6a02. Citada en el informe: no.
- [33] Guerra, E.. *The geography of car ownership in Mexico City: a joint model of households' residential location and car ownership decisions*. Journal of Transport Geography (2015). https://doi.org/10.1016/j.jtrangeo.2015.01.014. Citada en el informe: no.
- [34] Klein, N. J.; Basu, R.; Smart, M. J.. *Transitions into and out of Car Ownership among Low-Income Households in the United States*. Journal of Planning Education and Research (2023). https://doi.org/10.1177/0739456x231163755. Citada en el informe: no.
- [35] Srisan, T.; Ong, P. M.; Bills, T. S.. *Auto insurance affordability and the gap in car ownership: An analysis of transportation burden*. Transport Policy (2026). https://doi.org/10.1016/j.tranpol.2026.104491. Citada en el informe: no.
- [36] Holtz, D.; Lobel, R.; Liskovich, I.; Aral, S.. *Reducing Interference Bias in Online Marketplace Pricing Experiments*. SSRN Electronic Journal (2020). https://doi.org/10.2139/ssrn.3583836. Citada en el informe: no.
- [37] Etro, F.. *Product Selection in Online Marketplaces*. Journal of Economics & Management Strategy (2020). https://doi.org/10.1111/jems.12428. Citada en el informe: no.
- [38] Quariguasi Frota Neto, J.; Bloemhof-Ruwaard, J. M.; Corbett, C. J.. *Market prices of remanufactured, used and new items: Evidence from eBay*. International Journal of Production Economics (2015). https://doi.org/10.1016/j.ijpe.2015.02.006. Citada en el informe: no. Resumen no indexado en OpenAlex; discrepancia de año documentada: 2015 en OpenAlex, 2016 en Crossref (published-print).
- [39] Department for Transport / DVLA. Vehicle statistics. GOV.UK. https://www.gov.uk/government/organisations/department-for-transport. **(metadata incomplete: URL profunda no confirmada)**. Citada en el informe: sí (§70 y §71.14).
- [40] ANFAC. Informes del sector automotriz español. https://anfac.com/. Citada en el informe: sí (fuente institucional en §70).
- [41] AEADE. Estadísticas de matriculaciones. https://www.aeade.net/. Citada en el informe: sí (fuente institucional en §70).
- **Alcance de la novedad:** el diferenciador declarado es de procedencia y normalización sobre datos cubanos, no de método; la última pasada no hizo búsqueda bibliográfica nueva ni lectura de texto completo (§71.14 del informe).
- **Términos:** TRMI (tasa de cambio informal), VSN-C (visión, pasos, novedad, contribuciones), WAHA (API de WhatsApp), MTProto (protocolo de Telegram), GQL (GraphQL), SHAP (explicación de modelos), MAE (error absoluto medio), KPI (indicador), OLS (mínimos cuadrados ordinarios), UTM (parámetros de seguimiento), E-E-A-T (experiencia, pericia, autoridad y confianza), CDN (red de distribución de contenidos), long-form (texto extenso).
- **Arquitectura y evolución:** `Data/analisis_rentabilidad/ARQUITECTURA_DATOS.md`, `Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md`, `Data/AUTOMATIZACION.md`, `Data/ESTRUCTURA_ESPACIO.md`, `Data/mapas/README.md`.
- **Referencia:** `INFORME_TECNICO.md` (secciones 1–71.15), `Data/referencias.md` (41 entradas), `Data/CRUDO_POR_CATEGORIA/INDICE.md`, `Data/fuentes-oficiales/ONEI/README.md`, `Data/analisis_rentabilidad/MODELOS_Y_FUNCIONES.md`.
- **Cómo hacerlo:** `Data/analisis_rentabilidad/README.md`, `Data/Revolico/chunks/README.md`.
- **Explicación:** `Data/analisis_rentabilidad/PRESENTACION_STORYTELLING.md`, `Data/auditoria-fuentes-2026-11-23.md`, `Data/auditoria-fuentes-contenido.md`, `Data/novedades-fuentes-2026-11-23.md`, `Data/fuentes-adicionales-2026-11-20.md`, `Data/fuentes-oficiales/ONEI/ANALISIS_DATO.md`, `Data/estructura_github.md`, `Data/mapas/TIMELAPSE_CIRCUITOS.md`.
- **Necesidades pendientes:** `Data/analisis_rentabilidad/NECESIDADES.md`.

## Marco legal y límites

**Disponibilidad y declaraciones:** el código y los datos derivados están en https://github.com/CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba; las bases crudas se reconstruyen desde `Data/Revolico/chunks/MANIFEST.json`. Licencia: código MIT y datos derivados CC BY 4.0; las fuentes de terceros se rigen por sus propias condiciones. No se declara conflicto de intereses. El uso de IA en redacción, código y auditoría se describe en §69 del informe técnico.

El proyecto respeta los términos de uso de los portales: no sortea muros de pago ni accede a áreas privadas —para contenido público que devuelve 403 se documenta el bloqueo y se usa navegación con fingerprint de Chrome y FlareSolverr—, no publica datos personales de anunciantes —los teléfonos se almacenan en la base de trabajo pero se excluyen de la publicación— y conserva la procedencia de cada dato. El uso de IA en redacción, código y auditoría se declara en §69 del informe técnico. El marco normativo es el **Decreto 163/2026** y las resoluciones 104, 17, 52, 171–175, 340 (que derogó la 312) y 102/2026.

Limitaciones actuales: elTOQUE no responde de forma estable desde este entorno (se usa su última TRMI publicada); `carrosw` está detrás de verificación de bots; parte del catálogo de BDC One y Changan solo está en PDF; la trueque de roles entre canales local e importación se mantiene separada con la columna `canal`.

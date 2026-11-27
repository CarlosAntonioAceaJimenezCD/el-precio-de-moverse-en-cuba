---
type: audit-artifact
phase: e2-literature
slug: informe-tecnico-2026-11-27
generated_at: 2026-11-27T05:36:32Z
preset: Standard
queries_run: 33
papers_l1: 38
papers_l2: 16
papers_l3: 2
language: es
---

# Literature Map

Nota de entrada. No se recibieron los inputs `queries_planned`, `hypotheses_planned`, `novelty_claims_preliminary`, `preset` ni `bibliography_extracted` descritos en el extractor, y no existe un archivo `<slug>.plan.md` en el destino ni en el caché de auditoría. En consecuencia: (a) el `preset: Standard` se asumió por defecto; (b) las queries se derivaron del título, objetivo y secciones 17–22, 34, 52–60 del documento; (c) la sección de hipótesis consigna comprobaciones derivadas, no hipótesis declaradas en un plan aprobado; (d) el documento no tiene bibliografía numerada, así que `Cited in document` se determina por mención nominal y `Document reference` se marca `(metadata incomplete)` cuando no hay número. Toda la metadata bibliográfica fue verificada en vivo el 2026-11-27; cuando un dato no pudo verificarse se marca explícitamente `(metadata incomplete)`.

## Clusters

### Cluster 1 — Asimetría de información y calidad en el mercado de vehículos usados

**Query**: `used car market asymmetric information adverse selection` (OpenAlex `fulltext.search`, 2026-11-27); query complementaria `market for lemons Akerlof` y búsqueda directa por DOI `10.2307/1879431`.

#### P001 — The Market for "Lemons": Quality Uncertainty and the Market Mechanism
- **Authors**: Akerlof, G. A.
- **Year**: 1970
- **Venue**: The Quarterly Journal of Economics
- **Citations**: 32562 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.2307/1879431
- **Layer**: L2
- **Cited in document**: yes
- **Document reference**: mención nominal «Akerlof» en las secciones 17, 19 y 20; sin numeración `(metadata incomplete)`
- **source_of_metadata**: OpenAlex (registro W2156109180, verificado por DOI)
- **Abstract analysis**: El artículo fundacional formaliza la selección adversa: cuando el comprador no observa la calidad, el precio promedio expulsa a los bienes buenos y puede colapsar el mercado. El documento lo invoca como marco teórico para justificar la captura de antigüedad, estado y palabras de defecto en los anuncios de La Habana. La concordancia es conceptual: ambos tratan la calidad como información privada del vendedor. La diferencia es de escala y de diseño: Akerlof construye un modelo teórico general, mientras el informe propone un esquema de datos y una clasificación empírica sin testear formalmente el mecanismo de selección adversa. El resumen indexado en OpenAlex contiene solo el índice de secciones, no un resumen sustantivo `(metadata incomplete)`.

#### P002 — Asymmetric Information, Adverse Selection and Online Disclosure: The Case of eBay Motors
- **Authors**: Lewis, G. M.
- **Year**: 2011 (el registro OpenAlex indexa la versión SSRN de 2010; la publicación AER es de 2011)
- **Venue**: American Economic Review
- **Citations**: 342 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1257/aer.101.4.1535
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W2157565524)
- **Abstract analysis**: Testea en eBay Motors la hipótesis de que la divulgación voluntaria de información privada por parte del vendedor mitiga la selección adversa y sostiene precios más altos; encuentra que las divulgaciones son determinantes importantes del precio. Es el puente natural entre Akerlof y el pipeline del informe: el documento registra defectos en el texto libre, estado, año y tipo de vendedor, pero no trata esas variables como una decisión estratégica de divulgación. Su ausencia es notable porque el informe afirma que el precio anunciado lleva implícita una señal de calidad y propone clasificar la calidad por antigüedad y palabras de defecto.

#### P003 — Adverse selection in the used-car market: evidence from purchase and repair patterns in the Consumer Expenditure Survey
- **Authors**: Peterson, J. R.; Schneider, H. S.
- **Year**: 2014
- **Venue**: The RAND Journal of Economics
- **Citations**: 34 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1111/1756-2171.12045
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W2108227678)
- **Abstract analysis**: Analiza la selección adversa tratando el auto como un ensamblaje de piezas, algunas con información simétrica y otras no, y usa patrones de compra y reparación para cuantificar el efecto sobre el volumen y la calidad del mercado secundario. Aporta una operacionalización de «costos ocultos» que el informe declara como requerimiento (sección 17) pero aún no mide: el documento lista la estimación de reacondicionamiento como tarea pendiente en la sección 20. La diferencia es de fuente de datos: encuestas de gasto estadounidenses frente a anuncios web habaneros.

#### P004 — Price Discontinuities in an Online Market for Used Cars
- **Authors**: Englmaier, F.; Schmöller, A.; Stowasser, T.
- **Year**: 2017
- **Venue**: Management Science
- **Citations**: 50 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1287/mnsc.2016.2714
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W1956884180)
- **Abstract analysis**: Documenta discontinuidades sistemáticas de precio en umbrales salientes de edad y kilometraje en un marketplace europeo: autos idénticos registrados en meses contiguos de años distintos pueden diferir hasta cinco veces más que autos dentro del mismo año, y aparece un patrón análogo en las marcas de 10.000 km. El informe construye series `precios_por_anio.csv` y comparables por modelo ±2 años, lo que hace relevante la advertencia: el año y el kilometraje no entran de forma lineal en el precio. La literatura sugiere además que los saltos pueden reflejar procesamiento burdo de información o fricciones de búsqueda, algo que el modelo log-lineal del documento no considera.

#### P005 — Warranty, Seller Reputation, and Buyer Experience: Evidence From EBAY Used Car Auctions
- **Authors**: Che, X.; Katayama, H.; Lee, P.; Shi, N.
- **Year**: 2019
- **Venue**: The Journal of Industrial Economics
- **Citations**: 13 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1111/joie.12213
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W2967052949)
- **Abstract analysis**: Encuentra que la garantía genera una prima de precio cuyo tamaño disminuye cuando el vendedor tiene reputación consolidada, y que los vendedores profesionales se benefician menos de la sustitubilidad entre garantía y reputación. El informe distingue canales locales e importación y registra tipo de vendedor, pero no incorpora garantía ni reputación como covariables. La superposición es el interés por la identidad del vendedor; la diferencia es que aquí esas señales se testean sobre precio final de subasta, no sobre precio pedido.

#### P006 — Adverse Selection and Reputation Systems in Online Auctions: Evidence from eBay Motors
- **Authors**: Wolf, J. R.; Muhanna, W. A.
- **Year**: 2005
- **Venue**: ICIS 2005 Proceedings (AIS Electronic Library)
- **Citations**: 28 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: http://aisel.aisnet.org/cgi/viewcontent.cgi?article=1273&context=icis2005
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W2166780536)

#### P007 — A model of the used car market with lemons and leasing
- **Authors**: Sultan, A.
- **Year**: 2009
- **Venue**: Applied Economics
- **Citations**: 11 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1080/00036840802314556
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W1965378525)

#### P008 — A Markovian model market—Akerlof's lemons and the asymmetry of information
- **Authors**: Tilles, P. F. C.; Ferreira, F. F.; Francisco, G.; Pereira, C. de B.; Sarti, F. M.
- **Year**: 2011
- **Venue**: Physica A: Statistical Mechanics and its Applications
- **Citations**: 9 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1016/j.physa.2011.03.007
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W1499498447)

### Cluster 2 — Modelos de precio, regresión hedónica y depreciación

**Query**: `hedonic price model used car depreciation` y `used car price prediction machine learning` (OpenAlex `fulltext.search`); query arXiv `all:"used car price"`; búsqueda adicional `Used Linear Regression For Used Car Price Prediction`.

#### P009 — Nonlinear Depreciation and Brand Heterogeneity in Chinese Used-Car Listing Prices: An Interpretable Hedonic Regression and Out-of-Sample Evaluation
- **Authors**: Du, Z.; Yang, Z.; Zhang, Y.; Li, S.; Liu, Y.
- **Year**: 2026
- **Venue**: Advances in Economics, Management and Political Sciences
- **Citations**: 0 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.54254/2754-1169/2026.38524
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W7225188457)
- **Abstract analysis**: Sobre 1.000 anuncios chinos divididos en 800 entrenamiento y 200 prueba, estima tres especificaciones OLS log-lineales anidadas y muestra que la relación edad–precio es no lineal y heterogénea por marca premium; el kilometraje orthogonalizado deja de ser significativo al incluir los términos de edad e interacción. Es el paralelo metodológico más cercano al informe: este también usa una especificación `log(precio) ~ car_age + condition_score + C(brand_tier)`, reporta una caída de −5,43 % anual y después reconoce que la pendiente no resiste la corrección por kilometraje. La coincidencia en la forma funcional y en la cautela interpretativa es alta; la diferencia es de tamaño muestral y de contexto de precios pedidos, y el trabajo chino advierte explícitamente que sus resultados son descriptivos dentro de la muestra, no causales.

#### P010 — The pricing of used electric vehicles via machine learning and hedonic price model: A comparative study
- **Authors**: Kang, W.; Fu, X.
- **Year**: 2026
- **Venue**: Computers & Industrial Engineering
- **Citations**: 2 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1016/j.cie.2026.111964
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W7134932779); resumen no indexado `(metadata incomplete)`

#### P011 — Depreciation Patterns in the UAE Used Car Market: Evidence from Dubizzle Listings
- **Authors**: Miranda, A. M.; Alavi, A. B.; Gella, M. A.
- **Year**: 2026
- **Venue**: Journal of Business Insight and Innovation
- **Citations**: 0 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.63544/jbii.v5i6.110
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W7171439123)
- **Abstract analysis**: Con 400 anuncios de Dubizzle y OLS sobre precio, edad, kilometraje y marca, estima una caída de unos 4.263 AED por año adicional (F = 27,16; p < 0,001; R² = 0,256), mientras el kilometraje no resulta significativo (p = 0,077) y está fuertemente correlacionado con la edad (r = 0,639). Es un casi-experimento del problema del informe: también trabaja con precios pedidos, también usa una muestra pequeña y también obtiene una tasa de depreciación que puede ser frágil frente a la multicolinealidad. La diferencia es que este estudio sí reporta una pendiente anual significativa, mientras el informe, con 744 autos únicos, retira la afirmación de depreciación significativa en la sección 59.

#### P012 — Price Hedonics: A Critical Review
- **Authors**: Hulten, C. R.
- **Year**: 2003
- **Venue**: Federal Reserve Bank of New York Economic Policy Review
- **Citations**: 82 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://newyorkfed.org/research/epr/03v09n3/0309hult.pdf
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W2164155028)

#### P013 — Modeling unobserved heterogeneity in hedonic price models
- **Authors**: Francke, M.; Van de Minne, A.
- **Year**: 2020
- **Venue**: Real Estate Economics
- **Citations**: 43 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1111/1540-6229.12320
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W3024067924)
- **Abstract analysis**: Revisa la especificación hedónica cuando la heterogeneidad no observada puede sesgar los coeficientes de calidad. El documento aplica una especificación hedónica log-lineal con `brand_tier` como proxy de calidad y advierte que la prima premium dejó de sostenerse tras corregir kilometraje (sección 60, p mínimo 0,165). El trabajo aporta el respaldo metodológico para interpretar esa inestabilidad como un problema de heterogeneidad no observada y no como ausencia de efecto. La diferencia es sustantiva: es literatura de precios inmobiliarios, no automotriz.

#### P014 — Car Price Prediction using Machine Learning Techniques
- **Authors**: Gegić, E.; Isaković, B.; Keco, D.; Mašetić, Z.; Kevrić, J.
- **Year**: 2019
- **Venue**: TEM Journal
- **Citations**: 188 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.18421/tem81-16
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4288610071)
- **Abstract analysis**: Recolecta anuncios del portal `autopijaca.ba` con un scraper propio en PHP, aplica ANN, SVM y Random Forest y reporta exactitud de 87,38 % al integrar el modelo en una aplicación Java. Es el antecedente más directo de la combinación scraping + modelado de precios que el informe implementa con Revolico y los concesionarios. La superposición es el flujo completo desde anuncios web hasta predicción; la diferencia es que no documenta deduplicación, procedencia por fuente ni separación de monedas, que son justamente los ejes del informe.

#### P015 — Using Linear Regression For Used Car Price Prediction
- **Authors**: Mutİ, S.; Yıldız, K.
- **Year**: 2023
- **Venue**: International Journal of Computational and Experimental Science and Engineering
- **Citations**: 40 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.22399/ijcesen.1070505
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4323355978)
- **Abstract analysis**: Evalúa regresión lineal sobre características de vehículos turcos de 2020 y obtiene R² de 73 % con un tercio de los datos reservado para prueba. Confirma que una especificación lineal simple alcanza ajuste aceptable en mercados de anuncios, pero también que el resultado depende fuertemente del preprocesamiento. El informe adopta una forma log-lineal con menos variables y reporta R² y VIF como parte de su documentación de modelo (sección 60); la diferencia es la escala: 40 citas frente a una muestra local de cientos de autos, con cobertura parcial de año y kilometraje.

#### P016 — Price Prediction of Used Cars Using Machine Learning
- **Authors**: Jin, C.
- **Year**: 2021
- **Venue**: IEEE International Conference on Emergency Science and Information Technology (ICESIT)
- **Citations**: 42 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1109/icesit53460.2021.9696839
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4211143196)

#### P017 — Used Car Price Prediction with Pyspark
- **Authors**: Ahtesham, M.; Zulfiqar, J.
- **Year**: 2022
- **Venue**: Lecture Notes in Networks and Systems (Springer)
- **Citations**: 15 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1007/978-3-031-01942-5_17
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4285160726)

#### P018 — ProbSAINT: Probabilistic Tabular Regression for Used Car Pricing
- **Authors**: Madhusudhanan, K.; Behrens, G.; Stubbemann, M.; Schmidt-Thieme, L.
- **Year**: 2024
- **Venue**: arXiv:2403.03812; IEEE BigData 2024, Industry & Government Track
- **Citations**: unknown (metadata incomplete; el registro arXiv no expone conteo y Semantic Scholar devolvió 403)
- **URL**: https://arxiv.org/abs/2403.03812
- **Layer**: L3
- **Cited in document**: no
- **source_of_metadata**: arXiv API + texto completo HTML (verificado 2026-11-27T05:30:00Z)
- **Abstract analysis**: Extiende SAINT con una cabeza probabilística entrenada por verosimilitud negativa para predecir media y desviación del precio, y muestra desempeño superior a CatBoost, NGBoost y MC-dropout en NLL sobre aproximadamente 2 millones de registros B2C. Introduce además pronóstico dinámico condicionado a los días de permanencia del anuncio, una noción directamente relacionada con las series de snapshots del informe. La lectura de Introducción, Método y Conclusión confirma dos lecciones aplicables: el tiempo de permanencia es una variable de decisión comercial, y la incertidumbre de la predicción debe reportarse, no solo el punto. El informe reporta puntos y p-valores pero no intervalos ni incertidumbre calibrada; la escala de datos (2 M frente a 744 autos) es la diferencia principal.

#### P019 — How much is my car worth? A methodology for predicting used cars prices using Random Forest
- **Authors**: Pal, N.; Arora, P.; Sundararaman, D.; Kohli, P.; Palakurthy, S. S.
- **Year**: 2017
- **Venue**: arXiv:1711.06970 (FICC, Camera Ready)
- **Citations**: unknown (metadata incomplete; Semantic Scholar devolvió 403)
- **URL**: https://arxiv.org/abs/1711.06970
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: arXiv API (verificado 2026-11-27T05:30:00Z)
- **Abstract analysis**: Entrena un Random Forest de 500 árboles tras EDA para identificar variables correlacionadas con el precio, con exactitud de entrenamiento 95,82 % y de prueba 83,63 %, yMotiva el problema por la asequibilidad en países en desarrollo y por precios irreales publicados por vendedores. El segundo motivo coincide casi literalmente con la problemática del informe: anuncios con precios pedidos que requieren filtros y validación. La diferencia es metodológica: EDA + Random Forest frente al esquema de limpieza auditada y regresión hedónica del proyecto cubano; además no separa entre monedas ni documenta deduplicación.

#### P020 — Second Hand Price Prediction for Tesla Vehicles
- **Authors**: Arefin, S. E.
- **Year**: 2021
- **Venue**: arXiv:2101.03788
- **Citations**: unknown (metadata incomplete; Semantic Scholar devolvió 403)
- **URL**: https://arxiv.org/abs/2101.03788
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: arXiv API (verificado 2026-11-27T05:15:00Z)

### Cluster 3 — Ética, legalidad, procedencia y calidad de datos

**Query**: `web scraping research data collection ethics legal` y `data provenance quality validation pipeline scraped data` (OpenAlex `fulltext.search`).

#### P021 — Legality and Ethics of Web Scraping
- **Authors**: Krotov, V.; Johnson, L.; Silva, L.
- **Year**: 2020
- **Venue**: Communications of the Association for Information Systems
- **Citations**: 224 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.17705/1cais.04724
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W3125851220)
- **Abstract analysis**: Revisa literatura legal y de privacidad para identificar áreas de riesgo y preguntas concretas que investigadores y profesionales deben responder antes de recolectar datos web. El informe declara una regla operativa equivalente —no eludir mecanismos anti-automatización y registrar HTTP 403/429 como limitación— pero no cita ningún marco de cumplimiento. La superposición es directa con la sección 10; la diferencia es de jurisdicción: la literatura analiza sobre todo los Estados Unidos y Europa, mientras el informe se remite a normas cubanas que aún deben verificarse antes de publicar.

#### P022 — Web scraping for research: Legal, ethical, institutional, and scientific considerations
- **Authors**: Brown, M. A.; Gruen, A.; Maldoff, G.; Messing, S.; Sanderson, Z.; Zimmer, M. T.
- **Year**: 2025
- **Venue**: Big Data & Society
- **Citations**: 118 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1177/20539517251381686
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4416422179)
- **Abstract analysis**: Propone un marco de cuatro dimensiones —legal, ética, institucional y científica— para investigadores que recurren al scraping cuando los canales oficiales se restringen, con recomendaciones para recolectar, almacenar y compartir datos de forma legítima. Encaja con la decisión del informe de conservar `raw_html`, `tables_json` y `jsonld_json` como respaldo de trazabilidad y de no publicar datos personales. La diferencia es que el marco se dirige a investigadores de ciencias sociales con base en los Estados Unidos y no aborda la particularidad de marketplaces cubanos ni la separación entre tasa oficial e informal.

#### P023 — A Survey of Data Quality Requirements That Matter in ML Development Pipelines
- **Authors**: Priestley, M.; O'Donnell, F.; Simperl, E. P. B.
- **Year**: 2023
- **Venue**: Journal of Data and Information Quality
- **Citations**: 153 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1145/3592616
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4366407820)
- **Abstract analysis**: Cuestiona la noción clásica de «aptitud para el uso» y propone organizar los requisitos de calidad por etapa del ciclo de vida de ML y por categoría (intrínseca, contextual, representacional, accesibilidad). El informe despliega exactamente esa lógica por etapas: deduplicación, clasificación en `autos`/`revision`, columnas de auditoría, validación con cuarentena y manifiestos con hashes en las secciones 16, 51 y 64–66. La diferencia es que la encuesta es normativa y general, mientras el documento describe una implementación concreta sin contrastarla con un marco de calidad reconocido.

#### P024 — Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability in LLMs
- **Authors**: Hohensinner, R.; Mutlu, B.; Mendoza Estrada, I. G.; Vukovic, M.; Kopeinik, S.; Kern, R.
- **Year**: 2026
- **Venue**: arXiv:2601.14311 (manuscrito enviado a ACM Computing Surveys)
- **Citations**: 13 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://arxiv.org/abs/2601.14311
- **Layer**: L3
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W7125390097) + texto completo HTML (verificado 2026-11-27T05:35:00Z)
- **Abstract analysis**: Sistematiza 95 publicaciones en torno a procedencia, trazabilidad y transparencia, con pilares de sesgo, privacidad y herramientas, y distingue formalmente procedencia (origen) de linaje (transformaciones a lo largo del ciclo de vida). El informe persigue esa misma distinción con `provenancia`, hashes SHA-256, watermarks e idempotencia por clave de fuente, aunque orientado a datos de mercado y no a modelos de lenguaje. La lectura de Introducción, Preliminares y Herramientas confirma que «registro de orígenes y procesamiento» es la definición estándar que el proyecto adopta de facto. La diferencia es el dominio: aquí la trazabilidad se persigue hasta pesos y tokens; en el informe, hasta la fila de anuncio y su fuente.

#### P025 — Data Isotopes for Data Provenance in DNNs
- **Authors**: Wenger, E.; Li, X.; Zhao, B. Y.; Shmatikov, V.
- **Year**: 2024
- **Venue**: Proceedings on Privacy Enhancing Technologies
- **Citations**: 24 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.56553/popets-2024-0024
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4387857422)

#### P026 — A Pipeline for Integrating and Analyzing Public Business Data in Albania Using Web Scraping and Machine Learning
- **Authors**: Muça, M.; Bani, K.; Alla, A.
- **Year**: 2026
- **Venue**: International Journal of Advanced Computer Science and Applications
- **Citations**: 0 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.14569/ijacsa.2026.0170845
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W7204683515)

#### P027 — The Ethics of Web Scraping In Research: A Review
- **Authors**: Essien, I. A.; Adebayo, A. O.; Afuwape, A. A.; Eboseremen, B. O.; Oladega, F.; Soneye, O. M.
- **Year**: 2023
- **Venue**: Journal of Frontiers in Multidisciplinary Research
- **Citations**: 22 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.54660/.jfmr.2023.4.1.529-538
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4413861058)

#### P028 — The Legality and Ethics of Web Scraping in Archaeology
- **Authors**: Paige, J.
- **Year**: 2024
- **Venue**: Advances in Archaeological Practice
- **Citations**: 8 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1017/aap.2023.42
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4394961981)

### Cluster 4 — Cuba: divisas informales, movilidad y asequibilidad

**Query**: `Cuba informal exchange rate dual currency economy`, `electric vehicle adoption Cuba willingness to pay` y `vehicle affordability price income car ownership` (OpenAlex `fulltext.search`).

#### P029 — Using AI in the informal currency market: evidence from Cuba
- **Authors**: Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A.
- **Year**: 2024
- **Venue**: Applied Economics
- **Citations**: 1 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1080/00036846.2024.2416091
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4403850866)
- **Abstract analysis**: Describe una metodología para extraer con PLN datos de grupos de redes sociales y sitios clasificados y calcular un tipo de cambio paralelo, implementada desde 2021, y valida la serie con modelos VAR e índices de spillover frente a un tipo oficial fijo y sobrevaluado. Es el precedente académico directo del uso del TRMI de elTOQUE en el informe: convierte señales informales en serie temporal verificable y mantiene separadas las tasas oficiales. La diferencia es que el informe toma la tasa publicada como insumo y no construye su propio estimador, y que su serie de precios es de autos, no de divisas.

#### P030 — Electromobility and Energy Transition in Cuba
- **Authors**: Castro Fernández, M.; Vilaragut Llanes, M.; Hernández, J. C.
- **Year**: 2024
- **Venue**: Sustainability
- **Citations**: 4 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.3390/su16229688
- **Layer**: L2
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4404141321)
- **Abstract analysis**: Analiza la introducción de energías renovables y la electrificación del transporte en Cuba, e identifica limitaciones y barreras de movilidad además de una hoja de ruta que incluye estaciones de carga y talleres de reparación/mantenimiento. Se solapa con las secciones 36, 41 y 42 del informe, que inventarian 12 estaciones de carga, 22 talleres y la dependencia de los circuitos eléctricos. La diferencia es de escala y propósito: el artículo propone política energética nacional, mientras el informe geolocaliza infraestructura existente para contextualizar el costo de moverse.

#### P031 — Cuba's Underground Economy
- **Authors**: Ritter, A. R. M.
- **Year**: 2004
- **Venue**: RePEc (Carleton Economic Papers)
- **Citations**: 20 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: http://www.carleton.ca/economics/wp-content/uploads/cep04-12.pdf
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W2188956700)

#### P032 — Currency exchange in post-ordenamiento Cuba: An exploration of institutional waiting for dollar purchases
- **Authors**: Ávila Castellanos, D. D.
- **Year**: 2024
- **Venue**: Revista Foro Cubano
- **Citations**: 2 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.22518/jour.rfc/2023.6a02
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4402744941)

#### P033 — The geography of car ownership in Mexico City: a joint model of households' residential location and car ownership decisions
- **Authors**: Guerra, E.
- **Year**: 2015
- **Venue**: Journal of Transport Geography
- **Citations**: 113 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1016/j.jtrangeo.2015.01.014
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W2015444861)

#### P034 — Transitions into and out of Car Ownership among Low-Income Households in the United States
- **Authors**: Klein, N. J.; Basu, R.; Smart, M. J.
- **Year**: 2023
- **Venue**: Journal of Planning Education and Research
- **Citations**: 27 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1177/0739456x231163755
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W4367844458)

#### P035 — Auto insurance affordability and the gap in car ownership: An analysis of transportation burden
- **Authors**: Srisan, T.; Ong, P. M.; Bills, T. S.
- **Year**: 2026
- **Venue**: Transport Policy
- **Citations**: 0 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1016/j.tranpol.2026.104491
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W7222828916)

### Cluster 5 — Señales de precio en marketplaces y lógica de comparables

**Query**: `online marketplace listing price asking transaction bias` y `used car market quality uncertainty Ebay motors online disclosure` (OpenAlex `fulltext.search`).

#### P036 — Reducing Interference Bias in Online Marketplace Pricing Experiments
- **Authors**: Holtz, D.; Lobel, R.; Liskovich, I.; Aral, S.
- **Year**: 2020
- **Venue**: SSRN Electronic Journal
- **Citations**: 59 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.2139/ssrn.3583836
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W3020710313)

#### P037 — Product Selection in Online Marketplaces
- **Authors**: Etro, F.
- **Year**: 2020
- **Venue**: Journal of Economics & Management Strategy
- **Citations**: 106 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1111/jems.12428
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W3163415732)

#### P038 — Market prices of remanufactured, used and new items: Evidence from eBay
- **Authors**: Quariguasi Frota Neto, J.; Bloemhof-Ruwaard, J. M.; Corbett, C. J.
- **Year**: 2015
- **Venue**: International Journal of Production Economics
- **Citations**: 136 (source: OpenAlex, fetched 2026-11-27T05:15:00Z)
- **URL**: https://doi.org/10.1016/j.ijpe.2015.02.006
- **Layer**: L1
- **Cited in document**: no
- **source_of_metadata**: OpenAlex (W1991842457)

## Recency distribution

El documento no contiene una sección de referencias bibliográficas numeradas. La única obra académica citada por nombre es P001 (1970); las demás fuentes mencionadas son normas, informes institucionales y repositorios, sin año bibliográfico asignable en este esquema. Por eso la columna derecha es 1 en `≤2021` y 0 en el resto.

| Year | In map | In document bibliography |
|---|---:|---:|
| 2026 | 7 | 0 |
| 2025 | 1 | 0 |
| 2024 | 6 | 0 |
| 2023 | 3 | 0 |
| 2022 | 1 | 0 |
| ≤2021 | 20 | 1 |

## Venue distribution

| Venue | Count in map |
|---|---:|
| arXiv (incl. arXiv/IEEE BigData) | 3 |
| Applied Economics | 2 |
| The Quarterly Journal of Economics | 1 |
| American Economic Review | 1 |
| The RAND Journal of Economics | 1 |
| Management Science | 1 |
| The Journal of Industrial Economics | 1 |
| ICIS Proceedings (AISeL) | 1 |
| Physica A | 1 |
| Advances in Economics, Management and Political Sciences | 1 |
| Computers & Industrial Engineering | 1 |
| Journal of Business Insight and Innovation | 1 |
| Federal Reserve Bank of New York Economic Policy Review | 1 |
| Real Estate Economics | 1 |
| TEM Journal | 1 |
| IJCESEN | 1 |
| IEEE ICESIT | 1 |
| Lecture Notes in Networks and Systems (Springer) | 1 |
| Communications of the AIS | 1 |
| Big Data & Society | 1 |
| Journal of Data and Information Quality | 1 |
| Proceedings on Privacy Enhancing Technologies | 1 |
| IJACSA | 1 |
| Journal of Frontiers in Multidisciplinary Research | 1 |
| Advances in Archaeological Practice | 1 |
| RePEc (Carleton Economic Papers) | 1 |
| Revista Foro Cubano | 1 |
| Journal of Transport Geography | 1 |
| Journal of Planning Education and Research | 1 |
| Transport Policy | 1 |
| SSRN Electronic Journal | 1 |
| Journal of Economics & Management Strategy | 1 |
| International Journal of Production Economics | 1 |

## Likely missing important works

### P002 — Asymmetric Information, Adverse Selection and Online Disclosure: The Case of eBay Motors
- Lewis, 2011, American Economic Review, 342 citas.
- **Cluster**: Asimetría de información y calidad en el mercado de vehículos usados.
- **Why likely missing**: Primero por citas en el clúster que da soporte teórico a una afirmación cargada del documento (la calidad se infiere de atributos visibles en el anuncios). Es el eslabón empírico entre Akerlof, citado, y la captura de defectos y tipo de vendedor; su ausencia deja el marco teórico sin la evidencia que lo conecta con precios observados en plataformas.

### P004 — Price Discontinuities in an Online Market for Used Cars
- Englmaier, Schmöller & Stowasser, 2017, Management Science, 50 citas.
- **Cluster**: Asimetría de información y calidad en el mercado de vehículos usados.
- **Why likely missing**: Top-5 por citas en un clúster directamente relevante para la serie `precios_por_anio.csv` y los comparables por modelo ±2 años. Advierte que el año de matrícula y el kilometraje operan como umbrales salientes, no como predictores lineales; el informe estima una pendiente log-lineal anual y después la retira, sin discutir esta alternativa.

### P014 — Car Price Prediction using Machine Learning Techniques
- Gegić et al., 2019, TEM Journal, 188 citas.
- **Cluster**: Modelos de precio, regresión hedónica y depreciación.
- **Why likely missing**: Obra más citada de su subárea y casi gemela metodológica del proyecto: scraping de portal de anuncios, extracción de atributos y modelo de predicción integrado en una aplicación. Cubre exactamente la combinación que el informe presenta como propio y permitiría situar la novedad del manejo de monedas, deduplicación y procedencia.

### P021 — Legality and Ethics of Web Scraping
- Krotov, Johnson & Silva, 2020, Communications of the AIS, 224 citas.
- **Cluster**: Ética, legalidad, procedencia y calidad de datos.
- **Why likely missing**: Obra fundacional del subárea que el informe declara central en la sección 10 sin referirla. La regla operativa «no eludir anti-automatización; registrar 403/429 como limitación» es una instancia de las preguntas que este trabajo formula para investigadores; citarlo reforzaría la distinción entre decisión técnica y justificación normativa.

### P023 — A Survey of Data Quality Requirements That Matter in ML Development Pipelines
- Priestley, O'Donnell & Simperl, 2023, Journal of Data and Information Quality, 153 citas.
- **Cluster**: Ética, legalidad, procedencia y calidad de datos.
- **Why likely missing**: Primera por citas del clúster de calidad de datos y directamente aplicable a la fase 7 (unificación, limpieza y control de calidad). El informe implementa validación por etapas pero no la enmarca en un marco reconocido, lo que deja sin respaldo la afirmación de que la arquitectura de colas y cuarentena es una decisión metodológica y no solo operativa.

### P022 — Web scraping for research: Legal, ethical, institutional, and scientific considerations
- Brown et al., 2025, Big Data & Society, 118 citas.
- **Cluster**: Ética, legalidad, procedencia y calidad de datos.
- **Why likely missing**: Cumple el criterio de publicación reciente del mismo tema (menos de 18 meses) y es la referencia más actualizada sobre cómo almacenar y compartir datos recolectados por scraping. La decisión del informe de conservar HTML crudo y excluir datos personales coincide con sus recomendaciones.

### P033 — The geography of car ownership in Mexico City
- Guerra, 2015, Journal of Transport Geography, 113 citas.
- **Cluster**: Cuba: divisas informales, movilidad y asequibilidad.
- **Why likely missing**: Obra influyente sobre asequibilidad y tenencia de automóvil en América Latina; el informe propone `asequibilidad = precio / salario` como métrica de la fase 8 sin antecedente regional. Su ausencia deja sin contexto comparativo una de las variables derivadas previstas en el marco analítico.

### P024 — Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability
- Hohensinner et al., 2026, arXiv:2601.14311, 13 citas.
- **Cluster**: Ética, legalidad, procedencia y calidad de datos.
- **Why likely missing**: Trabajo reciente del mismo tema que define con precisión la distinción entre procedencia y linaje que el informe aplica de facto en `provenancia`, hashes y manifiestos. Es la referencia contemporánea que permitiría declarar esa arquitectura como una adopción deliberada y no una solución ad hoc.

## Hypothesis checks (from plan)

No se recibieron `hypotheses_planned`. Las comprobaciones siguientes son observaciones derivadas de las afirmaciones cargadas del propio documento (secciones 17–20, 34, 52, 59–60); no son tests de hipótesis declaradas en un plan aprobado y no emiten veredicto.

### H1 — Los precios pedidos recogidos de anuncios pueden sustituir a estadísticas oficiales de transacción (derivada de §18 y §52)

La literatura coincide en que los datos de anuncios son una señal de precios pedidos y no de transacciones: Lewis (P002) muestra que el precio de subasta depende de divulgaciones del vendedor; Holtz et al. (P036) documentan interferencia entre participantes en experimentos de precios de marketplace; Etro (P037) modela la selección de productos en marketplaces; Quariguasi Frota Neto et al. (P038) comparan precios de bienes remanufacturados, usados y nuevos en eBay. Ninguno de estos trabajos sostiene que el precio anunciado sea equivalente al precio transado. El informe ya registra la salvedad en su auditoría de fuentes («precios pedidos, no transaccionados»), de modo que la evidencia encontrada respalda la cautela y no la sustitución. Queda sin dirección empírica la compatibilidad entre anuncios y estadísticas oficiales cubanas, porque los anuarios ONEI revisados no contienen series de parque ni de matriculaciones según el propio documento (§56).

### H2 — La tasa de depreciación anual estimada es estable y significativa (derivada de §34, §59 y §60)

El estado de la evidencia es mixto y desfavorable a una tasa única. Du et al. (P009), con especificación log-lineal anidada casi idéntica a la del informe, muestran que la relación edad–precio es no lineal y que el kilometraje pierde significancia al introducir términos de edad e interacción. Miranda et al. (P011) obtienen una pendiente anual significativa pero con R² de 0,256, kilometraje no significativo (p = 0,077) y correlación alta entre edad y kilometraje (r = 0,639). Englmaier et al. (P004) documentan saltos de precio en umbrales de año y cada 10.000 km. Francke y Van de Minne (P013) advierten sobre heterogeneidad no observada en modelos hedónicos. Este conjunto es compatible con la decisión del informe de retirar la afirmación de −5,43 % anual tras corregir kilometraje (p mínimo 0,165) y sugiere que la inestabilidad es un resultado esperable de la especificación, no una anomalía del proyecto.

### H3 — El marco de asimetría de información es aplicable al mercado de usados de La Habana (derivada de §17, §19 y §20)

Akerlof (P001) proporciona el marco y el documento lo cita explícitamente. La evidencia posterior muestra que los mecanismos que mitigan la asimetría son observables en datos de anuncios: divulgación voluntaria (P002), garantía y reputación del vendedor (P005), patrones de reparación como proxy de calidad oculta (P003) y alternativas institucionales como el leasing (P007). El informe captura año, texto de defectos y tipo de vendedor, pero no ha convertido esas variables en prueba del mecanismo; los campos de condición y costos de reacondicionamiento siguen en la lista de datos faltantes (§20). La literatura apoya la relevancia del marco, aunque no validan directamente su validez en un mercado con doble tasa de cambio y parque automotor informal.

### H4 — La recolección por scraping es sostenible sin eludir mecanismos anti-automatización (derivada de §10 y §11)

Krotov et al. (P021) y Brown et al. (P022) coinciden en que la legitimidad depende de revisar términos de uso, privacidad y normativa institucional antes de recolectar, no solo de la viabilidad técnica. Priestley et al. (P023) y Hohensinner et al. (P024) añaden que la calidad y la procedencia deben documentarse por etapa. El informe satisface la parte operativa —respeta HTTP 403/429, registra como limitación el bloqueo de carrosw y Cybo, conserva trazabilidad y evita datos personales— pero las fuentes revisadas no cubren el derecho cubano aplicable, que el propio informe deja como verificación pendiente antes de publicar. La evidencia encontrada apoya la coherencia procedimental; no permite pronunciarse sobre el cumplimiento legal en Cuba.

### H5 — La separación entre tasa oficial e informal es metodológicamente necesaria (derivada de §23, §52 y §18)

Vidal Alejandro et al. (P029) construyen una serie de tipo de cambio paralelo a partir de redes sociales y clasificados y la validan econométricamente, manteniendo separado el tipo oficial fijo y sobrevaluado. Ávila Castellanos (P032) documenta la experiencia cubana de espera institucional para comprar dólares. El informe adopta la TRMI de elTOQUE para convertir precios y conserva la tasa oficial de la BCC como referencia contrastada, sin mezclarlas. La literatura confirma que esa separación es una decisión metodológica estándar en el contexto cubano, aunque no resuelve cuál de las dos tasas debe emplearse para medir asequibilidad frente al salario.

## Sources used

- WebSearch queries: 8 intentos, todos con HTTP 403; registrados como fallo sostenido del proveedor.
- WebFetch URLs: 26 (OpenAlex API, arXiv API/abs/HTML y Crossref API).
- Semantic Scholar API hits: 0 (HTTP 403 en la única llamada intentada).
- OpenAlex API hits: 92 registros devueltos a partir de 18 consultas (búsquedas por texto completo, búsqueda por DOI y filtros por ID para resúmenes); 38 trabajos únicos incorporados al mapa.
- arXiv API hits: 9 registros de la consulta `all:"used car price"`; 3 páginas de resumen y 2 textos completos HTML consultados.
- Crossref API hits: 3 registros de la consulta `used car market asymmetric information`; solo uno relevante y ya cubierto por OpenAlex.
- Degradación: `degraded: false` — 38 trabajos L1 frente a 50 objetivo del preset Standard (76 %). La cobertura L3 quedó en 2 de 3 por disponibilidad de texto completo; los trabajos restantes se mantienen en L2.
- Nota de confianza: todas las citas y años se tomaron de las respuestas en vivo de OpenAlex o arXiv el 2026-11-27. Los conteos de citas de P018, P019 y P020 no son verificables desde las fuentes accesibles y se marcan `(metadata incomplete)`; el resumen de P010 no está indexado y también se marca `(metadata incomplete)`.

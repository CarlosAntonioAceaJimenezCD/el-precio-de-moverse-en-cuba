---
type: audit-artifact
phase: e2-literature
slug: corpus-total-2026-11-28
generated_at: 2026-11-28T21:10:00-05:00
preset: Standard
queries_run: 0
papers_l1: 41
papers_l2: 0
papers_l3: 0
language: es
degraded: false
---

# Literature Map — Corpus total

Nota de entrada. El plan aprobado (`reviews/corpus-total-2026-11-28.plan.md`, 20 líneas) declara `language: es`, `level: master` y `preset: Standard`, pero **no contiene `queries_planned` ni `hypotheses_planned`**. El mandato recibido para este extractor es estrecho y difiere del de la pasada anterior: el corpus auditado incorpora ahora el `README.md` con las 41 referencias numeradas **y** el anexo `Data/referencias.md`, por lo que hay que cotejar coherencia entre ambos y marcar lo no verificable. En consecuencia: (a) no se ejecutaron búsquedas web nuevas —los metadatos, conteos de citas y marcas `(metadata incomplete)` se heredan de la verificación OpenAlex/Crossref del 27/11/2026 consignada en `Data/referencias.md`—; (b) todos los ítems son L1, sin lectura de resúmenes (L2) ni de texto completo (L3); (c) los IDs `P001`–`P041` corresponden uno a uno a las entradas `[1]`–`[41]` del anexo; (d) los números de línea corresponden a la copia en caché `.playground/audit-cache/corpus-total-2026-11-28/corpus-total-2026-11-28.text.md` (2.584+ líneas); (e) `Cited in document` significa «presente en el corpus auditado», que ahora incluye tanto el README como el propio anexo; (f) el campo `Citada en el informe` del anexo se refiere al informe técnico de la pasada 1, **no** a este corpus.

**Resultado del cotejo:** correspondencia **41/41**. Las 41 entradas `[1]`–`[41]` del README (líneas 1717–1757 del cache; 97–137 de `README.md`) son **prefijos exactos** de las entradas homónimas de `Data/referencias.md` (líneas 2505–2584 del cache; 8–87 del original): mismo número, mismos autores, mismo título, mismo año y mismos identificadores en la parte visible. No hay reordenación, duplicados, huecos ni discrepancias de autoría, título o año entre ambos documentos. La única diferencia es de forma: el README **trunca** cada entrada (~150 caracteres), de modo que DOI/URL y la marca de verificación quedan cortados; la resolución completa solo está en el anexo.

## Clusters

Los seis clústers siguen la convención ya establecida en §71.14 del informe y en la pasada anterior; el séptimo agrupa el bloque institucional `[39]`–`[41]`, que no figura en la tabla de §71.14.

### Cluster 1 — Asimetría de información y selección adversa (mercado de autos usados)

**Query**: `asymmetric information adverse selection used car market` ∩ `Data/referencias.md` [1]–[8] (derivada del título y del resumen; sin búsqueda nueva).

#### P001 — The Market for "Lemons": Quality Uncertainty and the Market Mechanism
- **Authors**: Akerlof, G. A.
- **Year**: 1970
- **Venue**: The Quarterly Journal of Economics
- **Citations**: no registradas en el anexo (source: OpenAlex heredado, fetch 27/11/2026; `metadata incomplete`)
- **URL**: https://doi.org/10.2307/1879431
- **Layer**: L1
- **Cited in document**: yes (README línea 1717; anexo línea 2505; señalado entre los «más próximos» en línea 1716)
- **Document reference**: [1]
- **source_of_metadata**: `Data/referencias.md` [1]; `README.md` entrada truncada
- **Metadata status**: **(metadata incomplete: resumen indexado no sustantivo; identidad y DOI verificados en OpenAlex)**. El DOI completo no es verificable desde el README (`https://doi.org/10`).

#### P002 — Asymmetric Information, Adverse Selection and Online Disclosure: The Case of eBay Motors
- **Authors**: Lewis, G. M.
- **Year**: 2011 (el registro OpenAlex indexa la versión SSRN de 2010; publicación AER 2011)
- **Venue**: American Economic Review
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1257/aer.101.4.1535
- **Layer**: L1
- **Cited in document**: yes (README línea 1718; anexo línea 2507)
- **Document reference**: [2]
- **source_of_metadata**: `Data/referencias.md` [2]
- **Metadata status**: coherente entre documentos; **discrepancia de año documentada** (2010/2011), visible ya en el prefijo del README.

#### P003 — Adverse selection in the used-car market: evidence from purchase and repair patterns in the Consumer Expenditure Survey
- **Authors**: Peterson, J. R.; Schneider, H. S.
- **Year**: 2014
- **Venue**: The RAND Journal of Economics
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1111/1756-2171.12045
- **Layer**: L1
- **Cited in document**: yes (README línea 1719; anexo línea 2509)
- **Document reference**: [3]
- **source_of_metadata**: `Data/referencias.md` [3]; prefijo del README coincide.

#### P004 — Price Discontinuities in an Online Market for Used Cars
- **Authors**: Englmaier, F.; Schmöller, A.; Stowasser, T.
- **Year**: 2017
- **Venue**: Management Science
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1287/mnsc.2016.2714
- **Layer**: L1
- **Cited in document**: yes (README línea 1720; anexo línea 2511)
- **Document reference**: [4]
- **source_of_metadata**: `Data/referencias.md` [4].

#### P005 — Warranty, Seller Reputation, and Buyer Experience: Evidence From EBAY Used Car Auctions
- **Authors**: Che, X.; Katayama, H.; Lee, P.; Shi, N.
- **Year**: 2019
- **Venue**: The Journal of Industrial Economics
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1111/joie.12213
- **Layer**: L1
- **Cited in document**: yes (README línea 1721; anexo línea 2513)
- **Document reference**: [5]
- **source_of_metadata**: `Data/referencias.md` [5].

#### P006 — Adverse Selection and Reputation Systems in Online Auctions: Evidence from eBay Motors
- **Authors**: Wolf, J. R.; Muhanna, W. A.
- **Year**: 2005
- **Venue**: ICIS 2005 Proceedings (AIS Electronic Library)
- **Citations**: no registradas en el anexo
- **URL**: http://aisel.aisnet.org/cgi/viewcontent.cgi?article=1273&context=icis2005
- **Layer**: L1
- **Cited in document**: yes (README línea 1722; anexo línea 2515)
- **Document reference**: [6]
- **source_of_metadata**: `Data/referencias.md` [6]; es la única entrada del clúster sin DOI.

#### P007 — A model of the used car market with lemons and leasing
- **Authors**: Sultan, A.
- **Year**: 2009
- **Venue**: Applied Economics
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1080/00036840802314556
- **Layer**: L1
- **Cited in document**: yes (README línea 1723; anexo línea 2517)
- **Document reference**: [7]
- **source_of_metadata**: `Data/referencias.md` [7]; una de las pocas entradas del README donde el DOI completo sobrevive al truncamiento.

#### P008 — A Markovian model market—Akerlof's lemons and the asymmetry of information
- **Authors**: Tilles, P. F. C.; Ferreira, F. F.; Francisco, G.; Pereira, C. de B.; Sarti, F. M.
- **Year**: 2011
- **Venue**: Physica A: Statistical Mechanics and its Applications
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1016/j.physa.2011.03.007
- **Layer**: L1
- **Cited in document**: yes (README línea 1724; anexo línea 2519)
- **Document reference**: [8]
- **source_of_metadata**: `Data/referencias.md` [8].

### Cluster 2 — Modelos de precio, regresión hedónica y predicción

**Query**: `used car price hedonic regression machine learning prediction` ∩ `Data/referencias.md` [9]–[20].

#### P009 — Nonlinear Depreciation and Brand Heterogeneity in Chinese Used-Car Listing Prices
- **Authors**: Du, Z.; Yang, Z.; Zhang, Y.; Li, S.; Liu, Y.
- **Year**: 2026
- **Venue**: Advances in Economics, Management and Political Sciences
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.54254/2754-1169/2026.38524
- **Layer**: L1
- **Cited in document**: yes (README línea 1725; anexo línea 2521; «más próximo», línea 1716; `Citada en el informe: sí`, §71.6 y §71.14)
- **Document reference**: [9]
- **source_of_metadata**: `Data/referencias.md` [9]; prefijo coincide.

#### P010 — The pricing of used electric vehicles via machine learning and hedonic price model
- **Authors**: Kang, W.; Fu, X.
- **Year**: 2026
- **Venue**: Computers & Industrial Engineering
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1016/j.cie.2026.111964
- **Layer**: L1
- **Cited in document**: yes (README línea 1726; anexo línea 2523)
- **Document reference**: [10]
- **source_of_metadata**: `Data/referencias.md` [10]
- **Metadata status**: **(metadata incomplete: resumen no indexado; campos bibliográficos verificados)**.

#### P011 — Depreciation Patterns in the UAE Used Car Market: Evidence from Dubizzle Listings
- **Authors**: Miranda, A. M.; Alavi, A. B.; Gella, M. A.
- **Year**: 2026
- **Venue**: Journal of Business Insight and Innovation
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.63544/jbii.v5i6.110
- **Layer**: L1
- **Cited in document**: yes (README línea 1727; anexo línea 2525)
- **Document reference**: [11]
- **source_of_metadata**: `Data/referencias.md` [11].

#### P012 — Price Hedonics: A Critical Review
- **Authors**: Hulten, C. R.
- **Year**: 2003
- **Venue**: Federal Reserve Bank of New York Economic Policy Review
- **Citations**: no registradas en el anexo
- **URL**: https://newyorkfed.org/research/epr/03v09n3/0309hult.pdf
- **Layer**: L1
- **Cited in document**: yes (README línea 1728; anexo línea 2527; «más próximo», línea 1716)
- **Document reference**: [12]
- **source_of_metadata**: `Data/referencias.md` [12]; el README corta la URL (`https://newyorkfed.org/research/ep`).
- **Metadata status**: **(metadata incomplete: PDF no extraído)**.

#### P013 — Modeling unobserved heterogeneity in hedonic price models
- **Authors**: Francke, M.; Van de Minne, A.
- **Year**: 2020
- **Venue**: Real Estate Economics
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1111/1540-6229.12320
- **Layer**: L1
- **Cited in document**: yes (README línea 1729; anexo línea 2529)
- **Document reference**: [13]
- **source_of_metadata**: `Data/referencias.md` [13].

#### P014 — Car Price Prediction using Machine Learning Techniques
- **Authors**: Gegić, E.; Isaković, B.; Keco, D.; Mašetić, Z.; Kevrić, J.
- **Year**: 2019
- **Venue**: TEM Journal
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.18421/tem81-16
- **Layer**: L1
- **Cited in document**: yes (README línea 1730; anexo línea 2531; «más próximo», línea 1716; `Citada en el informe: sí`, §71.6 y §71.14)
- **Document reference**: [14]
- **source_of_metadata**: `Data/referencias.md` [14].

#### P015 — Using Linear Regression For Used Car Price Prediction
- **Authors**: Mutİ, S.; Yıldız, K.
- **Year**: 2023
- **Venue**: International Journal of Computational and Experimental Science and Engineering
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.22399/ijcesen.1070505
- **Layer**: L1
- **Cited in document**: yes (README línea 1731; anexo línea 2533)
- **Document reference**: [15]
- **source_of_metadata**: `Data/referencias.md` [15]; la grafía `Mutİ` (İ con punto) coincide en ambos documentos.

#### P016 — Price Prediction of Used Cars Using Machine Learning
- **Authors**: Jin, C.
- **Year**: 2021
- **Venue**: IEEE International Conference on Emergency Science and Information Technology (ICESIT)
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1109/icesit53460.2021.9696839
- **Layer**: L1
- **Cited in document**: yes (README línea 1732; anexo línea 2535)
- **Document reference**: [16]
- **source_of_metadata**: `Data/referencias.md` [16].

#### P017 — Used Car Price Prediction with Pyspark
- **Authors**: Ahtesham, M.; Zulfiqar, J.
- **Year**: 2022
- **Venue**: Lecture Notes in Networks and Systems (Springer)
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1007/978-3-031-01942-5_17
- **Layer**: L1
- **Cited in document**: yes (README línea 1733; anexo línea 2537)
- **Document reference**: [17]
- **source_of_metadata**: `Data/referencias.md` [17].

#### P018 — ProbSAINT: Probabilistic Tabular Regression for Used Car Pricing
- **Authors**: Madhusudhanan, K.; Behrens, G.; Stubbemann, M.; Schmidt-Thieme, L.
- **Year**: 2024
- **Venue**: arXiv:2403.03812; IEEE BigData 2024, Industry & Government Track
- **Citations**: 13 (source: OpenAlex heredado, fetch 27/11/2026)
- **URL**: https://arxiv.org/abs/2403.03812 · https://doi.org/10.1109/bigdata62323.2024.10825740
- **Layer**: L1
- **Cited in document**: yes (README línea 1734; anexo línea 2539; `Citada en el informe: sí`, §71.14)
- **Document reference**: [18]
- **source_of_metadata**: `Data/referencias.md` [18]; es una de las tres entradas con conteo de citas verificadas.

#### P019 — How much is my car worth? A methodology for predicting used cars prices using Random Forest
- **Authors**: Pal, N.; Arora, P.; Sundararaman, D.; Kohli, P.; Palakurthy, S. S.
- **Year**: 2017 (preprint; publicación 2018)
- **Venue**: arXiv:1711.06970 (FICC, Camera Ready)
- **Citations**: 96 (source: OpenAlex heredado, fetch 27/11/2026)
- **URL**: https://arxiv.org/abs/1711.06970 · https://doi.org/10.1007/978-3-030-03402-3_28
- **Layer**: L1
- **Cited in document**: yes (README línea 1735; anexo línea 2541)
- **Document reference**: [19]
- **source_of_metadata**: `Data/referencias.md` [19]; preprint 2017 / publicación 2018, discrepancia de año documentada en ambas copias.

#### P020 — Second Hand Price Prediction for Tesla Vehicles
- **Authors**: Arefin, S. E.
- **Year**: 2021
- **Venue**: arXiv:2101.03788
- **Citations**: 9 (source: OpenAlex heredado, fetch 27/11/2026)
- **URL**: https://arxiv.org/abs/2101.03788
- **Layer**: L1
- **Cited in document**: yes (README línea 1736; anexo línea 2543; entrada completa en el README)
- **Document reference**: [20]
- **source_of_metadata**: `Data/referencias.md` [20].

### Cluster 3 — Ética, legalidad y procedencia del scraping; calidad de datos

**Query**: `web scraping ethics legality data provenance quality pipelines` ∩ `Data/referencias.md` [21]–[28].

#### P021 — Legality and Ethics of Web Scraping
- **Authors**: Krotov, V.; Johnson, L.; Silva, L.
- **Year**: 2020
- **Venue**: Communications of the Association for Information Systems
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.17705/1cais.04724
- **Layer**: L1
- **Cited in document**: yes (README línea 1737; anexo línea 2545)
- **Document reference**: [21]
- **source_of_metadata**: `Data/referencias.md` [21].

#### P022 — Web scraping for research: Legal, ethical, institutional, and scientific considerations
- **Authors**: Brown, M. A.; Gruen, A.; Maldoff, G.; Messing, S.; Sanderson, Z.; Zimmer, M. T.
- **Year**: 2025
- **Venue**: Big Data & Society
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1177/20539517251381686
- **Layer**: L1
- **Cited in document**: yes (README línea 1738; anexo línea 2547)
- **Document reference**: [22]
- **source_of_metadata**: `Data/referencias.md` [22]; única entrada 2025 del mapa.

#### P023 — A Survey of Data Quality Requirements That Matter in ML Development Pipelines
- **Authors**: Priestley, M.; O'Donnell, F.; Simperl, E. P. B.
- **Year**: 2023
- **Venue**: Journal of Data and Information Quality
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1145/3592616
- **Layer**: L1
- **Cited in document**: yes (README línea 1739; anexo línea 2549)
- **Document reference**: [23]
- **source_of_metadata**: `Data/referencias.md` [23].

#### P024 — Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability in LLMs
- **Authors**: Hohensinner, R.; Mutlu, B.; Mendoza Estrada, I. G.; Vukovic, M.; Kopeinik, S.; Kern, R.
- **Year**: 2026
- **Venue**: arXiv:2601.14311 (manuscrito enviado a ACM Computing Surveys)
- **Citations**: no registradas en el anexo
- **URL**: https://arxiv.org/abs/2601.14311
- **Layer**: L1
- **Cited in document**: yes (README línea 1740; anexo línea 2551)
- **Document reference**: [24]
- **source_of_metadata**: `Data/referencias.md` [24]; **no verificable en esta pasada** si el estado de «enviado» cambió desde el 27/11/2026.

#### P025 — Data Isotopes for Data Provenance in DNNs
- **Authors**: Wenger, E.; Li, X.; Zhao, B. Y.; Shmatikov, V.
- **Year**: 2024
- **Venue**: Proceedings on Privacy Enhancing Technologies
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.56553/popets-2024-0024
- **Layer**: L1
- **Cited in document**: yes (README línea 1741; anexo línea 2553)
- **Document reference**: [25]
- **source_of_metadata**: `Data/referencias.md` [25].

#### P026 — A Pipeline for Integrating and Analyzing Public Business Data in Albania Using Web Scraping and Machine Learning
- **Authors**: Muça, M.; Bani, K.; Alla, A.
- **Year**: 2026
- **Venue**: International Journal of Advanced Computer Science and Applications
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.14569/ijacsa.2026.0170845
- **Layer**: L1
- **Cited in document**: yes (README línea 1742; anexo línea 2555; «más próximo», línea 1716; `Citada en el informe: sí`, §71.6 y §71.14)
- **Document reference**: [26]
- **source_of_metadata**: `Data/referencias.md` [26].

#### P027 — The Ethics of Web Scraping In Research: A Review
- **Authors**: Essien, I. A.; Adebayo, A. O.; Afuwape, A. A.; Eboseremen, B. O.; Oladega, F.; Soneye, O. M.
- **Year**: 2023
- **Venue**: Journal of Frontiers in Multidisciplinary Research
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.54660/.jfmr.2023.4.1.529-538
- **Layer**: L1
- **Cited in document**: yes (README línea 1743; anexo línea 2557)
- **Document reference**: [27]
- **source_of_metadata**: `Data/referencias.md` [27].

#### P028 — The Legality and Ethics of Web Scraping in Archaeology
- **Authors**: Paige, J.
- **Year**: 2024
- **Venue**: Advances in Archaeological Practice
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1017/aap.2023.42
- **Layer**: L1
- **Cited in document**: yes (README línea 1744; anexo línea 2559)
- **Document reference**: [28]
- **source_of_metadata**: `Data/referencias.md` [28].

### Cluster 4 — Cuba: divisas informales, economía sumergida y electromovilidad

**Query**: `Cuba informal currency market underground economy electromobility car ownership` ∩ `Data/referencias.md` [29]–[32].

#### P029 — Using AI in the informal currency market: evidence from Cuba
- **Authors**: Vidal Alejandro, P.; Muñiz-Cuza, C. E.; Calas Torres, A.
- **Year**: 2024
- **Venue**: Applied Economics
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1080/00036846.2024.2416091
- **Layer**: L1
- **Cited in document**: yes (README línea 1745; anexo línea 2561; «más próximo», línea 1716; `Citada en el informe: sí`, §71.6 y §71.14)
- **Document reference**: [29]
- **source_of_metadata**: `Data/referencias.md` [29]; solapamiento temático directo con la TRMI informal del README (líneas 1712 y 1751 del cache).

#### P030 — Electromobility and Energy Transition in Cuba
- **Authors**: Castro Fernández, M.; Vilaragut Llanes, M.; Hernández, J. C.
- **Year**: 2024
- **Venue**: Sustainability
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.3390/su16229688
- **Layer**: L1
- **Cited in document**: yes (README línea 1746; anexo línea 2563)
- **Document reference**: [30]
- **source_of_metadata**: `Data/referencias.md` [30].

#### P031 — Cuba's Underground Economy
- **Authors**: Ritter, A. R. M.
- **Year**: 2004
- **Venue**: RePEc (Carleton Economic Papers)
- **Citations**: no registradas en el anexo
- **URL**: https://ir.library.carleton.ca/pub/15983
- **Layer**: L1
- **Cited in document**: yes (README línea 1747; anexo línea 2565; entrada completa en el README)
- **Document reference**: [31]
- **source_of_metadata**: `Data/referencias.md` [31].

#### P032 — Currency exchange in post-ordenamiento Cuba: An exploration of institutional waiting for dollar purchases
- **Authors**: Ávila Castellanos, D. D.
- **Year**: 2024
- **Venue**: Revista Foro Cubano
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.22518/jour.rfc/2023.6a02
- **Layer**: L1
- **Cited in document**: yes (README línea 1748; anexo línea 2567)
- **Document reference**: [32]
- **source_of_metadata**: `Data/referencias.md` [32]; nótese el desfase año del DOI (`...2023.6a02`) frente al año declarado 2024, presente en ambas copias y no marcado como discrepancia en el anexo.

### Cluster 5 — Propiedad y asequibilidad del automóvil (México y EE. UU.)

**Query**: `car ownership affordability households transport burden` ∩ `Data/referencias.md` [33]–[35] (agrupado con [29]–[32] en §71.14).

#### P033 — The geography of car ownership in Mexico City
- **Authors**: Guerra, E.
- **Year**: 2015
- **Venue**: Journal of Transport Geography
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1016/j.jtrangeo.2015.01.014
- **Layer**: L1
- **Cited in document**: yes (README línea 1749; anexo línea 2569)
- **Document reference**: [33]
- **source_of_metadata**: `Data/referencias.md` [33].

#### P034 — Transitions into and out of Car Ownership among Low-Income Households in the United States
- **Authors**: Klein, N. J.; Basu, R.; Smart, M. J.
- **Year**: 2023
- **Venue**: Journal of Planning Education and Research
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1177/0739456x231163755
- **Layer**: L1
- **Cited in document**: yes (README línea 1750; anexo línea 2571)
- **Document reference**: [34]
- **source_of_metadata**: `Data/referencias.md` [34].

#### P035 — Auto insurance affordability and the gap in car ownership: An analysis of transportation burden
- **Authors**: Srisan, T.; Ong, P. M.; Bills, T. S.
- **Year**: 2026
- **Venue**: Transport Policy
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1016/j.tranpol.2026.104491
- **Layer**: L1
- **Cited in document**: yes (README línea 1751; anexo línea 2573)
- **Document reference**: [35]
- **source_of_metadata**: `Data/referencias.md` [35].

### Cluster 6 — Señales de precio en marketplaces

**Query**: `online marketplace pricing experiments product selection remanufactured used goods eBay` ∩ `Data/referencias.md` [36]–[38].

#### P036 — Reducing Interference Bias in Online Marketplace Pricing Experiments
- **Authors**: Holtz, D.; Lobel, R.; Liskovich, I.; Aral, S.
- **Year**: 2020
- **Venue**: SSRN Electronic Journal
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.2139/ssrn.3583836
- **Layer**: L1
- **Cited in document**: yes (README línea 1752; anexo línea 2575; entrada completa en el README)
- **Document reference**: [36]
- **source_of_metadata**: `Data/referencias.md` [36]; `SSRN Electronic Journal` implica estado de preprint, no marcado `(metadata incomplete)` en el anexo.

#### P037 — Product Selection in Online Marketplaces
- **Authors**: Etro, F.
- **Year**: 2020
- **Venue**: Journal of Economics & Management Strategy
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1111/jems.12428
- **Layer**: L1
- **Cited in document**: yes (README línea 1753; anexo línea 2577)
- **Document reference**: [37]
- **source_of_metadata**: `Data/referencias.md` [37].

#### P038 — Market prices of remanufactured, used and new items: Evidence from eBay
- **Authors**: Quariguasi Frota Neto, J.; Bloemhof-Ruwaard, J. M.; Corbett, C. J.
- **Year**: 2015 (2015 en OpenAlex; 2016 en Crossref published-print)
- **Venue**: International Journal of Production Economics
- **Citations**: no registradas en el anexo
- **URL**: https://doi.org/10.1016/j.ijpe.2015.02.006
- **Layer**: L1
- **Cited in document**: yes (README línea 1754; anexo línea 2579)
- **Document reference**: [38]
- **source_of_metadata**: `Data/referencias.md` [38]; resumen no indexado en OpenAlex; **discrepancia de año documentada** (2015/2016) en el anexo, pero **no visible en el README** por truncamiento.

### Cluster 7 — Fuentes institucionales foráneas (bloque [39]–[41])

**Query**: `institutional vehicle registration statistics sources` ∩ `Data/referencias.md` [39]–[41].

#### P039 — Vehicle statistics (DfT / DVLA)
- **Authors**: Department for Transport / DVLA (organismo oficial del Reino Unido)
- **Year**: sin año declarado
- **Venue**: GOV.UK
- **Citations**: no aplica
- **URL**: https://www.gov.uk/government/organisations/department-for-transport
- **Layer**: L1
- **Cited in document**: yes (README línea 1755; anexo línea 2580; `Citada en el informe: sí`, §70)
- **Document reference**: [39]
- **source_of_metadata**: `Data/referencias.md` [39]; el README conserva la marca `(metadata incompl...` truncada.
- **Metadata status**: **(metadata incomplete: URL profunda no confirmada)**. El anexo afirma «Citada en el informe: sí (§70 y §71.14)», pero la tabla de §71.14 (líneas 1568–1607) **no contiene fila [39]** → inconsistencia interna marcada más abajo.

#### P040 — Informes del sector automotriz español
- **Authors**: ANFAC (asociación sectorial)
- **Year**: sin año declarado
- **Venue**: https://anfac.com/ (sitio oficial)
- **Citations**: no aplica
- **URL**: https://anfac.com/
- **Layer**: L1
- **Cited in document**: yes (README línea 1756; anexo línea 2582; `Citada en el informe: sí`, fuente institucional en §70)
- **Document reference**: [40]
- **source_of_metadata**: `Data/referencias.md` [40]; entrada completa en el README. Sin año, DOI ni fecha de acceso: **no verificable bibliográficamente** más allá del sitio raíz.

#### P041 — Estadísticas de matriculaciones
- **Authors**: AEADE (asociación sectorial)
- **Year**: sin año declarado
- **Venue**: https://www.aeade.net/ (sitio oficial)
- **Citations**: no aplica
- **URL**: https://www.aeade.net/
- **Layer**: L1
- **Cited in document**: yes (README línea 1757; anexo línea 2584; `Citada en el informe: sí`, fuente institucional en §70)
- **Document reference**: [41]
- **source_of_metadata**: `Data/referencias.md` [41]; entrada completa en el README. Misma limitación que P040.

## Cotejo README ↔ `Data/referencias.md`

| Comprobación | Resultado | Evidencia |
|---|---|---|
| Números `[1]`–`[41]` presentes en ambos | 41/41 | Búsqueda literal; sin huecos ni duplicados |
| Orden de las entradas | idéntico | `[n]` del README aparece en la misma posición del anexo |
| Autores y títulos | idénticos | Las 41 cadenas del README son prefijos exactos de las del anexo |
| Años visibles en el prefijo | idénticos | Incluye los casos con discrepancia documentada [2], [19], [38] |
| Identificadores visibles (DOI/URL/arXiv) | idénticos en la parte no truncada | p. ej. [7], [20], [28], [31], [37], [39]–[41] |
| Marcas `(metadata incomplete)` | preservadas cuando caen dentro del prefijo | [1], [12], [39]; [10] y [38] quedan fuera del truncamiento |
| Marcas `Citada en el informe` | preservadas cuando caen dentro del prefijo | [20], [31], [40], [41] y otras |
| Completitud de DOI/URL en el README | **no** — 38 de 41 están truncadas a mitad de identificador | p. ej. [1] `https://doi.org/10`, [12] `https://newyorkfed.org/research/ep`, [18] `arXiv:2403.038` |
| «Más próximos» declarados en README | 6: [1], [9], [12], [14], [26], [29] | línea 1716 |
| Discutidos en §71.6 según §71.14 | 5: [1], [9], [14], [26], [29] | línea 1609 — **[12] queda fuera** de esa lista aunque sí está entre los «más próximos» |

## Recency distribution

| Year | In map | In document bibliography |
|---|---:|---:|
| 2026 | 6 | 6 |
| 2025 | 1 | 1 |
| 2024 | 6 | 6 |
| 2023 | 4 | 4 |
| 2022 | 1 | 1 |
| ≤2021 | 20 | 20 |
| Sin año verificable | 3 | 3 |

Ambas columnas coinciden porque el mapa *es* la bibliografía del documento: `P001`–`P041` se derivan uno a uno de `[1]`–`[41]`. Los tres «sin año» son [39]–[41] (fuentes institucionales). El desglose de ≤2021 es: 2020 (4), 2019 (2), 2017 (2), 2015 (2), 2014 (1), 2011 (2), 2009 (1), 2005 (1), 2004 (1), 2003 (1), 1970 (1).

## Venue distribution

| Venue (agrupado) | Count in map |
|---|---:|
| Revistas de economía, mercados y transporte / congresos afines ([1]–[8], [29]–[38]) | 18 |
| Revistas y centros de metodología, predicción y modelado ([9]–[20]) | 12 |
| Revistas de ética, legalidad, calidad y procedencia de datos ([21]–[28]) | 8 |
| Sitios institucionales foráneos ([39]–[41]) | 3 |

## Likely missing important works

No se proponen obras externas nuevas: no se ejecutaron búsquedas temáticas y la bibliografía del documento es exactamente el conjunto mapeado, por lo que cualquier candidato «ausente de la bibliografía» sería **no verificable** en esta pasada. Con criterio adaptado, se registran las únicas ausencias *internas* detectadas (obras del anexo que no aparecen donde el propio anexo dice que aparecen):

### P039 — Vehicle statistics (DfT / DVLA) — ausente de la tabla §71.14

- Department for Transport / DVLA, sin año, GOV.UK, [39] en `Data/referencias.md`.
- **Cluster**: Fuentes institucionales foráneas.
- **Why likely missing**: el anexo declara `Citada en el informe: sí (§70 y §71.14)`, pero la tabla de §71.14 enumera solo `[1]`–`[38]` (líneas 1570–1607). [39] sí está en §70 (líneas 1506/1508) y en el README, de modo que la mención §71.14 es la única no corroborada. **No verificable** la afirmación tal como está redactada.

### P012 — Price Hedonics: A Critical Review — fuera de la lista de «discutidos en §71.6»

- Hulten, C. R. (2003), Federal Reserve Bank of New York Economic Policy Review, [12]; `metadata incomplete: PDF no extraído`.
- **Cluster**: Modelos de precio, regresión hedónica y predicción.
- **Why likely missing**: el README lo cuenta entre los seis «más próximos» (línea 1716) y §71.14 lo include en su tabla, pero el propio §71.14 dice que solo `[1], [9], [14], [26] y [29]` «se discuten además en §71.6» (línea 1609). No es una ausencia de la bibliografía, sino una discrepancia de alcance entre dos declaraciones del corpus. **No verificable** cuál de las dos listas es la vigente sin consultar §71.6 completo.

## Hypothesis checks (from plan)

El plan no declara hipótesis; las cinco siguientes se derivan del mandato recibido y son observaciones sin veredicto.

### H1 — Los marcadores `[1]`–`[41]` del README coinciden con las entradas de `Data/referencias.md` (derivada)

Estado de la evidencia: **sí, 41/41**. Cotejo literal: mismos números, mismos autores, mismos títulos, mismos años y mismos identificadores en la parte visible. No hay reordenación, duplicados ni huecos. A diferencia de la pasada anterior —donde el cotejo dio cero coincidencias porque el corpus de usuario no contenía marcadores— la incorporación del README al corpus total resuelve la discrepancia: el anexo y la cara pública del proyecto comparten ahora un único régimen de citas.

### H2 — Los identificadores del README permiten verificar las referencias por sí solos (derivada)

Estado de la evidencia: **no**. 38 de las 41 entradas del README están truncadas a mitad de DOI/URL, y las tres marcas `(metadata incomplete)` que caen dentro del prefijo ([1], [12], [39]) aparecen cortadas (`**(metadata incompl`). Las dos entradas completas ([20], [40], [41], y casi [7], [28], [31], [37]) son la excepción. La resolución depende del anexo: el README es un índice legible, no una bibliografía autocontenida. Esto es coherente con la línea 141 del README, que remite explícitamente a `Data/referencias.md` (41 entradas).

### H3 — Toda entrada del anexo tiene metadatos verificables (derivada)

Estado de la evidencia: **no**. Cuatro entradas llevan marca explícita `(metadata incomplete)`: [1] (resumen indexado no sustantivo, identidad y DOI sí verificados), [10] (resumen no indexado, campos bibliográficos verificados), [12] (PDF no extraído) y [39] (URL profunda no confirmada). Tres más registran discrepancias de año: [2] (SSRN 2010 / AER 2011), [19] (preprint 2017 / publicación 2018) y [38] (OpenAlex 2015 / Crossref 2016). El bloque [39]–[41] carece de año, DOI y fecha de acceso; [24] depende de un estado de «manuscrito enviado» que no se re-verificó. Ninguna de estas marcas fue re-fetcheada en esta pasada.

### H4 — El bloque institucional [39]–[41] está reflejado de forma coherente en §70, §71.14 y el README (derivada)

Estado de la evidencia: **parcial**. Los tres aparecen en §70 (líneas 1506/1508), en el README (líneas 1755–1757) y en el anexo (líneas 2580–2584). Pero la tabla de §71.14 solo cubre `[1]`–`[38]`; el anexo atribuye a [39] una mención en §71.14 que la tabla no respalda, mientras que [40] y [41] se declaran correctamente como «fuente institucional en §70». La coherencia es, por tanto, completa para §70 y el README, y rota para el par `[39]`/§71.14.

### H5 — La novedad declarada (procedencia y normalización sobre datos cubanos) está respaldada por el mapa literario (derivada)

Estado de la evidencia: **el mapa contiene los antecedentes, pero el corpus no los activa como respaldo**. La línea 1758 del README declara que el diferenciador es de procedencia y normalización, no de método, y que la última pasada «no hizo búsqueda bibliográfica nueva ni lectura de texto completo (§71.14)». En el anexo existen [23] (calidad de datos en pipelines ML), [24] y [25] (procedencia y trazabilidad), [21]/[22]/[27]/[28] (ética y legalidad del scraping) y [29]/[32] (divisas informales cubanas), todos con `Citada en el informe: no`. El solapamiento temático es alto; la activación discursiva en la cara pública del proyecto, nula aparte de la lista numerada. Esto reproduce, con otro corpus, la observación de la pasada anterior: documentación metodológicamente argumentada pero bibliográficamente muda fuera del anexo.

## Sources used

- WebSearch queries: 0 (cotejo dirigido entre dos documentos del corpus; sin búsquedas temáticas nuevas).
- WebFetch URLs: 0; no se re-fetchearon los DOI, arXiv ni las URLs GOV.UK, anfac.com o aeade.net.
- Semantic Scholar API hits: 0.
- OpenAlex API hits: 0 nuevos; los metadatos, los conteos de citas de [18] (13), [19] (96) y [20] (9) y las marcas `(metadata incomplete)` se heredan de la verificación del 27/11/2026 consignada en `Data/referencias.md`.
- Archivos locales inspeccionados: `reviews/corpus-total-2026-11-28.plan.md` (20 líneas); `.playground/audit-cache/corpus-total-2026-11-28/corpus-total-2026-11-28.text.md` (10 bloques `ARCHIVO`; cotejo en líneas 1619–1776 para README, 1566–1609 para §71.14, 1504–1508 para §70 y 2496–2584 para `Data/referencias.md`); `README.md` (152 líneas); `Data/referencias.md` (87 líneas); `reviews/corpus-documentacion-2026-11-28.e2-literature.md` (convención de formato y antecedente del cotejo).
- Verificación mecanizada: comparación prefijo-a-prefijo de las 41 entradas README frente a las 41 del anexo; 41/41 coincidencias, 0 discrepancias.
- Degradación: `degraded: false` para el mandato recibido —las 41 entradas, sus marcadores y sus estados quedaron resueltos por inspección directa—. Limitación declarada: sin búsqueda bibliográfica nueva, sin lectura de resúmenes y sin re-fetch de URLs; este mapa certifica **coherencia documental**, no la vigencia externa de los metadatos heredados del 27/11/2026. V4/V5 deben tratar las cuatro marcas `(metadata incomplete)`, las tres discrepancias de año y la anomalía `[39]`/§71.14 como extremos no verificables en esta pasada.

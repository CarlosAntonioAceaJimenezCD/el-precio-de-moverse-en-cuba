---
type: audit-artifact
phase: v5-state-of-the-art
slug: corpus-documentacion-2026-11-28
generated_at: 2026-11-28T03:53:58-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md
language: es
level: master
---

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

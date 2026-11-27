---
type: audit-report
slug: informe-tecnico-2026-11-27-iter2
generated_at: 2026-11-27
audited_document: INFORME_TECNICO.md
audited_document_title: Informe técnico / Technical report — El precio de moverse en Cuba
language: es
level: master
preset: Standard
phases_executed: [0, 1, 2, 3]
dimensions_run: [V1, V2, V3, V4, V5, V6, V7, V8, V9]
dimensions_skipped: []
phase1_failures: []
phase2_failures: []
phase_artifacts:
  plan: reviews/informe-tecnico-2026-11-27-iter2.plan.md
  e1: reviews/informe-tecnico-2026-11-27-iter2.e1-claims.md
  e2: reviews/informe-tecnico-2026-11-27-iter2.e2-literature.md
  e3: reviews/informe-tecnico-2026-11-27-iter2.e3-artifacts.md
  v1: reviews/informe-tecnico-2026-11-27-iter2.v1-structure.md
  v2: reviews/informe-tecnico-2026-11-27-iter2.v2-methodology.md
  v3: reviews/informe-tecnico-2026-11-27-iter2.v3-results-evidence.md
  v4: reviews/informe-tecnico-2026-11-27-iter2.v4-novelty.md
  v5: reviews/informe-tecnico-2026-11-27-iter2.v5-state-of-the-art.md
  v6: reviews/informe-tecnico-2026-11-27-iter2.v6-reproducibility.md
  v7: reviews/informe-tecnico-2026-11-27-iter2.v7-writing.md
  v8: reviews/informe-tecnico-2026-11-27-iter2.v8-bibliography.md
  v9: reviews/informe-tecnico-2026-11-27-iter2.v9-ethics.md
  forensic: reviews/informe-tecnico-2026-11-27-iter2.forensic.md
  report: reviews/informe-tecnico-2026-11-27-iter2.md
previous_iterations: [reviews/informe-tecnico-2026-11-27.md]
---

# Auditoría — Informe técnico / Technical report

**Autor / Tesista:** responsable del proyecto / project owner; el documento no consigna nombre propio  
**Título:** Informe técnico / Technical report — El precio de moverse en Cuba  
**Institución:** no declarada  
**Tutor:** no declarado  
**Fecha del documento:** 23/11/2026; última actualización 27/11/2026  
**Fecha de la auditoría:** 27/11/2026  
**Páginas:** sin paginación en la copia cacheada; 1.484 líneas de texto bilingüe español/inglés  
**Repositorio:** CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba

## 1. Resumen ejecutivo

La segunda pasada muestra un trabajo con bases metodológicas sólidas y con avances formales verificables, que todavía requiere revisión mayor antes de la defensa porque tres estados del mismo modelo conviven sin etiqueta de vigencia y el aparato bibliográfico recién incorporado no ha entrado en el argumento. El diagnóstico se apoya en el cotejo entre lo que el documento declara y lo que los archivos del repositorio contienen, y en la comprobación de las ocho observaciones transversales de la pasada anterior: dos quedaron resueltas, cuatro permanecen abiertas de forma parcial y una sigue sin resolución. El texto incorporó 520 palabras y 22 líneas, siete reescrituras puntuales y dos secciones nuevas; ese incremento es medible y no altera los patrones de prosa dominantes.

La divergencia más visible de la iteración primera ha quedado circunscrita. Las dos introducciones enuncian ahora el mismo objetivo —«un análisis del mercado automotor cubano» (§1)— y el recomendador interactivo queda diferido por escrito en ambas lenguas; la tabla de fases añade una nota que remite los resultados vigentes a §59–§60. Persisten, sin embargo, la fila octava de la tabla inglesa, que conserva «interactive product» en el nombre de la fase (§2), y la quinta conclusión, que afirma en español que el modelo «se regeneran de forma automática» (§12) y en inglés que «are not implemented yet» (§12). Un tribunal que lea solo la Parte II hallará una negación de la fase 8 donde la Parte I documenta su ejecución.

El relato de cierre fija en §59 «2.029 anuncios limpios» y «43.000 km» y sostiene que «los valores se actualizan solos en `outputs/tables/kpis.csv`». El archivo citado registra 2.156 anuncios y 33.256 km: coinciden tres de las nueve cifras y difieren las otras seis. El párrafo inglés inmediato conserva 744 autos y 2.014 anuncios, y §58 guarda todavía 2.014 anuncios y 44.125 km. La automatización opera en el repositorio —el README y la presentación de storytelling llevan los marcadores resueltos—, pero la copia cacheada del informe no se regeneró y ofrece tres lecturas distintas del mismo objeto.

La retirada de la depreciación es correcta en su fondo: en los archivos vigentes ninguno de los siete coeficientes no intercepto alcanza p < 0,05 y la edad del vehículo figura con p = 0,1504. El relato, sin embargo, no coincide con el archivo en el R² —0,277 frente a 0,2744—, omite la especificación de 584 observaciones y reproduce en §60 las cifras «p mínimo 0,165; VIF 1,13–1,58» que pertenecen a una corrida anterior. El paso de 584 a 28 observaciones confunde el efecto del componente con la selección muestral, sin ablación declarada ni contraste pareado entre configuraciones.

El aparato bibliográfico cambió de naturaleza: 38 entradas numeradas con DOI o URL, campo de citación y cuatro fuentes declaradas verificadas. El cuerpo del informe conserva cero marcas numéricas de cita; una sola entrada figura como citada; nueve de las trece afirmaciones portantes carecen de cita; las dieciocho obras de 2022–2026 permanecen sin mención. La mejora es de transparencia formal, no de engagement argumentativo. En paralelo, la declaración de uso de inteligencia artificial cierra una ausencia y enuncia un protocolo de contraste —«ninguna afirmación empírica se originó en una salida de IA sin contraste contra los archivos» (§69)—, pero nombra solo la skill de auditoría, omite la generación de los seis scripts propios y la traducción del texto bilingüe.

El único rasgo de novedad del inventario sigue siendo la adopción de una arquitectura ajena adaptada a fuentes cubanas; el único párrafo comparativo opone el proyecto a un repositorio egipcio por escala de datos. Los vecinos académicos más cercanos figuran en la lista numerada sin citas en el cuerpo. En el repositorio, las cotas compatibles de dependencias, la semilla del orquestador y la prueba de humo existen en el árbol de trabajo y no en el commit declarado, de modo que un clon limpio no las encuentra.

Una jornada de trabajo concentrado resuelve la tabla de versiones y la divergencia inglesa; llevar el documento a estado defendible insume entre treinta y cuarenta y dos horas repartidas en cuatro bloques, sin nueva recolección de datos.

## 2. Fortalezas estructurales del documento

La primera fortaleza es la densidad de la captura y la precisión con que se declara su tamaño en cada etapa. El texto consigna once bases SQLite preparadas por tienda, ocho marketplaces con inventario real, doce anuarios del ONEI correspondientes a 2014–2025, 82 fragmentos de 10 MB con manifiesto verificado y 25 tablas en la base consolidada de repositorios de referencia. Los recuentos no se presentan solo como totales: §22 declara 323 autos con 248 precios en USD válidos, §34 reporta 972 filas ingeridas y 499 limpias, §50 cuantifica la encuesta en 33 personas y las entrevistas en 30 + 30 + 8, y §59 fija 981 candidatas. El rasero de maestría exige al menos veinte ensayos y diez conjuntos o instancias; el documento los supera con holgura en el plano declarado y los acompaña de rutas verificables en el repositorio. La cobertura es desigual —la marca alcanza 68,4 %, el año 63,5 % y el kilometraje 6,2 % (§22)—, pero esa desigualdad está cuantificada y no se disfraza.

La segunda fortaleza es la consistencia aritmética de los desgloses internos. Las once filas de la tabla por tienda suman exactamente las 256 filas anunciadas; en §15, 304 autos más 6.028 exclusiones dan 6.332 anuncios, y 5.983 más 45 dan 6.028; en §31, 548 autos y 9.409 exclusiones dan 9.957; en §50, 369 anuncios ya presentes más 3.589 nuevos dan 3.958; en §51, 748 identificadores únicos menos cuatro anuncios excluidos dan 744; y 872 más 99 más dos dan 973 precios recuperados. Cada cadena aparece con las mismas cifras en su paralelo inglés. Estas sumas constituyen la porción del documento que mejor resiste una réplica: no requieren interpretación, solo repetición de la operación.

La tercera fortaleza es el tratamiento explícito de los límites. §19 dedica un apartado propio a los límites y enumera precios pedidos no transaccionados, sesgo de supervivencia de anuncios, ausencia de datos personales y vigencia normativa pendiente. §18 remata la auditoría de procedencia con la frase «No son estadísticas oficiales; son precios pedidos, no transaccionados» y distingue entre fuentes que sirven de contexto y anuncios que constituyen la señal de precio. §23 hace explícito el supuesto de que los anuncios son comprables sin comprobación de disponibilidad en tiempo real, y §63 rotula su proyección de retención como «inferencia de diseño, no medición». El léxico no excede en esos puntos el tipo de evidencia disponible, y esa disciplina terminológica sostiene la parte más defendible del trabajo.

La cuarta fortaleza reside en la práctica estadística de la corrida vigente y en la decisión de retirar una afirmación. El pipeline declara modelo hedónico log-lineal, factoriales de inflación de varianza, prueba de Kruskal-Wallis, prueba de Welch y detección de anomalías, y el archivo de coeficientes archivado sostiene la conclusión cualitativa: la edad del vehículo aparece con p = 0,1504 y la categoría premium con p = 0,8753, sin que ninguno de los siete coeficientes no intercepto alcance 0,05. La decisión de retirar «−5,43 % anual (p<0,001)» (§34) en lugar de mantenerla con una cautela retórica coincide con el estado de la evidencia y con lo que la literatura reunida en el mapa califica como comportamiento esperable de esas especificaciones. El acierto es metodológico aunque el texto no lo respalde con la cita correspondiente ni separe el efecto de la reparación del campo del efecto del cambio de muestra.

La quinta fortaleza concierne a la infraestructura de integridad de datos. El documento describe un manifiesto que guarda el hash SHA-256 del archivo completo, el orden, el desplazamiento y el hash de cada fragmento, con verificación de los 82 chunks registrada como correcta; la reconstrucción por hash aparece también en la sincronización periódica. La regeneración se documenta en dos puntos con entorno, base de entrada y fecha, y la construcción del sitio se cierra con una compilación estricta sin errores ni enlaces rotos. En el repositorio esa descripción encuentra correlato material: los dos SQLite de Revolico están bajo LFS con 157 objetos referenciados, los doce anuarios llevan URL, tamaño y SHA-256 por archivo, y la serie británica de licencias se cita con organismo, fecha de actualización y licencia abierta.

La sexta fortaleza es la trazabilidad del descubrimiento documental. §7 regula tres búsquedas con regla de parada, paginación y conteo de aciertos y fallos por tanda: 159 páginas recorridas, 1.542 resultados devueltos y manifiesto e índice producidos. §17 convierte ese corpus en una tabla de doce filas donde cada fuente queda vinculada a un aporte metodológico y a un requerimiento concreto, y los siete requerimientos derivados alimentan los nueve bloques del marco analítico de §20. La procedencia de cada decisión de diseño se conserva dentro del documento incluso cuando la fuente es un informe institucional o un repositorio de código y no una obra académica.

La séptima fortaleza concierne al estilo y se confirma en esta pasada. El paralelismo español-inglés cubre las secciones iniciales y 54 de las 55 secciones fechadas; la comparación línea por línea de las dos iteraciones muestra siete reescrituras puntuales y ningún cambio en los rasgos dominantes. La densidad global de metaconceptos pasa de 6,89 a 7,04 por mil palabras y la de adjetivos valorativos sin ancla de 0,14 a 0,24, incrementos localizados íntegramente en las dos secciones nuevas. El hedging permanece en una sola instancia y los openers de fórmula y la construcción «not just X, but Y» en cero. Las reescrituras editadas añaden anclaje concreto —la TRMI fija de 930 CUP/USD en `config.py` (§23), las 28 observaciones de 981 candidatas (§59)— en lugar de atenuadores.

La octava fortaleza es la elección del ancla teórica y su verificación. Akerlof (1970) sostiene el marco en la tabla de aportes de §17, en el paso tercero de §19 y en el bloque correspondiente de §20, y la clasificación de calidad por antigüedad y palabras de defecto opera como su concreción empírica. La re-verificación confirma todos los campos bibliográficos de la obra por OpenAlex —DOI, autor con identificador, revista, volumen 84(3) y páginas 488–500— y sitúa la cuestión de la calidad como información privada del vendedor en el centro del problema que los anuncios recolectados plantean. La elección resulta bien calibrada para una audiencia de maestría.

## 3. Defectos a corregir antes de imprimir

El primer grupo afecta al aparato inicial y a la arquitectura del texto. El encabezado conserva seis campos en negrita y la firma consigna un rol, no un nombre; no hay resumen estructurado, enumeración de contribuciones ni hipótesis central formulada como proposición falsable. Las dos secciones nuevas, aunque aportan declaración procedimental y aparato bibliográfico, no sustituyen esas tres piezas: §34 presenta un coeficiente de depreciación sin que el lector pueda identificar la proposición sometida a contraste, y §59 lo retira sin que exista un enunciado previo que haya quedado refutado. La numeración se reinicia en dos secciones «1.» y dos apartados de conclusiones antes de continuar hasta §70; el registro automático de §13 ocupa 475 líneas con encabezado de nivel 1 mientras las secciones restantes usan nivel 2, y declara 175 entradas omitidas. Los títulos de edición de §45–§47 —«Reescritura de la sección 3», «Apertura de la sección 3», «Reescritura de la sección 4 del storytelling»— permanecen junto a los títulos descriptivos de §69–§70. Este grupo requiere corrección antes de imprimir: una página de resumen, una lista breve de contribuciones y una hipótesis con términos observables.

El segundo grupo concierne a las referencias cruzadas y a la coherencia bilingüe. No aparecen marcadores de remisión pendientes ni comandos sin resolver, y las tablas y figuras se localizan por encabezado, sección o ruta porque carecen de numeración; se trata de una observación descriptiva sobre la presentación. La incidencia de fondo es otra: la fila octava de la tabla inglesa reintroduce un nombre de fase ya retirado en §21, la quinta conclusión niega en inglés lo que afirma en español, y el párrafo inglés de §59 reproduce el estado previo de la corrida en lugar del vigente. A ello se añaden cuatro marcadores de plantilla insertados en la prosa de §59 y un «apéndice visual con cinco cuadros y seis gráficos reales» descrito pero no incorporado a la copia cacheada. La puesta en concordancia de las dos partes pertenece al mismo bloque que la tabla de versiones.

El tercer grupo reúne las inconsistencias formales y de cifras. En §59 coinciden con el archivo de indicadores 691 anuncios de importación, la mediana de 21.000 USD y las 50 marcas; difieren 772 frente a 952 autos, 2.029 frente a 2.156 anuncios, 1.338 frente a 1.465 locales, 43.000 frente a 33.256 km, 101 frente a 113 grupos y 81 frente a 89 anomalías. El R² de 0,277 no es el redondeo de 0,2744 y coincide con el estado retirado de 22 observaciones de 897 candidatas que todavía describen tres documentos derivados. La tasa de cambio informal aparece como 920 CUP/USD en un pasaje de §23 y como 930 en su aclaración vigente y en §52, sin que el espejo inglés registre el cambio. El número de gasolineras pasa de 137 en §41 a 131 en §42 sin nota de depuración; el corpus del ONEI se cuenta como 117 enlaces, 118 documentos, 221 archivos y 233 archivos según la sección; y §16 describe 119 enlaces en siete lotes de 25 cuando el máximo de lotes completos es cuatro. El mismo modelo se describe, por tanto, en tres estados sin marca de corrida: 28 observaciones de 981 candidatas en el relato vigente, 584 de 981 en el archivo de muestra y 22 de 897 en la documentación derivada. Estas divergencias requieren una tabla de versión única con fecha, corrida, ruta de archivo y sección de origen para cada cifra cargada.

El cuarto grupo afecta al aparato de citas y a la integridad bibliográfica. La lista numerada existe y las 38 fichas siguen una plantilla uniforme con autores, título, revista, año, identificador y campo de citación; el cuerpo, sin embargo, no contiene ninguna marca numérica entre corchetes en sus 1.484 líneas, y las dieciocho entradas de 2022–2026 conservan la indicación de no citadas. Seis fichas comparten la etiqueta genérica de metadatos incompletos para cinco causas distintas: dos resúmenes no sustantivos o no indexados, tres conteos de citas ya recuperados por otra vía y un marcador aparecido en esta iteración sin motivo declarado, con una discrepancia de año entre 2015 y 2016 no consignada. La obra que sostiene el marco teórico se presenta en §70 como verificada externamente y en su ficha como incompleta, sin que la ficha nombre el campo afectado; la parte Crossref de esa afirmación no pudo contrastarse en esta pasada. Tres fuentes institucionales se verificaron a nivel de organismo, pero una pertenece a la asociación ecuatoriana y la vecindad de la española en la misma frase puede inducir otra lectura, y la serie británica carece de enlace profundo confirmado. El cuerpo del informe no gana nada argumentativo con la lista mientras no inserte las remisiones.

El quinto grupo reúne lagunas metodológicas y patrones de escritura. La comparación que sostiene el cambio de conclusión enfrenta dos ejecuciones sobre estados de datos distintos sin prueba pareada ni intervalo de la diferencia; el único contraste entre configuraciones disponible confunde el componente con la selección muestral, y el «benchmark» declarado enumera 21 grupos y 30 infravalorados sin comparar el modelo con otro enfoque. Las atribuciones causales sobre el ritmo de captura y la regla de diez páginas se apoyan en reglas y conteos, no en condiciones comparadas. En prosa, la declaración nueva concentra dos series de cola creciente, tres adjetivos sin ancla numérica y unos doce metaconceptos en unas 200 palabras, mientras los bloques §17–§21 y §59–§63 mantienen su densidad alta de la iteración primera. Las 51 líneas que se abren con «Se + verbo», los bloques ingleses de participio inicial y las reescrituras descritas sin mostrarse pertenecen a la pasada de revisión de prosa; ninguno invalida una afirmación.

## 4. Código y reproducibilidad

El repositorio responde hoy a la pregunta de cómo ejecutar el análisis y de dónde proceden los datos, pero no responde de forma operativa a la pregunta de qué versión produjo cada cifra ni qué prueba sostiene el componente central. El README de 105 líneas abre con el nombre del proyecto, contiene una sección de inicio rápido con tres comandos encadenados y las tres salidas esperadas, asocia cada archivo de configuración con lo que controla y enlaza informe, guías y datos por tipo. Diez puntos de entrada están inventariados con sus líneas de código; el orquestador fija la secuencia de cinco etapas y continúa con la actualización de marcadores, la generación del panel solo si hay cambios y la exportación compacta. Los argumentos constan para la verificación y el ensamblado de fragmentos y para la construcción del sitio; el componente central carece de docstring de uso y de banderas propias, punto débil de alcance acotado frente al requisito de documentar argumentos.

Las mejoras pedidas tras la primera pasada están materialmente presentes en el árbol de trabajo. El archivo de dependencias sustituyó las cotas inferiores por operadores compatibles en doce paquetes y su segunda línea afirma que están fijadas a versiones menores; en la semántica de versiones aplicable, esa notación fija la serie mayor y no el número menor, por lo que la afirmación no es exacta. Las restricciones excluyen además versiones declaradas en el propio informe: la cota de tenacity excluye la 9.2.1 de §6 y la de pyarrow excluye la 26 de §34. No hay archivo de proyecto, bloqueo de dependencias ni imagen de contenedor, y la versión de Python solo aparece como «3.10+». El orquestador define una semilla numérica y llama a los generadores aleatorios, con un docstring que afirma que la semilla se declara «aqui y en el informe»; la cifra no aparece en la copia cacheada, donde las únicas «semillas» son ocho URLs de partida. Los cinco pasos se lanzan en intérpretes nuevos que no heredan el estado de los generadores del padre, de modo que la semilla no alcanza a las etapas; los pasos son deterministas por agregación y regresión por mínimos cuadrados, no por fijación de semilla.

La prueba de humo del componente central existe y pasa sus cuatro comprobaciones: compila los siete scripts, verifica siete salidas, lee cuatro archivos de datos y comprueba que el README cite el orquestador y que el código contenga la semilla. El inventario de artefactos la omite porque se cerró a las 17:15, antes de que el archivo apareciera. La prueba verifica presencia y compilación, no la reproducción numérica de los indicadores ni la ejecución completa del pipeline. Las tres pruebas inventariadas cubren el panel, la exportación compacta y la coherencia interna del archivo de muestra; `test_modelo.py` comprueba el esquema y la idempotencia de la estimación, pero no que los coeficientes concuerden con la narrativa de §59. La pregunta que un tribunal formularía —qué prueba sostiene la deduplicación de 814 filas a 744 autos y la retirada del coeficiente de edad— no tiene respuesta operativa hoy; cerrarla con una comparación de los marcadores contra los archivos de salida insume entre seis y nueve horas.

Un desajuste de estado limita todo lo anterior: las cotas, la semilla, la prueba de humo y tres documentos derivados figuran como modificados o no rastreados frente al commit declarado, que sigue siendo el último de la rama con fecha 27/11/2026. La declaración de §69 afirma que las cifras y las decisiones de diseño provienen de datos y código versionados, y esa afirmación describe un estado posterior al commit. Un clon limpio no encuentra ninguna de las mejoras. La etiqueta de versión y la incorporación de los cambios al historial constituyen el bloque de bajo coste y mayor efecto sobre la reproducibilidad.

La correspondencia documento-repositorio presenta tres desincronizaciones. El archivo de muestra contiene dos filas —una con 584 observaciones, R² 0,101 y probabilidad del estadístico F de 0,0, otra con 28 observaciones, R² 0,2744 y p 0,4114— y la narrativa elige la segunda con un R² que no coincide. Los indicadores regenerados y el README convergen en 952 autos y 2.156 anuncios, pero la caché auditada conserva los valores anteriores y el espejo inglés, otro estado más. El panel autocontenido de 109.929 bytes existe, está versionado y se regenera desde el orquestador; el informe cita en cambio los paneles descriptivos antiguos de `Data/analisis/` y describe en §59 un apéndice visual sin declarar la ruta vigente, que aparece solo en la documentación de automatización. La lista numerada de referencias, por su parte, no porta una marca positiva de verificación para las cuatro fuentes que §70 declara como tales: la distinción vive en el artefacto literario de la auditoría, de modo que el estado afirmado no es autónomo dentro del archivo citado.

La disponibilidad de datos presenta un perfil mixto y desigual. La base de Revolico no se versiona como archivo único, pero los manifiestos publican hash de origen, offsets y hashes por fragmento, y la reconstrucción está documentada y probada. Los doce anuarios, la serie británica y la geolocalización de gasolineras cumplen el rasero de ruta, licencia y checksum. Frente a esos casos correctos, las series oficiales de parque automotor y matriculaciones no existen entre los anuarios descargados, la fuente india y el endpoint del banco central no son accesibles desde este entorno, el índice y los archivos de gacetas residen fuera del árbol, y los repositorios citados como insumo metodológico quedan excluidos de Git aunque el texto los use como antecedente. La cobertura de campos derivados por expresiones regulares y la ausencia de precios transados condicionan la réplica de las estimaciones desde los datos publicados. La conclusión es la misma que en la pasada anterior con un matiz: hoy hay una prueba de humo y un comando único, pero la versión que produjo cada cifra sigue sin declararse en un lugar.

## 5. Posicionamiento en el campo: novedad y estado del arte

La evaluación de novedad cuenta ahora con una señal explícita donde la pasada anterior no tenía ninguna. El inventario registra una afirmación etiquetada como tal: la creación del esqueleto de rentabilidad «siguiendo la arquitectura del repositorio Egyptian-Used-Cars» (§34), adaptada a las fuentes cubanas. El enunciado usa verbos de adopción y el encabezado rotula el trabajo como inspirado en ese repositorio; el objetivo vigente excluye la novedad de producto al diferir el recomendador. No aparece una reclamación de primacía, de método nuevo ni de contribución original, y la única comparación disponible —«Brecha frente a Egipto» (§34)— se enuncia en dirección desfavorable al propio proyecto: 23.500 anuncios frente a 497 usados, una sola instantánea y campos mayormente ausentes. No hay sobreclaim que corregir, y el alcance local está declarado como tal.

Lo que sigue sin resolverse es la diferenciación frente a los vecinos académicos. El trabajo egipcio es una fuente de ingeniería ajena al mapa literario, y la comparación opone escalas de datos, no métodos. Los tres referentes más cercanos al enunciado de novedad están en el mapa completo y figuran en la lista numerada sin citas en el cuerpo: el estudio de Gegić y colaboradores de 2019, que documenta la combinación de captura y modelado de precios; el trabajo de Muça y colaboradores de 2026 sobre una canalización de datos públicos con web scraping y aprendizaje automático; y el análisis de Du y colaboradores de 2026 sobre depreciación no lineal y heterogeneidad de marca en anuncios, con especificación hedónica log-lineal anidada casi idéntica a la del informe. El estudio regional de Vidal Alejandro y colaboradores de 2024, sobre el uso de la tasa informal cubana, completa el grupo y tampoco aparece citado. La forma del criterio de diferenciación se cumple solo respecto de una fuente externa al mapa; no hay párrafo comparativo con el trabajo académico más cercano.

La novedad local que está infravalorada en la redacción es de integración y de contexto, no de formulación de problema. La decisión de mantener una base SQLite por tienda con adaptadores por dominio, renderizado opcional, escrituras por lotes de 25 anuncios, deduplicación por título normalizado, prefijo y dominio, separación de monedas y columnas de auditoría constituye una contribución de ingeniería sobre la que el mapa no registra equivalente directo. La conversión anclada al día del anuncio y la distinción entre tasa informal y oficial tienen como precedente regional el estudio cubano ausente. La arquitectura de colas desacopladas, idempotencia por clave de fuente, cuarentena de datos inválidos y manifiestos con hashes se emparenta con los marcos de calidad y procedencia de Priestley y Hohensinner, también ausentes. El mapa sin conexión con contorno embebido y la extracción de 2.473 puntos, 244 circuitos y 166 polígonos del paquete de circuitos se distinguen por propósito de la hoja de ruta energética nacional. Tres párrafos de comparación —procedencia de datos, conversión por tasa informal y cautela hedónica— convertirían diferenciadores implícitos en contribuciones defendibles.

La cobertura del estado del arte es el flanco más cuantificable y no mejora con la numeración. De 38 trabajos, uno solo se nombra por su autor en el cuerpo: el clásico fundacional, en tabla, marcos y lista. La distribución por clúster es de uno de ocho en asimetría de información y de cero de doce, cero de ocho, cero de siete y cero de tres en los restantes. La proporción global es del 2,6 % frente al rango esperable de 25 a 60 trabajos en este nivel. Dieciocho referencias de 2022–2026 superan el umbral de actualidad del 40 % si se mide la bibliografía numerada, pero ninguna aparece citada: la proporción de obras recientes en el argumento es de cero sobre uno. De los 23 trabajos que encabezan sus clústeres por número de citas, 22 están ausentes, y la lista de ocho obras probablemente decisivas se reafirma sin cambios. Entre ellas figuran el estudio de Lewis de 2011 sobre divulgación y selección adversa, el de Gegić, el de Priestley y el de Guerra sobre la métrica de precio respecto al salario.

La relación entre esas ausencias y las afirmaciones portantes es directa. Lewis corresponde a la captura de defectos y tipo de vendedor de §19; Englmaier advierte sobre saltos en umbrales de año y cada 10.000 km frente a las series de §34; Gegić es el paralelo metodológico del pipeline; los trabajos sobre ética de captura corresponden a la regla operativa de §10; Guerra corresponde a la asequibilidad de §19; y el estudio sobre procedencia corresponde a los manifiestos de §54. El esfuerzo de descubrimiento de §7 y la tabla de doce fuentes de §17 no se transfirieron a las secciones analíticas. No hay tabla comparativa que enfrente la aproximación propia con los trabajos más cercanos, y la línea de investigación regional se menciona como contexto sin entrar en el debate metodológico.

La retirada de la depreciación ilustra la distancia entre coincidencia y citación. Cuatro obras del mapa apuntan en el mismo sentido que la conclusión vigente de §59–§60: el trabajo de Du, el de Miranda sobre precios de anuncios con R² de 0,256 y kilometraje con p = 0,077, el de Englmaier sobre discontinuidades y el de Francke y Van de Minne sobre heterogeneidad no observada. Las cuatro figuran como no citadas. La coincidencia es de resultado, no de atribución: sin esas remisiones, un lector no puede distinguir entre una decisión informada y una convergencia fortuita. La iteración segunda fue una re-verificación de metadatos —22 consultas dirigidas, seis registros de primer nivel, seis de segundo y ninguno de texto completo— sin búsquedas temáticas nuevas y con proveedor de búsqueda web fallido. Una conclusión de novedad confirmada excedería esa evidencia; la lectura permitida es que no se añadió antecedente nuevo en esta pasada, no que no exista arte previo.

## 6. Integridad bibliográfica y declaración de IA

La integridad bibliográfica y la declaración de uso de inteligencia artificial forman un bloque contiguo por localización y por forma. Las dos secciones nuevas se sitúan después del cierre anterior de §68 y convierten procedimientos realizados durante la auditoría en enunciados del propio informe: §69 describe la auditoría sin incluir ninguno de sus hallazgos, y §70 enumera fuentes sin vincularlas a los resultados de §59–§60. La convergencia es de localización y de forma declarativa; el expediente no atribuye autoría ni intención, y la evaluación de escritura dejó constancia de que no recibió la tabla de densidad que la evaluación de ética echó en falta, tabla que sí consta en el ensamble revisado.

El aparato numerado resiste el cotejo formal. Las 38 entradas siguen una plantilla única, incluyen autores nominales, no duplican una misma obra con identidades distintas y no contienen identificadores espurios: los DOI declarados ajustan su patrón y los cuatro identificadores de prepublicación tienen prefijo de fecha compatible con un documento de noviembre de 2026. Dos artefactos tipográficos son sistemáticos y no afectan a la atribución. La verificación en vivo confirmó tres conteos de citas que la pasada anterior no pudo consultar por una restricción de acceso —13, 96 y 9— junto con los DOI de las versiones publicadas de dos de esas obras. Ninguno de esos datos figura en las fichas, que conservan la etiqueta genérica sin nombrar el campo. Un marcador por campo permitiría confiar o descontar cada entrada; la etiqueta actual impide distinguir entre un resumen ausente, un dato ya recuperado y un marcador nuevo sin justificación.

La contradicción de estado en la obra fundacional no es de existencia sino de etiqueta. Los campos bibliográficos se confirman en el registro consultado, pero el campo de resumen contiene solo el índice de secciones de la revista, que era el motivo original del marcador; la otra mitad de la afirmación de verificación externa no pudo contrastarse por un error de transporte. Las dos afirmaciones solo se reconcilian si se entiende que la etiqueta alude al resumen y no a la identidad, y la ficha no lo dice. En las otras dos fichas con motivo sustantivo, el resumen sigue sin indexarse y el resto de campos se confirma campo por campo. La nueva marca aparece sin motivo declarado en ninguno de los dos artefactos y añade una discrepancia de año entre la versión electrónica y la impresa no consignada en la ficha.

Las tres fuentes institucionales se verificaron a nivel de organismo y de serie, con tres límites de precisión. La asociación española expone matriculaciones y cifras de 2025; la asociación ecuatoriana publica ventas de enero a septiembre de 2026 y no declara su país en la lista, donde la vecindad de la española puede inducir una atribución distinta; la agencia británica mantiene 48 millones de registros y la serie de estadísticas de licencias con fecha de actualización, aunque tres intentos de enlace directo devolvieron error y la búsqueda de apoyo falló a nivel de proveedor. Ninguna de las tres tiene ficha numerada, de modo que el cómputo de cuatro fuentes verificadas mezcla dos regímenes de cita: una entrada bibliográfica y tres menciones nominales.

La declaración de inteligencia artificial cierra la ausencia que la pasada anterior registró en las secciones iniciales. Nombra cuatro actividades —redacción, edición, revisión bibliográfica y auditoría— y enuncia un protocolo de contraste: «ninguna afirmación empírica se originó en una salida de IA sin contraste contra los archivos» (§69), con procedencia declarada y huella conservada en el directorio de auditorías. El rasero de maestría pide además nombrar herramientas, enumerar fases de investigación, redacción, generación de código y traducción, y designar un protocolo de supervisión. La declaración nombra solo el procedimiento de auditoría; las herramientas generativas quedan en el genérico, la generación de los seis scripts propios no se atribuye ni se excluye, la traducción del documento bilingüe no se menciona, y la supervisión aparece como principio sin pasos designados. La huella citada apunta a los artefactos de la iteración primera, no a los de esta. La densidad media de la sección procede de dispositivos de superficie —series de cola larga, tres adjetivos sin ancla y metaconceptos— y no de atenuadores ni de openers de fórmula.

## 7. Calibración de esfuerzo y riesgos para la defensa o el sometimiento

El esfuerzo se distribuye en cuatro bloques desiguales. La coherencia documental —tabla de versiones de cifras, concordancia de las dos partes, etiqueta de corrida vigente y separación de las dos especificaciones del modelo— insume entre diez y catorce horas. La reproducibilidad —incorporación de las mejoras al commit, fijación real de dependencias, propagación o retirada de la semilla declarada, prueba de los marcadores contra los archivos de salida y declaración de la ruta del panel— insume entre seis y nueve horas. La cobertura bibliográfica —párrafos de contraste con los tres vecinos más cercanos, inclusión de las obras recientes del mapa y tabla comparativa— insume entre nueve y doce horas. El aparato de fuentes y la declaración —fichas que nombren el campo incompleto, marcas positivas de verificación, remisiones numéricas en el cuerpo y nombrado de herramientas y fases— insume entre cinco y siete horas. El total se sitúa entre treinta y cuarenta y dos horas, unas cuatro o cinco jornadas concentradas, sin nueva recolección de datos.

Tres preguntas concentran el riesgo. La primera —qué corrida produce cada cifra y por qué el espejo inglés conserva 744 autos y 2.014 anuncios— se neutraliza con una tabla de una página que asocie cada número cargado a su fecha, su corrida, su ruta de archivo y su sección de origen, y con la regeneración de la copia cacheada. La segunda —sobre cuántas observaciones se ajusta el modelo y por qué se retiró la pendiente del −5,43 % anual— se neutraliza declarando las dos especificaciones archivadas, 584 y 28 observaciones sobre 981 candidatas, con R² 0,2744 y probabilidad del estadístico F de 0,411 para la vigente, y situando la retirada dentro de una comparación de especificaciones con el contraste pareado ausente. La tercera —qué trabajo previo hace distinta la contribución— se neutraliza con los tres párrafos de comparación señalados y con remisiones nominales completas en el cuerpo, no solo en la lista.

La prioridad sigue el orden de dependencia. Las cifras se corrigen primero porque afectan a todas las secciones analíticas y al README; la etiqueta de vigencia y la concordancia inglesa van en el mismo bloque. El código se corrige después, porque el estado no versionado y la ausencia de comparación de marcadores explican por qué las cifras divergen. La literatura y la bibliografía se cierran al final, sobre un texto ya estabilizado, de modo que los párrafos de contraste se escriban contra una versión fija del modelo. La secuencia invierte el orden en que el documento se escribió y reduce el número de pasadas posteriores.

## Anexo — Artefactos de la auditoría

### Iteración anterior, heredada como contexto

**informe-tecnico-2026-11-27.plan.md** — Plan de la primera pasada con alcance completo y mejoras; fijó nivel, documento, repositorio y reparto de fases.

**informe-tecnico-2026-11-27.e1-claims.md** — Inventario de afirmaciones con reformulación y evidencia; registró catorce afirmaciones portantes y cero señales de novedad.

**informe-tecnico-2026-11-27.e2-literature.md** — Mapa de 38 trabajos en cinco clústeres con metadatos verificados en vivo y lista de obras probablemente ausentes; sigue siendo el mapa vigente.

**informe-tecnico-2026-11-27.e3-artifacts.md** — Inventario de conjuntos de datos, tablas, figuras y artefactos ausentes, producido sin clon local.

**informe-tecnico-2026-11-27.v1-structure.md** — Evaluación de la macroestructura bilingüe, la numeración duplicada y la ausencia de resumen, contribuciones e hipótesis.

**informe-tecnico-2026-11-27.v2-methodology.md** — Evaluación de tamaños muestrales, pruebas, amenazas a la validez, líneas base, ablaciones y protocolo de reproducibilidad.

**informe-tecnico-2026-11-27.v3-results-evidence.md** — Cotejo de las afirmaciones numéricas contra los archivos de salida del pipeline de rentabilidad.

**informe-tecnico-2026-11-27.v4-novelty.md** — Derivación de candidatos de originalidad a partir de un texto sin etiquetas y cotejo con los trabajos más cercanos.

**informe-tecnico-2026-11-27.v5-state-of-the-art.md** — Medición de cobertura, actualidad y peso de la citación, con delimitación de los fallos de búsqueda.

**informe-tecnico-2026-11-27.v6-reproducibilidad.md** — Inspección del checkout: documentación, dependencias, orquestador, pruebas y desajustes entre código y documento.

**informe-tecnico-2026-11-27.v7-writing.md** — Conteo de patrones de prosa y densidad de metaconceptos por sección.

**informe-tecnico-2026-11-27.v8-bibliography.md** — Auditoría de las fuentes nominales y registro de metadatos incompletos sin invención de identificadores.

**informe-tecnico-2026-11-27.v9-ethics.md** — Evaluación de la regla de recolección, consentimiento, anonimato y declaraciones de disponibilidad.

**informe-tecnico-2026-11-27.forensic.md** — Ensamble estructurado de la primera pasada; origina las ocho observaciones transversales comprobadas aquí.

**informe-tecnico-2026-11-27.md** — Informe narrativo de la primera pasada; su priorización y sus estimaciones de esfuerzo se reescriben en la sección 7.

### Plan de la iteración 2

**informe-tecnico-2026-11-27-iter2.plan.md** — Plan aprobado que declara nivel de maestría, preset estándar, re-ejecución de extracciones y evaluaciones, y comprobación de las ocho observaciones heredadas.

### Fase 1 — inventarios de la iteración 2

**informe-tecnico-2026-11-27-iter2.e1-claims.md** — Inventario de 120 afirmaciones, trece portantes, con una señal de novedad y nueve afirmaciones portantes sin citas numeradas.

**informe-tecnico-2026-11-27-iter2.e2-literature.md** — Re-verificación dirigida de seis entradas marcadas y tres fuentes institucionales; 22 consultas, sin búsquedas temáticas ni lectura de texto completo.

**informe-tecnico-2026-11-27-iter2.e3-artifacts.md** — Inventario en disco con 190 commits, puntos de entrada, pruebas, datasets, artefactos nuevos y ausentes; cerrado antes de inventariar la prueba de humo.

### Fase 2 — evaluaciones de la iteración 2

**informe-tecnico-2026-11-27-iter2.v1-structure.md** — Evaluación de la macroestructura: objetivo ya alineado, divergencia residual de la fase 8, numeración duplicada y secciones nuevas.

**informe-tecnico-2026-11-27-iter2.v2-methodology.md** — Evaluación de ablaciones, pruebas pareadas, semillas, tamaños muestrales, límites y tres estados incompatibles del modelo.

**informe-tecnico-2026-11-27-iter2.v3-results-evidence.md** — Cotejo de las cifras de §59–§60 contra los CSV vigentes; detecta seis de nueve indicadores desincronizados y tres estados de la corrida.

**informe-tecnico-2026-11-27-iter2.v4-novelty.md** — Evaluación de la única señal de novedad, del único párrafo comparativo y de la ausencia de contraste con los vecinos académicos.

**informe-tecnico-2026-11-27-iter2.v5-state-of-the-art.md** — Medición de cobertura, actualidad y peso de la citación tras la numeración; una entrada citada de 38 y ninguna obra reciente en el cuerpo.

**informe-tecnico-2026-11-27-iter2.v6-reproducibilidad.md** — Inspección de dependencias, semilla, comando único, prueba de humo, estado de Git y correspondencia entre cifras, panel y documento.

**informe-tecnico-2026-11-27-iter2.v7-writing.md** — Diff de 520 palabras, conteo de patrones, densidad por sección y tabla de densidad de patrones de asistencia.

**informe-tecnico-2026-11-27-iter2.v8-bibliography.md** — Auditoría de las 38 fichas numeradas, verificación de conteos y DOI, y registro de los seis marcadores por causa.

**informe-tecnico-2026-11-27-iter2.v9-ethics.md** — Evaluación de la declaración de inteligencia artificial, las fases nombradas y las fases ausentes de generación de código y traducción.

### Síntesis forense de la iteración 2

**informe-tecnico-2026-11-27-iter2.forensic.md** — Ensamble de los once artefactos de fase con resumen, hallazgos por dimensión, observaciones transversales y apéndices de afirmaciones, literatura y artefactos; soporte de cada enunciado de este informe.

### Documento auditado

**INFORME_TECNICO.md** — Informe técnico bilingüe de 1.484 líneas, fechado el 23/11/2026 y actualizado el 27/11/2026; su copia cacheada sirvió de base para las citas literales.

### Repositorio

**CarlosAntonioAceaJimenezCD/el-precio-de-moverse-en-cuba** — Repositorio declarado en el documento e inspeccionado en checkout local: 190 commits, 41.689 líneas de Python propio, datos bajo LFS, panel autocontenido y archivos de salida del modelo.

### Informe narrativo de la iteración 2

**informe-tecnico-2026-11-27-iter2.md** — El presente informe; reorganiza los hallazgos del ensamble en secciones editoriales para el autor del documento.

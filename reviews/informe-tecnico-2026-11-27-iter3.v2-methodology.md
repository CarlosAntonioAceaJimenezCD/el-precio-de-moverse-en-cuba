---
type: audit-artifact
phase: v2-methodology
slug: informe-tecnico-2026-11-27-iter3
generated_at: 2026-11-28T00:00:00-05:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/informe-tecnico-2026-11-27-iter3/informe-tecnico-2026-11-27-iter3.text.md
language: es
level: master
---

# V2 — Methodology (findings)

### F-V2-001 — Las bases de comparación no incluyen un enfoque adyacente al estado del arte operacionalizado

La nueva §71.1 (L1489–1495) enumera tres filas: la mediana global ingenua (MAE 18.220,46 USD sobre 1.444 anuncios), `Egyptian-Used-Cars` como «referencia de ingeniería del campo» con «contraste cualitativo de cobertura y frescura», y el «Modelo principal propio» (R² 0,101 sobre 584 observaciones). El criterio `V2.baselines` para `level=master` se lee: «≥2 baselines, one of which corresponds to a SOTA-adjacent approach in the field». La primera fila es un baseline trivial; la segunda es un contraste cualitativo de cobertura sin métrica calculada sobre los datos propios; la tercera es el modelo propuesto, no una base externa. Los trabajos más cercanos citados en §71.6 (Gegić et al. 2019, Muça et al. 2026, Du et al. 2026) se usan para posicionamiento argumentativo, no se operacionalizan como bases con métrica comparable. La sección declara tres filas, pero no dos bases en el sentido del criterio.

— polarity: negative · confidence: high · related: [[#C014]], [[#C011]], [[#C012]], [[#C016]] · criteria: V2.baselines.master

### F-V2-002 — Ablación explícita del término `hp`, con especificación y muestra informadas conjuntamente

La §71.2 (L1499) declara la ablación del término `hp` apoyada en `modelo_muestra.csv`: al retirarlo, la muestra pasa de 28 a 584 observaciones de 981 candidatas y el R² de 0,274 a 0,101, e informa explícitamente que «el cambio de especificación y el cambio de muestra se informan juntos». El criterio `V2.ablations` para `level=master` se lee: «Explicit ablation of at least one component». La ablación existe, está etiquetada como tal y cuantifica el efecto, por lo que supera el estándar de nivel. Como matiz observacional, la retirada del componente y el cambio de tamaño muestral están confundidos en el mismo contraste, de modo que el texto no aísla la contribución del término de la contribución de la selección de anuncios con kilometraje declarado; el propio párrafo atribuye a esa selección el signo positivo de antigüedad.

— polarity: positive · confidence: high · related: [[#C015]], [[#C004]], [[#C005]] · criteria: V2.ablations.master

### F-V2-003 — Tests declarados para grupos independientes, sin test del contraste central

La §71.3 (L1505) afirma que no hay diseño pareado y que se usan Kruskal-Wallis y Welch para grupos independientes; la §60 (L1389) reporta p mínimo 0,165, VIF 1,13–1,58 y Kruskal-Wallis p = 1e−05. El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)». Dado que el documento declara observaciones independientes, los tests pareados no son aplicables y la elección de tests de grupos independientes es coherente con el criterio. Sin embargo, los dos contrastes comparativos centrales —la caída de R² de 0,274 a 0,101 en la ablación de §71.2 y el paso de −5,43 % anual con p<0,001 en §34 (L1056) a la no significancia actual de §59— se presentan sin test de diferencia ni intervalo de confianza que acompañe la comparación. El criterio de nivel master se satisface en la forma (tests declarados y elegidos según el diseño), pero queda sin cuantificar la incertidumbre de esos dos contrastes.

— polarity: neutral · confidence: medium · related: [[#C004]], [[#C006]], [[#C015]], [[#C060]] · criteria: V2.statistical_tests.master

### F-V2-004 — Tamaño expresado en anuncios, con una especificación completa de 28 observaciones y ocho marketplaces

La §71.3 (L1505) fija el tamaño en 981 candidatas de 8 marketplaces; la §71.1 (L1493) reporta 584 observaciones para el modelo principal y la §59 (L1381) reporta 28 observaciones completas de 981 candidatas para el modelo con todos los términos. El criterio `V2.sample_size` para `level=master` se lee: «≥20 trials; ≥10 datasets/instances». La unidad declarada son anuncios observacionales, no ensayos: el modelo principal (584) supera holgadamente el umbral numérico de 20, pero el modelo completo se apoya en 28 observaciones y ningún coeficiente alcanza p < 0,05 (§71.4, L1512), y el número de fuentes/instancias declaradas es 8, por debajo de 10. La propia §71.4 registra la limitación, de modo que la desviación está documentada aunque no corregida. No hay análisis de potencia; el criterio de nivel master no lo exige.

— polarity: neutral · confidence: high · related: [[#C005]], [[#C060]], [[#C061]] · criteria: V2.sample_size.master

### F-V2-005 — Subsección dedicada que cubre los cuatro tipos de amenaza a la validez

La §71.4 (L1509–1512) dedica una subsección explícita a amenazas externa (solo La Habana, precios pedidos), de constructo (kilometraje y potencia ausentes en la mayoría de los anuncios, condición inferida del texto), interna (sin asignación aleatoria, ablación observacional) y estadística conclusiva (28 observaciones, ningún coeficiente con p < 0,05, signo de antigüedad reflejo de selección). El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations». El documento no solo cumple sino que enumera las cuatro categorías que el nivel doctoral exige como sección dedicada, aunque sin mitigaciones explícitas ni declaración de replicabilidad, que son requisitos de nivel `paper`. La subsección además reformula límites ya presentes en §18 y §19, lo que refuerza la coherencia interna del apartado.

— polarity: positive · confidence: high · related: [[#C061]], [[#C013]], [[#C007]] · criteria: V2.threats_to_validity.master

### F-V2-006 — Protocolo de reproducción con semilla, comando único, dependencias fijadas y prueba de humo

La §71.5 (L1516) declara `SEED = 20261127` en `run_all.py`, el comando único `Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py`, cuatro puntos de entrada con argumentos, dependencias fijadas a serie menor en `requirements.txt` y la prueba de humo `python3 Auxiliares/herramientas/test_smoke_pipeline.py`. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced». Los tres elementos están presentes y se refiere al código versionado; la declaración de dependencias y la prueba de humo exceden el mínimo del nivel. No se declaran versiones de los datasets ni un commit/DOI pinnado, requisitos propios de los niveles `phd` y `paper`, no del nivel evaluado.

— polarity: positive · confidence: high · related: [[#C059]], [[#C008]] · criteria: V2.reproducibility_protocol.master

### F-V2-007 — Coexistencia de dos especificaciones y dos valores de R² sin reconciliación explícita en la sección 71

La §59 (L1381) describe «el modelo con todos los términos» con 28 observaciones, R² 0,277 y p del F 0,411; la §71.1 (L1493) presenta como «Modelo principal propio» un OLS con 584 observaciones y R² 0,101; la §71.2 (L1499) atribuye R² 0,274 a la especificación de 28 observaciones. La sección nueva no identifica explícitamente ambos ajustes como dos especificaciones separadas ni explica la diferencia entre 0,277 y 0,274 para la misma muestra de 28, pese a que ambos valores se presentan como resultados de la corrida vigente del 27/11/2026. Bajo el criterio `V2.reproducibility_protocol` para `level=master` —«Protocol fully described + seeds mentioned + code referenced»—, la coherencia entre declaraciones de distintas secciones forma parte del protocolo descripto; la falta de reconciliación deja ambiguo cuál de los dos modelos es el principal y cuál es el de referencia para la ablación.

— polarity: negative · confidence: medium · related: [[#C003]], [[#C005]], [[#C014]], [[#C015]], [[#F-V2-004]], [[#F-V2-006]] · criteria: V2.reproducibility_protocol.master

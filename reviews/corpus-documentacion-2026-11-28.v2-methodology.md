---
type: audit-artifact
phase: v2-methodology
slug: corpus-documentacion-2026-11-28
generated_at: 2026-11-28T03:53:37-04:00
audited_document: /home/thony70807/Proyectos/El precio de moverse en Cuba/.playground/audit-cache/corpus-documentacion-2026-11-28/corpus-documentacion-2026-11-28.text.md
language: es
level: master
---

# V2 — Methodology (findings)

### F-V2-001 — Protocolo de ejecución y trazabilidad descrito de extremo a extremo

El corpus describe una cadena de ejecución identificable: `README.md` §Quickstart (L.26–40) fija Python 3.10+, `requirements.txt`, el entorno `Auxiliares/.venv-py` y la entrada `Data/analisis_rentabilidad/scripts/run_all.py`, con salidas nominales `listings_clean.parquet`, `kpis.csv` y `kpis_canal.csv`; `config.py` concentra «Rutas, umbrales de precio/año, TRMI, marcas y tiers» (L.79). La trazabilidad se declara en tres capas: `MANIFEST.json` con «recuentos y SHA-256 por archivo» (L.504), `manifiesto_ejecucion.jsonl` con «commit, SHA de scripts, Python, entradas/salidas, filas, métricas de calidad y watermark antes/después» y `VERSIONES.json` con dependencias y hash de configuración (L.687–688). El cierre del bucle está documentado en `actualizar_numeros.py` con modo `--check` y pruebas en `probar_actualizar_numeros.py` (L.663), y la reconstrucción de bases desde chunks en L.84–89. El criterio `V2.reproducibility_protocol` para `level=master` se lee: «Protocol fully described + seeds mentioned + code referenced». La descarga de protocolo y código se satisface; el apartado de semillas se observa en F-V2-002.

— polarity: positive · confidence: high · related: [[#C061]], [[#C062]], [[#C076]], [[#C110]] · criteria: V2.reproducibility_protocol.master

### F-V2-002 — Ninguna semilla aleatoria declarada en los ocho archivos

No aparece `seed`, `semilla`, `random_state` ni equivalente en el corpus unificado (L.1–833). La única noción de aleatorización es `RandomizedDelaySec=5m` en la programación de timers (L.655), que es jitter de scheduling y no una semilla de generador. Las únicas rutinas estocásticas implícitas —OLS, VIF, Kruskal-Wallis, percentiles— son deterministas dada la muestra, y el propio `MODELOS_Y_FUNCIONES.md` §1 califica la preparación como «Preparación determinista (sin inferencia)» con respaldo en «la reproducibilidad y la trazabilidad» (L.401–403). Bajo el criterio `V2.reproducibility_protocol.master` («seeds mentioned»), el elemento de semillas está ausente como declaración explícita, sin que ello altere la determinism de los cómputos descritos.

— polarity: neutral · confidence: high · related: [[#C110]], [[#C111]] · criteria: V2.reproducibility_protocol.master

### F-V2-003 — Ablación explícita del término `hp` entre modelo principal y completo

`MODELOS_Y_FUNCIONES.md` §3.1 (L.452) estima dos especificaciones del mismo modelo hedónico y contrasta los resultados: «el modelo principal (sin `hp`) usa 586 observaciones de 993 candidatas (R² = 0,101; p del F 0,000) y el completo usa 28 (R² = 0,274; p del F = 0,411)». La comparación aísla un componente —la potencia— manteniendo fijas la fórmula base, la muestra de candidatas y el resto de términos, y se apoya en `modelo_muestra.csv`. El pasaje no emplea la etiqueta «ablación», pero la estructura es funcionalmente una ablación de un término declarado. El criterio `V2.ablations` para `level=master` se lee: «Explicit ablation of at least one component»; el corpus lo satisface con un componente explícito. La interpretación del resultado se acota en el propio texto: la asociación positiva de antigüedad en el modelo principal es «un artefacto de selección, no una tasa anual» (L.452).

— polarity: positive · confidence: high · related: [[#C007]], [[#C008]], [[#C043]] · criteria: V2.ablations.master

### F-V2-004 — Cuatro recuentos de muestra incompatibles para el modelo hedónico

La muestra del modelo hedónico se declara con cuatro valores distintos en el corpus. §3.1 (L.450) afirma «28 observaciones completas» y, en la misma oración, «La muestra se reduce a 22 porque `hp` solo está presente en 52 filas y `mileage_km` en 572»; el apéndice Cuadro 5 (L.377) repite «las 22 observaciones de este modelo frente a las 572 del modelo principal»; §3.1 (L.452) da 586 y 28 con respaldo en `modelo_muestra.csv`; y la tabla de depreciación histórica registra 584 de 981 según el contraste externo del inventario de claims. A la vez, la regla de inclusión del propio §3.1 (L.441) exige «más de 30 observaciones por término y más de 30 filas», umbral que el recuento 28 —y con más razón el 22— no alcanza. El criterio `V2.sample_size` para `level=master` se lee: «≥20 trials; ≥10 datasets/instances». El número de fuentes/instancias del corpus (8 marketplaces, 11 concesionarios, 12 anuarios, Revolico, ICD) supera diez, pero la muestra efectiva del modelo completo queda por debajo del umbral que el propio documento declara, y las cuatro cifras no se reconcilian entre secciones.

— polarity: negative · confidence: high · related: [[#C007]], [[#C008]], [[#C040]], [[#C046]] · criteria: V2.sample_size.master

### F-V2-005 — Suficiencia de 104 observaciones semanales en tensión con el límite de serie temporal

`AUTOMATIZACION.md` §2 (L.645) registra «Snapshots de precio (`price_history`) | Semanal, tras Revolico | 104 observaciones en 2 años bastan para depreciación», y §5 (L.690) repite «104 semanas ≈ 2 años». En sentido opuesto, `MODELOS_Y_FUNCIONES.md` §4 (L.485) declara «No se presenta una curva de depreciación temporal: hace falta una serie mensual de 6–12 meses», y el storytelling §8 (L.290) sitúa «Convertir el snapshot semanal en una serie de precios de 6–12 meses» en lo que viene. El encabezado del storytelling (L.123) añade «y una serie oficial detrás», que el propio inventario de modelos niega como curva temporal. La afirmación de suficiencia de la tabla de periodicidades no guarda consistencia con el criterio de serie exigido en el bloque de límites, y ambas afirmaciones conviven sin reconciliación en el mismo corpus. El criterio `V2.sample_size.master` fija «≥20 trials; ≥10 datasets/instances»; el conflicto no es de cantidad sino de la idoneidad declarada de la muestra temporal para la estimación que se dice habilitar.

— polarity: negative · confidence: high · related: [[#C003]], [[#C010]], [[#C038]], [[#C051]], [[#C064]], [[#C108]] · criteria: V2.sample_size.master, V2.threats_to_validity.master

### F-V2-006 — Límites y riesgos distribuidos en subsecciones dedicadas de cuatro archivos

El corpus incorpora varias secciones explícitamente consagradas a límites. `MODELOS_Y_FUNCIONES.md` §4 «Lo que NO se hace (y por eso el análisis es honesto)» (L.480–486) enumera cinco acotaciones: «No se usa la tasa oficial de cambio», «No se imputan precios ni kilómetros faltantes», «No se afirma causalidad: el modelo es de asociación sobre un corte transversal», «No se presenta una curva de depreciación temporal» y «No se mezclan mercados». `ARQUITECTURA_DATOS.md` §5 «Riesgos» (L.556–560) cubre archivos pequeños, watermark desincronizado y overkill; `AUTOMATIZACION.md` §7 «Límites que hay que aceptar» (L.728–730) describe la ventana de ~8 días de Telegram y el envejecimiento de selectores; `README.md` §«Marco legal y límites» (L.110–114) registra cuatro limitaciones operativas; y `ALCANCE_Y_RETENCION.md` L.575 califica el análisis como «diseño, no una medición: el proyecto no tiene analytics». El criterio `V2.threats_to_validity` para `level=master` se lee: «Brief dedicated subsection on threats / limitations»; el corpus excede esa línea base en cantidad de subsecciones, aunque la consistencia entre ellas se evalúa en F-V2-005 y F-V2-009.

— polarity: positive · confidence: high · related: [[#C009]], [[#C021]], [[#C051]], [[#C084]] · criteria: V2.threats_to_validity.master

### F-V2-007 — Tests estadísticos nombrados, con estadísticos y umbrales desactualizados

El inventario de inferencia incluye OLS con p-valores y test F (L.450–452), VIF (§3.2, L.454–458), Kruskal-Wallis (§3.3, L.460–464: «H = 25,741, p = 1e−05») y Welch t-test (§3.4, L.466–470, «codificado, no ejecutado en la corrida actual»), además de reglas de percentiles para anomalías (§3.5). El criterio `V2.statistical_tests` para `level=master` se lee: «Expected for paired comparisons (Wilcoxon signed-rank, sign test, t-test on differences, bootstrap CI)». El diseño es transversal y no contiene comparaciones pareadas, de modo que la familia de tests pareados no se activa; en su lugar hay tests de grupo y de especificación. Los valores reportados no coinciden con las tablas de respaldo: el rango VIF «1,13 a 1,58» (L.458) frente a 1,12–1,40 en `vif.csv`, y H = 25,741 / p = 1e−05 frente a H = 32,818 / p = 0,0 en `tests.csv`, según el contraste externo del inventario de claims. La conclusión cualitativa se mantiene en ambos casos; los estadísticos no. No se reporta corrección por comparaciones múltiples, elemento que el criterio master no exige.

— polarity: neutral · confidence: high · related: [[#C043]], [[#C047]], [[#C048]], [[#C049]] · criteria: V2.statistical_tests.master

### F-V2-008 — Contrastes de diseño y un único espejo externo, sin líneas base experimentales

El corpus ofrece dos puntos de contraste. `ARQUITECTURA_DATOS.md` §2 (L.516–527) presenta una matriz de seis motores —DuckDB, Polars, PyArrow, Iceberg/Delta, DuckLake, ClickHouse/chDB— con Adopción y Veredicto; la ventaja de Polars se atribuye a «benchmarks de proveedor» y el propio texto la condiciona a «Segundo motor, solo con medición» (L.521). El storytelling §7 (L.275–283) toma como único referente a `Egyptian-Used-Cars` y afirma «Nuestro proyecto ya tiene esa arquitectura». La única medición antes/después propia es la compactación Parquet «849 MB → 27,5 MB» (L.502) y el dashboard «107 KB» frente a los 6 HTML y ~4,5 MB remotos previos (L.659). El criterio `V2.baselines` para `level=master` se lee: «≥2 baselines, one of which corresponds to a SOTA-adjacent approach in the field». Los contrastes presentes son de arquitectura y de producto, no líneas base de evaluación de un método propuesto; el referente externo es singular y su calificativo «uno de los análisis más completos que tenemos» no se contrasta dentro del corpus.

— polarity: neutral · confidence: medium · related: [[#C035]], [[#C053]], [[#C107]], [[#C011]], [[#C060]] · criteria: V2.baselines.master

### F-V2-009 — Estados de implementación y periodicidades declarados de forma inconsistente entre secciones

Varias declaraciones del protocolo se contradicen entre bloques. El ledger LFS aparece como operativo en §3 («LFS con ledger `_state/lfs_push_ledger.jsonl`», L.671) y como pendiente en §6 («Pendiente (fase siguiente): … ledger LFS», L.711). El aislamiento de carriles afirma «Ningún job de recolección hace `git push`» (L.637) y «sin git push» (L.564), mientras §6 atribuye a los scripts de Revolico y marketplaces «push o reescritura completa» (L.711). La Tabla de periodicidades fija Revolico como «Semanal» (L.644) mientras el estado actual describe «Extracción continua … timer cada 10 minutos» (L.564). DuckDB figura como «Recomendado» (L.520) y, catorce líneas después, bloqueado por `SIGILL` (L.566). La compactación Parquet se da por «ya implementado» sobre 10.217 anuncios y 812 autos (L.497–502), cifras incompatibles con los 10.379 y 974 del README (L.19) a igual fecha. Estas tensiones afectan a la consistencia interna exigida por el criterio `V2.reproducibility_protocol.master`: el protocolo está descrito, pero su estado declarado varía según el archivo.

— polarity: negative · confidence: high · related: [[#C011]], [[#C013]], [[#C053]], [[#C055]], [[#C058]], [[#C059]], [[#C062]], [[#C071]] · criteria: V2.reproducibility_protocol.master

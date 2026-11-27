# Cómo se hicieron las encuestas y entrevistas

Fuente: instrumentos, metodologías y datos de los repositorios de referencia.
No son encuestas propias del proyecto; se documentan para valorar su uso en el
storytelling y en el análisis de demanda.

## 1. Encuesta de demanda de `Mercado-automotriz` (la única con datos tabulados)

**Quién y para qué.** Proyecto de la asignatura *Introducción a la Ciencia de
Datos*, titulado *Estudio del mercado automotriz en La Habana*. Se aplicó por
Google Forms con consentimiento informado explícito: "Esta encuesta es anónima,
sus datos se usarán solo con fines de estudio de la investigación de la
asignatura. ¿Acepta participar?".

**A quién.** Partiendo del informe de ICEX, se definieron cuatro segmentos con
poder adquisitivo: arrendadores de vivienda, propietarios de Mipymes, empleados
de Mipymes y trabajadores de empresas mixtas o agencias internacionales.

**Cómo se reclutó.** Trabajo de campo en el entorno del barrio: visita a la
oficina de la ONAT del municipio para conocer el número de propietarios que
arriendan viviendas; recorrido por la zona elaborando una lista de 13 viviendas
en alquiler y 12 Mipymes; además, se encuestó a empleados de esos negocios y a
trabajadores de CIMEX, FAO, CITROEM, Tabacos de Cuba, una constructora portuguesa
y agencias como PNUD, UNICEF y el aeropuerto. Algunas direcciones y centros de
trabajo quedaron registrados en la metodología.

**Cuántos y cómo se midió.** 33 respuestas: 18 hombres (55 %) y 15 mujeres
(45 %). Predominaron los de 51–70 años (11) y 31–50 (9); 22 de 33 (67 %) llevaban
5 años o más en el mismo trabajo. Por ocupación: 13 arrendadores (39 %), 8
empleados de Mipyme y 8 trabajadores de empresas mixtas (24 % cada uno), 4
propietarios de Mipyme (12 %). El formulario se llenó con respuestas codificadas
(1, 2, 3…) y una "leyenda" que traduce cada código; 32 preguntas en cinco bloques:
generales, desplazamiento, conocimiento y preferencias, disposición de compra y
obstáculos/infraestructura/información. Los datos llegaron en siete exportaciones
sucesivas (11, 12, 16, 19, 27, 30 y 33 respuestas); se conservó la última.

**Resultados útiles para nuestro análisis.**
- 17 encuestados de 18 a 25 años prefieren el eléctrico; entre 51–70 predomina
  la combustión (6) y el híbrido (3), con solo 2 eléctricos.
- 7 de 8 empleados de Mipyme prefieren eléctrico; los trabajadores de empresas
  mixtas prefieren gasolina/diésel; 3 de 4 propietarios de Mipyme, híbrido.
- Disposición de pago: 7 de 10 que prefieren combustión pagarían ≥5.000 USD; en
  el eléctrico, 11 de 18 (61 %) se ubican en 1.000–3.000 USD y 16 de 18 (89 %)
  no superan los 4.000 USD.
- De 28 interesados: 14 eléctrico (50 %), 10 combustión (36 %), 4 híbrido (14 %).
  9 de 14 aceptarían pagar el eléctrico en 24 meses o menos.
- Bestune Pony fue el modelo eléctrico más mencionado (7 menciones, 9 sumando
  Bestune Joyee), coherente con el registro de la Dirección Nacional de Tránsito
  de 2026: 124 autos y 17 jeeps eléctricos particulares, 74 autos y 30 paneles
  estatales.
- La oferta de Revolico es mayoritariamente de autos usados: los encuestados que
  quieren nuevos y eléctricos encuentran una oferta "prácticamente inexistente".

## 2. Encuesta de `ICD-Mercado-Automotriz` (instrumento, sin datos en el repo)

Cuestionario anónimo de 10 preguntas, "menos de 2 minutos", para un proyecto
universitario de Ciencia de Datos. Perfil, tenencia de carro, experiencia
compraventa, marca preferida (abierta), cuánto pagaría, tipo preferido (clásico
nacional / moderno importado / eléctrico / indiferente), percepción de precios,
intención de compra, forma de pago y tiempo estimado de venta.

**Aplicación prevista:** mercados informales, paradas de taxis, universidad y
WhatsApp. El entrevistador lee la pregunta y marca la respuesta (más rápido que
entregar papel). Meta: 30+ respuestas; pasarlas a `data/raw/encuestas.csv` al
final del día. Las instrucciones insisten en normalizar la marca preferida en la
fase de limpieza. **El repo no incluye el CSV de respuestas**: solo el guion.

## 3. Encuesta de `autos-cuba` (instrumento, sin datos en el repo)

Cuestionario de interés de compra con pregunta filtro ("¿tiene pensado comprar o
cambiar un vehículo en los próximos 3 años?") y cinco bloques: perfil, movilidad
actual, conocimiento de eléctricos/híbridos, intención y condiciones de compra,
barreras. Pide prueba piloto con 10–15 personas, preguntas cerradas o de escala,
códigos `user_001`, `user_002`… y prohibición de guardar nombres o teléfonos.
Tampoco hay respuestas tabuladas en el repositorio.

## 4. Entrevistas de `ICD-Mercado-Automotriz` (30 entrevistas + 8 audios)

Entrevista corta de 5–7 minutos, anónima, a vendedores y compradores en puntos
informales de venta. El guion dice **no leerlo**, conversar con naturalidad y
anotar después; no grabar sin permiso; nunca registrar nombre, teléfono ni placa.
Guion de apertura: "Buenos días, soy estudiante de la Universidad de La Habana…
Todo es anónimo y me tomará 5 minutos". Si se niega, agradecer y no insistir.

Preguntas al vendedor: tiempo vendiendo, precio pedido, precio acordado en la
última venta similar, margen de negociación, moneda preferida, papeles que se
entregan, tiempo de venta, motivo de venta, percepción del mercado y consejo al
comprador. Variante para compradores: presupuesto, bajadas conseguidas, forma de
pago, percepción de precios y consejo a un primerizo. El propio documento señala
que **precio pedido vs. acordado es "la perla del proyecto"**.

Se conservan 8 grabaciones (m4a/mp3) y un archivo `Entrevistas.txt` con 30
entrevistas **ya procesadas** —advierte que no son las respuestas literal—; algunas
personas se negaron a grabar o a dar datos personales. El tema central es el
costo de tener auto, muy alineado con nuestro storytelling:

- Chevrolet 1954 de carga: 40–100/200 litros diarios, 2,00–2,30 USD/L; reparación
  "bastante elevada", piezas en Mipymes e importadas.
- Chevrolet 55: 20–25 L/mes a 2,30 USD/L; mantenimiento cada 10.000 km en casa;
  15.000–30.000 CUP al año (19–38 USD a la tasa de 788 CUP/USD que usó el repo).
- Kia Picanto: 20–25 L/mes, ~2,50 USD/L; 200 USD/año de mantenimiento; neumáticos
  60–80 USD y batería 300 USD.
- Lada 2101: 80 L/mes a 2,60 USD/L; 200–300 USD de reparaciones.
- BYD F3: 60–80 L/mes; reparaciones de 2.000–3.000 USD.
- Lada 2107: 80–90 L/mes, 2,20–2,70 USD/L; 2.000–3.000 USD anuales.

## 5. Entrevistas de `Proyecto-Mercado-Automotriz` (30 entrevistas)

Objetivo declarado: al menos 30 declaraciones sobre la modernización del
automóvil en La Habana. Individuales o en grupos pequeños, voluntarias, anónimas,
sin nombres, teléfonos ni direcciones. Cada registro lleva `id_entrevista`, zona,
ocupación, relación con el mercado, tenencia de vehículo y experiencia con
eléctricos, más cuatro respuestas codificadas: tipo de vehículo observado,
marcas modernas observadas, opinión sobre eléctricos y predominio de clásicos.

Zonas mencionadas: Cerro y Alamar, entre otras. Ocupaciones: mecánico
independiente, cuentapropia, taxista particular, joven profesional informático,
Mipyme de mensajería, jubilado. Casi todos observan clásicos como mayoría y
califican de "mala" la opinión sobre vehículos eléctricos; las marcas modernas
más vistas son Kia, Hyundai, Foton, Bestune, Geely, DFSK y Mercedes.

## 6. Entrevistas estructuradas de `AutosxCuba` (8 registros)

Mezclan entrevistas presenciales con chats de Telegram. **Advertencia ética**:
este es el único conjunto que incluye nombres propios (Yosiel Galiano Jaime,
Maikol Sangron, Josue Libano, Darex Diaz) y un mecánico anónimo; no debe
reutilizarse tal cual en material público. Aporta citas de valor:

- Mipyme *Yosiel Auto*: Hyundai es la más vendida, seguida de Kia, Honda, Toyota,
  Geely, SASA, MCV; venden autos de segunda mano vía Europa–Panamá–Cuba; Rentacal
  da 2–3 años de explotación y luego vende en tienda; problema con el pago de
  Dongfeng por ser desde el exterior.
- Vendedor particular: "La gente lo busca mucho xq son económicos y no se rompen";
  Corolla 2018 entre 22.000 y 24.000 USD.
- Mecánico: los carros que más llegan al taller son Kia y Hyundai (2016–2024);
  MG es la marca con menos repuestos, Geely sí tiene; Toyota la más confiable;
  los problemas graves aparecen después de los 200.000 km; lo que más se trabaja
  es la dirección (cremallera) por los baches; las piezas importadas encarecen la
  reparación, sobre todo en autos posteriores a 2017.

## Valoración para el proyecto

- La encuesta de `Mercado-automotriz` es la única con **datos cuantitativos de
  demanda** y puede respaldar la sección de "fuerzas invisibles" (expectativas de
  precio, preferencia por tecnología, brecha entre interés y capacidad de pago).
- Las 30 entrevistas del repo ICD y las 8 de AutosxCuba son cualitativas y sirven
  para **profundidad explicativa**, no para inferencia estadística; encajan con el
  apartado de combustible, mantenimiento y retorno de inversión ya aprobado.
- Ninguna de las tres fuentes de encuesta es representativa a nivel nacional: dos
  son instrumentos sin respuestas y una es un muestreo deliberado de barrio con 33
  personas. Conviene citarlas como "estudios de caso" y no como medición de mercado.

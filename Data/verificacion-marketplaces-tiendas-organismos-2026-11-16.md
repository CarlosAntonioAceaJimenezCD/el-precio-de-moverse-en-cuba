# Verificación de marketplaces, tiendas de coches y organismos reguladores

**Fecha:** 16/11/2026  
**Proyecto:** ICD Automotive Market Project  
**Alcance:** 40 sitios/URLs de compraventa y mercados online, 15 tiendas con web propia y los organismos del Estado cubano con competencia sobre el mercado automotor.

> Criterio de “cumple”: el sitio tiene una categoría o sección de vehículos localizable, con enlaces de anuncios o fichas de vehículos. Se separan las secciones activas, las categorías vacías, los sitios de solo piezas/motos/servicios y los que no tienen sección.

---

## 1. Marketplaces con sección de automóviles activa

| # | Marketplace | URL exacta de la sección | Evidencia (16/11/2026) | Tipo |
|---|---|---|---|---|
| 1 | **Autocubana** | https://www.autocubana.com/anuncios-carros | **667 vehículos** publicados; carros, motos y utilitarios | C2C especializado |
| 2 | **iTENCEL** | https://itencel.com/anuncio-categoria/vehiculos/carros/ | **951 anuncios** en “Autos”; incluye piezas, motos y renta | C2C generalista |
| 3 | **VentaCuba** | http://www.ventacuba.com/vehiculos/carros-y-camionetas | **801 anuncios** en carros y camionetas; **1.392** en todo Vehículos | C2C generalista |
| 4 | **Timbirichi** | https://www.timbirichi.com/vehiculos-y-piezas/carros | **281 carros**; además 389 motos, 394 piezas de carros y 13 camiones/camionetas | C2C generalista |
| 5 | **Revolico** | https://www.revolico.com/search?category=vehiculos&subcategory=vehiculos-carros | Sección activa; **112 enlaces de anuncios** en la primera página, sin contador global | C2C líder |
| 6 | **Cogetucarro** | https://cogetucarro.com/index.php?categoria=1 | **5.225 anuncios** y **5.008 resultados**; categorías Carros, Motos, Barcos, Piezas y Alquiler | C2C especializado |
| 7 | **Cubisima** | https://www.cubisima.com/carros | **155 fichas de carros** en `sitemap-carros-1.xml`; el listado se carga por JS | C2C generalista |
| 8 | **Apululu** | https://apululu.es/anuncio-categoria/carros/ | **7 carros**, **35 autos** (incluye piezas) y **5 motos** | C2C generalista |
| 9 | **Carros.com — Cuba** | https://www.carros.com/cars-for-sale/cuba-co47/?lang=es | **15 fichas** con ubicación Cuba; plataforma internacional | Clasificados internacionales |

### 1.1. Categorías existentes pero vacías o sin coches

| Marketplace | URL de la categoría | Resultado |
|---|---|---|
| TuCuevita | https://www.tucuevita.com/categorias/vehiculos | Categoría creada, sin anuncios de vehículos |
| Mercubano | https://mercubano.com/c/vehiculos | Categoría creada, sin stock |
| Mercandil | https://www.mercandil.com/explorar/vehiculos | Categoría creada, sin stock |
| Revoltillo | https://www.revoltillo.com/autos | Categoría creada, sin stock |
| QvaVentas Anuncios | https://anuncios.qvaventas.com/listing-category/autos/ | Categoría “Autos” con **0** anuncios; el buscador usa `_category=113` |
| Casinuevo Cuba | https://cuba.casinuevo.com/coches-de-segunda-mano/ | **0** coches |
| Publicid.ad Cuba | https://publicid.ad/pais/cu/vehiculos | **0** anuncios |
| WAnuncios Cuba | https://cuba.wanuncios.com/coches-todoterreno-173.html | **1** resultado irrelevante |
| AnunciosCuba | https://anuncioscuba.net/anuncios/autos-en-cuba-carros/ | **1** anuncio, de alquiler, no de venta |

### 1.2. Solo piezas, motos o servicios automotrices

| Sitio | URL | Qué tiene realmente |
|---|---|---|
| BizneCubano Marketplace | https://marketplace.biznecubano.com/category/piezas-de-automoviles-y-motos | **19 piezas** de automóviles y motos; no vehículos completos |
| Katapulk | https://www.katapulk.com/ | Categorías “Autos y Motos” y “Partes y Piezas” dentro de Ferretería; el catálogo visible es de motos Aikon y accesorios |
| A la Venta Cuba | https://alaventacuba.com/servicios/vehiculos-automotriz | Servicios automotrices (mecánica, chapa, poncheras, grúas); la categoría pública de vehículos devuelve 404 |
| Pymes Bulevar | https://www.pymesbulevar.com/products/search?CategoryId=1211 | “Automotriz e Industrial” y “Motores”: lubricantes, aerosoles, piezas y una moto Jomar; no coches |
| MeroliCU | https://merolicu.com/category/vehicles | **13 productos** de “Vehículos”, casi todos motos, triciclos, bicimotos y patinetes; no coches completos |
| Rico Cuba | https://www.rico-cuba.com/ | Clasificados generales; no se pudo confirmar una categoría navegable de vehículos en el DOM renderizado |

### 1.3. Sin sección de vehículos

| Sitio | URL | Nota |
|---|---|---|
| Ecomcuba | https://ecomcuba.com/ | Negocios y productos; sin vehículos |
| Baznova | https://baznova.com/ | Tiendas locales; sin vehículos |
| Cuba Marketplace | https://cubamarketplace.com/ | Sin categoría de vehículos |
| Plaza Cubana | https://plazacubana.com/ | Sin categoría de vehículos |
| Cubazon | https://cubazon.dpdns.org/ | Sin categoría de vehículos |
| GrandCuba | https://www.grandcubamarket.com/ | Sin categoría de vehículos |
| Pati | https://www.pati.cu/ | Sin categoría de vehículos |
| Mercazón | https://mercazon.com/es | Supermercado; sin vehículos |
| Marketplace Cuba | https://marketplacecuba.com/ | Sin categoría de vehículos |
| HogarEnCuba | https://hogarencuba.com/ | Hogar; sin vehículos |
| Porlalivre | https://porlalivre.com/ | Clasificados; sin sección de vehículos |
| DoFiMall | https://www.dofimall.com/ | B2B; portada sin catálogo navegable |
| Mercadoba | https://mercadobausa.com/ | Catálogo de mercado; sin vehículos |
| Fagales Market | https://www.fagalesmarket.com/tienda/ | Solo aparecen coches de juguete, no vehículos reales |

### 1.4. Inaccesibles o no verificables por red

| Sitio | URL | Problema |
|---|---|---|
| Cuballama | https://www.cuballama.com/ | Reinicio de conexión TLS; no se pudo verificar la sección de autos |
| TuEnvio | https://www.tuenvio.cu/ | Timeout / 404; no verificable |

---

## 2. Tiendas web de coches que venden en Cuba

### 2.1. Concesionarios y distribuidores con operación directa en Cuba

| # | Tienda | URL | Marcas / oferta | Evidencia y observaciones |
|---|---|---|---|---|
| 1 | **BDC One** | https://bdcone.online/autos/ | MG, Maxus, Mitsubishi | Concesionario de referencia; stock “en plaza”; precios en EUR desde **14.849** (MG3) hasta **31.478** (MG RX9); garantía y posventa |
| 2 | **Dongfeng Cuba** | https://www.dongfengcuba.com/catalogo/ | Dongfeng, Voyah, MHERO | Catálogo 2026; eléctricos, híbridos, diésel y gasolina; precios desde **€21.900**; garantía 5 años/150.000 km |
| 3 | **MCV Commercial** | https://www.mcvcommercial.com/ | Mercedes-Benz, FUSO | Venta, leasing y renta; tienda virtual y catálogos; no publica precios unitarios en la portada |
| 4 | **Finauto International** | https://finautointernational.com/ | KIA, SsangYong (KGM) | Distribuidor oficial; catálogo con precios en EUR desde **15.500**; sede en Siboney, Playa |
| 5 | **Changan Automotive** | https://changanautomotive.com/ | Changan, BYD, Foton | Distribuidor exclusivo para Cuba; exportación directa desde China; catálogo con precios y más de 500 vehículos vendidos |
| 6 | **Chinautos Cuba (LXWY)** | https://chinautoscuba.com/autos/ | BYD, Changan, Toyota | Más de 40 modelos: eléctricos, híbridos, combustión y motos; catálogo con fichas por modelo |
| 7 | **Envision Autos Cuba** | https://envisionsol.com/ | Vehículos nuevos y usados; eléctricos e híbridos | Venta en Cuba con servicio postventa y talleres asociados; contacto por formulario/redes |
| 8 | **ATR Export** | https://www.atrexport.com/ | Changan, Suzuki, Toyota y otras | **46 modelos**; 5 eléctricos, 33 gasolina, 8 comerciales y 4 “en plaza”; importación a Cuba |
| 9 | **carrosw** | https://carrosw.com/ | Chevrolet, Ford, Kia, Hyundai, MG y otras | Importación para personas jurídicas (MIPYMEs, sucursales, ONG, iglesias, consulados y embajadas); sitio con verificación anti-bot, puede requerir navegador real |
| 10 | **ConnectingCuba** | https://www.connectingcuba.com/#vehiculos | Vehículos de EE. UU. y Europa; marcas comerciales y de pasajeros | Proveedor directo en Cuba; lista oficial de vehículos por marca/modelo; logística y entrega |
| 11 | **LlamaCuba** | https://llamacuba.com/venta-de-autos/ | Compra de vehículos en Cuba | Servicio para cubanos en el exterior; atención por teléfono/WhatsApp |
| 12 | **La Subasta Cubana** | https://lasubastacubana.com/ | Subastas Copart, IAAI y Manheim | Acceso a más de 500.000 vehículos; cobra tarifas de gestión; no es un concesionario con stock propio |

### 2.2. Comercializadoras estatales con web propia

| # | Tienda | URL | Oferta | Observaciones |
|---|---|---|---|---|
| 13 | **SASA** | https://www.sasa.com.cu/ | Venta en tienda, importación MLC, taller y repuestos | Autorizada por el Decreto 163/2026; su web no publica catálogo de coches, la venta de vehículos es presencial/reposición |
| 14 | **DIVEP** | https://portal-divep.xutil.cu/es | Comercialización de equipos, piezas y vehículos de la industria nacional | Autorizada por la Resolución 17/2026; la web está centrada en piezas, equipos y servicios, no en un catálogo de coches |

### 2.3. Exportadores internacionales con entrega en Cuba

| # | Tienda | URL | Oferta | Observaciones |
|---|---|---|---|---|
| 15 | **AGN Motors** | https://www.agnmotors.com/cuba/available-cars.htm | Usados y nuevos: BYD, Toyota, Hyundai, Kia, MG, etc. | Exportador con sede en Hamburgo; página específica para Cuba y cotización por contacto |

### 2.4. Servicios de importación/logística (no venden el coche, trasladan el tuyo)

| Servicio | URL | Qué hace |
|---|---|---|
| CubanCargos | https://cubancargos.com/carros | Importa tu auto desde EE. UU. a Cuba; no es un inventario de venta |
| GranAzul | https://www.granazul.com/es/offers/cars-to-cuba | Envío de autos desde Miami; logística y documentación |

### 2.5. Sitios que no deben confundirse con tiendas de coches

| Sitio | Motivo |
|---|---|
| Cubamax (https://cubamax.com/) | Renta de autos y travel; no venta directa verificada |
| Transtur / RentCarCuba (https://www.rentcarcuba.com/) | Renta de autos |
| Cuballama (https://www.cuballama.com/) | Renta/travel; sección de autos no verificable por TLS |
| CIMEX / Tiendas Caribe / La Copita | Venden vehículos en tiendas estatales, pero no tienen una web propia funcional con catálogo de coches; operan por Facebook y presencial |
| VEDCA (http://www.vedca.cu/) | Vehículos eléctricos, pero su línea visible es motos, triciclos, cuatriciclos y bicicletas; no coches |
| Carros Cubanos (https://www.carroscubanos.com/) | Recambios, neumáticos, baterías y accesorios; no vehículos completos |
| SOLIMPORT, DIVSE, IMPLUS | Ciclomotores, motos, triciclos y cuatriciclos; no coches |

---

## 3. Organismos del Estado que controlan el mercado automotor

No existe un único regulador: el mercado está repartido entre varios ministerios y un comité interinstitucional, el **CEMA**. La norma marco es el **Decreto 163/2026**, publicado en la **Gaceta Oficial No. 65 Ordinaria del 04/08/2026** y vigente desde el **11/08/2026**.

| # | Organismo / entidad | Función concreta en el mercado | Base legal / fuente |
|---|---|---|---|
| 1 | **Consejo de Ministros y Consejo de Estado** | Aprueban el Decreto 163/2026 y el Decreto Ley 122/2026 (Código de Seguridad Vial); definen la política y autorizan proyectos de inversización extranjera con objeto automotor | Gaceta Oficial No. 65/2026: https://www.gacetaoficial.gob.cu/es/gaceta-oficial-no-65-ordinaria-de-2026 |
| 2 | **MINCEX** — Ministerio del Comercio Exterior y la Inversión Extranjera | Autoriza a las personas jurídicas cubanas a importar vehículos para compraventa o arrendamiento; autoriza la importación de autos de personas naturales residentes, cooperantes, diplomáticos y tripulantes; gestiona el VUCE | Decreto 163/2026, Disposición Final Tercera; Resolución 104/2026: https://www.gacetaoficial.gob.cu/es/resolucion-104-de-2026-de-ministerio-del-comercio-exterior-y-la-inversion-extranjera |
| 3 | **MINCIN** — Ministerio del Comercio Interior | Autoriza a las entidades que pueden comercializar vehículos a personas naturales y jurídicas; aprueba la venta en USD; exige Licencia Comercial del Registro Central Comercial | Decreto 163/2026, Disposición Final Cuarta; Resolución 17/2026: https://www.gacetaoficial.gob.cu/es/resolucion-17-de-2026-de-ministerio-del-comercio-interior |
| 4 | **MITRANS** — Ministerio del Transporte | Dicta las regulaciones técnicas de importación, comercialización, fabricación, ensamblaje, homologación, recuperación y desarme; controla administrativamente las ventas; mantiene la lista de marcas, modelos y proveedores aprobados; preside el CEMA | Decreto 163/2026, Disposición Final Primera; Resolución 52/2026: https://www.gacetaoficial.gob.cu/es/resolucion-52-de-2026-de-ministerio-del-transporte |
| 5 | **CEMA** — Comité Evaluador de Medios Automotores | Órgano interinstitucional presidido por MITRANS. Acredita importadores, comercializadores y fabricantes; evalúa y aprueba proveedores, marcas y modelos; controla el Registro de Marcas de Vehículos; puede suspender importaciones o ventas; propone homologaciones | Decreto 163/2026, Art. 16; Resolución 52/2026, Anexo I |
| 6 | **MFP** — Ministerio de Finanzas y Precios | Fija los valores referenciales mínimos para los impuestos de transmisión e ingresos personales; regula el Impuesto Especial a Productos y Servicios por venta en USD; aprueba la formación de precios en CUP y USD; fija tarifas aduaneras y de servicios | Resoluciones 171, 172, 173, 174 y 175 de 2026, Gaceta No. 65; p. ej. https://www.gacetaoficial.gob.cu/es/resolucion-172-de-2026-de-ministerio-de-finanzas-y-precios |
| 7 | **ONAT** — Oficina Nacional de Administración Tributaria | Recauda el Impuesto sobre los Ingresos Personales y el Impuesto sobre Transmisión de Bienes y Herencias; controla el pago de tributos por vehículos y embarcaciones; depende del MFP | Resolución 171/2026; portal: https://www.onat.gob.cu/ |
| 8 | **Aduana General de la República** | Controla el despacho aduanero, las importaciones comerciales y no comerciales, los valores de referencia y las reglas de equipaje/envíos; emitió la Resolución 312/2026, derogada por la Resolución 340/2026 | Decreto Ley 108/2025 y Decreto 134/2025; Resolución 312/2026: https://www.gacetaoficial.gob.cu/es/resolucion-312-de-2026-de-aduana-general-de-la-republica |
| 9 | **Banco Central de Cuba (BCC)** | Define los instrumentos de pago permitidos para la compraventa y comercialización; regula las cuentas en divisas y las transacciones en USD o monedas convertibles; prohíbe el pago en efectivo en la compraventa entre particulares | Decreto 163/2026, Art. 3.2.c y Disposición Final Séptima; Resolución 102/2026: https://www.gacetaoficial.gob.cu/es/resolucion-102-de-2026-de-banco-central-de-cuba |
| 10 | **MININT** — Ministerio del Interior | A través de la Dirección Nacional de Tránsito y el **Registro de Vehículos**: inscribe la propiedad, expide licencias de circulación y chapas, controla bajas y cambios; la transmisión debe inscribirse en 30 días | Decreto 163/2026, Arts. 3, 5 y 6; https://www.minint.gob.cu/tramites/registro-de-vehiculos |
| 11 | **MINJUS** — Ministerio de Justicia | Ejerce la dirección técnica y normativa de la función notarial y de los registros públicos; las compraventas, donaciones, permutas y herencias de vehículos se formalizan ante notario; publica la Gaceta Oficial | Decreto 163/2026, Art. 3; https://www.minjus.gob.cu/es/mision-y-funciones |
| 12 | **MEP** — Ministerio de Economía y Planificación | Aprueba el **Balance de asignación de vehículos** en el marco del Plan de Inversiones Anual, a propuesta de MITRANS; participa en la planificación de la economía | Decreto 163/2026, Disposición Final Octava |
| 13 | **MINREX** — Ministerio de Relaciones Exteriores | Fija la cantidad máxima de vehículos que pueden importar o adquirir las misiones diplomáticas, oficinas consulares y organismos internacionales; autoriza cambios de chapa | Decreto 163/2026, Art. 15 y Disposición Final Quinta |
| 14 | **MINSAP** — Ministerio de Salud Pública | Autoriza la importación o compra en el país de vehículos por el personal de salud que trabaja en el exterior mediante contratos o convenios | Decreto 163/2026, Disposición Final Sexta |

### 3.1. Composición del CEMA

El CEMA está presidido por el **Ministro del Transporte** e integrado por representantes de:

- Ministerio de Economía y Planificación (MEP)
- Ministerio de Energía y Minas (MINEM)
- Ministerio de Industrias (MINDUS)
- Ministerio de Comercio Interior (MINCIN)
- Ministerio de Comercio Exterior y la Inversión Extranjera (MINCEX)
- Ministerio de Comunicaciones (MINCOM)
- Ministerio de Turismo (MINTUR)
- Ministerio de Finanzas y Precios (MFP)
- Ministerio de Ciencia, Tecnología y Medio Ambiente (CITMA)
- Ministerio del Interior (MININT)
- Fuerzas Armadas Revolucionarias (FAR)
- Ministerio de Educación Superior (MES)
- Banco Central de Cuba (BCC)
- Grupo de Administración Empresarial S.A. (GAESA)
- Aduana General de la República
- Instituto Nacional de Actores Económicos No Estatales (INAE)
- Instituto Nacional de Activos Económicos Estatales (INE)

**Lectura práctica:** para operar legalmente en Cuba no basta con tener una web o un catálogo. Se necesita autorización de MINCEX (importación), autorización de MINCIN (comercialización), acreditación ante el CEMA, aprobación de marcas/modelos/proveedores, licencia comercial del Registro Central Comercial y cumplimiento técnico de MITRANS. La inscripción de cada venta y la conciliación mensual con MITRANS/CEMA cierran el circuito administrativo.

---

## 4. Conclusiones para el proyecto ICD

1. **Marketplaces prioritarios para scraping de coches:** Autocubana, iTENCEL, VentaCuba, Timbirichi, Revolico, Cogetucarro, Cubisima y Apululu. Son los únicos con volumen relevante y sección de coches activa.
2. **Marketplaces secundarios:** Carros.com Cuba (internacional, bajo volumen) y MeroliCU (vehículos ligeros/motos, no coches).
3. **No perder tiempo con:** TuCuevita, Mercubano, Mercandil, Revoltillo, QvaVentas, Casinuevo, Publicid, WAnuncios y AnunciosCuba mientras no tengan stock; sus categorías existen pero están vacías.
4. **Tiendas con mejor información estructurada:** BDC One, Dongfeng Cuba, Finauto, ATR Export, Changan Automotive y Chinautos Cuba. Tienen catálogo, modelos y precios o cotización.
5. **Tiendas con fricción técnica:** carrosw (anti-bot), Cubisima (JS), MCV (catálogo poco accesible), Finauto (catálogo con 403 intermitente).
6. **Regulación:** el marco vigente es el Decreto 163/2026 y el paquete de resoluciones de la Gaceta No. 65/2026. Cualquier cambio de precios, aranceles o autorizaciones debe contrastarse con la Gaceta Oficial y con el CEMA/MITRANS.

---

## 5. Fuentes principales

- Gaceta Oficial No. 65 Ordinaria de 2026 (PDF completo): https://www.gacetaoficial.gob.cu/sites/default/files/goc-2026-o65_0.pdf
- Decreto 163/2026: https://www.gacetaoficial.gob.cu/es/decreto-163-de-2026-de-consejo-de-ministros
- Decreto Ley 122/2026: https://www.gacetaoficial.gob.cu/es/decreto-ley-122-de-2026-de-consejo-de-estado
- Resolución 104/2026 (MINCEX): https://www.gacetaoficial.gob.cu/es/resolucion-104-de-2026-de-ministerio-del-comercio-exterior-y-la-inversion-extranjera
- Resolución 17/2026 (MINCIN): https://www.gacetaoficial.gob.cu/es/resolucion-17-de-2026-de-ministerio-del-comercio-interior
- Resolución 52/2026 (MITRANS): https://www.gacetaoficial.gob.cu/es/resolucion-52-de-2026-de-ministerio-del-transporte
- Resolución 171/2026 (MFP): https://www.gacetaoficial.gob.cu/es/resolucion-171-de-2026-de-ministerio-de-finanzas-y-precios
- Resolución 172/2026 (MFP): https://www.gacetaoficial.gob.cu/es/resolucion-172-de-2026-de-ministerio-de-finanzas-y-precios
- Resolución 173/2026 (MFP): https://www.gacetaoficial.gob.cu/es/resolucion-173-de-2026-de-ministerio-de-finanzas-y-precios
- Resolución 312/2026 (Aduana, derogada por 340/2026): https://www.gacetaoficial.gob.cu/es/resolucion-312-de-2026-de-aduana-general-de-la-republica
- Resolución 102/2026 (BCC): https://www.gacetaoficial.gob.cu/es/resolucion-102-de-2026-de-banco-central-de-cuba
- Registro de Vehículos (MININT): https://www.minint.gob.cu/tramites/registro-de-vehiculos
- MINJUS, misión y funciones: https://www.minjus.gob.cu/es/mision-y-funciones
- ONAT: https://www.onat.gob.cu/
- Banco Central de Cuba: https://www.bc.gob.cu/
- MINCIN: https://www.mincin.gob.cu/es
- VUCE/MINCEX: https://vuceregulaciones.mincex.gob.cu/

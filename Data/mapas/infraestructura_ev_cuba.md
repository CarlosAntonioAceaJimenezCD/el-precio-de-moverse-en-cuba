# Infraestructura auxiliar para vehículos eléctricos en Cuba

Fecha: 18/11/2026. Búsqueda web (Yahoo/ddgs) por permiso del usuario.

## Hallazgos principales

| Fuente | Dato |
|---|---|
| [Dongfeng Cuba (20/04/2026)](https://www.dongfengcuba.com/blog/2026/04/20/dongfeng-cuba-impulsa-nuevas-estaciones-de-carga-para-vehiculos-electricos-en-el-pais) | Dongfeng Cuba / NWI impulsa estaciones de carga para EV. |
| [Directorio Cubano (18/04/2026)](https://www.directoriocubano.info/panorama/anuncian-11-estaciones-de-carga-solar-para-vehiculos-electricos-en-estas-provincias-de-) | Anuncio de **11 estaciones de carga solar** en varias provincias. |
| [Cubadebate (11/08/2026)](http://www.cubadebate.cu/noticias/2026/08/11/inauguran-la-primera-estacion-de-carga-solar-para-vehiculos-electricos-en-cuba/) | Primera estación de carga rápida/ultrarrápida en la Autopista Nacional, ~5 km de Santa Clara. |
| [CiberCuba (20/04/2026)](https://www.cibercuba.com/noticias/2026-04-20-u1-e13-s27061-nid326515-dongfeng-cuba-expande-infraestructura-carga-electrica) | Dongfeng Cuba construiría **11 estaciones** multiprovincia. |
| [Directorio Cubano (11/04/2025)](https://www.directoriocubano.info/panorama/cuba-anuncia-21-estaciones-de-carga-rapida-para-autos-electricos-primeras-ubicaciones-c) | CIMEX + MITRANS anunciaron **21 estaciones de recarga rápida**. |
| [KargalaYa](https://www.kargalaya.com/estaciones) | Directorio comunitario cubano de puntos de carga con mapa interactivo, conectores, precios y horarios. |
| [ChargeFinder](https://chargefinder.com/es/cuba/puntos-carga/zz9k82) y [Electromaps](https://www.electromaps.com/es/puntos-carga/cuba) | Listados internacionales; reportan conectores **CCS2** como mayoritarios. |

## Lectura para el proyecto

1. La red de carga aún está en despliegue (anuncios 2025–2026), por lo que el dato más confiable es el **directorio comunitario KargalaYa**.
2. Conectores predominantes: **CCS2**.
3. La fiabilidad de la red depende del suministro eléctrico; por eso es clave cruzar estas estaciones con el historial de circuitos de **Circuitos Habana** (ver `Data/apklis/`).
4. Próximo paso: scrapear KargalaYa y Electromaps para poblar la capa `charging_station` del mapa offline.

## Mapa offline

`Data/mapas/mapa_ofline.html` contiene el contorno de Cuba embebido y marcadores de los concesionarios con coordenadas verificadas desde los propios mapas incrustados en sus webs (BDC One, Dongfeng). Plotly se incluye dentro del HTML, así que funciona sin internet.

**Limitación:** Google Maps no se pudo usar porque el daemon Docker no arranca sin privilegios de root en este entorno. Overpass/OSM no devolvió locales etiquetados en Cuba (`shop=car`, `shop=car_repair`), así que los talleres y concesionarios adicionales tendrán que obtenerse de las webs y directorios (KargalaYa, páginas de contacto) y geocodificarse después.

## Capas añadidas al mapa offline (18/11/2026)

`Data/mapas/mapa_ofline.html` ya incluye tres capas:

| Capa | Puntos | Fuente |
|---|---:|---|
| Concesionarios | 3 | Coordenadas incrustadas en webs (BDC One ×2, Dongfeng) y geocodificación |
| **Estaciones de carga** | **9 con coordenadas + 3 referencias sin coords** | Kargalaya (9) y Electromaps (3) |
| **Gasolineras La Habana** | **137** | OpenStreetMap/Overpass, la misma base que usa WhereFUEL |

### Estaciones de carga con coordenadas (Kargalaya)

| Nombre | Provincia | Precio/hora | Estado | Renovable |
|---|---|---:|---|---|
| Super48 | Holguín | 250 CUP | verificada | sí |
| Battery Lab | La Habana | 0 CUP | verificada | sí |
| Estación de carga SOLGUARA | Villa Clara | 1000 CUP | no verificada | sí |
| Parqueo M y 25 | La Habana | 200 CUP | no verificada | no |
| Universidad de Ciencias Médicas de La Habana | La Habana | 100 CUP | no verificada | sí |
| Trisolinera Habana | La Habana | 250 CUP | no verificada | sí |
| PDL Campeño | La Habana | 0 CUP | no verificada | no |
| Estación de Carga de ADT64 | Villa Clara | 0 CUP | no verificada | sí |
| Automovion SRL | La Habana | 500 CUP | no verificada | no |

Electromaps aporta tres referencias más (Tecxol_Xetid_1 en La Lisa, Campismo Las Almendras en Bejucal y Campismo Peña Blanca) que quedan registradas en `estaciones_carga.csv` sin coordenadas hasta geocodificarlas.

ChargeFinder responde HTTP 403 en su API (`api.chargefinder.com`), por lo que solo se conserva como fuente documental.

## Gasolineras y precios

Además del mapa, se creó `Data/combustible/precios_combustible.sqlite` con **18 observaciones** entre el 20/08/2026 y el 18/11/2026, incluyendo tarifas oficiales CIMEX y precios informales. Los datos se actualizan mensualmente con `scrape_infraestructura.py`.

Hallazgo relevante para el análisis: desde el 07/02/2026 la venta oficial de combustible en CUP está suspendida y se vende en USD mediante el sistema Ticket; cada importador fija su precio desde mayo de 2026. La gasolina informal se movía en agosto entre 3.200 y 5.000 CUP/litro según tipo, y en septiembre la B94 llegó a 7.000–8.000 CUP/litro.

## Talleres y concesionarios añadidos (18/11/2026)

La base `mapa_elementos.sqlite` unifica cuatro capas con colores propios: gasolineras **negro**, estaciones de carga **verde**, concesionarios **azul** y talleres **rojo**. Estado actual: **131 gasolineras**, **12 estaciones de carga**, **25 concesionarios (17 con coords)** y **22 talleres (todos con coords)**.

Fuentes nuevas incorporadas:

- **BDC One**: `tiendas-y-talleres/` aportó el `Place` de schema.org con coordenadas y dirección (Fábrica entre Aspuru y Línea de Ferrocarril, Habana Vieja) y un segundo punto desde el mapa incrustado.
- **Dongfeng Cuba**: la web declara talleres especializados y postventa; se añadieron 3 puntos de servicio/showroom con coordenadas obtenidas de sus direcciones.
- **Cubisima**: Taller Calle 8, Calle 8 #112 entre 1ra y 3ra, Miramar, Playa (23.128616, -82.418164).
- **NearPlace**: 15 talleres de La Habana con coordenadas (CarFix, Taller VÉLO, SASA Servicios Automotores, Talleres de motos eléctricas, etc.).
- **Páginas Amarillas**: entradas de la categoría “Mecánica, Talleres de” (16 iniciales, 7 conservadas tras limpiar registros mal formateados).
- **tallermanolito.com** y **Yellocu/Cybo**: concesionarios y talleres adicionales; Cybo requirió `patchright`/FlareSolverr porque `curl_cffi` recibió 403.

Las direcciones sin coordenadas exactas se geocodificaron con Nominatim y, como respaldo, Photon. Las tres estaciones de Electromaps que solo tenían “La Habana” como dirección quedaron marcadas como **aproximadas al centro de la ciudad**.

Para generar solo ciertas capas:

```bash
.venv/bin/python herramientas/generar_mapa_ofline.py --tipos gasolinera,estacion_carga
.venv/bin/python herramientas/generar_mapa_ofline.py --tipos concesionario,taller
```

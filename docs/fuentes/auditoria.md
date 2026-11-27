# Auditoría de frescura de fuentes (23/11/2026)

Se consultan los sitios de origen y se comparan con la fecha más reciente guardada.
HTTP `ERR` indica que el sitio no respondió desde este entorno; no implica que esté caído.

## Marketplaces

| Fuente | Semilla | HTTP | Última modificación | Anuncios BD | Último dato |
|---|---|---|---|---:|---|
| apululu | https://apululu.es/anuncio-categoria/carros/ | 200 | — | 33 | 2026-11-17 |
| autocubana | https://www.autocubana.com/es/vehicle_listings?car_type=carr | 200 | — | 667 | 2026-11-18 |
| carroscom | https://www.carros.com/cars-for-sale/cuba-co47/?lang=es | 200 | — | 15 | 2026-11-17 |
| cogetucarro | https://cogetucarro.com/view.php?id=7859 | 200 | — | 200 | 2026-11-17 |
| cubisima | https://www.cubisima.com/carros | 200 | — | 155 | 2026-11-17 |
| itencel | https://itencel.com/anuncio-categoria/vehiculos/carros/ | 200 | — | 951 | 2026-11-18 |
| timbirichi | https://www.timbirichi.com/vehiculos-y-piezas/carros | 200 | — | 170 | 2026-11-18 |
| ventacuba | http://www.ventacuba.com/vehiculos/carros-y-camionetas | 200 | — | 31 | 2026-11-17 |

## Concesionarios

| Fuente | BD | Filas | Último dato |
|---|---|---:|---|
| agn_motors | `agn_motors.sqlite` | 60 | 2026-11-17 |
| atr_export | `atr_export.sqlite` | 6 | 2026-11-17 |
| bdc_one | `bdc_one.sqlite` | 19 | 2026-11-17 |
| changan | `changan.sqlite` | 2 | 2026-11-17 |
| chinautos_cuba | `chinautos_cuba.sqlite` | 70 | 2026-11-17 |
| connectingcuba | `connectingcuba.sqlite` | 1 | 2026-11-17 |
| dongfeng_cuba | `dongfeng_cuba.sqlite` | 45 | 2026-11-17 |
| envision_autos | `envision_autos.sqlite` | 1 | 2026-11-17 |
| finauto | `finauto.sqlite` | 45 | 2026-11-17 |
| mcv_commercial | `mcv_commercial.sqlite` | 4 | 2026-11-17 |
| subasta_cubana | `subasta_cubana.sqlite` | 3 | 2026-11-17 |

## Fuentes oficiales y complementarias

| Fuente | URL | HTTP | Nota |
|---|---|---|---|
| ONEI anuario | http://www.onei.gob.cu/cuba | 200 | verificación 23/11/2026 |
| Gaceta Oficial | https://www.gacetaoficial.gob.cu/es/gaceta-oficial-no-65-ordinaria-de-2026 | 200 | verificación 23/11/2026 |
| BCC tasas | https://api.bc.gob.cu/v1/tasas-de-cambio/activas | 200 | verificación 23/11/2026 |
| elTOQUE | https://eltoque.com/tasas-de-cambio-cuba | ERR | verificación 23/11/2026 |
| Womy | https://womy.cu/cars/ | 200 | verificación 23/11/2026 |
| Clasificados.st | https://cu.clasificados.st/motor | 200 | verificación 23/11/2026 |
| TecnoTáctil | https://www.tecnotactil.com/clasificados/mercado | 200 | verificación 23/11/2026 |

## Repositorios cubanos

| Repo | HEAD local | Commit remoto conocido | Cambios locales | Estado |
|---|---|---|---:|---|
| AppCubAutosScrapper_QMLQt | 822c697 2026-05-19 | 822c697 2026-05-19 | 57 | ## main...origin/main |
| AutosxCuba | c78b6a3 2026-11-09 | 9a6a8f2 2026-11-21 | 28 | ## main...origin/main [detrás 24] |
| ICD-Mercado-Automotriz | 4381244 2026-11-09 | 4381244 2026-11-09 | 346 | ## master...origin/master |
| Mercado-automotriz | 695407e 2026-11-06 | 695407e 2026-11-06 | 89 | ## master...origin/master |
| Proyecto-Mercado-Automotriz | c8d7757 2026-11-06 | c8d7757 2026-11-06 | 130 | ## main...origin/main |
| autos-cuba | 4d4e913 2026-10-25 | 4d4e913 2026-10-25 | 15 | ## master...origin/master |
| scrapper_autos_electricos | 9199eb5 2026-05-12 | 9199eb5 2026-05-12 | 48 | ## main...origin/main |

## Hallazgos calculados

- Fuentes web consultadas: 15; respondieron HTTP 200: 14; sin respuesta: 1.
- Repositorios cubanos revisados: 7; con ref remoto atrasada: 1; con cambios locales: 7.
- Esta auditoría es de solo lectura: no se modificaron sitios, bases ni repositorios.

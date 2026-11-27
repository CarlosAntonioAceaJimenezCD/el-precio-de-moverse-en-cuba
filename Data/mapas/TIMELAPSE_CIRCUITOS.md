# Factibilidad: timelapse de circuitos eléctricos desde el canal oficial

**Respuesta corta: sí.** Ya hay fuente pública, geometría de circuitos y lógica de parseo referida en el propio proyecto.

## 1. Fuente verificada

La app `Circuitos Habana` (APK en `Data/apklis/`) obtiene el estado eléctrico del canal público de Telegram de la Empresa Eléctrica de La Habana:

```text
https://t.me/s/EmpresaElectricaDeLaHabana
```

Verificación del 23/11/2026: HTTP 200, 111 KB de HTML, decenas de mensajes con fecha `2026-11-23T…+00:00`. No hace falta login ni API privada para la vista pública.

La app pagina con `?before=<message_id>` y en su código (descompilado en `Data/apklis/decompilado/`) figura el límite observado: **16 páginas, ~300 mensajes, 8 días** de historial (`OCHO_DIAS_MS`). El parseo usa palabras clave (afectación, restablecido, energizado, interrupción, traspasos, etc.), extrae circuitos y aplica **+1 hora** al timestamp UTC por horario de verano de Cuba.

## 2. Geometría disponible

Del APK se extrajeron tres archivos a `Data/mapas/circuitos/`:

| Archivo | Contenido |
|---|---|
| `circuitos_geodata.json` | 2.473 puntos georreferenciados (id, lat, lng, municipio, referencia) |
| `circuitos_habana.json` | 244 circuitos con circuito, municipio y ubicación |
| `circuitos_zonas.json` | 166 zonas con polígonos por código de circuito (D632, etc.) |

Con esto se puede colorear cada zona como **con luz / sin luz / sin dato** en un mapa Leaflet, sin buscar nuevas fuentes cartográficas.

## 3. Arquitectura propuesta

1. **Captura** — `Auxiliares/herramientas/scraper_circuitos.py`
   - Descarga `t.me/s/<canal>` y pagina con `?before=` de forma gradual y respetuosa (pausas, User-Agent, sin ráfagas).
   - Guarda cada mensaje en `Data/mapas/circuitos_estado.sqlite`: `mensaje_id`, `fecha_utc`, `circuito`, `estado`, `texto`, `causa`, `traspaso`.
   - Deduplica por `mensaje_id`; reconstruye el estado por circuito aplicando el evento más reciente.

2. **Parseo** — reglas inspiradas en el APK
   - Clasifica mensajes relevantes por palabras clave.
   -extrae códigos de circuito y distingue afectación de restablecimiento.
   - Normaliza fecha a hora de Cuba (+1 h) y ordena por timestamp.

3. **Timelapse** — `Data/mapas/timelapse_circuitos.html`
   - Mapa Leaflet con los 166 polígonos.
   - Slider temporal: para cada fecha, colorea las zonas según el último estado conocido.
   - Contador por fecha: circuitos encendidos, apagados y sin dato.
   - Opción de exportar fotogramas y armar un MP4 con `ffmpeg`.

4. **Actualización continua** — servicio systemd con timer cada 10–15 minutos. Sin captura continua no hay historia: la vista pública solo permite retroceder alrededor de 8 días.

## 4. Límites y consideraciones

- El canal es público, pero conviene respetar ritmo y términos de Telegram; para producción, la vía correcta es la **API oficial de Telegram** con autorización del canal.
- El history retroactivo está acotado; el timelapse verdadero empieza a construirse desde que se active el capturador.
- Algunos mensajes son ambiguos o mencionan traspasos; el estado "sin dato" debe ser explícito, no asumido.
- La política zonal y el horario de verano pueden cambiar: la conversión +1 h debe quedar parametrizada.

## 5. Relación con el proyecto

Este timelapse complementa el análisis automotriz: permite cruzar disponibilidad eléctrica con estaciones de carga, talleres y concesionarios, y refuerza la cuarta fuerza del storytelling (expectativas y restricciones reales de movilidad).

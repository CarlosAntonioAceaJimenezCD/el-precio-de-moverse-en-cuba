# Análisis técnico de la app `Circuitos Habana` (Apklis)

Fecha: 18/11/2026. Permiso del usuario para descargar herramientas de decompilación.

## APKs descargados desde Apklis

| App | Package | Versión | SHA-256 del release | Archivo |
|---|---|---|---|---|
| **Circuitos Habana** | `com.ermetic.circuitoshabana` | v2.2 | `6a299e9cf7f022fd9335db836632bc484ad7f386043311830d35dde38bedf71a` | `circuitos_habana.apk` (9,4 MB) |
| Apagones Habana | `cu.apagones.habana` | v12 | `698fc7e5151eb74b87aa920aeac74ac840783437e48b16f38e1577d91f2229d8` | `apagones_habana.apk` (2,9 MB) |
| Donde Hay Luz Habana | `com.apagonhabana.app` | v1.10.4 | `d5043ae8a870581180477c4a76d9cf4120518d15ae9698f90f271e95054dfa98` | `donde_hay_luz.apk` (22 MB) |

API usada: `https://api.apklis.cu/v2/application/` y `POST /v2/release/get_url/` con `{release: sha256}`. Descarga desde `archive.apklis.cu`.

Herramienta: **jadx 1.5.6** (Java 27 ya instalado). Código descompilado relevante copiado a `decompilado/`.

---

## Cómo se entera la app del estado eléctrico

**No usa una API privada ni Firebase.** Hace **scraping del canal público de Telegram de la Empresa Eléctrica de La Habana**:

```text
https://t.me/s/EmpresaElectricaDeLaHabana
```

El sufijo `/s/` es la vista web pública de Telegram. La app la descarga con Jsoup y un User-Agent de Chrome:

```java
private static final String TELEGRAM_CHANNEL_URL = "https://t.me/s/EmpresaElectricaDeLaHabana";
private static final String UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ... Chrome/121...";

Document document = Jsoup.connect(url).userAgent(UA).timeout(10000).followRedirects(true).get();
Elements messages = document.select("div.tgme_widget_message");
```

### Paginación

Para retroceder en el historial usa el ID del mensaje:

```text
https://t.me/s/EmpresaElectricaDeLaHabana?before=<message_id>
```

Límites observados en el código:

- hasta **16 páginas**;
- hasta **300 mensajes**;
- ventana de **8 días** (`OCHO_DIAS_MS = 691200000`);
- sincronización incremental con `ultimoIdConocido`.

### Parseo de cada mensaje

```java
Element time = element.select("time.time, time").first();
String datetime = time.attr("datetime");          // ISO UTC
Element text = element.select("div.tgme_widget_message_text, .js-message_text").first();
text.select("br").before("\n");
```

- `parsearIsoDateTime()` toma los primeros 19 caracteres, los interpreta como `yyyy-MM-dd'T'HH:mm:ss` en UTC y suma **+1 hora** (horario de verano de Cuba, `OFFSET_HORARIO_VERANO_MS = 3600000`).
- Los mensajes se ordenan por timestamp; se descartan los más antiguos que sobrescriben información reciente.

### Filtro de relevancia

`esMensajeRelevante()` acepta mensajes que contienen palabras como:

> afectación, afectados, déficit, avería, disparo, restablecido, restablecer, servicio, energizado, incorporado, normalizado, abierto, cerrado, desconectado, rotación, interrupción, apagón, apagado, traspasos.

Después un parser propio extrae:

- circuitos afectados y circuitos normales;
- bloques afectados;
- eventos ordenados y duraciones;
- causa de la avería;
- si es restablecimiento;
- traspasos entre circuitos (`Traspasos.java`).

### Almacenamiento y alertas

Los reportes se guardan localmente en SQLite (`ReporteAfectaciones`, `fechaPublicacionMs`, `mensajeId`, `duracionesMs`). La app genera notificaciones con distinto sonido para “se fue la luz” y “volvió la luz”, y muestra los circuitos sobre un mapa con teselas **OpenStreetMap / OpenTopoMap** (no Google Maps).

También incluye un enlace de comunidad WhatsApp: `https://chat.whatsapp.com/HbaEgn7ZGGGI6hoihlFBnH`.

---

## Utilidad para el ICD Automotive Market Project

1. **Fuente de datos real y gratuita**: el mismo canal de Telegram puede alimentar nuestro propio dataset histórico de apagones por circuito, sin depender de la app.
2. **Cruce con infraestructura eléctrica**: permite relacionar disponibilidad de energía con estaciones de carga de vehículos eléctricos y con la operación de talleres/concesionarios.
3. **Patrón reutilizable**: el enfoque `t.me/s/<canal>?before=<id>` + Jsoup es applicable a otros canales oficiales (transporte, combustible, etc.).
4. **Advertencia**: es un canal público, pero hay que respetar ritmo y términos de Telegram; para producción conviene usar la API oficial de Telegram con un bot y autorización del canal.

## Archivos generados

- `Data/apklis/*.apk` — APKs originales.
- `Data/apklis/decompilado/TelegramChannelFetcher.java` — lógica de descarga/parseo.
- `Data/apklis/decompilado/Traspasos.java` — detección de traspasos entre circuitos.
- `Data/apklis/analisis_circuitos_habana.md` — este informe.

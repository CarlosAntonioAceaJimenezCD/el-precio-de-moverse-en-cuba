# Revolico — categoría Vehículos

Base de datos generada por `Auxiliares/herramientas/scrape_revolico.py`.

## Proceso

1. Se recorren las **100 páginas válidas** de `https://www.revolico.com/search?category=vehiculos&cu=1&page=x` **desde la última (100) hacia la primera (1)**.
2. De cada página se extraen todos los `permalink` de anuncios desde el estado Apollo (`__APOLLO_STATE__`).
3. Cada anuncio se descarga con el sufijo `?p`, que evita la pantalla de verificación de Cloudflare.
4. Se guarda el objeto `AdType` completo, sus referencias (imágenes, provincia, municipio, categoría, teléfonos) y el HTML crudo.

## Archivos

- `revolico.sqlite`: base de datos.
- `urls.txt`: URLs únicas descubiertas.
- `resumen.md`: conteos y rango de fechas.

## Tablas

| Tabla | Contenido |
|---|---|
| `anuncios` | `id`, `url`, `title`, `description`, `price`, `currency`, `status`, `seller_name`, `contact_info`, `updated_on_by_user`, `updated_on_to_order`, `is_promoted`, `is_sold`, `views`, `images_count`, provincia/municipio/categoría, `meta_json`, `ad_json`, `apollo_full`, `text`, `raw_html`, `scraped_at` |
| `imagenes` | `ad_id`, `image_id`, `gcs_key`, `url` |
| `telefonos` | `ad_id`, `number`, `prefix`, `type`, `is_whatsapp` |

## Consultas

```bash
sqlite3 revolico.sqlite "SELECT COUNT(*) FROM anuncios;"
sqlite3 revolico.sqlite "SELECT title, price, currency FROM anuncios WHERE category_name LIKE '%Carro%' LIMIT 20;"
sqlite3 revolico.sqlite "SELECT MIN(updated_on_by_user), MAX(updated_on_by_user) FROM anuncios;"
sqlite3 revolico.sqlite "SELECT a.title, t.number FROM anuncios a JOIN telefonos t ON t.ad_id=a.id LIMIT 10;"
```

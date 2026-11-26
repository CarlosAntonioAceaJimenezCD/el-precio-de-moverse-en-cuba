# Integraciones / Integrations

Scripts importados de repositorios auxiliares (no versionados como clones) y adaptados a las rutas y variables de entorno de AutoDecide Habana.

| Ruta | Origen | Utilidad | Dependencias |
|---|---|---|---|
| `fuentes_cubanas/scrape_autocubana.py` | `anapaula65/AutosxCuba` | Catálogo Autocubana | `bs4`, `curl_cffi`, `requests` |
| `fuentes_cubanas/scraping_dongfeng.py` | `anapaula65/AutosxCuba` | Catálogo Dongfeng | `bs4`, `curl_cffi`, `requests` |
| `fuentes_cubanas/scraper_telegram.py` | `anapaula65/AutosxCuba` | Anuncios en canales de Telegram | `telethon` (credenciales en `TELEGRAM_API_ID`/`TELEGRAM_API_HASH`) |
| `fuentes_cubanas/scraper_revolico.py`, `scraper_itencel.py`, `scraper_vedca.py`, `scraper_cubamerica.py` | `AdrianaAmadorVerdecia/analisis-del-mercado-de-motos-bicicletas-patinetes` | Cuatro portales cubanos | `requests` |
| `spinny/*.py` | `2scraper/spinny-scraper` | Sesión, fingerprint, CAPTCHA, proxies, parseo y `diff_runs.py` | `playwright`, `bs4`, `requests`, `python-dotenv` |
| `telegram/telegraphite/*` | `hamodywe/telegram-scraper-TeleGraphite` | Cliente Telegram estructurado (contactos, fetcher, CLI) | `telethon`, `python-dotenv`, `pyyaml` |
| `facebook/marketplace_scraper.py`, `marketplace_gui.py` | `happyendpointhq/facebook-marketplace-scraper` | Marketplace con Playwright + UI | `bs4`, `playwright`, `fastapi`, `uvicorn`, `Pillow`, `streamlit` (credenciales en `FACEBOOK_EMAIL`/`FACEBOOK_PASSWORD`) |
| `facebook/selenium_car_scraper.py` | `vespertiliamvir/FacebookMarketplaceScraper` | Variante Selenium para autos | `selenium`, `webdriver_manager` |
| `facebook/facebook_gql_scraper/*` | `SoCloseSociety/facebook-gql-scraper` | Extracción GQL, limpieza de ruido, parser y normalización | `mini-racer`, `price-parser`, `pydantic`, `iso4217parse`, `requests` |
| `facebook/post_comment_scraper/*` | `mohdtalal3/facebook_post_comment_scraper` | Publicaciones y comentarios de grupos | `flask`, `requests` |
| `facebook/facebook_scraper/*` | `kevinzg/facebook-scraper` | Posts de páginas (ligero, sin navegador) | `bs4`, `lxml`, `dateparser`, `fake-useragent`, `demjson3` |
| `facebook/facebook_page_scraper/*` | `shaikhsajid1111/facebook_page_scraper` | Páginas con Selenium | `selenium`, `bs4` |
| `whatsapp/waha_client.py` | cliente propio sobre `devlikeapro/waha` | Lectura incremental de chats/grupos vía REST + dedup por id | `httpx` |
| `whatsapp/whatsapp_mcp_reader.py` | `lharries/whatsapp-mcp` | Lector de la BD SQLite del bridge Go (referencia) | `requests`, bridge Go |
| `whatsapp/whatsapp_web_example.js` | `wwebjs/whatsapp-web.js` | Ejemplo Node con Puppeteer (referencia) | Node + `puppeteer` |

Todas las salidas se escriben en `Data/integraciones/`. Las credenciales se leen de variables de entorno; no están en el código.

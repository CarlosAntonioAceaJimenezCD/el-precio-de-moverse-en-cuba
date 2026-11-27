# Repositorios de GitHub para CAPTCHA — evaluación para ICD

**Proyecto:** ICD Automotive Market Project  
**Fecha:** 16/11/2026  
**Método:** GitHub REST API (`/search/repositories`), 12 consultas temáticas, 92 repositorios únicos; verificación de estrellas, último push, licencia y README.  
**Criterio:** utilidad real para scraping de portales de autos en Cuba, mantenimiento reciente, licencia compatible y riesgo de abandono o malas prácticas.

> Las estrellas y fechas son las devueltas por GitHub en la fecha de la consulta. Un push reciente no garantiza calidad: revisar código, issues y dependencias antes de usar en producción.

---

## 1. Evasión / anti-detección (evitar que aparezca el CAPTCHA)

| Repositorio | ⭐ | Último push | Licencia | Valoración para ICD |
|---|---:|---|---|---|
| [Kaliiiiiiiiii-Vinyzu/patchright-python](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-python) | 1.604 | 2026-11-10 | Apache-2.0 | **Recomendado.** Playwright indetectable, drop-in; ideal para portales con Cloudflare/anti-bot. |
| [ultrafunkamsterdam/nodriver](https://github.com/ultrafunkamsterdam/nodriver) | 4.944 | 2026-10-26 | AGPL-3.0 | Sucesor de undetected-chromedriver; rápido y activo. AGPL: revisar implicaciones si se distribuye. |
| [ultrafunkamsterdam/undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) | 12.909 | 2025-07-05 | GPL-3.0 | **Legado.** Sin actualizaciones desde julio 2025; no usarlo en proyectos nuevos. |
| [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | 32.928 | 2026-11-15 | MIT | Chromium stealth, reemplazo directo de Playwright. Muy popular; verificar procedencia/telemetría antes de confiar. |
| [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | 12.328 | 2026-11-10 | MIT | Navegador stealth basado en Camoufox (Firefox) para agentes; buena alternativa a Chromium. |
| [seleniumbase/SeleniumBase](https://github.com/seleniumbase/SeleniumBase) | 13.264 | 2026-11-16 | MIT | Framework maduro con modo UC (undetected). Útil si el equipo ya usa Selenium. |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 103.582 | 2026-11-14 | BSD-3-Clause | Framework de scraping con modo stealth/Camoufox; no es un solver, pero reduce bloqueos. Ya clonado. |
| [oss-invisible/playwright](https://github.com/oss-invisible/playwright) | 2.588 | 2026-11-16 | MIT | Playwright sobre Firefox anti-detect con acciones humanizadas. Joven; evaluar estabilidad. |
| [TheGP/untidetect-tools](https://github.com/TheGP/untidetect-tools) | 2.072 | 2026-10-07 | Sin licencia | Lista curada de navegadores anti-detect, proxies y solvers. Solo referencia, no código. |
| [niespodd/browser-fingerprinting](https://github.com/niespodd/browser-fingerprinting) | 5.164 | 2026-07-27 | Sin licencia | Análisis de fingerprinting y contramedidas. Referencia técnica. |

**Conclusión:** para el stack ICD, `patchright-python` es la opción base; `camofox-browser`/`CloakBrowser` son alternativas si hay que rotar motores; `nodriver` solo si se acepta AGPL. Evitar `undetected-chromedriver` por falta de mantenimiento.

---

## 2. Cloudflare / Turnstile (resolver el challenge)

| Repositorio | ⭐ | Último push | Licencia | Valoración |
|---|---:|---|---|---|
| [FlareSolverr/FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) | 16.244 | 2026-10-24 | MIT | **Recomendado como microservicio local.** Proxy Docker que resuelve Cloudflare IUAM y devuelve cookies/HTML. Consume RAM; una instancia por request. |
| [sarperavci/CloudflareBypassForScraping](https://github.com/sarperavci/CloudflareBypassForScraping) | 2.651 | 2026-11-02 | MIT | API Docker con pool de Brave/DrissionPage, proxies y endpoint `/fetch`. Buena alternativa a FlareSolverr. |
| [chris124567/cfsolve](https://github.com/chris124567/cfsolve) | 778 | 2026-11-13 | MIT | Rust, resuelve Turnstile y `cf_clearance` sin navegador headless. Rápido, pero requiere perfiles de navegador y es más frágil. |
| [Theyka/Turnstile-Solver](https://github.com/Theyka/Turnstile-Solver) | 987 | 2026-10-28 | NOASSERTION | Solver con patchright, multihilo y API. **Licencia no estándar: revisar antes de usar.** |
| [techinz/playwright-captcha](https://github.com/techinz/playwright-captcha) | 364 | 2026-06-12 | Apache-2.0 | Integración con Playwright para Turnstile, interstitial y reCAPTCHA. Útil como capa de automatización. |
| [germondai/trawl](https://github.com/germondai/trawl) | 1.184 | 2026-11-16 | AGPL-3.0 | Motor de scraping autoalojado que evita challenges JS/CAPTCHA. AGPL; revisar antes de integrar. |
| [2captcha/2captcha-python](https://github.com/2captcha/2captcha-python) | 816 | 2026-10-20 | MIT | Cliente oficial de 2Captcha (servicio de pago). Solo como fallback. |
| [NopeCHALLC/nopecha-extension](https://github.com/NopeCHALLC/nopecha-extension) | 11.134 | 2026-10-02 | MIT | Extensión para reCAPTCHA, hCaptcha, Turnstile, PerimeterX, GeeTest, AWS WAF. Freemium: requiere API key/servicio de pago. |
| [noCaptchaAi/NoCaptcha-Ai-Browser-Extension](https://github.com/noCaptchaAi/NoCaptcha-Ai-Browser-Extension) | 353 | 2026-11-16 | Sin licencia | Extensión para reCAPTCHA v2 y OCR; servicio de pago. |

**Conclusión:** si los portales cubanos usan Cloudflare (Revolico y algunos marketplaces lo han hecho), empezar con `FlareSolverr` en Docker y cachear `cf_clearance`. Para Turnstile puro, `cfsolve` es la opción más ligera, pero exige más trabajo de perfil. `Theyka/Turnstile-Solver` es atractivo técnicamente, pero su licencia impide recomendarlo sin revisión legal.

---

## 3. OCR / ML local (CAPTCHA de imagen o texto)

| Repositorio | ⭐ | Último push | Licencia | Valoración |
|---|---:|---|---|---|
| [sml2h3/ddddocr](https://github.com/sml2h3/ddddocr) | 14.947 | 2026-03-10 | MIT | **Recomendado para CAPTCHA simple de imagen.** OCR general chino/inglés; no sirve para reCAPTCHA/Turnstile. |
| [kerlomz/captcha_trainer](https://github.com/kerlomz/captcha_trainer) | 3.218 | 2025-11-09 | Python (repo) | Entrenamiento de modelos CNN/RNN+CTC para CAPTCHA específicos de un sitio. Útil si ddddocr falla. |
| [f0ng/captcha-killer-modified](https://github.com/f0ng/captcha-killer-modified) | 1.955 | 2025-08-26 | Java (repo) | Plugin de Burp Suite con OCR; orientado a pruebas de seguridad, no a producción. |
| [shenhao-stu/ohmycaptcha](https://github.com/shenhao-stu/ohmycaptcha) | 912 | 2026-03-09 | MIT | Autoalojado, compatible con YesCaptcha; Playwright + OpenAI. Requiere clave de LLM y revisar coste. |
| [aydinnyunus/ai-captcha-bypass](https://github.com/aydinnyunus/ai-captcha-bypass) | 1.238 | 2026-05-23 | Python (repo) | Enfoque AI/visión. Revisar dependencias y calidad antes de usar. |
| [ypwhs/captcha_break](https://github.com/ypwhs/captcha_break) | 2.821 | 2022-02-25 | Jupyter (repo) | Antiguo; solo valor educativo. |
| [nladuo/captcha-break](https://github.com/nladuo/captcha-break) | 727 | 2018-11-06 | C++ (repo) | Muy antiguo; no usar. |

**Conclusión:** los CAPTCHA de los portales cubanos suelen ser imágenes simples o de texto; `ddddocr` cubre la mayoría. Solo si el sitio usa un esquema propio conviene entrenar con `captcha_trainer`.

---

## 4. Solvers gratuitos / basados en tokens

| Repositorio | ⭐ | Último push | Licencia | Valoración |
|---|---:|---|---|---|
| [xHossein/PyPasser](https://github.com/xHossein/PyPasser) | 627 | 2026-10-24 | MIT | **Recomendado como primera opción libre.** reCAPTCHA v2/v3, GeeTest v4, Lemin, Turnstile y muros anti-bot; HTTP puro + navegador stealth. |
| [dessant/buster](https://github.com/dessant/buster) | 9.391 | 2026-11-16 | GPL-3.0 | **Humano en el bucle.** Extensión que resuelve reCAPTCHA por audio con reconocimiento de voz. Buen fallback ético y de bajo volumen. |
| [sarperavci/GoogleRecaptchaBypass](https://github.com/sarperavci/GoogleRecaptchaBypass) | 1.910 | 2026-10-22 | Sin licencia | Resuelve reCAPTCHA por audio con DrissionPage/ffmpeg. **Sin licencia: no apto para producción.** |
| [nonecap/nonecap-py](https://github.com/nonecap/nonecap-py) | 350 | 2026-11-14 | MIT | Cliente de API para hCaptcha; freemium (según README, 100 resoluciones gratis/día). Verificar tarifas y privacidad. |
| [alenkimov/anycaptcha](https://github.com/alenkimov/anycaptcha) | 47 | 2026-04-01 | Python (repo) | API unificada para varios servicios de pago (2Captcha, CapSolver, etc.). Útil para no acoplar el código a un proveedor. |
| [2captcha/2captcha-python](https://github.com/2captcha/2captcha-python) | 816 | 2026-10-20 | MIT | Cliente oficial 2Captcha. Servicio de pago. |
| [capsolver/capsolver-python](https://github.com/capsolver/capsolver-python) | 75 | 2024-11-19 | MIT | Cliente Capsolver; algo desactualizado. |
| [CapMonsterCloud/capmonster-python-captcha-solver](https://github.com/CapMonsterCloud/capmonster-python-captcha-solver) | 39 | 2026-11-05 | Python (repo) | SDK de CapMonster Cloud; servicio de pago. |

**Conclusión:** `PyPasser` es la mejor relación libertad/mantenimiento para empezar. `Buster` es el fallback humano recomendable. Los servicios de pago (2Captcha, CapSolver, NopeCHA, NoneCap, CapMonster) solo si el volumen lo justifica y tras revisar privacidad y condiciones.

---

## 5. Listas, benchmarks y detección

| Repositorio | ⭐ | Último push | Licencia | Uso |
|---|---:|---|---|---|
| [TheGP/untidetect-tools](https://github.com/TheGP/untidetect-tools) | 2.072 | 2026-10-07 | Sin licencia | Directorio de navegadores anti-detect, proxies y solvers. |
| [scrapfly/Antibot-Detector](https://github.com/scrapfly/Antibot-Detector) | 630 | 2026-11-16 | JavaScript (repo) | Detecta Cloudflare, DataDome, PerimeterX, CAPTCHA y fingerprinting en un sitio. Útil para diagnosticar antes de elegir herramienta. |
| [techinz/browsers-benchmark](https://github.com/techinz/browsers-benchmark) | 426 | 2026-09-01 | Python (repo) | Benchmark de motores de automatización frente a Cloudflare; ayuda a elegir navegador. |
| [niespodd/browser-fingerprinting](https://github.com/niespodd/browser-fingerprinting) | 5.164 | 2026-07-27 | Sin licencia | Análisis técnico de fingerprinting y contramedidas. |

---

## 6. Stack recomendado para ICD

### Fase 1 — Evitar el CAPTCHA (preferido)
1. **patchright-python** como navegador base para portales con anti-bot.
2. **curl_cffi** para requests HTTP con huella TLS de navegador real (ya clonado).
3. **Scrapling** para extracción y modo stealth (ya clonado).
4. **camofox-browser** o **CloakBrowser** como motor alternativo si un sitio detecta Chromium.
5. **changedetection.io** para monitoreo de precios/stock sin navegar agresivamente.

### Fase 2 — CAPTCHA de imagen
1. **ddddocr** para OCR local.
2. **captcha_trainer** solo si el portal usa un CAPTCHA propio y ddddocr no alcanza.

### Fase 3 — Cloudflare / Turnstile
1. **FlareSolverr** en Docker para IUAM y retos de Cloudflare.
2. **CloudflareBypassForScraping** como alternativa con pool de navegadores y proxies.
3. **cfsolve** si se necesita velocidad y se puede mantener un perfil de navegador.

### Fase 4 — reCAPTCHA / hCaptcha
1. **PyPasser** (MIT, sin API de pago) como primer intento.
2. **Buster** para resolución humana asistida en bajo volumen.
3. **2Captcha / CapSolver / NopeCHA** solo como fallback de pago, con límite de gasto y revisión de privacidad.

### Fase 5 — Validación
- **Antibot-Detector** y **browsers-benchmark** para medir la tasa de bloqueo antes de escalar.
- Métricas: % de páginas con CAPTCHA, % de resoluciones correctas, latencia, coste por 1.000 páginas, IPs bloqueadas.

---

## 7. Advertencias importantes

1. **Términos de servicio:** resolver o evadir CAPTCHAs puede violar los ToS de Revolico, Facebook, WhatsApp, Telegram y otros portales. El incumplimiento puede suponer cierre de cuenta, bloqueo de IP o acciones legales según la jurisdicción.
2. **Legalidad:** no usar estas herramientas para acceder a cuentas ajenas, datos personales, áreas autenticadas ni para eludir controles de acceso. Limitarse a datos públicos y a sitios donde se tenga autorización.
3. **Privacidad:** los servicios de pago reciben imágenes/HTML de la página; no enviar datos personales, credenciales ni información de terceros.
4. **Licencias:** GPL/AGPL (nodriver, Buster, trawl, Botright) imponen obligaciones de copyleft si se distribuye el software. Varios repos no tienen licencia: no son aptos para producción.
5. **Seguridad:** auditar el código antes de ejecutarlo; usar contenedores, usuario no root, límites de red y variables de entorno para claves. Desconfiar de repos con pocas estrellas que prometen "gratis e ilimitado".
6. **Fragilidad:** los CAPTCHA y las defensas anti-bot cambian constantemente; prever mantenimiento y no depender de una sola herramienta.
7. **Ética de scraping:** respetar `robots.txt`, limitar la concurrencia, cachear, identificar el user-agent y no sobrecargar los sitios.

---

## 8. Repositorios ya disponibles en el proyecto

En `Auxiliares/Repositorios` están clonados con profundidad 1 (61 repositorios, ~2,2 GB). Los relevantes para CAPTCHA/anti-bot son:

**Base de scraping y evasión:**
- `patchright` y `patchright-python`
- `Scrapling`
- `SeleniumBase`
- `nodriver`
- `camofox-browser`
- `CloakBrowser`
- `curl_cffi`

**Resolución de CAPTCHA/Cloudflare:**
- `ddddocr`
- `PyPasser`
- `FlareSolverr`
- `CloudflareBypassForScraping`
- `cfsolve`
- `Buster`
- `Antibot-Detector`

**Monitoreo y automatización:**
- `changedetection.io`
- `browser-use`
- `firecrawl`
- `crawl4ai`
- `Scrapegraph-ai`

Registro autoritativo de clones: `~/Utilidades/HerramientasScraping/_clone_log.tsv` (61 entradas `OK`).

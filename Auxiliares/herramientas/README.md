# Herramientas auxiliares de investigación

## `ddg_research.py` — buscador DuckDuckGo resistente a bloqueos

Ubicación: `Auxiliares/herramientas/ddg_research.py`
Entorno: `Auxiliares/.venv/bin/python`

### Qué bloqueo encontramos y qué se aplicó

| Señal observada | Causa | Se aplicó |
|---|---|---|
| HTTP **202** + página “anomaly” tras ~24 peticiones seguidas | **IP marcada por ritmo alto** | Sí: pausa 6–10 s con jitter, backoff exponencial y cooldown |
| CAPTCHA de imágenes | No apareció | No |
| HTTP 403 / redirect a `duckduckgo.com/?q=` | No apareció (ya se usaba `curl_cffi`) | No |
| 200 con 0 resultados | No apareció | Se detecta de todos modos |

El fingerprint TLS **no era el problema**: ya se usaba `curl_cffi` con `impersonate="chrome"`. Tampoco hacía falta cambiar de IP: con 7–10 s entre peticiones se recuperaron 112 páginas. Lo que faltaba era **sesión, warm-up, `vqd`, caché, reanudación y backoff**.

### Características

- `curl_cffi.Session(impersonate="chrome")` con headers coherentes (UA ↔ TLS).
- Warm-up en `duckduckgo.com` para conservar cookies `__ddg1_`/`__ddg2_`.
- Página 1 por POST a `html.duckduckgo.com/html/`; páginas profundas por **GET paginado con `vqd`** (funciona incluso después de un 202).
- Rate limit con jitter, backoff exponencial y `--proxy` opcional (`DDG_PROXY`).
- Cache SQLite en `Auxiliares/cache/ddg.sqlite`: reanuda desde la última página buena y deduplica por URL.
- Fallbacks: `lite.duckduckgo.com` → `ddgs` → Mojeek.
- `analyze`: descarta ruido, mirrors y subpáginas, y localiza la racha de N páginas sin enlaces útiles.

### Comandos

```bash
PY=../../.venv/bin/python    # desde Auxiliares/herramientas

# 1. Diagnosticar bloqueo
$PY ddg_research.py doctor "mercado automovilistico trabajos investigativos"

# 2. Importar resultados de una sesión anterior
$PY ddg_research.py import-json /tmp/opencode/ddg_deep.json "mercado automovilistico trabajos investigativos"

# 3. Buscar de forma segura (reanuda sola desde la última página guardada)
$PY ddg_research.py search "mercado automovilistico trabajos investigativos" \
    --pages 112 --delay 7 --jitter 3 --backoff 60 --max-retries 2

# 4. Ver estado y exportar
$PY ddg_research.py status
$PY ddg_research.py export "mercado automovilistico trabajos investigativos" \
    --format markdown --out ../../Data/ddg_resultados.md

# 5. Analizar duplicados/mirrors y registrar la parada por 10 páginas vacías
$PY ddg_research.py analyze "mercado automovilistico trabajos investigativos" \
    --streak 10 --out ../../Data/ddg-trabajos-investigativos-analisis.md
```

Si aparece un bloqueo persistente, el proceso guarda el estado y termina con código 2.
Para reanudar, se vuelve a llamar a `search` con el mismo query; no repite páginas ya cacheadas.

### Criterio de “enlace útil” usado en `analyze`

Se cuenta como útil solo la **primera aparición** de un trabajo investigativo automotriz:
tesis, TFG/TFM, artículo, estudio de mercado o informe académico/oficial con título automotriz.
**No cuentan** como útiles:

- resultados repetidos;
- mirrors del mismo trabajo en ResearchGate / Academia / Dialnet / SciELO;
- subpáginas de un resultado principal (mismo dominio ya visto);
- noticias, guías “cómo hacer…”, ofertas de empleo, vídeos, foros y páginas comerciales.

Informe generado: `Data/ddg-trabajos-investigativos-analisis.md`.

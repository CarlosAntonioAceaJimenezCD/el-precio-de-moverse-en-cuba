# Regenerar el análisis y el sitio

Supone Python 3.10+ y el entorno `Auxiliares/.venv-py`.

## Pasos

```bash
Auxiliares/.venv-py/bin/pip install -r requirements.txt mkdocs mkdocs-material
Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py
Auxiliares/.venv-py/bin/python Auxiliares/herramientas/generar_sitio_mkdocs.py
Auxiliares/.venv-py/bin/mkdocs build
```

## Resultado esperado

- `Data/analisis_rentabilidad/data/listings_clean.parquet` actualizado.
- `site/` con la página publicable.
- Si hay enlaces rotos, `mkdocs build --strict` los señala.

## Servir en local

```bash
Auxiliares/.venv-py/bin/mkdocs serve
```

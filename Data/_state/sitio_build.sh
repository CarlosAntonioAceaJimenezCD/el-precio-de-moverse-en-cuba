#!/usr/bin/env bash
set -euo pipefail
ROOT="/home/thony70807/Proyectos/El precio de moverse en Cuba"
"$ROOT/Auxiliares/.venv-py/bin/python" "$ROOT/Auxiliares/herramientas/generar_dashboard.py" --solo-si-cambia
"$ROOT/Auxiliares/.venv-py/bin/python" "$ROOT/Auxiliares/herramientas/generar_sitio_mkdocs.py"
"$ROOT/Auxiliares/.venv-py/bin/mkdocs" build --strict -f "$ROOT/mkdocs.yml" -d "$ROOT/site"

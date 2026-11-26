#!/usr/bin/env bash
set -uo pipefail
ROOT="/home/thony70807/Proyectos/El precio de moverse en Cuba"
"$ROOT/Data/_state/run_step.sh" circuitos /usr/bin/python3 "$ROOT/Auxiliares/herramientas/scraper_circuitos.py" --pages 2 --resumen || exit $?
# El estado eléctrico cambia cada captura: refrescar el panel de inmediato.
"$ROOT/Auxiliares/.venv-py/bin/python" "$ROOT/Auxiliares/herramientas/generar_dashboard.py" --solo-si-cambia

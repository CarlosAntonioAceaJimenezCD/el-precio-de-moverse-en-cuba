#!/usr/bin/env bash
set -uo pipefail
ROOT="/home/thony70807/Proyectos/El precio de moverse en Cuba"
exec "$ROOT/Data/_state/run_step.sh" calidad "$ROOT/Auxiliares/.venv-py/bin/python" "$ROOT/Auxiliares/herramientas/validar_calidad.py"

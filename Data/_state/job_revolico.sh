#!/usr/bin/env bash
set -uo pipefail
ROOT="/home/thony70807/Proyectos/El precio de moverse en Cuba"
export TIMEOUT=2700
exec "$ROOT/Data/_state/run_step.sh" revolico \
  "$ROOT/Auxiliares/.venv-py/bin/python" \
  "$ROOT/Auxiliares/herramientas/scrape_revolico_pipeline.py" \
  --max-pages 3 --downloaders 2 --processors 2 --batch-size 50

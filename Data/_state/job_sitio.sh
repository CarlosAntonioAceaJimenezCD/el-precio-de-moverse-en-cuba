#!/usr/bin/env bash
set -uo pipefail
ROOT="/home/thony70807/Proyectos/El precio de moverse en Cuba"
exec "$ROOT/Data/_state/run_step.sh" sitio bash "$ROOT/Data/_state/sitio_build.sh"

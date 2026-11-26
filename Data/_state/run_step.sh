#!/usr/bin/env bash
# Envoltorio común para todos los jobs automáticos.
# Uso: run_step.sh <job> <comando> [args...]
set -uo pipefail

JOB="${1:?falta nombre del job}"
shift
[ "$#" -gt 0 ] || { echo "falta comando" >&2; exit 2; }

ROOT="/home/thony70807/Proyectos/El precio de moverse en Cuba"
STATE="$ROOT/Data/_state"
LOCKS="$STATE/.locks"
mkdir -p "$LOCKS"

exec 9>"$LOCKS/$JOB.lock"
if ! flock -n 9; then
  echo "[$JOB] ya hay otra instancia corriendo; se omite" >&2
  exit 0
fi

PY="${PY:-$ROOT/Auxiliares/.venv-py/bin/python}"
INICIO=$(date -u +%s)
"$PY" - "$STATE" "$JOB" running "$INICIO" <<'PYEOF' || true
import json, sys
from pathlib import Path
state, job, status, inicio = Path(sys.argv[1]), sys.argv[2], sys.argv[3], int(sys.argv[4])
archivo = state / f"{job}.json"
datos = {}
if archivo.exists():
    try: datos = json.loads(archivo.read_text())
    except Exception: datos = {}
datos.update(status=status, heartbeat_utc=__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(), inicio=inicio)
tmp = archivo.with_suffix('.tmp'); tmp.write_text(json.dumps(datos, indent=2)); tmp.replace(archivo)
PYEOF

echo "[$JOB] inicio $(date -u +%FT%TZ)"
# El comando corre en su propio grupo de procesos: si este envoltorio recibe
# TERM/INT, mata a todo el grupo y no deja hijos huérfanos tras un reinicio.
setsid timeout "${TIMEOUT:-3600}" "$@" 9>&- &
CHILD=$!
trap 'kill -TERM -"$CHILD" 2>/dev/null || true' TERM INT
wait "$CHILD"
RC=$?
trap - TERM INT
FIN=$(date -u +%s)
ESTADO="ok"; [ "$RC" -ne 0 ] && ESTADO="error"

"$PY" - "$STATE" "$JOB" "$ESTADO" "$INICIO" "$FIN" "$RC" <<'PYEOF' || true
import json, sys
from datetime import datetime, timezone
from pathlib import Path
state, job, status, inicio, fin, rc = Path(sys.argv[1]), sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
archivo = state / f"{job}.json"
datos = {}
if archivo.exists():
    try: datos = json.loads(archivo.read_text())
    except Exception: datos = {}
ahora = datetime.now(timezone.utc).isoformat()
datos.update(status=status, fin_utc=ahora, heartbeat_utc=ahora,
             duracion_s=fin-inicio, exit_code=rc,
             last_success_utc=ahora if rc == 0 else datos.get('last_success_utc'),
             last_failure_utc=None if rc == 0 else ahora,
             fallos_consecutivos=0 if rc == 0 else int(datos.get('fallos_consecutivos', 0)) + 1)
tmp = archivo.with_suffix('.tmp'); tmp.write_text(json.dumps(datos, indent=2)); tmp.replace(archivo)
PYEOF

echo "[$JOB] fin $ESTADO rc=$RC duracion=$((FIN-INICIO))s"
exit "$RC"

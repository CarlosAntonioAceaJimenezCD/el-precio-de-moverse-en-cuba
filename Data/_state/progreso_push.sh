#!/bin/bash
# Escribe un reporte de progreso de la subida a GitHub.
# Lo ejecuta precio-push-progreso.timer cada 10 minutos.
cd "$(dirname "$0")/../.." || exit 1

OUT=Data/PROGRESO_PUSH.md
LOG=Data/_state/push_github.log
now=$(date -u '+%Y-%m-%d %H:%M UTC')

state=$(systemctl --user show -p ActiveState --value precio-push.service 2>/dev/null)
start=$(systemctl --user show -p ActiveEnterTimestamp --value precio-push.service 2>/dev/null)
epoch=$(date -d "$start" +%s 2>/dev/null)
if [ -n "$epoch" ]; then
  elapsed=$(( ($(date +%s) - epoch) / 60 ))
  tiempo="$elapsed minutos"
else
  tiempo="desconocido"
fi

local_head=$(git rev-parse --short HEAD 2>/dev/null)
remote=$(timeout 12 git ls-remote origin refs/heads/main 2>/dev/null | cut -c1-12)
remote=${remote:-"sin respuesta"}
lfs_local=$(find .git/lfs/objects -type f 2>/dev/null | wc -l)
lfs_refs=$(/home/thony70807/.local/bin/git-lfs ls-files 2>/dev/null | wc -l)
activos=$(pgrep -fc git-lfs 2>/dev/null)

{
  echo "# Progreso de la subida a GitHub"
  echo
  echo "- Actualizado: $now"
  echo "- Servicio: **$state**"
  echo "- Tiempo transcurrido: $tiempo"
  echo "- Commit local: $local_head"
  echo "- GitHub (origin/main): $remote"
  echo "- Objetos LFS en disco: $lfs_local | referenciados: $lfs_refs"
  echo "- Procesos git-lfs activos: $activos"
  echo
  echo "## Últimas líneas del log"
  echo '```'
  tail -12 "$LOG" 2>/dev/null || echo '(sin log)'
  echo '```'
  echo
  if [ "$remote" = "40ed0cdba142" ]; then
    echo "**Aún no se publicó nada.** La subida de objetos LFS continúa en segundo plano."
  else
    echo "**GitHub ya apunta a $remote.** Revisa el log por LFS_EXIT/GIT_EXIT para confirmar."
  fi
} > "$OUT"

#!/bin/bash
# Subida reanudable: primero los objetos LFS, luego los commits.
# Lo ejecuta el servicio de usuario precio-push.service.
cd "$(dirname "$0")/../.." || exit 1

LOG=Data/_state/push_github.log
GIT=/usr/bin/git
LFS=/home/thony70807/.local/bin/git-lfs

echo "INICIO $(date -u '+%Y-%m-%d %H:%M UTC')" >> "$LOG"

"$LFS" push origin main >> "$LOG" 2>&1
echo "LFS_EXIT=$?" >> "$LOG"

"$GIT" push origin main >> "$LOG" 2>&1
echo "GIT_EXIT=$?" >> "$LOG"

echo "FIN $(date -u '+%Y-%m-%d %H:%M UTC')" >> "$LOG"

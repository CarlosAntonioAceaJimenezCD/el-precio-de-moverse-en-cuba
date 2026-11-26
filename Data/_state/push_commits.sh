#!/bin/bash
# Sube los commits saltando el hook de LFS (los objetos ya están en GitHub).
# Los blobs grandes del historial hacen que la transferencia sea lenta.
cd "$(dirname "$0")/../.." || exit 1

LOG=Data/_state/push_commits.log
echo "INICIO $(date -u '+%Y-%m-%d %H:%M UTC')" >> "$LOG"
/usr/bin/git -c core.hooksPath=Data/_state/hooks_vacios push origin main >> "$LOG" 2>&1
echo "GIT_EXIT=$?" >> "$LOG"
echo "FIN $(date -u '+%Y-%m-%d %H:%M UTC')" >> "$LOG"

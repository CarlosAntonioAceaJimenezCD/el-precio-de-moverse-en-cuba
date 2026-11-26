#!/bin/bash
# Sube el objeto LFS grande que falta en GitHub (revolico.sqlite viejo, 804 MB).
cd "$(dirname "$0")/../.." || exit 1
LOG=Data/_state/lfs_big.log
OID=b57a8800f7fae8fa71bcc1db9e47bdeb9c29b838d1a3c437a900953548b788f0
echo "INICIO $(date -u '+%Y-%m-%d %H:%M UTC')" >> "$LOG"
/home/thony70807/.local/bin/git-lfs push --object-id origin "$OID" >> "$LOG" 2>&1
echo "LFS_EXIT=$?" >> "$LOG"
echo "FIN $(date -u '+%Y-%m-%d %H:%M UTC')" >> "$LOG"

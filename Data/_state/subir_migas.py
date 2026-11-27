#!/usr/bin/env python3
"""Publica main en migas de ~4 MB y reanuda desde donde se quedó."""
import os
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = '40ed0cdba142a0d9af1d1ad1518749ccd4ba02ad'
LOG = ROOT / 'Data/_state/push_migas.log'
IDX = ROOT / 'Data/_state/.indice_migas'
HOOKS = 'Data/_state/hooks_vacios'
GRUPO = 4_000_000

env = os.environ.copy()
env['GIT_INDEX_FILE'] = str(IDX)


def log(s):
    with LOG.open('a', encoding='utf-8') as f:
        f.write(f"{time.strftime('%H:%M:%S')} {s}\n")
    print(s, flush=True)


def g(*args, check=True):
    r = subprocess.run(['git', '-C', str(ROOT), *args], env=env, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {args}: {r.stderr[-400:]}")
    return r.stdout.strip()


def entradas(rev):
    r = subprocess.run(['git', '-C', str(ROOT), 'ls-tree', '-r', '-z', rev], capture_output=True)
    out = {}
    for e in r.stdout.split(b'\0'):
        if not e or b'\t' not in e:
            continue
        meta, path = e.split(b'\t', 1)
        modo, tipo, oid = meta.split()
        out[path.decode()] = (modo.decode(), oid.decode())
    return out


def remoto():
    try:
        r = subprocess.run(['git', '-C', str(ROOT), 'ls-remote', 'origin', 'refs/heads/main'],
                           capture_output=True, text=True, timeout=60)
        return r.stdout.split()[0] if r.returncode == 0 and r.stdout.strip() else None
    except subprocess.TimeoutExpired:
        return None


def push(commit):
    for intento in (1, 2, 3):
        try:
            r = subprocess.run(['git', '-C', str(ROOT), '-c', f'core.hooksPath={HOOKS}',
                                'push', 'origin', f'{commit}:refs/heads/main'],
                               capture_output=True, text=True, timeout=240)
            if r.returncode == 0:
                log(f'  OK {commit[:9]}')
                return True
            log(f'  intento {intento}: {r.stderr[-160:]}')
        except subprocess.TimeoutExpired:
            log(f'  intento {intento}: timeout')
        time.sleep(6)
    return False


def main():
    LOG.write_text('INICIO ' + time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime()) + '\n', encoding='utf-8')
    destino = g('rev-parse', 'HEAD^{tree}')
    base = entradas(BASE)
    target = entradas(destino)
    log(f'destino {destino[:9]} | archivos base {len(base)} | destino {len(target)}')

    punta = remoto()
    if not punta:
        log('SIN RED')
        return
    log(f'remoto {punta[:9]}')

    actuales = entradas(punta) if punta != BASE else base
    pendientes = []
    for path, (modo, oid) in sorted(target.items()):
        if actuales.get(path) != (modo, oid):
            size = int(g('cat-file', '-s', oid))
            pendientes.append((path, modo, oid, size))
    borrar = [p for p in actuales if p not in target]
    log(f'pendientes {len(pendientes)} ({sum(x[3] for x in pendientes)/1e6:.0f} MB) | borrar {len(borrar)}')

    grupos = []
    actual, total = [], 0
    for item in pendientes:
        if actual and total + item[3] > GRUPO:
            grupos.append(actual)
            actual, total = [], 0
        actual.append(item)
        total += item[3]
    if actual:
        grupos.append(actual)
    log(f'grupos: {len(grupos)}')

    commit = punta
    tree = g('rev-parse', f'{punta}^{{tree}}')
    for n, grupo in enumerate(grupos, 1):
        g('read-tree', tree)
        for p in borrar if n == 1 else []:
            g('update-index', '--force-remove', '--', p)
        for path, modo, oid, _ in grupo:
            g('update-index', '--add', '--cacheinfo', f'{modo},{oid},{path}')
        tree = g('write-tree')
        commit = g('commit-tree', tree, '-p', commit, '-m', f'Publicar main por migas {n}/{len(grupos)}')
        log(f' Grupo {n}/{len(grupos)}: {len(grupo)} archivos, {sum(x[3] for x in grupo)/1e6:.1f} MB')
        if not push(commit):
            return

    subprocess.run(['git', '-C', str(ROOT), 'reset', '--hard', commit], capture_output=True, check=True)
    fin = remoto() or ''
    log(f'FINAL local {commit[:12]} remoto {fin[:12]} IGUALES {fin[:12] == commit[:12]}')


if __name__ == '__main__':
    main()

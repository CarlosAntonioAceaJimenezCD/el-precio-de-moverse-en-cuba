#!/usr/bin/env python3
"""Pipeline de 3 etapas con colas persistentes para Revolico.

Etapas (se ejecutan en paralelo):
  1. Descubrimiento: recorre página por página y guarda el enlace de cada anuncio
     en `url_queue`.
  2. Descarga: workers toman URLs pendientes, descargan la página con curl_cffi
     y guardan TODOS los datos parseados en `download_queue`.
  3. Procesamiento: workers clasifican cada anuncio (4+ ruedas + datos necesarios)
     y dejan la decisión en `process_queue`.

Cada 25 anuncios **procesados** (aceptados o rechazados) se hace un commit por
lotes en la BD principal: aceptados -> `anuncios` + `autos` (+ imágenes y teléfonos),
rechazados -> `revision`. Nada se descarta sin registro.

Uso:
  python scrape_revolico_pipeline.py --max-pages 5 --downloaders 8 --processors 4
"""

from __future__ import annotations

import argparse
import json
import signal
import sqlite3
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import scrape_revolico as sr
import limpiar_revolico as lr
from db_chunks import ensure_db

FECHA_MINIMA = "2021-01-01"

OUT = sr.OUT
MAIN_DB = sr.DB
QUEUE_DB = OUT / "pipeline.sqlite"
ensure_db(OUT / "pipeline_chunks" / "MANIFEST.json", QUEUE_DB)
# Adaptado de integraciones/spinny (output_writer.py + diff_runs.py):
# snapshot {id: precio} entre corridas para no descargar anuncios sin cambios.
SNAP_DIR = OUT / "snapshots"
SNAP_FILE = SNAP_DIR / "ultimo.json"
BATCH = 25


def conn_queue() -> sqlite3.Connection:
    c = sqlite3.connect(QUEUE_DB, timeout=30, check_same_thread=False)
    c.execute("PRAGMA journal_mode=WAL")
    c.execute("PRAGMA busy_timeout=30000")
    return c


def init_queues() -> None:
    c = conn_queue()
    c.executescript(
        """
        CREATE TABLE IF NOT EXISTS url_queue (
            path TEXT PRIMARY KEY, status TEXT DEFAULT 'pending',
            discovered_at TEXT, error TEXT
        );
        CREATE TABLE IF NOT EXISTS download_queue (
            id TEXT PRIMARY KEY, payload TEXT, status TEXT DEFAULT 'pending',
            downloaded_at TEXT, error TEXT
        );
        CREATE TABLE IF NOT EXISTS process_queue (
            id TEXT PRIMARY KEY, decision TEXT, motivo TEXT,
            status TEXT DEFAULT 'pending', processed_at TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_url_status ON url_queue(status);
        CREATE INDEX IF NOT EXISTS idx_dl_status ON download_queue(status);
        CREATE INDEX IF NOT EXISTS idx_pr_status ON process_queue(status);
        """
    )
    for col, decl in (
        ("ad_id", "TEXT"), ("price", "TEXT"), ("sig", "TEXT"),
        ("titulo", "TEXT"), ("es_auto_candidato", "INTEGER DEFAULT 1"), ("motivo", "TEXT"),
    ):
        existing = {r[1] for r in c.execute("PRAGMA table_info(url_queue)")}
        if col not in existing:
            c.execute(f"ALTER TABLE url_queue ADD COLUMN {col} {decl}")
    c.commit()
    c.close()


def load_snapshot() -> dict:
    if SNAP_FILE.is_file():
        try:
            return json.loads(SNAP_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def save_snapshot() -> None:
    SNAP_DIR.mkdir(parents=True, exist_ok=True)
    m = conn_main()
    data = {str(r[0]): str(r[1] or "") for r in m.execute("SELECT id, updated_on_to_order FROM anuncios")}
    m.close()
    SNAP_FILE.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def conn_main() -> sqlite3.Connection:
    c = sqlite3.connect(MAIN_DB, timeout=60, check_same_thread=False)
    c.execute("PRAGMA journal_mode=WAL")
    c.execute("PRAGMA busy_timeout=60000")
    return c


AD_COLS = [
    "id", "url", "title", "short_description", "description", "price", "currency",
    "status", "seller_name", "contact_info", "updated_on_by_user", "updated_on_to_order",
    "is_promoted", "is_sold", "views", "images_count", "province_id", "province_name",
    "municipality_id", "municipality_name", "category_id", "category_name",
    "subcategory_id", "subcategory_name", "meta_json", "ad_json", "apollo_full",
    "text", "raw_html", "scraped_at",
]
AUDIT_COLS = ["es_auto", "motivo_exclusion", "pagina_revisada", "datos_necesarios"]


def ensure_main_tables(c: sqlite3.Connection) -> None:
    c.execute(
        """CREATE TABLE IF NOT EXISTS revision (
            id TEXT PRIMARY KEY, url TEXT, categoria TEXT, motivo TEXT, revisado_utc TEXT)"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS autos AS SELECT
            id,url,title,short_description,description,price,currency,status,
            province_name,municipality_name,category_id,subcategory_id,
            images_count,scraped_at,raw_html,text FROM anuncios WHERE 0"""
    )
    c.commit()


STOP = threading.Event()
DISCOVERY_DONE = threading.Event()
lock_commit = threading.Lock()
processed_counter = {"n": 0}
skipped_counter = {"n": 0}
SNAPSHOT: dict[str, str] = {}
# El timestamp `updatedOnToOrder` del listado cambia por ranking, no por edición
# del anuncio, así que no es una firma fiable. Por defecto se descarga todo.
SKIP_UNCHANGED = False


def clasificar_enlace(titulo: str) -> tuple[int, str]:
    """Clasificación temprana con el título del listado (antes de descargar).

    Regla: si el título tiene palabras claramente excluidas (moto, repuesto,
    accesorio, llanta, alquiler, servicio…) y NO tiene palabras de vehículo
    4+ ruedas, se descarta. En caso de duda se marca candidato para no perder
    autos reales; la clasificación definitiva sigue siendo la del procesamiento.
    """
    texto = titulo or ""
    excluido = bool(lr.EXCLUDE_TITLE.search(texto))
    # Antes, una marca en el título podía vencer a la exclusión y dejar pasar
    # motos/repuestos. La exclusión manda siempre.
    if excluido:
        return 0, "descartado en descubrimiento: no es vehículo 4+ ruedas"
    return 1, ""


def descubrir_hasta_fecha() -> None:
    """Modo solo-descubrimiento: página por página hacia atrás hasta 2021-01-01
    o hasta que se acaben las páginas. No descarga ni escribe en `anuncios`.
    """
    c = conn_queue()
    pagina = 1
    anterior: set[str] = set()
    vistos_totales: set[str] = set()
    total = 0
    motivo_fin = "límite de seguridad"

    while pagina <= 2000:
        if STOP.is_set():
            motivo_fin = "detenido"
            break
        html = sr.get_html(sr.SEARCH.format(page=pagina))
        st = sr.state_from(html)
        ads: dict[str, tuple[str, str, str]] = {}
        fechas: list[str] = []
        for k, v in st.items():
            if k.startswith("AdType:") and isinstance(v, dict) and v.get("permalink"):
                fecha = str(v.get("updatedOnToOrder") or "")[:10]
                ads[v["permalink"]] = (
                    str(v.get("id") or ""),
                    str(v.get("updatedOnToOrder") or ""),
                    str(v.get("title") or ""),
                )
                if fecha:
                    fechas.append(fecha)

        if not ads:
            motivo_fin = "sin anuncios en la página"
            break

        rutas_pagina = set(ads)
        nuevos = len(rutas_pagina - vistos_totales)
        repetidos = len(rutas_pagina & vistos_totales)
        vistos_totales |= rutas_pagina
        insertados = 0
        ahora = sr.now()
        for path, (ad_id, sig, titulo) in ads.items():
            candidato, motivo = clasificar_enlace(titulo)
            cur = c.execute(
                """INSERT OR IGNORE INTO url_queue
                   (path,status,discovered_at,ad_id,sig,titulo,es_auto_candidato,motivo)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (path, "descubierto", ahora, ad_id, sig, titulo, candidato, motivo),
            )
            insertados += cur.rowcount
        c.commit()
        total += nuevos

        fecha_min = min(fechas) if fechas else "—"
        print(
            f"[descubrimiento] página {pagina}: {len(ads)} anuncios, {nuevos} nuevos, "
            f"{repetidos} repetidos, insertados {insertados}, fecha mínima {fecha_min} (acumulado {total})",
            flush=True,
        )

        if fechas and min(fechas) < FECHA_MINIMA:
            motivo_fin = f"alcanzada fecha mínima {FECHA_MINIMA}"
            break
        if nuevos == 0:
            motivo_fin = "los anuncios se están repitiendo; se detiene el descubrimiento"
            break
        actual = set(ads)
        if actual == anterior:
            motivo_fin = "fin de páginas (página repetida)"
            break
        anterior = actual
        pagina += 1
        time.sleep(0.35)

    c.close()
    marca = OUT / ".backfill_completo"
    marca.write_text(
        f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} | {motivo_fin} | páginas={pagina} | enlaces={total}\n",
        encoding="utf-8",
    )
    print(f"Descubrimiento terminado: {motivo_fin} | páginas={pagina} | enlaces={total}", flush=True)


def discover(max_pages: int) -> None:
    """Página por página, anuncio por anuncio: guarda el enlace en la cola."""
    c = conn_queue()
    written = 0
    for page in range(max_pages, 0, -1):
        if STOP.is_set():
            break
        html = sr.get_html(sr.SEARCH.format(page=page))
        st = sr.state_from(html)
        found = {}
        for k, v in st.items():
            if k.startswith("AdType:") and isinstance(v, dict) and v.get("permalink"):
                found[v["permalink"]] = (
                    str(v.get("id") or ""),
                    str(v.get("updatedOnToOrder") or ""),
                    str(v.get("title") or ""),
                )
        now = sr.now()
        m = conn_main()
        for path, (ad_id, sig, titulo) in found.items():
            candidato, motivo = clasificar_enlace(titulo)
            estado = "pending" if candidato else "rechazado"
            c.execute(
                """INSERT OR IGNORE INTO url_queue
                   (path,status,discovered_at,ad_id,sig,titulo,es_auto_candidato,motivo)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (path, estado, now, ad_id, sig, titulo, candidato, motivo),
            )
            if not candidato:
                m.execute(
                    "INSERT OR IGNORE INTO revision VALUES (?,?,?,?,?)",
                    (ad_id, "https://www.revolico.com" + path, "", motivo, now),
                )
            written += 1
        m.commit()
        m.close()
        c.commit()
        print(f"[descubridor] página {page}: {len(found)} enlaces (cola {written})", flush=True)
        time.sleep(0.35)
    c.close()
    DISCOVERY_DONE.set()


def _retry_exec(c, sql, params=()):
    """Reintenta escrituras cuando SQLite devuelve 'database is locked'."""
    for intento in range(8):
        try:
            return c.execute(sql, params)
        except sqlite3.OperationalError as e:
            if "locked" not in str(e).lower() or intento == 7:
                raise
            time.sleep(0.15 * (intento + 1))
    return None


def download_loop() -> None:
    c = conn_queue()
    while not STOP.is_set():
        row = c.execute(
            "SELECT path,ad_id,sig FROM url_queue WHERE status='pending' AND es_auto_candidato=1 LIMIT 1"
        ).fetchone()
        if not row:
            time.sleep(0.5)
            continue
        path, ad_id, sig = row
        # Adaptado de diff_runs.py: si la firma no cambió, no volvemos a descargar.
        if SKIP_UNCHANGED and ad_id and sig and SNAPSHOT.get(ad_id) == sig:
            c.execute("UPDATE url_queue SET status='done' WHERE path=?", (path,))
            c.commit()
            with lock_commit:
                skipped_counter["n"] += 1
            continue
        _retry_exec(c, "UPDATE url_queue SET status='downloading' WHERE path=?", (path,))
        for _ in range(8):
            try:
                c.commit()
                break
            except sqlite3.OperationalError:
                time.sleep(0.2)
        try:
            d = sr.fetch_one(path)
            if d:
                payload = dict(d)
                payload["meta_json"] = json.dumps(d.get("meta", {}), ensure_ascii=False)
                payload["scraped_at"] = sr.now()
                c.execute(
                    "INSERT OR IGNORE INTO download_queue (id,payload,status,downloaded_at) VALUES (?,?,?,?)",
                    (str(d["id"]), json.dumps(payload, ensure_ascii=False), "pending", sr.now()),
                )
                c.execute("UPDATE url_queue SET status='done' WHERE path=?", (path,))
            else:
                c.execute("UPDATE url_queue SET status='failed', error='fetch_one=None' WHERE path=?", (path,))
        except Exception as e:
            _retry_exec(c, "UPDATE url_queue SET status='failed', error=? WHERE path=?", (str(e)[:300], path))
        for _ in range(8):
            try:
                c.commit()
                break
            except sqlite3.OperationalError:
                time.sleep(0.2)
    c.close()


def commit_batch() -> None:
    """Vuelca los procesados pendientes a la BD principal."""
    q = conn_queue()
    m = conn_main()
    ensure_main_tables(m)
    rows = q.execute(
        "SELECT id,decision,motivo FROM process_queue WHERE status='pending' LIMIT ?", (BATCH,)
    ).fetchall()
    if not rows:
        q.close(); m.close(); return

    accepted = rejected = 0
    now = sr.now()
    for pid, decision, motivo in rows:
        dl = q.execute("SELECT payload FROM download_queue WHERE id=?", (pid,)).fetchone()
        if not dl:
            continue
        d = json.loads(dl[0])
        if decision == "accept":
            values = []
            for col in AD_COLS:
                if col == "meta_json":
                    values.append(d.get("meta_json", "{}"))
                else:
                    values.append(d.get(col, ""))
            values += [1, motivo or "", 1, 1]  # es_auto, motivo, pagina_revisada, datos_necesarios
            all_cols = AD_COLS + AUDIT_COLS
            m.execute(
                f"INSERT OR IGNORE INTO anuncios ({','.join(all_cols)}) VALUES ({','.join('?'*len(all_cols))})",
                values,
            )
            auto_cols = [c for c in all_cols if c in
                         {"id","url","title","short_description","description","price","currency",
                          "status","province_name","municipality_name","category_id","subcategory_id",
                          "images_count","scraped_at","raw_html","text"}]
            m.execute(
                f"INSERT OR IGNORE INTO autos ({','.join(auto_cols)}) VALUES ({','.join('?'*len(auto_cols))})",
                [values[all_cols.index(c)] for c in auto_cols],
            )
            for im in d.get("images", []):
                m.execute(
                    "INSERT OR IGNORE INTO imagenes (ad_id,image_id,gcs_key,url) VALUES (?,?,?,?)",
                    (pid, str(im.get("id", "")), im.get("key", ""), im.get("url", "")),
                )
            for ph in d.get("phones", []):
                m.execute(
                    "INSERT OR IGNORE INTO telefonos (ad_id,number,prefix,type,is_whatsapp) VALUES (?,?,?,?,?)",
                    (pid, str(ph.get("number", "")), ph.get("prefix", ""), ph.get("type", ""),
                     int(ph.get("is_whatsapp", 0))),
                )
            accepted += 1
        else:
            m.execute(
                "INSERT OR IGNORE INTO revision VALUES (?,?,?,?,?)",
                (pid, d.get("url", ""), lr.categoria(d.get("text", "")), motivo or "", now),
            )
            rejected += 1
        q.execute("UPDATE process_queue SET status='committed' WHERE id=?", (pid,))
    m.commit()
    q.commit()
    q.close(); m.close()
    print(f"[commit] lote de {len(rows)}: {accepted} aceptados, {rejected} rechazados", flush=True)


def process_loop() -> None:
    q = conn_queue()
    while not STOP.is_set():
        row = q.execute("SELECT id,payload FROM download_queue WHERE status='pending' LIMIT 1").fetchone()
        if not row:
            time.sleep(0.5)
            continue
        pid, payload = row
        q.execute("UPDATE download_queue SET status='processing' WHERE id=?", (pid,))
        q.commit()
        try:
            d = json.loads(payload)
            guardar, motivo, pagina_ok, datos_ok = lr.clasificar(d)
            if guardar and pagina_ok and datos_ok:
                decision, motivo_final = "accept", ""
            else:
                decision = "reject"
                motivo_final = motivo or "sin motivo"
                if not pagina_ok:
                    motivo_final += "; página sin datos suficientes"
            q.execute(
                "INSERT OR REPLACE INTO process_queue (id,decision,motivo,status,processed_at) VALUES (?,?,?,?,?)",
                (pid, decision, motivo_final, "pending", sr.now()),
            )
            q.execute("UPDATE download_queue SET status='processed' WHERE id=?", (pid,))
            q.commit()
            with lock_commit:
                processed_counter["n"] += 1
                if processed_counter["n"] % BATCH == 0:
                    commit_batch()
        except Exception as e:
            q.execute(
                "INSERT OR REPLACE INTO process_queue (id,decision,motivo,status,processed_at) VALUES (?,?,?,?,?)",
                (pid, "reject", f"error de procesamiento: {e}", "pending", sr.now()),
            )
            q.execute("UPDATE download_queue SET status='failed' WHERE id=?", (pid,))
            q.commit()
    q.close()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-pages", type=int, default=100)
    ap.add_argument("--downloaders", type=int, default=8)
    ap.add_argument("--processors", type=int, default=4)
    ap.add_argument("--batch-size", type=int, default=25)
    ap.add_argument("--skip-unchanged", action="store_true", help="omitir anuncios cuya firma de listado no cambió (no fiable para precio)")
    ap.add_argument("--solo-colas", action="store_true", help="no descubre páginas nuevas; solo drena las colas pendientes")
    ap.add_argument("--solo-descubrimiento", action="store_true", help="solo recorre páginas hasta 2021-01-01 o fin; sin descarga ni BD")
    args = ap.parse_args()
    global BATCH, SKIP_UNCHANGED
    BATCH = args.batch_size
    SKIP_UNCHANGED = args.skip_unchanged

    OUT.mkdir(parents=True, exist_ok=True)
    init_queues()

    if args.solo_descubrimiento:
        descubrir_hasta_fecha()
        return

    # Los enlaces descubiertos en el backfill pasan a cola de descarga normal.
    q = conn_queue()
    q.execute("UPDATE url_queue SET status='pending' WHERE status='descubierto' AND es_auto_candidato=1")
    q.execute("UPDATE url_queue SET status='rechazado' WHERE status='descubierto' AND es_auto_candidato=0")
    q.commit()
    q.close()

    global SNAPSHOT
    SNAPSHOT = load_snapshot()
    print(f"Snapshot cargado: {len(SNAPSHOT)} anuncios", flush=True)
    m = conn_main()
    ensure_main_tables(m)
    m.close()

    threads = []
    if args.solo_colas:
        print("Modo solo-colas: sin descubrimiento de páginas nuevas", flush=True)
        DISCOVERY_DONE.set()
    else:
        t = threading.Thread(target=discover, args=(args.max_pages,), daemon=True)
        t.start(); threads.append(t)
    for _ in range(args.downloaders):
        t = threading.Thread(target=download_loop, daemon=True); t.start(); threads.append(t)
    for _ in range(args.processors):
        t = threading.Thread(target=process_loop, daemon=True); t.start(); threads.append(t)

    signal.signal(signal.SIGTERM, lambda *_: STOP.set())
    try:
        while True:
            time.sleep(2)
            q = conn_queue()
            pending = q.execute(
                """SELECT
                   (SELECT count(*) FROM url_queue WHERE status IN ('pending','downloading') AND es_auto_candidato=1),
                   (SELECT count(*) FROM download_queue WHERE status IN ('pending','processing')),
                   (SELECT count(*) FROM process_queue WHERE status='pending')"""
            ).fetchone()
            q.close()
            if DISCOVERY_DONE.is_set() and sum(pending) == 0:
                print("Colas vacías; cerrando pipeline.", flush=True)
                break
    except KeyboardInterrupt:
        print("Interrumpido por el usuario", flush=True)
    finally:
        STOP.set()
        commit_batch()
        for t in threads:
            t.join(timeout=5)
        save_snapshot()
    print(
        f"Procesados: {processed_counter['n']} | omitidos por snapshot: {skipped_counter['n']}",
        flush=True,
    )

    # Mantener las partes de la BD listas para revolico-git.timer.
    try:
        import actualizar_revolico as ar

        estado = ar.split_database()
        ar.update_report(estado)
        print(f"Partes generadas: {len(estado['partes'])}", flush=True)
    except Exception as exc:
        print(f"No se pudieron generar partes: {exc}", flush=True)


if __name__ == "__main__":
    main()

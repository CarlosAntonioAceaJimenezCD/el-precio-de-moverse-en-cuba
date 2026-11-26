#!/usr/bin/env python3
"""
Buscador DuckDuckGo resistente a bloqueos para el ICD Automotive Market Project.

Diseñado para el bloqueo real observado: HTTP 202 + pagina "anomaly" por ritmo alto,
no por fingerprint TLS. Incluye:

- Sesion unica con warm-up y cookies (curl_cffi impersonate=chrome).
- Endpoint HTML con token vqd; POST para la pagina 1 y GET paginado para las demas.
- Rate limit con jitter, backoff exponencial y cooldown configurable.
- Deteccion explicita de 202/403/429/anomaly/captcha/0-resultados.
- Cache SQLite, reanudacion por pagina y deduplicacion por URL.
- Fallbacks: endpoint lite, libreria ddgs y Mojeek (opcional).
- Export a JSONL, CSV y Markdown.

Uso:
  python ddg_research.py doctor
  python ddg_research.py import-json /ruta/resultados.json "consulta"
  python ddg_research.py search "consulta" --pages 72 --start 63 --delay 7
  python ddg_research.py status
  python ddg_research.py export "consulta" --format markdown --out Data/ddg.md
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import random
import re
import sqlite3
import sys
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator
from urllib.parse import unquote, urlencode

from bs4 import BeautifulSoup
from curl_cffi import requests as creq

BASE = Path(__file__).resolve().parents[1]
DEFAULT_DB = BASE / "cache" / "ddg.sqlite"
DEFAULT_OUT = BASE.parent / "Data" / "ddg_results"

BLOCK_MARKERS = (
    "anomaly",
    "if this persists",
    "captcha",
    "unusual traffic",
    "verify you are",
    "challenge",
)
NO_RESULT_MARKERS = (
    "no results",
    "no results found",
    "no se encontraron resultados",
    "sin resultados",
)


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def qhash(query: str) -> str:
    return hashlib.sha256(query.strip().lower().encode("utf-8")).hexdigest()[:16]


def clean_url(href: str) -> str:
    """Decodifica los redirects uddg de DuckDuckGo."""
    if not href:
        return ""
    if "uddg=" in href:
        part = href.split("uddg=", 1)[1].split("&", 1)[0]
        return unquote(part)
    return href


def fq(url: str, base: str = "https://duckduckgo.com") -> str:
    if url.startswith("//"):
        return "https:" + url
    if url.startswith("/"):
        return base + url
    return url


# --------------------------------------------------------------------------- #
# Base de datos / cache
# --------------------------------------------------------------------------- #
@contextmanager
def db_conn(path: Path) -> Iterator[sqlite3.Connection]:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS runs (
            qhash TEXT PRIMARY KEY,
            query TEXT NOT NULL,
            vqd TEXT,
            created_at TEXT,
            updated_at TEXT,
            last_page INTEGER DEFAULT 0,
            status TEXT DEFAULT 'idle',
            note TEXT DEFAULT ''
        );
        CREATE TABLE IF NOT EXISTS pages (
            qhash TEXT NOT NULL,
            page INTEGER NOT NULL,
            status_code INTEGER,
            fetched_at TEXT,
            result_count INTEGER DEFAULT 0,
            new_count INTEGER DEFAULT 0,
            blocked INTEGER DEFAULT 0,
            engine TEXT DEFAULT 'ddg',
            note TEXT DEFAULT '',
            PRIMARY KEY (qhash, page)
        );
        CREATE TABLE IF NOT EXISTS results (
            qhash TEXT NOT NULL,
            url TEXT NOT NULL,
            page INTEGER NOT NULL,
            position INTEGER NOT NULL,
            title TEXT,
            snippet TEXT,
            engine TEXT DEFAULT 'ddg',
            first_seen TEXT,
            PRIMARY KEY (qhash, url)
        );
        CREATE INDEX IF NOT EXISTS idx_results_page ON results(qhash, page);
        """
    )


def ensure_run(conn: sqlite3.Connection, query: str) -> str:
    h = qhash(query)
    conn.execute(
        "INSERT OR IGNORE INTO runs (qhash, query, created_at, updated_at) VALUES (?,?,?,?)",
        (h, query.strip(), utcnow(), utcnow()),
    )
    return h


def save_results(
    conn: sqlite3.Connection,
    h: str,
    page: int,
    items: list[dict[str, Any]],
    engine: str = "ddg",
) -> int:
    added = 0
    for pos, item in enumerate(items, 1):
        url = clean_url(item.get("url", ""))
        if not url:
            continue
        cur = conn.execute(
            """INSERT OR IGNORE INTO results
               (qhash, url, page, position, title, snippet, engine, first_seen)
               VALUES (?,?,?,?,?,?,?,?)""",
            (
                h,
                url,
                page,
                pos,
                item.get("title", "") or "",
                item.get("snippet", "") or "",
                engine,
                utcnow(),
            ),
        )
        added += cur.rowcount
    return added


def save_page(
    conn: sqlite3.Connection,
    h: str,
    page: int,
    *,
    status_code: int | None,
    result_count: int,
    new_count: int,
    blocked: bool,
    engine: str = "ddg",
    note: str = "",
) -> None:
    conn.execute(
        """INSERT OR REPLACE INTO pages
           (qhash, page, status_code, fetched_at, result_count, new_count,
            blocked, engine, note)
           VALUES (?,?,?,?,?,?,?,?,?)""",
        (
            h,
            page,
            status_code,
            utcnow(),
            result_count,
            new_count,
            1 if blocked else 0,
            engine,
            note,
        ),
    )
    conn.execute(
        """UPDATE runs SET last_page = MAX(last_page, ?), updated_at = ?, status = ?, note = ?
           WHERE qhash = ?""",
        (
            page if not blocked else page - 1,
            utcnow(),
            "blocked" if blocked else "ok",
            note,
            h,
        ),
    )


# --------------------------------------------------------------------------- #
# Cliente DDG
# --------------------------------------------------------------------------- #
class Blocked(Exception):
    def __init__(self, kind: str, status: int | None, detail: str = ""):
        self.kind = kind
        self.status = status
        self.detail = detail
        super().__init__(f"{kind} (HTTP {status}) {detail}".strip())


class DDGClient:
    def __init__(
        self,
        *,
        proxy: str | None = None,
        impersonate: str = "chrome",
        timeout: int = 35,
        min_delay: float = 6.0,
        max_delay: float = 10.0,
        backoff: float = 60.0,
        max_retries: int = 2,
        verbose: bool = True,
    ) -> None:
        self.impersonate = impersonate
        self.timeout = timeout
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.backoff = backoff
        self.max_retries = max_retries
        self.verbose = verbose
        self.block_count = 0
        self.session = creq.Session(impersonate=impersonate)
        self.session.headers.update(
            {
                "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
                "Referer": "https://duckduckgo.com/",
                "Origin": "https://duckduckgo.com",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            }
        )
        if proxy or os.environ.get("DDG_PROXY"):
            p = proxy or os.environ["DDG_PROXY"]
            self.session.proxies = {"http": p, "https": p}

    def log(self, *a: Any) -> None:
        if self.verbose:
            print(*a, flush=True)

    def pause(self) -> None:
        d = random.uniform(self.min_delay, self.max_delay)
        self.log(f"  pausa {d:.1f}s")
        time.sleep(d)

    def warmup(self) -> None:
        """Calienta cookies __ddg1_/__ddg2_ en la misma sesion."""
        self.session.get("https://duckduckgo.com/", timeout=self.timeout)
        time.sleep(random.uniform(1.5, 3.0))

    @staticmethod
    def detect_block(status: int | None, text: str) -> Blocked | None:
        low = (text or "").lower()
        if status == 202:
            return Blocked("anomaly_202", status)
        if status == 429:
            return Blocked("rate_429", status)
        if status == 403:
            return Blocked("forbidden_403", status)
        # "anomaly" aparece a veces en scripts de paginas validas: solo cuenta
        # si ademas aparece el texto de la pagina de anomalia real.
        hard = ("if this persists", "unusual traffic", "verify you are not a robot")
        if any(m in low for m in hard):
            return Blocked("anomaly_page", status)
        if "captcha" in low and "result__a" not in low and "result-link" not in low:
            return Blocked("captcha", status)
        return None

    def _get(self, url: str, params: dict[str, Any]) -> Any:
        return self.session.get(url, params=params, timeout=self.timeout, allow_redirects=True)

    def _post(self, url: str, data: dict[str, Any]) -> Any:
        return self.session.post(url, data=data, timeout=self.timeout, allow_redirects=True)

    def get_vqd(self, query: str, conn: sqlite3.Connection | None = None, h: str = "") -> str:
        if conn and h:
            row = conn.execute("SELECT vqd FROM runs WHERE qhash=?", (h,)).fetchone()
            if row and row["vqd"]:
                return row["vqd"]
        r = self._get("https://html.duckduckgo.com/html/", {"q": query})
        blocked = self.detect_block(r.status_code, r.text)
        if blocked:
            raise blocked
        soup = BeautifulSoup(r.text or "", "lxml")
        vqd = None
        for form in soup.find_all("form"):
            inp = form.find("input", {"name": "vqd"})
            if inp and inp.get("value"):
                vqd = inp["value"]
                break
        if not vqd:
            raise RuntimeError("No se pudo extraer vqd del HTML de DuckDuckGo")
        if conn and h:
            conn.execute("UPDATE runs SET vqd=? WHERE qhash=?", (vqd, h))
        return vqd

    @staticmethod
    def parse_html(html: str, base: str = "https://duckduckgo.com") -> list[dict[str, str]]:
        soup = BeautifulSoup(html or "", "lxml")
        items: list[dict[str, str]] = []
        for res in soup.select(".result"):
            a = res.select_one("a.result__a")
            if not a:
                continue
            sn = res.select_one(".result__snippet")
            items.append(
                {
                    "title": a.get_text(" ", strip=True),
                    "url": clean_url(fq(a.get("href", ""), base)),
                    "snippet": sn.get_text(" ", strip=True) if sn else "",
                }
            )
        # Fallback para lite (a.result-link)
        if not items:
            for a in soup.select("a.result-link"):
                href = clean_url(fq(a.get("href", ""), base))
                row = a.find_parent("tr")
                sn = row.select_one("td.result-snippet") if row else None
                items.append(
                    {
                        "title": a.get_text(" ", strip=True),
                        "url": href,
                        "snippet": sn.get_text(" ", strip=True) if sn else "",
                    }
                )
        return items

    def fetch(self, query: str, page: int, vqd: str) -> tuple[Any, list[dict[str, str]]]:
        """Devuelve (response, resultados). page=1 usa POST; las demas GET paginado."""
        s = (page - 1) * 10
        if page == 1:
            r = self._post(
                "https://html.duckduckgo.com/html/",
                {"q": query, "kl": "wt-wt"},
            )
        else:
            r = self._get(
                "https://html.duckduckgo.com/html/",
                {
                    "q": query,
                    "s": str(s),
                    "v": "l",
                    "o": "json",
                    "dc": str(s + 1),
                    "api": "d.js",
                    "vqd": vqd,
                    "kl": "wt-wt",
                },
            )
        blocked = self.detect_block(r.status_code, r.text)
        if blocked:
            raise blocked
        items = self.parse_html(r.text or "")
        low = (r.text or "").lower()
        if not items and any(m in low for m in NO_RESULT_MARKERS):
            return r, []
        return r, items

    def fetch_lite(self, query: str, page: int, vqd: str) -> list[dict[str, str]]:
        """Fallback: endpoint lite por POST."""
        s = (page - 1) * 10
        r = self._post(
            "https://lite.duckduckgo.com/lite/",
            {
                "q": query,
                "s": str(s),
                "v": "l",
                "o": "json",
                "dc": str(s + 1),
                "api": "d.js",
                "vqd": vqd,
                "kl": "wt-wt",
            },
        )
        blocked = self.detect_block(r.status_code, r.text)
        if blocked:
            raise blocked
        return self.parse_html(r.text or "", "https://lite.duckduckgo.com")

    def fetch_ddgs(self, query: str, page: int) -> list[dict[str, str]]:
        """Fallback: libreria ddgs (gestiona vqd/headers y otros backends)."""
        from ddgs import DDGS

        with DDGS(timeout=self.timeout) as d:
            raw = d.text(query, region="wt-wt", max_results=10, page=page)
        return [
            {
                "title": x.get("title", ""),
                "url": x.get("href", "") or x.get("url", ""),
                "snippet": x.get("body", "") or x.get("snippet", ""),
            }
            for x in raw
        ]

    def fetch_mojeek(self, query: str, page: int) -> list[dict[str, str]]:
        """Fallback: Mojeek, casi no bloquea."""
        r = self.session.get(
            "https://www.mojeek.com/search",
            params={"q": query, "s": (page - 1) * 10},
            timeout=self.timeout,
        )
        soup = BeautifulSoup(r.text or "", "lxml")
        out: list[dict[str, str]] = []
        for li in soup.select("li.result, .results-standard li"):
            a = li.select_one("a.ob")
            if not a:
                continue
            sn = li.select_one("p.s")
            out.append(
                {
                    "title": a.get_text(" ", strip=True),
                    "url": fq(a.get("href", ""), "https://www.mojeek.com"),
                    "snippet": sn.get_text(" ", strip=True) if sn else "",
                }
            )
        return out


# --------------------------------------------------------------------------- #
# Comandos
# --------------------------------------------------------------------------- #
def cmd_doctor(args: argparse.Namespace) -> int:
    client = DDGClient(
        proxy=args.proxy,
        min_delay=args.delay,
        max_delay=args.delay + 2,
        timeout=args.timeout,
        verbose=True,
    )
    print(f"impersonate : {client.impersonate}")
    print(f"proxy       : {args.proxy or os.environ.get('DDG_PROXY') or 'ninguno'}")
    print(f"ventana     : {args.delay}s")
    try:
        client.warmup()
        r = client._get("https://html.duckduckgo.com/html/", {"q": args.query})
        blocked = client.detect_block(r.status_code, r.text)
        vqd = None
        soup = BeautifulSoup(r.text or "", "lxml")
        for f in soup.find_all("form"):
            inp = f.find("input", {"name": "vqd"})
            if inp and inp.get("value"):
                vqd = inp["value"]
                break
        print(f"HTTP        : {r.status_code}")
        print(f"bloqueo     : {blocked.kind if blocked else 'no'}")
        print(f"vqd         : {vqd}")
        print(f"resultados  : {len(client.parse_html(r.text or ''))}")
        print(f"cookies     : {list(client.session.cookies.keys())}")
        return 0 if not blocked else 2
    except Exception as e:
        print(f"ERROR: {e}")
        return 3


def cmd_import_json(args: argparse.Namespace) -> int:
    rows = json.loads(Path(args.path).read_text(encoding="utf-8"))
    with db_conn(args.db) as conn:
        init_db(conn)
        h = ensure_run(conn, args.query)
        pages: dict[int, list[dict[str, str]]] = {}
        for row in rows:
            pages.setdefault(int(row.get("page", 1)), []).append(row)
        for page, items in sorted(pages.items()):
            added = save_results(conn, h, page, items)
            save_page(
                conn,
                h,
                page,
                status_code=200,
                result_count=len(items),
                new_count=added,
                blocked=False,
                note="importado desde JSON",
            )
        total = conn.execute("SELECT COUNT(*) FROM results WHERE qhash=?", (h,)).fetchone()[0]
        print(f"Importados {len(rows)} registros / {total} unicos en {args.db}")
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    with db_conn(args.db) as conn:
        init_db(conn)
        h = ensure_run(conn, args.query)
        row = conn.execute("SELECT * FROM runs WHERE qhash=?", (h,)).fetchone()
        vqd = row["vqd"] if row and row["vqd"] else ""
        last = row["last_page"] if row else 0

        client = DDGClient(
            proxy=args.proxy,
            impersonate=args.impersonate,
            timeout=args.timeout,
            min_delay=args.delay,
            max_delay=args.delay + args.jitter,
            backoff=args.backoff,
            max_retries=args.max_retries,
            verbose=not args.quiet,
        )
        client.warmup()
        if not vqd:
            try:
                vqd = client.get_vqd(args.query, conn, h)
                client.log(f"vqd={vqd}")
            except Exception as e:
                print(f"No se pudo obtener vqd: {e}", file=sys.stderr)
                return 3

        start = args.start if args.start is not None else last + 1
        end = args.pages
        if end is None:
            end = start + args.count - 1

        print(f"consulta : {args.query}")
        print(f"rango    : paginas {start}-{end} (ultima guardada: {last})")
        print(f"ritmo    : {args.delay}-{args.delay + args.jitter}s, backoff {args.backoff}s")

        for page in range(start, end + 1):
            cached = conn.execute(
                "SELECT 1 FROM pages WHERE qhash=? AND page=? AND blocked=0", (h, page)
            ).fetchone()
            if cached and not args.refresh:
                client.log(f"P{page:02d} ya en cache, omito")
                continue

            items: list[dict[str, str]] = []
            engine = "ddg"
            note = ""
            status: int | None = None
            blocked = False
            client.pause()

            for attempt in range(1, args.max_retries + 2):
                try:
                    r, items = client.fetch(args.query, page, vqd)
                    status = r.status_code
                    break
                except Blocked as b:
                    client.block_count += 1
                    note = f"{b.kind} intento {attempt}"
                    client.log(f"P{page:02d} BLOQUEADO: {b}")
                    if attempt <= args.max_retries:
                        wait = args.backoff * (2 ** (attempt - 1)) + random.uniform(0, 15)
                        client.log(f"  cooldown {wait:.0f}s (intento {attempt}/{args.max_retries})")
                        time.sleep(wait)
                        try:
                            client.warmup()
                            vqd = client.get_vqd(args.query, conn, h)
                        except Exception as e:
                            client.log(f"  warmup fallido: {e}")
                    else:
                        blocked = True
                except Exception as e:
                    note = f"error: {e}"
                    client.log(f"P{page:02d} ERROR: {e}")
                    if attempt <= args.max_retries:
                        time.sleep(args.backoff * (2 ** (attempt - 1)))
                    else:
                        blocked = True

            if not blocked and not items and args.fallback:
                client.log(f"P{page:02d} sin resultados DDG, probando fallbacks")
                for name, fn in (
                    ("ddg-lite", lambda: client.fetch_lite(args.query, page, vqd)),
                    ("ddgs", lambda: client.fetch_ddgs(args.query, page)),
                    ("mojeek", lambda: client.fetch_mojeek(args.query, page)),
                ):
                    try:
                        items = fn()
                        if items:
                            engine = name
                            note = f"fallback {name}"
                            status = 200
                            break
                    except Exception as e:
                        client.log(f"  fallback {name} fallo: {e}")

            added = save_results(conn, h, page, items, engine)
            save_page(
                conn,
                h,
                page,
                status_code=status,
                result_count=len(items),
                new_count=added,
                blocked=blocked,
                engine=engine,
                note=note,
            )
            client.log(
                f"P{page:02d} {engine} status={status} resultados={len(items)} "
                f"nuevos={added} nota={note or 'ok'}"
            )

            if blocked:
                print(
                    "\nBloqueo persistente: estado guardado. "
                    "Reanuda mas tarde con: "
                    f'python {Path(__file__).name} search "{args.query}" --start {page}',
                    file=sys.stderr,
                )
                return 2
            if not items and page > 1:
                print(f"P{page} sin resultados: fin del indice o limite silencioso.", flush=True)
                break

        print("Listo.")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    with db_conn(args.db) as conn:
        init_db(conn)
        for r in conn.execute("SELECT * FROM runs ORDER BY updated_at DESC"):
            n = conn.execute(
                "SELECT COUNT(*) FROM results WHERE qhash=?", (r["qhash"],)
            ).fetchone()[0]
            pages = conn.execute(
                "SELECT COUNT(*) FROM pages WHERE qhash=? AND blocked=0", (r["qhash"],)
            ).fetchone()[0]
            print(
                f"{r['qhash']} | {r['status']:7} | paginas={pages:3} | urls={n:4} | "
                f"last={r['last_page']:3} | {r['query'][:70]}"
            )
    return 0


def cmd_export(args: argparse.Namespace) -> int:
    h = qhash(args.query)
    with db_conn(args.db) as conn:
        init_db(conn)
        rows = conn.execute(
            "SELECT page, position, title, url, snippet, engine FROM results "
            "WHERE qhash=? ORDER BY page, position",
            (h,),
        ).fetchall()
    if not rows:
        print("No hay resultados para esa consulta.", file=sys.stderr)
        return 1
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    if args.format == "jsonl":
        out.write_text(
            "\n".join(json.dumps(dict(r), ensure_ascii=False) for r in rows) + "\n",
            encoding="utf-8",
        )
    elif args.format == "csv":
        with out.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["page", "position", "title", "url", "snippet", "engine"])
            w.writeheader()
            w.writerows([dict(r) for r in rows])
    else:
        lines = [f"# Resultados DDG: {args.query}", "", f"Total: {len(rows)} URLs", ""]
        last = None
        for r in rows:
            if r["page"] != last:
                lines += ["", f"## Pagina {r['page']}", ""]
                last = r["page"]
            lines.append(f"- **{r['title']}** — {r['url']}")
            if r["snippet"]:
                lines.append(f"  - {r['snippet'][:220]}")
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Exportados {len(rows)} resultados a {out}")
    return 0


def norm_title(s: str) -> str:
    s = (s or "").lower()
    s = re.split(r"\s+[-–—|]\s+", s)[0]
    s = re.sub(r"\.(pdf|doc|docx|html?)$", "", s)
    s = re.sub(r"[^a-z0-9áéíóúñü ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    stop = {"de", "del", "la", "el", "los", "las", "un", "una", "en", "y", "y", "para", "por", "con", "al", "su", "sus"}
    words = [w for w in s.split() if w not in stop]
    return " ".join(words)[:90]


def norm_url(url: str) -> tuple[str, str]:
    u = (url or "").strip().lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    u = re.sub(r"[?#].*$", "", u)
    u = re.sub(r"/+$", "", u)
    parts = u.split("/")
    host = parts[0] if parts else ""
    path = "/".join(parts[1:])
    return host, path


def is_noise(title: str, url: str) -> bool:
    t = (title or "").lower()
    h, p = norm_url(url)
    job_markers = (
        "linkedin.com/jobs", "occ.com.mx/empleos", "indeed.com", "infojobs",
        "trabajosdiarios", "bumeran.com.ar/blog/mercado-laboral", "porsche.com/spain/aboutporsche/jobs",
    )
    howto_markers = (
        "wikipedia.org", "clubensayos.com", "studocu.com", "scribd.com",
        "buenastareas.com", "docsity.com", "1library.co", "coursehero.com",
        "tesismaestro.com", "expertouniversitario.es", "aprobare.es", "ejemplos.co",
        "wikihow", "questionpro.com/blog", "hubspot.es", "concepto.de", "lifeder",
        "ejemplos.co", "deunatesis", "hacertutesis", "tecnicasdeestudio", "clientify.com/blog",
        "neoattack.com/blog", "infoautonomos", "empresaactual.com", "promonegocios.net",
        "aprendizaje.diaonia", "riosubterraneo", "blog.getdarwin.ai", "t-mapp.com/post",
        "jaimerodriguez.mx", "unprofesor.com", "owl.excelsior.edu", "educaweb.com",
        "centro de estudio", "guia completa", "paso a paso", "qué es un trabajo",
        "cómo redactar", "cómo hacer", "ejemplos de", "plantillas", "10 mejores",
        "ventajas y desventajas", "tipos de investigación",
    )
    media_markers = (
        "youtube.com", "tiktok", "facebook.com", "reddit.com", "prezi.com",
        "slideshare.net", "pinterest", "msn.com", "telecinco", "elmundo.es",
        "elperiodico.com", "abc.es", "lavanguardia.com", "expansion.com", "eleconomista.es",
        "cincodias.elpais.com", "motor.elpais.com", "elpais.com", "infobae.com",
        "ambito.com", "noticias.yahoo.com", "marketscreener.com", "businessinsider.es",
        "vozdegalicia", "diariobajocinca", "elcorreo.com", "publico.es", "20minutos.es",
        "lavoz", "eldiario.es", "rtve.es", "dw.com", "lasexta", "okdiario",
        "meganoticias", "guijuelonoticias", "diariosigloxxi", "elconfidencial",
        "elconfidencialdigital", "elespanol.com", "infobae", "noticiasdenavarra",
        "elperiodicodearagon", "lavanguardia", "motor16.com", "cocheglobal.com",
        "todosobreautos.com", "xataka.com", "motor.es", "autofacil.es", "autonocion",
        "actualidadmotor", "europacoche.com", "motorpasion", "theconversation.com",
        "cnn", "nationalgeographic", "historia.nationalgeographic", "historiaybiografias",
        "tecnologia-lcp.orgfree", "libroazul", "guiaebc", "mercadolibre", "autocasion",
        "kavak.com", "carroya", "tork.news", "advancedfleetmanagement", "globalautoinsight",
        "empresas10.com", "worldwidemobility.io/blog", "institutocoordenadas.com",
        "infor.com/latam/blog", "mutatio.es/publicaciones", "zaguan.unizar.es/record/118532",
    )
    if any(m in h or m in p or m in t for m in job_markers):
        return True
    if any(m in h or m in p for m in howto_markers if "." in m or "/" in m):
        return True
    if any(m in t for m in howto_markers if " " in m or m.startswith("10 ")):
        return True
    if any(m in h or m in p for m in media_markers if "." in m or "/" in m):
        return True
    return False


AUTO_WORDS = (
    "automovil", "automóvil", "automotriz", "automotrí", "automocion", "automoción",
    "vehiculo", "vehículo", "carro", "coche", "coches", "auto ", "autos ",
    "moto", "movilidad", "transporte", "parque automotor", "concesionario",
    "repuesto", "neumatico", "neumático", "chasis", "matriculacion", "matriculación",
)
RESEARCH_WORDS = (
    "tesis", "tfg", "tfm", "trabajo final", "trabajo de investigaci", "trabajo de grado",
    "investigaci n de mercado", "investigación de mercado", "estudio de mercado",
    "estudio del mercado", "an lisis del sector", "análisis del sector",
    "art culo", "artículo", "paper", "informe", "report", "survey", "study",
    "análisis", "analisis", "mercado", "industria", "sector", "panorámica",
)


def is_research(title: str, url: str, snippet: str = "") -> bool:
    """Solo trabajos investigativos: titulo automotriz + senal de trabajo academico."""
    t = (title or "").lower()
    full = ((title or "") + " " + (snippet or "")).lower()
    h, p = norm_url(url)
    if not any(w in full for w in AUTO_WORDS):
        return False
    strong = (
        "tesis", "tfg", "tfm", "trabajo final", "trabajo de investigaci",
        "trabajo de grado", "investigaci n de mercado", "investigación de mercado",
        "estudio de mercado", "estudio del mercado", "art culo", "artículo",
        "paper", "panor mica", "panorámica", "an lisis emp rico", "análisis empírico",
        "estudio emp rico", "estudio empírico", "disertaci n", "disertación",
        "monograf a", "monografía", "informe", "informe de", "an lisis del sector",
        "análisis del sector", "an lisis sectorial", "análisis sectorial",
        "estudio de", "estudio sobre", "investigaci n de", "investigación de",
        "panorama", "revisi n", "revisión", "inteligencia de negocios",
        "comportamiento del consumidor", "cadena de valor", "oligopolio",
        "ventaja comparativa", "estrategia de mercadotecnia", "plan de negocios",
    )
    if not any(w in t for w in strong):
        return False
    academic_hosts = (
        ".edu", ".gob.", ".ac.cr", ".edu.ec", ".edu.ni", ".edu.pe", ".edu.mx",
        ".gob.mx", "researchgate.net", "academia.edu", "dialnet.unirioja.es",
        "scielo.org", "scielo.sld.cu", "scielo.cl", "redalyc.org", "sciencedirect",
        "elsevier.es", "springer", "mdpi.com", "emerald", "tandfonline", "sagepub",
        "repositorio", "dspace", "zaguan", "riunet", "uvadoc", "bibdigital",
        "tesis", "tfg", "master", "universidad", "unam.mx", "ucp.edu.pe", "pucp.edu.pe",
        "puce.edu.ec", "unan.edu.ni", "utpl.edu.ec", "uide.edu.ec", "urjc.es", "ual.es",
        "comillas.edu", "upm.es", "upv.es", "unizar.es", "uchile.cl", "uminho",
        "icex.es", "mintur.gob.es", "mincotur.gob.es", "anfac.com", "sernauto.es",
        "banrep.gov.co", "banxico.org.mx", "undp.org", "ilo.org", "oecd.org",
        "worldbank.org", "iadb.org", "github.com",
    )
    if any(m in h for m in academic_hosts):
        return True
    # Fuera de dominios academicos, solo se aceptan trabajos explicitos.
    return any(w in t for w in ("tesis", "tfg", "tfm", "trabajo final", "trabajo de investigaci", "trabajo de grado"))


def cmd_analyze(args: argparse.Namespace) -> int:
    """Deduplica, descarta ruido y localiza la racha de 10 paginas sin nada util."""
    h = qhash(args.query)
    with db_conn(args.db) as conn:
        init_db(conn)
        rows = conn.execute(
            "SELECT page, position, title, url, snippet, engine FROM results "
            "WHERE qhash=? ORDER BY page, position",
            (h,),
        ).fetchall()

    seen_titles: dict[str, tuple[int, str]] = {}
    seen_paths: dict[tuple[str, str], tuple[int, str]] = {}
    seen_prefix: dict[str, tuple[int, str]] = {}
    seen_hosts: set[str] = set()
    per_page: dict[int, dict[str, int]] = {}
    useful_items: list[dict[str, Any]] = []

    for r in rows:
        page = int(r["page"])
        title = r["title"] or ""
        url = r["url"] or ""
        d = per_page.setdefault(page, {"total": 0, "noise": 0, "dup": 0, "useful": 0})
        d["total"] += 1

        snippet = r["snippet"] or ""
        if is_noise(title, url):
            d["noise"] += 1
            continue
        if not is_research(title, url, snippet):
            d["noise"] += 1
            continue

        nt = norm_title(title)
        host, path = norm_url(url)
        prefix = re.sub(r"[^a-z0-9]+", "", nt)[:45]
        dup = False
        # Un resultado ya visto, su mirror (otro dominio) o una subpagina
        # de un resultado principal deja de contar como util.
        if nt and nt in seen_titles:
            dup = True
        elif (host, path[:60]) in seen_paths:
            dup = True
        elif prefix and prefix in seen_prefix and len(prefix) > 18:
            dup = True
        elif host in seen_hosts:
            dup = True
        if dup:
            d["dup"] += 1
            continue

        if nt:
            seen_titles[nt] = (page, title)
        if path:
            seen_paths[(host, path[:60])] = (page, title)
        if prefix:
            seen_prefix[prefix] = (page, title)
        if host:
            seen_hosts.add(host)
        d["useful"] += 1
        useful_items.append({"page": page, "title": title, "url": url, "snippet": r["snippet"] or ""})

    pages = sorted(per_page)
    # primera racha de N paginas consecutivas sin utiles
    streak: list[int] = []
    stop_page: int | None = None
    for p in pages:
        if per_page[p]["useful"] == 0:
            streak.append(p)
            if len(streak) >= args.streak:
                stop_page = p
                break
        else:
            streak = []

    lines = [
        f"# Analisis de resultados DDG: {args.query}",
        "",
        f"- Resultados procesados: {len(rows)}",
        f"- Paginas: {len(pages)}",
        f"- Utiles (unicos, no ruido, no duplicados): {len(useful_items)}",
        f"- Regla: {args.streak} paginas consecutivas sin ningun enlace util",
        "",
    ]
    if stop_page:
        first = streak[-args.streak]
        lines += [
            f"## Parada: pagina {stop_page}",
            "",
            f"Racha paginas {first}-{stop_page}: {len(streak)} paginas consecutivas sin enlaces utiles.",
            "Los resultados de esas paginas son repetidos, mirrors o subpaginas de items ya vistos, o ruido/no investigacion.",
            "",
        ]
    else:
        lines += [
            "## Sin parada",
            "",
            f"No se encontro una racha de {args.streak} paginas sin enlaces utiles en las paginas analizadas.",
            "",
        ]

    lines += ["## Desglose por pagina", "", "| Pagina | Total | Utiles | Duplicados/mirror | Ruido |", "|---:|---:|---:|---:|---:|"]
    for p in pages:
        d = per_page[p]
        lines.append(f"| {p} | {d['total']} | {d['useful']} | {d['dup']} | {d['noise']} |")

    lines += ["", "## Enlaces utiles (unicos)", ""]
    for it in useful_items:
        lines.append(f"- P{it['page']:02d} **{it['title']}** — {it['url']}")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Analisis guardado en {out}")
    if stop_page:
        print(f"STOP en pagina {stop_page} (racha {streak[-args.streak]}-{stop_page})")
    else:
        print("Sin racha de parada")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--db", type=Path, default=DEFAULT_DB, help="SQLite de cache")
    sub = p.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("doctor", help="Diagnosticar bloqueo")
    d.add_argument("query", nargs="?", default="mercado automovilistico trabajos investigativos")
    d.add_argument("--proxy")
    d.add_argument("--delay", type=float, default=3.0)
    d.add_argument("--timeout", type=int, default=35)
    d.set_defaults(func=cmd_doctor)

    i = sub.add_parser("import-json", help="Importar resultados de la sesion anterior")
    i.add_argument("path", type=Path)
    i.add_argument("query")
    i.set_defaults(func=cmd_import_json)

    s = sub.add_parser("search", help="Buscar paginas con ritmo seguro y reanudacion")
    s.add_argument("query")
    s.add_argument("--start", type=int, help="Primera pagina (por defecto, ultima+1)")
    s.add_argument("--pages", type=int, help="Ultima pagina absoluta")
    s.add_argument("--count", type=int, default=10, help="Numero de paginas si no se da --pages")
    s.add_argument("--delay", type=float, default=6.0)
    s.add_argument("--jitter", type=float, default=3.0)
    s.add_argument("--backoff", type=float, default=60.0)
    s.add_argument("--max-retries", type=int, default=2)
    s.add_argument("--timeout", type=int, default=35)
    s.add_argument("--impersonate", default="chrome")
    s.add_argument("--proxy")
    s.add_argument("--no-fallback", dest="fallback", action="store_false")
    s.add_argument("--refresh", action="store_true")
    s.add_argument("--quiet", action="store_true")
    s.set_defaults(func=cmd_search, fallback=True)

    st = sub.add_parser("status", help="Ver estado de la cache")
    st.set_defaults(func=cmd_status)

    a = sub.add_parser("analyze", help="Deduplicar y localizar 10 paginas sin enlaces utiles")
    a.add_argument("query")
    a.add_argument("--streak", type=int, default=10)
    a.add_argument("--out", type=Path, default=DEFAULT_OUT.parent / "ddg_analisis.md")
    a.set_defaults(func=cmd_analyze)

    e = sub.add_parser("export", help="Exportar resultados")
    e.add_argument("query")
    e.add_argument("--format", choices=["jsonl", "csv", "markdown"], default="markdown")
    e.add_argument("--out", type=Path, required=True)
    e.set_defaults(func=cmd_export)
    return p


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

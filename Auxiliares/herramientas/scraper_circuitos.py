#!/usr/bin/env python3
"""Captura mensajes del canal público de la Empresa Eléctrica de La Habana.

Guarda un histórico deduplicado por mensaje y el último estado conocido por circuito.
No modifica otras bases del proyecto. Uso:

    python3 scraper_circuitos.py --pages 3
    python3 scraper_circuitos.py --pages 1 --resumen
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
BASE = "https://t.me/s/EmpresaElectricaDeLaHabana"
MAPAS = ROOT / "Data/mapas"
CIRCUITOS = MAPAS / "circuitos"
DB = MAPAS / "circuitos_estado.sqlite"
ESTADO_HTTP = ROOT / "Data/_state/telegram_circuitos.json"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121 Safari/537.36"

RELEVANTES = re.compile(
    r"afectaci|afectad|d[eé]ficit|aver[ií]a|disparo|restablec|servicio|energiz|"
    r"incorporad|normaliz|abierto|cerrado|desconectad|rotaci|interrupci|"
    r"apag[oó]n|apagad|traspaso",
    re.I,
)
RESTAURACION = re.compile(r"restablec|normaliz|energiz|incorporad|con luz|sin afectaci", re.I)
AFECTACION = re.compile(r"afectaci|afectad|afecta|afect[oó]|d[eé]ficit|sin luz|interrupci|apag[oó]n|apagad|desconectad|aver[ií]a|disparo", re.I)


def circuitos_conocidos() -> list[str]:
    datos = json.loads((CIRCUITOS / "circuitos_habana.json").read_text(encoding="utf-8"))
    return sorted({str(x["circuito"]).strip().upper() for x in datos if x.get("circuito")})


def descargar(url: str, condicional: bool = True) -> tuple[str, bool]:
    """Descarga con ETag/Last-Modified; devuelve (html, sin_cambios)."""
    cabeceras = {"User-Agent": UA}
    if condicional and ESTADO_HTTP.exists():
        guardado = json.loads(ESTADO_HTTP.read_text(encoding="utf-8"))
        if guardado.get("etag"):
            cabeceras["If-None-Match"] = guardado["etag"]
        if guardado.get("last_modified"):
            cabeceras["If-Modified-Since"] = guardado["last_modified"]
    req = urllib.request.Request(url, headers=cabeceras)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
            validadores = None
            if condicional:
                validadores = {
                    "etag": r.headers.get("ETag", ""),
                    "last_modified": r.headers.get("Last-Modified", ""),
                }
            return html, False, validadores
    except urllib.error.HTTPError as e:
        if e.code == 304:
            return "", True, None
        raise


def inicializar(codes: list[str]) -> sqlite3.Connection:
    conn = sqlite3.connect(DB)
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS mensajes (
            id TEXT PRIMARY KEY, fecha_utc TEXT, fecha_local TEXT, circuito TEXT,
            estado TEXT, relevante INTEGER, texto TEXT, causa TEXT, capturado_utc TEXT
        );
        CREATE TABLE IF NOT EXISTS estado_circuito (
            circuito TEXT PRIMARY KEY, estado TEXT, fecha_utc TEXT, mensaje_id TEXT
        );
        CREATE TABLE IF NOT EXISTS capturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT, fecha_utc TEXT, paginas INTEGER,
            mensajes_vistos INTEGER, nuevos INTEGER
        );
        CREATE INDEX IF NOT EXISTS idx_mensajes_fecha ON mensajes(fecha_utc);
        """
    )
    for c in codes:
        conn.execute(
            "INSERT OR IGNORE INTO estado_circuito(circuito, estado) VALUES (?, 'sin dato')", (c,)
        )
    conn.commit()
    return conn


def analizar(mensaje: dict, codes: list[str]) -> tuple[list[str], str, str]:
    texto = mensaje["texto"] or ""
    if not RELEVANTES.search(texto):
        return [], "no relevante", ""
    upper = texto.upper()
    encontrados = [c for c in codes if re.search(r"\b" + re.escape(c) + r"\b", upper)]
    if RESTAURACION.search(texto) and AFECTACION.search(texto):
        estado = "mixto"
    elif RESTAURACION.search(texto):
        estado = "con luz"
    elif AFECTACION.search(texto):
        estado = "sin luz"
    else:
        estado = "sin dato"
    causa = ""
    mc = re.search(r"(por|debido a|causa)[:\s]+([^\n.]{3,80})", texto, re.I)
    if mc:
        causa = mc.group(2).strip()
    return encontrados, estado, causa


def guardar(conn: sqlite3.Connection, mensaje: dict, circuitos: list[str], estado: str, causa: str) -> int:
    try:
        conn.execute(
            "INSERT INTO mensajes VALUES (?,?,?,?,?,?,?,?,?)",
            (mensaje["id"], mensaje["fecha_utc"], mensaje["fecha_local"],
             ",".join(circuitos), estado, 1 if estado != "no relevante" else 0,
             mensaje["texto"], causa, datetime.now(timezone.utc).isoformat()),
        )
    except sqlite3.IntegrityError:
        return 0
    for c in circuitos:
        anterior = conn.execute(
            "SELECT fecha_utc FROM estado_circuito WHERE circuito=?", (c,)
        ).fetchone()
        if not anterior or not anterior[0] or anterior[0] <= mensaje["fecha_utc"]:
            conn.execute(
                "UPDATE estado_circuito SET estado=?, fecha_utc=?, mensaje_id=? WHERE circuito=?",
                (estado, mensaje["fecha_utc"], mensaje["id"], c),
            )
    return 1


def parsear_html(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    salida = []
    for node in soup.select("div.tgme_widget_message_wrap"):
        msg = node.select_one("div.tgme_widget_message")
        if not msg:
            continue
        post = msg.get("data-post", "")
        mid = post.rsplit("/", 1)[-1] if "/" in post else ""
        if not mid.isdigit():
            continue
        t = node.select_one("time")
        fecha = t.get("datetime", "") if t else ""
        if not fecha:
            continue
        cuerpo = node.select_one("div.tgme_widget_message_text, .js-message_text")
        texto = cuerpo.get_text("\n", strip=True) if cuerpo else ""
        local = datetime.fromisoformat(fecha.replace("Z", "+00:00")).astimezone(
            timezone(timedelta(hours=1))
        ).isoformat()
        salida.append({"id": mid, "fecha_utc": fecha, "fecha_local": local, "texto": texto})
    return salida


def resumen(conn: sqlite3.Connection) -> None:
    print("\n=== Estado actual de circuitos ===")
    for estado, n in conn.execute("select estado,count(*) from estado_circuito group by 1 order by 2 desc"):
        print(f"  {estado:12s} {n}")
    print("  total mensajes:", conn.execute("select count(*) from mensajes").fetchone()[0])
    print("  ultimo mensaje:", conn.execute("select max(fecha_utc) from mensajes").fetchone()[0])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pages", type=int, default=3)
    ap.add_argument("--before", type=str, default="")
    ap.add_argument("--delay", type=float, default=1.5)
    ap.add_argument("--resumen", action="store_true")
    args = ap.parse_args()

    codes = circuitos_conocidos()
    conn = inicializar(codes)
    vistos = nuevos = 0
    before = args.before
    validadores = None
    for pagina in range(1, args.pages + 1):
        url = BASE + (f"?before={before}" if before else "")
        html, sin_cambios, validadores = descargar(url, condicional=(not before))
        if sin_cambios:
            print("canal sin cambios (HTTP 304); se omite descarga")
            break
        mensajes = parsear_html(html)
        vistos += len(mensajes)
        for m in mensajes:
            circuitos, estado, causa = analizar(m, codes)
            nuevos += guardar(conn, m, circuitos, estado, causa)
        conn.commit()
        siguiente = re.search(r'data-before="(\d+)"', html)
        if not siguiente:
            break
        before = siguiente.group(1)
        if pagina < args.pages:
            time.sleep(args.delay)
    conn.execute(
        "INSERT INTO capturas(fecha_utc,paginas,mensajes_vistos,nuevos) VALUES (?,?,?,?)",
        (datetime.now(timezone.utc).isoformat(), pagina, vistos, nuevos),
    )
    conn.commit()
    # El validador HTTP solo avanza después de confirmar la escritura en SQLite.
    if validadores is not None:
        ESTADO_HTTP.parent.mkdir(parents=True, exist_ok=True)
        ESTADO_HTTP.write_text(json.dumps({
            **validadores,
            "ultima_descarga_utc": datetime.now(timezone.utc).isoformat(),
        }, indent=2), encoding="utf-8")
    print(f"captura: paginas={pagina} vistos={vistos} nuevos={nuevos} | BD={DB.name}")
    if args.resumen:
        resumen(conn)
    conn.close()


if __name__ == "__main__":
    main()

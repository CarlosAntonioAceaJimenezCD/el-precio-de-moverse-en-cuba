#!/usr/bin/env python3
"""Base SQLite compartida para datos de Telegram (canales + anuncios)."""

from __future__ import annotations

import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "Data/integraciones/telegram/telegram.sqlite"


def conectar() -> sqlite3.Connection:
    DB.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB, timeout=60, check_same_thread=False)
    c.execute("PRAGMA journal_mode=WAL")
    c.execute("PRAGMA busy_timeout=60000")
    return c


def init_db() -> None:
    c = conectar()
    c.executescript(
        """
        CREATE TABLE IF NOT EXISTS canales (
            usuario TEXT PRIMARY KEY,
            titulo TEXT,
            audiencia TEXT,
            mensajes_publicos INTEGER DEFAULT 0,
            es_automotriz INTEGER DEFAULT 0,
            es_relevante INTEGER DEFAULT 0,
            publico INTEGER DEFAULT 0,
            muestra TEXT,
            url TEXT,
            validado_utc TEXT
        );
        CREATE TABLE IF NOT EXISTS anuncios (
            id TEXT PRIMARY KEY,
            fuente TEXT,
            canal TEXT,
            id_mensaje INTEGER,
            fecha TEXT,
            url TEXT,
            texto TEXT,
            es_auto INTEGER DEFAULT 0,
            precio REAL,
            moneda TEXT,
            anio INTEGER,
            km INTEGER,
            recogido_utc TEXT
        );
        CREATE TABLE IF NOT EXISTS estado (
            clave TEXT PRIMARY KEY,
            valor TEXT,
            actualizado_utc TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_canales_auto ON canales(es_automotriz);
        CREATE INDEX IF NOT EXISTS idx_anuncios_canal ON anuncios(canal);
        """
    )
    c.commit()
    c.close()


def upsert_canal(fila: dict) -> None:
    init_db()
    c = conectar()
    c.execute(
        """INSERT OR REPLACE INTO canales
           (usuario,titulo,audiencia,mensajes_publicos,es_automotriz,es_relevante,
            publico,muestra,url,validado_utc)
           VALUES (?,?,?,?,?,?,?,?,?,?)""",
        (
            fila.get("usuario", ""), fila.get("titulo", ""), fila.get("audiencia", ""),
            int(fila.get("mensajes_publicos") or 0),
            int(bool(fila.get("es_automotriz"))),
            int(bool(fila.get("es_relevante"))),
            int(bool(fila.get("publico"))),
            fila.get("muestra", ""), fila.get("url", ""), fila.get("validado_utc", ""),
        ),
    )
    c.commit()
    c.close()


def upsert_anuncio(fila: dict) -> None:
    init_db()
    c = conectar()
    c.execute(
        """INSERT OR REPLACE INTO anuncios
           (id,fuente,canal,id_mensaje,fecha,url,texto,es_auto,precio,moneda,anio,km,recogido_utc)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (
            fila.get("id", ""), fila.get("fuente", "telegram"), fila.get("canal", ""),
            fila.get("id_mensaje"), fila.get("fecha", ""), fila.get("url", ""),
            fila.get("texto", ""), int(bool(fila.get("es_auto"))),
            fila.get("precio"), fila.get("moneda"), fila.get("anio"), fila.get("km"),
            fila.get("recogido_utc", ""),
        ),
    )
    c.commit()
    c.close()


def set_estado(clave: str, valor: str) -> None:
    from datetime import datetime, timezone

    init_db()
    c = conectar()
    c.execute(
        "INSERT OR REPLACE INTO estado VALUES (?,?,?)",
        (clave, valor, datetime.now(timezone.utc).isoformat(timespec="seconds")),
    )
    c.commit()
    c.close()


def resumen() -> dict:
    init_db()
    c = conectar()
    out = {
        "canales": c.execute("SELECT count(*) FROM canales").fetchone()[0],
        "canales_auto": c.execute("SELECT count(*) FROM canales WHERE es_automotriz=1").fetchone()[0],
        "anuncios": c.execute("SELECT count(*) FROM anuncios").fetchone()[0],
        "anuncios_auto": c.execute("SELECT count(*) FROM anuncios WHERE es_auto=1").fetchone()[0],
    }
    c.close()
    return out

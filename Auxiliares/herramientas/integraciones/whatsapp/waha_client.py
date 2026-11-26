#!/usr/bin/env python3
"""Cliente Python para WAHA (WhatsApp HTTP API) orientado a AutoDecide Habana.

Lee mensajes de chats/grupos de WhatsApp ya autorizados en una instancia WAHA
(auto-hospedada) y los guarda como JSONL con deduplicación por id de mensaje.

Variables de entorno:
    WAHA_URL      base de la API, por defecto http://localhost:3000
    WAHA_SESSION  nombre de sesión, por defecto "default"
    WAHA_API_KEY  cabecera X-Api-Key si la instancia la requiere
"""

from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

import httpx

RAIZ = Path(__file__).resolve().parents[4]
SALIDA = RAIZ / "Data" / "integraciones" / "whatsapp"
BASE = os.environ.get("WAHA_URL", "http://localhost:3000").rstrip("/")
SESSION = os.environ.get("WAHA_SESSION", "default")
HEADERS = {"Content-Type": "application/json"}
if os.environ.get("WAHA_API_KEY"):
    HEADERS["X-Api-Key"] = os.environ["WAHA_API_KEY"]

# Palabras clave para filtrar anuncios de vehículos sin tocar datos personales.
PATRON = re.compile(
    r"\b(vendo|se vende|carro|auto|coche|veh[ií]culo|moto|precio|USD|MLC|CUP)\b",
    re.IGNORECASE,
)


def client() -> httpx.Client:
    return httpx.Client(base_url=BASE, headers=HEADERS, timeout=30.0)


def sesiones() -> list[dict]:
    with client() as c:
        r = c.get("/api/sessions")
        r.raise_for_status()
        return r.json()


def chats() -> list[dict]:
    with client() as c:
        r = c.get(f"/api/{SESSION}/chats")
        r.raise_for_status()
        return r.json()


def mensajes(chat_id: str, limite: int = 100) -> list[dict]:
    with client() as c:
        r = c.get(f"/api/{SESSION}/chats/{chat_id}/messages", params={"limit": limite})
        r.raise_for_status()
        return r.json()


def extraer(m: dict, chat: dict) -> dict | None:
    texto = m.get("body") or m.get("text") or ""
    if not texto or not isinstance(texto, str):
        return None
    if not PATRON.search(texto):
        return None
    return {
        "id": m.get("id") or m.get("messageId"),
        "chat_id": chat.get("id"),
        "chat_name": chat.get("name"),
        "timestamp": m.get("timestamp"),
        "from": m.get("from"),
        "text": texto[:2000],
        "url": f"https://wa.me/{chat.get('id','').split('@')[0]}",
        "recogido_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "fuente": "waha",
    }


def guardar(filas: list[dict], destino: Path) -> tuple[int, int]:
    destino.parent.mkdir(parents=True, exist_ok=True)
    vistos: set[str] = set()
    if destino.is_file():
        for line in destino.read_text(encoding="utf-8").splitlines():
            try:
                vistos.add(json.loads(line)["id"])
            except (json.JSONDecodeError, KeyError):
                continue
    nuevos = 0
    with destino.open("a", encoding="utf-8") as fh:
        for fila in filas:
            key = fila.get("id")
            if not key or key in vistos:
                continue
            vistos.add(key)
            fh.write(json.dumps(fila, ensure_ascii=False) + "\n")
            nuevos += 1
    return nuevos, len(vistos)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chats", action="store_true", help="listar chats disponibles")
    ap.add_argument("--limite", type=int, default=100, help="mensajes por chat")
    ap.add_argument("--salida", type=Path, default=SALIDA / "anuncios.jsonl")
    args = ap.parse_args()

    try:
        if args.chats:
            for c in chats():
                print(f"{c.get('id')}\t{c.get('name')}")
            return
        todos: list[dict] = []
        for chat in chats():
            for m in mensajes(chat.get("id", ""), args.limite):
                fila = extraer(m, chat)
                if fila:
                    todos.append(fila)
        nuevos, total = guardar(todos, args.salida)
        print(f"Mensajes candidatos={len(todos)} nuevos={nuevos} total={total} -> {args.salida}")
    except httpx.HTTPError as exc:
        raise SystemExit(f"Error de WAHA ({BASE}): {exc}") from exc


if __name__ == "__main__":
    main()

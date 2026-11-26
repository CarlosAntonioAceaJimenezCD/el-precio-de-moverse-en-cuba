#!/usr/bin/env python3
"""Descubre canales de Telegram referentes al mercado cubano hasta 100.

Fuentes: tgden.com (búsquedas por término y tipo). Cada candidato se valida
con la vista pública t.me/s/<usuario> para obtener título, miembros, mensajes
y una muestra. Salida: Data/integraciones/telegram/canales_referencia.jsonl
"""

from __future__ import annotations

import json
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

from bs4 import BeautifulSoup
from curl_cffi import requests as creq

import telegram_db as tdb

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "Data/integraciones/telegram"
SALIDA = OUT / "canales_referencia.jsonl"
OBJETIVO = 100

CONSULTAS = [
    ("cuba", "channel"), ("cuba", "chat"),
    ("habana", "channel"), ("habana", "chat"),
    ("revolico", "channel"), ("revolico", "chat"),
    ("carros cuba", "channel"), ("carros cuba", "chat"),
    ("autos cuba", "channel"), ("autos cuba", "chat"),
    ("venta cuba", "channel"), ("venta cuba", "chat"),
    ("mercado cuba", "channel"), ("mercado cuba", "chat"),
    ("cubano", "channel"), ("compra venta cuba", "chat"),
    ("la habana", "channel"), ("la habana", "chat"),
    ("anuncios cuba", "channel"), ("anuncios cuba", "chat"),
    ("cuba mlc", "chat"), ("cuba usd", "chat"),
    ("revolico habana", "channel"), ("revolico habana", "chat"),
    ("cuba ventas", "chat"), ("cuba compras", "chat"),
]

RELEVANTE = re.compile(
    r"\b(cuba|cubano|cubana|habana|revolico|carros?|autos?|venta|mercado|"
    r"compra|tasa|eltoque|isla|emprendimiento)\b", re.I
)
AUTO = re.compile(r"\b(carros?|autos?|coches?|camionetas?|veh[ií]culos?|motos?|repuestos?)\b", re.I)
CUBA = re.compile(r"\b(cuba|cubano|cubana|habana|revolico|isla)\b", re.I)


def get(url: str, params: dict | None = None) -> str:
    r = creq.get(url, params=params, impersonate="chrome", timeout=25,
                 headers={"Accept-Language": "es-ES,es;q=0.9"})
    r.raise_for_status()
    return r.text


def candidatos() -> list[str]:
    vistos: set[str] = set()
    for q, tipo in CONSULTAS:
        try:
            html = get("https://tgden.com/en/search", {"q": q, "type": tipo})
        except Exception as exc:
            print(f"[busqueda] {q}/{tipo}: {exc}", flush=True)
            continue
        s = BeautifulSoup(html, "lxml")
        encontrados = []
        for a in s.select(f'a[href^="/en/{tipo}/"]'):
            user = a.get("href", "").rsplit("/", 1)[-1]
            if not user or "-" in user or len(user) > 40:
                continue
            if user not in vistos:
                vistos.add(user)
                encontrados.append(user)
        print(f"[busqueda] {q}/{tipo}: {len(encontrados)} nuevos", flush=True)
        time.sleep(0.3)
    return sorted(vistos)


def validar(usuario: str) -> dict:
    fila = {
        "usuario": usuario,
        "url": f"https://t.me/{usuario}",
        "validado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    try:
        html = get(f"https://t.me/s/{usuario}")
        s = BeautifulSoup(html, "lxml")
        titulo = s.select_one(".tgme_channel_info_header_title") or s.select_one(".tgme_page_title")
        contadores = s.select(".tgme_channel_info_counter")
        extra = contadores[0] if contadores else s.select_one(".tgme_page_extra")
        mensajes = s.select("div.tgme_widget_message")
        textos = [
            m.select_one(".tgme_widget_message_text").get_text(" ", strip=True)
            for m in mensajes if m.select_one(".tgme_widget_message_text")
        ]
        titulo_txt = titulo.get_text(" ", strip=True) if titulo else ""
        audiencia_txt = extra.get_text(" ", strip=True) if extra else ""
        fila.update({
            "titulo": titulo_txt,
            "audiencia": audiencia_txt,
            "mensajes_publicos": len(mensajes),
            "muestra": (textos[0][:200] if textos else ""),
            "es_automotriz": bool(AUTO.search(" ".join(textos) + " " + titulo_txt)),
            "es_relevante": bool(RELEVANTE.search(titulo_txt + " " + " ".join(textos))),
            "publico": len(mensajes) > 0,
        })
    except Exception as exc:
        fila.update({"titulo": "", "audiencia": "", "mensajes_publicos": 0,
                     "muestra": "", "es_automotriz": False, "es_relevante": False,
                     "publico": False, "error": str(exc)[:160]})
    return fila


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    usuarios = candidatos()
    print(f"Candidatos totales: {len(usuarios)}", flush=True)

    resultados: list[dict] = []
    with ThreadPoolExecutor(max_workers=6) as ex:
        futuros = {ex.submit(validar, u): u for u in usuarios}
        for i, fut in enumerate(as_completed(futuros), 1):
            fila = fut.result()
            resultados.append(fila)
            tdb.upsert_canal(fila)
            if i % 25 == 0:
                print(f"  validados {i}/{len(usuarios)}", flush=True)

    utiles = [
        f for f in resultados
        if (f["publico"] or f["es_relevante"])
        and CUBA.search((f["titulo"] or "") + " " + (f["muestra"] or ""))
    ]
    utiles.sort(key=lambda f: (f["es_automotriz"], f["mensajes_publicos"]), reverse=True)
    resultados = utiles
    if len(resultados) < OBJETIVO:
        print(f"AVISO: solo {len(resultados)} canales con contexto cubano (objetivo {OBJETIVO})", flush=True)

    with SALIDA.open("w", encoding="utf-8") as fh:
        for fila in resultados:
            fh.write(json.dumps(fila, ensure_ascii=False) + "\n")

    tdb.set_estado("canales_referencia", str(len(resultados)))
    print(f"Referencias guardadas: {len(resultados)} (objetivo {OBJETIVO})", flush=True)
    print(f"Automotrices: {sum(1 for f in resultados if f['es_automotriz'])}", flush=True)
    print(f"Con mensajes públicos: {sum(1 for f in resultados if f['publico'])}", flush=True)


if __name__ == "__main__":
    main()

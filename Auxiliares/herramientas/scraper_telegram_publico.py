#!/usr/bin/env python3
"""Scraper de canales públicos de Telegram sin credenciales MTProto.

Usa la vista pública `https://t.me/s/<canal>` y su paginación `?before=<id>`.
Solo lee mensajes públicos; no recopila nombres ni teléfonos (los redacta).

Salidas:
  Data/integraciones/telegram/anuncios.jsonl
  Data/integraciones/telegram/anuncios.csv
  Data/integraciones/telegram/estado.json

Variables:
  TELEGRAM_CHANNELS  canales separados por coma (sin @)
"""

from __future__ import annotations

import csv
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

from bs4 import BeautifulSoup
from curl_cffi import requests as creq

import telegram_db as tdb

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "Data/integraciones/telegram"
CANALES_POR_DEFECTO = ["goldenbullbusinessfamilycars", "Motos_Autos_Discover"]

# Canales cubanos encontrados en la búsqueda. La mayoría son de noticias o
# compra-venta general y no publican anuncios de autos; se dejan como catálogo.
CANALES_DESCUBIERTOS = [
    "Revolico_Cuba_Oficial",          # avisos/eventos, sin anuncios de autos
    "Ventas_Revolico_Holguin_Cuba",   # grupo, sin vista pública
    "revolico_baracoa",               # sin mensajes públicos
    "timbirichi_compra_y_venta_cuba", # sin vista pública
    "PiezasdeCarrosCU",               # repuestos, no vehículos
    "directoriocubano",               # noticias
    "eltoquecom",                     # noticias/tasas
    "coventcuba",                     # 7 suscriptores, sin anuncios
    "APublished",                     # mercado informal, sin anuncios
    "GEEKSCUBANS_PLUS",               # tecnología/compra-venta general
    "lachopivaraderooo",              # compra-venta general
]
BASE = "https://t.me/s/{canal}"

PATRON_AUTO = re.compile(
    r"\b(carro|auto|coche|camioneta|veh[uí]culo|sed[aá]n|suv|pickup|"
    r"toyota|hyundai|kia|chevrolet|ford|honda|nissan|mazda|audi|bmw|"
    r"mercedes|peugeot|fiat|renault|volkswagen|geely|changan|dongfeng)\b",
    re.I,
)
PATRON_PRECIO = re.compile(r"(\d{1,3}(?:[.,]\d{3})+|\d{3,6})\s*(USD|EUR|MLC|CUP)\b", re.I)
# Solo números con forma de teléfono cubano (7-8 dígitos, a veces +53),
# para no redactar kilómetros como "25500K".
PATRON_TEL = re.compile(r"(?:\+?53[\s\-]?)?\b[5-9]\d{2,3}[\s\-]?\d{4}\b")
PATRON_ANIO = re.compile(r"\b(19[5-9]\d|20[0-2]\d)\b")
PATRON_KM = re.compile(r"\b(\d{1,3}(?:[.,]\d{3})+|\d{4,6})\s*(?:km|kms)\b", re.I)


def redactar(texto: str) -> str:
    return PATRON_TEL.sub("[telefono]", texto or "")


def obtener(canal: str, before: str | None = None) -> str:
    url = BASE.format(canal=canal)
    params = {"before": before} if before else None
    r = creq.get(url, params=params, impersonate="chrome", timeout=25,
                 headers={"Accept-Language": "es-ES,es;q=0.9"})
    r.raise_for_status()
    return r.text


def parsear(html: str, canal: str) -> list[dict]:
    s = BeautifulSoup(html, "lxml")
    filas = []
    for nodo in s.select("div.tgme_widget_message"):
        post = nodo.get("data-post") or ""
        msg_id = post.rsplit("/", 1)[-1]
        if not msg_id.isdigit():
            continue
        caja = nodo.select_one(".tgme_widget_message_text")
        texto = redactar(caja.get_text(" ", strip=True) if caja else "")
        hora = nodo.select_one("time")
        fecha = hora.get("datetime") if hora else ""
        filas.append({
            "id": f"tg_{canal}_{msg_id}",
            "fuente": "telegram",
            "canal": canal,
            "id_mensaje": int(msg_id),
            "fecha": fecha,
            "url": f"https://t.me/{canal}/{msg_id}",
            "texto": texto,
            "es_auto": bool(PATRON_AUTO.search(texto)),
        })
    return filas


def extraer_campos(fila: dict) -> dict:
    texto = fila["texto"]
    precio = PATRON_PRECIO.search(texto)
    anio = PATRON_ANIO.search(texto)
    km = PATRON_KM.search(texto)
    fila["precio"] = float(precio.group(1).replace(".", "").replace(",", "")) if precio else None
    fila["moneda"] = precio.group(2).upper() if precio else None
    fila["anio"] = int(anio.group(1)) if anio else None
    fila["km"] = int(km.group(1).replace(".", "").replace(",", "")) if km else None
    fila["recogido_utc"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return fila


def scrapear(canal: str, max_paginas: int) -> list[dict]:
    vistos: dict[str, dict] = {}
    before = None
    for pagina in range(max_paginas):
        html = obtener(canal, before)
        filas = parsear(html, canal)
        if not filas:
            break
        nuevos = 0
        for fila in filas:
            if fila["id"] not in vistos:
                vistos[fila["id"]] = fila
                nuevos += 1
        menor = min(f["id_mensaje"] for f in filas)
        print(f"[{canal}] página {pagina+1}: {len(filas)} mensajes, {nuevos} nuevos, before={menor}", flush=True)
        if nuevos == 0 or menor <= 1:
            break
        before = str(menor)
        time.sleep(0.8)
    return list(vistos.values())


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-paginas", type=int, default=20)
    ap.add_argument("--canales", default=os.environ.get("TELEGRAM_CHANNELS", ""))
    args = ap.parse_args()

    canales = [c.strip().lstrip("@") for c in args.canales.split(",") if c.strip()] or CANALES_POR_DEFECTO
    OUT.mkdir(parents=True, exist_ok=True)

    todas: list[dict] = []
    for canal in canales:
        for fila in scrapear(canal, args.max_paginas):
            fila = extraer_campos(fila)
            todas.append(fila)
            if fila["es_auto"]:
                tdb.upsert_anuncio(fila)

    anuncios = [f for f in todas if f["es_auto"]]
    with (OUT / "anuncios.jsonl").open("w", encoding="utf-8") as fh:
        for fila in anuncios:
            fh.write(json.dumps(fila, ensure_ascii=False) + "\n")
    if anuncios:
        with (OUT / "anuncios.csv").open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=list(anuncios[0].keys()))
            writer.writeheader()
            writer.writerows(anuncios)

    estado = {
        "actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "canales": canales,
        "mensajes_totales": len(todas),
        "anuncios_auto": len(anuncios),
    }
    (OUT / "estado.json").write_text(json.dumps(estado, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tdb.set_estado("anuncios_telegram", str(len(anuncios)))
    print(f"Total mensajes={len(todas)} | anuncios auto={len(anuncios)}", flush=True)


if __name__ == "__main__":
    main()

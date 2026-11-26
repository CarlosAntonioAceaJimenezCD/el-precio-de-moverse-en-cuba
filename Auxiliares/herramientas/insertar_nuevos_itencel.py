#!/usr/bin/env python3
"""Scrapea e inserta los 10 anuncios nuevos detectados en iTENCEL."""
from __future__ import annotations

import importlib.util
import sqlite3
import urllib.request
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "Data/catalogos_concesionarios/marketplaces/itencel.sqlite"
BAK = DB.with_suffix(".sqlite.bak-20261123")
URLS = [
    "https://itencel.com/anuncio/gmc-sierra-2022-add",
    "https://itencel.com/anuncio/honda-acord-2025-add",
    "https://itencel.com/anuncio/hyundai-santa-cruz-202-add",
    "https://itencel.com/anuncio/hyundai-santa-fe-2024-add",
    "https://itencel.com/anuncio/kia-forte-gt-line-2020-add",
    "https://itencel.com/anuncio/maxus-2015-add",
    "https://itencel.com/anuncio/mercedes-sprinter-211-ano-2020",
    "https://itencel.com/anuncio/nissan-titan-2017-add",
    "https://itencel.com/anuncio/sonata-2021-sel-add",
    "https://itencel.com/anuncio/van-nissan-2020-add",
]


def canon(u: str) -> str:
    """El scraper guarda las URLs con barra final; canonizar evita duplicados."""
    return u.split("#")[0].rstrip("/") + "/"


def cargar_scraper():
    p = ROOT / "Auxiliares/herramientas/scrape_marketplaces.py"
    spec = importlib.util.spec_from_file_location("sm", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def descargar(url: str) -> tuple[str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "replace"), r.geturl()


def hacer_backup() -> None:
    if BAK.exists():
        return
    tmp = BAK.with_suffix(BAK.suffix + ".tmp")
    src = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    dst = sqlite3.connect(tmp)
    try:
        src.backup(dst)
    finally:
        dst.close()
        src.close()
    if tmp.stat().st_size == 0:
        raise RuntimeError("backup vacío")
    tmp.replace(BAK)
    print("backup:", BAK.name)


def main() -> None:
    sm = cargar_scraper()
    hacer_backup()

    conn = sqlite3.connect(DB)
    try:
        antes = conn.execute("select count(*) from anuncios").fetchone()[0]
        sitio = {"key": "itencel", "name": "iTENCEL"}
        insertados = 0
        for url in URLS:
            url = canon(url)
            try:
                if conn.execute("select 1 from anuncios where url=?", (url,)).fetchone():
                    print("ya existe:", url)
                    continue
                html, final = descargar(url)
                datos = sm.parse_detail(html, url, BeautifulSoup(html, "html.parser"))
                sm.save_detail(conn, sitio, url, datos, 200, final)
                insertados += 1
                print(f"insertado: {datos['title'][:55]} | {datos['price']} {datos['currency']}")
            except Exception as e:
                print(f"ERROR {url}: {type(e).__name__}: {e}")
        conn.commit()
    finally:
        despues = conn.execute("select count(*) from anuncios").fetchone()[0]
        conn.close()
        print(f"filas: {antes} -> {despues} (+{despues-antes}); procesados={insertados}")
        if despues - antes != insertados:
            print("AVISO: discrepancia entre filas insertadas y procesados")


if __name__ == "__main__":
    main()

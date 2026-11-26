#!/usr/bin/env python3
"""Limpieza de la BD de Revolico: solo vehículos de 4+ ruedas con datos útiles.

La revisión de la "página web" de cada anuncio se hace sobre el snapshot guardado
en `raw_html`/`text` en el momento del scraping (no se vuelve a descargar cada URL).
Opcionalmente `--verificar-online` comprueba una muestra en vivo con curl_cffi.

No borra los datos originales: crea las tablas `autos` (útiles) y `revision`
(motivo de exclusión), y marca cada fila de `anuncios` con columns de auditoría.
"""

from __future__ import annotations

import argparse
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "Data/Revolico/revolico.sqlite"
# Rango temporal permitido para anuncios: desde 2021-01-01 hasta hoy.
FECHA_MINIMA = "2021-01-01"

# Anuncios que Revolico publica dentro de "Vehículos > Carros" pero no son autos:
# combustible por litro, transporte de mudanza, taxi y Uber.
EXCLUDE_IDS = {"58867937", "53777554", "53843413", "58886962"}

# Categorías que SÍ son vehículos de al menos 4 ruedas.
INCLUDE = re.compile(
    r"Vehículos\s*>\s*(Carros|Camionetas|Camiones|Furgonetas|Autobuses|Autos)\b",
    re.IGNORECASE,
)
# Categorías que se descartan aunque digan "Vehículos".
EXCLUDE_CAT = re.compile(
    r"Motos|Triciclos|Bicicletas|Repuestos|Accesorios|Llantas|Neumáticos|"
    r"Alquiler|Servicios|Navegación|Otros\s*-\s*Vehículos",
    re.IGNORECASE,
)
# Palabras del título que indican que no es un vehículo completo.
EXCLUDE_TITLE = re.compile(
    r"\b(moto|motocicleta|bicimoto|scooter|triciclo|bici|bicicleta|llanta|neumático|"
    r"repuesto|accesorio|radio|pantalla|estereo|alarma|faros?|parachoques?|"
    r"espejos?|amortiguador|radiador|escatolina|alternador|arranque|"
    r"empleo|chofer|alquiler|renta|servicio t[ée]cnico|taller|lavado|"
    r"kit solar|estaci[oó]n de energ[ií]a|aditamento|soporte para bicicletas)\b"
    r"|(?:vendo|se vende|venta de)\s+(?:un\s+)?(?:motor|caja|transmisi[oó]n|bater[ií]a|radiador|alternador)\b"
    r"|\bmotor suelto\b",
    re.IGNORECASE,
)
INCLUDE_TITLE = re.compile(
    r"\b(carro|autom[oó]vil|coche|camioneta|furgoneta|cam[ií]on|autob[oú]s|microb[uú]s|microbus|guagua|[oó]mnibus|bus|jeep|suv|pickup|"
    r"chevrolet|ford|toyota|renault|nissan|honda|hyundai|kia|mazda|vw|volkswagen|"
    r"pontiac|buick|changan|dongfeng|volvo|bmw|mercedes|lexus|peugeot|fiat)\b",
    re.IGNORECASE,
)


def categoria(texto: str) -> str:
    if not texto:
        return ""
    m = re.search(r"Inicio\s*>\s*(.*?)\s*>\s*La Habana", texto[:500])
    return (m.group(1) if m else texto[:120]).strip()


def preparar(con: sqlite3.Connection) -> None:
    cols = {r[1] for r in con.execute("PRAGMA table_info(anuncios)")}
    for name, decl in [
        ("es_auto", "INTEGER DEFAULT 0"),
        ("motivo_exclusion", "TEXT"),
        ("pagina_revisada", "INTEGER DEFAULT 0"),
        ("datos_necesarios", "INTEGER DEFAULT 0"),
    ]:
        if name not in cols:
            con.execute(f"ALTER TABLE anuncios ADD COLUMN {name} {decl}")
    con.execute(
        """CREATE TABLE IF NOT EXISTS autos AS SELECT
        id, url, title, short_description, description, price, currency, status,
        province_name, municipality_name, category_id, subcategory_id,
        images_count, scraped_at, raw_html, text FROM anuncios"""
    )
    # La tabla se reconstruye en cada corrida para reflejar cambios de la BD.
    con.execute("DELETE FROM autos")
    con.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_autos_id ON autos(id)")
    con.execute(
        """CREATE TABLE IF NOT EXISTS revision (
        id TEXT PRIMARY KEY, url TEXT, categoria TEXT, motivo TEXT, revisado_utc TEXT)"""
    )
    con.execute("DELETE FROM revision")


def clasificar(row: dict) -> tuple[bool, str, bool, bool]:
    titulo = row.get("title") or ""
    texto = row.get("text") or ""
    cat = categoria(texto)
    html = row.get("raw_html") or ""

    # 1) Revisión del snapshot de la página.
    pagina_ok = len(html) > 1000 and (
        "AdType" in html or "og:title" in html or "Revolico" in html
    ) and "anomaly" not in html[:2000].lower()

    # 1a) Exclusión manual: servicios y combustible mal categorizados.
    if str(row.get("id")) in EXCLUDE_IDS:
        return False, "no es auto: servicio/combustible", pagina_ok, False

    # 1b) Rango temporal: 2021-01-01 hasta hoy.
    fecha = str(row.get("updated_on_by_user") or "")[:10]
    hoy = datetime.now(timezone.utc).date().isoformat()
    if fecha and (fecha < FECHA_MINIMA or fecha > hoy):
        return False, f"fuera de rango temporal ({fecha})", pagina_ok, False

    # 2) ¿Es vehículo de 4+ ruedas?
    if EXCLUDE_CAT.search(cat):
        return False, f"categoría excluida: {cat}", pagina_ok, False
    # Una marca en el título NO debe poder vencer a una exclusión explícita
    # (moto, repuesto, llanta, servicio, alquiler...). La exclusión manda siempre.
    excluida = bool(EXCLUDE_TITLE.search(titulo)) or bool(EXCLUDE_CAT.search(cat))
    incluida = bool(INCLUDE.search(cat)) or bool(INCLUDE_TITLE.search(titulo))
    es_auto = incluida and not excluida
    if not es_auto:
        return False, f"no es vehículo 4+ ruedas: {cat or titulo[:60]}", pagina_ok, False

    # 3) ¿Tiene los datos mínimos para el análisis de rentabilidad?
    try:
        precio = float(row.get("price") or 0)
    except (TypeError, ValueError):
        precio = 0
    datos_ok = (
        precio > 0
        and bool(row.get("currency"))
        and len(titulo.strip()) > 5
        and bool(row.get("url"))
        and bool(row.get("province_name"))
        and bool(row.get("scraped_at"))
    )
    motivo = "" if datos_ok else "faltan datos necesarios (precio/moneda/título/url/provincia/fecha)"
    return datos_ok, motivo, pagina_ok, datos_ok


def verificar_online(con: sqlite3.Connection, limite: int) -> None:
    try:
        from curl_cffi import requests as curl_requests
    except ImportError:
        print("curl_cffi no disponible; se omite verificación online")
        return
    ids = [r[0] for r in con.execute("SELECT id FROM autos LIMIT ?", (limite,))]
    caidos = []
    for aid in ids:
        url = con.execute("SELECT url FROM autos WHERE id=?", (aid,)).fetchone()[0]
        try:
            r = curl_requests.get(url, impersonate="chrome", timeout=15)
            if r.status_code >= 400 or "No se encontr" in r.text:
                caidos.append(aid)
        except Exception:
            caidos.append(aid)
    for aid in caidos:
        con.execute("DELETE FROM autos WHERE id=?", (aid,))
    print(f"Verificación online: {len(ids)} revisadas, {len(caidos)} eliminadas")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verificar-online", type=int, default=0, metavar="N", help="revisar N URLs en vivo")
    args = ap.parse_args()

    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    preparar(con)
    stats = {"total": 0, "autos": 0, "sin_datos": 0, "no_auto": 0, "pagina_mal": 0}
    ahora = datetime.now(timezone.utc).isoformat(timespec="seconds")

    for fila in con.execute("SELECT * FROM anuncios"):
        row = dict(fila)
        stats["total"] += 1
        guardar, motivo, pagina_ok, datos_ok = clasificar(row)

        if not pagina_ok:
            stats["pagina_mal"] += 1
            motivo = (motivo + "; " if motivo else "") + "página sin datos suficientes"
        if guardar and pagina_ok and datos_ok:
            stats["autos"] += 1
            columns = [d[1] for d in con.execute("PRAGMA table_info(autos)")]
            values = [row.get(c) for c in columns]
            con.execute(
                f"INSERT OR REPLACE INTO autos ({','.join(columns)}) VALUES ({','.join('?'*len(columns))})",
                values,
            )
        else:
            if not datos_ok and "faltan datos" in motivo:
                stats["sin_datos"] += 1
            else:
                stats["no_auto"] += 1
            con.execute(
                "INSERT OR REPLACE INTO revision VALUES (?,?,?,?,?)",
                (row["id"], row["url"], categoria(row.get("text") or ""), motivo, ahora),
            )
        con.execute(
            "UPDATE anuncios SET es_auto=?, motivo_exclusion=?, pagina_revisada=?, datos_necesarios=? WHERE id=?",
            (1 if guardar and pagina_ok else 0, motivo, 1 if pagina_ok else 0, 1 if datos_ok else 0, row["id"]),
        )

    if args.verificar_online:
        verificar_online(con, args.verificar_online)

    con.commit()
    print("Limpieza completada:", stats)
    print("Tabla `autos`:", con.execute("SELECT count(*) FROM autos").fetchone()[0])
    print("Tabla `revision`:", con.execute("SELECT count(*) FROM revision").fetchone()[0])
    con.close()


if __name__ == "__main__":
    main()

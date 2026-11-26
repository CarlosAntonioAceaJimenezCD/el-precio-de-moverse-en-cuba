#!/usr/bin/env python3
"""Estructura precios/modelos/specs de los concesionarios y parsea catalogos PDF."""
import re
import sqlite3
import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DBDIR = BASE.parent / "Data" / "catalogos_concesionarios"
CATDIR = BASE.parent / "Data" / "fuentes_oficiales" / "catalogos"
OUT = BASE.parent / "Data" / "analisis_rentabilidad" / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

TARGETS = ["bdc_one", "dongfeng_cuba", "finauto", "changan", "chinautos_cuba", "atr_export"]
BRANDS = [
    "chevrolet", "lada", "moskvich", "fiat", "ford", "hyundai", "hyunday", "volkswagen",
    "peugeot", "dodge", "plymouth", "kia", "toyota", "nissan", "honda", "mazda",
    "renault", "mercedes", "bmw", "audi", "volvo", "lexus", "changan", "dongfeng",
    "geely", "byd", "foton", "mg", "isuzu", "suzuki", "jeep", "citroen", "seat",
]
ALIASES = {"hyunday": "hyundai", "benz": "mercedes", "vw": "volkswagen", "chevy": "chevrolet"}


def parse_price(v):
    if v is None:
        return 0.0, ""
    s = str(v).strip()
    if not s:
        return 0.0, ""
    cur = "EUR" if ("€" in s or "EUR" in s.upper()) else ("CUP" if "CUP" in s.upper() else "USD")
    num = re.sub(r"[^\d,.]", "", s)
    if not num:
        return 0.0, cur
    if "," in num and "." in num:
        num = num.replace(".", "").replace(",", ".") if num.rfind(",") > num.rfind(".") else num.replace(",", "")
    elif "," in num:
        num = num.replace(",", "") if re.match(r"^\d{1,3},\d{3}$", num) else num.replace(",", ".")
    try:
        return float(num), cur
    except Exception:
        return 0.0, cur


def parse_title(title: str):
    t = (title or "").lower()
    brand = ""
    for b in BRANDS:
        if re.search(r"\b" + re.escape(b) + r"\b", t):
            brand = ALIASES.get(b, b)
            break
    model = ""
    if brand:
        m = re.search(r"\b" + re.escape(brand) + r"\s+([a-z0-9][a-z0-9 \-/]{1,30})", t)
        if m:
            model = m.group(1).strip()
    return brand, model


def ensure_cols(c):
    cols = {r[1] for r in c.execute("PRAGMA table_info(vehiculos)")}
    wanted = {
        "precio_num": "REAL", "moneda_struct": "TEXT", "marca_struct": "TEXT",
        "modelo_struct": "TEXT", "anio_struct": "INTEGER", "km_struct": "REAL",
        "combustible_struct": "TEXT", "transmision_struct": "TEXT", "potencia_struct": "TEXT",
        "cilindrada_struct": "TEXT", "puertas_struct": "INTEGER", "asientos_struct": "INTEGER",
        "carroceria_struct": "TEXT", "estado_struct": "TEXT", "fuente_specs": "TEXT",
    }
    for name, decl in wanted.items():
        if name not in cols:
            c.execute(f"ALTER TABLE vehiculos ADD COLUMN {name} {decl}")
    c.commit()


def enrich_db(name):
    db = DBDIR / f"{name}.sqlite"
    if not db.exists():
        return
    c = sqlite3.connect(db)
    ensure_cols(c)
    rows = c.execute(
        "SELECT rowid, title, text, precio, moneda, marca, modelo, anio, km, "
        "combustible, transmision, potencia, cilindrada, puertas, asientos, carroceria, estado "
        "FROM vehiculos"
    ).fetchall()
    updated = 0
    for (rid, title, text, precio, moneda, marca, modelo, anio, km, comb, trans,
         pot, cil, puertas, asientos, carro, estado) in rows:
        p, cur = parse_price(precio)
        brand, model = parse_title(title or "")
        brand = brand or (marca or "").lower()
        model = model or (modelo or "").lower()
        blob = (text or "")[:8000]
        hp = re.search(r"\b(\d{2,3})\s*(?:hp|cv)\b", blob, re.I)
        yr = re.search(r"\b(20[0-2]\d)\b", title or "")
        fuel = re.search(r"\b(gasolina|di[eé]sel|h[ií]brido|el[eé]ctrico)\b", blob, re.I)
        tr = re.search(r"\b(autom[aá]tico|manual)\b", blob, re.I)
        body = re.search(r"\b(sed[aá]n|suv|pickup|hatchback|furgoneta|camioneta|coup[eé])\b", blob, re.I)
        c.execute(
            """UPDATE vehiculos SET precio_num=?, moneda_struct=?, marca_struct=?, modelo_struct=?,
               anio_struct=?, km_struct=?, combustible_struct=?, transmision_struct=?,
               potencia_struct=?, cilindrada_struct=?, puertas_struct=?, asientos_struct=?,
               carroceria_struct=?, estado_struct=?, fuente_specs='ficha'
               WHERE rowid=?""",
            (
                p, cur or (moneda or ""), brand, model[:60],
                int(yr.group(1)) if yr else (anio if str(anio or "").isdigit() else None),
                float(km) if str(km or "").replace(".", "").isdigit() else None,
                fuel.group(1).lower() if fuel else (comb or "")[:40],
                tr.group(1).lower() if tr else (trans or "")[:40],
                hp.group(1) if hp else (pot or "")[:40], (cil or "")[:40],
                int(puertas) if str(puertas or "").isdigit() else None,
                int(asientos) if str(asientos or "").isdigit() else None,
                body.group(1).lower() if body else (carro or "")[:40],
                (estado or "")[:40], rid,
            ),
        )
        updated += 1
    c.commit()
    nprice = c.execute("SELECT COUNT(*) FROM vehiculos WHERE precio_num>0").fetchone()[0]
    print(f"{name}: {updated} filas, {nprice} con precio")
    c.close()


def parse_changan_pdf():
    pdf = CATDIR / "changan_catalogo_2026.pdf"
    if not pdf.exists():
        print("Sin PDF de Changan")
        return
    txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    items = []
    for block in txt.split("\f"):
        if "TIPO DE VEH" not in block:
            continue
        lines = [l.strip() for l in block.splitlines() if l.strip()]
        model = next((l for l in lines if re.match(r"^[A-Z0-9][A-Z0-9 \-]{2,30}$", l) and "TIPO" not in l), "")
        price = re.search(r"\$\s?([\d\s.,]+)", block)
        hp = re.search(r"(\d{2,3})\s*(?:HP|CV)", block, re.I)
        fuel = re.search(r"TIPO DE ENERG[IÍ]A:\s*(.+)", block, re.I)
        body = re.search(r"TIPO DE VEH[IÍ]CULO:\s*(.+)", block, re.I)
        drive = re.search(r"TIPO DE TRACCI[IÓ]N:\s*(.+)", block, re.I)
        motor = re.search(r"TIPO DE MOTOR:\s*(.+)", block, re.I)
        items.append({
            "marca": "changan", "modelo": model,
            "precio_usd": float(price.group(1).replace(" ", "").replace(",", "")) if price else None,
            "hp": int(hp.group(1)) if hp else None,
            "energia": fuel.group(1).strip() if fuel else "",
            "carroceria": body.group(1).strip() if body else "",
            "traccion": drive.group(1).strip() if drive else "",
            "motor": motor.group(1).strip() if motor else "",
        })
    import csv
    out = OUT / "catalogo_changan.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(items[0].keys()))
        w.writeheader(); w.writerows(items)
    print(f"Changan PDF: {len(items)} modelos -> {out}")

    # Volcar precios del PDF en la BD de Changan cuando coincide el modelo
    db = DBDIR / "changan.sqlite"
    if db.exists() and items:
        c = sqlite3.connect(db)
        for it in items:
            if not it["precio_usd"]:
                continue
            c.execute(
                """UPDATE vehiculos SET precio_num=?, moneda_struct='USD', marca_struct='changan',
                   modelo_struct=?, potencia_struct=?, combustible_struct=?, carroceria_struct=?,
                   transmision_struct=?, fuente_specs='PDF catalogo 2026'
                   WHERE lower(title) LIKE ? OR lower(modelo_struct) LIKE ?""",
                (it["precio_usd"], it["modelo"], str(it["hp"] or ""), it["energia"],
                 it["carroceria"], it["traccion"], f"%{it['modelo'].lower()}%", f"%{it['modelo'].lower()}%"),
            )
        c.commit(); c.close()


def main():
    for name in TARGETS:
        enrich_db(name)
    parse_changan_pdf()


if __name__ == "__main__":
    main()

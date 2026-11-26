#!/usr/bin/env python3
"""Ingesta incremental de todas las fuentes a un Parquet canonico."""
import json
import re
import sqlite3
import sys
from pathlib import Path
from urllib.parse import unquote

import pandas as pd
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import config as cfg

sys.path.insert(0, str(cfg.PROJECT / "Auxiliares" / "herramientas"))

YEAR_RE = re.compile(r"\b(19\d{2}|20[0-2]\d)\b")
KM_RE = re.compile(r"\b([\d]{1,3}[.,]?[\d]{0,3})\s*(?:km|kil[oó]metros)\b", re.I)
HP_RE = re.compile(r"\b(\d{2,3})\s*(?:hp|cv)\b", re.I)
TRANS_RE = re.compile(r"\b(autom[aá]tico|manual|automatic|semiautomatic)\b", re.I)
FUEL_RE = re.compile(r"\b(gasolina|di[eé]sel|h[ií]brido|el[eé]ctrico|gnc|gas)\b", re.I)

# Titulos que son texto de navegacion, no del anuncio.
UI_TITLE_RE = re.compile(
    r"^(comprar carros|reportar este anuncio|administrar mis anuncios|"
    r"iniciar sesi[oó]n|registrarse|resultados de b[uú]squeda)\b",
    re.I,
)
# Palabras que delatan un no-auto cuando abren el titulo.
NON_CAR_RE = re.compile(
    r"(triciclos?|motocicletas?|motos?|scooters?|patinetes?|bicicletas?|bicis?|"
    r"repuestos?|piezas?|accesorios?|fusibles?|tapa de|bater[ií]as?|llantas?|"
    r"neum[aá]ticos?|parachoques|faros?|luces?|espejos?|cargador\w*|gps|"
    r"kit de|compresor\w*|arrancador\w*|inflador\w*|aditamento|soporte|"
    r"motor de arranque)\b",
    re.I,
)
# Frases que delatan un no-auto en cualquier posicion del titulo.
NON_CAR_ANY_RE = re.compile(
    r"\b(moto todoterreno|moto el[eé]ctrica|triciclo|bicicleta|patinete)\b",
    re.I,
)
# Avisos de prestamos, farmacia o hechizos que se cuelan en los clasificados.
SPAM_TITLE_RE = re.compile(
    r"(pr[eé]stamos?|micro ?cr[eé]dito|cr[eé]dit\w*|love spell|abortion|"
    r"aphetamine|sels de bain|viagra|casino)",
    re.I,
)
# iTENCEL publica ofertas de importacion desde EE. UU., no mercado local.
IMPORT_SITES = {"itencel"}


def parse_number(value) -> float | None:
    """Numero con separador de miles (80,000 / 80.000) o decimal (80,5)."""
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None
    s = str(value).strip()
    if not s:
        return None
    num = re.sub(r"[^\d,.]", "", s)
    if not num:
        return None
    if re.match(r"^\d{1,3}(,\d{3})+$", num):
        num = num.replace(",", "")
    elif re.match(r"^\d{1,3}(\.\d{3})+$", num):
        num = num.replace(".", "")
    elif "," in num and "." in num:
        num = num.replace(".", "").replace(",", ".") if num.rfind(",") > num.rfind(".") else num.replace(",", "")
    elif "," in num:
        num = num.replace(",", ".")
    try:
        return float(num)
    except Exception:
        return None


SPEC_PATTERNS = {
    "mileage_km": (r"\b(\d{1,3}[.,]?\d{0,3})\s*(?:km|kil[oó]metros)\b", 1),
    "hp": (r"\b(\d{2,3})\s*(?:hp|cv)\b|potencia[^\d]{0,15}(\d{2,3})", None),
    "displacement": (r"\b(\d[.,]\d)\s*(?:l|litros)\b|\b(\d{3,4})\s*cc\b", None),
    "fuel": (r"\b(gasolina|di[eé]sel|h[ií]brido|el[eé]ctrico|gnc|gas)\b", 1),
    "transmission": (r"\b(autom[aá]tico|automatic|manual|semiautom[aá]tico)\b", 1),
    "drivetrain": (r"\b(4x4|4x2|tracci[oó]n delantera|tracci[oó]n trasera|fwd|rwd|awd)\b", 1),
    "body": (r"\b(sed[aá]n|suv|pickup|hatchback|furgoneta|camioneta|coup[eé]|monovolumen|microb[uú]s|autob[uú]s)\b", 1),
    "doors": (r"\b(\d)\s*puertas\b", 1),
    "seats": (r"\b(\d)\s*(?:asientos|plazas)\b", 1),
    "condition": (r"\b(nuevo|usado|excelente|impecable|bueno|regular|mal estado)\b", 1),
}


def parse_specs(text: str) -> dict:
    t = text or ""
    out = {}
    for field, (pattern, group) in SPEC_PATTERNS.items():
        m = re.search(pattern, t, re.I)
        if not m:
            continue
        if group is not None:
            out[field] = m.group(group)
        else:
            out[field] = next((g for g in m.groups() if g), "")
    if "mileage_km" in out:
        out["mileage_km"] = parse_number(out["mileage_km"])
    return out


def parse_title(title: str) -> dict:
    t = title or ""
    years = YEAR_RE.findall(t)
    km = KM_RE.findall(t)
    hp = HP_RE.findall(t)
    fuel = FUEL_RE.search(t)
    trans = TRANS_RE.search(t)
    brand = ""
    tl = t.lower()
    for b in cfg.BRANDS:
        if re.search(r"\b" + re.escape(b) + r"\b", tl):
            brand = b
            break
    model = ""
    if brand:
        m = re.search(r"\b" + re.escape(brand) + r"\s+([A-Za-z0-9 \-]{2,30})", t, re.I)
        if m:
            model = m.group(1).strip()[:40]
    return {
        "brand": brand,
        "model": model,
        "year": int(years[0]) if years else None,
        "mileage_km": parse_number(km[0]) if km else None,
        "hp": parse_number(hp[0]) if hp else None,
        "fuel": fuel.group(1).lower() if fuel else "",
        "transmission": trans.group(1).lower() if trans else "",
    }


def parse_price(value):
    """Devuelve (float, moneda) desde '€ 22.900', '$30,538.14', '17.900', 22900."""
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return 0.0, "USD"
    s = str(value).strip()
    if not s:
        return 0.0, "USD"
    upper = s.upper()
    cur = "EUR" if "€" in s or "EUR" in upper else (
        "CUP" if "CUP" in upper else "USD"
    )
    num = re.sub(r"[^\d,.]", "", s)
    if not num:
        return 0.0, cur
    if re.match(r"^\d{1,3}(\.\d{3})+$", num):
        num = num.replace(".", "")          # 13.000 -> 13000
    elif re.match(r"^\d{1,3}(,\d{3})+$", num):
        num = num.replace(",", "")          # 2,300 -> 2300
    elif "," in num and "." in num:
        num = num.replace(".", "").replace(",", ".") if num.rfind(",") > num.rfind(".") else num.replace(",", "")
    elif "," in num:
        num = num.replace(",", ".")
    try:
        return float(num), cur
    except Exception:
        return 0.0, cur


def jsonld_offer(html: str) -> tuple[float, str, str]:
    """Precio, moneda y nombre del bloque JSON-LD schema.org de una ficha."""
    if not html:
        return 0.0, "", ""
    soup = BeautifulSoup(html, "html.parser")
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or script.get_text() or "{}")
        except Exception:
            continue
        for item in data if isinstance(data, list) else [data]:
            if not isinstance(item, dict):
                continue
            offer = item.get("offers")
            if isinstance(offer, list):
                offer = offer[0] if offer else None
            if not isinstance(offer, dict):
                continue
            price = parse_price(offer.get("price"))[0]
            if price >= cfg.PRICE_MIN_USD:
                currency = str(offer.get("priceCurrency") or "USD").upper()
                if currency == "CUC":
                    currency = "USD"
                return price, currency, str(item.get("name") or "")
    return 0.0, "", ""


def slug_title(url: str) -> str:
    """Titulo legible desde la URL: .../kia-rio-2020!123.htm -> kia rio 2020."""
    value = unquote(url or "")
    if "/anuncio/" in value:
        value = value.split("/anuncio/", 1)[1].strip("/").split("/")[0]
    else:
        value = value.rstrip("/").split("/")[-1].split("!")[0]
        value = re.sub(r"\.html?$", "", value)
    value = re.sub(r"[-_]+", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    low = value.lower()
    for brand in cfg.BRANDS:
        if low.startswith(brand) and len(low) > len(brand) and low[len(brand)] != " ":
            value = value[: len(brand)] + " " + value[len(brand):]
            break
    value = re.sub(r"(?<=[a-z])(19\d{2}|20[0-2]\d)", r" \1", value, flags=re.I)
    return re.sub(r"\s+", " ", value).strip()


def repair_title(title: str, name: str, url: str) -> str:
    """Reemplaza titulos de interfaz por el nombre del JSON-LD o por el slug."""
    current = str(title or "").strip()
    if current and not UI_TITLE_RE.match(current):
        return current
    candidate = str(name or "").strip()
    if not candidate or UI_TITLE_RE.match(candidate):
        candidate = slug_title(url)
    return candidate or current


def is_non_car(title: str) -> bool:
    """True solo si el titulo abre con un no-auto o trae una frase inequivoca."""
    clean = re.sub(r"^[^0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", "", str(title or "")).strip()
    return bool(NON_CAR_RE.match(clean) or NON_CAR_ANY_RE.search(clean))


def read_sql(path: Path, query: str) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        c = sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=30)
        df = pd.read_sql_query(query, c)
        c.close()
        return df
    except Exception as e:
        print(f"  WARN {path.name}: {e}")
        return pd.DataFrame()


def ingest_revolico() -> pd.DataFrame:
    print("Revolico...")
    if not cfg.REVOLICO_DB.exists() and cfg.REVOLICO_MANIFEST.exists():
        from db_chunks import assemble

        print("  reconstruyendo revolico.sqlite desde chunks...")
        assemble(cfg.REVOLICO_MANIFEST, cfg.REVOLICO_DB)
    df = read_sql(
        cfg.REVOLICO_DB,
        """SELECT id AS source_id, url, title, short_description, description, price, currency,
                  province_name, municipality_name, scraped_at, text,
                  images_count, status
           FROM autos""",
    )
    if df.empty:
        return df
    df["source"] = "revolico"
    df["description"] = df.get("short_description", "") + " " + df.get("text", "")
    df["is_new"] = 0
    df["canal"] = "local"
    df["location"] = df.get("municipality_name", "") + ", " + df.get("province_name", "")
    df["date"] = df.get("scraped_at", "")
    return df


def ingest_concesionarios() -> pd.DataFrame:
    print("Concesionarios...")
    frames = []
    for db in sorted(cfg.CONCESIONARIOS_DIR.glob("*.sqlite")):
        d = read_sql(
            db,
            """SELECT url AS source_id, url, title, precio AS price, moneda AS currency,
                      marca, modelo, anio, km, combustible, transmision, color,
                      carroceria, estado, text, scraped_at, images_json
               FROM vehiculos""",
        )
        if d.empty:
            continue
        d["source"] = "concesionario:" + db.stem
        d["description"] = d["text"].fillna("").astype(str)
        empty = d["description"].str.strip() == ""
        d.loc[empty, "description"] = d.loc[empty, "title"].fillna("").astype(str)
        d["is_new"] = 1
        d["canal"] = "local"
        d["location"] = ""
        d["date"] = d.get("scraped_at", "")
        frames.append(d)
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def ingest_marketplaces() -> pd.DataFrame:
    print("Marketplaces...")
    frames = []
    descartes = []
    for db in sorted(cfg.MARKETPLACES_DIR.glob("*.sqlite")):
        d = read_sql(
            db,
            """SELECT url AS source_id, url, title, price, currency, location, date,
                      description, seller_name, scraped_at, images_json, raw_html
               FROM anuncios""",
        )
        if d.empty:
            continue
        d = d.copy()
        d["source"] = "marketplace:" + db.stem
        d["is_new"] = 0
        d["canal"] = "importacion" if db.stem in IMPORT_SITES else "local"
        d["raw_html"] = d["raw_html"].fillna("") if "raw_html" in d.columns else ""
        d["price"] = d["price"].astype("object")

        for i in d.index:
            price = parse_price(d.at[i, "price"])[0]
            title = str(d.at[i, "title"] or "")
            name = ""
            if price < cfg.PRICE_MIN_USD or UI_TITLE_RE.match(title):
                found, currency, name = jsonld_offer(d.at[i, "raw_html"])
                if price < cfg.PRICE_MIN_USD and found >= cfg.PRICE_MIN_USD:
                    price = found
                    d.at[i, "price"] = found
                    d.at[i, "currency"] = currency
            d.at[i, "title"] = repair_title(d.at[i, "title"], name, d.at[i, "url"])

        titles = d["title"].fillna("").astype(str)
        motivo = pd.Series("", index=d.index)
        motivo[titles.apply(lambda t: bool(UI_TITLE_RE.match(t)))] = "titulo de interfaz"
        motivo[titles.apply(is_non_car)] = "no es auto"
        motivo[titles.apply(lambda t: bool(SPAM_TITLE_RE.search(t)))] = "spam"

        if db.stem == "ventacuba":
            precios = d["price"].apply(parse_price)
            marcador = precios.apply(lambda x: x[1] == "EUR" and 0 < x[0] <= 300)
            motivo[marcador] = "precio marcador"

        if db.stem == "cogetucarro":
            artefactos = []
            for i in d.index:
                precio = parse_price(d.at[i, "price"])[0]
                if precio < cfg.PRICE_MIN_USD:
                    continue
                tokens = set(re.findall(r"\b\d{2,5}\b", str(d.at[i, "title"] or "")))
                if str(int(round(precio))) in tokens:
                    artefactos.append(i)
            motivo[d.index.isin(artefactos)] = "precio = modelo/anio"

        drop = motivo != ""
        if drop.any():
            bad = d.loc[drop, ["source", "source_id", "url", "title", "price", "currency", "canal"]].copy()
            bad["motivo"] = motivo[drop]
            descartes.append(bad)
        d = d[~drop].copy()
        d = d.drop(columns=["raw_html"], errors="ignore")
        frames.append(d)

    if descartes:
        out = pd.concat(descartes, ignore_index=True)
        out.to_csv(cfg.TABLES / "descartes_marketplaces.csv", index=False)
        print(f"  descartes: {len(out)} -> {cfg.TABLES / 'descartes_marketplaces.csv'}")

    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


CANON = [
    "source", "source_id", "url", "title", "description", "price", "currency",
    "price_usd", "canal", "brand", "model", "year", "mileage_km", "hp", "fuel",
    "transmission", "location", "date", "scraped_at", "is_new", "images_count",
    "displacement", "drivetrain", "body", "doors", "seats", "condition",
]


def main():
    cfg.DATA.mkdir(parents=True, exist_ok=True)
    cfg.TABLES.mkdir(parents=True, exist_ok=True)
    frames = [f for f in (ingest_revolico(), ingest_concesionarios(), ingest_marketplaces()) if not f.empty]
    if not frames:
        raise SystemExit("No se encontraron datos en ninguna fuente")
    raw = pd.concat(frames, ignore_index=True)
    for col in CANON:
        if col not in raw.columns:
            raw[col] = None

    parsed = raw["title"].apply(parse_title).apply(pd.Series)
    for c in ("brand", "model", "year", "mileage_km", "hp", "fuel", "transmission"):
        raw[c] = parsed[c].combine_first(raw[c])
    raw["brand"] = raw["brand"].apply(cfg.normalize_brand)
    raw["model"] = raw["model"].apply(cfg.normalize_model)

    specs = raw["description"].fillna("").apply(parse_specs).apply(pd.Series)
    for c in specs.columns:
        raw[c] = specs[c].combine_first(raw[c]) if c in raw.columns else specs[c]

    parsed_price = raw["price"].apply(parse_price)
    raw["price"] = parsed_price.apply(lambda x: x[0])
    raw["currency"] = parsed_price.apply(lambda x: x[1]).combine_first(raw["currency"])
    for col in ("price", "year", "mileage_km", "hp", "images_count", "doors", "seats"):
        raw[col] = pd.to_numeric(raw[col], errors="coerce")
    raw["price"] = raw["price"].fillna(0)
    raw["price_usd"] = [
        cfg.to_usd(p, c) for p, c in zip(raw["price"], raw["currency"])
    ]
    raw["ingested_at"] = pd.Timestamp.now("UTC").isoformat()
    raw = raw[CANON + ["ingested_at"]].drop_duplicates(subset=["source", "source_id"], keep="last")
    out = cfg.DATA / "listings_raw.parquet"
    raw.to_parquet(out, index=False)
    print(f"INGESTA: {len(raw)} filas -> {out}")
    print(raw.groupby("source").size().to_string())


if __name__ == "__main__":
    main()

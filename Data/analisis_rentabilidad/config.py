"""Configuracion central del analisis. Editar aqui, no en los scripts."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"
CHARTS = OUTPUTS / "charts"
TABLES = OUTPUTS / "tables"

PROJECT = ROOT.parents[1]
REVOLICO_DB = PROJECT / "Data" / "Revolico" / "revolico.sqlite"
REVOLICO_CHUNKS = PROJECT / "Data" / "Revolico" / "chunks"
REVOLICO_MANIFEST = REVOLICO_CHUNKS / "MANIFEST.json"
PIPELINE_DB = PROJECT / "Data" / "Revolico" / "pipeline.sqlite"
PIPELINE_CHUNKS = PROJECT / "Data" / "Revolico" / "pipeline_chunks"
PIPELINE_MANIFEST = PIPELINE_CHUNKS / "MANIFEST.json"
DB_CHUNKS_TOOL = PROJECT / "Auxiliares" / "herramientas" / "db_chunks.py"
CONCESIONARIOS_DIR = PROJECT / "Data" / "catalogos_concesionarios"
MARKETPLACES_DIR = CONCESIONARIOS_DIR / "marketplaces"

# Tipo de cambio INFORMAL (TRMI elTOQUE), 18/11/2026 00:52.
# En Cuba la tasa oficial no aplica a las transacciones cotidianas: se usa TRMI.
# Fuente: https://www.dolar-app.com/cu (atribuye a API Tasas de elTOQUE).
FX = {"USD": 1.0, "CUP": 1 / 930.0, "EUR": 1000.0 / 930.0, "MLC": 845.35 / 930.0}
FX_NOTE = "TRMI elTOQUE 18/11/2026: USD 930 CUP | EUR 1000 CUP | MLC 845.35 CUP"

CURRENT_YEAR = 2026
YEAR_MIN = 1990
YEAR_MAX = CURRENT_YEAR + 1
PRICE_MIN_USD = 200
PRICE_MAX_USD = 250_000
MILEAGE_MAX_KM = 600_000

# Marcas y tiers (ampliar cuando haya mas datos)
BRANDS = [
    "chevrolet", "lada", "moskvich", "fiat", "ford", "hyundai", "volkswagen",
    "peugeot", "dodge", "plymouth", "kia", "toyota", "nissan", "honda", "mazda",
    "renault", "mercedes", "bmw", "audi", "volvo", "lexus", "changan", "dongfeng",
    "geely", "byd", "foton", "mg", "isuzu", "suzuki", "jeep", "citroen", "seat",
    "buick", "pontiac", "oldsmobile", "chery", "jac", "gmc", "mitsubishi",
    "land rover", "jaguar", "infiniti", "acura", "baic", "daewoo", "opel",
    "volga", "gac", "bestune", "maxus", "ssangyong", "vw",
]
PREMIUM = {
    "mercedes", "bmw", "audi", "volvo", "lexus", "porsche", "cadillac",
    "land rover", "jaguar", "infiniti", "acura",
}
MID = {
    "toyota", "honda", "nissan", "hyundai", "kia", "mazda", "volkswagen", "ford",
    "chevrolet", "peugeot", "renault", "citroen", "mitsubishi", "jeep", "suzuki",
    "isuzu", "gmc", "fiat", "changan", "dongfeng", "byd", "geely", "mg",
    "baic", "daewoo", "opel", "ssangyong",
}


ALIASES = {
    "hyunday": "hyundai", "hyundai": "hyundai", "toyota": "toyota",
    "mercedes-benz": "mercedes", "mercedes benz": "mercedes", "benz": "mercedes",
    "vw": "volkswagen", "volskwagen": "volkswagen", "chevrolet": "chevrolet",
    "chevy": "chevrolet", "nissan": "nissan", "mazda": "mazda",
    "fiat": "fiat", "peugeot": "peugeot", "renault": "renault",
    "lada": "lada", "moskvich": "moskvich", "moscovich": "moskvich",
    "kia": "kia", "ford": "ford", "dodge": "dodge", "plymouth": "plymouth",
    "citroen": "citroen", "seat": "seat", "bmw": "bmw", "audi": "audi",
    "volvo": "volvo", "lexus": "lexus", "changan": "changan", "chery": "chery",
    "dongfeng": "dongfeng", "geely": "geely", "byd": "byd", "foton": "foton",
    "mg": "mg", "isuzu": "isuzu", "suzuki": "suzuki", "jeep": "jeep",
    "gmc": "gmc", "buick": "buick", "pontiac": "pontiac", "oldsmobile": "oldsmobile",
    "jac": "jac", "mitsubishi": "mitsubishi", "porsche": "porsche", "cadillac": "cadillac",
    "land rover": "land rover", "landrover": "land rover", "range rover": "land rover",
    "jaguar": "jaguar", "infiniti": "infiniti", "acura": "acura",
    "baic": "baic", "daewoo": "daewoo", "opel": "opel", "volga": "volga",
    "gac": "gac", "bestune": "bestune", "maxus": "maxus", "ssangyong": "ssangyong",
    "vw": "volkswagen", "futon": "foton", "pegeot": "peugeot", "moskovis": "moskvich",
}


def normalize_brand(value: str) -> str:
    b = (value or "").lower().strip()
    return ALIASES.get(b, b)


def normalize_model(value: str) -> str:
    m = (value or "").lower().strip()
    m = re.sub(r"\s+", " ", m)
    m = re.sub(r"^(auto|carro|coche|vehiculo)\s+", "", m)
    return m[:60]


def brand_tier(brand: str) -> str:
    b = (brand or "").lower()
    if b in PREMIUM:
        return "premium"
    if b in MID:
        return "medio"
    if b:
        return "economico"
    return "desconocido"


def to_usd(price, currency: str) -> float:
    try:
        p = float(price or 0)
    except (TypeError, ValueError):
        return 0.0
    if p <= 0:
        return 0.0
    cur = (currency or "USD").upper().replace("US$", "USD")
    return p * FX.get(cur, 1.0)

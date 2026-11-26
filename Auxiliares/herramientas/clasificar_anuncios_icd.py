#!/usr/bin/env python3
"""Clasifica los 3.958 anuncios del repo ICD y mide el impacto porcentual
de añadirlos a nuestra base. Escribe un informe en Data/repos-autos-referencias/.
"""
import csv, re, sqlite3, statistics, os
from collections import Counter

BASE = '/home/thony70807/Proyectos/El precio de moverse en Cuba'
ICD = f'{BASE}/Auxiliares/Repositorios Referencias/ICD-Mercado-Automotriz/data/raw/clasificados/revolico/anuncios.csv'
DB = f'{BASE}/Data/Revolico/revolico.sqlite'
OUT = f'{BASE}/Data/repos-autos-referencias/IMPACTO_PORCENTUAL.md'
FX = {'USD': 1.0, 'CUP': 1/930.0, 'EUR': 1000.0/930.0, 'MLC': 845.35/930.0}

EXCLUDE = re.compile(
    r"\b(moto|motocicleta|bicimoto|scooter|triciclo|bici|bicicleta|llanta|neumático|neumatico|"
    r"repuesto|accesorio|radio|pantalla|estereo|alarma|faros?|parachoques?|espejos?|amortiguador|"
    r"radiador|escatolina|alternador|arranque|empleo|chofer|alquiler|renta|servicio t[ée]cnico|"
    r"taller|lavado|kit solar|estaci[oó]n de energ[ií]a|aditamento|soporte para bicicletas)\b|"
    r"(?:vendo|se vende|venta de)\s+(?:un\s+)?(?:motor|caja|transmisi[oó]n|bater[ií]a|radiador|"
    r"alternador)\b|\bmotor suelto\b", re.I)
INCLUDE = re.compile(
    r"\b(carro|autom[oó]vil|coche|camioneta|furgoneta|cam[ií]on|autob[oú]s|microb[uú]s|microbus|"
    r"guagua|[oó]mnibus|bus|jeep|suv|pickup|chevrolet|ford|toyota|renault|nissan|honda|hyundai|"
    r"kia|mazda|vw|volkswagen|pontiac|buick|changan|dongfeng|volvo|bmw|mercedes|lexus|peugeot|"
    r"fiat|lada|moskvich|mitsubishi|geely|byd|jac|gmc|seat|skoda|daewoo|suzuki|dodge|plymouth|"
    r"audi|porsche|cadillac|jaguar|infiniti|acura|land rover|mg|foton|bestune|chery|isuzu|citroen)\b",
    re.I)


def usd(price, cur):
    try:
        p = float(price or 0)
    except (TypeError, ValueError):
        return 0.0
    if p <= 0:
        return 0.0
    return p * FX.get((cur or 'USD').upper(), 1.0)


with open(ICD, encoding='utf-8-sig', newline='') as fh:
    icd = list(csv.DictReader(fh))

con = sqlite3.connect(DB)
ours = {}
for r in con.execute('select id,es_auto,motivo_exclusion,category_name,title,price,currency,description from anuncios'):
    ours[str(r[0])] = {'es_auto': int(r[1] or 0), 'motivo': r[2] or '',
                       'cat': r[3] or '', 'title': r[4] or '',
                       'usd': usd(r[5], r[6]), 'desc': r[7] or ''}
our_autos = [v for v in ours.values() if v['es_auto'] == 1 and v['usd'] > 0]

# Clasificación de los anuncios ICD
clas = []
for r in icd:
    i = r['anuncio_id']
    if i in ours:
        es = ours[i]['es_auto']
        mot = 'nuestra base: ' + (ours[i]['motivo'] or 'auto válido')
        conf = 'cruce'
    else:
        t = ' '.join([r.get('descripcion', ''), r.get('modelo', ''), r.get('marca', '')])
        if EXCLUDE.search(t):
            es, mot, conf = 0, 'título excluido', 'regla'
        elif INCLUDE.search(t):
            es, mot, conf = 1, 'marca/modelo en título', 'regla'
        elif r.get('marca', '').strip():
            es, mot, conf = 1, 'marca declarada', 'regla'
        else:
            es, mot, conf = 0, 'sin señal suficiente', 'regla'
    r['_auto'] = es
    r['_motivo'] = mot
    r['_conf'] = conf
    r['_usd'] = usd(r.get('precio_usd') or r.get('precio_original'), r.get('moneda'))
    clas.append(r)

total = len(clas)
autos = [r for r in clas if r['_auto'] == 1]
noautos = [r for r in clas if r['_auto'] == 0]
autos_precio = [r for r in autos if r['_usd'] > 0]
nuevos = [r for r in autos_precio if r['anuncio_id'] not in ours]
solapados = [r for r in autos_precio if r['anuncio_id'] in ours]

def stats(rows):
    precios = [r['_usd'] for r in rows]
    return {
        'n': len(precios),
        'mediana': statistics.median(precios) if precios else 0,
        'media': sum(precios)/len(precios) if precios else 0,
    }

s_ours = {'n': len(our_autos), 'mediana': statistics.median([a['usd'] for a in our_autos]),
          'media': sum(a['usd'] for a in our_autos)/len(our_autos)}
s_new = stats(nuevos)
combinado = [a['usd'] for a in our_autos] + [r['_usd'] for r in nuevos]
s_comb = {'n': len(combinado), 'mediana': statistics.median(combinado),
          'media': sum(combinado)/len(combinado)}

# marcas (solo autos con precio)
brand_new = Counter((r.get('marca') or 'sin marca').lower() for r in nuevos)
brand_ours = Counter((a['title'] or '').lower() for a in [])  # no usado

# motivos de exclusión
motivos = Counter(r['_motivo'] for r in noautos)

def pct(a, b):
    return (a-b)/b*100 if b else 0

lines = []
lines.append('# Impacto porcentual de los anuncios del repo ICD\n')
lines.append('Fecha: 19/11/2026. Clasificación con las reglas de `limpiar_revolico.py` '
             'y cruce con nuestra base para los 369 anuncios ya presentes.\n')
lines.append('## 1. ¿Todos son autos?\n')
lines.append('| Clasificación | Anuncios | % |\n|---|---:|---:|')
lines.append(f'| Autos / vehículos 4+ ruedas | {len(autos):,} | {len(autos)/total*100:.1f} % |')
lines.append(f'| No autos (motos, triciclos, piezas, servicios, etc.) | {len(noautos):,} | {len(noautos)/total*100:.1f} % |')
lines.append(f'| **Total** | **{total:,}** | **100 %** |')
lines.append('\n### Motivos de exclusión (no autos)\n')
lines.append('| Motivo | Anuncios |\n|---|---:|')
for k, n in motivos.most_common(12):
    lines.append(f'| {k} | {n} |')
lines.append('\n## 2. Autos con precio utilizable\n')
lines.append('| Grupo | Autos | % del total de autos |\n|---|---:|---:|')
lines.append(f'| Con precio válido | {len(autos_precio):,} | {len(autos_precio)/len(autos)*100:.1f} % |')
lines.append(f'| Sin precio válido | {len(autos)-len(autos_precio):,} | {(len(autos)-len(autos_precio))/len(autos)*100:.1f} % |')
lines.append(f'| Ya estaban en nuestra base | {len(solapados):,} | {len(solapados)/len(autos_precio)*100:.1f} % |')
lines.append(f'| Nuevos (no estaban) | {len(nuevos):,} | {len(nuevos)/len(autos_precio)*100:.1f} % |')
lines.append('\n## 3. Qué porcentajes cambian en nuestros KPIs\n')
lines.append('| Métrica | Hoy (nuestra base) | Con los nuevos | Cambio |\n|---|---:|---:|---:|')
lines.append(f'| Tamaño de muestra | {s_ours["n"]:,} | {s_comb["n"]:,} | **+{pct(s_comb["n"], s_ours["n"]):.1f} %** |')
lines.append(f'| Precio mediano (USD) | {s_ours["mediana"]:,.0f} | {s_comb["mediana"]:,.0f} | **{pct(s_comb["mediana"], s_ours["mediana"]):+.1f} %** |')
lines.append(f'| Precio medio (USD) | {s_ours["media"]:,.0f} | {s_comb["media"]:,.0f} | **{pct(s_comb["media"], s_ours["media"]):+.1f} %** |')
lines.append(f'\nSolo los nuevos: n={s_new["n"]:,}, mediana={s_new["mediana"]:,.0f} USD, media={s_new["media"]:,.0f} USD.')
lines.append('\n## 4. Marcas más frecuentes entre los autos nuevos\n')
lines.append('| Marca | Anuncios | % de los nuevos |\n|---|---:|---:|')
for m, n in brand_new.most_common(15):
    lines.append(f'| {m} | {n} | {n/len(nuevos)*100:.1f} % |')
lines.append('\n## Nota metodológica\n')
lines.append('- La clasificación de los 369 anuncios solapados usa nuestra columna `es_auto` (auditoría real del pipeline).')
lines.append('- Para el resto se aplican las mismas reglas de título de `limpiar_revolico.py`; '
             'puede haber falsos positivos/negativos, sobre todo en títulos genéricos sin marca.')
lines.append('- Precios convertidos a USD con la TRMI informal del 18/11/2026 (930 CUP/USD).')
lines.append('- No se modificó `revolico.sqlite`: el cálculo es un escenario, no una integración.')

open(OUT, 'w', encoding='utf-8').write('\n'.join(lines))
print('\n'.join(lines))
print('\nGuardado en', OUT)

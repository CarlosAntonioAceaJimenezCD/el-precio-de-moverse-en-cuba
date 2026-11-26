#!/usr/bin/env python3
"""Cruza las preferencias declaradas en encuestas/entrevistas con los modelos
del catálogo formal. Genera Data/repos-autos-referencias/PRODUCTOS_VS_GUSTOS.md
"""
import sqlite3, csv, json, collections, os

BASE = '/home/thony70807/Proyectos/El precio de moverse en Cuba'
DB = f'{BASE}/Data/repos-autos-referencias/referencias_autos.sqlite'
OUT = f'{BASE}/Data/repos-autos-referencias/PRODUCTOS_VS_GUSTOS.md'
EUR_USD = 1000.0 / 930.0  # TRMI informal 18/11/2026

con = sqlite3.connect(DB)

# --- Preferencias declaradas -------------------------------------------------
cols = [d[1] for d in con.execute('pragma table_info(encuesta_demanda_33)')]
survey = [dict(zip(cols, r)) for r in con.execute('select * from encuesta_demanda_33')]
cmodelo = next(c for c in cols if c == '_qué_modelo_')
cpref = next(c for c in cols if 'preferencia_de_tipo' in c)
cwev = next(c for c in cols if 'eléctricos___cuánto' in c)
cwc = next(c for c in cols if 'combustible__cuánto' in c)
cint = next(c for c in cols if 'le_interesaría_comprar_un_vehículo_en_el_futuro' in c)

modelos = collections.Counter()
for r in survey:
    m = (r.get(cmodelo) or '').strip().lower()
    if not m or m in ('aun no me decido', 'no me interesa', 'no se aun'):
        continue
    m = m.replace('betsune', 'bestune').replace('jooye', 'joyee')
    modelos[m] += 1

entrev = collections.Counter()
for (raw,) in con.execute('select respuestas from entrevistas_mercado_30'):
    if not raw:
        continue
    try:
        d = json.loads(raw)
    except Exception:
        continue
    for b in (d.get('marcas_modernas_observadas') or []):
        entrev[b] += 1

# --- Catálogo formal ---------------------------------------------------------
prod = []
for marca, modelo, prop, precio, moneda, precio_usd in con.execute(
        'select marca,modelo,propulsion,precio_original,moneda,precio_usd from comercializadoras_icd'):
    try:
        p = float(precio)
    except (TypeError, ValueError):
        continue
    if (moneda or '').upper() == 'EUR':
        p *= EUR_USD
    prod.append({'marca': marca, 'modelo': modelo, 'prop': prop or '',
                 'usd': p, 'moneda': moneda})
# Añadir Womy (Toyota) que no está en la tabla unificada
for empresa, tipo, marca, modelo, anio, precio, moneda, pago, prov in con.execute(
        'select * from cat_womy'):
    try:
        p = float(precio)
    except (TypeError, ValueError):
        continue
    if (moneda or '').upper() == 'EUR':
        p *= EUR_USD
    prod.append({'marca': marca, 'modelo': modelo, 'prop': '', 'usd': p, 'moneda': moneda})

def tipo_prop(modelo: str, prop: str) -> str:
    """Separa estado (nuevo/usado) de propulsion, infiriendo la de los modelos ICD."""
    m = (modelo or '').lower()
    p = (prop or '').lower()
    estado = 'usado' if ('segunda mano' in m or 'usado' in m) else 'nuevo'
    if 'phev' in m or 'phev' in p or 'enchufable' in p:
        return f'{estado} · híbrido enchufable'
    if 'reev' in m or 'reev' in p:
        return f'{estado} · eléctrico (extensor)'
    if 'hev' in m and 'phev' not in m:
        return f'{estado} · híbrido'
    if m.endswith('-ev') or '-ev ' in m or 'eléctric' in p or 'electric' in p:
        return f'{estado} · eléctrico'
    if 'diésel' in p or 'diesel' in p:
        return f'{estado} · diésel'
    if 'gasolina' in p:
        return f'{estado} · gasolina'
    return f'{estado} · {prop or "combustión"}'


prod.sort(key=lambda x: x['usd'])

L = []
L.append('# ¿Hay productos que se ajusten al gusto de las personas?\n')
L.append('Cruce entre lo declarado en la encuesta de 33 personas y las 38 entrevistas '
         '(30 + 8) y los modelos del catálogo formal de comercializadoras.\n')
L.append('## 1. Lo que pide la gente\n')
L.append('### Marcas modernas observadas en 30 entrevistas\n')
L.append('| Marca | Menciones | % de 30 |\n|---|---:|---:|')
for b, n in entrev.most_common():
    L.append(f'| {b} | {n} | {n/30*100:.0f} % |')
L.append('\n### Modelos mencionados en la encuesta (pregunta abierta)\n')
L.append('| Modelo | Menciones |\n|---|---:|')
for m, n in modelos.most_common():
    L.append(f'| {m} | {n} |')
L.append('\n### Preferencia y disposición de pago (encuesta)\n')
pref = collections.Counter((r.get(cpref) or '').strip() for r in survey)
PREF = {'1': 'Combustión', '2': 'Eléctrico', '3': 'Híbrido', '4': 'Indiferente / no sabe'}
L.append('| Preferencia | Personas | % de 33 |\n|---|---:|---:|')
for k, n in pref.most_common():
    L.append(f'| {PREF.get(k, k or "sin respuesta")} | {n} | {n/33*100:.0f} % |')
interesados_rows = [r for r in survey if (r.get(cint) or '').strip() == '1']
pref_i = collections.Counter((r.get(cpref) or '').strip() for r in interesados_rows)
interesados = sum(n for k, n in pref_i.items() if k in ('1', '2', '3'))
L.append(f'\nEntre las {len(interesados_rows)} personas a las que les interesaría comprar '
         f'({interesados} con preferencia concreta): '
         f'eléctrico {pref_i.get("2",0)} ({pref_i.get("2",0)/interesados*100:.0f} %), '
         f'combustión {pref_i.get("1",0)} ({pref_i.get("1",0)/interesados*100:.0f} %), '
         f'híbrido {pref_i.get("3",0)} ({pref_i.get("3",0)/interesados*100:.0f} %).\n')
L.append('Disposición a pagar por un **eléctrico** (18 respuestas):')
L.append('| Rango | Personas |\n|---|---:|')
L.append('| 1.000–3.000 USD | 11 |')
L.append('| 3.000–4.000 USD | 5 |')
L.append('| 5.000–10.000 USD | 1 |')
L.append('| 10.000–20.000 USD | 1 |')
L.append('\n**16 de 18 (89 %) no pagarían más de 4.000 USD por un eléctrico.**\n')
L.append('Disposición a pagar por un **combustión** (10 respuestas):')
L.append('| Rango | Personas |\n|---|---:|')
L.append('| 3.000–4.000 USD | 1 |')
L.append('| 4.000–5.000 USD | 2 |')
L.append('| 5.000–10.000 USD | 4 |')
L.append('| 10.000–20.000 USD | 1 |')
L.append('| 20.000+ USD | 2 |')

L.append('\n## 2. Lo que vende el catálogo formal (precio en USD, TRMI 930)\n')
L.append('| Marca | Modelo | Estado y propulsión | Precio USD |\n|---|---|---|---:|')
for p in prod:
    if p['usd'] > 60000:
        continue
    L.append(f'| {p["marca"]} | {p["modelo"]} | {tipo_prop(p["modelo"], p["prop"])} | {p["usd"]:,.0f} |')

L.append('\n## 3. Cruce: qué productos encajan y cuáles no\n')
L.append('| Producto | Precio USD | Encaja con | Veredicto |\n|---|---:|---|---|')
L.append('| **Bestune Pony** | 10.215 | Modelo más mencionado (7) y eléctrico más barato | **El mejor encaje**, pero 2,6× el techo de 4.000 USD |')
L.append('| **Dongfeng Shine / Shine GS** | 17.097–19.247 | Combustión 10.000–20.000; un encuestado nombró "Shine E1" | Encaja en precio y uso |')
L.append('| **MG3 / MG5 / MG ZS** | 15.967–16.963 | Combustión 10.000–20.000 | Encaja en precio, **pero el mecánico dice que MG es la marca con menos repuestos** |')
L.append('| **DFSK Glory 330 S** | 19.805 | Combustión 10.000–20.000; DFSK observada 3 veces | Encaja justo en el techo |')
L.append('| **Bestune Joyee 03** | 25.177 | Eléctrico 10.000–20.000 (solo 1 persona) | Fuera del presupuesto de 16 de 18 |')
L.append('| **Foton View G5** | 26.129 | Foton es la 3.ª marca más observada (14/30) | Precio por encima de casi todos |')
L.append('| **Toyota Levin** | 22.380 | Toyota: fiabilidad valorada; 1 mención | Cerca, pero fuera del rango 5.000–10.000 |')
L.append('| **Mercedes-Benz Clase A** | 45.054 | Mercedes observada 5 veces | Solo para el segmento de mayor ingreso |')

L.append('\n## 4. Los tres huecos del mercado\n')
L.append('1. **Kia y Hyundai no están en el catálogo formal.** Son las marcas más '
         'observadas (28 y 25 de 30 entrevistas) y las más valoradas por repuestos y '
         'reparación, pero solo se consiguen usadas o importadas. El gusto mayoritario '
         'no tiene oferta oficial.')
L.append('2. **No hay ningún eléctrico por debajo de 4.000 USD.** El más barato es el '
         'Bestune Pony (~10.215 USD), aun así el que más gente nombra. La barrera no es '
         'el deseo: es el precio.')
L.append('3. **No hay combustión nueva por debajo de ~16.000 USD.** Quien puede pagar '
         '5.000–10.000 USD (4 de 10) queda fuera del catálogo formal y empujado al usado.')

L.append('\n## 5. Conclusión\n')
L.append('Sí hay productos que se ajustan, pero **el encaje es parcial y con una paradoja**: '
         'lo que la gente quiere (Kia, Hyundai, Bestune Pony) no es lo que la oferta oficial '
         'vende; y lo que la oferta oficial vende a precio alcanzable (MG, Dongfeng Shine) '
         'no siempre coincide con lo que los mecánicos recomiendan por repuestos. '
         'El producto que mejor combina deseo + precio es el **Bestune Pony**, seguido del '
         '**Dongfeng Shine** para combustión. El resto del gusto se cubre en el mercado usado.')

open(OUT, 'w', encoding='utf-8').write('\n'.join(L))
print('\n'.join(L))
print('\nGuardado en', OUT)

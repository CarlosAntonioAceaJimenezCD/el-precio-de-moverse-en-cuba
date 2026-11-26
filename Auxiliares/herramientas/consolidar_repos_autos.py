#!/usr/bin/env python3
"""Consolida las bases de datos de los repositorios de referencia sobre el
mercado automotor cubano, descartando duplicados y registrando procedencia.

Salida: Data/repos-autos-referencias/referencias_autos.sqlite
"""
import csv, json, os, re, shutil, sqlite3

BASE = '/home/thony70807/Proyectos/El precio de moverse en Cuba'
REPOS = os.path.join(BASE, 'Auxiliares/Repositorios Referencias')
OUT = os.path.join(BASE, 'Data/repos-autos-referencias')
DB = os.path.join(OUT, 'referencias_autos.sqlite')

MA = os.path.join(REPOS, 'Mercado-automotriz')
ICD = os.path.join(REPOS, 'ICD-Mercado-Automotriz')
AXC = os.path.join(REPOS, 'AutosxCuba')
PMA = os.path.join(REPOS, 'Proyecto-Mercado-Automotriz')
ACU = os.path.join(REPOS, 'autos-cuba')

os.makedirs(os.path.join(OUT, 'documentacion'), exist_ok=True)
os.makedirs(os.path.join(OUT, 'audios'), exist_ok=True)

if os.path.exists(DB):
    os.remove(DB)
con = sqlite3.connect(DB)
con.execute('pragma journal_mode=wal')
provenance = []


def read_csv(path):
    with open(path, encoding='utf-8-sig', newline='') as fh:
        r = csv.reader(fh)
        header = next(r)
        rows = [row for row in r if any(c.strip() for c in row)]
    header = [re.sub(r'[^0-9A-Za-zÁÉÍÓÚáéíóúÑñ_]', '_', h.strip()) or 'col' for h in header]
    seen, cols = {}, []
    for i, h in enumerate(header):
        h = h.lower()
        if h in seen:
            seen[h] += 1
            h = f'{h}_{seen[h]}'
        else:
            seen[h] = 0
        cols.append(h)
    return cols, rows


def add_table(name, path=None, cols=None, rows=None, note='', key=None):
    """Crea una tabla y registra su procedencia."""
    if path:
        cols, rows = read_csv(path)
    cols = cols or []
    rows = rows or []
    # convertir a texto para evitar tipos mixtos
    clean = [[str(v) if v is not None else '' for v in row] for row in rows]
    coldef = ', '.join(f'"{c}" TEXT' for c in cols)
    con.execute(f'CREATE TABLE "{name}" ({coldef})')
    if cols:
        ph = ', '.join('?' for _ in cols)
        con.executemany(f'INSERT INTO "{name}" VALUES ({ph})', clean)
    con.commit()
    provenance.append((name, os.path.relpath(path, REPOS) if path else '(generado)',
                       len(clean), key or '', note))
    print(f'  {name:36} {len(clean):5} filas')


def copy_doc(src, subdir='documentacion'):
    if not os.path.exists(src):
        print('  FALTA:', src)
        return
    dst = os.path.join(OUT, subdir, os.path.basename(src))
    shutil.copy2(src, dst)


print('== Anuncios de Revolico (ICD-Mercado-Automotriz) ==')
with sqlite3.connect(os.path.join(BASE, 'Data/Revolico/revolico.sqlite')) as rc:
    nuestros = {str(r[0]) for r in rc.execute('select id from autos')}

cols, rows = read_csv(os.path.join(ICD, 'data/raw/clasificados/revolico/anuncios.csv'))
idx = cols.index('anuncio_id')
cols += ['en_nuestro_proyecto']
rows = [r + ['1' if r[idx] in nuestros else '0'] for r in rows]
add_table('anuncios_revolico_icd', cols=cols, rows=rows,
          key='anuncio_id', note='3.958 anuncios; 369 ya están en Data/Revolico/revolico.sqlite')
add_table('verificacion_anuncios_icd',
          os.path.join(ICD, 'data/raw/clasificados/revolico/verificacion_anuncios.csv'),
          key='anuncio_id', note='estado HTTP de cada anuncio')
add_table('anuncios_limpios_icd',
          os.path.join(ICD, 'data/interim/anuncios_limpios.csv'),
          key='anuncio_id', note='idéntico a data/processed/mercado_havana.csv (duplicado descartado)')

print('== Catálogos de comercializadoras ==')
for name, rel, note in [
    ('cat_mcv', 'data/raw/mcv_commercial_2026-03-03.csv', 'duplicado en autos-cuba, conservada una copia'),
    ('cat_dongfeng_nwi', 'data/raw/dongfeng_nwi_commercial.csv', 'duplicado en autos-cuba, conservada una copia'),
    ('cat_womy', 'data/raw/womy_catalog_july_2026.csv', 'duplicado en autos-cuba, conservada una copia'),
    ('cat_bdcone', 'data/raw/bdcone_commercial.csv', 'duplicado en autos-cuba, conservada una copia'),
]:
    add_table(name, os.path.join(MA, rel), note=note)
add_table('comercializadoras_icd',
          os.path.join(ICD, 'data/processed/comercializadoras.csv'),
          note='catálogo unificado 83 filas')
add_table('catalogo_dongfeng_icd',
          os.path.join(ICD, 'data/raw/comercializadoras/catalogos/catalogo_dongfeng.csv'))
add_table('catalogo_bdcone_icd',
          os.path.join(ICD, 'data/raw/comercializadoras/catalogos/catalogo_bdcone.csv'))
add_table('catalogo_cimex_icd',
          os.path.join(ICD, 'data/raw/comercializadoras/catalogos/catalogo_CIMEX.csv'))
add_table('estado_comercializadoras_icd',
          os.path.join(ICD, 'data/raw/comercializadoras/estado_comercializadoras.csv'))
add_table('tasas_cambio_icd',
          os.path.join(ICD, 'data/tasas_cambio/tasas_usd.csv'))
add_table('regresion_dataset_icd',
          os.path.join(ICD, 'data/processed/regresion_dataset.csv'))

print('== Encuesta de demanda (Google Forms, 33 respuestas) ==')
form_files = sorted(
    [p for p in os.listdir(os.path.join(MA, 'data/raw')) if 'ESTUDIO DEL MERCADO' in p and p.endswith('.csv')],
    key=lambda p: int(re.search(r'\((\d+)\)', p).group(1)))
ultimo = os.path.join(MA, 'data/raw', form_files[-1])
add_table('encuesta_demanda_33', ultimo,
          note='snapshot final (9) del Google Forms; 6 snapshots anteriores son versiones parciales')
# snapshots intermedios: se copian como documentación, no se importan
for p in form_files:
    copy_doc(os.path.join(MA, 'data/raw', p))

print('== Entrevistas ==')
txt = open(os.path.join(ICD, 'data/raw/entrevistas/Entrevistas.txt'), encoding='utf-8').read()
ent, cur = [], None
for line in txt.splitlines():
    m = re.match(r'\s*Entrevista\s+(\d+)', line)
    if m:
        if cur:
            ent.append(cur)
        cur = {'entrevista': m.group(1)}
        continue
    m = re.match(r'\s*(\d+)\s*-\s*(.*)', line)
    if m and cur:
        cur[f'p{m.group(1)}'] = m.group(2).strip()
if cur:
    ent.append(cur)
cols = sorted({k for e in ent for k in e}, key=lambda k: (k != 'entrevista', k))
rows = [[e.get(c, '') for c in cols] for e in ent]
add_table('entrevistas_icd', cols=cols, rows=rows, key='entrevista',
          note='30 entrevistas transcritas y anonimizadas (combustible, mantenimiento, repuestos)')

pma_path = os.path.join(PMA, 'data/processed/entrevistas.json')
data = json.load(open(pma_path, encoding='utf-8'))
cols = sorted({k for d in data for k in d})
rows = []
for d in data:
    r = []
    for c in cols:
        v = d.get(c, '')
        r.append(json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else str(v))
    rows.append(r)
add_table('entrevistas_mercado_30', cols=cols, rows=rows, key='id_entrevista',
          note='30 entrevistas declarativas anónimas (percepción de eléctricos y clásicos)')
add_table('entrevistas_estructuradas_autosxcuba',
          os.path.join(AXC, 'entrevistas_estructuradas.csv'),
          note='8 registros: entrevistas presenciales y chats de Telegram')

print('== Dataset de AutosxCuba ==')
add_table('dataset_autosxcuba_157',
          os.path.join(AXC, 'DATASET_COMPLETO_MEJORADO.csv'),
          note='versión más completa; DATASET_PARA_GRAFICOS es duplicado exacto')
add_table('dataset_oficial_autosxcuba_157',
          os.path.join(AXC, 'PROYECTO_AUTOS_DATASET_OFICIAL.csv'),
          note='72 claves coinciden con el dataset mejorado; conservado como fuente alterna')
add_table('revolico_80_autosxcuba', os.path.join(AXC, 'revolico_80_anuncios.csv'))
add_table('telegram_autosxcuba', os.path.join(AXC, 'telegram_autos.csv'))
add_table('autocubana_autosxcuba', os.path.join(AXC, 'autocubana_autos_limpio.csv'))
add_table('dongfeng_catalogo_autosxcuba', os.path.join(AXC, 'dongfeng_cuba_catalogo.csv'))

con.execute('''CREATE TABLE provenancia (
    tabla TEXT, archivo_origen TEXT, filas INTEGER, clave TEXT, nota TEXT)''')
con.executemany('INSERT INTO provenancia VALUES (?,?,?,?,?)', provenance)
con.commit()

# Documentación metodológica
print('== Documentación ==')
for src in [
    os.path.join(ICD, 'docs/instrumentos/encuesta.md'),
    os.path.join(ICD, 'docs/instrumentos/entrevista.md'),
    os.path.join(ICD, 'data/raw/entrevistas/Entrevistas.txt'),
    os.path.join(PMA, 'docs/entrevistas.md'),
    os.path.join(PMA, 'docs/interview_methodology.md'),
    os.path.join(PMA, 'docs/mercado_formal_methodology.md'),
    os.path.join(ACU, 'docs/encuesta_compradores.md'),
    os.path.join(ACU, 'docs/contexto_mercado.md'),
    os.path.join(MA, 'docs/methodology/Explicacion_pasos_seguidos_4_11_2026_metodologia_oficial_corregido.docx'),
    os.path.join(MA, 'docs/methodology/Anexo_2_Cuestionario final_demanda_para form_google_.docx'),
    os.path.join(MA, 'docs/methodology/cuestionario final_demanda_para form_google.docx'),
    os.path.join(MA, 'docs/methodology/leyenda_para_respuestas del cuestionario.docx'),
    os.path.join(MA, 'data/processed/INFORME_4_11_2026_con_interpretaciones.docx'),
]:
    copy_doc(src)

for f in os.listdir(os.path.join(MA, 'data/processed/tablas_gráficas')):
    copy_doc(os.path.join(MA, 'data/processed/tablas_gráficas', f))
copy_doc(os.path.join(MA, 'data/raw/prefrencias_propulsión_encuesta.xlsx'))

print('== Audios de entrevistas ==')
for f in os.listdir(os.path.join(ICD, 'data/raw/entrevistas/Audios')):
    copy_doc(os.path.join(ICD, 'data/raw/entrevistas/Audios', f), 'audios')

print('\nListo:', DB)
print('Tablas:', con.execute("select count(*) from sqlite_master where type='table'").fetchone()[0])
con.close()

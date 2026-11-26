#!/usr/bin/env python3
"""Genera un panel HTML único, liviano y autocontenido.

Reúne gráficos del mercado, mapa de infraestructura y estado de circuitos en
un solo archivo sin dependencias externas (vanilla JS + SVG). Se regenera
desde los datos vigentes, así que se actualiza solo cuando hay información
nueva. La fecha mostrada sale de los propios datos, no del reloj.

Uso:
    python generar_dashboard.py [--solo-si-cambia] [--salida RUTA]
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAPAS = ROOT / "Data/mapas"
CIR = MAPAS / "circuitos"
TABLAS = ROOT / "Data/analisis_rentabilidad/outputs/tables"
SALIDA = ROOT / "Data/dashboard.html"
HUELLA = ROOT / "Data/_state/dashboard_fingerprint.json"

COLORES = {
    "gasolinera": "#222222",
    "estacion_carga": "#1b9e77",
    "concesionario": "#1f5fa9",
    "taller": "#d62728",
}
COLOR_CIRCUITO = {
    "sin luz": "#d62728",
    "mixto": "#f28e2b",
    "sin dato": "#9e9e9e",
    "no relevante": "#bbbbbb",
}


def filas_csv(nombre: str) -> list[dict]:
    ruta = TABLAS / nombre
    if not ruta.exists():
        return []
    with ruta.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def bd(ruta: Path) -> sqlite3.Connection | None:
    if not ruta.exists():
        return None
    return sqlite3.connect(f"file:{ruta}?mode=ro", uri=True, timeout=20)


def rdp(puntos: list[list[float]], eps: float) -> list[list[float]]:
    """Simplifica una polilínea con Ramer-Douglas-Peucker."""
    if len(puntos) < 3:
        return puntos

    def dist(p: list[float], a: list[float], b: list[float]) -> float:
        dx, dy = b[0] - a[0], b[1] - a[1]
        if dx == 0 and dy == 0:
            return math.hypot(p[0] - a[0], p[1] - a[1])
        t = max(0.0, min(1.0, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy)))
        return math.hypot(p[0] - (a[0] + t * dx), p[1] - (a[1] + t * dy))

    idx, mejor = 0, 0.0
    for i in range(1, len(puntos) - 1):
        d = dist(puntos[i], puntos[0], puntos[-1])
        if d > mejor:
            idx, mejor = i, d
    if mejor > eps:
        return rdp(puntos[: idx + 1], eps)[:-1] + rdp(puntos[idx:], eps)
    return [puntos[0], puntos[-1]]


def redondear(p: list[float]) -> list[float]:
    return [round(p[0], 5), round(p[1], 5)]


def fecha_datos(conexiones: list[sqlite3.Connection | None]) -> str:
    fechas: list[str] = []
    for nombre in ("listings_clean.parquet",):
        ruta = ROOT / "Data/analisis_rentabilidad/data" / nombre
        if ruta.exists():
            fechas.append(ruta.stat().st_mtime)
    for c in conexiones:
        if c is None:
            continue
        for tabla, col in (("elementos", "scraped_at"), ("estado_circuito", "fecha_utc"), ("mensajes", "capturado_utc")):
            try:
                v = c.execute(f"select max({col}) from {tabla}").fetchone()[0]
                if v:
                    fechas.append(str(v)[:10])
            except sqlite3.Error:
                pass
    if not fechas:
        return "fecha desconocida"
    texto = max(str(x)[:10] for x in fechas)
    try:
        anio, mes, dia = texto.split("-")
        return f"{dia}/{mes}/{anio}"
    except ValueError:
        return texto


def recoger_datos() -> dict:
    ce = bd(MAPAS / "mapa_elementos.sqlite")
    cc = bd(MAPAS / "circuitos_estado.sqlite")

    cuba: list[list[float]] = []
    Geo = MAPAS / "cuba.geo.json"
    if Geo.exists():
        geo = json.loads(Geo.read_text(encoding="utf-8"))
        anillo = geo["features"][0]["geometry"]["coordinates"][0]
        cuba = [redondear([p[1], p[0]]) for p in anillo[::2]]

    elementos: list[list] = []
    if ce is not None:
        for r in ce.execute("select tipo,nombre,lat,lon,direccion,estado,fuente from elementos where lat is not null and lon is not null order by tipo,nombre"):
            elementos.append([
                r[0], (r[1] or "")[:60], round(r[2], 5), round(r[3], 5),
                (r[4] or "")[:70], (r[5] or "")[:30], (r[6] or "")[:30],
            ])

    circuitos: list[list] = []
    estados_por_circuito: dict[str, str] = {}
    if cc is not None:
        for r in cc.execute("select circuito,estado,fecha_utc from estado_circuito order by circuito"):
            codigo, estado, fecha = r
            estados_por_circuito[codigo] = estado
            circuitos.append([codigo, estado, str(fecha)[:16]])
        fechas_mensaje = cc.execute("select max(capturado_utc) from mensajes").fetchone()[0]
        if fechas_mensaje:
            for fila in circuitos:
                fila[2] = str(fechas_mensaje)[:16]

    ubicaciones: dict[str, list[str]] = {}
    habana = CIR / "circuitos_habana.json"
    if habana.exists():
        for x in json.loads(habana.read_text(encoding="utf-8")):
            ubicaciones[x["circuito"]] = [x.get("municipio", ""), x.get("ubicacion", "")]
    for fila in circuitos:
        fila.extend(ubicaciones.get(fila[0], ["", ""]))

    zonas: dict[str, list] = {}
    zonas_path = CIR / "circuitos_zonas.json"
    if zonas_path.exists():
        crudo = json.loads(zonas_path.read_text(encoding="utf-8"))["zonas"]
        for codigo, anillos in crudo.items():
            if codigo not in estados_por_circuito:
                continue
            simplificados = []
            for anillo in anillos[:3]:
                # Cada anillo llega como [ [lat, lon, lat, lon, ...] ] (lista plana).
                plano = anillo[0] if anillo and isinstance(anillo[0], (list, tuple)) else anillo
                pts = [[round(plano[i], 5), round(plano[i + 1], 5)] for i in range(0, len(plano) - 1, 6)]
                if len(pts) >= 4:
                    simp = rdp(pts, 0.0006)
                    if len(simp) >= 4:
                        simplificados.append(simp)
            if simplificados:
                zonas[codigo] = simplificados

    precios: list[float] = []
    try:
        import pyarrow.parquet as pq  # opcional: solo si está disponible
        tabla = pq.read_table(ROOT / "Data/analisis_rentabilidad/data/listings_clean.parquet", columns=["price_usd"])
        precios = [float(x) for x in tabla.column("price_usd").to_pylist() if x is not None and 200 <= float(x) <= 250000]
    except Exception:
        for nombre in ("gap_usado_nuevo.csv", "anomalias.csv", "infravalorados.csv"):
            for r in filas_csv(nombre):
                try:
                    v = float(r.get("price_usd", ""))
                    if 200 <= v <= 250000:
                        precios.append(v)
                except (ValueError, TypeError):
                    pass
    hist: list[list[int]] = []
    if precios:
        ancho = 5000
        maximo = int(max(precios) // ancho) + 1
        conteo = [0] * maximo
        for v in precios:
            conteo[min(int(v // ancho), maximo - 1)] += 1
        hist = [[i * ancho, n] for i, n in enumerate(conteo) if n]

    marcas = [[r["brand"], int(float(r["n"])), round(float(r["mediana"]))] for r in filas_csv("por_marca.csv")[:15]]
    canales = [[r["canal"], r["source_type"], int(r["anuncios"]), round(float(r["mediana_usd"]))] for r in filas_csv("kpis_canal.csv")]
    kpis = [[r["metrica"], r["valor"]] for r in filas_csv("kpis.csv")]

    datos = {
        "fecha": fecha_datos([ce, cc]),
        "kpis": kpis,
        "canales": canales,
        "marcas": marcas,
        "hist": hist,
        "elementos": elementos,
        "circuitos": circuitos,
        "zonas": zonas,
        "cuba": cuba,
        "colores": COLORES,
        "color_circuito": COLOR_CIRCUITO,
    }
    if ce:
        ce.close()
    if cc:
        cc.close()
    return datos


def huella_actual(datos: dict) -> dict:
    return {
        "elementos": len(datos["elementos"]),
        "circuitos": len(datos["circuitos"]),
        "zonas": len(datos["zonas"]),
        "hist": len(datos["hist"]),
        "kpis": str(datos["kpis"]),
        "fecha": datos["fecha"],
    }


PLANTILLA = r"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Panel interactivo — El precio de moverse en Cuba</title>
<style>
:root{--bg:#0f1419;--caja:#1a222b;--tx:#e8edf2;--mut:#9fb0bf;--borde:#2c3945;--ac:#4ea3ff}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}
header{padding:18px 22px;border-bottom:1px solid var(--borde)}h1{margin:0 0 4px;font-size:1.25rem}.fecha{color:var(--mut);font-size:.85rem}
nav{display:flex;gap:6px;flex-wrap:wrap;padding:10px 22px;border-bottom:1px solid var(--borde)}
button.tab{background:transparent;color:var(--mut);border:1px solid var(--borde);border-radius:8px;padding:7px 13px;cursor:pointer;font:inherit}
button.tab[aria-selected="true"]{background:var(--ac);color:#07121f;border-color:var(--ac);font-weight:600}
main{padding:18px 22px;max-width:1400px;margin:auto}.seccion{display:none}.seccion.activa{display:block}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-bottom:18px}
.card{background:var(--caja);border:1px solid var(--borde);border-radius:10px;padding:12px}.card b{display:block;font-size:1.3rem;color:var(--ac)}.card span{color:var(--mut);font-size:.78rem}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:14px}
.caja{background:var(--caja);border:1px solid var(--borde);border-radius:10px;padding:14px;min-width:0}.caja h2{font-size:1rem;margin:0 0 10px}
svg{width:100%;height:auto;display:block;background:#111820;border-radius:6px;touch-action:none}
.capas{display:flex;gap:12px;flex-wrap:wrap;margin:8px 0;font-size:.85rem}.capas label{cursor:pointer}
input[type=search]{width:100%;background:#111820;border:1px solid var(--borde);color:var(--tx);padding:8px;border-radius:6px;margin-bottom:8px}
#ficha{position:fixed;right:0;top:0;bottom:0;width:min(340px,90vw);background:#131c25;border-left:1px solid var(--borde);padding:18px;transform:translateX(105%);transition:transform .2s;overflow:auto;z-index:5}
#ficha.abierta{transform:none}#ficha h3{margin-top:0;font-size:1.05rem}#ficha button{background:var(--borde);color:var(--tx);border:0;border-radius:6px;padding:5px 10px;cursor:pointer}
.barra{cursor:pointer}.barra:hover{filter:brightness(1.35)}.punto{cursor:pointer}.punto:focus{outline:2px solid #fff}
.nota{color:var(--mut);font-size:.78rem;margin-top:8px}footer{padding:20px 22px;color:var(--mut);font-size:.8rem;border-top:1px solid var(--borde)}
@media(max-width:600px){main{padding:12px}nav{padding:8px 12px}header{padding:14px 12px}}
</style></head><body>
<header><h1>El precio de moverse en Cuba · Panel interactivo</h1>
<div class="fecha">Datos actualizados: __FECHA__ · funciona sin internet</div></header>
<nav role="tablist">
<button class="tab" role="tab" aria-selected="true" data-s="resumen">Resumen</button>
<button class="tab" role="tab" aria-selected="false" data-s="graficos">Gráficos</button>
<button class="tab" role="tab" aria-selected="false" data-s="servicios">Mapa de servicios</button>
<button class="tab" role="tab" aria-selected="false" data-s="circuitos">Circuitos eléctricos</button>
</nav>
<main>
<section id="resumen" class="seccion activa"><div class="cards" id="cards"></div>
<div class="caja"><h2>Cómo leer este panel</h2><p>Los números, gráficos y mapas se regeneran solos con cada actualización de los datos. Pasa el cursor sobre un punto o barra para ver el detalle; haz clic para abrir la ficha. En los mapas puedes arrastrar y usar la rueda del ratón para acercar.</p><p class="nota">Fuentes: anuncios de compraventa, catálogos de concesionarios, ONEI y canal público de la Empresa Eléctrica de La Habana. El panel es un complemento del informe y el storytelling.</p></div></section>
<section id="graficos" class="seccion"><div class="grid">
<div class="caja"><h2>Distribución de precios (USD)</h2><svg id="g-hist" viewBox="0 0 600 260" role="img" aria-label="Histograma de precios"></svg></div>
<div class="caja"><h2>Marcas más frecuentes</h2><svg id="g-marcas" viewBox="0 0 600 320" role="img" aria-label="Marcas más frecuentes"></svg><p class="nota">Haz clic en una barra para resaltarla.</p></div>
<div class="caja"><h2>Mercado local e importación</h2><svg id="g-canales" viewBox="0 0 600 220" role="img" aria-label="Comparación por canal"></svg></div>
</div></section>
<section id="servicios" class="seccion"><div class="caja">
<input type="search" id="buscar-serv" placeholder="Buscar por nombre o dirección…" aria-label="Buscar servicio">
<div class="capas" id="capas-serv"></div>
<svg id="mapa-serv" viewBox="0 0 1100 520" role="img" aria-label="Mapa de gasolineras, carga, concesionarios y talleres"></svg>
<p class="nota">Puntos geolocalizados de la base de infraestructura. Las capas se pueden activar o desactivar.</p></div></section>
<section id="circuitos" class="seccion"><div class="caja">
<input type="search" id="buscar-cir" placeholder="Buscar circuito o municipio…" aria-label="Buscar circuito">
<div class="capas" id="capas-cir"></div>
<div class="grid"><svg id="mapa-cir" viewBox="0 0 1100 520" role="img" aria-label="Mapa de circuitos"></svg>
<div><svg id="lista-cir" viewBox="0 0 360 520" role="img" aria-label="Lista de circuitos"></svg></div></div>
<p class="nota">Zonas aproximadas a partir de puntos conocidos; no son límites oficiales. El estado viene de los mensajes públicos de la eléctrica.</p></div></section>
</main>
<aside id="ficha" aria-live="polite"><button id="cerrar" aria-label="Cerrar ficha">Cerrar ✕</button><div id="ficha-contenido"></div></aside>
<footer>Proyecto <b>El precio de moverse en Cuba</b> · datos verificables, actualización automática · <span id="pie-fecha"></span></footer>
<script id="datos" type="application/json">__DATOS__</script>
<script>
const D=JSON.parse(document.getElementById('datos').textContent);
const NS='http://www.w3.org/2000/svg';
const fmt=n=>new Intl.NumberFormat('es-CU').format(Math.round(n));
function nodo(t,a={},txt){const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);if(txt!=null)e.textContent=txt;return e}
const proyecto=(lat,lon)=>[ (lon+85)*100, (24-lat)*100 ];

document.querySelectorAll('.tab').forEach(b=>b.onclick=()=>{
  document.querySelectorAll('.tab').forEach(x=>x.setAttribute('aria-selected',x===b?'true':'false'));
  document.querySelectorAll('.seccion').forEach(s=>s.classList.toggle('activa',s.id===b.dataset.s));
});
document.getElementById('pie-fecha').textContent=D.fecha;

// Resumen
const KPIS={anuncios_totales:'Anuncios limpios',anuncios_locales:'Mercado local',anuncios_importacion:'Importación',
 marcas_distintas:'Marcas',precio_mediano_usd:'Mediana USD',km_medianos:'Km medianos',antiguedad_media:'Antigüedad',autos_revolico:'Autos únicos'};
const cards=document.getElementById('cards');
for(const [k,v] of D.kpis){ if(!(k in KPIS))continue; const c=document.createElement('div');c.className='card';
 c.innerHTML='<b>'+v+'</b><span>'+KPIS[k]+'</span>';cards.appendChild(c)}

// Graficos
function escala(vals,w,h){const m=Math.max(...vals,1);return v=>h-(v/m)*(h-30)}
function ejes(svg,w,h){svg.appendChild(nodo('line',{x1:35,y1:h-20,x2:w-10,y2:h-20,stroke:'#456'}));}
function histograma(){const svg=document.getElementById('g-hist');if(!D.hist.length){svg.appendChild(nodo('text',{x:20,y:30,fill:'#9fb0bf'},'Sin datos'));return}
 const w=600,h=260,y=escala(D.hist.map(x=>x[1]),w,h),bw=(w-50)/D.hist.length;
 D.hist.forEach(([ini,cnt],i)=>{const alt=h-20-y(cnt);const r=nodo('rect',{x:35+i*bw,y:y(cnt),width:Math.max(1,bw-1),height:alt,fill:'#4ea3ff',class:'barra'},'');
  r.appendChild(nodo('title',{},fmt(ini)+'–'+(ini+5000)+' USD: '+cnt+' anuncios'));svg.appendChild(r)});
 ejes(svg,w,h);svg.appendChild(nodo('text',{x:35,y:12,fill:'#9fb0bf','font-size':11},'USD · cada barra = 5 000'))}
function marcas(){const svg=document.getElementById('g-marcas');const bh=19;
 D.marcas.forEach(([marca,n,med],i)=>{const ancho=Math.max(2,(n/D.marcas[0][1])*430);const r=nodo('rect',{x:110,y:8+i*bh,width:ancho,height:14,fill:'#4ea3ff',class:'barra',tabindex:0},'');
  r.appendChild(nodo('title',{},marca+': '+n+' anuncios · mediana '+fmt(med)+' USD'));
  r.onclick=()=>{document.querySelectorAll('.barra').forEach(x=>x.setAttribute('fill','#4ea3ff'));r.setAttribute('fill','#f28e2b')};
  r.onkeydown=e=>{if(e.key==='Enter')r.onclick()};
  svg.appendChild(r);svg.appendChild(nodo('text',{x:104,y:19+i*bh,fill:'#9fb0bf','font-size':11,'text-anchor':'end'},marca));
  svg.appendChild(nodo('text',{x:112+ancho,y:19+i*bh,fill:'#e8edf2','font-size':10},fmt(med)+' USD'))})}
function canales(){const svg=document.getElementById('g-canales');const w=600,h=220;
 D.canales.forEach((c,i)=>{const [canal,tipo,n,med]=c;const x=60+i*180;const alt=Math.min(150,med/300);
  const r=nodo('rect',{x,y:h-30-alt,width:110,height:alt,fill:canal==='importacion'?'#f28e2b':'#4ea3ff',class:'barra'},'');
  r.appendChild(nodo('title',{},canal+' '+tipo+': '+n+' anuncios · mediana '+fmt(med)+' USD'));svg.appendChild(r);
  svg.appendChild(nodo('text',{x:x+5,y:h-38-alt,fill:'#e8edf2','font-size':12},fmt(med)+' USD'));
  svg.appendChild(nodo('text',{x:x+5,y:h-10,fill:'#9fb0bf','font-size':11},canal+' '+tipo))})}
histograma();marcas();canales();

// Ficha
const ficha=document.getElementById('ficha');
function abrir(titulo,lineas){document.getElementById('ficha-contenido').innerHTML='<h3>'+titulo+'</h3>'+lineas.map(x=>'<p>'+x+'</p>').join('');ficha.classList.add('abierta')}
document.getElementById('cerrar').onclick=()=>ficha.classList.remove('abierta');
document.addEventListener('keydown',e=>{if(e.key==='Escape')ficha.classList.remove('abierta')});

// Mapa base con zoom y arrastre
function navegar(svg){let vb=svg.getAttribute('viewBox').split(' ').map(Number);
 svg.addEventListener('wheel',e=>{e.preventDefault();const f=e.deltaY>0?1.12:0.88;const ancho=vb[2]*f,alto=vb[3]*f;
  vb=[vb[0]+(vb[2]-ancho)/2,vb[1]+(vb[3]-alto)/2,ancho,alto];svg.setAttribute('viewBox',vb.join(' '))},{passive:false});
 let arrastrando=false,x0,y0;
 svg.addEventListener('pointerdown',e=>{arrastrando=true;x0=e.clientX;y0=e.clientY});
 svg.addEventListener('pointerup',()=>arrastrando=false);
 svg.addEventListener('pointermove',e=>{if(!arrastrando)return;const r=svg.getBoundingClientRect();
  vb[0]-=(e.clientX-x0)*vb[2]/r.width;vb[1]-=(e.clientY-y0)*vb[3]/r.height;x0=e.clientX;y0=e.clientY;svg.setAttribute('viewBox',vb.join(' '))})}
function contorno(svg){if(!D.cuba.length)return;const pts=D.cuba.map(p=>proyecto(p[0],p[1]).join(',')).join(' ');
 svg.appendChild(nodo('polygon',{points:pts,fill:'#1d2a1c',stroke:'#5a7d52','stroke-width':2,'pointer-events':'none'}))}

// Servicios
const sm=document.getElementById('mapa-serv');navegar(sm);contorno(sm);
const capas=document.getElementById('capas-serv');const grupos={};
for(const tipo of Object.keys(D.colores)){const g=nodo('g',{'data-tipo':tipo});sm.appendChild(g);grupos[tipo]=g;
 const l=document.createElement('label');l.innerHTML='<input type="checkbox" checked> '+tipo;
 l.querySelector('input').onchange=e=>g.style.display=e.target.checked?'':'none';capas.appendChild(l)}
for(const e of D.elementos){const [x,y]=proyecto(e[2],e[3]);const c=nodo('circle',{cx:x,cy:y,r:4,fill:D.colores[e[0]]||'#888',class:'punto',tabindex:0,
  'aria-label':e[1]});c.appendChild(nodo('title',{},e[1]+' — '+e[4]));
 c.onclick=()=>abrir(e[1],[e[0],e[4],e[5]?'Estado: '+e[5]:'',e[6]?'Fuente: '+e[6]:'']);
 c.onkeydown=ev=>{if(ev.key==='Enter')c.onclick()};grupos[e[0]].appendChild(c)}
document.getElementById('buscar-serv').oninput=e=>{const q=e.target.value.toLowerCase();
 document.querySelectorAll('#mapa-serv .punto').forEach(p=>{const t=(p.getAttribute('aria-label')+' '+(p.querySelector('title')?.textContent||'')).toLowerCase();
  p.setAttribute('opacity',!q||t.includes(q)?'1':'.12')})}

// Circuitos
const cm=document.getElementById('mapa-cir');navegar(cm);contorno(cm);
for(const [codigo,anillos] of Object.entries(D.zonas)){const estado=(D.circuitos.find(c=>c[0]===codigo)||[])[1]||'sin dato';
 const color=D.color_circuito[estado]||'#9e9e9e';
 for(const anillo of anillos){const pts=anillo.map(p=>proyecto(p[0],p[1]).join(',')).join(' ');
  const pol=nodo('polygon',{points:pts,fill:color,'fill-opacity':.28,stroke:color,'stroke-width':1,class:'zona','data-codigo':codigo,tabindex:0},
   '');pol.appendChild(nodo('title',{},'Circuito '+codigo+': '+estado));
  pol.onclick=()=>{const c=D.circuitos.find(x=>x[0]===codigo)||[];abrir('Circuito '+codigo,[ 'Estado: '+estado, c[4]?c[3]+', '+c[4]:'', 'Último aviso: '+(c[2]||'sin dato')])};
  pol.onkeydown=ev=>{if(ev.key==='Enter')pol.onclick()};cm.appendChild(pol)}}
const capasC=document.getElementById('capas-cir');
for(const estado of Object.keys(D.color_circuito)){const l=document.createElement('label');l.innerHTML='<input type="checkbox" checked> '+estado;
 l.querySelector('input').onchange=e=>document.querySelectorAll('#mapa-cir .zona').forEach(z=>{
  const c=D.circuitos.find(x=>x[0]===z.dataset.codigo);if(c&&c[1]===estado)z.style.display=e.target.checked?'':'none'});capasC.appendChild(l)}
const lista=document.getElementById('lista-cir');
D.circuitos.slice(0,200).forEach((c,i)=>{const [codigo,estado]=c;const color=D.color_circuito[estado]||'#9e9e9e';
 const t=nodo('text',{x:8,y:16+i*15,fill:color,'font-size':12,class:'cir-item','data-codigo':codigo},codigo+'  ·  '+estado);
 t.style.cursor='pointer';t.onclick=()=>{const z=document.querySelector('#mapa-cir .zona[data-codigo="'+codigo+'"]');if(z)z.onclick()};lista.appendChild(t)});
document.getElementById('buscar-cir').oninput=e=>{const q=e.target.value.toLowerCase();
 document.querySelectorAll('.cir-item').forEach(x=>{x.setAttribute('opacity',!q||x.textContent.toLowerCase().includes(q)?'1':'.12')})};
</script></body></html>
"""


def generar(datos: dict, salida: Path) -> None:
    blob = json.dumps(datos, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    html = PLANTILLA.replace("__FECHA__", datos["fecha"]).replace("__DATOS__", blob)
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(html, encoding="utf-8")
    print(f"panel generado: {salida.name} ({len(html.encode()) / 1024:.0f} KB)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-si-cambia", action="store_true")
    ap.add_argument("--salida", default=str(SALIDA))
    a = ap.parse_args()
    datos = recoger_datos()
    Actual = huella_actual(datos)
    if a.solo_si_cambia and HUELLA.exists() and json.loads(HUELLA.read_text()) == Actual and Path(a.salida).exists():
        print("sin cambios; no se reescribe el panel")
        return
    generar(datos, Path(a.salida))
    HUELLA.parent.mkdir(parents=True, exist_ok=True)
    HUELLA.write_text(json.dumps(Actual, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()

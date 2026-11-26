#!/usr/bin/env python3
"""Genera el mapa offline desde mapa_elementos.sqlite.

Colores: gasolineras negro, estaciones de carga verde, concesionarios azul, talleres rojo.
Permite elegir que capas generar con --tipos.
"""
import argparse
import csv
import json
import sqlite3
from pathlib import Path

import plotly.graph_objects as go

BASE = Path(__file__).resolve().parents[1]
MAPS = BASE.parent / "Data" / "mapas"
DB = MAPS / "mapa_elementos.sqlite"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tipos", default="all", help="all o lista separada por comas: gasolinera,estacion_carga,concesionario,taller")
    ap.add_argument("--out", default=str(MAPS / "mapa_ofline.html"))
    a = ap.parse_args()

    c = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    c.row_factory = sqlite3.Row
    tipos = {r["tipo"]: dict(r) for r in c.execute("SELECT * FROM tipos")}
    if a.tipos.strip().lower() == "all":
        elegidos = list(tipos)
    else:
        elegidos = [x.strip() for x in a.tipos.split(",") if x.strip() in tipos]

    cuba = json.loads((MAPS / "cuba.geo.json").read_text(encoding="utf-8"))
    fig = go.Figure()
    fig.add_trace(go.Choropleth(
        geojson=cuba, locations=["CU"], z=[1],
        colorscale=[[0, "#d9ead3"], [1, "#d9ead3"]], showscale=False,
        marker_line_color="#274e13", marker_line_width=2, name="Cuba",
    ))

    resumen = []
    sin_coords = []
    for tipo in elegidos:
        rows = c.execute(
            """SELECT nombre,lat,lon,direccion,fuente,url,telefono,horario,precio,estado,detalles_json
               FROM elementos WHERE tipo=? ORDER BY nombre""", (tipo,)
        ).fetchall()
        con = [r for r in rows if r["lat"] is not None and r["lon"] is not None]
        sin = [r for r in rows if r["lat"] is None or r["lon"] is None]
        sin_coords += [dict(r) | {"tipo": tipo} for r in sin]
        meta = tipos[tipo]
        if not con:
            resumen.append((tipo, 0, 0))
            continue
        hover = []
        for r in con:
            det = []
            for k in ("direccion", "fuente", "telefono", "horario", "precio", "estado"):
                if r[k]:
                    det.append(f"{k}: {r[k]}")
            hover.append(f"<b>{r['nombre']}</b><br>" + "<br>".join(det))
        size = 6 if tipo == "gasolinera" else 10
        fig.add_trace(go.Scattergeo(
            lon=[r["lon"] for r in con], lat=[r["lat"] for r in con],
            text=hover,
            mode="markers" + ("+text" if tipo in ("concesionario", "taller", "estacion_carga") else ""),
            textposition="top center",
            marker=dict(size=size, color=meta["color_hex"], symbol=meta["simbolo"],
                        line=dict(width=1, color="white")),
            name=f"{meta['descripcion']} ({len(con)})",
        ))
        resumen.append((tipo, len(con), len(sin)))

    c.close()
    fig.update_geos(
        scope="south america", center=dict(lat=22.7, lon=-81.5), projection_scale=7,
        showland=False, showocean=True, oceancolor="#cfe2f3", landcolor="white",
    )
    fig.update_layout(
        title="Mapa offline — ICD Automotive Market Project",
        height=760, margin=dict(l=0, r=0, t=55, b=0), font=dict(size=11),
        legend=dict(x=0, y=1, bgcolor="rgba(255,255,255,0.85)"),
    )
    out = Path(a.out)
    fig.write_html(out, include_plotlyjs=True, full_html=True)
    print(f"Mapa: {out} ({out.stat().st_size} bytes)")
    for tipo, n, s in resumen:
        print(f"  {tipo}: {n} con coords, {s} sin coords")
    if sin_coords:
        p = MAPS / "elementos_sin_coordenadas.csv"
        with p.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(sin_coords[0].keys()))
            w.writeheader(); w.writerows(sin_coords)
        print(f"Sin coordenadas: {p}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Resume el estado de los jobs y publica SALUD.md como dead-man's switch."""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ESTADO = ROOT / "Data/_state"
SALUD_JSON = ROOT / "Data/_estado/salud.json"
SALUD_MD = ROOT / "Data/auditoria/SALUD.md"
ALERTAS = ROOT / "Data/_estado/alertas.jsonl"
STALE = ROOT / "Data/_estado/ALERTA.stale"
PERIODOS = {
    "revolico": 1.5, "circuitos": 24, "marketplaces": 168, "snapshots": 168,
    "fx": 168, "onei": 2160, "analisis": 168, "sitio": 168, "salud": 24,
    "calidad": 168,
}


def main() -> None:
    ahora = datetime.now(timezone.utc)
    filas = []
    for job, periodo in PERIODOS.items():
        archivo = ESTADO / f"{job}.json"
        datos = {}
        if archivo.exists():
            try:
                datos = json.loads(archivo.read_text(encoding="utf-8"))
            except Exception:
                pass
        ultimo = datos.get("last_success_utc") or datos.get("fin_utc")
        horas = None
        if ultimo:
            try:
                horas = round((ahora - datetime.fromisoformat(ultimo)).total_seconds() / 3600, 1)
            except (TypeError, ValueError):
                ultimo = None
        try:
            fallos = int(datos.get("fallos_consecutivos", 0))
        except (TypeError, ValueError):
            fallos = 0
        if datos.get("status") == "error" or fallos > 0:
            estado = "FALLIDO"
        elif ultimo is None:
            estado = "SIN DATOS"
        elif horas is None or horas > 2 * periodo:
            estado = "STALE"
        elif horas is not None and horas > periodo * 1.5:
            estado = "DEGRADADO"
        else:
            estado = "OK"
        filas.append({
            "job": job, "periodo_horas": periodo, "estado": estado,
            "ultimo_exito": ultimo, "edad_horas": horas,
            "fallos_consecutivos": fallos,
            "ultimo_error": datos.get("ultimo_error", ""),
        })

    SALUD_JSON.parent.mkdir(parents=True, exist_ok=True)
    SALUD_JSON.write_text(json.dumps(filas, indent=2), encoding="utf-8")
    SALUD_MD.parent.mkdir(parents=True, exist_ok=True)
    lineas = ["# Salud de la automatización", "",
              f"Generado: {ahora.isoformat()}", "",
              "| Job | Periodo h | Estado | Último éxito | Edad h | Fallos |", "|---|---:|---|---|---:|---:|"]
    for f in filas:
        lineas.append(f"| {f['job']} | {f['periodo_horas']} | {f['estado']} | {f['ultimo_exito'] or '—'} | "
                      f"{f['edad_horas'] if f['edad_horas'] is not None else '—'} | {f['fallos_consecutivos']} |")
    if any(f["estado"] == "STALE" for f in filas):
        STALE.write_text("Hay jobs sin ejecutarse en más de 2 periodos.\n", encoding="utf-8")
        lineas += ["", "**ALERTA:** hay jobs STALE; revisar `Data/_estado/ALERTA.stale`."]
    else:
        STALE.unlink(missing_ok=True)
    SALUD_MD.write_text("\n".join(lineas) + "\n", encoding="utf-8")

    vistos = set()
    if ALERTAS.exists():
        for l in ALERTAS.read_text(encoding="utf-8").splitlines():
            try:
                d = json.loads(l); vistos.add((d.get("job"), d.get("clase"), d.get("dia")))
            except Exception:
                pass
    nuevas = []
    dia = ahora.strftime("%Y-%m-%d")
    for f in filas:
        if f["estado"] in ("FALLIDO", "STALE") and (f["job"], f["estado"], dia) not in vistos:
            nuevas.append({"fecha_utc": ahora.isoformat(), "job": f["job"],
                           "clase": f["estado"], "dia": dia})
    if nuevas:
        with ALERTAS.open("a", encoding="utf-8") as fh:
            for d in nuevas:
                fh.write(json.dumps(d) + "\n")
    print(f"salud: {len(filas)} jobs | alertas nuevas={len(nuevas)} | SALUD.md actualizado")


if __name__ == "__main__":
    main()

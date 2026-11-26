#!/usr/bin/env python3
"""Genera el sitio MkDocs del proyecto desde los Markdown y CSV vigentes."""
from __future__ import annotations

import csv
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
ANA = ROOT / "Data/analisis_rentabilidad"


def limpiar(texto: str, carpeta: str) -> str:
    """Reescribe enlaces del repositorio a rutas internas del sitio."""
    texto = texto.replace("../../INFORME_TECNICO.md", "../referencia/informe.md")
    texto = texto.replace("../auditoria-fuentes-2026-11-23.md", "../fuentes/auditoria.md")
    texto = texto.replace("../fuentes-oficiales/ONEI/ANALISIS_DATO.md", "../fuentes/anuarios.md")
    texto = texto.replace("outputs/charts/", "../graficos/")
    texto = texto.replace("outputs/tables/kpis.csv", "../referencia/kpis.md")
    texto = texto.replace("MODELOS_Y_FUNCIONES.md", "../referencia/modelos.md")
    texto = texto.replace("../mapas/TIMELAPSE_CIRCUITOS.md", "../fuentes/circuitos.md")
    texto = re.sub(r"\]\(#cuadro-(\d+)[^)]*\)", r"](apendice.md#cuadro-\1)", texto)
    texto = re.sub(r"\]\(#gráfico-(\d+)[^)]*\)", r"](apendice.md#grafico-\1)", texto)
    texto = texto.replace("](#apoyos)", "](apendice.md#apoyos)")
    texto = re.sub(r"\]\(apendice\.md#cuadro-(\d+)[^)]*\)", r"](apendice.md#cuadro-\1)", texto)
    texto = re.sub(r"\]\(apendice\.md#gráfico-(\d+)[^)]*\)", r"](apendice.md#grafico-\1)", texto)
    if carpeta != "historia":
        texto = texto.replace("../graficos/", "../graficos/")
    return texto


def escribir(ruta: Path, contenido: str) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(contenido, encoding="utf-8")
    print("escrito", ruta.relative_to(ROOT))


def dividir_historia() -> None:
    texto = (ANA / "PRESENTACION_STORYTELLING.md").read_text(encoding="utf-8")
    partes = re.split(r"(?m)^## ", texto)
    intro = limpiar(partes[0], "historia")
    escribir(DOCS / "historia/index.md", intro)

    nombres: list[tuple[str, str]] = []
    for bloque in partes[1:]:
        titulo = bloque.splitlines()[0].strip()
        if titulo.startswith("Anexo:"):
            archivo = "apendice.md"
            titulo_nav = "Apéndice visual"
        else:
            num = re.match(r"(\d+)\.", titulo)
            assert num, "sección sin número: " + titulo
            archivo = f"{int(num.group(1)):02d}-seccion.md"
            titulo_nav = titulo
        cuerpo = "## " + bloque
        cuerpo = cuerpo.replace("## " + titulo, "# " + titulo, 1)
        if archivo == "apendice.md":
            cuerpo = cuerpo.replace("# Anexo: cuadros y gráficos\n",
                                    "# Anexo: cuadros y gráficos\n\n<a id=\"apoyos\"></a>\n", 1)
            cuerpo = re.sub(r"(?m)^### Cuadro (\d+)\.", r'<a id="cuadro-\1"></a>\n\n### Cuadro \1.', cuerpo)
            cuerpo = re.sub(r"(?m)^- \[Gráfico (\d+)\.", r'<a id="grafico-\1"></a>\n\n- [Gráfico \1.', cuerpo)
        escribir(DOCS / "historia" / archivo, limpiar(cuerpo, "historia"))
        nombres.append((titulo_nav, "historia/" + archivo))
    (ANA / "_nav_historia.txt").write_text(
        "\n".join(f"{t}|{r}" for t, r in nombres), encoding="utf-8"
    )


def copiar_referencias() -> None:
    (DOCS / "referencia").mkdir(parents=True, exist_ok=True)
    (DOCS / "fuentes").mkdir(parents=True, exist_ok=True)
    escribir(DOCS / "referencia/modelos.md",
             (ANA / "MODELOS_Y_FUNCIONES.md").read_text(encoding="utf-8"))
    shutil.copy2(ROOT / "INFORME_TECNICO.md", DOCS / "referencia/informe.md")
    shutil.copy2(ROOT / "Data/auditoria-fuentes-2026-11-23.md", DOCS / "fuentes/auditoria.md")
    shutil.copy2(ROOT / "Data/fuentes-oficiales/ONEI/ANALISIS_DATO.md", DOCS / "fuentes/anuarios.md")
    shutil.copy2(ROOT / "Data/estructura_github.md", DOCS / "fuentes/estructura.md")
    shutil.copy2(ROOT / "Data/AUTOMATIZACION.md", DOCS / "guias/automatizacion.md")
    shutil.copy2(ROOT / "Data/analisis_rentabilidad/ALCANCE_Y_RETENCION.md", DOCS / "guias/alcance.md")
    shutil.copy2(ROOT / "Data/mapas/TIMELAPSE_CIRCUITOS.md", DOCS / "fuentes/circuitos.md")
    shutil.copy2(ROOT / "Data/analisis_rentabilidad/ARQUITECTURA_DATOS.md", DOCS / "guias/arquitectura_datos.md")
    shutil.copy2(ROOT / "Data/ESTRUCTURA_ESPACIO.md", DOCS / "fuentes/espacio.md")


def tabla_csv(ruta: Path) -> str:
    with ruta.open(encoding="utf-8") as fh:
        filas = list(csv.reader(fh))
    if not filas:
        return ""
    head, bodies = filas[0], filas[1:]
    out = ["| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|"]
    out += ["| " + " | ".join(fila) + " |" for fila in bodies]
    return "\n".join(out)


def generar_kpis() -> None:
    k = tabla_csv(ANA / "outputs/tables/kpis.csv")
    c = tabla_csv(ANA / "outputs/tables/kpis_canal.csv")
    m = tabla_csv(ANA / "outputs/tables/modelo_depreciacion.csv")
    texto = (
        "# KPIs y evidencia del modelo\n\n"
        "Página de referencia generada desde los CSV del pipeline. Si cambia el análisis, vuelve a generar el sitio.\n\n"
        "## KPIs generales\n\n" + k + "\n\n## Por canal\n\n" + c +
        "\n\n## Coeficientes del modelo\n\n" + m +
        "\n\nEl p_valor mínimo vigente es 0,165: ningún coeficiente es significativo con la base actual.\n"
    )
    escribir(DOCS / "referencia/kpis.md", texto)


def generar_index() -> None:
    texto = """# El precio de moverse en Cuba

Análisis del mercado automotor cubano con datos verificables: 744 autos únicos de Revolico, 2.014 anuncios limpios y series oficiales del ONEI.

## Empieza por aquí

- **La historia completa** — [el punto de partida](historia/01-seccion.md), las cuatro preguntas, el retrato del mercado y el cierre.
- **Los números** — [KPIs y evidencia del modelo](referencia/kpis.md).
- **Cómo se calcula** — [funciones y modelos matemáticos](referencia/modelos.md), con su justificación.
- **Las fuentes** — [auditoría de fuentes](fuentes/auditoria.md) y [anuarios del ONEI](fuentes/anuarios.md).

## Cómo actualizar el sitio

Todo se genera desde los Markdown y CSV del repositorio con `python3 Auxiliares/herramientas/generar_sitio_mkdocs.py` y luego `mkdocs build`. No edites el HTML a mano.

**Versión:** 23/11/2026 · Conversión con TRMI informal (930 CUP/USD).
"""
    escribir(DOCS / "index.md", texto)


def generar_guia() -> None:
    texto = """# Regenerar el análisis y el sitio

Supone Python 3.10+ y el entorno `Auxiliares/.venv-py`.

## Pasos

```bash
Auxiliares/.venv-py/bin/pip install -r requirements.txt mkdocs mkdocs-material
Auxiliares/.venv-py/bin/python Data/analisis_rentabilidad/scripts/run_all.py
Auxiliares/.venv-py/bin/python Auxiliares/herramientas/generar_sitio_mkdocs.py
Auxiliares/.venv-py/bin/mkdocs build
```

## Resultado esperado

- `Data/analisis_rentabilidad/data/listings_clean.parquet` actualizado.
- `site/` con la página publicable.
- Si hay enlaces rotos, `mkdocs build --strict` los señala.

## Servir en local

```bash
Auxiliares/.venv-py/bin/mkdocs serve
```
"""
    escribir(DOCS / "guias/regenerar.md", texto)


def generar_mkdocs() -> None:
    nav_hist = (DOCS / "_nav_historia.txt").read_text(encoding="utf-8").splitlines()
    lineas = [
        "site_name: El precio de moverse en Cuba",
        "site_description: Análisis del mercado automotor cubano con datos verificables",
        "theme:",
        "  name: material",
        "  language: es",
        "  features:",
        "    - navigation.sections",
        "    - content.code.copy",
        "plugins:",
        "  - search",
        "exclude_docs: |",
        "  _nav_historia.txt",
        "markdown_extensions:",
        "  - tables",
        "  - toc:",
        "      permalink: true",
        "  - admonition",
        "  - attr_list",
        "nav:",
        "  - Inicio: index.md",
        "  - Panel interactivo: dashboard.html",
        "  - Historia:",
        "    - Introducción: historia/index.md",
    ]
    for fila in nav_hist:
        titulo, ruta = fila.split("|", 1)
        lineas.append(f'    - "{titulo}": {ruta}')
    lineas += [
        "  - Referencia:",
        "    - Funciones y modelos: referencia/modelos.md",
        "    - KPIs y evidencia: referencia/kpis.md",
        "    - Informe técnico: referencia/informe.md",
        "  - Cómo:",
        "    - Regenerar análisis y sitio: guias/regenerar.md",
        "    - Automatización a dos años: guias/automatizacion.md",
        "    - Alcance y retención: guias/alcance.md",
        "    - Arquitectura de datos: guias/arquitectura_datos.md",
        "  - Fuentes:",
        "    - Auditoría de fuentes: fuentes/auditoria.md",
        "    - Anuarios ONEI: fuentes/anuarios.md",
        "    - Estructura en GitHub: fuentes/estructura.md",
        "    - Timelapse de circuitos: fuentes/circuitos.md",
        "    - Mapa de espacio: fuentes/espacio.md",
        "",
    ]
    (ROOT / "mkdocs.yml").write_text("\n".join(lineas), encoding="utf-8")
    print("escrito mkdocs.yml")


def copiar_graficos() -> None:
    dest = DOCS / "graficos"
    dest.mkdir(parents=True, exist_ok=True)
    for f in (ANA / "outputs/charts").glob("*.html"):
        shutil.copy2(f, dest / f.name)
    print("graficos copiados:", len(list(dest.glob('*.html'))))


def copiar_dashboard() -> None:
    origen = ROOT / "Data/dashboard.html"
    if origen.exists():
        shutil.copy2(origen, DOCS / "dashboard.html")
        print("panel interactivo copiado")


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    dividir_historia()
    copiar_referencias()
    generar_kpis()
    generar_index()
    generar_guia()
    copiar_graficos()
    copiar_dashboard()
    generar_mkdocs()


if __name__ == "__main__":
    main()

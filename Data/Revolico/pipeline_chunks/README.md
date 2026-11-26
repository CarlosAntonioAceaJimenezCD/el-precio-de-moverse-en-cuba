# `pipeline.sqlite` distribuido en chunks

Igual que `revolico.sqlite`, la base de colas `pipeline.sqlite` (542.957.568 bytes) se divide en **52 chunks de 10 MB** (el último de 8,18 MB) para que una subida interrumpida solo pierda el fragmento en curso.

- `MANIFEST.json`: orden, offsets, tamaños y SHA-256 de cada chunk y del archivo completo.
- Los `.bin` están en Git LFS según `.gitattributes`.
- Herramienta: `python3 Auxiliares/herramientas/db_chunks.py verify|assemble Data/Revolico/pipeline_chunks/MANIFEST.json ...`.
- `db_chunks.ensure_db()` se llama desde `scrape_revolico_pipeline.py`, `aviso_revolico.py` y `reporte_progreso.py`: si `pipeline.sqlite` no existe, se reconstruye antes de abrirlo. El archivo original se conserva en el árbol de trabajo.

# Base de Revolico distribuida en chunks

`revolico.sqlite` (811 MiB) se divide en **82 chunks de 10 MB** para poder subirlos por partes y reanudar la transferencia tras un reinicio: si se interrumpe, solo se pierde el chunk en curso.

## Archivos

- `chunk_0000.bin` … `chunk_0081.bin`: fragmentos en orden, de 10 MB (el último de 0,12 MB).
- `MANIFEST.json`: tamaño total, SHA-256 del archivo completo, tamaño de chunk, orden, offset y SHA-256 de cada fragmento.
- Todos los `.bin` están gestionados por Git LFS (ver `.gitattributes`). El manifiesto es texto normal.

## Herramienta

```bash
# Dividir
python3 Auxiliares/herramientas/db_chunks.py split \
  Data/Revolico/revolico.sqlite Data/Revolico/chunks 10

# Verificar fragmentos
python3 Auxiliares/herramientas/db_chunks.py verify \
  Data/Revolico/chunks/MANIFEST.json

# Reconstruir (solo si el destino no existe; --force para reemplazar)
python3 Auxiliares/herramientas/db_chunks.py assemble \
  Data/Revolico/chunks/MANIFEST.json Data/Revolico/revolico.sqlite
```

La reconstrucción valida el SHA-256 de cada fragmento y del conjunto antes de escribir el archivo final.

## Adaptación del pipeline

`Data/analisis_rentabilidad/config.py` define `REVOLICO_CHUNKS`, `REVOLICO_MANIFEST` y `DB_CHUNKS_TOOL`. Si `revolico.sqlite` no existe pero está el manifiesto, `scripts/01_ingest.py` lo reconstruye automáticamente antes de leerlo. El archivo original se conserva en el árbol de trabajo; nada se ha borrado.

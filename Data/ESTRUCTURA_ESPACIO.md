# Dónde está el espacio (23/11/2026)

## Cuánto pesa en GitHub

La API de GitHub reporta **205.002 KB ≈ 0,20 GB**. Ese número cuenta solo el historial normal del repositorio: los archivos grandes se guardan aparte y la API pública no dice cuánto ocupan allí.

En esta computadora, la copia de esos archivos grandes ocupa **3,3 GB** (174 archivos). Es una referencia mínima: en GitHub puede haber además versiones antiguas que ya no están aquí. Para saber el total exacto habría que mirar el apartado de almacenamiento de la cuenta en la web de GitHub.

## Mapa sencillo de la carpeta local

```text
Proyecto (10 GB)
├── .git (4,3 GB)
│   ├── archivos grandes guardados aparte   3,3 GB
│   └── historial normal                   1,0 GB
├── Data (4,1 GB)
│   └── Revolico (3,4 GB)
│       ├── revolico.sqlite                810 MB  ← base principal
│       ├── pipeline.sqlite                552 MB  ← colas de trabajo
│       ├── chunks                         811 MB  ← copia partida de la base
│       ├── partes                         759 MB  ← copia partida anterior
│       └── pipeline_chunks                518 MB  ← copia partida de las colas
├── Auxiliares (1,5 GB)
│   ├── entorno de Python en uso           885 MB
│   └── repos de referencia                606 MB
├── Hombros                                179 MB
├── Copias                                  82 MB
└── Anexos                                   8 MB
```

## Dónde mirar primero si queremos seguir ahorrando

1. **Las tres copias partidas de Revolico** (811 + 759 + 518 MB). Son la misma base y las colas divididas en trozos. Solo conviene tocarlas si el trabajo automático deja de escribir en alguna.
2. **El historial normal de `.git`** (1,0 GB). Guarda versiones viejas de archivos de texto y documentos.
3. **El entorno de Python en uso** (885 MB). Tiene bibliotecas que quizá ya no necesitamos, por ejemplo `duckdb` (66 MB), que además no funciona en esta CPU.
4. **Los repos de referencia** (606 MB). No están subidos a GitHub; si algún estudio ya no se consulta, se puede mover a `Utilidades` como hicimos con las herramientas.
5. **`Hombros` y `Copias`** (261 MB entre ambos). Informes descargados y copias antiguas; revisar si siguen sirviendo.

## Cómo buscarlo sin herramientas especiales

```bash
# Ver cuánto ocupa cada carpeta
du -sh Data Auxiliares Hombros Copias Anexos .git

# Ver los archivos más grandes
find . -path ./.git -prune -o -type f -printf '%s %p\n' | sort -nr | head -20

# Ver archivos repetidos (mismo tamaño y contenido)
md5sum $(find Data Hombros Copias -type f -size +1M) | sort
```

Regla: antes de quitar cualquier cosa, confirmar que ningún trabajo automático la esté usando y dejar una copia en `~/Utilidades` si todavía puede servir.

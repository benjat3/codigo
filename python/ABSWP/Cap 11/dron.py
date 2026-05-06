import os

# El dron empieza a recorrer todas las carpetas
for carpeta_actual, subcarpetas, archivos in os.walk('C:\\Documentos'):
    # Hacemos un loop sobre la lista de archivos que el dron encontró aquí
    for nombre_archivo in archivos:
        # Capítulo 8: Verificamos si el string termina en .txt
        if nombre_archivo.endswith('.txt'):
            print(f"¡Encontré un texto! Se llama {nombre_archivo}")

import os, shutil
from pathlib import Path

for carpeta_actual, subcarpetas, archivos in os.walk(':\\Trabajo'):
    for nombre_archivo in archivos:
        if nombre_archivo.endswith('.pdf'):
            shutil.copy(Path(carpeta_actual) / nombre_archivo, 'C:\\Backup_PDFs')
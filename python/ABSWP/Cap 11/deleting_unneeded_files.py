from pathlib import Path

folder = Path.cwd()

for archivo in folder.rglob('*'):
    if archivo.is_file() and archivo.stat().st_size > 100*10**6:
        print(archivo)
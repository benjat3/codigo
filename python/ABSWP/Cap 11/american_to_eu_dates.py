#Take a folder with files that include an american date in their name
#Convert it to european and preserve the rest of the name

import re
from pathlib import Path

#Open data folder
dates_folder = Path.cwd() / 'laboratorio_ensayos'

#regex pattern for dates
pattern = re.compile(r'^(.*?)(\d\d)-(\d\d)-(\d{4})(.*?)$')

#Recursively look into folder
for archivo in dates_folder.rglob('*'):
    match = pattern.search(str(archivo.name))
    if match: 
        nuevo_nombre = f'{match.group(1)}{match.group(3)}-{match.group(2)}-{match.group(4)}{match.group(5)}'
        archivo.rename(archivo.with_name(str(nuevo_nombre)))

print('Nombres cambiados correctamente')
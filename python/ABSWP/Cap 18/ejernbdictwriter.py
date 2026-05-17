import csv

anomalias = [
    {'timestamp': '2026-05-16 10:15:00', 'eje_z': '15.4'},
    {'timestamp': '2026-05-16 10:15:02', 'eje_z': '18.1'}
]

with open('alertas_z.csv', 'w', newline='', encoding='UTF-8') as archivo:
    nombres_columnas = anomalias[0].keys()

    escritor = csv.DictWriter(archivo, fieldnames=nombres_columnas)

    escritor.writeheader()

    for diccionario in anomalias:
        escritor.writerow(diccionario)
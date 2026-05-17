import csv

resultados = [
    {'timestamp': '10:00:01', 'estado': 'CRITICO'},
    {'timestamp': '10:00:02', 'estado': 'NORMAL'}
]

with open('reporte_mantenimiento.csv', 'w', newline='', encoding='UTF-8') as archivo:
    # 1. Definimos el nombre de las columnas
    nombres_columnas = ['timestamp', 'estado']
    
    # 2. Creamos la "máquina" escritora
    escritor = csv.DictWriter(archivo, fieldnames=nombres_columnas)
    
    # 3. Escribimos los encabezados
    escritor.writeheader()
    
    # 4. Iteramos y escribimos
    for diccionario in resultados:
        escritor.writerow(diccionario)
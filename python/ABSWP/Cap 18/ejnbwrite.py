import csv

resultados = [
    {'timestamp': '10:00:01', 'estado': 'CRITICO'},
    {'timestamp': '10:00:02', 'estado': 'NORMAL'}
]

primer_dic = resultados[1]

encabezados = primer_dic.keys()
encabezados = f"{','.join(encabezados)}\n"

with open('reporte_mantenimiento.csv', 'w', encoding='UTF-8') as archivo:
    archivo.write(encabezados)
    for diccionario in resultados:
        valores = diccionario.values()
        valores = f"{','.join(valores)}\n"
        archivo.write(valores)
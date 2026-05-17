import csv

datos_z = []
with open('vibraciones.csv', 'r', encoding='UTF-8') as vibraciones:
    lector_csv = csv.reader(vibraciones)

    for fila in lector_csv:
        if lector_csv.line_num != 1:
            datos_z.append(float(fila[3]))
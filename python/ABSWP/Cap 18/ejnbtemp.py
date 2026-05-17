import csv

with open('temperaturas.csv', 'r', encoding='UTF-8') as archivo:
    # 1. Creamos el objeto lector
    lector_csv = csv.reader(archivo)
    
    # 2. Iteramos bandeja por bandeja (fila por fila)
    for fila in lector_csv:
        # 3. El atributo .line_num nos dice en qué fila vamos.
        # Si es la fila 1, usamos 'continue' para saltarla y no leer el texto del encabezado.
        if lector_csv.line_num == 1:
            continue
        
        # 4. Extraemos el índice 1 (la segunda columna)
        temperatura = fila[4]
        print(temperatura)

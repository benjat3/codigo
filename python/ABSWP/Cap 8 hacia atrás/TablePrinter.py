"""
Takes lists of words and prints it as a table 
"""
def printTable(data):
    
    #Primero capturo el ancho de cada columna
    colWidths = [0] * len(data)
    i = -1
    for item in data:
        maxlength = 0
        i += 1
        for word in item:
            if len(word) > maxlength:
                maxlength = len(word)
        colWidths[i] = maxlength

    #Ahora debo imprimir cada fila con mismo índice en las listas
    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i].rjust(colWidths[j]), end=" ")
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
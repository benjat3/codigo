import re
"""
Copia el comportamiento de .strip(entrada,separador)
"""


texto = input("Inserte el texto para strip\n>")
separador = input("Inserte el separador\n>")

def re_strip(entrada, argumento):
    if argumento == "":
        patron = re.compile(r"^\s+|\s+$")
        salida = patron.sub('', entrada)
    else:
        argumento = re.escape(argumento)
        patron = re.compile(rf'^[{argumento}]+|[{argumento}]+$')
        salida = patron.sub('', entrada)
    return(salida)

print(re_strip(texto,separador))
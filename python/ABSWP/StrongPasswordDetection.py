'''
Toma una contraseña y revisa si es fuerte
'''
import re

print("Inserte su contraseña")
test_password = input(">")

#Compilo por fuera para no gastar recursos de más al ejecutar muchas veces la función
minlength = re.compile(r'\S{8,}')
upcase = re.compile(r'[A-Z]')
lowcase = re.compile(r'[a-z]')
digit = re.compile(r'\d')
special = re.compile(r'\W')

def check_password(password):
    '''Valida la contraseña contra los patrones'''
    Validity = True
    #por lo menos 8 caracteres
    if not minlength.search(password):
        print("At least 8 digits without spaces.")
        Validity = False
    #contener uppercase
    if not upcase.search(password):
        print("There has to be an upper case letter")
        Validity = False
    #contener lowercase
    if not lowcase.search(password):
        print("There has to be a lower case letter")
        Validity = False
    #Un dígito o símbolo
    if not digit.search(password):
        print("There has to be a digit")
        Validity = False
    #Extra, control de caracteres especiales
    if not special.search(password):
        print("There has to be an special character")
        Validity = False
    return(Validity)

print(check_password(test_password))
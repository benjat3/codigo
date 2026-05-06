#This program reads a text file and lets the user add 
# their own text anywhere the following words appear in the text file:
#ADJECTIVE, NOUN, ADVERB, or VERB

import re, logging

#Activo logging en debug para hacer pruebas
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#Desactivo logging porque terminé el código
logging.disable(logging.CRITICAL)

pattern = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
file = 'text.txt'

with open(file, 'r', encoding='UTF-8') as text:
    text = text.read()
    # Mi primera vez usando logging
    logging.debug(f'Este es el texto que leímos: {text}')
    matches = pattern.findall(text)
    logging.debug(f'Estas son las coincidencias de regex: {matches}')

replace = []
for word in matches:
    wordl = word.lower()
    if wordl == 'adjective' or wordl == 'adverb':
        replace.append(input(f"Enter an {wordl}:\n"))
    else:
        replace.append(input(f"Enter a {wordl}:\n"))
logging.debug(f'lista de reemplazos: {replace}')

for i in range(len(replace)):
    text = text.replace(matches[i],replace[i],1)
logging.debug(f'Texto reemplazado:{text}')

with open(f'replaced_{file}', 'w', encoding='UTF-8') as replaced_text:
    replaced_text.write(text)
    
print(f'\nMad Lib terminado:\n{text}')

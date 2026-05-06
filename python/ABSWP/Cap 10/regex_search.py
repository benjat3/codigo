#This code opens all .txt files in a folder and searches for any line that matches
#a user-supplied regular expression

import re, pathlib #reg ex, pathlib to manage paths

#TODO: Ask user for regular expression
pattern = input('Supply regular expression:\n')
pattern = re.compile(fr'{pattern}')

#TODO: Select a folder where to look
folder = pathlib.Path('tests')

#TODO: Search files in folder and save coincidences to a list
coincidences = []
for file in folder.iterdir():
    #TODO: Search for matches on every .txt 
    if file.is_file() and file.suffix == '.txt':
        coincidences.append(file)

#TODO: Read line by line and send to a list
matches = []
for file_path in coincidences:
    with open(file_path, 'r', encoding='UTF-8') as f:
        for line in f:
            if pattern.search(line):
                matches.append(line)
                #TODO: print on screen
                print(f'{file_path.name}\n\t{(line.strip())}')

if not matches:
    print('No se encontraron coincidencias.')
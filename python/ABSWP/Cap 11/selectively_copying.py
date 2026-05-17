#Selectively Copying

#Write a program that walks through a folder tree and searches for files with
#a certain file extension (such as .pdf or .jpg). Copy these files from their 
#current location to a new folder.

from pathlib import Path
import shutil

#TODO:Specify a folder to copy from and one to copy to
folder1 = Path('tests/1')
folder2 = Path('tests') / '2'
folder2.mkdir(exist_ok=True)
#TODO:"Walk" troughout a folder and subfolders
pdf_list = list(folder1.rglob('*.pdf'))
for pdf in pdf_list:
        #TODO: copy to second folder 
        shutil.copy(pdf,folder2)
from pathlib import Path
spam_folder = Path('tests')
i = 0
for spam in sorted(spam_folder.glob('spam*.txt')):
    i+=1
    spam.rename(spam.with_name('spam'+ str(i).zfill(3) + '.txt'))
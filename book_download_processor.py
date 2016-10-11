import os
from zipfile import ZipFile

assert os.path.isdir('books')==True, 'are pgb books downloaded?'


## get list of all zips and the directories they are in

zips = []
for root, dirs, files in os.walk('books/www.gutenberg.lib.md.us/'):
    zips.append([os.path.join(root, f) for f in files if '.zip' in f])
    
## remove empty lists
zips = [items for items in zips if items != []]

## unnest and get rid of -8, -0, etc duplicates of the same book
zip_files = []
for item in zips:
    if isinstance(item, list):
        zip_files.append(item[0])
    else:
        zip_files.append(item)

print('list of: {} .zips retrieved'.format(len(zip_files)))


os.makedirs('books/output', exist_ok=True)


def unzipper(file):
    with ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall('books/output')
        print('.', end='')	
	

for f in zip_files:
    unzipper(f)


print('files unzipped to one directory')


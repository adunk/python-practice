import zipfile

# Open and list
zip = zipfile.ZipFile('Archive.zip', 'r')
# Will print a list of the files in the compressed zip file
print(zip.namelist())

# Metadata in the zip folder
for meta in zip.infolist():
    print(meta)

# Get the meta info of a particular file in the zip
info = zip.getinfo('purchased.txt')
print(info)

# Access to files in zip folder
print(zip.read('wishlist.txt'))
# Preferred way of opening files as we get the file as an f object
# TODO - Would like to know more abotu the 'with <> as' python structure...
with zip.open('wishlist.txt') as f:
    print(f.read())

# Extracting files
# A particular file
zip.extract('purchased.txt')
# All files
zip.extractall()

# Closing the zip

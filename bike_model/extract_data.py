import zipfile
import os

path = os.path.join("data", 'data.zip')

with zipfile.ZipFile(path, 'r') as zip_file:
    zip_file.extractall("data")

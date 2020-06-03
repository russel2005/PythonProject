import os
from zipfile import ZipFile

def zip_all(search_dir, extension_list, output_path):
    with ZipFile(output_path, 'w') as output_zip:
        for root, dirs, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                name, extension_list = os.path.splitext(file)
                if extension_list.lower() in extension_list:
                    output_zip.write(os.path.join(root, file),
                                     arcname=os.path.join(rel_path, file))


zip_all('C:\\test\\my_stuff', ['.jpg', '.txt'], 'my_stuff.zip')
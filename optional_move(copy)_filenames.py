import shutil, os
from pathlib import Path

source_path = Path(r'D:\03_program\python\source_folder')
dest_path = Path(r'D:\03_program\python\destination_folder')


for foldername, subfolder, filenames in os.walk(source_path):
    print (filenames)
    for filename in filenames:
        if filename.endswith('.PNG') or filename.endswith('.txt'):  # endswith()是字符串独有的方法
            # print(type(filename))
            shutil.copy(source_path / filename, dest_path)
        else:
            continue





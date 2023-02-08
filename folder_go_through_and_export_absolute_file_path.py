import os, shutil
from pathlib import Path

source_path = Path('D:\\00_Persuit\\06_CEM200')
dest_path = ('D:\\03_program\\python\\destination_folder')

'''
最关键的是正确理解os.walk()方法
(root,dirs,files) in os.walk(path)
    1.root(current_folder): 所指的是当前正在遍历的这个文件夹的本身的地址（隐含：这个文件夹会随着遍历不断更新）
    2.dirs(current_subfolder, without subfolers in subfolders): 是一个 list ，内容是该文件夹(当前正在遍历的这个文件夹， 这个文件夹会随着遍历不断更新)中所有的目录的名字(不包括子目录)
    3.files(current_folder_file, without files in subfolders): 同样是 list , 内容是该文件夹(当前正在遍历的这个文件夹，这个文件夹会随着遍历不断更新)中所有的文件(不包括子目录)
    then go through
    change the root folder
        1.new_root(new current folder): （隐含：这个文件夹会随着遍历不断更新）
        2.new_dirs(new current subfolder, without subfolers in subfolders)
        3.new_files(new current folder file, without files in subfolders)

为了理解，可以使用以下代码： 观察root的变化
for folder, subfolders, filenames in os.walk(source_path):   # (root,dirs,files) in os.walk(path)
    for filename in filenames:
        print(f'filname is {filename}')
        print(f'folder is {folder}')

'''

for folder, subfolders, filenames in os.walk(source_path):   # (root,dirs,files) in os.walk(path)
    for filename in filenames:
        if os.path.getsize(os.path.join(folder,filename)) >= 10000000:
            print (f'filename - {filename} size: ', os.path.getsize(os.path.join(folder,filename)))   # 输出文件的大小
            # folder 会自动变化 
            print (f'file absolute address is: ', os.path.join(folder, filename))   # 输出文件的绝对地址

      
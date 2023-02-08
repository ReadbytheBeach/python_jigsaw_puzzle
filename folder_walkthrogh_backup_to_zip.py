# 为一个文件件创建一个快照 --  Github的原型，只不过Git是通过时间来保存快照，并且有compare功能。
# 希望保存不同的版本，文件夹中的文件名每次创建时都会检索原有的文件名，然后有所变化--比如在原有的命名上数字加1，
'''
    强调文件名的命名规则： 雷达型号+日期， 例如 ARS620_Recoring_2023_02_04
    
    创建一个遍历文件夹生成zip文件的函数backToZip()
    引入两个变量，一个是源文件夹--要压缩的文件夹； 另一个是目的地---存放压缩后文件的文件夹
        1. 检查源文件夹是一个绝对路径
        2.1 会重复运行程序，生成快照名。所以制定命名规则 当前目录名+N+zip, 其中N-1表示之前已存在的快照版本,本次新生成的版本为N。
        2.1 当前目录os.path.basenem(绝对路径)
        2.2 用一个while循环 + os.path.exists(新文件名) 来检查文件名，并显示生成新文件夹名
        3. 生成一个zipfile.ZipFile的对象,赋予新文件名
        4. 遍历原文件夹的文件和子文件夹及文件,for foldername, subfolders, filename in os.work(源文件夹)
            a. 显示当前文件夹 -- 绝对路径
            b. 将文件夹压缩，生成文件夹压缩包， 名字就是快照名（ 当前目录名+N+zip)
            c. 遍历所有文件 （当下的文件夹和子文件夹）
            c. 遍历的文件名 记录为filename -- 为以后生成压缩文件时使用
            d. 将当前文件所在的目录记录在newBase变量中,同样使用os.path.basename(当前绝对路径)
                1). 如果本身文件就是zip,就跳转到下一条， 
                        i.使用 if filename.startswith('newBase')  该文件夹
                        ii.使用if filename.endswith('.zip'),   是压缩文件                        
                        iii. 两者同时满足，就使用continue跳过
                2). 不然就生成一个压缩文件，文件名 =  目录（绝对路径） + 该文件名， 使用write(os.join(目录，文件名))
        5. 完成遍历后，关闭压缩对象。 .close(), 并显示压缩完成
        6. 将新生成的压缩文件包移去目的地
            a. 避免重复写入，设置try...except
            b. 强调避免写入的前提是，要有一个强文件名命名规则 = '雷达类型 + 日期'

'''


import zipfile, os
from pathlib import Path
import shutil

def backupToZip(folder, dest_folder):
    # Back up the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder) # make sure folder is absolute

    #Figure out the filename this code should use based on
    #What files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
    print('zipFilename: ', zipFilename) # ToDo: 加上: TestCase + 日期 + 时分秒 + + 测试条件（10DB_10M) 就基本够用了

    # ToDo: Create the Zip file.
    print(f'Creating {zipFilename}...')  #  使用'{}'可以实现在print()方法中输出'非str'类型的变量
    backup_to_zip = zipfile.ZipFile(zipFilename, 'w')
    # ToDo: 之后可能反复执行，为了防止覆盖，可以使用追加的方式'a'
    # backupToZip = zipfile.ZipFile(zipFilename, 'a')
    # print('backupToZip: ', backupToZip)

    
    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')  # 使用print(f'string {Para}') 方法
        # Add the current folder to the ZIP file
        backup_to_zip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            print(f'newBase is {newBase}')   
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't back up the backup ZIP files
            backup_to_zip.write(os.path.join(foldername, filename))
            
    backup_to_zip.close()
    print('Compress done.')

    # 压缩后的文件在当前Python的执行目录下，需要将压缩后的文件移入目标文件夹
    intermediate_locat = Path.cwd() / zipFilename # 创建压缩文件夹的绝对路径 = 压缩后文件所在的目录 + 文件名
    try:
        print(shutil.move(intermediate_locat, dest_folder))  # 转移当前目录下的压缩文件到目标目录下， 并显示结果
    except:
        # 避免重复放入相同数据
        print(("Sorry, Destination path -- '%s'  has already exists" %dest_folder))


 

# 使用Path， 或不使用Path,可能会有不同的结果
# compress_path = Path('D:\\07_recordings\\recording_from_harddisk\\ARS620_Recording\\10DB_10M')
# ToDo: 如果需要自动化，就需要检查文件夹是否已经存在csv列表中，没有的才自动压缩.
# 其实自动化有点复杂，考虑文件夹和文件（难点是： 已有文件夹下的新文件识别）， 所以可以考虑文件夹金雀到日期+小时分钟，这样就不会有老文件夹了，每次生成新文件夹
compress_path = 'D:\\07_recordings\\recording_from_harddisk\\ARS620_Recording_2023_02_03'  # 每次需要手动收入

dest_path = 'D:\\07_recordings\\local_recording_destination_database'
# print(compress_path)

backupToZip(compress_path, dest_path)
print (Path.cwd())
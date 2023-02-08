import zipfile, os
from pathlib import Path
p = Path('D:\\03_program\\python\\for_future_use')


# 读取压缩文件的相关信息
exampleZip = zipfile.ZipFile (p / 'game_of_life_conway.zip' )  # 压缩文件所在路径
print(exampleZip.namelist())

zipInfo = exampleZip.getinfo('how_use_print.py')
print(zipInfo)

print(f'Compressed file is {round(zipInfo.file_size / zipInfo.compress_size,2)}x smaller')
# exampleZip.close()


# 解压缩相关文件到指定的目录下
extraZip = zipfile.ZipFile (p / 'game_of_life_conway.zip' )
extraZip.extract('how_use_print.py','D:\\03_program\\python\\source_folder')  # 仅解压单个文件
extraZip.close()

# 创建一个ZIP文件
newZip = zipfile.ZipFile('tiny_db.zip','a')   # 'w' 会覆盖原有内容，'a'在原有基础上追加压缩文件
newZip.write('tiny_db.py', compress_type=zipfile.ZIP_DEFLATED) # 仅压缩文件，而非文件夹
newZip.close()
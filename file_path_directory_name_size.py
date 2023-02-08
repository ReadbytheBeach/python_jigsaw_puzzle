from pathlib import Path
import sys, os

# 显示当前绝对路径
print(Path.cwd()) 

# 将目录和文件区分开来
p = 'D:\\03_program\\python\\for_future_use\\sandwich_vending_machine_program.py'
print(os.path.split(p))
print(os.path.split(p)[0])
print(os.path.split(p)[1])

# 用Path方法替代os方法
p = Path('D:\\03_program\\python\\for_future_use\\sandwich_vending_machine_program.py')
print(p.anchor)
print(p.drive)
print(p.parent) # == os.path.split(p)[0]
print(p.name) # ==os.path.split(p)[1]
print(p.stem) 
print(p.suffix)
print(p.parents[0])
print(p.parents[1])
print(p.parents[2])
print(p.parents[3])

# 显示当前用户根目录
print(Path.home())


# 连接路径和文件名
p_dir = Path('D:\\03_program\\python\\for_future_use')  # 使用Path方法
p_name = 'sandwich_vending_machine_program.py' # 或使用Path方法： p_name = Path('sandwich_vending_machine_program.py')
joint_path = p_dir / p_name  # Path方法的结合。 等同于 os.path.join(文件夹， 文件名) = os.path.join('D:\\03_program\\python\\for_future_use'，'sandwich_vending_machine_program.py')

# 显示文件的大小
print (str(os.path.getsize(r'D:\03_program\python\for_future_use\sandwich_vending_machine_program.py'))+ ' Byte')

# 显示文件夹的内容
print(os.listdir('D:\\03_program\\python\\for_future_use')) # 反斜杠'\' 是windows的标准用法

# 统计文件夹大小
totalsize = 0
for filename in os.listdir(r'D:\03_program\python\for_future_use'):
    totalsize = totalsize + os.path.getsize(os.path.join('D:\\03_program\\python\\for_future_use', filename))
print('total folder size= %s Byte' %(totalsize))

# 当下小程序大小
print('currently prgram size:  ' + str(os.path.getsize(r'D:\03_program\python\for_future_use\file_path_directory_name_size.py')) + ' Byte')


# 查找闪存是否连在计算机上
dDrive = Path('H:\\')  # windows中，盘符不区分大小写，用倒斜杠'\'代表目录
print(dDrive.exists())
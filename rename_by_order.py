# rename_by_order.py 的要求
# 在一个文件夹中找所有带指定前缀的文件， 如spam001.txt, spam002.txt, spam004.txt, spam007.txt
# 定位缺失的编号
# 对后面的所有文件重命名， 消除缺失的编号 


# 以下文件都存在于同一文件夹下，可使用os.path.join(source_path, filename)
# 使用遍历文件夹会逻辑上会更复杂---可活用os.walk()中的folder， os.path.join(folder, filename)
# 文件名中必须有一个数字
# 生成的命名是顺序的，但顺序命名的规则是按文件的“Date modified”来排序的

# 遍历文件夹 -- os.walk()
# 匹配合适的文件名 -- compile()
    # 方法一： re.compile(r'^(spam)(\d){3}(.txt)$')  /  re.compile(r'spam(\d){3}.txt$') / re.compile(r'spam(\d{3}).txt$') / re.compile(r'spam+(\d{3})+.txt')
    # 方法二： if filename.startswith('spam') and filename.endswith('.txt'): 

# 依次比对文件名，找出第一个不匹配的位置 
    # 事先设置一个全局的起使变量
    # 依次将文件名的编号用次序'n'来替代
    # 存入： #  beforeFilename =  os.path.joint(source_path, file_lsit[i]),  文件的绝对路径
            # afterFilename = os.path.joint(source_path, new_file_name)， 文件的绝对路径

# 在相同文件夹下依次重命名文件名 -- shutil.move
    # shutil.move(beforeFilename, afterFilename)
    # 使用shutil.move()方法前，先注释掉试一试。使用时在外面加print()查看输出内容



import os, shutil, re
from pathlib import Path

source_path = Path(r'D:\03_program\python\source_folder')
print(source_path)

# 以下四种正则表达式都可以
# search_reg = re.compile(r'^(spam)(\d{1,3})(.txt)')  # 该表达式可以
# search_reg = re.compile(r'^(spam)(\d){1,3}(.txt)')  # 该表达式可以
# search_reg = re.compile(r'spam+\d{1,3}+.txt')  # 该表达式可以
search_reg = re.compile(r'spam+(\d{1,3})+.txt')  # 该表达式可以

n = 0 

for folder, subfolder, filenames in os.walk(source_path):
    print(filenames)
    for filename in filenames: 
        if search_reg.search(filename):
                        
            '''
            老的路径 = 绝对路径文件夹 + 文件名: os.path.join(folder, filename)
            新文件名: = f'spam{n}.txt'
            新的路径 = 绝对路径文件夹 + 文件名: os.path.join(folder, 新文件名)
            改名: print(shutil.move(老的路径，新的路径))
            n += 1
            '''
            # print(folder)
            # beforeFilename = os.path.join(source_path, filename) # 代码规定了具体的改写文件夹，但不包含遍历子文件夹改名
            beforeFilename = os.path.join(folder, filename) # 代码用于遍历子文件： 

            # new_file_name = 'spam' + str(n) + '.txt' # 该表达式可以. # ToDo 找个更讨巧的命名规则
            new_file_name = f'spam{n}.txt'   #  该表达式可以. # ToDo 找个更讨巧的命名规则  
            # afterFilename = os.path.join(source_path, new_file_name)  # 代码规定了具体的改写文件夹，但不包含遍历子文件夹改名
            afterFilename = os.path.join(folder, new_file_name)  # 代码用于遍历子文件： 

            print(shutil.move(beforeFilename,afterFilename))  # 改名

            n += 1

print('done.')



    

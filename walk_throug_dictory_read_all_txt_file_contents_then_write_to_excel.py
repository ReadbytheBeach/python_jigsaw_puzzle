# 目标
    # # 读取几个文本文件的内容
    # 将内容插入电子表格
    # 每行写入一行文本
    # 第一个文本文件的行写入A列中的单元格
    # 第二个文本文件的行写入B列中的单元格
# 程序
    # 利用File对象的readlines()方法来返回一个字符串的列表，每个字符串就是文件中的一行
    # 第一个文件，将第1行写入列1行1， 第二行写入列1行2
    # 第二个文件重新写入列2行1，以此类推

# 执行
# 创建一个excel
# 创建一个正则表达式
# 找一个文件夹中的多个文本文件，使用os.walk()
# 找文本文件---使用正则表达式匹配每一个找的文件名
    # 每找到一个文本文件，
        # 每次清空内容列表 （放的位置很重要），防止保留上个循环中的内容
        # 每找到文本文件，统计数n+1 (放的位置很重要）
        # 使用readlines()按行读取文本文件内容
        # 去掉每行的换行符'\n'
        # 读完别忘了关闭文件对象
        # 列表有多少个元素，就写入多少行 len(line_content)
        # 第i列依次写入每行内容--将第1行写入列1行1， 第二行写入列1行2...
# 当遍历整个文件夹完成后，自动就会结束 
# 写完记得及时保存(也可以在最后保存)


import re, os, openpyxl
from pathlib import Path

txtRegex = re.compile(r'.txt$',re.I)
path = Path(r'D:\03_program\python\destination_folder')
# print(path)
account = 0  # 统计文本文件的数量--并用作写入的列号
contents = []
line_content = [] # 不含换行符'\n'的每一行

# 准备一个sheet
wb = openpyxl.Workbook()
sheet = wb.create_sheet('txt_input')
# sheet = wb.active

# 遍历文件夹
for dir, sub_dir, filenames in os.walk(path):
    # print(filenames)
    for filename in filenames:
        # 找到txt文件
        if txtRegex.search(filename):
            # 只有找到txt文件，才account+1，并用作写入的excel中的列值---wb.cell(row =, column= account).value
            account += 1
            # 每个循环中content要清空
            # 每个循环中line_content要清空
            contents = []
            line_content=[]
            absFileAddress = os.path.join(dir, filename) # 结合路径和文件名
            # print(absFileAddress)
            # 将文本文件内容存了一个列表
            fileObj = open(absFileAddress)
            contents = fileObj.readlines()
            # 假设文本文件的每一行内容都以换行符结尾。去除每一行的换行符'\n'
            for line in contents:
                line_content.append(line[:-1])
            fileObj.close()
            print('file name %s, lines: %s'% (absFileAddress, len(line_content)))
            # 存入第i列中的每一行
            for i in range(len(line_content)):
                sheet.cell(row=i+1, column= account).value = line_content[i] # row 从1开始
    
wb.save('txt_input.xlsx')




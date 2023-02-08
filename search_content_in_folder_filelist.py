# 该程序目的：文件夹中遍历所有的txt文件，查找与正则表达式匹配的内容

# 打开文件夹 
# 设定事先要匹配的正则表达式  --searchRegex = re.compile(r'(^[0-9]{1,})(.*)(invest$)', re.I)
# 找到所有的txt文档   -- search_file = search_dir.glob('*.txt')
# 逐行查找文档内容是否与表达式匹配   -- if searchRegex.search(check_content[i]):
# 如匹配输出行号， 文件名， 内容  -- print ('match file:%s,  line:%s,   matching contents:%s'%(searchPathObj, i+1, check_content[i]))

# ToDo: 如果输出路径，那不就是Everything工具的雏形吗，只不过他可以查找整个盘符，并且用类似并行查找--更快。 用匹配方式更模糊--列出所有可能匹配的项

from pathlib import Path
import re, os


# 给出要查找文件夹的绝对路径
search_dir = Path('D:\\03_program\\python\\automate_the_boring_stuff_with_python')  # serach_dir 是Path格式的对象，Python3.6之后可以用open()打开


# 查找文件的条件--使用Path下的glob()方法
search_file = search_dir.glob('*.txt')
'''
使用下面任意一行则程序就找不到txt文件了, 我怀疑list()方法导致的， 也可能本身用Path.glob()方法有局限性
# print(list(search_file))
# print(type(search_file))  # 所以要用list()方法，生成一个对象并输出
# if len(list(search_file)) == 0:
#     print('Not found any *.txt file in this folder')

但使用search_file == [] 则没有问题。
'''

# 确定想查找的内容 -- 'ADAS companies research and invest'
# 定义要匹配的正则表达式: 开头第一位是数字， 以字符串vest结尾，不区分大小写
searchRegex = re.compile(r'(^[0-9]{1,})(.*)(invest$)', re.I)


# 遍历文件夹下的所有txt文件
# 如果没有找到任何txt文件，则提示没有txt文件
if search_file == []:
    print('Not found any *.txt file in this folder')
else:
    for searchPathObj in search_file:
        # print(searchPathObj)
        content = open(searchPathObj,'r')
        check_content = content.readlines()
        # print(check_content)
        
        # 逐行读取并与正则表达式匹配，匹配就显示该行内容,并显示匹配的文件名，和行号
        # 如果没找到，就提示该txt没有匹配项
        n = 0 # 如果没
        for i in range(len(check_content)):
            if searchRegex.search(check_content[i]):
                print ('match file:%s,  line:%s,   matching contents:%s'%(searchPathObj, i+1, check_content[i]))
                n += 1
        if n==0: # 该文档匹配一次就加1
            print('No any content match in %s'%(searchPathObj))

        content.close()

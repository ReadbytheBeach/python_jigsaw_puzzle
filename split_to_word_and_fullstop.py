# 对一篇文章，按关键字做替换，替换内容由客户定 --- Ctrl+f & Ctrl+v 的基础嘛

from pathlib import Path
import re

print(Path.cwd())

# 手动创建一个文本文件

# 读入文本
content = open('mad_lib.txt', 'r')
modify_content = content.read()
content.close()
print(modify_content)


# 字符串变字符串列表 -- split()方法,  list()方法变字母
word_content = re.split(r'[ .]', modify_content)  # 同时区分'.' and ' ' 两种
# 难点：  将单词分开，单词和句号也分开--比如'VERB.' 要分开成'VERB' and '.'
# 添加句号 -- 把''替换成'.'
add_fullstop = []
for i in range(len(word_content)):
    if word_content[i] == '':
        # 替换成'.'
        add_fullstop.append('.')
    else:
        add_fullstop.append(word_content[i])

print(add_fullstop)


# 查找特定的内容： ADJECTIVE、NOUN、ADVERB、VERB
modify_list = ['ADJECTIVE','NOUN','VERB','ADVERB',]


new_content = []
# 让用户输入取代的词
# 依次查找内容
for i in range(len(modify_list)):
   
    # 逐个比较字符串列表
    for j in range(len(word_content)):
  
        if modify_list[i] == word_content[j]:
            if modify_list[i] == 'ADJECTIVE':
                print('Enter and adjective: ')
                input_adj = input()
                # ToDo: 加输入检查
                word_content[j]= input_adj

            elif modify_list[i] == 'NOUN':
                print('Enter a noun: ')
                input_nou = input()
                word_content[j]= input_nou

            elif modify_list[i] == 'VERB':
                print('Enter a ver')
                input_ver = input()+ '.'
                word_content[j]= input_ver
                

            elif modify_list[i] == 'ADVERB':  # 如果替换成else： 是为了保证至少有一个条件被执行
                print('Enter a adverb')
                input_adb = input()
                word_content[j]= input_adb

        new_content.append(word_content[j])

# 把单词重新整合成句子
new_string = ' '.join(word_content)
print(new_string)


# 整体输出
new_content = open('new_mad_lib.txt','w')
new_content.write(new_string)
new_content.close()



# to check the pswd
# 长度不少于8
# 有大写，有小写
# 至少一位数字
# 提示： 可能需要多个正则表达式来测试该字符串

import re


print ('Please input your PSWD here: ')

pswdRegex = re.compile(r'[a-zA-Z0-9]{8,}')

while True:
    message = input()
    try:
        if pswdRegex.search(message).group():
            break
    except AttributeError:
        print ('''PSWD format wrong! 
            Check following:
                length more than 8 elpha
                with Upper & Lower
                at least One number
                Please try to input again:   
                ''')
       
        continue

print('Done! PSWD setted as ',message)



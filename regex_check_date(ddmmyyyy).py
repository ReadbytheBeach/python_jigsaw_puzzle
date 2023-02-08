# DD/MM/YYYY
# DD: 01~31
# MM: 01~12
# YYYY: 1000~2999
# DD & MM长度为1，自动左补0变成2位
# Part 2
# 编写其他代码用以确定日期的有效性,
# 闰年年被4整除或被400整除
# 闰年2月有29天，其余都是30天
# 4，6，9，11 四个月只有30天
# 剩余月份都是31天

import re

# 随便输入一个日期： 符合DD/MM/YYYY的模式
input_date = f'26/1/2023'  # print('Please input a DD/MM/YYYY for check.") input_date = input()

# 按位取数，用正则表达式匹配是唯一快建的方法，这也是其存在的意义
dateRegex = re.compile(r'(\w{1,2})/(\w{1,2})/(\w{4})')

# 取出年月日
str_dd = dateRegex.search(input_date).group(1)
if len(str_dd) == 1:
    str_dd = '0' + str_dd
str_mm = dateRegex.search(input_date).group(2)
if len(str_mm) == 1:
    str_mm = '0' + str_mm
str_yy = dateRegex.search(input_date).group(3)
# print(type(dd))
print('年-月-日： '+ str_yy + '-' + str_mm +'-' + str_dd)

# 转换成整型
dd = int(str_dd)
mm = int(str_mm)
yy = int(str_yy)
# 检查日-月-年 的范围
if dd > 31: 
    print('only 31 days in a month.' + 'Currently you input: %s'%(str_dd))
if mm > 12:
    print('only 12 months in a year. ' + 'Currently you input: %s'%(str_mm))
if yy < 1000 or yy > 2999:
    print('Currently we only focus the year from 1000 to 2999. ' + 'Currently you input: %s'%(str_yy))


# 检查是否是闰年
# 闰年2月有29天
if (yy % 4 == 0 or yy % 400 == 0) and mm == 2:
    print('remind Leap Year Feb has 29 days')
    if dd > 29:
        print('Please modify the date')
 
# 如果不是闰年
# 2月有28天
# 4，6，9.11月有30天
else:
    if mm == 2:
        print('Feb has 28 days')
        if dd >28:
            print('Please modify the date')

    elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
        print('remind in Apr,Jun, Sep, Nov has 30 days')
        if dd > 30:
            print('Please modify the date')

    elif mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
        if dd > 31:
            print('remind rest month has 31 days')
            print('Please modify the date')


import time

this_moment = time.ctime()
print(this_moment)


import datetime

'''没有写函数，调用程序即触发内容'''

import json_request_websiteAPI_to_get_weather_in_shanghai

print(datetime.datetime.now())
# dt = datetime.datetime(2023,2,25,8,19,59)

# 显示： 年-月-日信息
dt = datetime.datetime.now()
# print(dt.year, dt.month, dt.day)

print('UNIX 纪元： ', datetime.datetime.fromtimestamp(1))
print()

# 一千天以后
# thousandDays = datetime.timedelta(days = 1000)
# which_day = dt+thousandDays
# print('一千天以后： ', which_day)

# 显示剩余的日子
year_after_10 = datetime.timedelta(days=365*10)

print('时光飞逝: ')
print('10年以后:  ',dt + year_after_10)
print('20年以后:  ',dt + year_after_10*2)
print('30年以后:  ',dt + year_after_10*3)
print('40年以后:  ',dt + year_after_10*4)
print()

make_a_mark_in_20230225 = '2063-02-15 09:55:57.863884'
print('Make a mark in 2023-2-25 09:55:57, 40年倒计时 ', make_a_mark_in_20230225)


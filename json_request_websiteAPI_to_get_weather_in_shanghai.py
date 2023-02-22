
# 并查看以下页面： https://blog.csdn.net/weixin_42210687/article/details/103480208 寻求解决方案
'''
    目标： 从天气网站取得上海的天气情况: https://openweathermap.org/
    技巧：  找到网站的API
            使用request爬取相关信息,
                从公司访问,可能不能通过SSL认证,所以须设置避免SSL
                    --url = 'https://api.openweathermap.org/data/2.5/weather?q=Shanghai&appid=ae33f3ffc8acb9fcc9fab130793dba53' 
                    --response = requests.get(url,verify=False)  # 要设置verify参数为False,避免ssl认证。
            将自动从网站取得的Json格式的资料转成python格式
                JSON文件保存在response.text
                    --response.raise_for_status() # 检查request是否有异常,如果没有异常,下载的文件将保存在response.text中
                从JSON转Python
            阅读内容，从字典中取出需要的键－值（天气信息）
'''

import json, requests, sys
import urllib3
urllib3.disable_warnings() # 不安全请求警告：正在发出未验证的HTTPS请求。强烈建议添加证书验证。方法：去除urllib3 warming 警告---urllib3.disable_warnings() 

# 公司电脑，sys.argv[] 都被屏蔽了

location = 'Shanghai'
appid = 'ae33f3ffc8acb9fcc9fab130793dba53' 

# Download the json data from OpenWeatherMap.org's API
# https://api.openweathermap.org/data/2.5/weather?q=Shanghai&appid=ae33f3ffc8acb9fcc9fab130793dba53  # try in the website, can work
# url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' %(location,appid)
url = 'https://api.openweathermap.org/data/2.5/weather?q=Shanghai&appid=ae33f3ffc8acb9fcc9fab130793dba53'  # its a problem for company network， could use verify = False
response = requests.get(url,verify=False)  # 要设置verify参数为False,避免ssl认证。
response.raise_for_status() # 检查request是否有异常，如果没有异常，下载的文件将保存在response.txt中

# Uncomment to see the raw JSON text:
# print(response.text)

# Load json data into a Python variable.
weatherData = json.loads(response.text)
# print(weatherData) 
w = weatherData # 为了少打一些字
# print(type(w))
print('Current weather in %s' %(location))
print(w['weather'][0]['main'], '-', w['weather'][0]['description'])

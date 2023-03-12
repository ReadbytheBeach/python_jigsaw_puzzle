# 必须在VPN登录下，才能打开国外网站

import requests, bs4
import urllib3
urllib3.disable_warnings() # 不安全请求警告：正在发出未验证的HTTPS请求。强烈建议添加证书验证。方法：去除urllib3 warming 警告---urllib3.disable_warnings() 

# 下载网页，并检查错误
res = requests.get('https://nostarch.com/', verify=False)
res.raise_for_status()

# 下载内容，用html格式解析，并存入BeautifulSoup的对象中
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))

# 找一个html, 用beautifulSoup解析
exampleFile = open('Python _ No Starch Press.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
# print(type(exampleSoup))

# 在网页中查询标签
elems = exampleSoup.select('#topics')  # 带有id属性为author的元素
print(type(elems))
# print(elems)
print(len(elems))
print(elems[0].getText())  # 标签Tag的文本 <a 文本 a>
# print(elems[0].attrs) # 标签Tag的属性

# BeautifulSoup的select()方法
elemp = exampleSoup.select('p')  # 解析 <p> 
print(len(elemp))
print(elemp[2].getText())

# 从网页中取值的方法，先定位Tag标签select()，然后从元素中找寻属性值get()
spanElem = exampleSoup.select('span')[0]
print(spanElem)
print()
print(spanElem.get('class'))  # get 的方法之后也会常被用到
print(spanElem.attrs)





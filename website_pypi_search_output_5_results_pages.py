# 给出网页，实现给出搜索条件，一键显示若干的搜索页面

import requests, sys, bs4, webbrowser
import urllib3
urllib3.disable_warnings() # 不安全请求警告：正在发出未验证的HTTPS请求。强烈建议添加证书验证。方法：去除urllib3 warming 警告---urllib3.disable_warnings() 

'''
在公司里，放弃使用 sys.argv[1:], 剪贴板、Cache是被禁用的
公司电脑对Cache有控制, 命令行运行,加参数会出现报错
print(sys.argv[:1])  # sys.argv[0] = 当前文件目录的全路径： d:/03_program/python/automate_the_boring_stuff_with_python/searchpypi.py
                     # sys.argv[1] = 即命令行中参数1:  requests  
                     # 比如在当前目录下，键入： searchpypi.py requests

所以暂时不用命令行输入方式， 即放弃sys.argv[]
替代方案: 直接输入希望查找的python lib名字, python_lib = 'requests'

语法上， print('https://pypi.org/search/?q=' + ''.join(python_lib)) == print('https://pypi.org/search/?q=' + python_lib)
'''

# 替代方案：直接输入希望查找的python lib名字
python_lib = 'requests'

print('Searching...')

# res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]), verify=False)  # 公司电脑对Cache有控制，命令行运行，加参数会出现报错
# 替代方案
# print('https://pypi.org/search/?q=' + ''.join(python_lib))
res = requests.get('https://pypi.org/search/?q=' + ''.join(python_lib), verify=False)  # 公司电脑对Cache有控制，命令行运行，加参数会出现报错
res.raise_for_status()


# 将原始网页存入文本文件，用于检索查询
web_content = open('pypi_content.txt', 'wb')
for chunk in res.iter_content(len(res.text)+100):
    web_content.write(chunk)
web_content.close()


# retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(soup)

# open a browser tab for each result
linkElems = soup.select('.package-snippet')                             #  <a class="package-snippet" href="/project/requests3/">
# print(linkElems)

# 每次最多打开五个页面
numOpen = min(2, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org/search/?q=' + linkElems[i].get('href')  # 打开文件的结构：https://pypi.org/search/?q=/project/requests/
    print('opening ', urlToOpen)
    # 打开网页
    webbrowser.open(urlToOpen)                                          


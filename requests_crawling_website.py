import requests, bs4
import urllib3
urllib3.disable_warnings() # 不安全请求警告：正在发出未验证的HTTPS请求。强烈建议添加证书验证。方法：去除urllib3 warming 警告---urllib3.disable_warnings() 


res = requests.get('https://automatetheboringstuff.com/files/rj.txt', verify=False)
res.raise_for_status()
print(type(res))
print(len(res.text))
# print(res.text[:1000])

# 从网上爬取文章
playFile = open('RemeoAndJuliet.txt','wb')
for chunk in res.iter_content(200000):  # 给出一个较大的空间
    playFile.write(chunk)
playFile.close()
print('downloaded Remeo & Juliet')

# 用beutifulsoup HTML解析器来解析网页
# 有了bs4之后，就可以定位HTML文档中特定的部分
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))





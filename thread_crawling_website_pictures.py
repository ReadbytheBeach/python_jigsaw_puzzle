# 利用多线程来完成网页图片（漫画）的下载

import requests, os, bs4, threading, shutil, time

import urllib3
urllib3.disable_warnings() # 不安全请求警告：正在发出未验证的HTTPS请求。强烈建议添加证书验证。方法：去除urllib3 warming 警告---urllib3.disable_warnings() 

import logging
logging.basicConfig(filename='xkcd_bs4.txt',level=logging.DEBUG, format ='%(asctime)s - %(levelname)s - %(message)s')

os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic): # range(startComic, endComic)的范围就是主程序for循环的步长step = 10
    for urlNumber in range(startComic, endComic):
        # download the page
        print('Downloading page https:/xkcd.com/%s...' %(urlNumber))
        logging.info('Downloading page https:/xkcd.com/%s...' %(urlNumber))
        res = requests.get('https://xkcd.com/%s' %(urlNumber), verify=False) 
        res.raise_for_status()
        # logging.info('Transfer to bs4.BeautifulSoup html parse...')
        logging.info('*'*80)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        # 把soup保存进日志
        logging.info(soup)

        # Find the URL of the comic image.
        '''
        XML content:  
        <div id="comic">
            <img src="//imgs.xkcd.com/comics/self_description.png" title="The contents of any one panel are dependent on 
            the contents of every panel including itself. The graph of panel dependencies is complete and bidirectional, 
            and each node has a loop. The mouseover text has two hundred and forty-two characters." alt="Self-Description" style="image-orientation:none">
        </div>        
        '''
        # 在comic中找img， 上文是网页的Html解析
        comicElem = soup.select('#comic img')  # <img>元素在<div id="comic">元素内, 如上所示
        print('comicElen: ', comicElem)
        if comicElem == []:
            print('could not find comic image.')

        else:
            comicUrl = comicElem[0].get('src')  # comicElen[0] 长度为1， 意识到'src'做为其中的属性， 所以能用方法get()
            # Download the image
            print('Downloading image %s...' %(comicUrl))
            # 生成一个图片所在的网页，并调用----每张图片（漫画）都有其专属的网页
            res = requests.get('https:'+comicUrl, verify=False)  # 该行等同于 <a href="https://imgs.xkcd.com/comics/semicontrolled_demolition.png">https://imgs.xkcd.com/comics/semicontrolled_demolition.png</a>
            res.raise_for_status()

            #save the image to ./xkcd
            # 用os.path.basename()方法，除了可以处理路径方式，也可以处理网路路径方式---https://imgs.xkcd.com/comics/the_problem_with_wikipedia.png。
            # 说到底两者都是斜杠方式来划分路径的， 为了做区别： 网路路径定义为正斜杠，文件路径定义为反斜杠。但两者都是“斜杠青年”。 os.path.basename()都可以识别并取出文件名
            # 以二进制的方式，存放图片数据到硬盘下的某个文件夹下的某个文件中
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')  # 只取文件名os.path.basename(文件名.后缀), 相对路径 + 文件名 = os.path.join(路径，文件名)
            # for 循环将一段图像数据写入文件
            for chunk in res.iter_content(100000): # chunk砖块的大小== 10万个Byte, 
                imageFile.write(chunk)
            imageFile.close()

# create and start the Thread objects
downloadThreads = []  # 存放所有线程的列表
for i in range(200, 220, 10):  # 循环6次=（260-200）/10 -- 即设置6个线程 thread
    start = i
    end = i + 9
    if start== 0:
        start = 1 # there is no comic 0, so set it to 1
    downloadThread = threading.Thread(target= downloadXkcd, args=(start, end)) # 将函数downloadXkcd 推入线程列表，并输送列表参数
    downloadThreads.append(downloadThread)
    downloadThread.start()

# wait for all threads to end
# 对所有的线程添加join()方法， 即主线程完成所有的子线程后，才能进入下一步操作
for downloadThread in downloadThreads:
    logging.info('*'*80)
    logging.info(downloadThread)
    downloadThread.join()

time.sleep(2)
shutil.move('D:\\03_program\\python\\xkcd_bs4.txt','D:\\03_program\\python\\xkcd\\xkcd_bs4.txt')
# downloadXkcd(1,2)
logging.info('End of program...')
print('Done.')
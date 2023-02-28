# 利用多线程来完成网页图片（漫画）的下载
'''
    目标： 从网站上下载漫画，并实现多线程同时下载
    
    实现：
    !!!前提： 还是要了解网站的结构：每一页图片网站的组成形式： https://xkcd.com/ + Number

    1. 做一个日志，存放相关过程
        --logging.basicConfig(filename='xkcd_bs4.txt',level=logging.DEBUG, format ='%(asctime)s - %(levelname)s - %(message)s')

    2. 创建一个文件夹用来发下载的文件（漫画）
        --os.makedirs('xkcd', exist_ok=True)

    3. 写一个爬取函数downloadXkcd
        设定子线程的循环次数 = 主线程循环的步数step
            1). 获取图片所在的页面， 赋给一个requests对象 res， 不需要SSL握手协议的验证verify=False
                -- res = requests.get('https://xkcd.com/%s' %(urlNumber), verify=False) 
            2). 如果获取过程中有问题， 则主动报错; 否则自动生成res.text 存放爬取的内容
                -- res.raise_for_status()
            3). 调用bs4.beautifulSoup()将爬取的内容以'html'的格式解析， 并写入beautifulSoup的对象soup
                -- soup = bs4.BeautifulSoup(res.text, 'html.parser')
            4). soup 的类型是BeautifulSoup, 所以用文本格式存入不是很方便，但可以用logging.info()直接保存
                --logging.info(soup)
            5). 对soup对象的内容进行解析 ( !!!前提是对该网站的html的结构要有一定的理解 )
                对该漫画网站HTML格式解析:
                    图片所在的HTML段落如下所示 :
                    ... ...
                    <div id="comic">
                    <img src="//imgs.xkcd.com/comics/self_description.png" title="The contents of any one panel are dependent on 
                    the contents of every panel including itself. The graph of panel dependencies is complete and bidirectional, 
                    and each node has a loop. The mouseover text has two hundred and forty-two characters." alt="Self-Description" style="image-orientation:none">
                    </div>   
                    ... ...  
        
                5.1) 找到图片所在的段落 id= comic
                    -- comicElem = soup.select('#comic img')  # <img>元素在<div id="comic">元素内
                5.2) 找到图片所在的位置
                        如果没有图片，
                            就跳转到下一个循环
                        如果有图片，
                            1. 则定位到图片所在的属性'src'， 并使用get()方法取出图片的网页链接
                                -- else:
                                    comicUrl = comicElem[0].get('src') 
                            2. 合并成图片所在的网页链接，爬取该网页上的图片数据，传递给requests的对象res中，
                                -- res = requests.get('https:'+comicUrl, verify=False) 
                            3. 检查爬取是否成功，有错则举手
                                -- res.raise_for_status()
                            4. 生成存放图片的目录和文件名
                                -- imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
                                a. 使用对网络路径使用basename()方法， 调出图片名（含后缀）
                                b. 生成指定目录下的保存文件的对象 imageFile， 指定使用二进制导入数据
                            5. 将数据从request对象中导入imageFile二进制文件中
                                -- for chunk in res.iter_content(100000): # chunk砖块的大小== 10万个Byte, 
                                        imageFile.write(chunk)            
                                a. 使用for循环，使用requests自带的iter_content()迭代方法， 每次导入100,000 bytes的大小
                                b. 写入二进制文件
                            6. 关闭文件
                                -- imageFile.close()

    4. 写一个主线程
        for循环
            1. 定义一个线程列表
            2. 确定线程的个数 = step, 确定每个'子'线程内的起、止位置 = startComic, endComic
                -- for i in range(200, 210, 10):  # 循环6次=（260-200）/10 -- 即设置6个线程 thread
                        start = i
                        end = i + 9
                        if start== 0:  # 网页图片是计数从1起, when start = 0, so set it to 1
                        start = 1
            3. 将函数和列表参数传递给'子'线程对象
                --downloadThread = threading.Thread(target= downloadXkcd, args=(start, end)) # 将函数downloadXkcd 推入线程列表，并输送列表参数
            4. 将子线程对象逐个压入主线程列表
                --downloadThreads.append(downloadThread)
            5. 启动'子'线程
                --downloadThread.start()

    5. 对所有的子线程赋予join()方法 -- 即等待所有的子线程都结束后。程序可以执行下一步   
        --for downloadThread in downloadThreads:
              downloadThread.join()

    6. 保存日志到文件所在的目录下， 采取shutil.copy()方法， 而非shutil.move()方法， 因为还没有关闭文件，所以无法移动文件
        --shutil.copy('D:\\03_program\\python\\xkcd_bs4.txt','D:\\03_program\\python\\xkcd\\Xkcd_bs4.txt') 
'''


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
        # print('comicElen: ', comicElem)
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
for i in range(200, 210, 10):  # 循环6次=（260-200）/10 -- 即设置6个线程 thread
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


logging.info('End of program...')
# 先要让logging.info()写完---先完成程序的关闭， 然后才能复制源文件到新的目录下
shutil.copy('D:\\03_program\\python\\xkcd_bs4.txt','D:\\03_program\\python\\xkcd\\Xkcd_bs4.txt')  # 当下选择的是Copy, 如果使用shutil.move()会发生文件打开中，无法移动的报警
print('Done.')
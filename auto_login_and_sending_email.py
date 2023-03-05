# 目标： 编写一个程序，
    # 通过命令行接收电子邮件地址和文本字符串 -- sys.argv[1:] 公司封了，改用input() 或 直接赋值 
    # 利用selenium自动登入到自己的电子邮箱账号。
    # 写邮件
    # 写（贴）接收人邮件地址，写（贴）邮件正文
    # 自动发送邮件

# 实现
    # 通过命令行接收电子邮件地址和文本字符串
        # receive_addr = 'jie.xun@continental-corporation.com'
        # mail_content = 'chi fan la!'
        # 发件人邮箱： Heinekenblue@163.com， 密码采用每次启动程序input() 方式---安全
        # 发件人邮箱链接地址：https://mail.163.com/?msg=authfail#return
   # 利用selenium自动登入到自己的电子邮箱账号。
        # 我用的是Microsoft Edge, 打开的是Google Gmail(但没有使用Chrome)
        # pswd = input()
        # driver.find_element(By.NAME, 'jie.ziqiangbuxi@gmail.com').send_keys('QSCesz01#' + Keys.Enter) # 也可以自己 submit()
        #   driver.clear()
   # 写邮件
        # 读懂网页
        # 在邮箱位置：
        # 在内容位置：
        # 发送：

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 书上没有的代码
from selenium.webdriver.common.keys import Keys

def login(pswd):
    # acount_num = input('请输入账号:\n')
    # passwd_str = input('请输入密码:\n')
    options = webdriver.EdgeOptions()  # 可能会有问题
    driver = webdriver.Edge(options=options)
    url = 'https://mail.163.com/?msg=authfail#return'
    driver.get(url)
    driver.maximize_window()
    time.sleep(5) # 5S后才自动关闭
    user_name = 'Heinekenblue@163.com'   #之后要用input方式来屏蔽掉
    user_pswd = pswd  #之后要用input方式来屏蔽掉
    sent_addr = 'jie.xun@continental-corporation.com'
    sent_topic = 'show me the topic'
    letter_content = 'what amazing for using selenium, python! '
    
    # 163登陆框是使用iframe进行嵌套的，所以需要先切换到该iframe
    # HTML原代码： <iframe name="" frameborder="0" id="x-URS-iframe1677894621840.8105"......</iframe>
    driver.switch_to.frame(0) 

    account_name = driver.find_element(by=By.NAME, value="email")
    account_name.clear()
    account_name.send_keys(user_name)
    # time.sleep(1)

    account_pswd = driver.find_element(by=By.NAME, value='password')
    account_pswd.clear()
    account_pswd.send_keys(user_pswd)
    # time.sleep(10)
    
    click_button = driver.find_element(by=By.ID, value='dologin')
    click_button.click()
    # time.sleep(6)
    # 保存进入后的页面
    cur_cookies = driver.get_cookies()[0]
    driver.save_screenshot('screenshot_logging.png')  # 页面保存在 D:\03_program\python
    
    time.sleep(2) # 登入后的页面保持2秒

    #点击“写信”，此时需要切回主文档！否则selenium无法定位元素，或者cannot access dead object
    driver.switch_to.default_content()

    # 找到写信按钮所在的位置
    # HTML原代码：<div class="frame-nav" id="dvNavContainer">  
    #               <nav class="tT0" role="navigation"><h1 class="tj0" id="dvNavTitle">邮件左侧导航</h1>
    #                  <div class="tx0" id="dvNavTop"><div class="qd0"><div class="jz0"></div></div>
    #                      <ul id="_mail_component_70_70" class="js-component-component tJ0">
    #                          <li id="_mail_component_72_72" class="js-component-component ra0 nb0" tabindex="0" role="button" ......
    #                              <span class="oz0">收 信</span></li>
    #                          <li id="_mail_component_74_74" class="js-component-component ra0 mD0" tabindex="0" role="button" ......
    #                              <span class="oz0">写 信</span></li>...
    # 如上所示‘写信’是网页结构中的第二个元素，索引号一层层往下推: div -> nav -> div -> ul -> li[1]
    '''   
    163邮箱大量采用动态id, 使得元素很难定位, 我的做法是用css选择器,
    编辑一个表达式, 在Chrome中搜索目标元素, 若是只搜索到1个, 那这个表达式可以.
    若是搜索到多个，则数清楚目标元素的次序，通过列表下标取到该元素。
    '''
    write_elem = driver.find_elements(by=By.CSS_SELECTOR,value='div nav div ul li')[1]  
    # print ("value='div nav div ul li':  ", write_elem)


    write_elem.click()
    cur_cookies = driver.get_cookies()[0]
    driver.save_screenshot('screenshot_writing_letter.png')  # 页面保存在 D:\03_program\python
    

    driver.implicitly_wait(5)

    time.sleep(1)

    # 写入邮箱
    '''   
    163邮箱大量采用动态id,使得元素很难定位, 以下做法是用XPATH

    但需要正确研读HTML的结构, 在Edge中搜索目标元素, 
    # HTML代码:
    # <input class="nui-editableAddr-ipt" type="text" role="combobox" tabindex="1" aria-label="收件人地址输入框，请输入邮件地址，多人时地址请以分号隔开">
    # 查看HTML结构图 D:\03_program\python\email_163_structure_for_write_letter.PNG

    找到其位置后, 正确使用find_element()方法 的XPATH的正确表达式 driver.find_element(by=By.XPATH, value = '//input[@class="nui-editableAddr-ipt"]')
    '''
    rec_elem = driver.find_element(by=By.XPATH, value = '//input[@class="nui-editableAddr-ipt"]')
    rec_elem.send_keys(sent_addr) 
    time.sleep(5)

    '''
    因为iframe的id是动态的，所以我们只能通过其他方法定位iframe，iframe的定位方法有：id，name，index等，这里我用name元素定位iframe
    
    '''

    # 写入主题 
    '''
    存放网页上的代码：

    '''
    # 方案 ---因为input后的代码是每次登入都会更新的iFrame方式，所以使用模糊匹配的方法, 并且使用了两级HTML合并，上一层的div 内容 和 下一层的input
    sub_elem = driver.find_element(by=By.XPATH, value = '//div[contains(@aria-label, "邮件主题输入框，请输入邮件主题")]/input')
    sub_elem.send_keys(sent_topic) 
    time.sleep(1)

    # 写入正文
    iframe = driver.find_element(by=By.CLASS_NAME, value = 'APP-editor-iframe') 
    driver.switch_to.frame(iframe) 
    letter_elem = driver.find_element(by=By.XPATH, value='/html/body[@class="nui-scroll"]')   # 相比于上文 by=By.CLASS_NAME, value = 'APP-editor-iframe' 的级别往下数，所以使用单层'/'表示向下一层
                                                                                              # ToDo: 试试主题也用这个方法，相对发件人的定位, 考虑是否需要 driver.switch_to.default_content(), 最终通过位置都能定位出来
    
    letter_elem.clear()
    letter_elem.send_keys(letter_content)

    # 按下“发送”
    # 退出iframe, 切回主文档
    driver.switch_to.default_content()
    # 按钮使用CSS定位更方便，因为有重名问题
    '''
    填写收件人邮箱，我习惯用css选择器，其实我觉得思维不难，最难的是元素的定位！
    163邮箱大量采用动态id，使得元素很难定位，我的做法是用css选择器，
    编辑一个表达式，在Chrome中搜索目标元素，若是只搜索到1个，那这个表达式可以，
    若是搜索到多个，则数清楚目标元素的次序，通过列表下标取到该元素。
    '''
    # 不用从’body'开始，从下一级'div'算起
    '''
    find_element: 只返回查找到的第一个元素，如果没有查找到元素，则返回NoSuchElementException的异常
    find_elements: 返回一个包含所有元素的列表，如果没有元素，则返回空列表
    '''
    send_elem = driver.find_elements(by=By.CSS_SELECTOR,value='div div div div footer div span')[0]
    print('send_elem =', send_elem)
    send_elem.click()
    time.sleep(3)

    cur_cookies = driver.get_cookies()[0]
    driver.save_screenshot('screenshot_send_letter.png')  # 页面保存在 D:\03_program\python
    time.sleep(1)



if __name__ == '__main__':
    print ('Please input your password here: ')
    email_pswd = input()

    if email_pswd:
        login(email_pswd)
    else:
        print('wrong password')


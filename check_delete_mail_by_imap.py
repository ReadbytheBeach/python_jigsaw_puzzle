# 目标：    1. 用来根据关键字来搜索邮箱中的邮件，比如日期（每次搜索手动更改日期，详见3.2）
#           2. 用来读取邮件
#           3. 选择性删除邮件

'''
策略：
    0. 对于使用IMAP， 请务必断开公司服务器， 不然可能出现IMAP无法正常通讯的情况
    1. 使用163邮箱标准的IMAP端口 (163邮箱使用 port=993）
      --设置一个imap对象: imapObj = imapclient.IMAPClient('imap.163.com',ssl=True, port=993)

    2. 登入IMAP服务器
        --imapObj.login(email, pswd)
        --163邮箱需要特别设置
            如果你是163邮箱
            并且如果你想使用imampObj.select_folder()
            必须使用以下语句， 否则系统会认为你在恶意进入邮箱， 因为根据RFC2971标准 IMPA协议必须含有头文件IMAP ID 
            可参见: 解决网易163邮箱`Unsafe Login.`错误 - yrPang: https://blog.yrpang.com/posts/45207/
            -- imapObj.id_({"name": "IMAPClient", "version":'2.3.1'})

    3.1 搜索电子邮件--选择文件夹
        -- imapObj.select_folder('INBOX', readonly = False)  # 选择文件夹中已读的邮件---readonly = True, 设置只读的另一层含义。一旦选了，之后有删除的动作会受影响。
            
    3.2 搜索电子邮件--执行搜索 (IMAP的缺陷) 
        此处的IMAP有一个缺陷: 对于日期信息是用“日期”固化在字符串中, 而不能以一个变量的方式存在, 每次操作都要手动更改很不方便）
        每次搜索手动更改日期："dd-Mon-yyyy"
        -- UIDs = imapObj.search('SINCE "06-Mar-2023"') 
        
    4. 读取邮件正文
        必须使用imap对象的fetch()方法来获得邮件的正文内容
        用pprint.pprint()方法来按人类能理解的方式显示正文
        --try:       
            rawMessages = imapObj.fetch(UIDs[id],['BODY[]'])  # 用imap的fetch()方法读取邮件内容            
            pprint.pprint(rawMessages)

    5. 另一种方法， 使用pyzmail库从原始邮件中获取信息
        a. 生成一个pyzmail的对象， 按属性打印内容
            --message = pyzmail.PyzMessage.factory(rawMessages[UIDs[id]][b'BODY[]'])
            print('email subject: ', message.get_subject())
            print('email from: ', message.get_address('from'))
            print('email to: ', message.get_address('to'))
            print('email cc: ', message.get_address('cc'))
        b. 邮件正文--文本内容
            用pprint.pprint()方法输出正文
            使用对象的test_part.get_payload()方法，并解密使用字符串方法 decode(message.text_part.charset)
            --if message.text_part != None:
                text_content = message.text_part.get_payload().decode(message.text_part.charset)
                print('email text content: ', text_content)
        c. 邮件正文，也可以输出HTML格式的内容
            --if message.html_part != None:
            html_content = message.html_part.get_payload().decode(message.html_part.charset)
            print('email html content: ', html_content)
      
    6. 删除电子邮件
       删除邮件前要先检查文件夹打开时，是否设置了只读： imapObj.select_folder('INBOX', readonly = False)，如果是只读，则无法删除（因为只读方式是无法修改的--包括删除，是故意为之）
       删除分为逻辑删除和物理删除
       删除的语句最要之前加个询问，或者是在程序调试过程中先注释掉。避免“误删除”
       删除后最好也给个反馈信息
       a. 逻辑删除
            --imapObj.delete_messages(delete_UIDs)
       b. 物理删除
            --imapObj.expunge()



'''
# 请务必断开公司服务器，不然可能出现IMAP无法正常通讯的情况
import imapclient
import imaplib
# 取消限制python程序消耗太多内存，将字节大小从10,000bytes, 改为10,000,000bytes

email = 'Heinekenblue@163.com'
'''
should be replace by pswd = input()
'''
print('please input your mail-box password')
pswd = input()

# 1.使用163邮箱标准的IMAP端口 port=993
imapObj = imapclient.IMAPClient('imap.163.com',ssl=True, port=993)

# 2.登入IMAP服务器
imapObj.login(email, pswd)
'''
如果你是163邮箱
并且如果你想使用imampObj.select_folder()
必须使用以下语句， 否则系统会认为你在恶意进入邮箱， 因为根据RFC2971标准 IMPA协议必须含有头文件IMAP ID 
可参见: 解决网易163邮箱`Unsafe Login.`错误 - yrPang: https://blog.yrpang.com/posts/45207/
'''
imapObj.id_({"name": "IMAPClient", "version":'2.3.1'})


# 3.1 搜索电子邮件--选择文件夹
import pprint
pprint.pprint(imapObj.list_folders())
# 选择邮箱中的一个文件夹
imapObj.select_folder('INBOX', readonly = False)# 选择文件夹中已读的邮件---readonly = True, 设置只读的另一层含义。一旦选了，之后有删除的动作会受影响


# 3.2 搜索电子邮件--执行搜索
UIDs = imapObj.search('SINCE "11-Mar-2023"') 
print('邮件编号：', UIDs)
# print(type(UIDs))


print('输入你想读的邮件id号, 输入“0”代表读第一个邮件, 以此类推1,2...,\n请在此输入,并按回车确认:  ')

# 4. 读取邮件正文fetch()
id = int(input()) 
delete_UIDs = UIDs[id] # 为delet预留伏笔    

try:       
    rawMessages = imapObj.fetch(UIDs[id],['BODY[]'])  # 用imap的fetch()方法读取邮件内容
    # 用pprint.pprint()方法输出正文
    pprint.pprint(rawMessages)

except ValueError:      # 必须先放except ValueError：, 再放单独的except
    print('No new email')

except IndexError:
    print('your choice out of mail range')


# 5. 另一种从原始邮件中获取信息的方法，使用pyzmail库
import pyzmail
try:
    message = pyzmail.PyzMessage.factory(rawMessages[UIDs[id]][b'BODY[]'])
    print('email subject: ', message.get_subject())
    print('email from: ', message.get_address('from'))
    print('email to: ', message.get_address('to'))
    print('email cc: ', message.get_address('cc'))
    # 邮件正文--文本内容：
    if message.text_part != None:
        text_content = message.text_part.get_payload().decode(message.text_part.charset)
        print('email text content: ', text_content)
    # 邮件正文--HTML内容：
    # if message.html_part != None:
    #     html_content = message.html_part.get_payload().decode(message.html_part.charset)
    #     print()
    #     print('email html content: ', html_content)
except:
    print('KeyErro: UIDs[Key], email ID not found ')



'''
以下代码使用时要小心
建议先注释掉，确认可以删除后，方可使用
'''
# 6.删除电子邮件
# 首先要确保之前邮件打开文件夹时没有被设置成只读，即 imapObj.select_folder('INBOX', readonly = False)
print()
print('if want to delete mail-%s: please input “y”, else input “n”'%(delete_UIDs))
delete = input()
       
if delete == 'y':
    print('has already deleted UIDs; ', delete_UIDs)
    # ToDo 删除邮件
    # 移入废件箱
    imapObj.delete_messages(delete_UIDs)

    # 物理删除
    print()
    print('Do you want phsically deleted the mail-%s? if yes, please input “y”, else input “n”'%(delete_UIDs))
    destroy = input()
    if destroy == 'y':
        print('mail-%s has been distoryed'%(delete_UIDs))
        imapObj.expunge()  #彻底删除

imapObj.logout()
      









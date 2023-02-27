#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip, time

# 公司禁用sys.argv[1:], 所以改为手动输入

'''
公司禁用sys.argv[1:] 和剪贴板
sys.argv[] 提供了一种“命令行执行程序并提供参数的方法”

if len(sys.argv) > 1:
    # Get address from command line.
    address = ''.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()   # 公司电脑对Cache有控制，命令行运行，加参数会出现报错
'''
address = 'shanghai'
time.sleep(5)       

webbrowser.open('https://www.google.com/maps/place/' + address)

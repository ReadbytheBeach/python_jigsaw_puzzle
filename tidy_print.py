"""
以下的输出主要是为字典这种结构做的设计
leftWidth: 字典的Key左对齐, ljust()
rightWidth: 字典的Value右对齐, rjust()
"""

def printPicnic(itemDict,leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemDict.items():
        print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth))

picnicItems = {'Paulaner': 4, 'beer': 5, 'water': 24} 

print(printPicnic(picnicItems, 20, 6))
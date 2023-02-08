import shelve
from pathlib import Path

# read the contents from harddisk
shelfFile = shelve.open('xj 2023 Wishes')
my_2023_Wishes = shelfFile['myWishes']
shelfFile.close()
print(type(my_2023_Wishes), my_2023_Wishes)


# ToDo:  Do something 


# save the content to binary file (*.bak, *.data, *.dir)
shelfFile = shelve.open(r'.\for_future_use\xj 2023 Wishes')  # 存在当前目录(.\)的子文件夹for_future_use下
my2023Wishes = ['1. Python learing\n',
                '2. ADAS companies research and invest\n',
                '3. robot direction\n',
                '4. practise inner peace, meditation\n',
                '5. practice focus, accept\n']    
shelfFile['myWishes'] = my2023Wishes
shelfFile.close()
print(Path.cwd()) # 查看一下当前存放路径

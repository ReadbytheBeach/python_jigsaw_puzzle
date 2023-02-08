# 使用通配符(wildcard character)
from pathlib import Path
import os


p = Path('D:\\03_program\\python\\for_future_use')
search_condition = p.glob('*.py')
disp_result = list(search_condition)
print(disp_result)

# 习惯用法： 输入条件搜索特定文件， 然后执行某些操作
p = Path('D:\\03_program\\python\\for_future_use')
for pyFilePathObj in p.glob('*.py'):
    if os.path.getsize(pyFilePathObj) <= 2000: # 如果搜索出的文件小于2K(单位Byte), 则显示该文件名，并进行如下操作
        print('File size less than 2k Byte:  %s'%(pyFilePathObj))
        # ToDo:  Do something with the text file

'''
    目标：
        去掉文件夹中所有CSV文件的标题(第一行)
    策略：
        创建一个新的csv文件，逐行加入， 然后插入一行，或去掉一行。 这样即完成了内容更迭，也保留了原始文档。
    技巧：
        如何自定义生成新文件的路径： 在生成对象的时候就有意的定义其生成的路径
            --csvFileObj = open(os.path.join('headerRemoved',csvFilename), 'w') 

        python一切皆对象： 
            先生成一个文件对象， 对应到最终存放的位置
            再生成一个CSV文件对象， 对应到这个文件对象
            之后对CSV文件对象写入内容， 就会传递给这个文件对象
            最后使用完文件对象后,关闭即可。
            --csvFileObj = open(os.path.join('headerRemoved',csvFilename), 'w', newline= '')  # 生成新文件的所在的路径
            --write_obj = csv.writer(csvFileObj)

            以上的过程就是函数化的过程， 逻辑上和函数类似： 先生成一个函数，然后调用这个函数并赋值。。。
'''

import csv, os

# os.makedirs('headerRemoved', exist_ok= False) # 创建一个文件件, exist_ok = False, 如果已存在就报一个os错误，提示文件夹已存在
os.makedirs('headerRemoved', exist_ok= True) 


# Loop through every file in the current working directory
for csvFilename in os.listdir('.\source_folder'):
    if not csvFilename.endswith('.csv'):
        continue
    print('Removing header from '+ csvFilename + '...')

    # Read the csv file in (skipping first row)
    csvRow = []
    csvFileObj = open(csvFilename)
    reader_obj = csv.reader(csvFileObj)
    for row in reader_obj: 
        if reader_obj.line_num == 1: # line_num count from 1 to n
            continue # skip the first line
        csvRow.append(row)
    csvFileObj.close()

    # Write out the CSV file.
    csvFileObj = open(os.path.join('headerRemoved',csvFilename), 'w', newline= '')  # 生成新文件的所在的路径
    write_obj = csv.writer(csvFileObj)
    for row in csvRow:
        write_obj.writerow(row)
    csvFileObj.close()

print('All CSV File re-writed!')
    



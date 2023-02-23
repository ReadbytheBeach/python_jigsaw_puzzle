''' 
    目标：
        遍历文件夹, 找到所有的excel文件
        一个excel可能有多个sheet, 每个sheet生成一个CSV
        CSV名字=EXCEL_Sheet

        建议先找一个excel试试转CSV
        遍历是件很容易的事

    技巧：
    for的使用
    对于一个文件夹
        对于一个excel
            对于excel下的一个sheet
                对于sheet下的每一行
                    对于一行中的每一列提取单元格的内容
                    以行为单位将内容存入对应的csv (因为CSV有个函数 CSV对象.writerow() )

    具体实现
    找到xlsx文件:
        --excelFile.endswith('.xlsx')
    打开excel, 提取Sheet表单, 并逐个激活
        -- wb = openpyxl.load_workbook(excelFile)
        -- for sheetName in wb.sheetnames:
        --      sheet = wb.get_sheet_by_name(sheetName) 
                在每一个表单下
                    给CSV命名
                        1.取出excel的名字, 方法split()
                            --excel_name = excelFile.split('.')[0]
                        2.合并新名字，方法： os.path.join()
                            --csv_name = os.path.join(excel_name + '_' +sheetName + '.csv')
                        3.给CSV取名, 方法: open() 和 csv.writer()
                            --csvWriteObj = open(csv_name,'w', newline= '')
                            --csw_write = csv.writer(csvWriteObj)
                    遍历每一行， 方法sheet.max_row
                        --for rowNum in range(1, sheet.max_row + 1):
                        1.每遍历一行第一步： 先清空rawData中上一行的内容
                          -- rawData = []
                        2.遍历行中的每一列--即一行中所有的单元格
                        3.将内容存入rawData,方法sheet.cell(row= , column=).value
                          --cell_value = sheet.cell(row=rowNum, column = colNum).value # 取得单元格的值
                          --rowData.append(cell_value)
                        4.将每一行内容按行存入csv中 方法： csv对象.writerow()
                          --csw_write.writerow(rowData)
                    遍历完所有的行，然后关闭文件对象
'''

import os, openpyxl, csv
from pathlib import Path

os.chdir(r'D:\03_program\python\source_folder')
print(os.getcwd())

for excelFile in os.listdir('.'):
    if excelFile.endswith('.xlsx'):
        # print(excelFile)
        wb = openpyxl.load_workbook(excelFile)
        # print(wb.sheetnames)
        for sheetName in wb.sheetnames:
            sheet = wb.get_sheet_by_name(sheetName) # 激活当下的sheet
            # print(sheet['A1'].value)
            # 给CSV命名
            excel_name = excelFile.split('.')[0]
            # print(excel_name)
            csv_name = os.path.join(excel_name + '_' +sheetName + '.csv')
            # print(csv_name)
            csvWriteObj = open(csv_name,'w', newline= '')
            csw_write = csv.writer(csvWriteObj)
            for rowNum in range(1, sheet.max_row + 1):
                rowData = [] # 每执行一行都会重新再次清空rawData的内容，一来便于不要累积，二来这样内存使用也最小
                for colNum in range(1, sheet.max_column + 1):
                    # pass
                    cell_value = sheet.cell(row=rowNum, column = colNum).value # 取得单元格的值
                    rowData.append(cell_value)
                csw_write.writerow(rowData)
            csvWriteObj.close()
                




# 目标：
    # 从excel电子表格中读取数据
    # 计算每个县中普查区的数目
    # 计算每个县的总人口数
    # 输出结果

# 动作
# 读取excel文档和单元格内容
# 计算每个县的普查区数目， 计算每个县的总人口数， 并将它保存在一个数据结构中
# 利用pprint,将该数据结构写入一个扩展为.py的文本文件

'''
本文的关键，
在于对于excel中的数据的理解;
设计了一个“嵌套字典”的数据结构;(特别是对tract的理解和处理)
并且巧妙的依次取出每行的单元格数据并赋给嵌套字典;

'''
import openpyxl, pprint
print('Opening workbook...') # 这个话术不错
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

# ToDo: Fill in countyData with each county's population and tracts.
print('Reading rows...')    # 这个话术不错    
for row in range(2, sheet.max_row +1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value     # 定位到第几列，第几行, eg: B2,B3
    county = sheet['C' +str(row)].value
    pop    = sheet['D' + str(row)].value
  
    # 填充数据结构
    # Make sure the key for this state exists.
    countyData.setdefault(state,{})
    # Make sure the key for this county in this state exists
    countyData[state].setdefault(county, {'tract':0, 'pop': 0})
    # Each row represents one census tract, so increment by one.
    countyData[state][county]['tract'] +=1
    # Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)

    # print(countyData)

'''
导入嵌套字典到python文件中
pprint.pformat() 产生一个字符串，本身就是格式化好的
'''
# ToDo: Open a new text file and write the contents of countyData to it
print('Writing results...')
resultFile = open('census2010.py','w')
resultFile.write('allData = '+ pprint.pformat(countyData)) # pprint.pformat() 产生一个字符串，本身就是格式化好的
resultFile.close
print('Done.')

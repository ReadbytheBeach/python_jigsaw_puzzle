import sys

tableDate = [['apple','orange','cherries','banana'],['Alice','Bob','Carol','David'],['dogs','cat','moose','goose']]
print(tableDate)
# tableDate = []


# 以下循环找出嵌套列表的最长字符串
colWidths = [0] * len(tableDate)
# print(colWidths)
line_list  = []
for i in range(len(tableDate)):
    max_len = 0
    for j in range (len(tableDate[i])):  # 这样的表达方式尽然可以实现列表的第二层嵌套， 即tableDate[i] == tableDate[i][:]
        
        item_len = len(tableDate[i][j])
        # 如果单词长度大于现有的最大长度记录，那最大记录替换成现有长度
        if item_len > max_len:
            max_len = item_len     

    colWidths[i] = max_len # 每一次的循环结尾收集最大的单词长度

    # 按行重新改造一下每个子列的元素
    if i == 0: # i 是
        for j in range (len(tableDate[i])):
            tableDate[i][j] = tableDate[i][j].rjust(max_len)

        # print(tableDate)
    else: 
        for j in range(len(tableDate[i])):
            tableDate[i][j] = tableDate[i][j].ljust(max_len)
        # print(tableDate)
print(tableDate)

   

# 如果tableDate是个空列表，则使用max()函数会报“ValueError”的错误
try:
    max_len = max(colWidths)
    print('max length item = ', max_len)
except ValueError:
    print(print("Nested List is empty."))
    

catNames =[]
while True:
    print('Enter the name of cat' + str(len(catNames)+1)+
    '(Or enter nothing to stop.):')
    name = input()
    if name == '':
        break # exit the while
    catNames = catNames + [name]  # list connect 这个技巧之前没用过
print('The cat names are:')
# for name in catNames:
#     print(''+ name)
'''
用 enumerate 改写以上的代码
'''
for index, item in enumerate(catNames):
    print('Index '+ str(index) + 'cat name is: ' + item  )

print('Totally '+str(len(catNames))+' cat names.')



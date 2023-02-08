import sys

birthdays = {'XJ': 'Apr-1', 'XLan': 'May-7'}


while True:
    print('Enter a name to check birthday: (blank to quit)')
    name = input()
    if name == '':
        sys.exit()
    
    if name in birthdays:
        print(birthdays[name] + 'is the birthday of ' + name)
    else:
        print('I don\'t have the birthday of ' + name)
        print('what is he/she birday')
        new_birthd = input()
        birthdays[name] = new_birthd
        print('Birthday database updated.')
    break

'''
Todo: 断电也能保存数据
'''
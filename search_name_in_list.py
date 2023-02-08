accessMembers = ['xj','ma jianyong','wang siliang']
print('Enter your name')
check_name = input().lower()
if check_name not in accessMembers:
    print (check_name + " You don't have the access.")
else:
    print(check_name + ' ,welcome to the new world!')
    pass
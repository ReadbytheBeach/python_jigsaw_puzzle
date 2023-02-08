while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal() and int(age) > 18:
        break
    print('Please enter a number for your age. Are you 18 years old?')


while True:
    print('Select a new password:(letter + number + special symbol, and length > 9) ')
    password = input()
    if ' ' in password:
        print ('passord can not with space')
        continue
    if password.isalnum():  # 包含了仅是字母的情况，也包含了仅是数字的情况
        print('password can not only have letters and numbers') 
        continue
    if len(password) < 10:  # 包含了不允许是空的情况
        print('password must be longer than 9')
        continue
   
    else:     # 关键else是否覆盖了其他不合格的password规定， 不好说
        break


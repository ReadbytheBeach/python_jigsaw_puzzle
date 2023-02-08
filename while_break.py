import sys


def collatz(number_para):
    if number_para % 2 == 0:
        return number_para // 2
    else:
        return 3 * number_para +1 

       
try:
    input_int = int(input('Please input an int:  '))

except ValueError:
    print('please input a int')
    input_int = int(input('Please input an int again:  '))

try:
    ret_value=0   
    while True:
        ret_value = collatz(input_int)  
        print (ret_value)
        if ret_value == 1:
            break
        else:
            input_int = ret_value

except KeyboardInterrupt:
    sys.exit()

print('finally result = 1, Collatz is Right!')


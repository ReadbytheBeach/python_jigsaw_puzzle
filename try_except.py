# 如何设置try - except

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print ('Error, Invalid Argument.')

print (spam(2))
print (spam(0))
print (spam(1))

"""
以下代码不建议, 因为一旦代码跳转到except,就不会再次进入try子句 （没有使用调用栈的功能吧 -- 记入调用时刻的行号）

def spam(divideBy):
    return 42 / divideBy

try:
    print (spam(2))
    print (spam(0))
    print (spam(1))

except ZeroDivisionError:
    print ('Error, Invalid Argument.')


"""
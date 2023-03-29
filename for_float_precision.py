'''
目的： 
    python 使用的是双精度'double precision',
    假如程序需要精确的浮点数运算, 考虑使用decimal.Decimal对象来替代普通浮点数, 做四则运算时不会损失精度
    需要注意一点： 在转换为Decimal对象时, 必须使用字符串来表示数字
'''

from decimal import Decimal
# 注意： 这里的'0.1'和'0.2'，必须是字符串
after_deal = Decimal('0.1') + Decimal('0.2')
print(after_deal)

print('Original 0.1 + 0.2 = ', 0.1+0.2)

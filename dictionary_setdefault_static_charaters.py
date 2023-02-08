import pprint


count = {} # 统计使用一个数组，key是字母，value是出现的次数
count_string = 'this is a very smart way to use setdefault() to count the character in a string'

for character in count_string:
    count.setdefault(character, 0)  # 如果字符还不在字典的key中， 则设置新key = charater, 并赋予初始值0
    count[character] = count[character] + 1

# print(count)
# 更优美的输出
pprint.pprint(count)


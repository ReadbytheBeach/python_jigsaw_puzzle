# English to Peg latin
print ('Enter the English message to translate into Pig Latin:')
message = input()
print (message+'\n')

VOWELS = ('a','e','i','o','u','y')


"""
1.从句子中选取单词
2.判断字符串（单词）的开头和结尾是否是字母
3.去头掐尾留下中间字母部分
4.留下大写记录，改成全小写，最后还原大写
4.对字母部分进行选取操作
5.添加被去头，和被掐尾的部分
"""

pigLatin =  [] # A list of the words in Pig Latin
for word in message.split():   # 从句子中提取单词
    
    # Separate the non-letters at the start of this word:
    prifixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():  # 收集所有首字母为非元音的簇
        prifixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:                      # 如果单词仅为一个元音字母
        pigLatin.append(prifixNonLetters)
        continue

    # Separate the non-letters at the end fo this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():   # 取出单词末尾所有是元音的字母
        suffixNonLetters += word[-1]
        word = word[:-1]   
    
    # Remeber if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()  # Make the word lowercase for translation

    # Separate the consonants at the start of this work
    prifixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prifixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the wordL
    if prifixConsonants != '':
        word += prifixConsonants + 'ay'
    else:
        word += 'yay'  # 元音加"yay"

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prifixNonLetters + word + suffixNonLetters)

#join all the word back together inot a single string:
print(' '.join(pigLatin))
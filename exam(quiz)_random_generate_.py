# 创建35份不同试卷
# 每份试卷50题，次序随机
# 每个问题提供一个正确答案和三个随机错误答案， 次序随机
# 试卷写入35个文本文件
# 答案也写入35个文本文件
# 将各州和他们的首府保存在一个字典中
# 针对测验文本文件和答案文本文件，调用open(), write(), close()
# 利用random.shuffle()随机调整问题和多重选项的次序

# randomQuizGenerator.py  - Creates quizzes with questions and answers in 
# random order, along with the answer key.


'''
自动生成考卷结构
用字典来存储题目和答案： key=问题， value=答案
先循环生成10份试卷和答案试卷
    1. 定义每份试卷的名字： -- quizFile = open(f'.\\automate_the_boring_stuff_with_python\\capitalsquiz\\capitalsquiz_{quizNum +1}.txt','w')  # {} 自动在名字中添加变量
    2. 定义每份答案试卷的名字： --answerKeyFile = open(f'.\\automate_the_boring_stuff_with_python\\capitalsquiz\\ capitalsquiz_answers_{quizNum + 1}.txt', 'w')
    3. 生成试卷表头，有名字、日期
    4. 打乱问题次序 -- 用random.shuffle(), 答案也随机打乱
    5. 随机打乱的基础上, 用循环生成30道问题, 题不重复
        1).每一道题写入试卷
        2).生成答案
            正确的答案存储在correctAnswer中
            错误的答案存储在wrongAnswer中
            错误的答案中去掉正确的答案：-- del wrongAnswers[wrongAnswers.index(correctAnswer)]  # index()方法在随机生成的列表中查找值，如果存在就返回该值的列表索引
            然后一起放入答题的四个选项optionAnswer中
            在随机打乱选项
            用循环生成四个选项
                把选项写入试卷： --quizFile.write(f"    {'ABCD'[i]}.{  answerOptions[i]}\n" ) 
        3).把证券的答案写入答案试卷： --answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}") 
    6.关闭打开的试卷
    6.关闭打开的答案试卷

    # ToDo: 现实生活中自动生成问答题考卷---问答题考卷。可以完全接用以上模式
    # ToDo: 现实生活中自动生成选择题考卷-- 如果题目类型不同(50个州是相同类型的题目, 字典结构相对简单)，可能要使用嵌套的字典结构{Key=问题, Value=[正确答案, 3个错误答案]}

'''

import random


# The quiz data, Keys are states and values are their Capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield',
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond',
            'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files
for quizNum in range(10):
    # create the quiz and answer file
    quizFile = open(f'.\\automate_the_boring_stuff_with_python\\capitalsquiz\\capitalsquiz_{quizNum +1}.txt','w')  # {} 自动在名字中添加变量
    answerKeyFile = open(f'.\\automate_the_boring_stuff_with_python\\capitalsquiz\\ capitalsquiz_answers_{quizNum + 1}.txt', 'w')


    # write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20)+f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')
    

    # shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)  # 每次随机打乱问题

    # loop through all 50 stats, making a question for each
    for questionNum in range(30):

        # get totoally four right and wrong answers for each question
        correctAnswer = capitals[states[questionNum]]  
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]  # index()方法在随机生成的列表中查找值，如果存在就返回该值的列表索引
        wrongAnswers = random.sample(wrongAnswers, 3)  # 随机从一个整体中，取出三个样品
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions) # 就地改变原列表的顺序


        # Write the question and the answer options to the quiz file.
        quizFile.write(f'{questionNum +1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}.{  answerOptions[i]}\n" )  # 这个写法蛮牛逼的{'ABCD'[i]...}
            quizFile.write('\n')

        # write the answer key to a file
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}")  # 找随机生成的正确答案对应'ABCD'四个选项中的哪一个，写法挺牛逼的！
    quizFile.close()
    answerKeyFile.close()




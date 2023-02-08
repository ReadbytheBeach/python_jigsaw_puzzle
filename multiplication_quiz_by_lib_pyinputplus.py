import pyinputplus as pyip
import random, time

"""
做10道题
numberOfQuestion: 做题数量
correctAnswer: 答对一道计1分

随机出题： 
pypi 一句话完成以下五个要求
出题形式： #题号： num1 * num2 = 答案
整数和字符串输出无缝链接 " '%s'%(num1 * num2) "
0.有优先级---首先判断答对，在答对不满足的情况下再考虑答错
1.答对，格式必须是数字开头，数字结束，避免误输入 
2.答错，不管任何形式，都显示'Incorrect!'
3.直接回车，输入空白会显示： Blank value is not allowed
4.每道题必须在10秒内给出答复
5.如果答案错误,每道题做多允许重新回答2次(共3次)

答对1题计1分
结束时给出总的答分结果  答对几题 / 答题总数

    该程序可以生成入职考试题目
    # ToDo:
    用一个字典嵌入字典存放选题， 用随机数自动生成考试的试卷 --- 每次10题,答对1题计1分
    嵌套字典格式: {key=题号, value={key=问题, value=答案}}
    
"""
numberOfQuestions = 10  
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)


    prompt = '#%s: %s x %s = '%(questionNumber, num1, num2)  # ‘#’ 代表第N题
    
    # 一个try + 带两个except + else 的组合方式
    try:
        # Right answer are handled by allowRegexes
        # Wrong answer are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$'%(num1 * num2)]   # 答对，格式必须是数字开头，数字结束，避免误输入
                            , blockRegexes=[('.*', 'Incorrect!')]   # 答错，任何形式，都显示'Incorrect!'
                            , timeout=9
                            , limit= 3)
        

    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    
    else:
        # This block runs if no excdptions were raised in the try block.
        print('Correct!')
        correctAnswers +=1

    time.sleep(1) # 1秒的暂停，帮助客户去阅读信息
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))



    

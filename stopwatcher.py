# 目标： 做一个超级秒表
#       使用字符串方法做左、右对齐， rjust()，ljust()

import time

# display the program's instructions
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. \nPress Ctrl-C to quit.')
input() # press enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

# start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime,2)
        # print(type(lapTime))
        totalTime = round(time.time()- startTime,2)
        # 使用字符串方法做左、右对齐， rjust()，ljust()
        print('Lap #%s:  %s (%s)' %(str(lapNum).rjust(4), str(totalTime).ljust(6), str(lapTime).rjust(7)), end='')  # end='' 避免重复出现空行
        lapNum +=1
        lastTime = time.time()  # rest the last lap
except KeyboardInterrupt:
    # handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone') # 正常退出，还能输出一个done



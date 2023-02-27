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
        totalTime = round(time.time()- startTime,2)
        print('Lap #%s: %s (%s)' %(lapNum, totalTime, lapTime), end='')  # end='' 避免重复出现空行
        lapNum +=1
        lastTime = time.time()  # rest the last lap
except KeyboardInterrupt:
    # handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone') # 正常退出，还能输出一个done



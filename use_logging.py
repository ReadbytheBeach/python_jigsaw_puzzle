import logging
logging.basicConfig(filename = 'myProgramLog.txt', level=logging.DEBUG, format ='%(asctime)s - %(levelname)s - %(message)s')  # 输出到指定文件中
# logging.basicConfig(level=logging.DEBUG, format ='%(asctime)s - %(levelname)s - %(message)s')  # 输出到'TERMINAL'面板里

# logging.disable(logging.DEBUG)  # 从下一行起，禁用DEBUG级别及以下 的日志消息

# 程序开始
logging.debug('\n\nStart of program.')

def factorial(n):
    # 每次循环开始时记录
    logging.debug('Start of factorical(%s)' %(n))
    total = 1
    for i in range(1,n+1):
        total *=i
        # 类似print输出结果
        logging.debug('i is '+str(i)+ ', total is '+str(total))   # print用于程序实时调用，logging用于整段程序的运行后查看。可以说 print == 日志
    logging.debug('End of factorial(%s)' %(n))
    return total

# 程序结束
print(factorial(5))
logging.disable(logging.ERROR)  # 从下一行起，禁用ERROR级别及以下 的日志消息,
logging.critical('End of program.')

import timeit

WORD = ['this is just a test'] * 40

def str_cat():
    s = []
    for word in WORD:
        s+= word
    return s

def str_join():
    l = []
    for word in WORD:
        l.append(word)
    return ' '.join(l)

# 默认执行100万次     
# 依赖其他包或模块：(setup = 'from __main__ import str_cat', stmt= 'str_cat()')       
cat_spend = timeit.timeit(setup = 'from __main__ import str_cat', stmt= 'str_cat()')
print('cat_spend = ', cat_spend)

join_spend = timeit.timeit(setup='from __main__ import str_join', stmt='str_join()')
print('joint_spend = ', join_spend)

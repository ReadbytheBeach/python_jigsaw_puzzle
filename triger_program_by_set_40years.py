import time, datetime

this_moment = time.ctime()
print(this_moment)

# set your trigger time, 
trigger = datetime.datetime(2063,2,15,9,30,0)  # 40年后
print('patient, the task will be start after 40years, %s' %(trigger))

try:
    while datetime.datetime.now() < trigger:
        time.sleep(10)

        
    # add your task after set time is passed
    pass
 
except KeyboardInterrupt:
    print('you stop the waiting young man, but %s still will come'%(trigger))



import time, subprocess
import datetime


timeLeft = 10

while int(timeLeft) > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft = timeLeft - 1

# at the end of the countdown, play a sound file
subprocess.Popen(['start', 'Ring04.wav'], shell=True)
subprocess.Popen(['start', 'break_time.txt'], shell=True)
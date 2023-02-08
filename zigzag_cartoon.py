import time, sys
indent = 0 # how many space to indent
indent_increase = True # whether indentation is increase or not

try:
    while True:
        print (' '* indent, end='')
        print ('***************')
        time.sleep(0.1)  # Pause for 1/10 seconds

        if indent_increase:
            # increase the number of spaces
            indent += 1 # 如果改成2，会出现很有意思的场景，也意味着 if indent == 25 基本失效，直接跨过奇数判断
            if indent == 25: 
                # change direction
                indent_increase = False
        
        else:
            # decrease the number of spaces
            indent -= 1
            if indent == 0:
                # change derection again
                indent_increase = True

        
except KeyboardInterrupt:
    sys.exit()
__author__ = 'zhw'
passwd = 'test'
break_flag = False
for i in range(3):
    user_input = raw_input("please input your passwd:")
    if len(user_input) == 0 :continue
    if user_input == passwd:
        while True:
            print "welcome login"
            user_choise = raw_input('''
                1. run a cmd
                2. send a file
                3. exit this loop
                4. exit hole loop''').strip()
            user_choise = int(user_choise)
            if user_choise == 1:
                print("run a cmd")
            if user_choise == 2:
                print("send a file")
            if user_choise == 3:
                print("exit this loop")
                break
            if user_choise == 4:
                break_flag = True
                break
        if break_flag == True:
            print("exit hole loop")
            break
            

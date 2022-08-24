real_num=111
retry_times=0
while retry_times<3:
    guess_num = int(raw_input("please input your guess:"))
    if guess_num < real_num:
        print("too small")
        retry_times += 1
    elif guess_num > real_num:
        print("too big")
        retry_times += 1
    else:
        print("correct")
        break
# encoding:utf-8
def func1():
    print("func1")

def func2():
    print("func2")

func_list=[None,func1,func2]

while True:
    print(""" 
    0 exit
    1 func1
    2 func2
     """)
    
    x=int(input("please input function number").strip())
    print("x is: %s"% x)
    print(func_list[x])
    
    # if not x.isdigit():
    #     print("please input number")
    if x == '0':
        break
    else:
        if x < len(func_list):
            func_list[x]()
        else:
            print("unknown number")
# encoding:utf-8
def func1():
    print("func1")

def func2():
    print("func2")

def func3():
    print("func3")

func_dict={
    "0":["退出",None],
    "1":["功能1",func1],
    "2":["功能2",func2],
    "3":["功能3",func3]
}

while True:
    for k in func_dict:
        print(k,func_dict[k][0])
    
    x=input("please input function number").strip()

    if not x.isdigit():
        print("please input number")
    elif x == '0':
        break
    else:
        if x in func_dict:
            func_dict[x][1]()
        else:
            print("unknown number")
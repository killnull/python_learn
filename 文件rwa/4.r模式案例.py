# encoding:utf-8
inusr=input("input your user").strip()
inpass=input("input your pass").strip()
with open('user.txt',mode='rt',encoding='utf-8') as f:
    for line in f:
        username,password = line.strip().split(":")  #这里需要把\n用strip去掉
        if inusr == username and inpass == password:
            print("login success")
            break
    else:
        print("err")

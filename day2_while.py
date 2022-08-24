# encoding:utf-8
print("=================")
print("""条件循环while基本语法""")
user = "a"
passw = "a"
tag = True
while tag:
    in_user = raw_input('input user:')
    in_pass = raw_input("input pass:")
    if in_user == user and in_pass == passw:
        print("login suc")
        tag=False
    else:
        print("user or pass err")
    print("end")


print("=================")
print("""while+break,直接跳出循环""")
tag = True
while tag:
    in_user = raw_input('input user:')
    in_pass = raw_input("input pass:")
    if in_user == user and in_pass == passw:
        print("login suc")
        break
    else:
        print("user or pass err")
    print("end")

print("=================")
print("""while+continue""")
i=0
while i<3:
    if i == 1:
        i += 1
        continue
    print(i)
    i += 1

print("=================")
print("""while+else,正常退出while，执行else""")
i=0
while i<3:
    if i == 1:
        i += 1
        continue
    print(i)
    i += 1
else:
    print("i >= 3")
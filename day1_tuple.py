# encoding:utf-8
print("=================")
print("""定义tuple""")
t1=(1,)
print(type(t1))
print("=================")
print("""取值""")
t1=(1,)
print(t1[0])
print("=================")
print("""切片，是一种复制操作，所以不算修改，使用和列表一样""")

print("=================")
print("""长度""")
print(len(t1))
print("=================")
print("""成员运算""")
print(1 in t1)
print(1 not in t1)
print("=================")
print("""循环""")
for x in t1:
    print x

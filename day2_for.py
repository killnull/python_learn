# encoding:utf-8
print("=================")
print("""迭代循环for基本语法""")
age_list = [1,2,3]
for i in age_list:
    print(i)
print("=================")
print("""for配合range，以及else就是正常退出循环，不被break时执行""")
for i in range(3):
    print i
else:
    print("normal exit")
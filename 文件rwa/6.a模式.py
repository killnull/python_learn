# encoding:utf-8
print("=================")
print("a，当不存在创建空文件，当文件存在指针到末尾，类似echo >>")
with open("a.txt",mode="at",encoding="utf-8") as f:
    f.write("追加写入1\n")
    print(f.read())
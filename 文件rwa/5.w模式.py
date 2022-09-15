# encoding:utf-8
print("=================")
print("w，当不存在创建空文件，当文件存在清空文件，类似echo >")
with open("a.txt",mode="wt",encoding="utf-8") as f:
    f.write("写入1")
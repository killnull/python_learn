# encoding:utf-8
print("只做了解，后面只用纯净模式")
print("=================")
print("r+,以r为基准，当文件不存在，直接报错")
with open('a.txt',mode='r+t',encoding='utf-8') as f:
    print(f.read())
    print("指针到末尾了")
    f.write("r+ --> write\n")
print("=================")
print("w+,以w为基准")
with open('a.txt',mode='w+t',encoding='utf-8') as f:
    f.write("w+1 --> write\n")
    f.write("w+2 --> write\n") 
    print(f.read())
    print("不打印是因为指针到末尾了，读不到前面")
print("=================")
print("a+,以a为基准")
with open('a.txt',mode='a+t',encoding='utf-8') as f:
    f.write("a+1 --> write\n")
    f.write("a+2 --> write\n") 
    print(f.read())
    print("不打印是因为指针到末尾了，读不到前面")
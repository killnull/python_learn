# coding:utf-8
print("=================")
print("相对同级路径")
f=open('a.txt',mode='rt',encoding='utf-8')
print(f.read())
print("相对不同级路径")
f=open('aaa/b.txt',mode='rt',encoding='utf-8')
print(f.read())
print("绝对路径,r代表rawstring")
f=open(r'C:\Users\lenovo\Desktop\python\文件\a.txt',mode='rt',encoding='utf-8')
print(f.read())
print("打开后要关闭")
f.close()
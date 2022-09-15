# encoding:utf-8
print("=================")
print("模拟注册")
inusr=input("input your user").strip()
inpass=input("input your pass").strip()
with open("db.txt",mode="at",encoding="utf-8") as f:
    f.write("{}:{}\n".format(inusr,inpass))
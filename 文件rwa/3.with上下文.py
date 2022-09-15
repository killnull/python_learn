# encoding:utf-8

print("=================")
print("with会自动管理上下文，不用手动close")
with open('a.txt',mode='rt',encoding='utf-8') as f,open('user.txt',mode='rt',encoding='utf-8') as f1:
    print(f1.read(),f.read())
# encoding:utf-8
print("=================")
print("把w2读出来，覆盖到w1上")
with open('w1.txt',mode='wt',encoding='utf-8') as f,\
    open('w2.txt',mode='rt',encoding='utf-8') as f1:
    res=f1.read()
    f.write(res)

# encoding:utf-8
print("x， 只写模式[不可读；不存在则创建，存在则报错]")

# with open('.txt',mode='x',encoding='utf-8') as f:
#     pass

# with open(r'c.txt',mode='x',encoding='utf-8') as f:
#     f.read()

with open(r'd.txt', mode='x', encoding='utf-8') as f:
    f.write('哈哈哈\n')
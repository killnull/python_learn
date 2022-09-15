# encoding:utf-8
# 一：读相关操作
# 1、readline：一次读一行
# with open(r'g.txt',mode='rt',encoding='utf-8') as f:
#     # res1=f.readline()
#     # res2=f.readline()
#     # print(res2)
#
#     while True:
#         line=f.readline()
#         if len(line) == 0:
#             break
#         print(line)

# 2、readlines： 把文件的内容读入一个列表 ，一行为一个元素
# with open(r'g.txt',mode='rt',encoding='utf-8') as f:
#     res=f.readlines()
#     print(res)

# 强调：
# f.read()与f.readlines()都是将内容一次性读入内存，如果内容过大会导致内存溢出，若还想将内容全读入内存，


# 二：写相关操作
# f.writelines()： 把一个列表里的内容写入文件
# with open('h.txt',mode='wt',encoding='utf-8') as f:
#     # f.write('1111\n222\n3333\n')
#
#     # l=['11111\n','2222','3333',4444]
#     l=['11111\n','2222','3333']
#     # for line in l:
#     #     f.write(line)
#     f.writelines(l)


# with open('h.txt', mode='wb') as f:
#     # l = [
#     #     '1111aaa1\n'.encode('utf-8'),
#     #     '222bb2'.encode('utf-8'),
#     #     '33eee33'.encode('utf-8')
#     # ]
#
#     # 补充1：如果是纯英文字符，可以直接加前缀b得到bytes类型
#     # l = [
#     #     b'1111aaa1\n',
#     #     b'222bb2',
#     #     b'33eee33'
#     # ]
#
#     # 补充2：'上'.encode('utf-8') 等同于bytes('上',encoding='utf-8')
#     l = [
#         bytes('上啊',encoding='utf-8'),
#         bytes('冲呀',encoding='utf-8'),
#         bytes('小垃圾们',encoding='utf-8'),
#     ]
#     f.writelines(l)


# 3、flush： 直接写入硬盘 ，不加载到缓存区
# with open('h.txt', mode='wt',encoding='utf-8') as f:
#     f.write('哈')
#     # f.flush()


# 4、了解
with open('h.txt', mode='wt', encoding='utf-8') as f:
    print(f.readable()) #输出是否可读 ，布尔类型
    print(f.writable()) #输出是否可写 ，布尔类型
    print(f.encoding)
    print(f.name)

print(f.closed)
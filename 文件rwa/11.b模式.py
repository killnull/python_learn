# encoding:utf-8
# 错误演示：t模式只能读文本文件
# with open(r'爱nmlgb的爱情.mp4',mode='rt') as f:
#     f.read() # 硬盘的二进制读入内存-》t模式会将读入内存的内容进行decode解码操作


#
# with open(r'test.jpg',mode='rb',encoding='utf-8') as f:
#     res=f.read() # 硬盘的二进制读入内存—>b模式下，不做任何转换，直接读入内存
#     print(res) # bytes类型—》当成二进制
#     print(type(res))

# with open(r'd.txt',mode='rb') as f:
#     res=f.read() # utf-8的二进制
#     print(res,type(res))
#
#     print(res.decode('utf-8'))

# with open(r'd.txt',mode='rt',encoding='utf-8') as f:
#     res=f.read() # utf-8的二进制->unicode
#     print(res)


# with open(r'e.txt',mode='wb') as f:
#     f.write('你好hello'.encode('gbk'))

# with open(r'f.txt',mode='wb') as f:
#     f.write('你好hello'.encode('utf-8'))
#     f.write('哈哈哈'.encode('gbk'))


# 文件拷贝工具
src_file=input('源文件路径>>: ').strip()
dst_file=input('源文件路径>>: ').strip()
with open(r'{}'.format(src_file),mode='rb') as f1,\
    open(r'{}'.format(dst_file),mode='wb') as f2:
    # res=f1.read() # 内存占用过大
    # f2.write(res)

    for line in f1:
        f2.write(line)
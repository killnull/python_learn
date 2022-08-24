# encoding:utf-8
print("=================")
print("""索引取值""")
msg="hello world"
print("""正向取""")
print(msg[0])
print("""反向取""")
print(msg[-1])
print("=================")
print("""切片""")
print(msg[0:3])
print(msg[1:])
print(msg[-3:])
print("""步长""")
print(msg[0:3:2])
print("""反向步长""")
print(msg[5:0:-2])
print("""利用反向步长倒转字符串""")
print(msg[::-1])
print("=================")
print("""strip去除两边""")
name="   aaa   "
print(name)
print(name.strip())
name=" -+(  aaa  )+_ "
print(name)
print(name.strip('-+_() '))
print("=================")
print("""lstrip去除左边""")
name=" -+(  aaa  )+_ "
print(name)
print(name.lstrip('-+_() '))
print("=================")
print("""rstrip去除右边""")
name=" -+(  aaa  )+_ "
print(name)
print(name.rstrip('-+_() '))
print("=================")
print("""左切分，把一个字符串按照分隔符从左切成列表""")
info="a,b,c,d,e,f"
info_list = info.split(",")
print(info_list)
print("""右切分，把一个字符串按照分隔符从右切成列表""")
info="a,b,c,d,e,f"
info_list = info.rsplit(",",1)
print(info_list)
print("=================")
print("""循环字符串""")
info="abc"
for x in info:
    print x
print("=================")
print("""大小写""")
msg="aabbCC"
print(msg)
print(msg.lower())
print(msg.upper())
print("=================")
print("""join 拼接列表""")
list1 = ["a","b","c"]
print(":".join(list1))
print("=================")
print("""replace 替换""")
msg="you can you up no can no bb"
print(msg.replace("you","YOU"))
print(msg.replace("you","YOU",1))
print("=================")
print("""isdigit 判断字符串是否由纯数字组成""")
print("12".isdigit())
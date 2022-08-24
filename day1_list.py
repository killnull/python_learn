# encoding:utf-8
name_list = ["a","b","c"]
print(name_list)
print("使用下标访问")
print(name_list[0])
print(name_list[2])
print("=================")
print("获取下标,只返回找到的第一个")
print(name_list.index("b"))
print("=================")
print("修改")
name_list[0] = "1"
print(name_list)
print("=================")
print("插入")
name_list.insert(1,"insert")
print(name_list)
print("=================")
print("追加")
name_list.append("append")
print(name_list)
print("=================")
name_list.insert(2,"chongfu")
name_list.insert(4,"chongfu")
print(name_list)
print("指定元素删除,从前往后删除")
name_list.remove("chongfu")
print(name_list)
print("=================")
print("pop删除")
print(name_list)
name_list.pop()
print(name_list)
name_list.pop(0)
print(name_list)
print("=================")
print("指定下标1删除")
print(name_list)
name_list.pop(1)
print(name_list)
print("=================")
print("正序取1:4值，或者叫做切片,原则是顾头不顾后,只打印1-3")
print(name_list[1:4])
print("=================")
print("倒序取-3:值，,原则是顾头不顾后,只打印单数第三个")
print(name_list[-3:])
print("=================")
print("统计元素个数")
name_list.append("append2")
name_list.append("append2")
print(name_list)
print(name_list.count("append2"))

print("=================")
print(name_list)
print("通过count方法循环删除")
for i in range(name_list.count("append2")):
    name_list.remove("append2")
    print(name_list)
print("=================")
print("合并列表")
name_list2 = ["e","f","g"]
print(name_list2)
name_list.extend(name_list2)
print(name_list)
print("=================")
print("排序")
age_list = [1,9,5,10,22]
print(age_list)
age_list.sort()
print(age_list)
print("=================")
print("倒序")
age_list = [1,9,5,10,22]
print(age_list)
age_list.reverse()
print(age_list)
#print("")
print("=================")
print("获取列表长度，可以配合for使用")
age_list = [1,9,5,10,22]
print(age_list)
print(len(age_list))

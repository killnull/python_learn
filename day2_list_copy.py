# encoding:utf-8
list1 = [1,2,[33,44]]
print("=================")
print("list1")
print("浅copy")
list2 = list(list1)
list3 = list1[:]
print(list2)
print(list3)
print("修改list1里的可变类型，list2\list3都跟着变")
list1[2][0]=55
print(list2)
print(list3)
print("=================")
print("深拷贝，要在python中使用list4=list1.deepcopy()")
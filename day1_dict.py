# encoding:utf-8
data = {
    "name":"zhw",
    "age":"18",
    "job":"learn"
}
print(data)
print("使用key访问")
print(data["job"])
print("=================")
print("插入")
data["salary"] = 50000
print(data["salary"])
print("=================")
print("修改")
data["salary"] = 90000
print(data["salary"])
print("=================")
print("删除")
data.pop("salary")
print(data)
print("=================")
print("遍历key")
for key in data:
    print(key,data[key])
print("=================")
print("检查是否有没有key,方式1")
if data.has_key("info"):
    print(data["info"])
print("检查是否有没有key,方式2")
print(data.get("info"))


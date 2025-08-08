#创建
a = []
b = {}
c = [1,"yyk",1]  #   列表 可以这么写 但没意义  列表 存储同一类数据时更有意义
d = {"name":"yyk","age":18}  # 字典 
e = list() #空列表
f = dict() #空字典  例如  JSON数据格式

#使用
print(a)  # []
# 0,1,2
total = 2 + c[2]
print(total)  # 2 + 1 = 3

print(d["name"])  # yyk
d.get("name")  # yyk

g = c+[1, 2, 3]  # 列表相加
print(g)  # [1, 'yyk', 1, 1, 2, 3]
d.update({"address":"beijing"})  # 字典更新
print(d)  # {'name': 'yyk', 'age': 18, 'address': 'beijing'}
#修改
c.append(2)  # 列表添加

print(c)  #  [1, 'yyk', 1, 2]
c.remove(1)  # 列表删除
print(c)  # ['yyk', 1, 2]
d["name"] = "sk" # 字典修改
print(d)  # {'name': 'sk', 'age': 18, 'address': 'beijing'}
d.update({"address":"beijing"})  # 字典更新
print(d)  # {'name': 'sk', 'age': 18, 'address': 'beijing'}

#删除

c.remove(2)  # 列表删除
print(c)  # ['yyk', 1]
d.pop("address")  # 字典删除
print(d)  # {'name': 'sk', 'age': 18}
del d["age"]  # 字典删除
print(d)  # {'name': 'sk'}



#循环

for i in c:  # 列表循环
    print(i)  # yyk 1
    
for i in d.keys():  # 字典循环
    print(i)  # name
    print(d[i])  # sk
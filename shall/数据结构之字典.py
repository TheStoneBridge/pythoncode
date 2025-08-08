import string

#输出
d = {}.fromkeys([i for i in string.ascii_letters ],'hi')  #  使用fromkeys方法创建字典
print(d)  # 输出字典
print("-----------------")

d['a'] = 1
print(d)  # 输出修改后的字典
print("-----------------")

#添加
d.update({"zz":12}) # 使用update方法更新字典
print(d)  # 输出更新后的字典
print("-----------------")

d.update({"a":12}) # 使用update方法更新字典中的键'a'
print(d)  # 输出更新后的字典
print("-----------------")

d.update({"a":19 ,"b":20})  # 使用update方法同时更新多个键
print(d)  # 输出更新后的字典    
print("-----------------")

d.setdefault("xx", 100)  # 如果键'a'不存在，则设置默认值为100
print(d)  # 输出字典
print("-----------------")
d.setdefault("a", 200)  # 如果键'a'存在，则不修改其值  使用一次之后  后续不允许修改
print(d)  # 输出字典
print("-----------------")

#删除

x = int(d.pop("xx") )  # 删除键'xx'并返回其值
print(x)  # 输出被删除的值
print("-----------------")

k,v = d.popitem()  # 删除字典中的最后一个键值对并返回
print(k, v)  # 输出被删除的键和值
print("-----------------")

d.clear()  # 删除字典中的所有元素
print(d)  # 输出清空后的字典

print("-----------------")

#修改
d = {}.fromkeys([i for i in string.ascii_letters ],'hi')  #  使用fromkeys方法创建字典

d['a'] = 1
print(d)  # 输出修改后的字典
print("-----------------")
d.update({"a":12}) # 使用update方法更新字典
print(d)  # 输出更新后的字典
print("-----------------")

# 查询
import string

d = {}.fromkeys([i for i in string.ascii_letters ],'hi')  #  使用fromkeys方法创建字典
print(d['a']) # 输出键'a'对应的值
print(d.get('a'))  # 使用get方法查询键'a'对应的值
print(d.keys()) # 输出字典中的所有键
print(d.items())  
print(d.values())  # 输出字典中的所有值


# 复制
import string
import copy

d = {}.fromkeys([i for i in string.ascii_letters ],'hi')  #  使用fromkeys方法创建字典
d2 = d.copy()  # 使用copy方法复制字典
print(d2)  # 输出复制后的字典

d3 = copy.copy(d)  # 使用copy模块的copy方法复制字典
print(d3)  # 输出复制后的字典


#字典转列表
import string
d = {}.fromkeys([i for i in string.ascii_letters ],'hi')  #  使用fromkeys方法创建字典
d1 = list(d.values())  # 将字典的值转换为列表
print(d1)  # 输出列表

for i in d.values():  # 遍历字典的值
    print(i)  # 输出每个值

for group in d.items():  # 遍历字典的键值对
    k, v = group  # 解包键值对
    print(k, v)  # 输出键和值


#列表转字典
import string
d = {}.fromkeys([1,2,3],"hi")  # 使用fromkeys方法创建字典
print(d)  # 输出字典


#字典推导式
a = {k:d[k] for k in d.keys()}
print(a)  # 输出字典推导式生成的字典

import string
d = {}.fromkeys([i for i in string.ascii_letters ],'hi') #  使用fromkeys方法创建字典
b = {k:d[k] for k  in d.keys() if k.isupper()}  # 使用字典推导式筛选出大写字母的键值对
print(b)  # 输出筛选后的字典
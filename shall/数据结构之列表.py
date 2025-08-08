import copy
import string

a = [1,2,3,4,5,6,7,8,9,10]

#索引

#正向
print(a[0])  # 正向输出列表的第一个元素
#逆向
print(a[-1])  # 反向输出列表的最后一个元素
#技巧
x = int(input("请输入一个数字："))
print(a[x])
print(a[x+1])
print(a[2*x+1])

#切片
#正向
print(a[0:5])  # 输出列表的前五个元素
print(a[2:]) # 输出列表从第三个元素开始到最后的所有元素
#逆向
print(a[-5:])  # 输出列表的最后五个元素
print(a[:-5])  # 输出列表的前五个元素
print(a[6:1000])  # 输出列表从第七个元素开始到最后的所有元素

#混合索引切片
print(a[3:-1]) # 输出列表从第四个元素到倒数第二个元素的所有元素

#在切片内间隔
print(a[:]) # 输出列表的所有元素
print(a[::1]) #  输出列表的所有元素
print(a[0::2])  # 输出列表的所有偶数索引元素
print(a[0:8:1]) # 输出列表的前八个元素
print(a[1:8:3]) # 输出列表从第二个元素开始到第八个元素，每隔三个元素取一个


print("-----------------")

#添加
x = int(input("请输入一个数字："))
a.append(x)  # 在列表末尾添加一个元素
print(a)
print("-----------------")
a.insert(3, x)  # 在列表的第四个位置插入一个元素
print(a)
print("-----------------")
a.extend([11,12,13])  # 在列表末尾添加多个元素
print(a)
print("-----------------")
z = a + [14,15,16]  # 连接两个列表
print(z)
print("-----------------")


#删除
a.remove(x)  # 删除列表中第一个出现的指定元素
print(a)
print("-----------------")
a.clear()  # 删除列表中的所有元素
print(a)
print("-----------------")
a = [1,2,3,4,5,6,7,8,9,10]
print(a)
print("-----------------")
a = []
print(a)
print("-----------------")

#修改
a = [1,2,3,4,5,6,7,8,9,10]
a[1] = 20  # 修改列表中第二个元素的值
print(a)
print("-----------------")

#查询
print(a[1]) # 输出列表中第二个元素的值
print(a.count(1)) # 统计列表中某个元素出现的次数

#排序
a.sort()  # 对列表进行升序排序
print(a)
print("-----------------")
a.reverse()  # 对列表进行降序排序
print(a)
print("-----------------")

#复制

b = a # 复制列表
print(f"这是a.clear()之前的b的列表{b}")
a.clear()  # 删除列表中的所有元素
print(a)
print(f"这是a.clear()之后b的列表{b}")  # b仍然保留原列表的值


a = [1,2,3,4,5,6,7,8,9,10]
b = a.copy()  # 复制列表
print(f"这是a.clear()之前的b的列表{b}")
a.clear()  # 删除列表中的所有元素
print(a)
print(f"这是a.clear()之后b的列表{b}")  # b仍然保留原列表的值
print("-----------------")

a = [1,2,3,4,5,6,7,8,9,10]
b= a[:]  # 复制列表
print(f"这是a.clear()之前的b的列表{b}")
a.clear()  # 删除列表中的所有元素
print(a)
print(f"这是a.clear()之后b的列表{b}")  # b仍然保留原列表的值
print("-----------------")

a = [1,2,3,4,5,6,7,8,9,10]
b = copy.copy(a)  # 复制列表
print(f"这是a.clear()之前的b的列表{b}")
a.clear()  # 删除列表中的所有元素
print(a)
print(f"这是a.clear()之后b的列表{b}")  # b仍然保留原列表的值
print("-----------------")



# 堆栈
a = [1,2,3,4,5,6,7,8,9,10]
b =a.pop()  # 弹出列表的最后一个元素
print(f"弹出的元素是：{b}")
print(f"弹出元素后列表的值是：{a}")

#其他
range(12) # 生成一个从0到11的整数序列
b = list(range(12))  # 将整数序列转换为列表
print(b)  # 输出列表
print("-----------------")

c = sum(b)  # 计算列表中所有元素的和
print(c)  # 输出列表元素的和
print("-----------------")

d = len(b)  # 计算列表的长度
print(d)  # 输出列表的长度
print("-----------------")



#列表解析式

#正常的
string.ascii_letters
print(string.ascii_letters)
print("-----------------")
b = [i for i in string.ascii_letters]  # 将字符串中的每个字符转换为列表中的一个元素
print(b)  # 输出列表1
print("-----------------")
s =[i for i in string.ascii_letters if i.isupper()]  # 将字符串中的每个大写字母转换为列表中的一个元素
print(s)  # 输出列表2
print("-----------------")

#成员判断
print('A' in s)  # 判断列表中是否包含指定元素
print('a' in s)  # 判断列表中是否包含指定元素

#解包
first,*others,before_last,last = b
print(first)
print(others)
print(before_last)
print(last)

#例子
a = ["www.baidu.com"]
first,*others,last = a[0].split('.')
print(first)
print(others)
print(last)
#创建数据

a =1   #  整数类型

f1 = 1.1 # 浮点类型

word = "hello"    #字符串类型

w_1  = 'good'

#三引号字符串  用于折现

w_2  = '''      
a long string  here   
this is extra line
'''

b1 = True   #布尔类型

b2 = False

THAT = "password"

THIS = 42    #在python种  变量全部大写 往往代表着是常量   通常来说 不希望被修改


#使用数据

print(42)   #打印数据

len("hello")  #用来测量长度

print(len("hello") )

print("qweqweqw".capitalize())   

r3 = a + THIS   #运算式

print(r3)
new_word = THAT + w_1
print(new_word) #字符串拼接


r1 = b1+ b2  #布尔类型的运算
print(r1)  #布尔类型的运算结果是整数

r2 = b1 and b2  #布尔类型的运算
print(r2)  #布尔类型的运算结果是布尔类型

r4 = b1 or b2  #布尔类型的运算
print(r4)  #布尔类型的运算结果是布尔类型



#修改数据
x = 12
print(x)
print(x+1)

x = x + 1  #修改变量的值
print(x)
x += 1  #修改变量的值
x -= 1  #修改变量的值
print(x)


#删除数据
del x  #删除变量
# print(x) #会报错，因为x已经被删除了



print(type('this'))

print(type(b'this is a string'))

# print(b'this is a string'+'zzzz')   #TypeError: can't concat str to bytes


#转码
z = "中文"
print(z.encode('utf-8'))  # b'\xe4\xb8\xad\xe6\x96\x87'

f = b'\xe4\xb8\xad\xe6\x96\x87'
print(f.decode('utf-8'))  # 中文

print(dir(str))  # 查看字符串的所有方法
print(help(str))  # 查看字符串的帮助文档  按回车显示more内容

# 文本处理
a = 'hello'
print(a.capitalize())  # Hello  capitalize() 不会改变变量 a 的值，只是返回一个新的字符串

print(a) 

b = a.capitalize()  # 将结果赋值给 b
print(b)  # Hello


print('that is bin'.split()) # ['that', 'is', 'bin']  split()将字符串分割成列表

g = 'that is bin'.split()  # 将结果赋值给 g
print(g[-1])  

print('that is bin'.partition(" "))# ('that', ' ', 'is bin')  partition()将字符串分割成三部分
print('that is bin'.rpartition(" ")) # ('that is', ' ', 'bin')  rpartition()从右边开始分割


print('this'.replace('i','I')) # thIs  replace()替换字符串中的字符
print('this'.replace('i','I').replace('s','S')) # thIS  可以链式调用

print('this'.translate(str.maketrans({'i': 'I', 's': 'S'})))  # 正确输出 thIS # thIS  translate()使用字典进行字符替换  str.translate() 方法需要传入一个“字符映射表”，而不是直接用字典。

print('this:'.strip(':'))  # this  strip()去除字符串两端的指定字符
print(".".join(["this", "is", "a", "test"]))  # this.is.a.test  join()将列表中的字符串连接成一个字符串，使用指定的分隔符
print(" ".join(["this", "is", "a", "test"]))  # this is a test  使用空格作为分隔符

#文本索引
print('that'.count('t'))  # 2  count()统计字符串中某个字符出现的次数
print('hello'.find('e')) # 1  find()返回子字符串第一次出现的位置，如果未找到则返回 -1
print('hello'.find('l')) # 2  find()可以找到多个字符中的第一个位置
print('hello'.rfind('l')) # 3  rfind()从右边开始查找，返回子字符串最后一次出现的位置
print('hello'.find('x')) # -1  如果未找到子字符串，find()返回 -1
# 下面的代码会抛出异常，因为 'x' 不在 'hello'
print('hello'.index('e')) # 1  index()与find()类似，但如果未找到子字符串会抛出 ValueError
print('hello'.index('l')) # 2   # index()可以找到多个字符中的第一个位置
print('hello'.rindex('l')) # 3  rindex()从右边  开始查找，返回子字符串最后一次出现的位置
#print('hello'.index('x')) # ValueError: substring not found  如果未找到子字符串，index()会抛出异常

#装饰
print('Hello'.swapcase()) # hELLO  swapcase()将字符串中的大写字母转换为小写字母，小写字母转换为大写字母
print('Hello'.casefold()) # hello  casefold()将字符串转换为小写字母，适用于不区分大小写的比较
print('Hello'.upper())  # HELLO  upper()将字符串转换为大写字母
print('Hello'.lower())  # hello  lower()将字符串转换为小写字
print('Hello'.center(11,'-'))  #   Hello    center()将字符串居中对齐，填充指定的字符（默认是空格）
print('Hello'.zfill(20))  # 0000000000000000Hello  zfill()将字符串左侧填充零，直到达到指定的长度  方法只能填充数字 0，不能指定其他字符。
print('Hello'.ljust(20,'-'))  # Hello----------------  ljust()将字符串左对齐，右侧填充指定的字符（默认是空格）
print('Hello'.rjust(20,'-'))  # ----------------Hello  rjust()
print('He\tllo'.expandtabs(4))  # Hello  expandtabs()将字符串中的制表符（\t）替换为指定数量的空格（默认是 8 个空格），这里设置为 4 个空格

#判断类型
print('yyk-9527'.startswith('yyk'))  # True  startswith()判断字符串是否以指定的前缀开头
print('2220702632@qq.com'.endswith('@qq.com'))  # True  endswith()判断字符串是否以指定的后缀结尾

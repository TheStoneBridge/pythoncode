# class Student:
#     # 构造方法：创建对象时自动执行
#     def __init__(self, name, age):
#         self.name = name  # 实例属性
#         self.age = age

#     # 实例方法
#     def introduce(self):
#         print(f"我叫{self.name}，今年{self.age}岁")

# # 创建对象
# s1 = Student("小明", 18)
# s1.introduce()  # 调用方法
# print(s1.name)  # 访问属性

# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def add(self):
#         return self.num1 + self.num2

#     def sub(self):
#         return self.num1 - self.num2

# c = Calculator(10, 5)
# print(c.add())  # 15
# print(c.sub())  # 5

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_info(self):
        print(f"书名：{self.title}，作者：{self.author}，价格：{self.price}")

book = Book("Python爬虫", "张三", 59.9)
book.show_info()
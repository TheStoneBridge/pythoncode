# 编写程序，输入两个数，计算除法。 
# 要求捕获：
# 除以 0
# 输入不是数字
# try:
#     a = int(input("请输入一个数字："))
#     b = int(input("请输入另一个数字："))
#     result = a / b
#     print("结果是：", result)
# except ValueError:
#     print("错误：输入的不是有效数字！")
# except ZeroDivisionError:
#     print("错误：除数不能为0！")


# 给定列表 list1 = [1, 2, 3]
# 让用户输入索引，输出对应元素。
# 要求捕获：
# 索引越界异常
# 输入不是整数异常
# try:
#     list1 = [1, 2, 3]
#     x = int(input("请输入一个索引：")) #字符串小数 → int 直接报错    浮点数 → int 可以转   索引场景 → 只写 int (input ()) 最正确
#     print(list1[x])
# except IndexError:
#     print("错误：索引超出范围！")
# except ValueError:
#     print("错误：输入的不是有效数字！")


# 编写程序，尝试打开并读取文件 data.txt。
# 要求：
# 捕获文件不存在异常
# 最后用 finally 输出 “文件操作结束”
try: 
    f = open("data1.txt", "r",encoding="utf-8")
    data = f.read()
    print(data)
except FileNotFoundError:
    print("错误：文件不存在！")
finally:
    print("文件操作结束")
# try /except
#当程序运行时出现错误（异常），程序会直接崩溃停止。
# 使用 try / except 可以捕获错误、处理错误，让程序继续运行

# 常见异常类型
# ZeroDivisionError: 除数为0
# NameError: 变量未定义
# IndexError: 索引超出范围
# KeyError: 字典中不存在该键
# TypeError: 类型错误
# ValueError: 值错误
# FileNotFoundError：文件不存在

# 示例 1：捕获数字转换异常
# try:
#     user_input = input("请输入一个数字：")
#     num = int(user_input)
#     print("转换成功，数字是：", num)
# except ValueError:
#     print("错误：你输入的不是有效数字！")

# print("程序正常结束")

# 示例 2：捕获除零错误
# try:
#     a = 10
#     b = 0
#     result = a / b
#     print("结果是：", result)
# except ZeroDivisionError:
#     print("错误：除数不能为0！")

# print("程序正常结束")

# 示例 3：捕获多种异常 + finally
# try:
#     lst = [1, 2, 3]
#     print(lst[99])
# except IndexError:
#     print("索引超出范围")
# except Exception as e:
#     print("其他错误：", e)
# finally:
#     print("操作结束")






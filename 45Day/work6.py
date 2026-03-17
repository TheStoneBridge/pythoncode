from functools import wraps
# 姓名 + 成绩闭包
def student(name):
    def info(score):
        return f"{name}的成绩是{score}"
    return info

zhang = student("张三")
print(zhang(100))

# 温度转换闭包
def temp_convert(type):
    if type == "c2f":
        def convert(c):
            return c * 9/5 + 32
    else:
        def convert(f):
            return (f - 32) *5/9
    return convert

c2f = temp_convert("c2f")
print(c2f(0))  # 32.0


def work(func):
    def wrapper(*args, **kwargs):
        print("开始工作")
        result = func(*args, **kwargs)
        print("结束工作")
        return result
    return wrapper

@work
def do_work():
    print("正在工作")

do_work()


def count_calls(func):
    count = 0
    @wraps(func)    #只要写装饰器，默认必加 @wraps (func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count +=1
        print(f"调用次数：{count}")
        return func(*args, **kwargs)
    return wrapper

@count_calls
def test():
    pass

test() # 1
test() # 2


def func_return_add_ten(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 10
    return wrapper

@func_return_add_ten
def add():
    return 5
print(add())  # 15

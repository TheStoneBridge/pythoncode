# 闭包：函数嵌套 + 内部函数引用外部函数变量 + 外部函数返回内部函数，是装饰器的基础。
# 装饰器：基于闭包实现，不修改原函数代码，为函数动态添加功能（语法糖 @）

# 基础闭包（计数器）
def outer(count):
    # 外部函数变量
    def inner():
        # 内部函数引用外部变量
        nonlocal count  # 声明修改外部变量
        count += 1
        return count
    # 外部函数返回内部函数对象（不加括号）
    return inner

# 创建闭包实例
counter = outer(0) #inner 记住了 outer 的 count 变量，即使外部函数执行完毕，变量依然保留。
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3


#带参数的闭包
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

# 生成 乘以2、乘以5 的函数
double = make_multiplier(2)
five_times = make_multiplier(5)

print(double(10))   # 20
print(five_times(10)) # 50

# 闭包保存状态
def person_info(name):
    def info(age):
        return f"姓名：{name}，年龄：{age}"
    return info

# 闭包永久保存姓名
zhang = person_info("张三")
li = person_info("李四")

print(zhang(20))  # 姓名：张三，年龄：20
print(li(22))    # 姓名：李四，年龄：22

# 装饰器函数
def log_decorator(func):
    def wrapper():
        print(f"执行函数：{func.__name__}")
        func()  # 调用原函数
        print("函数执行完毕")
    return wrapper

# 装饰器的本质，就是把被修饰的函数，当成参数传给了装饰器函数。
# 基础装饰器（打印函数执行日志）
@log_decorator
def say_hello():
    print("Hello World!")

say_hello()

#带参数的装饰器
def log_decorator(func):
    # wrapper接收原函数参数
    def wrapper(*args, **kwargs):
        print(f"开始执行：{func.__name__}")
        # 传递参数给原函数
        result = func(*args, **kwargs)
        print(f"执行结束，结果：{result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 5)  # 自动打印日志

#计时装饰器（统计函数执行时间）
import time

def timer(func): #这个代码里，wrapper(*args, **kwargs) 写不写这些参数都能跑，功能完全一样。
# 但是 —— 写 *args, **kwargs 是【标准、通用、专业】的写法！
# wrapper()
# → 只能装饰 无参函数
#wrapper(*args, **kwargs)
# → 所有函数都能装饰（万能通用）
# 写装饰器的标准规范就是：永远写万能参数，让它通用！
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"函数耗时：{end - start:.4f}秒")
        return res
    return wrapper

@timer
def test_func():
    time.sleep(1)  # 模拟耗时操作

test_func()

# 装饰器的参数，无法通过方法调用来传参，
# 只能嵌套一层方法来传装饰器需要的参数！
def repeat(times):
    # 三层嵌套：装饰器工厂
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

# 让函数重复执行3次
@repeat(3)
def print_msg(msg):
    print(msg)

print_msg("Hello")


from functools import wraps

#装饰器保留原函数元信息（必备）
# 默认装饰器会覆盖原函数名，用 functools.wraps 修复：  穿着原函数 “衣服” 的 wrapper 函数！**
#  @wraps 根本不改功能，只改函数信息！调用效果还是装饰后的效果！
def log_decorator(func):
    @wraps(func)  # 保留原函数信息
    def wrapper(*args, **kwargs):
        print("日志：执行中")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def test():
    """这是测试函数"""
    pass

print(test.__name__)  # test（未被覆盖）
print(test.__doc__)   # 这是测试函数
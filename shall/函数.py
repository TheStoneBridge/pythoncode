# 使用
z = print() # 使用函数
pt = print #给函数重命名
pt('hello world')


#定义
def hello():  # 定义一个无参函数
    print('hello')

hello()

def  rectangle(width,height):  # 定义一个有参函数
    return width * height
print('这个矩形的面积是:', rectangle(5,6))


#类型 trick
def example(head:str,butt:str) -> str:  # :str表示参数的类型   -> str表示返回值的类型
    if head.startswith('?'):
        head = head[1:]
    return head + butt
e = example('?hello', 'world')
print(e)
 

# One more thing
#装饰器
#rule
#(func) -> func  接收一个函数，返回一个函数
def useless(func):
    def deco():
        return func()+1
    return deco
@useless
def one():
    return 1
print(one())



#关键词参数
def  date_gen(m,d):
    return f'2025-{m}-{d}'
print(date_gen(m=12,d=31))


def  date_gen(m,d,y=2025):
    return f'{y}-{m}-{d}'
print(date_gen(m=12,d=31))


def formatter(num ):
    if 1<=num<=9:
        return f'0{num}'
    return num

def  date_gen(m,d,y=2025):
    m = formatter(m)
    d = formatter(d)
    return f'{y}-{m}-{d}'
print(date_gen(m=1,d=31))


#偏函数   :  简化带有复杂参数的函数
def formatter(num):
    if 1<=num<=9:
        return f'0{num}'
    return num
def  date_gen(m,d,y=2025,sep='-',with_prefix=None):
    m = formatter(m)
    d = formatter(d)
    if with_prefix:
        return f'{with_prefix}:{y}{sep}{m}{sep}{d}'
    return f'{y}{sep}{m}{sep}{d}'

def date_slash(m,d,y=2025):
    return date_gen(m,d,y,sep='/',with_prefix='日期')
print(date_gen(m=1,d=31))
print(date_slash(1,31))



#闭包 outer函数返回了inner函数  这个返回的inner函数就叫闭包
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

#eg
def setup():
    #lots stuff here
    def install():
        pass
    return install
intsaller = setup()
intsaller()



# *args **kwargs   *args用来给函数传递任意数量的参数  是个数组  **kwargs用来给函数传递任意数量的参数   是个字典
def show(*args,**kwargs):
    print(args)
    print(kwargs)
    
def formatter(num):
    if 1<=num<=9:
        return f'0{num}'
    return num
def  date_gen(m,d,y=2025,sep='-',with_prefix=None):
    m = formatter(m)
    d = formatter(d)
    if with_prefix:
        return f'{with_prefix}:{y}{sep}{m}{sep}{d}'
    return f'{y}{sep}{m}{sep}{d}'

def date_slash(m,d,y=2025):
    return date_gen(m,d,y,sep='/',with_prefix='日期')

print(date_gen(m=1,d=31))
print(date_slash(1,31))    
print(show(1,2,3,something='hello',something_else='world'))


#eg
def formatter(num):
    if 1<=num<=9:
        return f'0{num}'
    return num
def  date_gen(m,d,y=2025,sep='-',with_prefix=None):
    m = formatter(m)
    d = formatter(d)
    if with_prefix:
        return f'{with_prefix}:{y}{sep}{m}{sep}{d}'
    return f'{y}{sep}{m}{sep}{d}'
def date__with_sub(m,d,*args):
    sub = f'''
    |
    +--->{' ' .join (args)}
    '''
    main_str =  date_gen(m,d,y=2025,sep='/',with_prefix='日期')
    return date_gen(m,d)+sub

print(date__with_sub(1,31,'xixi','heihei'))



#类函数
class Nothing:
    @staticmethod
    def hello():
        print('hello world')
Nothing.hello()


#匿名函数
result = lambda x:x+1
print(result(1))
result = lambda x,y:x+y
print(result(1,2))

r2 = map(lambda x:x+1,[1,2,3])
print(list(r2))
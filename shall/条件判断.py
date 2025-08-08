# TODO把式
# if else elif
# 多个事件判断   -if  。。。if
# 单个事件多种特征   -if  ....elif

# TODO细则
'''
都会先判断第一个条件，只有当第一个条件不成立时，才会依次判断后续的elif条件，且仅执行第一个满足的分支。  一个符合  后面就不执行了

'''
user_input = "123"
another_thing = False
if user_input:
    print("hello world")
elif user_input.startswith("1"):
    print("hello world 1")
elif user_input.endswith("3"):
    print("hello world 3")

if another_thing:
    print("another thing is true")
    
    
    
#单一事件捕捉

post = input("请输入内容")

if '@' in post:
    print("内容中包含@符号无效输入")
elif 1 <= len(post) <= 10:
    print(f'you said: {post}   ')
else:
    print("内容长度不能小于1或大于10")  
    
#多事件捕捉  关联性    例子：且
user = input("请输入账号")
pwd = input("请输入密码")
user_db = {
    "2220702632":"zxcqwe123"
}
if  user in user_db and pwd == user_db[user]:
    print("登录成功")
else:
    print("账号或密码错误")
    
    
#多事件捕捉  时序性    
user = input("请输入账号")
user_db = {
    "2220702632":"zxcqwe123"
}
if user in user_db:
    pwd = input("请输入密码")
    if pwd == user_db.get(user):
        print(f'欢迎{user}登录')
    else:
        print("密码错误")
else:        
    print("账号不存在")        


#表达式
import string
print(string.punctuation)  #所有标点符号

# l = [p in '@yyk' for p in string.punctuation]
# print(l)  #判断标点符号是否在@yyk中


post = input("请输入评论")

if any( p in post for p in string.punctuation): #any  有一个为真就为真
    print("评论中包含标点符号")
elif len(post) < 1 or len(post) > 10:
    print("评论长度不符合要求")
else:
    print(f"评论内容：{post}")        
    

#三目运算符
import random
a = "first" if random.choice([True,False]) else "second"
print(a)
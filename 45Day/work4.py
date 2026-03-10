class Person:
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
    
    def say_hello(self):
        print("你好，我是%s，今年%d岁，性别%s"%(self.name,self.age,self.sex))

p1 = Person('ikun','男',18)
p1.say_hello()  


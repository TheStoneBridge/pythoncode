# 单继承和方法重写
# 父类
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "动物发出声音"

# 子类继承 Animal
class Dog(Animal):
    # 重写方法
    def speak(self):
        return f"{self.name} 汪汪叫"

class Cat(Animal):
    def speak(self):
        return f"{self.name} 喵喵叫"

# 测试
dog = Dog("旺财")
cat = Cat("咪咪")
print(dog.speak())  # 旺财 汪汪叫
print(cat.speak())  # 咪咪 喵喵叫




class Fly:
    def fly(self):
        return f"{self.name} 会飞"

# 多继承 + super () 调用父类方法
# 继承 Animal + Fly 两个父类
class Bird(Animal, Fly):
    def __init__(self, name):
        # super() 调用父类构造方法
        super().__init__(name)

bird = Bird("麻雀")
print(bird.speak())  # 动物发出声音（继承自Animal）
print(bird.fly())    # 麻雀 会飞（继承自Fly）


#经典多态（同一接口，不同实现）
# 统一调用函数（多态核心）
def make_sound(animal: Animal):
    print(animal.speak())

# 传入不同子类对象，执行不同逻辑
make_sound(Dog("小黑"))  # 小黑 汪汪叫
make_sound(Cat("小白"))  # 小白 喵喵叫
make_sound(Bird("鸽子")) # 动物发出声音

#基础 property（只读属性）
class Person:
    def __init__(self, name):
        self.__name = name  # 私有属性

    # 伪装成属性调用
    @property
    def name(self):
        return self.__name

p = Person("张三")
print(p.name)  # 张三（像属性一样使用，不用加()）
# p.name = "李四"  # 报错：只读属性，无法修改

#高级 property（可读写 + 校验）+ 继承多态组合
class Student(Person):
    def __init__(self, name, score):
        super().__init__(name)
        self.__score = score

    @property
    def score(self):
        return self.__score

    # 可修改 + 数据校验
    @score.setter
    def score(self, value):
        if not 0 <= value <= 100:
            raise ValueError("分数必须在0-100之间")
        self.__score = value

s = Student("小明", 90)
print(s.score)    # 90
s.score = 85      # 合法修改
# s.score = 150   # 报错：分数非法

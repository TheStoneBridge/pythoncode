# 定义父类 Vehicle（交通工具），有属性 brand、speed
# 定义子类 Car 继承它，新增方法 drive() 输出：品牌 + 速度行驶
# 创建对象并测试
# class Vehicle :
#     def __init__(self,brand,speed):
#         self.brand = brand
#         self.speed = speed

# class Car(Vehicle):

#     def drive(self):
#         print(f"{self.brand} is driving at {self.speed} km/h")

# car = Car("小米苏七", 120)
# car.drive()

# 基于 Vehicle 定义 Bike、Truck 子类
# 所有子类都重写 move() 方法
# 写一个函数 start_move(vehicle)，接收任意交通工具，调用 move()
# class Bike(Vehicle):

#     def move(self):
#         print(f"{self.brand}自行车慢慢骑行")

# class Truck(Vehicle):

#     def move(self):
#         print(f"{self.brand}卡车正在运输货物")

# def start_move(vehicle):
#     vehicle.move()

# start_move(Bike("小黄", 30))
# start_move(Truck("小蓝", 60))


# 定义 Book 类，私有属性 __price
# 用 @property 和 @price.setter 包装价格
# 限制：价格不能低于 0
# class  Book:

#     def __init__(self,price):
#         self.__price = price
    
#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self,value):
#         if value > 0:
#             self.__price = value
#         else:
#             raise ValueError("价格不能小于0")
        
# book = Book(0)
# book.price = 0
# print(book.price)


# 父类 Employee：属性 name，@property 方法 get_salary()
# 子类 FullTimeEmployee：月薪，实现 get_salary
# 子类 PartTimeEmployee：时薪 × 小时，实现 get_salary
# 多态调用：统一打印工资
# class Employee:
#     def __init__(self,name):
#         self.name = name 
    
#     @property
#     def get_salary(self):
#         return 0
# class FullTimeEmployee(Employee):
#     def __init__(self, name,monthly_salary):
#         super().__init__(name)    
#         self.monthly_salary = monthly_salary

#     @property
#     def get_salary(self):
#         return self.monthly_salary

# class PartTimeEmployee(Employee):
#     def __init__(self, name, hourly_rate, hours_worked):
#         super().__init__(name)
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked

#     @property
#     def get_salary(self):
#         return self.hourly_rate * self.hours_worked
    
# def show_salary(employees):
#     return employees.get_salary

# full_time_employee = FullTimeEmployee("张三", 5000)
# part_time_employee = PartTimeEmployee("李四", 20, 160)

# print(f"全职员工 {full_time_employee.name} 的薪水: {show_salary(full_time_employee)}")
# print(f"兼职员工 {part_time_employee.name} 的薪水: {show_salary(part_time_employee)}")


# 父类 Shape（图形），有抽象方法 area（用 property）
# 子类 Circle（圆）、Rectangle（矩形）实现 area
# 实现多态：传入任意图形，打印面积

import math
class Shape:

    @property
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

def print_area(shape):
    print(f"面积: {shape.area}")

# 测试
circle = Circle(5)
rectangle = Rectangle(4, 6)

print_area(circle)
print_area(rectangle)
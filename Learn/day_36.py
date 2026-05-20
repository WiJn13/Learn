# day_36.py

# 核心复习内容：面向对象编程 (OOP) 基础

## 1. 类 (Class) 与 对象 (Object)
    ### 1.1. 定义：类是蓝图，对象是实例
    ### 1.2. 语法：`class ClassName:`
    ### 1.3. 实例化：`obj = ClassName()`

## 2. 构造方法 `__init__`
    ### 2.1. 作用：初始化对象属性
    ### 2.2. `self` 的含义：指向实例本身

## 3. 实例属性与方法
    ### 3.1. 定义属性：`self.attribute = value`
    ### 3.2. 定义方法：`def method(self):`

## 4. 封装 (Encapsulation)
    ### 4.1. 私有属性与方法：`__attribute` (双下划线)
    ### 4.2. Getter 与 Setter 方法：控制属性访问

## 5. 继承 (Inheritance)
    ### 5.1. 语法：`class Child(Parent):`
    ### 5.2. 方法重写 (Override)
    ### 5.3. `super()` 函数：调用父类方法

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def meow(self):
        return f'{self.name}正在喵喵叫'
    
my_cat = Cat('猫猫', '橘猫')
print(my_cat.name)
print(my_cat.meow())
print(my_cat.breed)

class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = None   # 私有属性，外部无法直接访问
        self.set_age(age)   # 调用setter方法初始化年龄，确保数据合规

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if isinstance(age, int) and 0 < age < 120:
            self.__age = age
        else:
            print('年龄必须0-120之间的整数')

p = person('小王', 13)
print(p.name)
print(p.get_age())
p.set_age(-3)
print(p.get_age())
p.__age = 15    # 创建了一个新的公有属性 __age
print(p.__age)  # 15
print(p._person__age)   # 13，打印出被封装的年龄，一般不建议直接访问

class NewPerson:
    def __init__(self, name, age):
        self._name = name
        self._age = None
        self.age = age

    @property   # 内置装饰器。把一个方法变成只读属性（相当于设置get_age())
    def age(self):
        return self._age
    
    @age.setter # 内置装饰器。和property搭配使用，age是property装饰的方法
    def age(self, value):
        if isinstance(value, int) and 0 < value < 120:
            self._age = value
        else:
            print('年龄必须是0-120的整数')

p2 = NewPerson('小杰', 24)
print(p2._name)
print(p2.age)
p2.age = -1
print(p2.age)

class status:
    def __init__(self, name , life):
        self.name = name
        self.life = life

class warrior(status):
    def attack(self):
        print('挥剑攻击×1')
class master(status):
    def attack(self):
        print('魔法攻击×1')

a = warrior('King', 13)
print(a.name)
print(a.life)
b= master('Jack',11)
print(b.name)
print(b.life)


    
# 6. 组合
class Job:
    def __init__(self, job_name, attack_style):
        self.job_name = job_name
        self.attack_style = attack_style
class character:
    def __init__(self, name, life, Job):
        self.name = name
        self.life = life
        self.job = Job

job1 = Job('warrior', '挥剑')
job2 = Job('master', '远程魔法攻击')
job3 = Job('shooter', '射击')
a = character('亚瑟', 23, job1)
b = character('杨玉环', 251, job2)
c = character('狄仁杰', 21, job3)
print(a.name)
print(a.life)
print(a.job.attack_style)
print(a.job.job_name)

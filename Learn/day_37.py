# TITLE: 面向对象编程进阶
# CATEGORY: 面向对象编程
# day_37.py


# 核心复习内容：面向对象编程 (OOP) 进阶

## 1. 方法重写 (Override)
    ### 1.1. 定义：子类定义与父类同名的方法
    ### 1.2. 作用：改变子类的行为，实现多态

## 2. `super()` 函数
    ### 2.1. 作用：调用父类的方法
    ### 2.2. 场景：在子类中扩展父类的 `__init__` 或其他方法

## 3. 多态 (Polymorphism)
    ### 3.1. 定义：不同对象对同一消息做出不同响应
    ### 3.2. 意义：提高代码的灵活性和可扩展性

## 4. 类属性与类方法
    ### 4.1. 类属性：所有实例共享的属性
    ### 4.2. 类方法 (`@classmethod`)：操作类属性的方法
    ### 4.3. 静态方法 (`@staticmethod`)：与类和实例无关的工具方法


# 1. 方法重写
class Animal:
    def speak(self, name):
        self.name = name
        print(f'{self.name}叫了。')
class Dog(Animal):
    def speak(self):
        print('汪汪')
d = Dog()
d.speak()
c = Animal()
c.speak('猫')

# 2. super()函数
class Animal:
    def __init__(self, name):
        self.name = name
        
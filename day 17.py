#!/usr/bin/env python3
# -*- cording: utf-8 -*-

'a test module'

__author__ = 'Walter Wang'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello,World!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many argument!')

if __name__=='__main__':
    test()
# NOTE:
# 面向过程的程序射击： 把计算机程序视为一系列的命令集合，即一组函数的顺序执行。
# 为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

# 面向对象的程序设计： 把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，
# 计算机程序的执行就是一系列消息在各个对象之间传递。

'''一、定义类: class'''
class Student(object):
    pass
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，
# 紧接着是(object)，表示该类是从哪个类继承下来的，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

'''二、创建实例: 类名+()'''
bart = Student()
print(bart) # <__main__.Student object at 0x000002249CC76E40>
print(Student)  # <class '__main__.Student'>
# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
class Student(object):
    def __init__(self,name,score):
        self.name= name
        self.score = score
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
# 但self不需要传，Python解释器自己会把实例变量传进去
bart = Student('Bart Simpson',90)
print(bart.name)    # Bart Simpson
# 在类中定义的函数仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

class Student(object):
    def __init__(self,name,age,score,height,weight):
        self.name = name
        self.age = age
        self.score = score
        self.height = height
        self.weight = weight
    def info(self):
        print(f'姓名：{self.name}\n年龄：{self.age}\n身高：{self.height}\n体重：{self.weight}\n成绩：{self.score}')
Wang = Student('Wang',18,100,160,45)
Wang.info()


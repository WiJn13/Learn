# TITLE: 类属性、实例属性与动态属性
# CATEGORY: 面向对象·类与实例属性
class Student(object):
    def __init__(self,name):
        self.name = name

s = Student('Bob')
s.score = 90

class Student(object):
    name = 'Student'

class Student(object):
    count = 0

    def __init__(self,name):
        self.name = name
        Student.count += 1



# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('lisa')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

print(Student.count)    # 2
print(lisa.name)    # lisa

class Student(object):
    pass
s = Student()
s.name = 'Walter'   # 动态给实例绑定一个属性

def set_age(self,age):  # 定义一个函数作为实例方法
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age,s)   # 给实例绑定一个方法
s.set_age(25)   # 调用实例方法
print(s.age)    # 25

class light(object):
    def set_state(self):
             pass
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
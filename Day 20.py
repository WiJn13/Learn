class Student():
    pass
s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)   # Michael
def set_age(self,age):  #定义一个函数作为实例方法
    self.age = age
from types import MethodType
# 使用 MethodType 将 set_age 绑定为 s 实例的方法，使其第一个参数自动接收实例自身（self）
s.set_age = MethodType(set_age,s)   # 给实例绑定该方法
s.set_age(25)   # 调用实例方法
print(s.age)   # 测试结果,25

s2 = Student()  # 创建新的实例
# 下面直接调用会报错，因为 set_age 只绑定到了 s 实例，而不是 Student 类
try:
    s2.set_age(30)  # 尝试调用方法（预期 AttributeError）
except AttributeError as e:
    print('错误: s2 没有 set_age 方法 ->', e)
    print('演示：将函数绑定到类，之后所有实例都可以调用该方法')
    # 把函数绑定到类，这样所有实例都可以调用（调用时 self 会是各自实例）
    Student.set_age = set_age
    s2.set_age(30)
    print('s2.age (绑定到类后):', s2.age)

try:
    class Student(object):
        __slots__ = ('name','age')  # 用tuple定义允许绑定的属性名称
    s = Student()
    s.name = 'Walter'   # 绑定属性'name'
    s.age = 25  # 绑定属性'age'
    s.score = 99    # 绑定属性'score'
    print(s.score)
except AttributeError as e:
    print('错误: 不能绑定 score 属性 ->', e)
# 子类不定义__slots__，则不起作用
# 如果子类定义__slots__，则：
# 子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class SubStudent(Student):
    __slots__ = ('high','__dict__')
m = SubStudent()
m.name = 'WiJn'
m.high = 56
print(m.name)   # WiJn
print(m.high)   # 56
try:
    m.score = 78
    print(m.score)
except AttributeError as e:
    print('错误: 不能绑定score属性 ->',e)

class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value> 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    
class Screen(object):
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @property
    def resolution(self):
        return self._height * self._width
    @width.setter
    def width(self,value1):
        self._width = value1
    @height.setter
    def height(self,value2):
        self._height = value2
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

class Runnable:
    def run(self):
        print("Running...")

class Flyable:
    def fly(self):
        print("Flying...")

class Animal:
    pass

class Bird(Animal, Flyable):
    pass

class Dog(Animal, Runnable):
    pass



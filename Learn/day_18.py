# TITLE: 封装、私有属性与 getter/setter
# CATEGORY: 面向对象编程
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s'& (self.name, self.score))
    
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
        
# 练习：
class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender
    
    def set_gender(self,gender):
        if gender in ('male','female'):
            self.__gender = gender
        else:
            raise ValueError('输入错误')
# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


# 判断对象类型：type()
print(type(234))

import types
def fn():
    pass
print(type(fn)==types.FunctionType) # True
print(type(abs)==types.BuiltinFunctionType) # True
print(type(lambda x: x)==types.LambdaType)  #True
print(type(x for x in range(10))==types.GeneratorType)  # True


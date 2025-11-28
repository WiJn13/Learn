from enum import Enum, unique
@unique
class Weekday(Enum):
     Sun = 0    # Sun的value被定义为0
     Mon = 1
     Tue = 2
     Wed = 3
     Thu = 4
     Fri = 5
     Sat = 6

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue.name) # Tue
print(Weekday.Wed.value)    # 3
print(day1 == Weekday.Sat)  # False
print(Weekday(4))   # Weekday.Thu
'''
Weekday(4)
#   Weekday.Thu
一个枚举成员对象
Weekday(4).name
#   Thu
成员的名字（字符串）
Weekday(4).value
#   4
成员的值（整数）
'''
print(type(Weekday.Mon)) # <enum 'Weekday'>

from enum import Enum, unique
@unique
class Gender(Enum):
     Male = 0
     Female = 1
class Student(object):
     def __init__(self, name, gender):
          self.name = name
          self.gender = gender
bart = Student('Bart', Gender.Male)

if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
  
    
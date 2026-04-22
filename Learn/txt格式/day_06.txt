# TITLE: 不可变对象、dict/set 与基础函数
# CATEGORY: Python基础
# 2025.08.28\29
# NOTE:
# dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这种通过key计算位置的算法成为哈希算法(Hash)。
# set：集合。集合里没有重复的元素，所以可以用来去重，⚠️注意：集合无序
# tuple，str，int，float，bool不可变
a = 'abc'
a = a.replace('a','A')
print(a)
# 字符串自身是不可变的。Abc可以理解为一个新的字符串。
# 所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容
# 且这些方法会创造新的对象并返回，这样，就保证了不可变对象本身永远是不可变的
a= ''.join(a)
print(a)
try:

    a[0] = 'A'  # 字符串不可变
    print(a)
except TypeError:
    pass

lst = list(a)
lst[0] = 'A'
b = ''.join(a)
print(b)

print(2 ** 4)

# note:函数
# 一、
def area_of_circle(x):  # 定义area_of_circle这个函数
    import math  # 记得先导入math模块
    return math.pi * x * x  # 返回圆的面积；math.pi 是math模块里的浮点常量，圆周率π
                            # return只能放在函数里
s = area_of_circle(2)
print(f'{s:.2f}')  # 12.57 

# 二、
print(abs(100))    # 100；absolute
print(abs(-20))    # 20
print(abs(3.2))    # 3.2
print(max(3,5,2,7,11)) # 11
print(min(2,6)) # 2
print(round(3.141592653589,3)) #3.14
print(divmod(10,3))    # (3,1)同时返回商和余数；divide+modulo
print(pow(2.1,3))   # 2.1**3；power
print(pow(10,3,100))   # 10**3%100
import math 
print(math.ceil(3.3))  #4；表示向上取整
print(math.floor(2.1)) #2；表示向下取整
# ceil/floor 属于“数学库”的函数集合（针对浮点数的精确取整与其它数学函数一起）
# Python 把最常用的基础函数放在 builtins（如 max/min/abs/round/pow/divmod）
# 把更专门的数学函数放到 math 模块，使用前需 import math。
# 这是语言设计和职责分工的结果。

# 三、数据类型转换函数
print(int('3'))    # 3
print(int(12.5))   # 12
print(str(12.5))   # '12.5'
print(float('12.5'))   # 12.5
print(float(12))   # 12.0
print(f'{float(12):.2f}')  # 12.00
print(bool(0)) # False
print(bool(2)) # True；任何非0都是True




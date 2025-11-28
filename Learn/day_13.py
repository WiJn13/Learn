# TITLE: Iterable、Iterator 与生成器
# CATEGORY: 迭代器与生成器
# 2025.09.09
# 可以直接作用于for循环的数据类型：list,tuple,dict,set,str.
# 一类是generator，包括生成器和带yield的generator function
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以使用isinstance()判断是否是iterable对象：
from collections.abc import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))
print(isinstance(int,Iterable)) # int是类型对象，不是可迭代对象，但是100，90，以及float类型，如18.6等也是不可迭代对象
# dict是类型对象，不是实例对象，不是可迭代对象，只有实例对象如{}才是可迭代对象
print(isinstance(dict,Iterable))  # False，类型对象不是可迭代对象，只有实例对象如{}才是

# 生成器都是Iterator对象，但list，dict，str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
from collections.abc import Iterable,Iterator
print(isinstance(iter([]),Iterator))    # True
print(isinstance(iter('abc'),Iterator)) # True

# 以下 for 循环与下方的 while/try/except 结构是等价的，均用于遍历可迭代对象
for x in [1,2,3,4,5]:
    print(x)
# 完全等价于：
a = iter([1,2,3,4,5])
# 循环终止条件依赖于 StopIteration 异常，异常被捕获后跳出循环
while True:
    try:
        x = next(a)
        print(x)
    except StopIteration:
        break

# 查看内建名
import builtins
print("len in builtins?", hasattr(builtins, "len"))
print(sorted(name for name in dir(builtins) if not name.startswith("_"))[:20])

import math
def add(x,y,f):
    return f(x) + f(y)
print(add(4,9,math.sqrt))   # 5

输出 = print
输出(2+3)   # 5

# max,min = min,max
# print(max(1,2,3,4,5))   # 1
# print(min(1,2,3,4,5))   # 5

def max(*args):
    return min(*args)
print(max(1,2,3,4,5))   # 1

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


a = map(int,[1,2,3,4,5])
from functools import reduce
def fn(x,y):
    return x * 10 + y
print(reduce(fn,a) )





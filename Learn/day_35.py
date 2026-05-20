# day_35.py

# 核心复习内容：函数进阶 (续)

## 1. 生成器 (Generator)
    ### 1.1. 定义：使用 `yield` 关键字的函数
    ### 1.2. `yield` 与 `return` 的区别：暂停与恢复执行
    ### 1.3. 惰性计算与内存优化：按需生成数据
    ### 1.4. `next()` 函数与 `send()` 方法：控制生成器执行与数据交互
    ### 1.5. 生成器表达式：简洁创建生成器

## 2. 迭代器 (Iterator)
    ### 2.1. 定义：实现 `__iter__` 和 `__next__` 方法的对象
    ### 2.2. `iter()` 与 `next()` 内置函数：获取迭代器与获取下一个元素
    ### 2.3. 可迭代对象 (Iterable) 与迭代器 (Iterator) 的关系
    ### 2.4. 自定义迭代器示例

## 3. 匿名函数 (Lambda 表达式)
    ### 3.1. 定义与基本语法：单行函数，无函数名
    ### 3.2. 应用场景：配合高阶函数 (map, filter, sorted) 进行简洁操作
    ### 3.3. 局限性：仅支持单表达式

## 4. 偏函数 (Partial Function)
    ### 4.1. `functools.partial` 的使用：固定函数的部分参数
    ### 4.2. 应用场景：创建新函数，简化函数调用

## 5. 递归函数 (Recursive Function)
    ### 5.1. 定义与基本结构：函数调用自身
    ### 5.2. 终止条件：避免无限递归
    ### 5.3. 栈溢出问题：Python 默认递归深度限制
    ### 5.4. 尾递归优化 (概念性了解，Python 解释器未原生支持)

def simple_generator(): # 一个简单的生成器函数，用于演示yield的工作机制
    print('--- 生成器开始执行 ---')
    yield   # 暂停执行
    print('--- 生成器恢复执行，继续到第二个yield ---')
    yield
    print('--- 生成器恢复执行，继续到第三个yield ---')
    yield
    print('--- 生成器执行完毕 ---')

def large_data_generator(n):    # 一个生成大量数据的生成器，演示惰性计算
    i = 0
    while i < n:
        yield i # 暂停并返回当前值
        i += 1
    print('已迭代完')   # 此行在所有yield执行完毕后，且在StopIteration抛出前执行。还是会抛出StopIteration
a = simple_generator()
print(type(a))    # <class 'generator'>
print(next(a))
print(next(a))
print(next(a))
try:
    print(next(a)) 
except StopIteration:
    print('simple_generator已耗尽，捕获到 StopIteration 异常')
b = large_data_generator(4)

for i in b:
    print(i)
print(type(b))  # <class generator>
'''相当于：print(next(b))
print(next(b))
print(next(b))
print(next(b))'''

try:
    print(next(b))
except StopIteration:
    print('结束迭代（i已变成3，不能再加，再加不满足条件）')

c = large_data_generator(5)
print(max(c))
print(list(c))  # 无论谁在前，都会迭代完，后面这个没有了    # []

d = large_data_generator(1784214)
print(sum(d))

# 3. 匿名函数
add = lambda x, y: x + y
print(add(3, 5))

numbers = [1, 2, 3, 4, 5, 6]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

students = [('Jack', 26), ('Lone', 31), ('Zim', 28), ('Iam', 13)]
sorted_students = sorted(students, key=lambda x: x[1])  # 按年龄排序（sorted函数默认从小到大）
print(sorted_students)
sorted_students_name = sorted(students, key=lambda name: name[0])
print(sorted_students_name)

# 4. 偏函数
from functools import partial
def greet(name, greeting='Hello!'):
    return f'{name}, {greeting}'

greet_morning = partial(greet, greeting='Good Morning!')
print(greet_morning('Jack'))

# 5. 递归函数
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(4)) # 24

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
print(fibonacci(5)) # 0, 1, 1, 2, 3, 5
# fibonacci(4) => fib(2) + fib(3)
#                   ↓        ↓
#          fib(0) + fib(1)  fib(1) + fib(2)
#                                      ↓
#                                   fib(0) + fib(1)
#   3个fib(1)   # 3

def idn(n):
    if n == 0:
        return 1    # 假设第0项为1
    elif n == 1:
        return 2        # 假设第1项为2
    else:
        return idn(n - 1) * idn(n - 2)
print(idn(4))   # 1, 2, 2, 4, 8


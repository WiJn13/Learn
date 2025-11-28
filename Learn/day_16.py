# TITLE: nonlocal 计数器闭包与 lambda
# CATEGORY: 闭包与匿名函数
# 2025.09.24
# 使用闭包时，对外层变量赋值前，
# 需要先使用nonlocal声明该变量不是当前函数的局部变量。

def createCounter():
    x = 0
    def counter():
       nonlocal x 
       x = x + 1
       return x
    return counter  # return counter() 返回的是 counter 的执行结果（即一个整数），而不是函数本身。
    # 应改为 return counter，这样 createCounter() 返回的是闭包函数，可以多次调用并累加计数。
# 测试：
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA())
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
    
# 匿名函数 lambda
print(list(map(lambda x: x * x,[1,2,3,4,5,6,7,8,9])))
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
# 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x * x
print(f)    # <function <lambda> at 0x000001B4800A0FE0>
print(f(3)) # 9
# 同样，也可以把匿名函数作为返回值返回，比如：
def build(x,y):
    return lambda: x * x + y * y
print(build)    # <function build at 0x0000018E70E711C0>
print(build(2,3))   # <function build.<locals>.<lambda> at 0x00000229F09604A0>  
print(build(2,3)()) # 13
# 练习：用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd,range(1,20)))
print(L)

L = list(filter(lambda n: n % 2 == 1,range(1,20)))
print(L)

# 面向对象的object-oriented programming(OOP)
# 面向过程的process-oriented programming(POP)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():'% func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2025-9-24')
print(now())

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@ log('现在的时间：')
def now():
    print('2025-09-24')
now()
    # 打印，并附上日志，在前面的定义中该日志为函数名
print(now.__name__) # wrapper

import functools
def log(func):
    @functools.wraps(func)  # 应加在 wrapper 定义前，确保保留原函数元数据
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 在定义wrapper()的前面加上@functools.wraps(func)

import time, functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        """计时装饰器：用于测量并打印被装饰函数的执行时间（毫秒）。"""
        start_time = time.time()
        result = func(*args, **kw)  # 调用函数
        end_time = time.time()  # end_time在调用函数之后
        print('%s executed in %.3f ms' % (func.__name__, (end_time - start_time) * 1000))
        return result
    return wrapper

@log
def fast(x,y):
    time.sleep(0.0012)
    return x + y

@log
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')  # time.sleep(seconds)：来自标准库 time 模块。
                    # 功能是阻塞当前线程指定秒数（可以是小数）。在同步代码中常用来暂停执行、模拟延迟或轮询等待。
elif s != 7986:
    print('测试失败!')
print(f)
print(s)

print(int('12345', 8))# = print(int('12345',base = 8))
print(int('11', 2))  # 把2进制转换为10进制
# 定义一个int2()的函数，默认把base=2传进去：
def int2(x):
    return int(x, 2)
print(int2('11'))   # 3

# functools.partial就是帮助我们创建一个偏函数的，
# 不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int2 = functools.partial(int,base = 2)
print(int2('1000000'))  # 64
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
print(int2('12345',base = 8))   # 5349  # functools.partial()仅仅是把base参数重新设定默认值为2可在调用函数时传入其他值，而前者定义的方式不可传入其他值

my_max = functools.partial(max, 9)  # 注意：此偏函数会将参数 9 固定为第一个参数，调用时会与后续参数一起比较大小
print(my_max(2,3,4))   # 因为 max(9,2,3,4) 返回最大值 9，说明 functools.partial 固定了第一个参数如 my_max(2,3,4) 实际等价于 max(9,2,3,4)
# Python内置函数文档：https://docs.python.org/3/library/functions.html


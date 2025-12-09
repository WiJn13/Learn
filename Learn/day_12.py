# TITLE: 列表推导式与 os.listdir
# CATEGORY: 高级特性
# 2025.09.05
L = []
for x in range(1,11):
    L.append(x*x)   # list.append()是就地生成，返回值是none,所以不能赋值再打印
print(L)

L = [x * x for x in range(1,11)]
print(L)

L = [x * x for x in range(1,11) if x % 2 != 0]
print(L)    # [1, 9, 25, 49, 81]，筛选出仅奇数平方

L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)    # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
            # 注意理解顺序
L = []
for m in 'ABC':
    for n in 'XYZ': # 先小循环，再大循环，先遍历n
        L.append(m+n)
print(L)
L = [m + n for n in 'XYZ' for m in 'ABC']
print(L)    # ['AX','BX','CX','AY','BY','CY','AZ','BZ','CZ']
            # m + n，还是m在前，只是循环顺序改变

import os
names = os.listdir('.')
full_paths = [os.path.join('.', name) for name in names]
print(full_paths)

print(os.listdir())
print([d for d in os.listdir('.')])
print([d for d in os.listdir('..')])    # 父目录

L = ['Hello','Jane','World','OK']
print([s.lower() for s in L])

print([x * x if x % 2 == 0 else -x for x in range(1,11)])
print([x * x for x in range(1,11) if x % 2 == 0])   # 在一个列表生成式中，for前面的if ... else是表达式
                                                    #  而for后面的if是过滤条件，不能带else
L1 = ['Hello','World',18,'Apple',None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L2)
if L2 == ['hello','world','apple']:
    print('测试成功')
else:
    print('测试失败')

L1 = ['Hello','World',18,None]
L = []
def low(s):
    for x in s:
        if isinstance(x,str):
            L.append(x)
        else:
            continue
    return L2
L2 = [x.lower() for x in L2]
print(L2)

# note:
# 不创建完整的list，在循环的过程中不断推算出后续的元素，这种一边循环一边计算的机制称为生成器：generator

#创建generator的方法：
# 一、把一个列表生成式的[]改成()：
# 列表生成式会一次性生成所有元素并存储在内存中，而生成器表达式则返回一个生成器对象，每次通过迭代或next()时才计算下一个元素，具有惰性计算的特性，节省内存。
L = [x * x for x in range(10)]  # 列表生成式，立即生成所有元素
print(L)
g = (x * x for x in range(10))  # 生成器表达式，返回一个生成器对象
print(g)    # <generator object <genexpr> at 0x0000018775D3B100>
# 那要怎样打印出generator的每一个元素呢？
# 如果要一个个打印出来，可以通过next()函数获得generator的下一个返回值

print(next(g))  # 0
print(next(g))  # 1

for value in g:
    print(value)    # 可以用for循环，因为generator也是可迭代对象

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n+1
    return('Done')
print(fib(5))

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b     # 这就是定义generator的另一种方法。
                    # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数，调用一个generator函数将返回一个generator
        a, b = b, a+b
        n = n+1
g = fib(5)
try:
    while True:
        print(next(g))
except StopIteration:
    pass
# 或者直接用 for 循环更安全：
# for value in fib(5):
#     print(value)

# 杨辉三角练习：
def triangles():
    L = [1]
    yield L
    while True:
        L =[1] + [L[i] + L[i + 1] for i in range(len(L)-1)] + [1]
        yield L
print(next(triangles()))
print(next(triangles()))
a = triangles()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


def triangles(max):
    L = [1]
    yield L
    for _ in range(max):
        L = [1] + [L[i]+L[i + 1] for i in range(len(L) - 1)] + [1]
        yield L

a = triangles(6)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))






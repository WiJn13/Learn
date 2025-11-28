def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum
print(lazy_sum(1,3,5))
f1 = lazy_sum(1,3,5)
f2 = lazy_sum(1,3,5)
print(f1 == f2) #False
print(f1())

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

# lamba函数:关键字lambda表示匿名函数，冒号前面的x表示函数参数。

def a():
    print('你好')
f = a
# 函数对象有个 __name__属性（注意前后各两个下划线）
print(a.__name__) # a
print(f.__name__) # a



from collections.abc import Iterable
print(isinstance('abc',Iterable))   # str是否可迭代。True

from collections.abc import Iterable

# 自定义可迭代：实现 __iter__ 返回一个迭代器
class MySeq:
    def __init__(self, data): self.data = list(data)
    def __iter__(self):
        return iter(self.data)

s = MySeq([1,2,3])
print(isinstance(s, Iterable))  # True
it = iter(s)                     # 得到迭代器
# next(iterator[, default])：从迭代器取出下一个元素。
# 如果迭代器没元素且没提供 default，会抛 StopIteration；提供 default 则返回 default。
# Python 的迭代器实现了 next()，内置 next() 是调用它的便捷函数。
print(next(it))                  # 1
print(next(it))                  # 2

lst = [10, 20, 30]
it = iter(lst)
print(next(it))       # 10
print(next(it))       # 20
print(next(it))       # 30
print(next(it, None)) # None（迭代结束，返回 default 而不是抛异常）

print('')

n = 12543
for ch in str(n):
    print(ch)   # 1
                # 2
                # 5
                # 4
                # 3     得到的是字符
for d in map(int,str(n)):
    print(d)    # 1
                # 2
                # 5
                # 4
                # 3     得到的是数字
m = map(int,[1,2,3,4,5])
print(list(m))





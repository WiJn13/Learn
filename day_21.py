class Student(object):
    def __init__(self,name):
        self.name = name
print(Student('Michael'))   # <__main__.Student object at 0x000001D2CAAD6E40>

class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
print(Student('Walter'))    # Student object (name: Walter)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1 # 初始化两个计数器a，b
    def __iter__(self):
        return self#实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b    # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a   #返回下一个值

for n in Fib():
    print(n)

class Fib(object):
    def __getitem__(self,n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b # 右边表达式先全部计算（左到右），然后把结果一起赋给左边目标（同样左到右）。
                            # 因此 a, b = b, a + b 是“同时”更新
        return a

f = Fib()
print(f[0]) # 1
print(f[8]) # 34

class Fib(object):
    def __getitem__(self,n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[0:5])
print(f[:10])
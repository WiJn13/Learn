# TITLE: map/reduce 与数据转换、字符串规范化
# CATEGORY: 高阶函数与函数式编程
# 2025.09.15
from functools import reduce
DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))
print((str2int('12345')))

x = [3,4,5,2,6]
for x in x:
    print(x)

# 全部大写：s.upper()
# 全部小写：s.lower()
# 首字母大写（句首风格）：s.capitalize()
# 每个单词首字母大写：s.title()
# 大小写反转：s.swapcase()
# 用于不区分大小写比较（更严格）：s.casefold()
def normalize(name):
    name = name.strip()
    return name.lower().title()
# 测试：
L1 = ['adam','LIsa','barT','Bde oje sJi']
L2 = list(map(normalize,L1))
print(L2)   # ['Adam', 'Lisa', 'Bart', 'Bde Oje Sji']

from functools import reduce
def prod(L):
    def fn(x,y):
        return x * y
    return reduce(fn,L)
print(prod([3,5,7,9]))

from functools import reduce
DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2float(s):
    def char2num(s):
        return DIGITS[s]
    def fn(x,y):
        return x * 10 + y
    if '.' in s:
        int_s, frac_s = s.split('.')
    else:
        int_s = s
        frac_s = ''
    int_s = reduce(fn,map(char2num,int_s))
    frac_s = reduce(fn,map(char2num,frac_s),0) / 10 ** len(frac_s)
    return int_s + frac_s
print(f'{str2float('2.573'):.2f}')  # 2.57
print(str2float('2'))   # 2.0

print(10 // 3)
print(10 % 3)

def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd,[1,2,3,4,5,6,7,8])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['a','','b',None,'c','    '])))

def idn(a):
    return a
a = ['a',None,'3','  '] # filter可以过滤''，None，但是'    '不是空字符，所以需要s.strip()
print(list(filter(idn,a)))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n # 生成一个不含1的奇数序列
def _not_divisible(n):
    return lambda x: x % n > 0  # 判断序列中的数是不是当前x的倍数，不是则返回True,后续filter会被保留
def prime():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n # yield 才把这个n输出出来
        it = filter(_not_divisible,it)
# 2，3，5，7，9在n=3时被筛了，11，13，15同理，17，19，21同理
L = []
for n in prime():
    if n < 100:
        L.append(n)
    else:
        break
print(L)

def nat(n):
    n = 1
    while True:
        n = n + 1
        yield n

def is_palindrome(n):
    n1 = str(n)
    n2 = n1[::-1]
    return n1 == n2
# 测试:
output = filter(is_palindrome, range(1, 100))
print('1~100:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

print(sorted([2,5,-8,4,-97],key = abs)) # 先把序列abs，赋值给key，然后按照key给排序
print(sorted(['Bob','J','gack','k'],key = str.lower))
print(sorted(['Jack','i','Yhu','kop'],key = str.upper,reverse = True))  # reverse = True，降序

L = [('Bob', 75), ('Adam', 92), ('Kart', 66), ('Lisa', 88)]
def by_score(t):
    return t[1]
L2 = sorted(L,key = by_score,reverse = True)   # 不改变L的内容，只是按照一定的规则排
print(L2)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# TITLE: 递归、尾递归与汉诺塔
# CATEGORY: 递归与算法
# 2025.09.10

def fact(n):    # factorial: 阶乘
    res = 1
    if n > 1:
        while n > 1:
            res *= n
            n = n - 1
        return res
    elif n == 1:
        return 1
    else:
        return '请输入大于等于1的数'    # raise ValueError('请输入大于等于1的数')
print(fact(5))

def fact(x):
    if x == 1:
        return 1
    elif x > 1:
        res = x * fact(x-1) # 递归
        return res
    else:
        raise ValueError('请输入大于等于1的数') # 调用栈
print(fact(10))

def fact(n):
    res = 1
    for i in range(1 , n+1):
        res *= i
    return res
print(fact(0))  # 1  显式栈（循环 + list）

# note:
# 尾递归优化（TCO）：tail recursion optimization
# 但是Python不会做TCO

# 汉诺塔：
def move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
    elif n > 1:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(4,'A','B','C')

L = ['M','S','T','B','J']
print(L[:3])

def trim(s:str) -> str: # 表示s的期望类型是str，函数返回值期望是str
    if not s:
        return s
    start = 0
    end = len(s) - 1
    while start <= end and s[start] == ' ':
        start = start + 1
    while end >= start and s[end] == ' ':
        end = end - 1
    return s[start:end + 1]
print(trim('       min   '))

d = {'a':1,'b':2,'c':3}
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
for k,v in d.items():
    print(k,v)  # a 1
                # b 2
                # c 3

print('1','a','b')




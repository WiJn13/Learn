# TITLE: 二次方程、默认参数与可变参数
# CATEGORY: 函数进阶
# 2025.08.31
def quadratic(a,b,c):
    import math
    if a == 0:
        return -c/b
    if a != 0:
        D = b**2-4*a*c
        if D < 0:
            return '无实数根'
        else :
            D = math.sqrt(D)
            x1 = (-b+D)/(2*a)
            x2 = (-b-D)/(2*a)
            return x1,x2
print (quadratic(4,888,6))

print (pow(2,4))
def power(x,n):
    s = 1
    while n > 0 :
        n = n - 1
        s = s * x
    return s
print (power(2,3))
# 默认参数：
def power(x,n=2):
    s = 1
    while n > 0 :
        n = n-1
        s = s*x
    return s
print (power(3))    # 9
print (power(3,3))  # 27
power(3,5)

def enroll(name, gender):
    print ('name:',name)
    print ('gender:',gender)
enroll('Wang','Male')

def calc(*numbers):
    tot = 0
    for n in numbers:
        tot = tot + n*n # 可以写成tot += n*n
    return tot
print (calc(2,3,4)) # 2*2+3*3+4*4
# 用*解包后，输出可以直接输入数字
# 如果没有解包，输入的是tule或list，在输入函数calc()，括号里应当是list或tuple

d = {'name':'Wang','Gender':'male'}
print(d['name'])   #Wang
def d(age,job,**kwargs):
    if 'name' in kwargs:
        print ('age:',age,'job:',job,'name:',kwargs['name'])
m = {'name':333}
d(13,'wang',**m)   # name:333；函数内部自带打印
# print(d(**m))  # None, because function d does not return a value

def s(age,job,**kwargs):
    if 'name' in kwargs:
        return 'age:',age,'job:',job,kwargs.get('name')
    else:
        return '您未输入名字'
m = {'name':'Wang'}
print (s(13,'wang',**m))  # ('age:', 13, 'job:', 'wang', 'Wang') ；函数内部只return，不打印
print (*s(13,'sudent',**m)) # age: 13 job: sudent Wang

# 如果要限制关键字参数的名字，就可以用命名关键字参数
# 例如，只接收city和gender作为关键字参数。这种方式定义的函数如下：
def s(age,job,*,city,gender):
    t = (age,job,city,gender)
    print(t)
w = {'city':'wang','gender':'male'}
s(13,13,**w)    # (13, 13, 'wang', 'male')

def s(age,job,*,city,gender):
    print(age,job,city,gender)
w = {'city':'wang','gender':'male'}
s(13,13,**w)    # 13 13 wang male

def s(age,job,*,city,gender):
    return age,job,city,gender
w = {'city':'wang','gender':'male'}
print(s(13,13,**w))    #(13, 13, 'wang', 'male')

# def func(必选参数, 默认参数, *可变参数, 命名关键字参数, **关键字参数):
def s(age,job,*args,city,gender):   #*args及后面的都是关键字参数
    return age,job,args,city,gender
m = {'city':'chengdu','gender':'male'}
print(s(13,'student',**m))  # (13, 'student', (), 'chengdu', 'male')
print (*s(13,'student',**m))    # 13 student () chengdu male
# print (s(13,'student',city ='x'))   # TypeError: s() missing 1 required keyword-only argument: 'gender'
print (s(13,'studen','x',gender = 'male',city = 'chengdu')) # (13, 'studen', ('x',), 'chengdu', 'male')；可见，与顺序无关
print (s(13,'student','x','y',city = 'chengdu',gender = 'male'))    # (13, 'student', ('x', 'y'), 'chengdu', 'male')
print (s(13,25,*('x','y'),city = 'chengdu',gender = 'male'))    # (13, 25, ('x', 'y'), 'chengdu', 'male')

def mul(x,y):
    if y==0:
        raise ValueError('除数不能为0')
    res = 1
    for n in (x,y):
        res *= n
    return res  # return 要在循环外部，保证每一个都乘。要是在循环的缩进里，return res*x，就停止运行了。
print(mul(3,5))    # 15

def mul(*args):
    if args == 0:
        print ('0')
    elif not args:
        raise TypeError('请输入一个参数')
    res = 1
    for n in args:
        res *= n
    return res
print(mul(3,5,4))  # 60

# 修改版：
def mul(*args):
    if not args:
        raise TypeError('请至少输入一个参数')
    for n in args:
        if not isinstance(n,(int,float)):
            raise TypeError('请输入正确数字')
    if 0 in args:
        return 0
    res = 1
    for n in args:
        res *= n
    return res
print(mul(3,6,7))  #126

# note:编码规范
def long_functin_name(var_one,var_two,
                      var_three,var_four):  # 编码规范
    pass

def long_function_name(
        var_one,var_two,
        var_three,var_four):
    pass

a = {
    1,2,
    3,4,5,
    ...
}

person = {'name:',
     'job:',
     'site:',
     'phone number:',
     'age:',
     'gender:',
     }

# x = y + 1  ✔️
# x=y+1      ❌

# 禁止行尾空白

try:
    imcome = (today
           + night
           + yestoday
           + tomorrow)
except NameError:
    pass
# 操作符放在前面易读
    
import math
import os
import sys
# 📝 每个导入应该独占一行。导入总应该放在文件顶部，位于模块注释和文档字符串之后，模块全局变量和常量之前。
# 📦 一般按照最通用到最不通用的顺序：
# 标准库
# 第三方库导入
# 本地导入
# 禁止导入了模块却不使用它😀
# 📝 注释一般是放在代码之上
# 🚧 TODO(王)：

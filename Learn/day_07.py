# TITLE: 自定义函数与参数检查
# CATEGORY: 函数与条件判断
# 2025.08.30
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs # 变量a指向abs函数
print(a(-1)) # 1；所以也可以通过a调用abs函数

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

def my_abs(x):
    if x > 0 :
        return x
    if x < 0:
        return -x
    if x == 0 :
        return 0
# 如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器
# ⚠️ 用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）
# form...import...
s = int(input('输入一个数'))
if s > 0:
    print(f'你输的这个数是{s}')

if a == 10086 :
    pass   

# 数据类型检查：内置函数isinstance(obj,type)
print(isinstance(2,int))
print(isinstance('a',str))
print(isinstance(2.3,float))
class A : pass  # class：定义一个新的类型
class B(A) : pass
b = B()
print(isinstance(b,A)) # True；b的意思是任何B类型里的obj，因为B是A的子集，返回True
# discriminant：判别式。
# quadratic：二次函数

import math
def quadratic(a,b,c):
    if a == 0:
        if b == 0:
            return None
        return (-c/b,)
    D = b**2-4*a*c
    sqrt_D = math.sqrt(D)
    if D < 0 :
        return "判别式小于0, 无实数根"
    else:

        x1 = (-b+sqrt_D)/(2*a)
        x2 = (-b-sqrt_D)/(2*a)
    return x1,x2
print('quadratic(2,3,1)=',quadratic(2,3,1))
if quadratic(2,3,1) != (-0.5,-1.0):
    print('测试失败')
elif quadratic(1,3,-4) != (1.0,-4.0):
    print('测试失败')
else:
    print('测试成功')






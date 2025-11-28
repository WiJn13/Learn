# 2025.09.01

def func(a,b,c,*args,name,**kw):
    print(a, b, c, args, name, kw)
args = (1,2,3)
kw = {'d':85,'m':96}
# 🐛 func(*args,'jolin',**kw)    # 错误。“name”为关键字参数
func(*args,name = 'Jolin',**kw) # 1 2 3 () Jolin {'d': 85, 'm': 96}
args = (1,2,3,4)
func(*args,name = 'Jolin',**kw) # 1 2 3 (4,) Jolin {'d': 85, 'm': 96}
func(*args,name = 'J',*kw)  # 1 2 3 (4, 'd', 'm') J {}  因为kw没有以**传入
                            # 把kw解包后，得到的位置参数'd'和'm'被收进*args里了

a = input('计算一个或多个数相乘：')
def mul(*args):
    if not args:
        # print('请输入正确参数！')   # 🧪 🐛 当没有参数时，仅打印提示信息，但函数继续执行，最终返回 res=1，不符合乘法的语义，建议直接 return 或抛出异常。
        raise TypeError('请输入正确参数！')
    for x in args:
        if  not isinstance(x,(int,float)):
            # print('请输入正确的数字！') # 检查到非数字参数时仅打印提示，但未中断函数执行，可能导致后续乘法逻辑出错。建议在此处直接抛出异常或 return，确保只处理有效数字。
            raise ValueError('请输入正确的数字！')
    res = 1
    if 0 in args:
        return 0
    for n in args:
        res *= n
    return res


print(mul(a))
print('mul(5) =',mul(5))
print('mul(5,6) =',mul(5,6))
print('mul(5,6,7) =',mul(5,6,7))
print('mul(5,6,7,9) =',mul(5,6,7,9))
if mul(5) != 5:
    print('mul(5)测试失败！')
elif mul(5,6) != 30:
    print('mul(5,6)测试失败！')
elif mul(5,6,7) != 210:
    print('mul(5,6,7)测试失败！')
elif mul(5,6,7,9) != 1890:
    print('mul(5,6,7,9)测试失败！')
else:
    try:
        mul()
        print('mul()测试失败！')
    except TypeError:
        print('测试成功！')




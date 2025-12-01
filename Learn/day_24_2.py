# TITLE: day24新文件
# CATEGORY: 错误处理
# UnicodeError是ValueError的子类

'''
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    bar('0')
print('--- 调用栈版本 A: 不捕获 ---')
main()'''

import logging
logging.basicConfig(level=logging.INFO)
def foo2(s):
    return 10 / int(s)
def bar2(s):
    return foo2(s) * 2
def main2():
    bar2('0')
print('--- 调用栈版本 B: 用 logging.exception 捕获 ---')
try:
    main2()
except Exception as e:
    logging.exception(e)
print('到这一步程序还在运行')

# asctime函数：将时间转换成字符串

class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
foo('0')    # __main__.FooError: invalid value: 0
# 对内置类型（builtins 模块里的），Python 在显示时会把模块名省略，
# 只显示类名本身，让它更简洁：<class 'ValueError'>。内置类的模块叫 builtins，显示时被特地隐藏。
# 对你自己定义的类，则完整显示：<class '__main__.FooError'>。

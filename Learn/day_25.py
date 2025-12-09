# TITLE：调试，单元测试
# CATEGORY：错误、调试和测试
# 2025.12.09
from functools import reduce

def str2num(s):
    if '.' in s:
        return float(s)
    return int(s)

def calc(exp):  # exp 是一个字符串表达式，比如 '100 + 200 + 345'
    ss = exp.split('+') # 按+，结果是一个列表
    ns = map(str2num, ss)   # 将ss中的字符串依次丢进str2num中，得到一个“可迭代对象”（可以当成一串数字）
    return reduce(lambda acc, x: acc + x, ns)   # acc：累计值

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' # assert 条件, '出错时的提示信息'
    return 10 / n
def main():
    foo('0')



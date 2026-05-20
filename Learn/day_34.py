# Day 34: 装饰器与闭包逻辑深度复习
# 今日复习大纲：
# 1. 装饰器三层嵌套逻辑：参数层 -> 装饰层 -> 包装层。
# 2. 内存绑定分析：闭包如何捕获外部作用域变量（delay）。
# 3. 元数据保护：functools.wraps(func) 的必要性。
# 4. 实战演练：尝试编写一个带权限验证或日志记录的装饰器。

import functools
def logger(level='INFO'):
    def decorator(func):
        @ functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'[{level}]正在调用函数：{func.__name__}')
            print(f'传入参数：args = {args}, kwargs = {kwargs}')
            result = func(*args, **kwargs)
            print(f'[{level}]执行结果：{result}')
            return result
        return wrapper
    return decorator

@logger(level='DEBUG')
def add_numbers(a, b):
    return a + b

@logger(level='WARNING')
def divide_numbers(a, b):
    if b == 0:
        return 'Error: Division by zero'
    return a / b

if __name__ == '__main__':
    print('--- 调用 add_numbers ---')
    add_numbers(10, 20)
    print('\n--- 调用divide_numbers正常 ---')
    divide_numbers(10, 2)
    print('\n--- 调用divide_numbers异常 ---')
    divide_numbers(10, 0)

print(add_numbers.__name__)
print(divide_numbers.__doc__)

import time
print(time.time())
print(time.localtime()) 
print(time.strftime('%Y-%m-%d %H:%M, %a，今天是今年的第%j天，一年中的第%W周',time.localtime()))

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'[LOG]调用函数：{func.__name__}with args = {args}, kwargs = {kwargs}')
        result = func(*args, **kwargs)
        print(f'[LOG]函数{func.__name__}返回的结果：{result}')
        return result
    return wrapper

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time() * 1000
        result = func(*args, **kwargs)
        end_time = time.time() * 1000
        total_time = end_time - start_time
        print(f'此次函数调用耗时{total_time:.3f}毫秒')
        return result
    return wrapper

@log_call
@timer
def complex_calculation(a, b):  # 执行一个复杂的计算
    time.sleep(0.1) # 模拟计算耗时
    return a * b + 10

if __name__ == '__main__':
    print('\n---装饰器叠加示例---')
    complex_calculation(10, 20)
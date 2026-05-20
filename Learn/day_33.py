# TITLE: 装饰器实战
# CATEGORY: 函数进阶
# Day 33: 装饰器实战练习

import time
from functools import wraps

# 任务：编写一个名为 timer 的装饰器
def timer(delay):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            time.sleep(delay) # 引入纯粹的延迟，数据完全由外部参数接管
            result = func(*args, **kwargs) # 执行原始函数
            end_time = time.time()
            total_time = (end_time - start_time) * 1000
            print(f'执行函数耗时：{total_time:.4f} 毫秒')
            return result
        return wrapper
    return decorator

BASE_DELAY = 0.1  # 全局基础延迟配置

@timer(delay=BASE_DELAY)
def fast_add(a, b):
    return a + b

@timer(delay=BASE_DELAY + 0.5)
def slow_task():
    print('慢任务完成')

print(fast_add(10, 20))
slow_task()

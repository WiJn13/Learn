# TITLE: filter, zip 与字典推导式
# CATEGORY: 函数进阶
# day_32.py

# 待练习知识点：
# 1. filter() 的布尔过滤逻辑
# 2. zip() 的并行迭代与木桶效应
# 3. 字典推导式的构建
# 4. 变量解包 (Unpacking) 与 * 运算符

# 1. 
my_list = [10, 'error', None, 21, (23, 13)]
a = lambda x: isinstance(x, int)
b = filter(a, my_list)
print(list(b))
c = filter(None, [0, 1, False, True, '', 'A'])
print(list(c))

# 2.
d = list(zip([1, 2], [3, 4, 5]))
print(d)    # [(1, 3), (2, 4)]
zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, chars = zip(*zipped)
print(nums)
print(chars)

# 3.
items = ['phone', 'laptop', 'watch']
prices = [5000, 6000, 2000]

inventory = {name: price for name, price in zip(items, prices) if price > 3000}   # 清单 
# 生成一个字典，格式为{name: peice}，并且保留价格大于3000的物品
print(inventory)

# 4.解包
# (1)基础解包
a, b, c = [1, 2, 3]
print(b)    # 2
# (2)扩展解包
a, *m, b = [1, 2, 3, 4 ,5]
print(m)    # [2, 3, 4] (打印完整的列表对象)
print(*m)   # 2 3 4 (解包为独立的多个参数传给 print。等价于 print(2, 3, 4))
print(b)    # 5

# 💡 补充：print() 的底层默认定义与参数
# 完整定义：print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#
# 1. *objects : 接收任意多个独立参数（这里结合 *m 解包传递非常合适）
# 2. sep=' '  : 分隔符 (separator)。默认打印多个参数时用空格隔开。
#    修改示例：print(*m, sep='-')  # 输出：2-3-4
#             print(*m, sep='')   # 输出：234 (利用无缝拼接可替代 .join 的部分操作)
# 3. end='\n' : 结束符。默认打印完所有的对象后追加一个换行符。
#    修改示例：print('A', end=''); print('B')  # 输出：AB (下一次打印会紧跟在同行末尾)
# 4. file     : 输出目标。默认是 sys.stdout (控制台屏幕)，也可以改成文件对象直接写入文件。
# 5. flush    : 是否强制立刻刷新缓冲区。默认 False。




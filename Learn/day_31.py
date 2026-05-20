# TITLE: 列表推导式
# CATEGORY: 高级特性
# day_31.py

# [对x的操作 for x in 可迭代对象 if 条件（可选）]
original = [1, 2, 3]
new_list = [x*x for x in original]
print(new_list)

# --- 补充：为什么有些方法打印出来是 None？ ---
my_list = ['a', 'b', 'c']

# 1. "产生新结果"的方法（会返回数据，但不改变原数据）：
# 列表本身没有 .upper() 方法，我们用刚学的“列表推导式”来生成大写结果
upper_list = [x.upper() for x in my_list]
print(upper_list)  # ['A', 'B', 'C']
print(my_list)       # ['a', 'b', 'c']

# 2. "就地修改"的方法（只干活，不返回数据，默认返回 None）：
result = my_list.append('d')
print(result)          # None
print(my_list)   # ['a', 'b', 'c', 'd']

# 但凡是直接修改了列表自身的操作，返回值统统是 None，千万不要用 print 直接包住它们
# 也不要用 = 把它们赋值给别的变量。

print('\n--- 列表操作的【三大门派】总结 ---')

# 【第一派】：原地修改，返回 None（原列表变了，没有返回值）
list_1 = [3, 1, 2]
res_1 = list_1.sort()
print(list_1) 
print(res_1)
# 包含: .append(), .extend(), .insert(), .remove(), .clear(), .sort(), .reverse()

# 【第二派】：原封不动，产生新结果（原列表不变，返回新列表）
list_2 = [3, 1, 2]
res_2 = sorted(list_2)
print(list_2)
print(res_2)
# 包含: sorted(), reversed(), .copy() 方法
#       切片 [:] , 拼接 list_a + list_b, 乘法 list_a * 3, 列表推导式
#       以及统计/高阶函数 len(), max(), sum(), map(), filter() 等

# 【第三派】：叛逆分子，既原地修改，又返回数据
# 唯一代表：.pop()
list_3 = ['苹果', '香蕉', '橘子']
res_3 = list_3.pop(1)  # 把索引为1的'香蕉'拿走
print(list_3)
print(res_3)

# ⚠️ 经典对比记忆：
# .sort() 是列表的方法，原地排序，返回 None
# sorted() 是内置函数，不改原列表，返回排好序的新列表
# .reverse() 是列表方法，原地翻转，返回 None
# reversed() 是内置函数，不改原列表，返回翻转后的迭代器(可用 list() 转为列表)

print('\n--- 补充：为什么列表有 append 却没有 upper？ ---')
# 因为在 Python 中，不同的数据类型拥有自己的“专属方法”。
# 1. 列表（容器）：专属动作是管理元素，比如装东西、拿东西（append, pop, sort）
# 2. 字符串（文本）：专属动作是文字处理（upper, lower, replace）
# 如果想对列表里的每一个文本进行处理，必须把文本“拿出来”单独处理（比如用列表推导式），
# 而不能直接对整个列表本身调用文本处理的方法。

new_list2 = [x*x for x in range(1,11) if x % 2 == 0]
print(new_list2)

# 除法复习
# 1. 经典除法
print(10 / 3)   # 3.3333333333333335
# 2. 地板除/整除（向下取整）
print(10 // 3)  # 3
print(-2 // 3)  # -1
print(11.00 // 3)   # 3.0 (注意：Python默认打印浮点整数只保留一位.0。若要保留两位需用 f"{...:.2f}")

# 3. 取模/取余数 (%)
print(10 % 3)   # 1
print(10.5 % 3) # 1.5
# 浮点数取余原理：余数 = 被除数 - (被除数 // 除数) * 除数
# 相当于：有 10.5 米的布，每次必须剪 3 米，最多能剪 3 段（用掉 9 米），最后剩下 1.5 米。

print(10.2 // -2)   # -6.0 
# 解释：10.2 / -2 = -5.1，向左取整是 -6.0。
# 💡 为什么这里只显示一位小数？因为地板除的结果在数学上永远是个“完整的整数”，
# -6.0 在计算机二进制里能被 100% 精确存储，Python 默认只加个 .0 表示它是浮点型即可。

print(10.2 % -2)    # -1.8000000000000007 (这是浮点数底层二进制存储的精度问题，数学上等于-1.8)
# 解释：套用公式 余数 = 10.2 - (-6.0 * -2) = 10.2 - 12.0 = -1.8。
# 💡 为什么这里显示这么多位？因为 10.2 里的 0.2 在二进制里无法精确存储（是一个无限循环小数），
# 经过减法运算后，这个微小的精度误差就被完全暴露出来了。

print(round(-10.2 % 2) )   # 2
# 💡 补充：如果要消除浮点数精度的小尾巴，可以使用 round() 函数保留一位小数：
print(round(10.2 % -2, 1))  # -1.8

print('\n--- round() 函数详解 ---')
# round(number, ndigits=None) -> 对数值进行近似舍入

# 1. 基础用法：保留指定小数位数
print(round(3.14159, 2)) # 3.14

# 2. 默认行为：不指定位数，则舍入到最近的整数
print(round(3.8)) # 4
print(round(3.1)) # 3

# 3. ⚠️ 最大陷阱：银行家舍入法（四舍六入，五成双）
# 当数字恰好在中间时（如 2.5），会向最近的【偶数】舍入
print(round(2.5)) # 2 (向偶数2舍入)
print(round(3.5)) # 4 (向偶数4舍入)

# 4. 隐藏技能：位数可以是负数，用于对整数部分进行舍入
print(round(12345, -1)) # 舍入到十位 -> 12340
print(round(12345, -2)) # 舍入到百位 -> 12300


# lambda函数：
square = lambda x: x*x
print(square(3))  # 9
# 💡 解释：lambda 表达式自带隐式的 return。
# lambda x: x*x 完全等价于 def square(x): return x*x
# 因为它实打实地计算并返回了 9 这个新结果，所以可以直接用 print 包裹打印。

users = [('Eben', 22), ('WiJn', 21),('Mac', 30)]

print('\n--- .sort() 底层原理与 key 参数深度解析 ---')
# 【底层原理】：瞎子裁判与代理人模型
# 1. sort() 本身是个“瞎子裁判”，遇到元组数据，默认只能挨个比对第一项（名字字母）。
# 2. key=... 相当于给每个元素派发了一个“特征提取器”。
# 3. 当传入 key=lambda x: x[1] 时，底层发生了这三步：
#    - [提取]: 裁判把 ('WiJn', 21) 丢进 lambda，提取出 21 作为“代理人”。
#    - [比拼]: 裁判完全无视原元组，只拿提取出的 [22, 21, 30] 互相比较大小。
#    - [归位]: 发现 21 最小，于是把 21 对应的原身 ('WiJn', 21) 排在最前面。
# 【记忆口诀】：
# key是特征提取器，抽出特征比高低；特征只做垫脚石，排完原身定座席。


print(users)

print(users.sort(key=lambda x: x[1]))  # 打印出 None

print(users)  # 打印出 [('WiJn', 21), ('Eben', 22), ('Mac', 30)]

# --- 补充答疑：lambda x: x[1] 到底等价于什么 def？ ---
# ⚠️ 误区：lambda 里面包含了 for 循环。
# ✅ 真相：lambda 绝不包含循环！循环是 sort() 自己在底层做的。
# lambda x: x[1] 完全等价于下面这个只能处理【单个】元素的普通函数：
def get_age(x):
    return x[1]

# ⚠️ 注意：直接调用 get_age(users) 和 sort(key=get_age) 的行为完全不同！
# 下面这行代码是把【整个列表】传给 get_age，所以 x[1] 取的是列表的第2个元素。
print(get_age(users)) # ('Eben', 22)

# 💡 为什么是 ('Eben', 22)？
# 因为在执行到这里时，上面的 users.sort() 已经把列表【就地修改】了！
# 排序后的列表变成了: [('WiJn', 21), ('Eben', 22), ('Mac', 30)]
# 所以此时列表的第2个元素（索引为1）正是 ('Eben', 22)。

# sort() 底层的真实工作流是这样的：
# 1. 先按顺序循环：for item in users:
# 2. 提取特征并缓存：挨个调用 get_age(item) 拿到年龄，并记在小本本上。
# 3. 集中比拼排序：等所有元素的年龄都提取完毕后，再统一对这些“年龄”进行集中排序。
# 4. 排序完成归位：按照排好的年龄顺序，把原元组放回列表。

# 所以，下面这行代码和上面用 lambda 的写法，效果 100% 一模一样：
# users.sort(key=get_age)

my_add = lambda a, b: a + b  #lambda可以同时接受多个参数
def add1(a, b):
    return a + b
print(my_add(2, 3))
print(add1(2, 3))
print((lambda a, b: a + b)(11, 12)) # 23 # 匿名函数即定义即执行

print('\n--- map() 函数深度解析 ---')
# 语法：map(func: Callable, iterable1: Iterable, iterable2: Iterable, ...)
# 原理模型：“工厂流水线”
# func: 代表可调用对象（如函数、lambda等），相当于流水线上的“加工机器”。
# iterable: 代表可迭代对象（如 list, tuple 等），相当于存放原料的“传送带”。
# map 会自动从 iterable 中提取数据，丢进 func 中处理，产出新数据。

# 1. 单传送带作业：把数字全转成字符串
nums = [1, 2, 3]
print(list(map(str, nums))) # ['1', '2', '3']

# 2. 多传送带并行（你的代码）：
# 因为 lambda a, b 需要两个参数，所以后面必须跟两条传送带 list1 和 list2
list1 = [1, 2, 4]
list2 = [2, 4, 7]
# 每次分别从 list1 和 list2 取出一个元素交给 a 和 b
combined = list(map(lambda a, b: a + b, list1, list2))
print(combined) # [3, 6, 11]

# ⚠️ 进阶细节：
# 1. 为什么外面要套一个 lst()？因为 map 是“惰性”的，直接打印 map(...) 只会得到一个机器对象。

#    套上 list() 是为了强迫流水线立刻启动，并把产出的结果装进一个列表盒子里。
# 2. 木桶效应：如果多条传送带长度不一样，只要最短的那条空了，机器就会停止。
print(list(map(lambda a, b: a + b, [1, 2], [10, 20, 30, 40]))) # [11, 22]




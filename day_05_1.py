# 2024.08.27

my_list=[1,2,3,4]
my_list[3]=5   # 修改列表中索引为3的元素
print (my_list)
print (len(my_list))    # 4
# print (my_list[4])  # IndexError: list index out of range;index:索引
print (my_list.append(6))
# print (my_list.append(6)) 会输出 None，因为 my_list.append() 方法返回值为 None，而不是修改后的列表。
# 应先调用 my_list.append(6)，然后再打印 my_list：
my_list.append(6)
print (my_list)
my_list.insert(3,7)
print (my_list)
my_list.remove(2)  # 删除列表中值为2的元素
print (my_list)
my_list.pop()  # 删除并返回列表的最后一个元素
print (my_list)
my_list.pop(2)  # 删除并返回列表中索引为2的元素；pop:弹出，取出
print (my_list)
my_list.clear()  # 清空列表
print (my_list)
#print(my_list[3]=5)    #  错误。print 函数不能在参数中进行赋值操作。应先赋值，再打印。
L = ['Apple', 123, True]    # 创建一个包含不同类型元素的列表
print (L)
s = ['python', 'java', ['asp', 'php'], 'scheme']    # list里也可以是另一个list
print (len(s))  # 4

'''list = [1, 2, 3, 4]
print(list[4])'''
#运行结果：
#Traceback (most recent call last):      # “最近的一次调用在最后”，即最底下的错误是最直接的原因
#  File "c:\Users\j5479\OneDrive\学习\Python\Day 5.py", line 32, in <module>     # “in <module>” 表示错误发生在主模块（不是函数或类内部）。
#    print(list[4])
#          ~~~~^^^
#IndexError: list index out of range     

u=['good','study']
p=[1,2,3,u,5]
# 要拿到study可以：
print (p[3][1])  # study

# 快速交换行:alt+↑/↓
# 快速复制粘贴：alt+shift+↑/↓

# tuple:元组，不可变的列表，用()表示
t = (1, 2, 3)
print (t)
# tuple，str，int，float，bool不可变
d = {'a': [1, 2, 3], 'b': 5}  # 值可以是列表（可变），键必须是不可变类型    # dict:字典
s = {1, 'abc', (2, 3)}        # 元素可以是数字、字符串、元组    # set:集合；集合的元素是不可变元素
# s = {[1, 2], 3}  # 错误，列表和字典不可作为集合元素

t=(2)
print (t)    # 2,不是元组
t=(2,)   # 要定义一个元素的元组，必须加逗号
print (t)    # (2,)

L = [
    ['Apple', 'Google', 'Microsoft'],
    [' Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]
# 遍历二维列表并打印所有元素
for sublist in L:
    for item in sublist:
        # 打印当前子列表中的每个元素
        print (item)

# 解释 for ... in ... 的工作机制
# - for：表示开始一个循环，每次循环会把可迭代对象里的下一个元素取出来。
# - in：表示从哪个对象里取元素（例如列表、元组、字符串等）。
# - 例子：for sublist in L:
#     解释：把 L（一个列表）当成“装子列表的箱子”，每次从箱子里取出一个子列表，赋给变量 sublist，然后进入循环体处理这个子列表。
# - 嵌套循环例子说明：
#     for sublist in L:           # 外层循环：每次给 sublist 一个子列表
#         for item in sublist:   # 内层循环：逐个拿出子列表里的元素并赋给 item
#             print(item)        # 对每个 item 做相同操作（这里是打印）
# 接下来是把嵌套列表“拉平”（flatten）的两种常见做法。

# === 一：一层展开（只合并外层的子序列） ===
# from itertools import chain   #iterates:迭代。
# 解释：从 Python 标准库的 itertools 模块导入 chain 工具。
# itertools：一组处理“迭代（逐个产出元素）”的工具函数集合；chain 用来把多个序列连在一起看成一个序列。
from itertools import chain
# flat_one = list(chain.from_iterable(L))
# 逐部分解释：
# - chain.from_iterable(L)：把 L 看作『由多个子序列组成的可迭代对象』，依次取出这些子序列并把它们拼接成一个长的迭代器（不一次性把所有元素放到内存里）。
# - list(...)：把上一步返回的迭代器转换成真正的 Python 列表（这样你可以像平常那样访问或打印）。
# - flat_one：变量名，可以理解为“展平后的一层列表”。
flat_one = list(chain.from_iterable(L))
# 打印说明性文字和结果，方便你在运行脚本时立刻看到含义
print ('one-level flattened (只合并一层):', flat_one)

# === 二：任意深度的递归展开（把所有层都展开） ===
# 下面用一个函数（生成器）一步步把任意深度的嵌套列表或元组展开成单层序列。
# 我们把字符串（str）和字节序列（bytes）当做原子元素，不会把它们拆开成字符或字节。

def flatten_recursive(seq):
    """
    递归(recursive)生成器：
    -  seq: 一个列表或元组，可能里面还包含列表/元组（任意深度）。   # seq: sequence, 序列
    - 返回：一个生成器对象（不是列表），你可以用 list(...) 把它转换成列表。
    关键点：
    - 使用 yield 把值“产出”，函数会暂停，下次继续从暂停处执行（这就是生成器的好处，节省内存）。
    - 我们只对 list 和 tuple 递归展开，其他类型（特别是 str/bytes) 不再展开，视为单个元素。
    """
    # for item in seq: 逐个取出 seq 中的元素
    for item in seq:
        # isinstance(item, (list, tuple))：判断当前元素是不是列表或元组
        if isinstance(item, (list, tuple)):
            # 如果是列表或元组，就递归调用自己，继续展开里面的元素
            for sub in flatten_recursive(item):
                # 用 yield 把递归得到的每一个元素逐个产出给调用者
                yield sub
        else:
            # 如果不是列表/元组（例如数字、字节、字符串、布尔等），直接把它作为一个元素产出
            # 注意：在这里我们把字符串看作一个整体，不会拆成单个字符
            yield item

# 示例：混合嵌套结构，包含列表、元组、字符串、字节等
nested = [1, [2, 3, [4, 5]], (6, [7, 8]), 'abc', [b'xy', [9]]]
# 打印原始结构
print ('nested (原始嵌套结构):', nested)
# list(flatten_recursive(nested))：把生成器的所有产出收集成列表并打印
print ('flatten_recursive result (递归展平后的结果):', list(flatten_recursive(nested)))

# 小白提示和常见疑问：
# - 为什么用生成器？因为生成器每次只产生一个元素，不会一次性把所有数据丢到内存，处理大数据时更省内存。
# - yield vs return：return 会结束函数并返回一个值；yield 会把一个值“交出去”但保留函数状态，下一次继续执行。
# - isinstance(item, (list, tuple))：这里用元组 (list, tuple) 表示要检测多种类型，括号里可以放多个类型。
# - 如果你确实想把字符串也拆开，可以把判断里的条件改掉，但大多数场景把字符串当作一个独立元素更安全。
# - list(chain.from_iterable(L)) 是最简单的“一层展平”写法；如果只要一层，尽量用这个，清晰且高效。

#集合set相关：
s = {1,2,3,4}
s.add(5)
s.add(6)
s.add(7)    #add()只能分别添加一个元素
print(s)
s.update('5','6','7')   #int不能直接添加
s.update([8,9,10])
p = {'a','b','c','d'}
print (s.union(p))   #并集, s|p
print (s & p)   #交集, s&p, s.intersection(p)
print (s - p)   #差集, s.difference(p)
print (s^p)   #对称差集, s.symmetric_difference(p)
print (s.issubset(p))   #判断是否是子集
print (p.issuperset(s)) #判断是否是超集
'''注意: 集合无序，且元素不能通过索引访问'''

age = input ('你的年龄是？')
if age.isdigit():
    #age=int(age)  # 可以把字符串转化成整数，后面的数字不用打引号
    if age>='18':
        print ('你是一个成年人')
    elif age>='16':
        print ('你是一个青年人')
    else:
        print ('你是一个小朋友')
else:
    print ('请输入有效整数')

print ('**good'.lstrip('*')) #leftstrip()：丢掉左边的
h='*#,#*good$%#'
print (h.lstrip('#*'))


year = input ('你的出生年份：')
year = int(year)
age = 2025 - year
if year >2025 :
    print('?')
elif year > 2000 :
    print('你是一个00后的人')
elif year < 1825 :
    print('你还活着啊？')
else :
    print('你是一个00前的人')

if year < 2025:
    age = 2025 - year
    print('而且，我还知道你今年{age}岁了！'.format(age=age))
else:
    print('请回娘胎')

print ('计算你的BMI: ')
h = input ('你的身高(m/cm): ')
w = input ('你的体重(kg): ')
h = float(h)
w = float(w)
if h > 3 :
    bmi = w/(h/100)**2
else :
    bmi= w/(h)**2
print (f'你的BMI为: {bmi:.2f}')
if bmi < 18.5 :
    print ('过轻')
elif bmi < 25 :
    print ('正常')
elif bmi < 28:
    print ('过重')
else :
    print ('严重肥胖')

choi= input('输入你的选择：')
match choi:
    case 'A':
        print ('A')
    case 'B':
        print ('B')
    case _ :
        print ('Others')

sty=input ('选择你更喜欢的风格：')
match sty:
    case  '蓝色'|'白色'|'棕色' :
        print ('嘿嘿我们一样')
    case '黑色' :
        print ('很沉稳')
    case _ :
        print ('你喜欢什么都好!')

# TODO:
# NOTE：
# BUG: 
# TEST:
# DONE:
# note:
# NOTE

















































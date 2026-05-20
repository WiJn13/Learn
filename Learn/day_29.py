# TITLE: 函数参数与作用域
# CATEGORY: 函数进阶
def greet(name):

    # name：[形式参数/形参]：变量名，相当于一个临时的“空位占位符/盒子”，不用加引号。
    print(f'Hello, {name}') 

greet('WiJn') # 'WiJn'：[实际参数/实参]：具体的数据。文本数据必须加引号表示它是字符串。
print(abs(-3))  # 3

WiJn = 'Hello World' # 提前定义一个变量（盒子），里面装上文本
# 此时 WiJn 是变量名，不用加引号。它会把装在里面的 'Hello World' 传给 greet 函数
greet(WiJn) # 打印结果：Hello, Hello World

print('\n--- 补充：为什么 upper() 括号里是空的？ ---')
# 1. 方法（Method）：自带数据的函数
name = 'wijn'
print(name.upper()) # upper() 是字符串对象自带的“方法”。
# 这里的点（.）非常神奇，它会自动把点前面的 name 当作隐藏参数（self）传进去。
# 所以虽然括号里没写东西，但 upper() 其实知道自己要处理的是 'wijn'。

# 2. 真正的“无参函数”：不需要外界提供数据就能执行固定任务
def print_line():
    print('-------------------')    # 比如专门用来打印分隔符

print_line() # 调用时括号也是空的

def new_add(a, b):
    return a + b
name = (2, 3)

# print(name.new_add()) # ❌ 会报错：AttributeError。因为 new_add 不是元组对象自带的方法。

# 正确方式一：老老实实把元组里的元素按索引取出来，作为参数传进去
print(new_add(name[0], name[1])) # 5

# 正确方式二：利用神奇的 * 号进行“解包”（你在 day_08 学过的技巧），直接把元组拆开塞进函数
print(new_add(*name)) # 5

print('\n--- 补充：如果我非要用 .new_add() 呢？ ---')
# 官方的 tuple 是锁死的，不能动态绑定方法。
# 但我们可以自己造一个“升级版”的元组，继承官方的 tuple！
class MyTuple(tuple):
    def new_add(self):
        # 这里的 self 就会自动接收点（.）前面的对象本身（也就是那个元组）
        return self[0] + self[1]

my_name = MyTuple((2, 3)) # 用我们的“升级版”类来创建元组
print(my_name.new_add())  # 5 ！成功实现了 .new_add() 的调用方式！

count = 2
def jone(num):
    # 为什么没报错？
    # 因为这里只是在函数内部“创造”了一个全新的同名【局部变量】。
    # 右边 1 + num 计算出 4 后，装进了局部的 count 盒子里，并没有触碰外部的全局变量。
    count = 1 + num
    print(f'-> 函数内部的局部 count = {count}')
    return num

print(f'调用 jone(3) 的返回值: {jone(3)}')
print(f'-> 函数外部的全局 count 依然是: {count}') # 依然是 2，证明外部全局变量没被改变

# ⚠️ 对比：如果写成 count = count + 1 就会报错（UnboundLocalError）
# 因为在赋值前，它试图读取局部 count 的值，但此时局部 count 还是空的。

count = 2
def indrement():
    global count
    count += 1
    return count
print(indrement())  #3


x = 10
def change():
    x = 20

print(change())
print(x)

class Robot:
    def __init__(self, name):
        self.name = name

my_robot = Robot('D340')
print(my_robot.name)
my_robot.__init__('D223')
print(my_robot.name)    # D223

class Robot:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f'Hello, I\'m {self.name}')
my_robot = Robot('J243')
my_robot.say_hello()
my_robot = Robot('0233')    # 新建机器人并把my_robot的标签给0233
# my_robot.name = '0233'    # 修改原机器人J243的名字为0233，其他属性不变
my_robot.say_hello()
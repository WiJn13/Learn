# 继承
# 创建一个Robot
class Robot:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f"Hello, I'm {self.name}")

# 继承：创建一个会飞的机器人，复用Robot的初始化逻辑
class FlyRobot(Robot):  # 声明继承自Robot
    def fly(self):
        print(f'{self.name} is now taking off!')

# 实例化
eva = FlyRobot('SkyEye')
eva.fly()
eva.say_hello()
print(eva.name)

# 内存标签实验
old_id = id(eva)
eva = FlyRobot('NewEye')    # 标签重指向，原'SkyEye'已被摧毁
new_id = id(eva)
print(f'旧地址：{old_id} | 新地址：{new_id}')

r1 = Robot('Mac')
r2 = r1 # 相当于贴了两个标签，两个标签都指向'Mac'
r2.name = 'Win'
print(r1.name)  

# 多态与模块化
class Robot:
    def __init__(self, name):
        self.name = name
    def work(self): # 父类定义一个通用概念
        raise NotImplementedError(f'子类必须实现work方法')

class CleaningRobot(Robot):
    def work(self):
        print(f'{self.name} 正在工作')

class ServiceRobot(Robot):
    def work(self):
        print(f'{self.name} 正在制作咖啡')

robots = [CleaningRobot('Ace'), ServiceRobot('Joe')]
for r in robots:
    r.work()


from abc import ABC, abstractmethod

class Robot(ABC):  # 1. 继承 ABC，让 Robot 变成一个正规的“抽象类”
    def __init__(self, name):
        self.name = name
        
    @abstractmethod    # 2. 加上这个装饰器，说明这是一个“抽象方法”，子类必须实现
    def work(self):
        pass           # 这里直接写 pass 就可以了，不需要 raise 报错

class CookRobot(Robot):
    def work(self):
        print('这次定义了work')
    pass  # 依然忘记写 work 方法

# 此时，代码不需要等到调用 work()，仅仅是试图创造这个机器人就会报错：
chef = CookRobot('Chef') 
# 报错：TypeError: Can't instantiate abstract class CookRobot with abstract method work

with open('text.txt', 'w') as f:    # open('文件名', '模式')    # 注意打引号
                                    # w（write）：覆盖写入。文件不存在则自动创建；文件若存在则清空原内容再写。
                                    # a（append）：追加写入。文件不存在则自动创建，文件若存在则在末尾续写。
                                    # r（read）：只读模式。文件不存在则报错（FileNotFoundError）
    f.write('Hello macOS')
# python中处理文件时永远推荐用with语法，既简洁又安全，优雅。

# 1. 使用相对路径：读取上一级目录（Python文件夹）中的 text.txt
'''with open('../text.txt', 'r') as f:
    print('相对路径读取的内容：', f.read())'''

# 2. 使用绝对路径：向该文件追加写入一行新内容
with open('/Users/wij13/Library/CloudStorage/OneDrive-个人/学习/Python/text.txt', 'a') as f:
    f.write('\nHello from absolute path!')

with open('text.txt', 'a') as f:
    f.write('\n新增一行内容')


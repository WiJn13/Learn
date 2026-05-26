# TITLE: 面向对象复习：继承初始化与参数传递
# CATEGORY: 面向对象编程
# day_39.py


# 今日目标：
# 1. 复习子类 __init__ 和父类 __init__ 的关系
# 2. 练习 super().__init__(...) 的参数传递
# 3. 区分普通参数、*args、**kwargs 的使用场景
# 4. 复盘 day_38 中容易混淆的位置：self、参数顺序、关键字参数


# Part 1：普通参数版本
# 要求：
# 1. 定义一个父类 Animal
# 2. Animal 接收 name、breed、colour、character
# 3. 定义一个子类 Dog
# 4. Dog 额外接收 size
# 5. Dog 中用 super().__init__(...) 初始化父类属性
# 6. 实例化后打印 name 和 size
class Animal:
    def __init__(self, name, breed, colour, character):
        self.name = name
        self.breed = breed
        self.colour = colour
        self.character = character

class Dog(Animal):
    def __init__(self, name, breed, colour, character, size):
        super().__init__(name, breed, colour, character)
        self.size = size
a = Dog('W', '种类', 'blue', '还行', 'big')
print(a.name)
print(a.size)



# Part 2：*args 版本
# 要求：
# 1. 定义一个子类 Cat
# 2. Cat 自己新增 personality
# 3. 其余参数用 *args 转交给 Animal
# 4. 实例化后打印 name 和 personality
class Cat(Animal):
    def __init__(self, personality,*args,):
        super().__init__(*args)
        self.personality = personality
b = Cat('傲娇','x', '种类', 'white', '一般般')
print(b.name)
print(b.personality)
# Part 3：**kwargs 版本
# 要求：
# 1. 定义一个子类 Zebra
# 2. Zebra 自己新增 stripes
# 3. 其余参数用 **kwargs 转交给 Animal
# 4. 实例化时使用关键字参数，不依赖参数顺序
# 5. 实例化后打印 stripes 和 colour
class Zebra(Animal):
    def __init__(self, stripes, **kwargs,):
        super().__init__(**kwargs)
        self.stripes = stripes
c = Zebra(
    name='aaa',
    stripes='13',
    colour='black',
    breed='野生炫彩',
    character='okk'
)
print(c.stripes)
print(c.colour)

# Part 4：错误排查练习
# 看到一个子类 __init__ 出错时，按这个顺序检查：
# 1. 子类 __init__ 接收了哪些参数？
# 2. super().__init__(...) 传了哪些参数？
# 3. 父类 __init__ 需要哪些参数？
# 4. 有没有手动传 self？
# 5. 如果用位置参数，顺序有没有对？
# 6. 如果用关键字参数，名字和值有没有对？


# Part 5：口头复盘问题
# 1. 如果子类没有写 __init__，会发生什么？
# 2. 如果子类写了自己的 __init__，父类 __init__ 会不会自动执行？
# 3. super().__init__(...) 的本质是在做什么？
# 4. 为什么 super().__init__(self, ...) 通常是错的？
# 5. 什么时候适合用 *args？什么时候适合用 **kwargs？

# 1. 会继承父类全局属性，类属性，但不会继承父类的初始化__init__下的方法 ❌      题目说的是子类没有写__init__！
#                                                                      应当是会继承父类的__init__
# 正确答案：如果子类没有写 __init__，创建子类对象时会直接使用父类的 __init__。
# 2. 不会 ✅
# 正确答案：不会自动执行。子类写了自己的 __init__ 后，如果还想使用父类初始化逻辑，需要手动写 super().__init__(...)。
# 3. 本质是在告诉解释器，回到上一级去找__init__方法 ❌
# 正确答案：super().__init__(...) 是在子类里调用父类的 __init__，复用父类初始化属性的逻辑。
# 4. self会自动传入，至于为什么我还不是很懂 ✅
# 正确答案：super().__init__ 已经绑定了当前对象，Python 会自动把当前对象作为 self 传进去，所以括号里只写业务参数。
# 5. 位置更重要用*args，名字正确、一一对应更重要用**kwargs ✅
# 正确答案：*args 适合按位置转交一组参数；**kwargs 适合按参数名转交一组参数，顺序不重要，但名字必须对。

# 今日完成标准：
# 1. 能独立写出普通参数版本
# 2. 能解释 *args 是怎么被转交给父类的
# 3. 能解释 **kwargs 为什么不依赖参数顺序
# 4. 能用 Part 4 的顺序检查 day_38 里的问题


# Part 6：类属性、实例属性、类方法、静态方法
# 要求：
# 1. 定义 Robot 类
# 2. 类属性 count 用来统计创建了几个机器人
# 3. 每个机器人都有自己的 name 和 job
# 4. 写一个实例方法 introduce()
# 5. 写一个类方法 show_count()
# 6. 写一个静态方法 is_valid_name(name)
# 7. 创建 3 个机器人，测试 count 是否正确

# 自测问题：
# 1. self.name 和 Robot.count 最大区别是什么？      # 一个是实例属性，一个是类属性 ✅
# 正确答案：self.name 属于某一个对象；Robot.count 属于整个类，所有 Robot 对象共享。
# 2. 为什么 count 不应该写成 self.count？           # 这个是类的属性 ✅
# 正确答案：count 是统计所有机器人总数的数据，不属于某一个机器人，所以应该放在类属性里。
# 3. cls 在 classmethod 里代表什么？                # Robot这个类 ✅
# 正确答案：cls 代表当前这个类本身，这里就是 Robot 类。
# 4. staticmethod 为什么不需要 self？               # 只判断数据，不传入对象或者类本身 ✅
# 正确答案：staticmethod 只是放在类里的工具函数，不需要访问某个对象的数据，也不需要访问类的数据。
# 5. introduce() 为什么应该是实例方法？               # 每个机器人的introduce可以不一样，每个机器人性格不一样，哈哈 ✅
# 正确答案：introduce() 需要使用每个机器人自己的 name 和 job，所以它应该接收 self，作为实例方法。

class Robot:
    count = 0
    def __init__(self, name, job):
        self.name = name
        self.job = job
        type(self).count += 1

    def introduce(self):
        print(f'Hello, my name is {self.name}, my job is {self.job}.')
    
    @classmethod
    def show_count(cls):
        print(cls.count)
    
    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and len(name) > 0
a = Robot('wa', 'cleaning')
b = Robot('dd', 'cooking')
c = Robot('cc', 'teaching')
a.introduce()
b.introduce()
c.introduce()
Robot.show_count()
print(Robot.is_valid_name(a.name))
print(Robot.is_valid_name(a))   # False
print(type(a.name))
print(type(a))

class Dancer(Robot):
    def introduce(self):
        super().introduce()
        print('I can dance')

    count = 0
    
d = Dancer('jj','dancing')
Robot.show_count()
Dancer.show_count() # 1
d.introduce()

# Part 7：方法重写和 super()
# 要求：
# 1. 在 Dancer 类里重写 introduce()
# 2. Dancer 的 introduce() 要先调用父类 introduce()
# 3. 然后再额外打印一句：I can dance.
# 4. 创建一个 Dancer 对象并调用 introduce()
# 5. 对比 Robot 对象调用 introduce() 和 Dancer 对象调用 introduce() 的区别

# 观察重点：
# 1. 如果子类没有写 introduce()，会直接使用父类的 introduce()
# 2. 如果子类写了同名 introduce()，会优先使用子类自己的 introduce()
# 3. super().introduce() 表示在子类方法里调用父类的 introduce()
# 4. super().__init__() 和 super().introduce() 的共同点：都是在子类里复用父类已有逻辑

# 自测问题：
# 1. 如果 Dancer 不写 introduce()，d.introduce() 会调用谁的？   # 父类的 ✅
# 正确答案：会调用继承来的 Robot.introduce()。
# 2. 如果 Dancer 写了 introduce()，d.introduce() 会优先调用谁的？   # 优先调用子类的 ✅
# 正确答案：会优先调用 Dancer 自己的 introduce()，这叫方法重写。
# 3. super().introduce() 是什么意思？   # 调用父类的introduce()方法 ✅
# 正确答案：在子类方法里，调用父类版本的 introduce()。
# 4. super().__init__() 和 super().introduce() 的共同点是什么？ # 调用父类的某一方法 ✅
# 正确答案：它们都是在子类中复用父类已有的方法逻辑；一个调用父类初始化方法，一个调用父类普通实例方法。


# Part 8：多态 Polymorphism
# 要求：
# 1. 定义 Singer 类，继承 Robot
# 2. Singer 也重写 introduce()
# 3. Singer 的 introduce() 先调用父类 introduce()
# 4. 然后额外打印一句：I can sing.
# 5. 创建 robots 列表，里面放 Robot、Dancer、Singer 三种对象
# 6. 用 for 循环遍历 robots
# 7. 每次都调用 robot.introduce()
# 8. 观察同一个 introduce() 调用，在不同对象身上输出不同结果

# 观察重点：
# 1. 多态的核心：不同对象有同名方法，但执行效果不同
# 2. for 循环里只需要写 robot.introduce()
# 3. Python 会根据对象的真实类型，自动决定调用哪个类的 introduce()
# 4. 方法重写是实现多态的重要基础

# 自测问题：
# 1. 多态的核心是什么？
# 2. 为什么 for 循环里只写 robot.introduce() 就够了？
# 3. Python 怎么知道该调用 Robot、Dancer 还是 Singer 的 introduce()？
# 4. 多态和方法重写有什么关系？
class Singer(Robot):
    def introduce(self):
        super().introduce()
        print('I can sing')
e = Singer('jone','singing')
robots = [a, b, c, d, e]
robots_1 = [
    Robot('wa','singing'),
    Robot('j','happy'),
    Dancer('jimmy','dancing'),
    Singer('ff','singing')
]
print('\n')
for r in robots:
    r.introduce()
print('\n')
for x in robots_1:
    x.introduce()

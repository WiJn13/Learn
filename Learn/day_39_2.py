# TITLE: 面向对象复习：组合与对象关系
# CATEGORY: 面向对象编程
# day_39_2.py


# 今日目标：
# 1. 复习组合 Composition
# 2. 区分继承 is-a 和组合 has-a
# 3. 练习一个对象中保存另一个对象
# 4. 继续巩固实例属性、方法调用和对象关系


# Part 1：组合 Composition
# 要求：
# 1. 定义 Job 类
# 2. Job 里保存 job_name 和 action
# 3. Robot 不再只保存 job 字符串，而是保存一个 Job 对象
# 4. Robot 的 introduce() 要能打印自己的 name、job_name 和 action
# 5. 创建 2 个 Job 对象，例如 cleaner_job、singer_job
# 6. 创建 2 个 Robot 对象，把不同 Job 对象传进去
# 7. 调用 introduce()，观察 Robot 是如何使用 Job 对象里的数据的


# 观察重点：
# 1. 继承表示 is-a：Dancer 是一种 Robot
# 2. 组合表示 has-a：Robot 有一个 Job
# 3. 如果一个类只是“拥有”另一个东西，通常优先考虑组合
# 4. 组合可以让对象之间的关系更灵活，不一定都靠继承解决


# 自测问题：
# 1. 继承和组合最大的区别是什么？   # 继承是继承父类的一些属性，组合是我俩的属性强强结合，感觉更有层次感，拼接感，独立感，感觉不会牵一发而动全身。NMIXX概念豪爵。 ✅
# 正确答案：继承表示 is-a，一个类是一种另一个类；组合表示 has-a，一个对象拥有另一个对象。
# 2. 为什么 Dancer 适合继承 Robot？ # Dancer是一种Robot ✅
# 正确答案：因为 Dancer 可以看作一种特殊的 Robot，符合 is-a 关系。
# 3. 为什么 Job 更适合被 Robot 拥有，而不是继承 Robot？ # Robot的Job, 后面编staff后，也可以用这个Job ✅
# 正确答案：Job 不是一种 Robot，而是 Robot 拥有的工作；而且 Job 以后也可以被 Staff、Person 等其他对象复用。
# 4. self.job.job_name 这类写法是什么意思？ # 已经定义了（说定义这个词好像不准确，请纠正我）self.job = Job，会调用创建对象时的Job,而Job本身又是类，.job_name就进入这个Job类的这个方法里了 ❌
# 正确答案：self.job 保存的是创建 Robot 时传进来的那个 Job 对象；self.job.job_name 是读取这个 Job 对象里的 job_name 属性。
class Job:
    def __init__(self, job_name, action, act):
        self.job_name = job_name
        self.action = action
        self.act = act
    def do_action(self):
        print(self.act)

class Robot:
    def __init__(self, name, ID, job):
        self.name = name
        self.ID = ID
        self.job = job
    def introduce(self):
        print(f'Hello, my name is {self.name}, my ID is {self.ID}, my job is {self.job.job_name}, I can {self.job.action}.')
    def work(self):
        self.job.do_action()


a = Job('cleaning', 'clean the room', 'clean')
b = Job('singing','sing NMIXX songs', 'sing')
c = Robot('james', 21712, a)
d = Robot('Jack', 725, b)
c.introduce()
d.introduce()
c.work()
d.work()
# Part 2：组合中的对象协作
# 要求：
# 1. 在 Job 类中新增一个方法 do_action()
# 2. do_action() 负责打印这个工作的具体动作
# 3. Robot 中新增一个方法 work()
# 4. Robot.work() 不自己写具体工作内容，而是调用 self.job.do_action()
# 5. 创建不同 Job 对象
# 6. 创建不同 Robot 对象，并传入不同 Job 对象
# 7. 调用 robot.work()，观察不同 Robot 因为拥有不同 Job 而执行不同动作


# 观察重点：
# 1. self.job 保存的是一个 Job 对象
# 2. self.job.do_action() 是调用这个 Job 对象自己的方法
# 3. Robot 不需要知道每种工作的细节，只需要把工作交给 self.job
# 4. 这就是组合的灵活性：对象可以把一部分责任交给自己拥有的另一个对象


# 自测问题：
# 1. Robot.work() 为什么不直接 print 工作内容？ # 把工作内容交给Job更轻松，不然每个Robot都要设置工作内容，而且可能同一个工作不同的工作内容 ✅
# 正确答案：因为具体工作细节属于 Job，Robot 只负责把任务交给自己拥有的 Job 对象，这样职责更清楚，也更容易替换工作。
# 2. self.job.do_action() 这句代码分成几步理解？    # 我理解了 ⚠️
# 正确答案：第一步找到当前 Robot 对象的 self.job；第二步确认 self.job 是一个 Job 对象；第三步调用这个 Job 对象的 do_action() 方法。
# 3. 如果给 Robot 换一个 Job 对象，Robot.work() 的结果会不会变？    # 会 ✅
# 正确答案：会。因为 Robot.work() 调用的是 self.job.do_action()，self.job 换了，实际执行的 Job 对象也换了。
# 4. 组合和多态有没有相似的地方？   # 同一个方法(self.job.do_action())，不同的结果 ✅
# 正确答案：有相似点：外层代码都不需要写死具体细节，只调用统一的方法；不同对象负责给出不同结果。


# Part 3：运行时更换组合对象
# 要求：
# 1. 继续使用 Job 和 Robot
# 2. 再创建一个新的 Job 对象，例如 dancer_job
# 3. 先让某个 Robot 调用 work()
# 4. 然后把这个 Robot 的 job 换成新的 Job 对象
# 5. 再次调用 work()
# 6. 观察同一个 Robot 因为 self.job 被替换，执行结果发生变化


# 观察重点：
# 1. self.job 只是一个属性，里面保存的是某个 Job 对象
# 2. self.job 可以重新赋值为另一个 Job 对象
# 3. Robot 对象本身没有换，但它拥有的 Job 对象换了
# 4. 这就是组合的灵活性：不用新建子类，也能改变对象行为


# 自测问题：
# 1. 为什么给 self.job 重新赋值后，work() 的结果会变？  # self.job指向的对象变了 ✅
# 正确答案：因为 work() 调用的是 self.job.do_action()；self.job 指向新的 Job 对象后，实际执行的 do_action() 也换成了新对象的。
# 2. Robot 对象本身变了吗？还是 Robot 拥有的 Job 变了？ # 没有，拥有的job变了 ✅
# 正确答案：Robot 对象本身还是同一个对象，只是它的 self.job 属性换成了另一个 Job 对象。
# 3. 这种写法和新建 Dancer 子类相比，有什么不同？   # 更简单 ✅
# 正确答案：换 Job 对象是在运行时更换“拥有的对象”；新建 Dancer 子类是创建一种新的 Robot 类型。组合更适合可替换的功能，继承更适合稳定的 is-a 关系。
# 4. 什么时候适合用“换对象”的方式，而不是继续写新子类？ # 只是一个小属性，可更改的，不是绑定性质，比如初始性别 ✅
# 正确答案：当变化的是对象拥有的角色、工具、工作、策略等可替换部分时，适合换对象；当它本质上就是另一种类型时，才更适合写子类。
dancer_job = Job('dancer', 'dance', 'guider')
d.work()
d.job = dancer_job
d.work()


# Part 4：组合中的接口约定 Duck Typing
# 要求：
# 1. 保留 Robot.work() 调用 self.job.do_action() 的写法
# 2. 定义一个不是 Job 子类的新类，例如 Tool
# 3. Tool 里也写一个 do_action() 方法
# 4. 创建 Tool 对象
# 5. 把某个 Robot 的 job 换成 Tool 对象
# 6. 再调用 Robot.work()
# 7. 观察：只要对象有 do_action()，Robot.work() 就能调用它


# 观察重点：
# 1. Robot 不一定关心 self.job 到底是不是 Job 类创建的对象
# 2. Robot 真正在意的是：self.job 有没有 do_action() 方法
# 3. 在 Python 里，这种“只看对象能不能做某件事”的思想叫鸭子类型
# 4. 这把组合和多态连接起来了：不同对象，只要有同名方法，就可以被统一调用


# 自测问题：
# 1. Robot.work() 真正在要求 self.job 具备什么？    
# 2. 如果传进去的对象没有 do_action()，会发生什么？
# 3. 为什么 Tool 不是 Job 子类，也可能被 Robot.work() 使用？
# 4. 鸭子类型和多态有什么关系？
class Tool:
    def __init__(self, act):
        self.act = act
    def do_action(self):
        print(self.act)
tool = Tool('ac')
new = Robot('james', 21712, tool)
new.work()  # job 只是形式参数。第三个位置传进来的对象会被保存到 self.job。
            # 只要这个对象所属的类里有 do_action() 方法，Robot.work() 调用 self.job.do_action() 时就能成功。


# Part 5：抽象类 ABC 和接口约束
# 要求：
# 1. 从 abc 模块导入 ABC 和 abstractmethod
# 2. 定义一个 ActionBase 抽象类
# 3. 在 ActionBase 里定义抽象方法 do_action()
# 4. 让 Job 继承 ActionBase，并实现 do_action()
# 5. 再定义一个 Tool 类，也继承 ActionBase，并实现 do_action()
# 6. 尝试定义一个继承 ActionBase 但没有实现 do_action() 的类
# 7. 观察：没有实现抽象方法的类，不能正常创建对象


# 观察重点：
# 1. 鸭子类型是“靠约定”：只要有 do_action() 就能用
# 2. 抽象类是“强制约束”：继承后必须实现 do_action()
# 3. ABC 不一定是为了复用代码，也可以是为了规定子类必须有什么方法
# 4. 这适合在你想提前防止“忘记写 do_action()”这类错误时使用




# 自测问题：
# 1. 鸭子类型和抽象类最大的区别是什么？
# 2. abstractmethod 的作用是什么？
# 3. 为什么没有实现 do_action() 的子类不能创建对象？
# 4. 什么时候只用鸭子类型就够了？什么时候更适合用 ABC？
from abc import ABC, abstractmethod
class ActionBase(ABC):
    
    def __init__(self, act):
        self.act = act
    @abstractmethod
    def do_action(self):
        print(self.act)
class Job1(ActionBase):
    def do_action(self):
        print('job action')
class Tool1(ActionBase):
    def do_action(self):
        print('tool1 action')
class Test(ActionBase):
    pass
aa = Job1('s')
    # bb = Test('s')    # 无法创建，抽象类方法要求子类必须拥有这个方法
# 笔记：
# 1. abc 是 Python 提供抽象基类功能的标准库模块
# 2. ABC 让一个类变成抽象基类
# 3. @abstractmethod 标记“子类必须实现”的方法
# 4. @abstractmethod 放在哪个方法上，子类就必须实现哪个方法
# 5. 鸭子类型是运行时靠约定；ABC 是创建对象前先检查约束


# Part 6：组合、鸭子类型、ABC 综合复盘
# 要求：
# 1. 定义一个抽象类 ActionBase
# 2. ActionBase 里规定必须有 do_action()
# 3. 定义 CleanAction 类，继承 ActionBase，并实现 do_action()
# 4. 定义 SingAction 类，继承 ActionBase，并实现 do_action()
# 5. 定义 Robot 类，让 Robot 保存一个 action 对象
# 6. Robot.work() 调用 self.action.do_action()
# 7. 创建同一个 Robot，先传 CleanAction，再更换为 SingAction
# 8. 观察：Robot 不变，但组合进去的 action 对象变了，work() 的结果也变了


# 观察重点：
# 1. ActionBase 负责规定接口：必须有 do_action()
# 2. CleanAction / SingAction 负责实现具体动作
# 3. Robot 负责调用动作，但不负责写死动作细节
# 4. 这同时用到了组合、鸭子类型思维、ABC 约束


# 自测问题：
# 1. 这个练习里，组合体现在哪里？
# 2. 这个练习里，ABC 约束体现在哪里？
# 3. Robot.work() 为什么不需要判断 action 是 CleanAction 还是 SingAction？
# 4. 如果以后新增 DanceAction，需要改 Robot 类吗？为什么？


class ActionBase1(ABC):
    def __init__(self, mm):
        self.mm = mm
    @abstractmethod
    def do_action(self):
        pass    # 抽象方法里通常写 pass，表示这里只规定接口，不写具体执行逻辑
                # 具体执行逻辑应该交给子类自己实现
class CleanAction(ActionBase1):
    def do_action(self):
        print('also')
class SingAction(ActionBase1):
    def do_action(self):
        print('too')
class Robot1:
    def __init__(self, action: ActionBase1):
        self.action: ActionBase1 = action
    def work(self):
        self.action.do_action() # self.action.do_action 只是取到方法对象，没有真正执行
                                # self.action.do_action() 才是调用方法
b = CleanAction('s')
c = SingAction('d')
a = Robot1(b)
a.work()
a.action = c
a.work()

class Weapon(ABC):
    def __init__(self, job):
        self.job = job
    @abstractmethod
    def attack(self):
        pass
class Sword(Weapon):

    def attack(self):
        print('挥剑')
class Gun(Weapon):

    def attack(self):
        print('装弹中......')
        print('瞄准')
        print('射击')
class MagicWand(Weapon):

    def attack(self):
        print('检测能量......')
        print('远程施法')

class GameCharacter:
    def __init__(self, name, weapon):   # 参数名不要大写开头，大写开头是类名，这里只是小小的参数
        self.name = name
        self.weapon: Weapon = weapon
    def attack(self):
        print(f'{self.name}，职业是{self.weapon.job}，正在:')
        self.weapon.attack()

sword = Sword('swordman')
gun = Gun('shooter')
magic_wand = MagicWand('master')
character = GameCharacter('Eben', sword)
character.attack()
character.weapon = gun
character.attack()
character.weapon = magic_wand
character.attack()

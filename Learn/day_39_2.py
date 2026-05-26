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
# 1. 继承和组合最大的区别是什么？   # 继承是继承父类的一些属性，组合是我俩的属性强强结合，感觉更有层次感，拼接感，独立感，感觉不会牵一发而动全身。NMIXX概念豪爵。
# 2. 为什么 Dancer 适合继承 Robot？ # Dancer是一种Robot
# 3. 为什么 Job 更适合被 Robot 拥有，而不是继承 Robot？ # Robot的Job, 后面编staff后，也可以用这个Job
# 4. self.job.job_name 这类写法是什么意思？ # 已经定义了（说定义这个词好像不准确，请纠正我）self.job = Job，会调用创建对象时的Job,而Job本身又是类，.job_name就进入这个Job类的这个方法里了
class Job:
    def __init__(self, job_name, action):
        self.job_name = job_name
        self.action = action

class Robot:
    def __init__(self, name, ID, job):
        self.name = name
        self.ID = ID
        self.job = job
    def introduce(self):
        print(f'Hello, my name is {self.name}, my ID is {self.ID}, my job is {self.job.job_name}, I can {self.job.action}.')

a = Job('cleaning', 'clean the room')
b = Job('singing','sing NMIXX songs')
c = Robot('james', 21712, a)
d = Robot('Jack', 725, b)
c.introduce()
d.introduce()

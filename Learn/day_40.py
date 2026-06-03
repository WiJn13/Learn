# TITLE: 面向对象复习：类属性、类方法与静态方法
# CATEGORY: 面向对象编程
# day_40.py


# 今日目标：
# 1. 复习实例属性和类属性的区别
# 2. 复习实例方法、类方法、静态方法的使用场景
# 3. 用 Robot 练习 count、change_job、show_count、is_valid_job
# 4. 继续巩固 self、cls 和普通参数的区别


# Part 1：Robot 综合练习
# 要求：
# 1. 定义 Robot 类
# 2. 定义类属性 count，用来统计创建了几个 Robot 对象
# 3. 每个 Robot 对象有自己的 name 和 job
# 4. 写实例方法 introduce()
# 5. 写实例方法 change_job(new_job)
# 6. 写类方法 show_count()
# 7. 写静态方法 is_valid_job(job)
# 8. 创建几个 Robot 对象，测试上面的方法


# 自测问题：
# 1. change_job() 为什么是实例方法？
# 2. show_count() 为什么是类方法？
# 3. is_valid_job() 为什么是静态方法？
# 4. self 和 cls 分别代表什么？
# 5. Robot.count 和 self.job 最大区别是什么？

class InvalidJobError(ValueError):
    pass

class Robot:
    count = 0

    def __init__(self, name, job):
        self._name = name
        self.job = job


    @property
    def job(self):
        return self.job
    
    @property
    def name(self):
        return self.name

    def introduce(self):
        print(f'I am {self.name}, I can {self._job}')

    def change_job(self, new_job):
        if Robot.is_valid_job(new_job):
            self._job = new_job
        else:
            raise InvalidJobError('job must be a non-empty string')
    @job.setter # 这里的job，指的是上面被@property创建出来的那个属性入口
                # 如果只写@property，那就是只读属性
    def job(self, new_job):
        if Robot.is_valid_job(new_job):
            self._job = new_job
        else:
            raise InvalidJobError('job must be a non-empty string')

    @classmethod
    def show_count(cls):
        print(cls.count)

    @staticmethod
    def is_valid_job(job):
        return isinstance(job, str) and len(job)>0

a = Robot('j', 'clean')
b = Robot('w', 'wash')
c = Robot('mm', 13)
Robot.show_count()
a.introduce()
print(Robot.is_valid_job(a.name))
a.change_job('shop')
print(a.job)

print(b.job)
print(c.job)
try:
    b.job = 3
except InvalidJobError as e:
    print('job error:', e)
    print(type(e))
except ValueError as e:
    print('another value error:', e)
    
print(b.job)

try:
    b.job = 'cook'
except InvalidJobError as e:
    print(e)
else:
    print('change success')
finally:
    print('finish')
print(b.job)




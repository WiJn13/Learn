# TITLE: 面向对象复习：封装、属性校验与异常流程
# CATEGORY: 面向对象编程
# day_41.py


# 今日目标：
# 1. 复习 @property 和 setter 的运行路径
# 2. 区分公开属性名 balance 和内部保存名 _balance
# 3. 练习在 __init__ 中触发 setter 校验
# 4. 复习自定义异常和 try/except/else/finally 的执行顺序
# 5. 巩固类属性 count 的统计时机


# Part 1：Account 基础封装
# 要求：
# 1. 定义 InvalidBalanceError，继承 ValueError
# 2. 定义 Account 类
# 3. 类属性 count 用来统计成功创建了几个 Account 对象
# 4. 每个账户有 owner 和 balance
# 5. balance 必须是 int 或 float，并且不能小于 0
# 6. 使用 @property 读取 balance
# 7. 使用 @balance.setter 校验并修改 _balance
# 8. __init__ 中通过 self.balance = balance 触发 setter


class InvalidBalanceError(ValueError):
    pass


class Account:
    count = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        type(self).count += 1

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if Account.is_valid_balance(new_balance):
            self._balance = new_balance
        else:
            raise InvalidBalanceError('设置余额错误')

    def deposit(self, amount):
        if self.is_valid_amount(amount):
            self.balance = self.balance + amount
        else:
            raise InvalidBalanceError('金额错误')

    def withdraw(self, amount):
        if self.is_valid_amount(amount):
            self.balance = self.balance - amount
        else:
            raise InvalidBalanceError('金额错误')

    @classmethod
    def show_count(cls):
        print(cls.count)

    @staticmethod
    def is_valid_balance(balance):
        return isinstance(balance, (float, int)) and balance >= 0
    @staticmethod
    def is_valid_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

a = Account('w', 1300)
b = Account('j', 3200)
print(a.balance)
print(b.balance)
a.deposit(13)
b.withdraw(22)
print(a.balance)
print(b.balance)
Account.show_count()
# Part 2：测试正常情况
# 要求：
# 1. 创建两个正常账户
# 2. 打印账户余额
# 3. 调用 deposit()
# 4. 调用 withdraw()
# 5. 调用 Account.show_count()


# Part 3：测试异常情况
# 要求：
# 1. 尝试创建一个负数余额账户
# 2. 尝试把 balance 改成字符串
# 3. 尝试 withdraw 超过当前余额的钱
# 4. 使用 try/except 捕获 InvalidBalanceError
# 5. 观察 else 和 finally 分别在什么时候执行
try:
    c = Account('w',-13)
except InvalidBalanceError:
    print('余额不能为负')

b.balance = 14
print(b.balance)
try:
    b.balance = '13'
except InvalidBalanceError:
    print(b.balance)    #打印的是原来的值，14

try:
    b.withdraw(15)
except InvalidBalanceError:
    print(b.balance)
else:
    print('success')
finally:
    print('finish')


# 自测问题：
# 1. 为什么 getter 里不能写 return self.balance？
# 答案：因为读取 self.balance 会再次调用 getter 自己，导致无限递归。
# getter 应该返回真正保存数据的内部属性：self._balance。
#
# 2. 为什么 setter 里最后应该修改 self._balance？
# 答案：因为 setter 本身就是 balance 的赋值入口。
# 如果在 setter 里写 self.balance = new_balance，会再次调用 setter 自己。
# 所以校验通过后，应该直接修改内部保存值 self._balance。
#
# 3. __init__ 里写 self.balance = balance 会调用哪个方法？
# 答案：会调用 @balance.setter 修饰的 balance 方法。
# 读取 self.balance 走 getter；给 self.balance 赋值走 setter。
#
# 4. count 应该在校验前增加，还是校验成功后增加？
# 答案：应该在校验成功后增加。
# 因为 count 统计的是成功创建的 Account 对象；如果余额不合法，创建失败，不应该计数。
#
# 5. deposit() 和 withdraw() 是直接改 _balance，还是通过 balance 入口修改？为什么？
# 答案：应该通过 self.balance 入口修改。
# 因为 self.balance = ... 会走 setter 校验，能防止余额变成负数。
# 只有 getter 和 setter 内部才应该直接接触 self._balance。⭐️⭐️⭐️

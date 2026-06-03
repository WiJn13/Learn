# TITLE: 面向对象进阶：继承、封装与多态综合练习
# CATEGORY: 面向对象编程
# day_42.py


# 今日判断：
# 你已经连续练过类属性、类方法、静态方法、@property、setter、自定义异常。
# day_42 不继续重复单个 setter，而是把它们放进继承场景里综合使用。


# 今日目标：
# 1. 复习父类和子类的职责分工
# 2. 在父类 Account 中集中处理 balance 的封装和校验
# 3. 在子类中新增自己的属性
# 4. 练习方法重写：子类改写 withdraw() 或 summary()
# 5. 用同一个 for 循环调用不同对象的同名方法，观察多态


# Part 1：父类 Account
# 要求：
# 1. 定义 InvalidBalanceError，继承 ValueError
# 2. 定义 Account 类
# 3. 类属性 count 统计成功创建的账户数量
# 4. __init__ 接收 owner 和 balance
# 5. balance 使用 @property 和 @balance.setter 管理
# 6. balance 必须是 int 或 float，并且不能小于 0
# 7. deposit(amount)：存钱，amount 必须大于 0
# 8. withdraw(amount)：取钱，amount 必须大于 0，且不能让余额变成负数
# 9. summary()：打印 owner 和 balance
# 10. show_count()：打印账户数量


class InvalidBalanceError(ValueError):
    pass


class Account:
    total_count = 0
    count = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        # type(self) 会拿到当前对象的真实类。
        # 如果 self 是 Account 对象，就改 Account.count。
        # 如果 self 是 SavingsAccount 对象，就改 SavingsAccount.count。
        # 如果 self 是 CheckingAccount 对象，就改 CheckingAccount.count。
        # Account.total_count 是固定写死的父类总账本：所有成功账户都加到这里。
        # type(self).count 是当前真实类型自己的账本：普通账户、储蓄账户、支票账户分开统计。
        Account.total_count += 1
        type(self).count += 1


    @property
    def balance(self):
        # 返回真正保存余额的内部属性
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        # 如果余额合法，保存到内部属性
        # 如果余额不合法，raise InvalidBalanceError
        if self.is_valid_balance(new_balance):
            self._balance = new_balance
        else:
            raise InvalidBalanceError('balance must >= 0')

    def deposit(self, amount):
        # 判断 amount 是否合法
        # 合法时通过 self.balance 修改余额
        if self.is_valid_amount(amount):
            self.balance = self.balance + amount
        else:
            raise InvalidBalanceError('deposit amount must > 0')

    def withdraw(self, amount):
        if self.is_valid_amount(amount):
            self.balance = self.balance - amount
        else:
            raise InvalidBalanceError('withdraw amount must > 0 and <= balance')

    def summary(self):
        # 打印 owner 和 balance
        print(self.owner, self.balance)

    @classmethod
    def show_count(cls):
        # 打印 cls.count
        print(cls.count)

    @staticmethod
    def is_valid_balance(balance):
        # 判断 balance 是否是 int 或 float，并且 >= 0
        return isinstance(balance, (int, float)) and balance >= 0

    @staticmethod
    def is_valid_amount(amount):
        # 判断 amount 是否是 int 或 float，并且 > 0
        return isinstance(amount, (int, float)) and amount > 0


# Part 2：子类 SavingsAccount
# 要求：
# 1. SavingsAccount 继承 Account
# 2. __init__ 额外接收 rate
# 3. 用 super().__init__(owner, balance) 复用父类初始化
# 4. 新增 add_interest()：把 balance 按 rate 增加
# 5. 重写 summary()：除了 owner 和 balance，也打印 rate


class SavingsAccount(Account):
    count = 0
    def __init__(self, owner, balance, rate):
        # 调用父类 __init__
        # 保存 rate
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        # 通过 self.balance 修改余额
        self.balance = self.balance * (1 + self.rate)

    def summary(self):
        # 重写父类 summary
        print(self.owner, f'{self.balance:.2f}', self.rate)


# Part 3：子类 CheckingAccount
# 要求：
# 1. CheckingAccount 继承 Account
# 2. __init__ 额外接收 fee
# 3. 用 super().__init__(owner, balance) 复用父类初始化
# 4. 重写 withdraw(amount)
# 5. 取钱时除了扣 amount，还要额外扣 fee
# 6. 仍然不能让余额变成负数


class CheckingAccount(Account):
    count = 0
    def __init__(self, owner, balance, fee):
        # 调用父类 __init__
        # 保存 fee
        super().__init__(owner, balance)
        self.fee = fee

    def withdraw(self, amount):
        # 判断 amount 是否合法
        # 实际扣除 amount + self.fee
        # 通过 self.balance 修改余额，让 setter 继续负责余额校验
        if self.is_valid_amount(amount):
            self.balance = self.balance - amount - self.fee
        else:
            raise InvalidBalanceError('withdraw amount must be valid')
    def summary(self):
        # 重写父类 summary
        print(self.owner, self.balance)


# Part 4：测试正常情况
# 要求：
# 1. 创建一个 Account
# 2. 创建一个 SavingsAccount
# 3. 创建一个 CheckingAccount
# 4. 分别调用 deposit()、withdraw()、add_interest()
# 5. 调用 Account.show_count()
a = Account('wang',2300)
# a 是 Account 对象：type(self) 是 Account，所以 Account.count 从 0 变成 1。
a.deposit(2100)

b = SavingsAccount('z', 1300, 0.1)
# b 是 SavingsAccount 对象：type(self) 是 SavingsAccount。
# SavingsAccount 类里已经写了 count = 0。
# 所以这里不会去父类 Account 借 count，而是直接让 SavingsAccount.count 从 0 变成 1。
# 同时，因为子类 __init__ 调用了 super().__init__()，Account.total_count 也会加 1。
b.add_interest()

c = CheckingAccount('j', 1300, 13)
# c 是 CheckingAccount 对象：type(self) 是 CheckingAccount。
# CheckingAccount 类里也写了 count = 0。
# 所以这里直接让 CheckingAccount.count 从 0 变成 1。
# 同时，Account.total_count 也会加 1。
c.withdraw(1100)
# Part 5：测试多态
# 要求：
# 1. 把 Account、SavingsAccount、CheckingAccount 对象放进同一个列表
# 2. 用 for 循环遍历
# 3. 每次只写 account.summary()
# 4. 观察：同一个 summary()，不同对象会执行不同版本
accounts = [a, b ,c]
for i in accounts:
    i.summary()


# Part 6：测试异常情况
# 要求：
# 1. 尝试创建负数余额账户
# 2. 尝试 deposit(-10)
# 3. 尝试 withdraw 超过余额的钱
# 4. 用 try/except 捕获 InvalidBalanceError
# 5. 观察余额是否保持在出错前的状态
try:
    e = Account('Q', -12)
except InvalidBalanceError:
    print('无法创建负余额账户')
# 这个对象创建失败：setter 抛出异常，__init__ 没有执行到 type(self).count += 1。
# 所以它不计数。
e = Account('Q', 12)
# e 是 Account 对象：Account.count 从 1 变成 2。
try:
    e.deposit(-10)
except InvalidBalanceError:
    print('存入金额为负！')
try:
    e.withdraw(13)
except InvalidBalanceError:
    print('你没有这么多钱！')
print(e.balance)
f = Account('w', 0)
# f 是 Account 对象：Account.count 从 2 变成 3。
print(f.balance)


# 自测问题：
# 1. Account 为什么适合做父类？
# 我的原回答：总类
# 答案：因为 Account 保存的是所有账户共有的数据和行为。
# owner、balance、deposit()、withdraw()、summary()、余额校验，都属于账户的共同基础。
#
# 2. SavingsAccount 为什么需要调用 super().__init__()？
# 我的原回答：父类有这个方法，自己也需要
# 答案：因为 SavingsAccount 也需要复用父类的初始化流程。
# super().__init__(owner, balance) 会完成 owner 保存、balance setter 校验、total_count 总计数、当前类型 count 计数。
#
# 3. CheckingAccount 重写 withdraw() 后，父类 withdraw() 还会自动执行吗？
# 我的原回答：不会
# 答案：不会。
# 子类写了同名方法后，会优先执行子类自己的 withdraw()。
# 除非在子类方法里手动写 super().withdraw(amount)，父类版本才会被调用。
#
# 4. 子类里为什么仍然通过 self.balance 修改余额，而不是直接改 self._balance？
# 我的原回答：校验
# 答案：因为 self.balance = ... 会走 setter，可以继续做余额校验。
# 如果直接改 self._balance，就绕过了统一校验入口。
#
# 5. for 循环里只写 account.summary()，Python 怎么知道该调用哪个版本？
# 我的原回答：每个账户内部都有 summary() 方法，多态。
# 答案：Python 会看 account 当前指向的真实对象类型。
# 如果是 SavingsAccount 对象，就优先调用 SavingsAccount.summary()。
# 如果是 CheckingAccount 对象，就优先调用 CheckingAccount.summary()。
# 如果子类没有自己的 summary()，才会去父类 Account 里找。
#
# 计数预测：
# 输出是 5。
# a、b、c、e、f 创建成功，各计数一次。
# Account('Q', -12) 因为余额校验失败，__init__ 没有执行到 Account.count += 1，所以不计数。
# 修正：上面这个预测适用于 Account.count += 1 的版本。
# 现在代码里同时写了 Account.total_count += 1 和 type(self).count += 1。
# 所以现在有两套统计：
# Account.total_count 是所有成功账户总数：a、b、c、e、f，一共 5。
# type(self).count 是按真实对象类型分别统计：
# Account.count 是 3：a、e、f。
# SavingsAccount.count 是 1：b。
# CheckingAccount.count 是 1：c。
#
# 三个位置彻底分清：
# 1. Account.xxx
# 意思是明确操作 Account 这个父类自己的属性。
# 例如 Account.total_count += 1，就是所有账户都统一加到父类总账本里。
#
# 2. type(self).xxx
# 用在实例方法里，因为 self 是具体对象，type(self) 可以拿到它的真实类。
# 例如创建 b 时，self 是 b 这个对象，type(self) 就是 SavingsAccount。
# 所以 type(self).count += 1 会修改 SavingsAccount.count。
#
# 3. cls.xxx
# 用在 classmethod 里，因为 cls 已经是调用这个方法的类本身。
# a.show_count() 时，cls 是 Account。
# b.show_count() 时，cls 是 SavingsAccount。
# Account.show_count() 时，cls 是 Account。
# 所以 classmethod 里直接写 cls.count，不要写 type(cls).count。


# 今日完成标准：
# 1. 能独立完成 Account 的 property 和 setter
# 2. 能写出至少一个子类的 __init__ + super().__init__(...)
# 3. 能解释“方法重写”不是覆盖文件，而是子类定义同名方法
# 4. 能看懂多态：同一个方法名，在不同对象身上有不同执行效果
a.show_count()  # 输出 3：a 是 Account 对象，所以 cls 是 Account，打印 Account.count。
b.show_count()  # 输出 1：b 是 SavingsAccount 对象，所以 cls 是 SavingsAccount。
c.show_count()  # 输出 1：c 是 CheckingAccount 对象，所以 cls 是 CheckingAccount。
e.show_count()  # 输出 3：e 是 Account 对象，所以 cls 是 Account。
f.show_count()  # 输出 3：f 是 Account 对象，所以 cls 是 Account。
Account.show_count()  # 输出 3：直接用 Account 调用，cls 是 Account。
SavingsAccount.show_count()  # 输出 1：直接用 SavingsAccount 调用，cls 是 SavingsAccount。
print(Account.total_count)  # 输出 5：这是属性，不是方法，所以用 print 看总数。
print(type(c))
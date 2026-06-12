# TITLE: 面向对象复习：从“会写类”到“会拆对象”
# CATEGORY: 面向对象编程
# day_43.py


# 今日判断：
# 你已经练过：
# 1. class / object / self
# 2. 类属性、类方法、静态方法
# 3. @property 和 setter
# 4. 自定义异常
# 5. 继承、super()、方法重写
# 6. 多态、组合、鸭子类型、ABC
#
# day_43 不继续重复“单个类怎么写”。
# 今天重点练：看到一个小需求时，怎么判断哪些东西应该是类，哪些适合继承，哪些适合组合。


# 今日目标：
# 1. 区分 is-a 和 has-a
# 2. 复习“父类负责共同规则，子类负责不同表现”
# 3. 复习“对象拥有另一个对象”的组合写法
# 4. 用 ABC 规定统一接口
# 5. 用一个小订单场景，把 property、异常、组合、多态串起来


# Part 1：先判断，不急着写代码
# 要求：
# 在每一题后面写一句判断：适合继承，还是适合组合？为什么？
#
# 1. SavingsAccount 和 Account
# 我的判断：适合继承
#
# 2. Robot 和 Job
# 我的判断：组合
#
# 3. Order 和 Product
# 我的判断：组合
#
# 4. Order 和 PaymentMethod
# 我的判断：组合
#
# 5. CardPayment、CashPayment 和 PaymentMethod
# 我的判断：绝对是继承
#
#
# 提示：
# is-a：A 是一种 B，通常考虑继承。
# has-a：A 拥有一个 B，通常考虑组合。
# same-interface：多个类都有同一个动作，可以考虑抽象类或鸭子类型。


# Part 2：定义支付接口 PaymentMethod
# 要求：
# 1. 从 abc 导入 ABC 和 abstractmethod
# 2. 定义 PaymentMethod，继承 ABC
# 3. 在 PaymentMethod 里定义抽象方法 pay(amount)
# 4. pay(amount) 只规定“必须有这个方法”，不负责具体支付细节
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass



# Part 3：定义不同支付方式
# 要求：
# 1. 定义 CashPayment，继承 PaymentMethod
# 2. 实现 pay(amount)，打印现金支付金额
# 3. 定义 CardPayment，继承 PaymentMethod
# 4. __init__ 接收 card_number
# 5. 实现 pay(amount)，打印银行卡尾号和支付金额
# 6. 定义 PointsPayment，继承 PaymentMethod
# 7. __init__ 接收 points
# 8. 实现 pay(amount)
# 9. 如果积分不够，raise ValueError
#
# 观察重点：
# 三个类的 pay() 输出不同，但外部都可以统一调用 .pay(amount)。
# 这就是多态：同一个方法名，不同对象有不同执行效果。
class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f'支付{amount}元')
class CardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number
    def pay(self, amount):
        print(self.card_number[-4:], f'{amount}元')
class PointsPayment(PaymentMethod):
    def __init__(self, points):
        self.points = points
    def pay(self, amount):
        if amount <= self.points:
            print(f'使用积分{amount}支付成功')
        else:
            raise ValueError('积分不足！')

# Part 4：定义 Product，复习 property 和 setter
# 要求：
# 1. 定义 InvalidPriceError，继承 ValueError
# 2. 定义 Product 类
# 3. __init__ 接收 name 和 price
# 4. price 使用 @property 和 @price.setter 管理
# 5. price 必须是 int 或 float，并且大于 0
# 6. 如果 price 不合法，raise InvalidPriceError
#
# 观察重点：
# Product 自己负责保护自己的 price。
# Order 不应该直接管 Product 的 price 校验细节。
class InvalidPriceError(ValueError):
    pass

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_num):
        if self.is_valid_price(new_num):
            self._price = new_num
        else:
            raise InvalidPriceError('价格错误')

    def is_valid_price(self, price):
        return isinstance(price, (int, float)) and price > 0
    



# Part 5：定义 Order，练习组合
# 要求：
# 1. 定义 Order 类
# 2. __init__ 接收 customer
# 3. 每个 Order 有自己的 products 列表
# 4. 每个 Order 有自己的 payment_method，初始值可以是 None
# 5. add_product(product)：把 Product 对象加入 products
# 6. set_payment_method(payment_method)：保存支付方式对象
# 7. total_price()：返回所有商品价格总和
# 8. checkout()：
#    - 如果没有商品，raise ValueError
#    - 如果没有支付方式，raise ValueError
#    - 否则调用 self.payment_method.pay(self.total_price())
#
# 观察重点：
# Order has products：一个订单拥有多个商品。
# Order has payment_method：一个订单拥有一种支付方式。
# Order 不需要知道现金、银行卡、积分支付的内部细节。
class Order:
    
    def __init__(self, customer):
        self.customer = customer
        self.products = []
        self.payment_method = None
    def add_product(self, product):
        self.products.append(product)

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def total_price(self):
        total = 0
        for i in self.products:
            total += i.price
        return total

    def checkout(self):
        if self.products == [] or self.payment_method == None:
            raise ValueError
        else:
            self.payment_method.pay(self.total_price())




# Part 6：测试正常流程
# 要求：
# 1. 创建两个 Product 对象
# 2. 创建一个 Order 对象
# 3. 把商品加入订单
# 4. 设置 CashPayment，调用 checkout()
# 5. 再把支付方式换成 CardPayment，调用 checkout()
# 6. 再把支付方式换成 PointsPayment，调用 checkout()
#
# 观察重点：
# 同一个 order.checkout()，因为 payment_method 换了，实际支付行为也会变。
# 这和 day_39_2 里 Robot 换 Job 对象是同一个思想。
fish = Product('fish', 13)
fork = Product('fork', 10)
a = Order('wang')
a.add_product(fish)
a.add_product(fork)
a.set_payment_method(CashPayment())
a.checkout()
a.set_payment_method(CardPayment('2017846618664'))
a.checkout()
a.set_payment_method(PointsPayment(55))
a.checkout()

# Part 7：测试异常流程
# 要求：
# 1. 尝试创建价格为负数的 Product
# 2. 尝试 checkout 一个没有商品的 Order
# 3. 尝试 checkout 一个没有支付方式的 Order
# 4. 尝试用积分不够的 PointsPayment 支付
# 5. 分别用 try/except 捕获错误
#
# 观察重点：
# 异常不是为了让程序“看起来复杂”。
# 异常的作用是：当对象进入不合法状态，或者操作无法完成时，明确中断当前流程。
try:
    water = Product('water', -1)
except InvalidPriceError:
    print('价格设置错误')

try:
    b = Order('jjj')
    b.checkout()
except ValueError:
    print('请添加商品')

try:
    b = Order('kkk')
    b.add_product(fish)
    b.checkout()
except ValueError:
    print('请选择支付方式')

# 自测问题：
# 1. 为什么 Product.price 适合用 setter 管理？
# 强制每个商品都设置价格
# 2. 为什么 Order 不应该直接写 if payment_method == "cash" 这类判断？
# 太复杂了！
# 3. Order.checkout() 调用 self.payment_method.pay(...) 时，Python 怎么知道执行哪个 pay()？
# order的实例对象设置支付方式的时候，self.payment_method的这个payment_method用的就是之前的类，把这个类的实例对象传入了，接着走这个支付方式的对应的Pay
# 4. PaymentMethod 这个抽象类主要是为了复用代码，还是为了规定接口？
# 规定接口
# 5. 如果某个类没有继承 PaymentMethod，但也写了 pay(amount)，Order 能不能调用它？
#    进一步想：这种写法属于鸭子类型，还是 ABC 约束？
# 能
# Python 不会先检查它是不是 PaymentMethod 子类。它只会看：self.payment_method 这个对象身上有没有 pay 方法，而且调用时参数能不能对上。
# 所以在当前代码里，Order 这一层体现的是鸭子类型：像支付方式一样有 pay(amount)，就能被当支付方式用。
# 6. 什么时候你会选择继承？什么时候你会选择组合？
# a is b 用继承，a has b 用组合

# 今日完成标准：
# 1. 能说出 Order 和 Product 为什么是组合关系
# 不同order可以有不同product，order和product都不是从属关系
# 2. 能说出 CardPayment 和 PaymentMethod 为什么是继承关系
# cardpayment从属于，属于paymentmethod的一种
# 3. 能独立写出 Product.price 的 getter 和 setter
# 4. 能让 Order.checkout() 不关心具体支付方式，只调用统一的 pay()
# 5. 能解释“换支付对象后，checkout 行为为什么会变”

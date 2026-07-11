# TITLE: Python 工程化入门：main()、程序入口与模块复用
# CATEGORY: 模块化与代码组织
# day_44.py


# 今日判断：
# 你已经基本掌握了单文件里的 OOP：
# 1. class / object / self
# 2. property / setter / 自定义异常
# 3. 继承、组合、多态
# 4. ABC 和鸭子类型的区别
#
# day_44 不继续堆新的 OOP 概念。
# 今天开始练：怎么把“能运行的练习代码”整理成“以后能复用、能导入、能测试的小模块”。


# 今日目标：
# 1. 区分“定义代码”和“执行代码”
# 2. 理解 __name__ 的作用
# 3. 理解 if __name__ == "__main__": 为什么常见
# 4. 学会把临时测试代码放进 main()
# 5. 为之后多文件项目做准备


# Part 1：先看核心规则
# 规则：
# 1. 函数、类的定义代码：被 import 时也会被加载。
# 2. 顶层执行代码：被 import 时也会直接运行。
# 3. if __name__ == "__main__": 里面的代码，只在当前文件被直接运行时执行。
#
# 判断方法：
# - 直接运行这个文件时，__name__ 的值是 "__main__"。
# - 被其他文件 import 时，__name__ 的值是模块名，比如 "day_44"。


# Part 2：定义可以复用的函数
# 观察重点：
# 下面这些函数只负责“能力”。
# 它们不应该自动执行，也不应该依赖某一次临时测试。
def is_valid_price(price):
    return isinstance(price, (int, float)) and price >= 0


def add_product(products, name, price):
    if not is_valid_price(price):
        raise ValueError("invalid price")
    products.append({"name": name, "price": price})

def remove_product(products, name):
    for product in products:
        if product['name'] == name:
            products.remove(product)
            return
    raise ValueError('商品不存在')

def clear_products(products):
    products.clear()

def update_product_price(products, name, new_price):
    if not is_valid_price(new_price):
        raise ValueError('new_price error')
    else:
        for product in products:
            if product['name'] == name:
                product['price'] = new_price
                return
        raise ValueError('找不到商品')

def total_price(products):
    total = 0
    for product in products:
        total += product["price"]
    return total

def count_products(products):
    return len(products)

def find_product(products, name):
    for product in products:
        if product['name'] == name:
            return product
    raise ValueError('无当前商品')

# Part 3：main() 只负责组织一次运行流程
# 观察重点：
# main() 不是 Python 强制要求的语法。
# 它是一种代码组织习惯：把“这次要跑什么”集中放在一起。
def main():
    products = []

    add_product(products, "fish", 13)
    add_product(products, "fork", 10)
    add_product(products, 'water', 5)
    try:
        add_product(products, 'go', -1)
    except ValueError:
        print('价格设置错误')
    remove_product(products, 'fork')
    print(total_price(products))
    clear_products(products)
    print(products)
    print(__name__)

# Part 4：程序入口
# 观察重点：
# 这一句的意思不是“定义 main”。
# 它的意思是：只有当这个文件被直接运行时，才调用 main()。
if __name__ == "__main__":
    main()


# Part 5：你来判断
# 先不要写代码，先回答判断。
#
# 1. is_valid_price() 属于“定义代码”还是“执行代码”？
# 我的回答：
# 定义代码

# 2. add_product(products, "water", -1) 如果直接写在文件最外层，有什么问题？
# 我的回答：
# main()的时候不会跑 ❎
# 正确答案：如果写在最外层，它会变成顶层执行代码。
#          这个文件被 import 时也会执行，容易产生不该发生的添加商品、报错或 print。
# 3. 为什么临时测试代码更适合放进 main()？
# 我的回答：
# 集中？
# 标准答案：临时测试代码放进main()，可以集中管理一次运行流程
# 并且避免import这个文件时自动执行测试代码

# 4. 如果另一个文件 import day_44，你希望它自动 print(total_price(products)) 吗？
# 我的回答：
# 不

# 5. if __name__ == "__main__": 主要是在解决什么问题？
# 我的回答：
# 让代码仅在当前文件可跑，不会被其他文件import

# Part 6：小练习
# 要求：
# 1. 在 main() 里再添加一个商品 "water"，价格 5
# 2. 运行文件，观察总价是否变成 28
# 3. 尝试添加一个价格为 -1 的商品
# 4. 用 try/except 捕获 ValueError
# 
#
# 注意：
# 这一步不是为了练异常本身。
# 重点是看清楚：函数负责规则，main() 负责组织流程。
# 相当于，函数部分负责规则，最后的一切都由一个main()来运行


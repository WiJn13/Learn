# TITLE: Python 工程化入门：assert、测试函数与行为验证
# CATEGORY: 测试与代码验证
# day_45.py


# 今日判断：
# day_44 已经完成了一个关键转变：
# 以前重点是“把代码写出来并运行”。
# 现在开始练“代码能不能被别人 import、复用、测试”。
#
# 今天不急着学 pytest。
# 先用最基础的 assert 理解测试的本质：
# 测试不是看函数有没有运行，而是看运行后的结果是否符合预期。


# 今日目标：
# 1. 理解 assert 的作用
# 2. 理解一个测试函数通常包含三步：准备数据、执行行为、验证结果
# 3. 理解为什么不同错误场景应该拆开测试
# 4. 继续巩固 import 模块时不会自动执行 main()


import day_44
import pytest

# Part 1：assert 的核心规则
# assert 后面应该是一个“判断表达式”。
# 如果判断结果是 True，程序继续运行。
# 如果判断结果是 False，Python 会抛出 AssertionError。
#
# 例子：
# assert 1 + 1 == 2
# assert 1 + 1 == 3, "math is wrong"
#
# 注意：
# 这里要用 == 判断是否相等。
# = 是赋值，不能写在 assert 的判断表达式里。

def make_products():
    return [
        {'name': 'goose', 'price': 13},
        {'name': 'fork', 'price': 25}
    ]
# Part 2：一个测试函数的三步
# 1. 准备数据：准备 products
# 2. 执行行为：调用 day_44.add_product(...)
# 3. 验证结果：用 assert 判断 products 是否变成预期状态
def test_add_product_behavior():
    products = []

    day_44.add_product(products, "apple", 6)

    assert products == [
        {"name": "apple", "price": 6}
    ]


# Part 3：测试 return 值
# total_price(products) 不负责修改列表。
# 它负责根据当前 products 计算并返回总价。
def test_total_price_return_value():
    products = make_products()

    result = day_44.total_price(products)

    assert result == 38

def test_total_price_returns_0_for_empty_list():
    products = []
    result = day_44.total_price(products)
    assert result == 0

# Part 4：测试异常
# 这个 helper 的意思是：
# 我预计 func() 会抛出 ValueError。
# 如果没有抛出，测试就失败。
# 如果确实抛出了 ValueError，测试通过。

def test_add_product_for_zero_price():
    products = make_products()
    day_44.add_product(products, 'milk', 0)
    expected = make_products()
    expected.append({'name': 'milk', 'price': 0})
    assert products == expected
    assert len(products) == 3
    assert products[-1] == {'name': 'milk', 'price': 0}

def test_add_product_invalid_price():
    products = []

    with pytest.raises(ValueError):
        day_44.add_product(products, 'goose', -3)


# Part 5：为什么错误场景要拆开
# 如果一个函数里连续写两个会报错的操作：
#
# def bad_case():
#     day_44.update_product_price(products, "no_exist", 16)
#     day_44.update_product_price(products, "goose", -1)
#
# 第一行一旦 raise ValueError，函数会立刻中断。
# 第二行根本不会执行。
#
# 所以这两个错误场景应该拆成两个测试：
# 1. 商品不存在
# 2. 新价格不合法
def test_update_product_price_missing_product():
    products = make_products()

    with pytest.raises(ValueError):
        day_44.update_product_price(products, 'no_exist', 15)


def test_update_product_price_invalid_price():
    products = [
        {"name": "goose", "price": 26}
    ]

    with pytest.raises(ValueError):
        day_44.update_product_price(products, 'goose', -1)

def test_count_products():
    products = make_products()

    result = day_44.count_products(products)
    assert result == 2
    assert products == make_products()

def test_count_products_returns_zero_for_empty_products():
    products = []
    result = day_44.count_products(products)
    assert result == 0

def test_find_product_found():
    products = make_products()
    result = day_44.find_product(products, 'goose')
    assert result == {'name': 'goose', 'price': 13}
    assert products == make_products()
    
def test_find_product_no_found():
    products = make_products()
    with pytest.raises(ValueError):
        day_44.find_product(products, 'milk')
    assert products == make_products()

# Part 6：main() 只负责临时运行这些测试
# 以后学 pytest 时，测试工具会自动找 test_ 开头的函数。
# 现在先手动调用，目的是看清楚每个测试函数的运行顺序。



# 自测问题：
# 1. assert 后面为什么应该写判断表达式？
# 我的回答：因为是判断是否完全等于，而非赋值
# 批改：✅ 方向对，但要更准确一点：
# assert 后面需要的是“能判断 True / False 的表达式”。
# 它不一定只能判断“完全等于”，也可以判断大小、是否在列表中、是否为 True 等。
# 关键区别是：== 是比较，= 是赋值，assert 里要写判断逻辑。
#
# 2. 为什么 test_add_product_behavior() 要先创建一个空列表？
# 我的回答：因为需要传入product列表，而且最开始一定是空的再加商品
# 批改：✅ 对。
# 这个空列表是测试的“初始状态”。
# 先把起点固定住，后面才能判断 add_product() 有没有把它改成预期结果。
#
# 3. 为什么商品不存在和价格不合法要拆成两个测试？
# 我的回答：因为第一行raise ValueError后函数就中断了，第二行没有进行检查
# 批改：✅ 对。
# 一个测试最好只验证一个明确场景。
# 否则前一个错误已经中断函数，后一个错误其实没有被测到。
#
# 4. day_45 import day_44 时，为什么不会自动执行 day_44.main()？
# 我的回答：因为day_44的main()的执行条件是__name__ == __main__，但是导入的day_44的__name__是day_44，现在的day_45才是__main__
# 批改：✅ 对，核心逻辑已经说清楚了。
# 更标准地写是：day_44 被 import 时，day_44 里的 __name__ 是 "day_44"。
# 所以 day_44.py 里的 if __name__ == "__main__": 条件不成立，main() 不会自动执行。




# TITLE: Python 工程化入门：pytest.mark.parametrize 与多组测试数据
# CATEGORY: 测试与代码验证
# day_46.py


# 今日判断：
# day_45 已经掌握了 assert、pytest.raises(ValueError) 和测试场景拆分。
# 今天不重复异常测试语法。
# 今天重点练一个新能力：
# 当同一个函数需要用多组输入验证同一条规则时，用 parametrize 减少重复。


# 今日目标：
# 1. 理解 pytest.mark.parametrize 的作用
# 2. 区分“同一条规则的多组输入”和“不同类型的行为”
# 3. 用参数化测试 total_price() 和 count_products()
# 4. 暂时不把正常返回和异常场景硬合并


import day_44
import pytest


def make_products():
    return [
        {"name": "goose", "price": 13},
        {"name": "fork", "price": 25},
    ]


# Part 1：parametrize 的基本读法
# @pytest.mark.parametrize(...) 是给测试函数加一个 pytest 标记。
# 这个标记告诉 pytest：
# 下面这个测试函数不要只运行一次，而是按多组数据重复运行。
#
# "products, expected" 表示测试函数会收到两个参数：
# 1. products
# 2. expected
#
# 后面的列表里，每一个 tuple 就是一组测试数据。
@pytest.mark.parametrize(
    "products, expected",
    [
        (make_products(), 38),
        ([], 0),
        ([{"name": "water", "price": 5}], 5),
        ([{'name': 'free', 'price': 0}, {'name': 'book', 'price': 10}], 10)
    ],
)
def test_total_price_with_many_cases(products, expected):
    result = day_44.total_price(products)

    assert result == expected


# Part 2：什么时候适合合并成参数化测试
# 适合：
# - 同一个函数
# - 同一类行为
# - 只是输入和预期结果不同
#
# count_products(products) 的规则是：
# 返回 products 里有几个商品。
# 所以下面几组都是同一条规则的不同输入。
@pytest.mark.parametrize(
    "products, expected",
    [
        (make_products(), 2),
        ([], 0),
        ([{"name": "milk", "price": 7}], 1),
        ([{'name': 'egg', 'price': 1}, {'name': 'chick', 'price': 35}], 2)
    ],
    ids=['whole_products', 'empty_list', 'one_product', 'two_products']
)
def test_count_products_with_many_cases(products, expected):
    result = day_44.count_products(products)

    assert result == expected


# Part 3：不适合硬合并的情况
# add_product(products, name, price) 有两类行为：
# 1. price 合法：应该添加商品
# 2. price 不合法：应该 raise ValueError
#
# 它们虽然都调用 add_product()，但验证的行为类型不同。
# 所以初学阶段先拆开写，更清楚。
@pytest.mark.parametrize(
    "name, price, expected_product",
    [
        ("apple", 6, {"name": "apple", "price": 6}),
        ("milk", 0, {"name": "milk", "price": 0}),
    ],
)
def test_add_product_valid_price_cases(name, price, expected_product):
    products = []

    day_44.add_product(products, name, price)

    assert products == [expected_product]


@pytest.mark.parametrize("price", [-1, -3])
def test_add_product_invalid_price_cases(price):
    products = []

    with pytest.raises(ValueError):
        day_44.add_product(products, "bad_product", price)


# Part 4：你来判断
# 下面这些问题先不用写进代码，先在对话里回答：
#
# 1. test_total_price_with_many_cases() 实际会被 pytest 运行几次？
# 三次

# 2. 为什么 total_price 的三个案例适合放在一起？
# 都是正常情况下的同一种方法

# 3. 为什么 add_product 的“合法价格”和“不合法价格”这里仍然拆成两个测试函数？
# 两种给出的结果不一样，一种是True，一种是False
# 正确答案：
# 因为它们验证的是两种不同类型的行为。
# 合法价格：函数应该正常执行，并把商品添加进 products。
# 不合法价格：函数不应该添加商品，而是应该 raise ValueError。
# 所以这里不是 True / False 的区别，而是“正常修改状态”和“抛出异常”的区别。

# 可选练习：
# 给 test_total_price_with_many_cases() 再加一组数据：
# 两个商品价格分别是 0 和 10，预期结果是 10。

@pytest.mark.parametrize(
    'name, expected',
    [('goose', {'name': 'goose', 'price': 13}),
     ('fork', {'name': 'fork', 'price': 25})
     ],
    ids=['find_goose', 'find_fork']
)

def test_find_product_found(name, expected):
    products = make_products()
    result = day_44.find_product(products, name)
    assert result == expected
    assert products == make_products()

@pytest.mark.parametrize('name', ['no_exist_1', 'no_exist_2'], ids=['missing_1', 'missing_2'])
def test_find_product_not_found(name):
    products = make_products()
    with pytest.raises(ValueError):
        day_44.find_product(products, name)
    
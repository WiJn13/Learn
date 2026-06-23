# TITLE: Python 工程化入门：测试数据复用与 fixture 思维
# CATEGORY: 测试与代码验证
# day_47.py


# 今日判断：
# day_45 你已经练过 assert、pytest.raises(ValueError) 和测试场景拆分。
# day_46 你已经练过 pytest.mark.parametrize，并开始给 find_product()
# 写“商品存在”和“商品不存在”的多组测试。
#
# 当前状态：可以继续推进。
# 今天不急着增加新的业务函数。
# 今天重点练一个工程化能力：
# 当多个测试都需要同一批准备数据时，如何把“准备数据”抽出来复用。


# 今日目标：
# 1. 理解 fixture 解决的不是“计算问题”，而是“测试准备数据重复”的问题
# 2. 区分 make_products() 和 pytest fixture 的角色
# 3. 学会判断哪些数据适合复用，哪些数据应该留在测试内部
# 4. 继续巩固：一个测试只验证一个明确行为


# Part 1：先看问题
# 你现在的 test_day_46.py 里，很多测试都需要 products：
#
# - total_price() 需要 products
# - count_products() 需要 products
# - find_product() 需要 products
# - add_product() 有时需要空列表，有时需要已有商品列表
#
# 如果每个测试都自己写一遍 products，代码会变重复。
# 如果所有测试都共用同一个可变列表，又容易互相影响。
#
# fixture 的核心目的：
# 给每个测试准备一份“干净的初始数据”。


# Part 2：今天你要做什么
# 新建或继续使用一个测试文件：
#
#     Learn/test_day_47.py
#
# 在这个文件里完成下面任务。
# 先不要改 day_44.py。


# 任务 1：创建 products fixture
# 要求：
# 1. import pytest
# 2. import day_44
# 3. 写一个 fixture，名字叫 products
# 4. 这个 fixture 返回三件商品：
#    - egg，价格 1
#    - chicken，价格 23
#    - fork，价格 12
# 5. 每个测试通过参数名 products 使用这份数据
#
# 注意：
# fixture 本质上还是一个函数。
# 不同点是 pytest 会在运行测试时自动调用它。
import pytest
import day_44
@pytest.fixture
def products():
    return [{'name': 'egg', 'price': 1}, {'name': 'chicken', 'price': 23}, {'name': 'fork', 'price': 12}]
expected_products = [{'name': 'egg', 'price': 1}, {'name': 'chicken', 'price': 23}, {'name': 'fork', 'price': 12}]

# 任务 2：用 fixture 重写 find_product 存在场景
# 目标：
# 测试 day_44.find_product(products, name) 找得到商品时能返回正确商品。
#
# 要求：
# 1. 使用 pytest.mark.parametrize
# 2. 参数包含 name 和 expected
# 3. 至少准备两组数据，这里按你自己的商品来：
#    - egg 对应 {"name": "egg", "price": 1}
#    - chicken 对应 {"name": "chicken", "price": 23}
#    - fork 对应 {"name": "fork", "price": 12}
# 4. 测试函数的参数里同时接收 products、name、expected
# 5. 断言 result == expected
# 6. 额外断言 products 没有被修改
@pytest.mark.parametrize(
    'name, expected',
    [('egg', {'name': 'egg', 'price': 1}),
     ('chicken', {'name': 'chicken', 'price': 23}),
     ('fork', {'name': 'fork', 'price': 12})
     ]
)
def test_find_product_found(products, name, expected):
    result = day_44.find_product(products, name)
    assert result == expected
    assert products == expected_products

# 任务 3：用 fixture 重写 find_product 不存在场景
# 目标：
# 测试 day_44.find_product(products, name) 找不到商品时会 raise ValueError。
#
# 要求：
# 1. 使用 pytest.mark.parametrize
# 2. 至少准备两个不存在的商品名
# 3. 使用 pytest.raises(ValueError)
# 4. 额外断言 products 没有被修改
@pytest.mark.parametrize(
    'name', ['no_exist_1', 'no_exist_2'], ids = ['1', '2']
)
def test_find_product_no_found(products, name):
    with pytest.raises(ValueError):
        day_44.find_product(products, name)
    assert products == expected_products

# 任务 4：继续主线，给 total_price() 写一个使用 fixture 的测试
# 目标：
# 测试 day_44.total_price(products) 能正确计算当前这组三个商品的总价。
#
# 要求：
# 1. 测试函数通过参数名 products 使用 fixture
# 2. 调用 day_44.total_price(products)
# 3. 用 assert 判断结果是否等于 36
# 4. 额外断言 products 没有被修改
#
# 注意：
# 这一步练的是“fixture 复用同一批测试数据”。
# 不需要使用 parametrize，因为这里只验证一组固定商品的总价。
def test_total_price(products):
    result = day_44.total_price(products)
    assert result == 36
    assert products == expected_products
# 任务 5：判断哪些测试不适合直接用同一个 products fixture
# 先在对话里回答，不急着写代码：
#
# 1. add_product(products, name, price) 的合法添加测试，适合用已有 products fixture 吗？
# 我的回答：如果从已有列表添加，适合；如果要测试从空列表添加，不适合
#
# 2. 如果一个测试需要空列表 products = []，它还应该强行使用这个 fixture 吗？
# 我的回答：不
#
# 3. fixture 每次返回一份新列表，主要是为了避免什么问题？
# 我的回答：避免重复打字，也避免污染其他测试的列表


# 任务 6：给 count_products() 写一个使用 fixture 的测试
# 目标：
# 测试 day_44.count_products(products) 能正确统计当前这组三个商品的数量。
#
# 要求：
# 1. 测试函数通过参数名 products 使用 fixture
# 2. 调用 day_44.count_products(products)
# 3. 用 assert 判断结果是否等于 3
# 4. 额外断言 products 没有被修改
#
# 注意：
# 这一步和 total_price() 类似。
# 不需要使用 parametrize，因为这里只验证一组固定商品的数量。
def test_count_products(products):
    result = day_44.count_products(products)
    assert result == 3
    assert products == expected_products
# 完成标准：
# 1. Learn/test_day_47.py 存在
# 2. 有一个 products fixture
# 3. find_product 的“存在场景”使用 fixture + parametrize
# 4. find_product 的“不存在场景”使用 fixture + parametrize + pytest.raises
# 5. total_price 的测试使用 fixture
# 6. count_products 的测试使用 fixture
# 7. 每个测试都能说明自己在验证哪一种行为
#
# 运行检查：
#     python3 -m pytest Learn/test_day_47.py -q
#
# 如果本机提示 No module named pytest，先不要安装。
# 把报错贴出来，我们再处理环境问题。


# 可选挑战：
# 1. 思考：为什么 add_product() 的某些测试反而更适合在函数内部创建空列表



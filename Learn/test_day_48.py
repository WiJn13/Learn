# TITLE: Python 工程化入门：测试会修改数据的函数
# CATEGORY: 测试与代码验证
# day_48.py


# 今日判断：
# day_47 你已经练过 pytest fixture。
# 你现在能把一批测试准备数据抽出来复用，并且知道 fixture 每次给测试一份干净数据。
#
# 今天继续往前一点：
# 不只测试“返回值”，还要测试“函数有没有正确修改列表”。


# 今日目标：
# 1. 区分两类函数：
#    - 只读取数据并返回结果
#    - 会修改传入的数据
# 2. 学会测试 add_product() 这种会改变 products 的函数
# 3. 继续巩固：测试要看清楚“执行前、执行动作、执行后”
# 4. 暂时不修改 day_44.py


# Part 1：先判断函数类型
# 先不要写测试代码。
# 你先在对话里回答：
#
# 1. total_price(products) 会不会修改 products？
# 我的回答：不会
#
# 2. find_product(products, name) 会不会修改 products？
# 我的回答：不会
#
# 3. add_product(products, name, price) 会不会修改 products？
# 我的回答：会
#
# 4. remove_product(products, name) 会不会修改 products？
# 我的回答：会
#
# 5. clear_products(products) 会不会修改 products？
# 我的回答：会
#
# 6. update_product_price(products, name, new_price) 会不会修改 products？
# 我的回答：会


# Part 2：今天的核心读法
# 测试会修改数据的函数时，不只看 result。
#
# 你要按这个顺序想：
#
# 1. 执行前：products 原来是什么样
# 2. 执行动作：调用了哪个函数
# 3. 执行后：products 应该变成什么样
#
# 这类函数通常没有明显的返回值。
# 所以重点不是 assert result，而是检查 products 本身有没有变对。


# Part 3：第一个练习
# 目标：
# 给 day_44.add_product() 写一个“合法价格”的测试。
#
# 要求：
# 1. 在测试里准备一个空列表 products
# 2. 调用 add_product() 添加一个商品
# 3. 检查 products 里确实多了这个商品
# 4. 先只测一组数据，不急着用 parametrize
# 
# 注意：
# 这一步练的是“函数修改了传入的 list”。
# 不是练返回值。

# 完成标准：
# 1. 你能说清楚 add_product() 修改的是哪个对象
# 修改的是空列表的products
# 2. 你能说清楚为什么这里重点检查 products，而不是检查 result
# 又不是计算值
# 3. 你能写出一个最小测试，只验证“合法添加”这一种行为
import day_44
import pytest

@pytest.fixture
def products():
    return [{'name': 'fork', 'price': 23}, {'name': 'egg', 'price': 2}, {'name': 'carrot', 'price': 12}]

def test_add_product():
    products = []
    day_44.add_product(products, 'milk', 6)
    assert products == [{'name': 'milk', 'price': 6}]


# Part 4：第二个练习
# 目标：
# 给 day_44.add_product() 写一个“非法价格”的测试。
#
# 要求：
# 1. 在测试里准备一个空列表 products
# 2. 调用 add_product()，价格使用一个非法值，比如 -1
# 3. 检查它会抛出 ValueError
# 4. 额外检查 products 仍然是空列表，没有被修改
# 
# 注意：
# 这一步验证的是另一种行为：
# 非法价格时，函数不应该添加商品，而是应该拒绝这次操作。
def test_add_product_invalid_price():
    products = []
    with pytest.raises(ValueError):
        day_44.add_product(products, 'goose', -1)
    assert products == []


# Part 5：第三个练习
# 目标：
# 给 day_44.remove_product() 写一个“成功删除”的测试。
#
# 要求：
# 1. 在测试里准备一个有多个商品的 products
# 2. 调用 remove_product() 删除其中一个商品
# 3. 检查被删除的商品已经不在 products 里
# 4. 检查其他商品仍然保留
#
# 注意：
# 这一步继续练“执行前、执行动作、执行后”。
# remove_product() 的重点不是返回值，而是 products 这个 list 被正确修改。
def test_remove_product(products):
    day_44.remove_product(products, 'fork')
    assert products == [{'name': 'egg', 'price': 2}, {'name': 'carrot', 'price': 12}]


# Part 6：第四个练习
# 目标：
# 给 day_44.remove_product() 写一个“删除不存在商品”的测试。
#
# 要求：
# 1. 使用 products fixture 准备一份已有商品列表
# 2. 调用 remove_product() 删除一个不存在的商品名
# 3. 检查它会抛出 ValueError
# 4. 额外检查 products 没有被修改
#
# 注意：
# 这一步和 Part 5 是同一个函数的另一种行为：
# - Part 5：商品存在，应该成功删除
# - Part 6：商品不存在，应该拒绝删除并抛出异常
def test_remove_product_no_found(products):
    with pytest.raises(ValueError):
        day_44.remove_product(products, 'no_exist')
    assert products == [{'name': 'fork', 'price': 23}, {'name': 'egg', 'price': 2}, {'name': 'carrot', 'price': 12}]


# Part 7：第五个练习
# 目标：
# 给 day_44.clear_products() 写一个“清空商品列表”的测试。
#
# 要求：
# 1. 使用 products fixture 准备一份已有商品列表
# 2. 调用 clear_products(products)
# 3. 检查 products 变成空列表
#
# 注意：
# clear_products() 和 remove_product() 一样，重点不是返回值。
# 它验证的是：传入的那个 list 对象被清空了。
def test_clear_products(products):
    day_44.clear_products(products)
    assert products == []


# Part 8：第六个练习
# 目标：
# 给 day_44.update_product_price() 写一个“成功修改价格”的测试。
#
# 要求：
# 1. 使用 products fixture 准备一份已有商品列表
# 2. 选择其中一个已经存在的商品名
# 3. 调用 update_product_price()，把它改成一个合法的新价格
# 4. 检查目标商品的 price 已经变成新价格
# 5. 检查其他商品没有被改动
#
# 完成标准：
# 1. 你能确认只改了目标商品
# 2. 你能确认其他商品仍然保留原来的 name 和 price
# 3. 当前文件里的测试继续全部通过
#
# 可选挑战：
# - 不只检查整个 products 列表，也尝试说明为什么这样能证明“只修改了目标商品”。
def test_update_product_price(products):
    day_44.update_product_price(products, 'fork', 20)
    assert products[0]['price'] == 20
    assert products == [{'name': 'fork', 'price': 20}, {'name': 'egg', 'price':2}, {'name': 'carrot', 'price': 12}]


# Part 9：第七个练习
# 目标：
# 给 day_44.update_product_price() 写一个“商品不存在”的测试。
#
# 要求：
# 1. 使用 products fixture 准备一份已有商品列表
# 2. 调用 update_product_price()，传入一个不存在的商品名
# 3. 检查它会抛出 ValueError
# 4. 额外检查 products 没有被修改
#
# 完成标准：
# 1. 你能确认不存在的商品不会被“新增”
# 2. 你能确认原来的三个商品仍然保持原样
# 3. 当前文件里的测试继续全部通过
#
# 可选挑战：
# - 思考：这个测试和 Part 6 的结构有什么相同点？
def test_update_product_price_no_product(products):
    with pytest.raises(ValueError):
        day_44.update_product_price(products, 'no_exist', 0)
    assert products == [{'name': 'fork', 'price': 23}, {'name': 'egg', 'price':2}, {'name': 'carrot', 'price': 12}]


# Part 10：第八个练习
# 目标：
# 练习测试里“原始数据”和“期望结果”不能指向同一个 list。
#
# 要求：
# 1. 准备一份 products 列表
# 2. 再准备一份 expected 列表，用来表示函数执行后的期望结果
# 3. 调用一个会修改 products 的函数
# 4. 检查 products 是否等于 expected
# 5. 注意：expected 必须是另一份独立的 list，不能直接等于 products 本身
#
# 注意：
# 这一步不是为了多测一个新函数。
# 它练的是一个测试思维：
# 如果 expected 和 products 指向同一个 list，那么 products 一变，expected 也会一起变。
# 这种测试可能看起来通过了，但其实没有真正验证行为。
#
# 完成标准：
# 1. 你能说清楚 products 和 expected 为什么要分开准备
# 2. 你能说清楚“同一个对象”和“内容相等”不是一回事
# 3. 当前文件里的测试继续全部通过
#
# 可选挑战：
# - 写完后，用自己的话解释：为什么不能先写 expected = products 再去调用会修改 products 的函数？
# 这样子的话，修改了products也会修改expected,必须给expected单独手打一个确定的固定的列表
# 临时测试文件：验证 import _47_product_manager 时不会自动执行 _47_product_manager.main()

import _47_product_manager
def assert_raise_value_error(func):
    try:
        func()
        assert False, 'ValueError was not raised'
    except ValueError:
        pass

def test_add_product():
    products = []
    _47_product_manager.add_product(products, "apple", 6)
    _47_product_manager.add_product(products, "milk", 9)
    assert products == [
        {'name': 'apple', 'price': 6}, 
        {'name': 'milk', 'price': 9}
    ]
    result = _47_product_manager.total_price(products)
    assert result == 15, 'total price should be 15'

def test_invalid_price():
    products = []
    def bad_add_product():
        _47_product_manager.add_product(products, 'egg', -1)
    assert_raise_value_error(bad_add_product)

def test_remove_product():
    products = [
        {'name': 'fork', 'price': 14},
        {'name': 'goose', 'price': 26}
    ]
    _47_product_manager.remove_product(products, 'fork')
    assert products == [
        {'name': 'goose', 'price': 26}
    ]
    result = _47_product_manager.total_price(products)
    assert result == 26, 'result should be 26'

    def bad_remove_product(): 
        _47_product_manager.remove_product(products, 'no_exist')
    assert_raise_value_error(bad_remove_product)


def test_clear_products():
    products = [
        {'name': 'fork', 'price': 14},
        {'name': 'goose', 'price': 26}
    ]
    _47_product_manager.clear_products(products)
    assert products == [], 'products should be []'

def test_update_product_price():
    products = [
        {'name': 'fork', 'price': 14},
        {'name': 'goose', 'price': 26}
    ]
    _47_product_manager.update_product_price(products, 'fork', 22)
    assert products == [
        {'name': 'fork', 'price': 22},
        {'name': 'goose', 'price': 26}
    ]

    result = _47_product_manager.total_price(products)
    assert result == 48, 'total price should be 48'

    def bad_update_product_price():
        _47_product_manager.update_product_price(products, 'no_exist', 16)
        _47_product_manager.update_product_price(products, 'goose', -1)
    assert_raise_value_error(bad_update_product_price)  # 错误，不同的测试要分开写，第一行商品不存在已经raise ValueError，函数中断，不会执行第二行


def test_count_products():
    products = [
        {'name': 'fork', 'price': 14},
        {'name': 'goose', 'price': 26}
    ]
    result = _47_product_manager.count_products(products)
    assert result == 2

def test_find_product():
    products = [
        {'name': 'fork', 'price': 14},
        {'name': 'goose', 'price': 26}
    ]
    result = _47_product_manager.find_product(products, 'fork')
    assert result == {'name': 'fork', 'price': 14}, '应该返回的是字典'
    assert products == [
        {'name': 'fork', 'price': 14},
        {'name': 'goose', 'price': 26}
    ], '列表不应该被更改'
    def bad_find_product():
        _47_product_manager.find_product(products, 'egg')
    assert_raise_value_error(bad_find_product)

if __name__ == '__main__':
    test_add_product()
    test_invalid_price()
    test_remove_product()
    test_clear_products()
    test_update_product_price()
    test_count_products()
    test_find_product()
    print('test pass')
print(_47_product_manager.__name__)
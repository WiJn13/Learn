# TITLE: 使用 unittest 测试预期异常
# CATEGORY: 标准库、异常与测试
# _61_unittest_exceptions.py


# ========================
# Part 1：验证不存在的商品会抛出 ValueError
# ========================
# 目标：
# - 学习使用 unittest.TestCase 的 assertRaises() 检查预期异常。
# - 将 _57_safe_product_deletion 中 delete_product() 的 ValueError 规则变成可自动运行的测试。
#
# 要求：
# - 导入 unittest。
# - 从 _57_safe_product_deletion 导入 delete_product()；不调用 _57_safe_product_deletion.main()。
# - 建立一个继承 unittest.TestCase 的测试类，类名由你自己设计。
# - 在 setUp() 中为每项测试准备一份合法的商品列表，保存为测试对象的属性。
# - 增加一个以 test_ 开头的测试方法，使用一个列表中不存在的商品名称。
# - 使用 with self.assertRaises(ValueError) 监视 delete_product() 的调用。
# - 在文件末尾加入 unittest 的直接运行入口。
# - 本阶段只使用内存数据，不读写 aa、bb、cc、dd 或其他 JSON 文件。
#
# 完成标准：
# - 直接运行 _61_unittest_exceptions.py 时，unittest 报告运行了 1 项测试并显示 OK。
# - 你能说明：这项测试通过不是因为 delete_product() 正常返回，而是因为它按预期抛出了 ValueError。
# - 你能说明：如果 delete_product() 没有抛出 ValueError，这项测试反而会失败。
#
# 可选挑战：
# - 在动手前预测：如果把不存在的名称换成真实存在的名称，assertRaises() 会通过还是失败？
# ========================
import unittest
from _57_safe_product_deletion import delete_product

class DelTest(unittest.TestCase):
    def setUp(self):
        self.products = [{'name': 'jacke', 'price': 24},
                         {'name': 'milk', 'price': 26},
                         {'name': 'chocolate', 'price': 21}]

    def test_none(self):
        with self.assertRaises(ValueError) as caught:
            delete_product(self.products, 'none')
        message = str(caught.exception)
        self.assertEqual(message, '未找到商品')
if __name__ == '__main__':
    unittest.main()





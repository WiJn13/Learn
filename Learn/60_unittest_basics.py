# TITLE: 使用 unittest 组织自动测试
# CATEGORY: 标准库、测试类与测试方法
# 60_unittest_basics.py


# ========================
# Part 1：认识 unittest 的测试类
# ========================
# 目标：
# - 把 59_confirmation_test_runner 的手写 assert 测试，交给 Python 标准库 unittest 统一发现和运行。
# - 理解：测试类用于归类测试；测试方法用于描述并验证一种具体行为。
#
# 要求：
# - 从 59_confirmation_test_runner 复用 ask_confirmation()；本阶段仍不使用真实 input()，也不读写商品文件。
# - 导入 unittest。它是 Python 自带的标准库，不需要安装。
# - 新建一个测试类，让它继承 unittest.TestCase。
# - 类名自行命名，但应能表达它测试的是确认流程；类名使用 PascalCase（每个英文单词首字母大写）。
# - 在类中建立第一个测试方法，方法名必须以 test_ 开头。
# - 用局部 answers 列表和一个局部假输入函数，测试输入 y 时 ask_confirmation() 返回 True。
# - 使用测试对象提供的相等检查方法判断实际结果与预期结果；不要继续使用普通 assert。
# - 文件末尾加入 unittest 的测试运行入口，使直接运行 60_unittest_basics.py 时可以执行测试。
# ========================


# ========================
# Part 2：添加更多测试方法（测试 n 的情况）
# ========================
# 目标：
# - 在 AskTest 类中增加第二个测试方法，验证输入 n 或 no 时返回 False。
# - 理解：同一个测试类可以容纳多个测试方法，每个测试方法独立运行，互不干扰。
#
# 要求：
# - 在 AskTest 类中新增一个方法，方法名依然必须以 test_ 开头（例如 test_n）。
# - 准备模拟输入为 'n' 或 'no' 的假输入函数。
# - 调用 ask_confirmation()，将返回值保存在 result 中。
# - 使用 self.assertEqual() 检查 result 是否等于 False，并附带失败提示信息。
#
# 完成标准：
# - 直接运行 60_unittest_basics.py 时，unittest 报告运行了 2 项测试并显示 OK。
# - 你能说明为什么新增测试方法不需要修改主程序函数 ask_confirmation()。
# ========================


# ========================
# Part 3：使用 setUp() 方法准备测试前置数据
# ========================
# 目标：
# - 学习并使用 unittest.TestCase 自带的特殊方法 setUp()，在每个测试方法运行前自动执行，减少重复代码。
# - 理解：测试前置方法（Fixture）的作用与执行时机。
#
# 要求：
# - 在 AskTest 类中定义一个名为 setUp(self) 的方法。
# - 将公共的 target 数据（如商品列表）初始化为 self.target 属性。
# - 修改 test_y 和 test_n，使其通过 self.target 访问测试对象。
#
# 完成标准：
# - 直接运行 60_unittest_basics.py 时，unittest 报告运行了 2 项测试并显示 OK。
# - 你能说明 setUp() 是在什么时候被调用的，以及它为什么能避免代码重复。
# ========================


import unittest
def ask_confirmation(target, max_attempts=3, input_func=input):
    attempts = max_attempts

    for _ in range(max_attempts):
        ans = input_func(f'确定删除{target}吗？"y"确定 / "n"取消：')
        ans = ans.lower().strip()
        if ans == 'y' or ans == 'yes':
            print('已确认删除')
            return True
        if ans == 'n' or ans == 'no':
            print('已取消删除')
            return False
        print(f'非法输入，{attempts}次后自动取消')
    print('已自动取消删除')
    return False



class AskTest(unittest.TestCase):

    def setUp(self):
        self.target = [{'name': 'gemini', 'price': 120}, {'name': 'gpt', 'price': 140}]

    def test_y(self):
        answers = ['yEs', 'no']
        def input_y(prompt):
            return answers.pop(0)
        result = ask_confirmation(self.target, 3, input_y)
        self.assertEqual(result, True)

    def test_n(self):
        answers = ['n', 'No']
        def input_n(prompt):
            return answers.pop(0)
        result = ask_confirmation(self.target, 3, input_n)
        self.assertEqual(result, False, '输入n时应取消，当前未正常触发')

    def test_invalid_then_y(self):
        answers = ['无效', 'y']
        def input_invalid_then_y(prompt):
            return answers.pop(0)
        result = ask_confirmation(self.target, 3, input_invalid_then_y)
        self.assertEqual(result , True)
        self.assertEqual(answers, [])

    def test_all_invalid(self):
        answers = ['无效', '还是无效', '仍然无效', '依旧无效']
        def input_all_invalid(prompt):
            return answers.pop(0)
        result = ask_confirmation(self.target, 4, input_all_invalid)
        self.assertEqual(result, False)
        self.assertEqual(answers, [])
if __name__ == '__main__':
    unittest.main()


# ========================
# Part 4：用测试暴露无效输入后的重试问题
# ========================
# 目标：
# - 把 58_testable_confirmation、59_confirmation_test_runner 已经测试过的“先无效、后确认”场景迁移到 unittest。
# - 理解：测试不只是证明代码正确，也能暴露实际运行流程与预期不一致的位置。
#
# 要求：
# - 在 AskTest 类中增加第三个以 test_ 开头的测试方法。
# - 为这项测试准备独立的 answers 列表：第一个回答无效，第二个回答表示确认。
# - 定义局部假输入函数，每次调用都从 answers 取出一个回答。
# - 使用 self.target，并允许 ask_confirmation() 最多尝试 2 次。
# - 使用 self.assertEqual() 检查返回值是否为 True。
# - 再检查 answers 是否已经变成空列表，确认两个回答都确实被读取。
# - 首次运行时不要修改 ask_confirmation()；先观察测试报告。
#
# 完成标准：
# - unittest 能发现并运行 3 项测试。
# - 你能从失败报告中找到“实际返回值”和“预期返回值”。
# - 你能通过 answers 剩余内容，判断第二个回答是否被读取。
#
# 可选挑战：
# - 先不改代码，用自己的话说出 input_func() 实际被调用了几次。
# ========================


# ========================
# Part 5：测试尝试次数耗尽后自动取消
# ========================
# 目标：
# - 验证所有回答都无效时，ask_confirmation() 会在达到最大尝试次数后返回 False。
# - 区分“用户输入 n 主动取消”和“无效输入耗尽后自动取消”两条不同路径。
#
# 要求：
# - 在 AskTest 类中增加第四个以 test_ 开头的测试方法。
# - 为这项测试准备独立的 answers 列表，其中包含 3 个无效回答。
# - 定义局部假输入函数，每次调用都从 answers 取出一个回答。
# - 使用 self.target，并把最大尝试次数设为 3。
# - 使用 self.assertEqual() 检查返回值是否为 False。
# - 再检查 answers 是否已经变成空列表，确认 3 次回答都被读取。
# - 本阶段不修改 ask_confirmation()。
#
# 完成标准：
# - unittest 能发现并运行 4 项测试，并显示 OK。
# - 你能说明这项测试为什么预期 False，以及它和 test_n 验证的路径有什么不同。
#
# 可选挑战：
# - 不改测试逻辑，先用自己的话预测 input_func() 在这项测试中会被调用几次。
# ========================


# ========================
# Part 6：为断言增加失败提示
# ========================
# 目标：
# - 补全 Part 2 中“附带失败提示信息”的要求。
# - 理解 self.assertEqual() 的第三个参数只在断言失败时帮助说明场景。
#
# 要求：
# - 找到 test_n 中检查 result 的 self.assertEqual()。
# - 在实际值和预期值之后，增加第三个字符串参数。
# - 提示文字由你自己设计，应能说明“输入 n 时应取消”这个预期行为。
# - 先在预期值正确时运行测试，观察提示文字是否显示。
# - 再临时把这一处预期值改错，运行并在失败报告中找到自己写的提示。
# - 观察完后立即恢复正确的预期值，再确认 4 项测试全部通过。
#
# 完成标准：
# - 预期值正确时，测试显示 OK，自定义失败提示不显示。
# - 预期值临时写错时，对应测试失败，报告中显示自己写的提示。
# - 最终恢复正确预期值，4 项测试全部通过。
#
# 可选挑战：
# - 选择一项 answers 列表检查，也为它增加一条能说明测试意图的失败提示。
# ========================

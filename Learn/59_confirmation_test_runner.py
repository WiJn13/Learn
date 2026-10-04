# TITLE: 集中运行自动测试
# CATEGORY: 函数组织、测试入口与可读性
# 59_confirmation_test_runner.py


# ========================
# Part 1：建立统一测试入口
# ========================
# 目标：
# - 把 58_testable_confirmation 中分散的确认测试集中到一个测试入口中执行。
# - 理解：测试函数负责验证；测试入口负责按顺序调用测试并报告整体结果。
#
# 要求：
# - 从 58_testable_confirmation 复用 ask_confirmation()，以及已经完成的三个测试场景：确认、取消、无效后确认、次数耗尽。
# - 为每个测试场景保留独立的测试函数；每个函数只验证一种行为。
# - 新建 run_tests()：按顺序调用所有测试函数。
# - 只有所有 assert 都通过后，run_tests() 才打印“全部测试通过”。
# - 如果任何 assert 失败，Python 应立刻抛出 AssertionError；不要仍然打印“全部测试通过”。
# - 本阶段不使用真实 input()，不读写 aa、bb、cc、dd 等商品文件。

def ask_confirmation(target, max_attempts=3, input_func=input):
    attempts = max_attempts
    for _ in range(max_attempts):
        ans = input_func(f'是否确认取消删除{target}? "y"确定 / "n"取消:')
        ans = ans.lower().strip()
        if ans == 'y' or ans == 'yes':
            print('已确认删除')
            return True
        elif ans == 'n' or ans == 'no':
            print('已确认取消删除')
            return False
        print(f'无效输入，将在{max_attempts}次错误后自动取消删除。')
        max_attempts = max_attempts - 1
    print(f'{attempts}次无效输入，已自动取消删除。')
    return False



target = {'name': 'grok', 'price': 64}
def test_ask_1():
    answers = ['y', 'n']
    def test_y(prompt):
        return answers.pop(0)
    result = ask_confirmation(target, 2, test_y)
    assert result == True
    assert answers == ['n']

def test_ask_2():
    answers = ['No', 'Yes']
    def test_n(prompt):
        return answers.pop(0)
    result = ask_confirmation(target, 2, test_n)
    assert result == False
    assert answers == ['Yes']

def test_ask_3():
    answers = ['无效输入', 'y']
    def test_bia(prompt):
        return answers.pop(0)
    result = ask_confirmation(target, 2, test_bia)
    assert result == True
    assert answers == []

def test_ask_4():
    answers = ['无效输入', 'y']
    def test_bia(prompt):
        return answers.pop(0)
    result = ask_confirmation(target, 1, test_bia)
    assert result == False
    assert answers == ['y']

def test_ask_5():
    answers = ['无', '效', '输', '入']
    def test_e(prompt):
        return answers.pop(0)
    result = ask_confirmation(target, 4, test_e)
    assert result == False
    assert answers == []

def run_test():
    test_ask_1()
    test_ask_2()
    test_ask_3()
    test_ask_4()
    test_ask_5()
    print('---全部测试通过---')

def main():
    run_test()
if __name__ == '__main__':
    main()

# 完成标准：
# - 运行 59_confirmation_test_runner.py 时，四种测试场景都会被执行。
# - 所有预期正确时，最后只出现一次“全部测试通过”。
# - 故意把任意一个预期结果写错时，程序在该 assert 处停止，且不打印成功提示。
# - 每个需要多次回答的测试都有自己的局部 answers 列表，重复运行也不会受上次影响。
#
# 可选挑战：
# - 为每个测试函数增加一条简短的测试名称输出，方便判断运行到了哪一项。
# ========================

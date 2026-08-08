# TITLE: 让交互式函数可以自动测试
# CATEGORY: 函数参数、输入来源与可测试性
# day_53.py


# ========================
# Part 1：把输入来源交给参数
# ========================
# 目标：
# - 在不改变 Day 52 确认规则的前提下，让 ask_confirmation() 不再只能使用真正的键盘输入。
# - 理解：函数除了接收普通数据，也可以接收另一个可调用的函数。
#
# 要求：
# - 参考 Day 52 的 ask_confirmation()，在 Day 53 中重新写出这个函数。
# - 保留 target 和 max_attempts 参数以及原来的确认、取消、重试规则。
# - 新增 input_func 参数，默认使用 Python 内置的 input。
# - input_func 是程序员自行设计的参数名：input 表示“输入”，func 是 function 的缩写。
# - 循环中通过 input_func 获取回答，不再把输入来源固定为 input()。
# - 本阶段不要读写 cc、dd，也不要编写商品删除流程。
#
# 完成标准：
# - 不传 input_func 时，函数仍然可以像 Day 52 一样等待键盘输入。
# - 传入另一个可调用对象时，函数会从它获得字符串，不要求用户真的敲键盘。
# - y、yes、n、no、无效重试和次数耗尽的行为都保持不变。
# - 你能说明 input_func 保存的不是输入结果，而是“稍后可以调用的函数”。
#
# 可选挑战：
# - 让次数耗尽后的提示使用实际的 max_attempts，而不是固定写“三次”。
# ========================
import json
def load_products(filename):
    try: 
        with open(filename, 'r') as f:
            a = json.load(f)
        if check(a):
            return a
        else:
            raise ValueError('商品格式错误')
    except FileNotFoundError:
        print('文件不存在，已自动创建空列表')
        return []

def check(products):
    if type(products) == list:
        for product in products:
            if type(product) == dict and 'name' in product and 'price' in product and type(product['name']) == str and isinstance(product['price'], (int, float)) and product['price'] >= 0 and type(product['price']) != bool:
                pass
            else: 
                return False
        return True
    else:
        return False

def save_products(products, filename):
    if check(products):
        with open(filename, 'w') as f:
            json.dump(products, f)
    else:
        raise ValueError('商品格式错误，无法保存')
    
def delete_product(products, name):
    if check(products):
        for i in products:
            if i['name'] == name:
                products.remove(i)
                return i
        else:
            raise ValueError('未找到商品')      
    else:
        raise ValueError('商品列表不合法')

def find_product(products, name):
    if check(products):
        for i in products:
            if i['name'] == name:
                return i
        else:
            raise ValueError('商品不存在')
    else:
        raise ValueError('商品不合法')


def ask_confirmation(target, max_attempts=3, input_func = input):
    for _ in range(max_attempts):

        ans = input_func(f'是否删除{target},按"y"删除，按"n"取消。')
        ans = ans.strip().lower()
        if ans == 'y' or ans == 'yes':
            
            return True
        if ans == 'n' or ans == 'no':
            return False
        print('非法输入')
    print(f'{max_attempts}次非法输入，已取消删除。')
    return False

def fake_y(prompt):
    return 'y'

def fake_n(prompt):
    return 'no'

answers = ['无效输入', 'n', 'y', 'no', 'yes', 'YEs', 'NO']
def fake_input(prompt):
    return answers.pop(0)

def test_attempts():
    answers = ['无效输入', 'y']
    def fake_input(prompt):
        return answers.pop(0)
    target = {'name': 'jack', 'price': 28}
    result_4 = ask_confirmation(
        target=target,
        input_func=fake_input
        )
    assert result_4 == True
    assert answers == []

def main():
    target = {'name': 'jack', 'price': 28}
    if target:
        result_1 = ask_confirmation(target, 4, fake_y)
        assert result_1 == True, 'fake_y分支出错'
        result_2 = ask_confirmation(
            target=target,
            input_func=fake_n
        )
        assert result_2 == False, 'fake_n分支出错'

        test_count = 7
        if 0 <= test_count <= len(answers):
            for _ in range(test_count):
                print(f'当前测试输入为：{answers[0]}')
                result_3 = ask_confirmation(target, 1, fake_input)
                if result_3:
                    print('执行状态：用户已确认删除')
                else:
                    print('执行状态：已取消删除')
                print(f'result_3返回结果为{result_3}')
                print(f'当前列表为{answers}')
                print('--- 测试结束--- \n')
        else:
            raise ValueError('测试数量不合法')
    a = test_attempts()
    print(a)


        
            

if __name__ == '__main__':
    main()



# ========================
# Part 2：用 assert 自动判断确认结果
# ========================
# 目标：
# - 让程序自动判断 ask_confirmation() 的返回值是否正确，不再只靠 print() 人工观察。
# - 理解：assert 检查的是一个条件，条件为 False 时会抛出 AssertionError。
#
# 要求：
# - 保留 Part 1 的 ask_confirmation()、fake_y() 和 fake_n()。
# - 使用 fake_y 作为 input_func，自动检查返回值是 True。
# - 使用 fake_n 作为 input_func，自动检查返回值是 False。
# - 比较返回值时使用 ==，不要把赋值符号 = 当作比较。
# - 两项检查都通过后，再打印一条“基础确认测试通过”的提示。
# - 本阶段不使用真实 input()，不测试 answers 列表和无效输入重试。
#
# 完成标准：
# - fake_y 测试通过时不抛出 AssertionError。
# - fake_n 测试通过时不抛出 AssertionError。
# - 任意一个预期结果写错时，程序能通过 AssertionError 报告测试失败。
# - 两项检查通过后，程序输出“基础确认测试通过”。
# - 能说明 print() 只显示结果，assert 会自动判断结果是否符合预期。
#
# 可选挑战：
# - 为 assert 增加失败提示，让报错时能看出是“确认分支”还是“取消分支”失败。
# ========================


# ========================
# Part 3：用独立回答列表测试重试流程
# ========================
# 目标：
# - 自动验证“第一次输入无效，第二次输入 y”时，ask_confirmation() 会重试并最终返回 True。
# - 理解：每个测试应该使用自己的回答列表，避免受全局 answers 已被修改的影响。
# - 学习在测试函数内定义一个小的假输入函数，让它访问当前测试的局部回答列表。
#
# 要求：
# - 新建一个只负责测试重试流程的函数。
# - 在这个测试函数内，创建一个局部回答列表：第一项是无效字符串，第二项是 y。
# - 在同一个测试函数内定义假输入函数：接收 prompt，每次从局部回答列表开头取出并返回一个字符串。
# - 只调用一次 ask_confirmation()，不传 max_attempts，使用默认值 3。
# - 通过关键字实参把当前测试的假输入函数交给 input_func。
# - 使用 assert 检查最终返值是 True。
# - 再使用 assert 检查局部回答列表已经变成空列表，证明两个回答都被取出。
# - 本测试不读写商品文件，不使用真实 input()，也不修改全局 answers。


# 完成标准：
# - 运行时先出现一次“非法输入”，然后测试正常通过。
# - ask_confirmation() 最终返回 True。
# - 局部回答列表最终是 []。
# - 重复调用整个测试函数时，每次都会重新创建自己的回答列表，不会因上一次列表已变空而失败。
# - 能说明：外层测试函数的局部变量，可以被其内部定义的假输入函数访问和修改。
#
# 可选挑战：
# - 再写一个独立测试，准备三个无效回答，检查次数耗尽后返回 False，并且局部回答列表被全部消耗。
# ========================

 

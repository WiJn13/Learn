# TITLE: 安全删除商品
# CATEGORY: 文件操作与数据安全
# day_52.py


# ========================
# Part 1：确认存在后再删除
# ========================
# 目标：
# - 完成商品数据的第三种修改：删除已有商品。
# - 理解：删除是不可逆操作之一，因此必须先确认目标存在，再改变内存列表，最后才保存。
#
# 要求：
# - 从 day_51.py 复用 load_products()、check() 和 save_products()。
# - 新建 delete_product(products, name)。
# - 先验证 products 整体符合既有规则；不符合时抛出 ValueError。
# - 按 name 找到商品；找不到时抛出 ValueError，原列表不变。
# - 找到时只删除这一件商品，并返回表示“已经删除”的状态。
# - 函数只修改内存列表，不负责读写文件。

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

def ask_confirmation(target, max_attempts = 3):
    for _ in range(max_attempts):
        answer = input(f'是否确认删除{target}？输入''y''确认，输入''n''取消。')
        ans = answer.strip().lower()
        if ans == 'y' or ans == 'yes':
            return True
        elif ans == 'n' or ans == 'no':
            return False
        print('输入无效')
    print('三次非法输入，已自动取消删除。')
    return False
    




# main() 流程：
# - 从 cc 读取商品列表。
# - 删除一件你自己选择的商品。
# - 只有删除成功时，才保存到新文件 dd。
# - 再读取 dd 并打印结果。

def main():
    c = load_products('cc')
    target = find_product(c, 'jack')
    if target:
        result = ask_confirmation(target)
        if result:
            print(f'准备删除{target}...')
            success = delete_product(c, 'jack')
            if success:
                save_products(c, 'dd')
                d = load_products('dd')
                print(f'已删除{target}...\n当前列表为：{d}。')
        else:
            print('已取消删除')




if __name__ == '__main__':
    main()
# 完成标准：
# - cc 的内容保持不变，dd 中少了被删除的商品。
# - 删除不存在的商品时抛出 ValueError，内存列表和 dd 文件都不改变。
# - 你能说明为什么不能“先保存、再尝试删除”。
#
# 可选挑战：
# - 删除前打印将要删除的商品名称与价格，确认后再调用删除函数。
# ========================


# ========================
# Part 2：返回被删除的商品
# ========================
# 目标：
# - 让 delete_product() 不只告诉 main()“删没删”，还把被删除的商品数据交回去。
# - 理解：返回值可以是 bool，也可以是一个有用的数据对象。
#
# 要求：
# - 保留 Part 1 的查找、删除和 ValueError 行为。
# - 找到目标商品时，先保留这件商品的数据，再从 products 中删除它。
# - 删除成功后，返回这件商品的 dict，而不是 True。
# - 找不到商品时仍然抛出 ValueError。
# - main() 接收返回的商品数据，打印“已删除的商品”，再保存到 dd。
#
# 完成标准：
# - delete_product() 成功时返回包含 name 和 price 的 dict。
# - 返回的商品正是从 products 中移除的那一件。
# - main() 既能打印被删除的商品，也只在删除成功后保存。
#
# 可选挑战：
# - 打印时只显示商品的 name 和 price，不直接打印整个 dict。
# ========================


# ========================
# Part 3：删除前先预览目标
# ========================
# 目标：
# - 把“查找”和“删除”分成两个清楚的步骤，减少误删风险。
# - 理解：查询函数只返回数据，不修改列表；删除函数才负责修改。
#
# 要求：
# - 新建 find_product(products, name)。
# - products 不合法或找不到商品时，抛出 ValueError。
# - 找到时返回对应的商品 dict，不修改 products。
# - main() 先调用 find_product()，打印准备删除的商品信息，再调用 delete_product()。
# - 只有 delete_product() 成功后，才保存到 dd。
#
# 完成标准：
# - 查询成功前后，products 列表完全不变。
# - 输出中先出现“准备删除”的商品，再出现“已删除”的商品。
# - 查找不存在的商品时，删除函数和保存函数都不会执行。
#
# 可选挑战：
# - 将“准备删除”和“已删除”的打印写得更清楚，分别显示 name 与 price。
# ========================


# ========================
# Part 4：确认后才删除
# ========================
# 目标：
# - 在真正修改数据前，让用户决定是否继续，模拟实际程序中的防误删流程。
# - 理解：预览、确认、修改、保存是四个不同步骤。
#
# 要求：
# - 保留 Part 3 先查找并打印“准备删除”的流程。
# - 使用 input() 询问用户是否确认删除；提示中明确告诉用户输入 y 才确认。
# - 只有输入 y 时，才调用 delete_product() 和 save_products()。
# - 输入任何其他内容时，打印“已取消删除”，并且不修改列表、不保存 dd。
# - 找不到商品时，仍然先抛出 ValueError，不进入确认步骤。
#
# 完成标准：
# - 输入 y：商品被删除，dd 被写入新列表。
# - 输入 n 或其他文字：商品未删除，dd 不被改动。
# - 你能区分“用户取消”和“商品不存在”这两种不同结果。
#
# 可选挑战：
# - 同时接受 Y 和 y 作为确认输入。
# ========================


# ========================
# Part 5：标准化确认输入
# ========================
# 目标：
# - 让确认判断能接受大小写不同、前后带空格的输入。
# - 理解：用户输入先是原始字符串，判断前常需要先清理和统一格式。
#
# 要求：
# - 新建 is_confirmed(answer)，只负责判断输入是否表示确认，不读取文件、不修改列表。
# - 在判断前去掉 answer 前后的空格，并把字母统一成小写。
# - 清理后的结果是 y 时返回 True；其他任何内容都返回 False。
# - main() 先接收 input() 的原始字符串，再调用 is_confirmed() 决定是否删除。
#
# 完成标准：
# - y、Y、` y ` 都会确认删除。
# - n、空字符串、其他文字都会取消删除。
# - 你能说清为什么不直接比较原始 input() 的结果。
#
# 可选挑战：
# - 让确认输入同时支持 yes 和 y。
# ========================


# ========================
# Part 6：无效输入可以重试
# ========================
# 目标：
# - 区分“明确取消”和“输入格式不正确”，让用户输错时可以重新输入。
# - 复习循环、计数和提前 return。
#
# 要求：
# - 新建 ask_confirmation(max_attempts=3)，由它负责询问用户并返回确认结果。
# - 每次输入后都先去掉首尾空格并统一成小写。
# - 输入 y 或 yes 时返回 True。
# - 输入 n 或 no 时返回 False，表示用户明确取消。
# - 输入其他内容时打印“输入无效”，然后重新询问。
# - 最多询问 max_attempts 次；次数用完仍无效时，打印提示并返回 False。
# - main() 使用 ask_confirmation() 的返回值决定是否删除和保存。
#
# 完成标准：
# - 第一次输入错误、第二次输入 y 时，程序能继续删除。
# - 输入 n 时立即取消，不再询问。
# - 连续三次输入无效内容时取消删除，列表和 dd 都不改变。
# - 循环不会无限运行。
#
# 可选挑战：
# - 在每次无效输入后，显示还剩多少次机会。
# ========================

# TITLE: 安全修改商品价格
# CATEGORY: 文件操作与数据安全
# day_51.py


# ========================
# Part 1：找到后再更新价格
# ========================
# 目标：
# - 在 Day 50 的安全新增基础上，安全地修改一件已经存在的商品。
# - 理解：更新不是新增；必须先找到目标商品，再验证新价格，最后才修改内存数据。
#
# 要求：
# - 从 day_50.py 复用 load_products()、check() 和 save_products()。
# - 新建 update_product_price(products, name, new_price)。
# - 先确认 products 整体符合既有规则；不符合时抛出 ValueError。
# - 按 name 找到对应商品；找不到时抛出 ValueError，不修改列表。
# - 新价格必须符合 Day 49 的规则：int 或 float、不是 bool、且不小于 0。
# - 新价格合法时才修改找到的那一件商品的 price。
# - 函数只修改内存列表，不负责写文件。

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


def update_product_price(products, name, new_price):
    if check(products):
        if isinstance(new_price, (int, float)) and type(new_price) != bool and new_price >= 0:
            for i in products:
                if i['name'] == name:
                    if i['price'] == new_price:
                        return False
                    else:
                        i['price'] = new_price
                        return True
            else:
                raise ValueError('未找到商品')
        else:
            raise ValueError('新价格错误')
    else:
        raise ValueError('原商品列表不合法')


# main() 流程：
# - 从 bb 读取 Day 50 保存的商品列表。
# - 将 nick 的价格修改为一个你自己选择的合法价格。
# - 保存到新文件 cc，不要覆盖 bb。
# - 再读取 cc 并打印结果。

def main():
    a = load_products('bb')
    new = update_product_price(a, 'nick', 23)
    if new:
        save_products(a, 'cc')
    else:
        pass
    c = load_products('cc')
    print(c)
if __name__ == '__main__':
    main()
# 完成标准：
# - bb 的内容保持不变，cc 中只有 nick 的价格被更新。
# - 找不到商品时抛出 ValueError，原列表不变。
# - new_price 为负数、字符串或 True 时抛出 ValueError，原列表不变。
# - 你能说清“先验证后修改”和“修改后统一保存”的作用。
#
# 可选挑战：
# - 如果新价格与旧价格相同，直接返回，不修改列表也不保存文件。
# ========================


# ========================
# Part 2：只在确实变化时保存
# ========================
# 目标：
# - 让 update_product_price() 把“本次是否真的修改了价格”告诉 main()。
# - 理解：函数的返回值不只可以返回数据，也可以返回操作是否发生的状态。
#
# 要求：
# - 保留 Part 1 对原列表、商品名称和新价格的所有校验。
# - 找到商品后，先比较它当前的 price 与 new_price。
# - 价格相同时：不修改字典，并返回一个表示“没有变化”的状态。
# - 价格不同时：更新 price，并返回一个表示“已经变化”的状态。
# - 找不到商品或新价格不合法时，仍然抛出 ValueError，不要用返回状态代替异常。
# - main() 根据这个返回状态决定是否调用 save_products()。
#
# 完成标准：
# - 新旧价格相同时，内存列表和 cc 文件都不改变。
# - 新旧价格不同时，内存列表更新，并且才保存到 cc。
# - 你能说明：为什么“没有变化”与“输入错误”要用不同方式表示。
#
# 可选挑战：
# - 在没有变化时打印一条提示，例如“价格没有变化，未保存文件”。
# ========================

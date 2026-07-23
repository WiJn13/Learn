# TITLE: 安全新增商品
# CATEGORY: 文件操作与数据安全
# day_50.py


# ========================
# Part 1：读取、修改、再保存
# ========================
# 目标：
# - 把 Day 49 已完成的“读取校验”和“保存校验”连成一次真实的数据更新。
# - 理解：程序要先把文件中的列表读进内存，修改这个列表，最后才保存回文件。
#
# 要求：
# - 从 day_49.py 复用已经验证过的 load_products()、check() 和 save_products()。
# - 新建 add_product(products, name, price)：在内存中的 products 列表新增一件商品。
# - 新增前先检查 name 和 price 是否符合 Day 49 的商品规则；不符合时抛出 ValueError。
# - 新增成功后，再由 main() 调用 save_products() 保存到另一个 JSON 文件。
# - 不要直接把新商品写进文件；先完成列表修改，再统一保存。
# - 价格 0 仍然是合法值，bool 不能当作价格。
#
# 完成标准：
# - 原 JSON 文件内容不变。
# - 程序读入商品列表后，成功新增一件合法商品。
# - 保存到新 JSON 文件后，再次读取能看到新增后的完整列表。
# - name 或 price 不合法时，程序抛出 ValueError，且目标文件不会被错误数据覆盖。
#
# 可选挑战：
# - 在新增前检查是否已有同名商品；若有，拒绝新增并说明原因。
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
    
def add_product(products, name, price):
    a = products.copy()
    if check(products):
        for i in a:
            if i['name'] == name:
                raise ValueError('已存在同名商品')
        a.append({'name': name, 'price': price})
    if check(a):
        products.append({'name': name, 'price': price})
    else:
        raise ValueError('商品错误')
    
def main():
    products = load_products('aa')
    add_product(products, 'nick', 0)
    save_products(products, 'bb')
    b = load_products('bb')
    print(b)
if __name__ == '__main__':
    main()

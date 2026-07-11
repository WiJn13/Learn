# TITLE: Python 工程化入门：JSON 文件持久化
# CATEGORY: 文件操作与数据保存
# day_48_2.py


# 今日判断：
# 前面你已经练过：
# - 把商品数据放在 products list 里
# - 用函数修改 products
# - 用 pytest 检查函数行为
#
# 现在进入新主题：
# 程序运行时的 list/dict 只存在于内存里。
# 如果希望程序关闭后数据还在，就需要把数据写入文件。


# 今日目标：
# 1. 区分“内存里的数据”和“文件里的数据”
# 2. 理解 JSON 适合保存 list / dict 这类结构化数据
# 3. 学会设计 save_products() / load_products() 这类函数的职责
# 4. 暂时先不急着写文件读写代码，先判断数据什么时候会丢失


# ========================
# Part 1：内存数据 vs 文件数据
# ========================
# 目标：
# 判断 products 数据在不同位置时，程序结束后会不会保留。
#
# 要求：
# 先不要写代码。
# 你在下面回答三个问题：
#
# 1. 如果只写 products = []，程序结束后 products 里的数据还在不在？
# 我的回答：不在了
# 标准答案：不在了。products 是内存里的变量，程序结束后这份内存数据会消失。
#
# 2. 如果把 products 写进 products.json 文件，程序结束后数据还在不在？
# 我的回答：在
# 标准答案：在。文件保存在磁盘/本地存储里，不依赖当前 Python 程序继续运行。
#
# 3. 为什么测试文件读写时，不应该直接使用真实的 products.json？
# 我的回答：不知道
# 标准答案：因为测试可能会覆盖、清空或写坏真实数据。测试文件读写应该使用临时文件，避免污染真实的 products.json。
#
# 完成标准：
# 1. 你能说清楚“变量”为什么不会长期保存数据
# 2. 你能说清楚“文件”为什么可以在程序结束后继续存在 # 保存在文件里，本地的存储位置上
# 3. 你能说清楚测试为什么要避免污染真实数据文件
#
# 可选挑战：
# - 想一想：如果 load_products() 读取的文件不存在，它应该返回空列表，还是直接报错？ # 报错
# 标准答案：两种都可以，取决于函数设计。商品程序第一次运行时，返回空列表更友好；如果文件是必须存在的配置文件，报错更合理。


# ========================
# Part 2：JSON 适合保存什么数据
# ========================
# 目标：
# 判断哪些 Python 数据适合直接保存成 JSON。
#
# 要求：
# 先不要写代码。
# 你在下面回答五个判断题：
#
# 1. list 适不适合保存成 JSON？
# 我的回答：适合
#
# 2. dict 适不适合保存成 JSON？
# 我的回答：适合
#
# 3. list 里面放 dict，例如 products = [{"name": "milk", "price": 6}]，适不适合保存成 JSON？
# 我的回答：适合
#
# 4. 函数本身，例如 add_product，适不适合保存成 JSON？
# 我的回答：不适合
#
# 5. 一个打开中的文件对象，适不适合保存成 JSON？
# 我的回答：不适合吧
#
# 完成标准：
# 1. 你能说清楚 JSON 主要保存的是“数据”，不是“行为”
# 2. 你能判断 list / dict / str / int / float / bool 这类常见数据能保存
# 3. 你能判断函数、文件对象这类运行时对象不适合直接保存
#
# 可选挑战：
# - 思考：products 里每个商品为什么用 dict 表示，而不是用一段普通字符串表示？
# 用dict可查询，而且贴了标签，，应该还有其他作用

# serise → serial → serialize / deserialize


# ========================
# Part 3：save_products() 和 load_products() 的职责
# ========================
# 目标：
# 判断“保存数据”和“读取数据”的函数应该负责什么，不应该负责什么。
#
# 要求：
# 先不要写代码。
# 你在下面回答四个问题：
#
# 1. save_products(products, filename) 应该负责添加商品吗？
# 我的回答：不应该。保存数据就是把这些商品数据保存，而不应该动里面的商品数据。
#
# 2. save_products(products, filename) 真正应该负责什么？
# 我的回答：读取已有的 products，把已有的商品数据保存到文件里。
#
# 3. load_products(filename) 应该偷偷创建一个默认商品吗？
# 我的回答：不可以。因为这样如果我不知道，我就以为这个 file 里面本来就有这个商品。
#
# 4. load_products(filename) 真正应该负责什么？
# 我的回答：读取已有的文件里面的商品，其他都不要动。
#
# 完成标准：
# 1. 你能说清楚 add_product() 和 save_products() 的职责区别
# 2. 你能说清楚 load_products() 不应该偷偷改变数据含义
# 3. 你能用自己的话解释“一个函数只负责一件清楚的事”
#
# 可选挑战：
# - 如果文件不存在，load_products() 应该返回空列表还是报错？请根据“商品程序第一次运行”的场景重新判断一次。


# ========================
# Part 4：json.dump 和 json.load 的方向
# ========================
# 目标：
# 先理解 JSON 读写的两个方向，不急着写完整函数。
#
# 要求：
# 先不要写代码。
# 你在下面回答四个判断题：
#
# 1. json.dump 是把 Python 数据写进 JSON 文件，还是从 JSON 文件读出 Python 数据？
# 我的回答：写进
#
# 2. json.load 是把 Python 数据写进 JSON 文件，还是从 JSON 文件读出 Python 数据？
# 我的回答：读取
#
# 3. save_products(products, filename) 里面更可能使用 dump 还是 load？
# 我的回答：dump
#
# 4. load_products(filename) 里面更可能使用 dump 还是 load？
# 我的回答：load
#
# 完成标准：
# 1. 你能区分 dump 是“写出去”
# 2. 你能区分 load 是“读回来”
# 3. 你能把 save_products / load_products 和 dump / load 对应起来
#
# 可选挑战：
# - 思考：dump 和 load 为什么都需要和文件对象配合使用？ # 因为要有一个可操作对象


# ========================
# Part 5：读文件模式和写文件模式
# ========================
# 目标：
# 理解保存 JSON 和读取 JSON 时，文件打开方式为什么不同。
#
# 要求：
# 先不要写代码。
# 你在下面回答四个判断题：
#
# 1. 保存 products 到 JSON 文件时，应该更像“读文件”还是“写文件”？
# 我的回答：写
#
# 2. 从 JSON 文件恢复 products 时，应该更像“读文件”还是“写文件”？
# 我的回答：读
#
# 3. 如果用写文件模式打开一个已经存在的文件，原内容通常会保留还是被覆盖？
# 我的回答：只是打开的话，应该保留
# 正确答案：会被覆盖/清空。用写文件模式打开已有文件时，原内容通常在打开那一刻就会被清空。
#
# 4. 为什么写入真实数据文件前要小心？
# 我的回答：容易覆盖源文件
#
# 完成标准：
# 1. 你能区分保存数据需要写文件
# 2. 你能区分读取数据需要读文件
# 3. 你知道写文件模式可能覆盖原文件内容
#
# 可选挑战：
# - 思考：为什么测试保存功能时，最好使用临时文件，而不是项目里的真实 JSON 文件？    # 容易覆盖源文件


# ========================
# Part 6：第一次写 save_products()
# ========================
# 目标：
# 写一个最小版本的 save_products(products, filename)，把 products 保存到 JSON 文件。
#
# 要求：
# 1. 在文件顶部导入 json 模块
# 2. 定义 save_products(products, filename)
# 3. 在函数里用写文件模式打开 filename
# 4. 把 products 写进这个文件
# 5. save_products() 不要添加、删除、修改任何商品
#

import json
import day_44

def save_products(products, filename):
    with open(filename, 'w') as f:
        json.dump(products, f)


def load_products_exist(filename):
    with open(filename, 'r') as f:
        result = json.load(f)
        return result





# 完成标准：
# 1. 调用 save_products() 后，会生成一个 JSON 文件
# 2. JSON 文件里能看到商品数据
# 3. 原来的 products 列表内容不应该被 save_products() 改变
#
# 可选挑战：
# - 思考：如果保存的是中文商品名，JSON 文件里应该尽量显示中文，还是显示转义字符？


# ========================
# Part 7：处理文件不存在的读取情况
# ========================
# 目标：
# 让商品程序第一次运行、数据文件还不存在时，可以从空商品列表开始。
#
# 要求：
# 1. 另外定义一个 load_products(filename)
# 2. 尝试读取 filename 指向的 JSON 文件
# 3. 只处理 FileNotFoundError
# 4. 文件不存在时返回空列表
# 5. 不要创建新的数据文件
# 6. 不要使用会捕获所有异常的写法
# 7. 保持现有的 load_products_exist() 不变
#
def load_products(filename):
    try:
        with open(filename, 'r') as f:
            result = json.load(f)
            return result
    except FileNotFoundError:
        return []

def clean(products):
    list_empty = []

    for product in products:
        n = product['name']
        p = product['price']
        try:
            day_44.find_product(list_empty, n)
        except ValueError:
            day_44.add_product(list_empty, n, p)
        else:
            pass
    return list_empty


# 完成标准：
# 1. 传入一个不存在的文件名时，函数返回空列表
# 2. 调用结束后，那个不存在的文件仍然没有被创建
# 3. 你能说明为什么这里只处理 FileNotFoundError
# 4. 你能说明“没有历史数据”和“数据文件损坏”不是同一种情况
#
# 可选挑战：
# - 思考：如果文件存在，但里面不是合法的 JSON，是否也应该返回空列表？为什么？应该报错，因为里面有东西，有无法读取的不合法的Json

def main():
    products_1 = [{'name': 'fork', 'price': 24}, {'name': 'egg', 'price': 12}, {'name': 'goose', 'price': 15}]
    b = load_products('kk')
    print(b)

    for product in products_1:
        n = product['name']
        p = product['price']
        try:
            c = day_44.find_product(b, n)
        except ValueError:
            day_44.add_product(b, n, p)
        else:
            if c['price'] == p:
                print('商品已存在')
            else: c['price'] = p


    new = clean(b)
    save_products(new, 'kk')

  

'''
    save_products(products_1, 'test_day_48_2.json')
    a = load_products('test_day_48_2.json')
    print(a) 

    day_44.add_product(a, 'goose', 15)
    print(a)
    save_products(a, 'test_day_48_2.json')
'''



if __name__ == '__main__':
    main()


# ========================
# Part 8：清理 JSON 文件里的重复商品
# ========================
# 目标：
# - 写一个 clean(products) 函数，把传入列表中重复出现的商品整理成每个 name 只保留一条。
#
# 要求：
# - 在 main() 中用 load_products('kk') 读取旧数据，再把读取到的列表传给 clean(...)
# - 准备一个新的空列表，用来保存清理后的商品
# - 遍历旧数据里的每个 product
# - 判断重复时，先按 product['name'] 判断，而不是按整个 dict 判断
# - 如果这个 name 第一次出现，就把这个商品保留下来
# - 如果这个 name 已经出现过，就跳过这个重复商品
# - clean(...) 返回清理后的新列表；由 main() 在全部处理完成后只调用一次 save_products(...) 保存结果
# - 不要直接手动编辑 kk 文件完成这一步
#
# 完成标准：
# - kk 中相同 name 的商品不会保留多条
# - clean(...) 返回的数据仍然是 list，里面每个元素仍然是 dict
# - 清理后再次运行 main()，不会继续增加重复的 goose / fork / egg
# - 你能说清楚“旧数据”“清理后的新数据”“保存回文件”分别是哪一步
#
# 可选挑战：
# - 如果同一个 name 出现多次但 price 不一样，思考应该保留第一次出现的价格，还是最后一次出现的价格。 # 按照逻辑，应该最后一个







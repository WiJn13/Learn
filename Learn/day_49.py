# TITLE: JSON 数据结构校验
# CATEGORY: 文件操作与数据安全
# day_49.py


# ========================
# Part 1：校验 JSON 顶层结构
# ========================
# 目标：
# - 让 load_products() 区分“文件不存在”和“JSON 结构不符合商品程序的要求”。
#
# 要求：
# - 参考 day_48_2.py 里现有的 load_products()，在本文件中定义新版本。
# - 在 json.load() 读取完成后、返回数据前，检查最外层数据是否为 list。
# - 如果最外层是 list，正常返回读取结果。
# - 如果最外层不是 list，主动抛出 ValueError。
# - 只在文件不存在时返回空列表。
# - 不要捕获所有异常，也不要把结构错误伪装成空数据。
#
# 完成标准：
# - 文件不存在时，load_products() 返回空列表。
# - JSON 最外层是 list 时，load_products() 正常返回数据。
# - JSON 语法合法但最外层是 dict、str 或其他类型时，load_products() 抛出 ValueError。
# - 你能说清“JSON 语法合法”和“数据结构符合程序约定”的区别。
#
# 可选挑战：
# - 思考：最外层是 list，但里面某个元素不是 dict 时，程序还需要做什么检查？

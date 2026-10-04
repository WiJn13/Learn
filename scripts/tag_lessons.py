#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
tag_lessons.py
给 Learn/ 目录下的 学习 .py 文件 自动添加：

# TITLE: ...
# CATEGORY: ...

若文件里已经有 TITLE 或 CATEGORY，就不会重复添加。
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEARN = ROOT / "Learn"

TAGS = {
    "01_input_variables.py": ("输入、变量和简单函数", "基础语法"),
    "02_strings_base_conversion.py": ("字符串操作与进制转换", "字符串与序列"),
    "03_unicode_bytes.py": ("字符编码、bytes 与进制", "字符编码与进制"),
    "04_script_headers_string_formatting.py": ("shebang 与编码声明", "脚本基础与环境"),
    "05_list_operations.py": ("list 的基本操作", "容器类型·列表"),
    "06_pattern_matching_loops.py": ("match/case 与 for 循环", "控制流与循环"),
    "07_immutability_dict_set.py": ("不可变对象、dict/set 与基础函数", "数据类型与函数基础"),
    "08_function_validation.py": ("自定义函数与参数检查", "函数与条件判断"),
    "09_default_variadic_arguments.py": ("二次方程、默认参数与可变参数", "函数进阶"),
    "10_argument_unpacking.py": ("*args/**kw 高级用法与参数校验", "函数参数进阶"),
    "11_recursion_hanoi.py": ("递归、尾递归与汉诺塔", "递归与算法"),
    "12_iterable_iterator_basics.py": ("Iterable / Iterator 与迭代器使用", "迭代与循环"),
    "13_comprehensions_generators.py": ("列表推导式与 os.listdir", "推导式与文件系统"),
    "14_iteration_higher_order_functions.py": ("Iterable、Iterator 与生成器", "迭代器与生成器"),
    "15_map_reduce_filter_sort.py": ("map/reduce 与数据转换、字符串规范化", "高阶函数与函数式编程"),
    "16_closures_lambda.py": ("闭包、lazy 函数与匿名函数", "闭包与函数式编程"),
    "17_nonlocal_decorators.py": ("nonlocal 计数器闭包与 lambda", "闭包与匿名函数"),
    "18_modules_classes.py": ("模块 test 与 Student 类入门", "模块与面向对象基础"),
    "19_encapsulation_accessors.py": ("封装、私有属性与 getter/setter", "面向对象·封装"),
    "20_class_instance_attributes.py": ("类属性、实例属性与动态属性", "面向对象·类与实例属性"),
    "21_dynamic_methods_slots_properties.py": ("动态方法绑定、MethodType 与 __slots__", "面向对象·高级特性"),
    "22_class_iteration_slicing.py": ("索引和切片", "面向对象"),
    "23_enums.py": ("定制类", "面向对象·定制类"),
    "24_classes_types.py": ("使用元类", "面向对象·元类"),

}


def add_tags_to_file(path: Path, title: str, category: str):
    text = path.read_text(encoding="utf-8")

    # 如果已经有 TITLE 或 CATEGORY，就先不动，避免重复插
    if "TITLE:" in text or "CATEGORY:" in text:
        print(f"[跳过] {path.name} 已包含 TITLE/CATEGORY")
        return

    # 特殊处理：如果第一行是 shebang，就把注释放在 shebang 后面
    lines = text.splitlines(keepends=True)
    new_text: str

    if lines and lines[0].startswith("#!"):
        # 保留 shebang 在第一行
        shebang = lines[0]
        rest = "".join(lines[1:])
        header = f"# TITLE: {title}\n# CATEGORY: {category}\n"
        new_text = shebang + header + rest
    else:
        header = f"# TITLE: {title}\n# CATEGORY: {category}\n"
        new_text = header + text

    path.write_text(new_text, encoding="utf-8")
    print(f"[已写入] {path.name}")


def main():
    if not LEARN.exists():
        print("未找到 Learn/ 目录，请确认项目结构。")
        return

    for fname, (title, cat) in TAGS.items():
        file_path = LEARN / fname
        if not file_path.exists():
            # 某些 22_class_iteration_slicing/22/23/24 可能还没创建，不报错，只提示
            print(f"[缺失] {fname} 不存在，已跳过。")
            continue
        add_tags_to_file(file_path, title, cat)

    print("\n✅ 所有可处理的 学习文件 已尝试写入 TITLE / CATEGORY。")


if __name__ == "__main__":
    main()
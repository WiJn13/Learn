# Python 学习记录

这里记录了我的 Python 学习过程。文件采用“学习顺序编号 + 主题”命名，例如 `01_input_variables.py`；测试文件采用 `test_48_product_manager.py`，保留 `test_` 前缀。编号表示学习顺序，不表示天数。普通学习文件直接以编号开头；引用这类文件时使用 `importlib.import_module()`，例如 `importlib.import_module("47_product_manager")`。

一个主题可以跨多天完成，也可以在一天学习多个主题。文件内部继续用 `Part` 划分阶段。

学习顺序记录在 `Learn/learning_order.json`，下方编号仅表示索引顺序。新文件即使尚未登记，也会被索引和每日测验读取。

早期基础学习文件于 2025-11-28 首次整理并上传至当前学习仓库。

旧文件名与新文件名可查阅 [文件改名对照](plans/file_rename_map.md)。

---

## 📘 学习进度目录

下面是自动整理后的文件列表（本段会由脚本自动更新）：

<!-- INDEX-START -->
```text
01 - 01_input_variables.py [第一个Python程序] 输入、变量和简单函数
02 - 02_strings_base_conversion.py [Python基础] 字符串操作与进制转换
03 - 03_unicode_bytes.py [Python基础] 字符编码、bytes 与进制
04 - 04_script_headers_string_formatting.py [Python基础] shebang 与编码声明
05 - 05_list_operations.py [Python基础] list 的基本操作
06 - 06_pattern_matching_loops.py [Python基础] match/case 与 for 循环
07 - 07_immutability_dict_set.py [Python基础] 不可变对象、dict/set 与基础函数
08 - 08_function_validation.py [函数] 自定义函数与参数检查
09 - 09_default_variadic_arguments.py [函数] 二次方程、默认参数与可变参数
10 - 10_argument_unpacking.py [函数] *args/**kw 高级用法与参数校验
11 - 11_recursion_hanoi.py [函数] 递归、尾递归与汉诺塔
12 - 12_iterable_iterator_basics.py [高级特性] Iterable / Iterator 与迭代器使用
13 - 13_comprehensions_generators.py [高级特性] 列表推导式与 os.listdir
14 - 14_iteration_higher_order_functions.py [高级特性] Iterable、Iterator 与生成器
15 - 15_map_reduce_filter_sort.py [函数式编程] map/reduce 与数据转换、字符串规范化
16 - 16_closures_lambda.py [函数式编程] 闭包、lazy 函数与匿名函数
17 - 17_nonlocal_decorators.py [函数式编程] nonlocal 计数器闭包与 lambda
18 - 18_modules_classes.py [模块] 模块 test 与 Student 类入门
19 - 19_encapsulation_accessors.py [面向对象编程] 封装、私有属性与 getter/setter
20 - 20_class_instance_attributes.py [面向对象编程] 类属性、实例属性与动态属性
21 - 21_dynamic_methods_slots_properties.py [面向对象高级编程] 动态方法绑定、MethodType 与 __slots__
22 - 22_class_iteration_slicing.py [面向对象高级编程] 索引和切片
23 - 23_enums.py [面向对象高级编程] 定制类
24 - 24_classes_types.py [面向对象高级编程] 使用元类
25 - 25_metaclasses_error_handling.py [面向对象高级编程] 使用元类，错误处理
26 - 26_exception_propagation.py [错误、调试和测试] 错误处理2
27 - 27_debugging_assertions.py [错误、调试和测试] 调试，单元测试
28 - 28_dict_subclass_unittest.py [错误、测试和调试] 单元测试
29 - 29_slicing_list_review.py [重启] 重启
30 - 30_list_copy_dict_errors.py [重启] 重启
31 - 31_function_arguments_scope.py [函数进阶] 函数参数与作用域
32 - 32_inheritance_file_io.py [面向对象编程] 继承与文件操作
33 - 33_list_comprehension_review.py [高级特性] 列表推导式
34 - 34_filter_zip_dict_comprehensions.py [函数进阶] filter, zip 与字典推导式
35 - 35_decorator_practice.py [函数进阶] 装饰器实战
36 - 36_decorator_closure_review.py [函数进阶] 装饰器与闭包深度复习
37 - 37_generator_iterator_practice.py [函数进阶] 生成器与迭代器
38 - 38_oop_basics.py [面向对象编程] 面向对象编程基础
39 - 39_inheritance_polymorphism.py [面向对象编程] 面向对象编程进阶
40 - 40_inheritance_initialization.py [面向对象编程] 继承中的初始化参数传递
41 - 41_inheritance_initialization_review.py [面向对象编程] 面向对象复习：继承初始化与参数传递
42 - 42_composition_object_relationships.py [面向对象编程] 面向对象复习：组合与对象关系
43 - 43_class_static_methods.py [面向对象编程] 面向对象复习：类属性、类方法与静态方法
44 - 44_account_validation.py [面向对象编程] 面向对象复习：封装、属性校验与异常流程
45 - 45_account_inheritance.py [面向对象编程] 面向对象进阶：继承、封装与多态综合练习
46 - 46_orders_payment_composition.py [面向对象编程] 面向对象复习：从“会写类”到“会拆对象”
47 - 47_product_manager.py [模块化与代码组织] Python 工程化入门：main()、程序入口与模块复用
48 - test_48_product_manager.py [未分类]
49 - test_49_product_behavior.py [测试与代码验证] Python 工程化入门：assert、测试函数与行为验证
50 - test_50_product_parametrize.py [测试与代码验证] Python 工程化入门：pytest.mark.parametrize 与多组测试数据
51 - test_51_product_fixtures.py [测试与代码验证] Python 工程化入门：测试数据复用与 fixture 思维
52 - test_52_product_mutations.py [测试与代码验证] Python 工程化入门：测试会修改数据的函数
53 - 53_json_product_storage.py [文件操作与数据保存] Python 工程化入门：JSON 文件持久化
54 - 54_json_product_validation.py [文件操作与数据安全] JSON 数据结构校验
55 - 55_safe_product_addition.py [文件操作与数据安全] 安全新增商品
56 - 56_safe_product_price_update.py [文件操作与数据安全] 安全修改商品价格
57 - 57_safe_product_deletion.py [文件操作与数据安全] 安全删除商品
58 - 58_testable_confirmation.py [函数参数、输入来源与可测试性] 让交互式函数可以自动测试
59 - 59_confirmation_test_runner.py [函数组织、测试入口与可读性] 集中运行自动测试
60 - 60_unittest_basics.py [标准库、测试类与测试方法] 使用 unittest 组织自动测试
61 - 61_unittest_exceptions.py [标准库、异常与测试] 使用 unittest 测试预期异常
62 - 62_calculate_days_lived.py [未分类]
63 - 63_capability_demo.py [未分类]
```
<!-- INDEX-END -->

> 我们一起努力。每天都有进步，每天都有新变化。
---

## 📦 目录结构

下面是自动生成的项目结构预览（由脚本自动更新）：

<!-- TREE-START -->
```text
Python/
│── Learn/
│     ├── 01_input_variables.py
│     ├── 02_strings_base_conversion.py
│     ├── 03_unicode_bytes.py
│     ├── 04_script_headers_string_formatting.py
│     ├── 05_list_operations.py
│     ├── 06_pattern_matching_loops.py
│     ├── 07_immutability_dict_set.py
│     ├── 08_function_validation.py
│     ├── 09_default_variadic_arguments.py
│     ├── 10_argument_unpacking.py
│     ├── 11_recursion_hanoi.py
│     ├── 12_iterable_iterator_basics.py
│     ├── 13_comprehensions_generators.py
│     ├── 14_iteration_higher_order_functions.py
│     ├── 15_map_reduce_filter_sort.py
│     ├── 16_closures_lambda.py
│     ├── 17_nonlocal_decorators.py
│     ├── 18_modules_classes.py
│     ├── 19_encapsulation_accessors.py
│     ├── 20_class_instance_attributes.py
│     ├── 21_dynamic_methods_slots_properties.py
│     ├── 22_class_iteration_slicing.py
│     ├── 23_enums.py
│     ├── 24_classes_types.py
│     ├── 25_metaclasses_error_handling.py
│     ├── 26_exception_propagation.py
│     ├── 27_debugging_assertions.py
│     ├── 28_dict_subclass_unittest.py
│     ├── 29_slicing_list_review.py
│     ├── 30_list_copy_dict_errors.py
│     ├── 31_function_arguments_scope.py
│     ├── 32_inheritance_file_io.py
│     ├── 33_list_comprehension_review.py
│     ├── 34_filter_zip_dict_comprehensions.py
│     ├── 35_decorator_practice.py
│     ├── 36_decorator_closure_review.py
│     ├── 37_generator_iterator_practice.py
│     ├── 38_oop_basics.py
│     ├── 39_inheritance_polymorphism.py
│     ├── 40_inheritance_initialization.py
│     ├── 41_inheritance_initialization_review.py
│     ├── 42_composition_object_relationships.py
│     ├── 43_class_static_methods.py
│     ├── 44_account_validation.py
│     ├── 45_account_inheritance.py
│     ├── 46_orders_payment_composition.py
│     ├── 47_product_manager.py
│     ├── 53_json_product_storage.py
│     ├── 54_json_product_validation.py
│     ├── 55_safe_product_addition.py
│     ├── 56_safe_product_price_update.py
│     ├── 57_safe_product_deletion.py
│     ├── 58_testable_confirmation.py
│     ├── 59_confirmation_test_runner.py
│     ├── 60_unittest_basics.py
│     ├── 61_unittest_exceptions.py
│     ├── 62_calculate_days_lived.py
│     ├── 63_capability_demo.py
│     ├── learning_order.json
│     ├── mm.json
│     ├── nn.json
│     ├── product_storage_sample.json
│     ├── test_48_product_manager.py
│     ├── test_49_product_behavior.py
│     ├── test_50_product_parametrize.py
│     ├── test_51_product_fixtures.py
│     ├── test_52_product_mutations.py
│
│── scripts/
│     ├── autopush.py
│     ├── batch_rename_modules.py
│     ├── generate_daily_quiz.py
│     ├── generate_index.py
│     ├── grade_issue_answer.py
│     ├── move_learning_files.py
│     ├── originize_files.py
│     ├── tag_lessons.py
│     ├── update_readme.py
│── AGENTS.md
│── README.md
│── resources/
│── images/
│── misc/
│── plans/
```
<!-- TREE-END -->

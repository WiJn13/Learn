# Python 学习记录

这里记录了我的 Python 学习过程。文件采用“学习顺序编号 + 主题”命名，例如 `_01_input_variables.py`；测试文件采用 `test_48_product_manager.py`，保留 `test_` 前缀。编号表示学习顺序，不表示天数。普通学习文件以 `_` 开头，使带编号的文件名也可以用于 Python 的 `import`。

一个主题可以跨多天完成，也可以在一天学习多个主题。文件内部继续用 `Part` 划分阶段。

学习顺序记录在 `Learn/learning_order.json`，下方编号仅表示索引顺序。新文件即使尚未登记，也会被索引和每日测验读取。

早期基础学习文件于 2025-11-28 首次整理并上传至当前学习仓库。

旧文件名与新文件名可查阅 [文件改名对照](plans/file_rename_map.md)。

---

## 📘 学习进度目录

下面是自动整理后的文件列表（本段会由脚本自动更新）：

<!-- INDEX-START -->
```text
01 - _01_input_variables.py [第一个Python程序] 输入、变量和简单函数
02 - _02_strings_base_conversion.py [Python基础] 字符串操作与进制转换
03 - _03_unicode_bytes.py [Python基础] 字符编码、bytes 与进制
04 - _04_script_headers_string_formatting.py [Python基础] shebang 与编码声明
05 - _05_list_operations.py [Python基础] list 的基本操作
06 - _06_pattern_matching_loops.py [Python基础] match/case 与 for 循环
07 - _07_immutability_dict_set.py [Python基础] 不可变对象、dict/set 与基础函数
08 - _08_function_validation.py [函数] 自定义函数与参数检查
09 - _09_default_variadic_arguments.py [函数] 二次方程、默认参数与可变参数
10 - _10_argument_unpacking.py [函数] *args/**kw 高级用法与参数校验
11 - _11_recursion_hanoi.py [函数] 递归、尾递归与汉诺塔
12 - _12_iterable_iterator_basics.py [高级特性] Iterable / Iterator 与迭代器使用
13 - _13_comprehensions_generators.py [高级特性] 列表推导式与 os.listdir
14 - _14_iteration_higher_order_functions.py [高级特性] Iterable、Iterator 与生成器
15 - _15_map_reduce_filter_sort.py [函数式编程] map/reduce 与数据转换、字符串规范化
16 - _16_closures_lambda.py [函数式编程] 闭包、lazy 函数与匿名函数
17 - _17_nonlocal_decorators.py [函数式编程] nonlocal 计数器闭包与 lambda
18 - _18_modules_classes.py [模块] 模块 test 与 Student 类入门
19 - _19_encapsulation_accessors.py [面向对象编程] 封装、私有属性与 getter/setter
20 - _20_class_instance_attributes.py [面向对象编程] 类属性、实例属性与动态属性
21 - _21_dynamic_methods_slots_properties.py [面向对象高级编程] 动态方法绑定、MethodType 与 __slots__
22 - _22_class_iteration_slicing.py [面向对象高级编程] 索引和切片
23 - _23_enums.py [面向对象高级编程] 定制类
24 - _24_classes_types.py [面向对象高级编程] 使用元类
25 - _25_metaclasses_error_handling.py [面向对象高级编程] 使用元类，错误处理
26 - _26_exception_propagation.py [错误、调试和测试] 错误处理2
27 - _27_debugging_assertions.py [错误、调试和测试] 调试，单元测试
28 - _28_dict_subclass_unittest.py [错误、测试和调试] 单元测试
29 - _29_slicing_list_review.py [重启] 重启
30 - _30_list_copy_dict_errors.py [重启] 重启
31 - _31_function_arguments_scope.py [函数进阶] 函数参数与作用域
32 - _32_inheritance_file_io.py [面向对象编程] 继承与文件操作
33 - _33_list_comprehension_review.py [高级特性] 列表推导式
34 - _34_filter_zip_dict_comprehensions.py [函数进阶] filter, zip 与字典推导式
35 - _35_decorator_practice.py [函数进阶] 装饰器实战
36 - _36_decorator_closure_review.py [函数进阶] 装饰器与闭包深度复习
37 - _37_generator_iterator_practice.py [函数进阶] 生成器与迭代器
38 - _38_oop_basics.py [面向对象编程] 面向对象编程基础
39 - _39_inheritance_polymorphism.py [面向对象编程] 面向对象编程进阶
40 - _40_inheritance_initialization.py [面向对象编程] 继承中的初始化参数传递
41 - _41_inheritance_initialization_review.py [面向对象编程] 面向对象复习：继承初始化与参数传递
42 - _42_composition_object_relationships.py [面向对象编程] 面向对象复习：组合与对象关系
43 - _43_class_static_methods.py [面向对象编程] 面向对象复习：类属性、类方法与静态方法
44 - _44_account_validation.py [面向对象编程] 面向对象复习：封装、属性校验与异常流程
45 - _45_account_inheritance.py [面向对象编程] 面向对象进阶：继承、封装与多态综合练习
46 - _46_orders_payment_composition.py [面向对象编程] 面向对象复习：从“会写类”到“会拆对象”
47 - _47_product_manager.py [模块化与代码组织] Python 工程化入门：main()、程序入口与模块复用
48 - test_48_product_manager.py [未分类]
49 - test_49_product_behavior.py [测试与代码验证] Python 工程化入门：assert、测试函数与行为验证
50 - test_50_product_parametrize.py [测试与代码验证] Python 工程化入门：pytest.mark.parametrize 与多组测试数据
51 - test_51_product_fixtures.py [测试与代码验证] Python 工程化入门：测试数据复用与 fixture 思维
52 - test_52_product_mutations.py [测试与代码验证] Python 工程化入门：测试会修改数据的函数
53 - _53_json_product_storage.py [文件操作与数据保存] Python 工程化入门：JSON 文件持久化
54 - _54_json_product_validation.py [文件操作与数据安全] JSON 数据结构校验
55 - _55_safe_product_addition.py [文件操作与数据安全] 安全新增商品
56 - _56_safe_product_price_update.py [文件操作与数据安全] 安全修改商品价格
57 - _57_safe_product_deletion.py [文件操作与数据安全] 安全删除商品
58 - _58_testable_confirmation.py [函数参数、输入来源与可测试性] 让交互式函数可以自动测试
59 - _59_confirmation_test_runner.py [函数组织、测试入口与可读性] 集中运行自动测试
60 - _60_unittest_basics.py [标准库、测试类与测试方法] 使用 unittest 组织自动测试
61 - _61_unittest_exceptions.py [标准库、异常与测试] 使用 unittest 测试预期异常
62 - _62_calculate_days_lived.py [未分类]
63 - _63_capability_demo.py [未分类]
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
│     ├── _01_input_variables.py
│     ├── _02_strings_base_conversion.py
│     ├── _03_unicode_bytes.py
│     ├── _04_script_headers_string_formatting.py
│     ├── _05_list_operations.py
│     ├── _06_pattern_matching_loops.py
│     ├── _07_immutability_dict_set.py
│     ├── _08_function_validation.py
│     ├── _09_default_variadic_arguments.py
│     ├── _10_argument_unpacking.py
│     ├── _11_recursion_hanoi.py
│     ├── _12_iterable_iterator_basics.py
│     ├── _13_comprehensions_generators.py
│     ├── _14_iteration_higher_order_functions.py
│     ├── _15_map_reduce_filter_sort.py
│     ├── _16_closures_lambda.py
│     ├── _17_nonlocal_decorators.py
│     ├── _18_modules_classes.py
│     ├── _19_encapsulation_accessors.py
│     ├── _20_class_instance_attributes.py
│     ├── _21_dynamic_methods_slots_properties.py
│     ├── _22_class_iteration_slicing.py
│     ├── _23_enums.py
│     ├── _24_classes_types.py
│     ├── _25_metaclasses_error_handling.py
│     ├── _26_exception_propagation.py
│     ├── _27_debugging_assertions.py
│     ├── _28_dict_subclass_unittest.py
│     ├── _29_slicing_list_review.py
│     ├── _30_list_copy_dict_errors.py
│     ├── _31_function_arguments_scope.py
│     ├── _32_inheritance_file_io.py
│     ├── _33_list_comprehension_review.py
│     ├── _34_filter_zip_dict_comprehensions.py
│     ├── _35_decorator_practice.py
│     ├── _36_decorator_closure_review.py
│     ├── _37_generator_iterator_practice.py
│     ├── _38_oop_basics.py
│     ├── _39_inheritance_polymorphism.py
│     ├── _40_inheritance_initialization.py
│     ├── _41_inheritance_initialization_review.py
│     ├── _42_composition_object_relationships.py
│     ├── _43_class_static_methods.py
│     ├── _44_account_validation.py
│     ├── _45_account_inheritance.py
│     ├── _46_orders_payment_composition.py
│     ├── _47_product_manager.py
│     ├── _53_json_product_storage.py
│     ├── _54_json_product_validation.py
│     ├── _55_safe_product_addition.py
│     ├── _56_safe_product_price_update.py
│     ├── _57_safe_product_deletion.py
│     ├── _58_testable_confirmation.py
│     ├── _59_confirmation_test_runner.py
│     ├── _60_unittest_basics.py
│     ├── _61_unittest_exceptions.py
│     ├── _62_calculate_days_lived.py
│     ├── _63_capability_demo.py
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

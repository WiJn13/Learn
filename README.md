# Python 学习记录

这里记录了我从 Day 01 开始的 Python 学习过程。  
文件名统一为 `day_XX.py`，符合 Python PEP 8 的模块命名规范。

---

## 📘 学习进度目录

下面是自动整理后的文件列表（本段会由脚本自动更新）：

<!-- INDEX-START -->
```text
01 - day_01.py [第一个Python程序] 输入、变量和简单函数
02 - day_02.py [Python基础] 字符串操作与进制转换
03 - day_03.py [Python基础] 字符编码、bytes 与进制
04 - day_04.py [Python基础] shebang 与编码声明
05 - day_05_2.py [Python基础] match/case 与 for 循环
05 - day_05_1.py [Python基础] list 的基本操作
06 - day_06.py [Python基础] 不可变对象、dict/set 与基础函数
07 - day_07.py [函数] 自定义函数与参数检查
08 - day_08.py [函数] 二次方程、默认参数与可变参数
09 - day_09.py [函数] *args/**kw 高级用法与参数校验
10 - day_10.py [函数] 递归、尾递归与汉诺塔
11 - day_11.py [高级特性] Iterable / Iterator 与迭代器使用
12 - day_12.py [高级特性] 列表推导式与 os.listdir
13 - day_13.py [高级特性] Iterable、Iterator 与生成器
14 - day_14.py [函数式编程] map/reduce 与数据转换、字符串规范化
15 - day_15.py [函数式编程] 闭包、lazy 函数与匿名函数
16 - day_16.py [函数式编程] nonlocal 计数器闭包与 lambda
17 - day_17.py [模块] 模块 test 与 Student 类入门
18 - day_18.py [面向对象编程] 封装、私有属性与 getter/setter
19 - day_19.py [面向对象编程] 类属性、实例属性与动态属性
20 - day_20.py [面向对象高级编程] 动态方法绑定、MethodType 与 __slots__
21 - day_21.py [面向对象高级编程] 索引和切片
22 - day_22.py [面向对象高级编程] 定制类
23 - day_23.py [面向对象高级编程] 使用元类
24 - day_24_2.py [错误、调试和测试] 错误处理2
24 - day_24_1.py [面向对象高级编程] 使用元类，错误处理
25 - day_25.py [错误、调试和测试] 调试，单元测试
26 - day_26.py [错误、测试和调试] 单元测试
27 - day_27.py [重启] 重启
28 - day_28.py [重启] 重启
29 - day_29.py [函数进阶] 函数参数与作用域
30 - day_30.py [面向对象编程] 继承与文件操作
31 - day_31.py [高级特性] 列表推导式
32 - day_32.py [函数进阶] filter, zip 与字典推导式
33 - day_33.py [函数进阶] 装饰器实战
34 - day_34.py [函数进阶] 装饰器与闭包深度复习
35 - day_35.py [函数进阶] 生成器与迭代器
36 - day_36.py [面向对象编程] 面向对象编程基础
37 - day_37.py [面向对象编程] 面向对象编程进阶
```
<!-- INDEX-END -->

> 我们一起努力。
---

## 📦 目录结构

下面是自动生成的项目结构预览（由脚本自动更新）：

<!-- TREE-START -->
```text
Python/
│── Learn/
│     ├── day_01.py
│     ├── day_02.py
│     ├── day_03.py
│     ├── day_04.py
│     ├── day_05_1.py
│     ├── day_05_2.py
│     ├── day_06.py
│     ├── day_07.py
│     ├── day_08.py
│     ├── day_09.py
│     ├── day_10.py
│     ├── day_11.py
│     ├── day_12.py
│     ├── day_13.py
│     ├── day_14.py
│     ├── day_15.py
│     ├── day_16.py
│     ├── day_17.py
│     ├── day_18.py
│     ├── day_19.py
│     ├── day_20.py
│     ├── day_21.py
│     ├── day_22.py
│     ├── day_23.py
│     ├── day_24_1.py
│     ├── day_24_2.py
│     ├── day_25.py
│     ├── day_26.py
│     ├── day_27.py
│     ├── day_28.py
│     ├── day_29.py
│     ├── day_30.py
│     ├── day_31.py
│     ├── day_32.py
│     ├── day_33.py
│     ├── day_34.py
│     ├── day_35.py
│     ├── day_36.py
│     ├── day_37.py
│
│── autopush.py
│── update_readme.py
│── generate_index.py
│── move_day_files.py
│── originize_files.py
│── batch_rename_modules.py
│── README.md
│── resources/
│── images/
│── misc/
```
<!-- TREE-END -->
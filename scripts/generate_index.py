#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
generate_index.py
扫描 Learn 目录所有 day_xx.py 文件，自动生成按顺序的索引列表。
"""

from pathlib import Path
import re

def main():
    p = Path("Learn")
    files = []

    for f in p.iterdir():
        if f.is_file() and f.name.startswith("day_") and f.suffix == ".py":
            # 提取数字序号
            match = re.search(r"day_(\d+)", f.name)
            if match:
                num = int(match.group(1))
                files.append((num, f.name))

    # 按序号排序
    files.sort()

    print("\n=== 自动生成 Python 学习索引 ===\n")
    for num, name in files:
        print(f"{num:02d} - {name}")
    print("\n（你可以把这些内容复制到 README）\n")

if __name__ == "__main__":
    main()
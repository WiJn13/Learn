#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
move_day_files.py
自动将所有 day_*.py 文件移动到 Learn/ 文件夹。
"""

from pathlib import Path

def main():
    root = Path(".")
    days_dir = root / "Learn"
    days_dir.mkdir(exist_ok=True)

    moved = []

    for f in root.iterdir():
        if f.is_file() and f.name.startswith("day_") and f.suffix == ".py":
            target = days_dir / f.name
            f.rename(target)
            moved.append(f.name)

    if moved:
        print("已移动以下文件到 Learn/：")
        for m in moved:
            print("  -", m)
    else:
        print("没有找到 day_*.py 文件。")

if __name__ == "__main__":
    main()
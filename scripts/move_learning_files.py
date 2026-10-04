#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
move_learning_files.py
将根目录带 TITLE 标记的学习 Python 文件移动到 Learn/，保留主题文件名。
"""

from pathlib import Path

def main():
    root = Path(__file__).resolve().parents[1]
    learn_dir = root / "Learn"
    learn_dir.mkdir(exist_ok=True)

    moved = []

    for f in root.iterdir():
        if f.is_file() and f.suffix == ".py" and "# TITLE:" in f.read_text(encoding="utf-8"):
            target = learn_dir / f.name
            if target.exists():
                raise FileExistsError(f"目标已存在，避免覆盖：{target}")
            f.rename(target)
            moved.append(f.name)

    if moved:
        print("已移动以下文件到 Learn/：")
        for m in moved:
            print("  -", m)
    else:
        print("没有找到需要移动的学习 Python 文件。")

if __name__ == "__main__":
    main()
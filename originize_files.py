#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
organize_files.py
自动将非 .py 文件整理到分类目录：
- PDF / 文档 -> resources/
- 图片 -> images/
- 其它杂项 -> misc/
"""

from pathlib import Path

def main():
    root = Path(".")
    resources = root / "resources"
    images = root / "images"
    misc = root / "misc"

    resources.mkdir(exist_ok=True)
    images.mkdir(exist_ok=True)
    misc.mkdir(exist_ok=True)

    for f in root.iterdir():
        if not f.is_file():
            continue
        if f.suffix == ".py" or f.name == "README.md":
            continue

        ext = f.suffix.lower()

        if ext in {".pdf", ".doc", ".docx", ".txt"}:
            target_dir = resources
        elif ext in {".png", ".jpg", ".jpeg", ".gif"}:
            target_dir = images
        else:
            target_dir = misc

        target = target_dir / f.name
        print(f"移动：{f.name} -> {target_dir.name}/{f.name}")
        f.rename(target)

    print("整理完成。")

if __name__ == "__main__":
    main()
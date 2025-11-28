#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
update_readme.py

功能：
1. 扫描 Learn/ 目录下的 day_*.py 文件
2. 读取每个文件的 TITLE / CATEGORY 注释
3. 生成简单索引文本，例如：
   01 - day_01.py [基础语法] 输入、变量和简单函数
4. 自动替换 README.md 中 <!-- INDEX-START --> 和 <!-- INDEX-END --> 之间的内容
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
LEARN = ROOT / "Learn"
README = ROOT / "README.md"


def parse_day_file(path: Path):
    """
    从 day_xx.py 文件中解析：
    - 编号 num（int）
    - TITLE（可选）
    - CATEGORY（可选）
    """
    m = re.search(r"day_(\d+)", path.name)
    if not m:
        return None
    num = int(m.group(1))

    title = ""
    category = ""

    try:
        with path.open("r", encoding="utf-8") as f:
            # 只看前几十行就够了
            for _ in range(30):
                line = f.readline()
                if not line:
                    break
                line = line.strip()
                if line.startswith("# TITLE:"):
                    title = line.replace("# TITLE:", "").strip()
                elif line.startswith("# CATEGORY:"):
                    category = line.replace("# CATEGORY:", "").strip()
    except Exception:
        pass

    if not category:
        category = "未分类"

    return {
        "num": num,
        "filename": path.name,
        "title": title,
        "category": category,
    }


def collect_items():
    """收集 Learn/ 目录下的所有 day_*.py 信息"""
    if not LEARN.exists():
        print("未找到 Learn/ 目录，请确认项目结构。")
        return []

    items = []
    for f in LEARN.iterdir():
        if f.is_file() and f.name.startswith("day_") and f.suffix == ".py":
            info = parse_day_file(f)
            if info:
                items.append(info)

    # 按编号排序
    items.sort(key=lambda x: x["num"])
    return items


def render_index_block(items):
    """
    生成将要写入 README 的文本块。
    形式如下：

    ```text
    01 - day_01.py [基础语法] 输入、变量和简单函数
    02 - day_02.py [字符串与序列] 字符串操作与进制转换
    ...
    ```
    """
    if not items:
        return "\n（当前没有检测到任何 day_*.py 文件）\n"

    lines = []
    lines.append("")
    lines.append("```text")
    for it in items:
        num = it["num"]
        fname = it["filename"]
        cat = it["category"]
        title = it["title"]
        # [分类] 和 标题 都是可选
        extra = ""
        if cat:
            extra += f" [{cat}]"
        if title:
            extra += f" {title}"
        lines.append(f"{num:02d} - {fname}{extra}")
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def update_readme(block: str):
    """
    把 README.md 中 <!-- INDEX-START --> 和 <!-- INDEX-END --> 之间替换掉
    """
    if not README.exists():
        print("未找到 README.md")
        return

    text = README.read_text(encoding="utf-8")

    start_tag = "<!-- INDEX-START -->"
    end_tag = "<!-- INDEX-END -->"

    if start_tag not in text or end_tag not in text:
        print("README.md 中缺少 INDEX-START 或 INDEX-END 标记。")
        return

    before, rest = text.split(start_tag, 1)
    _, after = rest.split(end_tag, 1)

    new_text = before + start_tag + block + end_tag + after
    README.write_text(new_text, encoding="utf-8")
    print("✅ README.md 已更新。")


def main():
    items = collect_items()
    block = render_index_block(items)
    update_readme(block)


if __name__ == "__main__":
    main()
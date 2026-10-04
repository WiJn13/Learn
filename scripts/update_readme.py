#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
update_readme.py

功能：
1. 扫描 Learn/ 目录下的 主题命名的 .py 文件
2. 读取每个文件的 TITLE / CATEGORY 注释
3. 生成简单索引文本，例如：
   01 - _01_input_variables.py [基础语法] 输入、变量和简单函数
4. 自动替换 README.md 中 <!-- INDEX-START --> 和 <!-- INDEX-END --> 之间的内容
"""


from pathlib import Path
import json


# Helper to replace a block between start_tag and end_tag in text
def _replace_block(text: str, start_tag: str, end_tag: str, block: str) -> str:
    if start_tag not in text or end_tag not in text:
        return text
    before, rest = text.split(start_tag, 1)
    _, after = rest.split(end_tag, 1)
    return before + start_tag + block + end_tag + after


ROOT = Path(__file__).resolve().parents[1]
LEARN = ROOT / "Learn"
README = ROOT / "README.md"


def parse_learning_file(path: Path):
    """读取学习文件中的 TITLE / CATEGORY，不依赖文件名中的编号。"""
    title = ""
    category = ""
    for line in path.read_text(encoding="utf-8").splitlines()[:30]:
        line = line.strip()
        if line.startswith("# TITLE:"):
            title = line.removeprefix("# TITLE:").strip()
        elif line.startswith("# CATEGORY:"):
            category = line.removeprefix("# CATEGORY:").strip()
    return {"filename": path.name, "title": title, "category": category or "未分类"}


def collect_items():
    """按独立的学习顺序收集文件；新文件未登记时也会出现在目录中。"""
    if not LEARN.exists():
        return []
    order_path = LEARN / "learning_order.json"
    order = json.loads(order_path.read_text(encoding="utf-8")) if order_path.exists() else []
    positions = {name: index for index, name in enumerate(order)}
    files = sorted(LEARN.glob("*.py"), key=lambda p: (positions.get(p.name, len(order)), p.name))
    items = []
    for num, path in enumerate(files, 1):
        info = parse_learning_file(path)
        info["num"] = num
        items.append(info)
    return items


def render_index_block(items):
    """
    生成将要写入 README 的文本块。
    形式如下：

    ```text
    01 - _01_input_variables.py [基础语法] 输入、变量和简单函数
    02 - _02_strings_base_conversion.py [字符串与序列] 字符串操作与进制转换
    ...
    ```
    """
    if not items:
        return "\n（当前没有检测到任何 主题命名的 .py 文件）\n"

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


# 生成项目目录结构预览代码块（TREE-START/TREE-END）
def build_tree_block() -> str:
    """生成项目目录结构预览代码块（TREE-START/TREE-END）。"""
    lines = []
    lines.append("")
    lines.append("```text")
    lines.append("Python/")

    # Learn 目录
    if LEARN.exists():
        lines.append("│── Learn/")
        learning_files = [f.name for f in LEARN.iterdir() if f.is_file() and f.suffix in {".py", ".json"}]
        for name in sorted(learning_files):
            lines.append(f"│     ├── {name}")
        lines.append("│")

    if (ROOT / "scripts").exists():
        lines.append("│── scripts/")
        for path in sorted((ROOT / "scripts").glob("*.py")):
            lines.append(f"│     ├── {path.name}")
    for name in ["AGENTS.md", "README.md"]:
        if (ROOT / name).exists():
            lines.append(f"│── {name}")

    # 资源类目录
    for dirname in ["resources", "images", "misc", "plans"]:
        if (ROOT / dirname).exists():
            lines.append(f"│── {dirname}/")

    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def update_readme(index_block: str, tree_block: str):
    """
    把 README.md 中 <!-- INDEX-START --> 和 <!-- INDEX-END --> 之间替换掉
    同时替换 <!-- TREE-START --> 和 <!-- TREE-END --> 之间的内容
    """
    if not README.exists():
        print("未找到 README.md")
        return

    text = README.read_text(encoding="utf-8")

    # 替换索引区域
    text = _replace_block(text, "<!-- INDEX-START -->", "<!-- INDEX-END -->", index_block)

    # 替换目录结构区域
    text = _replace_block(text, "<!-- TREE-START -->", "<!-- TREE-END -->", tree_block)

    README.write_text(text, encoding="utf-8")
    print("✅ README.md 已更新。")


def main():
    items = collect_items()
    index_block = render_index_block(items)
    tree_block = build_tree_block()
    update_readme(index_block, tree_block)


if __name__ == "__main__":
    main()

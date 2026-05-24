#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
batch_rename_modules.py

批量把目录下的 .py 文件名标准化为合法的 Python 模块名（小写、下划线、移除非法字符）。
特性：
 - 预览（默认 dry-run）
 - 只有加上 --apply 才会真正修改文件名
 - 冲突检测：若目标名冲突会自动在末尾追加 _1,_2...
"""

import re
import sys
import argparse
from pathlib import Path
from typing import Dict, Set


def make_safe_module_name(name: str) -> str:
    """
    把不规范的基名（不含 .py）转换为安全模块名：
      - 全部小写
      - 空格/连字符/点 -> 下划线
      - 删除非字母数字下划线字符
      - 若以数字开头，前加下划线
      - 若最终为空，命名为 module
    """
    s = name.strip().lower()
    # 先显式把全角括号替换成下划线
    s = s.replace("（", "_").replace("）", "_")
    # 再把空格、连字符、点换成下划线
    s = re.sub(r"[ \-\.]+", "_", s)
    # 删除其它非法字符（包括中文、括号等）
    s = re.sub(r"[^a-z0-9_]", "", s)
    # 合并连续下划线并去掉首尾下划线
    s = re.sub(r"_+", "_", s)
    s = s.strip("_")
    # 仅补齐第一个数字段（例如 Day 5（1） -> 5 补齐为 05，括号内 1 不补齐）
    number_iter = list(re.finditer(r"\d+", s))
    if number_iter:
        first = number_iter[0]
        padded = first.group().zfill(2)
        s = s[:first.start()] + padded + s[first.end():]
    # 不能以数字开头
    if re.match(r"^[0-9]", s):
        s = "_" + s
    # 空名兜底
    if not s:
        s = "module"
    return s


def unique_name(base: str, existing: Set[str]) -> str:
    """
    给定 base（不含 .py），在 existing 集合里寻找唯一名称，
    若冲突追加 _1,_2...，并把最终名加入 existing 后返回。
    """
    candidate = base
    i = 1
    while candidate in existing:
        candidate = f"{base}_{i}"
        i += 1
    existing.add(candidate)
    return candidate


def collect_py_files(directory: Path):
    """收集目录下所有 .py 文件（不递归子目录）"""
    return sorted(
        [p for p in directory.iterdir() if p.is_file() and p.suffix == ".py"],
        key=lambda p: p.name.lower(),
    )


def build_rename_map(files) -> Dict[Path, str]:
    """
    构建映射 old_path -> new_filename
    保证 new_filename 在目标集合中唯一
    """
    mapping: Dict[Path, str] = {}
    used_basenames: Set[str] = set()

    for f in files:
        orig_basename = f.stem           # 原来的名字（不含 .py）
        safe_base = make_safe_module_name(orig_basename)
        unique_base = unique_name(safe_base, used_basenames)
        new_filename = unique_base + ".py"
        mapping[f] = new_filename

    return mapping


def perform_rename(mapping: Dict[Path, str]):
    """
    执行重命名：为避免覆盖，先把原文件重命名为临时名（添加 .renametmp），
    然后把临时名批量改为目标名。若出错，尝试回滚已做的操作。
    """
    tmp_map = {}
    try:
        # 第一步：原文件 -> 临时名
        for old_path, new_filename in mapping.items():
            if old_path.name == new_filename:
                continue
            tmp = old_path.with_name(old_path.name + ".renametmp")
            if tmp.exists():
                raise FileExistsError(f"临时文件已存在，无法安全操作: {tmp}")
            old_path.rename(tmp)
            tmp_map[tmp] = new_filename

        # 第二步：临时名 -> 最终名
        for tmp_path, final_name in tmp_map.items():
            final_path = tmp_path.with_name(final_name)
            if final_path.exists():
                raise FileExistsError(f"目标文件已存在，避免覆盖: {final_path}")
            tmp_path.rename(final_path)

        return True, None
    except Exception as exc:
        # 回滚：把已改的临时名改回原来的名字（尽量恢复）
        for tmp_path, final_name in tmp_map.items():
            try:
                if tmp_path.exists():
                    orig_name = tmp_path.name.replace(".renametmp", "")
                    orig_path = tmp_path.with_name(orig_name)
                    tmp_path.rename(orig_path)
            except Exception:
                pass
        return False, exc


def main():
    print(">>> batch_rename_modules.py started")

    parser = argparse.ArgumentParser(
        description="批量标准化 .py 文件名为合法模块名（dry-run 默认）"
    )
    parser.add_argument("dir", nargs="?", default=".", help="目标目录（默认当前目录）")
    parser.add_argument(
        "--apply", action="store_true", help="实际执行重命名（默认仅预览）"
    )
    args = parser.parse_args()

    target = Path(args.dir).resolve()
    if not target.is_dir():
        print(f"错误：目标不是目录：{target}")
        sys.exit(1)

    files = collect_py_files(target)
    if not files:
        print("未发现 .py 文件于：", target)
        return

    mapping = build_rename_map(files)

    print("\n=== 重命名预览（原名 -> 新名） ===")
    changed = False
    for old_path, new_name in mapping.items():
        if old_path.name == new_name:
            print(f"  (保持不变) {old_path.name}")
        else:
            changed = True
            print(f"  {old_path.name}  ->  {new_name}")

    if not changed:
        print("所有文件名已是合法模块名且无冲突，无需修改。")
        return

    if not args.apply:
        print("\n注意：当前为预览（dry-run）。如确认无误，使用 --apply 参数来执行实际重命名。")
        print("示例：python3 batch_rename_modules.py . --apply")
        return

    # 执行重命名
    print("\n开始执行重命名...（请确保你已做好备份或在 git 下）")
    ok, err = perform_rename(mapping)
    if ok:
        print("重命名成功。建议运行测试并检查导入(import)语句。")
    else:
        print("重命名失败，已尝试回滚。错误信息：", err)


if __name__ == "__main__":
    main()
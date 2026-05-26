#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
autopush.py

一键自动化流程：
1. 运行 update_readme.py（如果存在）
2. 运行 organize_files.py / originize_files.py（如果存在）
3. git add -A
4. 若无改动则退出
5. 询问提交说明并 git commit
6. git push
"""

from pathlib import Path
import re
import subprocess
import sys


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
EXCLUDED_PATTERNS = (
    ".DS_Store",
    "__pycache__/",
    ".pyc",
)


def run_cmd(cmd, cwd=None, check=True):
    """打印并运行命令"""
    print("\n$ " + " ".join(cmd))
    result = subprocess.run(cmd, cwd=cwd, text=True)
    if check and result.returncode != 0:
        print(f"命令执行失败：{' '.join(cmd)}，退出码 {result.returncode}")
        sys.exit(result.returncode)
    return result


def is_excluded_status_line(line: str) -> bool:
    """判断 git status --porcelain 的一行是否属于缓存/系统文件。"""
    path = line[3:]
    return any(pattern in path for pattern in EXCLUDED_PATTERNS)


def get_included_changes():
    """返回排除缓存/系统文件后的改动列表。"""
    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    lines = [line for line in status.stdout.splitlines() if line.strip()]
    return [line for line in lines if not is_excluded_status_line(line)]


def stage_included_changes(changes):
    """只暂存非缓存/系统文件，避免 .DS_Store 和 __pycache__ 进入提交。"""
    if not changes:
        return
    paths = [line[3:] for line in changes]
    run_cmd(["git", "add", "--", *paths], cwd=ROOT)


def parse_day_number(name: str):
    match = re.search(r"day_(\d+)(?:_(\d+))?\.py$", name)
    if not match:
        return (-1, -1)
    return (int(match.group(1)), int(match.group(2) or 0))


def read_title(path: Path) -> str:
    try:
        for line in path.read_text(encoding="utf-8").splitlines()[:20]:
            if line.startswith("# TITLE:"):
                return line.replace("# TITLE:", "", 1).strip()
    except OSError:
        pass
    return ""


def generate_commit_message(changes) -> str:
    """根据最新 Learn/day_*.py 生成默认提交说明。"""
    learn_files = []
    for line in changes:
        path = line[3:]
        p = Path(path)
        if len(p.parts) == 2 and p.parts[0] == "Learn" and p.name.startswith("day_") and p.suffix == ".py":
            learn_files.append(p)

    if not learn_files:
        return "Update Python learning notes"

    latest = max(learn_files, key=lambda p: parse_day_number(p.name))
    day_num = parse_day_number(latest.name)[0]
    title = read_title(ROOT / latest)
    if title:
        return f"Day {day_num}: {title}"
    return f"Day {day_num}: Python 学习记录"


def main():
    # 1. 运行 update_readme.py（如果存在）
    update_script = SCRIPT_DIR / "update_readme.py"
    if update_script.exists():
        run_cmd(["python3", str(update_script)], cwd=ROOT)
    else:
        print("提示：未发现 update_readme.py，跳过 README 自动更新。")

    # 2. 运行 organize_files.py / originize_files.py（如果存在）
    organize_candidates = ["organize_files.py", "originize_files.py"]
    ran_organize = False
    for name in organize_candidates:
        script_path = SCRIPT_DIR / name
        if script_path.exists():
            run_cmd(["python3", str(script_path)], cwd=ROOT)
            ran_organize = True
            break
    if not ran_organize:
        print("提示：未发现 organize_files.py / originize_files.py，跳过自动分类整理。")

    # 3. 检查是否有改动
    print("\n检查是否有需要提交的更改...")
    changes = get_included_changes()
    if not changes:
        print("没有检测到改动，Nothing to commit，结束。")
        return

    print("检测到以下改动：")
    print("\n".join(changes))

    # 4. 只暂存需要提交的改动
    stage_included_changes(changes)

    # 5. 询问提交信息
    default_msg = generate_commit_message(changes)
    try:
        msg = input(f"\n请输入本次提交说明（直接回车使用：{default_msg}）：").strip()
    except KeyboardInterrupt:
        print("\n已取消。")
        return

    if not msg:
        msg = default_msg

    # 6. git commit
    run_cmd(["git", "commit", "-m", msg], cwd=ROOT)

    # 7. git push
    run_cmd(["git", "push"], cwd=ROOT)

    print("\n✅ 自动提交并推送完成。")


if __name__ == "__main__":
    main()

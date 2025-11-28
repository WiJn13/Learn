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
import subprocess
import sys


ROOT = Path(__file__).resolve().parent


def run_cmd(cmd, cwd=None, check=True):
    """打印并运行命令"""
    print("\n$ " + " ".join(cmd))
    result = subprocess.run(cmd, cwd=cwd, text=True)
    if check and result.returncode != 0:
        print(f"命令执行失败：{' '.join(cmd)}，退出码 {result.returncode}")
        sys.exit(result.returncode)
    return result


def main():
    # 1. 运行 update_readme.py（如果存在）
    update_script = ROOT / "update_readme.py"
    if update_script.exists():
        run_cmd(["python3", str(update_script)])
    else:
        print("提示：未发现 update_readme.py，跳过 README 自动更新。")

    # 2. 运行 organize_files.py / originize_files.py（如果存在）
    organize_candidates = ["organize_files.py", "originize_files.py"]
    ran_organize = False
    for name in organize_candidates:
        script_path = ROOT / name
        if script_path.exists():
            run_cmd(["python3", str(script_path)])
            ran_organize = True
            break
    if not ran_organize:
        print("提示：未发现 organize_files.py / originize_files.py，跳过自动分类整理。")

    # 3. git add -A
    run_cmd(["git", "add", "-A"], cwd=ROOT)

    # 4. 检查是否有改动
    print("\n检查是否有需要提交的更改...")
    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    changes = status.stdout.strip()
    if not changes:
        print("没有检测到改动，Nothing to commit，结束。")
        return

    print("检测到以下改动：")
    print(changes)

    # 5. 询问提交信息
    try:
        msg = input("\n请输入本次提交说明（例如：Day 24: 类与对象）：").strip()
    except KeyboardInterrupt:
        print("\n已取消。")
        return

    if not msg:
        msg = "Auto update"

    # 6. git commit
    run_cmd(["git", "commit", "-m", msg], cwd=ROOT)

    # 7. git push
    run_cmd(["git", "push"], cwd=ROOT)

    print("\n✅ 自动提交并推送完成。")


if __name__ == "__main__":
    main()
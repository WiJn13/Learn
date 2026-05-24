import os
from pathlib import Path
from datetime import datetime, timezone, timedelta

from google import genai


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = ROOT / "today_quiz.md"

# 你可以按需要调整
MAX_FILES = 8
MAX_CHARS_PER_FILE = 6000

# 读取这些类型的文件
ALLOWED_SUFFIXES = {".py", ".md", ".txt"}

# 排除这些路径，避免读到无关内容
EXCLUDED_PARTS = {
    ".git",
    ".github",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
}
EXCLUDED_FILENAMES = {
    "generate_daily_quiz.py",
    "grade_issue_answer.py",
    "batch_rename_modules.py",
    "flag_days.py",
    "generate_index.py",
    "autopush.py",
}

def is_allowed_file(path: Path) -> bool:
    if path.suffix.lower() not in ALLOWED_SUFFIXES:
        return False

    # 排除隐藏/环境/工具目录
    if any(part in EXCLUDED_PARTS for part in path.parts):
        return False

    # scripts 是工具目录，不作为每日测验材料
    if "scripts" in path.parts:
        return False

    if path.name == "today_quiz.md":
        return False

    # 只读取 day_XX.py 这类学习文件
    if path.name.startswith("day_") and path.suffix.lower() == ".py":
        return True

    # 读取 README
    if path.name == "README.md":
        return True

    # 读取笔记目录
    if any(part in {"notes", "note", "笔记"} for part in path.parts):
        return True

    # 其他文件默认不读
    return False

def collect_recent_files() -> list[Path]:
    files = []

    for path in ROOT.rglob("*"):
        if path.is_file() and is_allowed_file(path):
            files.append(path)

    # 按最近修改时间排序，越新越靠前
    files.sort(key=lambda p: p.stat().st_mtime, reverse=True)

    return files[:MAX_FILES]


def read_file_safely(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            text = path.read_text(encoding="gbk")
        except Exception:
            return ""
    except Exception:
        return ""

    if len(text) > MAX_CHARS_PER_FILE:
        text = text[:MAX_CHARS_PER_FILE] + "\n\n【内容过长，后文已截断】"

    return text


def build_materials(files: list[Path]) -> str:
    parts = []

    for file in files:
        relative_path = file.relative_to(ROOT)
        content = read_file_safely(file)

        if not content.strip():
            continue

        parts.append(
            f"""
==============================
文件：{relative_path}
==============================
{content}
"""
        )

    return "\n".join(parts)


def build_prompt(materials: str) -> str:
    # GitHub Actions服务器通常是UTC，这里转北京时间
    beijing_time = datetime.now(timezone.utc) + timedelta(hours=8)
    today = beijing_time.strftime("%Y-%m-%d")

    return f"""
你是我的Python学习测验助手。

今天日期：{today}

下面是我最近修改的学习文件、代码和笔记。请你根据这些内容，自动判断我最近在学什么，然后生成一份每日小测。

要求：
1. 生成5道题。
2. 不要直接给答案。
3. 难度适合Python零基础到入门阶段。
4. 题目必须贴合我文件里的内容，不要泛泛而谈。
5. 优先考察我容易混淆的地方，包括但不限于：
   - 变量赋值
   - print输出
   - input输入
   - if判断
   - =和==的区别
   - 函数/类/实例/继承等概念，如果文件里出现了才考
6. 题型安排：
   - 第1题：概念理解题
   - 第2题：判断或选择题
   - 第3题：代码阅读题
   - 第4题：简单代码书写题
   - 第5题：综合理解题


输出格式如下：

# Python每日小测｜{today}

## 今日根据这些文件出题
- 文件1
- 文件2

## 测验题

1. ...


2. ...


---

下面是我的学习材料：

{materials}
"""


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("缺少环境变量 GEMINI_API_KEY，请在GitHub Secrets里添加。")

    files = collect_recent_files()
    materials = build_materials(files)

    if not materials.strip():
        quiz_text = """# Python每日小测

今天没有读取到可用的学习文件。

请检查仓库里是否有 `.py`、`.md` 或 `.txt` 文件。
"""
        OUTPUT_FILE.write_text(quiz_text, encoding="utf-8")
        print(quiz_text)
        return

    client = genai.Client(api_key=api_key)

    prompt = build_prompt(materials)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    quiz_text = response.text or "Gemini没有返回内容，请检查API状态或模型名称。"

    OUTPUT_FILE.write_text(quiz_text, encoding="utf-8")
    print(quiz_text)


if __name__ == "__main__":
    main()
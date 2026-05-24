import os
from google import genai


GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

ISSUE_TITLE = os.environ.get("ISSUE_TITLE", "")
ISSUE_BODY = os.environ.get("ISSUE_BODY", "")
COMMENT_BODY = os.environ.get("COMMENT_BODY", "")


def build_prompt() -> str:

    return f"""

你是我的Python学习老师。

下面是一次每日Python小测的题目，以及我在GitHub Issue评论区提交的内容。

请你先判断我的评论类型：

1. 如果评论中包含“## 我的答案”，说明我是在提交答案。请逐题批改。

2. 如果评论中包含“## 追问”，说明我是在追问某道题或某个知识点。请不要重新批改整套题，而是针对我的疑问进行解释。

3. 如果评论内容不完整，请指出需要我补充什么。

回答要求：

- 如果是批改答案：逐题判断正确 / 部分正确 / 错误，并给总分。

- 如果是追问：直接解释疑问，必要时举一个小例子。

- 语气认真、清楚，不要太官方。

- Python代码题要重点检查运行逻辑、变量变化、输出结果和语法。

- 不要因为表达不够书面就扣分，重点看理解是否正确。

输出格式：

## 批改结果

总分：x/5

### 第1题
判断：
说明：

### 第2题
判断：
说明：

### 第3题
判断：
说明：

### 第4题
判断：
说明：

### 第5题
判断：
说明：

## 需要复习的点
- ...
- ...

## 一道巩固题
...

下面是测验标题：
{ISSUE_TITLE}

下面是测验题目：
{ISSUE_BODY}

下面是我的答案：
{COMMENT_BODY}
"""


def main():
    if not GEMINI_API_KEY:
        raise RuntimeError("缺少环境变量 GEMINI_API_KEY，请在GitHub Secrets里添加。")

    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=build_prompt(),
    )

    result = response.text or "Gemini没有返回批改结果。"

    with open("grade_result.md", "w", encoding="utf-8") as f:
        f.write(result)

    print(result)


if __name__ == "__main__":
    main()
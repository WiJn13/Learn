import os
from google import genai


GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

ISSUE_TITLE = os.environ.get("ISSUE_TITLE", "")
ISSUE_BODY = os.environ.get("ISSUE_BODY", "")
COMMENT_BODY = os.environ.get("COMMENT_BODY", "")


def build_prompt() -> str:
    return f"""
你是我的Python学习批改老师。

下面是一次每日Python小测的题目，以及我在GitHub Issue评论区提交的答案。

请你批改我的答案。

要求：
1. 逐题判断：正确 / 部分正确 / 错误。
2. 每题都要说明原因。
3. 如果我概念混淆，要直接指出。
4. 语气认真、清楚，但不要太官方。
5. 最后给出总分，例如：4/5。
6. 最后列出我最需要复习的2-4个点。
7. 如果我的答案太简略，可以根据上下文判断，但要说明哪里不够完整。
8. 不要重新出题，除非最后给1道很短的巩固题。
9. 如果题目或答案里有代码，重点检查运行逻辑、变量变化、输出结果和语法。
10. 不要因为表达不够书面就扣分，重点看理解是否正确。

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
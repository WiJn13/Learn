import os
from google import genai


PRIMARY_MODEL = "gemini-3.5-flash"
FALLBACK_MODEL = "gemini-2.5-flash"

ISSUE_TITLE = os.environ.get("ISSUE_TITLE", "")
ISSUE_BODY = os.environ.get("ISSUE_BODY", "")
COMMENT_BODY = os.environ.get("COMMENT_BODY", "")
ISSUE_COMMENTS = os.environ.get("ISSUE_COMMENTS", "")


def detect_comment_type(comment_body: str) -> str:
    text = comment_body.strip()

    if "巩固题回答" in text:
        return "consolidation_answer"

    if "我的答案" in text or "小测答案" in text:
        return "quiz_answer"

    if "追问" in text:
        return "follow_up"

    return "unknown"


def build_prompt() -> str:
    comment_type = detect_comment_type(COMMENT_BODY)

    return f"""
你是我的Python学习老师。

下面是一次每日Python小测的题目、Issue历史评论，以及我最新提交的评论。

请你根据“评论类型”处理，不要混淆原小测和巩固题。

评论类型：
{comment_type}

判断规则：

1. 如果评论类型是 quiz_answer：
说明我是在提交原小测答案。
请根据“每日Python小测题目”逐题批改。

2. 如果评论类型是 consolidation_answer：
说明我是在回答上一次批改后生成的“巩固题”。
请从“Issue历史评论”里找到最近一次AI生成的“## 一道巩固题”，然后只批改这道巩固题。
不要重新批改原小测。
如果历史评论里找不到巩固题，请明确说明：没有找到巩固题题目，无法准确批改。

3. 如果评论类型是 follow_up：
说明我是在追问某道题或某个知识点。
请不要重新批改整套题，也不要重新出题，只针对我的疑问解释。

4. 如果评论类型是 unknown：
说明我的评论没有明确标记。
请提醒我在评论开头加：
- ## 我的答案
- ## 巩固题回答
- ## 追问

回答要求：

- 如果是批改原小测：逐题判断正确 / 部分正确 / 错误，并给总分。
- 如果是批改巩固题：只批改巩固题，不要给原小测总分。
- 如果是追问：直接解释疑问，必要时举一个小例子。
- 语气认真、清楚，不要太官方。
- Python代码题要重点检查运行逻辑、变量变化、输出结果和语法。
- 不要因为表达不够书面就扣分，重点看理解是否正确。

如果是批改原小测，输出格式：

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

回答巩固题时，请在评论开头写：## 巩固题回答

如果是批改巩固题，输出格式：

## 巩固题批改

判断：
说明：

## 需要注意的点
- ...

## 下一道巩固题
...

回答巩固题时，请在评论开头写：## 巩固题回答

如果是追问，输出格式：

## 解释

...

## 小例子

...

下面是测验标题：
{ISSUE_TITLE}

下面是每日Python小测题目：
{ISSUE_BODY}

下面是Issue历史评论：
{ISSUE_COMMENTS}

下面是我最新提交的评论：
{COMMENT_BODY}
"""


def generate_content_with_fallback(client, prompt: str):
    model = os.environ.get("GEMINI_MODEL") or PRIMARY_MODEL

    try:
        return client.models.generate_content(
            model=model,
            contents=prompt,
        )
    except Exception:
        if model == FALLBACK_MODEL:
            raise

        return client.models.generate_content(
            model=FALLBACK_MODEL,
            contents=prompt,
        )


def main():
    gemini_api_key = os.environ.get("GEMINI_API_KEY")

    if not gemini_api_key:
        raise RuntimeError("缺少环境变量 GEMINI_API_KEY，请在GitHub Secrets里添加。")

    client = genai.Client(api_key=gemini_api_key)

    response = generate_content_with_fallback(client, build_prompt())

    result = response.text or "Gemini没有返回批改结果。"

    with open("grade_result.md", "w", encoding="utf-8") as f:
        f.write(result)

    print(result)


if __name__ == "__main__":
    main()

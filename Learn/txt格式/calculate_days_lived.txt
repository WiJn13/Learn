"""
计算你活了多少天的小工具

用法示例：
- 交互模式（运行后输入出生日期）：
    python calculate_days_lived.py

- 命令行参数（一次运行直接给出生日期）：
    python calculate_days_lived.py --birth 1990-01-01
    python calculate_days_lived.py -b 1990/01/01

支持的日期格式（宽松）：YYYY-MM-DD, YYYY/MM/DD, YYYY.MM.DD

输出会显示从出生日期到“今天”之间相差的天数（不含时分秒）。
如果出生日期在今天之后，会提示错误。
"""

from datetime import date, datetime
import argparse
import sys

SUPPORTED_FORMATS = ["%Y-%m-%d", "%Y/%m/%d", "%Y.%m.%d"]


def parse_birth_date(s: str) -> date:
    """尝试用多种格式解析出生日期字符串，成功返回 date 对象，失败抛 ValueError。"""
    s = s.strip()
    last_exc = None
    for fmt in SUPPORTED_FORMATS:
        try:
            return datetime.strptime(s, fmt).date()
        except Exception as e:
            last_exc = e
    raise ValueError(f"无法解析的日期格式: '{s}'. 支持的格式例如 1990-01-01 或 1990/01/01")


def days_lived(birth: date, today: date = None) -> int:
    """返回从出生日期(birth)到 today 的天数差（整数天）。
    公式：(today - birth).days
    注意：如果 birth > today 会抛 ValueError。
    """
    if today is None:
        today = date.today()
    if birth > today:
        raise ValueError("出生日期在今天之后，请检查输入。")
    delta = today - birth
    return delta.days


def main(argv=None):
    parser = argparse.ArgumentParser(description="计算活了多少天")
    parser.add_argument("-b", "--birth", help="出生日期，格式 YYYY-MM-DD 或 YYYY/MM/DD（可选）")
    args = parser.parse_args(argv)

    if args.birth:
        try:
            bd = parse_birth_date(args.birth)
        except ValueError as e:
            print("错误：", e)
            sys.exit(2)
    else:
        # 交互式读取
        txt = input("请输入你的出生日期（例如 1990-01-01）: ")
        try:
            bd = parse_birth_date(txt)
        except ValueError as e:
            print("错误：", e)
            sys.exit(2)

    try:
        n = days_lived(bd)
    except ValueError as e:
        print("错误：", e)
        sys.exit(2)

    print()
    print(f"出生日期: {bd.isoformat()}")
    print(f"今天日期: {date.today().isoformat()}")
    print(f"恭喜你活了{n}天!!!\n你很了不起!!!")



if __name__ == '__main__':
    main()

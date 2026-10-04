#!/usr/bin/env python3
"""按主题文件及独立学习顺序生成索引，不执行学习程序。"""
from update_readme import collect_items, render_index_block


def main():
    print(render_index_block(collect_items()))


if __name__ == "__main__":
    main()

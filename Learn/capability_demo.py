from typing import List, Any, Callable, Iterable
import sys

def analyze_list_comprehension(data: Iterable[int]) -> List[int]:
    """
    【底层实现】：
    列表推导式在 CPython 中被编译为独立的 code object。
    相比于显式的 for 循环调用 list.append()，它利用了 LIST_APPEND 字节码指令，
    该指令直接操作 C 层次的列表对象，规避了 Python 层次的方法查找开销。
    
    【内存追踪】：
    1. 创建一个新的 PyListObject。
    2. 预估（或动态调整）内存空间。
    3. 迭代过程中，对象的引用计数增加。
    
    【比喻模型】：
    普通 for 循环像是在超市里每买一件商品就跑一次收银台；
    列表推导式则是推着购物车一次性结算。
    """
    if not isinstance(data, Iterable):
        raise TypeError(f"Expected Iterable, got {type(data).__name__}")
    
    # 强制类型校验与防御性编程
    return [int(x) ** 2 for x in data if isinstance(x, (int, float))]

def demonstrate_sort_mechanism() -> None:
    """
    【底层实现】：
    Python 的 sort 使用 Timsort 算法（结合了归并排序和插入排序）。
    key 参数指定的函数在排序开始前对每个元素调用一次，结果被“装饰”在原始对象旁。
    
    【内存追踪】：
    CPython 内部会创建一个临时数组存储 (key_value, original_value) 的对，
    排序完成后再提取 original_value，这被称为 DSU (Decorate-Sort-Undecorate) 模式。
    """
    raw_data: List[tuple[str, int]] = [('Eben', 22), ('WiJn', 21), ('Mac', 30)]
    
    # 使用 context manager 模拟资源监控（此处仅为演示架构思维）
    try:
        # 原地排序：引用关系在原 PyListObject 的 ob_item 数组中重新排列
        raw_data.sort(key=lambda x: x[1])
        print(raw_data)
    except Exception as e:
        print(f"Sort failed: {e}")

if __name__ == "__main__":
    # 1. 列表推导式深度演示
    result = analyze_list_comprehension([1, 2, 3, 4])
    print(result)
    
    # 2. 排序机制演示
    demonstrate_sort_mechanism()
    
    # 3. 内存对象大小观察
    empty_list: List[Any] = []
    print(sys.getsizeof(empty_list))  # 打印空列表的基础内存开销（字节）

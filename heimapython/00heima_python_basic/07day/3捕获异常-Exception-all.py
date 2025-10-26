try:
    # 任何可能出错的代码
    list_data = [1, 2, 3]
    print(list_data[10])  # 触发IndexError（列表索引越界）
except Exception as e:
    # 处理所有异常（通用方案）
    print(f"程序出错：{e}")  # 输出：list index out of range
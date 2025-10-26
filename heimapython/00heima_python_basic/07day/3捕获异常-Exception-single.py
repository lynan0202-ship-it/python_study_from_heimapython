try:
    print(name)  # 使用未定义的变量，触发NameError
except NameError as e:
    # 仅处理NameError类型的异常
    print(f"处理NameError：{e}")  # 输出：name 'name' is not defined
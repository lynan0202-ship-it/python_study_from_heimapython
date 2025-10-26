try:
    # 可能触发多种异常的代码
    #print(10 // 0)  # 触发ZeroDivisionError
    #print(name)     # 触发NameError
    open("1.txt", "r")  # 触发FileNotFoundError
except (ZeroDivisionError, NameError, FileNotFoundError) as e:
    # 处理多种指定异常
    print(f"发生已知异常：{e}")
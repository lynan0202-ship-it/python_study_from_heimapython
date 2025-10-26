# 演示异常的传递路径
def func1():
    print("----- func1 开始 -----")
    print(10 // 0)  # 触发除零异常
    print("----- func1 结束 -----")  # 不会执行

def func2():
    print("----- func2 开始 -----")
    func1()  # 调用func1，会接收其传递的异常
    print("----- func2 结束 -----")  # 若异常未处理，不会执行

def func3():
    print("----- func3 开始 -----")
    func2()  # 接收func2传递的异常
    print("----- func3 结束 -----")  # 若异常未处理，不会执行

if __name__ == "__main__":
    try:
        func3()  # 接收func3传递的异常
    except ZeroDivisionError:
        print("在main中捕获到异常：除数不能为0")
    print("程序继续执行")
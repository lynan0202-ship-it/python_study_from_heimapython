# 模块：calc.py
def add(a, b):
    c=a+b
    print('a+b=',c)
    return a + b


# 只有自己运行时，才执行测试
print("不经过-name-限制的部分")
if __name__ == "__main__":
    print("我自己跑啦！测试add(2,3)的结果：", add(2,3))  # 输出5
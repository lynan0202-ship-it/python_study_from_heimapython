# 定义函数：计算n的阶乘
def factorial(n):
    # 出口：n=1时，直接返回1（不用再拆了）
    if n == 1:
        return 1
    # 规律：n! = n × (n-1)!，自己调用自己算(n-1)!
    print (f'return= {n} * factorial({n})')
    return n * factorial(n - 1)

# 测试：计算5的阶乘
if __name__ == '__main__':
    print(factorial(5))  # 输出：120（因为5! = 5×4×3×2×1=120）
'''
递归虽然代码简洁，但可能重复计算。比如斐波那契数列中，计算get_rabbit(5)时，get_rabbit(3)被算了两次，get_rabbit(2)被算了三次……月份越大，重复越多，效率越低。

解决办法：记忆化递归
用字典存已经算过的结果，避免重复计算：

'''
# 用字典缓存计算结果（键=月份，值=对数）
memo = {1: 1, 2: 1}

def get_rabbit_optimized(m):
    if m in memo:  # 已经算过，直接返回缓存的值
        return memo[m]
    # 没算过，计算后存到缓存
    result = get_rabbit_optimized(m-1) + get_rabbit_optimized(m-2)
    memo[m] = result
    return result

print(get_rabbit_optimized(100))  # 优化后能算很大的月份，不会卡
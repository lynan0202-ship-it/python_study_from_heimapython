"""
三元(三目)表达式介绍:
    概述:
        它是一种特殊写法, 可以用来优化 if.else 的操作.
    格式:
        值1 if 判断条件 else 值2
    执行流程:
        1. 先执行判断条件, 看其结果是否成立.
        2. 成立就返回 值1
        3. 不成立就返回 值2
"""

# 需求1: 获取两个整数的最大值.


a, b = 10, 31
if a >= b:
    max_num = a  # 用max_num替代max，避免冲突
else:
    max_num = b
print(f'最大值为: {max_num}')  # 输出：最大值为: 31
# 方式2: 三元表达式.
max2 = a if a > b else b

print(f'最大值为: {max2}')

"""
1. 功能层面：能正确输出结果
代码中通过 if-else 逻辑给变量 max 赋了值（a 和 b 中的较大值）：
当 a=10、b=31 时，b 更大，因此 max 被赋值为 31。
f-string 会解析 {max} 中的变量，最终输出 最大值为: 31，完全符合 “获取两个整数最大值并打印” 的需求。
"""
# 扩展: 三元表达式嵌套.
# 需求: 求3个整数的最大值.
c, d, e = 10, 20, 15

# 场景1: if.else实现
if c >= d:
    # c大, 比较 c 和 e
    if c >= e:
        max = c
    else:
        max = e
else:
    # d大, 比较 d 和 e
    if d >= e:
        max = d
    else:
        max = e
print(f'最大值为: {max}')

# 场景2: 用三元搞定.
# max2 = c大 if c >= d else d大

#          比较 C 和 E          比较 C 和 D       比较 D 和 E
max2 = (c if c >= e else e) if c >= d else (d if d >= e else e)      # 小括号可以省略.
max3 = c if c >= e else e if c >= d else d if d >= e else e      # 小括号可以省略.
print(f'最大值为: {max2}')
print(f'最大值为: {max3}')
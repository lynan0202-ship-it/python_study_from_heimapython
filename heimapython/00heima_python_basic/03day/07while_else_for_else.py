"""
循环 + else语法:
    概述:
        else语句除了可以和 if语句结合使用外, 还可以和 循环一起使用.
    格式:
        while 或者 for循环:
            循环体
        else:
            语句体
    执行特点:
        1. 只要循环是正常退出的, 就一定会执行 else中的内容.
        2. 循环正常退出 指的是 非break的方式跳出.
        3. 大白话: 只要循环不是break方式跳出的, 就会走else的内容, 否则不执行else的内容.
"""

# 需求1: 演示 for + else语句.
for i in range(1, 11):      # i的值: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if i % 3 == 0:
        # continue            # 结束本次循环, 进行下次循环的.
        break
    print(f'hello world! {i}')
else:
    print('我是else, 看看我执行了吗?')

print('else没有执行直接被breakout了')

"""
在for + else结构中，break的作用确实是针对整个f
or循环的 —— 当break被触发时，它会直接终止整个for循环的执行（包括后续所有迭代），并且会导致else块不执行。

"""
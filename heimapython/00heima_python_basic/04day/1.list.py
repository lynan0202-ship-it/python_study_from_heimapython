# 定义列表的三种方式
list1 = [10, 20.3, True, 'abc']  # 直接定义
list2 = list()                    # 使用list()函数
list3 = []                        # 空列表语法糖

print(f'列表内容: {list1}')        # [10, 20.3, True, 'abc']
print(f'数据类型: {type(list1)}')   # <class 'list'>
print(f'列表内容: {list2}')
print(f'列表内容: {list3}')
print(f'列表内容：{type(list2)}')

# 列表索引（从0开始）
fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits[1])
print(fruits[0:3])
print(fruits[-1:-3:-1])
print(fruits.index('banana'))

print(fruits[1:3])    # ['banana', 'cherry'] - 包左不包右
print(fruits[:2])     # ['apple', 'banana']  - 从头开始
print(fruits[2:])     # ['cherry', 'date']   - 到末尾结束
numbers = [11, 22, 33, 44, 55]

# 直接遍历元素
for num in numbers:
    print(f'当前数字: {num}')
"""
在 Python 中，使用 for num in numbers 这种方式遍历列表时，之所以不需要 “初始化”，是因为这种循环本质是迭代器遍历，Python 解释器会自动处理循环变量的初始化和更新过程。
具体来说：
列表 numbers 是一个 “可迭代对象”，当你用 for...in 循环遍历它时，Python 会自动创建一个迭代器，负责从列表中依次取出元素。
循环变量 num 不需要提前定义或初始化，每次循环时，迭代器会自动将列表中的下一个元素赋值给 num（第一次循环赋值 11，第二次 22，以此类推）。
这种机制是 Python 简化循环语法的设计：它隐藏了底层迭代器的初始化、元素获取、循环终止判断等细节，让开发者更专注于 “要对每个元素做什么”，而不是 “如何控制循环过程”。
如果对比其他语言（比如 C 语言）的 for (i=0; i<len; i++) 循环，会发现 Python 的 for...in 把 i 的初始化（i=0）、更新（i++）、边界判断（i<len）都自动完成了，所以不需要手动写初始化代码。
"""


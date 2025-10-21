"""
扩展题:
    需求1: 删除列表中的重复元素, 只保留1个.
        [10, 20, 30, 10, 30]        =>   [10, 20, 30]

    需求2: 键盘录入字符串, 接收并存储到列表中. 直至用户录入 end, 结束录入. 判断其中是否有 abc 这个字符串, 有就全部删除.
        [10, 20, 'abc', 'abc', 10.3, 'abc', 'bcd']     =>   至少2种解题思路.


"""
"""
list1 = [10, 20, 30, 10, 30]
for element in list1:
    list1.remove(element)
    for element2 in list1:
        if element == element2:
            print(f'{element} 重复需要去除')

print(list1)
"""
"""
list.remove() 无返回值：list1.remove(element) 会直接修改原列表，但返回值是 None，因此 list2 会被赋值为 None，后续遍历 list2 会报错（'NoneType' is not iterable）。
遍历列表时修改列表：在 for element in list1 循环中删除元素，会导致列表长度和元素位置动态变化，遍历逻辑混乱（会跳过部分元素）。
重复判断逻辑错误：原代码试图通过 list2 对比元素，但 list2 本身无效，无法实现重复检测。
"""
list1 = [10, 20, 30, 10, 30]
seen = set()  # 记录已出现过的元素
i = 0  # 用索引控制遍历

while i < len(list1):
    element = list1[i]
    if element in seen:
        # 元素重复，打印提示并删除
        print(f'{element} 重复需要去除')
        del list1[i]  # 删除当前索引的元素（后续元素会自动前移，索引无需+1）
    else:
        # 元素首次出现，加入集合，索引+1继续遍历
        seen.add(element)
        i += 1

print(list1)  # 输出：[10, 20, 30]
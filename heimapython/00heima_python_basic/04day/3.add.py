"""
列表相关操作介绍:
    概述:
        列表的相关操作主要指的是 CURD(增删改查), 以及常用的 公共运算符 和 函数等.
    列表 增(添加元素) 相关操作如下:
        列表名.append(单个值 或者 列表)       在列表末尾添加元素, 如果(添加的内容)是列表, 则是把列表当做1个元素, 来添加的.
        列表名.extend(列表)                 在列表末尾添加元素, 如果(添加的内容)是列表, 则是把列表中逐个元素添加过来.
        列表名.insert(索引值, 要插入的元素)    在指定的位置插入元素, 如果索引不存在, 就默认往 "最后" 添加.
    结论:
        列表 是 可变类型, 即: 其中的元素值时可以变化的.
"""
list1=[1,2,3,4]
list2=[5,6,7]
list1.append(8)
print(list1)
list1.append(list2)
print(list1)
list1.extend(list2)
print(list1)
list1.insert(2,0)
print(list1)
list1.insert(2,list2)
print(list1)

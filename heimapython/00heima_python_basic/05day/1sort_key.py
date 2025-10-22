list1=[11,33,44,55]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

LIST2=['BC','CBD','AJ','AHSD']
LIST2.sort()
print(LIST2)
'''
[11, 33, 44, 55]
[55, 44, 33, 11]
['AHSD', 'AJ', 'BC', 'CBD']
按照首字母大小排列
'''

LIST2.sort(key=len)  # 会先用len()函数计算每个字符串的长度, 然后按照结果(长度)排序
print(LIST2)
LIST2.sort(key=len, reverse=True)  # 会先用len()函数计算每个字符串的长度, 然后按照结果(长度)排序
print(LIST2)
'''
['AJ', 'BC', 'CBD', 'AHSD']
['AHSD', 'CBD', 'AJ', 'BC']
'''

list3 = [(1, 3), (2, 2), (5, 1), (3, 9)]
list3.sort()
print(list3)
'''
[(1, 3), (2, 2), (3, 9), (5, 1)]
'''
## 该函数接收1个元组, 然后返回该元组的 第2个元素(即: 索引为1的元素)
def get_data(t1):
    return t1[1] #
list3.sort(key=get_data) # key参数接收的是1个函数, 该函数会做用到列表中的每个元素.
print(list3)
'''
[(5, 1), (2, 2), (1, 3), (3, 9)]
'''
def get_data(t1):
    return t1[1] #
list3.sort(key=get_data, reverse=True)
'''
[(3, 9), (1, 3), (2, 2), (5, 1)]
'''
print(list3)
list3.sort(reverse=True)
print(list3)
'''
[(5, 1), (2, 2), (1, 3), (3, 9)]
[(5, 1), (3, 9), (2, 2), (1, 3)]
'''
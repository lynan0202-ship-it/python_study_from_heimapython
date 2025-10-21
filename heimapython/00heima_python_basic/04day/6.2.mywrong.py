list1 = [10, 20, 30, 10, 30]
list2 = [10, 20, 30, 10, 30]
repeater=[]
for element in list1:
    list2.remove(element)
    for element2 in list2:
        if element == element2:
            print(f'{element} 重复需要去除')
            repeater.append(element2)
print(repeater)
for element in repeater:
    list1.remove(element)
print(list1)
"""
[10, 30]
[20, 10, 30]
"""
"""
list1 = [10, 20, 30, 10, 10, 30]
list2 = [10, 20, 30, 10, 10, 30]
repeater=[]
for element in list1:
    list2.remove(element)
    for element2 in list2:
        if element == element2:
            print(f'{element} 重复需要去除')
            repeater.append(element2)
print(repeater)
for element in repeater:
    list1.remove(element)
print(list1)
10 重复需要去除
10 重复需要去除
30 重复需要去除
10 重复需要去除
[10, 10, 30, 10]
[20, 30]

进程已结束，退
"""
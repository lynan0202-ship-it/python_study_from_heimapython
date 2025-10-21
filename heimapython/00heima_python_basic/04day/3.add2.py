list1 = [1,2,3,4]
list2 = [5,6,7]

# 第一次操作：复制list1得到副本，再append(8)
copy1 = list1[:]  # 复制原list1
copy1.append(8)
print("第一次操作后的副本：", copy1)  # [1,2,3,4,8]
print("原list1：", list1)  # [1,2,3,4]（不变）

# 第二次操作：基于上一个副本再复制，append(list2)
copy2 = copy1[:]  # 复制copy1
copy2.append(list2)
print("第二次操作后的副本：", copy2)  # [1,2,3,4,8, [5,6,7]]
print("原list1：", list1)  # [1,2,3,4]（仍不变）

# 后续操作以此类推：每次基于前一个副本复制，再修改新副本
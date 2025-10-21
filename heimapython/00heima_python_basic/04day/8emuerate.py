fruits = ["apple", "banana", "orange"]
i = 0
for fruit in fruits:
    print(f"索引 {i}：{fruit}")  # 索引 0：apple；索引 1：banana...
    i += 1  # 手动维护索引，繁琐且易漏写

fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"索引 {index}：{fruit}")  # 结果同上，但无需手动维护i
'''
索引 0：apple
索引 1：banana
索引 2：orange
索引 0：apple
索引 1：banana
索引 2：orange
'''

# 机器人关节列表，从1开始编号更直观
joints = ["肩关节", "肘关节", "腕关节"]
for num, joint in enumerate(joints, start=1):
    print(f"关节 {num}：{joint}")  # 关节 1：肩关节；关节 2：肘关节...
'''
关节 1：肩关节
关节 2：肘关节
关节 3：腕关节
'''

# 机器人关节列表，从1开始编号更直观
joints = ["肩关节", "肘关节", "腕关节"]
for num, joint in enumerate(joints, start=2):
    print(f"关节 {num}：{joint}")  # 关节 1：肩关节；关节 2：肘关节...

'''
关节 2：肩关节
关节 3：肘关节
关节 4：腕关节

'''
# 3D点云：每个元素是一个点的(x,y,z)坐标
point_cloud = [[1.2, 3.4, 2.1], [2.5, 4.1, 3.3], [0.8, 2.9, 1.7]]

# 用enumerate获取每个点的索引（序号）和坐标
for point_idx, (x, y, z) in enumerate(point_cloud):
    print(f"点 {point_idx}：x={x}, y={y}, z={z}")
'''
点 0：x=1.2, y=3.4, z=2.1
点 1：x=2.5, y=4.1, z=3.3
点 2：x=0.8, y=2.9, z=1.7
'''
nums = [10, 20, 30]
enum_list = list(enumerate(nums))
print(enum_list)  # [(0, 10), (1, 20), (2, 30)]

# 自定义start=5
enum_list2 = list(enumerate(nums, start=5))
print(enum_list2)  # [(5, 10), (6, 20), (7, 30)]在Python中，`enumerate` 是一个**内置函数**，核心作用是：**遍历可迭代对象（如列表、元组、字符串等）时，同时获取每个元素的「索引」和「值」**，避免手动维护索引变量，让代码更简洁、不易出错。

'''
[(0, 10), (1, 20), (2, 30)]
[(5, 10), (6, 20), (7, 30)]
'''
# 点云处理中的矩阵操作示例：结合嵌套列表、索引和enumerate
# 场景：对3个3D点云依次执行剪切变换和平移变换


# 1. 原始点云数据（嵌套列表存储）
# 外层列表：所有点的集合；内层子列表：单个点的[x, y, z]坐标
# 索引说明：point_cloud[i][0] → 第i个点的x坐标，[i][1]→y坐标，[i][2]→z坐标
point_cloud = [
    [1.0, 2.0, 3.0],  # 点0
    [4.0, 5.0, 6.0],  # 点1
    [7.0, 8.0, 9.0]  # 点2
]
print("原始点云：")
for point in point_cloud:
    print(f"  {point}")  # 输出：[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]

# 2. 定义变换矩阵（嵌套列表/列表存储）
# 2.1 剪切矩阵（3x3二维嵌套列表）：沿x轴剪切y分量（剪切系数0.5）
# 矩阵数学形式：
# [ [1, 0.5, 0],   → x' = 1*x + 0.5*y + 0*z
#   [0, 1, 0],     → y' = 0*x + 1*y + 0*z
#   [0, 0, 1] ]    → z' = 0*x + 0*y + 1*z
# 索引说明：shear_matrix[row][col] → 第row行第col列的系数
shear_matrix = [
    [1.0, 0.5, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
]

# 2.2 平移矩阵（一维列表）：x方向+2，y方向+3，z方向+1
# 索引说明：translation[0]→x平移量，[1]→y平移量，[2]→z平移量
translation = [2.0, 3.0, 1.0]

# 3. 执行剪切变换（利用索引提取坐标和矩阵元素）
sheared_points = []  # 存储剪切后的点云（嵌套列表）
for point in point_cloud:
    # 用索引提取点的x, y, z分量（等价于x = point[0], y = point[1], z = point[2]）
    x, y, z = point

    # 矩阵乘法计算剪切后坐标（通过矩阵行索引和列索引定位系数）
    new_x = shear_matrix[0][0] * x + shear_matrix[0][1] * y + shear_matrix[0][2] * z
    new_y = shear_matrix[1][0] * x + shear_matrix[1][1] * y + shear_matrix[1][2] * z
    new_z = shear_matrix[2][0] * x + shear_matrix[2][1] * y + shear_matrix[2][2] * z

    sheared_points.append([new_x, new_y, new_z])  # 存入嵌套列表

print("\n剪切变换后点云：")
for point in sheared_points:
    print(f"  {point}")  # 输出：[2.0, 2.0, 3.0], [6.5, 5.0, 6.0], [11.0, 8.0, 9.0]

# 4. 执行平移变换（利用索引提取平移分量）
transformed_points = []  # 存储最终变换后的点云（嵌套列表）
for point in sheared_points:
    x, y, z = point
    # 用索引提取平移量并计算最终坐标
    final_x = x + translation[0]  # x方向平移
    final_y = y + translation[1]  # y方向平移
    final_z = z + translation[2]  # z方向平移
    transformed_points.append([final_x, final_y, final_z])

print("\n平移变换后最终点云：")
for point in transformed_points:
    print(f"  {point}")  # 输出：[4.0, 5.0, 4.0], [8.5, 8.0, 7.0], [13.0, 11.0, 10.0]

# 5. 用enumerate跟踪每个点的序号（关联原始点与变换后点）
print("\n各点变换过程对比：")
# zip将三个点云按顺序打包，enumerate获取每个点的索引（序号）
for idx, (original, sheared, final) in enumerate(zip(point_cloud, sheared_points, transformed_points)):
    print(f"点{idx}：")
    print(f"  原始坐标：{original}")
    print(f"  剪切后：{sheared}")
    print(f"  最终坐标：{final}\n")
    '''
    原始点云：
  [1.0, 2.0, 3.0]
  [4.0, 5.0, 6.0]
  [7.0, 8.0, 9.0]

剪切变换后点云：
  [2.0, 2.0, 3.0]
  [6.5, 5.0, 6.0]
  [11.0, 8.0, 9.0]

平移变换后最终点云：
  [4.0, 5.0, 4.0]
  [8.5, 8.0, 7.0]
  [13.0, 11.0, 10.0]

各点变换过程对比：
点0：
  原始坐标：[1.0, 2.0, 3.0]
  剪切后：[2.0, 2.0, 3.0]
  最终坐标：[4.0, 5.0, 4.0]

点1：
  原始坐标：[4.0, 5.0, 6.0]
  剪切后：[6.5, 5.0, 6.0]
  最终坐标：[8.5, 8.0, 7.0]

点2：
  原始坐标：[7.0, 8.0, 9.0]
  剪切后：[11.0, 8.0, 9.0]
  最终坐标：[13.0, 11.0, 10.0]
    '''
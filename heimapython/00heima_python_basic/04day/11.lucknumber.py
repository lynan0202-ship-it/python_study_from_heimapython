"""
需求:
    输入任意的数字, 然后生成 1 ~ 该数字之间额列表, 从中选取幸运数字(能被6整除的)移动到新列表 lucky, 并打印两个列表.
"""
nums=[]
luckynum=[]
input_num=int(input('请录入1个大于0的数'))
for i in range(input_num):
    nums.append(i)
print(nums)
for num in nums:
    if num % 6 == 0:
        luckynum.append(num)
print(luckynum)

'''
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 6]
'''
# 合并版, 列表推导式.
# 1. 提示用户键盘录入1个值, 并接收. 细节: 转成int类型.
input1_num = int(input('请录入1个大于0的整数: '))     # 例如: 9

# 2. 生成 1 ~ 用户录入的数字之间的 数字列表.
nums1 = [i for i in range(1, input1_num + 1)]

# 3. 从上述的 nums列表中, 找到 幸运数字.
lucky1 = [i for i in nums1 if i % 6 == 0]


# 7. 打印 nums 和 lucky两个列表的信息.
print(f'nums: {nums1}')
print(f'lucky: {lucky1}')

'''
请录入1个大于0的数34
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
[0, 6, 12, 18, 24, 30]
请录入1个大于0的整数: 25
nums: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
lucky: [6, 12, 18, 24]

'''
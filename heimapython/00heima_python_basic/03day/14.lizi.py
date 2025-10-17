# 案例1: 输入1个字符串, 打印所有偶数位上的字符. 例如: 下标是 0, 2, 4, 6, 8, 10...

# # 1. 键盘录入1个字符串, 并接收.
# s1 = input('请录入您要操作的字符串: ')   # 假设: abcde
#
# # 2. for循环方式, 获取到 字符串中所有 偶数索引.
# for i in range(0, len(s1), 2):
#     # 3. 根据上述获取到的索引, 打印其对应的元素即可.
#     print(s1[i])
#
# print("-" * 28)


# 案例2: 给定一个文件名，判断其尾部是否以".png"结尾
# 1. 定义变量, 记录: 文件名
file_name = 'abc.123.txt.png'

# 方式1: 切片思路实现, 即: 只切割出最后的4个字符, 比较是否是: .png
# 2. 获取文件名 最后的 4个字符.
end_name =  file_name[-4:]

# 3. 判断, 并提示.
if end_name == '.png' and len(file_name) > 4:
    print('文件名 是 以.png结尾的')
    print(file_name)
    print(end_name)
    print(len(file_name))
else:
    print('文件名 不是 以.png结尾的')

# 方式2: 索引方式实现, 即: 通过rfind()找到 最后1个 .的索引, 然后做操作.

"""
文件名 是 以.png结尾的
abc.123.txt.png
.png
15

"""
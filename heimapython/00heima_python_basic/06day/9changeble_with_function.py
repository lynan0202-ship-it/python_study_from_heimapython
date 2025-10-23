'''

不可变类型作为函数参数：函数内修改参数值，不会影响外部变量（因为创建了新对象）。
可变类型作为函数参数：函数内修改参数值，会影响外部变量（因为修改的是原对象）。
'''

# 不可变类型参数
def change_num(n):
    n = 100  # 内部修改，创建新对象
    print("函数内n：", n)

num = 10
change_num(num)
print("函数外num：", num)  # 输出：10（外部变量未变）

# 可变类型参数
def change_list(l):
    l.append(4)  # 内部修改原对象
    print("函数内list：", l)

my_list = [1, 2, 3]
change_list(my_list)
print("函数外my_list：", my_list)  # 输出：[1, 2, 3, 4]（外部变量被修改）

'''
函数内n： 100
函数外num： 10
函数内list： [1, 2, 3, 4]
函数外my_list： [1, 2, 3, 4]
'''
# 案例2: 上网案例, 键盘录入年龄并接收, 判断是否可以上网. 即: 年龄大于或者等于18岁, 可以上网.
# 1. 键盘录入年龄并接收.
age_str = input('请录入您的年龄: ')
# 2. 把上述的年龄转成 => int类型
age1 = eval(age_str)     # '20' -> 20
print(age1)
# 合并版写法.
age2 = eval(input('请录入您的年龄: '))

print(age2)

print(eval(input('请录入您的年龄: ')))#嵌套举例
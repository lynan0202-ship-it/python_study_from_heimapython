
# 准备动作, 定义多个变量值.
name = '威震天'
age = 99
salary = 1000.1235
flag = True  # 标记是否是反派, True: 是, False: 不是

# 演示 1. 输出单个值.
print('我的姓名是: ' + name)
print(age)
# print('我的年龄是: ' + age)      # 报错, Python中 字符串 和 整数不能进行 加法运算(拼接操作)
print('-' * 28)

# 演示 2. 同时输出多个值.
print(name, age, salary, flag)
print('-' * 28)

# 演示 3. 换行输出 和 不换行输出.
# 换行输出
print('hello')
print('world')
print('name' * 28)
print(name * 28)
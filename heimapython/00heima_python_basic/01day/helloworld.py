print("hello world")
"""
注释
print("注释不会运行")
"""

#单行注释

"""
没有黑色的注释
"""
print("a")
a=100
print(a)
d='刘亦菲'
a=10
b=10.3
c=True
e='胡歌'
f="“”"

# 2. 打印上述的变量值.
print(a)
print(b)

# 3. 细节, Python独有写法, 同时输出多个变量值.
print(a, b, c, d, e)

print(f)    # 发现: 三引号会保留字符串格式.
print(type(20))     # <class 'int'>

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'bool'>
print(type(d))  # <class 'str'>

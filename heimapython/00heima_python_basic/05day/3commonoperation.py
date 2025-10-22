s="abc"
lst=[1,2,3]
tup=(4,5,6)
d={"name":"张三","年龄":"38"}
st={5,6,8}

# 1. + 运算符（合并）：仅支持字符串、列表、元组
print(s + "def")       # 字符串拼接：abcdef
print(lst + [3, 4])    # 列表合并：[1, 2, 3, 4]
print(tup + (5, 6))    # 元组合并：(3, 4, 5, 6)
# print(d + {"age": 20})  # 字典不支持，报错
# print(st + {7})         # 集合不支持，报错
'''
abcdef
[1, 2, 3, 3, 4]
(4, 5, 6, 5, 6)
'''
# 2. * 运算符（复制）：仅支持字符串、列表、元组
print(s * 2)           # 字符串复制：abcabc
print(lst * 2)         # 列表复制：[1, 2, 1, 2]
print(tup * 2)         # 元组复制：(3, 4, 3, 4)
# print(d * 2)            # 字典不支持，报错
# print(st * 2)           # 集合不支持，报错
'''
abcabc
[1, 2, 3, 1, 2, 3]
(4, 5, 6, 4, 5, 6)
'''

# 3. in 运算符（判断存在）：所有容器支持（字典只判断键）
print("a" in s)        # 字符串：True（含字符"a"）
print(1 in lst)        # 列表：True（含元素1）
print(3 in tup)        # 元组：True（含元素3）
print("name" in d)     # 字典：True（含键"name"）
print(5 in st)         # 集合：True（含元素5）
'''
True
True
False
True
True
'''
# 4. not in 运算符（判断不存在）：所有容器支持（字典只判断键）
print("x" not in s)    # 字符串：True（不含"x"）
print(3 not in lst)    # 列表：True（不含3）
print(5 not in tup)    # 元组：True（不含5）
print("age" not in d)  # 字典：True（不含键"age"）
print(7 not in st)     # 集合：True（不含7）
'''
True
False
False
True
True
'''
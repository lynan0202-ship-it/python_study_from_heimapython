basic_list = [i for i in range(1,11)]
print(basic_list)
basic_list = [i for i in range(1,11) if i % 2 == 0]
print(basic_list)
basic_list = [i for i in range(6,58,5)]
print(basic_list)
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2, 4, 6, 8, 10]
[6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56]
'''
convert_list = [n if n > 3 else '小' for n in range(7)]  # 大于3保留数字，否则标'小'
'''
[6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56]
'''
text= "brOken heArt"
lower_chars = [c for c in text if c.islower()]
higher_chars = [c for c in text if c.isupper()]
print(lower_chars)
print(higher_chars)


'''
usage
'''
# 定义包含多种字符的字符串（模拟机器人配置信息片段）
text = "Robo3 关节: 123，角度三 | \t\n"

# 1. 大小写判断类
lower_chars = [c for c in text if c.islower()]  # 小写字母
upper_chars = [c for c in text if c.isupper()]  # 大写字母
title_chars = [c for c in text if c.istitle()]  # 标题格式字符（首字母大写）

# 2. 字符类型判断类
alpha_chars = [c for c in text if c.isalpha()]  # 纯字母
num_digit = [c for c in text if c.isdigit()]    # 数字字符（含部分特殊数字符号）
alnum_chars = [c for c in text if c.isalnum()]  # 字母或数字
space_chars = [c for c in text if c.isspace()]  # 空白字符（空格、制表符等）
printable_chars = [c for c in text if c.isprintable()]  # 可打印字符

# 3. 特殊格式判断类
decimal_chars = [c for c in text if c.isdecimal()]  # 严格十进制数字（0-9）
numeric_chars = [c for c in text if c.isnumeric()]  # 数值字符（含中文数字等）


# 打印结果（简化输出，只展示核心）
print("小写字母：", lower_chars)
print("大写字母：", upper_chars)
print("标题格式字符：", title_chars)
print("纯字母：", alpha_chars)
print("digit数字：", num_digit)
print("字母/数字：", alnum_chars)
print("空白字符：", space_chars)
print("可打印字符：", printable_chars)
print("严格十进制数字：", decimal_chars)
print("数值字符（含中文）：", numeric_chars)
'''
小写字母： ['o', 'b', 'o']
大写字母： ['R']
标题格式字符： ['R']
纯字母： ['R', 'o', 'b', 'o', '关', '节', '角', '度', '三']
digit数字： ['3', '1', '2', '3']
字母/数字： ['R', 'o', 'b', 'o', '3', '关', '节', '1', '2', '3', '角', '度', '三']
空白字符： [' ', ' ', ' ', ' ', '\t', '\n']
可打印字符： ['R', 'o', 'b', 'o', '3', ' ', '关', '节', ':', ' ', '1', '2', '3', '，', '角', '度', '三', ' ', '|', ' ']
严格十进制数字： ['3', '1', '2', '3']
数值字符（含中文）： ['3', '1', '2', '3', '三']
'''
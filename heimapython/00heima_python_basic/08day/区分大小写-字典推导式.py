s=input('请输入字符串')

char_count={char : s.count(char) for char in s}

'''
这行代码使用了 Python 中的字典推导式（Dictionary Comprehension），用于快速创建一个 “字符 - 出现次数” 的映射字典。其功能是统计字符串s中每个字符的出现次数，并将结果以字典形式存储在char_count中。
分解分析
1. 整体结构：字典推导式
字典推导式的基本语法是：{key_expression: value_expression for item in iterable}作用是通过遍历可迭代对象（iterable），为每个元素item生成对应的key和value，最终聚合为一个字典。
2. 各部分解析
for char in s：遍历字符串s中的每个字符，char是当前迭代到的字符（例如s = "abc"时，char依次为'a'、'b'、'c'）。
key_expression: char：字典的 “键” 是当前遍历到的字符char（每个键是字符串中的一个字符）。
value_expression: s.count(char)：字典的 “值” 是该字符char在字符串s中出现的次数。
s.count(char)是字符串的内置方法，用于统计子字符串char在s中出现的总次数（例如s = "aab"，s.count('a')返回 2）。

'''

print(char_count)
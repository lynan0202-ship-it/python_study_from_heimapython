s = input('请输入字符串: ')
char_count = {}  # 空字典存结果

for char in s:
    if char in char_count:
        # 字符已存在，次数+1
        char_count[char] += 1
    else:
        # 字符不存在，新增记录
        char_count[char] = 1
'''
 char_count[char] = char_count[char] + 1 if char in char_count else 1
 char_count = {char: s.count(char) for char in s}
 
'''
print(char_count)  # 输入"aaabbc" → {'a':3, 'b':2, 'c':1}
'''
请输入字符串: agfgsahdja ajgdjsagj jagd  hasjgd
{'a': 7, 'g': 6, 'f': 1, 's': 3, 'h': 2, 'd': 4, 'j': 6, ' ': 4}
'''
s = input('请输入字符串: ')
char_count = {}

for char in s:
    if char.isalnum():  # 只统计字母和数字
        char_count[char] = char_count.get(char, 0) + 1  # get方法：没有键则返回0

print(char_count)  # 输入"Hello! 123" → {'H':1, 'e':1, 'l':2, 'o':1, '1':1, '2':1, '3':1}
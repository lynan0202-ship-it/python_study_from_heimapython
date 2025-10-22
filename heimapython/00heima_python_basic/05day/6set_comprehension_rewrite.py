odd_set = {x for x in range(1, 11) if x % 2 != 0}
print("1-10的奇数集合：", odd_set)  # 输出类似 {1, 3, 5, 7, 9}（集合无序，顺序可能变）

repeat_list = [2, 2, 3, 3, 4]
unique_squares = {num **2 for num in repeat_list}  # 计算平方后去重
print("去重后的平方集合：", unique_squares)  # 输出 {4, 9, 16}（2²=4、3²=9、4²=16，重复的被合并）

triple_dict={n: n*3  for n in range(1,11)}
print(triple_dict)
'''
{1: 3, 2: 6, 3: 9, 4: 12, 5: 15, 6: 18, 7: 21, 8: 24, 9: 27, 10: 30}\
'''

keys1 = ['1','2','3','4']
keys2= ['a','b','c','d']
num_dict= {keys1[i] : keys2[i] for i in range(len(keys1))}
print(num_dict)
'''
{'1': 'a', '2': 'b', '3': 'c', '4': 'd'}
'''
repeat_keys = ['a', 'a', 'b']
overwrite_dict = {k: k*2 for k in repeat_keys}  # 'a'出现两次
print("键重复的字典（覆盖后）：", overwrite_dict)  # 输出 {'a': 'aa', 'b': 'bb'}（后面的'a'覆盖了前面的）
'''
键重复的字典（覆盖后）： {'a': 'aa', 'b': 'bb'}
'''
# 外层i=1,2；内层j=3,4
dict4 = {(i,j): i+j for i in range(1,3) for j in range(3,5)}
print(dict4)  # 输出：{(1,3):4, (1,4):5, (2,3):5, (2,4):6}
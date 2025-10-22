
dict = {'年龄':'18', '性别':'男', '体重':'87kg'}
print(f'dict1: {dict}')
print(type(dict))

"""
演示字典的常用 函数 如下:
    增:  字典名[键名] =  值
    删:  del 字典名   或者 clear()
    改:  字典名[键名] =  值
    查:  get(), keys(), values(), items()

字典使用细节:
    1. 字典存储的是键值对元素, 键具有唯一性, 值可以重复.
    2. 字典属于可变类型, 其元素值可以修改.
"""

#增加

dict['住址'] = '合肥'
print(dict)
dict['年龄'] = '24'
print(dict)
dict.clear()
print(dict)
dict = {'年龄':'18', '性别':'男', '体重':'87kg'}
del dict['年龄']
print(dict)
'''
dict1: {'年龄': '18', '性别': '男', '体重': '87kg'}
<class 'dict'>
{'年龄': '18', '性别': '男', '体重': '87kg', '住址': '合肥'}
{'年龄': '24', '性别': '男', '体重': '87kg', '住址': '合肥'}
{}
{'性别': '男', '体重': '87kg'}

'''
print(dict.get('性别'))
print(dict.get('岁数','无此内容'))
'''
男
无此内容
'''
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())
'''
{'性别': '男', '体重': '87kg'}
dict_keys(['性别', '体重'])
dict_values(['男', '87kg'])
dict_items([('性别', '男'), ('体重', '87kg')])
'''
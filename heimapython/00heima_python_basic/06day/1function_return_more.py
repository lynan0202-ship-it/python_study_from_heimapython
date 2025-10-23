def calculate (a,b):
    '''
    :param a:
    :param b:
    :return:
    '''
    sum = a + b
    sub = a - b
    mul = a*b
    div = a/b
    return sum, sub, mul, div
return1=calculate(1,2)
print(return1)
'''
(3, -1, 2, 0.5)
'''
print(type(return1))  # <class 'tuple'>

'''
如何把元素类型进行转换
'''
lister = list(return1)
print(lister)
print(type(lister))
'''
[3, -1, 2, 0.5]
<class 'list'>
'''

'''
若返回值数量与接收变量数量不匹配，会报错（ValueError）。例如：a, b = calculate(10, 3) 会报错（需要4个变量接收）。
可通过 *变量名 接收多余的返回值（拆包技巧），例如：a, b, *rest = calculate(10, 3)，其中 rest 会接收剩余的两个值（[30, 3]）。
'''


a, b,c,d = calculate(10,3)
print(a,b,c,d)
'''
13 7 30 3.3333333333333335
'''

a, b,*rest = calculate(10,3)
print(a,b)
print(*rest)
'''
13 7
30 3.3333333333333335

'''
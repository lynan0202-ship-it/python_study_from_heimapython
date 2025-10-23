"""
代码名称：匿名函数简明教程
知识要点总结：
1. 匿名函数：没有函数名的简单函数，使用lambda关键字定义
2. 语法：lambda 参数: 表达式（自动返回表达式结果）
3. 适用场景：简单操作、一次性使用、作为函数参数传递

代码总体逻辑说明：
通过对比普通函数和匿名函数的实现方式，展示匿名函数的简洁性和应用场景
"""


# 示例1：基本匿名函数 - 计算两数之和

# 普通函数实现
def add_numbers(a, b):
    return a + b


# 匿名函数实现
add_lambda = lambda a, b: a + b

# 测试两种实现
print("普通函数:", add_numbers(10, 20))
print("匿名函数:", add_lambda(10, 20))
print("匿名函数:", add_lambda(34, 20))
print("-" * 30)

'''
普通函数: 30
匿名函数: 30
匿名函数: 54
------------------------------
'''
# 示例2：匿名函数作为参数传递 - 灵活的计算器

def calculator(a, b, operation):
    """
    通用计算函数

    参数:
        a, b: 要计算的数字
        operation: 计算规则的函数（可以是匿名函数）
    """
    return operation(a, b)


# 使用匿名函数实现不同的计算规则
print("加法:", calculator(10, 3, lambda x, y: x + y))
print("减法:", calculator(10, 3, lambda x, y: x - y))
print("乘法:", calculator(10, 3, lambda x, y: x * y))
print("除法:", calculator(10, 3, lambda x, y: x // y))
print("最大值:", calculator(10, 3, lambda x, y: x if x > y else y))
print("平均值:", calculator(10, 3, lambda x, y: (x + y) / 2))
'''
加法: 13
减法: 7
乘法: 30
除法: 3
最大值: 10
平均值: 6.5
'''
"""
代码测试及验证建议方案：
1. 测试基本匿名函数：验证与普通函数结果一致
2. 测试不同运算规则：通过传递不同lambda表达式验证灵活性
3. 测试边界情况：如除零、负数等特殊情况

易错点提醒：
1. 匿名函数只能包含单个表达式，不能写复杂逻辑
2. 表达式结果会自动返回，不需要写return
3. 匿名函数适合简单操作，复杂逻辑建议使用普通函数
4. 匿名函数可以作为变量赋值，但通常直接作为参数传递
"""
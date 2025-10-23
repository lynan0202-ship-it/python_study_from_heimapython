# 组包示例
# 多个值赋值给一个变量，自动封装为元组
data = 10, 20, 30, "hello"
print(data)  # 输出：(10, 20, 30, 'hello')
print(type(data))  # 输出：<class 'tuple'>

# 列表拆包
list1 = [100, 200, 300]
a, b, c = list1
print(a, b, c)  # 输出：100 200 300

# 元组拆包
tuple1 = ("张三", 23, "北京")
name, age, address = tuple1
print(name, age, address)  # 输出：张三 23 北京

# 字典拆包（默认获取键，通过.values()获取值，.items()获取键值对）
dict1 = {"name": "李四", "age": 25}
k1, k2 = dict1  # 获取键
print(k1, k2)  # 输出：name age
#  拆包值（通过 .values()）
v1, v2 = dict1.values()
print(v1, v2)  # 输出：李四 25


v1, v2 = dict1.values()  # 获取值
print(v1, v2)  # 输出：李四 25

item1, item2 = dict1.items()  # 获取键值对（元组形式）
print(item1, item2)  # 输出：('name', '李四') ('age', 25)
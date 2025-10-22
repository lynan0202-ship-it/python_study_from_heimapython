# 定义5种容器类型的示例数据，涵盖字符串、列表、元组、字典、集合
s = "hello"  # 字符串（不可变，元素是字符）
lst = [3, 1, 4, 2]  # 列表（可变，元素是数字）
tup = (5, 8, 6, 7)  # 元组（不可变，元素是数字）
d = {"name": "Python", "version": 3.11, "usage": "coding"}  # 字典（可变，元素是键值对）
st = {10, 20, 5, 15}  # 集合（可变，元素是数字，无重复）


# 1. len()：获取容器的元素数量（所有容器都支持）
print("===== len() 示例 =====")
print(f"字符串长度（字符数）：len(s) = {len(s)}")  # 输出5（"hello"有5个字符）
print(f"列表长度（元素数）：len(lst) = {len(lst)}")  # 输出4（列表有4个元素）
print(f"元组长度（元素数）：len(tup) = {len(tup)}")  # 输出4（元组有4个元素）
print(f"字典长度（键值对数量）：len(d) = {len(d)}")  # 输出3（字典有3个键）
print(f"集合长度（元素数）：len(st) = {len(st)}")  # 输出4（集合有4个元素）


# 2. del：删除容器中的元素（仅支持可变容器：列表、字典、集合；字符串和元组不可变，不能删元素）
print("\n===== del 示例 =====")
# 列表：删除索引为1的元素（值为1）
del lst[1]
print(f"删除列表索引1后：lst = {lst}")  # 输出[3, 4, 2]

# 字典：删除键为"usage"的键值对
del d["usage"]
print(f"删除字典键'usage'后：d = {d}")  # 输出{'name': 'Python', 'version': 3.11}

# 集合：删除元素15（集合无索引，直接删值）
del st  # 集合不能通过索引删单个元素，这里演示删除整个集合（后续不能再用st）
# 注意：集合删单个元素用st.remove(15)，但此处为了统一用del演示删除容器/元素

# 字符串和元组不可变，以下代码会报错（注释掉避免运行错误）
# del s[0]  # 报错：字符串不可变，不能删元素
# del tup[0]  # 报错：元组不可变，不能删元素


# 3. max()：获取容器中的最大值（元素需可比较，字典默认比较键）
print("\n===== max() 示例 =====")
print(f"字符串最大字符（按ASCII值）：max(s) = {max(s)}")  # 输出'o'（'h','e','l','l','o'中'o'最大）
print(f"列表最大值：max(lst) = {max(lst)}")  # 输出4（当前列表[3,4,2]中最大）
print(f"元组最大值：max(tup) = {max(tup)}")  # 输出8（元组(5,8,6,7)中最大）
print(f"字典最大键（按键比较）：max(d) = {max(d)}")  # 输出'version'（键'name'和'version'中，'version'更大）
# 上面删除了整个集合st，重新定义一个集合演示
st_new = {10, 20, 5, 15}
print(f"集合最大值：max(st_new) = {max(st_new)}")  # 输出20


# 4. min()：获取容器中的最小值（规则同max()）
print("\n===== min() 示例 =====")
print(f"字符串最小字符：min(s) = {min(s)}")  # 输出'e'（'h','e','l','l','o'中'e'最小）
print(f"列表最小值：min(lst) = {min(lst)}")  # 输出2（当前列表[3,4,2]中最小）
print(f"元组最小值：min(tup) = {min(tup)}")  # 输出5（元组(5,8,6,7)中最小）
print(f"字典最小键：min(d) = {min(d)}")  # 输出'name'（键'name'比'version'小）
print(f"集合最小值：min(st_new) = {min(st_new)}")  # 输出5


# 5. range()：生成数字序列（不直接作用于容器，但常用于遍历容器）
print("\n===== range() 示例 =====")
# 生成1-9的奇数（start=1，end=10，步长2）
print(f"range(1,10,2)生成的序列：{list(range(1,10,2))}")  # 输出[1,3,5,7,9]
# 生成0-4的数字（默认start=0，步长=1）
print(f"range(5)生成的序列：{list(range(5))}")  # 输出[0,1,2,3,4]


# 6. enumerate()：给元素加下标（支持字符串、列表、元组、字典等可迭代对象）
print("\n===== enumerate() 示例 =====")
# 字符串：给每个字符加下标（默认从0开始）
print("字符串的下标+元素：")
for idx, char in enumerate(s):
    print(f"下标{idx}：{char}")  # 输出(0:'h')、(1:'e')、(2:'l')、(3:'l')、(4:'o')

# 列表：指定下标从10开始
print("\n列表的下标+元素（从10开始）：")
for idx, num in enumerate(lst, start=10):
    print(f"下标{idx}：{num}")  # 输出(10:3)、(11:4)、(12:2)

# 字典：默认遍历键，给键加下标
print("\n字典的下标+键：")
for idx, key in enumerate(d):
    print(f"下标{idx}：键{key}（值：{d[key]}）")  # 输出(0:'name')、(1:'version')
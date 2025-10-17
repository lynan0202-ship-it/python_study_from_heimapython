# Python容器类型详解：列表、元组、字典

## 🎯 列表(List)详解

### 1. 列表基础入门

#### 基础结构
```python
# 定义列表的三种方式
list1 = [10, 20.3, True, 'abc']  # 直接定义
list2 = list()                    # 使用list()函数
list3 = []                        # 空列表语法糖

print(f'列表内容: {list1}')        # [10, 20.3, True, 'abc']
print(f'数据类型: {type(list1)}')   # <class 'list'>
```

#### 索引和切片
```python
# 列表索引（从0开始）
fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits[1])      # 'banana' - 正向索引
print(fruits[-2])     # 'cherry' - 逆向索引

# 列表切片
print(fruits[1:3])    # ['banana', 'cherry'] - 包左不包右
print(fruits[:2])     # ['apple', 'banana']  - 从头开始
print(fruits[2:])     # ['cherry', 'date']   - 到末尾结束
```

**💡 核心要点：**
- 列表是**可变类型**，可以存储不同类型数据
- 索引从0开始，支持正向和逆向索引
- 切片格式：`列表[起始:结束:步长]`

---

### 2. 列表遍历的两种思路

#### 方法1：直接获取元素
```python
numbers = [11, 22, 33, 44, 55]

# 直接遍历元素
for num in numbers:
    print(f'当前数字: {num}')
```

#### 方法2：通过索引遍历
```python
# while循环 + 索引
i = 0
while i < len(numbers):
    print(f'索引{i}的值: {numbers[i]}')
    i += 1

# for循环 + 索引
for i in range(len(numbers)):
    print(f'索引{i}的值: {numbers[i]}')
```

**🚀 应用场景：**
- 方法1：只需读取元素值时使用
- 方法2：需要同时知道索引和元素值时使用

---

### 3. 列表的增删改查操作

#### 📈 增加元素
```python
my_list = [10, 20, 30]

# 三种添加方式
my_list.append(40)           # 末尾添加单个元素: [10, 20, 30, 40]
my_list.extend([50, 60])     # 末尾添加多个元素: [10, 20, 30, 40, 50, 60]
my_list.insert(1, 15)        # 指定位置插入: [10, 15, 20, 30, 40, 50, 60]

print(f'添加后: {my_list}')
```

#### 🔍 查询元素
```python
colors = ['red', 'blue', 'green', 'red', 'yellow']

# 查询方法
print(colors.index('blue'))          # 1 - 查找元素位置
print(colors.count('red'))           # 2 - 统计出现次数
print('green' in colors)             # True - 判断是否存在
print('purple' not in colors)        # True - 判断是否不存在
```

#### 🗑️ 删除元素
```python
nums = [10, 20, 30, 40, 50, 30]

# 五种删除方式
del nums[1]                 # 根据索引删除: [10, 30, 40, 50, 30]
nums.remove(30)             # 根据值删除(只删第一个): [10, 40, 50, 30]
popped = nums.pop(2)        # 根据索引删除并返回: 50, nums变为[10, 40, 30]
nums.clear()                # 清空所有元素: []
```

#### ✏️ 修改元素
```python
numbers = [5, 2, 8, 1, 9]

# 修改方式
numbers[2] = 88            # 直接赋值: [5, 2, 88, 1, 9]
numbers.reverse()          # 反转列表: [9, 1, 88, 2, 5]
numbers.sort()             # 升序排序: [1, 2, 5, 9, 88]
numbers.sort(reverse=True) # 降序排序: [88, 9, 5, 2, 1]
```

**🎯 实战技巧：**
- `append()` vs `extend()`：单个元素用append，多个元素用extend
- `remove()` 只删除第一个匹配项
- `pop()` 会返回被删除的元素

---

### 4. 列表嵌套与高级应用

#### 列表嵌套结构
```python
# 二维列表（列表嵌套）
classrooms = [
    ['张三', '李四', '王五'],      # 教室1
    ['赵六', '钱七'],             # 教室2  
    ['孙八', '周九', '吴十']       # 教室3
]

# 访问嵌套元素
print(classrooms[0])           # ['张三', '李四', '王五']
print(classrooms[1][0])        # '赵六'
```

#### 嵌套列表遍历
```python
# 方法1：索引遍历
for i in range(len(classrooms)):
    print(f'教室{i+1}:')
    for j in range(len(classrooms[i])):
        print(f'  - {classrooms[i][j]}')

# 方法2：直接遍历（推荐）
for classroom in classrooms:
    print(f'教室:')
    for student in classroom:
        print(f'  - {student}')
```

---

### 5. 实战案例：随机分配办公室

```python
import random

# 初始化数据
classrooms = [[], [], []]  # 三个空教室
teachers = ['张老师', '李老师', '王老师', '赵老师', '刘老师', '陈老师', '杨老师', '黄老师']

# 随机分配
for teacher in teachers:
    class_id = random.randint(0, 2)  # 随机选择教室(0,1,2)
    classrooms[class_id].append(teacher)

# 显示结果
for i, classroom in enumerate(classrooms):
    print(f'教室{i+1}: {classroom}')
```

**📊 输出示例：**
```
教室1: ['张老师', '王老师', '刘老师', '黄老师']
教室2: ['李老师', '杨老师']  
教室3: ['赵老师', '陈老师']
```

---

## 🔒 元组(Tuple)详解

### 1. 元组基础概念

#### 定义方式
```python
# 三种定义方式
t1 = (10, 20.3, True, 'abc')  # 标准定义
t2 = tuple()                   # 空元组
t3 = (50,)                     # 单元素元组（必须有逗号）
t4 = (50)                      # ❌ 这只是整数，不是元组！

print(type(t3))  # <class 'tuple'>
print(type(t4))  # <class 'int'>
```

#### 元组特性
```python
colors = ('red', 'blue', 'green', 'blue')

# 基本操作
print(colors[1])              # 'blue' - 索引访问
print(colors.index('green'))   # 2 - 查找索引
print(colors.count('blue'))    # 2 - 统计次数
print('red' in colors)         # True - 成员判断

# ❌ 不可修改（会报错）
# colors[1] = 'yellow'  
```

**🎯 核心要点：**
- 元组是**不可变类型**，创建后不能修改
- 单元素元组必须在元素后加逗号
- 支持索引、切片等操作，但不能增删改

---

### 2. 元组 vs 列表对比

| 特性 | 列表(List) | 元组(Tuple) |
|------|------------|-------------|
| 可变性 | ✅ 可变 | ❌ 不可变 |
| 语法 | `[1, 2, 3]` | `(1, 2, 3)` |
| 性能 | 稍慢 | 更快 |
| 使用场景 | 需要修改的数据 | 固定数据、字典键 |

---

## 📚 字典(Dictionary)详解

### 1. 字典基础入门

#### 定义方式
```python
# 三种定义方式
dict1 = {'name': '张三', 'age': 25, 'city': '北京'}  # 标准定义
dict2 = {}                                          # 空字典
dict3 = dict()                                      # 使用dict()函数

print(dict1)  # {'name': '张三', 'age': 25, 'city': '北京'}
```

#### 字典特性
```python
student = {'name': '李四', 'age': 20, 'major': '计算机'}

# 键的唯一性
student['age'] = 21           # 修改已存在键的值
student['grade'] = '大一'      # 添加新键值对

print(student)  # {'name': '李四', 'age': 21, 'major': '计算机', 'grade': '大一'}
```

**💡 核心要点：**
- 字典存储**键值对**数据
- **键必须唯一**，值可以重复
- 字典是**可变类型**

---

### 2. 字典的CRUD操作

#### 增删改查
```python
person = {'name': '王五', 'age': 30}

# 增加
person['city'] = '上海'

# 修改  
person['age'] = 31

# 查询
print(person['name'])          # 王五
print(person.get('email', '暂无'))  # 暂无（键不存在返回默认值）

# 删除
del person['city']             # 删除指定键值对
# person.clear()               # 清空字典
```

#### 常用方法
```python
info = {'name': '赵六', 'age': 28, 'city': '广州'}

print(info.keys())    # dict_keys(['name', 'age', 'city']) - 所有键
print(info.values())  # dict_values(['赵六', 28, '广州'])  - 所有值
print(info.items())   # dict_items([('name', '赵六'), ...]) - 所有键值对
```

---

### 3. 字典遍历技巧

#### 方法1：通过键遍历值
```python
scores = {'数学': 90, '语文': 85, '英语': 92}

for subject in scores.keys():
    score = scores[subject]
    print(f'{subject}: {score}分')
```

#### 方法2：直接遍历键值对（推荐）
```python
# 标准写法
for item in scores.items():
    subject, score = item[0], item[1]
    print(f'{subject}: {score}分')

# 简化写法（拆包）
for subject, score in scores.items():
    print(f'{subject}: {score}分')
```

**🚀 性能建议：**
- 需要同时使用键和值时，用`items()`方法
- 只需要键时，用`keys()`方法  
- 只需要值时，用`values()`方法

---

## 🎯 综合实战案例

### 案例1：幸运数字筛选
```python
# 生成1-n的数字，筛选能被6整除的幸运数字
n = int(input('请输入数字n: '))

# 传统方法
all_nums = []
lucky_nums = []

for i in range(1, n+1):
    all_nums.append(i)
    if i % 6 == 0:
        lucky_nums.append(i)

print(f'所有数字: {all_nums}')
print(f'幸运数字: {lucky_nums}')

# 列表推导式（高级写法）
all_nums = [i for i in range(1, n+1)]
lucky_nums = [i for i in all_nums if i % 6 == 0]
```

### 案例2：学生成绩管理系统
```python
# 使用字典管理学生信息
students = {
    '001': {'name': '张三', 'scores': {'数学': 90, '语文': 85}},
    '002': {'name': '李四', 'scores': {'数学': 78, '语文': 92}}
}

# 添加学生
students['003'] = {'name': '王五', 'scores': {'数学': 88, '语文': 79}}

# 查询成绩
student_id = '001'
print(f"{students[student_id]['name']}的数学成绩: {students[student_id]['scores']['数学']}")

# 遍历所有学生
for sid, info in students.items():
    print(f"学号: {sid}, 姓名: {info['name']}")
    for subject, score in info['scores'].items():
        print(f"  {subject}: {score}")
```

---

## 🔍 拓展问题与思考

### 问题1：如何删除列表中的重复元素？
```python
# 方法1：转集合再转回列表（不保序）
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(numbers))

# 方法2：遍历判断（保序）
unique_nums = []
for num in numbers:
    if num not in unique_nums:
        unique_nums.append(num)
```

### 问题2：字典键的类型限制？
```python
# 字典键必须是不可变类型
valid_dict = {
    'string': '值1',      # ✅ 字符串
    123: '值2',           # ✅ 数字  
    (1, 2): '值3'         # ✅ 元组
}

# invalid_dict = {
#     [1, 2]: '值4'       # ❌ 列表不能作为键
# }
```

### 问题3：多层嵌套数据结构
```python
# 学校 -> 班级 -> 学生 三级结构
school = {
    '高一': {
        '1班': ['张三', '李四', '王五'],
        '2班': ['赵六', '钱七']
    },
    '高二': {
        '1班': ['孙八', '周九'],
        '2班': ['吴十', '郑十一']
    }
}

# 访问嵌套数据
print(school['高一']['1班'][0])  # 张三
```

---

## 💡 学习建议

1. **理解可变性**：列表字典可变，元组不可变
2. **掌握遍历**：熟练各种遍历方式，根据场景选择
3. **善用方法**：记住常用方法如`append()`, `get()`, `items()`等  
4. **实践练习**：多写小项目巩固理解

**记住：编程就像学语言，多练习才能流利！** 🚀
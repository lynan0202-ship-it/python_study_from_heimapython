# Python容器类型与函数详解

## 1. sort函数的key参数详解

### 基础结构
```python
list.sort(key=函数名, reverse=布尔值)
```

### 核心理解
- **key参数**：让sort()知道按什么规则排序
- **工作原理**：sort()会先对每个元素应用key函数，然后用返回值排序

### 经典用法
```python
# 按字符串长度排序
words = ['apple', 'hi', 'banana', 'a']
words.sort(key=len)
print(words)  # ['a', 'hi', 'apple', 'banana']

# 按元组的第二个元素排序
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
students.sort(key=lambda x: x[1])  # 按成绩排序
print(students)  # [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# 按自定义规则排序（按姓名字母逆序）
students.sort(key=lambda x: x[0], reverse=True)
print(students)  # [('Charlie', 78), ('Bob', 92), ('Alice', 85)]
```

### 拓展应用
```python
# 复杂数据结构排序
data = [
    {'name': '张三', 'age': 25, 'score': 88},
    {'name': '李四', 'age': 22, 'score': 95},
    {'name': '王五', 'age': 28, 'score': 76}
]

# 按年龄排序
data.sort(key=lambda x: x['age'])
print(data)

# 按分数降序排序
data.sort(key=lambda x: x['score'], reverse=True)
print(data)
```

---

## 2. set集合完全掌握

### 基础结构
```python
# 创建集合
set1 = {1, 2, 3, 2, 1}        # 自动去重：{1, 2, 3}
set2 = set([1, 2, 3, 2, 1])   # 从列表转换：{1, 2, 3}
set3 = set()                  # 空集合
empty_dict = {}               # 这是空字典，不是集合！
```

### 核心特性
- **无序性**：元素存储顺序≠读取顺序
- **唯一性**：自动去除重复元素
- **可变性**：可以增删元素

### 经典用法
```python
# 去重应用（最常用）
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = list(set(numbers))
print(unique_numbers)  # [1, 2, 3, 4]

# 集合运算
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # 并集：{1, 2, 3, 4, 5, 6}
print(A & B)  # 交集：{3, 4}
print(A - B)  # 差集：{1, 2}
print(A ^ B)  # 对称差集：{1, 2, 5, 6}
```

### 拓展应用
```python
# 网站用户标签去重
user_tags = ['python', '编程', '学习', 'python', '代码', '学习']
unique_tags = set(user_tags)
print(f"用户唯一标签: {unique_tags}")

# 快速查找共同兴趣
alice_interests = {'读书', '音乐', '旅游', '编程'}
bob_interests = {'游戏', '编程', '音乐', '运动'}
common_interests = alice_interests & bob_interests
print(f"共同兴趣: {common_interests}")
```

---

## 3. 容器类型公共运算符

### 运算符汇总表
| 运算符 | 描述 | 支持的数据类型 |
|--------|------|----------------|
| `+` | 合并 | str, list, tuple |
| `*` | 复制 | str, list, tuple |
| `in` | 成员检查 | 所有容器类型 |
| `not in` | 非成员检查 | 所有容器类型 |

### 详细示例
```python
# + 合并操作
str1 = "Hello" + " " + "World"      # "Hello World"
list1 = [1, 2] + [3, 4]            # [1, 2, 3, 4]
tuple1 = (1, 2) + (3, 4)           # (1, 2, 3, 4)

# * 复制操作
str2 = "Hi" * 3                     # "HiHiHi"
list2 = [0] * 5                     # [0, 0, 0, 0, 0]
tuple2 = (1, 2) * 2                 # (1, 2, 1, 2)

# in 成员检查
print('a' in 'apple')               # True
print(3 in [1, 2, 3])               # True
print('name' in {'name': 'Tom'})    # True (检查键)
print(3 in {1, 2, 3})               # True

# not in 非成员检查
print('x' not in 'apple')           # True
print(5 not in [1, 2, 3])           # True
```

### 记忆技巧
> **口诀**：字符串、列表、元组是"好兄弟"，支持`+`和`*`操作；所有容器都支持`in`检查！

---

## 4. 容器类型公共函数

### 函数大全
```python
# len() - 获取长度
print(len("hello"))     # 5
print(len([1, 2, 3]))   # 3
print(len({'a': 1}))    # 1

# del - 删除元素
my_list = [1, 2, 3, 4]
del my_list[1]          # 删除索引1的元素 → [1, 3, 4]
del my_list[0:2]        # 删除切片 → [4]

# max() / min() - 最值
numbers = [5, 2, 8, 1]
print(max(numbers))     # 8
print(min(numbers))     # 1

# range() - 生成序列
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(1, 6)))        # [1, 2, 3, 4, 5]
print(list(range(1, 10, 2)))    # [1, 3, 5, 7, 9]

# enumerate() - 枚举遍历
fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits):
    print(f"索引{index}: {fruit}")
# 输出：
# 索引0: apple
# 索引1: banana  
# 索引2: orange

# 自定义起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"第{index}个水果: {fruit}")
```

### 实战应用
```python
# 学生成绩处理
scores = [85, 92, 78, 96, 88]

print(f"学生人数: {len(scores)}")
print(f"最高分: {max(scores)}")
print(f"最低分: {min(scores)}")

# 带序号输出成绩
for i, score in enumerate(scores, 1):
    print(f"第{i}名学生成绩: {score}")
```

---

## 5. 推导式（重点掌握）

### 列表推导式

#### 基础格式
```python
[表达式 for 变量 in 可迭代对象 if 条件]
```

#### 渐进学习
```python
# Level 1: 基础推导式
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Level 2: 带条件的推导式
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Level 3: 多循环推导式
pairs = [(x, y) for x in range(2) for y in range(3)]
print(pairs)  # [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)]
```

#### 实际应用场景
```python
# 数据处理：提取数字
data = ['a1', 'b2', 3, 'c4', 5]
numbers = [x for x in data if isinstance(x, int)]
print(numbers)  # [3, 5]

# 文本处理：单词长度统计
sentence = "Python is an amazing programming language"
word_lengths = [len(word) for word in sentence.split()]
print(word_lengths)  # [6, 2, 2, 7, 11, 8]

# 数据转换：温度转换
celsius = [0, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)  # [32.0, 68.0, 86.0, 104.0]
```

### 集合推导式

#### 格式对比
```python
# 列表推导式：[]
list_comp = [x for x in range(5)]      # [0, 1, 2, 3, 4]

# 集合推导式：{}
set_comp = {x for x in range(5)}       # {0, 1, 2, 3, 4}
```

#### 去重特性
```python
# 自动去重是最大特点
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x**2 for x in numbers}
print(unique_squares)  # {16, 1, 9, 4} 自动去重且无序
```

### 字典推导式

#### 基础格式
```python
{键:值 for 变量 in 可迭代对象 if 条件}
```

#### 经典示例
```python
# 创建数字平方字典
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 键值互换
original = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in original.items()}
print(reversed_dict)  # {1: 'a', 2: 'b', 3: 'c'}

# 列表合并为字典
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Beijing']
person = {keys[i]: values[i] for i in range(len(keys))}
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
```

#### 实用技巧
```python
# 数据筛选：只保留值大于2的项
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {k: v for k, v in data.items() if v > 2}
print(filtered)  # {'c': 3, 'd': 4}

# 文本处理：单词频率统计（简化版）
text = "apple banana apple orange banana apple"
words = text.split()
word_count = {word: words.count(word) for word in set(words)}
print(word_count)  # {'orange': 1, 'banana': 2, 'apple': 3}
```

---

## 6. 函数详解

### 函数定义结构
```python
def 函数名(参数1, 参数2, ...):
    """文档字符串（可选）"""
    函数体
    return 返回值
```

### 四种函数类型详解

#### ① 无参无返回值
```python
def say_hello():
    """简单的问候函数"""
    print("Hello, World!")
    print("欢迎学习Python！")

# 调用
say_hello()
```

#### ② 有参无返回值
```python
def greet(name, time="早上"):
    """带参数的问候函数"""
    print(f"{time}好，{name}！")

# 调用
greet("小明")              # 早上好，小明！
greet("小红", "下午")      # 下午好，小红！
```

#### ③ 无参有返回值
```python
def get_current_time():
    """获取当前时间信息"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 调用
current_time = get_current_time()
print(f"当前时间: {current_time}")
```

#### ④ 有参有返回值
```python
def calculate_bmi(weight, height):
    """计算BMI指数"""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# 调用
bmi_result = calculate_bmi(70, 1.75)
print(f"您的BMI指数是: {bmi_result}")
```

### 函数调用图解理解

```
调用过程：
1. 主程序执行到函数调用 → 暂停主程序
2. 跳转到函数定义处执行
3. 函数执行完毕 → 返回主程序继续执行
4. 如果有返回值 → 用返回值替换函数调用

示例：
def add(a, b):
    result = a + b
    return result

x = add(3, 5)  # 调用过程：3和5传给a,b → 执行add函数 → 返回8 → x=8
```

### 综合实战案例
```python
def student_management():
    """学生成绩管理系统（综合示例）"""
    
    # 嵌套函数：计算平均分
    def calculate_average(scores):
        return sum(scores) / len(scores)
    
    # 嵌套函数：判断等级
    def get_grade(score):
        if score >= 90: return "优秀"
        elif score >= 80: return "良好"
        elif score >= 70: return "中等"
        elif score >= 60: return "及格"
        else: return "不及格"
    
    # 主逻辑
    students = [
        {'name': '张三', 'scores': [85, 92, 78]},
        {'name': '李四', 'scores': [76, 88, 95]},
        {'name': '王五', 'scores': [92, 96, 88]}
    ]
    
    for student in students:
        avg_score = calculate_average(student['scores'])
        grade = get_grade(avg_score)
        print(f"{student['name']}的平均分: {avg_score:.1f}, 等级: {grade}")

# 调用综合函数
student_management()
```

---

## 7. 匿名函数

### 基础语法
```python
lambda 参数1, 参数2, ...: 表达式
```

### 与普通函数对比
```python
# 普通函数
def add(x, y):
    return x + y

# 匿名函数
add_lambda = lambda x, y: x + y

print(add(3, 5))        # 8
print(add_lambda(3, 5)) # 8
```

### 实际应用场景
```python
# 场景1：作为sort的key参数
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
students.sort(key=lambda x: x[1])  # 按成绩排序
print(students)

# 场景2：在map函数中使用
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# 场景3：在filter函数中使用
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8]

# 场景4：简单的条件判断
grade_check = lambda score: "及格" if score >= 60 else "不及格"
print(grade_check(85))  # 及格
print(grade_check(45))  # 不及格
```

### 使用建议
> **何时使用匿名函数**：
> - 函数逻辑简单（一行表达式）
> - 只在当前位置使用一次
> - 作为其他函数的参数
> 
> **何时使用普通函数**：
> - 函数逻辑复杂
> - 需要重复使用
> - 需要文档说明

---

## 🎯 学习总结

### 核心要点回顾
1. **sort的key参数**：让排序更灵活
2. **set集合**：去重利器，运算方便  
3. **公共运算符**：`+ * in`的适用场景
4. **公共函数**：`len, max, min, enumerate`要熟练
5. **推导式**：Pythonic编程的精华
6. **函数设计**：四种类型灵活运用
7. **匿名函数**：简洁的临时函数

### 下一步学习建议
- 多练习推导式，写出更Pythonic的代码
- 尝试设计复杂的函数，理解参数传递
- 在实际项目中应用这些知识点
- 学习函数的高级特性（装饰器、生成器等）

**记住**：编程就像学游泳，光看不行，要多写代码！每个知识点都要亲手敲一遍，遇到问题就多调试，你会进步很快的！💪
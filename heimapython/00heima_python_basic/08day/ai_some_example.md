# 🐍 Python趣味案例合集：从游戏到实用工具


## 一、约瑟夫环：古代“幸运数字”游戏

### 🌟 先懂规则：什么是约瑟夫环？
想象你穿越到古代，和一群人围成圈“数3淘汰”——从1开始数，数到3或3的倍数的人被淘汰，直到只剩1人，他的位置就是“幸运数字”。  
比如10个人玩，最后剩下的是第4位，那4就是幸运数字～


### 🎯 需求
键盘输入总人数，打印出最后的“幸运数字”。


### 🚩 核心原理：用列表模拟“圆圈”
我们用**列表**存储每个人的编号（比如[1,2,3,4,5]代表5个人），用**索引**模拟“转圈数人”，关键细节有3个：
1. 数到圈尾时，索引要重置为0（比如数完最后一个人，下一个从第一个开始）；
2. 淘汰人后，列表长度变短，索引要减1（否则会跳过下一个人）；
3. 用`num`变量记录当前数到的数字，判断是否该淘汰。


### 💻 代码实战（逐行解析）
```python
# 1. 输入总人数（比如输入10）
n = int(input('请录入参与游戏的总人数: '))  

# 2. 生成编号列表（比如n=5时，列表是[1,2,3,4,5]）
num_list = [i for i in range(1, n + 1)]

# 3. 初始化：num=当前数的数字，i=当前人的索引（从第0个开始）
num, i = 0, 0

# 4. 循环淘汰，直到只剩1人
while len(num_list) != 1:
    num += 1  # 每轮数1个数字（1→2→3→1...）
    
    # 细节1：数到圈尾，索引重置为0（转圈）
    if i == len(num_list):
        i = 0
    
    # 细节2：数到3或3的倍数，淘汰当前人
    if num % 3 == 0:
        num_list.pop(i)  # 从列表中删除当前人
        i -= 1  # 删除后列表变短，索引回退1，避免跳过下一个人
    
    i += 1  # 下一个人准备数数

# 5. 打印幸运数字（列表最后剩下的元素）
print(f'参与游戏总人数为: {n}, 幸运数字为: {num_list[0]}')
```


### 📚 拓展技巧：让游戏更灵活
#### 1. 自定义淘汰数字（不只是3）
把固定的“3”改成变量`k`，让用户自己决定数到几淘汰：
```python
n = int(input('总人数: '))
k = int(input('数到几淘汰: '))  # 比如输入4，就是数到4淘汰
num_list = list(range(1, n+1))
num, i = 0, 0

while len(num_list) > 1:
    num += 1
    if i >= len(num_list):
        i = 0
    if num % k == 0:  # 用k代替3
        num_list.pop(i)
        i -= 1
    i += 1

print(f'幸运数字: {num_list[0]}')
```

#### 2. 用“队列”实现（更贴合“转圈”逻辑）
队列是“先进先出”的结构，把没被淘汰的人放到队尾，模拟转圈：
```python
from collections import deque  # 导入队列模块

n = int(input('总人数: '))
q = deque(range(1, n+1))  # 把编号放进队列
count = 0  # 计数用

while len(q) > 1:
    count += 1
    person = q.popleft()  # 取出队首的人
    if count % 3 != 0:    # 不是3的倍数，放回队尾
        q.append(person)
    # 是3的倍数，直接淘汰（不放回）

print(f'幸运数字: {q[0]}')
```


## 二、排列组合：1-4数字的“拼图游戏”

### 🌟 需求回顾
用1、2、3、4四个数字组成**不重复的四位数**，满足：
1. 数字不能重复（比如1122不行）；
2. 1和3不能挨着（比如1324、3142不行）；
3. 4不能开头（比如4123不行）；
4. 每3个结果打印一行。


### 🚩 核心原理：“范围筛选法”
四位数的范围是1234（最小）到4321（最大），我们循环这个范围，对每个数做“三层检查”：
1. 转成字符串，看是否包含1、2、3、4所有数字（确保不重复）；
2. 检查字符串里没有“13”或“31”（确保1和3不挨着）；
3. 检查第一个字符不是“4”（确保4不开头）。


### 💻 代码实战（逐行解析）
```python
count = 0  # 计数器，控制每3个换行
# 循环所有可能的四位数（1234到4321）
for i in range(1234, 4322):
    s = str(i)  # 把数字转成字符串，方便检查
    # 三层检查：1.含所有数字 2.1和3不挨着 3.4不开头
    if ('1' in s and '2' in s and '3' in s and '4' in s 
        and '13' not in s and '31' not in s 
        and s[0] != '4'):
        count += 1  # 符合条件，计数+1
        # 打印：count是3的倍数就换行，否则用制表符分隔
        print(i, end='\n' if count % 3 == 0 else '\t')
```

**运行结果**（符合条件的数）：
```
1234    1243    1423
2143    2314    2341
2413    3214    3241
3421    4213    4231
```


### 📚 拓展技巧：更高效的“排列生成法”
上面的“范围筛选法”会循环很多无效数字（比如1111、1223），用`itertools.permutations`直接生成所有排列，效率更高：
```python
from itertools import permutations  # 导入排列生成模块

count = 0
# 生成1-4的所有4个数字的排列（返回元组，比如(1,2,3,4)）
for p in permutations([1,2,3,4], 4):
    s = ''.join(map(str, p))  # 转成字符串，比如"1234"
    # 同样的检查条件
    if '13' not in s and '31' not in s and s[0] != '4':
        count += 1
        print(s, end='\n' if count%3==0 else '\t')
```
**优势**：只生成不重复的排列，不用循环无效数字，速度更快，适合更多数字的场景（比如1-5的排列）。


## 三、统计字符次数：给字符“点名计数”

### 🌟 需求
键盘输入一个字符串，统计每个字符出现的次数（比如输入“aaabbc”，输出`{'a':3, 'b':2, 'c':1}`）。


### 🚩 核心原理：用字典“键值对”记录
字典的**键**存字符，**值**存次数。遍历字符串时：
- 如果字符已在字典里，次数+1；
- 如果不在，新增键值对，次数设为1。


### 💻 三种实现方法（从基础到简洁）
#### 方法1：基础循环（适合新手理解）
```python
s = input('请输入字符串: ')
char_count = {}  # 空字典存结果

for char in s:
    if char in char_count:
        # 字符已存在，次数+1
        char_count[char] += 1
    else:
        # 字符不存在，新增记录
        char_count[char] = 1

print(char_count)  # 输入"aaabbc" → {'a':3, 'b':2, 'c':1}
```

#### 方法2：三元运算符（简化代码）
把if-else写成一行，更简洁：
```python
s = input('请输入字符串: ')
char_count = {}

for char in s:
    # 三元运算符：存在则+1，否则设为1
    char_count[char] = char_count[char] + 1 if char in char_count else 1

print(char_count)
```

#### 方法3：字典推导式（一行搞定）
用`str.count(char)`统计每个字符的次数，一行生成字典：
```python
s = input('请输入字符串: ')
# 推导式：键是s中的每个字符，值是该字符的出现次数
char_count = {char: s.count(char) for char in s}

print(char_count)
```


### 📚 拓展技巧：更实用的统计功能
#### 1. 区分大小写（比如A和a算不同字符）
默认是区分的，如果想不区分，先把字符串转成小写/大写：
```python
s = input('请输入字符串: ').lower()  # 转成小写，A和a算同一个
char_count = {char: s.count(char) for char in s}
print(char_count)  # 输入"AaBb" → {'a':2, 'b':2}
```

#### 2. 排除空格和标点（只统计字母/数字）
用`str.isalnum()`判断是否是字母或数字：
```python
s = input('请输入字符串: ')
char_count = {}

for char in s:
    if char.isalnum():  # 只统计字母和数字
        char_count[char] = char_count.get(char, 0) + 1  # get方法：没有键则返回0

print(char_count)  # 输入"Hello! 123" → {'H':1, 'e':1, 'l':2, 'o':1, '1':1, '2':1, '3':1}
```

#### 3. 用`collections.Counter`（专业工具）
Python自带的`Counter`类专门用于计数，比自己写字典更方便：
```python
from collections import Counter

s = input('请输入字符串: ')
char_count = Counter(s)  # 直接生成计数字典
print(dict(char_count))  # 转成普通字典输出
```


## 四、模拟登录：3次机会的“门禁验证”

### 🌟 需求
模拟用户登录，规则：
1. 预设正确账号（比如`heima`）和密码（比如`ai28`）；
2. 最多给3次输入机会；
3. 正确则提示欢迎，错误则提示剩余机会，3次全错则锁定账号。


### 🚩 核心原理：用for循环控制次数
用`range(3)`循环3次，每次输入账号密码：
- 正确则用`break`结束循环；
- 错误则判断是否是最后一次（i==2），最后一次提示锁定，否则提示剩余机会。


### 💻 代码实战（逐行解析）
```python
# 1. 预设正确的账号和密码
correct_username = 'heima'
correct_password = 'ai28'

# 2. 循环3次（0→1→2，对应3次机会）
for i in range(3):
    # 3. 输入账号密码
    input_username = input('请输入账号: ')
    input_password = input('请输入密码: ')
    
    # 4. 验证是否正确
    if input_username == correct_username and input_password == correct_password:
        print(f'欢迎您，{input_username}！')
        break  # 登录成功，结束循环
    else:
        # 5. 错误提示：最后一次提示锁定，否则提示剩余机会
        if i == 2:
            print('录入错误次数已达上限，账号被锁定，请联系管理员：010-123456')
        else:
            remaining = 2 - i  # 剩余机会：2→1（第一次错剩2次，第二次错剩1次）
            print(f'账号或密码错误，您还有{remaining}次机会！')
```


### 📚 拓展技巧：让登录更真实
#### 1. 密码隐藏输入（不显示明文）
用`getpass`模块隐藏输入的密码，避免被别人看到：
```python
import getpass  # 导入密码隐藏模块

correct_username = 'heima'
correct_password = 'ai28'

for i in range(3):
    input_username = input('请输入账号: ')
    # getpass.getpass()：输入时不显示明文，适合密码
    input_password = getpass.getpass('请输入密码: ')
    
    if input_username == correct_username and input_password == correct_password:
        print(f'欢迎您，{input_username}！')
        break
    else:
        if i == 2:
            print('账号锁定！')
        else:
            print(f'还有{2-i}次机会！')
```

#### 2. 记录登录日志（时间+结果）
用`datetime`模块记录每次登录的时间和结果，方便追溯：
```python
import datetime  # 导入时间模块

correct_username = 'heima'
correct_password = 'ai28'

for i in range(3):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间
    input_username = input('请输入账号: ')
    input_password = input('请输入密码: ')
    
    if input_username == correct_username and input_password == correct_password:
        print(f'[{now}] 登录成功，欢迎{input_username}！')
        break
    else:
        log = f'[{now}] 登录失败，账号：{input_username}，剩余机会：{2-i}次'
        print(log)
        # 还可以把日志写入文件：with open('login.log', 'a') as f: f.write(log+'\n')
```


## 💡 整体总结
这四个案例覆盖了Python的核心基础：
- **约瑟夫环**：列表/队列的循环操作，适合理解“线性结构模拟环形逻辑”；
- **排列组合**：范围筛选 vs 专业模块，适合理解“高效生成数据”；
- **统计字符**：字典的键值对应用，还有专业工具`Counter`；
- **模拟登录**：循环控制+条件判断，还有实用的密码隐藏、日志记录。

每个案例都可以从“基础实现”拓展到“灵活应用”，多动手改改参数（比如约瑟夫环的淘汰数字、登录的机会次数），就能更快掌握～
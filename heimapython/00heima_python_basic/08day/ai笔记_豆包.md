# 🐍 Python趣味编程小课堂：从模块到实战

嗨，各位编程小探险家！今天咱们要一起拆解一份超实用的Python笔记，里面藏着不少好玩的知识点和实战案例。从操作电脑文件的OS模块，到烧脑的约瑟夫环，再到连接数据库的PyMySQL，保证让你学得津津有味～ let's go！


## 一、OS模块：你的电脑文件小管家 📂

OS模块就像一个贴心的小管家，帮你打理电脑里的文件夹和文件。它不是Python自带的"亲戚"，所以用之前得先"请过来"（导入模块）～

### 🌟 常用技能（函数）大揭秘

| 函数名 | 作用 | 通俗解释 |
|--------|------|----------|
| `os.getcwd()` | 获取当前工作目录 | 告诉你"现在在哪文件夹里" |
| `os.chdir(路径)` | 切换工作目录 | "搬家"到另一个文件夹 |
| `os.mkdir(文件夹名)` | 创建文件夹 | 新建一个空文件夹（已存在会报错哦） |
| `os.rmdir(文件夹名)` | 删除文件夹 | 只能删空文件夹（里面有东西会耍赖不删） |
| `os.rename(旧名, 新名)` | 重命名 | 给文件或文件夹改个新名字 |
| `os.listdir(路径)` | 获取目录下所有子文件/夹 | 列出来指定文件夹里的"小伙伴"（不包含子子孙孙） |


### 📝 实战小例子

```python
import os  # 先把小管家请进来

# 看看我现在在哪
print("当前位置：", os.getcwd())

# 新建一个叫"我的文件夹"的文件夹
os.mkdir("我的文件夹")

# 看看当前目录有啥
print("当前目录内容：", os.listdir("./"))

# 给文件夹改个名
os.rename("我的文件夹", "我的新文件夹")

# 删掉这个空文件夹
os.rmdir("我的新文件夹")
```

💡 小提醒：操作文件/夹时要注意路径是否正确，不然小管家会"迷路"哦～


## 二、趣味编程练习题：动手又动脑 🧩

光说不练假把式，来几个有趣的题目练练手吧！


### 1. 约瑟夫环：找个安全的位置保命 🛡️

**故事背景**：古代皇帝杀人游戏——一群人围成圈，数到3或3的倍数就被淘汰，最后剩下的位置就是"幸运数字"（保命位）。

**需求**：输入总人数，输出幸运数字。

**思路拆解**：
1. 生成1到总人数的编号列表（比如10人就是[1,2,...,10]）
2. 循环数数，数到3的倍数就踢掉对应编号
3. 直到只剩1个人，就是答案！

**核心代码解析**：
```python
n = int(input("请输入总人数："))
num_list = list(range(1, n+1))  # 生成编号列表
num, i = 0, 0  # num是当前数的数，i是当前索引

while len(num_list) > 1:
    num += 1  # 数数：1,2,3,1,2,3...
    if i == len(num_list):  # 数完一圈从头来
        i = 0
    if num % 3 == 0:  # 数到3的倍数，踢掉！
        num_list.pop(i)
        i -= 1  # 踢掉后后面的元素会前移，索引减1
    i += 1  # 下一个人准备数数

print(f"幸运数字是：{num_list[0]}")
```

✨ 小测试：10个人的话，幸运数字是4哦，快去验证一下～


### 2. 1234排列组合：数字的排列游戏 🔢

**需求**：用1、2、3、4组成不重复的四位数，满足：
- 1和3不能挨着（比如1324不行）
- 4不能开头（比如4123不行）
- 每3个一行打印

**思路**：遍历所有可能的四位数，用字符串判断条件筛选。

**精简代码**（总共不到7行！）：
```python
count = 0
for i in range(1234, 4322):
    s = str(i)
    if '1' in s and '2' in s and '3' in s and '4' in s and '13' not in s and '31' not in s and s[0] != '4':
        count += 1
        print(i, end='\n' if count%3==0 else '\t')
```

💡 技巧：把数字转成字符串，判断包含的字符和相邻关系超方便！


### 3. 模拟斗地主：发牌大师就是你 🃏

**需求**：模拟斗地主发牌流程——买牌、洗牌、发牌、看牌。

**流程拆解**：
1. **买牌**：生成54张牌（4种花色+13个点数+大小王）
2. **洗牌**：随机打乱牌的顺序
3. **发牌**：3个玩家轮着拿牌，最后3张留作底牌
4. **看牌**：按大小排序后展示每个人的牌

**核心代码片段**：
```python
import random

# 买牌：生成牌库（键是索引，值是具体牌）
poker_dict = {i: f"{c}{n}" for i, (n, c) in enumerate([(n, c) for n in ['3','4','5','6','7','8','9','10','J','Q','K','A','2'] for c in ['♠','♥','♦','♣']])}
poker_dict[52], poker_dict[53] = '小🤡', '大🤡'

# 洗牌：打乱索引
poker_index = list(poker_dict.keys())
random.shuffle(poker_index)

# 发牌：3个玩家+底牌
p1, p2, p3, dp = [], [], [], []
for i in range(len(poker_index)):
    if i >= 51:  # 最后3张是底牌
        dp.append(poker_index[i])
    elif i%3 == 0: p1.append(poker_index[i])
    elif i%3 == 1: p2.append(poker_index[i])
    else: p3.append(poker_index[i])

# 看牌：排序后展示
def look_poker(name, nums):
    nums.sort()
    print(f"{name}的牌：{[poker_dict[i] for i in nums]}")

look_poker("玩家1", p1)
look_poker("底牌", dp)
```

🎉 效果：运行后就能看到每个人的牌啦，是不是有内味儿了～


### 4. 字符计数：数数每个字出现几次 📊

**需求**：输入一个字符串，统计每个字符出现的次数（比如"aaabbc"输出{'a':3, 'b':2, 'c':1}）。

**三种实现方式**：

1. **基础循环法**：
```python
s = input("请输入字符串：")
wc_dict = {}
for c in s:
    if c in wc_dict:
        wc_dict[c] += 1
    else:
        wc_dict[c] = 1
print(wc_dict)
```

2. **三元运算符法**（精简版）：
```python
wc_dict = {}
for c in s:
    wc_dict[c] = wc_dict[c] + 1 if c in wc_dict else 1
```

3. **字典推导式**（一行搞定！）：
```python
wc_dict = {c: s.count(c) for c in s}
```

💡 小知识：`str.count(c)`可以直接返回字符c在字符串中出现的次数，超方便！


### 5. 模拟登录：3次机会的考验 🔑

**需求**：输入账号密码，最多错3次，错满就锁定。

**代码解析**：
```python
username, password = "heima", "ai28"  # 正确账号密码

for i in range(3):  # 3次机会
    uname = input("请输入账号：")
    pwd = input("请输入密码：")
    if uname == username and pwd == password:
        print(f"欢迎回来，{uname}！")
        break  # 登录成功就跳出循环
    else:
        # 提示剩余次数，最后一次提示锁定
        print("账号锁定，请联系管理员" if i == 2 else f"错啦！还剩{2-i}次机会")
```

🚨 注意：实际开发中密码不会明文存储，这里只是模拟哦～


## 三、递归：函数自己调用自己？有点绕但很酷！ ♻️

递归就是"自己调用自己"，听起来像绕口令，但掌握了超好用！不过有两个铁律：
1. 必须有**出口**（不然会无限循环，内存爆炸）
2. 必须有**规律**（重复做类似的事）


### 1. 递归求阶乘：数学题的小帮手 🧮

**阶乘定义**：n! = n × (n-1) × ... × 1（比如5! = 5×4×3×2×1）

**出口**：1! = 1（再往下算就是0! = 1，不过这里简化到1）

**规律**：n! = n × (n-1)!

**代码**：
```python
def factorial(n):
    if n == 1:  # 出口
        return 1
    return n * factorial(n-1)  # 规律：自己调用自己

print(factorial(5))  # 输出：120
```


### 2. 斐波那契数列：不死神兔的故事 🐰

**故事**：1对小兔子1个月长成大兔子，大兔子每个月生1对小兔子，求1年后有多少对兔子？

**规律**：
- 第1、2个月：1对兔子
- 从第3个月起：当月兔子数 = 上月 + 上上月（因为大兔子生小兔子，小兔子长大）

**代码**：
```python
def get_rabbit(month):
    if month in [1, 2]:  # 出口：前两个月都是1对
        return 1
    return get_rabbit(month-1) + get_rabbit(month-2)  # 规律

print(get_rabbit(12))  # 输出：144（1年后144对！）
```

💡 小提醒：递归虽然优雅，但调用次数多了会变慢，复杂场景可以用循环优化～


## 四、PyMySQL：Python和MySQL的桥梁 🚀

想让Python操作MySQL数据库？PyMySQL就是它们的"翻译官"！


### 🔧 准备工作：安装PyMySQL

```bash
pip install pymysql  # 直接安装
# 或者用国内镜像加速
pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple
```


### 📝 操作步骤（重点！）

1. **建立连接**：Python和MySQL"握手"
2. **获取游标**：执行SQL的"工具人"
3. **执行SQL**：增删改查全靠它
4. **处理结果**：查询到的数据要处理
5. **释放资源**：用完记得"说再见"

用比喻理解：连接像"前台小姐姐"，游标像"任课老师"，SQL像"课程内容"，结果像"笔记作业"～


### 🔍 CRUD实战（增删改查）

#### 1. 查（查询数据）
```python
import pymysql

# 1. 连接数据库
conn = pymysql.connect(
    host="localhost",  # 数据库地址（本地是localhost）
    port=3306,         # 端口号（MySQL默认3306）
    user="root",       # 账号
    password="123456", # 密码
    database="day02",  # 数据库名
    charset="utf8"     # 编码
)

# 2. 获取游标
cur = conn.cursor()

# 3. 执行查询SQL
cur.execute("select * from hero;")

# 4. 处理结果（获取3条数据）
data = cur.fetchmany(3)
print("查询结果：", data)

# 5. 释放资源
cur.close()
conn.close()
```


#### 2. 增删改（注意要提交！）
增删改需要最后"提交"才能生效，就像写完作业要交上去才有效～

```python
def add_hero():
    conn = pymysql.connect(...)
    cur = conn.cursor()
    # 新增数据
    sql = "insert into hero values(6, '杨过', 20);"
    n = cur.execute(sql)  # n是受影响的行数
    conn.commit()  # 必须提交！
    print("添加成功" if n > 0 else "添加失败")
    cur.close()
    conn.close()

# 同理：删除用delete，修改用update，都要加conn.commit()
```


## 总结：今天学了啥？ 📝

- **OS模块**：操作文件/夹的小管家
- **趣味练习**：约瑟夫环、排列组合、斗地主等实战案例
- **递归**：自己调用自己，记住出口和规律
- **PyMySQL**：连接MySQL，实现增删改查

这些知识点都是Python编程中的"家常菜"，多敲几遍代码就能熟练啦～ 下次遇到类似问题，别忘了今天学的小技巧哦！😉
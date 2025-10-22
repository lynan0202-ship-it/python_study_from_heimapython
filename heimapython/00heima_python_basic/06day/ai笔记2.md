# Python核心知识点详解（续）


## 七、交换变量值

### 1. 基础方法
交换变量值有多种实现方式，核心是让两个变量的值互换，常见方法包括：临时变量法、拆包法、算术运算法、位运算法。


### 2. 经典用法

#### （1）临时变量法（通用）
通过第三方变量暂存其中一个值，实现交换，适用于所有类型变量。
```python
# 交换字符串变量
s1 = "刘亦菲"
s2 = "胡歌"

# 临时变量法
tmp = s1  # 暂存s1的值
s1 = s2   # s1接收s2的值
s2 = tmp  # s2接收暂存的s1原值
print(f"s1: {s1}, s2: {s2}")  # 输出：s1: 胡歌, s2: 刘亦菲
```


#### （2）拆包法（Python特有，推荐）
利用Python的拆包特性，一行代码完成交换，简洁高效，适用于所有类型变量。
```python
# 交换数字变量
a = 10
b = 20

# 拆包法（本质：先组包(b,a)为元组，再拆包给a和b）
a, b = b, a
print(f"a: {a}, b: {b}")  # 输出：a: 20, b: 10
```


#### （3）算术运算法（仅适用于数字）
通过加减法实现交换，无需临时变量，但仅适用于整数/浮点数。
```python
a = 10
b = 20

# 算术运算法
a = a + b  # a = 30（总和）
b = a - b  # b = 30 - 20 = 10（原a的值）
a = a - b  # a = 30 - 10 = 20（原b的值）
print(f"a: {a}, b: {b}")  # 输出：a: 20, b: 10
```


#### （4）位运算法（仅适用于整数）
利用位运算的特性（一个数异或另一个数两次等于自身），无需临时变量，仅适用于整数。
```python
a = 10  # 二进制：1010
b = 20  # 二进制：10100

# 位运算法（异或^）
a = a ^ b  # a = 10 ^ 20 = 30（二进制：11110）
b = a ^ b  # b = 30 ^ 20 = 10（原a的值）
a = a ^ b  # a = 30 ^ 10 = 20（原b的值）
print(f"a: {a}, b: {b}")  # 输出：a: 20, b: 10
```


### 3. 拓展问题
- 推荐使用**拆包法**：简洁、通用（支持所有类型），是Python中交换变量的最佳实践。
- 算术/位运算法局限性：仅适用于数字，且算术法可能出现溢出（如超大整数相加）。
- 临时变量法优势：逻辑清晰，适合初学者理解，兼容所有编程语言。


## 八、引用详解

### 1. 基础概念
- **引用**：变量在内存中的地址（位置），Python中所有变量赋值本质都是“引用传递”（拷贝地址）。
- **查看引用**：通过`id(变量名)`函数获取变量的内存地址（整数形式）。
- **可变与不可变类型**：
  - 可变类型：修改内容时地址不变（如列表、字典、集合）。
  - 不可变类型：修改内容时地址改变（如整数、字符串、元组、布尔值）。


### 2. 经典示例

#### （1）引用的基本特性
多个变量可指向同一地址（共享引用）。
```python
# 多个变量共享同一引用
a = 10
b = a  # b拷贝a的地址（引用）
c = a  # c拷贝a的地址

print(id(a))  # 输出：140714022086720（地址相同）
print(id(b))  # 输出：140714022086720
print(id(c))  # 输出：140714022086720
```


#### （2）可变类型的引用特性
修改内容时地址不变（原对象被修改）。
```python
# 列表（可变类型）
list1 = [1, 2, 3]
print(f"修改前内容：{list1}，地址：{id(list1)}")  # 地址1

# 修改列表内容（不改变地址）
list1.append(100)  # 追加元素
list1[1] = 200     # 修改元素
print(f"修改后内容：{list1}，地址：{id(list1)}")  # 地址1（与修改前相同）
```


#### （3）不可变类型的引用特性
修改内容时地址改变（创建新对象）。
```python
# 字符串（不可变类型）
s1 = "abc"
print(f"修改前内容：{s1}，地址：{id(s1)}")  # 地址2

# 修改字符串内容（创建新对象，地址改变）
s1 = "xyz"  # 重新赋值，指向新字符串
print(f"修改后内容：{s1}，地址：{id(s1)}")  # 地址3（与修改前不同）
```


### 3. 拓展问题
- 引用传递 vs 值传递：Python中只有**引用传递**，不存在值传递。变量赋值、函数传参都是拷贝地址。
- 可变类型的“陷阱”：多个变量指向同一可变对象时，修改其中一个会影响所有变量（因为共享引用）。
  ```python
  list2 = [1, 2, 3]
  list3 = list2  # 共享引用
  list3.append(4)
  print(list2)  # 输出：[1, 2, 3, 4]（list2也被修改）
  ```


## 九、引用相关面试题

### 1. 核心结论
- 当函数参数为**不可变类型**（如int、str）：修改形参不会影响实参（形参会指向新地址）。
- 当函数参数为**可变类型**（如list、dict）：修改形参会直接影响实参（共享同一地址）。


### 2. 经典示例
```python
# 函数1：参数为不可变类型（int）
def change_num(num):
    num = 200  # 形参指向新地址，不影响实参

# 函数2：参数为可变类型（list）
def change_list(list1):
    list1[1] = 28  # 形参与实参共享地址，修改会影响实参

if __name__ == '__main__':
    # 测试不可变类型
    a = 100
    print(f"调用前a：{a}")  # 输出：100
    change_num(a)
    print(f"调用后a：{a}")  # 输出：100（无变化）

    # 测试可变类型
    list1 = [1, 2, 3, 4, 5]
    print(f"调用前list1：{list1}")  # 输出：[1, 2, 3, 4, 5]
    change_list(list1)
    print(f"调用后list1：{list1}")  # 输出：[1, 28, 3, 4, 5]（被修改）
```


### 3. 拓展问题
- 如何避免可变类型参数被修改？可通过拷贝创建新对象（如`list1.copy()`或`list(list1)`）。
  ```python
  def safe_change(list1):
      new_list = list1.copy()  # 创建副本，不影响原列表
      new_list[1] = 28
      print("函数内新列表：", new_list)

  list1 = [1, 2, 3]
  safe_change(list1)
  print("函数外原列表：", list1)  # 输出：[1, 2, 3]（未修改）
  ```


## 十、匿名函数（lambda）

### 1. 基础结构
- **定义**：没有名字的函数，适用于简单逻辑（仅一行代码）。
- **格式**：`变量名 = lambda 形参列表 : 函数体`（函数体结果自动返回）。


### 2. 经典用法

#### （1）基本使用（替代简单函数）
```python
# 普通函数：计算两数之和
def get_sum(a, b):
    return a + b
print(get_sum(10, 20))  # 输出：30

# 匿名函数实现相同功能
my_sum = lambda a, b: a + b  # 形参为a、b，函数体为a+b
print(my_sum(10, 20))  # 输出：30
```


#### （2）作为参数传递（灵活适配逻辑）
匿名函数可作为参数传递给其他函数，动态指定处理逻辑。
```python
# 定义通用函数，接收一个处理逻辑（函数）
def calculate(a, b, func):
    """根据传入的func逻辑计算a和b的结果"""
    return func(a, b)

# 调用时传入不同匿名函数，实现不同计算
print("和：", calculate(10, 3, lambda a, b: a + b))       # 输出：13
print("差：", calculate(10, 3, lambda a, b: a - b))       # 输出：7
print("积：", calculate(10, 3, lambda a, b: a * b))       # 输出：30
print("最大值：", calculate(10, 3, lambda a, b: a if a > b else b))  # 输出：10
```


### 3. 拓展问题
- 适用场景：逻辑简单（一行代码）、仅需调用一次的函数（如排序、过滤的回调逻辑）。
- 局限性：函数体只能有一行代码，无法实现复杂逻辑（需用普通函数）。
- 与普通函数的选择：简单逻辑用lambda简化代码，复杂逻辑用普通函数保证可读性。


## 十一、文件操作-读

### 1. 基础流程
文件读取的基本步骤：打开文件 → 读取内容 → 关闭文件。


### 2. 核心API
| 函数          | 说明                                  |
|---------------|---------------------------------------|
| `open(路径, 模式)` | 打开文件，返回文件对象                |
| `read(num)`   | 读取num个字节（默认读取全部）         |
| `readline()`  | 读取一行内容（包含换行符`\n`）        |
| `readlines()` | 读取所有行，返回列表（每行作为元素）  |
| `close()`     | 关闭文件（释放资源）                  |


### 3. 经典用法

#### （1）路径写法（绝对路径 vs 相对路径）
```python
# 绝对路径：完整路径（不同系统写法不同）
# Windows：r'D:\data\a.txt'（r取消转义）或 'D:/data/a.txt'
# Linux/Mac：'/home/user/data/a.txt'

# 相对路径：相对于当前项目的路径（推荐）
# ./ 表示当前目录，../ 表示上一级目录
f = open('./data/a.txt', 'r', encoding='utf-8')  # 打开当前目录下的a.txt
```


#### （2）三种读取方式
```python
# 打开文件（读模式'r'）
f = open('./data/a.txt', 'r', encoding='utf-8')

# 1. read()：读取全部内容（适合小文件）
content = f.read()
print("全部内容：", content)

# 2. readline()：逐行读取（适合大文件）
f.seek(0)  # 移动指针到文件开头
line1 = f.readline()
line2 = f.readline()
print("第一行：", line1)
print("第二行：", line2)

# 3. readlines()：读取所有行（返回列表）
f.seek(0)
lines = f.readlines()
print("所有行：", lines)  # 输出：['第一行\n', '第二行\n', '第三行']

# 关闭文件
f.close()
```


### 4. 拓展问题
- 大文件读取：避免用`read()`或`readlines()`（占用大量内存），推荐用`readline()`循环读取：
  ```python
  with open('./data/big_file.txt', 'r') as f:
      while True:
          line = f.readline()
          if not line:  # 读取到空行，说明文件结束
              break
          print(line.strip())  # 处理每行内容（strip()移除换行符）
  ```
- 指针位置：读取后指针会移动，需用`f.seek(0)`重置到开头才能重新读取。


## 十二、文件操作-读-中文处理

### 1. 编码基础
- 计算机存储字符需通过“码表”转换为二进制：
  - `ASCII`：仅包含英文、数字、符号（1字节）。
  - `GBK`：中文占2字节（国内常用）。
  - `UTF-8`：中文占3字节（国际通用，推荐）。
- 乱码原因：读取时使用的编码与文件保存时的编码不一致。


### 2. 经典用法（解决中文乱码）
打开文件时指定正确的编码（与文件保存编码一致）。
```python
# 读取含中文的文件（指定编码为utf-8）
f = open('./data/chinese.txt', 'r', encoding='utf-8')  # 关键：指定encoding
content = f.read()
print(content)  # 正常显示中文
f.close()

# 二进制模式读取（无需指定编码，返回字节数据）
f = open('./data/chinese.txt', 'rb')  # 二进制读模式'rb'
byte_data = f.read()
print(byte_data)  # 输出：b'中文内容'（字节形式）
print(byte_data.decode('utf-8'))  # 解码为字符串（需指定编码）
f.close()
```


### 3. 拓展问题
- 编码检测：若不确定文件编码，可使用`chardet`库检测（需安装：`pip install chardet`）。
  ```python
  import chardet
  with open('./data/unknown.txt', 'rb') as f:
      data = f.read()
      result = chardet.detect(data)  # 检测编码
      print("文件编码：", result['encoding'])  # 输出检测到的编码
  ```


## 十三、文件操作-写

### 1. 基础模式
- `w`：覆盖写入（文件不存在则创建，存在则清空原有内容）。
- `a`：追加写入（文件不存在则创建，新内容添加到末尾）。


### 2. 核心API
| 函数            | 说明                          |
|-----------------|-------------------------------|
| `write(内容)`   | 写入字符串（需手动加换行符`\n`） |
| `writelines(列表)` | 写入字符串列表（不自动加换行）  |


### 3. 经典用法

#### （1）基本写入
```python
# 覆盖写入（w模式）
with open('./data/write_test.txt', 'w', encoding='utf-8') as f:
    f.write('第一行内容\n')  # 手动加换行符
    f.write('第二行内容')

# 追加写入（a模式）
with open('./data/write_test.txt', 'a', encoding='utf-8') as f:
    f.write('\n第三行内容')  # 追加到末尾
```


#### （2）文件拷贝（读+写结合）
```python
# 拷贝文件（以二进制模式兼容所有文件类型：文本、图片、视频等）
def copy_file(src_path, dest_path):
    # 打开源文件（读）和目标文件（写）
    with open(src_path, 'rb') as src_f, open(dest_path, 'wb') as dest_f:
        # 循环读取（每次8KB，避免内存占用过大）
        while True:
            data = src_f.read(8192)  # 8192字节 = 8KB
            if not data:  # 读取完毕
                break
            dest_f.write(data)  # 写入目标文件

# 调用拷贝函数
copy_file('./data/source.txt', './data/copy.txt')
```


### 4. 拓展问题
- 二进制模式的必要性：拷贝非文本文件（图片、视频）时，必须用`rb`和`wb`模式（避免编码转换错误）。
- 换行符差异：Windows用`\r\n`，Linux/Mac用`\n`，Python会自动处理（文本模式下）。


## 十四、综合案例-文件备份

### 1. 需求
输入文件名，生成备份文件，格式为“原文件名[备份].原后缀”（如`test.txt`→`test[备份].txt`）。


### 2. 实现代码
```python
# 文件备份工具
old_name = input("请输入要备份的文件名：")

# 找到最后一个'.'的位置（区分文件名和后缀）
index = old_name.rfind('.')

if index > 0:  # 文件名合法（有后缀）
    # 拼接新文件名：原文件名[备份].后缀
    new_name = old_name[:index] + '[备份]' + old_name[index:]
    
    # 二进制模式读写（兼容所有文件类型）
    with open(old_name, 'rb') as old_f, open(new_name, 'wb') as new_f:
        while True:
            data = old_f.read(8192)  # 每次读8KB
            if not data:
                break
            new_f.write(data)  # 写入备份文件
    print(f"备份成功！新文件：{new_name}")
else:  # 文件名不合法（无后缀或'.'在开头）
    print("文件名格式错误，无法备份！")
```


### 3. 关键知识点
- `rfind('.')`：从右向左查找`.`的位置（处理含多个`.`的文件名，如`abc.tar.gz`）。
- 二进制读写：`rb`和`wb`模式确保图片、压缩包等非文本文件也能正确备份。
- 边界处理：判断文件名合法性（避免`.`在开头或无后缀的情况）。


## 十五、扩展：with-open语法

### 1. 基础结构
`with-open`语句自动管理文件资源，无需手动调用`close()`，适用于所有文件操作。

```python
# 基本格式
with open('文件路径', '模式', encoding='编码') as 别名:
    # 对文件的读写操作（语句体执行完自动关闭文件）
```


### 2. 经典用法

#### （1）单文件操作
```python
# 读取文件（自动关闭）
with open('./data/a.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)  # 无需手动close()
```


#### （2）多文件操作（同时打开多个文件）
```python
# 同时打开源文件和目标文件（拷贝场景）
with open('./data/source.txt', 'rb') as src_f, open('./data/dest.txt', 'wb') as dest_f:
    # 循环拷贝
    while True:
        data = src_f.read(8192)
        if not data:
            break
        dest_f.write(data)
```


### 3. 拓展问题
- 优势：避免因忘记`close()`导致的资源泄露，尤其在异常场景下（如程序崩溃前仍能关闭文件）。
- 适用场景：所有文件操作均推荐使用`with-open`，替代手动`open()`和`close()`。


## 总结
本部分重点讲解了变量交换、引用机制、匿名函数及文件操作的核心知识点。其中，**引用传递**是理解Python变量行为的关键，**文件操作**需掌握读写模式、编码处理及`with-open`的正确用法，**匿名函数**则为简单逻辑提供了简洁的实现方式。这些知识点在实际开发中应用广泛，需结合案例深入理解。
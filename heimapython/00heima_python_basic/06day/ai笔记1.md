# Python核心知识点详解

## 一、函数返回多个值

### 1. 基础结构
函数可以同时返回多个值，默认会将多个值封装成元组返回；也可手动封装为列表、集合等容器类型。

```python
# 函数返回多个值的基础结构
def 函数名(参数1, 参数2, ...):
    # 业务逻辑处理
    结果1 = ...
    结果2 = ...
    ...
    return 结果1, 结果2, ...  # 默认组包为元组
    # 或 return [结果1, 结果2, ...]  # 手动封装为列表
```


### 2. 经典用法
```python
# 案例：自定义计算器函数，返回两个数的加减乘除结果
def calculate(num1, num2):
    """计算两个整数的加减乘除结果"""
    sum_result = num1 + num2    # 和
    sub_result = num1 - num2    # 差
    mul_result = num1 * num2    # 积
    div_result = num1 // num2   # 整除商（假设num2不为0）
    return sum_result, sub_result, mul_result, div_result  # 默认组包为元组

# 调用函数并接收返回值
if __name__ == '__main__':
    result = calculate(10, 3)
    print("返回结果：", result)  # 输出：(13, 7, 30, 3)
    print("结果类型：", type(result))  # 输出：<class 'tuple'>

    # 也可拆包接收每个结果
    sum_res, sub_res, mul_res, div_res = calculate(10, 3)
    print(f"和：{sum_res}，差：{sub_res}，积：{mul_res}，商：{div_res}")
```


### 3. 拓展问题
- 若返回值数量与接收变量数量不匹配，会报错（`ValueError`）。例如：`a, b = calculate(10, 3)` 会报错（需要4个变量接收）。
- 可通过 `*变量名` 接收多余的返回值（拆包技巧），例如：`a, b, *rest = calculate(10, 3)`，其中 `rest` 会接收剩余的两个值（`[30, 3]`）。


## 二、函数参数详解

函数参数分为**实参**（调用时传递的参数）和**形参**（定义时声明的参数）两类。


### （一）实参：位置参数与关键字参数

#### 1. 位置参数
- **定义**：按参数位置顺序传递的实参，要求实参的**数量和顺序必须与形参完全一致**。
- **经典用法**：
  ```python
  # 定义函数：打印用户信息
  def user_info(name, age, address):
      print(f"姓名：{name}，年龄：{age}，地址：{address}")

  # 调用函数（位置参数）
  if __name__ == '__main__':
      user_info("张三", 23, "北京")  # 正确：顺序和数量与形参一致
      user_info("张三", "北京", 23)  # 错误：顺序错误，结果不符合预期（年龄会显示"北京"）
  ```


#### 2. 关键字参数
- **定义**：通过 `形参名=值` 的形式传递实参，**不要求顺序，但必须保证参数名正确**。
- **规则**：若同时使用位置参数和关键字参数，**位置参数必须放在前面**。
- **经典用法**：
  ```python
  # 延续上面的user_info函数
  if __name__ == '__main__':
      # 纯关键字参数（顺序可任意）
      user_info(address="上海", name="李四", age=25)  # 正确：通过参数名指定，顺序无关
      
      # 混合使用（位置参数在前，关键字参数在后）
      user_info("王五", age=24, address="广州")  # 正确："王五"是位置参数（对应name）
      
      # user_info(address="深圳", "赵六", 26)  # 错误：关键字参数不能在位置参数前面
  ```


### （二）形参：缺省参数与不定长参数

#### 1. 缺省参数（默认参数）
- **定义**：在形参列表中预先指定默认值的参数，格式为 `形参名=默认值`。
- **规则**：缺省参数必须放在**形参列表的最后**（避免位置混淆）。
- **特性**：调用时若不传递该参数，则使用默认值；若传递，则覆盖默认值。
- **经典用法**：
  ```python
  # 定义带缺省参数的函数（address默认值为"三亚"）
  def user_info(name, age, address="三亚"):  # 缺省参数放最后
      print(f"姓名：{name}，年龄：{age}，地址：{address}")

  if __name__ == '__main__':
      user_info("张三", 23)  # 不传递address，使用默认值"三亚"
      user_info("李四", 25, "北京")  # 传递address，覆盖默认值
  ```


#### 2. 不定长参数（可变参数）
用于处理实参数量不确定的场景，分为两种：

##### （1）`*args`：接收位置参数
- **作用**：接收所有未匹配的位置参数，封装成**元组**。
- **命名**：`args` 是约定俗成的名称，可自定义，但建议使用 `args`。
- **经典用法**：
  ```python
  # 定义接收任意位置参数的函数
  def print_args(*args):
      print("接收的参数：", args)
      print("参数类型：", type(args))  # 输出：<class 'tuple'>

  if __name__ == '__main__':
      print_args(10, "hello", True)  # 输出：(10, 'hello', True)
      print_args()  # 允许接收0个参数，输出：()
  ```


##### （2）`**kwargs`：接收关键字参数
-** 作用 **：接收所有未匹配的关键字参数，封装成**字典**（键为参数名，值为参数值）。
-** 命名 **：`kwargs` 是约定俗成的名称，可自定义，但建议使用 `kwargs`。
-** 经典用法 **：
  ```python
  # 定义接收任意关键字参数的函数
  def print_kwargs(**kwargs):
      print("接收的参数：", kwargs)
      print("参数类型：", type(kwargs))  # 输出：<class 'dict'>

  if __name__ == '__main__':
      print_kwargs(name="张三", age=23, address="北京")  # 输出：{'name': '张三', 'age': 23, 'address': '北京'}
      print_kwargs()  # 允许接收0个参数，输出：{}
  ```


##### （3）混合使用规则
若同时使用 `*args`、`**kwargs` 和其他参数，顺序必须为：  
`普通参数 → *args → 缺省参数 → **kwargs`

```python
# 混合使用示例
def mix_params(a, *args, b="默认值", **kwargs):
    print(f"普通参数a：{a}")
    print(f"*args：{args}")
    print(f"缺省参数b：{b}")
    print(f"** kwargs：{kwargs}")

if __name__ == '__main__':
    mix_params(10, 20, 30, b="新值", name="张三", age=23)
    # 输出：
    # 普通参数a：10
    # *args：(20, 30)
    # 缺省参数b：新值
    # **kwargs：{'name': '张三', 'age': 23}
```


##### （4）不定长参数的典型应用：求任意个数的和
```python
# 计算任意个整数的和
def get_sum(*args):
    return sum(args)  # sum()函数可直接计算元组元素的和

if __name__ == '__main__':
    print(get_sum(1, 2, 3))  # 输出：6
    print(get_sum(10, 20, 30, 40))  # 输出：100
    print(get_sum())  # 输出：0（无参数时sum()返回0）
```


## 三、组包和拆包

### 1. 基础概念
-** 组包 **：将多个值赋值给一个变量时，Python会自动将其封装成元组（多→1）。
-** 拆包 **：将一个容器（元组、列表、字典等）的元素分别赋值给多个变量（1→多）。


### 2. 经典用法

#### （1）组包
```python
# 组包示例
# 多个值赋值给一个变量，自动封装为元组
data = 10, 20, 30, "hello"
print(data)  # 输出：(10, 20, 30, 'hello')
print(type(data))  # 输出：<class 'tuple'>
```


#### （2）拆包
```python
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

v1, v2 = dict1.values()  # 获取值
print(v1, v2)  # 输出：李四 25

item1, item2 = dict1.items()  # 获取键值对（元组形式）
print(item1, item2)  # 输出：('name', '李四') ('age', 25)
```


### 3. 拓展问题
- 拆包时，变量数量必须与容器元素数量一致，否则报错。例如：`a, b = [1, 2, 3]` 会报错（需要3个变量）。
- 可通过 `*变量名` 接收多余元素（变量会被封装成列表）：
  ```python
  list2 = [1, 2, 3, 4, 5]
  x, y, *rest = list2
  print(x, y)  # 输出：1 2
  print(rest)  # 输出：[3, 4, 5]（多余元素被封装成列表）
  ```


## 四、扩展：交换变量值

利用拆包特性，可简洁地交换两个变量的值，无需临时变量。

```python
# 传统交换方式（需要临时变量）
a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)  # 输出：20 10

# 利用拆包交换（简洁）
a = 10
b = 20
a, b = b, a  # 本质：先组包(b, a)为元组，再拆包给a和b
print(a, b)  # 输出：20 10
```


## 五、可变类型与不可变类型

### 1. 基础概念
-** 不可变类型 **：变量的值修改后，内存地址会改变（原数据不可修改，修改时会创建新对象）。
-** 可变类型 **：变量的值修改后，内存地址不变（原数据可直接修改，不创建新对象）。


### 2. 常见类型分类
| 类型       | 可变/不可变 | 示例                 |
|------------|-------------|----------------------|
| 整数(int)  | 不可变      | `a = 10; a = 20`     |
| 字符串(str)| 不可变      | `s = "abc"; s += "d"`|
| 元组(tuple)| 不可变      | `t = (1, 2); t[0] = 3`（报错）|
| 列表(list) | 可变        | `l = [1, 2]; l.append(3)` |
| 字典(dict) | 可变        | `d = {"a":1}; d["b"] = 2` |
| 集合(set)  | 可变        | `s = {1, 2}; s.add(3)` |


### 3. 经典示例
```python
# 不可变类型：整数
a = 10
print("修改前a的地址：", id(a))  # 地址1
a = 20  # 修改值，创建新对象
print("修改后a的地址：", id(a))  # 地址2（与地址1不同）

# 不可变类型：字符串
s = "hello"
print("修改前s的地址：", id(s))  # 地址3
s += " world"  # 修改值，创建新对象
print("修改后s的地址：", id(s))  # 地址4（与地址3不同）

# 可变类型：列表
list1 = [1, 2, 3]
print("修改前list1的地址：", id(list1))  # 地址5
list1.append(4)  # 修改值，原对象直接修改
print("修改后list1的地址：", id(list1))  # 地址5（与修改前相同）
```


### 4. 拓展问题：函数参数传递的影响
- 不可变类型作为函数参数：函数内修改参数值，不会影响外部变量（因为创建了新对象）。
- 可变类型作为函数参数：函数内修改参数值，会影响外部变量（因为修改的是原对象）。

```python
# 不可变类型参数
def change_num(n):
    n = 100  # 内部修改，创建新对象
    print("函数内n：", n)

num = 10
change_num(num)
print("函数外num：", num)  # 输出：10（外部变量未变）

# 可变类型参数
def change_list(l):
    l.append(4)  # 内部修改原对象
    print("函数内list：", l)

my_list = [1, 2, 3]
change_list(my_list)
print("函数外my_list：", my_list)  # 输出：[1, 2, 3, 4]（外部变量被修改）
```


## 六、文件相关操作

### （一）os模块（操作系统交互）
`os` 模块提供与操作系统交互的功能，如文件/目录操作。

#### 1. 基础用法（常用函数）
```python
import os

# 1. 获取当前工作目录
current_dir = os.getcwd()
print("当前目录：", current_dir)

# 2. 创建目录（mkdir：创建单级目录；makedirs：创建多级目录）
os.mkdir("test_dir")  # 创建单级目录
os.makedirs("a/b/c")  # 创建多级目录（a→b→c）

# 3. 删除目录（rmdir：删除空目录；若目录非空，需先删除内容）
os.rmdir("test_dir")  # 删除单级空目录

# 4. 列出目录下的文件和子目录
files = os.listdir(".")  # "."表示当前目录
print("当前目录内容：", files)

# 5. 删除文件
with open("test.txt", "w") as f:  # 先创建文件
    f.write("测试文件")
os.remove("test.txt")  # 删除文件
```


### （二）文件读写基础

#### 1. 文件打开模式
| 模式 | 说明 |
|------|------|
| `r`  | 只读（默认），文件不存在则报错 |
| `w`  | 只写，文件不存在则创建，存在则覆盖原有内容 |
| `a`  | 追加，文件不存在则创建，新内容添加到末尾 |
| `r+` | 读写 |
| `b`  | 二进制模式（如`rb`、`wb`，用于非文本文件如图片） |


#### 2. 读文件
```python
# 方法1：手动打开和关闭文件（需确保关闭，否则占用资源）
file = open("example.txt", "r", encoding="utf-8")  # 打开文件（指定编码避免中文乱码）
content = file.read()  # 读取全部内容
print("全部内容：", content)

file.seek(0)  # 移动文件指针到开头（否则readline()会从上次结束位置开始）
line1 = file.readline()  # 读取一行
print("第一行：", line1)

file.seek(0)
lines = file.readlines()  # 读取所有行，返回列表
print("所有行：", lines)

file.close()  # 必须关闭文件


# 方法2：推荐使用with...open()（自动关闭文件，无需手动调用close()）
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("with方式读取：", content)
```


#### 3. 写文件
```python
# 1. 覆盖写入（w模式）
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("第一行内容\n")  # 写入字符串（需手动加换行符\n）
    f.writelines(["第二行内容\n", "第三行内容\n"])  # 写入字符串列表

# 2. 追加写入（a模式）
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("追加的内容\n")
```


### （三）扩展：with...open()语句
-** 优势 **：自动管理文件资源，无论是否发生异常，都会确保文件被关闭（避免资源泄露）。
-** 多文件操作 **：可同时打开多个文件：
  ```python
  # 同时打开两个文件（读一个，写一个）
  with open("input.txt", "r") as f_read, open("output.txt", "w") as f_write:
      content = f_read.read()
      f_write.write(content)  # 将input.txt内容复制到output.txt
  ```


### 4. 拓展问题
- 中文乱码：打开文件时指定 `encoding="utf-8"`（或文件实际编码）。
- 大文件读取：若文件过大，`read()` 会占用大量内存，建议用 `readline()` 逐行读取：
  ```python
  with open("big_file.txt", "r") as f:
      while True:
          line = f.readline()
          if not line:  # 读取到空行，说明文件结束
              break
          print(line)  # 处理每行内容
  ```
# Python异常处理详解


## 一、异常概述

### 1. 基础概念
- **定义**：程序运行过程中出现的所有非正常情况，统称为“异常”（俗称Bug）
- **本质**：打破程序正常执行流程的错误事件


### 2. 常见异常类型
| 异常类型 | 说明 |
|---------|------|
| `FileNotFoundError` | 尝试读取不存在的文件时触发 |
| `ZeroDivisionError` | 除数为0时触发 |
| `NameError` | 使用未定义的变量时触发 |
| `TypeError` | 数据类型不匹配时触发（如字符串+数字） |
| `ValueError` | 数据值不合法时触发（如`int("abc")`） |


### 3. 异常的默认处理方式
- 程序会打印3类信息：异常类型、异常原因、异常位置
- 打印后立即终止程序执行（后续代码不再运行）

```python
# 演示异常的默认处理
# 1. 除零异常（会终止程序）
print(10 // 0)  # ZeroDivisionError: integer division or modulo by zero
print("这段代码不会执行")  # 因为上面的异常已终止程序
```


### 4. 拓展问题
- 为什么需要处理异常？  
  避免程序意外崩溃，提高程序健壮性（比如用户输入错误时，程序应提示而非直接退出）
- 异常和错误的区别？  
  错误一般指语法错误（编写阶段就能发现），异常是运行时错误（编写时可能无法预知）


## 二、捕获异常基础（try-except）

### 1. 基础结构
```python
try:
    # 可能出现异常的代码块
    可能出问题的代码
except:
    # 异常发生时的处理方案
    出问题后的解决方案
```


### 2. 执行流程
1. 先执行`try`中的代码
2. 若`try`中无异常：跳过`except`，继续执行后续代码
3. 若`try`中有异常：立即跳转到`except`执行处理逻辑，之后继续执行后续代码


### 3. 经典用法
```python
# 演示基本的异常捕获
try:
    print("尝试读取文件...")
    # 尝试打开不存在的文件（会触发异常）
    file = open("不存在的文件.txt", "r")
    print("文件读取成功")  # 若上面出错，这句不会执行
except:
    # 异常处理逻辑
    print("出错了：文件不存在，请检查文件名！")

# 异常处理后，程序会继续执行
print("程序继续运行中...")
```


### 4. 拓展问题
- `try`中哪行代码出错，就从哪行跳转到`except`，`try`中后续代码不再执行
- `except`不指定异常类型时，会捕获**所有异常**（不推荐，可能掩盖未知问题）


## 三、精准捕获异常（Exception）

### 1. 基础结构
```python
try:
    可能出问题的代码
except 异常类型 as 异常对象:
    # 处理指定类型的异常
    print(f"发生{异常类型}：{异常对象}")
```

- `Exception`：所有异常的父类，可代表所有异常
- `as 异常对象`：将异常信息保存到变量中（通常用`e`表示）


### 2. 经典用法
#### （1）捕获单个指定异常
```python
try:
    print(name)  # 使用未定义的变量，触发NameError
except NameError as e:
    # 仅处理NameError类型的异常
    print(f"处理NameError：{e}")  # 输出：name 'name' is not defined
```

#### （2）捕获多种异常
```python
try:
    # 可能触发多种异常的代码
    # print(10 // 0)  # 触发ZeroDivisionError
    # print(name)     # 触发NameError
    open("1.txt", "r")  # 触发FileNotFoundError
except (ZeroDivisionError, NameError, FileNotFoundError) as e:
    # 处理多种指定异常
    print(f"发生已知异常：{e}")
```

#### （3）通用异常捕获（捕获所有异常）
```python
try:
    # 任何可能出错的代码
    list_data = [1, 2, 3]
    print(list_data[10])  # 触发IndexError（列表索引越界）
except Exception as e:
    # 处理所有异常（通用方案）
    print(f"程序出错：{e}")  # 输出：list index out of range
```


### 3. 拓展问题
- 为什么要精准捕获异常？  
  不同异常的处理方式可能不同（如文件不存在可能需要创建文件，而除零异常需要提示输入合法数字）
- 异常捕获的顺序？  
  应先捕获具体异常，再捕获通用异常（子类异常在前，父类异常在后）


## 四、完整的异常处理格式（try-except-else-finally）

### 1. 基础结构
```python
try:
    可能出问题的代码
except 异常类型 as e:
    异常发生时的处理
else:
    # 仅当try中无异常时执行
    无异常时的逻辑
finally:
    # 无论是否有异常，必定执行
    释放资源等收尾操作
```


### 2. 各部分作用
| 关键字 | 作用 |
|-------|------|
| `try` | 包裹可能出现异常的代码 |
| `except` | 处理异常（可多个，处理不同类型） |
| `else` | 无异常时执行（可选） |
| `finally` | 必定执行（常用于关闭文件、释放连接等） |


### 3. 经典用法
#### （1）基础演示
```python
try:
    print("执行try中的代码")
    result = 10 // 2  # 无异常
    print("try执行完毕")
except Exception as e:
    print(f"异常处理：{e}")
else:
    print(f"else执行：计算结果是{result}")  # 仅无异常时执行
finally:
    print("finally执行：无论有无异常都走这里")  # 必定执行
```

#### （2）文件操作案例（释放资源）
```python
# 拷贝文件并处理异常
try:
    # 打开源文件和目标文件
    src_file = open("source.txt", "rb")
    dest_file = open("dest.txt", "wb")
except Exception as e:
    print(f"文件打开失败：{e}")
else:
    # 无异常时执行拷贝
    while True:
        data = src_file.read(1024)  # 每次读1024字节
        if not data:  # 读取完毕
            break
        dest_file.write(data)
    print("文件拷贝成功")
finally:
    # 确保文件关闭（释放资源）
    try:
        src_file.close()
    except:
        pass  # 若文件未打开，关闭会报错，直接忽略
    try:
        dest_file.close()
    except:
        pass
```

#### （3）结合with语句（自动释放资源）
```python
# with语句会自动关闭文件，简化finally操作
try:
    with open("source.txt", "rb") as src_file, open("dest.txt", "wb") as dest_file:
        while True:
            data = src_file.read(1024)
            if not data:
                break
            dest_file.write(data)
    print("文件拷贝成功")
except Exception as e:
    print(f"拷贝失败：{e}")
```


### 4. 拓展问题
- `else`的意义？  
  区分“正常执行逻辑”和“异常处理逻辑”，使代码更清晰（避免把正常逻辑写在try中）
- `finally`必须用吗？  
  当需要释放资源（如文件、网络连接、数据库连接）时，必须用finally确保资源释放


## 五、异常的传递性

### 1. 基础概念
- 函数内部的异常会传递给调用者，逐级向上传递
- 若传递到程序入口（`main`）仍未处理，则程序报错终止
- 若在传递过程中被某个`try-except`捕获，则停止传递并执行处理逻辑


### 2. 经典用法
```python
# 演示异常的传递路径
def func1():
    print("----- func1 开始 -----")
    print(10 // 0)  # 触发除零异常
    print("----- func1 结束 -----")  # 不会执行

def func2():
    print("----- func2 开始 -----")
    func1()  # 调用func1，会接收其传递的异常
    print("----- func2 结束 -----")  # 若异常未处理，不会执行

def func3():
    print("----- func3 开始 -----")
    func2()  # 接收func2传递的异常
    print("----- func3 结束 -----")  # 若异常未处理，不会执行

if __name__ == "__main__":
    try:
        func3()  # 接收func3传递的异常
    except ZeroDivisionError:
        print("在main中捕获到异常：除数不能为0")
    print("程序继续执行")
```

**执行流程**：  
`func1`产生异常 → 传递给`func2` → 传递给`func3` → 传递给`main` → 被`main`的`try-except`捕获处理


### 3. 拓展问题
- 异常传递的意义？  
  允许在合适的层级处理异常（如在顶层统一处理日志，底层只负责产生业务逻辑）
- 如何中断异常传递？  
  在任意层级用`try-except`捕获异常即可中断传递


## 总结
异常处理是保证程序健壮性的核心机制，关键知识点：
1. 异常是运行时错误，默认会终止程序
2. `try-except`是基础捕获结构，可拦截异常并继续执行
3. 用`Exception`或具体异常类型实现精准处理
4. `else`和`finally`分别处理“无异常逻辑”和“必执行逻辑”
5. 异常具有传递性，可在合适层级统一处理

通过合理使用异常处理，能让程序在遇到错误时更友好地提示用户，而非直接崩溃。
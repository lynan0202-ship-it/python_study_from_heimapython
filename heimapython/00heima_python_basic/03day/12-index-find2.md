在Python中，字符串的 `index()` 和 `find()` 方法都是用于**查找子字符串在原字符串中的起始位置（索引）**，但两者在处理“子字符串不存在”的情况时行为不同。以下是详细说明：


### 一、共同功能
- 作用：查找子字符串 `sub` 在原字符串 `str` 中**第一次出现的起始索引**（索引从0开始）。
- 语法（参数相同）：
  ```python
  str.index(sub, [start], [end])
  str.find(sub, [start], [end])
  ```
  - `sub`：必需，要查找的子字符串。
  - `start`：可选，查找的起始位置（默认从0开始）。
  - `end`：可选，查找的结束位置（不包含此位置，默认到字符串末尾）。


### 二、核心区别（关键！）
当**子字符串 `sub` 不存在于原字符串中时**：
- `index()` 会**抛出 `ValueError` 异常**（程序会报错中断）。
- `find()` 会**返回 `-1`**（不报错，通过返回值告知“未找到”）。


### 三、用法示例
以字符串 `s = "hello world, hello python"` 为例演示：


#### 1. 基本用法（无start/end参数）
```python
s = "hello world, hello python"

# 查找子字符串"hello"的位置
print(s.index("hello"))  # 输出：0（第一个"hello"在索引0处）
print(s.find("hello"))   # 输出：0（同上）

# 查找子字符串"python"的位置
print(s.index("python"))  # 输出：18（"python"从索引18开始）
print(s.find("python"))   # 输出：18（同上）
```


#### 2. 带start/end参数（限制查找范围）
```python
s = "hello world, hello python"

# 从索引10开始查找"hello"（跳过第一个"hello"）
print(s.index("hello", 10))  # 输出：13（第二个"hello"从索引13开始）
print(s.find("hello", 10))   # 输出：13（同上）

# 在索引0-10范围内查找"python"（此范围不含"python"）
print(s.find("python", 0, 10))  # 输出：-1（未找到）
# print(s.index("python", 0, 10))  # 会抛出 ValueError: substring not found
```


#### 3. 子字符串不存在的情况
```python
s = "hello world"

# 查找不存在的子字符串"java"
print(s.find("java"))  # 输出：-1（不报错）
# print(s.index("java"))  # 抛出异常：ValueError: substring not found
```


### 四、使用场景选择
- 若**确定子字符串一定存在**（如处理固定格式的字符串），用 `index()` 更直接。
- 若**不确定子字符串是否存在**（如用户输入校验），用 `find()` 更安全（通过返回 `-1` 判断，避免程序报错）。


总结：两者功能相似，核心区别在于“子字符串不存在时的行为”，根据是否需要捕获异常选择即可。
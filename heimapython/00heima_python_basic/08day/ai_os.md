# 🐍 Python os模块大揭秘：你的文件管理小助手


## 🌟 先聊聊：os模块是个啥？

你有没有想过，用Python代码操控电脑里的文件夹、文件？比如新建个文件夹、改个文件名、看看当前在哪个目录……这些活儿，`os`模块全包了！

`os`全称是Operating System（操作系统），它是Python自带的**标准库**（划重点：不是第三方包，不用额外安装，直接导入就能用），专门负责和操作系统打交道，处理文件、文件夹、路径这些琐事，简直是你的“电脑管家”～


## 🚀 常用函数实战：上手就会用


### 1. `os.getcwd()`：我现在在哪？

**功能**：告诉你当前的“工作目录”——也就是你写代码时，相对路径参考的那个文件夹（相当于你现在“站”在哪个文件夹里）。

**用法示例**：
```python
import os

# 打印当前工作目录
current_dir = os.getcwd()
print("我现在在：", current_dir)  # 比如输出：C:\Users\你的名字\Desktop
```

**小提示**：如果你的代码里用了相对路径（比如`open("test.txt")`），Python就会默认去`getcwd()`返回的目录里找这个文件哦～


### 2. `os.chdir()`：换个地方“站站”

**功能**：改变当前工作目录（相当于“cd”命令，换个文件夹待着）。

**用法示例**：
```python
import os

# 先看看现在在哪
print("之前的目录：", os.getcwd())  # 比如：C:\Users\你

# 切换到D盘根目录（Windows）或"/home"（Linux/Mac）
os.chdir("d:/")  # Windows写法
# os.chdir("/home")  # Linux/Mac写法

# 再看看现在在哪
print("切换后的目录：", os.getcwd())  # 输出：d:\
```

**小提示**：切换目录后，后续的相对路径都会以新目录为参考，别“迷路”啦～


### 3. `os.mkdir()`：新建一个文件夹

**功能**：创建一个空文件夹（相当于右键“新建文件夹”）。

**用法示例**：
```python
import os

# 在当前目录下新建一个叫"my_notes"的文件夹
os.mkdir("my_notes")
print("文件夹创建成功！")
```

**注意**：
- 如果文件夹已经存在，会直接报错（比如`FileExistsError`）
- 只能创建单级文件夹，比如`os.mkdir("a/b")`会报错（因为a文件夹可能不存在）


### 4. `os.rmdir()`：删除空文件夹

**功能**：删除一个空文件夹（必须是空的！有文件的话删不了）。

**用法示例**：
```python
import os

# 删除刚才创建的"my_notes"文件夹（确保它是空的）
os.rmdir("my_notes")
print("空文件夹删除成功！")
```

**注意**：
- 文件夹里有文件/子文件夹？删不了！会报错`OSError`
- 删之前一定要确认：别误删重要文件！


### 5. `os.rename()`：给文件/文件夹改个名

**功能**：给文件或文件夹重命名（还能顺便移动位置哦～）。

**用法示例**：
```python
import os

# 1. 给文件夹改名：把"old_dir"改成"new_dir"
os.rename("old_dir", "new_dir")

# 2. 给文件改名：把"test.txt"改成"my_test.txt"
os.rename("test.txt", "my_test.txt")

# 3. 顺便移动位置：把"a.txt"移到"docs"文件夹里，并重命名为"b.txt"
os.rename("a.txt", "docs/b.txt")  # 前提是docs文件夹存在
```

**注意**：如果目标位置已有同名文件/文件夹，会直接覆盖（Windows可能提示错误，Linux/Mac会直接覆盖），小心操作！


### 6. `os.listdir()`：看看文件夹里有啥

**功能**：获取指定目录下所有的“直接子级”（文件或文件夹），但不会深入子文件夹里面看。

**用法示例**：
```python
import os

# 查看当前目录下的所有子级
current_children = os.listdir("./")  # "./"表示当前目录
print("当前目录里的东西：", current_children)

# 查看D盘根目录下的所有子级（Windows）
d_children = os.listdir("d:/")
print("D盘里的东西：", d_children)
```

**输出样例**：
```
当前目录里的东西： ['笔记.txt', '图片文件夹', 'code.py']
D盘里的东西： ['软件', '电影', '工作资料']
```


## 📚 拓展知识点：这些技能更实用！


### 1. `os.path`子模块：路径处理小能手

`os`模块里还有个“小弟”`os.path`，专门处理路径相关的问题，超常用！

| 函数 | 功能 | 示例 |
|------|------|------|
| `os.path.exists(path)` | 判断路径（文件/文件夹）是否存在 | `os.path.exists("test.txt")` → True/False |
| `os.path.isfile(path)` | 判断是不是文件 | `os.path.isfile("a.txt")` → True（如果是文件） |
| `os.path.isdir(path)` | 判断是不是文件夹 | `os.path.isdir("docs")` → True（如果是文件夹） |
| `os.path.getsize(path)` | 获取文件大小（单位：字节） | `os.path.getsize("bigfile.zip")` → 102400（表示100KB） |
| `os.path.join(a, b)` | 拼接路径（自动处理斜杠） | `os.path.join("d:/", "docs", "note.txt")` → "d:/docs/note.txt" |

**示例**：检查文件是否存在，再决定是否读取
```python
import os

file_path = "data.txt"

if os.path.exists(file_path) and os.path.isfile(file_path):
    print("文件存在，大小是：", os.path.getsize(file_path), "字节")
    with open(file_path, "r") as f:
        print(f.read())
else:
    print("文件不存在哦～")
```


### 2. `os.makedirs()`：批量创建多级文件夹

`os.mkdir()`只能创建单级文件夹，要是想一次性创建“a/b/c”这样的多级目录，用`os.makedirs()`：

```python
import os

# 一次性创建a文件夹，以及a里的b，b里的c
os.makedirs("a/b/c", exist_ok=True)  # exist_ok=True：如果已存在，不报错
```

`exist_ok=True`是个好参数，避免重复创建时报错～


### 3. `os.walk()`：遍历目录里的所有内容

想把一个文件夹里的所有文件（包括子文件夹里的）都找出来？用`os.walk()`！它会返回一个生成器，每次迭代返回三个值：当前目录路径、当前目录下的子文件夹、当前目录下的文件。

**示例**：遍历“docs”文件夹里的所有文件
```python
import os

for root, dirs, files in os.walk("docs"):
    print("当前目录：", root)
    print("子文件夹：", dirs)
    print("文件：", files)
    print("---")
```

输出会一层层列出所有内容，超适合批量处理文件！


### 4. 处理非空文件夹：`shutil`模块来帮忙

`os.rmdir()`删不了非空文件夹？别慌，Python还有个`shutil`模块（也是标准库），专门处理文件复制、删除等操作：

```python
import shutil

# 删除非空文件夹（慎用！会直接删光所有内容）
shutil.rmtree("non_empty_dir")  # 连文件夹带里面的东西全删了

# 复制文件
shutil.copy("source.txt", "dest.txt")  # 复制source.txt到dest.txt

# 复制文件夹（包括里面所有内容）
shutil.copytree("old_dir", "new_dir")  # 把old_dir复制一份叫new_dir
```

**警告**：`shutil.rmtree()`删除不可逆，删之前一定要再三确认！


## 💡 小总结

`os`模块是Python操作文件和文件夹的“利器”，记住这些核心技能：
- 查目录、换目录：`getcwd()`、`chdir()`
- 建文件夹、删空文件夹：`mkdir()`、`rmdir()`
- 改名/移动：`rename()`
- 列内容：`listdir()`
- 拓展技能：`os.path`处理路径、`os.walk()`遍历目录、`shutil`处理复杂操作

多动手试试，你会发现用代码管理文件比手动点鼠标高效100倍！😎
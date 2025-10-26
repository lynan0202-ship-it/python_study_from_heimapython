下面我用一个「学生管理系统」的完整案例，把包的所有知识点串起来！包含具体文件夹结构、每个文件的代码内容，以及运行效果，跟着做就能完全掌握～


## 📋 项目整体结构
先看这个项目的「家谱图」，咱们一步步实现每个文件：
```
student_management/  # 项目根目录
├─ student_manager/  # 主包（核心功能）
│  ├─ __init__.py    # 主包的初始化文件
│  ├─ core.py        # 核心模块（计算平均分等）
│  ├─ data/          # 子包（处理学生数据）
│  │  ├─ __init__.py  # 子包初始化文件
│  │  └─ students.py  # 学生数据增删改查
│  └─ ui/            # 子包（处理界面显示）
│     ├─ __init__.py  # 子包初始化文件
│     └─ display.py   # 打印学生信息
├─ main.py           # 主程序（调用包的功能）
└─ setup.py          # 打包配置文件（用于分享）
```


## 🔨 逐个实现文件内容
按顺序创建文件，代码可以直接复制运行～


### 1. 主包 `student_manager` 及核心模块
#### ① `student_manager/core.py`（核心逻辑）
```python
# 核心功能：计算学生平均分、判断是否及格
def calculate_average(scores):
    """计算分数列表的平均分"""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def is_passed(score):
    """判断单个分数是否及格（60分及以上）"""
    return score >= 60
```

#### ② `student_manager/__init__.py`（主包初始化）
这里展示`__all__`（控制批量导入）和「简化导入路径」的技巧：
```python
# 1. 控制 from student_manager import * 能导入的模块
__all__ = ["core", "data", "ui"]  # 只允许导入这3个（core模块、data子包、ui子包）

# 2. 简化导入：把常用功能提到包级别，用户不用写多级路径
from .core import calculate_average  # 直接用 student_manager.calculate_average()
from .data import students  # 直接用 student_manager.students.xxx()
from .ui import display  # 直接用 student_manager.display.xxx()
```


### 2. 子包 `data`（处理学生数据）
#### ① `student_manager/data/students.py`（数据操作）
```python
# 学生数据存储和操作
students_db = [
    {"id": 1, "name": "小明", "scores": [85, 92, 78]},
    {"id": 2, "name": "小红", "scores": [60, 75, 88]}
]

def add_student(name, scores):
    """新增学生（自动生成ID）"""
    new_id = len(students_db) + 1
    students_db.append({"id": new_id, "name": name, "scores": scores})
    return new_id

def get_student_by_id(student_id):
    """根据ID查询学生"""
    for student in students_db:
        if student["id"] == student_id:
            return student
    return None
```

#### ② `student_manager/data/__init__.py`（子包初始化）
```python
# 控制 from student_manager.data import * 能导入的模块
__all__ = ["students"]  # 只允许导入students模块

# 子包内简化导入（比如其他模块想调用students.py时更方便）
from . import students
```


### 3. 子包 `ui`（处理界面显示）
#### ① `student_manager/ui/display.py`（显示功能）
这里用「相对导入」调用主包的`core.py`功能：
```python
# 显示学生信息（调用主包的core模块计算平均分）
# 相对导入：.. 代表父包（student_manager），从父包导入core模块
from ..core import calculate_average, is_passed

def show_student_detail(student):
    """显示单个学生的详细信息（带平均分和及格情况）"""
    if not student:
        print("❌ 未找到该学生")
        return
    avg = calculate_average(student["scores"])
    passed_status = "✅ 全部及格" if all(is_passed(s) for s in student["scores"]) else "❌ 有不及格科目"
    print(f"\n📌 学生ID：{student['id']}")
    print(f"姓名：{student['name']}")
    print(f"分数：{student['scores']}")
    print(f"平均分：{avg:.1f}")
    print(passed_status)

def show_all_students(students_list):
    """显示所有学生的简略信息"""
    print("\n📋 所有学生列表：")
    for s in students_list:
        print(f"ID: {s['id']} | 姓名: {s['name']} | 分数: {s['scores']}")
```

#### ② `student_manager/ui/__init__.py`（子包初始化）
```python
# 控制 from student_manager.ui import * 能导入的模块
__all__ = ["display"]

# 子包内简化导入
from . import display
```


### 4. 主程序 `main.py`（调用所有功能）
这里展示三种导入方式的实际应用：
```python
# 方式1：import 包.模块（完整路径）
import student_manager.data.students as s_data  # 起别名简化

# 方式2：from 包 import 模块/子包
from student_manager.ui import display  # 从ui子包导入display模块
from student_manager import core  # 从主包导入core模块（因为__init__.py简化过）

# 方式3：from 包.模块 import 函数（直接用函数）
from student_manager.core import is_passed


def main():
    # 1. 新增一个学生（用方式1的导入）
    new_id = s_data.add_student("小刚", [55, 70, 90])
    print(f"✨ 新增学生成功，ID：{new_id}")

    # 2. 显示所有学生（用方式2的display模块）
    display.show_all_students(s_data.students_db)

    # 3. 查看单个学生详情（用方式2的core模块计算平均分）
    student = s_data.get_student_by_id(1)
    display.show_student_detail(student)

    # 4. 用方式3导入的函数判断分数
    score = 58
    print(f"\n💡 分数{score}是否及格？{is_passed(score)}")

    # 5. 测试批量导入（from 包 import *）
    from student_manager import *  # 受__init__.py的__all__限制，只能导入core、data、ui
    print(f"\n📊 小明的平均分：{calculate_average(s_data.students_db[0]['scores']):.1f}")


if __name__ == "__main__":
    main()
```


### 5. 打包配置 `setup.py`（用于分享）
```python
from setuptools import setup, find_packages

setup(
    name="student_manager",  # 包名（pip安装后用这个名导入）
    version="1.0.0",
    packages=find_packages(),  # 自动包含所有包
    author="你的名字",
    description="学生管理系统工具包（包含数据处理、成绩计算、界面显示）",
    python_requires=">=3.6",  # 支持的Python版本
)
```


## 🚀 运行效果与操作步骤
### 1. 运行主程序
在`student_management`目录下打开命令行，执行：
```bash
python main.py
```
输出结果：
```
✨ 新增学生成功，ID：3

📋 所有学生列表：
ID: 1 | 姓名: 小明 | 分数: [85, 92, 78]
ID: 2 | 姓名: 小红 | 分数: [60, 75, 88]
ID: 3 | 姓名: 小刚 | 分数: [55, 70, 90]

📌 学生ID：1
姓名：小明
分数：[85, 92, 78]
平均分：85.0
✅ 全部及格

💡 分数58是否及格？False

📊 小明的平均分：85.0
```


### 2. 测试批量导入限制
修改`main.py`，尝试导入`__all__`外的内容（其实没有，这里只是演示限制效果）：
```python
from student_manager import *
# 因为__all__里没有"xxx"（假设不存在的模块），所以下面这行会报错
xxx.xxx()  # 报错：NameError: name 'xxx' is not defined
```


### 3. 打包并安装自己的包
#### ① 生成安装包
在`student_management`目录下执行：
```bash
python setup.py sdist
```
会生成`dist/student_manager-1.0.0.tar.gz`文件。

#### ② 安装到本地
```bash
pip install dist/student_manager-1.0.0.tar.gz
```

#### ③ 在其他项目中使用
新建一个`test.py`，不用关心原来的文件夹结构，直接导入：
```python
from student_manager import calculate_average
from student_manager.data.students import students_db

print(calculate_average([90, 80, 70]))  # 输出80.0
print(students_db[0]["name"])  # 输出小明
```


### 4. 用虚拟环境隔离包（避冲突）
```bash
# 1. 创建虚拟环境
python -m venv venv

# 2. 激活虚拟环境（Windows用这个）
venv\Scripts\activate

# 3. 在虚拟环境中安装自己的包
pip install dist/student_manager-1.0.0.tar.gz

# 4. 退出虚拟环境
deactivate
```


## 🚫 避坑演示：循环导入问题
如果`core.py`和`data/students.py`互相导入，会报错：
```python
# 错误示例：core.py
from .data.students import students_db  # 导入data的内容

# 错误示例：data/students.py
from ..core import calculate_average  # 又导入core的内容
```
运行会报错`ImportError`。

**解决方法**：把导入放到函数内部（延迟导入）：
```python
# 修复后：core.py
def calculate_average(scores):
    from .data.students import students_db  # 函数内才导入，避免循环
    # 其他逻辑...
```


通过这个案例，你已经掌握了包的所有核心用法：文件夹结构、`__init__.py`的作用、三种导入方式、子包嵌套、相对导入、打包分享、虚拟环境和避坑技巧！可以直接基于这个框架扩展更多功能～
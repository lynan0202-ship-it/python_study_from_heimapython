# Python模块、包与综合案例详解


## 一、模块（Module）详解

### 1. 模块基础概念
- **定义**：1个`.py`文件就是1个模块，模块中可包含函数、类、变量等（相当于“工具包”）
- **作用**：实现代码复用（写一次可在多个程序中调用）、便于代码管理（按功能拆分文件）


### 2. 模块导入的5种方式

#### （1）方式1：`import 模块名`
- **基础结构**：
  ```python
  import 模块名  # 导入整个模块
  模块名.函数名()  # 调用模块中的函数
  ```
- **经典用法**（以`time`模块为例）：
  ```python
  # 导入时间模块
  import time
  
  print("程序开始")
  time.sleep(2)  # 调用模块中的sleep函数（休眠2秒）
  print("程序结束")  # 2秒后才会执行
  ```
- **特点**：导入模块中所有内容，需通过`模块名.函数名`调用，避免命名冲突


#### （2）方式2：`import 模块名 as 别名`
- **基础结构**：
  ```python
  import 模块名 as 别名  # 给模块起别名
  别名.函数名()  # 通过别名调用
  ```
- **经典用法**：
  ```python
  # 给time模块起别名t（简化调用）
  import time as t
  
  print("开始")
  t.sleep(1)  # 用别名调用更简洁
  print(t.localtime())  # 获取本地时间
  ```
- **特点**：解决模块名过长问题，不改变模块功能


#### （3）方式3：`from 模块名 import 函数名`
- **基础结构**：
  ```python
  from 模块名 import 函数1, 函数2  # 只导入指定函数
  函数名()  # 直接调用（无需模块名）
  ```
- **经典用法**：
  ```python
  # 只导入time模块中的sleep和localtime函数
  from time import sleep, localtime
  
  sleep(1)  # 直接调用函数（无需加模块名）
  print(localtime())
  # print(time())  # 报错：未导入的函数不能用
  ```
- **特点**：只导入需要的函数，调用简洁，但可能引发命名冲突（不同模块有同名函数时）


#### （4）方式4：`from 模块名 import 函数名 as 别名`
- **基础结构**：
  ```python
  from 模块名 import 函数名 as 别名  # 给函数起别名
  别名()  # 通过别名调用
  ```
- **经典用法**：
  ```python
  # 给sleep函数起别名sl，避免与其他同名函数冲突
  from time import sleep as sl, localtime as lt
  
  sl(1)  # 用别名调用
  print(lt())
  ```
- **特点**：解决函数名冲突问题（如两个模块有同名函数时）


#### （5）方式5：`from 模块名 import *`
- **基础结构**：
  ```python
  from 模块名 import *  # 导入模块中所有函数
  函数名()  # 直接调用
  ```
- **经典用法**：
  ```python
  # 导入time模块中所有函数
  from time import *
  
  sleep(1)  # 直接调用
  print(time())  # 可调用模块中所有函数
  ```
- **特点**：导入所有函数，调用简洁，但可能导致命名冲突（不推荐大型项目使用）


### 3. 自定义模块核心知识点

#### （1）`__name__`属性
- **作用**：区分模块是“自身运行”还是“被导入运行”
- **规则**：
  - 模块自身运行时，`__name__ == "__main__"`
  - 模块被导入时，`__name__ == 模块名`
- **经典用法**（模块内测试代码）：
  ```python
  # 自定义模块 my_module.py
  def add(a, b):
      return a + b
  
  # 测试代码（仅在模块自身运行时执行）
  if __name__ == "__main__":
      print(add(10, 20))  # 模块自己运行时会执行
  ```
  当其他程序导入该模块时，测试代码不会执行。


#### （2）`__all__`属性
- **作用**：限制`from 模块名 import *`导入的内容（仅对这种导入方式有效）
- **经典用法**：
  ```python
  # 自定义模块 my_module.py
  __all__ = ["fun1", "fun2"]  # 只允许导入fun1和fun2
  
  def fun1():
      print("fun1")
  
  def fun2():
      print("fun2")
  
  def fun3():  # 不会被from my_module import *导入
      print("fun3")
  ```


#### （3）多模块同名函数处理
- 当导入的多个模块有同名函数时，**最后导入的函数会覆盖前面的**
- 解决方式：使用别名或通过模块名调用
  ```python
  from my_module1 import add as add1
  from my_module2 import add as add2
  
  print(add1(1, 2))  # 调用my_module1的add
  print(add2(1, 2))  # 调用my_module2的add
  ```


### 4. 拓展问题
- 模块导入路径：Python会从当前目录、系统目录（如Python安装目录的`site-packages`）查找模块
- 循环导入问题：模块A导入模块B，同时模块B导入模块A，会导致错误（避免这种设计）
- 导入最佳实践：优先使用`import 模块名`或`from 模块名 import 函数`，避免`from 模块名 import *`（减少冲突）


## 二、包（Package）详解

### 1. 包基础概念
- **定义**：包含多个模块（`.py`文件）和1个`__init__.py`文件的文件夹（相当于“工具包的集合”）
- **作用**：当模块数量过多时，通过包对模块进行分类管理（类似文件夹管理文件）


### 2. 包的核心文件：`__init__.py`
- **作用**：标识该文件夹是Python包，可在其中定义包的初始化逻辑
- **`__all__`属性**：限制`from 包名 import *`导入的模块（仅对这种方式有效）
  ```python
  # __init__.py 文件
  __all__ = ["module1", "module2"]  # 只允许导入这两个模块
  ```


### 3. 包的导入方式

#### （1）方式1：`import 包名.模块名`
- **基础结构**：
  ```python
  import 包名.模块名
  包名.模块名.函数名()  # 调用函数
  ```
- **经典用法**：
  ```python
  # 导入my_package包中的my_module1模块
  import my_package.my_module1
  
  # 调用模块中的函数
  my_package.my_module1.fun01()
  ```


#### （2）方式2：`from 包名 import 模块名`
- **基础结构**：
  ```python
  from 包名 import 模块名
  模块名.函数名()  # 调用函数
  ```
- **经典用法**：
  ```python
  # 从my_package包中导入my_module1模块
  from my_package import my_module1
  
  # 直接通过模块名调用
  my_module1.fun01()
  ```


#### （3）方式3：`from 包名.模块名 import 函数名`
- **基础结构**：
  ```python
  from 包名.模块名 import 函数名
  函数名()  # 直接调用
  ```
- **经典用法**：
  ```python
  # 从包的模块中直接导入函数
  from my_package.my_module1 import fun01
  
  fun01()  # 直接调用
  ```


### 4. 拓展问题
- 包的嵌套：包中可以包含子包（子文件夹+`__init__.py`），导入时用`.`分隔（如`import 包.子包.模块`）
- 包的安装：第三方包可通过`pip install 包名`安装（如`pip install requests`），安装后可直接导入使用


## 三、综合案例：学生管理系统

### 1. 需求与整体设计
- **核心功能**：添加、删除、修改、查询学生信息（学号、姓名、手机号）
- **数据存储**：用`列表嵌套字典`存储学生信息（`[{'id': '001', 'name': '张三', 'tel': '123'}, ...]`）
- **程序结构**：通过函数封装各功能，主循环处理用户输入，调用对应函数


### 2. 核心功能详解

#### （1）主界面与入口
```python
# 打印功能菜单
def print_info():
    print("1.添加学生")
    print("2.删除学生")
    print("3.修改学生信息")
    print("4.查询单个学生信息")
    print("5.查询所有学生信息")
    print("6.退出系统")

# 主循环（程序入口）
def student_manager():
    while True:
        print_info()  # 显示菜单
        choice = input("请输入操作编号：")  # 获取用户选择
        # 根据选择调用对应函数
        if choice == "1":
            add_info()
        elif choice == "2":
            delete_info_by_name()
        # ... 其他选项
        elif choice == "6":
            print("退出系统")
            break
        else:
            print("输入错误，请重新输入")

# 启动程序
if __name__ == "__main__":
    student_manager()
```


#### （2）添加学生（确保学号唯一）
```python
# 存储学生信息的列表
user_info = []

def add_info():
    new_id = input("请输入学号：")
    # 检查学号是否已存在
    for stu in user_info:
        if new_id == stu["id"]:
            print(f"学号{new_id}已存在！")
            return  # 退出函数
    # 录入其他信息并添加到列表
    new_name = input("请输入姓名：")
    new_tel = input("请输入手机号：")
    user_info.append({"id": new_id, "name": new_name, "tel": new_tel})
    print("添加成功！")
```


#### （3）删除学生（按姓名删除，支持重复姓名）
```python
def delete_info_by_name():
    del_name = input("请输入要删除的姓名：")
    flag = False  # 标记是否删除成功
    i = 0
    # 遍历列表（用while避免删除元素后索引错位）
    while i < len(user_info):
        if user_info[i]["name"] == del_name:
            user_info.pop(i)  # 删除该学生
            flag = True
            i -= 1  # 索引回退（因为元素减少了1个）
        i += 1
    if flag:
        print(f"姓名为{del_name}的学生已删除")
    else:
        print(f"未找到姓名为{del_name}的学生")
```


#### （4）修改学生信息（按学号修改）
```python
def update_info():
    update_id = input("请输入要修改的学号：")
    for stu in user_info:
        if stu["id"] == update_id:
            # 修改姓名和手机号
            stu["name"] = input("请输入新姓名：")
            stu["tel"] = input("请输入新手机号：")
            print("修改成功！")
            return
    print(f"未找到学号{update_id}的学生")
```


#### （5）查询功能（单个/所有）
```python
# 按姓名查询（支持重复姓名）
def search_info_by_name():
    search_name = input("请输入要查询的姓名：")
    flag = False
    for stu in user_info:
        if stu["name"] == search_name:
            print(f"学号：{stu['id']}，姓名：{stu['name']}，手机号：{stu['tel']}")
            flag = True
    if not flag:
        print(f"未找到姓名为{search_name}的学生")

# 查询所有学生
def search_all():
    if not user_info:  # 列表为空
        print("暂无学生信息")
        return
    for stu in user_info:
        print(f"学号：{stu['id']}，姓名：{stu['name']}，手机号：{stu['tel']}")
```


### 3. 拓展升级思路
- **数据持久化**：将学生信息保存到文件（如`txt`、`json`），程序重启后数据不丢失
- **增加密码验证**：添加管理员登录功能，限制操作权限
- **图形界面**：用`tkinter`或`PyQt`制作可视化界面，更友好
- **数据库存储**：使用`MySQL`等数据库替代列表，支持大量数据管理


## 总结
- **模块**：`.py`文件，通过5种方式导入，实现代码复用
- **包**：含`__init__.py`的文件夹，用于管理多个模块，支持嵌套
- **学生管理系统**：综合运用函数、循环、条件判断、列表字典等知识，实现数据的增删改查

掌握这些知识后，可进一步学习第三方模块（如`requests`、`pandas`）和大型项目的包结构设计。
# 🐬 Python操作MySQL：pymysql入门到CRUD实战


## 🌟 先认识一下：pymysql是个啥？

你想过用Python代码直接操控MySQL数据库吗？比如自动往表里插数据、批量修改记录、查询数据后做分析……这时候就需要`pymysql`出马啦！

`pymysql`是Python操作MySQL数据库的**第三方模块**（非Python自带），它定义了一套API，让我们能用Python代码轻松实现对MySQL的“增删改查”（CRUD）。简单说：有了它，Python和MySQL就能“对话”啦～


## 📦 第一步：安装pymysql

因为是第三方模块，用之前得先“请进门”（安装），两种方式任你选：

### 方式1：命令行pip安装（推荐）
打开CMD或终端，输入下面的命令，速度慢的话加个国内镜像（比如清华大学的，贼快！）：
```bash
# 基础安装
pip install pymysql

# 加镜像加速（国内用户首选）
pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 方式2：IDE里直接安装
如果用PyCharm这类IDE，写代码时先导入`import pymysql`，这时会报错（红色波浪线），把鼠标放上去，按`Alt + Enter`，选择“Install package pymysql”，自动安装搞定～


## 🚀 pymysql操作5步走（附大白话比喻）

用pymysql操作MySQL，就像去餐厅吃饭，步骤超有逻辑！

| 步骤 | 专业说法 | 大白话比喻 | 作用 |
|------|----------|------------|------|
| 1 | 获取连接对象 | 找到餐厅前台小姐姐 | 建立Python和MySQL的连接（相当于你和餐厅搭上了线） |
| 2 | 获取游标对象 | 前台喊来服务员 | 负责执行SQL语句（服务员帮你下单、传菜） |
| 3 | 执行SQL语句 | 告诉服务员需求 | 比如“查一下菜单”“来份宫保鸡丁”（对应查询、插入等操作） |
| 4 | 处理结果集 | 拿到菜/看到菜单 | 对查询结果做处理（比如打印、分析），或确认增删改是否成功 |
| 5 | 释放资源 | 吃完买单走人 | 关闭游标和连接（不占着资源，讲武德） |


### 实操演示：连接数据库并查询数据

先看个完整例子，感受下5步走流程：
```python
import pymysql

# 1. 获取连接对象（和MySQL建立连接）
conn = pymysql.connect(
    host='localhost',  # MySQL所在主机的IP/域名（本地一般是localhost）
    port=3306,         # 端口号（MySQL默认3306）
    user='root',       # 数据库账号（默认root）
    password='123456', # 你的数据库密码（自己设置的哦）
    database='day02',  # 要操作的数据库名（必须先创建好）
    charset='utf8'     # 字符集（utf8支持中文，别写成utf-8！）
)

# 2. 获取游标对象（用来执行SQL）
cur = conn.cursor()

# 3. 执行SQL语句（这里查hero表的所有数据）
sql = 'select * from hero;'  # 要执行的SQL语句
cur.execute(sql)  # 执行SQL，返回受影响的行数（查询时返回总记录数）

# 4. 处理结果集（获取查询到的数据）
# 可选：fetchall()取所有数据 / fetchone()取1条 / fetchmany(n)取n条
data = cur.fetchmany(3)  # 取前3条数据
print("查询到的数据：", data)  # 结果是元组嵌套元组，比如((1, '鸠摩智', 9), ...)

# 5. 释放资源（用完记得关！）
cur.close()  # 先关游标
conn.close() # 再关连接
```

**注意**：运行前要确保MySQL服务已启动（比如用小皮面板、命令行启动），否则连接会失败哦！


## 🔍 CRUD实战：增删改查一个都不能少

CRUD是数据库操作的四大天王：Create（增）、Read（查）、Update（改）、Delete（删）。咱们一个个来搞定～


### 1. Create（增）：往表里插数据

**核心点**：插入数据后必须用`conn.commit()`提交，否则数据不会保存到数据库！

```python
import pymysql

def add_hero():
    # 1. 建立连接
    conn = pymysql.connect(
        host='localhost', port=3306, user='root', 
        password='123456', database='day02', charset='utf8'
    )
    # 2. 获取游标
    cur = conn.cursor()
    
    try:
        # 3. 执行插入SQL
        sql = 'insert into hero values(6, "杨过", 20);'  # 假设hero表有hid, hname, kongfu_id字段
        row_count = cur.execute(sql)  # row_count是受影响的行数（成功插入1条就返回1）
        
        # 关键：增删改必须commit提交！
        conn.commit()
        
        # 4. 处理结果
        if row_count > 0:
            print("插入成功！新增了", row_count, "条数据")
    except Exception as e:
        # 出错就回滚（撤销操作）
        conn.rollback()
        print("插入失败：", e)
    finally:
        # 5. 释放资源（放finally里确保一定执行）
        cur.close()
        conn.close()

# 调用函数试试
add_hero()
```


### 2. Read（查）：从表里查数据

查询不用commit，直接获取结果就行，常用3种取数据方式：

```python
import pymysql

def query_hero():
    conn = pymysql.connect(
        host='localhost', port=3306, user='root', 
        password='123456', database='day02', charset='utf8'
    )
    cur = conn.cursor()
    
    try:
        sql = 'select * from hero;'
        cur.execute(sql)  # 执行查询
        
        # 方式1：取所有数据（元组嵌套元组）
        all_data = cur.fetchall()
        print("所有数据：", all_data)
        
        # 方式2：取1条数据（指针会移动，再取就是下一条）
        one_data = cur.fetchone()
        print("第1条数据：", one_data)
        
        # 方式3：取指定条数（比如2条）
        many_data = cur.fetchmany(2)
        print("接下来2条数据：", many_data)
    except Exception as e:
        print("查询失败：", e)
    finally:
        cur.close()
        conn.close()

query_hero()
```


### 3. Update（改）：修改表里的数据

和插入一样，修改后必须commit才生效～

```python
import pymysql

def update_hero():
    conn = pymysql.connect(
        host='localhost', port=3306, user='root', 
        password='123456', database='day02', charset='utf8'
    )
    cur = conn.cursor()
    
    try:
        # 修改hid=6的英雄名字和功夫ID
        sql = 'update hero set hname="神雕侠", kongfu_id=100 where hid=6;'
        row_count = cur.execute(sql)
        
        conn.commit()  # 提交修改
        print("修改成功！影响了", row_count, "条数据")
    except Exception as e:
        conn.rollback()  # 出错回滚
        print("修改失败：", e)
    finally:
        cur.close()
        conn.close()

update_hero()
```


### 4. Delete（删）：删除表里的数据

删除有风险，操作需谨慎！同样需要commit～

```python
import pymysql

def delete_hero():
    conn = pymysql.connect(
        host='localhost', port=3306, user='root', 
        password='123456', database='day02', charset='utf8'
    )
    cur = conn.cursor()
    
    try:
        # 删除hid大于3的英雄（按需修改条件！）
        sql = 'delete from hero where hid > 3;'
        row_count = cur.execute(sql)
        
        conn.commit()  # 提交删除
        print("删除成功！删掉了", row_count, "条数据")
    except Exception as e:
        conn.rollback()  # 出错回滚
        print("删除失败：", e)
    finally:
        cur.close()
        conn.close()

delete_hero()
```


## 📚 拓展知识点：这些坑别踩！

### 1. 防SQL注入：用参数化查询

直接拼接SQL字符串超危险！比如下面的代码，坏人可能输入`' or '1'='1`让你的查询条件失效：
```python
# 危险！不要这么写！
name = input("请输入英雄名：")
sql = f"select * from hero where hname='{name}'"  # 拼接字符串有注入风险
```

**正确做法**：用`%s`当占位符，传参数给`execute`：
```python
name = input("请输入英雄名：")
sql = "select * from hero where hname=%s"  # %s是占位符（不用加引号）
cur.execute(sql, [name])  # 第二个参数是参数列表，自动处理引号和特殊字符
```


### 2. 游标类型：返回字典更方便

默认游标返回的是元组（比如`(1, '杨过', 20)`），不知道哪个值对应哪个字段？可以用`DictCursor`，返回字典（键是字段名）：
```python
# 获取游标时指定类型
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 查询结果是字典列表，比如：
# [{'hid': 1, 'hname': '鸠摩智', 'kongfu_id': 9}, ...]
data = cur.fetchall()
print(data[0]['hname'])  # 直接用字段名取数据，超方便！
```


### 3. 异常处理：让程序更健壮

数据库操作可能出各种错（比如密码错、表不存在），用`try-except-finally`捕获异常，确保资源释放：
```python
try:
    # 连接、执行SQL等操作
    ...
except pymysql.MySQLError as e:  # 捕获MySQL相关错误
    print("数据库错误：", e)
    conn.rollback()  # 出错回滚
finally:
    # 不管成功失败，都关闭资源
    if cur:  # 判断游标是否存在
        cur.close()
    if conn:  # 判断连接是否存在
        conn.close()
```


## 💡 总结一下

用pymysql操作MySQL，记住这几个关键点：
1. 安装：`pip install pymysql`（加镜像更快）
2. 流程：连接→游标→执行SQL→处理结果→释放资源
3. 增删改：必须`conn.commit()`，出错用`rollback()`回滚
4. 查询：用`fetchall()`/`fetchone()`/`fetchmany()`取数据
5. 安全：用参数化查询（`%s`占位符）防SQL注入
6. 方便：用`DictCursor`返回字典格式结果

多动手写几个例子，你会发现用Python操作数据库比手动敲SQL爽多啦！😎
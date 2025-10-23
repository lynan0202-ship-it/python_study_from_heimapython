import os

# 创建示例目录和文件路径
base_path = r'D:\data\PythonProject'
file_path = os.path.join(base_path, 'example.txt')
'''
这里，我们定义了一个基础路径base_path，它是一个原始字符串（字符串前面的r表示原始字符串，这样反斜杠就不会被当作转义字符）。然后，我们使用os.path.join
将基础路径和文件名组合起来，形成完整的文件路径。这样做的好处是，代码在不同的操作系统上都能正确工作，因为os.path.join会自动使用适合当前操作系统的路径分隔符。
'''
# 确保目录存在
os.makedirs(base_path, exist_ok=True)

print("=" * 60)
print("Python文件读写操作完整指南")
print("=" * 60)

# 1. 文件写入操作
print("\n1. 文件写入操作:")
print("-" * 30)

# 1.1 覆盖写入（'w'模式）
with open(file_path, 'w', encoding='utf-8') as file:
    file.write("这是第一行内容\n")
    file.write("这是第二行内容\n")
    file.writelines(["第三行：Python文件操作\n", "第四行：简单易学\n"])
print("● 覆盖写入完成")

# 2.1 读取整个文件
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print("● read() - 读取全部内容:")
    print(content[:100] + "..." if len(content) > 100 else content)


# 1.2 追加写入（'a'模式）
with open(file_path, 'a', encoding='utf-8') as file:
    file.write("第五行：这是追加的内容\n")
print("● 追加写入完成")

# 2.1 读取整个文件
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print("● read() - 读取全部内容:")
    print(content[:100] + "..." if len(content) > 100 else content)

# 1.3 带格式化的写入
data = ["苹果", "香蕉", "橙子"]
with open(file_path, 'a', encoding='utf-8') as file:
    file.write("\n水果列表:\n")
    for item in data:
        file.write(f"- {item}\n")
print("● 格式化写入完成")

# 2.1 读取整个文件
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print("● read() - 读取全部内容:")
    print(content[:100] + "..." if len(content) > 100 else content)

# 2. 文件读取操作
print("\n2. 文件读取操作:")
print("-" * 30)

# 2.1 读取整个文件
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print("● read() - 读取全部内容:")
    print(content[:100] + "..." if len(content) > 100 else content)

# 2.2 逐行读取
print("\n● readline() - 逐行读取:")
with open(file_path, 'r', encoding='utf-8') as file:
    first_line = file.readline().strip()
    second_line = file.readline().strip()
    print(f"第一行: {first_line}")
    print(f"第二行: {second_line}")

# 2.3 读取所有行到列表
print("\n● readlines() - 所有行到列表:")
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(f"总行数: {len(lines)}")
    for i, line in enumerate(lines[:3], 1):  # 只显示前3行
        print(f"  行{i}: {line.strip()}")

# 2.4 遍历文件对象（推荐用于大文件）
print("\n● 遍历文件对象 - 内存友好:")
with open(file_path, 'r', encoding='utf-8') as file:
    for line_num, line in enumerate(file, 1):
        if line_num <= 3:  # 只显示前3行
            print(f"  行{line_num}: {line.strip()}")

# 3. 读写模式详解
print("\n3. 文件模式详解:")
print("-" * 30)
modes_info = {
    'r': '只读模式（文件必须存在）',
    'w': '写入模式（覆盖，文件不存在则创建）',
    'a': '追加模式（文件不存在则创建）',
    'r+': '读写模式（文件必须存在）',
    'w+': '读写模式（覆盖，文件不存在则创建）',
    'a+': '读写模式（追加，文件不存在则创建）',
    'rb': '二进制读取模式',
    'wb': '二进制写入模式'
}

for mode, desc in modes_info.items():
    print(f"  '{mode}': {desc}")

# 4. 读写混合操作
print("\n4. 读写混合操作:")
print("-" * 30)

# 4.1 r+ 模式：读取并修改
with open(file_path, 'r+', encoding='utf-8') as file:
    content = file.read()
    # 移动到文件开头进行写入
    file.seek(0)
    file.write("=== 文件开头添加的内容 ===\n" + content)
print("● r+模式：读取并修改完成")

# 4.2 a+ 模式：读取并追加
with open(file_path, 'a+', encoding='utf-8') as file:
    file.write("=== 文件末尾添加的内容 ===\n")
    # 移动到开头读取
    file.seek(0)
    first_line = file.readline()
    print(f"● a+模式：第一行内容: {first_line.strip()}")

# 5. 二进制文件操作
print("\n5. 二进制文件操作:")
print("-" * 30)

# 写入二进制数据
binary_file = os.path.join(base_path, 'data.bin')
with open(binary_file, 'wb') as file:
    file.write(b'Binary data: \x48\x65\x6c\x6c\x6f')  # Hello的十六进制

# 读取二进制数据
with open(binary_file, 'rb') as file:
    binary_content = file.read()
    print(f"● 二进制内容: {binary_content}")

# 6. 异常处理
print("\n6. 异常处理:")
print("-" * 30)

try:
    with open('nonexistent_file.txt', 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print("● 文件不存在异常已捕获")
except PermissionError:
    print("● 权限错误异常已捕获")
except UnicodeDecodeError:
    print("● 编码错误异常已捕获")
except Exception as e:
    print(f"● 其他异常: {e}")
finally:
    print("● 异常处理演示完成")

# 7. 实用技巧
print("\n7. 实用技巧:")
print("-" * 30)

# 7.1 检查文件是否存在
if os.path.exists(file_path):
    print(f"● 文件存在: {file_path}")

    # 7.2 获取文件大小
    file_size = os.path.getsize(file_path)
    print(f"● 文件大小: {file_size} 字节")

    # 7.3 读取特定行
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) >= 2:
            print(f"● 第二行内容: {lines[1].strip()}")

# 8. 上下文管理器的高级用法
print("\n8. 高级用法 - 同时操作多个文件:")
print("-" * 30)

source_file = os.path.join(base_path, 'example.txt')
backup_file = os.path.join(base_path, 'backup.txt')

try:
    with open(source_file, 'r', encoding='utf-8') as src, \
            open(backup_file, 'w', encoding='utf-8') as dst:
        content = src.read()
        dst.write(f"备份时间戳\n{content}")
    print("● 文件备份完成")
except Exception as e:
    print(f"● 备份失败: {e}")

# 9. 文件编码处理
print("\n9. 编码处理:")
print("-" * 30)

encodings_to_try = ['utf-8', 'gbk', 'latin-1']
for encoding in encodings_to_try:
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            file.read()
        print(f"● {encoding}: 编码兼容")
    except UnicodeDecodeError:
        print(f"● {encoding}: 编码不兼容")

print("\n" + "=" * 60)
print("文件操作总结:")
print("1. 写入模式: 'w'覆盖, 'a'追加")
print("2. 读取方法: read(), readline(), readlines(), 遍历")
print("3. 推荐使用 with 语句自动管理文件")
print("4. 处理中文务必指定 encoding='utf-8'")
print("5. 二进制文件使用 'rb', 'wb' 模式")
print("6. 异常处理确保程序健壮性")
print(f"7. 示例文件位置: {file_path}")
print("=" * 60)

# 清理：删除创建的示例文件（可选）
# os.remove(file_path)
# os.remove(binary_file)
# os.remove(backup_file)
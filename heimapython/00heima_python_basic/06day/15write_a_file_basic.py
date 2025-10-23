import os

# 创建目录和文件路径
base_path = r'D:\data\PythonProject'
file_path = os.path.join(base_path, 'example.txt')
os.makedirs(base_path, exist_ok=True)

print("Python文件操作简明指南")
print("=" * 40)

# 1. 文件写入操作
print("\n1. 文件写入:")
with open(file_path, 'w', encoding='utf-8') as file:
    file.write("第一行内容\n第二行内容\n")

with open(file_path, 'a', encoding='utf-8') as file:
    file.write("第三行：追加的内容\n")

print("● 写入完成")

# 2. 文件读取操作
print("\n2. 文件读取:")

# 读取全部内容
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print("● 全部内容:")
    print(content)

# 逐行读取
print("\n● 逐行读取:")
with open(file_path, 'r', encoding='utf-8') as file:
    for i, line in enumerate(file, 1):
        print(f"行{i}: {line.strip()}")

# 3. 文件模式说明
print("\n3. 常用文件模式:")
modes = {'r': '读取', 'w': '写入(覆盖)', 'a': '追加', 'rb': '二进制读', 'wb': '二进制写'}
for mode, desc in modes.items():
    print(f"  '{mode}': {desc}")

# 4. 异常处理
print("\n4. 异常处理:")
try:
    with open('不存在的文件.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("● 文件不存在错误已处理")

print("\n操作完成!")
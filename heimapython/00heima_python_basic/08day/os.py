# Python os模块综合实战：修复非空目录删除错误版（指定目录操作）
# 修复核心：删除文件夹前先清空内部文件，确保os.rmdir()操作的目录为空
# 工作目录：D:\adate\PythonProject\heimapython\00heima_python_basic\08day

'''
D:\adate\PythonProject\heimapython\00heima_python_basic\08day  # 顶层根目录（TARGET_DIR）
├─ [os_demo_root]  # 原创建的根文件夹
│  └─ [work_folder]  # 由 sub_folder 改名后的文件夹
│     └─ [data]  # 多级创建的子文件夹（存放测试文件）
│        └─ (os_practice.txt)  # 由 initial_note.txt 改名后的测试文件
├─ [os_demo_root_copy]  # 复制 os_demo_root 得到的文件夹（结构与原文件夹完全一致）
│  └─ [work_folder]  # 复制的子文件夹（与原 work_folder 内容相同）
│     └─ [data]  # 复制的 data 子文件夹
│        └─ (os_practice.txt)  # 复制的测试文件（与原文件内容相同）
└─ (os_practice_copy.txt)  # 单独复制到根目录的测试文件副本

'''

import os
import shutil


# 1. 固定工作目录并验证
print("="*50)
TARGET_DIR = "D:/adate/PythonProject/heimapython/00heima_python_basic/08day"
if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR, exist_ok=True)
os.chdir(TARGET_DIR)
current_dir = os.getcwd()
print(f"【步骤1】当前工作目录：{current_dir}")
print(f"【步骤1】目录有效性：{'正常' if os.path.exists(current_dir) else '异常'}")


# 2. 创建多级文件夹（os_demo_root→sub_folder→data）
print("\n" + "="*50)
sub_folder = os.path.join(TARGET_DIR, "os_demo_root", "sub_folder")
data_folder = os.path.join(sub_folder, "data")
os.makedirs(data_folder, exist_ok=True)
print(f"【步骤2】已创建多级文件夹：{data_folder}")


# 3. 创建测试文件
print("\n" + "="*50)
old_file_path = os.path.join(data_folder, "initial_note.txt")
with open(old_file_path, "w", encoding="utf-8") as f:
    f.write("修复非空目录删除错误的测试文件\n")
    f.write("工作目录：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\n")
print(f"【步骤3】已创建测试文件：{old_file_path}")


# 4. 文件与文件夹改名（按正确顺序）
print("\n" + "="*50)
# 4.1 先改文件
new_file_path = os.path.join(data_folder, "os_practice.txt")
os.rename(old_file_path, new_file_path)
print(f"【步骤4.1】文件改名成功：{old_file_path} → {new_file_path}")

# 4.2 处理文件夹（先删目标文件夹避免冲突）
new_folder_path = os.path.join(TARGET_DIR, "os_demo_root", "work_folder")
if os.path.exists(new_folder_path):
    shutil.rmtree(new_folder_path)
    print(f"【步骤4.2】已删除残留目标文件夹：{new_folder_path}")
os.rename(sub_folder, new_folder_path)
updated_data_folder = os.path.join(new_folder_path, "data")  # 更新data文件夹路径
print(f"【步骤4.2】文件夹改名成功：{sub_folder} → {new_folder_path}")


# 5. 验证文件状态
print("\n" + "="*50)
target_file = os.path.join(updated_data_folder, "os_practice.txt")
print(f"【步骤5】目标文件存在：{os.path.exists(target_file)}")
print(f"【步骤5】文件大小：{os.path.getsize(target_file)} 字节")


# 6. 遍历目录
print("\n" + "="*50)
print("【步骤6】遍历os_demo_root目录：")
for root, dirs, files in os.walk(os.path.join(TARGET_DIR, "os_demo_root")):
    print(f"  → 当前目录：{root}")
    print(f"    - 子文件夹：{dirs}")
    print(f"    - 文件：{files}")
    print("    ---")


# 7. 复制操作
print("\n" + "="*50)
# 7.1 复制文件
copied_file = os.path.join(TARGET_DIR, "os_practice_copy.txt")
shutil.copy(target_file, copied_file)
print(f"【步骤7.1】文件复制成功：{copied_file}")

# 7.2 复制文件夹
copied_folder = os.path.join(TARGET_DIR, "os_demo_root_copy")
if os.path.exists(copied_folder):
    shutil.rmtree(copied_folder)
shutil.copytree(os.path.join(TARGET_DIR, "os_demo_root"), copied_folder)
print(f"【步骤7.2】文件夹复制成功：{copied_folder}")


# 8. 清理临时文件（核心修复：先删文件，再删空文件夹）
print("\n" + "="*50)
# 8.1 先删除data文件夹内的文件（关键步骤！确保文件夹变空）
if os.path.exists(target_file):
    os.remove(target_file)
    print(f"【步骤8.1】已删除data文件夹内的文件：{target_file}")

# 8.2 再删除空的data文件夹（此时文件夹已空，os.rmdir可正常执行）
if os.path.exists(updated_data_folder):
    os.rmdir(updated_data_folder)
    print(f"【步骤8.2】已删除空的data文件夹：{updated_data_folder}")

# 8.3 删除复制的单个文件
if os.path.exists(copied_file):
    os.remove(copied_file)
    print(f"【步骤8.3】已删除复制文件：{copied_file}")

# 8.4 删除非空文件夹
root_folder = os.path.join(TARGET_DIR, "os_demo_root")
if os.path.exists(root_folder):
    shutil.rmtree(root_folder)
    print(f"【步骤8.4】已删除原根文件夹：{root_folder}")
if os.path.exists(copied_folder):
    shutil.rmtree(copied_folder)
    print(f"【步骤8.4】已删除复制文件夹：{copied_folder}")


# 9. 错误原因与修复总结
print("\n" + "="*50)
print("【本次错误修复总结】")
print("1. 原错误原因：删除data文件夹（updated_data_folder）时，里面还存在os_practice.txt文件，导致os.rmdir()因目录非空报错（WinError 145）")
print("2. 修复方案：")
print("   - 清理阶段先删除data文件夹内的文件（target_file）")
print("   - 确认文件删除后，再用os.rmdir()删除空的data文件夹")
print("3. 关键逻辑：os.rmdir()仅能删除空目录，必须先清空内部所有文件/子文件夹")

'''
==================================================
【步骤1】当前工作目录：D:\adate\PythonProject\heimapython\00heima_python_basic\08day
【步骤1】目录有效性：正常

==================================================
【步骤2】已创建多级文件夹：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_demo_root\sub_folder\data

==================================================
【步骤3】已创建测试文件：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_demo_root\sub_folder\data\initial_note.txt

==================================================
【步骤4.1】文件改名成功：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_demo_root\sub_folder\data\initial_note.txt → D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_demo_root\sub_folder\data\os_practice.txt
【步骤4.2】文件夹改名成功：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_demo_root\sub_folder → D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_demo_root\work_folder

==================================================
【步骤5】目标文件存在：True
【步骤5】文件大小：125 字节

==================================================
【步骤6】遍历os_demo_root目录：
  → 当前目录：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_demo_root
    - 子文件夹：['work_folder']
    - 文件：[]
    ---
  → 当前目录：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_demo_root\work_folder
    - 子文件夹：['data']
    - 文件：[]
    ---
  → 当前目录：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_demo_root\work_folder\data
    - 子文件夹：[]
    - 文件：['os_practice.txt']
    ---

==================================================
【步骤7.1】文件复制成功：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_practice_copy.txt
【步骤7.2】文件夹复制成功：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_demo_root_copy

==================================================
【步骤8.1】已删除data文件夹内的文件：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_demo_root\work_folder\data\os_practice.txt
【步骤8.2】已删除空的data文件夹：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_demo_root\work_folder\data
【步骤8.3】已删除复制文件：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_practice_copy.txt
【步骤8.4】已删除原根文件夹：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_demo_root
【步骤8.4】已删除复制文件夹：D:/adate/PythonProject/heimapython/00heima_python_basic/08day\os_demo_root_copy

==================================================
【本次错误修复总结】
1. 原错误原因：删除data文件夹（updated_data_folder）时，里面还存在os_practice.txt文件，导致os.rmdir()因目录非空报错（WinError 145）
2. 修复方案：
   - 清理阶段先删除data文件夹内的文件（target_file）
   - 确认文件删除后，再用os.rmdir()删除空的data文件夹
3. 关键逻辑：os.rmdir()仅能删除空目录，必须先清空内部所有文件/子文件夹

'''
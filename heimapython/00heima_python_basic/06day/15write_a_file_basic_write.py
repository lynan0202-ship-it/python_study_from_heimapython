import os
import json  # 推荐用json处理字典的读写，更规范
base_path = r"D:\adate\PythonProject"
file_path = os.path.join(base_path, 'example.txt')
os.makedirs(base_path, exist_ok=True)  # 只创建文件夹，不包含文件名




with open(file_path, 'w', encoding='utf-8') as file:
    mydate = {"name": "liunainian", "age": 18}
    json.dump(mydate, file, ensure_ascii=False)

with open(file_path, 'r', encoding='utf-8') as file:
    content = json.load(file)  # 用json读取字典
    print(content)  # 输出：{'name': 'liunainian', 'age': 18}

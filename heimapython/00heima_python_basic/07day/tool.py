# 模块：tool.py
__all__ = ["clean_str", "format_date"]  # 只允许这两个“出门”

def clean_str(s):  # 能被导入
    print("clean_str可以引用")
    return s.strip()

def format_date(int):  # 能被导入
    print("format_date可以引用")
    return 0

def secret_func():  # 门禁外，不能被from tool import *导入
    print("这是内部函数，别碰！")
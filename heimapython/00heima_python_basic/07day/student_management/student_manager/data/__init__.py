# 控制 from student_manager.data import * 能导入的模块
__all__ = ["students"]  # 只允许导入students模块

# 子包内简化导入（比如其他模块想调用students.py时更方便）
from . import students
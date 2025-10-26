# student_manager/__init__.py 必须包含这两行
__all__ = ["core", "data", "ui"]  # 允许批量导入的模块/子包
from .core import calculate_average  # 把core模块的calculate_average导入到主包
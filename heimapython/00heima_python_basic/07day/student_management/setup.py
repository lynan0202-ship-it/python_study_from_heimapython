from setuptools import setup, find_packages

setup(
    name="student_manager",  # 包名（pip安装后用这个名导入）
    version="1.0.0",
    packages=find_packages(),  # 自动包含所有包
    author="你的名字",
    description="学生管理系统工具包（包含数据处理、成绩计算、界面显示）",
    python_requires=">=3.6",  # 支持的Python版本
)
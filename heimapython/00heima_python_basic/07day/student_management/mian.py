# 方式1：import 包.模块（完整路径）
import student_manager.data.students as s_data

# 方式2：from 包 import 模块/子包
from student_manager.ui import display
from student_manager import core

# 方式3：from 包.模块 import 函数（直接用函数）
from student_manager.core import is_passed

# 【关键】明确导入calculate_average函数（从主包或core模块都可以）
from student_manager import calculate_average  # 因为主包__init__.py已经导入了它
# 或者从core模块直接导入：from student_manager.core import calculate_average


def main():
    # 1. 新增学生
    new_id = s_data.add_student("小刚", [55, 70, 90])
    print(f"✨ 新增学生成功，ID：{new_id}")

    # 2. 显示所有学生
    display.show_all_students(s_data.students_db)

    # 3. 查看单个学生详情
    student = s_data.get_student_by_id(1)
    display.show_student_detail(student)

    # 4. 判断分数是否及格
    score = 58
    print(f"\n💡 分数{score}是否及格？{is_passed(score)}")

    # 5. 计算平均分（现在能正常调用了）
    print(f"\n📊 小明的平均分：{calculate_average(s_data.students_db[0]['scores']):.1f}")


if __name__ == "__main__":
    main()
'''
✨ 新增学生成功，ID：3

📋 所有学生列表：
ID: 1 | 姓名: 小明 | 分数: [85, 92, 78]
ID: 2 | 姓名: 小红 | 分数: [60, 75, 88]
ID: 3 | 姓名: 小刚 | 分数: [55, 70, 90]

📌 学生ID：1
姓名：小明
分数：[85, 92, 78]
平均分：85.0
✅ 全部及格

💡 分数58是否及格？False

📊 小明的平均分：85.0
'''
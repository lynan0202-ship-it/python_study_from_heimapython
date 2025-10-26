# 显示学生信息（调用主包的core模块计算平均分）
# 相对导入：.. 代表父包（student_manager），从父包导入core模块
from ..core import calculate_average, is_passed

def show_student_detail(student):
    """显示单个学生的详细信息（带平均分和及格情况）"""
    if not student:
        print("❌ 未找到该学生")
        return
    avg = calculate_average(student["scores"])
    passed_status = "✅ 全部及格" if all(is_passed(s) for s in student["scores"]) else "❌ 有不及格科目"
    print(f"\n📌 学生ID：{student['id']}")
    print(f"姓名：{student['name']}")
    print(f"分数：{student['scores']}")
    print(f"平均分：{avg:.1f}")
    print(passed_status)

def show_all_students(students_list):
    """显示所有学生的简略信息"""
    print("\n📋 所有学生列表：")
    for s in students_list:
        print(f"ID: {s['id']} | 姓名: {s['name']} | 分数: {s['scores']}")
# 学生数据存储和操作
students_db = [
    {"id": 1, "name": "小明", "scores": [85, 92, 78]},
    {"id": 2, "name": "小红", "scores": [60, 75, 88]}
]

def add_student(name, scores):
    """新增学生（自动生成ID）"""
    new_id = len(students_db) + 1
    students_db.append({"id": new_id, "name": name, "scores": scores})
    return new_id

def get_student_by_id(student_id):
    """根据ID查询学生"""
    for student in students_db:
        if student["id"] == student_id:
            return student
    return None
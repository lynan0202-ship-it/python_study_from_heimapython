# 核心功能：计算学生平均分、判断是否及格
def calculate_average(scores):
    """计算分数列表的平均分"""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def is_passed(score):
    """判断单个分数是否及格（60分及以上）"""
    return score >= 60
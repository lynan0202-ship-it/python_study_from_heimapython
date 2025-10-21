import random

# 初始化数据
classrooms = [[], [], []]  # 三个空教室
teachers = ['张老师', '李老师', '王老师', '赵老师', '刘老师', '陈老师', '杨老师', '黄老师']

# 随机分配
for teacher in teachers:
    class_id = random.randint(0, 2)  # 随机选择教室(0,1,2)
    classrooms[class_id].append(teacher)
print(classrooms)
# 显示结果
for i, classroom in enumerate(classrooms):
    print(f'教室{i+1}: {classroom}')

    '''
    [['赵老师', '陈老师', '黄老师'], ['张老师', '李老师', '王老师', '刘老师'], ['杨老师']]
教室1: ['赵老师', '陈老师', '黄老师']
教室2: ['张老师', '李老师', '王老师', '刘老师']
教室3: ['杨老师']

    '''
"""
YOLO模型类别字典遍历:
    概述:
        在YOLO目标检测中，我们需要遍历类别字典来处理不同的检测对象。
        遍历操作帮助我们逐个获取每个类别及其相关信息。

    YOLO类别字典遍历方式:
        思路1: 根据 类别ID 获取其对应的类别名称.          理解为: 根据 身份证号 找 人名.
        思路2: 根据 键值对 同时获取类别ID和名称.          理解为: 根据 身份证 找 编号和姓名.
"""

# 1. 定义YOLO模型常用的COCO数据集类别字典
coco_classes = {
    0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane',
    5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light',
    10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench',
    16: 'bird', 17: 'cat', 18: 'dog', 19: 'horse', 20: 'sheep'
}

# 2. 遍历YOLO类别字典
print("=== YOLO类别字典遍历演示 ===")

# 思路1: 根据类别ID获取类别名称
print("\n--- 方法1: 根据类别ID获取类别名称 ---")

# 2.1 获取所有的类别ID
class_ids = coco_classes.keys()
print(class_ids)
'''
#dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20])
'''
# 2.2 遍历每个类别ID，获取对应的类别名称
for class_id in class_ids:
    class_name = coco_classes.get(class_id)
    print(f'检测类别ID {class_id}: {class_name}')
'''
检测类别ID 0: person
检测类别ID 1: bicycle
检测类别ID 2: car
检测类别ID 3: motorcycle
检测类别ID 4: airplane
检测类别ID 5: bus
检测类别ID 6: train
检测类别ID 7: truck
检测类别ID 8: boat
检测类别ID 9: traffic light
检测类别ID 10: fire hydrant
检测类别ID 11: stop sign
检测类别ID 12: parking meter
检测类别ID 13: bench
检测类别ID 16: bird
检测类别ID 17: cat
检测类别ID 18: dog
检测类别ID 19: horse
检测类别ID 20: sheep
'''
print('-' * 40)

# 简化写法
for class_id in coco_classes.keys():
    print(f'类别 {class_id} -> {coco_classes.get(class_id)}')
'''
类别 0 -> person
类别 1 -> bicycle
类别 2 -> car
类别 3 -> motorcycle
类别 4 -> airplane
类别 5 -> bus
类别 6 -> train
类别 7 -> truck
类别 8 -> boat
类别 9 -> traffic light
类别 10 -> fire hydrant
类别 11 -> stop sign
类别 12 -> parking meter
类别 13 -> bench
类别 16 -> bird
类别 17 -> cat
类别 18 -> dog
类别 19 -> horse
类别 20 -> sheep
'''
print('-' * 40)

# 思路2: 同时获取类别ID和名称
print("\n--- 方法2: 同时获取类别ID和名称 ---")
print("2.1")
# 2.1 获取所有的键值对
class_items = coco_classes.items()
print(class_items)
'''
dict_items([(0, 'person'), (1, 'bicycle'), (2, 'car'), (3, 'motorcycle'), (4, 'airplane'), (5, 'bus'), (6, 'train'), (7, 'truck'), (8, 'boat'), (9, 'traffic light'), (10, 'fire hydrant'), (11, 'stop sign'), (12, 'parking meter'), (13, 'bench'), (16, 'bird'), (17, 'cat'), (18, 'dog'), (19, 'horse'), (20, 'sheep')])
'''
print("2.2")
# 2.2 遍历每个键值对
for item in class_items:
    class_id, class_name = item[0], item[1]
    print(f'ID: {class_id} -> 类别: {class_name}')
'''
0: person
1: bicycle
2: car
3: motorcycle
4: airplane
5: bus
6: train
7: truck
8: boat
9: traffic light
10: fire hydrant
11: stop sign
12: parking meter
13: bench
16: bird
17: cat
18: dog
19: horse
20: sheep
'''

print('-' * 40)

# 实际开发中的拆包写法
for class_id, class_name in coco_classes.items():
    print(f'{class_id}: {class_name}')
'''

0: person
1: bicycle
2: car
3: motorcycle
4: airplane
5: bus
6: train
7: truck
8: boat
9: traffic light
10: fire hydrant
11: stop sign
12: parking meter
13: bench
16: bird
17: cat
18: dog
19: horse
20: sheep
'''
print('-' * 40)

# 3. YOLO应用场景扩展操作
print("\n=== YOLO字典扩展操作 ===")

print("3.1")
# 扩展1: 根据类别名称反向查找ID
def find_class_id_by_name(class_dict, target_name):
    """根据类别名称查找对应的ID"""
    for class_id, class_name in class_dict.items():
        if class_name == target_name:
            return class_id
    return None


# 测试反向查找
target_class = 'car'
found_id = find_class_id_by_name(coco_classes, target_class)
print(f"类别 '{target_class}' 的ID是: {found_id}")
'''
类别 'car' 的ID是: 2
'''
print("3.2")
# 扩展2: 筛选特定类型的类别
def filter_classes_by_keyword(class_dict, keyword):
    """根据关键词筛选类别"""
    filtered = {}
    for class_id, class_name in class_dict.items():
        if keyword in class_name:
            filtered[class_id] = class_name
    return filtered

# 筛选交通工具类别
vehicle_classes = filter_classes_by_keyword(coco_classes, 'cycle')
print("\n包含'cycle'的类别:", vehicle_classes)

'''
包含'cycle'的类别: {1: 'bicycle', 3: 'motorcycle'}
'''

# 扩展3: 构建类别统计信息
def get_class_statistics(class_dict):
    """获取类别统计信息"""
    stats = {
        'total_classes': len(class_dict),
        'classes_by_length': {},
        'class_ids': list(class_dict.keys()),
        'class_names': list(class_dict.values())
    }

    # 按名称长度分组
    for class_name in class_dict.values():
        length = len(class_name)
        if length not in stats['classes_by_length']:
            stats['classes_by_length'][length] = []
        stats['classes_by_length'][length].append(class_name)

    return stats


# 获取统计信息
stats = get_class_statistics(coco_classes)
print(f"\n类别统计信息:")
print(f"总类别数: {stats['total_classes']}")
print(f"按名称长度分组: {stats['classes_by_length']}")


# 扩展4: YOLO检测结果处理
def process_detection_results(detections, class_dict):
    """处理YOLO检测结果"""
    processed_results = []

    for detection in detections:
        class_id = detection['class_id']
        confidence = detection['confidence']
        bbox = detection['bbox']

        # 使用字典遍历知识获取类别名称
        class_name = class_dict.get(class_id, 'unknown')

        processed_results.append({
            'class_name': class_name,
            'confidence': confidence,
            'bbox': bbox
        })

    return processed_results


# 模拟YOLO检测结果
sample_detections = [
    {'class_id': 2, 'confidence': 0.95, 'bbox': [100, 150, 200, 250]},
    {'class_id': 0, 'confidence': 0.87, 'bbox': [50, 80, 120, 200]},
    {'class_id': 17, 'confidence': 0.92, 'bbox': [300, 200, 400, 350]}
]

# 处理检测结果
results = process_detection_results(sample_detections, coco_classes)
print("\n处理后的检测结果:")
for result in results:
    print(f"检测到: {result['class_name']}, 置信度: {result['confidence']:.2f}")

# 扩展5: 字典推导式在YOLO中的应用
print("\n=== 字典推导式应用 ===")

# 创建名称到ID的映射
name_to_id = {name: id for id, name in coco_classes.items()}
print("名称到ID的映射:", name_to_id)

# 只保留特定ID范围的类别
filtered_classes = {id: name for id, name in coco_classes.items() if id <= 10}
print("ID≤10的类别:", filtered_classes)

# 为所有类别添加前缀
prefixed_classes = {id: f"COCO_{name}" for id, name in coco_classes.items()}
print("添加前缀的类别:", prefixed_classes)

print("\n=== YOLO字典遍历完成 ===")
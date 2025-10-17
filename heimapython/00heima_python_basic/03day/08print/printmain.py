import json  # 用于解析JSON文件


# 1. 读取本地JSON文件，获取查询参数
def get_query_params(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # 解析JSON数据为字典
            params = json.load(f)
            # 校验必要参数是否存在（避免后续报错）
            required_keys = ['status', 'start_date', 'countries', 'limit_num']
            for key in required_keys:
                if key not in params:
                    raise ValueError(f"JSON文件缺少必要参数：{key}")
            return params
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在：{file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"JSON文件格式错误：{file_path}")


# 2. 定义SQL查询模板
query_template = """
                 SELECT user_id, \
                        username, \
                        email, \
                        created_at
                 FROM users
                 WHERE status = %s
                   AND created_at >= %s
                   AND country IN ({})
                 ORDER BY created_at DESC
                     LIMIT %s \
                 """

# 3. 主逻辑：读取参数→生成最终查询→准备执行参数
if __name__ == "__main__":
    # 本地JSON文件路径（根据实际位置修改，这里假设和代码同目录）
    params_file = "query_params.json"

    # 读取参数
    params = get_query_params(params_file)
    print("从文件读取的参数：", params)

    # 处理IN子句的占位符（根据国家列表长度生成%s,%s...）
    countries = params['countries']
    placeholders = ','.join(['%s'] * len(countries))  # 生成"%s,%s,%s"

    # 生成最终SQL查询
    final_query = query_template.format(placeholders)
    print("\n生成的最终查询：\n", final_query)

    # 准备数据库执行参数（注意顺序要和SQL中的%s一一对应）
    # 顺序：status → start_date → 每个国家 → limit_num
    execute_params = (
        params['status'],
        params['start_date'],
        *countries,  # 解包国家列表（等同于country1, country2, country3）
        params['limit_num']
    )
    print("\n准备传入数据库的参数：", execute_params)

    # 4. （可选）连接数据库执行查询（以MySQL为例）
    # import mysql.connector
    # conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="test")
    # cursor = conn.cursor()
    # cursor.execute(final_query, execute_params)  # 用参数执行查询
    # result = cursor.fetchall()  # 获取结果
    # print("查询结果：", result)
    # cursor.close()
    # conn.close()

    """
    从文件读取的参数： {'status': 'active', 'start_date': '2023-01-01', 'countries': ['US', 'CN', 'JP'], 'limit_num': 10}

生成的最终查询：
 
                 SELECT user_id,                         username,                         email,                         created_at
                 FROM users
                 WHERE status = %s
                   AND created_at >= %s
                   AND country IN (%s,%s,%s)
                 ORDER BY created_at DESC
                     LIMIT %s                  

准备传入数据库的参数： ('active', '2023-01-01', 'US', 'CN', 'JP', 10)
    """
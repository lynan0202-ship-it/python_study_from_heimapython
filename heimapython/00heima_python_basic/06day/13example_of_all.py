import os


# 1. 首先创建data文件夹和test.txt文件
def create_test_file():
    # 检查data文件夹是否存在，不存在则创建
    if not os.path.exists('./data'):
        os.makedirs('./data')
        print("创建data文件夹")

    # 创建并写入test.txt文件
    with open('./data/test.txt', 'w', encoding='utf-8') as file:
        file.write("""这是第一行内容
这是第二行内容
Python文件操作很简单！
这是最后一行""")
    print("创建test.txt文件并写入内容")


# 2. 演示不同的文件读取方式
def demo_file_operations():
    print("\n=== 文件操作演示 ===")

    # 方法1: read() - 一次性读取全部内容
    print("1. 使用read()读取全部内容:")
    with open('./data/test.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

    print("\n" + "=" * 50)

    # 方法2: readline() - 逐行读取
    print("2. 使用readline()逐行读取:")
    with open('./data/test.txt', 'r', encoding='utf-8') as file:
        line1 = file.readline().strip()  # strip()去除换行符
        line2 = file.readline().strip()
        line3 = file.readline().strip()
        line4 = file.readline().strip()

        print(f"第一行: {line1}")
        print(f"第二行: {line2}")
        print(f"第三行: {line3}")
        print(f"第四行: {line4}")

    print("\n" + "=" * 50)

    # 方法3: readlines() - 读取所有行到列表
    print("3. 使用readlines()读取到列表:")
    with open('./data/test.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(f"所有行: {lines}")

        # 遍历列表并显示行号
        for i, line in enumerate(lines, 1):
            print(f"第{i}行: {line.strip()}")

    print("\n" + "=" * 50)

    # 方法4: 直接遍历文件对象（推荐方式）
    print("4. 直接遍历文件对象（推荐）:")
    with open('./data/test.txt', 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            print(f"第{line_num}行: {line.strip()}")


# 3. 演示不同路径写法
def demo_different_paths():
    print("\n=== 不同路径写法演示 ===")

    # 方法1: 相对路径（推荐）
    print("相对路径写法:")
    with open('./data/test.txt', 'r', encoding='utf-8') as file:
        print(f"内容: {file.read().strip()}")

    # 方法2: 原始字符串（Windows绝对路径）
    # print("\n原始字符串写法（Windows）:")
    # with open(r'C:\完整路径\test.txt', 'r', encoding='utf-8') as file:
    #     print(f"内容: {file.read().strip()}")

    # 方法3: 双反斜杠
    # print("\n双反斜杠写法:")
    # with open('C:\\完整路径\\test.txt', 'r', encoding='utf-8') as file:
    #     print(f"内容: {file.read().strip()}")


# 4. 文件操作异常处理
def demo_with_exception_handling():
    print("\n=== 异常处理演示 ===")

    try:
        # 尝试读取不存在的文件
        with open('./data/nonexistent.txt', 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("文件不存在！请检查文件路径")
    except Exception as e:
        print(f"发生错误: {e}")
    else:
        print("文件读取成功！")
    finally:
        print("异常处理演示结束")


# 主函数
def main():
    print("Python文件操作完整示例")
    print("=" * 60)

    # 创建测试文件
    create_test_file()

    # 演示各种文件操作
    demo_file_operations()

    # 演示不同路径写法
    demo_different_paths()

    # 演示异常处理
    demo_with_exception_handling()

    print("\n" + "=" * 60)
    print("程序执行完毕！")


# 运行程序
if __name__ == "__main__":
    main()
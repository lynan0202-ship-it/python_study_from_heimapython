# 1. 定义print_line()：打印一行指定列数和字符的图形（支持自定义字符，默认用'*'）
def print_line(cols, char='*'):
    """打印一行图形，cols为列数，char为图形字符"""
    for _ in range(cols):
        print(char, end='')
    print()  # 每行结束后换行


# 2. 定义print_lines()：调用print_line()打印锥形三角形（每行列数递增）
def print_lines(rows):
    """打印rows行的锥形三角形，第i行（0开始）列数为2i+1"""
    for i in range(rows):  # i表示当前行数（0到rows-1）
        current_cols = 2 * i + 1  # 计算当前行的列数（逐行递增2）
        print_line(current_cols)  # 调用单行打印函数


# 3. 调用函数，打印3行锥形三角形
print_lines(3)
'''
*
***
*****
'''
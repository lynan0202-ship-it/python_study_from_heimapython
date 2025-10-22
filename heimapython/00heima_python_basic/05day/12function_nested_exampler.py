# 需求1: 定义函数print_line()用于打印 一行图形, 定义函数 print_lines(), 底层调用 print_line()函数, 实现打印多行图形.

# 1. 定义函数print_line()用于打印 一行图形.
def print_line(cols):       # columns: 列.
    """
    定义函数, 用于打印1行图形.
    :param cols: 该行的列数.
    :return: 无
    """
    for i in range(cols):
        print('-', end='')
    print()                 # 打印完毕后, 记得换行


# 2. 定义函数 print_lines(), 底层调用 print_line()函数, 实现打印多行图形.
def print_lines(rows, cols):
    """
    该函数用于打印 多行图形.
    :param rows: 行数
    :param cols: 每行的列数
    :return: 无
    """
    for j in range(rows):
        # 具体的打印每一行图形的操作, 直接调用 print_line()函数即可.
        print_line(cols)


# 3. 调用print_lines()函数, 查看图形.
print_lines(3, 5)
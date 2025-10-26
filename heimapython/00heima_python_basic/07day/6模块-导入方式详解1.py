# 导入timer模块及相关函数
import timer
import timer as n  # timer模块的别名
from timer import sleeper  # 直接导入sleeper函数
from timer import sleeper as sle  # sleeper函数的别名
from timer import printer1  # 关键：导入printer1函数（否则调用会报错）
from time import *  # 导入time模块的所有函数

# 定义sleep()函数，调用timer模块的sleeper
def sleep():
    timer.sleeper()  # 用模块名调用
    n.sleeper()      # 用别名调用（等价于timer.sleeper()）

# 测试
if __name__ == "__main__":
    sleep()
    print("已经执行完以上内容")
    sleeper()  # 直接调用导入的sleeper函数
    print("已经执行完以上内容2")
    sle()      # 用别名调用sleeper函数
    printer1()  # 现在可以正常调用（已导入）
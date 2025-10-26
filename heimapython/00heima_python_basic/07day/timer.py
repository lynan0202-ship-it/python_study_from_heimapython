
#这是一个名叫timer的模块，其中应该有随机数生成现在的时间然后，根据此时间定义一些函数，函数的进入条件是在一定时间应该做具体某件事情
#首先先生成一个随机数
import random

def sleeper ():


    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    print(f"现在是{hour}时：{minute}分：{second}秒")
    if (hour <= 7 or(hour == 7 and minute <= 30))or (hour >= 23):
        print("现在是睡一觉的时间")
    else:
        print("现在不是睡觉的时间")
    return 0
def printer1():
    print("这个函数通过*被引用进来了")
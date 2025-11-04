#此算法有逻辑问题会出现num=9与i=0,不利于理解

n = int(input('请录入参与游戏的总人数：'))

num_list= [i for i in range(1,n+1)]


print(num_list)
num,i = 0,0

while len(num_list) != 1:
    num += 1  # 每轮数1个数字（1→2→3→1...）
    print(f'num为{num}')
    print(f'i为{i}')
    # 细节1：数到圈尾，索引重置为0（转圈）
    if i == len(num_list):
        i = 0

    # 细节2：数到3或3的倍数，淘汰当前人
    if num % 3 == 0:
        print(f'删去{num}')

        num_list.pop(i)  # 从列表中删除当前人
        print(num_list)
        i -= 1  # 删除后列表变短，索引回退1，避免跳过下一个人


    i += 1  # 下一个人准备数数

print(f'参与游戏总人数为: {n}, 幸运数字为: {num_list[0]}')

'''
请录入参与游戏的总人数：8
[1, 2, 3, 4, 5, 6, 7, 8]
num为1
i为0
num为2
i为1
num为3
i为2
删去3
[1, 2, 4, 5, 6, 7, 8]
num为4
i为2
num为5
i为3
num为6
i为4
删去6
[1, 2, 4, 5, 7, 8]
num为7
i为4
num为8
i为5
num为9
i为6
删去9
[2, 4, 5, 7, 8]
num为10
i为0
num为11
i为1
num为12
i为2
删去12
[2, 4, 7, 8]
num为13
i为2
num为14
i为3
num为15
i为4
删去15
[4, 7, 8]
num为16
i为0
num为17
i为1
num为18
i为2
删去18
[4, 7]
num为19
i为2
num为20
i为1
num为21
i为2
删去21
[7]
参与游戏总人数为: 8, 幸运数字为: 7
'''
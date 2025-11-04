import random  # 导入随机模块，用来洗牌
'''
思路为
1.poker_list = [color + num for num in num_list for color in color_list] 生成一个list(全色牌)

2.poker_dict = {i: poker_list[i] for i in range(len(poker_list))} 生成键值对字典，再加入 
 poker_dict[52] = '小🤡'
 poker_dict[53] = '大🤡'
3.poker_index = list(poker_dict.keys())获取值列表[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 。。。。

4.random.shuffle(poker_index) 随机打乱列表 list

5. for i in range(len(poker_index)):
[24, 12, 29, 22, 0, 10, 26, 3, 11, 6, 45, 43, 47, 13, 18, 1, 49, 53, 27, 19, 9, 38, 34, 7, 20, 8, 16, 5, 28, 23, 44,
 36, 4, 31, 41, 14, 51, 32, 40, 39, 15, 17, 30, 52, 46, 37, 50, 48, 2, 21, 35, 42, 33, 25]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
用索引来发值给每个人
索引i >= len(poker_index) - 3:
dp.append(current_card)留牌
索引i % 3 == 0:
p1.append(current_card)
索引i % 3 == 1:
p2.append(current_card)
else:（i % 3 == 2）
p3.append(current_card)

'''
# 1. 定义全局变量（牌桌的“基础设备”）
poker_dict = {}  # 牌的“身份证字典”：键=索引（身份证号），值=具体的牌（比如♠3）
poker_index = []  # 所有牌的“身份证号列表”：发牌时用它，看牌时按它排序
p1 = []  # 玩家1的手牌（存的是“身份证号”）
p2 = []  # 玩家2的手牌
p3 = []  # 玩家3的手牌
dp = []  # 底牌（同样存“身份证号”）


# 2. 第一步：买牌（生成54张扑克牌）
def get_poker():
    global poker_dict  # 声明用全局的poker_dict，不然函数里改不了外面的
    # 2.1 定义花色和点数（按斗地主牌的大小顺序来）
    color_list = ['♠', '♥', '♦', '♣']  # 四种花色（顺序不影响大小）
    num_list = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']  # 点数从小到大

    # 2.2 生成52张普通牌（花色+点数组合）
    # 列表推导式：先遍历点数（保证3最小、2最大），再遍历花色
    poker_list = [color + num for num in num_list for color in color_list]
    print(poker_list)
    # 2.3 给牌分配“身份证号”（0~51对应普通牌，52=小🤡，53=大🤡）
    poker_dict = {i: poker_list[i] for i in range(len(poker_list))}

    # 加上大小王（索引越大，牌越大）
    poker_dict[52] = '小🤡'
    poker_dict[53] = '大🤡'
    print(poker_dict)


# 3. 第二步：洗牌（打乱“身份证号列表”）
def shuffle_poker():
    global poker_index  # 声明用全局的poker_index
    # 3.1 获取所有牌的“身份证号”（0~53，共54个）
    poker_index = list(poker_dict.keys())
    print(poker_index)
    # 3.2 随机打乱列表（random.shuffle直接修改原列表，不用返回值）
    random.shuffle(poker_index)
    print(poker_index)


# 4. 第三步：发牌（轮询给玩家发牌，留3张底牌）
def send_poker():
    global p1, p2, p3, dp  # 声明用全局的玩家手牌和底牌
    # 遍历打乱后的“身份证号列表”，i是索引（0~53）
    for i in range(len(poker_index)):
        current_card = poker_index[i]  # 当前要发的牌的“身份证号”
        # 规则1：最后3张（i>=51）留作底牌
        if i >= len(poker_index) - 3:
            dp.append(current_card)
        # 规则2：轮询发牌（i%3=0→p1，i%3=1→p2，i%3=2→p3）
        elif i % 3 == 0:
            p1.append(current_card)
        elif i % 3 == 1:
            p2.append(current_card)
        else:
            p3.append(current_card)
    print(dp)
    print(p1)
    print(p2)
    print(p3)

# 5. 第四步：看牌（按“身份证号”排序，再显示具体的牌）
def look_poker(player_name, player_poker_num):
    """
    按大小整理并显示玩家手牌
    :param player_name: 玩家名字（比如“刘亦菲”）
    :param player_poker_num: 玩家手牌的“身份证号列表”（比如[5, 12, 52]）
    """
    # 5.1 排序：“身份证号”越小，牌越小（3<4<...<2<小🤡<大🤡）
    player_poker_num.sort() #p1,p2,p3
    # 5.2 把“身份证号”转成具体的牌（查poker_dict字典）
    player_poker = [poker_dict[i] for i in player_poker_num]
    print(player_poker)
    player_poker_dict = {i:poker_dict[i] for i in player_poker_num}
    print(player_poker_dict)
    # 5.3 打印结果
    print(f'\n{player_name}的牌是：{player_poker}')


# 主程序：启动发牌流程
if __name__ == '__main__':
    print("🎮 斗地主发牌开始！")
    get_poker()  # 1. 买牌
    shuffle_poker()  # 2. 洗牌
    send_poker()  # 3. 发牌
    # 4. 看牌
    look_poker('刘亦菲', p1)
    look_poker('赵丽颖', p2)
    look_poker('张小二', p3)
    look_poker('底牌', dp)
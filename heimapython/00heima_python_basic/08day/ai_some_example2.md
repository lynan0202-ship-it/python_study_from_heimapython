# 🃏 Python模拟斗地主发牌：手把手教你当“牌桌裁判”


## 🌟 先唠唠：我们要做啥？
想不想用Python代码还原斗地主的发牌流程？从“买一副新牌”到“打乱顺序”，再到“给3个玩家发牌+留底牌”，最后“按大小整理手牌”——全程自动化，比手动发牌还公平！

最终效果：3个玩家（比如“刘亦菲”“赵丽颖”“张小二”）各拿到17张牌，剩下3张当底牌，所有手牌自动按从小到大排序，清晰明了～


## 🚩 核心流程拆解（像真实斗地主一样）
和现实中玩斗地主一样，代码也分4步走：
1. **买牌**：生成一副完整的54张扑克牌（13种点数×4种花色 + 大小王）；
2. **洗牌**：打乱牌的顺序（不然每次发牌都一样，没意思）；
3. **发牌**：3个玩家轮着拿牌，最后3张留作底牌；
4. **看牌**：把每个玩家手里的牌按“从小到大”排序，方便查看。


## 💻 原代码逐行解析（小白也能懂）
先看完整的基础代码，再一步步拆讲解透：
```python
import random  # 导入随机模块，用来洗牌

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
    
    # 2.3 给牌分配“身份证号”（0~51对应普通牌，52=小🤡，53=大🤡）
    poker_dict = {i: poker_list[i] for i in range(len(poker_list))}
    # 加上大小王（索引越大，牌越大）
    poker_dict[52] = '小🤡'
    poker_dict[53] = '大🤡'


# 3. 第二步：洗牌（打乱“身份证号列表”）
def shuffle_poker():
    global poker_index  # 声明用全局的poker_index
    # 3.1 获取所有牌的“身份证号”（0~53，共54个）
    poker_index = list(poker_dict.keys())
    # 3.2 随机打乱列表（random.shuffle直接修改原列表，不用返回值）
    random.shuffle(poker_index)


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


# 5. 第四步：看牌（按“身份证号”排序，再显示具体的牌）
def look_poker(player_name, player_poker_num):
    """
    按大小整理并显示玩家手牌
    :param player_name: 玩家名字（比如“刘亦菲”）
    :param player_poker_num: 玩家手牌的“身份证号列表”（比如[5, 12, 52]）
    """
    # 5.1 排序：“身份证号”越小，牌越小（3<4<...<2<小🤡<大🤡）
    player_poker_num.sort()
    # 5.2 把“身份证号”转成具体的牌（查poker_dict字典）
    player_poker = [poker_dict[i] for i in player_poker_num]
    # 5.3 打印结果
    print(f'\n{player_name}的牌是：{player_poker}')


# 主程序：启动发牌流程
if __name__ == '__main__':
    print("🎮 斗地主发牌开始！")
    get_poker()    # 1. 买牌
    shuffle_poker()# 2. 洗牌
    send_poker()   # 3. 发牌
    # 4. 看牌
    look_poker('刘亦菲', p1)
    look_poker('赵丽颖', p2)
    look_poker('张小二', p3)
    look_poker('底牌', dp)
```


### 关键概念解释（避免懵圈）
1. **为什么用“身份证号（索引）”？**  
   因为斗地主的牌有大小顺序（3<4<...<2<小王<大王），给每张牌分配一个“索引”（0最小，53最大），排序时直接排索引，就能自动按牌的大小整理，比直接排“♠3”“♥4”这类字符串简单10倍！

2. **`global`关键字有啥用？**  
   函数里默认不能修改全局变量（比如`poker_dict`），加`global`就是告诉函数：“我要改的是外面那个全局变量，不是我自己的局部变量”。


## 📚 拓展功能：让发牌更真实！
基础版只能发牌看牌，加点功能更像真的斗地主～


### 拓展1：自动选地主（随机让一个玩家拿底牌）
斗地主得有地主！让程序随机选一个玩家，把底牌加到他手里：
```python
def choose_landlord():
    global p1, p2, p3, dp
    # 随机选地主（0=玩家1，1=玩家2，2=玩家3）
    landlord_idx = random.randint(0, 2)
    if landlord_idx == 0:
        p1 += dp  # 玩家1拿底牌
        return '刘亦菲（地主）'
    elif landlord_idx == 1:
        p2 += dp  # 玩家2拿底牌
        return '赵丽颖（地主）'
    else:
        p3 += dp  # 玩家3拿底牌
        return '张小二（地主）'

# 主程序里修改：发牌后选地主，再看牌
if __name__ == '__main__':
    print("🎮 斗地主发牌开始！")
    get_poker()    
    shuffle_poker()
    send_poker()   
    # 新增：选地主
    landlord = choose_landlord()
    print(f'\n🎉 地主是：{landlord}')
    # 看牌（此时地主的牌已经包含底牌）
    look_poker('刘亦菲', p1)
    look_poker('赵丽颖', p2)
    look_poker('张小二', p3)
```


### 拓展2：优化看牌格式（每10张牌换行，不挤在一起）
手牌太多时一行显示会很乱，加个换行逻辑：
```python
def look_poker(player_name, player_poker_num):
    player_poker_num.sort()
    player_poker = [poker_dict[i] for i in player_poker_num]
    # 优化：每10张牌换行
    print(f'\n{player_name}的牌是：')
    for idx, card in enumerate(player_poker):
        if (idx + 1) % 10 == 0:  # 每10张换一行
            print(card)
        else:
            print(card, end='  ')  # 没到10张就用空格分隔
```

**效果示例**：
```
刘亦菲（地主）的牌是：
♠3  ♥3  ♦3  ♣3  ♠4  ♥4  ♦4  ♣4  ♠5  ♥5
♦5  ♣5  ♠6  ♥6  ♦6  ♣6  小🤡  大🤡
```


### 拓展3：判断是否有“炸弹”（4张相同点数的牌）
炸弹是斗地主的王炸！教你简单判断玩家有没有炸弹：
```python
def check_bomb(player_poker_num):
    # 先把“身份证号”转成具体的牌，提取点数（比如♠3→3，小🤡→小王）
    player_poker = [poker_dict[i] for i in player_poker_num]
    # 提取点数（处理10和大小王：10是两位，大小王单独标记）
    points = []
    for card in player_poker:
        if card in ['小🤡', '大🤡']:
            points.append(card)
        elif card.endswith('10'):  # 处理“♠10”这类，点数是10
            points.append('10')
        else:
            points.append(card[1])  # 比如♠3→取索引1的字符“3”
    
    # 统计每个点数出现的次数，>=4就是炸弹
    from collections import Counter  # 用Counter快速计数
    point_count = Counter(points)
    bombs = [p for p, cnt in point_count.items() if cnt >= 4]
    if bombs:
        return f'有炸弹！{bombs}'
    else:
        return '没有炸弹'

# 看牌时顺便判断炸弹
if __name__ == '__main__':
    # ... 前面的代码不变 ...
    look_poker('刘亦菲', p1)
    print(f'刘亦菲：{check_bomb(p1)}')
    look_poker('赵丽颖', p2)
    print(f'赵丽颖：{check_bomb(p2)}')
```


### 拓展4：支持多轮游戏（问用户要不要再来一局）
一局不过瘾？加个循环，让用户决定是否继续：
```python
def reset_game():
    # 重置所有变量，准备下一局
    global poker_dict, poker_index, p1, p2, p3, dp
    poker_dict = {}
    poker_index = []
    p1 = []
    p2 = []
    p3 = []
    dp = []

if __name__ == '__main__':
    while True:
        reset_game()  # 重置游戏状态
        print("🎮 斗地主发牌开始！")
        get_poker()    
        shuffle_poker()
        send_poker()   
        landlord = choose_landlord()
        print(f'\n🎉 地主是：{landlord}')
        look_poker('刘亦菲', p1)
        look_poker('赵丽颖', p2)
        look_poker('张小二', p3)
        
        # 问用户是否继续
        again = input('\n要不要再来一局？（y/n）：').lower()
        if again != 'y':
            print("👋 游戏结束，下次再玩！")
            break
```


## 💡 总结：这个案例能学到啥？
看似只是模拟发牌，其实用到了很多Python核心知识点：
1. **数据结构**：用字典存“牌-索引”映射，用列表存手牌；
2. **循环与条件**：轮询发牌、判断底牌/地主；
3. **模块使用**：`random`（洗牌、选地主）、`collections.Counter`（统计牌型）；
4. **函数设计**：把“买牌、洗牌、发牌”拆成独立函数，代码更清晰；
5. **全局变量**：用`global`管理跨函数的变量（比如手牌、牌字典）。

试着改改代码吧！比如把玩家名字改成自己的朋友，或者加个“判断顺子”的功能，成就感拉满～ 🎉
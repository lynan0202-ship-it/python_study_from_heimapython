# 需求: 统计 小串 在 大串中出现的次数.

# 1. 定义变量, 表示: 大串.
max_str = "woaiheima, buguanheimahaishibaima, zhaodaogongzuojiushihaoma"


# 2. 定义变量, 表示: 小串.
min_str = "heima"


# 3. 统计 小串在大串中出现的次数.
# 思路1: 字符串自带的count()函数.
result1 = max_str.count(min_str)
print(result1)
# 思路2: split()切割 + 统计 元素个数.
list1 = max_str.split(min_str)   #"woai  heima   , buguan    heima   haishibaima, zhaodaogongzuojiushihaoma"  会分成3段
#[ 'woai','buguan ','haishibaima, zhaodaogongzuojiushihaoma'],len处理后为3
result2 = len(list1) - 1         # 分析出的规律.
print(result2)
# 思路3: 替换的思路.  公式: (大串长度 - 新串长度) / 小串长度
new_str = max_str.replace(min_str, '')
print(max_str)
print(new_str)
result3 = (len(max_str) - len(new_str)) // len(min_str)

# 思路4: find() + 切片, 自己写.


# 4. 打印结果.
print(result3)
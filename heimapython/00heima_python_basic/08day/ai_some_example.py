count = 0
for i in range(1234, 4322):
    s = str(i)
    # 检查是否包含1、2、3、4，且不包含'13'和'31'
    if ('1' in s and '2' in s and '3' in s and '4' in s and '13' not in s and '31' not in s):
        count += 1
        # 每3个数字换行，否则用制表符分隔（修正括号为英文半角）
        print(i, end='\n' if count % 3 == 0 else '\t')

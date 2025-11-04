# 1. 预设正确的账号和密码
correct_username = 'heima'
correct_password = 'ai28'
print(list(range(3)))
# 2. 循环3次（0→1→2，对应3次机会）
for i in range(3):
    # 3. 输入账号密码
    input_username = input('请输入账号: ')
    input_password = input('请输入密码: ')

    # 4. 验证是否正确
    if input_username == correct_username and input_password == correct_password:
        print(f'欢迎您，{input_username}！')
        break  # 登录成功，结束循环
    else:
        # 5. 错误提示：最后一次提示锁定，否则提示剩余机会
        if i == 2:
            print('录入错误次数已达上限，账号被锁定，请联系管理员：010-123456')
        else:
            remaining = 2 - i  # 剩余机会：2→1（第一次错剩2次，第二次错剩1次）
            print(f'账号或密码错误，您还有{remaining}次机会！')
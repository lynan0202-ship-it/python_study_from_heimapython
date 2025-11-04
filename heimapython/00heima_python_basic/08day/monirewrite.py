import datetime
import getpass

correct_name = 'heimapython'
correct_key = '2021600'

print("=== 账号登录（共3次机会）===")  # 增加登录引导
for i in range(3):
    # 1. 用户名输入：增加“第X次”提示，明确当前进度
    print(f"\n【第{i + 1}次尝试】")
    inputname = input("请输入用户名（输入后按Enter）：")

    # 2. getpass兼容处理：若环境不支持，降级为普通输入（并提示风险）
    try:
        # 正常情况：用getpass隐藏密码输入
        inputkey = getpass.getpass("请输入密码（输入后按Enter，密码会隐藏）：")
    except Exception:
        # 兼容IDE/在线环境：降级为普通输入，提示密码可见
        print("⚠️ 当前环境不支持隐藏密码，输入时密码会显示在屏幕上")
        inputkey = input("请输入密码（输入后按Enter）：")

    # 3. 登录判断逻辑不变
    if inputname == correct_name and inputkey == correct_key:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"\n{now} 欢迎您，登录成功！")
        break
    elif i == 2:
        print("\n输入次数已达上限，请联系管理员！")
    else:
        remaining = 2 - i
        print(f"\n账号或密码错误！您还有{remaining}次机会。")
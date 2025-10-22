# 1. 全局变量：定义在所有函数外面，相当于"公共变量"，整个文件都能访问
global_num = 100  # 全局变量：从这行开始到文件结束，所有地方都可能用到它


# 2. 函数内的局部变量：相当于函数的"私房钱"，只能在函数内部用，函数结束就消失
def use_local():
    local_num = 200  # 局部变量：只属于这个函数，出了函数就找不到了
    print("函数内访问局部变量local_num：", local_num)  # 能正常访问（自己的钱自己用）
    print("函数内访问全局变量global_num：", global_num)  # 能访问全局变量（公共财产大家用）


# 3. 函数内修改全局变量：需要用global声明，否则会被当成局部变量
def modify_global():
    # 情况1：不声明global，直接赋值会创建局部变量（相当于自己造了个同名"私房钱"）
    # global_num = 300  # 不写global时，这行是创建局部变量，不会影响外面的全局变量

    # 情况2：用global声明后，才是真正修改全局变量（告诉函数：我要改公共财产）
    global global_num
    global_num = 300  # 现在修改的是外面的全局变量
    print("函数内用global修改后，全局变量global_num：", global_num)


# 4. 演示"就近原则"：函数内有局部变量就用局部的，没有就找全局的
def near_first():
    global_num = 400  # 局部变量（和全局变量同名）
    print("函数内有同名局部变量时，优先用局部的：", global_num)  # 用自己的400，不是全局的100


# 调用函数观察结果
print("调用use_local()：")
use_local()
print("-" * 50)

print("调用modify_global()：")
modify_global()
print("函数外查看全局变量是否被修改：", global_num)  # 已经被改成300
print("-" * 50)

print("调用near_first()：")
near_first()
print("函数外查看全局变量（不受局部同名变量影响）：", global_num)  # 还是300，局部变量不影响全局
print("-" * 50)

# 尝试访问局部变量（会报错）
try:
    print("函数外访问局部变量local_num：", local_num)
except NameError as e:
    print("报错原因：", e)  # 提示局部变量未定义，因为出了函数就消失了

    '''
    调用use_local()：
函数内访问局部变量local_num： 200
函数内访问全局变量global_num： 100
--------------------------------------------------
调用modify_global()：
函数内用global修改后，全局变量global_num： 300
函数外查看全局变量是否被修改： 300
--------------------------------------------------
调用near_first()：
函数内有同名局部变量时，优先用局部的： 400
函数外查看全局变量（不受局部同名变量影响）： 300
--------------------------------------------------
报错原因： name 'local_num' is not defined
    '''
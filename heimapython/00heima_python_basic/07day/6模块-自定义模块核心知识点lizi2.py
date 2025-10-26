from tool import *

clean_str("name")
format_date(10)
try:
    secret_func()
except Exception as e:
    print(e)
print("程序已经运行结束")
'''
clean_str可以引用
format_date可以引用
name 'secret_func' is not defined
程序已经运行结束
'''
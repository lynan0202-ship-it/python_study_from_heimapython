# 拷贝文件并处理异常
try:
    # 打开源文件和目标文件
    src_file = open("source.txt", "rb")
    dest_file = open("dest.txt", "wb")
except Exception as e:
    print(f"文件打开失败：{e}")
else:
    # 无异常时执行拷贝
    while True:
        data = src_file.read(1024)  # 每次读1024字节
        if not data:  # 读取完毕
            break
        dest_file.write(data)
    print("文件拷贝成功")
finally:
    # 确保文件关闭（释放资源）
    try:
        src_file.close()
    except:
        print("close_source_error")  # 若文件未打开，关闭会报错，直接忽略
    try:
        dest_file.close()
    except:
        print("close_dest_error")
        '''
        文件打开失败：[Errno 2] No such file or directory: 'source.txt'
close_source_error
close_dest_error
        '''
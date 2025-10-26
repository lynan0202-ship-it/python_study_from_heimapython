#结合with语句（自动释放资源）

# with语句会自动关闭文件，简化finally操作
try:
    with open("source.txt", "rb") as src_file, open("dest.txt", "wb") as dest_file:
        while True:
            data = src_file.read(1024)
            if not data:
                break
            dest_file.write(data)
    print("文件拷贝成功")
except Exception as e:
    print(f"拷贝失败：{e}")

try:
    with open("mydate.txt","rb") as src_file, open("dest.txt","wb") as dest_file:
        while True :
            data = src_file.read(1024)
            if not data:
                break
            dest_file.write(data)
        print("文件拷贝成功")
except Exception as e:
    print(e)
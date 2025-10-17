# 诗歌、歌词等需要保留格式的文本
poem = '''
静夜思
床前明月光，疑是地上霜。
举头望明月，低头思故乡。
'''
print(poem)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
    </style>
</head>
<body>
    <h1>{heading}</h1>
    <p>{content}</p>
</body>
</html>
"""
"""


<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
    </style>
</head>
<body>
    <h1>{heading}</h1>
    <p>{content}</p>
</body>
</html>


"""

# 使用时格式化
formatted_html = html_template.format(
    title="我的网页",
    heading="欢迎光临",
    content="这是网页内容"
)

print(html_template)
print(formatted_html)

"""

<!DOCTYPE html>
<html>
<head>
    <title>我的网页</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
    </style>
</head>
<body>
    <h1>欢迎光临</h1>
    <p>这是网页内容</p>
</body>
</html>"""
email_template = """
尊敬的 {name} 先生/女士：

感谢您注册我们的服务！
您的账户信息如下：
- 用户名：{username}
- 注册时间：{register_time}

如有任何问题，请随时联系客服。

此致
敬礼！

{company} 团队
{date}
"""

formatted_html = email_template.format(
    name="我的网页",
    username="lnn",
    register_time="这是网页内容",
    company="zhes",
    date="abb",

)
print(formatted_html )

formatted_email = email_template.format(
    name="张三",
    username="lnn",
    register_time="2024-01-15",
    company="ABC科技有限公司",
    date="2024年1月15日"
)
print(formatted_html )

"""



感谢您注册我们的服务！
您的账户信息如下：
- 用户名：lnn
- 注册时间：这是网页内容

如有任何问题，请随时联系客服。

此致
敬礼！

zhes 团队
abb
"""
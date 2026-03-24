#代理,可以使用第三方机器来代理你的请求

import requests

#  https://www.kuaidaili.com/free/intr/ 获取代理
# 代理的弊端：
# 1.代理服务器的IP地址和端口号可能随时改变，导致代理失效
# 2.慢


#准备代理信息
proxy ={
    "http":"http://223.215.177.245:8089",
    "https":"https://223.215.177.245:8089"
}


url  = "https://www.baidu.com"

#proxies 代理
try:
    # 添加超时控制（建议5-10秒），避免无限等待
    resp = requests.get(url, proxies=proxy, timeout=10)
    resp.encoding = "utf-8"
    print("请求成功，响应内容前200字：")
    print(resp.text[:200])
except requests.exceptions.ProxyError as e:
    print(f"代理连接失败：{e}")
    print("请检查代理IP是否可用，或更换最新的免费代理")
except requests.exceptions.Timeout as e:
    print(f"请求超时：{e}")
except Exception as e:
    print(f"其他错误：{e}")
finally:
    # 关闭响应连接（可选，requests会自动处理，但显式关闭更规范）
    if 'resp' in locals():
        resp.close()
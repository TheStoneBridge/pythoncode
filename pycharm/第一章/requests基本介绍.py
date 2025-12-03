#导入网络请求的第三方模块
import requests

#模拟构造headers请求头信息

headers = {
    'user-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0'
    }


#通过requests模块发送网络请求
response = requests.get('https://www.douban.com',headers=headers)

print(response)
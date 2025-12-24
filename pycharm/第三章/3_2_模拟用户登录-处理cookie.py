#登录 ->得到cookie
#带着cookie 去请求到书架url->书架上的内容
#必须得把上面的两个操作连起来
#我们可以使用session进行请求 -> session你可以认为是一连串的请求。在这个过程中的cookie不会丢失
import requests

# 会话
session = requests.session()
data={
    "username": "zxcasdqwe",
    "password": "zxcqwe123"
}


#1. 登录
url = 'https://www.171k.com/login'
session.post(url, data=data)
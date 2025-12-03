import requests

url = "https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php"

# #模拟构造headers请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

data = {
    'log': 'ceshi',
    'pwd': '1234566',
    'rememberme': 'forever',
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
}

response = requests.post(url,data=data,headers=headers)

response.encoding = 'utf-8'

print(response.text)
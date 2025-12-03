import requests

#构建参数的字典

kw={
    "kw" : input("请输入要翻译的内容：")
}
url ="https://fanyi.baidu.com/sug"
#模拟构造headers请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Referer' :'https://fanyi.baidu.com/'  # 新增：指定请求来源
    }

response = requests.post(url,headers=headers,data=kw)

#手动设置编码格式

# response.encoding = 'utf-8'

print(response.text) #返回的是字符串格式的数据
print(response.json()) #返回的是json格式的数据

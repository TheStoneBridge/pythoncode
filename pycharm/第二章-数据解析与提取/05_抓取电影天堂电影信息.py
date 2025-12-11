"""
1. 提取到主页面中的每一个电影背后的那个url地址
   1. 拿到"2023新片精品"那一块的HTML代码
   2. 从刚才拿到的HTML代码中提取到href的值
2.访问子页面，提取到电影的名称以及下载地址
"""
import requests
import re

url = "http://www.dytt8.net/index.htm"

headers={  
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
}
resp = requests.get(url,headers=headers)
resp.encoding = "gbk"
# print(resp.text)


#1.拿到"2023新片精品"那一块的HTML代码
obj1 = re.compile(r"2023新片精品.*?<ul>(?P<html>.*?)</ul>",re.S)
result1 = obj1.search(resp.text)
html = result1.group("html")
# print(html) 

#2. 提取a标签中的href的值

obj2 = re.compile(r"<a href='(?P<href>.*?)'>20")

result2 = obj2.finditer(html)

obj3 = re.compile(r'<div id="Zoom">.*?片　　名(?P<name>.*?)<br />.*?href="(?P<download>.*?)">',re.S)
for item in result2:
    # print(item.group("href"))
    child_url = url.strip("/") + item.group("href")
    child_url1 = child_url.replace("/index.htm", "")
    # print(child_url1)
    child_resp = requests.get(child_url1,headers=headers)
    child_resp.encoding = "gbk"
    
    result3 = obj3.search(child_resp.text)
    name = result3.group("name")
    download = result3.group("download")
    print(name,download)
    
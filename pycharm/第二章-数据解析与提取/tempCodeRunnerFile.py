# 思路
#1.拿到页面源代码
#2.编写正则，提取页面数据
#3.保存数据

import requests
import re

url="https://movie.douban.com/top250"
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
}
resp = requests.get(url,headers=headers)

pageSource = resp.text


#编写正则表达式
#re.S 让.匹配换行符
obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?导演: (?P<director>.*?)&nbsp;.*?<br>'
                 r'(?P<year>.*?)&nbsp;<span class="rating_num" property="v:average">'
                 r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>',re.S)

#进行正则匹配
result = obj.finditer(pageSource)
for item in result:
    name=item.group("name")
    director=item.group("director")
    year=item.group("year").strip()
    score=item.group("score")
    num=item.group("num").strip()
    print(name,director,year,score,num)
    
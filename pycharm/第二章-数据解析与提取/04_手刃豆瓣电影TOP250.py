# 思路
#1.拿到页面源代码
#2.编写正则，提取页面数据
#3.保存数据

import requests
import re
import os  # 导入os模块用于处理路径

# 获取当前脚本所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 拼接CSV文件的完整路径（当前目录下的top250.csv）
csv_path = os.path.join(current_dir, "top250.csv")

# 使用拼接好的路径打开文件
f = open(csv_path, mode="a", encoding="utf-8")  

for i  in range(0,250,25):
    url=f"https://movie.douban.com/top250?start={i}&filter="

    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        "referer":"https://movie.douban.com/explore?support_type=movie&is_all=false&category=%E7%83%AD%E9%97%A8&type=%E5%85%A8%E9%83%A8"
    }
    resp = requests.get(url,headers=headers)

    pageSource = resp.text
    #编写正则表达式
    #re.S 让.匹配换行符
    obj= re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)'
                    r'</span>.*?<p>.*?导演:(?P<director>.*?)&nbsp;.*?'
                    r'<br>(?P<year>.*?)&nbsp;.*?'
                    r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                    r'<span>(?P<num>.*?)人评价</span>',re.S)

    #进行正则匹配
    result = obj.finditer(pageSource)
    for item in result:
        name = item.group("name").strip()  #strip()去掉字符串前后的空格
        director = item.group("director").strip()
        year = item.group("year").strip()
        score = item.group("score").strip()
        num = item.group("num").strip()
        f.write(f"{name},{director},{year},{score},{num}\n")
f.close()
resp.close()
print("豆瓣top250数据提取完成")
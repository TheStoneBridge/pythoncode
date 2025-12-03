from urllib.request import urlopen

url = "https://www.baidu.com"

response = urlopen(url)

# print(response.read().decode("utf-8")) #此时拿到的是页面的源代码

with open("baidu.html", "w", encoding="utf-8") as f:
    f.write(response.read().decode("utf-8"))


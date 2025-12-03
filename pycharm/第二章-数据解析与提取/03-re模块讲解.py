import re


# resurlt = re.findall("a","abcdefa")
# print(resurlt)

# result = re.findall(r"\d+","abc123def456ghi789")
# print(result)

# result = re.finditer(r"\d+","我今年18岁,我有2只猫,我每天花费100元养猫")   #出来是一个match的迭代器
# for i in result:  #从迭代器中拿内容   
#     print(i.group())  #从匹配结果中拿数据  i.group() 的作用就是从 Match 对象中提取出实际匹配的字符串内容。

#search方法 只会匹配字符串中第一个匹配项
# result = re.search(r"\d+","abc123def456ghi789")
# print(result.group()) 

# result = re.match(r"\d+","我叫ikun,今年18岁,我有2只猫,我每天花费100元养猫")
# print(result)  #match方法是从字符串的开头开始匹配的,所以这里返回None  等价于在正则前面加^ 即为^/d+

# result = re.match(r"\d+","1我叫ikun,今年18岁,我有2只猫,我每天花费100元养猫")
# print(result.group())  #match方法是从字符串的开头开始匹配的,所以这里返回None  等价于在正则前面加^ 即为^/d+

# #预加载，提前把正则对象加载完毕
# obj = re.compile(r"\d+")
# #直接把加载好的正则进行使用
# result = obj.findall("我叫ikun,今年18岁,我有2只猫,我每天花费100元养猫")
# print(result)



#想要提取数据必须用小括号括起来，可以单独起名字
#(?P<名字>正则表达式)
#提取数据的时候，需要group("名字")

s="""
    <div class='西游记'><span id='01'>美猴王</span></div>
    <div class='红楼梦'><span id='02'>贾宝玉</span></div>
"""

# obj = re.compile(r"<span id='(\d+)'>(.*?)</span>")
# result = obj.findall(s)
# print(result)  #返回的是一个列表，列表中每一项是一个元组，元组中是每个分组匹配到的内容

obj = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")
result = obj.finditer(s)
for i in result:
    print(i.group("id"))
    print(i.group("name"))
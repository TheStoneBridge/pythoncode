from pyquery import PyQuery

html="""
<ul>
<li class="aaa"><a href="http://www.google.com">谷歌</a></Li>
<li class="aaa"><a href="http://www.baidu.com">百度</a></Li>
<li class="bbb" id="qq"><a href="http://www.qq.com">腾讯</a></li>
<li class="bbb"><a href="http://www.yuanlai.com">猿来</a></li>
</ul>
"""

# 加载html内容
p = PyQuery(html)
# print(p)
# print(type(p))   #<class 'pyquery.pyquery.PyQuery'>  是PyQuery对象

# a = p("a")   # 通过标签名获取标签
# print(a)
# print(type(a))   #<class 'pyquery.pyquery.PyQuery'>  还是PyQuery对象

# #链式操作
a = p("li")("a")   # 通过标签名获取标签 
# a = p ("li a")
print(a) 
# print(type(a))  #<class 'pyquery.pyquery.PyQuery'>  还是PyQuery对象

# a = p(".aaa a")   # 通过类名获取标签
# print(a)

# a = p("#qq a")   # 通过id名获取标签
# print(a)

# href =  p("#qq a").attr("href")   # 获取属性值
# print(href)
# text = p("#qq a").text()    # 获取文本内容
# print(text)

#坑 如果多个标签同时拿属性，只能默认拿到第一个
# hrefs = p("li a").attr("href")
# print(hrefs)

#多个标签拿属性
# it = p("li a").items()
# for i in it:
#     href = i.attr("href")
#     text = i.text()
#     print(text,href)

# 快速总结
#  1.pyquery(选择器)
#  2. items() 当选择器选择的内容很多的时候，需要一个一个处理
#  3. attr(属性名) 获取属性信息
#  4. text()获取文本

# div = """
#     <div><span>心峰已被云窃去</span></div>
# """
# p = PyQuery(div)
# html = p("div").html()   #获取div标签内的所有内容
# text = p("div").text()   #获取div标签内的文本内容
# print(html)
# print(text)
 

# html = """
# <HTML>
# <div class="aaa">哒哒</div>
# <div class="bbb">嘟嘟嘟</div>
# </HTML>
# """
# p = PyQuery(html)
# # p("div.aaa").after("""<div class='ccc'>哈哈哈</div>""")   #在指定标签后面添加内容
# # p("div.aaa").append("""<span>哈哈哈</span>""")  #在指定标签里面添加内容

# # p("div.bbb").attr("class","aaa") #修改属性值
# # p("div.bbb").attr("id","1234") #新增属性值  前提是没有这个属性
# # p("div.bbb").remove_attr("id")   #删除属性
# p("div.bbb").remove() #删除标签
# print(p)
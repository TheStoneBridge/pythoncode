# 练习 1（os 模块）
# 获取当前目录
# 列出当前目录下所有文件
# 判断当前目录下是否存在 a.txt
# import os

# # 获取当前目录
# os.chdir(os.path.dirname(__file__))  # 切换到当前脚本所在目录
# current_document = os.getcwd()
# print(current_document)

# # 列出当前目录下所有文件
# for file in os.listdir() :
#     print(file)

# # 判断当前目录下是否存在 a.txt
# if os.path.exists("a.txt"):
#     print("a.txt 存在")
# else:
#     print("a.txt 不存在")

# 练习 2（json 模块）
# 定义字典：{"class": "Python班", "count": 30, "teacher": "张老师"}
# 转为 JSON 字符串并打印
# 再把 JSON 字符串转回字典，输出班级人数

# import json

# # 定义字典：{"class": "Python班", "count": 30, "teacher": "张老师"}
# data = {"class": "Python班", 
#         "count": 30, 
#         "teacher": "张老师"}
# # 转为 JSON 字符串并打印
# json_data = json.dumps(data, ensure_ascii=False, indent=4)
# print(json_data)

# # 再把 JSON 字符串转回字典，输出班级人数
# str_data  = json.loads(json_data)
# print(str_data["count"])


# 练习 3（re 模块）
# 给定字符串："价格：¥199，折扣价¥99"
# 用正则提取所有数字
# 把所有数字替换为 0

# import re 
# # 给定字符串："价格：¥199，折扣价¥99"
# str = "价格：¥199，折扣价¥99"
# # 用正则提取所有数字
# number = re.findall(r"\d+",str)
# print(number)

# # 把所有数字替换为 0
# sub = re.sub(r"\d+","0",str)
# print(sub)

# 练习 4（pathlib 模块）
# 使用 Path 判断 data 文件夹是否存在
# 如果不存在，创建它
# 遍历当前目录，打印所有 .py 文件

from pathlib import Path
# 使用 Path 判断 data 文件夹是否存在
if Path("data").exists():
    print("data 文件夹存在")
# 如果不存在，创建它
else:
    print("data 文件夹不存在")
    Path("data").mkdir()

# 遍历当前目录，打印所有 .py 文件
current_dir = Path(__file__).parent  # 获取当前脚本所在目录
for file in current_dir.iterdir():  #iterdir() 方法返回一个生成器，生成当前目录下的所有文件和文件夹的 Path 对象
    if file.suffix == ".py":
        print(file)
# 一、os 模块（操作系统相关）
# 知识点讲解
# 用来操作文件、文件夹、路径、系统信息
# 常用功能：
# os.getcwd() 获取当前目录
# os.listdir() 列出目录下文件
# os.path.exists() 判断文件 / 文件夹是否存在
# os.mkdir() 创建文件夹
# os.rename() 重命名
# os.remove() 删除文件

# import os

# # 切换到当前 .py 文件所在的文件夹  
# os.chdir(os.path.dirname(__file__))  
# # 1. 获取当前工作目录
# current_dir = os.getcwd()  #在 VS Code 里看到的文件夹是 45day，这就是项目文件夹，但它不一定等于 Python 运行时的 当前工作目录（cwd）。  
# print("当前目录:", current_dir)

# # 2. 列出当前目录下所有文件
# files = os.listdir(current_dir)
# print("目录内容:", files)

# # 3. 判断文件是否存在
# if os.path.exists("test.txt"):
#     print("文件存在")
# else:
#     print("文件不存在")


# 二、json 模块（处理 JSON 数据）
# 知识点讲解
# 用于 Python 字典 ↔ JSON 字符串 / 文件 互相转换
# 核心方法：
# json.dumps()：字典 → JSON 字符串
# json.loads()：JSON 字符串 → 字典
# json.dump()：字典写入 JSON 文件
# json.load()：从 JSON 文件读成字典

# import json

# # 字典
# data = {
#     "name": "小明",
#     "age": 20,
#     "hobby": ["篮球", "游戏"]
# }

# # 1. 字典转 JSON 字符串
# json_str = json.dumps(data, ensure_ascii=False, indent=4)  #ensure_ascii=False 让中文正常显示  indent=4 格式化输出，更美观 loads 把字符串变成可操作的字典
# print("JSON字符串:\n", json_str)

# # 2. JSON 字符串转回字典
# data2 = json.loads(json_str)
# print("姓名:", data2["name"])


# 三、re 模块（正则表达式）
# 知识点讲解
# 用来字符串匹配、查找、替换、提取内容
# 常用函数：
# re.findall() 查找所有匹配内容
# re.search() 查找第一个匹配
# re.sub() 替换字符串
# 常用规则：
# \d 匹配数字
# \w 匹配字母 / 数字 / 下划线
# [a-z] 小写字母
# + 至少一个

# import re

# text = "我的电话是13812345678，邮箱是abc123@qq.com"

# # 1. 提取手机号
# phone = re.findall(r"\d{11}", text)
# print("手机号:", phone)

# # 2. 替换数字为 *
# new_text = re.sub(r"\d", "*", text)
# print("替换后:", new_text)

# \d{11} 匹配 11 位连续数字（手机号）
# re.findall 返回所有匹配结果列表
# re.sub 把所有数字替换成 *

# 四、pathlib 模块（面向对象路径操作）
# 知识点讲解
# Python3 推荐的现代路径操作模块，比 os 更好用
# 用面向对象方式处理路径
# 常用：
# Path() 创建路径对象
# .exists() 判断是否存在
# .mkdir() 创建文件夹
# .iterdir() 遍历目录
# .suffix 获取文件后缀

from pathlib import Path

# 创建路径对象
p = Path("test.txt")

# 判断是否存在
if p.exists():
    print("文件存在")
else:
    print("文件不存在")

# 遍历当前目录
for file in Path(".").iterdir():
    print(file)


# Path(".") 表示当前目录
# .exists()、.iterdir() 都是对象方法，写法更简洁
# 跨平台（Windows/macOS/Linux）自动兼容路径格式
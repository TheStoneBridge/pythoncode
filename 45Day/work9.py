# 练习 1
# 编写代码：
# 配置 logging，级别设为 INFO
# 日志格式包含：时间、日志级别、日志内容
# 分别输出一条 info、warning、error 日志

# import logging

# logging.basicConfig(
#     level = logging.INFO, # 设置最低日志级别为 INFO，INFO 及以上级别日志会显示
#     format = '%(asctime)s - %(levelname)s - %(message)s', # 设置日志格式
#     datefmt= '%Y-%m-%d %H:%M:%S'
# )
# logging.info("这是一个 info 日志")
# logging.warning("这是一个 warning 日志")
# logging.error("这是一个 error 日志")

# 练习 2
# 实现文件日志：
# 将日志保存到 app_log.txt
# 设置编码 utf-8，级别为 WARNING
# 输出一条警告日志、一条错误日志

# import logging
# import os

# os.chdir(os.path.dirname(__file__)) # 切换到当前脚本所在目录，日志文件也会保存在这里

# logging.basicConfig(
#     level = logging.WARNING, # 设置最低日志级别为 WARNING，WARNING 及以上级别日志会显示
#     format = '%(asctime)s - %(levelname)s - %(message)s', # 设置日志格式
#     datefmt= '%Y-%m-%d %H:%M:%S',
#     filename = 'app_log.txt', # 设置日志文件名
#     encoding='utf-8' # 设置文件编码为 utf-8，防止中文乱码
# )

# logging.warning("这是一个 warning 日志")
# logging.error("这是一个 error 日志")

# 练习 3
# 综合应用题：
# 定义函数 read_text()，尝试读取 test.txt
# 用 try 捕获文件不存在异常
# 正常读取用 logging.info 记录；
# 读取失败用 logging.error 记录错误信息

import logging
import os 

os.chdir(os.path.dirname(__file__)) # 切换到当前脚本所在目录，日志文件也会保存在这里

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    datefmt= '%Y-%m-%d %H:%M:%S',
    filename = 'app_log.txt',
    encoding='utf-8'
)

def read_text():
    try:
        with open("test.txt", "r", encoding="utf-8") as f:
            file_content = f.read()
            logging.info("文件读取成功")
    except FileNotFoundError:
        logging.error("文件不存在")

read_text()

# Python logging 日志模块
# 一、知识讲解
# 1. 作用
# logging 是 Python内置日志模块，替代 print 打印：
# 分级输出信息（调试、正常、警告、错误、严重错误）
# 可输出到控制台 / 本地文件
# 可记录：时间、日志级别、代码行号、自定义内容
# 项目开发必备，方便排查 bug
# 级别	函数	用途
# DEBUG	logging.debug()	调试细节，开发用
# INFO	logging.info()	正常运行提示
# WARNING	logging.warning()	不影响程序的警告
# ERROR	logging.error()	功能异常、局部错误
# CRITICAL	logging.critical()	致命错误、程序崩溃

# 默认只显示 WARNING 及以上 级别日志。
# 3. 核心配置
# logging.basicConfig()：统一设置日志格式、输出位置、级别
# 常用参数：
# level：设置最低日志级别
# format：自定义日志输出格式
# filename：日志写入文件
# encoding="utf-8"：防止中文乱码
# 常用格式符号
# %(asctime)s：日志时间
# %(levelname)s：日志级别
# %(message)s：日志内容
# %(filename)s：当前文件名
# %(lineno)d：代码行号

# 二、基础语法
# import logging

# #全局配置
# logging.basicConfig(
#     level = logging.DEBUG, # 设置最低日志级别为 DEBUG
#     format = "%(asctime)s  - %(levelname)s - %(message)s", # 自定义日志格式
#     datefmt="%Y-%m-%d %H:%M:%S" # 时间格式
# )

# #分级打印日志
# logging.debug("调试信息")
# logging.info("正常提示")
# logging.warning("警告信息")
# logging.error("错误信息")
# logging.critical("致命错误")

# 三、示例 + 逐行详细讲解
# 示例 1：控制台输出完整日志（最常用）
#1.导入内置模块
# import logging

# #2.日志全局初始化配置
# logging.basicConfig(
#     level = logging.DEBUG, # 设置最低日志级别为 DEBUG，所有级别日志都会显示
#     format = "%(asctime)s | %(levelname)s | %(message)s", # 自定义日志格式，包含时间、级别和内容))
#     datefmt = "%Y-%m-%d %H:%M:%S" # 时间格式
# )

# #3.不同级别日志输出
# logging.debug("程序启动，初始化变量")
# logging.info("用户登录成功")
# logging.warning("内存占用过高")
# logging.error("文件读取失败")
# logging.critical("数据库连接断开，程序即将退出")


# 示例 2：日志保存到本地文件 + 中文不乱码
# import logging 
# import os

# os.chdir(os.path.dirname(__file__)) # 切换到当前脚本所在目录，日志文件也会保存在这里
# #日志写入txt文件
# logging.basicConfig(
#     level = logging.INFO, # 设置最低日志级别为 INFO，DEBUG 级别日志不会显示
#     format = "%(asctime)s | %(levelname)s | %(message)s", # 自定义日志格式，包含时间、级别和内容
#     filename = "log.txt", # 日志写入文件
#     encoding="utf-8", # 防止中文乱码
#     datefmt= "%Y-%m-%d %H:%M:%S" # 时间格式
# )

# logging.info("系统开始运行")
# logging.warning("参数配置非默认")
# logging.error("数据解析异常")

# 示例 3：结合异常处理，记录错误日志
import  logging
import os

os.chdir(os.path.dirname(__file__)) # 切换到当前脚本所在目录，日志文件也会保存在这里

logging.basicConfig(

    level = logging.INFO, # 设置最低日志级别为 INFO，DEBUG 级别日志不会显示
    format = "%(asctime)s | %(levelname)s | %(message)s", # 自定义日志格式，包含时间、级别和内容   
    filename = "error.txt", # 日志写入文件
    encoding="utf-8", # 防止中文乱码    
)

def divide(a,b):
    try:
        return a/b
    except Exception as e:
        logging.error(f"除数不能为0，错误信息：{e}")

divide(10,0)
from pymongo import MongoClient

# 1. 建立连接（和之前一样）
client = MongoClient("mongodb://localhost:27017/")

# 2. 核心操作：删除数据库
# 传入你要删除的数据库名称字符串
client.drop_database("我的第一个数据库")

# 3. 验证是否删除成功
print("删除后剩余的数据库列表：")
print(client.list_database_names())
# 此时打印结果里，应该已经没有「我的第一个数据库」了
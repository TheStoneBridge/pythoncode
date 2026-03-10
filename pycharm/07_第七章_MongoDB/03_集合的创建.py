from pymongo import MongoClient

# 创建连接
client = MongoClient('mongodb://localhost:27017/')

# 创建数据库
db = client['test']

# 创建集合
db.create_collection('my_collection')


print("数据库和集合创建成功！",db.list_collection_names())
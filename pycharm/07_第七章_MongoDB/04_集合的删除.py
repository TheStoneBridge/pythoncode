from pymongo import MongoClient

# 连接MongoDB数据库
client = MongoClient('mongodb://localhost:27017/')

#连接数据库
db = client['test']

print("删除前的集合列表：", db.list_collection_names())

# 删除集合
db.drop_collection('my_collection')
print("删除后的集合列表：", db.list_collection_names())
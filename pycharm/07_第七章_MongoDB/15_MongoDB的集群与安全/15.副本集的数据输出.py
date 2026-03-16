from pymongo import MongoClient



client = MongoClient('localhost:28017,localhost:28018,localhost:28019')

db = client['articledb']

collection = db['comment']
#查询集合下的所有文档
print("查询集合下的所有文档：",list(collection.find()))
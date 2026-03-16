from pymongo import MongoClient

#连接数据库
client = MongoClient('mongodb://localhost:27017/')
#选择数据库
db = client['test']
#选择集合
collection = db['students']

print(collection.find({'name':'张三'}).explain())
print('---------------------------------------------------------------')

collection.create_index({'name': 1})  # create_index() 方法用于在集合中创建索引，参数是要索引的字段名称；
print(collection.find({'name':'张三'}).explain())   
from pymongo import MongoClient

#连接数据库
client = MongoClient('mongodb://localhost:27017/')
#选择数据库
db = client['test']
#选择集合
collection = db['students']

print(collection.find({'name':'张三'},{'name':1,'_id':0}).explain())
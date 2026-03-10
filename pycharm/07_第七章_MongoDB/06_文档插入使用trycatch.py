from pymongo import MongoClient 

# 连接MongoDB数据库
client = MongoClient('mongodb://localhost:27017/')

# 选择数据库
db = client['test']

# 选择集合
collection = db['students']

# 插入数据
try:
    result = collection.insert_one({'name': '张三', 'age': 20, 'gender': '男'})
    print(result.inserted_id)
    print('数据库列表:', client.list_database_names())
    print('集合列表:', db.list_collection_names())
    print('集合中的文档:', list(collection.find()))
except Exception as e:
    print(e)

collection.drop()
print('数据库列表:', client.list_database_names())
# print('集合列表:', db.list_collection_names()) 
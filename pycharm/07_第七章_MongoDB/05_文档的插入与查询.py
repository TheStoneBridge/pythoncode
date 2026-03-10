from pymongo import MongoClient

# 连接MongoDB数据库
client = MongoClient('mongodb://localhost:27017/')

# 连接数据库
db = client['test']

#创建集合
collection = db['test_collection']

# # 插入文档
# result = collection.insert_one({'name': '张三', 'age': 18, 'gender': '男'})
# print(result.inserted_id)

# 插入多个文档
result = collection.insert_many([{'name': '李四', 'age': 20, 'gender': '男'},
                                  {'name': '王五', 'age': 22, 'gender': '女'}])

# 查询集合下的所有文档
# for doc in collection.find():
#     print(doc)

print("查询集合下的所有文档：",list(db.test_collection.find()))
#查询单条数据
print("查询集合的某条文档:",collection.find_one({'name': '李四'}))
#查询集合的某条数据的某个字段
print("查询集合的某条文档的某个字段:",collection.find_one({'name': '李四'},{'age':1}))
#查询集合的某条数据的多个字段
print("查询集合的某条文档的多个字段:",collection.find_one({'name': '李四'},{'age':1,'gender':1}))
#查询集合的某条数据的多个字段，不显示_id字段
print("查询集合的某条文档的多个字段，不显示_id字段:",collection.find_one({'name': '李四'},{'age':1,'gender':1,'_id':0}))


#查询数据库
print(client.list_database_names())
#查询集合
print(db.list_collection_names())

#清空集合
collection.drop()

#查询集合下的所有文档
for doc in collection.find():
    print(doc)

#查询数据库
print(client.list_database_names())
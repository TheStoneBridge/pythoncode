from pymongo import MongoClient

# 连接MongoDB数据库
client = MongoClient('mongodb://localhost:27017/')

# 连接数据库
db = client['school']

# 连接集合
collection = db['students']

#插入文档
collection.insert_many([
    {'name': 'xiaoming', 'age': 18, 'gender': 'male'},
    {'name': 'xiaohong', 'age': 19, 'gender': 'female'},
    {'name': 'xiaoli', 'age': 20, 'gender': 'male'},
    {'name': 'xiaozhang', 'age': 21, 'gender': 'female'}
])

# 查询文档
print("查询结果：", list(db.students.find()))
# 更新文档
collection.replace_one({'name': 'xiaoming'}, {'age': 20}) #覆盖原有文档
# 同时执行：删除name/gender字段 + 把age设为20（一个update_one完成，原子操作）
# collection.update_one(
#     {'name': 'xiaoming'},
#     {
#         '$set': {'age': 20},    # 更新age为20
#         '$unset': {'name': '', 'gender': ''}  # 删除name和gender字段（值写空即可）
#     }
# )
collection.update_one({'name': 'xiaohong'}, {'$set': {'age': 21}}) #更新指定字段
collection.update_many({'gender': 'female'}, {'$set': {'gender': 'male'}}) #更新多个文档
collection.update_one({'name': 'xiaohong'},{'$inc':{'age':1}}) #列值增长的修改

# 查询文档
print("更新后查询结果：", list(db.students.find()))

# 删除文档
collection.drop()
client.close()
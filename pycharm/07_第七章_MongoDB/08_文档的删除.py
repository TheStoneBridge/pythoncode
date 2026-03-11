from pymongo import MongoClient

# 连接MongoDB
client = MongoClient('mongodb://localhost:27017/')

# 选择数据库
db = client['test']

# 选择集合
collection = db['students']

#插入文档

collection.insert_many([
    {'_id': 1, 'name': '张三', 'age': 18, 'gender': '男', 'address': '北京'},
    {'_id': 2, 'name': '李四', 'age': 19, 'gender': '男', 'address': '上海'},
    {'_id': 3, 'name': '王五', 'age': 20, 'gender': '男', 'address': '广州'},
    {'_id': 4, 'name': '赵六', 'age': 21, 'gender': '男', 'address': '深圳'},
    {'_id': 5, 'name': '钱七', 'age': 21, 'gender': '男', 'address': '杭州'},
    {'_id': 6, 'name': '孙八', 'age': 23, 'gender': '男', 'address': '南京'}
])
# 查询文档
print("查询结果：", list(db.students.find()))

# 删除文档
collection.delete_one({'name': '张三'}) # delete_one() 删除一条文档
# 查询文档
print("删除后查询结果：", list(db.students.find()))

collection.delete_many({'age': 21}) # delete_many() 删除多条文档
# 查询文档
print("删除后查询结果：", list(db.students.find()))

collection.delete_many({}) # delete_many({}) 删除所有文档
# 查询文档
print("删除后查询结果：", list(db.students.find()))

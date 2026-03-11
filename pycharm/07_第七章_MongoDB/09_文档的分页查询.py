from pymongo import MongoClient

# 创建连接
client = MongoClient('mongodb://localhost:27017/')

# 选择数据库
db = client['test']

# 选择集合
collection = db['students']

collection.delete_many({}) # delete_many({}) 删除所有文档
#插入文档
collection.insert_many([
    {'_id': 1, 'name': '张三', 'age': 18, 'gender': '男', 'address': '北京'},
    {'_id': 2, 'name': '李四', 'age': 19, 'gender': '男', 'address': '上海'},
    {'_id': 3, 'name': '王五', 'age': 18, 'gender': '男', 'address': '广州'},
    {'_id': 4, 'name': '赵六', 'age': 21, 'gender': '男', 'address': '深圳'},
    {'_id': 5, 'name': '钱七', 'age': 22, 'gender': '男', 'address': '杭州'}
])

#统计查询
print("统计查询结果：", collection.count_documents({})) #统计集合中所有文档的数量
print("统计查询结果：", collection.count_documents({'age': 20})) #统计集合中age为20的文档数量

#分页查询
print("分页查询结果：", list(collection.find().limit(2))) #跳过0条，查询2条
print("分页查询结果：", list(collection.find().skip(2).limit(2))) #跳过2条，查询2条
print("分页查询结果：", list(collection.find().skip(4).limit(2))) #跳过4条，查询2条
 
#排序查询
print("排序查询结果：", list(collection.find().sort('age', 1))) #按照age升序排序
print("排序查询结果：", list(collection.find().sort('age', -1))) #按照age降序排序
print("排序查询结果：", list(collection.find({},{'age':1}).sort('age', -1))) #按照age降序排序，只显示age字段升序排序，如果age相同则按照name降序排序
print("排序查询结果：", list(collection.find({},{'age':1}).sort([('age', 1), ('_id', -1)])))   #按照age升序排序，如果age相同则按照_id降序排序

#清空文档
collection.delete_many({}) # delete_many({}) 删除所有文档
print("清空后查询结果：", list(db.students.find()))
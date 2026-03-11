from pymongo import MongoClient

#连接数据库
client = MongoClient('mongodb://localhost:27017/')

#选择数据库
db = client['test']

#选择集合
collection = db['students']

#插入数据
collection.delete_many({}) # delete_many({}) 删除所有文档

collection.insert_many([
    {'_id': 1, 'name': '张三', 'age': 18, 'content': '学生', 'introduction': '张三是一个学生，喜欢学习。'},
    {'_id': 2, 'name': '李四', 'age': 19, 'content': '学生', 'introduction': '李四是一个学生，喜欢摄影。'},
    {'_id': 3, 'name': '王五', 'age': 18, 'content': '学生', 'introduction': '王五是一个学生，喜欢看电影。'},
    {'_id': 4, 'name': '赵六', 'age': 21, 'content': '学生', 'introduction': '赵六是一个学生，喜欢打球。'},
    {'_id': 5, 'name': '钱七', 'age': 22, 'content': '班长', 'introduction': '钱七是班长，喜欢玩游戏。'}
])

#查询集合下的所有文档
print("查询集合下的所有文档：",list(db.students.find()))

print('正则查询',list(collection.find({'introduction': {'$regex': '影'}})))  # 正则查询 
#$regex 是 MongoDB 正则操作符：专门用于正则匹配，替代 Python 的re模块，直接在查询条件中使用；

print('比较查询',list(collection.find({'age': {'$gt': 21}})))  # 比较查询 
# $gt 大于  $lt 小于  $gte 大于等于  $lte 小于等于

print('包含查询',list(collection.find({'age': {'$in': [18, 19]}})))  # 包含查询

print('存在查询',list(collection.find({'content': {'$exists': True}})))  # 存在查询

print('条件查询or',list(collection.find({'$or': [{'age': 18}, {'age': {'$lt':20}}]})))  # 条件查询

print('条件查询and',list(collection.find({'$and': [{'age': 22}, {'content': '班长'}]})))  # 条件查询
from pymongo import MongoClient

#连接数据库
client = MongoClient('mongodb://localhost:27017/')

#选择集合
db = client['test']

comment = db['students']

#查看文档的索引
# print('查看文档的索引：',list(db.students.index_information()))
print('查看文档的索引：',list(comment.index_information()))

#建立索引
comment.create_index({'name': -1})  # create_index() 方法用于在集合中创建索引，参数是要索引的字段名称；
print('查看文档的索引：',list(comment.index_information()))
comment.drop_index('name_-1')  # drop_index() 方法用于删除集合中的索引，参数是要删除的索引名称；
print('查看文档的索引：',list(comment.index_information()))

comment.create_index({'id': 1,'age':-1})  # create_indexes() 方法用于在集合中创建多个索引，参数是一个列表，包含要索引的字段名称和排序方式；
print('查看文档的索引：',list(comment.index_information()))

comment.drop_index('id_1_age_-1')  # drop_indexes() 方法用于删除集合中的所有索引
print('查看文档的索引：',list(comment.index_information()))

comment.drop_indexes()  # drop_indexes() 方法用于删除集合中的所有索引
print('查看文档的索引：',list(comment.index_information()))  #不会删除_id索引，因为_id索引是MongoDB默认创建的索引，不能删除。
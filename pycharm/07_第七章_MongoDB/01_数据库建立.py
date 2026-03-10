from pymongo import MongoClient
# 连接本地 MongoDB（和你原有代码一致）
client = MongoClient("mongodb://localhost:27017/")

# 1. 声明要创建的数据库（此时仅为引用，未实际创建）
mydb = client["我的第一个数据库"]  # 自定义数据库名，比如mydb/student_db等

# 2. 声明要创建的集合（此时也仅为引用，未实际创建）
mycol = mydb["用户表"]  # 自定义集合名，比如user/student/order等

# 3. 插入一条数据（关键！首次插入时，自动创建上述数据库和集合）
mydata = {"name": "张三", "age": 20, "gender": "男"}
mycol.insert_one(mydata)  # 插入单条数据，触发创建

# 验证：查看已连接的数据库（此时能看到新建的数据库）
print("已连接的数据库：", client.list_database_names())
# 验证：查看新建数据库下的集合
print("新建数据库的集合：", mydb.list_collection_names())
# 验证：查询插入的数据
print("插入的数据：", mycol.find_one())
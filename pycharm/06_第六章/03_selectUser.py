import sqlite3

#创建连接对象
conn =  sqlite3.connect('test.db')
#创建游标对象
cursor = conn.cursor()
#执行sql语句
sql = 'select * from user'
cursor.execute(sql)
# cursor.fetchone() #获取一条数据 若多次执行则会获取下一条数据
# result = cursor.fetchone()
result = cursor.fetchmany(3) #获取多条数据  
print(result)


#关闭游标
cursor.close()
#关闭连接
conn.close()
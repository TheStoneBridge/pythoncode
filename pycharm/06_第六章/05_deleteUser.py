import sqlite3

#创建连接对象
conn =  sqlite3.connect('test.db')
#创建游标对象
cursor = conn.cursor()
#执行sql语句
sql = 'delete from user where id = ?'
cursor.execute(sql,(5,)) # ,表示元组
cursor.execute('select * from user')
result = cursor.fetchall() #获取所有数据
print(result)
#关闭游标

cursor.close()
#提交事务
conn.commit()
#关闭连接
conn.close()
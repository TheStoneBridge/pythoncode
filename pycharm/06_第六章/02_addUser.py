import sqlite3

#创建连接对象
conn =  sqlite3.connect('test.db')
#创建游标对象
cursor = conn.cursor()
#执行sql语句
# sql = 'insert into user(id,name) values(1,"ikun")'
# cursor.execute(sql)
# sql = 'insert into user(id,name) values(?,?)'
# cursor.execute(sql,(2,'pink baby'))
sql = 'insert into user(id,name) values(?,?)'
data = [(3,'pink'),(4,'baby'),(5,'old brother sister')]
cursor.executemany(sql,data)
#关闭游标
cursor.close()
#提交事务
conn.commit()
#关闭连接
conn.close()
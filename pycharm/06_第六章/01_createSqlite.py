import sqlite3

#创建连接对象
conn =  sqlite3.connect('test.db')
#创建游标对象
cursor = conn.cursor()
#执行sql语句
cursor.execute('create  table user(id int(10) primary key,name varchar(20))')
#关闭游标
cursor.close()
#关闭连接
conn.close()
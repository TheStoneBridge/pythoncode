#导入PyMySQL模块
import pymysql
# 调用connect()函数生产connection连接对象
db =  pymysql.connect(host='localhost',user = 'root',password='host',database='mrsoft',charset='utf8')
#调用cursor()方法获取cursor对象
cursor = db.cursor() 
#执行SQL语句
# data = ('Python编程指南', '计算机科学', 59.80, '2023-01-01')
data = [('Pytho编程指南', '计算机科学', 59.80, '2023-01-01'),
        ('Java编程指南', '计算机科学', 69.80, '2023-02-01'),
        ('C++编程指南', '计算机科学', 79.80, '2023-03-01')]
sql = 'insert into books(name,category,price,publish_time) values(%s,%s,%s,%s)'

cursor.executemany(sql,data)
#关闭连接
cursor.close()
db.close()

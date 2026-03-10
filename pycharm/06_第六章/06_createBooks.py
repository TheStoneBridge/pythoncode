#导入PyMySQL模块
import pymysql
# 调用connect()函数生产connection连接对象
db =  pymysql.connect(host='localhost',user = 'root',password='host',database='mrsoft')
#调用cursor()方法获取cursor对象
cursor = db.cursor()
cursor.execute('drop table if exists books') 
#执行SQL语句
sql = """
create table books(
    id int(8) not null auto_increment,
    name varchar(50) not null,
    category varchar(50) not null,
    price decimal(10,2) default null,
    publish_time date default null,
    primary key(id)
)engine = MyISAM AUTO_INCREMENT=1 default charset=utf8;
"""
cursor.execute(sql)
#关闭连接
cursor.close()
db.close()

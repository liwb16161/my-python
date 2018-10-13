import pymysql

class Mysqldo():
    def __init__(self, host = "localhost", port = 3306, user = "root",
                password = "a15932378445", db = "mydb1", charset = "utf8")
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset

        self.myconn = pymysql.connect(host = self.host,
                          port = self.port,
                          user = self.user,
                          password = self.password,
                          db = self.db,
                          charset = self.charset)

    def sql_exec(self,sql):

        cursor = self.myconn.cursor()

effect_row = cursor.execute('''
DROP TABLE `tbusers`
''')

# 创建数据表
effect_row = cursor.execute('''
CREATE TABLE `tbusers` (
  `name` varchar(32) NOT NULL,
  `age` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
''')

# 插入数据(元组或列表)
effect_row = cursor.execute('INSERT INTO `tbusers` (`name`, `age`) VALUES (%s, %s)', ('mary', 18))

# 插入数据(字典)
info = {'name': 'fake', 'age': 15}
effect_row = cursor.execute('INSERT INTO `tbusers` (`name`, `age`) VALUES (%(name)s, %(age)s)', info)

# 获取游标
cursor = connection.cursor()

# 批量插入
effect_row = cursor.executemany(
    'INSERT INTO `tbusers` (`name`, `age`) VALUES (%s, %s) ON DUPLICATE KEY UPDATE age=VALUES(age)', [
        ('hello', 13),
        ('fake', 28),
    ])

connection.commit()




myconn.commit()

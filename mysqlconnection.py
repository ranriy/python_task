import pymysql.cursors

from datetime import datetime

class MySQLConnection:
	def __init__(self,db):
		self.connection = pymysql.connect(host='localhost',
										user='root',
										password='root',
										db=db,
										charset='utf8mb4',
										cursorclass=pymysql.cursors.DictCursor,
										autocommit=True)
		self.cursor = self.connection.cursor()


	def query_db(self):
		self.cursor.execute('SELECT * FROM datatable;')
		return self.cursor.fetchall()

	def log_requests(self):
		self.cursor.execute('CREATE TABLE IF NOT EXISTS `logtable` (`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT, `requested_at` TIMESTAMP, `message` TEXT);')
		requested_time = datetime.now()
		self.cursor.execute('INSERT INTO `logtable` (requested_at,message) VALUES (%(requested_time)s, %(message)s)', {'requested_time':requested_time, 'message': f'Data requested at {requested_time}'})

	def close(self):
		self.connection.close()
		self.cursor.close()


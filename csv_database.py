import pandas as pd
import pymysql.cursors
from sqlalchemy import create_engine

connection = pymysql.connect(host='localhost',
							user='root',
							password='root',
							charset='utf8mb4',
							cursorclass=pymysql.cursors.DictCursor,
							autocommit=True)
cursor = connection.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS `taskdb`;')
cursor.execute('USE taskdb;')
cursor.execute('CREATE TABLE IF NOT EXISTS `datatable` (`id` INT NOT NULL, `timestamp` TIMESTAMP, `temperature` FLOAT ,`duration` TEXT);')

engine = create_engine('mysql+pymysql://root:root@localhost/taskdb')

df = pd.read_csv('task_data.csv',dtype={'id':int,'temperature':float,'duration':str},parse_dates=['timestamp'])
df.to_sql('datatable',con=engine,index=False,if_exists='replace')

cursor.close()
connection.close()
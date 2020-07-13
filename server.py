from flask import Flask, render_template
from mysqlconnection import MySQLConnection

app = Flask(__name__)

@app.route('/')
def home():
	conn = MySQLConnection('taskdb')
	conn.log_requests()
	result = conn.query_db()
	conn.close()
	return render_template('index.html', data=result)

if __name__=="__main__":
	app.run()


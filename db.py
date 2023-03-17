from flask_mysqldb import MySQL
from app import app



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'adi2020'
app.config['MYSQL_DB'] = 'flask'



mysql = MySQL(app)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{user}:{password}@{server}/{database}'.format(user='admin', password='sit312Group!', server='rfidcheckin.cljhbnnuplh1.ap-southeast-2.rds.amazonaws.com', database='rfidDB')
app.config['SECRET_KEY'] = '2392510167989ae56f41070a'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'
from dashboardPackage import routes

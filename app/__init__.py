from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from config import basedir,SQLALCHEMY_DATABASE_URI,SECRET_KEY
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__, static_url_path='', static_folder='static')
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
admin = Admin(app)

from app import views, models
admin.add_view(ModelView(models.User,db.session))

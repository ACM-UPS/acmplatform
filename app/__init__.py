from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from config import basedir,SQLALCHEMY_DATABASE_URI,SECRET_KEY
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask.ext.mail import Message, Mail

app = Flask(__name__, static_url_path='', static_folder='static')


from app.blog.views import mod
app.register_blueprint(blog.views.mod, url_prefix='/blog')

app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
admin = Admin(app)

db.create_all()

from app import views, models as UserModel
from app.blog import models as BlogModel
admin.add_view(ModelView(UserModel.User,db.session))
admin.add_view(ModelView(UserModel.BlogPost,db.session))

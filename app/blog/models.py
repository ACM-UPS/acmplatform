from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class BlogPost(db.Model):
	'''Blog Post Model'''
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(120), index=True, unique=True)
	content = db.Column(db.Text(), index=True)

	# def __init__(self, id, title, content):
	# 	self.id = id
	# 	self.title = title
	# 	self.content = content

# still figuring out how to to make this work

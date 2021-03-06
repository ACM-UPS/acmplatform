from app import db

class User(db.Model):
	'''User Model'''
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index= True, unique=True)

	def __repr__(self):
		'''toString()'''
		return '<user %r>' % (self.nickname)

class BlogPost(db.Model):
	'''Blog Post Model'''
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(120), index=True, unique=True)
	content = db.Column(db.Text(), index=True)

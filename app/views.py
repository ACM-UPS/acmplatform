from flask import render_template, flash, redirect, session, url_for, request, g, jsonify, Flask, Markup
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, models
# from .models import User
# from .models import BlogPost
import json
import datetime


# index view function supressed for brevity

@app.route('/')
def index():
	'''index route (main page)'''
	return render_template('index.html')

@app.route('/blog/')
def blog():
	return render_template('blog.html', post = models.BlogPost.query.all())

@app.route('/blog/new/', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['title'] or not request.form['content']:
         flash('Please enter all the fields', 'error')
      else:
         post = models.BlogPost(id=777, title=request.form['title'], content=request.form['content'])
         db.session.add(post)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('blog'))
   return render_template('blog/new.html')

# if __name__ == '__init__':
#    db.create_all()
#    app.run(debug = True)

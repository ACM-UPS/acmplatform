from flask import render_template, flash, redirect, session, url_for, request, g, jsonify, Flask
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from .models import User
import json
import datetime


# index view function supressed for brevity

@app.route('/')
@app.route('/index')
def index():
	'''index route (main page)'''
	user = {'nickname': 'Jesse'} # fake user
	posts = [ # fake array of posts
		{
			'author': {'nickname': 'John'},
			'body': 'Beautiful day in portland'
		},
		{
			'author': {'nickname': 'Susan'},
			'body': 'The Avengers movie was so cool!'
		}
	]
	return render_template('index.html',
							title='Home',
							user=user, 
							posts=posts)
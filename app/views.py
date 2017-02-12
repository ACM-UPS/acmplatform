from flask import render_template, flash, redirect, session, url_for, request, g, jsonify, Flask, Markup
from app import app, db
from .models import User

# index view function supressed for brevity


@app.route('/')
@app.route('/index.html') # TODO: REMOVE LATER FROM HTML
def index():
	'''index route (main page)'''
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html') # TODO replace w/ 'about.html'

@app.route('/team')
def team():
	return render_template('team.html') # TODO replace w/ 'team.html'

@app.route('/<var>')
def pageNotFound(var):
	'''POSSIBLE: 404 page ROUTE'''
	return render_template('404.html');

# ALL BELOW NEED REVAMP

@app.route('/blog-leftsidebar') 
def blog_leftsidebar():
	return render_template('blog-leftsidebar.html')

@app.route('/blog-rightsidebar') 
def blog_rightsidebar():
	return render_template('blog-rightsidebar.html')

@app.route('/post-leftsidebar') # TODO Remove ".html"
def left_sidebar():
	return render_template('post-leftsidebar.html')

@app.route('/post-rightsidebar') # TODO Remove ".html"
def right_sidebar():
	return render_template('post-rightsidebar.html')

# below more revamp

@app.route('/comingsoon') 
def comingsoon():
	return render_template('comingsoong.html')

@app.route('/components.html') 
def components():
	return render_template('components.html')

@app.route('/contact.html') # TODO Remove ".html"
def contact():
	return render_template('contact.html')

@app.route('/fullwidth.html') # TODO Remove ".html"
def fullwidth():
	return render_template('fullwidth.html')



@app.route('/login.html') # TODO Remove ".html"
def login():
	return render_template('login.html')

@app.route('/portfolio.html') # TODO Remove ".html"
def portfolio():
	return render_template('portfolio.html')

@app.route('/post-leftsidebar.html') # TODO Remove ".html"
def post_leftsidebar():
	return render_template('post-leftsidebar.html')

@app.route('/post-rightsidebar.html') # TODO Remove ".html"
def post_rightsidebar():
	return render_template('post-rightsidebar.html')

@app.route('/pricing-box.html') # TODO Remove ".html"
def pricing_box():
	return render_template('pricing-box.html')

@app.route('/register.html') # TODO Remove ".html"
def register():
	return render_template('register.html')

@app.route('/search-result.html') # TODO Remove ".html"
def search_result():
	return render_template('search-result.html')

@app.route('/typography.html')  # TODO Remove ".html"
def typography():
	return render_template('typography.html')

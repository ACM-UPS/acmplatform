from flask import render_template, flash, redirect, session, url_for, request, g, jsonify, Flask, Markup
from app import app, db
from .models import User

# index view function supressed for brevity

@app.route('/')
def index():
	'''index route (main page)'''
	return render_template('index.html')

@app.route('/<var>')
def 404(var):
	'''POSSIBLE: 404 page ROUTE'''
	return '''<h1>404 Page</h1>'''

from flask import render_template, flash, redirect, session, url_for, request, g, jsonify, Flask, Markup
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from .models import User
import json
import datetime


# index view function supressed for brevity

@app.route('/')
def index():
	'''index route (main page)'''
	return render_template('index.html')

from flask import render_template, flash, redirect, session, url_for, request, g, jsonify, Flask, Markup
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from .models import User
import json
import datetime


# index view function supressed for brevity

@app.route('/')
def index():
	calendar = Markup("<iframe src=\"https://calendar.google.com/calendar/embed?height=600&amp;wkst=1&amp;bgcolor=%2366cccc&amp;src=acm%40pugetsound.edu&amp;color=%231B887A&amp;ctz=America%2FLos_Angeles\" style=\"border-width:0\" width=\"800\" height=\"600\" frameborder=\"0\" scrolling=\"no\"></iframe>")
	'''index route (main page)'''
	return render_template('index.html', calendar=calendar)
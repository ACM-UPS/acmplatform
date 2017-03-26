from flask import render_template, flash, redirect, session, url_for, request, g, jsonify, Flask, Markup
from app import app, db
from .models import User
from forms import ContactForm
from flask.ext.mail import Message, Mail

# index view function supressed for brevity

mail = Mail()

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'upsacm.contact@gmail.com'
app.config["MAIL_PASSWORD"] = '$upsacm2017'

mail.init_app(app)

app.url_map.strict_slashes = False

@app.before_request
def clear_trailing():
	from flask import redirect, request

	rp = request.path
	if rp != '/' and rp.endswith('/'):
		return redirect(rp[:-1])

@app.route('/')
@app.route('/index')
def index():
	'''index route (main page)'''
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/team')
def team():
	return render_template('team.html')

# New 404 page using errorhandler
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404



# ALL BELOW NEED REVAMP

@app.route('/blog-leftsidebar')
def blog_leftsidebar():
	return render_template('blog-leftsidebar.html')

@app.route('/blog-rightsidebar')
def blog_rightsidebar():
	return render_template('blog-rightsidebar.html')

@app.route('/post-leftsidebar')
def left_sidebar():
	return render_template('post-leftsidebar.html')

@app.route('/post-rightsidebar')
def right_sidebar():
	return render_template('post-rightsidebar.html')

# below more revamp

@app.route('/comingsoon')
def comingsoon():
	return render_template('comingsoon.html')

@app.route('/components')
def components():
	return render_template('components.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash('All field are required.')
			return render_template('contact.html', form=form)
		else:
			msg = Message(form.subject.data, sender='upsacm.contact@gmail.com', recipients=['acm@pugetsound.edu'])
			msg.body = """
			From : %s <%s>
			%s
			""" % (form.name.data, form.email.data, form.message.data)
			mail.send(msg)
			return render_template('contact.html', success=True)
	elif request.method == 'GET':
		return render_template('contact.html', form=form)

@app.route('/fullwidth')
def fullwidth():
	return render_template('fullwidth.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/portfolio')
def portfolio():
	return render_template('portfolio.html')

@app.route('/post-leftsidebar')
def post_leftsidebar():
	return render_template('post-leftsidebar.html')

@app.route('/post-rightsidebar')
def post_rightsidebar():
	return render_template('post-rightsidebar.html')

@app.route('/pricing-box')
def pricing_box():
	return render_template('pricing-box.html')

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/search-result')
def search_result():
	return render_template('search-result.html')

@app.route('/typography')
def typography():
	return render_template('typography.html')

from flask import render_template, Blueprint
from app.blog.models import BlogPost

mod = Blueprint('blog', __name__, template_folder='templates', static_folder='static')

@mod.route('/')
def root():
 	return render_template('blog.html')

# @app.route('/blog/new/', methods = ['GET', 'POST'])
# def new():
#     if request.method == 'POST':
#        if not request.form['title'] or not request.form['content']:
#           flash('Please entesr all the fields', 'error')
#        else:
#           post = models.BlogPost(id=777, title=request.form['title'], content=request.form['content'])
#           db.session.add(post)
#           db.session.commit()
#           flash('Record was successfully added')
#           return redirect(url_for('blog'))
#     return render_template('blog/new.html')

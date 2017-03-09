import os

# config settings
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'acm.db')
SECRET_KEY = 'jesseisdank43' # generate different sessions
WTF_CSRF_ENABLED = True

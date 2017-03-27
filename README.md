[ACM site](http://acm.pugetsound.edu)

## Hello this is the acm website's platform for development.

## Frameworks in place
##### Python
##### Flask
##### Jinja2
##### more... (look in requirements.pip)

## SETUP START
##### 1. Fork ACM-UPS Repository
##### 2. Go to forked repository and clone via SSH or HTTPS (We will be using SSH).

##### Prereqs: https://help.github.com/articles/generating-an-ssh-key/
##### 3. Clone: `git clone git@github.com:username/acmplatform.git`
##### 4. cd acmplatform

##### Prereqs: Python 2.7+ && pip
##### 5. Install virtual environemnt: `pip install virtualenv`
##### 6. Check current packages: `pip freeze` - virtualenv=15.0.3

##### Prereqs: virtualenv
##### 7. Create virtual environment: `virtualenv acm`
##### 8. Activate virtual environment: `source ./acm/scripts/activate`
##### Note: If that doesn't work, use: `source ./acm/bin/activate`

##### Prereqs: (acm) should appear.
##### 9. Check current packages: `pip freeze` - virtualenv != exist
##### 10. Install requirements: `pip install -U -r requirements.pip`
##### 11. Check current packages: `pip freeze` - packages=several
##### 12. Make a tmp folder: `mkdir tmp`
## SETUP END

## FETCHING LATEST CHANGES
##### Prereqs: ACM-UPS repository remote
##### 1. Add remote: `git remote add upstream git@github.com:ACM-UPS/acmplatform.git`
##### 2. Fetch remote: `git fetch upstream`

## RUNNING SERVER & SHUTING DOWN SERVER
##### Prereqs: a browser, terminal, typing skills.
##### 1. Make sure your in the root folder `../acmplatform/`
##### 2. Run the Server: `python run.py`
##### 3. Open Browser and go to: `http://localhost:5000/`
##### 4. Browse until satisfied.

##### Prereqs: terminal with server running
##### 5. Shut Server Down: `Ctrl + C`

## NOTES
##### app folder: (app) is where our website logic lives
##### root folder (acmplatform) is where we run, update/backup the database and holds different types of platforms.
##### static folder (static) is where our css, images, anything static, live at.
##### templates folder: (templates) is where our html pages live at.
##### tmp folder: (tmp) is where the cache lives (?doublecheck needed?)

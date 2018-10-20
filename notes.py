# helloTest.py

from flask import Flask #import Flask class
app = Flask(__name__) #create instance of it
# name argument indicates the app's module or package so that flask 
# knows where to find other files such as templates

@app.route('/') #tells Flask which path to display result of function
def hello_world():
    return 'HackHarvard is ours'

# We need to set up proper directory structure for our web app
# /app is the directory for all code 
# /app/templates for our HTML
# /app/static for CSS and JS and images

# Basic file structure:
# 1. run.py: application entry point, this file starts the Flask server
# and launches our application

# 2. config.py: contains config variables for the app, e.g. db details 

# 3. app/__init__.py: intializes a Python module, so that Python can 
# recognize the app directory as a module 

# 4. app/views.py: contains all routes for our application, tells Flask 
# what to display on which path 

# 5. app/models.py: where we define models (representation of a db table
# in code)



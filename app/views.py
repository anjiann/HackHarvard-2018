# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/moodeum')
def moodeum():
    return render_template("moodeum.html")

#Flask's provided method render_template, which we use to specify
#the HTML file to load for each particular view

#Jinja2 is a template language that we installed for our dependencies
#provides syntax for added functionality to HTML files, like if-else,
#for loops and variables inside templates. Also has template inheritance
#so we can define a base template and have other templates inherit
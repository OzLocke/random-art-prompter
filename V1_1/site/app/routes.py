from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    options = ['object', 'scene', 'concept']
    return render_template('index.html', title='Home', options=options)

@app.route('/prompt')
def prompt():
    return render_template('prompt.html', title='Prompt')
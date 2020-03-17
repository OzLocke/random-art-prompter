from flask import render_template
from app import app
from app.forms import PromptForm

@app.route('/')
@app.route('/index')
def index():
    form = PromptForm()
    return render_template('index.html', title='Home', form=form)

@app.route('/prompt')
def prompt():
    return render_template('prompt.html', title='Prompt')
from flask import render_template, flash, redirect
from app import app
from app.forms import PromptForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PromptForm()
    return render_template('index.html', title='Home', form=form)

@app.route('/prompt', methods=['GET', 'POST'])
def prompt():
    return render_template('prompt.html', title='Prompt')
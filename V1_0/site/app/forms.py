from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, validators

class PromptForm(FlaskForm):
    choices = [('object', 'object'), ('scene', 'scene'), ('concept', 'concept')]
    radio = RadioField('test', [validators.Required()], choices=choices, default='object')
    submit = SubmitField('Prompt me!')
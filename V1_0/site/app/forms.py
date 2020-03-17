from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

class PromptForm(FlaskForm):
    choices = [('object', 'object'), ('scene', 'scene'), ('concept', 'concept')]
    radio = RadioField(choices[0][0], choices=choices)
    submit = SubmitField('Prompt me!')
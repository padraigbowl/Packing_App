from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BagForm(FlaskForm):
    name = StringField('Bag Name', validators=[DataRequired()])
    submit = SubmitField('Create Bag')

class ItemForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired()])
    submit = SubmitField('Add Item')

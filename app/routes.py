from crypt import methods
from app import myobj
from flask import render_template, flash
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField


name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

class LoginForm(FlaskForm):
    city = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@myobj.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit:
        flash(form.city.data)
        #print(f'{form.city.data}')
    return render_template('home.html', name = name, city_names = city_names, form = form)
    #home.html and name


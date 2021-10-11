from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import DataRequired
from wtforms import ValidationError

class CourseForm(FlaskForm):

    submit1 = SubmitField('Continue ->')
    submit2 = SubmitField('Continue ->')
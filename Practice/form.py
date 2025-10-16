from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(message="We need your name, it cannot be empty")])
    email = StringField("Email", validators=[DataRequired(message="Email is required"), Email("This doesn't look like a email")])
    password = PasswordField("Password", validators=[DataRequired("Password is required"), Length(min=6, message="Password should be at least 6 characters long")])
    submit = SubmitField("Register")
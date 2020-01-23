from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField,DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError,Required
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name',validators=[DataRequired(),Length(min=2,max=15)])
    lastname = StringField('Last Name',validators=[DataRequired(),Length(min=2,max=15)])	
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    DOB=DateTimeField('Your Birthday (dd/mm/yy)',format='%d/%m/%y')
    batch=StringField('Batch',validators=[DataRequired(),Length(min=10,max=10)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def vlaidate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("that username already exist.Choose another")
    def vlaidate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("that username is taken.")
     
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ProfileForm(FlaskForm):
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('update picture')


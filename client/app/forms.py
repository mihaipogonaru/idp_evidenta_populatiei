import datetime as dt

from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms.fields.html5 import DateField

from .messages import LoginValidationMessages
from .extensions import db
from .models import User

class LoginForm(FlaskForm):
    username = StringField('Username (your e-mail)',
                           validators=[DataRequired(LoginValidationMessages.data_required),
                                       Email(LoginValidationMessages.email_format)])
    password = PasswordField('Password')
    remember = BooleanField('Keep me signed in')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        self.user = db.call_no_throw(db.select_user, email=self.username.data)

        if not self.user or self.user == db.err:
            self.password.errors.append('Invalid username or password')
            return False

        self.user = User(self.user)

        if not self.user.check_password(self.password.data):
            self.password.errors.append('Invalid username or password')
            return False

        return True

class BirthForm(FlaskForm):
    pin = IntegerField('Personal identity number',
                       validators=[DataRequired()])
    surname = StringField('Surname',
                          validators=[DataRequired()])
    name = StringField('Name',
                       validators=[DataRequired()])
    city = StringField('City',
                       validators=[DataRequired()])
    dt = DateField('', format='%Y-%m-%d',
                       validators=[DataRequired()])


    def __init__(self, *args, **kwargs):
        super(BirthForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(BirthForm, self).validate()
        if not initial_validation:
            return False

        if db.call_no_throw(db.insert_birth, pin=self.pin.data,
                surname=self.surname.data, name=self.name.data,
                city=self.city.data, date=self.dt.data) == db.err:
            
            self.pin.errors.append('Invalid pin or city')
            self.city.errors.append('Invalid pin or city')
            return False

        return True

class DeathForm(FlaskForm):
    pin1 = IntegerField('Personal identity number',
                       validators=[DataRequired()])
    city1 = StringField('City',
                       validators=[DataRequired()])
    dt1 = DateField('', format='%Y-%m-%d',
                       validators=[DataRequired()])


    def __init__(self, *args, **kwargs):
        super(DeathForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(DeathForm, self).validate()
        if not initial_validation:
            return False

        if db.call_no_throw(db.insert_death, person=self.pin1.data,
                city=self.city1.data, date=self.dt1.data) == db.err:
            
            self.pin.errors.append('Invalid pin or city')
            self.city.errors.append('Invalid pin or city')
            return False

        return True

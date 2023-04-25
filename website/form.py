from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField,IntegerField, SubmitField, DateField, TimeField, TextAreaField, StringField, SelectField
from wtforms.validators import DataRequired, Length, InputRequired, NumberRange, Email
import email_validator
from wtforms.fields import EmailField

class DonorForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password1", validators=[DataRequired()])	
    blood_group = StringField("Blood_Group", validators=[DataRequired()])
    age = IntegerField("Age", validators=[ InputRequired(), NumberRange(18, 74)])
    submit = SubmitField("submit")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("submit")

class RequestForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    contact_no = StringField("Recipient Contact Number(with country code)", validators=[DataRequired()])
    blood_group = StringField("Which Blood Group Do You Need?", validators=[DataRequired()])
    date_details = StringField("Date of the Blood Drive", validators=[DataRequired()])
    address = StringField("Address where the drive will be held", validators=[DataRequired()])
    details = StringField("Details of the blood drive", validators=[DataRequired()])
    submit = SubmitField("submit")


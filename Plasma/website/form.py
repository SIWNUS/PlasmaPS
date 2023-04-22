from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField,IntegerField, SubmitField, DateField, TimeField, TextAreaField, StringField, RadioField
from wtforms.validators import DataRequired, Length

class DonorForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password1", validators=[DataRequired()])	
    blood_group = StringField("Blood_Group", validators=[DataRequired()])
    age = IntegerField("Age")
    submit = SubmitField("submit")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("submit")

class RequestForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    reg_no = IntegerField("Doctor's Register Number")
    blood_group = StringField("Which Blood Group Do You Need?", validators=[DataRequired()])
    date_details = StringField("Date of the Blood Drive", validators=[DataRequired()])
    address = TextAreaField("Address where the drive will be held", validators=[DataRequired()])
    details = TextAreaField("Details of the blood drive", validators=[DataRequired()])
    submit = SubmitField("submit")


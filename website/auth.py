from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .form  import DonorForm, LoginForm
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__)

@auth.route('/donor-login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist!', category='error')
    form.email.data = ''
    form.password.data = ''

    if form.is_submitted():
        return redirect('/dashboard')
    return render_template("login.html", form=form, user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/donor-register', methods=['GET', 'POST'])
def donor_register():
    form1 = DonorForm()
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        blood_group = request.form.get('blood_group')
        age = request.form.get('age')

        user = User.query.filter_by(email=form1.email.data).first()
        if user:
            flash('Email already exists', category='error')
        else:
            new_user = User(name=form1.name.data, email=form1.email.data, password=generate_password_hash(form1.password.data, method='sha256'),blood_group=form1.blood_group.data, age=form1.age.data)
            db.session.add(new_user)
            db.session.commit()
            flash('user added successfully')
            return redirect(url_for('auth.login'))
    return render_template("Register.html", form1=form1, user=current_user)

@auth.route('/admin')
@login_required
def Admin(id):
    id = current_user.id()
    if id == 1:
        return redirect(url_for('views.dashboard'))

@auth.route('/admin-delete/<int:id>')
@login_required
def admin_delete(id):
    user_to_delete = User.query.get_or_404(id)
    id = current_user.id
    if id == 1:
        try:
            db.session.delete(user_to_delete)
            db.session.commit()
            flash('User Successfully Deleted!!', category='success')
            return redirect(url_for('views.dashboard'))
        except:
            flash('Whoops! There was a problem deleting the user!', category='error')
            return redirect(url_for('views.dashboard'))

    else:
        flash('You are not authorised!!', category='error')
        return redirect(url_for('views.dashboard'))
@auth.route('/user-update/<int:id>', methods=['GET', 'POST'])
@login_required
def user_update(id):
    form = DonorForm()
    user_to_update = User.query.get_or_404(id)
    if request.method == "POST":
        user_to_update.email = request.form.get('email')
        user_to_update.name = request.form.get('name')
        user_to_update.password = request.form.get('password')
        user_to_update.blood_group = request.form.get('blood_group')
        user_to_update.age = request.form.get('age')
        try:
            db.session.commit()
            flash("User Updated Successfully!", category = 'success')
            return redirect('/dashboard')
        except:
            flash("Error! There was a problem updating your profile!", category = 'error') 
            return redirect('/dashboard')
    else:
        return render_template("update.html", form=form, user_to_update=user_to_update, user=current_user)

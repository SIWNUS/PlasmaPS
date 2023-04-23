from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user
from .form import RequestForm
from . import db
from .models import Plasma, User
 
views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/Donor')
def Donor():
    return render_template("Donor.html", user=current_user)

@views.route('/info-plasma')
def info_plasma():
    return render_template("plasma.html", user=current_user)

@views.route('/recipient')
def recipient():
    return render_template("recipient.html", user=current_user)


@views.route('/board', methods=['GET'])
@login_required
def Board():
    plasma = Plasma.query.all()
    return render_template("board.html", plasma=plasma, user=current_user)

@views.route('/request', methods=['GET', 'POST'])
@login_required
def Request():
    form = RequestForm()
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        reg_no = request.form.get('reg_no')
        blood_group = request.form.get('blood_group')
        date_details = request.form.get('date_details')
        address = request.form.get('address')
        details = request.form.get('details')
        entry = Plasma.query.order_by(Plasma.id)
        new_entry = Plasma(name=form.name.data, email=form.email.data, reg_no=form.reg_no.data, blood_group=form.blood_group.data, date_details=form.date_details.data, address=form.address.data, details=form.details.data)
        db.session.add(new_entry)
        db.session.commit()
        flash('Request Posted', category='success')
        return redirect(url_for('views.Board'))
    return render_template("apply.html", form=form, user=current_user)

@views.route('/delete/<int:id>')
@login_required
def delete(id):
    entry_to_delete = Plasma.query.get_or_404(id)
    id =  current_user.email
    if id == entry_to_delete.email:
        try:
            db.session.delete(entry_to_delete)
            db.session.commit()
            flash('Request Successfully Deleted!!', category='success')
            return redirect(url_for('views.Board'))
        except:
            flash('Whoops! There was a problem deleting the request!', category='error')
            return redirect(url_for('views.Board'))
    else:
        flash('You are not authorised!!', category='error')
        return redirect(url_for('views.Board'))

@views.route('/request-update/<int:id>', methods=['GET', 'POST'])
@login_required
def request_update(id):
    form = RequestForm()
    request_to_update = Plasma.query.get_or_404(id)
    if request.method == "POST":
        request_to_update.email = request.form.get('email')
        request_to_update.name = request.form.get('name')
        request_to_update.reg_no = request.form.get('reg_no')
        request_to_update.blood_group = request.form.get('blood_group')
        request_to_update.date_details = request.form.get('date_details')
        request_to_update.address = request.form.get('address')
        request_to_update.details = request.form.get('details')
        try:
            db.session.commit()
            flash("Request Updated Successfully!", category = 'success')
            return redirect('/board')
        except:
            flash("Error! There was a problem updating your profile!", category = 'error') 
            return redirect('/board')
    else:
        return render_template("update1.html", form=form, request_to_update=request_to_update, user=current_user)


@views.route('/dashboard')
@login_required
def dashboard():
    users = User.query.all()
    return render_template("dashboard.html", users=users, user=current_user)

@views.route('/terms')
def terms():
    return render_template("terms.html", user=current_user)

@views.route('/privacy')
def privacy():
    return render_template("privacy.html", user=current_user)

@views.route('/faq')
def faq():
    return render_template("faq.html", user=current_user)

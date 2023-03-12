from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views',__name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/Donor')
@login_required
def Donor():
    return render_template("Donor.html", user=current_user)


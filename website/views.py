from flask import Blueprint, render_template
from flask_login import login_user, login_required, current_user

views = Blueprint('views', __name__)


@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/about')
@login_required
def about():
    return render_template("about.html", user=current_user)


@views.route('/change_password')
@login_required
def change_password():
    return render_template("change_password.html", user=current_user)
from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/home')
def home():
    return render_template("home.html")


@views.route('/about')
def about():
    return render_template("about.html")


@views.route('/change_password')
def change_password():
    return render_template("change_password.html")
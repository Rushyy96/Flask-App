from flask import Blueprint, redirect, render_template

auth = Blueprint('auth', __name__)


@auth.route('/')
def root():
    return render_template("layout.html")


@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/register')
def sign_up():
    return render_template("register.html")


@auth.route('/logout')
def logout():
    return redirect("/")
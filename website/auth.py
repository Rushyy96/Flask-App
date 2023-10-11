from flask import Blueprint, redirect, render_template, request, flash, url_for, views
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/')
def root():
    return redirect('/login')


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged In Successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password!', category='error')
        else:
            flash('An account with this email does not exist', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/register', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password')
        password2 = request.form.get('confirm-password')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('A user with this email already exists.', category='error')
            return redirect(url_for("auth.sign_up"))
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('Please input your name', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 8 characters', category='error')
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password2, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account created", category='success')
            return redirect(url_for("views.home"))
     
    return render_template("register.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged Out', category='error')
    return redirect(url_for('auth.login'))
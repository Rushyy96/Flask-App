from flask import Blueprint, redirect, render_template, request, session, flash

auth = Blueprint('auth', __name__)


@auth.route('/')
def root():
    return render_template("layout.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    data = request.form
    return render_template("login.html")


@auth.route('/register', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password')
        password2 = request.form.get('confirm-password')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 8 characters', category='error')
        else:
            #add user to db
            flash("Account created", category='success')
            
    return render_template("register.html")


@auth.route('/logout')
def logout():
    return redirect("/")
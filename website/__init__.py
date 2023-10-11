from flask import Flask, redirect, session
from flask_session import Session
from functools import wraps

#sess = Session()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qawdtacv qesdffgasd'
    #sess.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
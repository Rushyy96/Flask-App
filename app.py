from website import create_app
from flask import Flask, session


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
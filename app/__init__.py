from .calc import soma
from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.get("/soma/<int:x>/<int: y>")
    def home(x, y):
        return f"blah {x} e {y}"

    return app

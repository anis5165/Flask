from flask import Flask
from routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = "my_secret"

    app.register_blueprint(auth_bp)

    return app